from __future__ import annotations

import re
import tempfile
import subprocess
import shutil
from pathlib import Path
import zipfile


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
                    insert = f'  <meta name="cover" content="{cover_id}" />\\n'
                    if "</metadata>" in md:
                        return md.replace("</metadata>", insert + "</metadata>", 1)
                    return md

                opf = re.sub(r"<metadata[\s\S]*?</metadata>", _add_cover_meta, opf, count=1)
                opf_path.write_text(opf, encoding="utf-8")

            # Rewrite cover.xhtml to a simple <img> cover page for better compatibility.
            # cover_href is relative to OPF; cover.xhtml lives under EPUB/text/.
            # Pandoc uses href like "media/file74.png".
            img_src = "../" + cover_href
            cover_doc = f'''<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n<head>\n  <meta charset="utf-8" />\n  <title>Cover</title>\n  <style>\n    body {{ margin: 0; padding: 0; }}\n    #cover {{ text-align: center; }}\n    #cover img {{ max-width: 100%; height: auto; }}\n  </style>\n  <link rel="stylesheet" type="text/css" href="../styles/stylesheet1.css" />\n</head>\n<body id="cover">\n  <div id="cover">\n    <img alt="Cover" src="{img_src}" />\n  </div>\n</body>\n</html>\n'''
            cover_xhtml.write_text(cover_doc, encoding="utf-8")

        # Wrap block MathML in <div class="math-block"> for scrollable overflow.
        text_dir = tmp / "EPUB" / "text"
        if text_dir.exists():
            for xhtml in sorted(text_dir.glob("*.xhtml")):
                s = xhtml.read_text(encoding="utf-8", errors="ignore")
                # Non-greedy match on individual MathML blocks.
                s2 = re.sub(
                    r'(<math\b[^>]*\bdisplay="block"[^>]*>[\s\S]*?</math>)',
                    r'<div class="math-block">\1</div>',
                    s,
                )
                if s2 != s:
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
