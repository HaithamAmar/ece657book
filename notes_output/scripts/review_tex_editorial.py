#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from openai import OpenAI  # type: ignore

try:
    from dotenv import load_dotenv  # type: ignore
except Exception:  # pragma: no cover
    load_dotenv = None  # type: ignore


SYSTEM_PROMPT = (
    "You are an editorial reviewer for a graduate-level technical book written in LaTeX. "
    "Review the provided LaTeX source snippet and report concrete editorial issues only. "
    "Focus on narrative flow, transition quality, repetitive templating, punctuation/spacing, "
    "and clarity of prose. Ignore pure mathematical correctness unless it causes prose ambiguity. "
    "Do not invent issues. Return concise bullet points with line numbers when possible. "
    "If no issues are found, respond exactly: No issues spotted."
)


@dataclass
class Chunk:
    file: Path
    start_line: int
    end_line: int
    text: str


def iter_tex_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.glob("*.tex")):
        if path.name.startswith("_"):
            continue
        yield path


def chunk_lines(path: Path, max_lines: int) -> list[Chunk]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    chunks: list[Chunk] = []
    for i in range(0, len(lines), max_lines):
        start = i + 1
        end = min(i + max_lines, len(lines))
        block = "\n".join(lines[i:end])
        numbered = "\n".join(f"{start + j}: {line}" for j, line in enumerate(block.splitlines()))
        chunks.append(Chunk(file=path, start_line=start, end_line=end, text=numbered))
    return chunks


def review_chunk(client: OpenAI, model: str, chunk: Chunk) -> str:
    user_text = (
        f"File: {chunk.file}\n"
        f"Line range: {chunk.start_line}-{chunk.end_line}\n\n"
        "LaTeX source:\n"
        f"{chunk.text}"
    )
    resp = client.responses.create(
        model=model,
        input=[
            {"role": "system", "content": [{"type": "input_text", "text": SYSTEM_PROMPT}]},
            {"role": "user", "content": [{"type": "input_text", "text": user_text}]},
        ],
    )
    return (resp.output_text or "").strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Run editorial LLM review directly on .tex sources.")
    parser.add_argument("--root", default="notes_output", help="Root containing chapter .tex files")
    parser.add_argument("--report", default="notes_output/review/report_llm_editorial_tex_20260216.md")
    parser.add_argument("--model", default="gpt-5-mini")
    parser.add_argument("--max-lines", type=int, default=320)
    parser.add_argument("--limit-files", type=int, default=None)
    parser.add_argument(
        "--include-regex",
        default=".*",
        help="Only review files whose basename matches this regex.",
    )
    args = parser.parse_args()

    if load_dotenv:
        load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is missing")

    root = Path(args.root).resolve()
    include_re = re.compile(args.include_regex)
    files = [p for p in iter_tex_files(root) if include_re.search(p.name)]
    if args.limit_files is not None:
        files = files[: args.limit_files]
    client = OpenAI()

    report_path = Path(args.report).resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        "# LLM Editorial Review (Direct TeX Pass)",
        "",
        f"- Root: `{root}`",
        f"- Model: `{args.model}`",
        f"- Files reviewed: `{len(files)}`",
        "",
    ]

    total_issue_files = 0
    for idx, path in enumerate(files, start=1):
        print(f"[+] Reviewing file {idx}/{len(files)}: {path.name}")
        chunks = chunk_lines(path, args.max_lines)
        findings: list[str] = []
        for cidx, chunk in enumerate(chunks, start=1):
            print(f"    - chunk {cidx}/{len(chunks)}")
            out = review_chunk(client, args.model, chunk)
            norm = " ".join(out.lower().split())
            if not norm.startswith("no issues spotted"):
                findings.append(out)

        if not findings:
            status = "No issues spotted."
        else:
            status = "\n\n".join(findings)
            total_issue_files += 1

        lines.extend(
            [
                f"## {path.name}",
                "",
                status,
                "",
            ]
        )

        # Mark non-TikZ figures for manual visual confirmation.
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "\\includegraphics" in text:
            lines.extend(
                [
                    f"- Visual check note: `{path.name}` contains `\\includegraphics`; verify caption/prose alignment against rendered figure crops.",
                    "",
                ]
            )

        # Persist progress after each file in case the run is interrupted.
        report_path.write_text("\n".join(lines), encoding="utf-8")

    lines.extend(
        [
            "## Summary",
            "",
            f"- Files with actionable editorial issues: `{total_issue_files}`",
            f"- Files with no issues spotted: `{len(files) - total_issue_files}`",
            "",
        ]
    )

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] Wrote report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
