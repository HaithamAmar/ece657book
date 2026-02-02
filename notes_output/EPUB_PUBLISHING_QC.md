# EPUB Publishing QC (Apple + Kindle)

This document tracks EPUB-quality decisions, automated checks, known issues, and remediation ideas.
It is written so a future reviewer (human or LLM) can reproduce results and understand why each
change exists.

## Scope

- Source LaTeX lives in `notes_output/`.
- EPUBs are built via the isolated Pandoc-based pipeline in `epub_builder/`.
- Targets: Apple Books and Kindle (EPUB3 variants).
- For the broader “publish-grade” backlog and editorial standards, see `notes_output/PRODUCTION_ROADMAP.md`.
- For operator docs (fresh machine + release procedure), see:
  - `notes_output/SETUP_CHECKLIST.md`
  - `notes_output/RELEASE_PLAYBOOK.md`
  - `notes_output/TEST_MATRIX.md`

## TOC and heading policy (EPUB)

- EPUB navigation TOC depth is capped at **2** (chapters + sections). Subsubsections are intentionally excluded to avoid clutter on e-readers.
- Starred headings (`\\section*`, `\\subsection*`) are reserved for front/end matter; within numbered chapters, prefer numbered headings or demote short “bridge” headings to `\\paragraph{...}` so they do not appear as unnumbered TOC entries.

## Equation labeling policy (EPUB)

- **Rule:** every numbered display-math environment (especially `\begin{align}` / `\begin{equation}`) must contain at least one `\label{eq:...}`.
- **Why:** Pandoc’s MathML output has no native equation numbers; our EPUB pipeline renders numbers only for labeled equations using the LaTeX `.aux` file.
- **Practice:** if a multi-line `align` block is just a derivation (not referenced), it may remain unlabeled *only if* it is converted to `align*`.
- **Note:** we permit “non-semantic” auto-labels in sources (e.g., `\label{eq:auto:lecture_8_part_i:3}`) when an `align` block is unreferenced but we still want its number visible in EPUB for reader trust and PDF/EPUB parity.

## Current required outputs

- Apple: `epub_builder/dist/ece657_ebook_apple.epub`
- Kindle: `epub_builder/dist/ece657_ebook_kindle.epub`

## Critical invariants (publish-grade)

1. **No missing figures**: the build must fail if any figure is missing (including TikZ failures).
   - Implementation: after building the EPUB, the builder checks that every `fig:` label present in the build `.aux` exists as a corresponding `<figure id="fig:...">` in the EPUB and that it contains renderable content (typically `<img>`).
2. **Reference continuity**: cross-references (Chapter/Figure/Table/Section/Appendix/Equation) must be readable and numbered consistently with the PDF.
   - Headings that should be numbered must have explicit `\\label{sec:...}` anchors in the LaTeX sources. Use `python3 epub_builder/scripts/add_missing_heading_labels.py` to fill in missing subsection/subsubsection labels (idempotent).
   - Equation numbers in EPUB are only shown for labeled equations. Use `python3 epub_builder/scripts/add_missing_equation_labels.py` to fill in missing `\\label{eq:...}` for `equation` environments (idempotent).
3. **High-resolution figures**: images must be crisp on high-density displays; prefer vector→high-DPI rasterization when necessary.
4. **No clipping**: long display math must not be cut off; allow scrolling as a last resort.
5. **Readable tables**: tables must never shrink to microscopic text on narrow screens.
   - Implementation: the EPUB builder wraps every HTML `<table>` in `<div class="table-wrap">` and enables horizontal scrolling in `epub_builder/epub.css`.
   - If a table is still unusable with scrolling, it must be redesigned at the LaTeX source level (split/convert to prose), not “fixed” by hardcoding sizes.

## Automated checks (run before every release)

### Prereqs (for QC scripts)

Some QC scripts use Playwright (headless Chromium) and basic image analysis deps.
If a script errors with “missing dependency”, install once into `epub_builder/.venv`:

```bash
python3 -m venv epub_builder/.venv
epub_builder/.venv/bin/pip install playwright pillow numpy opencv-python
epub_builder/.venv/bin/python -m playwright install chromium
```

### 1) Clean rebuild (both variants)

```bash
python3 epub_builder/build.py --variant both --clean
```

### Cover source

- Current cover source is configured in `notes_output/book_metadata.json` under `cover_image`.
- Prefer the higher-resolution `notes_output/BookCover.png` (1600×2560) over `notes_output/BookCover_1024x1536.png`.
 - Build behavior: the EPUB builder converts the cover to JPEG and upscales to at least 2560px wide (when smaller) for better thumbnails on high-DPI devices.
 - If Finder/Quick Look (macOS) shows a generic EPUB thumbnail, the builder postprocesses the EPUB to:
   - add an EPUB2-style `meta name="cover"` entry in the OPF
   - emit an `<img>`-based `cover.xhtml` (instead of an SVG wrapper), which is more widely thumbnail-compatible.

### 2) Regression screenshots: PDF vs EPUB (figures/tables/equations)

Produces side-by-side images keyed by `.aux` labels.

```bash
epub_builder/.venv/bin/python epub_builder/scripts/qc_epub_vs_pdf.py \
  --epub epub_builder/dist/ece657_ebook_apple.epub \
  --pdf notes_output/ece657_notes.pdf \
  --aux epub_builder/artifacts/tmp/aux/ece657_notes_epub_aux.aux \
  --out epub_builder/artifacts/qc/pdf_vs_epub_$(date +%Y%m%d_%H%M%S)_apple \
  --max-eq 0
```

Repeat for Kindle by swapping `--epub`.

Notes:
- The Pandoc builder generates `epub_builder/artifacts/tmp/aux/ece657_notes_epub_aux.aux` on every build; prefer it for EPUB QC so section/equation numbering matches the exact sources used to build the EPUB.
- If you are doing PDF-only regression checks, you can use `notes_output/ece657_notes.aux` instead (produced by the PDF toolchain).
- The aux compile is run only to extract numbering and does **not** run BibTeX; ignore “undefined citations” / missing `.bbl` warnings in `ece657_notes_epub_aux.log`.

### 3) Image resolution audit (EPUB media)

Flags embedded images below a minimum resolution threshold.

```bash
epub_builder/.venv/bin/python epub_builder/scripts/audit_epub_images.py \
  --epub epub_builder/dist/ece657_ebook_apple.epub \
  --out epub_builder/artifacts/qc/epub_image_audit_$(date +%Y%m%d_%H%M%S).json \
  --min-width 2400 \
  --min-height 1400
```

### 4) Layout overflow audit (all XHTML chapters)

Finds elements that extend beyond the viewport (math/code/tables/images).

```bash
export TMPDIR=/tmp
epub_builder/.venv/bin/python epub_builder/scripts/audit_epub_layout.py \
  --epub epub_builder/dist/ece657_ebook_apple.epub \
  --out-md notes_output/EPUB_EDITORIAL_AUDIT.md \
  --viewport-w 1000 \
  --viewport-h 1400
```

### 5) Table audit (EPUB)

Lists every table (caption + column estimate) to help identify “must redesign” offenders.

```bash
stamp=$(date +%Y%m%d_%H%M%S)
python3 epub_builder/scripts/audit_epub_tables.py \
  --epub epub_builder/dist/ece657_ebook_apple.epub \
  --out-json epub_builder/artifacts/qc/epub_table_audit_${stamp}.json \
  --out-md notes_output/EPUB_TABLES_AUDIT.md \
  --flag-cols 5
```

Policy and remediation guidance live in `notes_output/EPUB_TABLES.md`.

## Known issues fixed (and why)

### Appendix references showing as “Appendix 22”

- **Symptom**: “Appendix 22” appeared in EPUB (Pandoc renumbered `\ref{app:...}`).
- **Root cause**: `app:` labels were not rewritten in the EPUB pipeline, so Pandoc applied its own counters.
- **Fix**: Rewrite `app:` references using `.aux` numbering (A/B/C) and hyperlink the correct appendix anchor.
- **Implementation**: `epub_builder/lib/latex.py` (`rewrite_crossrefs` now handles `app:` for `\ref`, `\Cref`, and `\Crefrange`).

### Display math clipped at right edge

- **Symptom**: long derivation line in “Two safe options from here” was cut off.
- **Root cause**: LaTeX used `\(\displaystyle ...\)` (inline math) preceded by `\\`; Pandoc emitted `<br/>` + inline MathML, which can overflow without scrolling.
- **Fix**:
  - Promote likely-display `\(\displaystyle ...\)` to `\[...\]` (block math) during preprocessing.
  - Add CSS safety net: `math[display="block"]` scrolls horizontally when needed.
- **Implementation**:
  - `epub_builder/lib/latex.py`: `promote_displaystyle_math()`
  - `epub_builder/build.py`: call `promote_displaystyle_math()` before Pandoc
  - `epub_builder/epub.css`: `math[display="block"] { overflow-x: auto; }`

## Editorial / continuity checklist (human review)

Automated tools cannot catch these reliably; review visually in Apple Books and Kindle Previewer:

- Chapter openings: consistent “Chapter N: Title” heading and a short lead paragraph.
- References: “Chapter”, “Section”, “Figure”, “Table”, “Appendix”, and equation numbers are present and consistent.
- Callouts/boxes: consistent styling and titles; no accidental truncation of titles.
- Tables: do not stretch to unreadable whitespace; align columns sensibly.
- Figures: captions match the figure; no blurry or mismatched assets.
- Voice: no “these notes / last lecture / course website” phrasing inside numbered chapters.

## High-priority future improvements (if needed for a $199.99 academic book)

- Dedicated typography pass (body font, headings, caption rhythm, blockquote spacing) with Apple/Kindle-specific CSS variants.
- Reader-tested MathML fallback for Kindle devices that don’t fully support MathML (rasterized math variant).
- Formal accessibility pass: alt-text for figures, semantic landmarks, and navigational TOC validation.
