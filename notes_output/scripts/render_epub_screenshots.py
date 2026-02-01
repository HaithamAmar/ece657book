#!/usr/bin/env python3
"""
Headless, offline visual QA for EPUBs (screenshots).

This does NOT replace testing in Kindle Previewer or Apple Books. It is meant to
catch obvious regressions early (broken CSS, tiny figures, clipped equations,
TOC/layout surprises) and to create a shareable screenshot bundle.

Requires Playwright:
  python3 -m venv notes_output/.venv_render
  notes_output/.venv_render/bin/pip install playwright
  notes_output/.venv_render/bin/python -m playwright install chromium webkit
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import xml.etree.ElementTree as ET


@dataclass(frozen=True)
class Viewport:
    width: int
    height: int


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _extract_epub(epub: Path, out_dir: Path) -> None:
    with zipfile.ZipFile(epub) as z:
        z.extractall(out_dir)


def _parse_container_rootfile(root: Path) -> Path:
    container = root / "META-INF" / "container.xml"
    if not container.exists():
        raise FileNotFoundError("Missing META-INF/container.xml in extracted EPUB.")

    xml = ET.fromstring(_read_text(container))
    # EPUB container.xml uses a default namespace; ignore by using wildcard.
    rootfile = xml.find(".//{*}rootfile")
    if rootfile is None:
        raise ValueError("Invalid container.xml: missing <rootfile> element.")
    full_path = rootfile.attrib.get("full-path")
    if not full_path:
        raise ValueError("Invalid container.xml: missing rootfile full-path.")
    return root / full_path


def _parse_spine_xhtml(opf_path: Path) -> list[Path]:
    """
    Returns spine XHTML paths in reading order, plus best-effort cover.xhtml first
    (if present).
    """
    opf_dir = opf_path.parent
    xml = ET.fromstring(_read_text(opf_path))

    manifest_items: dict[str, dict[str, str]] = {}
    for item in xml.findall(".//{*}manifest/{*}item"):
        item_id = item.attrib.get("id", "")
        if not item_id:
            continue
        manifest_items[item_id] = dict(item.attrib)

    spine_ids: list[str] = [
        it.attrib.get("idref", "") for it in xml.findall(".//{*}spine/{*}itemref")
    ]
    spine_ids = [s for s in spine_ids if s]

    xhtml: list[Path] = []
    for item_id in spine_ids:
        href = manifest_items.get(item_id, {}).get("href")
        if not href:
            continue
        if not href.lower().endswith((".xhtml", ".html")):
            continue
        p = (opf_dir / href).resolve()
        if p.exists():
            xhtml.append(p)

    # Prefer an explicit cover.xhtml if present; it is often not in spine.
    cover = (opf_dir / "cover.xhtml").resolve()
    if cover.exists():
        xhtml = [cover] + [p for p in xhtml if p != cover]

    return xhtml


def _pick_default_engines(epub: Path, requested: list[str] | None) -> list[str]:
    if requested:
        return requested
    name = epub.name.lower()
    if "apple" in name:
        return ["webkit"]
    if "kindle" in name:
        return ["chromium"]
    return ["webkit", "chromium"]


def _wait_for_images_best_effort(page: Any, timeout_ms: int = 10_000) -> None:
    try:
        page.wait_for_function(
            "Array.from(document.images).every(img => img.complete)",
            timeout=timeout_ms,
        )
    except Exception:
        # Non-fatal; screenshots still help even if one image is missing.
        pass


def _safe_slug(name: str) -> str:
    name = re.sub(r"[^\w.\-]+", "_", name, flags=re.ASCII).strip("_")
    return name or "page"


def _render_epub(
    epub: Path,
    out_dir: Path,
    engines: list[str],
    viewports: list[Viewport],
    max_pages: int | None,
    only_xhtml: list[str] | None,
    elements_per_page: int,
    wait_after_scroll_ms: int,
    wait_for_img_timeout_ms: int,
) -> dict[str, Any]:
    from playwright.sync_api import sync_playwright

    report: dict[str, Any] = {
        "epub": str(epub),
        "out_dir": str(out_dir),
        "engines": engines,
        "viewports": [vp.__dict__ for vp in viewports],
        "pages": [],
    }

    with tempfile.TemporaryDirectory(prefix="ece657_visualqa_") as tmp:
        root = Path(tmp)
        _extract_epub(epub, root)
        opf = _parse_container_rootfile(root)
        xhtml = _parse_spine_xhtml(opf)
        if only_xhtml:
            wanted = {Path(x).name for x in only_xhtml}
            xhtml = [p for p in xhtml if p.name in wanted]
            if not xhtml:
                available = ", ".join(p.name for p in _parse_spine_xhtml(opf))
                raise ValueError(
                    "No spine XHTML matched --only-xhtml. "
                    f"Wanted={sorted(wanted)}. Available={available}"
                )
        if max_pages is not None:
            xhtml = xhtml[:max_pages]

        with sync_playwright() as p:
            for engine in engines:
                browser_type = getattr(p, engine, None)
                if browser_type is None:
                    raise ValueError(f"Unsupported engine: {engine}")

                browser = browser_type.launch(headless=True)
                try:
                    for vp in viewports:
                        viewport_dir = out_dir / engine / f"{vp.width}x{vp.height}"
                        elements_dir = viewport_dir / "elements"
                        viewport_dir.mkdir(parents=True, exist_ok=True)
                        elements_dir.mkdir(parents=True, exist_ok=True)

                        page = browser.new_page(viewport={"width": vp.width, "height": vp.height})
                        failures: list[str] = []

                        def _on_request_failed(req: Any) -> None:
                            url = req.url
                            failure = req.failure
                            failures.append(f"{url} :: {failure}")

                        page.on("requestfailed", _on_request_failed)

                        for idx, path in enumerate(xhtml, start=1):
                            url = path.as_uri()
                            slug = _safe_slug(path.name)
                            shot_name = f"{idx:02d}_{slug}.png"
                            page_info: dict[str, Any] = {
                                "engine": engine,
                                "viewport": vp.__dict__,
                                "xhtml": str(path),
                                "png": str((viewport_dir / shot_name).resolve()),
                            }

                            try:
                                page.goto(url, wait_until="load", timeout=60_000)
                                _wait_for_images_best_effort(page)
                                page.wait_for_timeout(200)

                                page.screenshot(path=str(viewport_dir / shot_name), full_page=False)

                                # Element shots (best-effort). These give quick signal on
                                # equation/figure/code layout without saving huge full-page images.
                                element_shots: list[dict[str, str]] = []

                                def snap(selector: str, kind: str) -> None:
                                    handles = page.query_selector_all(selector)
                                    for j, h in enumerate(handles[:elements_per_page], start=1):
                                        try:
                                            h.scroll_into_view_if_needed(timeout=3_000)
                                            if kind != "code":
                                                try:
                                                    page.wait_for_function(
                                                        """
                                                        (el) => {
                                                          if (!el) return false;
                                                          if (el.tagName && el.tagName.toLowerCase() === 'img') {
                                                            return el.complete && el.naturalWidth > 0;
                                                          }
                                                          const imgs = Array.from(el.querySelectorAll('img'));
                                                          return imgs.length === 0
                                                            ? true
                                                            : imgs.every(img => img.complete && img.naturalWidth > 0);
                                                        }
                                                        """,
                                                        h,
                                                        timeout=wait_for_img_timeout_ms,
                                                    )
                                                except Exception:
                                                    pass
                                            # WebKit sometimes needs a paint tick after scrolling.
                                            if wait_after_scroll_ms > 0:
                                                page.wait_for_timeout(wait_after_scroll_ms)
                                            out = elements_dir / f"{idx:02d}_{slug}__{kind}_{j:02d}.png"
                                            h.screenshot(path=str(out))
                                            element_shots.append({"kind": kind, "selector": selector, "png": str(out)})
                                        except Exception:
                                            continue

                                snap("div.equation, div.eqnarray, table.equation", "equation")
                                snap("img.math-display", "math_display")
                                snap("div.tcolorbox", "tcolorbox")
                                snap("div.figure", "figure")
                                snap("pre", "code")
                                snap("img[src^='code/']", "code_img")
                                snap("table", "table")

                                if element_shots:
                                    page_info["elements"] = element_shots

                                if failures:
                                    page_info["requestfailed"] = failures[-20:]
                            except Exception as e:
                                page_info["error"] = str(e)
                            finally:
                                report["pages"].append(page_info)

                        page.close()
                finally:
                    browser.close()

    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--epub",
        action="append",
        help="Path to an EPUB file (repeatable). Defaults to the built Apple+Kindle EPUBs.",
    )
    parser.add_argument(
        "--out",
        default="notes_output/artifacts/visual_qa",
        help="Output directory for screenshots and report.json",
    )
    parser.add_argument(
        "--engine",
        action="append",
        choices=["chromium", "webkit"],
        help="Rendering engine(s) to use (repeatable). Default: auto based on EPUB name.",
    )
    parser.add_argument(
        "--viewport",
        action="append",
        help="Viewport as WIDTHxHEIGHT (repeatable). Default: 390x844 and 768x1024.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Limit the number of XHTML pages rendered (spine order).",
    )
    parser.add_argument(
        "--only-xhtml",
        action="append",
        help=(
            "Render only these XHTML files (basename match, repeatable). "
            "Example: --only-xhtml ece657_ebookse5.xhtml"
        ),
    )
    parser.add_argument(
        "--elements-per-page",
        type=int,
        default=3,
        help="Max element screenshots per kind per page.",
    )
    parser.add_argument(
        "--wait-after-scroll-ms",
        type=int,
        default=250,
        help="Extra wait after scrolling an element into view (ms).",
    )
    parser.add_argument(
        "--wait-for-img-timeout-ms",
        type=int,
        default=3000,
        help="Timeout when waiting for images inside a figure (ms).",
    )
    args = parser.parse_args()

    epubs: list[Path]
    if args.epub:
        epubs = [Path(p).expanduser().resolve() for p in args.epub]
    else:
        epubs = [
            Path("notes_output/artifacts/ebook/ece657_ebook_apple.epub").resolve(),
            Path("notes_output/artifacts/ebook/ece657_ebook_kindle.epub").resolve(),
        ]

    missing = [p for p in epubs if not p.exists()]
    if missing:
        for p in missing:
            print(f"ERROR: EPUB not found: {p}", file=sys.stderr)
        return 2

    viewports: list[Viewport]
    if args.viewport:
        viewports = []
        for raw in args.viewport:
            m = re.fullmatch(r"(\d+)x(\d+)", raw.strip())
            if not m:
                print(f"ERROR: invalid viewport: {raw} (expected WIDTHxHEIGHT)", file=sys.stderr)
                return 2
            viewports.append(Viewport(width=int(m.group(1)), height=int(m.group(2))))
    else:
        viewports = [Viewport(390, 844), Viewport(768, 1024)]

    out_root = Path(args.out).expanduser().resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    all_reports: list[dict[str, Any]] = []
    for epub in epubs:
        engines = _pick_default_engines(epub, args.engine)
        out_dir = out_root / epub.stem
        out_dir.mkdir(parents=True, exist_ok=True)
        try:
                report = _render_epub(
                    epub=epub,
                    out_dir=out_dir,
                    engines=engines,
                    viewports=viewports,
                    max_pages=args.max_pages,
                    only_xhtml=args.only_xhtml,
                    elements_per_page=args.elements_per_page,
                    wait_after_scroll_ms=args.wait_after_scroll_ms,
                    wait_for_img_timeout_ms=args.wait_for_img_timeout_ms,
                )
        except ModuleNotFoundError as e:
            if "playwright" in str(e).lower():
                print(
                    "ERROR: Playwright not installed. See script docstring for install steps.",
                    file=sys.stderr,
                )
                return 2
            raise

        (out_dir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        all_reports.append(report)

        total = len([p for p in report["pages"] if "png" in p])
        errors = len([p for p in report["pages"] if p.get("error")])
        print(f"{epub.name}: wrote {total} page screenshots under {out_dir} (errors: {errors})")

    (out_root / "reports.json").write_text(json.dumps(all_reports, indent=2), encoding="utf-8")
    print(f"Wrote combined report: {out_root / 'reports.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
