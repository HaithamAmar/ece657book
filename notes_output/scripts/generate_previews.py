#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from PIL import Image


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def _ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def _load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _render_pdf_pages(pdf: Path, out_dir: Path, pages: list[int], dpi: int) -> dict:
    gs = shutil.which("gs") or shutil.which("gswin64c") or shutil.which("gswin32c")
    if not gs:
        raise RuntimeError("Ghostscript not found on PATH (install via `brew install ghostscript`).")

    pdf_dir = out_dir / "pdf"
    _ensure_dir(pdf_dir)

    results: dict[str, dict] = {}
    for page in pages:
        out_png = pdf_dir / f"ece657_notes_page-{page:03d}.png"
        _run(
            [
                gs,
                "-dSAFER",
                "-dBATCH",
                "-dNOPAUSE",
                "-dTextAlphaBits=4",
                "-dGraphicsAlphaBits=4",
                "-dBackgroundColor=16#FFFFFF",
                "-dUseCropBox",
                "-dFirstPage=" + str(page),
                "-dLastPage=" + str(page),
                # Use an RGB device (not pngalpha) so previews don't display
                # transparent regions as black in some image viewers.
                "-sDEVICE=png16m",
                f"-r{dpi}",
                f"-sOutputFile={out_png}",
                str(pdf),
            ]
        )
        with Image.open(out_png) as im:
            width, height = im.size
        results[str(page)] = {"file": out_png.name, "sha256": _sha256(out_png), "w": width, "h": height}

    return results


def _extract_epub_targets(epub: Path, out_dir: Path, keywords: list[str]) -> dict:
    epub_dir = out_dir / "epub"
    _ensure_dir(epub_dir)

    matches: dict[str, dict] = {}
    with tempfile.TemporaryDirectory(prefix="ece657_epub_previews_") as tmp:
        tmp_dir = Path(tmp)
        with zipfile.ZipFile(epub) as z:
            z.extractall(tmp_dir)

        # Support both TeX4ht-style EPUBs (OEBPS/) and Pandoc-style EPUBs (EPUB/).
        content_root: Path | None = None
        xhtml_root: Path | None = None

        oebps = tmp_dir / "OEBPS"
        if oebps.exists():
            content_root = oebps
            xhtml_root = oebps
        else:
            candidates = list(tmp_dir.rglob("OEBPS"))
            if len(candidates) == 1:
                content_root = candidates[0]
                xhtml_root = candidates[0]

        if content_root is None:
            epub3 = tmp_dir / "EPUB"
            if epub3.exists():
                content_root = epub3
                if (epub3 / "text").exists():
                    xhtml_root = epub3 / "text"
                else:
                    xhtml_root = epub3
            else:
                candidates = list(tmp_dir.rglob("EPUB"))
                if len(candidates) == 1:
                    content_root = candidates[0]
                    if (content_root / "text").exists():
                        xhtml_root = content_root / "text"
                    else:
                        xhtml_root = content_root

        if content_root is None or xhtml_root is None:
            raise FileNotFoundError("Could not locate OEBPS/ or EPUB/ in extracted EPUB.")

        xhtml_files = sorted(xhtml_root.glob("*.xhtml"))
        for xf in xhtml_files:
            text = xf.read_text(encoding="utf-8", errors="replace")
            hit = [k for k in keywords if k in text]
            if not hit:
                continue

            rel = xf.relative_to(xhtml_root).as_posix()
            entry = matches.setdefault(rel, {"keywords": hit, "images": [], "pre_txt": []})

            # Copy referenced images.
            img_srcs = set()
            for m in re.findall(r"<img\b[^>]*\bsrc=(?:'([^']+)'|\"([^\"]+)\")", text):
                src = m[0] or m[1]
                img_srcs.add(src)
            for src in sorted(img_srcs):
                # Resolve relative to the XHTML file location (works for both
                # `OEBPS/foo.png` and `EPUB/text/../media/file0.png`).
                img_path = (xf.parent / src).resolve()
                try:
                    img_path.relative_to(content_root.resolve())
                except Exception:
                    # If src resolution escaped the content root, fall back to
                    # resolving from the content root itself.
                    img_path = (content_root / src).resolve()
                if not img_path.exists() or img_path.is_dir():
                    continue
                out_path = epub_dir / src.replace("/", "__")
                shutil.copyfile(img_path, out_path)
                meta = {"src": src, "file": out_path.name, "sha256": _sha256(out_path)}
                if out_path.suffix.lower() in {".png", ".jpg", ".jpeg"}:
                    try:
                        with Image.open(out_path) as im:
                            meta.update({"w": im.size[0], "h": im.size[1]})
                    except Exception:
                        pass
                entry["images"].append(meta)

            # Extract <pre> blocks (pseudocode/code) into text files for quick review.
            pres = []
            for pm in re.finditer(r"<pre[^>]*>([\s\S]*?)</pre>", text):
                pre = re.sub(r"<[^>]+>", "", pm.group(1))
                pre = pre.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
                pres.append(pre.strip())
            if pres:
                for idx, pre in enumerate(pres, start=1):
                    out_txt = epub_dir / f"{Path(rel).stem}__pre{idx}.txt"
                    out_txt.write_text(pre + "\n", encoding="utf-8")
                    entry["pre_txt"].append({"file": out_txt.name, "sha256": _sha256(out_txt)})

    return matches


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, help="Path to compiled PDF (print)")
    parser.add_argument("--epub", required=True, help="Path to EPUB (Kindle-optimized recommended)")
    parser.add_argument("--out", required=True, help="Output directory for previews and manifest")
    parser.add_argument(
        "--config",
        default="critical_checks.json",
        help="JSON config with pdf_pages and epub_keywords (relative to notes_output unless absolute)",
    )
    parser.add_argument("--pdf-dpi", type=int, default=150, help="DPI for PDF page rasterization")
    args = parser.parse_args()

    out_dir = Path(args.out).resolve()
    _ensure_dir(out_dir)

    pdf = Path(args.pdf).resolve()
    epub = Path(args.epub).resolve()

    config_path = Path(args.config)
    if not config_path.is_absolute():
        # Assume invoked from notes_output.
        config_path = (Path.cwd() / config_path).resolve()
    config = _load_config(config_path)

    pdf_pages = [int(p) for p in config.get("pdf_pages", [])]
    epub_keywords = [str(s) for s in config.get("epub_keywords", [])]

    manifest_path = out_dir / "manifest.json"
    prev = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}

    pdf_manifest = _render_pdf_pages(pdf, out_dir, pdf_pages, dpi=args.pdf_dpi)
    epub_manifest = _extract_epub_targets(epub, out_dir, epub_keywords)

    manifest = {
        "pdf": {"file": str(pdf), "dpi": args.pdf_dpi, "pages": pdf_manifest},
        "epub": {"file": str(epub), "xhtml_matches": epub_manifest},
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")

    # Simple diff summary.
    changed_pages = []
    prev_pages = (prev.get("pdf", {}) or {}).get("pages", {}) if isinstance(prev, dict) else {}
    for p, meta in pdf_manifest.items():
        if prev_pages.get(p, {}).get("sha256") and prev_pages[p]["sha256"] != meta["sha256"]:
            changed_pages.append(p)

    report = out_dir / "report.txt"
    lines = []
    lines.append(f"PDF preview pages: {len(pdf_pages)} (changed vs previous: {len(changed_pages)})")
    if changed_pages:
        lines.append("Changed pages: " + ", ".join(changed_pages))
    lines.append(f"EPUB XHTML matches: {len(epub_manifest)}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
