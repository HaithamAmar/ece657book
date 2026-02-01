#!/usr/bin/env python3
"""
Drive OpenAI-assisted polishing of ECE657 lecture transcripts into structured notes.

The workflow is:
1. Split the merged lecture transcript into one text blob per lecture.
2. OCR the matching handwritten board notes (PDF) for additional equation context.
3. Feed both pieces into OpenAI to generate polished notes, saved as Markdown.

Usage:
    python scripts/compile_notes.py \
        --transcript merged_lectures.docx \
        --board-notes-dir "NOTES ON BOARD ECE657" \
        --out-dir notes_output

Environment:
    Ensure .env contains OPENAI_API_KEY and optional OPENAI_MODEL (default gpt-4.1).

Dependencies:
    pip install python-docx python-dotenv openai pdfplumber pdf2image pytesseract pillow rich

Notes on OCR:
    - For handwritten PDFs, install Tesseract on macOS via `brew install tesseract`.
    - If OCR fails, the script still runs but will flag missing board context.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent
from typing import Dict, List, Optional, Sequence, Tuple

from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

console = Console()

try:
    from docx import Document
except ImportError as exc:  # pragma: no cover - dependency guard
    console.print(
        "[bold red]python-docx is required. Install with `pip install python-docx`.[/bold red]"
    )
    raise SystemExit(1) from exc


def try_import(name: str):
    try:
        return __import__(name)
    except ImportError:
        return None


pdfplumber = try_import("pdfplumber")
pdf2image = try_import("pdf2image")
pytesseract = try_import("pytesseract")
Image = None
if pdf2image:
    try:
        from PIL import Image  # type: ignore
    except Exception:  # pragma: no cover - optional dependency
        Image = None

try:
    from openai import OpenAI
except ImportError as exc:  # pragma: no cover - dependency guard
    console.print(
        "[bold red]openai>=1.0 is required. Install with `pip install openai`.[/bold red]"
    )
    raise SystemExit(1) from exc


DEFAULT_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4.1")
OUTPUT_MARKDOWN = "markdown"
OUTPUT_LATEX = "latex"


@dataclass
class LectureMaterial:
    title: str
    transcript: str
    board_text: Optional[str]
    board_path: Optional[Path]


PART_ROMAN = {
    "I": "Part I",
    "II": "Part II",
    "III": "Part III",
    "IV": "Part IV",
    "V": "Part V",
}


def normalize_title(lecture_no: int, part: Optional[str]) -> str:
    title = f"Lecture {lecture_no}"
    if part:
        upper = part.upper()
        title += f" {PART_ROMAN.get(upper, f'Part {upper}')}"
    return title


def match_heading(text: str) -> Optional[str]:
    pattern = re.compile(
        r"(?:ece\s*\d+\s*)?lecture\s*(\d+)(?:\s*(?:part|section)\s*([A-Za-z0-9]+))?",
        re.IGNORECASE,
    )
    m = pattern.search(text)
    if not m:
        return None
    lecture_no = int(m.group(1))
    part = m.group(2)
    return normalize_title(lecture_no, part)


def extract_lectures(transcript_path: Path) -> Dict[str, str]:
    doc = Document(transcript_path)
    lectures: Dict[str, List[str]] = defaultdict(list)
    current_title = None
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if not text:
            continue
        heading = match_heading(text)
        if heading:
            current_title = heading
            continue
        if current_title is None:
            current_title = "Lecture 0"
        lectures[current_title].append(text)

    combined = {
        title: "\n".join(blocks).strip()
        for title, blocks in lectures.items()
        if blocks
    }
    return combined


def extract_text_from_pdf(pdf_path: Path) -> str:
    if pdfplumber:
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = "\n".join(
                    page.extract_text() or "" for page in pdf.pages
                ).strip()
                if text:
                    return text
        except Exception as exc:  # pragma: no cover - best effort logging
            console.print(
                f"[yellow]pdfplumber failed on {pdf_path.name}: {exc}. Falling back to OCR.[/yellow]"
            )

    if pytesseract and pdf2image:
        try:
            images = pdf2image.convert_from_path(str(pdf_path))
            text_chunks = []
            for idx, img in enumerate(images):
                try:
                    chunk = pytesseract.image_to_string(img)
                except Exception as exc:
                    console.print(
                        f"[yellow]OCR failed on page {idx + 1} of {pdf_path.name}: {exc}[/yellow]"
                    )
                    continue
                if chunk.strip():
                    text_chunks.append(chunk)
            if text_chunks:
                return "\n".join(text_chunks).strip()
        except Exception as exc:  # pragma: no cover - best effort logging
            console.print(
                f"[yellow]OCR conversion failed for {pdf_path.name}: {exc}[/yellow]"
            )

    return ""


def match_board_note(lecture_title: str, board_dir: Path) -> Optional[Path]:
    lecture_number = None
    match = re.search(r"lecture\s*(\d+)", lecture_title, re.IGNORECASE)
    if match:
        lecture_number = int(match.group(1))
    if lecture_number is None:
        return None

    candidates = sorted(board_dir.glob("*.pdf"))
    for candidate in candidates:
        if re.search(fr"{lecture_number}\b", candidate.stem, re.IGNORECASE):
            return candidate
    return None


def word_chunks(text: str, max_words: int = 1200) -> List[str]:
    words = text.split()
    chunks = []
    for idx in range(0, len(words), max_words):
        chunk = " ".join(words[idx : idx + max_words]).strip()
        if chunk:
            chunks.append(chunk)
    return chunks


def strip_code_fence(text: str) -> str:
    fence = re.compile(r"^```(?:\w+)?\s*([\s\S]*?)\s*```$", re.DOTALL)
    match = fence.match(text.strip())
    return match.group(1).strip() if match else text.strip()


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return slug or "lecture"


def build_prompt(
    material: LectureMaterial,
    chunk: str,
    output_format: str,
    chunk_index: int,
    total_chunks: int,
) -> str:
    board_hint = (
        material.board_text[:4000] if material.board_text else "Board notes unavailable."
    )
    chunk_position = (
        "first"
        if chunk_index == 1
        else "last"
        if chunk_index == total_chunks
        else "middle"
    )

    if output_format == OUTPUT_LATEX:
        formatting_instructions = dedent(
            """
            Produce LaTeX that can be included inside a larger document.
            - Do NOT add \\documentclass or \\begin{document}.
            - Use \\section, \\subsection, \\paragraph etc. appropriately; only start a new \\section in the first chunk.
            - Express equations using LaTeX math mode with alignment (\\begin{align}) when helpful and label key equations (\\label{eq:...}).
            - Preserve symbols from the course; introduce definitions before use.
            - Escape special characters (% $ _ & #) when they are plain text.
            - Insert \\TODO{...} commands for uncertainties or missing details.
            """
        ).strip()
        summary_instruction = (
            "Conclude with a concise \\subsection*{Summary} and optionally \\subsection*{References} in the final chunk."
            if chunk_position == "last"
            else "Do not include a concluding summary in this chunk."
        )
    else:
        formatting_instructions = dedent(
            """
            Produce polished Markdown lecture notes with headings, lists, and GitHub-flavored math fences ($$ ... $$).
            - Maintain rigorous terminology and complete derivations.
            - Convert equations into LaTeX math within Markdown.
            - Insert [TODO: ...] for uncertainties or missing details.
            """
        ).strip()
        summary_instruction = (
            "Close with a concise summary and list of key references if any, because this is the final chunk."
            if chunk_position == "last"
            else "Do not write a summary in this chunk."
        )

    chunk_instruction = (
        "This is the first chunk—establish context clearly."
        if chunk_position == "first"
        else "This is the final chunk—wrap up open derivations and provide closure."
        if chunk_position == "last"
        else "This is a middle chunk—continue seamlessly from previous content."
    )

    intro = dedent(
        f"""
        Write polished graduate-level lecture notes for {material.title}. {chunk_instruction}

        Output format: {output_format}.
        {formatting_instructions}
        {summary_instruction}
        """
    ).strip()

    prompt = dedent(
        f"""
        Instructions:
        {intro}

        Handwritten board notes (OCR approximation):
        {board_hint}

        Transcript excerpt:
        {chunk}
        """
    ).strip()
    return prompt


def call_openai(prompt: str, model: str) -> str:
    client = OpenAI()
    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "system",
                "content": [{"type": "input_text", "text": "You are an expert TA creating ECE657 lecture notes."}],
            },
            {
                "role": "user",
                "content": [{"type": "input_text", "text": prompt}],
            },
        ],
        temperature=0.2,
        max_output_tokens=1200,
    )
    return response.output_text.strip()


def ensure_output_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_main_tex(out_dir: Path, lecture_files: Sequence[Path]) -> Path:
    main_path = out_dir / "ece657_notes.tex"
    inputs = "\n".join(f"\\input{{{file.name}}}" for file in lecture_files)
    main_content = dedent(
        rf"""
        \documentclass[11pt]{{article}}
        \usepackage[margin=1in]{{geometry}}
        \usepackage{{amsmath, amssymb, amsthm}}
        \usepackage{{physics}}
        \usepackage{{siunitx}}
        \usepackage{{hyperref}}
        \usepackage{{cleveref}}
        \usepackage{{enumitem}}
        \usepackage{{graphicx}}
        \usepackage{{xcolor}}
        \usepackage{{bookmark}}

        \newcommand{{\TODO}}[1]{{\textcolor{{red}}{{[TODO: #1]}}}}

        \setcounter{{secnumdepth}}{3}
        \setcounter{{tocdepth}}{2}

        \title{{ECE657 Lecture Notes}}
        \author{{Automated Draft via Transcripts + Board Notes}}
        \date{{\today}}

        \begin{{document}}
        \maketitle
        \tableofcontents
        \newpage

        {inputs}

        \end{{document}}
        """
    ).strip()
    main_path.write_text(main_content)
    return main_path


def compile_latex_pdf(out_dir: Path, main_tex: Path) -> None:
    console.print(f"[blue]Compiling PDF for {main_tex.name}...[/blue]")
    latexmk = shutil.which("latexmk")
    if latexmk:
        command = [latexmk, "-pdf", "-quiet", main_tex.name]
        result = subprocess.run(command, cwd=out_dir)
        if result.returncode == 0:
            console.print("[green]PDF generated with latexmk.[/green]")
            return
        console.print("[yellow]latexmk failed, falling back to tectonic/pdflatex.[/yellow]")

    tectonic = shutil.which("tectonic")
    if tectonic:
        result = subprocess.run(
            [tectonic, "--keep-logs", "--keep-intermediates", main_tex.name],
            cwd=out_dir,
        )
        if result.returncode == 0:
            console.print("[green]PDF generated with tectonic.[/green]")
            return
        log_path = main_tex.with_suffix(".log")
        console.print(
            f"[bold red]tectonic failed (see {log_path}). Fix the LaTeX issues and rerun.[/bold red]"
        )
        raise SystemExit(result.returncode)

    pdflatex = shutil.which("pdflatex")
    if not pdflatex:
        console.print(
            "[bold red]pdflatex/tectonic not found. Install TeX Live, MiKTeX, or tectonic to compile PDFs.[/bold red]"
        )
        raise SystemExit(1)

    for pass_no in range(2):
        result = subprocess.run([pdflatex, "-interaction=nonstopmode", main_tex.name], cwd=out_dir)
        if result.returncode != 0:
            console.print(
                f"[bold red]pdflatex failed on pass {pass_no + 1}. Check the .log file for details.[/bold red]"
            )
            raise SystemExit(result.returncode)
    console.print("[green]PDF generated with pdflatex.[/green]")


def summarise_plan(materials: Sequence[LectureMaterial], model: str) -> None:
    table = Table(title="Lecture Extraction Plan")
    table.add_column("Lecture")
    table.add_column("Transcript Words", justify="right")
    table.add_column("Board Notes", justify="center")
    table.add_column("Model")
    for material in materials:
        word_count = len(material.transcript.split())
        table.add_row(
            material.title,
            f"{word_count:,}",
            "✅" if material.board_text else "⚠️",
            model,
        )
    console.print(table)


def run_pipeline(
    transcript_path: Path,
    board_dir: Path,
    out_dir: Path,
    model: str,
    dry_run: bool,
    output_format: str,
    compile_pdf: bool,
    overwrite: bool,
) -> None:
    load_dotenv()
    if "OPENAI_API_KEY" not in os.environ:
        console.print("[bold red]OPENAI_API_KEY not found in environment.[/bold red]")
        raise SystemExit(1)

    lectures = extract_lectures(transcript_path)
    materials: List[LectureMaterial] = []

    for title, text in lectures.items():
        board_path = match_board_note(title, board_dir)
        board_text = None
        if board_path:
            board_text = extract_text_from_pdf(board_path)
            if not board_text:
                console.print(
                    f"[yellow]No board text extracted for {title}. Check {board_path.name} manually.[/yellow]"
                )
        else:
            console.print(
                f"[yellow]No board PDF matched for {title}. Add a file named with the lecture number.[/yellow]"
            )
        materials.append(
            LectureMaterial(
                title=title,
                transcript=text,
                board_text=board_text,
                board_path=board_path,
            )
        )

    summarise_plan(materials, model)
    ensure_output_dir(out_dir)

    latex_files: List[Path] = []

    for material in materials:
        console.print(f"[cyan]Processing {material.title}...[/cyan]")
        chunks = word_chunks(material.transcript)
        lecture_sections: List[str] = []
        total_chunks = len(chunks)
        extension = ".md" if output_format == OUTPUT_MARKDOWN else ".tex"
        filename = f"{slugify(material.title)}{extension}"
        output_path = out_dir / filename

        if not dry_run and output_path.exists() and not overwrite:
            console.print(
                f"[yellow]Skipping {material.title} because {output_path.name} already exists (use --overwrite to regenerate).[/yellow]"
            )
            if output_format == OUTPUT_LATEX:
                latex_files.append(output_path)
            continue

        for idx, chunk in enumerate(chunks, start=1):
            prompt = build_prompt(material, chunk, output_format, idx, total_chunks)
            if dry_run:
                console.print(
                    f"[green]Dry run chunk {idx} for {material.title}. No API call made.[/green]"
                )
                continue
            console.print(
                f"[magenta]Calling OpenAI for {material.title}, chunk {idx}/{len(chunks)}[/magenta]"
            )
            try:
                section = call_openai(prompt, model)
            except Exception as exc:
                console.print(
                    f"[bold red]OpenAI request failed for {material.title} chunk {idx}: {exc}[/bold red]"
                )
                raise
            lecture_sections.append(strip_code_fence(section))

        if dry_run:
            continue

        output_path.write_text("\n\n".join(lecture_sections))
        console.print(f"[green]Saved {output_path}[/green]")
        if output_format == OUTPUT_LATEX:
            latex_files.append(output_path)

    if dry_run or output_format != OUTPUT_LATEX:
        return

    main_tex = write_main_tex(out_dir, latex_files)
    console.print(f"[green]Main LaTeX file written to {main_tex}[/green]")

    if compile_pdf:
        compile_latex_pdf(out_dir, main_tex)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate polished ECE657 lecture notes with OpenAI.")
    parser.add_argument(
        "--transcript",
        type=Path,
        default=Path("merged_lectures.docx"),
        help="Path to merged transcript DOCX.",
    )
    parser.add_argument(
        "--board-notes-dir",
        type=Path,
        default=Path("NOTES ON BOARD ECE657"),
        help="Directory containing handwritten board note PDFs.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("notes_output"),
        help="Directory to store generated Markdown notes.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help=f"OpenAI model to use (default: {DEFAULT_MODEL}).",
    )
    parser.add_argument(
        "--format",
        choices=[OUTPUT_MARKDOWN, OUTPUT_LATEX],
        default=OUTPUT_LATEX,
        help="Output format for generated notes.",
    )
    parser.add_argument(
        "--compile-pdf",
        action="store_true",
        help="Compile the LaTeX output into a PDF (requires TeX installed).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Regenerate outputs even if files already exist.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run extraction and OCR steps without calling OpenAI.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> None:
    args = parse_args(argv)
    if not args.transcript.exists():
        console.print(f"[bold red]Transcript file {args.transcript} not found.[/bold red]")
        raise SystemExit(1)

    if not args.board_notes_dir.exists():
        console.print(
            f"[bold red]Board notes directory {args.board_notes_dir} not found.[/bold red]"
        )
        raise SystemExit(1)

    run_pipeline(
        transcript_path=args.transcript,
        board_dir=args.board_notes_dir,
        out_dir=args.out_dir,
        model=args.model,
        dry_run=args.dry_run,
        output_format=args.format,
        compile_pdf=args.compile_pdf,
        overwrite=args.overwrite,
    )


if __name__ == "__main__":
    main()
