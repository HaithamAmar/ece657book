#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import fnmatch
import re
from pathlib import Path

def _read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None


def _parse_toml_list(value: str) -> list[str]:
    # `["a", "b"]` is also valid Python literal.
    try:
        parsed = ast.literal_eval(value)
        if isinstance(parsed, list):
            return [str(x) for x in parsed]
    except Exception:
        pass
    return []


def _load_style(path: Path) -> dict:
    raw = _read_text(path)
    if raw is None:
        return {}

    style: dict = {"spelling": [], "lint": {"include_globs": [], "exclude_globs": []}}
    current_section: str | None = None
    current_spelling: dict | None = None

    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        line = line.split("#", 1)[0].strip()
        if not line:
            i += 1
            continue
        if line == "[lint]":
            current_section = "lint"
            current_spelling = None
            i += 1
            continue
        if line == "[[spelling]]":
            current_section = "spelling"
            current_spelling = {}
            style["spelling"].append(current_spelling)
            i += 1
            continue

        if "=" not in line:
            i += 1
            continue
        key, value = [x.strip() for x in line.split("=", 1)]
        if value.startswith("[") and not value.rstrip().endswith("]"):
            buf = [value]
            j = i + 1
            while j < len(lines):
                nxt = lines[j].split("#", 1)[0].strip()
                buf.append(nxt)
                if nxt.endswith("]"):
                    break
                j += 1
            value = " ".join(buf)
            i = j

        if current_section == "lint":
            if key in ("include_globs", "exclude_globs"):
                style["lint"][key] = _parse_toml_list(value)
            i += 1
            continue

        if current_section == "spelling" and current_spelling is not None:
            if key in ("name",):
                if value.startswith('"') and value.endswith('"'):
                    current_spelling[key] = value[1:-1]
            if key in ("variants", "preferred"):
                current_spelling[key] = _parse_toml_list(value)

        i += 1
    return style


def _iter_files(root: Path, include_globs: list[str], exclude_globs: list[str]) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if any(fnmatch.fnmatch(rel, g) for g in exclude_globs):
            continue
        if include_globs and not any(fnmatch.fnmatch(rel, g) for g in include_globs):
            continue
        files.append(path)
    return files


def _case_like(src: str, replacement: str) -> str:
    if src.isupper():
        return replacement.upper()
    if src[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def _levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        cur = [i]
        for j, cb in enumerate(b, start=1):
            ins = cur[j - 1] + 1
            delete = prev[j] + 1
            sub = prev[j - 1] + (0 if ca == cb else 1)
            cur.append(min(ins, delete, sub))
        prev = cur
    return prev[-1]


def _build_replacements(style: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    spelling = style.get("spelling") if isinstance(style, dict) else None
    if not isinstance(spelling, list):
        return out

    for group in spelling:
        if not isinstance(group, dict):
            continue
        variants = [str(x) for x in (group.get("variants") or [])]
        preferred = [str(x) for x in (group.get("preferred") or [])]
        if not variants or not preferred:
            continue

        pref_lower = [p.lower() for p in preferred]
        for v in variants:
            v_lower = v.lower()
            if v_lower in pref_lower:
                continue
            best = min(preferred, key=lambda p: _levenshtein(v_lower, p.lower()))
            out[v_lower] = best
    return out


def _apply_to_text(text: str, replacements: dict[str, str]) -> tuple[str, int]:
    count = 0
    out_lines: list[str] = []
    in_verbatim = False

    # Precompile regexes once.
    patterns: list[tuple[re.Pattern[str], str]] = []
    for src, dst in replacements.items():
        patterns.append((re.compile(rf"(?<!\\)\b{re.escape(src)}\b", flags=re.IGNORECASE), dst))

    for line in text.splitlines(keepends=False):
        if r"\begin{verbatim}" in line:
            in_verbatim = True
        if r"\end{verbatim}" in line:
            in_verbatim = False

        if in_verbatim:
            out_lines.append(line)
            continue

        def repl_factory(dst: str):
            def _repl(m: re.Match[str]) -> str:
                nonlocal count
                count += 1
                return _case_like(m.group(0), dst)

            return _repl

        new_line = line
        for pat, dst in patterns:
            new_line = pat.sub(repl_factory(dst), new_line)
        out_lines.append(new_line)

    return "\n".join(out_lines) + ("\n" if text.endswith("\n") else ""), count


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply house-style spelling normalization.")
    parser.add_argument("--root", default="notes_output", help="notes_output root directory")
    parser.add_argument("--style", default="editorial_style.toml", help="Style config (TOML)")
    parser.add_argument("--check", action="store_true", help="Do not write changes, just report.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    style = _load_style(root / args.style)
    lint = style.get("lint") if isinstance(style, dict) else {}
    include_globs = [str(x) for x in (lint.get("include_globs") or [])] if isinstance(lint, dict) else []
    exclude_globs = [str(x) for x in (lint.get("exclude_globs") or [])] if isinstance(lint, dict) else []

    replacements = _build_replacements(style)

    changed: list[str] = []
    total = 0
    for path in _iter_files(root, include_globs, exclude_globs):
        before = _read_text(path)
        if before is None:
            continue
        after, n = _apply_to_text(before, replacements)
        if before == after:
            continue
        rel = path.relative_to(root).as_posix()
        changed.append(f"{rel} ({n})")
        total += n
        if not args.check:
            path.write_text(after, encoding="utf-8")

    if changed:
        verb = "Would change" if args.check else "Changed"
        print(f"{verb} {len(changed)} file(s), {total} replacement(s):")
        for rel in changed:
            print(f"- {rel}")
    else:
        print("No house-style spelling changes needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
