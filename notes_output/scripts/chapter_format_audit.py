#!/usr/bin/env python3
"""
Chapter format audit for Modern Intelligent Systems.

Reads chapter inputs from notes_output/book_chapters.tex and checks each chapter
against the formatting rules documented in notes_output/ONBOARDING.md.

This is intentionally heuristic (regex based) and designed to catch drift early.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]  # notes_output/
BOOK_CHAPTERS = ROOT / "book_chapters.tex"
ONBOARDING = ROOT / "ONBOARDING.md"
QC_DIR = ROOT / "artifacts" / "qc"


INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
TITLE_RE = re.compile(r"title\s*=\s*\{([^}]*)\}")

# Match: \begin{tcolorbox}[<opts>]
TCOLORBOX_BEGIN_RE = re.compile(r"\\begin\{tcolorbox\}\[(.*?)\]", re.DOTALL)

PARA_WHERE_NEXT_RE = re.compile(r"\\paragraph\{\s*Where\s+we\s+head\s+next\.\s*\}")
PARA_REFERENCES_RE = re.compile(r"\\paragraph\{\s*References\.\s*\}")

TITLE_LEARNING_OUTCOMES_RE = re.compile(r"title\s*=\s*\{\s*Learning\s+Outcomes\s*\}")
TITLE_DESIGN_MOTIF_RE = re.compile(r"title\s*=\s*\{\s*Design\s+motif\s*\}")
TITLE_KEY_TAKEAWAYS_RE = re.compile(r"title\s*=\s*\{\s*Key\s+takeaways\s*\}")
TITLE_EXERCISES_RE = re.compile(r"title\s*=\s*\{\s*Exercises\s+and\s+lab\s+ideas\s*\}")

INLINE_DESIGN_MOTIF_RE = re.compile(r"\\textit\{\s*Design\s+motif\s*:", re.IGNORECASE)
INLINE_KEY_TAKEAWAYS_RE = re.compile(r"\\textbf\{\s*Key\s+takeaways\s*\}", re.IGNORECASE)

OPENING_CREF_RE = re.compile(r"\\Cref\{")

# "Course voice" phrases to avoid in numbered chapters (per ONBOARDING.md).
BANNED_PHRASES = [
    r"\btoday\b",
    r"\blast time\b",
    r"\bthis course\b",
    r"\bin (the )?course\b",
    r"\blecture\b",
    r"\bthese notes\b",
    r"\bnext chapter\b",
]
BANNED_RE = re.compile("|".join(BANNED_PHRASES), re.IGNORECASE)


@dataclass
class ChapterAudit:
    chapter_index: int
    chapter_path: Path
    issues: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def ok(self) -> bool:
        return not self.issues


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="strict")


def _is_ascii(s: str) -> bool:
    try:
        s.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False


def _find_inputs(book_chapters_tex: str) -> list[str]:
    inputs: list[str] = []
    for m in INPUT_RE.finditer(book_chapters_tex):
        p = m.group(1).strip()
        if p:
            inputs.append(p)
    return inputs


def _scan_tcolorbox_titles(tex: str) -> list[str]:
    titles: list[str] = []
    for m in TCOLORBOX_BEGIN_RE.finditer(tex):
        opts = m.group(1)
        tm = TITLE_RE.search(opts)
        if tm:
            titles.append(tm.group(1).strip())
        else:
            titles.append("")
    return titles


def _scan_opening_window(tex: str, max_lines: int = 120) -> str:
    lines = tex.splitlines()
    return "\n".join(lines[:max_lines])


def audit_chapter(chapter_index: int, chapter_path: Path, tex: str) -> ChapterAudit:
    a = ChapterAudit(chapter_index=chapter_index, chapter_path=chapter_path)

    if not _is_ascii(tex):
        a.issues.append("Non-ASCII characters found in .tex source (must be ASCII-only).")

    titles = _scan_tcolorbox_titles(tex)

    # Required opening blocks.
    if not TITLE_LEARNING_OUTCOMES_RE.search(tex):
        a.issues.append('Missing tcolorbox titled "Learning Outcomes" near chapter start.')

    if TITLE_DESIGN_MOTIF_RE.search(tex):
        pass
    elif INLINE_DESIGN_MOTIF_RE.search(tex):
        a.issues.append('Design motif appears inline; convert to tcolorbox titled "Design motif".')
    else:
        a.issues.append('Missing "Design motif" hook (tcolorbox titled "Design motif").')

    opening = _scan_opening_window(tex)
    if not OPENING_CREF_RE.search(opening):
        a.warnings.append("Opening bridge lacks a \\Cref{...} cross-reference (recommended).")

    # End-of-chapter kit.
    if not TITLE_KEY_TAKEAWAYS_RE.search(tex):
        if INLINE_KEY_TAKEAWAYS_RE.search(tex):
            a.issues.append('Key takeaways box exists but is not titled "Key takeaways" (tcolorbox title=...).')
        else:
            a.issues.append('Missing tcolorbox titled "Key takeaways" near chapter end.')

    if not TITLE_EXERCISES_RE.search(tex):
        a.issues.append('Missing tcolorbox titled "Exercises and lab ideas" near chapter end.')

    if not PARA_WHERE_NEXT_RE.search(tex):
        a.issues.append('Missing paragraph titled "Where we head next." near chapter end.')

    # Tcolorbox hygiene: summary boxes without titles tend to be ambiguous in EPUB.
    untitled = sum(1 for t in titles if t == "")
    if untitled:
        a.warnings.append(f"{untitled} tcolorbox(es) appear without a title=... option.")

    # "Course voice" phrases (heuristic).
    banned_hits = sorted(set(m.group(0) for m in BANNED_RE.finditer(tex)))
    if banned_hits:
        a.warnings.append(f'Contains course-voice phrasing (consider rewriting): {", ".join(banned_hits)}')

    return a


def render_report(audits: Iterable[ChapterAudit]) -> str:
    audits = list(audits)
    total = len(audits)
    ok = sum(1 for a in audits if a.ok())
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines: list[str] = []
    lines.append(f"# Chapter format audit (Chapters 1-{total})")
    lines.append("")
    lines.append(f"- Timestamp: {now}")
    lines.append(f"- Rules source: `{ONBOARDING}`")
    lines.append(f"- Chapter list: `{BOOK_CHAPTERS}`")
    lines.append(f"- Pass: {ok}/{total}")
    lines.append("")

    for a in audits:
        rel = a.chapter_path.as_posix()
        status = "PASS" if a.ok() else "FAIL"
        lines.append(f"## Chapter {a.chapter_index}: `{rel}` — {status}")
        if a.issues:
            lines.append("")
            lines.append("Issues:")
            for it in a.issues:
                lines.append(f"- {it}")
        if a.warnings:
            lines.append("")
            lines.append("Warnings:")
            for it in a.warnings:
                lines.append(f"- {it}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="Write report to notes_output/artifacts/qc/")
    args = ap.parse_args()

    book_tex = _read_text(BOOK_CHAPTERS)
    inputs = _find_inputs(book_tex)
    if not inputs:
        raise SystemExit(f"No chapters found in {BOOK_CHAPTERS}")

    audits: list[ChapterAudit] = []
    for idx, rel in enumerate(inputs, start=1):
        path = (ROOT / rel).resolve()
        tex = _read_text(path)
        audits.append(audit_chapter(idx, path.relative_to(ROOT), tex))

    report = render_report(audits)
    print(report)

    if args.write:
        QC_DIR.mkdir(parents=True, exist_ok=True)
        stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        out = QC_DIR / f"chapter_format_audit_{stamp}.md"
        out.write_text(report, encoding="utf-8")
        print(f"Wrote: {out}")

    # Non-zero exit if any failures (helps CI-like usage).
    return 0 if all(a.ok() for a in audits) else 2


if __name__ == "__main__":
    raise SystemExit(main())
