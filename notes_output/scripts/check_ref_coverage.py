#!/usr/bin/python3
from __future__ import annotations

"""
Figure/table reference coverage audit.

Checks:
- Each fig:/tab: label is referenced at least once.
- Optional strict-order check: at least one reference before the label and
  at least one reference after the label, when references occur in the same file.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_SINGLE_RE = re.compile(r"\\(?:ref|eqref|Cref|cref|autoref|nameref)\{([^}]+)\}")
REF_RANGE_RE = re.compile(r"\\(?:Crefrange|crefrange)\{([^}]+)\}\{([^}]+)\}")


@dataclass(frozen=True)
class Occurrence:
    file: Path
    line: int


def tex_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for path in root.rglob("*.tex"):
        if "artifacts" in path.parts or "archive" in path.parts:
            continue
        out.append(path)
    return sorted(out)


def split_keys(raw: str) -> list[str]:
    return [k.strip() for k in raw.split(",") if k.strip()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="notes_output root")
    ap.add_argument(
        "--strict-order",
        action="store_true",
        help="Fail if a figure/table label does not have both before/after references in its own file",
    )
    ap.add_argument(
        "--out",
        default="artifacts/qc/ref_coverage_report.md",
        help="Markdown report path",
    )
    args = ap.parse_args()

    root = Path(args.root).resolve()
    files = tex_files(root)

    labels: dict[str, Occurrence] = {}
    refs: dict[str, list[Occurrence]] = {}

    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        lines = text.splitlines()
        for i, raw in enumerate(lines, start=1):
            for m in LABEL_RE.finditer(raw):
                key = m.group(1).strip()
                if key.startswith(("fig:", "tab:")):
                    labels[key] = Occurrence(file=path, line=i)

            for m in REF_SINGLE_RE.finditer(raw):
                for key in split_keys(m.group(1)):
                    refs.setdefault(key, []).append(Occurrence(file=path, line=i))

            for m in REF_RANGE_RE.finditer(raw):
                for key in (m.group(1).strip(), m.group(2).strip()):
                    if key:
                        refs.setdefault(key, []).append(Occurrence(file=path, line=i))

    unreferenced: list[str] = []
    order_gaps: list[str] = []
    rows: list[str] = []

    for key in sorted(labels.keys()):
        lab = labels[key]
        r = refs.get(key, [])
        rel_file = lab.file.relative_to(root)
        if not r:
            unreferenced.append(key)
            rows.append(f"| `{key}` | `{rel_file}:{lab.line}` | 0 | no | no |")
            continue

        same_file = [occ for occ in r if occ.file == lab.file]
        has_before = any(occ.line < lab.line for occ in same_file)
        has_after = any(occ.line > lab.line for occ in same_file)
        rows.append(
            f"| `{key}` | `{rel_file}:{lab.line}` | {len(r)} | {'yes' if has_before else 'no'} | {'yes' if has_after else 'no'} |"
        )
        if args.strict_order and (not has_before or not has_after):
            order_gaps.append(key)

    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    report = [
        "# Figure/Table Reference Coverage",
        "",
        f"- Root: `{root}`",
        f"- Labels scanned: `{len(labels)}`",
        f"- Strict-order mode: `{'on' if args.strict_order else 'off'}`",
        "",
        "## Coverage table",
        "",
        "| Label | Defined at | #refs | before in file | after in file |",
        "|---|---:|---:|---:|---:|",
        *rows,
        "",
        "## Summary",
        "",
        f"- Unreferenced labels: `{len(unreferenced)}`",
        f"- Strict-order gaps: `{len(order_gaps)}`",
        "",
    ]
    if unreferenced:
        report.append("- Unreferenced list:")
        report.extend([f"  - `{k}`" for k in unreferenced])
        report.append("")
    if order_gaps:
        report.append("- Strict-order gap list:")
        report.extend([f"  - `{k}`" for k in order_gaps])
        report.append("")

    out.write_text("\n".join(report), encoding="utf-8")

    if unreferenced:
        print("ERROR: unreferenced figure/table labels found", file=sys.stderr)
        for key in unreferenced[:100]:
            print(f"  - {key}", file=sys.stderr)
        return 2
    if args.strict_order and order_gaps:
        print("ERROR: strict-order figure/table reference gaps found", file=sys.stderr)
        for key in order_gaps[:100]:
            print(f"  - {key}", file=sys.stderr)
        return 2

    print(f"OK: figure/table reference coverage ({len(labels)} labels)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

