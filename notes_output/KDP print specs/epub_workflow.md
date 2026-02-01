## ePub generation workflow

### 1) Generate a cover (optional, via OpenAI API)
Run the helper script (uses `OPENAI_API_KEY` from `.env`):

```bash
python scripts/generate_cover.py
```

Output: `notes_output/KDP print specs/cover.png` (wide). Crop/resize to your 7×10 trim at 300 dpi if embedding in print/ePub. To embed in the ePub, add `--epub-cover-image=notes_output/KDP\ print\ specs/cover.png` to the Pandoc command below.

### 2) Build a reflowable ePub with Pandoc

Requirements: `pandoc` installed.

```bash
cd /path/to/ece657Book
pandoc \
  --from=latex \
  --to=epub3 \
  --metadata title="Modern Intelligent Systems: A Graduate Companion" \
  --metadata author="Haitham Amar" \
  --output "notes_output/KDP print specs/modern_intelligent_systems.epub" \
  notes_output/preface.tex \
  notes_output/lecture_1.tex \
  notes_output/lecture_2_part_i.tex \
  notes_output/lecture_2_part_ii.tex \
  notes_output/lecture_3_part_i.tex \
  notes_output/lecture_3_part_ii.tex \
  notes_output/lecture_4_part_i.tex \
  notes_output/lecture_4_part_ii.tex \
  notes_output/lecture_5_part_i.tex \
  notes_output/lecture_5_part_ii.tex \
  notes_output/lecture_6.tex \
  notes_output/lecture_7.tex \
  notes_output/lecture_8_part_i.tex \
  notes_output/lecture_8_part_ii.tex \
  notes_output/lecture_9.tex \
  notes_output/lecture_10_part_i.tex \
  notes_output/lecture_10_part_ii.tex \
  notes_output/lecture_11.tex \
  notes_output/notation.tex \
  notes_output/appendix_linear_systems.tex \
  notes_output/appendix_logistics.tex
```

Optional flags:
- `--epub-cover-image=notes_output/KDP\ print\ specs/cover.png`
- `--mathjax` (if you want MathJax rendering of formulas; otherwise Pandoc emits MathML where supported)

### 3) Accessibility and cleanup
- Ensure figures have alt text in the TeX sources; Pandoc will carry them into the ePub.
- Keep the ePub reflowable: avoid hard page breaks and fixed-width figures where possible.
- Validate with `epubcheck` before upload.

### 4) Print PDF reminders (already set)
- Trim: 7×10 in; mirrored margins with 1″ inner, 0.75″ outer, 0.75″/0.8″ top/bottom (see `ece657_notes.tex`).
- Embed fonts (tectonic does this); keep figures vector/300 dpi; running headers updated to the new title.
