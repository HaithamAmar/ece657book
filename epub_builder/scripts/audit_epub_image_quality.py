#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image


def _read_png_jpg(path: Path) -> Image.Image:
    img = Image.open(path)
    # Normalize into RGB for consistent metrics.
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA" if "A" in img.getbands() else "RGB")
    return img


def _to_gray_np(img: Image.Image) -> np.ndarray:
    # Use Rec. 601 luma.
    arr = np.asarray(img)
    if arr.ndim == 2:
        return arr.astype(np.float32) / 255.0
    if arr.shape[2] == 4:
        arr = arr[:, :, :3]
    r = arr[:, :, 0].astype(np.float32)
    g = arr[:, :, 1].astype(np.float32)
    b = arr[:, :, 2].astype(np.float32)
    y = 0.299 * r + 0.587 * g + 0.114 * b
    return y / 255.0


def _laplacian_variance(gray: np.ndarray) -> float:
    # Simple 3x3 Laplacian kernel.
    k = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
    # Convolution via slicing; avoid scipy dependency.
    g = gray
    if g.shape[0] < 3 or g.shape[1] < 3:
        return 0.0
    c = (
        k[0, 1] * g[:-2, 1:-1]
        + k[1, 0] * g[1:-1, :-2]
        + k[1, 1] * g[1:-1, 1:-1]
        + k[1, 2] * g[1:-1, 2:]
        + k[2, 1] * g[2:, 1:-1]
    )
    return float(np.var(c))

def _autocrop_nonwhite(gray: np.ndarray, *, thr: float = 0.985, pad: int = 8) -> np.ndarray:
    """
    Crop to the bounding box of non-white pixels (gray < thr). This helps avoid
    captions/margins dominating sharpness metrics.
    """
    if gray.size == 0:
        return gray
    mask = gray < thr
    if not mask.any():
        return gray
    ys, xs = np.where(mask)
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    y0 = max(0, y0 - pad)
    x0 = max(0, x0 - pad)
    y1 = min(gray.shape[0] - 1, y1 + pad)
    x1 = min(gray.shape[1] - 1, x1 + pad)
    cropped = gray[y0 : y1 + 1, x0 : x1 + 1]
    # If the crop is suspiciously tiny, fall back to the full image.
    if cropped.shape[0] < 80 or cropped.shape[1] < 80:
        return gray
    return cropped


def _edge_density(gray: np.ndarray) -> float:
    # Gradient magnitude thresholding.
    if gray.shape[0] < 2 or gray.shape[1] < 2:
        return 0.0
    gx = np.abs(gray[:, 1:] - gray[:, :-1])
    gy = np.abs(gray[1:, :] - gray[:-1, :])
    # Normalize by typical contrast; threshold at ~2% change.
    thr = 0.02
    edges = (gx > thr).sum() + (gy > thr).sum()
    denom = gx.size + gy.size
    return float(edges / max(1, denom))


def _white_fraction(gray: np.ndarray, *, thr: float = 0.97) -> float:
    return float((gray >= thr).mean())


def _border_nonwhite_fraction(gray: np.ndarray, *, thr: float = 0.97, border_px: int = 3) -> float:
    h, w = gray.shape
    b = min(border_px, h // 2, w // 2)
    if b <= 0:
        return 0.0
    top = gray[:b, :]
    bot = gray[-b:, :]
    left = gray[:, :b]
    right = gray[:, -b:]
    border = np.concatenate([top.ravel(), bot.ravel(), left.ravel(), right.ravel()])
    return float((border < thr).mean())


@dataclass(frozen=True)
class Ref:
    xhtml: str
    figure_id: str | None
    src: str
    caption: str | None


def _extract_refs(epub: Path) -> dict[str, list[Ref]]:
    """
    Map media href (EPUB/media/fileNN.png) -> references (xhtml, caption, id).
    """
    refs: dict[str, list[Ref]] = {}
    with zipfile.ZipFile(epub, "r") as z:
        names = set(z.namelist())
        xhtmls = [n for n in names if n.startswith("EPUB/text/") and n.endswith(".xhtml")]
        for x in xhtmls:
            s = z.read(x).decode("utf-8", errors="ignore")
            # Naive figure id association: look for <figure id="..."> and the first <img ... src=...>
            for fig_m in re.finditer(r'<figure\b([^>]*)>(.*?)</figure>', s, flags=re.DOTALL | re.IGNORECASE):
                attrs = fig_m.group(1) or ""
                body = fig_m.group(2) or ""
                id_m = re.search(r'\bid="([^"]+)"', attrs)
                fig_id = id_m.group(1) if id_m else None
                img_m = re.search(r'<img\b[^>]*\bsrc="([^"]+)"', body, flags=re.IGNORECASE)
                if not img_m:
                    continue
                src = img_m.group(1)
                if not src.startswith("../media/"):
                    continue
                media = "EPUB/" + src[len("../") :]
                if media not in names:
                    continue
                cap_m = re.search(r"<figcaption\b[^>]*>(.*?)</figcaption>", body, flags=re.DOTALL | re.IGNORECASE)
                caption = None
                if cap_m:
                    cap_txt = re.sub(r"<[^>]+>", " ", cap_m.group(1))
                    caption = re.sub(r"\s+", " ", cap_txt).strip()
                refs.setdefault(media, []).append(
                    Ref(xhtml=x, figure_id=fig_id, src=src, caption=caption)
                )
            # Tables often reference no <img>; ignore here.
    return refs


def audit(*, epub: Path, qc_dir: Path | None, out_json: Path) -> None:
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="ece657_epub_imgq_") as td:
        root = Path(td)
        with zipfile.ZipFile(epub, "r") as z:
            z.extractall(root)
        media_dir = root / "EPUB" / "media"
        if not media_dir.exists():
            raise SystemExit("EPUB/media not found")

        # Detect cover image from OPF to avoid misclassifying full-bleed covers
        # as "cropping" (they intentionally touch borders).
        cover_media: str | None = None
        opf = root / "EPUB" / "content.opf"
        if opf.exists():
            xml = opf.read_text(encoding="utf-8", errors="ignore")
            m = re.search(r'<item[^>]*properties="cover-image"[^>]*href="([^"]+)"', xml)
            if m:
                href = m.group(1)
                if href.startswith("media/"):
                    cover_media = "EPUB/" + href

        refs_by_media = _extract_refs(epub)

        # Optional: compare against QC bundle (PDF vs EPUB crops) for sharpness regression.
        qc_items: dict[str, dict] = {}
        if qc_dir and qc_dir.exists():
            mf = qc_dir / "manifest.json"
            if mf.exists():
                try:
                    qc = json.loads(mf.read_text(encoding="utf-8"))
                    items = qc.get("items", {})
                    if isinstance(items, dict):
                        qc_items = items
                except Exception:
                    qc_items = {}

        results = []
        for p in sorted(media_dir.iterdir()):
            if not p.is_file():
                continue
            if p.suffix.lower() not in (".png", ".jpg", ".jpeg"):
                continue
            img = _read_png_jpg(p)
            w, h = img.size
            gray = _to_gray_np(img)
            lap = _laplacian_variance(gray)
            edge = _edge_density(gray)
            white = _white_fraction(gray)
            border_nonwhite = _border_nonwhite_fraction(gray)

            # Heuristic flags
            flags: list[str] = []
            if min(w, h) < 1200:
                flags.append("small_pixel_dimensions")
            if white > 0.985 and edge < 0.002:
                flags.append("mostly_blank")
            # Border activity suggests possible cropping (content touches border).
            if border_nonwhite > 0.20 and white < 0.95:
                flags.append("content_touches_border")
            # Sharpness: lower values indicate blur, but depends on type; use conservative thresholds.
            if lap < 0.00035 and edge < 0.01 and white < 0.98:
                flags.append("low_sharpness")

            media_path = "EPUB/media/" + p.name
            is_cover = bool(cover_media and media_path == cover_media)
            if cover_media and media_path == cover_media:
                # Full-bleed cover art will touch borders; that's expected.
                flags = [f for f in flags if f not in ("content_touches_border", "small_pixel_dimensions")]
            refs = refs_by_media.get(media_path, [])

            results.append(
                {
                    "media_path": media_path,
                    "file_bytes": p.stat().st_size,
                    "width": w,
                    "height": h,
                    "aspect": round(w / h, 4) if h else None,
                    "metrics": {
                        "laplacian_var": lap,
                        "edge_density": edge,
                        "white_fraction": white,
                        "border_nonwhite_fraction": border_nonwhite,
                    },
                    "flags": flags,
                    "risk_score": None,
                    "is_cover": is_cover,
                    "refs": [
                        {
                            "xhtml": r.xhtml,
                            "figure_id": r.figure_id,
                            "caption": r.caption,
                        }
                        for r in refs
                    ],
                }
            )

        # Risk scoring (used to prioritize review even when nothing crosses hard thresholds).
        for im in results:
            m = im["metrics"]
            w = im["width"]
            h = im["height"]
            if im.get("is_cover"):
                im["risk_score"] = 0.0
                continue
            score = 0.0
            score += max(0.0, (1400 - min(w, h)) / 1400) * 10  # small images
            score += max(0.0, (0.001 - m["laplacian_var"]) / 0.001) * 12  # blur-ish
            score += max(0.0, (m["border_nonwhite_fraction"] - 0.15) / 0.85) * 8  # cropping-ish
            score += max(0.0, (m["white_fraction"] - 0.97) / 0.03) * 15  # blank-ish
            im["risk_score"] = round(float(score), 3)

        # Add figure sharpness regression vs PDF crops when QC bundle is available.
        blur_regressions: list[dict] = []
        if qc_items:
            for key, it in qc_items.items():
                if not isinstance(it, dict) or it.get("kind") != "fig":
                    continue
                pdf_png = it.get("pdf_png")
                epub_png = it.get("epub_png")
                if not pdf_png or not epub_png:
                    continue
                try:
                    pdf_im = _read_png_jpg(Path(pdf_png))
                    epub_im = _read_png_jpg(Path(epub_png))
                except Exception:
                    continue
                pdf_full = _to_gray_np(pdf_im)
                epub_full = _to_gray_np(epub_im)
                # Only compare sharpness when the crops appear to represent the same
                # content scale (otherwise page-crop text dominates PDF metrics).
                pdf_white = _white_fraction(pdf_full)
                epub_white = _white_fraction(epub_full)
                if abs(pdf_white - epub_white) > 0.08:
                    continue
                pdf_ar = pdf_im.size[0] / max(1, pdf_im.size[1])
                epub_ar = epub_im.size[0] / max(1, epub_im.size[1])
                if abs(pdf_ar - epub_ar) > 0.12:
                    continue

                pdf_g = _autocrop_nonwhite(pdf_full)
                epub_g = _autocrop_nonwhite(epub_full)
                pdf_lap = _laplacian_variance(pdf_g)
                epub_lap = _laplacian_variance(epub_g)
                if pdf_lap <= 0:
                    continue
                ratio = epub_lap / pdf_lap
                # Flag only when both have meaningful detail but EPUB is significantly softer.
                if pdf_lap > 0.001 and epub_lap > 0.001 and ratio < 0.70:
                    blur_regressions.append(
                        {
                            "label": key.replace("fig:", "fig:") if key.startswith("fig:") else key,
                            "number": it.get("number"),
                            "pdf_lap": pdf_lap,
                            "epub_lap": epub_lap,
                            "ratio": ratio,
                            "pdf_white": pdf_white,
                            "epub_white": epub_white,
                            "compare_png": it.get("compare_png"),
                            "epub_png": epub_png,
                            "pdf_png": pdf_png,
                            "epub_xhtml": it.get("epub_xhtml"),
                        }
                    )
            blur_regressions.sort(key=lambda r: r["ratio"])

        payload = {
            "epub": str(epub),
            "qc_dir": str(qc_dir) if qc_dir else None,
            "cover_media": cover_media,
            "images": results,
            "qc_blur_regressions": blur_regressions,
            "summary": {
                "total_images": len(results),
                "flagged_images": sum(1 for r in results if r["flags"]),
            },
        }
        out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_markdown(*, src_json: Path, out_md: Path, top_n: int) -> None:
    data = json.loads(src_json.read_text(encoding="utf-8"))
    images = data["images"]
    # Sort by severity: number of flags then risk score.
    def score(it):
        return (len(it["flags"]) * 100) + float(it.get("risk_score") or 0.0)

    worst = [im for im in images if not im.get("is_cover")]
    worst = sorted(worst, key=score, reverse=True)[:top_n]

    out_md.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# EPUB image quality audit (heuristic + model-assisted triage)\n\n")
    lines.append(f"- Source JSON: `{src_json}`\n")
    lines.append(f"- Total images: {data['summary']['total_images']}\n")
    lines.append(f"- Flagged images: {data['summary']['flagged_images']}\n\n")
    lines.append("## How to interpret flags\n\n")
    lines.append("- `small_pixel_dimensions`: likely to appear soft when zoomed.\n")
    lines.append("- `low_sharpness`: blurred / low-detail raster (often from low-DPI conversion).\n")
    lines.append("- `content_touches_border`: potential cropping or insufficient padding.\n")
    lines.append("- `mostly_blank`: likely missing render or transparent/blank export.\n\n")

    lines.append("## Worst offenders (prioritized)\n\n")
    cover = data.get("cover_media")
    if cover:
        cover_item = next((im for im in images if im.get("media_path") == cover), None)
        if cover_item:
            lines.append("### Cover image\n")
            lines.append(f"- Media: `{cover}`\n")
            lines.append(f"- Size: {cover_item['width']}×{cover_item['height']} ({cover_item['file_bytes']} bytes)\n")
            lines.append("\n")
    for im in worst:
        lines.append(f"### `{im['media_path']}`\n")
        lines.append(f"- Size: {im['width']}×{im['height']} ({im['file_bytes']} bytes)\n")
        lines.append(f"- Risk score: {im.get('risk_score')}\n")
        lines.append(f"- Flags: {', '.join(im['flags']) if im['flags'] else '(none)'}\n")
        m = im["metrics"]
        lines.append(
            f"- Metrics: lap_var={m['laplacian_var']:.6f}, edge={m['edge_density']:.4f}, "
            f"white={m['white_fraction']:.3f}, border_nonwhite={m['border_nonwhite_fraction']:.3f}\n"
        )
        if im["refs"]:
            r = im["refs"][0]
            if r.get("figure_id"):
                lines.append(f"- Ref: `{r['figure_id']}` in `{r['xhtml']}`\n")
            else:
                lines.append(f"- Ref: `{r['xhtml']}`\n")
            if r.get("caption"):
                lines.append(f"- Caption: {r['caption']}\n")
        lines.append("\n")

    # QC comparison section (PDF vs EPUB sharpness)
    regress = data.get("qc_blur_regressions") or []
    lines.append("## Figures softer than PDF (from QC bundle)\n\n")
    if not regress:
        lines.append("- None detected by the current sharpness regression heuristic.\n\n")
    else:
        for r in regress[: min(30, len(regress))]:
            lines.append(f"- `{r.get('label')}` (Figure {r.get('number')}): ratio={r.get('ratio'):.3f}, epub_lap={r.get('epub_lap'):.6f}, pdf_lap={r.get('pdf_lap'):.6f}\n")
            if r.get("compare_png"):
                lines.append(f"  - Compare: `{r['compare_png']}`\n")
        lines.append("\n")

    lines.append("## Suggested fixes (global)\n\n")
    lines.append("- Prefer PDF→PNG rasterization at high DPI for plots/diagrams when a `.pdf` exists.\n")
    lines.append("- Keep TikZ extracted figures at high DPI (already enabled) and consider increasing figure physical size for very thin diagrams.\n")
    lines.append("- Ensure images referenced by `\\includegraphics{...png}` prefer sibling `.pdf` sources when available.\n")
    lines.append("\n")
    out_md.write_text("".join(lines), encoding="utf-8")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--epub", required=True)
    ap.add_argument("--qc-dir", default="")
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-md", default="")
    ap.add_argument("--top", type=int, default=25)
    args = ap.parse_args(argv)

    epub = Path(args.epub)
    qc_dir = Path(args.qc_dir) if args.qc_dir else None
    out_json = Path(args.out_json)
    audit(epub=epub, qc_dir=qc_dir, out_json=out_json)
    if args.out_md:
        write_markdown(src_json=out_json, out_md=Path(args.out_md), top_n=args.top)
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv[1:]))
