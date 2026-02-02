#!/usr/bin/python3
from __future__ import annotations

"""
Citations + BibTeX hygiene checks.

This is a publish-grade guardrail:
- Every \\cite{key} / \\citep{key} / \\citet{key} / \\nocite{key} must exist in `notes_output/refs.bib`.
- No duplicate keys in `refs.bib`.

It also reports (as warnings) likely “informal citations” like `Author (2012)` that
should usually be converted to \\citet{...}.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]  # notes_output/


@dataclass(frozen=True)
class Finding:
    where: str
    msg: str


_CITE_RE = re.compile(
    r"""\\
    (?P<cmd>cite|citep|citet|citealp|citealt|citeauthor|citeyear|nocite)
    \s*
    (?:\[[^\]]*\]\s*)?
    (?:\[[^\]]*\]\s*)?
    \{(?P<keys>[^}]+)\}
    """,
    re.X,
)

_BIB_KEY_RE = re.compile(r"^\s*@\w+\{([^,]+),", re.M)

# Conservative “informal citation” detector: name + (YEAR) without a \cite nearby.
_INFORMAL_YEAR_RE = re.compile(r"\b([A-Z][A-Za-z][A-Za-z\-]{1,40}(?:\s+and\s+[A-Z][A-Za-z\-]{2,40})?(?:\s+et\s+al\.)?)\s*\((19|20)\d{2}[a-z]?\)")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _tex_files(*, root: Path) -> list[Path]:
    files: list[Path] = []
    for p in root.rglob("*.tex"):
        if "artifacts" in p.parts:
            continue
        if "archive" in p.parts:
            continue
        files.append(p)
    return sorted(files)


def _extract_cite_keys(tex: str) -> set[str]:
    keys: set[str] = set()
    for m in _CITE_RE.finditer(tex):
        raw = m.group("keys")
        for k in raw.split(","):
            k = k.strip()
            if k:
                keys.add(k)
    return keys


def _extract_bib_keys(bib: str) -> list[str]:
    return [m.group(1).strip() for m in _BIB_KEY_RE.finditer(bib) if m.group(1).strip()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--notes", default=str(ROOT), help="Path to notes_output/ (default: auto-detected)")
    ap.add_argument("--bib", default="", help="Path to refs.bib (default: <notes>/refs.bib)")
    ap.add_argument("--fail-on-informal", action="store_true", help='Fail if informal citations like "Author (2012)" are found')
    args = ap.parse_args()

    notes = Path(args.notes).resolve()
    bib_path = Path(args.bib).resolve() if args.bib else (notes / "refs.bib").resolve()
    if not notes.exists():
        print(f"ERROR: notes dir not found: {notes}", file=sys.stderr)
        return 2
    if not bib_path.exists():
        print(f"ERROR: refs.bib not found: {bib_path}", file=sys.stderr)
        return 2

    tex_files = _tex_files(root=notes)
    cited: set[str] = set()
    informal: list[Finding] = []
    for p in tex_files:
        s = _read_text(p)
        cited |= _extract_cite_keys(s)
        for m in _INFORMAL_YEAR_RE.finditer(s):
            # Ignore if the match is already immediately preceded by a \cite command.
            ctx = s[max(0, m.start() - 40) : m.start()]
            if "\\cite" in ctx:
                continue
            line = s.count("\n", 0, m.start()) + 1
            informal.append(Finding(where=f"{p.relative_to(notes)}:{line}", msg=f'Possible informal citation: "{m.group(0)}"'))

    bib_raw = _read_text(bib_path)
    bib_keys = _extract_bib_keys(bib_raw)
    bib_set = set(bib_keys)

    # Duplicate keys.
    seen: set[str] = set()
    dup: set[str] = set()
    for k in bib_keys:
        if k in seen:
            dup.add(k)
        seen.add(k)

    missing = sorted(cited - bib_set)

    ok = True
    if missing:
        ok = False
        print("ERROR: cited keys missing from refs.bib:", file=sys.stderr)
        for k in missing:
            print(f"  - {k}", file=sys.stderr)
    if dup:
        ok = False
        print("ERROR: duplicate keys in refs.bib:", file=sys.stderr)
        for k in sorted(dup):
            print(f"  - {k}", file=sys.stderr)

    if informal:
        print("WARN: possible informal citations (prefer \\citet{...} / \\citep{...}):", file=sys.stderr)
        for f in informal[:200]:
            print(f"  - {f.where}: {f.msg}", file=sys.stderr)
        if len(informal) > 200:
            print(f"  ... ({len(informal) - 200} more)", file=sys.stderr)
        if args.fail_on_informal:
            ok = False

    if ok:
        print(f"OK: citations/bib hygiene ({len(cited)} cited keys, {len(bib_set)} bib entries)")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
