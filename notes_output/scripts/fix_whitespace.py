#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fnmatch
import ast
from pathlib import Path

def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _parse_toml_list(value: str) -> list[str]:
    try:
        parsed = ast.literal_eval(value)
        if isinstance(parsed, list):
            return [str(x) for x in parsed]
    except Exception:
        pass
    return []


def _load_style(path: Path) -> dict:
    raw = _read_text(path)
    style: dict = {"lint": {"include_globs": [], "exclude_globs": []}}
    current_section: str | None = None

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

        if current_section == "lint" and key in ("include_globs", "exclude_globs"):
            style["lint"][key] = _parse_toml_list(value)

        i += 1

    if not style["lint"]["include_globs"]:
        style["lint"]["include_globs"] = ["*.tex", "*.md"]
    if not style["lint"]["exclude_globs"]:
        style["lint"]["exclude_globs"] = [
            "build/**",
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


def _normalize(text: str) -> str:
    out_lines: list[str] = []
    for line in text.splitlines():
        line = line.replace("\t", "    ").rstrip()
        out_lines.append(line)
    return "\n".join(out_lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Replace tabs and trim trailing whitespace (source hygiene).")
    parser.add_argument("--root", default=".", help="notes_output root directory")
    parser.add_argument("--style", default="editorial_style.toml", help="Style config (TOML)")
    parser.add_argument("--check", action="store_true", help="Do not write changes, just report.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    style = _load_style(root / args.style)
    lint = style.get("lint") if isinstance(style, dict) else {}
    include_globs = [str(x) for x in (lint.get("include_globs") or [])] if isinstance(lint, dict) else []
    exclude_globs = [str(x) for x in (lint.get("exclude_globs") or [])] if isinstance(lint, dict) else []

    changed: list[str] = []
    for path in _iter_files(root, include_globs, exclude_globs):
        before = _read_text(path)
        after = _normalize(before)
        if before == after:
            continue
        rel = path.relative_to(root).as_posix()
        changed.append(rel)
        if not args.check:
            path.write_text(after, encoding="utf-8")

    if changed:
        print(f"{'Would change' if args.check else 'Changed'} {len(changed)} file(s):")
        for rel in changed:
            print(f"- {rel}")
    else:
        print("No whitespace issues detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
