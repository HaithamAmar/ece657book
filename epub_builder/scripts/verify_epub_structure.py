#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Issue:
    where: str
    msg: str


def _read_zip_text(z: zipfile.ZipFile, name: str) -> str:
    try:
        return z.read(name).decode("utf-8", errors="ignore")
    except KeyError:
        return ""


def _extract_aux_labels(aux_path: Path, *, prefix: str) -> list[str]:
    try:
        s = aux_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    pat = re.compile(r"\\newlabel\{(" + re.escape(prefix) + r"[^}]+)\}\{")
    labs = sorted(set(m.group(1) for m in pat.finditer(s)))
    return [l for l in labs if "@" not in l]


def _collect_ids(html: str) -> set[str]:
    return set(m.group(1) for m in re.finditer(r'\bid="([^"]+)"', html))


def _collect_href_targets(html: str) -> list[tuple[str, str | None]]:
    """
    Return list of (href, kind), where kind is:
    - None for non-fragment/non-xhtml hrefs
    - "local" for "#frag"
    - "xhtml" for "foo.xhtml#frag"
    """
    out: list[tuple[str, str | None]] = []
    for m in re.finditer(r'\bhref="([^"]+)"', html):
        href = m.group(1)
        if href.startswith("#") and len(href) > 1:
            out.append((href, "local"))
        elif ".xhtml#" in href:
            out.append((href, "xhtml"))
        else:
            out.append((href, None))
    return out


def verify_epub(epub_path: Path, *, aux_path: Path | None = None) -> list[Issue]:
    issues: list[Issue] = []

    with zipfile.ZipFile(epub_path, "r") as z:
        names = set(z.namelist())
        opf = _read_zip_text(z, "EPUB/content.opf")
        nav = _read_zip_text(z, "EPUB/nav.xhtml")

        if not opf:
            issues.append(Issue("EPUB/content.opf", "missing"))
        if not nav:
            issues.append(Issue("EPUB/nav.xhtml", "missing"))

        # nav.xhtml must not contain MathML (EPUBCheck strict) or empty spans.
        if "<math" in nav:
            issues.append(Issue("EPUB/nav.xhtml", "contains MathML (<math>); TOC should be plain text"))
        if re.search(r"<span\b[^>]*/>", nav) or re.search(r"<span\b[^>]*>\s*</span>", nav):
            issues.append(Issue("EPUB/nav.xhtml", "contains empty <span> inside nav; EPUBCheck rejects this"))

        # cover.xhtml should not be declared as svg after we rewrite it to <img>.
        if re.search(r'id="cover_xhtml"[^>]*\\bproperties="[^"]*\\bsvg\\b', opf):
            issues.append(Issue("EPUB/content.opf", 'cover_xhtml has properties="svg" (should be removed)'))

        # Structural scan of XHTML files.
        text_dir = "EPUB/text/"
        xhtmls = sorted([n for n in names if n.startswith(text_dir) and n.endswith(".xhtml")])
        id_map: dict[str, str] = {}
        xhtml_by_name: dict[str, str] = {}
        for name in xhtmls:
            s = _read_zip_text(z, name)
            xhtml_by_name[Path(name).name] = s
            for lab in _collect_ids(s):
                id_map.setdefault(lab, Path(name).name)

        # Validate fragment links:
        for name in xhtmls:
            fn = Path(name).name
            s = xhtml_by_name.get(fn, "")
            ids = _collect_ids(s)
            for href, kind in _collect_href_targets(s):
                if kind == "local":
                    frag = href[1:]
                    if frag not in ids:
                        issues.append(Issue(name, f'local fragment "{href}" not defined in same file'))
                elif kind == "xhtml":
                    x, frag = href.split("#", 1)
                    target = Path(x).name
                    target_html = xhtml_by_name.get(target)
                    if target_html is None:
                        issues.append(Issue(name, f'fragment target file missing: "{x}"'))
                        continue
                    if frag not in _collect_ids(target_html):
                        issues.append(Issue(name, f'fragment "#{frag}" not defined in "{target}"'))

            # Guardrails: no raw TikZ and no Pandoc ref-style drift.
            if "\\begin{tikzpicture}" in s:
                issues.append(Issue(name, "contains raw tikzpicture (missed replacement)"))
            if re.search(r'data-reference-type="ref"\s+data-reference="(chap:|sec:|fig:|tab:)', s):
                issues.append(Issue(name, "contains pandoc ref-style crossrefs (data-reference=chap/sec/fig/tab)"))

            # Every table should be wrapped in a scroll container.
            if "<table" in s and '<div class="table-wrap">' not in s:
                issues.append(Issue(name, 'contains <table> without <div class="table-wrap"> wrapper'))

        # Ensure each fig: label from aux exists as a <figure id="..."> with renderable content.
        if aux_path is not None and aux_path.exists():
            fig_labels = _extract_aux_labels(aux_path, prefix="fig:")
            for lab in fig_labels:
                fn = id_map.get(lab)
                if not fn:
                    issues.append(Issue("AUX", f"missing fig id in EPUB: {lab}"))
                    continue
                s = xhtml_by_name.get(fn, "")
                m = re.search(
                    r'<figure\b[^>]*\bid="' + re.escape(lab) + r'"[^>]*>[\s\S]*?</figure>',
                    s,
                    flags=re.DOTALL,
                )
                if not m:
                    issues.append(Issue(f"EPUB/text/{fn}", f'figure id="{lab}" missing <figure> wrapper'))
                    continue
                block = m.group(0)
                if "<img" not in block and "<svg" not in block and "<math" not in block:
                    issues.append(Issue(f"EPUB/text/{fn}", f'figure "{lab}" has no renderable content'))

    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--epub", required=True, help="Path to an EPUB (Apple or Kindle)")
    ap.add_argument("--aux", default="", help="Optional .aux file to validate fig: ids (recommended)")
    args = ap.parse_args()

    epub = Path(args.epub).resolve()
    aux = Path(args.aux).resolve() if args.aux else None
    issues = verify_epub(epub, aux_path=aux)
    if issues:
        print("EPUB structural verification failed:")
        for it in issues[:80]:
            print(f"- {it.where}: {it.msg}")
        return 2
    print("OK: EPUB structural verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
