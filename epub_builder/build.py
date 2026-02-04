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
    promote_displaystyle_math,
    promote_long_inline_math,
    transform_tcolorbox_to_quote,
    extract_tikz_blocks,
    replace_tikz_blocks_with_images,
    resolve_bare_includegraphics,
    strip_captionsetup_commands,
    unwrap_graphics_wrappers,
    rasterize_pdf_includegraphics,
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


@dataclass(frozen=True)
class AuxInfo:
    numbers: dict[str, str]
    aux_path: Path


def _run(cmd: list[str], *, cwd: Path | None = None, env: dict[str, str] | None = None) -> None:
    proc = subprocess.run(cmd, cwd=cwd, env=env, check=False, text=True)
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)

def _png_dimensions(path: Path) -> tuple[int, int] | None:
    """
    Read PNG width/height without external deps (IHDR chunk).
    """
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    try:
        width = int.from_bytes(data[16:20], "big")
        height = int.from_bytes(data[20:24], "big")
    except Exception:
        return None
    if width <= 0 or height <= 0:
        return None
    return width, height


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

def _build_aux_info(*, p: Paths) -> AuxInfo:
    """
    Best-effort: compile `notes_output/ece657_notes.tex` into a temp output dir
    so `.aux` reflects the current sources (including newly added labels). If
    compilation fails, fall back to `notes_output/ece657_notes.aux`.
    """
    aux_fallback = p.notes_output / "ece657_notes.aux"
    tex = p.notes_output / "ece657_notes.tex"
    if not tex.exists():
        return AuxInfo(numbers=load_aux_label_numbers(aux_path=aux_fallback), aux_path=aux_fallback)

    aux_out_dir = p.artifacts / "tmp" / "aux"
    aux_out_dir.mkdir(parents=True, exist_ok=True)
    jobname = "ece657_notes_epub_aux"
    aux_out = aux_out_dir / f"{jobname}.aux"
    # Citations are not required for `.aux` numbering, but unresolved citations
    # can leak as `[?]` into intermediate outputs and make debugging noisy.
    # Reuse the most recent PDF build's `.bbl` when available.
    src_bbl = p.notes_output / "ece657_notes.bbl"
    if src_bbl.exists():
        try:
            shutil.copyfile(src_bbl, aux_out_dir / f"{jobname}.bbl")
        except OSError:
            pass

    try:
        for _ in range(2):
            _run(
                [
                    "pdflatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-jobname",
                    jobname,
                    "-output-directory",
                    str(aux_out_dir),
                    str(tex.name),
                ],
                cwd=p.notes_output,
            )
    except SystemExit:
        return AuxInfo(numbers=load_aux_label_numbers(aux_path=aux_fallback), aux_path=aux_fallback)

    if aux_out.exists():
        return AuxInfo(numbers=load_aux_label_numbers(aux_path=aux_out), aux_path=aux_out)
    return AuxInfo(numbers=load_aux_label_numbers(aux_path=aux_fallback), aux_path=aux_fallback)


def _extract_aux_labels(aux_path: Path, *, prefix: str) -> list[str]:
    """
    Extract label names from a LaTeX .aux file via \\newlabel{...}{...}.
    """
    try:
        s = aux_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    pat = re.compile(r"\\newlabel\{(" + re.escape(prefix) + r"[^}]+)\}\{")
    labs = sorted(set(m.group(1) for m in pat.finditer(s)))
    # Exclude cleveref helper labels like `fig:...@cref` and similar.
    labs = [l for l in labs if "@" not in l]
    return labs


def _sips_dimensions(path: Path) -> tuple[int, int] | None:
    """
    Use macOS `sips` to read image dimensions for common formats.
    """
    if shutil.which("sips") is None:
        return None
    proc = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return None
    w = h = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line.startswith("pixelWidth:"):
            try:
                w = int(line.split(":", 1)[1].strip())
            except ValueError:
                w = None
        if line.startswith("pixelHeight:"):
            try:
                h = int(line.split(":", 1)[1].strip())
            except ValueError:
                h = None
    if w and h and w > 0 and h > 0:
        return (w, h)
    return None


def _prepare_cover_for_epub(*, cover_path: Path, out_dir: Path) -> Path:
    """
    Ensure the cover is large enough and in a Kindle/Apple-friendly format.

    Strategy:
    - Convert to JPEG (quality ~92) for size efficiency.
    - Upscale to at least 2560px wide if smaller (maintain aspect).
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    out_jpg = out_dir / "cover.jpg"

    if shutil.which("sips") is None:
        return cover_path

    dims = _sips_dimensions(cover_path) or _png_dimensions(cover_path)
    if dims is None:
        # Fall back: at least convert format if possible.
        _run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "92", str(cover_path), "--out", str(out_jpg)])
        return out_jpg

    width, height = dims
    target_w = 2560

    # If aspect is far from 1:1.6, don't resample; just convert.
    aspect = (height / width) if width else 0.0
    if not (1.55 <= aspect <= 1.65):
        _run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "92", str(cover_path), "--out", str(out_jpg)])
        return out_jpg

    if width < target_w:
        _run(
            [
                "sips",
                "-s",
                "format",
                "jpeg",
                "-s",
                "formatOptions",
                "92",
                "--resampleWidth",
                str(target_w),
                str(cover_path),
                "--out",
                str(out_jpg),
            ]
        )
    else:
        _run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "92", str(cover_path), "--out", str(out_jpg)])
    return out_jpg


def _verify_epub_figures(epub_path: Path, *, expected_fig_labels: list[str] | None = None) -> None:
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

            # Guard against Pandoc's internal ref numbering drifting from the
            # PDF's global numbering. After LaTeX preprocessing we expect
            # chapter/section/figure/table refs to be emitted via \hyperref with
            # fixed text, not \ref-style data-reference attributes.
            if re.search(r'data-reference-type="ref"\s+data-reference="(chap:|sec:|fig:|tab:)', s):
                bad.append(f"{name}: contains pandoc \\ref-style crossrefs (data-reference=chap/sec/fig/tab)")

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

        if expected_fig_labels:
            # Strong guarantee: every fig: label in the build aux must appear as
            # a renderable figure block in the EPUB.
            all_xhtml = {n: z.read(n).decode("utf-8", errors="ignore") for n in xhtmls}
            for lab in expected_fig_labels:
                found = False
                for name, s in all_xhtml.items():
                    # Prefer <figure id="fig:..."> because that's what Pandoc emits.
                    m = re.search(
                        r'<figure\b[^>]*\bid="' + re.escape(lab) + r'"[^>]*>.*?</figure>',
                        s,
                        flags=re.DOTALL,
                    )
                    if not m:
                        continue
                    block = m.group(0)
                    if "<img" in block or "<svg" in block or "<math" in block:
                        found = True
                        break
                if not found:
                    bad.append(f"missing labeled figure: {lab}")

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

    aux_info = _build_aux_info(p=p)
    aux_numbers = aux_info.numbers
    doc_body = inject_equation_targets(doc_body)
    doc_body = rewrite_crossrefs(doc_body, aux_numbers=aux_numbers)
    doc_body = prefix_chapter_sections(doc_body, aux_numbers=aux_numbers)
    doc_body = prefix_numbered_headings(doc_body, aux_numbers=aux_numbers)

    tikz_blocks = extract_tikz_blocks(doc_body)
    rendered: dict = {}
    tikz_dpi = int(getattr(build, "_tikz_dpi", 300))  # set by main()
    tikz_min_w = int(getattr(build, "_tikz_min_w", 0))  # set by main()
    tikz_min_h = int(getattr(build, "_tikz_min_h", 0))  # set by main()
    tikz_max_dpi = int(getattr(build, "_tikz_max_dpi", 0))  # set by main()
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
        # Some TikZ figures are short line art; increase DPI only for those to
        # keep them crisp on high-density displays without inflating every figure.
        if ok and tikz_max_dpi > 0 and (tikz_min_w > 0 or tikz_min_h > 0):
            dims = _png_dimensions(out_png)
            if dims:
                w, h = dims
                need = 1.0
                if tikz_min_w > 0:
                    need = max(need, tikz_min_w / max(1, w))
                if tikz_min_h > 0:
                    need = max(need, tikz_min_h / max(1, h))
                if need > 1.02:
                    new_dpi = int(min(tikz_max_dpi, int((tikz_dpi * need) + 0.999)))
                    if new_dpi > tikz_dpi:
                        ok2 = compile_tikz_block_to_png(
                            tikz_code=block.content,
                            out_png=out_png,
                            notes_output_dir=p.notes_output,
                            log_dir=p.tikz_logs,
                            stem=name,
                            dpi=new_dpi,
                        )
                        ok = ok2 or ok
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
    asset_dpi = int(getattr(build, "_asset_dpi", int(getattr(build, "_tikz_dpi", 600))))  # set by main()
    doc_body = rasterize_pdf_includegraphics(
        doc_body, repo_root=p.repo_root, notes_output_dir=p.notes_output, media_dir=p.media, dpi=asset_dpi
    )
    doc_body = promote_displaystyle_math(doc_body)
    doc_body = promote_long_inline_math(doc_body)
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
    identifier = metadata.get("identifier")
    publisher = metadata.get("publisher")
    rights = metadata.get("rights")
    cover_val = metadata.get("cover_image") or metadata.get("cover") or metadata.get("cover-image")
    if title:
        pandoc_metadata_args += ["-M", f"title={title}"]
    if creator:
        pandoc_metadata_args += ["-M", f"author={creator}"]
    if lang:
        pandoc_metadata_args += ["-M", f"lang={lang}"]
    # Publishing metadata: keep stable across rebuilds for consistency in readers and stores.
    if identifier:
        pandoc_metadata_args += ["-M", f"identifier={identifier}"]
    if publisher:
        pandoc_metadata_args += ["-M", f"publisher={publisher}"]
    if rights:
        pandoc_metadata_args += ["-M", f"rights={rights}"]

    cover_path: Path | None = None
    if cover_val:
        cand = Path(str(cover_val))
        if not cand.is_absolute():
            # Prefer paths relative to notes_output (same folder as metadata).
            cand_notes = (p.notes_output / cand).resolve()
            cand_repo = (p.repo_root / cand).resolve()
            if cand_notes.exists():
                cand = cand_notes
            elif cand_repo.exists():
                cand = cand_repo
        if cand.exists() and cand.is_file():
            cover_path = cand
    if cover_path is None:
        for cand in (
            p.notes_output / "BookCover_1024x1536.png",
            p.notes_output / "BookCover.png",
            p.notes_output / "upload" / "Modern_Intelligent_Systems_cover.png",
        ):
            if cand.exists():
                cover_path = cand.resolve()
                break

    pandoc_cmd = [
        "pandoc",
        "--from=latex",
        "--to=epub3",
        "--standalone",
        "--mathml",
        # Split so each "Chapter N: ..." starts a new XHTML spine item (reader-visible unit).
        # Pandoc maps LaTeX `\section` to heading level 3 when `\part` is present:
        #   part -> h1, chapter(section) -> h3, subsection -> h4, ...
        "--split-level=3",
        "--toc",
        "--toc-depth",
        "3",
        "--css",
        str(css_path),
        *(["--epub-cover-image", str(_prepare_cover_for_epub(cover_path=cover_path, out_dir=p.artifacts / "tmp" / "cover"))] if cover_path else []),
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
        expected = _extract_aux_labels(aux_info.aux_path, prefix="fig:")
        _verify_epub_figures(out_epub, expected_fig_labels=expected)
    if not skip_validate:
        run_epubcheck(out_epub, out_dir=p.artifacts / "epubcheck")
    return out_epub


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--variant", choices=["apple", "kindle", "both"], default="apple")
    parser.add_argument("--clean", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--skip-validate", action="store_true")
    # High-DPI by default: this is an electronic book; prioritize crisp figures.
    parser.add_argument("--tikz-dpi", type=int, default=1200)
    parser.add_argument("--asset-dpi", type=int, default=1200)
    parser.add_argument("--tikz-min-width", type=int, default=2400)
    parser.add_argument("--tikz-min-height", type=int, default=1400)
    parser.add_argument("--tikz-max-dpi", type=int, default=3000)
    parser.add_argument("--strict-figures", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)

    setattr(build, "_tikz_dpi", args.tikz_dpi)
    setattr(build, "_asset_dpi", args.asset_dpi)
    setattr(build, "_strict_figures", args.strict_figures)
    setattr(build, "_tikz_min_w", args.tikz_min_width)
    setattr(build, "_tikz_min_h", args.tikz_min_height)
    setattr(build, "_tikz_max_dpi", args.tikz_max_dpi)

    if args.variant == "both":
        build(variant="apple", clean=args.clean, skip_validate=args.skip_validate)
        build(variant="kindle", clean=False, skip_validate=args.skip_validate)
        return 0

    build(variant=args.variant, clean=args.clean, skip_validate=args.skip_validate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
