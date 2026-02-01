#!/usr/bin/env python3
"""
Post-process a TeX4ht/tex4ebook-generated EPUB for Kindle friendliness.

Goals:
- Replace SVG images with PNG (Kindle renderers are inconsistent with SVG).
- Replace PDF images with PNG (many EPUB renderers cannot display PDF).
- Add lightweight CSS overrides for image scaling and code/pre readability.
- Avoid touching LaTeX sources (single source of truth stays in .tex files).
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image
from PIL import ImageDraw, ImageFont


def _normalize_pre_text(text: str) -> str:
    # The TeX4ht XHTML contains HTML entities inside <pre> (e.g. `&gt;`, `&lt;`,
    # `&amp;`) which browsers would normally decode. We rasterize <pre> blocks for
    # Kindle, so decode entities up front to avoid emitting `&gt;` literally.
    text = html.unescape(text)
    # TeX4ht often emits NBSP inside <pre>, which prevents wrapping and can
    # trigger clipping in Kindle engines. Also strip soft-hyphens and
    # zero-width spaces that can create confusing breaks in code listings.
    return (
        text.replace("\u00a0", " ")
        .replace("\u00ad", "")
        .replace("\u200b", "")
        .replace("\ufeff", "")
    )


def _normalize_mathml(mathml: str) -> str:
    return re.sub(r"\s+", " ", mathml).strip()


def _mathml_to_alt(mathml: str) -> str:
    text = re.sub(r"<[^>]+>", " ", mathml)
    text = re.sub(r"\s+", " ", text).strip()
    return text if text else "Math equation"


def _is_display_math(mathml: str) -> bool:
    return re.search(r"\bdisplay\s*=\s*['\"]block['\"]", mathml, flags=re.IGNORECASE) is not None


def _svg_intrinsic_width_px(svg_path: Path) -> int | None:
    """
    Best-effort parse of an SVG's intrinsic width. Returns pixels (rounded) or None.
    Used to avoid upscaling small equations to a fixed target width.
    """
    try:
        # Read enough to capture the opening <svg ...> tag.
        head = svg_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None

    # Restrict parsing to the opening <svg ...> tag; SVGs commonly contain nested
    # elements with width="0" that would otherwise cause us to clamp to 1px.
    svg_tag_match = re.search(r"<svg\b[^>]*>", head, flags=re.IGNORECASE | re.DOTALL)
    if not svg_tag_match:
        return None
    svg_tag = svg_tag_match.group(0)

    # Prefer viewBox width when present; MathJax-generated SVGs typically use
    # width/height in ex units but include a numeric viewBox.
    vb = re.search(r'\bviewBox\s*=\s*"([^"]+)"', svg_tag, flags=re.IGNORECASE)
    if vb:
        parts = [p for p in re.split(r"[\s,]+", vb.group(1).strip()) if p]
        if len(parts) == 4:
            try:
                return max(1, int(round(float(parts[2]))))
            except Exception:
                pass

    # Fallback: <svg ... width="1234" ...> or width="1234px" or width="12pt".
    m = re.search(r'\bwidth\s*=\s*"([0-9.]+)\s*([a-z%]*)"', svg_tag, flags=re.IGNORECASE)
    if m:
        try:
            value = float(m.group(1))
        except Exception:
            return None
        unit = (m.group(2) or "").lower()
        # Heuristic conversions when viewBox is absent.
        if unit in ("", "px"):
            return max(1, int(round(value)))
        if unit == "pt":
            # CSS px per point at 96dpi: 1pt = 96/72 px.
            return max(1, int(round(value * (96.0 / 72.0))))
        # Units like ex/em depend on font metrics; don't guess.
        return None

    return None


def _style_img_tags(text: str) -> str:
    """
    Kindle's HTML/CSS support can ignore external stylesheet sizing rules.
    Add an inline style to <img> tags as a stronger hint to scale images to
    the viewport width.
    """

    def _inject_style(m: re.Match[str]) -> str:
        attrs = m.group(1)
        closing = m.group(2) or ""
        # Math images have their own sizing rules; don't force full-width.
        if re.search(r"\bclass=['\"][^'\"]*\bmath-(?:inline|display)\b", attrs, flags=re.IGNORECASE):
            return f"<img{attrs}{closing}>"
        if re.search(r"\bstyle=", attrs, flags=re.IGNORECASE):
            return f"<img{attrs}{closing}>"
        sep = "" if attrs.endswith((" ", "\n", "\t")) else " "
        # Force a white background behind images to avoid dark-mode engines
        # rendering transparent regions as black blocks.
        # Avoid forcing width:100% (it can create giant blank whitespace when
        # TeX4ht emits page-sized rasters).
        style = "style='max-width:100%;height:auto;background:#fff;'"
        return f"<img{attrs}{sep}{style}{closing}>"

    return re.sub(r"<img\b([^>]*?)(/?)>", _inject_style, text, flags=re.IGNORECASE)


MATHML_RE = re.compile(r"<math\b[^>]*>[\s\S]*?</math>", flags=re.IGNORECASE)

def _extract_tex4ht_label_ids(mathml: str) -> list[str]:
    """
    TeX4ht often encodes equation anchors inside MathML as:
      <mstyle class='label' id='x6-55001r1'></mstyle><!-- endlabel -->

    When we replace MathML with an <img>, those anchors disappear unless we
    promote them to a normal HTML anchor.
    """
    ids = re.findall(r"\bclass=['\"]label['\"][^>]*\bid=['\"]([^'\"]+)['\"]", mathml, flags=re.IGNORECASE)
    out: list[str] = []
    seen: set[str] = set()
    for ident in ids:
        if ident in seen:
            continue
        seen.add(ident)
        out.append(ident)
    return out

_TEX4HT_IMG_CAPTION_RE = re.compile(
    r"(?P<imgp><p\b[^>]*>\s*<img\b[^>]*>\s*(?:<a\b[^>]*>\s*</a>\s*)?</p>)\s*"
    r"(?P<cap><div\s+class=['\"]caption['\"][\s\S]*?</div>)"
    r"(?P<label>\s*<!--\s*tex4ht:label\?:[\s\S]*?-->\s*)?",
    flags=re.IGNORECASE,
)

def _wrap_tex4ht_img_captions(text: str) -> str:
    """
    TeX4ht commonly emits figures as:
      <p> <img .../> </p>
      <div class='caption'> ... </div>

    Many readers paginate between these blocks, causing "caption-only pages"
    with large blank space. Wrap them together so pagination keeps them as one
    unit.
    """

    def _repl(m: re.Match[str]) -> str:
        imgp = m.group("imgp")
        cap = m.group("cap")
        label = m.group("label") or ""
        return f"<div class='figure'>\n{imgp}\n{cap}{label}\n</div>"

    return _TEX4HT_IMG_CAPTION_RE.sub(_repl, text)

def _style_anchor_tags(text: str) -> str:
    """
    Some EPUB readers ignore CSS link-color overrides (especially in TOCs).
    Inject a minimal inline style so links remain uncolored (i.e., match body
    text color) while staying clickable.
    """

    def _inject_style(m: re.Match[str]) -> str:
        attrs = m.group(1)
        if re.search(r"\bstyle=", attrs, flags=re.IGNORECASE):
            return f"<a{attrs}>"
        sep = "" if attrs.endswith((" ", "\n", "\t")) else " "
        style = "style='color:inherit !important;text-decoration:none !important;'"
        return f"<a{attrs}{sep}{style}>"

    return re.sub(r"<a\b([^>]*?)>", _inject_style, text, flags=re.IGNORECASE)


def _run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def _escape_html_attr(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def _load_metadata(path: Path) -> dict[str, str]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    if not isinstance(raw, dict):
        return {}
    out: dict[str, str] = {}
    for k in ("title", "creator", "language", "identifier", "publisher", "rights"):
        v = raw.get(k)
        if isinstance(v, str) and v.strip():
            out[k] = v.strip()
    return out


def _replace_dc_tag(opf_text: str, tag: str, value: str) -> str:
    pat = re.compile(rf"(<dc:{re.escape(tag)}\b[^>]*>)([^<]*)(</dc:{re.escape(tag)}>)", re.IGNORECASE)
    return pat.sub(rf"\g<1>{value}\g<3>", opf_text, count=1)


def _replace_dc_identifier(opf_text: str, value: str) -> str:
    pat = re.compile(r"(<dc:identifier\b[^>]*>)([^<]*)(</dc:identifier>)", re.IGNORECASE)
    return pat.sub(rf"\g<1>{value}\g<3>", opf_text, count=1)


def _ensure_dc_tag(opf_text: str, tag: str, value: str) -> str:
    if re.search(rf"<dc:{re.escape(tag)}\b", opf_text, flags=re.IGNORECASE):
        return _replace_dc_tag(opf_text, tag, value)
    return re.sub(r"</metadata>", rf"  <dc:{tag}>{value}</dc:{tag}>\n</metadata>", opf_text, count=1, flags=re.IGNORECASE)


def _zip_epub(src_dir: Path, out_file: Path) -> None:
    # EPUB spec: `mimetype` must be first and stored (no compression).
    mimetype = src_dir / "mimetype"
    if not mimetype.exists():
        raise FileNotFoundError(f"Missing mimetype file in {src_dir}")

    out_file.parent.mkdir(parents=True, exist_ok=True)
    if out_file.exists():
        out_file.unlink()

    with zipfile.ZipFile(out_file, "w") as z:
        z.write(mimetype, "mimetype", compress_type=zipfile.ZIP_STORED)
        for path in sorted(src_dir.rglob("*")):
            if path == mimetype:
                continue
            if path.is_dir():
                continue
            rel = path.relative_to(src_dir).as_posix()
            z.write(path, rel, compress_type=zipfile.ZIP_DEFLATED)


def _trim_png(path: Path, pad: int = 8) -> None:
    """
    Trim transparent/white borders to make figures readable on small screens.

    TeX4ht can produce page-sized images with lots of whitespace; if we don't
    crop those margins, diagrams become too small in reflowable ebook viewers.
    """
    try:
        img = Image.open(path)
    except Exception:
        return

    # Many TeX4ht-rendered images have transparent margins. Kindle renderers can
    # display transparency as black (especially in dark mode), which makes
    # figures look like they have a black page background. Flatten onto white.
    try:
        if "A" in img.getbands():
            white = Image.new("RGBA", img.size, (255, 255, 255, 255))
            img = Image.alpha_composite(white, img.convert("RGBA")).convert("RGB")
        else:
            img = img.convert("RGB")
    except Exception:
        return

    # Prefer a "near-white" background trim. Many TeX4ht-rendered figures are
    # fully opaque (alpha=255 everywhere), so alpha-based bbox won't help.
    bbox = None
    try:
        gray = img.convert("L")

        # Anything close to white is treated as background. Keep the threshold
        # high; many figures use light pastel fills.
        white_threshold = 252
        mask = gray.point(lambda p: 255 if p < white_threshold else 0)

        # Drop a thin border strip before bbox detection; some renderers emit a
        # 1px page frame that prevents trimming.
        border = 8
        if mask.size[0] > 2 * border and mask.size[1] > 2 * border:
            inner = mask.crop((border, border, mask.size[0] - border, mask.size[1] - border))
            trimmed_mask = Image.new("L", mask.size, 0)
            trimmed_mask.paste(inner, (border, border))
            mask = trimmed_mask

        bbox = mask.getbbox()
    except Exception:
        bbox = None

    if bbox is None:
        return

    if not bbox:
        return

    left, upper, right, lower = bbox
    left = max(0, left - pad)
    upper = max(0, upper - pad)
    right = min(img.size[0], right + pad)
    lower = min(img.size[1], lower + pad)
    if right <= left or lower <= upper:
        return

    try:
        img.crop((left, upper, right, lower)).save(path)
    except Exception:
        return


def _flatten_png_alpha(path: Path) -> None:
    """
    Flatten RGBA/LA PNGs to RGB on a white background.

    Kindle (and some other readers) can display transparency as black,
    especially in dark mode, which makes otherwise-white figures look like
    they have black page backgrounds.
    """
    try:
        img = Image.open(path)
    except Exception:
        return

    try:
        if "A" not in img.getbands():
            return
        rgba = img.convert("RGBA")
        white = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        out = Image.alpha_composite(white, rgba).convert("RGB")
        out.save(path)
    except Exception:
        return


def _wrap_code_lines(text: str, max_cols: int = 92) -> str:
    """
    Wrap long code lines to keep rasterized blocks readable on small screens.
    This is a best-effort, display-only transformation for the Kindle EPUB.
    """
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.rstrip("\n\r")
        if len(line) <= max_cols:
            lines.append(line)
            continue
        # Preserve leading indentation for wrapped continuations.
        indent = len(line) - len(line.lstrip(" "))
        prefix = " " * indent
        rest = line.lstrip(" ")
        while len(prefix) + len(rest) > max_cols:
            take = max(12, max_cols - len(prefix))
            chunk = rest[:take]
            # Prefer breaking on a nearby space.
            cut = chunk.rfind(" ")
            if cut >= 8:
                chunk, rest = rest[:cut], rest[cut + 1 :]
            else:
                chunk, rest = rest[:take], rest[take:]
            lines.append(prefix + chunk)
            prefix = " " * (indent + 2)
            rest = rest.lstrip(" ")
        if rest:
            lines.append(prefix + rest)
    return "\n".join(lines).strip("\n") + "\n"


def _render_code_png(code: str, out_path: Path) -> None:
    """
    Render a <pre> block to a PNG image for Kindle. Kindle tends to hyphenate
    or clip preformatted text; rasterizing avoids that.
    """
    code = _normalize_pre_text(code)
    code = _wrap_code_lines(code)

    # Prefer a readable monospace font. PIL's default bitmap font is small and
    # produces blurry results after scaling on larger viewports.
    try:
        font_size = 22
        font_paths = [
            "/System/Library/Fonts/Menlo.ttc",
            "/System/Library/Fonts/Supplemental/Menlo.ttc",
            "/System/Library/Fonts/Courier New.ttf",
            "/Library/Fonts/Menlo.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        ]
        font = None
        for fp in font_paths:
            try:
                if Path(fp).exists():
                    font = ImageFont.truetype(fp, font_size)
                    break
            except Exception:
                continue
        if font is None:
            font = ImageFont.load_default()
    except Exception:
        return

    # Measure text.
    lines = code.splitlines() or [""]
    try:
        # PIL >= 8: use getbbox for accurate sizing.
        line_heights = []
        line_widths = []
        for ln in lines:
            bbox = font.getbbox(ln)
            line_widths.append(bbox[2] - bbox[0])
            line_heights.append(bbox[3] - bbox[1])
        line_height = max(line_heights) if line_heights else 14
        text_width = max(line_widths) if line_widths else 10
    except Exception:
        line_height = 14
        text_width = max(len(ln) for ln in lines) * 8

    pad_x, pad_y = 18, 14
    border = 2
    img_w = int(text_width + 2 * pad_x + 2 * border)
    img_h = int(len(lines) * (line_height + 2) + 2 * pad_y + 2 * border)

    # Cap width to keep memory bounded; wrap should have handled most cases.
    img_w = min(img_w, 2400)

    bg = (250, 250, 250)
    fg = (0, 0, 0)
    border_color = (210, 210, 210)

    img = Image.new("RGB", (img_w, img_h), bg)
    draw = ImageDraw.Draw(img)
    # Border rectangle.
    draw.rectangle((0, 0, img_w - 1, img_h - 1), outline=border_color, width=border)

    y = pad_y + border
    for ln in lines:
        draw.text((pad_x + border, y), ln, fill=fg, font=font)
        y += line_height + 2

    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        img.save(out_path)
    except Exception:
        return


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input EPUB")
    parser.add_argument("--output", required=True, help="Path to output EPUB")
    parser.add_argument("--metadata", default="", help="Optional JSON metadata file (title/creator/language/identifier).")
    parser.add_argument(
        "--cover",
        default="",
        help="Optional path to a cover image (PNG/JPG) to embed as the EPUB cover.",
    )
    parser.add_argument(
        "--stamp-identifier",
        action="store_true",
        help="Append a build timestamp to the package identifier (useful for Kindle Previewer cache-busting).",
    )
    parser.add_argument(
        "--png-width",
        type=int,
        default=2400,
        help="Target PNG width for converted SVGs",
    )
    parser.add_argument(
        "--inline-png-width",
        type=int,
        default=800,
        help="Target PNG width for rasterized inline MathML (keeps Kindle file size reasonable).",
    )
    parser.add_argument(
        "--pdf-dpi",
        type=int,
        default=300,
        help="DPI used when rasterizing PDF images to PNG",
    )
    args = parser.parse_args()

    input_epub = Path(args.input).resolve()
    output_epub = Path(args.output).resolve()
    if not input_epub.exists():
        raise FileNotFoundError(input_epub)

    metadata: dict[str, str] = {}
    if args.metadata:
        metadata_path = Path(args.metadata).expanduser().resolve()
        if metadata_path.exists():
            metadata = _load_metadata(metadata_path)

    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        raise RuntimeError("rsvg-convert not found on PATH (install via `brew install librsvg`).")

    gs = shutil.which("gs") or shutil.which("gswin64c") or shutil.which("gswin32c")
    if not gs:
        raise RuntimeError("Ghostscript not found on PATH (install via `brew install ghostscript`).")

    with tempfile.TemporaryDirectory(prefix="ece657_epub_kindle_") as tmp:
        tmp_dir = Path(tmp)
        with zipfile.ZipFile(input_epub) as z:
            z.extractall(tmp_dir)

        oebps = tmp_dir / "OEBPS"
        if not oebps.exists():
            raise FileNotFoundError(f"Missing OEBPS in extracted EPUB: {tmp_dir}")

        # 0) Optional cover page + metadata.
        cover_src = Path(args.cover).expanduser().resolve() if args.cover else None
        cover_href = "cover.png"
        cover_xhtml_href = "cover.xhtml"
        cover_image_id = "cover_image"
        cover_xhtml_id = "cover_xhtml"

        if cover_src and cover_src.exists():
            # Kindle and many EPUB readers are happiest with a simple PNG cover.
            # If the source is not PNG, convert it.
            cover_dst = oebps / cover_href
            try:
                if cover_src.suffix.lower() == ".png":
                    shutil.copyfile(cover_src, cover_dst)
                else:
                    img = Image.open(cover_src).convert("RGB")
                    img.save(cover_dst)
            except Exception:
                cover_src = None

        if cover_src and (oebps / cover_href).exists():
            cover_xhtml = oebps / cover_xhtml_href
            # Keep this minimal; Kindle post-processing will inject CSS and inline img sizing.
            cover_xhtml.write_text(
                "\n".join(
                    [
                        "<!DOCTYPE html>",
                        "<html lang='en-US' xmlns='http://www.w3.org/1999/xhtml'>",
                        "<head><title>Cover</title>",
                        "<meta charset='UTF-8' />",
                        "<link href='ece657_ebook.css' rel='stylesheet' type='text/css' />",
                        "</head><body>",
                        "<div class='cover'>",
                        f"<img src='{cover_href}' alt='Cover' />",
                        "</div>",
                        "</body></html>",
                        "",
                    ]
                ),
                encoding="utf-8",
            )

        # 0b) Kindle engines are inconsistent with MathML; rasterize all MathML
        # (inline + display) to PNG images for reliable equation rendering.
        xhtml_files = sorted(oebps.glob("*.xhtml"))
        math_entries: list[dict[str, object]] = []
        math_by_key: dict[str, dict[str, object]] = {}

        for xf in xhtml_files:
            text = xf.read_text(encoding="utf-8", errors="replace")
            for m in MATHML_RE.finditer(text):
                mathml = m.group(0)
                norm = _normalize_mathml(mathml)
                key = hashlib.md5(norm.encode("utf-8")).hexdigest()
                if key in math_by_key:
                    continue
                display = _is_display_math(mathml)
                math_id = f"math-{'display' if display else 'inline'}-{key[:12]}"
                math_by_key[key] = {"id": math_id, "display": display}
                math_entries.append({"id": math_id, "mathml": mathml, "display": display})

        if math_entries:
            svg_dir = tmp_dir / "mathml_svg"
            svg_dir.mkdir(parents=True, exist_ok=True)
            payload_path = tmp_dir / "mathml_all.json"
            payload_path.write_text(json.dumps(math_entries), encoding="utf-8")
            node_script = Path(__file__).resolve().parent / "mathml_batch_to_svg.js"
            subprocess.run(
                ["node", str(node_script), str(payload_path), str(svg_dir)],
                check=True,
            )

            math_dir = oebps / "math"
            math_dir.mkdir(parents=True, exist_ok=True)
            inline_width = min(args.inline_png_width, args.png_width)
            for entry in math_entries:
                math_id = str(entry["id"])
                display = bool(entry["display"])
                svg = svg_dir / f"{math_id}.svg"
                if not svg.exists():
                    continue
                png = math_dir / f"{math_id}.png"
                target_width = args.png_width if display else inline_width
                intrinsic = _svg_intrinsic_width_px(svg)
                # Avoid upscaling short equations to the target width.
                width = target_width
                if intrinsic is not None:
                    width = min(width, intrinsic)
                try:
                    _run([rsvg, "-a", "-w", str(width), "-o", str(png), str(svg)])
                except subprocess.CalledProcessError:
                    continue
                _trim_png(png, pad=6 if display else 4)
                _flatten_png_alpha(png)

        # 1) Convert SVG images to PNG.
        svg_files = sorted(oebps.rglob("*.svg"))
        svg_to_png: dict[str, str] = {}
        for svg in svg_files:
            png = svg.with_suffix(".png")
            # Preserve alpha and viewBox scaling.
            try:
                _run([rsvg, "-a", "-w", str(args.png_width), "-o", str(png), str(svg)])
            except subprocess.CalledProcessError as e:
                # If conversion fails, keep the SVG and skip rewriting references.
                continue
            _trim_png(png)
            svg_rel = svg.relative_to(oebps).as_posix()
            png_rel = png.relative_to(oebps).as_posix()
            svg_to_png[svg_rel] = png_rel

        # 1b) Convert PDF images to PNG (EPUB renderers typically don't support PDF).
        pdf_files = sorted(oebps.rglob("*.pdf"))
        pdf_to_png: dict[str, str] = {}
        for pdf in pdf_files:
            png = pdf.with_suffix(".png")
            # Render first page only (figures should be single-page PDFs).
            try:
                _run(
                    [
                        gs,
                        "-dSAFER",
                        "-dBATCH",
                        "-dNOPAUSE",
                        "-dFirstPage=1",
                        "-dLastPage=1",
                        "-sDEVICE=pngalpha",
                        f"-r{args.pdf_dpi}",
                        f"-sOutputFile={png}",
                        str(pdf),
                    ]
                )
            except subprocess.CalledProcessError:
                continue
            _trim_png(png)
            pdf_rel = pdf.relative_to(oebps).as_posix()
            png_rel = png.relative_to(oebps).as_posix()
            pdf_to_png[pdf_rel] = png_rel

        # 1c) Flatten any remaining RGBA PNGs (especially under OEBPS/assets/).
        for png in sorted(oebps.rglob("*.png")):
            _flatten_png_alpha(png)

        # 2) Add CSS overrides for Kindle readability.
        overrides_css = oebps / "kindle_overrides.css"
        overrides_css.write_text(
            "\n".join(
                [
                    "/* Kindle-targeted overrides for reflowable EPUB. */",
                    "html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }",
                    # Keep a safe default for figures, but do not override inline-math sizing.
                    "img { max-width: 100% !important; height: auto !important; }",
                    "img { background: #fff !important; }",
                    # Display math should never scale *up* (it can look comically large).
                    # Standardize display-math sizing across the book:
                    # - Fit to viewport width for consistency with figures
                    # - Cap height in ems so short equations don't dominate a page
                    # - Use object-fit to preserve aspect ratio when capped
                    # Display math: avoid forcing width=100% (some short equations get comically upsized).
                    # Keep a max-height cap for consistency, but let the intrinsic width decide scale.
                    # Make display-math sizing more consistent across the book by using a fixed
                    # height (with object-fit). This avoids large per-equation size swings.
                    "img.math-display { display: block !important; width: auto !important; max-width: 100% !important; height: 4.8em !important; object-fit: contain !important; margin: 0.6em auto !important; }",
                    # Global `img{height:auto!important}` would otherwise blow up inline-math PNGs
                    # (notably in the TOC/listings).
                    "img.math-inline { height: 1.1em !important; width: auto !important; vertical-align: middle !important; }",
                    # Do not force `width:100%` for figures; it can upscale and create large
                    # blank whitespace around TeX4ht rasters. Let max-width constrain instead.
                    # Standardize figure size: scale to the available width.
                    "figure img, .float img, div.figure img { width: 100% !important; max-width: 100% !important; display: block; margin: 0 auto; }",
                    "figure, .float { margin-left: 0; margin-right: 0; }",
                    "",
                    "/* Kindle reading surfaces are narrow; reclaim horizontal space. */",
                    # Reduce body font slightly to reclaim space for figures/equations.
                    "body { margin: 0 !important; padding: 0 0.5em !important; max-width: none !important; font-size: 0.96em !important; }",
                    "",
                    "/* Keep tcolorbox callouts within the viewport on Kindle. */",
                    ".tcolorbox, .tcolorbox-title, .tcolorbox-content {",
                    "  box-sizing: border-box;",
                    "  max-width: 100% !important;",
                    "}",
                    ".tcolorbox-title, .tcolorbox-content {",
                    "  overflow-wrap: anywhere;",
                    "  word-break: normal;",
                    "}",
                    ".tcolorbox-content {",
                    "  overflow-x: auto !important;",
                    "  overflow-y: visible !important;",
                    "  -webkit-overflow-scrolling: touch;",
                    "}",
                    # Callouts are narrower; keep equations readable but not oversized.
                    ".tcolorbox img.math-display { width: auto !important; max-width: 100% !important; height: 4.2em !important; object-fit: contain !important; }",
                    "",
                    "/* Keep figure images + captions together under pagination. */",
                    "div.figure {",
                    "  break-inside: avoid !important;",
                    "  page-break-inside: avoid !important;",
                    "  margin: 0.75em 0 !important;",
                    "}",
                    "div.figure img {",
                    "  display: block;",
                    "  margin: 0 auto;",
                    "}",
                    "div.figure .caption {",
                    "  margin-top: 0.5em;",
                    "}",
                    "",
                    "/* MathML can overflow narrow screens; allow horizontal scrolling instead of clipping. */",
                    "div.math-display, div.par-math-display, table.equation, table.equation-star {",
                    "  overflow-x: auto !important;",
                    "  overflow-y: hidden !important;",
                    "  -webkit-overflow-scrolling: touch;",
                    "}",
                    "table.equation { display: block !important; max-width: 100% !important; }",
                    "table.equation-star { display: block !important; max-width: 100% !important; }",
                    ".equation td { white-space: nowrap; }",
                    "math { max-width: 100%; }",
                    "math[display='block'] { display: block; }",
                    "",
                    "/* Keep internal/external links black (but still clickable). */",
                    "a, a:link, a:visited, a:hover, a:active {",
                    "  color: inherit !important;",
                    "  text-decoration: none !important;",
                    "}",
                    "",
                    "/* Kindle engines have spotty CSS grid support; avoid clipped enumerate layouts. */",
                    "dl.enumerate-enumitem { display: block !important; }",
                    "dl.enumerate-enumitem > dt { float: left; width: 3ch; }",
                    "dl.enumerate-enumitem > dd { margin-left: 3ch; }",
                    "dl.enumerate-enumitem::after { content: ''; display: block; clear: both; }",
                    "pre, pre.verbatim {",
                    "  white-space: pre-wrap !important;",
                    "  overflow-wrap: anywhere !important;",
                    "  word-break: normal !important;",
                    "  hyphens: none !important;",
                    "  -webkit-hyphens: none !important;",
                    "  font-family: monospace !important;",
                    "  font-size: 0.82em;",
                    "  line-height: 1.2;",
                    "}",
                    "code { font-size: 0.95em; }",
                    "",
                ]
            ),
            encoding="utf-8",
        )

        # 3) Rewrite XHTML to (a) link the override CSS, (b) remove hard-coded
        # width/height on external images, and (c) swap SVG src -> PNG src.
        xhtml_files = sorted(oebps.glob("*.xhtml"))
        head_link = "<link rel='stylesheet' type='text/css' href='kindle_overrides.css' />"
        for xf in xhtml_files:
            text = xf.read_text(encoding="utf-8", errors="replace")

            if "kindle_overrides.css" not in text:
                # Insert before closing head.
                text = re.sub(r"</head>", head_link + "\n</head>", text, count=1, flags=re.IGNORECASE)

            # Rasterize code listings for Kindle (prevents clipping/hyphenation).
            code_images_dir = oebps / "code"
            pre_index = 0

            def _fix_pre(m: re.Match[str]) -> str:
                nonlocal pre_index
                open_tag, inner, close_tag = m.group(1), m.group(2), m.group(3)
                pre_index += 1

                id_match = re.search(r"\bid='([^']+)'", open_tag, flags=re.IGNORECASE)
                pre_id = id_match.group(1) if id_match else f"verbatim-auto-{pre_index}"
                img_name = f"code_{pre_id}.png"
                img_rel = f"code/{img_name}"

                # Render and save.
                _render_code_png(inner, code_images_dir / img_name)

                # Preserve the original anchor id for internal links.
                return (
                    f"<p class='codeblock' id='{pre_id}'>"
                    f"<img class='codeblock' src='{img_rel}' alt='Code listing' />"
                    f"</p>"
                )

            text = re.sub(
                r"(<pre\b[^>]*>)([\s\S]*?)(</pre>)",
                _fix_pre,
                text,
                flags=re.IGNORECASE,
            )

            def _replace_mathml(m: re.Match[str]) -> str:
                mathml = m.group(0)
                norm = _normalize_mathml(mathml)
                key = hashlib.md5(norm.encode("utf-8")).hexdigest()
                info = math_by_key.get(key)
                if not info:
                    return mathml
                math_id = str(info["id"])
                display = bool(info["display"])
                src = f"math/{math_id}.png"
                alt = _escape_html_attr(_mathml_to_alt(mathml))
                anchors = "".join(f"<a id='{_escape_html_attr(i)}'></a>" for i in _extract_tex4ht_label_ids(mathml))
                if display:
                    return (
                        anchors
                        + f"<img class='math-display' src='{src}' alt=\"{alt}\" "
                        + "style='height:auto;max-width:100%;background:#fff;'/>"
                    )
                return (
                    anchors
                    + f"<img class='math-inline' src='{src}' alt=\"{alt}\" "
                    + "style='height:1.1em;width:auto;vertical-align:middle;background:#fff;'/>"
                )

            if math_by_key:
                text = MATHML_RE.sub(_replace_mathml, text)

            # EPUBCheck (EPUB 3.3 rules) is stricter about HTML5 semantics than
            # typical ebook readers. TeX4ht emits `figure/figcaption` wrappers
            # around some `tabular` output; convert these to plain `div`s.
            text = re.sub(r"<\s*figure\b", "<div", text, flags=re.IGNORECASE)
            text = re.sub(r"</\s*figure\s*>", "</div>", text, flags=re.IGNORECASE)
            text = re.sub(r"<\s*figcaption\b", "<div", text, flags=re.IGNORECASE)
            text = re.sub(r"</\s*figcaption\s*>", "</div>", text, flags=re.IGNORECASE)

            # Remove obsolete/invalid table attributes that trip EPUBCheck.
            text = re.sub(r"\s+rules=(['\"]).*?\1", "", text, flags=re.IGNORECASE)

            # Remove fixed dimensions on images (prevents tiny thumbnails and enables reflow).
            text = re.sub(
                r"(<img\b[^>]*?)\s+width='\d+'\s+height='\d+'([^>]*>)",
                r"\1\2",
                text,
            )

            # Keep image+caption together (avoid caption-only pages).
            text = _wrap_tex4ht_img_captions(text)

            # Stronger sizing hint for Kindle engines: add inline width style.
            text = _style_img_tags(text)
            text = _style_anchor_tags(text)

            for svg_rel, png_rel in svg_to_png.items():
                text = text.replace(f"'{svg_rel}'", f"'{png_rel}'")
                text = text.replace(f'\"{svg_rel}\"', f'\"{png_rel}\"')

            for pdf_rel, png_rel in pdf_to_png.items():
                text = text.replace(f"'{pdf_rel}'", f"'{png_rel}'")
                text = text.replace(f'\"{pdf_rel}\"', f'\"{png_rel}\"')

            xf.write_text(text, encoding="utf-8")

        # 4) Update OPF manifest to include kindle_overrides.css and to swap SVG -> PNG.
        opf = oebps / "content.opf"
        if opf.exists():
            opf_text = opf.read_text(encoding="utf-8", errors="replace")

            if metadata:
                if "title" in metadata:
                    opf_text = _replace_dc_tag(opf_text, "title", metadata["title"])
                if "creator" in metadata:
                    opf_text = _replace_dc_tag(opf_text, "creator", metadata["creator"])
                if "language" in metadata:
                    opf_text = _replace_dc_tag(opf_text, "language", metadata["language"])
                if "identifier" in metadata:
                    opf_text = _replace_dc_identifier(opf_text, metadata["identifier"])
                if "publisher" in metadata:
                    opf_text = _ensure_dc_tag(opf_text, "publisher", metadata["publisher"])
                if "rights" in metadata:
                    opf_text = _ensure_dc_tag(opf_text, "rights", metadata["rights"])

            # Kindle target: we remove MathML from XHTML, so any `properties="mathml"`
            # markers in the OPF must be removed.
            opf_text = re.sub(
                r"(\bproperties=(['\"]))(.*?)(\2)",
                lambda m: (
                    f"{m.group(1)}"
                    + " ".join([t for t in m.group(3).split() if t.lower() != "mathml"])
                    + f"{m.group(4)}"
                ),
                opf_text,
                flags=re.IGNORECASE | re.DOTALL,
            )
            # If we removed the only token, drop the attribute entirely.
            opf_text = re.sub(r"\s+properties=(['\"])\s*\1", "", opf_text, flags=re.IGNORECASE)

            if args.stamp_identifier:
                # Kindle Previewer and some Kindle engines cache by package identifier.
                # Stamp a build id so re-importing the EPUB refreshes.
                build_id = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
                opf_text = re.sub(
                    r"(<dc:identifier\b[^>]*>)([^<]*)(</dc:identifier>)",
                    lambda m: f"{m.group(1)}{m.group(2).strip()}-{build_id}{m.group(3)}",
                    opf_text,
                    count=1,
                    flags=re.IGNORECASE,
                )
            # Add overrides CSS if missing.
            if "kindle_overrides.css" not in opf_text:
                opf_text = opf_text.replace(
                    "</manifest>",
                    "  <item href='kindle_overrides.css' id='kindle_overrides_css' media-type='text/css'></item>\n</manifest>",
                )

            # Add cover image + cover.xhtml to the manifest/spine (if present).
            if (oebps / cover_href).exists() and (oebps / cover_xhtml_href).exists():
                if cover_href not in opf_text:
                    opf_text = opf_text.replace(
                        "</manifest>",
                        (
                            f"  <item href='{cover_xhtml_href}' id='{cover_xhtml_id}' media-type='application/xhtml+xml'></item>\n"
                            f"  <item href='{cover_href}' id='{cover_image_id}' media-type='image/png' properties='cover-image'></item>\n"
                            "</manifest>"
                        ),
                    )
                # EPUB2-style cover hint (still used by some readers/KDP ingestion).
                if re.search(r"<meta\s+name='cover'", opf_text, flags=re.IGNORECASE) is None:
                    opf_text = re.sub(
                        r"</metadata>",
                        f"  <meta name='cover' content='{cover_image_id}' />\n</metadata>",
                        opf_text,
                        count=1,
                        flags=re.IGNORECASE,
                    )
                # Ensure cover.xhtml is the first spine item.
                if f"idref='{cover_xhtml_id}'" not in opf_text:
                    opf_text = re.sub(
                        r"(<spine\b[^>]*>)",
                        r"\1\n" + f"<itemref idref='{cover_xhtml_id}'></itemref>",
                        opf_text,
                        count=1,
                        flags=re.IGNORECASE,
                    )

            for svg_rel, png_rel in svg_to_png.items():
                opf_text = opf_text.replace(f"href='{svg_rel}'", f"href='{png_rel}'")
                opf_text = opf_text.replace("media-type='image/svg+xml'", "media-type='image/png'")
            for pdf_rel, png_rel in pdf_to_png.items():
                opf_text = opf_text.replace(f"href='{pdf_rel}'", f"href='{png_rel}'")
                opf_text = opf_text.replace("media-type='application/pdf'", "media-type='image/png'")

            # Add rasterized code images to the manifest if present.
            code_imgs = sorted((oebps / "code").glob("*.png")) if (oebps / "code").exists() else []
            if code_imgs and "</manifest>" in opf_text:
                inserts: list[str] = []
                for p in code_imgs:
                    href = p.relative_to(oebps).as_posix()
                    item_id = re.sub(r"[^a-zA-Z0-9_]+", "_", href)
                    if href in opf_text:
                        continue
                    inserts.append(
                        f"  <item href='{href}' id='{item_id}' media-type='image/png'></item>"
                    )
                if inserts:
                    opf_text = opf_text.replace("</manifest>", "\n".join(inserts) + "\n</manifest>")

            # Add rasterized math images to the manifest if present.
            math_imgs = sorted((oebps / "math").glob("*.png")) if (oebps / "math").exists() else []
            if math_imgs and "</manifest>" in opf_text:
                inserts = []
                for p in math_imgs:
                    href = p.relative_to(oebps).as_posix()
                    item_id = re.sub(r"[^a-zA-Z0-9_]+", "_", href)
                    if href in opf_text:
                        continue
                    inserts.append(f"  <item href='{href}' id='{item_id}' media-type='image/png'></item>")
                if inserts:
                    opf_text = opf_text.replace("</manifest>", "\n".join(inserts) + "\n</manifest>")
            opf.write_text(opf_text, encoding="utf-8")

            # Keep the legacy NCX (dtb:uid) in sync with the OPF identifier.
            m = re.search(r"<dc:identifier\b[^>]*>([^<]+)</dc:identifier>", opf_text, flags=re.IGNORECASE)
            opf_identifier = m.group(1).strip() if m else ""
            if opf_identifier:
                for ncx in oebps.glob("*.ncx"):
                    ncx_text = ncx.read_text(encoding="utf-8", errors="replace")
                    ncx_text = re.sub(
                        r"<meta\b[^>]*\bname=['\"]dtb:uid['\"][^>]*\/?>",
                        lambda mm: re.sub(r"content=(['\"]).*?\1", f"content='{opf_identifier}'", mm.group(0)),
                        ncx_text,
                        flags=re.IGNORECASE,
                    )
                    ncx.write_text(ncx_text, encoding="utf-8")

        # 5) Remove SVG files that were successfully converted.
        for svg_rel in svg_to_png:
            (oebps / svg_rel).unlink(missing_ok=True)

        # 6) Remove PDF files that were successfully converted.
        for pdf_rel in pdf_to_png:
            (oebps / pdf_rel).unlink(missing_ok=True)

        _zip_epub(tmp_dir, output_epub)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
