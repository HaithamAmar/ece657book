# EPUB Publishing QC (Apple + Kindle)

This document tracks EPUB-quality decisions, automated checks, known issues, and remediation ideas.
It is written so a future reviewer (human or LLM) can reproduce results and understand why each
change exists.

## Scope

- Source LaTeX lives in `notes_output/`.
- EPUBs are built via the isolated Pandoc-based pipeline in `epub_builder/`.
- Targets: Apple Books and Kindle (EPUB3 variants).

## Current required outputs

- Apple: `epub_builder/dist/ece657_ebook_apple.epub`
- Kindle: `epub_builder/dist/ece657_ebook_kindle.epub`

## Critical invariants (publish-grade)

1. **No missing figures**: the build must fail if any figure is missing (including TikZ failures).
2. **Reference continuity**: cross-references (Chapter/Figure/Table/Section/Appendix/Equation) must be readable and numbered consistently with the PDF.
3. **High-resolution figures**: images must be crisp on high-density displays; prefer vector→high-DPI rasterization when necessary.
4. **No clipping**: long display math must not be cut off; allow scrolling as a last resort.

## Automated checks (run before every release)

### 1) Clean rebuild (both variants)

```bash
python3 epub_builder/build.py --variant both --clean
```

### Cover source

- Current cover source is configured in `notes_output/book_metadata.json` under `cover_image`.
- Prefer the higher-resolution `notes_output/BookCover.png` (1600×2560) over `notes_output/BookCover_1024x1536.png`.

### 2) Regression screenshots: PDF vs EPUB (figures/tables/equations)

Produces side-by-side images keyed by `.aux` labels.

```bash
epub_builder/.venv/bin/python epub_builder/scripts/qc_epub_vs_pdf.py \
  --epub epub_builder/dist/ece657_ebook_apple.epub \
  --pdf notes_output/ece657_notes.pdf \
  --aux notes_output/ece657_notes.aux \
  --out epub_builder/artifacts/qc/pdf_vs_epub_$(date +%Y%m%d_%H%M%S)_apple \
  --max-eq 0
```

Repeat for Kindle by swapping `--epub`.

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
