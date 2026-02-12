#!/usr/bin/python3
from __future__ import annotations

"""
Bibliography style/policy audit.

Policy:
- Required fields per entry type are present.
- DOI-first preference: if DOI exists, entry is fine.
- If no DOI and arXiv info exists, enforce coherent arXiv metadata.
- If DOI/arXiv are unavailable, allow a canonical `url` fallback.
- Report entries missing DOI, arXiv, and URL (warning, not hard fail).
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Entry:
    kind: str
    key: str
    fields: dict[str, str]


@dataclass(frozen=True)
class Finding:
    level: str  # ERROR/WARN
    key: str
    message: str


ENTRY_START_RE = re.compile(r"@([A-Za-z]+)\s*\{", re.M)
KEY_RE = re.compile(r"\s*([^,\s]+)\s*,", re.S)
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")
METADATA_EXCEPTION_KEYS = {
    # Canonical publication metadata exists, but DOI/arXiv records are not reliable/available.
    "MacQueen1967",
    "DebAgrawal1995",
    "Zitzler2002",
    "Fritzke1994GrowingNeuralGas",
    "Zadeh1997",
}


def parse_entries(raw: str) -> list[Entry]:
    entries: list[Entry] = []
    idx = 0
    n = len(raw)

    while idx < n:
        m = ENTRY_START_RE.search(raw, idx)
        if not m:
            break
        kind = m.group(1).lower()
        start_brace = raw.find("{", m.start())
        if start_brace == -1:
            break

        depth = 0
        end = start_brace
        while end < n:
            ch = raw[end]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    break
            end += 1
        if end >= n:
            break

        body = raw[start_brace + 1 : end].strip()
        idx = end + 1
        km = KEY_RE.match(body)
        if not km:
            continue
        key = km.group(1).strip()
        fields_blob = body[km.end() :].strip()
        fields = parse_fields(fields_blob)
        entries.append(Entry(kind=kind, key=key, fields=fields))

    return entries


def parse_fields(blob: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    i = 0
    n = len(blob)
    while i < n:
        while i < n and blob[i] in " \t\r\n,":
            i += 1
        if i >= n:
            break

        j = i
        while j < n and (blob[j].isalnum() or blob[j] in "_-"):
            j += 1
        name = blob[i:j].lower()
        i = j
        while i < n and blob[i] in " \t\r\n":
            i += 1
        if i >= n or blob[i] != "=":
            while i < n and blob[i] != ",":
                i += 1
            continue
        i += 1
        while i < n and blob[i] in " \t\r\n":
            i += 1
        if i >= n:
            break

        if blob[i] == "{":
            depth = 0
            k = i
            while k < n:
                if blob[k] == "{":
                    depth += 1
                elif blob[k] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                k += 1
            value = blob[i + 1 : k].strip()
            i = k + 1
        elif blob[i] == '"':
            k = i + 1
            while k < n:
                if blob[k] == '"' and blob[k - 1] != "\\":
                    break
                k += 1
            value = blob[i + 1 : k].strip()
            i = k + 1
        else:
            k = i
            while k < n and blob[k] not in ",\n":
                k += 1
            value = blob[i:k].strip()
            i = k

        fields[name] = value
    return fields


def has_any(fields: dict[str, str], names: list[str]) -> bool:
    return any((fields.get(n) or "").strip() for n in names)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bib", default="refs.bib", help="Path to BibTeX file")
    ap.add_argument("--out", default="artifacts/qc/bib_style_report.md", help="Report output path")
    args = ap.parse_args()

    bib_path = Path(args.bib).resolve()
    if not bib_path.exists():
        print(f"ERROR: missing bibliography file: {bib_path}", file=sys.stderr)
        return 2

    entries = parse_entries(bib_path.read_text(encoding="utf-8", errors="ignore"))
    findings: list[Finding] = []

    required = {
        "article": ["author", "title", "journal", "year"],
        "inproceedings": ["author", "title", "booktitle", "year"],
        "book": ["title", "publisher", "year"],
    }

    for e in entries:
        req = required.get(e.kind, [])
        for f in req:
            if not (e.fields.get(f) or "").strip():
                findings.append(Finding(level="ERROR", key=e.key, message=f"missing required field `{f}` for `{e.kind}`"))

        if e.kind == "book" and not has_any(e.fields, ["author", "editor"]):
            findings.append(Finding(level="ERROR", key=e.key, message="book entry missing `author`/`editor`"))

        doi = (e.fields.get("doi") or "").strip()
        eprint = (e.fields.get("eprint") or "").strip()
        archiveprefix = (e.fields.get("archiveprefix") or "").strip().lower()
        url = (e.fields.get("url") or "").strip()

        if doi and doi.lower().startswith(("http://", "https://")):
            findings.append(Finding(level="ERROR", key=e.key, message="DOI must be canonical identifier only (remove URL prefix)"))

        if not doi:
            if eprint:
                if archiveprefix and archiveprefix != "arxiv":
                    findings.append(Finding(level="ERROR", key=e.key, message=f"eprint present but archiveprefix is `{archiveprefix}` (expected `arXiv`)"))
                if not ARXIV_RE.match(eprint):
                    findings.append(Finding(level="WARN", key=e.key, message=f"eprint does not look like canonical arXiv id: `{eprint}`"))
            elif not url and e.kind in {"article", "inproceedings"} and e.key not in METADATA_EXCEPTION_KEYS:
                findings.append(Finding(level="WARN", key=e.key, message="no DOI, no arXiv id, and no URL fallback"))

        venue = (e.fields.get("journal") or e.fields.get("booktitle") or "").strip()
        if venue and venue.isupper() and len(venue) > 6:
            findings.append(Finding(level="WARN", key=e.key, message="venue name appears all-caps; normalize casing"))

    errors = [f for f in findings if f.level == "ERROR"]
    warns = [f for f in findings if f.level == "WARN"]

    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Bibliography style report",
        "",
        f"- File: `{bib_path}`",
        f"- Entries scanned: `{len(entries)}`",
        "",
        "## Summary",
        "",
        f"- Errors: `{len(errors)}`",
        f"- Warnings: `{len(warns)}`",
        "",
    ]
    if errors:
        lines.append("## Errors")
        lines.append("")
        for f in errors:
            lines.append(f"- `{f.key}`: {f.message}")
        lines.append("")
    if warns:
        lines.append("## Warnings")
        lines.append("")
        for f in warns:
            lines.append(f"- `{f.key}`: {f.message}")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")

    if errors:
        print("ERROR: bibliography style check failed", file=sys.stderr)
        for f in errors[:100]:
            print(f"  - {f.key}: {f.message}", file=sys.stderr)
        return 2

    print(f"OK: bibliography style check ({len(entries)} entries)")
    if warns:
        print(f"WARN: bibliography style warnings={len(warns)} (see {out})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
