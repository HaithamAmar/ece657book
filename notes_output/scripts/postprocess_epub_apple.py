#!/usr/bin/env python3
"""
Post-process a TeX4ht/tex4ebook-generated EPUB for Apple Books.

Goals:
- Keep inline MathML (searchable, selectable).
- Convert display math to SVG for reliable Apple Books rendering.
- Add lightweight CSS overrides for image scaling and link styling.
- Avoid touching LaTeX sources (single source of truth stays in .tex files).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import unicodedata
import zipfile
from pathlib import Path

from PIL import Image

DISPLAY_MATH_RE = re.compile(
    r"<math\b[^>]*display=[\"']block[\"'][^>]*>.*?</math>",
    re.IGNORECASE | re.DOTALL,
)

def _canonicalize_display_math_for_key(mathml: str) -> str:
    """
    Return a canonicalized MathML string used for stable hashing.

    We strip attributes that we later remove from XHTML to satisfy EPUBCheck.
    If we don't, the keys computed during the initial scan (pre-strip) won't
    match keys computed during replacement (post-strip), causing display math
    to remain as MathML even when the SVG assets exist.
    """

    out = mathml
    out = re.sub(r"\s+stretchy=(['\"]).*?\1", "", out, flags=re.IGNORECASE)
    out = re.sub(r"\s+rowlines=(['\"]).*?\1", "", out, flags=re.IGNORECASE)
    return _normalize_mathml(out)


def _style_img_tags(text: str) -> str:
    """
    Apple Books can ignore some external stylesheet sizing rules.
    Add an inline style to <img> tags as a stronger hint to scale images.
    """

    def _inject_style(m: re.Match[str]) -> str:
        attrs = m.group(1)
        closing = m.group(2) or ""
        # Don't stomp existing inline styles.
        if re.search(r"\bstyle=", attrs, flags=re.IGNORECASE):
            return f"<img{attrs}{closing}>"
        sep = "" if attrs.endswith((" ", "\n", "\t")) else " "
        # Avoid forcing width:100%. It can massively upscale small diagrams and
        # short display-math SVGs (e.g., inside tcolorboxes), which looks bad in
        # EPUB readers. Use max-width instead and let intrinsic sizing win.
        if re.search(r"\bclass=['\"][^'\"]*\bmath-display\b", attrs, flags=re.IGNORECASE):
            style = "style='height:auto;max-width:100%;background:#fff;'"
        else:
            style = "style='max-width:100%;height:auto;background:#fff;'"
        return f"<img{attrs}{sep}{style}{closing}>"

    return re.sub(r"<img\b([^>]*?)(/?)>", _inject_style, text, flags=re.IGNORECASE)


def _style_anchor_tags(text: str) -> str:
    """
    Keep link styling neutral (black, no underline) while preserving clickability.
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

_TEX4HT_IMG_CAPTION_RE = re.compile(
    r"(?P<imgp><p\b[^>]*>\s*<img\b[^>]*>\s*(?:<a\b[^>]*>\s*</a>\s*)?</p>)\s*"
    r"(?P<cap><div\s+class=['\"]caption['\"][\s\S]*?</div>)"
    r"(?P<label>\s*<!--\s*tex4ht:label\?:[\s\S]*?-->\s*)?",
    flags=re.IGNORECASE,
)

def _wrap_tex4ht_img_captions(text: str) -> str:
    """
    TeX4ht often emits figures as a standalone <p><img/></p> followed by a
    sibling <div class='caption'>. Many paginated readers split these across
    pages. Wrap them into a single block to keep the caption attached.
    """

    def _repl(m: re.Match[str]) -> str:
        imgp = m.group("imgp")
        cap = m.group("cap")
        label = m.group("label") or ""
        return f"<div class='figure'>\n{imgp}\n{cap}{label}\n</div>"

    return _TEX4HT_IMG_CAPTION_RE.sub(_repl, text)


def _trim_png(path: Path, pad: int = 8) -> None:
    try:
        img = Image.open(path)
    except Exception:
        return

    try:
        if "A" in img.getbands():
            white = Image.new("RGBA", img.size, (255, 255, 255, 255))
            img = Image.alpha_composite(white, img.convert("RGBA")).convert("RGB")
        else:
            img = img.convert("RGB")
    except Exception:
        return

    bbox = None
    try:
        gray = img.convert("L")
        white_threshold = 252
        mask = gray.point(lambda p: 255 if p < white_threshold else 0)
        mask = mask.crop((2, 2, mask.size[0] - 2, mask.size[1] - 2))
        bbox = mask.getbbox()
    except Exception:
        bbox = None

    if not bbox:
        return

    left, upper, right, lower = bbox
    left = max(0, left - pad)
    upper = max(0, upper - pad)
    right = min(img.size[0], right + pad)
    lower = min(img.size[1], lower + pad)
    try:
        img.crop((left, upper, right, lower)).save(path)
    except Exception:
        return


def _flatten_png_alpha(path: Path) -> None:
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


def _normalize_mathml_glyphs(mathml: str) -> str:
    # Prefer MathML attributes + plain ASCII/Greek letters over Unicode
    # "mathematical alphanumeric symbols" which can render as tofu on some
    # ebook fonts/readers.
    double_struck = {
        "ℝ": "R",
        "ℕ": "N",
        "ℤ": "Z",
        "ℚ": "Q",
        "ℂ": "C",
        "ℙ": "P",
    }
    for sym, base in double_struck.items():
        mathml = re.sub(
            rf"<mi>{re.escape(sym)}</mi>",
            f"<mi mathvariant='double-struck'>{base}</mi>",
            mathml,
        )

    out_chars: list[str] = []
    for ch in mathml:
        cp = ord(ch)
        if 0x1D400 <= cp <= 0x1D7FF:
            out_chars.append(unicodedata.normalize("NFKD", ch))
        else:
            out_chars.append(ch)
    return "".join(out_chars)


MATHML_BLOCK_RE = re.compile(r"<math\b[^>]*>[\s\S]*?</math>", flags=re.IGNORECASE)

def _extract_tex4ht_label_ids(mathml: str) -> list[str]:
    ids = re.findall(r"\bclass=['\"]label['\"][^>]*\bid=['\"]([^'\"]+)['\"]", mathml, flags=re.IGNORECASE)
    out: list[str] = []
    seen: set[str] = set()
    for ident in ids:
        if ident in seen:
            continue
        seen.add(ident)
        out.append(ident)
    return out


def _normalize_pre_blocks(text: str) -> str:
    def _fix(m: re.Match[str]) -> str:
        open_tag, inner, close_tag = m.group(1), m.group(2), m.group(3)
        inner = (
            inner.replace("\u00a0", " ")
            .replace("\u00ad", "")
            .replace("\u200b", "")
            .replace("\ufeff", "")
        )
        return f"{open_tag}{inner}{close_tag}"

    return re.sub(r"(<pre\b[^>]*>)([\s\S]*?)(</pre>)", _fix, text, flags=re.IGNORECASE)


def _zip_epub(src_dir: Path, out_file: Path) -> None:
    mimetype = src_dir / "mimetype"
    if not mimetype.exists():
        raise FileNotFoundError(f"Missing mimetype file in {src_dir}")

    out_file.parent.mkdir(parents=True, exist_ok=True)
    if out_file.exists():
        out_file.unlink()

    with zipfile.ZipFile(out_file, "w") as z:
        z.write(mimetype, "mimetype", compress_type=zipfile.ZIP_STORED)
        for path in sorted(src_dir.rglob("*")):
            if path == mimetype or path.is_dir():
                continue
            rel = path.relative_to(src_dir).as_posix()
            z.write(path, rel, compress_type=zipfile.ZIP_DEFLATED)


def _find_content_root(root: Path) -> Path:
    oebps = root / "OEBPS"
    if oebps.exists():
        return oebps
    candidates = list(root.rglob("OEBPS"))
    if len(candidates) == 1:
        return candidates[0]
    return root


def _find_opf(root: Path) -> Path:
    candidates = list(root.rglob("*.opf"))
    if len(candidates) == 1:
        return candidates[0]
    if candidates:
        return candidates[0]
    raise FileNotFoundError("Could not locate OPF package file in extracted EPUB.")


def _normalize_mathml(mathml: str) -> str:
    return re.sub(r"\s+", " ", mathml).strip()


def _mathml_to_alt(mathml: str) -> str:
    text = re.sub(r"<[^>]+>", " ", mathml)
    text = re.sub(r"\s+", " ", text).strip()
    return text if text else "Math equation"


def _update_opf_manifest(opf_path: Path, svg_paths: list[Path]) -> None:
    if not svg_paths:
        return
    opf_text = opf_path.read_text(encoding="utf-8", errors="replace")
    if "</manifest>" not in opf_text:
        return
    items = []
    for svg_path in svg_paths:
        href = svg_path.relative_to(opf_path.parent).as_posix()
        if href in opf_text:
            continue
        item_id = f"math-{svg_path.stem}"
        items.append(f"  <item id=\"{item_id}\" href=\"{href}\" media-type=\"image/svg+xml\"/>")
    if not items:
        return
    opf_text = opf_text.replace("</manifest>", "\n".join(items) + "\n</manifest>", 1)
    opf_path.write_text(opf_text, encoding="utf-8")


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


def _apply_metadata(opf_path: Path, metadata: dict[str, str]) -> None:
    if not metadata:
        return
    opf_text = opf_path.read_text(encoding="utf-8", errors="replace")
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
    opf_path.write_text(opf_text, encoding="utf-8")


def _embed_cover(opf_path: Path, content_root: Path, cover_src: Path) -> None:
    cover_href = "cover.png"
    cover_xhtml_href = "cover.xhtml"
    cover_image_id = "cover_image"
    cover_xhtml_id = "cover_xhtml"

    cover_dst = content_root / cover_href
    try:
        if cover_src.suffix.lower() == ".png":
            shutil.copyfile(cover_src, cover_dst)
        else:
            img = Image.open(cover_src).convert("RGB")
            img.save(cover_dst)
    except Exception:
        return

    cover_xhtml = content_root / cover_xhtml_href
    cover_xhtml.write_text(
        "\n".join(
            [
                "<!DOCTYPE html>",
                "<html lang='en-US' xmlns='http://www.w3.org/1999/xhtml'>",
                "<head><title>Cover</title>",
                "<meta charset='UTF-8' />",
                "<link href='ece657_ebook.css' rel='stylesheet' type='text/css' />",
                "<link href='apple_overrides.css' rel='stylesheet' type='text/css' />",
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

    opf_text = opf_path.read_text(encoding="utf-8", errors="replace")

    if re.search(r"<meta\\s+name=['\"]cover['\"]", opf_text, flags=re.IGNORECASE) is None:
        opf_text = re.sub(
            r"</metadata>",
            f"  <meta name='cover' content='{cover_image_id}' />\n</metadata>",
            opf_text,
            count=1,
            flags=re.IGNORECASE,
        )

    if cover_href not in opf_text:
        opf_text = opf_text.replace(
            "</manifest>",
            (
                f"  <item href='{cover_xhtml_href}' id='{cover_xhtml_id}' media-type='application/xhtml+xml'></item>\n"
                f"  <item href='{cover_href}' id='{cover_image_id}' media-type='image/png' properties='cover-image'></item>\n"
                "</manifest>"
            ),
            1,
        )

    if f"idref='{cover_xhtml_id}'" not in opf_text:
        opf_text = re.sub(
            r"(<spine\\b[^>]*>)",
            r"\1\n" + f"<itemref idref='{cover_xhtml_id}'></itemref>",
            opf_text,
            count=1,
            flags=re.IGNORECASE,
        )

    opf_path.write_text(opf_text, encoding="utf-8")

def _sync_opf_mathml_properties(opf_path: Path, mathml_hrefs: set[str]) -> None:
    opf_text = opf_path.read_text(encoding="utf-8", errors="replace")

    def _fix_item(m: re.Match[str]) -> str:
        tag = m.group(0)
        href_m = re.search(r"\bhref=(['\"])(.*?)\1", tag, flags=re.IGNORECASE)
        if not href_m:
            return tag
        href = href_m.group(2)
        if not href.lower().endswith(".xhtml"):
            return tag

        should_have_mathml = href in mathml_hrefs
        prop_m = re.search(r"\bproperties=(['\"])(.*?)\1", tag, flags=re.IGNORECASE)
        tokens: list[str] = []
        if prop_m:
            tokens = [t for t in prop_m.group(2).split() if t]
        tokens = [t for t in tokens if t.lower() != "mathml"]
        if should_have_mathml:
            tokens.append("mathml")

        if prop_m:
            if tokens:
                new_val = " ".join(tokens)
                return re.sub(r"\bproperties=(['\"])(.*?)\1", f"properties='{new_val}'", tag, count=1, flags=re.IGNORECASE)
            return re.sub(r"\s+properties=(['\"])(.*?)\1", "", tag, count=1, flags=re.IGNORECASE)

        if not tokens:
            return tag
        # Insert properties just before the tag close.
        if tag.endswith("/>"):
            return tag[:-2] + f" properties='{' '.join(tokens)}'/>"
        if tag.endswith(">"):
            return tag[:-1] + f" properties='{' '.join(tokens)}'>"
        return tag

    opf_text = re.sub(r"<item\b[^>]*?>", _fix_item, opf_text, flags=re.IGNORECASE)
    opf_path.write_text(opf_text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input EPUB")
    parser.add_argument("--output", required=True, help="Path to output EPUB")
    parser.add_argument("--metadata", default="", help="Optional JSON metadata file (title/creator/language/identifier).")
    parser.add_argument("--cover", default="", help="Optional cover image (PNG/JPG) to embed as cover.xhtml+cover.png.")
    args = parser.parse_args()

    input_epub = Path(args.input).resolve()
    output_epub = Path(args.output).resolve()
    if not input_epub.exists():
        raise FileNotFoundError(f"Input EPUB not found: {input_epub}")

    metadata: dict[str, str] = {}
    if args.metadata:
        metadata_path = Path(args.metadata).expanduser().resolve()
        if metadata_path.exists():
            metadata = _load_metadata(metadata_path)

    with tempfile.TemporaryDirectory(prefix="ece657_epub_apple_") as tmp:
        tmp_dir = Path(tmp)
        with zipfile.ZipFile(input_epub) as z:
            z.extractall(tmp_dir)

        content_root = _find_content_root(tmp_dir)
        opf_path = _find_opf(tmp_dir)

        if metadata:
            _apply_metadata(opf_path, metadata)

        if args.cover:
            cover_src = Path(args.cover).expanduser().resolve()
            if cover_src.exists():
                _embed_cover(opf_path, content_root, cover_src)

        overrides_css = content_root / "apple_overrides.css"
        overrides_css.write_text(
            "\n".join(
                [
                    "/* Apple Books overrides for reflowable EPUB. */",
                    "html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }",
                    "img { max-width: 100% !important; height: auto !important; }",
                    "img { background: #fff !important; }",
                    # Avoid forcing display math or figures to stretch to full width. That can
                    # Standardize display-math sizing across the book:
                    # - Fit to viewport width for consistency with figures
                    # - Cap height in ems so short equations don't dominate a page
                    # - Use object-fit to preserve aspect ratio when capped
                    # Display math: avoid forcing width=100% (some short equations get comically upsized).
                    # Keep a max-height cap for consistency, but let the intrinsic width decide scale.
                    # Make display-math sizing more consistent across the book by using a fixed
                    # height (with object-fit). This avoids large per-equation size swings.
                    "img.math-display { display: block !important; width: auto !important; max-width: 100% !important; height: 4.8em !important; object-fit: contain !important; margin: 0.6em auto !important; }",
                    # Slightly favor larger figure rendering on mobile screens.
                    "figure img, .float img, div.figure img { width: 100% !important; max-width: 100% !important; display: block; margin: 0 auto; }",
                    "figure, .float { margin-left: 0; margin-right: 0; }",
                    "",
                    # Reduce body font slightly to reclaim space for figures/equations.
                    "body { margin: 0 !important; padding: 0 0.5em !important; max-width: none !important; font-size: 0.96em !important; }",
                    "",
                    "/* Keep tcolorbox callouts within the viewport on Apple Books. */",
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
                    "/* Allow long MathML to scroll instead of clipping. */",
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
                    "/* Apple Books has uneven CSS grid support; avoid clipped enumerate layouts. */",
                    "dl.enumerate-enumitem { display: block !important; }",
                    "dl.enumerate-enumitem > dt { float: left; width: 3ch; }",
                    "dl.enumerate-enumitem > dd { margin-left: 3ch; }",
                    "dl.enumerate-enumitem::after { content: ''; display: block; clear: both; }",
                    "",
                    "/* Keep internal/external links black (but still clickable). */",
                    "a, a:link, a:visited, a:hover, a:active {",
                    "  color: inherit !important;",
                    "  text-decoration: none !important;",
                    "}",
                    "",
                ]
            ),
            encoding="utf-8",
        )

        # Ensure the Apple overrides stylesheet is declared in the OPF manifest
        # (EPUBCheck requires all referenced resources to be manifest items).
        opf_text = opf_path.read_text(encoding="utf-8", errors="replace")
        if "apple_overrides.css" not in opf_text:
            opf_text = opf_text.replace(
                "</manifest>",
                "  <item href='apple_overrides.css' id='apple_overrides_css' media-type='text/css'></item>\n</manifest>",
                1,
            )
            opf_path.write_text(opf_text, encoding="utf-8")

        head_link = "<link rel='stylesheet' type='text/css' href='apple_overrides.css' />"
        xhtml_files = sorted(content_root.glob("*.xhtml"))

        mathml_hrefs: set[str] = set()

        display_math_entries: list[dict[str, str]] = []
        display_math_map: dict[str, str] = {}
        for xf in xhtml_files:
            text = xf.read_text(encoding="utf-8", errors="replace")
            for match in DISPLAY_MATH_RE.finditer(text):
                mathml = match.group(0)
                canon = _canonicalize_display_math_for_key(mathml)
                key = hashlib.md5(canon.encode("utf-8")).hexdigest()
                if key in display_math_map:
                    continue
                math_id = f"math-display-{key[:12]}"
                display_math_map[key] = math_id
                # Pass the canonicalized MathML to MathJax to avoid relying on
                # attributes we strip later for EPUBCheck compliance.
                display_math_entries.append({"id": math_id, "mathml": canon})

        svg_dir = content_root / "math-display"
        svg_paths: list[Path] = []
        svg_ids: set[str] = set()
        if display_math_entries:
            svg_dir.mkdir(parents=True, exist_ok=True)
            payload_path = tmp_dir / "mathml_display.json"
            payload_path.write_text(json.dumps(display_math_entries), encoding="utf-8")
            node_script = Path(__file__).resolve().parent / "mathml_batch_to_svg.js"
            subprocess.run(
                ["node", str(node_script), str(payload_path), str(svg_dir)],
                check=True,
            )
            svg_paths = [svg_dir / f"{entry['id']}.svg" for entry in display_math_entries]
            svg_ids = {p.stem for p in svg_paths if p.exists()}
            failures_path = svg_dir / "_mathml_failures.json"
            if failures_path.exists():
                failures_path.unlink()

        # Apple Books can render SVG, but TeX4ht SVG figures sometimes have huge
        # whitespace/bounding boxes that make them appear tiny in reflow. For
        # predictable sizing, rasterize non-math SVG figures to trimmed PNG.
        rsvg = shutil.which("rsvg-convert")
        svg_to_png: dict[str, str] = {}
        if rsvg:
            for svg in sorted(content_root.rglob("*.svg")):
                if "math-display" in svg.parts:
                    continue
                png = svg.with_suffix(".png")
                try:
                    _run([rsvg, "-a", "-w", "2400", "-o", str(png), str(svg)])
                except subprocess.CalledProcessError:
                    continue
                _trim_png(png)
                _flatten_png_alpha(png)
                svg_to_png[svg.relative_to(content_root).as_posix()] = png.relative_to(content_root).as_posix()

        for xf in xhtml_files:
            text = xf.read_text(encoding="utf-8", errors="replace")

            if "apple_overrides.css" not in text:
                text = re.sub(r"</head>", head_link + "\n</head>", text, count=1, flags=re.IGNORECASE)

            # EPUBCheck (EPUB 3.3 rules) is stricter about HTML5 semantics than
            # typical ebook readers. TeX4ht emits `figure/figcaption` wrappers
            # around some `tabular` output; convert these to plain `div`s.
            text = re.sub(r"<\s*figure\b", "<div", text, flags=re.IGNORECASE)
            text = re.sub(r"</\s*figure\s*>", "</div>", text, flags=re.IGNORECASE)
            text = re.sub(r"<\s*figcaption\b", "<div", text, flags=re.IGNORECASE)
            text = re.sub(r"</\s*figcaption\s*>", "</div>", text, flags=re.IGNORECASE)

            # Remove obsolete/invalid table attributes that trip EPUBCheck.
            text = re.sub(r"\s+rules=(['\"]).*?\1", "", text, flags=re.IGNORECASE)

            # TeX4ht MathML can include invalid `stretchy` attributes on elements
            # such as `<mtext>`; strip these to satisfy EPUBCheck.
            text = re.sub(r"\s+stretchy=(['\"]).*?\1", "", text, flags=re.IGNORECASE)
            # TeX4ht can also emit invalid `rowlines` values; strip the attribute.
            text = re.sub(r"\s+rowlines=(['\"]).*?\1", "", text, flags=re.IGNORECASE)

            text = re.sub(
                r"(<img\b[^>]*?)\s+width='\d+'\s+height='\d+'([^>]*>)",
                r"\1\2",
                text,
            )

            def _replace_display_math(m: re.Match[str]) -> str:
                mathml = m.group(0)
                canon = _canonicalize_display_math_for_key(mathml)
                key = hashlib.md5(canon.encode("utf-8")).hexdigest()
                math_id = display_math_map.get(key)
                if not math_id or math_id not in svg_ids:
                    return mathml
                alt_text = _mathml_to_alt(mathml)
                anchors = "".join(f"<a id='{i}'></a>" for i in _extract_tex4ht_label_ids(mathml))
                rel = (svg_dir / f"{math_id}.svg").relative_to(content_root).as_posix()
                return anchors + f"<img src=\"{rel}\" alt=\"{alt_text}\" class=\"math-display\" />"

            text = DISPLAY_MATH_RE.sub(_replace_display_math, text)

            # Strip whitespace-only text nodes inside MathML: EPUBCheck validates
            # MathML against a non-mixed-content model (so indentation/newlines
            # become illegal text nodes under `<mrow>`, etc.).
            text = MATHML_BLOCK_RE.sub(
                lambda m: re.sub(r">\s+<", "><", _normalize_mathml_glyphs(m.group(0))),
                text,
            )
            text = _normalize_pre_blocks(text)

            # Keep image+caption together (avoid caption-only pages).
            text = _wrap_tex4ht_img_captions(text)

            text = _style_img_tags(text)
            text = _style_anchor_tags(text)

            for svg_rel, png_rel in svg_to_png.items():
                text = text.replace(f"'{svg_rel}'", f"'{png_rel}'")
                text = text.replace(f'\"{svg_rel}\"', f'\"{png_rel}\"')

            if re.search(r"<math\b", text, flags=re.IGNORECASE):
                mathml_hrefs.add(xf.relative_to(content_root).as_posix())

            xf.write_text(text, encoding="utf-8")

        if svg_paths:
            _update_opf_manifest(opf_path, [p for p in svg_paths if p.exists()])

        if svg_to_png:
            opf_text = opf_path.read_text(encoding="utf-8", errors="replace")
            for svg_rel, png_rel in svg_to_png.items():
                opf_text = opf_text.replace(f"href='{svg_rel}'", f"href='{png_rel}'")
                opf_text = opf_text.replace(f'href=\"{svg_rel}\"', f'href=\"{png_rel}\"')
                opf_text = re.sub(
                    rf"(<item\b[^>]*href=['\"]{re.escape(png_rel)}['\"][^>]*?)media-type=['\"]image/svg\+xml['\"]",
                    r"\1media-type='image/png'",
                    opf_text,
                    flags=re.IGNORECASE,
                )
            opf_path.write_text(opf_text, encoding="utf-8")

            for svg_rel in svg_to_png:
                (content_root / svg_rel).unlink(missing_ok=True)

        # Ensure OPF `mathml` properties match reality (EPUBCheck is strict).
        _sync_opf_mathml_properties(opf_path, mathml_hrefs)

        # Keep the legacy NCX (dtb:uid) in sync with the OPF identifier.
        opf_text = opf_path.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"<dc:identifier\b[^>]*>([^<]+)</dc:identifier>", opf_text, flags=re.IGNORECASE)
        opf_identifier = m.group(1).strip() if m else ""
        if opf_identifier:
            for ncx in content_root.glob("*.ncx"):
                ncx_text = ncx.read_text(encoding="utf-8", errors="replace")
                ncx_text = re.sub(
                    r"<meta\b[^>]*\bname=['\"]dtb:uid['\"][^>]*\/?>",
                    lambda mm: re.sub(r"content=(['\"]).*?\1", f"content='{opf_identifier}'", mm.group(0)),
                    ncx_text,
                    flags=re.IGNORECASE,
                )
                ncx.write_text(ncx_text, encoding="utf-8")

        _zip_epub(tmp_dir, output_epub)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
