# Figure Style Guide (PDF + EPUB)

This project targets a premium, publication-grade look. Figures must be readable on phone-sized EPUB readers and still look crisp in PDF.

## Matplotlib figures (Python)

- **Single source of truth:** `scripts/figure_style.py`.
- Every `scripts/gen_fig*.py` must import and call `apply_style(...)` (no ad-hoc `plt.rcParams.update(...)` blocks).
- Always export **both**:
  - Vector: `.pdf` (preferred source for the EPUB pipeline; it gets rasterized at high DPI)
  - Raster: `.png` at 300 DPI (useful for quick previews and as a fallback)
- Save with **tight bounding boxes** (handled globally via `savefig.bbox='tight'` in `figure_style.py`).

## TikZ / PGFPlots figures (LaTeX)

- TikZ figures are pre-rendered as high-DPI PNGs for EPUB via `epub_builder/lib/tikz.py`.
- Global defaults for ebook readability (line width, node padding) live in the TikZ standalone preamble there; if you change figure aesthetics, update that preamble and rebuild.

## “Definition of done” (visual)

- No figure should require zooming to read labels on a typical phone viewport (~375–430 px wide).
- No heavy whitespace borders (tight crop).
- Line-art is not “hairline thin” (strokes visible at normal zoom).

## Captions (house rule)

- Prefer captions that start with `Schematic:` for conceptual visuals.
- For `Schematic:` figures, end the caption with a short, decision-oriented sentence:
  - `Use this when...`
  This keeps schematics from becoming decorative and helps reflowable EPUB readers understand why the visual matters.
