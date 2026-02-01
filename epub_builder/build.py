#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
import zipfile

from lib.latex import (
    flatten_latex_inputs,
    select_ifdefined_hcode_branch,
    strip_document_environment,
    load_aux_label_numbers,
    inject_equation_targets,
    rewrite_crossrefs,
    prefix_chapter_sections,
    prefix_numbered_headings,
    prefix_caption_numbers,
    add_visible_equation_numbers,
    transform_tcolorbox_to_quote,
    extract_tikz_blocks,
    replace_tikz_blocks_with_images,
    resolve_bare_includegraphics,
    strip_captionsetup_commands,
    unwrap_graphics_wrappers,
    verify_includegraphics_targets,
)
from lib.tikz import compile_tikz_block_to_png
from lib.epub import postprocess_epub_minimal, run_epubcheck


@dataclass(frozen=True)
class Paths:
    repo_root: Path
    notes_output: Path
    entry_tex: Path
    artifacts: Path
    dist: Path
    work: Path
    media: Path
    tikz_logs: Path


def _run(cmd: list[str], *, cwd: Path | None = None) -> None:
    proc = subprocess.run(cmd, cwd=cwd, check=False, text=True)
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)


def _ensure_tools() -> None:
    required = ["pandoc", "pdflatex", "pdftoppm"]
    missing = [t for t in required if shutil.which(t) is None]
    if missing:
        raise SystemExit(f"Missing required tools on PATH: {', '.join(missing)}")


def _paths() -> Paths:
    repo_root = Path(__file__).resolve().parents[1]
    notes_output = repo_root / "notes_output"
    entry_tex = notes_output / "ece657_ebook.tex"
    if not entry_tex.exists():
        raise SystemExit(f"Missing entry file: {entry_tex}")
    artifacts = repo_root / "epub_builder" / "artifacts"
    dist = repo_root / "epub_builder" / "dist"
    work = artifacts / "work"
    media = artifacts / "media"
    tikz_logs = artifacts / "tikz_logs"
    return Paths(
        repo_root=repo_root,
        notes_output=notes_output,
        entry_tex=entry_tex,
        artifacts=artifacts,
        dist=dist,
        work=work,
        media=media,
        tikz_logs=tikz_logs,
    )


def _verify_epub_figures(epub_path: Path) -> None:
    """
    Best-effort sanity check that EPUB figure blocks actually contain renderable
    content (typically <img>). This guards against the "caption shows but image
    missing" failure mode.
    """
    with zipfile.ZipFile(epub_path, "r") as z:
        names = set(z.namelist())
        xhtmls = [n for n in names if n.startswith("EPUB/text/") and n.endswith(".xhtml")]
        bad: list[str] = []

        def _zip_media_path(src: str) -> str | None:
            s = src.strip()
            if not s or "://" in s or s.startswith("data:"):
                return None
            s = s.split("#", 1)[0].split("?", 1)[0]
            if s.startswith("../media/"):
                return "EPUB/media/" + s[len("../media/") :]
            if s.startswith("media/"):
                return "EPUB/media/" + s[len("media/") :]
            if s.startswith("../"):
                # Most EPUB text files live under EPUB/text/.
                return "EPUB/" + s[len("../") :]
            return None

        for name in sorted(xhtmls):
            s = z.read(name).decode("utf-8", errors="ignore")
            # Any leftover TikZ means a missed replacement and almost certainly a missing figure.
            if "\\begin{tikzpicture}" in s:
                bad.append(f"{name}: contains raw tikzpicture")
                continue

            # Check each <figure>...</figure> has an <img> or <svg> or <math> (rare).
            for m in re.finditer(r"<figure\b.*?</figure>", s, flags=re.DOTALL):
                block = m.group(0)
                if "<img" in block or "<svg" in block or "<math" in block:
                    continue
                bad.append(f"{name}: figure missing renderable content")
                break

            # Ensure referenced <img src="..."> resources exist in the EPUB zip.
            for m in re.finditer(r"<img\b[^>]*\bsrc=\"([^\"]+)\"", s):
                src = m.group(1)
                zp = _zip_media_path(src)
                if not zp:
                    continue
                if zp not in names:
                    bad.append(f"{name}: missing image file in EPUB zip: {zp}")
                    continue
                try:
                    if z.getinfo(zp).file_size <= 0:
                        bad.append(f"{name}: empty image file in EPUB zip: {zp}")
                except KeyError:
                    bad.append(f"{name}: missing image file in EPUB zip: {zp}")

        if bad:
            raise SystemExit("EPUB figure verification failed:\n- " + "\n- ".join(bad[:60]))


def build(*, variant: str, clean: bool, skip_validate: bool) -> Path:
    _ensure_tools()
    p = _paths()

    css_path = p.repo_root / "epub_builder" / "epub.css"
    if not css_path.exists():
        raise SystemExit(f"Missing CSS file: {css_path}")

    metadata_path = p.notes_output / "book_metadata.json"
    metadata: dict[str, str] = {}
    if metadata_path.exists():
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            metadata = {}

    # Always rebuild the EPUB outputs. "clean" removes only transient build
    # outputs (work/dist/epubcheck), while preserving the TikZ/media cache.
    if clean:
        for d in (p.work, p.dist, p.artifacts / "epubcheck", p.artifacts / "tmp"):
            if d.exists():
                shutil.rmtree(d)
    p.work.mkdir(parents=True, exist_ok=True)
    p.media.mkdir(parents=True, exist_ok=True)
    p.tikz_logs.mkdir(parents=True, exist_ok=True)
    p.dist.mkdir(parents=True, exist_ok=True)

    raw_flat = flatten_latex_inputs(p.entry_tex, root_dir=p.notes_output)
    raw_flat = select_ifdefined_hcode_branch(raw_flat)
    doc_body = strip_document_environment(raw_flat)

    aux_numbers = load_aux_label_numbers(aux_path=p.notes_output / "ece657_notes.aux")
    doc_body = inject_equation_targets(doc_body)
    doc_body = rewrite_crossrefs(doc_body, aux_numbers=aux_numbers)
    doc_body = prefix_chapter_sections(doc_body, aux_numbers=aux_numbers)
    doc_body = prefix_numbered_headings(doc_body, aux_numbers=aux_numbers)

    tikz_blocks = extract_tikz_blocks(doc_body)
    rendered: dict = {}
    tikz_dpi = int(getattr(build, "_tikz_dpi", 300))  # set by main()
    strict_figures = bool(getattr(build, "_strict_figures", True))  # set by main()
    failed: list[str] = []
    for idx, block in enumerate(tikz_blocks, start=1):
        name = f"tikz_{idx:04d}"
        png_name = f"{name}.png"
        out_png = p.media / png_name
        ok = compile_tikz_block_to_png(
            tikz_code=block.content,
            out_png=out_png,
            notes_output_dir=p.notes_output,
            log_dir=p.tikz_logs,
            stem=name,
            dpi=tikz_dpi,
        )
        if not ok:
            failed.append(name)
        rendered[block] = png_name if ok else None

    if strict_figures and failed:
        msg = ["TikZ figure compilation failed; refusing to produce an EPUB in strict mode."]
        msg.append(f"Failed blocks: {', '.join(failed)}")
        msg.append("See logs under: epub_builder/artifacts/tikz_logs/")
        raise SystemExit("\n".join(msg))

    doc_body = replace_tikz_blocks_with_images(doc_body, rendered)
    doc_body = transform_tcolorbox_to_quote(doc_body)
    doc_body = resolve_bare_includegraphics(doc_body, repo_root=p.repo_root)
    doc_body = strip_captionsetup_commands(doc_body)
    doc_body = unwrap_graphics_wrappers(doc_body)
    doc_body = prefix_caption_numbers(doc_body, aux_numbers=aux_numbers)
    doc_body = add_visible_equation_numbers(doc_body, aux_numbers=aux_numbers)
    if strict_figures:
        verify_includegraphics_targets(
            doc_body, repo_root=p.repo_root, notes_output_dir=p.notes_output, media_dir=p.media
        )

    preprocessed_tex = p.work / "book_preprocessed.tex"
    preprocessed_tex.write_text(doc_body, encoding="utf-8")

    out_epub = p.dist / f"ece657_ebook_{variant}.epub"
    pandoc_metadata_args: list[str] = []
    title = metadata.get("title")
    creator = metadata.get("creator") or metadata.get("author")
    lang = metadata.get("language")
    if title:
        pandoc_metadata_args += ["-M", f"title={title}"]
    if creator:
        pandoc_metadata_args += ["-M", f"author={creator}"]
    if lang:
        pandoc_metadata_args += ["-M", f"lang={lang}"]

    pandoc_cmd = [
        "pandoc",
        "--from=latex",
        "--to=epub3",
        "--standalone",
        "--mathml",
        "--css",
        str(css_path),
        "--resource-path",
        str(p.media) + ":" + str(p.repo_root) + ":" + str(p.notes_output),
        "--output",
        str(out_epub),
        *pandoc_metadata_args,
        str(preprocessed_tex),
    ]
    _run(pandoc_cmd, cwd=p.repo_root)

    postprocess_epub_minimal(out_epub)
    if strict_figures:
        _verify_epub_figures(out_epub)
    if not skip_validate:
        run_epubcheck(out_epub, out_dir=p.artifacts / "epubcheck")
    return out_epub


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--variant", choices=["apple", "kindle", "both"], default="apple")
    parser.add_argument("--clean", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--skip-validate", action="store_true")
    parser.add_argument("--tikz-dpi", type=int, default=300)
    parser.add_argument("--strict-figures", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)

    setattr(build, "_tikz_dpi", args.tikz_dpi)
    setattr(build, "_strict_figures", args.strict_figures)

    if args.variant == "both":
        build(variant="apple", clean=args.clean, skip_validate=args.skip_validate)
        build(variant="kindle", clean=False, skip_validate=args.skip_validate)
        return 0

    build(variant=args.variant, clean=args.clean, skip_validate=args.skip_validate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
