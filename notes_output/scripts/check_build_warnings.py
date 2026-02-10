#!/usr/bin/python3
from __future__ import annotations

"""
Strict TeX log warning gate for camera-ready builds.

Fails on:
- Undefined references/citations.
- "There were undefined references/citations."
- Overfull \\hbox above a configurable threshold.
- pdfTeX/driver warnings.
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    kind: str
    line_no: int
    message: str


PATTERNS = {
    "undefined_reference": re.compile(r"LaTeX Warning: Reference `[^']+' on page .* undefined"),
    "undefined_citation": re.compile(r"LaTeX Warning: Citation `[^']+' on page .* undefined"),
    "undefined_refs_summary": re.compile(r"LaTeX Warning: There were undefined references\."),
    "undefined_cites_summary": re.compile(r"LaTeX Warning: There were undefined citations\."),
    "pdftex_warning": re.compile(r"pdfTeX warning", re.IGNORECASE),
    "driver_warning": re.compile(r"(xdvipdfmx|dvipdfmx|dvipdf) warning", re.IGNORECASE),
}

OVERFULL_RE = re.compile(r"Overfull \\hbox \((?P<pt>[0-9]+(?:\.[0-9]+)?)pt too wide\)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default="ece657_notes.log", help="TeX log path")
    ap.add_argument(
        "--max-overfull-pt",
        type=float,
        default=3.0,
        help="Maximum allowed Overfull \\\\hbox width in points",
    )
    ap.add_argument(
        "--out",
        default="artifacts/qc/build_warning_gate.md",
        help="Markdown report output path",
    )
    args = ap.parse_args()

    log_path = Path(args.log).resolve()
    if not log_path.exists():
        print(f"ERROR: missing log file: {log_path}", file=sys.stderr)
        return 2

    findings: list[Finding] = []
    overfull_findings: list[Finding] = []

    for i, raw in enumerate(log_path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
        line = raw.strip()

        m_overfull = OVERFULL_RE.search(line)
        if m_overfull:
            pt = float(m_overfull.group("pt"))
            if pt > args.max_overfull_pt:
                overfull_findings.append(
                    Finding(kind="overfull_hbox", line_no=i, message=f"{line} (>{args.max_overfull_pt}pt)")
                )
            continue

        for kind, pat in PATTERNS.items():
            if pat.search(line):
                findings.append(Finding(kind=kind, line_no=i, message=line))
                break

    all_failures = findings + overfull_findings

    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    report_lines = [
        "# Build warning gate report",
        "",
        f"- Log: `{log_path}`",
        f"- Max allowed Overfull hbox: `{args.max_overfull_pt}pt`",
        "",
    ]

    if not all_failures:
        report_lines.extend(
            [
                "## Result",
                "",
                "- PASS: no blocking TeX log warnings detected.",
                "",
            ]
        )
        out_path.write_text("\n".join(report_lines), encoding="utf-8")
        print("OK: build warning gate passed")
        return 0

    report_lines.extend(["## Result", "", "- FAIL: blocking warnings found.", ""])
    report_lines.append("## Findings")
    report_lines.append("")
    for f in all_failures:
        report_lines.append(f"- `{f.kind}` line {f.line_no}: {f.message}")
    report_lines.append("")
    out_path.write_text("\n".join(report_lines), encoding="utf-8")

    print("ERROR: build warning gate failed", file=sys.stderr)
    for f in all_failures[:100]:
        print(f"  - {f.kind} @ line {f.line_no}: {f.message}", file=sys.stderr)
    if len(all_failures) > 100:
        print(f"  ... ({len(all_failures) - 100} more)", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

