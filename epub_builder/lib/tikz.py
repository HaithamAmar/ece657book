from __future__ import annotations

import hashlib
import shutil
import subprocess
from pathlib import Path


def _preamble() -> str:
    # Keep this minimal but compatible with common pgfplots/TikZ usage.
    return r"""
\documentclass[tikz,border=2pt]{standalone}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{positioning,arrows.meta,decorations.pathreplacing,decorations.markings,calc,shapes.geometric,matrix,backgrounds,fit,patterns,shadows.blur}
\usepackage{pgfplots}
\usepgfplotslibrary{groupplots,fillbetween}
\pgfplotsset{compat=1.18}

% Match the book's common figure palette so extracted TikZ blocks compile.
\pgfplotsset{every axis/.append style={
    tick label style={font=\scriptsize},
    label style={font=\small},
    legend style={font=\scriptsize, fill=none, draw=none},
    line width=0.9pt,
    grid=both,
    grid style={gray!15}
}}
\definecolor{cbBlue}{RGB}{0,114,178}
\definecolor{cbOrange}{RGB}{230,159,0}
\definecolor{cbGreen}{RGB}{0,158,115}
\definecolor{cbPink}{RGB}{213,94,0}
\definecolor{cbGray}{gray}{0.45}
\definecolor{lstmCbBlue}{RGB}{218, 232, 252}
\definecolor{lstmCbOrange}{RGB}{255, 230, 204}
\definecolor{lstmCbGray}{RGB}{235, 235, 235}
\definecolor{lstmArrowGray}{RGB}{100, 100, 100}
\definecolor{gruCbBlue}{RGB}{218, 232, 252}
\definecolor{gruCbOrange}{RGB}{255, 230, 204}
\definecolor{gruCbGray}{RGB}{235, 235, 235}
\definecolor{gruArrowGray}{RGB}{100, 100, 100}
\pgfplotscreateplotcyclelist{cbPalette}{%
    {cbBlue, mark=*, mark options={scale=0.6,solid}},
    {cbOrange, mark=square*, mark options={scale=0.6,solid}},
    {cbGreen, mark=triangle*, mark options={scale=0.6,solid}},
    {cbPink, mark=diamond*, mark options={scale=0.6,solid}}
}
\pgfplotsset{cycle list name=cbPalette}

% Make thin line-art readable on high-DPI ebook readers.
\tikzset{
    every picture/.append style={line width=0.8pt},
    every node/.append style={inner sep=3pt},
}

% SOM helper functions (used in lecture_5_part_i.tex figures)
\pgfmathdeclarefunction{somindex}{2}{%
    \pgfmathsetmacro{\da}{(#1-0.2)^2 + (#2-0.2)^2}%
    \pgfmathsetmacro{\db}{(#1-0.8)^2 + (#2-0.25)^2}%
    \pgfmathsetmacro{\dc}{(#1-0.28)^2 + (#2-0.78)^2}%
    \pgfmathsetmacro{\dd}{(#1-0.78)^2 + (#2-0.78)^2}%
    \pgfmathparse{%
        (\da<=\db) && (\da<=\dc) && (\da<=\dd) ? 0 :
        ((\db<=\da) && (\db<=\dc) && (\db<=\dd) ? 1 :
        ((\dc<=\da) && (\dc<=\db) && (\dc<=\dd) ? 2 : 3))}%
}
\pgfmathdeclarefunction{somsoftpeak}{2}{%
    \pgfmathsetmacro{\beta}{8}%
    \pgfmathsetmacro{\ta}{exp(-\beta*((#1-0.2)^2 + (#2-0.2)^2))}%
    \pgfmathsetmacro{\tb}{exp(-\beta*((#1-0.8)^2 + (#2-0.25)^2))}%
    \pgfmathsetmacro{\tc}{exp(-\beta*((#1-0.28)^2 + (#2-0.78)^2))}%
    \pgfmathsetmacro{\td}{exp(-\beta*((#1-0.78)^2 + (#2-0.78)^2))}%
    \pgfmathsetmacro{\sumw}{\ta+\tb+\tc+\td}%
    \pgfmathsetmacro{\maxw}{max(max(\ta,\tb),max(\tc,\td))}%
    \pgfmathparse{\maxw/\sumw}%
}
\pgfplotsset{colormap={somregions}{
        color(0cm)=(cbBlue);
        color(0.33cm)=(cbOrange);
        color(0.66cm)=(cbGreen);
        color(1cm)=(cbPink)
}}

% Some book TikZ blocks call this helper after axes to keep background layers
% consistent when tcolorbox is present. For standalone compilation it is safe
% as a minimal layer initializer.
\pgfdeclarelayer{background}
\pgfsetlayers{background,main}
\providecommand{\ensuretikzbackgroundlayers}{\pgfsetlayers{background,main}}
\begin{document}
"""


def _sha256_text(text: str) -> str:
    h = hashlib.sha256()
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def compile_tikz_block_to_png(
    *,
    tikz_code: str,
    out_png: Path,
    notes_output_dir: Path,
    log_dir: Path,
    stem: str,
    dpi: int,
) -> bool:
    out_png.parent.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    cache_key = _sha256_text(f"dpi={dpi}\n" + _preamble() + "\n" + tikz_code)
    cache_path = out_png.with_suffix(out_png.suffix + ".sha256")
    if out_png.exists() and cache_path.exists():
        try:
            if cache_path.read_text(encoding="utf-8").strip() == cache_key:
                return True
        except OSError:
            pass

    work_dir = log_dir / stem
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)

    tex_path = work_dir / f"{stem}.tex"
    tex_path.write_text(_preamble() + tikz_code + "\n\\end{document}\n", encoding="utf-8")

    pdf_path = work_dir / f"{stem}.pdf"
    log_path = log_dir / f"{stem}.pdflatex.txt"

    cmd = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-output-directory",
        str(work_dir),
        str(tex_path),
    ]
    with log_path.open("w", encoding="utf-8") as logf:
        proc = subprocess.run(cmd, cwd=notes_output_dir, stdout=logf, stderr=subprocess.STDOUT, check=False)
    if proc.returncode != 0 or not pdf_path.exists():
        return False

    ppm_cmd = ["pdftoppm", "-r", str(dpi), "-png", "-singlefile", str(pdf_path), str(work_dir / stem)]
    proc2 = subprocess.run(ppm_cmd, cwd=notes_output_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    gen = work_dir / f"{stem}.png"
    if proc2.returncode != 0 or not gen.exists():
        return False

    shutil.copyfile(gen, out_png)
    try:
        cache_path.write_text(cache_key + "\n", encoding="utf-8")
    except OSError:
        pass
    return True
