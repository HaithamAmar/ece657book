#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
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


@dataclass(frozen=True)
class Issue:
    xhtml: str
    kind: str
    detail: str


def _extract_epub(epub: Path, out_dir: Path) -> None:
    if out_dir.exists():
        for p in out_dir.iterdir():
            if p.is_dir():
                for c in p.rglob("*"):
                    if c.is_file():
                        c.unlink(missing_ok=True)
                cdirs = sorted([d for d in p.rglob("*") if d.is_dir()], reverse=True)
                for d in cdirs:
                    try:
                        d.rmdir()
                    except OSError:
                        pass
            else:
                p.unlink(missing_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(epub, "r") as z:
        z.extractall(out_dir)


def audit_epub(*, epub: Path, viewport_w: int, viewport_h: int) -> tuple[list[Issue], dict]:
    _ensure_playwright()
    from playwright.sync_api import sync_playwright

    # Playwright uses TMPDIR for its own artifacts. If the environment TMPDIR
    # points at a non-existent directory (common when running inside a shell
    # script that rebinds TMPDIR), force it to a sane default.
    env_tmp = os.environ.get("TMPDIR")
    if env_tmp and not Path(env_tmp).exists():
        os.environ["TMPDIR"] = tempfile.gettempdir()

    with tempfile.TemporaryDirectory(prefix="ece657_epub_layout_") as td:
        root = Path(td)
        _extract_epub(epub, root)
        text_dir = root / "EPUB" / "text"
        css_path = root / "EPUB" / "styles" / "stylesheet1.css"
        if not text_dir.exists():
            raise SystemExit("EPUB/text not found in extracted epub")

        xhtmls = sorted(text_dir.glob("*.xhtml"))
        issues: list[Issue] = []
        stats = {"xhtml_files": len(xhtmls), "issues": 0}

        def _standalone_html(xhtml_path: Path) -> Path:
            html = xhtml_path.read_text(encoding="utf-8", errors="ignore")
            if css_path.exists():
                html = re.sub(r'href="\\.\\./styles/stylesheet1\\.css"', f'href="{css_path.as_uri()}"', html)
            out = root / (xhtml_path.stem + ".standalone.html")
            out.write_text(html, encoding="utf-8")
            return out

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": viewport_w, "height": viewport_h})

            for x in xhtmls:
                url = _standalone_html(x).as_uri()
                page.goto(url, wait_until="load")
                page.wait_for_timeout(120)

                findings = page.evaluate(
                    """() => {
  const vw = window.innerWidth;
  const out = [];
  const candidates = Array.from(document.querySelectorAll('math, pre, code, table, img, svg'));
  for (const el of candidates) {
    const rect = el.getBoundingClientRect();
    if (!rect || rect.width === 0 || rect.height === 0) continue;
    // horizontal overflow: element extends beyond viewport
    if (rect.right > vw + 2 || rect.left < -2) {
      out.push({
        tag: el.tagName.toLowerCase(),
        id: el.id || null,
        className: (el.getAttribute('class') || '').slice(0, 120),
        width: rect.width,
        left: rect.left,
        right: rect.right,
        display: (el.tagName.toLowerCase() === 'math') ? (el.getAttribute('display') || null) : null
      });
    }
  }
  return out;
}"""
                )

                for f in findings:
                    tag = f.get("tag") or "unknown"
                    disp = f.get("display")
                    kind = "overflow"
                    if tag == "math" and disp == "inline":
                        kind = "math-inline-overflow"
                    elif tag == "math" and disp == "block":
                        kind = "math-block-overflow"
                    detail = f"{tag} overflow (left={f.get('left'):.1f}, right={f.get('right'):.1f}, width={f.get('width'):.1f})"
                    if f.get("id"):
                        detail += f" id={f['id']}"
                    if f.get("className"):
                        detail += f" class={f['className']}"
                    issues.append(Issue(xhtml=x.name, kind=kind, detail=detail))

            browser.close()

        stats["issues"] = len(issues)
        return issues, stats


def write_markdown(*, out_md: Path, epub: Path, issues: list[Issue], stats: dict) -> None:
    out_md.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# EPUB editorial layout audit\n")
    lines.append(f"- EPUB: `{epub}`\n")
    lines.append(f"- XHTML files scanned: {stats.get('xhtml_files')}\n")
    lines.append(f"- Issues found: {stats.get('issues')}\n")
    lines.append("\n## What this audit checks\n")
    lines.append(
        "- Horizontal overflow candidates (`math`, `pre`, `code`, `table`, `img`, `svg`) whose bounding box extends beyond the viewport.\n"
    )
    lines.append("\n## Issues\n")
    if not issues:
        lines.append("- None detected by the automated layout scanner.\n")
    else:
        by_file: dict[str, list[Issue]] = {}
        for it in issues:
            by_file.setdefault(it.xhtml, []).append(it)
        for xhtml in sorted(by_file):
            lines.append(f"\n### `{xhtml}`\n")
            for it in by_file[xhtml]:
                lines.append(f"- `{it.kind}`: {it.detail}\n")

    lines.append("\n## Suggested global fixes\n")
    lines.append("- Prefer block math for long derivations (promote `\\(\\displaystyle ...\\)` to `\\[...\\]`).\n")
    lines.append("- Keep `math[display=\"block\"]` horizontally scrollable as a safety net.\n")
    lines.append("- Avoid oversized tables; ensure table CSS sets reasonable `min-width` and preserves readability.\n")
    lines.append("\n")
    out_md.write_text("".join(lines), encoding="utf-8")


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--epub", required=True)
    p.add_argument("--out-md", required=True)
    p.add_argument("--viewport-w", type=int, default=1000)
    p.add_argument("--viewport-h", type=int, default=1400)
    args = p.parse_args(argv)

    epub = Path(args.epub)
    out_md = Path(args.out_md)
    issues, stats = audit_epub(epub=epub, viewport_w=args.viewport_w, viewport_h=args.viewport_h)
    write_markdown(out_md=out_md, epub=epub, issues=issues, stats=stats)
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv[1:]))
