#!/usr/bin/python3
from __future__ import annotations

"""
Cross-reference and label hygiene checks.

Publish-grade guardrails:
- Every referenced label must exist in the LaTeX sources.
- Disallow `\\ref{chap:...}` / `\\ref{fig:...}` / `\\ref{tab:...}` / `\\ref{sec:...}` / `\\ref{app:...}` / `\\ref{eq:...}`:
  - Use `\\Cref`/`\\cref` for chapter/section/figure/table/appendix references.
  - Use `\\eqref` for equation references.

Soft warnings:
- Potentially hardcoded numbering like "Chapter 7" / "Figure 12" in prose.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    where: str
    msg: str


_LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
_REF_RE = re.compile(r"\\ref\{([^}]+)\}")

_CREF_RE = re.compile(r"\\(?:[cC]ref|[cC]refrange)\{([^}]+)\}")
_EQREF_RE = re.compile(r"\\eqref\{([^}]+)\}")

_HARD_CODED = [
    re.compile(r"\bChapter\s+\d+\b"),
    re.compile(r"\bFigure\s+\d+\b"),
    re.compile(r"\bTable\s+\d+\b"),
    re.compile(r"\bAppendix\s+\d+\b"),
]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _tex_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for p in root.rglob("*.tex"):
        if "artifacts" in p.parts or "archive" in p.parts:
            continue
        out.append(p)
    return sorted(out)


def _split_keys(raw: str) -> list[str]:
    return [k.strip() for k in raw.split(",") if k.strip()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Root directory containing release LaTeX sources (default: auto-detect)")
    ap.add_argument("--fail-on-hardcoded", action="store_true", help='Fail if hardcoded refs like "Chapter 7" are found')
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if args.root == ".":
        if not (root / "ece657_notes.tex").exists() and (root / "notes_output" / "ece657_notes.tex").exists():
            root = (root / "notes_output").resolve()
    if not root.exists():
        print(f"ERROR: missing root dir: {root}", file=sys.stderr)
        return 2

    tex_files = _tex_files(root)
    labels: set[str] = set()
    for p in tex_files:
        s = _read_text(p)
        for m in _LABEL_RE.finditer(s):
            lab = m.group(1).strip()
            if lab:
                labels.add(lab)

    errors: list[Finding] = []
    warnings: list[Finding] = []

    def check_label_exists(path: Path, pos: int, lab: str, *, kind: str) -> None:
        if lab not in labels:
            line = _read_text(path).count("\n", 0, pos) + 1
            errors.append(Finding(where=f"{path.relative_to(root)}:{line}", msg=f"{kind} references missing label: {lab}"))

    for p in tex_files:
        s = _read_text(p)

        for m in _REF_RE.finditer(s):
            lab = m.group(1).strip()
            if not lab:
                continue
            # Ignore macro placeholders like \ref{#1}.
            if "#" in lab:
                continue
            # Disallow \ref for semantic label prefixes.
            if lab.startswith(("chap:", "sec:", "fig:", "tab:", "app:", "eq:")):
                line = s.count("\n", 0, m.start()) + 1
                errors.append(
                    Finding(
                        where=f"{p.relative_to(root)}:{line}",
                        msg=f'Disallowed \\\\ref{{{lab}}}; use \\\\Cref/\\\\cref for chap/sec/fig/tab/app and \\\\eqref for eq',
                    )
                )
            check_label_exists(p, m.start(), lab, kind="\\ref")

        for m in _CREF_RE.finditer(s):
            for lab in _split_keys(m.group(1)):
                # \Crefrange{a}{b} uses two args, but we only enforce existence on the first arg list here.
                check_label_exists(p, m.start(), lab, kind="\\Cref/\\cref")

        for m in _EQREF_RE.finditer(s):
            for lab in _split_keys(m.group(1)):
                check_label_exists(p, m.start(), lab, kind="\\eqref")

        # Hardcoded-number warnings (ignore LaTeX comment lines).
        for pat in _HARD_CODED:
            for m in pat.finditer(s):
                line_start = s.rfind("\n", 0, m.start()) + 1
                line_end = s.find("\n", m.start())
                if line_end == -1:
                    line_end = len(s)
                line = s[line_start:line_end]
                if line.lstrip().startswith("%"):
                    continue
                line_no = s.count("\n", 0, m.start()) + 1
                warnings.append(
                    Finding(
                        where=f"{p.relative_to(root)}:{line_no}",
                        msg=f'Potential hardcoded cross-reference: "{m.group(0)}"',
                    )
                )

    if errors:
        print("ERROR: crossref/label checks failed:", file=sys.stderr)
        for e in errors[:200]:
            print(f"  - {e.where}: {e.msg}", file=sys.stderr)
        if len(errors) > 200:
            print(f"  ... ({len(errors) - 200} more)", file=sys.stderr)
        return 2

    if warnings:
        print("WARN: potential hardcoded numbering (prefer label-based refs):", file=sys.stderr)
        for w in warnings[:200]:
            print(f"  - {w.where}: {w.msg}", file=sys.stderr)
        if len(warnings) > 200:
            print(f"  ... ({len(warnings) - 200} more)", file=sys.stderr)
        if args.fail_on_hardcoded:
            return 2

    print(f"OK: crossref/label hygiene ({len(labels)} labels scanned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
