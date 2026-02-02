#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TableInfo:
    xhtml: str
    index_in_file: int
    caption: str | None
    n_cols: int | None
    width_style: str | None


def _strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()


def audit_epub_tables(epub_path: Path) -> list[TableInfo]:
    out: list[TableInfo] = []
    with zipfile.ZipFile(epub_path, "r") as z:
        names = [n for n in z.namelist() if n.startswith("EPUB/text/") and n.endswith(".xhtml")]
        for name in sorted(names):
            html = z.read(name).decode("utf-8", errors="ignore")
            tables = list(re.finditer(r"<table\b[\s\S]*?</table>", html))
            for idx, m in enumerate(tables, start=1):
                block = m.group(0)
                width_style = None
                mstyle = re.search(r'<table\b[^>]*\bstyle="([^"]+)"', block)
                if mstyle:
                    width_style = mstyle.group(1)

                cap = None
                mcap = re.search(r"<caption\b[^>]*>([\s\S]*?)</caption>", block)
                if mcap:
                    cap = _strip_tags(mcap.group(1))

                n_cols = None
                # Prefer header cells for column count; fall back to first body row.
                mhead = re.search(r"<thead\b[\s\S]*?<tr\b[\s\S]*?</tr>[\s\S]*?</thead>", block)
                if mhead:
                    n_cols = len(re.findall(r"<th\b", mhead.group(0)))
                if not n_cols:
                    mtr = re.search(r"<tr\b[\s\S]*?</tr>", block)
                    if mtr:
                        n_cols = len(re.findall(r"<t[dh]\b", mtr.group(0))) or None

                out.append(
                    TableInfo(
                        xhtml=Path(name).name,
                        index_in_file=idx,
                        caption=cap,
                        n_cols=n_cols,
                        width_style=width_style,
                    )
                )
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--epub", required=True)
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-md", required=True)
    ap.add_argument("--flag-cols", type=int, default=5, help="Flag tables with >= this many columns")
    args = ap.parse_args()

    epub = Path(args.epub).resolve()
    tables = audit_epub_tables(epub)

    Path(args.out_json).write_text(
        json.dumps([t.__dict__ for t in tables], indent=2, sort_keys=True), encoding="utf-8"
    )

    lines: list[str] = []
    lines.append("# EPUB table audit\n")
    lines.append(f"- EPUB: `{epub}`\n")
    lines.append(f"- Tables found: {len(tables)}\n")
    lines.append(f"- Flag threshold: >= {args.flag_cols} columns\n")
    lines.append("\n## Tables (by file order)\n")
    for t in tables:
        cols = str(t.n_cols) if t.n_cols is not None else "?"
        cap = t.caption or "(no caption)"
        flag = ""
        if t.n_cols is not None and t.n_cols >= args.flag_cols:
            flag = " **FLAG: wide**"
        lines.append(f"- `{t.xhtml}` table#{t.index_in_file}: cols={cols}{flag} — {cap}\n")
        if t.width_style:
            lines.append(f"  - style: `{t.width_style}`\n")

    Path(args.out_md).write_text("".join(lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

