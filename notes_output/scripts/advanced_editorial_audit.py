#!/usr/bin/env python3
"""
Advanced editorial audit helpers for Modern Intelligent Systems.

This script is *not* a replacement for human editorial review. It produces a
chapter-by-chapter outline + structural metrics to make a narrative audit
repeatable and to help future LLMs/editors spot drift after rearrangements.

Outputs a Markdown report. Intended usage:
  python3 notes_output/scripts/advanced_editorial_audit.py --write
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]  # notes_output/
BOOK_CHAPTERS = ROOT / "book_chapters.tex"
BOOK_APPENDICES = ROOT / "book_appendices.tex"
EBOOK_ENTRYPOINT = ROOT / "ece657_ebook.tex"
QC_DIR = ROOT / "artifacts" / "qc"


INPUT_RE = re.compile(r"\\input\{([^}]+)\}")

SECTION_RE = re.compile(r"^\\section\*?\{([^}]*)\}", re.MULTILINE)
SUBSECTION_RE = re.compile(r"^\\subsection\*?\{([^}]*)\}", re.MULTILINE)
SUBSUBSECTION_RE = re.compile(r"^\\subsubsection\*?\{([^}]*)\}", re.MULTILINE)
PARA_RE = re.compile(r"^\\paragraph\*?\{([^}]*)\}", re.MULTILINE)
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")

TCOLORBOX_BEGIN_RE = re.compile(r"\\begin\{tcolorbox\}\[(.*?)\]", re.DOTALL)
TCB_TITLE_RE = re.compile(r"title\\s*=\\s*\\{([^}]*)\\}")

CAPTION_SCHEMATIC_RE = re.compile(r"\\caption\{\s*(Schematic:)", re.IGNORECASE)
# Plain-text numeric chapter references should be rare; prefer \\Cref{chap:...}
# or \\ChapterRef{chap:...}{fallback}.
PLAIN_CHAPTER_NUM_RE = re.compile(r"\bChapter\s+\d+\b")
NLP_TERM_RE = re.compile(r"\bNLP\b|\bnatural language\b", re.IGNORECASE)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="strict")


def _strip_comments(tex: str) -> str:
    """
    Remove LaTeX comments for heuristic scanning.

    This is intentionally conservative and line-based:
    - Treat % as a comment start unless it is escaped as \\%.
    - Preserve line breaks to keep other heuristics stable.
    """
    out_lines: list[str] = []
    for line in tex.splitlines():
        out_lines.append(re.sub(r"(?<!\\\\)%.*$", "", line))
    return "\n".join(out_lines)


def _find_inputs(tex: str) -> list[str]:
    inputs: list[str] = []
    for m in INPUT_RE.finditer(tex):
        p = m.group(1).strip()
        if p:
            inputs.append(p)
    return inputs


def _scan_tcolorbox_titles(tex: str) -> list[str]:
    titles: list[str] = []
    for m in TCOLORBOX_BEGIN_RE.finditer(tex):
        opts = m.group(1)
        tm = TCB_TITLE_RE.search(opts)
        titles.append(tm.group(1).strip() if tm else "")
    return titles


def _first_label_near_section(tex: str, max_lines: int = 40) -> str | None:
    """
    Best-effort: find the first \\label{...} that appears close to the first
    \\section{...}. This is a heuristic, but it helps identify chap/app labels.
    """
    section = SECTION_RE.search(tex)
    if not section:
        return None
    start = section.start()
    window = "\n".join(tex[start:].splitlines()[:max_lines])
    m = LABEL_RE.search(window)
    return m.group(1) if m else None


@dataclass(frozen=True)
class UnitAudit:
    index: int
    kind: str  # "chapter" | "appendix"
    relpath: str
    title: str | None
    label: str | None
    section_count: int
    subsection_count: int
    subsubsection_count: int
    paragraph_count: int
    figure_count: int
    table_count: int
    tcolorbox_titles: tuple[str, ...]
    schematic_caption_count: int
    plain_chapter_num_count: int
    nlp_term_count: int

    @property
    def tcolorbox_title_counts(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for t in self.tcolorbox_titles:
            counts[t] = counts.get(t, 0) + 1
        return counts


def audit_unit(index: int, kind: str, relpath: str, tex: str) -> UnitAudit:
    tex_no_comments = _strip_comments(tex)
    section_title = None
    section_m = SECTION_RE.search(tex_no_comments)
    if section_m:
        section_title = section_m.group(1).strip()

    label = _first_label_near_section(tex_no_comments)

    tcb_titles = tuple(_scan_tcolorbox_titles(tex_no_comments))

    return UnitAudit(
        index=index,
        kind=kind,
        relpath=relpath,
        title=section_title,
        label=label,
        section_count=len(SECTION_RE.findall(tex_no_comments)),
        subsection_count=len(SUBSECTION_RE.findall(tex_no_comments)),
        subsubsection_count=len(SUBSUBSECTION_RE.findall(tex_no_comments)),
        paragraph_count=len(PARA_RE.findall(tex_no_comments)),
        figure_count=tex_no_comments.count("\\begin{figure}"),
        table_count=tex_no_comments.count("\\begin{table}"),
        tcolorbox_titles=tcb_titles,
        schematic_caption_count=len(CAPTION_SCHEMATIC_RE.findall(tex_no_comments)),
        plain_chapter_num_count=len(PLAIN_CHAPTER_NUM_RE.findall(tex_no_comments)),
        nlp_term_count=len(NLP_TERM_RE.findall(tex_no_comments)),
    )


def _render_outline(tex: str, max_subsections: int = 60) -> list[str]:
    lines: list[str] = []
    subs = SUBSECTION_RE.findall(tex)
    if subs:
        lines.append("Subsections:")
        for name in subs[:max_subsections]:
            lines.append(f"- {name.strip()}")
        if len(subs) > max_subsections:
            lines.append(f"- … ({len(subs) - max_subsections} more)")
    else:
        lines.append("Subsections: (none found)")
    return lines


def render_report(chapters: Iterable[UnitAudit], appendices: Iterable[UnitAudit]) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chapters = list(chapters)
    appendices = list(appendices)

    lines: list[str] = []
    lines.append("# Advanced editorial audit (outline + structural metrics)")
    lines.append("")
    lines.append(f"- Timestamp: {now}")
    lines.append(f"- Chapters source: `{BOOK_CHAPTERS}`")
    lines.append(f"- Appendices source: `{BOOK_APPENDICES}`")
    lines.append(f"- Entry point: `{EBOOK_ENTRYPOINT}`")
    lines.append("")
    lines.append("This report is meant to support *editorial* review by making it easy to spot:")
    lines.append("- unusually long/short chapters,")
    lines.append("- missing scaffolding boxes,")
    lines.append("- stale numeric chapter references,")
    lines.append("- schematic caption overuse,")
    lines.append("- NLP term usage and cross-part continuity hints.")
    lines.append("")

    def render_unit(u: UnitAudit) -> None:
        lines.append(f"## {u.kind.title()} {u.index}: `{u.relpath}`")
        title = u.title or "(missing \\section{...})"
        label = u.label or "(missing \\label{...} near chapter start)"
        lines.append("")
        lines.append(f"- Title: {title}")
        lines.append(f"- Label: `{label}`")
        lines.append(
            "- Headings:"
            f" sections={u.section_count},"
            f" subsections={u.subsection_count},"
            f" subsubsections={u.subsubsection_count},"
            f" paragraphs={u.paragraph_count}"
        )
        lines.append(f"- Floats: figures={u.figure_count}, tables={u.table_count}")
        lines.append(
            "- Text signals:"
            f" schematic-captions={u.schematic_caption_count},"
            f" plain-\"Chapter N\"={u.plain_chapter_num_count},"
            f" NLP-terms={u.nlp_term_count}"
        )

        tcb_counts = u.tcolorbox_title_counts
        # Only show the most relevant titles (others are noise).
        interesting = [
            "Learning Outcomes",
            "Design motif",
            "Risk & audit",
            "Key takeaways",
            "Exercises and lab ideas",
            "Part I takeaways",
            "Part II takeaways",
            "Part III takeaways",
            "Part IV takeaways",
        ]
        present = {k: tcb_counts.get(k, 0) for k in interesting if tcb_counts.get(k, 0)}
        if present:
            lines.append("- Scaffolding boxes:")
            for k in interesting:
                v = present.get(k)
                if v:
                    lines.append(f"  - {k}: {v}")

        lines.append("")

    # Chapters
    lines.append("## Chapters")
    lines.append("")
    for u in chapters:
        render_unit(u)

    # Appendices
    if appendices:
        lines.append("## Appendices")
        lines.append("")
        for u in appendices:
            render_unit(u)

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="Write report to notes_output/artifacts/qc/")
    args = ap.parse_args()

    chapters_inputs = _find_inputs(_read_text(BOOK_CHAPTERS))
    if not chapters_inputs:
        raise SystemExit(f"No chapter inputs found in {BOOK_CHAPTERS}")

    appendix_inputs = _find_inputs(_read_text(BOOK_APPENDICES))

    chapters: list[UnitAudit] = []
    for idx, rel in enumerate(chapters_inputs, start=1):
        path = (ROOT / rel).resolve()
        tex = _read_text(path)
        chapters.append(audit_unit(idx, "chapter", rel, tex))

    appendices: list[UnitAudit] = []
    for idx, rel in enumerate(appendix_inputs, start=1):
        path = (ROOT / rel).resolve()
        tex = _read_text(path)
        appendices.append(audit_unit(idx, "appendix", rel, tex))

    report = render_report(chapters, appendices)
    print(report)

    if args.write:
        QC_DIR.mkdir(parents=True, exist_ok=True)
        stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        out = QC_DIR / f"advanced_editorial_audit_{stamp}.md"
        out.write_text(report, encoding="utf-8")
        print(f"Wrote: {out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
