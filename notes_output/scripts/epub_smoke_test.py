#!/usr/bin/env python3
"""
Lightweight, offline EPUB smoke test for the ebook pipeline.

This does NOT replace Kindle Previewer visual QA, but it catches the main
regressions we've seen:
- Missing/unsupported image formats (svg/pdf references).
- Broken <img src> references.
- Images likely to render tiny due to excessive margins/whitespace.
- CSS-grid enumerate layout (known to clip in some Kindle engines).
- Very long code lines that can clip in reflow.
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops


@dataclass(frozen=True)
class ImageInfo:
    href: str
    path: Path
    pixel_width: int
    pixel_height: int
    content_ratio: float | None


def _extract_epub(epub: Path, out_dir: Path) -> None:
    with zipfile.ZipFile(epub) as z:
        z.extractall(out_dir)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _find_oebps(root: Path) -> Path:
    oebps = root / "OEBPS"
    if oebps.exists():
        return oebps
    # Some EPUBs have a different layout; fall back to searching.
    candidates = list(root.rglob("OEBPS"))
    if len(candidates) == 1:
        return candidates[0]
    raise FileNotFoundError("Could not locate OEBPS directory in extracted EPUB.")


def _compute_content_ratio(img: Image.Image) -> float | None:
    """
    Estimate how much of the image area contains non-background content.
    Returns None if the heuristic can't be computed.
    """
    try:
        rgba = img.convert("RGBA")
        rgb = rgba.convert("RGB")
        gray = rgb.convert("L")

        # Near-white background mask.
        white_threshold = 252
        mask = gray.point(lambda p: 255 if p < white_threshold else 0)

        if "A" in rgba.getbands():
            alpha = rgba.getchannel("A")
            # Ignore very faint pixels.
            alpha_mask = alpha.point(lambda p: 255 if p > 20 else 0)
            mask = ImageChops.multiply(mask, alpha_mask)

        bbox = mask.getbbox()
        if not bbox:
            return 0.0
        left, upper, right, lower = bbox
        content_area = max(0, right - left) * max(0, lower - upper)
        total_area = img.size[0] * img.size[1]
        if total_area <= 0:
            return None
        return content_area / total_area
    except Exception:
        return None


def _gather_images(oebps: Path, xhtml_files: list[Path]) -> tuple[list[ImageInfo], list[str]]:
    missing: list[str] = []
    infos: list[ImageInfo] = []

    seen: set[str] = set()
    for xf in xhtml_files:
        text = _read_text(xf)
        for src in re.findall(r"<img\b[^>]*\bsrc=(?:'([^']+)'|\"([^\"]+)\")", text):
            src = src[0] or src[1]
            if src in seen:
                continue
            seen.add(src)
            img_path = oebps / src
            if not img_path.exists():
                missing.append(src)
                continue
            if img_path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif"}:
                continue
            try:
                with Image.open(img_path) as im:
                    ratio = _compute_content_ratio(im)
                    infos.append(
                        ImageInfo(
                            href=src,
                            path=img_path,
                            pixel_width=im.size[0],
                            pixel_height=im.size[1],
                            content_ratio=ratio,
                        )
                    )
            except Exception:
                # Non-fatal; still note it as "missing-like" for debugging.
                missing.append(src + " (unreadable)")

    return infos, missing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("epub", help="Path to an EPUB file to test")
    parser.add_argument(
        "--allow-svg",
        action="store_true",
        help="Allow SVG assets/refs (useful for Apple Books builds that keep SVG math).",
    )
    args = parser.parse_args()

    epub = Path(args.epub).resolve()
    if not epub.exists():
        print(f"ERROR: file not found: {epub}", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory(prefix="ece657_epub_smoke_") as tmp:
        root = Path(tmp)
        _extract_epub(epub, root)
        oebps = _find_oebps(root)

        xhtml_files = sorted(oebps.glob("*.xhtml"))
        if not xhtml_files:
            print("ERROR: no .xhtml files found in OEBPS", file=sys.stderr)
            return 2

        # 0) Cover presence (Kindle-friendly pipeline should embed one if provided).
        cover_png = (oebps / "cover.png").exists()
        cover_xhtml = (oebps / "cover.xhtml").exists()

        # 1) Hard bans: unsupported assets or references.
        banned_exts = {".pdf"} if args.allow_svg else {".svg", ".pdf"}
        banned_assets = [p for p in oebps.rglob("*") if p.suffix.lower() in banned_exts]
        banned_refs: list[str] = []
        for xf in xhtml_files:
            t = _read_text(xf)
            if any(ext in t for ext in banned_exts):
                banned_refs.append(xf.name)

        # 2) CSS checks.
        if args.allow_svg:
            overrides = oebps / "apple_overrides.css"
            overrides_ok = overrides.exists()
            overrides_label = "Apple overrides present"
        else:
            overrides = oebps / "kindle_overrides.css"
            overrides_ok = overrides.exists() and "dl.enumerate-enumitem" in _read_text(overrides)
            overrides_label = "Kindle overrides present + enumerate fix"

        # 3) Images: existence + "likely tiny" heuristic (content ratio).
        images, missing_images = _gather_images(oebps, xhtml_files)
        tiny_candidates = [
            i
            for i in images
            if (i.content_ratio is not None and i.content_ratio < 0.12 and i.pixel_width >= 1200)
        ]

        # 4) Code blocks: flag very long lines (likely to clip).
        long_code: list[tuple[str, int]] = []
        nbsp_in_pre: list[str] = []
        anchors_without_style: list[str] = []
        toc_anchors_without_style: list[str] = []
        mathml_tags: list[str] = []
        for xf in xhtml_files:
            t = _read_text(xf)
            if re.search(r"<math\\b", t, flags=re.IGNORECASE):
                mathml_tags.append(xf.name)
            anchor_tags = re.findall(r"<a\\b[^>]*>", t, flags=re.IGNORECASE)
            if anchor_tags:
                missing = 0
                for a in anchor_tags:
                    if "style=" not in a.lower():
                        missing += 1
                if missing:
                    anchors_without_style.append(f"{xf.name} ({missing}/{len(anchor_tags)})")
                    if xf.name.startswith("ece657_ebookli"):
                        toc_anchors_without_style.append(f"{xf.name} ({missing}/{len(anchor_tags)})")
            for m in re.finditer(r"<pre[^>]*>([\s\S]*?)</pre>", t):
                pre = re.sub(r"<[^>]+>", "", m.group(1))
                if "\u00a0" in pre:
                    nbsp_in_pre.append(xf.name)
                for line in pre.splitlines():
                    if len(line) > 140:
                        long_code.append((xf.name, len(line)))
                        break

        # Report
        print(f"EPUB: {epub}")
        print(f"XHTML files: {len(xhtml_files)}")
        print(f"Cover present (cover.xhtml+cover.png): {'OK' if (cover_png and cover_xhtml) else 'MISSING'}")
        print(f"Banned assets (.svg/.pdf): {len(banned_assets)}")
        print(f"Banned refs in XHTML (.svg/.pdf): {len(banned_refs)}")
        print(f"Missing/unreadable images: {len(missing_images)}")
        print(f"{overrides_label}: {'OK' if overrides_ok else 'MISSING'}")
        print(f"Images found: {len(images)}")
        print(f"Whitespace-heavy images (may render tiny): {len(tiny_candidates)}")
        print(f"XHTML with very long <pre> lines: {len(long_code)}")
        print(f"XHTML with NBSP in <pre>: {len(set(nbsp_in_pre))}")
        print(f"XHTML with <a> lacking style: {len(anchors_without_style)}")
        print(f"TOC/listing XHTML with <a> lacking style: {len(toc_anchors_without_style)}")
        print(f"XHTML containing MathML (<math>): {len(set(mathml_tags))}")

        if banned_assets:
            print("\nBANNED ASSETS (first 20):")
            for p in banned_assets[:20]:
                print(f"- {p.relative_to(oebps).as_posix()}")

        if banned_refs:
            print("\nBANNED XHTML REFS:")
            for n in banned_refs[:20]:
                print(f"- {n}")

        if missing_images:
            print("\nMISSING/UNREADABLE IMAGES (first 30):")
            for src in missing_images[:30]:
                print(f"- {src}")

        if tiny_candidates:
            print("\nWHITESPACE-HEAVY IMAGES (top 20 worst):")
            worst = sorted(
                (i for i in tiny_candidates if i.content_ratio is not None),
                key=lambda x: x.content_ratio,
            )[:20]
            for i in worst:
                print(
                    f"- {i.href}  {i.pixel_width}x{i.pixel_height}  content_ratio={i.content_ratio:.3f}"
                )

        if long_code:
            print("\nLONG CODE LINES (first 20):")
            for name, ln in long_code[:20]:
                print(f"- {name}: longest_line_len~{ln}")

        if mathml_tags:
            print("\nMATHML TAGS PRESENT (first 20 files):")
            for name in sorted(set(mathml_tags))[:20]:
                print(f"- {name}")

        if nbsp_in_pre:
            print("\nNBSP IN <pre> (first 20):")
            for name in sorted(set(nbsp_in_pre))[:20]:
                print(f"- {name}")

        if toc_anchors_without_style:
            print("\nTOC/LISTING ANCHORS MISSING INLINE STYLE (first 20):")
            for name in toc_anchors_without_style[:20]:
                print(f"- {name}")

        # Non-zero exit for hard failures only.
        if banned_assets or banned_refs or missing_images:
            return 1
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
