# Production Roadmap (Publish-Grade PDF + Apple + Kindle)

This is the editor-facing roadmap for pushing **ECE 657 / Modern Intelligent Systems** from “working EPUB/PDF” to **high production value** suitable for a premium-priced academic companion.

Goals:
- **Continuity**: no “random” formatting or numbering behaviors.
- **Crispness**: figures, math, and tables remain legible when zoomed.
- **Platform correctness**: Apple Books and Kindle/KDP behave as expected.
- **Reproducibility**: future humans/LLMs can rerun checks and understand decisions.

Non-goals:
- Rewriting core content in this pass (unless needed to fix correctness/continuity).

## Current state (baseline)

- Source LaTeX lives in `notes_output/`.
- EPUBs are built via `epub_builder/` and output to:
  - Apple: `epub_builder/dist/ece657_ebook_apple.epub`
  - Kindle: `epub_builder/dist/ece657_ebook_kindle.epub`
- Numbering is treated as **data** and sourced from a LaTeX-generated `.aux` during the EPUB build:
  - Canonical aux for EPUB QC: `epub_builder/artifacts/tmp/aux/ece657_notes_epub_aux.aux`

## Quality bar (what “publish-grade” means here)

### Must-have (release blockers)
- No missing figures (including TikZ failures or missing media in the EPUB zip).
- All cross-references read naturally:
  - “Chapter 14”, “Section 3.7”, “Figure 11”, “Table 4”, “Appendix B”, “(4.1)”, etc.
- Equation numbering is consistent with the PDF conventions:
  - If it’s meant to be numbered/referenced, it must be an `equation` (or equivalent) with a stable `\\label{eq:...}`.
  - “Display-ish inline math” must not clip.
- Tables are readable on phone + tablet + desktop:
  - No “microscopic” tables due to over-wide layouts.
  - No overflow / clipping.
- Cover thumbnail is correct in Apple Books and in common OS previews (Finder/QuickLook).
- Metadata is complete and consistent (title/subtitle/author/publisher/rights/language/identifiers).
- Automated QC outputs exist and are current for the release candidate.

### Should-have (strongly recommended before pricing high)
- Accessibility pass:
  - `alt` text for all figures.
  - Table headers are proper `<th>` with correct scope.
  - Reasonable heading semantics (no “skips” that break screen readers).
- A consistent typographic system across PDF + EPUB (headings, callouts, code blocks, captions).
- Kindle-specific verification on **Kindle Previewer** (not just “it builds”).

## Release workflow (repeatable)

1) **Clean rebuild** (Apple + Kindle):
```bash
python3 epub_builder/build.py --variant both --clean
```

2) **Layout overflow audit** (Apple EPUB):
```bash
export TMPDIR=/tmp
epub_builder/.venv/bin/python epub_builder/scripts/audit_epub_layout.py \
  --epub epub_builder/dist/ece657_ebook_apple.epub \
  --out-md notes_output/EPUB_EDITORIAL_AUDIT.md \
  --viewport-w 1000 \
  --viewport-h 1400
```

3) **Image audits**:
```bash
epub_builder/.venv/bin/python epub_builder/scripts/audit_epub_image_quality.py \
  --epub epub_builder/dist/ece657_ebook_apple.epub \
  --out-json epub_builder/artifacts/qc/epub_image_quality_$(date +%Y%m%d_%H%M%S).json \
  --out-md notes_output/EPUB_IMAGE_QC.md \
  --top 60
```

4) **Spot-check bundle: PDF vs EPUB** (representative figures + some equations):
```bash
epub_builder/.venv/bin/python epub_builder/scripts/qc_epub_vs_pdf.py \
  --epub epub_builder/dist/ece657_ebook_apple.epub \
  --pdf notes_output/ece657_notes.pdf \
  --aux epub_builder/artifacts/tmp/aux/ece657_notes_epub_aux.aux \
  --out epub_builder/artifacts/qc/pdf_vs_epub_$(date +%Y%m%d_%H%M%S)_apple \
  --max-eq 40
```

5) **Human visual pass (non-negotiable)**:
- Apple Books (macOS + iOS).
- Kindle Previewer (KDP).
- Verify: cover thumbnail, TOC/navigation, a few “worst case” pages (dense math, wide tables, figure-heavy chapters).

## High-impact improvements (prioritized backlog)

### P0 — Structural / metadata (platform correctness)
- Ensure OPF metadata is “publisher-grade”:
  - `dc:title`, `dc:creator`, `dc:language`, `dc:identifier`, `dc:publisher`, `dc:rights`, `dc:date`.
  - Apple/KDP often behave better with explicit `modified` timestamps and consistent identifiers.
- Ensure TOC depth is intentional:
  - Decide the maximum depth (e.g., Chapters + Sections, but not Subsubsections) and enforce it.
- Cover asset:
  - Produce a **higher-resolution cover** (recommend: 3000×4800 PNG/JPG) and set `notes_output/book_metadata.json: cover_image`.

### P0 — Cross-reference continuity (reader trust)
- Authoring rule: never write “see 14” or “see (10)” manually.
  - Always use `\\Cref{chap:...}`, `\\Cref{sec:...}`, `\\Cref{fig:...}`, `\\Cref{tab:...}`, `\\eqref{eq:...}`.
- Policy for appendices:
  - Use `app:` labels for appendix chapters and **never** refer to them using raw numbers.

### P0 — Equation policy (consistency + no clipping)
Problem pattern: a meaningful derivation is sometimes typeset as inline math (or displaystyle inline), which can clip and also breaks equation numbering expectations.

Recommended authoring policy:
- If the expression is important enough to be referenced later: use `equation` (or `align`) + `\\label{eq:...}`.
- If the expression is display math but not meant to be numbered: use `\\[ ... \\]` (not `\\(\\displaystyle ...\\)`).
- Avoid `$$ ... $$` entirely.

Recommended clean-up (source-level, not hardcoded counters):
- Audit for large inline math blocks and promote them to `equation`/`align` where appropriate.
- For multi-line derivations:
  - Prefer `align` with *intentional* labeling (label only the line(s) referenced later).
  - If Kindle rendering is unreliable, consider converting a small set of “hero derivations” to figures (last resort).

### P1 — Tables (EPUB-first redesign)
Known risk: LaTeX tables that look fine in PDF can be awkward in reflowable EPUB.

Recommended policy:
- Keep tables narrow (≤ 3–4 columns) where possible.
- Convert dense tables to:
  - bullet lists,
  - definition blocks,
  - or multiple smaller tables.

Recommended technical approach:
- Ensure EPUB HTML wraps tables in a scroll container (so they never become microscopic).
- Add a manual override mechanism:
  - for specific tables, export as a high-DPI figure and include as an image (Kindle can be picky; use sparingly).

### P1 — Figures (crispness and “no wasted whitespace”)
Even high-resolution PNGs can feel low-quality if:
- the figure is mostly whitespace (tiny content),
- strokes are too thin relative to device pixel ratio,
- font sizes are too small.

Recommended policy:
- Standardize figure typography (font family + sizes) across matplotlib/TikZ.
- Enforce minimum readable label sizes at phone-width.
- Prefer vector sources (PDF/SVG) and rasterize at high DPI only when needed.

Recommended pipeline enhancements (optional but high ROI):
- Add automatic trimming/cropping for PNG outputs with a small margin (remove useless whitespace).
- For line-art figures, evaluate **SVG in EPUB** (Apple Books supports it well; Kindle support must be tested).

### P1 — Typography / CSS system (make it look like a book)
Define a consistent, book-like reading experience:
- Base font size, line height, margins, paragraph spacing.
- Heading scale and spacing (“rhythm”).
- Callouts (asides/notes/exercises) must have a consistent style system.
- Captions: consistent size/spacing and placement.
- Code blocks: consistent font and wrapping behavior.

### P2 — Accessibility and semantics (premium quality)
- Ensure every `<img>` has `alt` text (use caption as a baseline; refine for meaning).
- Ensure tables have headers (`<th>`) and a meaningful reading order.
- Ensure heading hierarchy is valid (no jumps that confuse navigation).

### P2 — Editorial continuity (content-level polish)
These are “editorial integrity” tasks that make a premium book feel premium:
- A consistent “notation + conventions” approach:
  - Symbol list and reused notation across chapters.
- Chapter-end consistency:
  - summary,
  - common pitfalls,
  - exercises,
  - references note.
- Terminology consistency:
  - “dataset split” vs “train/val/test”, “objective” vs “loss”, etc.
- Tighten transitions between strands (symbolic → supervised → neural → fuzzy → evolutionary) using the roadmap.

## Recommended working mode (to avoid regressions)

- Prefer changing the **LaTeX sources** to encode intent (labels, equation environments, table structure).
- Use the EPUB builder to:
  - translate consistently,
  - enforce invariants,
  - and catch missing assets.
- Avoid hardcoding numbers in the pipeline (counters should come from `.aux` + stable labels).

