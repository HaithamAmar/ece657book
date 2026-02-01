#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ImgRef:
    xhtml: str
    figure_id: str | None
    src: str
    caption: str | None


def _sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()


def _strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _collect_img_refs(xhtml: str, content: str) -> list[ImgRef]:
    out: list[ImgRef] = []
    # Capture <figure ...> blocks and associate <img src> with that figure id/caption.
    for fm in re.finditer(r"<figure\b.*?</figure>", content, flags=re.DOTALL):
        block = fm.group(0)
        fig_id_m = re.search(r'id="([^"]+)"', block)
        fig_id = fig_id_m.group(1) if fig_id_m else None
        cap_m = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", block, flags=re.DOTALL)
        caption = _strip_tags(cap_m.group(1)) if cap_m else None
        for im in re.finditer(r'<img\b[^>]*\bsrc="([^"]+)"', block):
            out.append(ImgRef(xhtml=xhtml, figure_id=fig_id, src=im.group(1), caption=caption))

    # Also include bare <img> not inside <figure> (rare, but can happen).
    for im in re.finditer(r'<img\b[^>]*\bsrc="([^"]+)"', content):
        src = im.group(1)
        if any(r.src == src and r.xhtml == xhtml for r in out):
            continue
        out.append(ImgRef(xhtml=xhtml, figure_id=None, src=src, caption=None))
    return out


def _zip_media_path(src: str) -> str | None:
    s = src.strip().split("#", 1)[0].split("?", 1)[0]
    if s.startswith("../media/"):
        return "EPUB/media/" + s[len("../media/") :]
    if s.startswith("media/"):
        return "EPUB/media/" + s[len("media/") :]
    if s.startswith("../"):
        return "EPUB/" + s[len("../") :]
    return None


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--epub", default="epub_builder/dist/ece657_ebook_apple.epub")
    ap.add_argument("--out", default="epub_builder/artifacts/qc/epub_image_audit.json")
    ap.add_argument("--min-width", type=int, default=1400)
    ap.add_argument("--min-height", type=int, default=900)
    args = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[2]
    epub_path = (repo_root / args.epub).resolve()
    out_path = (repo_root / args.out).resolve()

    if not epub_path.exists():
        raise SystemExit(f"Missing EPUB: {epub_path}")

    # PIL is optional; the audit still works without dimensions.
    try:
        from PIL import Image  # type: ignore
    except Exception:
        Image = None  # type: ignore

    report: dict[str, object] = {
        "epub": str(epub_path),
        "min_width": args.min_width,
        "min_height": args.min_height,
        "images": [],
    }

    with zipfile.ZipFile(epub_path, "r") as z:
        names = set(z.namelist())
        xhtmls = sorted(n for n in names if n.startswith("EPUB/text/") and n.endswith(".xhtml"))

        refs: list[ImgRef] = []
        for n in xhtmls:
            s = z.read(n).decode("utf-8", errors="ignore")
            refs.extend(_collect_img_refs(n, s))

        # Deduplicate by (xhtml, src, figure_id)
        seen: set[tuple[str, str, str | None]] = set()
        refs2: list[ImgRef] = []
        for r in refs:
            key = (r.xhtml, r.src, r.figure_id)
            if key in seen:
                continue
            seen.add(key)
            refs2.append(r)

        by_media: dict[str, list[ImgRef]] = {}
        for r in refs2:
            zp = _zip_media_path(r.src)
            if not zp:
                continue
            by_media.setdefault(zp, []).append(r)

        for media_path, refs_for in sorted(by_media.items()):
            if media_path not in names:
                report["images"].append(
                    {
                        "media_path": media_path,
                        "missing_in_zip": True,
                        "refs": [r.__dict__ for r in refs_for],
                    }
                )
                continue

            b = z.read(media_path)
            sha = _sha256_bytes(b)
            w = h = None
            if Image is not None:
                try:
                    import io

                    img = Image.open(io.BytesIO(b))
                    w, h = img.size
                except Exception:
                    w = h = None

            low = False
            if w is not None and h is not None:
                low = w < args.min_width or h < args.min_height

            report["images"].append(
                {
                    "media_path": media_path,
                    "sha256": sha,
                    "width": w,
                    "height": h,
                    "file_bytes": len(b),
                    "low_resolution": low,
                    "refs": [r.__dict__ for r in refs_for],
                }
            )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lows = [x for x in report["images"] if isinstance(x, dict) and x.get("low_resolution")]
    print(f"Wrote: {out_path}")
    print(f"Total media images referenced: {len(report['images'])}")
    print(f"Flagged low-resolution: {len(lows)}")
    return 0


if __name__ == "__main__":
    import sys

    raise SystemExit(main(sys.argv[1:]))

