from __future__ import annotations

import re
import tempfile
import subprocess
import shutil
from pathlib import Path
import zipfile


def _strip_mathml_from_nav(nav: str) -> str:
    """
    EPUBCheck is strict about MathML inside nav.xhtml (TOC). Replace any MathML
    blocks with a plain-text fallback taken from the x-tex annotation when
    available.
    """

    def _replace_math(m: re.Match[str]) -> str:
        block = m.group(0)
        ann = re.search(r'<annotation[^>]*encoding="application/x-tex"[^>]*>([\s\S]*?)</annotation>', block)
        if ann:
            text = re.sub(r"\s+", " ", ann.group(1)).strip()
            return text
        return ""

    return re.sub(r"<math\b[\s\S]*?</math>", _replace_math, nav)

def _strip_empty_spans_from_nav(nav: str) -> str:
    """
    Pandoc can emit empty anchor spans (e.g., from \\hypertarget) inside heading
    text, and then copy them into nav.xhtml. EPUBCheck rejects empty <span>
    elements inside <nav>.
    """
    nav2 = re.sub(r"<span\b[^>]*/>", "", nav)
    nav2 = re.sub(r"<span\b[^>]*>\s*</span>", "", nav2)
    return nav2


def _id_to_xhtml_map(text_dir: Path) -> dict[str, str]:
    """
    Build a mapping from element id -> xhtml filename (e.g., 'fig:roadmap' -> 'ch005.xhtml').
    """
    mapping: dict[str, str] = {}
    for xhtml in sorted(text_dir.glob("*.xhtml")):
        s = xhtml.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r'\bid="([^"]+)"', s):
            lab = m.group(1)
            # Keep first occurrence; duplicate ids are invalid anyway.
            mapping.setdefault(lab, xhtml.name)
    return mapping


def _rewrite_cross_file_fragment_links(xhtml_text: str, *, current_xhtml: str, id_map: dict[str, str]) -> str:
    """
    Pandoc emits href="#fig:..." for figure ids, but EPUB splits content across
    multiple XHTML files. Rewrite to href="chXXX.xhtml#fig:..." when the id lives
    in a different file.
    """

    def _sub(m: re.Match[str]) -> str:
        frag = m.group(1)
        target = id_map.get(frag)
        if not target or target == current_xhtml:
            return m.group(0)
        return f'href="{target}#{frag}"'

    return re.sub(r'href="#([^"]+)"', _sub, xhtml_text)

def _wrap_tables(html: str) -> str:
    """
    Wrap HTML tables in a scroll container so wide tables remain readable on
    small screens (instead of shrinking to microscopic text).
    """
    if "<table" not in html:
        return html

    def _sub(m: re.Match[str]) -> str:
        block = m.group(0)
        # Avoid double-wrapping.
        if re.search(r'<div\s+class="table-wrap"\s*>[\s\S]*?<table\b', block):
            return block
        return f'<div class="table-wrap">{block}</div>'

    # Only wrap full table blocks; tables are block-level and should not be
    # inside <p> in Pandoc output.
    return re.sub(r"(<table\b[\s\S]*?</table>)", _sub, html)

def _strip_table_inline_widths(html: str) -> str:
    """
    Some readers treat Pandoc's inline `style="width:XX%"` on <table>/<col> as
    authoritative and render tables extremely narrow. We prefer responsive CSS.
    """
    if "<table" not in html and "<col" not in html:
        return html

    def _strip_width_style(m: re.Match[str]) -> str:
        tag = m.group(0)
        style = m.group(1)
        # Remove width declarations but keep other style properties.
        style2 = re.sub(r"(^|;)\s*width\s*:\s*[^;]+", "", style, flags=re.IGNORECASE)
        style2 = re.sub(r";{2,}", ";", style2)
        style2 = style2.strip().strip(";").strip()
        if not style2:
            return re.sub(r'\s+style="[^"]*"', "", tag)
        return tag.replace(style, style2)

    # Strip width from any inline style attribute.
    html = re.sub(r'(<(?:table|col)\b[^>]*\sstyle=")([^"]+)(")', lambda m: m.group(1) + re.sub(r"(^|;)\s*width\s*:\s*[^;]+", "", m.group(2), flags=re.IGNORECASE).strip().strip(";") + m.group(3), html)
    # Remove now-empty style attributes.
    html = re.sub(r'(<(?:table|col)\b[^>]*?)\sstyle=""', r"\1", html)
    return html

def _normalize_table_captions(html: str) -> str:
    """
    Table captions sometimes reuse the 'Schematic:' prefix used for figures.
    For tables, use 'Table:'.
    """
    if "<caption>" not in html:
        return html
    return re.sub(r"(<caption>\s*)Schematic:\s*", r"\1Table: ", html)


def postprocess_epub_minimal(epub_path: Path) -> None:
    if not epub_path.exists():
        raise FileNotFoundError(epub_path)

    # Postprocess goals:
    # - Make the cover visible to picky thumbnailers (macOS Quick Look) by:
    #   - adding EPUB2-style `<meta name="cover" ...>` in the OPF metadata
    #   - rewriting `cover.xhtml` to use `<img>` (some renderers ignore SVG covers)
    # - Reduce equation clipping in readers that ignore overflow on `<math>` by
    #   wrapping block MathML in a scrollable container.

    with tempfile.TemporaryDirectory(prefix="epub_builder_post_") as td:
        tmp = Path(td)
        with zipfile.ZipFile(epub_path, "r") as z:
            z.extractall(tmp)

        opf_path = tmp / "EPUB" / "content.opf"
        cover_xhtml = tmp / "EPUB" / "text" / "cover.xhtml"
        nav_xhtml = tmp / "EPUB" / "nav.xhtml"
        if not opf_path.exists() or not cover_xhtml.exists():
            return

        opf = opf_path.read_text(encoding="utf-8", errors="ignore")

        # Identify the cover-image manifest item.
        cover_id = None
        cover_href = None
        m_manifest = re.search(r"<manifest[\s\S]*?</manifest>", opf)
        if m_manifest:
            for line in m_manifest.group(0).splitlines():
                if "cover-image" in line:
                    m = re.search(r'id="([^"]+)"', line)
                    h = re.search(r'href="([^"]+)"', line)
                    if m and h:
                        cover_id = m.group(1)
                        cover_href = h.group(1)
                        break

        if cover_id and cover_href:
            # Add `<meta name="cover" content="...">` if missing.
            if 'name="cover"' not in opf:
                def _add_cover_meta(m: re.Match[str]) -> str:
                    md = m.group(0)
                    insert = f'  <meta name="cover" content="{cover_id}" />\n'
                    if "</metadata>" in md:
                        return md.replace("</metadata>", insert + "</metadata>", 1)
                    return md

                opf = re.sub(r"<metadata[\s\S]*?</metadata>", _add_cover_meta, opf, count=1)
                opf_path.write_text(opf, encoding="utf-8")

            # Pandoc can mark cover.xhtml with properties="svg" when it uses an
            # SVG wrapper. We rewrite cover.xhtml to a plain <img>, so remove
            # that property for EPUBCheck compliance.
            opf2 = re.sub(
                r'(<item\b[^>]*\bid="cover_xhtml"[^>]*?)\s+properties="[^"]*\bsvg\b[^"]*"(.*?)\s*/>',
                r"\1\2 />",
                opf,
                flags=re.IGNORECASE,
            )
            if opf2 != opf:
                opf = opf2
                opf_path.write_text(opf, encoding="utf-8")

            # Rewrite cover.xhtml to a simple <img> cover page for better compatibility.
            # cover_href is relative to OPF; cover.xhtml lives under EPUB/text/.
            # Pandoc uses href like "media/file74.png".
            img_src = "../" + cover_href
            cover_doc = f'''<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n<head>\n  <meta charset="utf-8" />\n  <title>Cover</title>\n  <style>\n    body {{ margin: 0; padding: 0; }}\n    body#cover {{ text-align: center; }}\n    .cover img {{ max-width: 100%; height: auto; }}\n  </style>\n  <link rel="stylesheet" type="text/css" href="../styles/stylesheet1.css" />\n</head>\n<body id="cover">\n  <div class="cover">\n    <img alt="Cover" src="{img_src}" />\n  </div>\n</body>\n</html>\n'''
            cover_xhtml.write_text(cover_doc, encoding="utf-8")

        # Remove MathML from nav.xhtml (TOC) for EPUBCheck compliance.
        if nav_xhtml.exists():
            nav = nav_xhtml.read_text(encoding="utf-8", errors="ignore")
            nav2 = _strip_mathml_from_nav(nav)
            nav2 = _strip_empty_spans_from_nav(nav2)
            if nav2 != nav:
                nav_xhtml.write_text(nav2, encoding="utf-8")

        # Wrap block MathML in a container for scrollable overflow.
        text_dir = tmp / "EPUB" / "text"
        if text_dir.exists():
            id_map = _id_to_xhtml_map(text_dir)
            for xhtml in sorted(text_dir.glob("*.xhtml")):
                orig = xhtml.read_text(encoding="utf-8", errors="ignore")
                s = orig
                s = _rewrite_cross_file_fragment_links(s, current_xhtml=xhtml.name, id_map=id_map)
                s = _wrap_tables(s)
                s = _strip_table_inline_widths(s)
                s = _normalize_table_captions(s)
                # Non-greedy match on individual MathML blocks.
                s2 = re.sub(
                    r'(<math\b[^>]*\bdisplay="block"[^>]*>[\s\S]*?</math>)',
                    r'<span class="math-block">\1</span>',
                    s,
                )
                if s2 != orig:
                    xhtml.write_text(s2, encoding="utf-8")

        # Repack EPUB: `mimetype` must be first and uncompressed.
        mimetype_path = tmp / "mimetype"
        if not mimetype_path.exists():
            return

        out_tmp = epub_path.with_suffix(".post.epub")
        if out_tmp.exists():
            out_tmp.unlink()
        with zipfile.ZipFile(out_tmp, "w") as z:
            z.write(mimetype_path, "mimetype", compress_type=zipfile.ZIP_STORED)
            for path in sorted(tmp.rglob("*")):
                if path.is_dir() or path == mimetype_path:
                    continue
                arc = path.relative_to(tmp).as_posix()
                z.write(path, arc, compress_type=zipfile.ZIP_DEFLATED)

        out_tmp.replace(epub_path)


def run_epubcheck(epub_path: Path, *, out_dir: Path) -> None:
    epubcheck = shutil.which("epubcheck")
    if epubcheck is None:
        return
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / f"{epub_path.stem}.epubcheck.txt"
    with log_path.open("w", encoding="utf-8") as f:
        subprocess.run([epubcheck, str(epub_path)], stdout=f, stderr=subprocess.STDOUT, check=False)
