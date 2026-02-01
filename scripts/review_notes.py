#!/usr/bin/env python3
"""
Scientific QA pass for the generated lecture notes.

This script converts a PDF into text, splits it into manageable chunks,
and sends each chunk to an OpenAI model that reviews the content for
scientific correctness, mathematical consistency, and clarity.  The
per-chunk findings are written to a Markdown report for further triage.

Example usage:
    python scripts/review_notes.py --pdf notes_output/ece657_notes.pdf
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, List, Optional, Sequence, Tuple

try:
    # Optional: provides better token accounting when available.
    import tiktoken  # type: ignore
except ImportError:  # pragma: no cover - optional dependency.
    tiktoken = None  # type: ignore

from openai import OpenAI  # type: ignore

try:  # pragma: no cover - optional dependency
    from dotenv import load_dotenv  # type: ignore
except ImportError:  # pragma: no cover
    load_dotenv = None  # type: ignore


DEFAULT_MODEL = "gpt-4.1-mini"
DEFAULT_CHUNK_TOKENS = 1500
SYSTEM_PROMPT = (
    "You are a senior scientific reviewer. Analyse the provided chunk of lecture "
    "notes for scientific or mathematical issues. Flag incorrect statements, "
    "logical gaps, missing definitions, ambiguous claims, inconsistent notation, "
    "or places where more justification is needed. Respond with clear bullet "
    "points. If nothing is wrong, say 'No issues spotted'."
)


@dataclass
class Chunk:
    index: int
    total: int
    start_char: int
    end_char: int
    text: str


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract raw text from a PDF using the pdftotext utility."""
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", "-nopgbrk", str(pdf_path), "-"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except FileNotFoundError as exc:  # pragma: no cover - environment dependent.
        raise RuntimeError(
            "pdftotext not found. Install poppler-utils (e.g. `brew install poppler` "
            "or `sudo apt-get install poppler-utils`)."
        ) from exc
    except subprocess.CalledProcessError as exc:  # pragma: no cover
        raise RuntimeError(f"pdftotext failed: {exc.stderr}") from exc
    return result.stdout


def get_encoder(model: str):
    """Return a token encoder if tiktoken is available; otherwise None."""
    if tiktoken is None:
        return None
    try:  # pragma: no cover - depends on local tiktoken version.
        return tiktoken.encoding_for_model(model)
    except KeyError:
        return tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str, encoder) -> int:
    if encoder is None:
        # Fallback: rough proxy assuming 4 characters per token.
        return max(1, len(text) // 4)
    return len(encoder.encode(text))


def chunk_text(
    text: str,
    max_tokens: int,
    encoder,
) -> Iterator[Chunk]:
    """Yield chunks of text that fit within the token budget."""
    start = 0
    paragraphs = text.split("\n\n")
    current: List[str] = []
    current_start = 0

    def flush(accum: List[str], start_idx: int, idx: int) -> Iterable[Chunk]:
        if not accum:
            return []
        chunk_text = "\n\n".join(accum).strip()
        if not chunk_text:
            return []
        yield (start_idx, start_idx + len(chunk_text), chunk_text)

    raw_chunks: List[Tuple[int, int, str]] = []
    for para in paragraphs:
        tentative = "\n\n".join(current + [para])
        if count_tokens(tentative, encoder) <= max_tokens:
            if not current:
                current_start = start
            current.append(para)
            start += len(para) + 2
            continue

        raw_chunks.extend(list(flush(current, current_start, start)))
        current = [para]
        current_start = start
        start += len(para) + 2

    raw_chunks.extend(list(flush(current, current_start, start)))

    total = len(raw_chunks)
    for idx, (chunk_start, chunk_end, chunk_text) in enumerate(raw_chunks, start=1):
        yield Chunk(idx, total, chunk_start, chunk_end, chunk_text)


def review_chunk(client: OpenAI, model: str, chunk: Chunk) -> str:
    """Send a chunk to the OpenAI model and return its critique."""
    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "system",
                "content": [{"type": "input_text", "text": SYSTEM_PROMPT}],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": f"Chunk {chunk.index}/{chunk.total}:\n{chunk.text}",
                    }
                ],
            },
        ],
        temperature=0.0,
    )
    return response.output_text.strip()


def write_report(report_path: Path, pdf_path: Path, reviews: Sequence[Tuple[Chunk, str]]) -> None:
    """Persist the per-chunk reviews as a Markdown report."""
    lines = [
        f"# Scientific QA Report",
        "",
        f"- Source PDF: `{pdf_path}`",
        f"- Total chunks: {len(reviews)}",
        "",
    ]
    for chunk, critique in reviews:
        lines.extend(
            [
                f"## Chunk {chunk.index}/{chunk.total}",
                f"- Character range: {chunk.start_char}–{chunk.end_char}",
                "",
                "```text",
                chunk.text.strip(),
                "```",
                "",
                "### Findings",
                critique or "No response returned.",
                "",
            ]
        )
    report_path.write_text("\n".join(lines))


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a scientific QA pass over the compiled lecture notes.")
    parser.add_argument(
        "--pdf",
        type=Path,
        default=Path("notes_output/ece657_notes.pdf"),
        help="Path to the PDF to review.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"OpenAI model to use (default: {DEFAULT_MODEL}).",
    )
    parser.add_argument(
        "--chunk-tokens",
        type=int,
        default=DEFAULT_CHUNK_TOKENS,
        help=f"Approximate token budget per chunk (default: {DEFAULT_CHUNK_TOKENS}).",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("notes_output/review/report.md"),
        help="Where to write the Markdown report.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Split the document and show chunk statistics without calling the API.",
    )
    parser.add_argument(
        "--limit-chunks",
        type=int,
        default=None,
        help="If provided, only review the first N chunks (useful for spot checks).",
    )
    parser.add_argument(
        "--start-chunk",
        type=int,
        default=1,
        help="Start reviewing from this 1-based chunk index (chunks below this index are skipped).",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    if not args.pdf.exists():
        print(f"[!] PDF not found: {args.pdf}", file=sys.stderr)
        return 1

    if load_dotenv:
        load_dotenv()

    text = extract_text_from_pdf(args.pdf)
    encoder = get_encoder(args.model)
    chunks = list(chunk_text(text, args.chunk_tokens, encoder))
    if not chunks:
        print("[!] No textual content extracted from PDF.", file=sys.stderr)
        return 1

    if args.dry_run:
        for chunk in chunks:
            print(
                f"Chunk {chunk.index}/{chunk.total}: "
                f"{len(chunk.text.split())} words, "
                f"{count_tokens(chunk.text, encoder)} tokens, "
                f"chars {chunk.start_char}-{chunk.end_char}"
            )
        return 0

    client = OpenAI()
    start_idx = max(1, args.start_chunk)
    if start_idx > 1:
        chunks = [chunk for chunk in chunks if chunk.index >= start_idx]
    if args.limit_chunks is not None:
        chunks = chunks[: args.limit_chunks]

    reviews: List[Tuple[Chunk, str]] = []
    for chunk in chunks:
        print(f"[+] Reviewing chunk {chunk.index}/{chunk.total}...")
        critique = review_chunk(client, args.model, chunk)
        reviews.append((chunk, critique))

    args.report.parent.mkdir(parents=True, exist_ok=True)
    write_report(args.report, args.pdf, reviews)
    print(f"[+] Review complete. Report written to {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
