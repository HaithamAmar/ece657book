#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path


def _ensure_playwright() -> None:
    try:
        import playwright.sync_api  # noqa: F401
    except ModuleNotFoundError as e:
        raise SystemExit(
            "Missing dependency: playwright. Install it with:\n"
            "  python3 -m venv epub_builder/.venv\n"
            "  epub_builder/.venv/bin/pip install playwright pillow\n"
            "  epub_builder/.venv/bin/python -m playwright install chromium\n"
        ) from e


def _run(cmd: list[str], *, cwd: Path | None = None) -> None:
    proc = subprocess.run(cmd, cwd=cwd, check=False, text=True)
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)


def _normalize_aux_page(s: str) -> int | None:
    # Handles plain "45" and also variants like "[1][45][]45".
    m = re.findall(r"\d+", s)
    if not m:
        return None
    try:
        return int(m[-1])
    except ValueError:
        return None


@dataclass(frozen=True)
class LabelInfo:
    label: str
    kind: str  # fig/tab/eq
    number: str
    page: int | None


def load_aux_labels(aux_path: Path) -> list[LabelInfo]:
    if not aux_path.exists():
        raise SystemExit(f"Missing aux file: {aux_path}")

    # \newlabel{fig:roadmap}{{1}{45}{...}{...}{}}
    # \newlabel{eq:foo}{{4.1}{43}{...}{}{}}
    newlabel = re.compile(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{([^}]*)\}")
    out: list[LabelInfo] = []
    for line in aux_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = newlabel.search(line)
        if not m:
            continue
        lab = m.group(1).strip()
        if lab.endswith("@cref"):
            continue
        if not (lab.startswith("fig:") or lab.startswith("tab:") or lab.startswith("eq:")):
            continue
        kind = lab.split(":", 1)[0]
        num = m.group(2).strip()
        page = _normalize_aux_page(m.group(3).strip())
        # Normalize noisy forms like "[equation][2][1]1.2" -> "1.2"
        m2 = re.search(r"\]([A-Za-z0-9.]+)\s*$", num)
        if m2:
            num = m2.group(1).strip()
        out.append(LabelInfo(label=lab, kind=kind, number=num, page=page))
    return out


def _ensure_pdf_tools() -> None:
    for t in ("pdftoppm",):
        if shutil.which(t) is None:
            raise SystemExit(f"Missing required tool on PATH: {t}")


def render_pdf_page(pdf_path: Path, *, page: int, out_png: Path, dpi: int) -> None:
    out_png.parent.mkdir(parents=True, exist_ok=True)
    if out_png.exists() and out_png.stat().st_size > 0:
        return
    prefix = out_png.with_suffix("")
    cmd = ["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi), "-png", str(pdf_path), str(prefix)]
    _run(cmd)
    generated = out_png.parent / f"{prefix.name}-{page}.png"
    if not generated.exists():
        # pdftoppm sometimes names as prefix-001.png when -f/-l present.
        fallback = out_png.parent / f"{prefix.name}-{page:03d}.png"
        if fallback.exists():
            generated = fallback
        else:
            raise SystemExit(f"pdftoppm did not produce expected output for page {page}")
    generated.replace(out_png)


def _find_epub_xhtml_for_label(extracted_root: Path, label: str) -> Path | None:
    text_dir = extracted_root / "EPUB" / "text"
    if not text_dir.exists():
        return None
    pat = f'id="{label}"'
    for xhtml in sorted(text_dir.glob("*.xhtml")):
        try:
            s = xhtml.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if pat in s:
            return xhtml
    return None


def _epub_label_locator(page, label: str):  # playwright Page
    # Use XPath to avoid CSS escaping issues with ':' in ids.
    return page.locator(f"xpath=//*[@id='{label}']")

def _stitch_vertical(*, top_png: Path, bottom_png: Path, out_png: Path, gap: int = 12) -> None:
    from PIL import Image

    a = Image.open(top_png).convert("RGB")
    b = Image.open(bottom_png).convert("RGB")
    w = max(a.width, b.width)
    out = Image.new("RGB", (w, a.height + gap + b.height), (255, 255, 255))
    out.paste(a, ((w - a.width) // 2, 0))
    out.paste(b, ((w - b.width) // 2, a.height + gap))
    out_png.parent.mkdir(parents=True, exist_ok=True)
    out.save(out_png)


def screenshot_epub_label(
    *,
    page,
    xhtml_path: Path,
    label: str,
    kind: str,
    out_png: Path,
    context_px: int,
) -> bool:
    out_png.parent.mkdir(parents=True, exist_ok=True)
    url = xhtml_path.resolve().as_uri()
    page.goto(url, wait_until="load")
    page.wait_for_timeout(200)

    loc = _epub_label_locator(page, label)
    if loc.count() == 0:
        return False

    # Equations: ids often land on a zero-size anchor; capture the next display math
    # and the following equation-number line (flushright) when present.
    if kind == "eq":
        # Pandoc typically emits MathML (<math>), but some readers/wrappers can
        # surface math as <span class="math ...">. Use a union XPath.
        math_loc = page.locator(
            f"xpath=(//*[@id='{label}']/following::math | //*[@id='{label}']/following::span[contains(@class,'math')])[1]"
        )
        if math_loc.count() == 0:
            # Fallback: try to scroll to the anchor, then screenshot the viewport.
            try:
                loc.first.scroll_into_view_if_needed()
                page.wait_for_timeout(120)
                page.screenshot(path=str(out_png), full_page=False)
            except Exception:
                page.screenshot(path=str(out_png), full_page=False)
            return True
        math_loc.first.scroll_into_view_if_needed()
        page.wait_for_timeout(180)

        tmp_math = out_png.with_suffix(".math.png")
        try:
            math_loc.first.screenshot(path=str(tmp_math))
        except Exception:
            page.screenshot(path=str(out_png), full_page=False)
            return True

        num_loc = page.locator(f"xpath=//*[@id='{label}']/following::div[contains(@class,'flushright')][1]")
        if num_loc.count() > 0:
            tmp_num = out_png.with_suffix(".num.png")
            try:
                num_loc.first.screenshot(path=str(tmp_num))
                _stitch_vertical(top_png=tmp_math, bottom_png=tmp_num, out_png=out_png, gap=10)
            finally:
                if tmp_num.exists():
                    tmp_num.unlink()
                if tmp_math.exists():
                    tmp_math.unlink()
            return True

        tmp_math.replace(out_png)
        return True

    # Figures/tables: capture the element itself (includes caption in most cases).
    loc.first.scroll_into_view_if_needed()
    page.wait_for_timeout(150)
    try:
        loc.first.screenshot(path=str(out_png))
        return True
    except Exception:
        # Fallback: cropped viewport around the element box.
        box = loc.first.bounding_box()
        if not box:
            page.screenshot(path=str(out_png), full_page=False)
            return True
        x = max(0, int(box["x"]) - context_px)
        y = max(0, int(box["y"]) - context_px)
        w = int(box["width"]) + 2 * context_px
        h = int(box["height"]) + 2 * context_px
        vw = page.viewport_size["width"]
        vh = page.viewport_size["height"]
        w = min(w, vw - x)
        h = min(h, vh - y)
        page.screenshot(path=str(out_png), clip={"x": x, "y": y, "width": w, "height": h})
        return True


def _side_by_side(*, left_png: Path, right_png: Path, out_png: Path) -> None:
    from PIL import Image

    a = Image.open(left_png).convert("RGB")
    b = Image.open(right_png).convert("RGB")

    # Fit right image to left height (keep aspect).
    if b.height != a.height:
        new_w = int(b.width * (a.height / b.height))
        b = b.resize((max(1, new_w), a.height))

    out = Image.new("RGB", (a.width + b.width, a.height), (255, 255, 255))
    out.paste(a, (0, 0))
    out.paste(b, (a.width, 0))
    out_png.parent.mkdir(parents=True, exist_ok=True)
    out.save(out_png)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--epub", default="epub_builder/dist/ece657_ebook_apple.epub")
    ap.add_argument("--pdf", default="notes_output/ece657_notes.pdf")
    ap.add_argument("--aux", default="notes_output/ece657_notes.aux")
    ap.add_argument("--out", default="epub_builder/artifacts/qc/pdf_vs_epub")
    ap.add_argument("--max-eq", type=int, default=120, help="Limit equation captures (0 = all).")
    ap.add_argument("--pdf-dpi", type=int, default=200)
    ap.add_argument("--viewport-w", type=int, default=1200)
    ap.add_argument("--viewport-h", type=int, default=1500)
    ap.add_argument("--context-px", type=int, default=80)
    args = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[2]
    epub_path = (repo_root / args.epub).resolve()
    pdf_path = (repo_root / args.pdf).resolve()
    aux_path = (repo_root / args.aux).resolve()
    out_root = (repo_root / args.out).resolve()

    if not epub_path.exists():
        raise SystemExit(f"Missing EPUB: {epub_path}")
    if not pdf_path.exists():
        raise SystemExit(f"Missing PDF: {pdf_path}")
    if not aux_path.exists():
        raise SystemExit(f"Missing AUX: {aux_path}")

    _ensure_playwright()

    labels = load_aux_labels(aux_path)
    figs = [l for l in labels if l.kind == "fig"]
    tabs = [l for l in labels if l.kind == "tab"]
    eqs = [l for l in labels if l.kind == "eq"]
    if args.max_eq != 0:
        eqs = eqs[: max(0, args.max_eq)]

    selected = figs + tabs + eqs
    # Prefer deterministic ordering: by kind then page then label.
    kind_rank = {"fig": 0, "tab": 1, "eq": 2}
    selected.sort(key=lambda x: (kind_rank.get(x.kind, 9), x.page or 999999, x.label))

    manifest: dict[str, dict] = {
        "epub": str(epub_path),
        "pdf": str(pdf_path),
        "counts": {"fig": len(figs), "tab": len(tabs), "eq": len(eqs)},
        "items": {},
    }

    # Extract EPUB once.
    tmp_root = out_root / "tmp"
    tmp_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="qc_epub_", dir=tmp_root) as tmp:
        tmp_dir = Path(tmp)
        with zipfile.ZipFile(epub_path, "r") as z:
            z.extractall(tmp_dir)

        from playwright.sync_api import sync_playwright

        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page(viewport={"width": args.viewport_w, "height": args.viewport_h})

            pdf_cache_dir = out_root / "pdf_pages"
            epub_cache_dir = out_root / "epub_snips"
            compare_dir = out_root / "compare"

            for info in selected:
                item: dict[str, object] = {"kind": info.kind, "number": info.number, "pdf_page": info.page}
                # PDF page screenshot (full page).
                if info.page is not None:
                    pdf_png = pdf_cache_dir / f"page_{info.page:04d}.png"
                    render_pdf_page(pdf_path, page=info.page, out_png=pdf_png, dpi=args.pdf_dpi)
                    item["pdf_png"] = str(pdf_png.relative_to(repo_root))
                else:
                    pdf_png = None

                xhtml = _find_epub_xhtml_for_label(tmp_dir, info.label)
                if not xhtml:
                    item["epub_missing"] = True
                    manifest["items"][info.label] = item
                    continue
                item["epub_xhtml"] = str(xhtml.relative_to(tmp_dir))

                epub_png = epub_cache_dir / info.kind / f"{info.label.replace(':', '_')}.png"
                ok = screenshot_epub_label(
                    page=page,
                    xhtml_path=xhtml,
                    label=info.label,
                    kind=info.kind,
                    out_png=epub_png,
                    context_px=args.context_px,
                )
                if not ok:
                    item["epub_missing"] = True
                    manifest["items"][info.label] = item
                    continue
                item["epub_png"] = str(epub_png.relative_to(repo_root))

                if pdf_png is not None:
                    out_cmp = compare_dir / info.kind / f"{info.label.replace(':', '_')}.png"
                    _side_by_side(left_png=pdf_png, right_png=epub_png, out_png=out_cmp)
                    item["compare_png"] = str(out_cmp.relative_to(repo_root))

                manifest["items"][info.label] = item

            browser.close()

    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote QC bundle to: {out_root}")
    print(f"- manifest: {out_root / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    import sys
    import shutil

    raise SystemExit(main(sys.argv[1:]))
