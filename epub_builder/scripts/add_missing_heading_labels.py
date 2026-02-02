#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


_LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
_CHAPTER_LABEL_RE = re.compile(r"\\label\{(chap|app):([^}]+)\}")


def _find_matching(s: str, *, start: int, open_ch: str, close_ch: str) -> int | None:
    if start < 0 or start >= len(s) or s[start] != open_ch:
        return None
    depth = 0
    i = start
    while i < len(s):
        ch = s[i]
        if ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return None


def _iter_headings(text: str):
    """
    Yield tuples of (cmd, indent, title, end_pos) for each subsection/subsubsection.

    `end_pos` points to the character *after* the closing `}` of the heading's
    required argument.
    """
    i = 0
    while True:
        m = re.search(r"(^[ \t]*)\\(subsection|subsubsection)\b", text[i:], flags=re.MULTILINE)
        if not m:
            return
        indent = m.group(1)
        cmd = m.group(2)
        cmd_start = i + m.start(0) + len(indent)
        j = i + m.end(0)

        # Skip starred variants.
        if j < len(text) and text[j] == "*":
            i = j + 1
            continue

        # Optional short title [...]
        if j < len(text) and text[j] == "[":
            j_end = _find_matching(text, start=j, open_ch="[", close_ch="]")
            if j_end is None:
                i = j + 1
                continue
            j = j_end + 1

        # Required title { ... } (brace-matched).
        while j < len(text) and text[j].isspace():
            j += 1
        if j >= len(text) or text[j] != "{":
            i = j + 1
            continue
        t_end = _find_matching(text, start=j, open_ch="{", close_ch="}")
        if t_end is None:
            i = j + 1
            continue
        title = text[j + 1 : t_end]
        yield cmd, indent, title, t_end + 1
        i = t_end + 1


def _slugify(title: str) -> str:
    s = title
    s = re.sub(r"\\[a-zA-Z@]+(\*?)", " ", s)  # control sequences
    s = s.replace("{", " ").replace("}", " ")
    s = s.replace("[", " ").replace("]", " ")
    s = s.replace("$", " ")
    s = s.replace("\\(", " ").replace("\\)", " ").replace("\\[", " ").replace("\\]", " ")
    s = re.sub(r"[^A-Za-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_").lower()
    return s or "untitled"


def _collect_existing_labels(root: Path) -> set[str]:
    labels: set[str] = set()
    for path in sorted(root.rglob("*.tex")):
        if "_archive" in path.parts or "archive" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for m in _LABEL_RE.finditer(text):
            labels.add(m.group(1).strip())
    return labels


def _find_chapter_key(text: str) -> str | None:
    m = _CHAPTER_LABEL_RE.search(text)
    if not m:
        return None
    return m.group(2).strip() or None


def _has_label_soon(text: str, *, start: int, end: int) -> bool:
    """
    Return True if a \\label{...} appears between end-of-heading and the next
    LaTeX command/blank-line boundary.
    """
    window = text[end : min(len(text), end + 400)]
    # Stop at a double newline (paragraph break) to avoid catching later labels.
    stop = window.find("\n\n")
    if stop != -1:
        window = window[:stop]
    # Stop at another heading command.
    stop2 = re.search(r"^\s*\\(subsection|subsubsection|section)\b", window, flags=re.MULTILINE)
    if stop2:
        window = window[: stop2.start()]
    return bool(_LABEL_RE.search(window))


@dataclass(frozen=True)
class FileChange:
    path: Path
    added: int


def add_missing_heading_labels(*, root: Path, dry_run: bool) -> list[FileChange]:
    existing = _collect_existing_labels(root)
    changes: list[FileChange] = []

    for path in sorted(root.rglob("*.tex")):
        if "_archive" in path.parts or "archive" in path.parts:
            continue
        if path.name in {"ece657_notes.tex", "ece657_ebook.tex"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue

        chapter_key = _find_chapter_key(text)
        if not chapter_key:
            continue

        out: list[str] = []
        last = 0
        added = 0
        for cmd, indent, title, end in _iter_headings(text):
            title = title.strip()
            if _has_label_soon(text, start=end, end=end):
                continue

            slug = _slugify(title)
            base = f"sec:{chapter_key}_{slug}"
            if cmd == "subsubsection":
                base = base + "_sub"
            lab = base
            n = 2
            while lab in existing:
                lab = f"{base}_{n}"
                n += 1

            existing.add(lab)
            out.append(text[last:end])
            out.append(f"\n{indent}\\label{{{lab}}}")
            last = end
            added += 1

        if added == 0:
            continue
        out.append(text[last:])
        new_text = "".join(out)
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")
        changes.append(FileChange(path=path, added=added))

    return changes


def main() -> None:
    ap = argparse.ArgumentParser(description="Add missing \\label{...} to subsection/subsubsection headings in notes_output.")
    ap.add_argument("--root", default="notes_output", help="Root directory containing LaTeX sources (default: notes_output)")
    ap.add_argument("--dry-run", action="store_true", help="Do not modify files; print what would change")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        raise SystemExit(f"Missing root dir: {root}")

    changes = add_missing_heading_labels(root=root, dry_run=args.dry_run)
    total = sum(c.added for c in changes)
    if not changes:
        print("No missing heading labels found.")
        return

    for c in changes:
        rel = c.path.relative_to(Path.cwd())
        print(f"{rel}: added {c.added} labels")
    print(f"Total labels added: {total}")


if __name__ == "__main__":
    main()
