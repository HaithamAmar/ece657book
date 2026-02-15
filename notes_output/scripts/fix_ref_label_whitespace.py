#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fnmatch
import re
from pathlib import Path


LABEL_PREFIXES = ("chap", "fig", "tab", "eq", "sec", "app")


def _iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    exclude_globs = [
        "build/**",
        "_archive/**",
        "archive/**",
        "artifacts/**",
        "upload/**",
        "review/**",
        "*.aux",
        "*.bbl",
        "*.blg",
        "*.log",
        "*.lof",
        "*.lot",
        "*.toc",
    ]
    for path in root.rglob("*.tex"):
        rel = path.relative_to(root).as_posix()
        if any(fnmatch.fnmatch(rel, g) for g in exclude_globs):
            continue
        files.append(path)
    return files


def _fix_text(text: str) -> str:
    # Remove accidental whitespace after ':' in common label prefixes when they
    # occur inside brace-delimited macro args or label definitions.
    #
    # Examples to fix:
    #   \Cref{chap: logistic}     -> \Cref{chap:logistic}
    #   \Crefrange{eq:foo}{eq: bar} -> \Crefrange{eq:foo}{eq:bar}
    #   \label{fig: myfig}        -> \label{fig:myfig}
    prefixes = "|".join(map(re.escape, LABEL_PREFIXES))
    # After "{" or "," inside a brace group.
    text = re.sub(rf"([{{,])\s*({prefixes}):\s+([^\s}}])", r"\1\2:\3", text)
    # Inside \label{...} specifically (more permissive on label body).
    text = re.sub(rf"(\\label\{{)\s*({prefixes}):\s+", r"\1\2:", text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fix accidental whitespace in LaTeX label keys (e.g., 'chap: foo' -> 'chap:foo')."
    )
    parser.add_argument("--root", default=".", help="notes_output root directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    changed: list[str] = []
    for path in _iter_files(root):
        before = path.read_text(encoding="utf-8", errors="ignore")
        after = _fix_text(before)
        if after != before:
            path.write_text(after, encoding="utf-8")
            changed.append(path.relative_to(root).as_posix())

    if changed:
        print(f"Changed {len(changed)} file(s):")
        for rel in changed:
            print(f"- {rel}")
    else:
        print("No label-whitespace issues detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
