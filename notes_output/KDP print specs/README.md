## KDP Print Specs for “Modern Intelligent Systems”

- **Trim size (print PDF):** 7 × 10 in (better for equations/figures). If you prefer the smaller standard, 6 × 9 in is acceptable—pick one and stay consistent in documentclass geometry.
- **Margins (for 7 × 10):**
  - Up to ~500 pages: outside/top/bottom ≥ 0.75 in; gutter ≥ 0.875–1.0 in.
  - Thicker books (>700 pages): increase gutter to 1.0–1.125 in.
  - Mirror margins enabled in LaTeX so odd/even pages swap gutter.
- **Bleed:** None (figures contained within margins). If you add bleed, set 0.125 in on all sides and export accordingly.
- **Figures:** Use vector (TikZ/PGF) wherever possible; for rasters keep ≥300 dpi at final size. Ensure color maps remain legible in grayscale.
- **Fonts:** Embed all fonts in the print PDF (tectonic/xelatex already does this); avoid system-only fonts.
- **Page layout:**
  - Clean page numbering; no blank-numbered pages.
  - Consistent running headers/footers (“Modern Intelligent Systems” + chapter title).
  - Section headings consistent in size/weight.
- **Links/metadata:** Color links fine for print; ensure PDF metadata matches title/subtitle.

## eBook / ePub Notes
- KDP prefers reflowable ePub. Export a reflowable version (e.g., via Pandoc) with:
  - Single-column flow, no fixed page sizes.
  - Alt text for all figures; consider converting math to MathML where supported or provide PNG fallbacks.
  - Avoid hard page breaks; use semantic headings.
- For fixed-layout (if absolutely necessary), match the chosen trim (7 × 10 or 6 × 9) and keep total package size within KDP limits.

## Action Items
1) Set geometry in `ece657_notes.tex` to the chosen trim + mirrored margins/gutter.
2) Rebuild print PDF with font embedding verified (check with `pdffonts`).
3) Spot-check figure resolution; regenerate any raster assets below 300 dpi.
4) Produce a reflowable ePub version from the TeX sources with alt text preserved.
