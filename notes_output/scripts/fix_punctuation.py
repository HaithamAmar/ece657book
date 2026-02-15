#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fnmatch
from pathlib import Path

PROTECTED_COMMANDS = (
    "cite", "Cite", "citet", "Citet", "citep", "Citep",
    "cref", "Cref", "crefrange", "Crefrange", "ref", "eqref", "autoref", "label",
    "url", "href", "path", "includegraphics", "begin", "end",
)

SKIP_ENVIRONMENTS = {
    "verbatim",
    "verbatim*",
    "Verbatim",
    "lstlisting",
    "minted",
}


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


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


def _protected_spans(line: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    i = 0
    while i < len(line):
        if line[i] != "\\":
            i += 1
            continue
        j = i + 1
        while j < len(line) and line[j].isalpha():
            j += 1
        cmd = line[i + 1 : j]
        if cmd in PROTECTED_COMMANDS:
            # Protect *all* immediate brace arguments for this command.
            # Many commands we protect (e.g., \Crefrange{..}{..}) take multiple
            # brace groups; touching inside them can break labels/citations.
            k = j
            while k < len(line) and line[k].isspace():
                k += 1
            last_end = None
            while k < len(line) and line[k] == "{":
                depth = 0
                start = k
                m = k
                while m < len(line):
                    if line[m] == "{":
                        depth += 1
                    elif line[m] == "}":
                        depth -= 1
                        if depth == 0:
                            spans.append((start, m + 1))
                            last_end = m + 1
                            k = last_end
                            while k < len(line) and line[k].isspace():
                                k += 1
                            break
                    m += 1
                else:
                    # Unbalanced; abort protecting this command.
                    last_end = None
                    break
            if last_end is not None:
                i = last_end
                continue
        i = j
    return spans


def _is_protected(idx: int, spans: list[tuple[int, int]]) -> bool:
    for start, end in spans:
        if start <= idx < end:
            return True
    return False


def _fix_line(line: str) -> str:
    if not line or line.lstrip().startswith("%"):
        return line

    spans = _protected_spans(line)

    # 1) Remove spaces before punctuation.
    out = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch.isspace():
            j = i
            while j < len(line) and line[j].isspace():
                j += 1
            if j < len(line) and line[j] in ",.;:!?":
                if not _is_protected(j, spans):
                    out.append(line[j])
                    i = j + 1
                    continue
            out.append(line[i])
            i += 1
            continue
        out.append(ch)
        i += 1
    line = "".join(out)

    spans = _protected_spans(line)

    # 2) Add space after , ; : when missing and safe.
    out = []
    i = 0
    while i < len(line):
        ch = line[i]
        if ch in ",;:":
            if i + 1 < len(line):
                nxt = line[i + 1]
                if nxt.isalpha() and not _is_protected(i, spans) and not _is_protected(i + 1, spans):
                    out.append(ch)
                    out.append(" ")
                    i += 1
                    continue
        out.append(ch)
        i += 1
    line = "".join(out)

    # 3) Fix "Figure 1to" / "Table 2to" / "Chapter 3to" patterns.
    for word in ("Figure", "Table", "Chapter", "Section", "Appendix", "Equation", "Eq."):
        line = _fix_digit_to(line, word)

    return line


def _fix_digit_to(line: str, word: str) -> str:
    import re
    pattern = rf"\\b{re.escape(word)}\\s+(\\d+)to\\b"
    return re.sub(pattern, rf"{word} \\1 to", line)


def _fix_file(path: Path) -> bool:
    before = _read_text(path)
    in_skip_env = False
    out_lines: list[str] = []
    for raw_line in before.splitlines():
        line = raw_line
        stripped = line.strip()
        if stripped.startswith("\\begin{"):
            env = stripped[7:].split("}", 1)[0]
            if env in SKIP_ENVIRONMENTS:
                in_skip_env = True
        if stripped.startswith("\\end{"):
            env = stripped[5:].split("}", 1)[0]
            if env in SKIP_ENVIRONMENTS:
                in_skip_env = False

        if in_skip_env:
            out_lines.append(line)
            continue

        out_lines.append(_fix_line(line))

    after = "\n".join(out_lines) + "\n"
    if before != after:
        path.write_text(after, encoding="utf-8")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Conservative punctuation spacing cleanup for LaTeX.")
    parser.add_argument("--root", default=".", help="notes_output root directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    changed = []
    for path in _iter_files(root):
        if _fix_file(path):
            changed.append(path.relative_to(root).as_posix())

    if changed:
        print(f"Changed {len(changed)} file(s):")
        for rel in changed:
            print(f"- {rel}")
    else:
        print("No punctuation issues detected by conservative rules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
