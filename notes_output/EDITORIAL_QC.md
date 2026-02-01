# Editorial & publishing QC workflow

This project is a book manuscript; publishing readiness requires more than “it compiles”.

## Goal
Catch and fix issues in:
- Table of contents / list of figures / list of tables typography (spacing, leader dots, page-number collisions).
- Tables and figures layout (overfull boxes, bad breaks, inconsistent caption style).
- Language consistency (dialect, spelling variants, hyphenation/dashes).
- Formatting consistency (indentation, stray tabs, trailing whitespace).

## The process (repeatable)
1) **Build + QC report (automated)**
   From `notes_output/` run:
   - `./scripts/run_editorial_qc.sh`
   - Review: `artifacts/qc/publish_qc_report.md`

2) **Optional auto-fixes (mechanical, safe)**
   - Normalize tabs/trailing whitespace: `python3 scripts/fix_whitespace.py --root .`
   - Apply house-style spellings (per `editorial_style.toml`): `python3 scripts/apply_house_style.py --root .`

3) **Fix “layout blockers” first**
   - Address `overfull_hbox` in the report first (these frequently correspond to tables/figures that “look weird” in the PDF).
   - For TOC/LOF/LOT issues, start in `ece657_notes.tex` (TOC widths, page-number box size) and verify with a fresh build.

4) **Language/style pass**
   - House style is tracked in `editorial_style.toml`. Update it before large systematic changes.
   - When changing dialect/spelling globally, do it as a dedicated pass (small, reviewable diff).

5) **Manual “editor eyes” scan (human or LLM)**
   - TOC pages: look for titles colliding with page numbers, missing/odd leader dots, and inconsistent capitalization.
   - LOF/LOT pages: check that entries don’t overflow and captions are consistent (punctuation, bracket tags like `[Schematic]`).
   - Tables: verify consistent use of `booktabs` (no vertical rules), readable line breaks, aligned columns, and consistent terminology.
   - Lists: check consistent dash usage and indentation in prose and `itemize` environments.

## Practical fixes (patterns)
- **TOC page numbers colliding**: increase `\\@pnumwidth` and `\\@tocrmarg` in `ece657_notes.tex`.
- **Subsection numbers “stick” to titles** (e.g., `19.25Pseudocode`): increase subsection number width by redefining `\\l@subsection`.
- **Wide tables**:
  - Prefer `tabularx`/`p{}` columns with controlled widths.
  - Break long unhyphenable tokens (URLs, code identifiers) with `\\url{...}` or discretionary breaks.
  - Consider splitting “two ideas in one table” into two separate tables.

## What to update for new LLM onboarding
- Keep `ONBOARDING.md` current about:
  - The QC command(s) to run
  - Where the report is written
  - Where house style decisions live (`editorial_style.toml`)
