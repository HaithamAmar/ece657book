#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path


def _ensure_playwright() -> None:
    try:
        import playwright.sync_api  # noqa: F401
    except ModuleNotFoundError as e:
        raise SystemExit(
            "Missing dependency: playwright. Install it with:\n"
            "  python3 -m venv epub_builder/.venv\n"
            "  epub_builder/.venv/bin/pip install playwright\n"
            "  epub_builder/.venv/bin/python -m playwright install chromium\n"
        ) from e


def _ensure_chromium_installed(python: str) -> None:
    proc = subprocess.run([python, "-m", "playwright", "install", "chromium"], check=False)
    if proc.returncode != 0:
        raise SystemExit("Failed to install Playwright Chromium. See output above.")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--epub", required=True, help="Path to an .epub file")
    ap.add_argument("--out", default="epub_builder/artifacts/screenshots", help="Output directory")
    ap.add_argument("--count", type=int, default=10, help="Number of chapter XHTML files to capture")
    ap.add_argument("--width", type=int, default=1100)
    ap.add_argument("--height", type=int, default=1400)
    ap.add_argument("--python", default=str(Path(__file__).resolve().parents[1] / ".venv" / "bin" / "python"))
    ap.add_argument(
        "--ensure-chromium",
        action="store_true",
        help="Run `python -m playwright install chromium` before rendering (may download).",
    )
    args = ap.parse_args(argv)

    epub_path = Path(args.epub).resolve()
    if not epub_path.exists():
        raise SystemExit(f"Missing EPUB: {epub_path}")

    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    _ensure_playwright()

    if args.ensure_chromium:
        python = args.python
        if Path(python).exists():
            _ensure_chromium_installed(python)

    from playwright.sync_api import sync_playwright

    tmp_root = Path("epub_builder/artifacts/tmp").resolve()
    tmp_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="render_epub_", dir=tmp_root) as tmp:
        tmp_dir = Path(tmp)
        with zipfile.ZipFile(epub_path, "r") as z:
            z.extractall(tmp_dir)

        text_dir = tmp_dir / "EPUB" / "text"
        if not text_dir.exists():
            raise SystemExit("Unexpected EPUB layout: missing EPUB/text/")

        # Prefer chapter-ish files (chNNN.xhtml), skip title/nav.
        pages = sorted([p for p in text_dir.glob("ch*.xhtml") if p.is_file()])
        pages = pages[: max(1, args.count)]

        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page(viewport={"width": args.width, "height": args.height})

            for idx, xhtml in enumerate(pages, start=1):
                url = xhtml.resolve().as_uri()
                page.goto(url, wait_until="load")
                # Give MathML/layout a moment in some engines.
                page.wait_for_timeout(250)
                stem = xhtml.stem
                out_png = out_dir / f"{idx:02d}_{stem}.png"
                page.screenshot(path=str(out_png), full_page=True)

            browser.close()

    # Convenience: copy the EPUB alongside screenshots for easy sharing.
    try:
        shutil.copyfile(epub_path, out_dir / epub_path.name)
    except OSError:
        pass

    print(f"Wrote screenshots to: {out_dir}")
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv[1:]))
