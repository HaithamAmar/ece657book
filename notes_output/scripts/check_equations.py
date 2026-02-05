#!/usr/bin/python3
from __future__ import annotations

"""
Equation hygiene checks (publish-grade guardrail).

Goals:
- Keep equation numbering consistent and meaningful (for PDF *and* EPUB).
- Ensure any *numbered* equation-like environment has an explicit `\\label{eq:...}`.
- Prevent "labels that can't be numbered" (e.g., `\\label{eq:...}` inside `\\[...\\]`
  or `equation*`), which breaks EPUB equation numbering (numbers come from the `.aux`).
- Avoid legacy display-math `$$ ... $$` which is brittle for both LaTeX tooling and Pandoc.

Notes:
- We intentionally do NOT require every `\\[...\\]` block to be numbered: numbering
  every intermediate step would shift equation numbers globally.
- We flag inline `\\(\\displaystyle ...\\)` outside TikZ as a warning (prefer `\\[...\\]`).
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


_EQ_LABEL_RE = re.compile(r"\\label\{(eq:[^}]+)\}")
_BEGIN_RE = re.compile(r"\\begin\{([^}]+)\}")
_END_RE = re.compile(r"\\end\{([^}]+)\}")

_INLINE_DISPLAYSTYLE = r"\(\displaystyle"


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _strip_comments(tex: str) -> str:
    out: list[str] = []
    for line in tex.splitlines(True):
        # Keep lines inside verbatim-ish contexts intact is too expensive here;
        # this is a conservative heuristic for our sources.
        if "%" not in line:
            out.append(line)
            continue
        buf = []
        i = 0
        while i < len(line):
            if line[i] == "%":
                # Escaped percent \% is not a comment.
                if i > 0 and line[i - 1] == "\\":
                    buf.append("%")
                    i += 1
                    continue
                break
            buf.append(line[i])
            i += 1
        out.append("".join(buf) + ("\n" if line.endswith("\n") else ""))
    return "".join(out)


def _tex_files(*, root: Path) -> list[Path]:
    files: list[Path] = []
    for p in root.rglob("*.tex"):
        if "artifacts" in p.parts:
            continue
        if "archive" in p.parts:
            continue
        files.append(p)
    return sorted(files)


def _find_env_blocks(tex: str, *, env: str) -> list[tuple[int, int, str]]:
    begin = f"\\begin{{{env}}}"
    end = f"\\end{{{env}}}"
    blocks: list[tuple[int, int, str]] = []
    i = 0
    while True:
        s = tex.find(begin, i)
        if s == -1:
            break
        e = tex.find(end, s + len(begin))
        if e == -1:
            break
        blocks.append((s, e + len(end), tex[s : e + len(end)]))
        i = e + len(end)
    return blocks


def _remove_tikz(tex: str) -> str:
    # Avoid flagging \(\displaystyle ...\) inside TikZ node text; those are rendered as images.
    begin = "\\begin{tikzpicture}"
    end = "\\end{tikzpicture}"
    out: list[str] = []
    i = 0
    while True:
        s = tex.find(begin, i)
        if s == -1:
            out.append(tex[i:])
            break
        out.append(tex[i:s])
        e = tex.find(end, s + len(begin))
        if e == -1:
            break
        block = tex[s : e + len(end)]
        # Preserve line numbers by replacing the TikZ block with the same number of newlines.
        out.append("\n" * max(1, block.count("\n")))
        i = e + len(end)
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT), help="Root directory containing LaTeX sources (default: notes_output)")
    ap.add_argument("--fail-on-warn", action="store_true", help="Treat warnings as errors")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"ERROR: root dir not found: {root}", file=sys.stderr)
        return 2

    tex_files = _tex_files(root=root)
    errors: list[Finding] = []
    warns: list[Finding] = []

    numbered_envs = ["equation", "align", "gather", "multline", "alignat", "flalign"]
    starred_envs = [f"{e}*" for e in numbered_envs]

    for p in tex_files:
        raw = _read_text(p)
        tex = _strip_comments(raw)

        # Disallow $$ ... $$ (legacy display math).
        if "$$" in tex:
            # Report each line that contains $$.
            for i, line in enumerate(tex.splitlines(), start=1):
                if "$$" in line:
                    errors.append(Finding(where=f"{p.relative_to(root)}:{i}", msg="Found '$$' display math; use \\[...\\] or amsmath environments"))

        # Starred equation-like envs must not carry eq: labels (they won't have stable numbers).
        for env in starred_envs:
            for s, _, block in _find_env_blocks(tex, env=env):
                if _EQ_LABEL_RE.search(block):
                    line = tex.count("\n", 0, s) + 1
                    errors.append(Finding(where=f"{p.relative_to(root)}:{line}", msg=f"{env} contains \\label{{eq:...}}; use the non-starred environment if numbering is intended"))

        # Non-starred equation-like envs must contain at least one eq: label.
        for env in numbered_envs:
            for s, _, block in _find_env_blocks(tex, env=env):
                if not _EQ_LABEL_RE.search(block):
                    line = tex.count("\n", 0, s) + 1
                    errors.append(Finding(where=f"{p.relative_to(root)}:{line}", msg=f"{env} has no \\label{{eq:...}} (EPUB shows numbers only for labeled equations via .aux)"))

        # Labels inside \[...\] are a common footgun: LaTeX doesn't number them by default.
        # If numbering is needed, prefer `equation` or `align`.
        #
        # Guardrail: do not confuse display math `\[` with line breaks `\\[<len>]`
        # (common inside TikZ nodes and tabular material).
        i = 0
        while True:
            s = tex.find("\\[", i)
            if s == -1:
                break
            if s > 0 and tex[s - 1] == "\\":  # skip `\\[` (newline + optional spacing)
                i = s + 2
                continue
            e = tex.find("\\]", s + 2)
            if e == -1:
                break
            while e > 0 and tex[e - 1] == "\\":  # skip `\\]` (rare, but symmetric guard)
                e = tex.find("\\]", e + 2)
                if e == -1:
                    break
            if e == -1:
                break
            block = tex[s : e + 2]
            if _EQ_LABEL_RE.search(block) and "\\tag{" not in block:
                line = tex.count("\n", 0, s) + 1
                errors.append(Finding(where=f"{p.relative_to(root)}:{line}", msg="\\[...\\] contains \\label{eq:...} without \\tag{...}; LaTeX won't assign a number—use equation/align instead"))
            i = e + 2

        # Warn on inline displaystyle outside TikZ (prefer display math).
        # (The EPUB builder also tries to promote these, but source should be clean.)
        cleaned = _remove_tikz(tex)
        if _INLINE_DISPLAYSTYLE in cleaned:
            for i, line in enumerate(cleaned.splitlines(), start=1):
                if _INLINE_DISPLAYSTYLE in line:
                    warns.append(Finding(where=f"{p.relative_to(root)}:{i}", msg="Inline \\(\\displaystyle ...\\) found; prefer \\[...\\] or an amsmath environment"))

    if errors:
        print("ERROR: equation hygiene failures:", file=sys.stderr)
        for f in errors[:200]:
            print(f"  - {f.where}: {f.msg}", file=sys.stderr)
        if len(errors) > 200:
            print(f"  ... ({len(errors) - 200} more)", file=sys.stderr)
    if warns:
        print("WARN: equation hygiene warnings:", file=sys.stderr)
        for f in warns[:200]:
            print(f"  - {f.where}: {f.msg}", file=sys.stderr)
        if len(warns) > 200:
            print(f"  ... ({len(warns) - 200} more)", file=sys.stderr)

    if errors or (warns and args.fail_on_warn):
        return 2

    print(f"OK: equation hygiene ({len(tex_files)} files checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
