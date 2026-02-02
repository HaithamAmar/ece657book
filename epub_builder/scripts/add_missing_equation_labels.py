#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


_LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
_CHAPTER_LABEL_RE = re.compile(r"\\label\{(chap|app):([^}]+)\}")


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


def _find_chapter_key(text: str, *, fallback: str) -> str:
    m = _CHAPTER_LABEL_RE.search(text)
    if not m:
        return fallback
    key = m.group(2).strip()
    return key or fallback


def _hash_block(s: str) -> str:
    # Normalize whitespace so trivial reflows don't rename labels.
    norm = re.sub(r"\s+", " ", s.strip())
    return hashlib.sha1(norm.encode("utf-8")).hexdigest()[:10]


@dataclass(frozen=True)
class FileChange:
    path: Path
    added: int


def add_missing_equation_labels(*, root: Path, dry_run: bool) -> list[FileChange]:
    """
    Add `\\label{eq:auto_...}` to unlabeled `equation` environments.

    Notes:
    - We intentionally do NOT touch `align` environments here, because they can
      contain multiple numbered lines; auto-labeling those would be misleading
      in EPUB (we currently render one visible number per labeled environment).
    - This script is idempotent: labels are derived from a content hash.
    """
    existing = _collect_existing_labels(root)
    changes: list[FileChange] = []

    begin = r"\begin{equation}"
    end = r"\end{equation}"

    for path in sorted(root.rglob("*.tex")):
        if "_archive" in path.parts or "archive" in path.parts:
            continue
        if path.name in {"ece657_notes.tex", "ece657_ebook.tex"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue

        chapter_key = _find_chapter_key(text, fallback=path.stem)

        out: list[str] = []
        i = 0
        added = 0
        while True:
            s = text.find(begin, i)
            if s == -1:
                out.append(text[i:])
                break
            out.append(text[i:s])
            e = text.find(end, s + len(begin))
            if e == -1:
                out.append(text[s:])
                break
            block = text[s : e + len(end)]

            # Skip if already has an eq: label.
            if re.search(r"\\label\{eq:[^}]+\}", block):
                out.append(block)
                i = e + len(end)
                continue

            # Derive a stable label from block content.
            h = _hash_block(block)
            base = f"eq:auto_{chapter_key}_{h}"
            lab = base
            n = 2
            while lab in existing:
                lab = f"{base}_{n}"
                n += 1
            existing.add(lab)

            # Insert label immediately before \end{equation}, keeping indentation.
            indent = ""
            m_indent = re.search(r"\n([ \t]*)\\end\{equation\}", block)
            if m_indent:
                indent = m_indent.group(1)
            new_block = block.replace(end, f"{indent}\\label{{{lab}}}\n{indent}{end}", 1)
            out.append(new_block)
            i = e + len(end)
            added += 1

        if added == 0:
            continue
        new_text = "".join(out)
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")
        changes.append(FileChange(path=path, added=added))

    return changes


def main() -> None:
    ap = argparse.ArgumentParser(description="Add missing equation labels (eq:auto_*) to notes_output LaTeX sources.")
    ap.add_argument("--root", default="notes_output", help="Root directory containing LaTeX sources (default: notes_output)")
    ap.add_argument("--dry-run", action="store_true", help="Do not modify files; print what would change")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        raise SystemExit(f"Missing root dir: {root}")

    changes = add_missing_equation_labels(root=root, dry_run=args.dry_run)
    total = sum(c.added for c in changes)
    if not changes:
        print("No missing equation labels found.")
        return

    for c in changes:
        rel = c.path.relative_to(Path.cwd())
        print(f"{rel}: added {c.added} equation labels")
    print(f"Total equation labels added: {total}")


if __name__ == "__main__":
    main()

