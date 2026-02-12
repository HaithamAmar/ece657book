Modern Intelligent Systems — onboarding guide
===========================================

Structure & logic
-----------------
- All book content lives in `notes_output/`. `ece657_notes.tex` is the print/PDF entrypoint: it includes unnumbered opening material (`preface.tex`, `notation.tex`), then the numbered chapter files (via `\input{...}`), then `key_takeaways.tex`, then appendices.
- Chapter progression and rationale:
  1. **Chapter 1** (`lecture_1_intro.tex`): framing and roadmap; the “Perspective” box (“ideas that survived multiple paradigm shifts”) lives in the preface (`preface.tex`) right before “How to use this book”.
  2. **Chapters 2–4** (`lecture_2_part_i.tex`, `lecture_supervised.tex`, `lecture_2_part_ii.tex`): problem-solving strategies, supervised learning foundations, and logistic regression as a bridge into neural network training.
  3. **Part I: Foundations and the ERM toolbox (Ch 1–4)**: how to read the book, then the two “evergreen” toolkits (safe vs. heuristic reasoning; ERM/MLE/MAP + diagnostics) that later chapters reuse.
  4. **Part II: Neural networks, sequence modeling, and NLP (Ch 5–14)**: perceptrons/MLPs/backprop and training hygiene, then architectural inductive biases (RBF/CNN/RNN), then applied NLP and attention-based sequence modeling.
  5. **Part III: Soft computing and fuzzy reasoning (Ch 15–18)**: fuzzy sets/relations/inference and hybrid reasoning patterns, grounded in worked control-style examples.
  6. **Part IV: Evolutionary optimization (Ch 19)**: population-based search when gradients are unavailable/unreliable, with reproducibility and budget-aware reporting as first-class concerns.
- Print output is `ece657_notes.pdf`; reflowable ebook output is an EPUB built from `ece657_ebook.tex` (see “Reflowable ebook (Kindle/Apple)” below). For publishing checks, use the generated regression bundle under `notes_output/artifacts/release_checks/` (built by `bash notes_output/scripts/run_release_checks.sh`).
- Production-quality plan (what to do next, in priority order): `notes_output/PRODUCTION_ROADMAP.md`.
- Setup + release operator docs:
  - `notes_output/SETUP_CHECKLIST.md`
  - `notes_output/RELEASE_PLAYBOOK.md`
  - `notes_output/TEST_MATRIX.md`
- Internal workflow artifacts/checklists (not part of the published book): `notes_output/_archive/internal_workflow/`
- Chapter house template (required structure for every chapter): `notes_output/CHAPTER_TEMPLATE.md`.
- Citation policy + bib hygiene:
  - `notes_output/CITATION_POLICY.md`
- Cross-reference policy + label hygiene:
  - Enforced by `notes_output/scripts/check_crossrefs.py` (run via `notes_output/scripts/run_editorial_qc.sh`).
- Equation policy + numbering hygiene (EPUB):
  - Enforced by `notes_output/scripts/check_equations.py` (run via `notes_output/scripts/run_editorial_qc.sh`).
- Table policy + latest table audit:
  - `notes_output/EPUB_TABLES.md`
  - `notes_output/EPUB_TABLES_AUDIT.md`
- Terminology concordance (book voice + consistency):
  - `notes_output/TERMINOLOGY.md`
- Terminology (publishing consistency): prefer “book” in prose (avoid “these notes” / “opening material” phrasing inside numbered chapters). Assume **no companion resources** exist; do not promise slides/bundles/code/solutions, and avoid phrasing like “provided with your copy”.

Original lecture transcript reference
------------------------------------
This project has a “ground truth voice” source: the original lecture transcripts that the book was derived from.

- Canonical source file (original transcript bundle): `merged_lectures_fixed.docx`
- Searchable reference (generated, do not hand-edit): `notes_output/artifacts/lecture_source/merged_lectures_fixed.md`
- Regenerate the markdown reference (safe, offline):
  - From repo root: `pandoc -t gfm -o notes_output/artifacts/lecture_source/merged_lectures_fixed.md merged_lectures_fixed.docx`

Use this reference when:
- Checking whether a chapter’s tone still sounds like the original lectures.
- Recovering missing “teaching intuition” that was present in the spoken version.
- Resolving “did I actually say/claim this?” questions (avoid overconfident claims that aren’t supported).

Editorial guardrails (hard constraints)
---------------------------------------
- **American English** in prose (do not change spellings inside bibliographic titles): e.g., `summarize`, `visualize`, `normalize`, `optimize`, `behavior`, `artifacts`.
- **ASCII-only `.tex` sources** (robust compilation): do not introduce Unicode punctuation or non-ASCII diacritics. Use LaTeX-safe equivalents:
  - Quotes: ``like this'' (not curly quotes)
  - Ranges/dashes: `--` for ranges, `---` for em dashes (or rewrite into two sentences)
  - Diacritics: `G\"odel`, `Karafi\'{a}t`, `\L{}ukasiewicz`, etc.
- **Important nuance:** PDF *text extraction* can show Unicode glyphs even when the `.tex` source is clean ASCII; treat source scans (not `pdftotext` output) as the ground truth for “Unicode hygiene”.
- **Book voice**: avoid “today/last time/throughout the course/these notes/next chapter” in chapter bodies. Course provenance/logistics belong only in the preface and Appendix C.
- **Notation consistency** (especially where “Notation note” boxes appear):
  - Layer indices: prefer `A^{(l)}`, `Z^{(l)}`, `W^{(l)}`, `b^{(l)}`, `\delta^{(l)}` (do not drift to `A(l)`/`A^l` in prose/ledgers).
  - Expectation: `\mathbb{E}[\cdot]` always.
  - Avoid symbol collisions (`\phi/\varphi`, `\sigma(\cdot)`): local “Notation note” boxes must agree with `notation.tex`.
- **Citations and bibliography (publisher-grade)**:
  - Use `\citet{...}` / `\citep{...}` consistently; do not leave informal inline citations like `(Author, 1989)` in prose.
  - The book prints a **single unified bibliography** via `notes_output/book_bibliography.tex` and `notes_output/refs.bib` (BibTeX + `plainnat-ece657.bst`).
  - Chapters may use `\nocite{...}` to force key works into the unified bibliography; avoid per-chapter reference lists.
  - Fix applied: converted remaining parenthetical citations to `\citep{...}` where keys exist (e.g., `Micchelli1986`, `ParkSandberg1991`, `Cybenko1989`).

Recent major content changes (what moved where)
----------------------------------------------
- **Chapter 3 (`lecture_supervised.tex`)** is the canonical “supervised learning toolkit” chapter. It now teaches the workflow first (splits → objectives → regularization → diagnostics), then ends with linear regression as the first full case study (`\label{sec:linear_regression_closed}`).
- **Regularization is now a full narrative section** in Chapter 3 (not just a box), including schematic figures for fit regimes and L1/L2 geometry.
- **Chapter 4 (`lecture_2_part_ii.tex`)** keeps the probabilistic Bayes/MLE/MAP framing, but it does not claim that Chapter 3 derives MLE/MAP for linear regression. It also includes a compact “likelihood → loss → gradient” section (`\label{sec:lec2_logistic_likelihood}`) plus a schematic figure (`\label{fig:lec2_sigmoid_bce}`).
- **References cleanup:** removed per-chapter manual `\subsection*{References}` lists and standardized on the unified bibliography from `notes_output/refs.bib` (chapters may keep `\nocite{...}` and short “Suggested reading” sentences).
- **Chapter 3 layout polish**: “Model Selection, Splits, and Learning Curves” is forced to start on a clean page (prevents box/float collisions), the “Proper scoring rules and calibration” box is contiguous, the ERM pipeline figure makes “best model only” explicit inside the final block, and “Scaling laws and double descent” is presented as an explicit aside to preserve the linear learning progression.
- **EPUB-specific robustness**: a small number of external `\includegraphics` calls are guarded with `\ifdefined\HCode ... \else ... \fi` to pick PNG for EPUB and PDF for print, when needed for reliability.

Chapter-to-file mapping
-----------------------
- Main (print/PDF) entrypoint: `ece657_notes.tex`
- Reflowable ebook (EPUB) entrypoint: `ece657_ebook.tex`
- Bibliography source: `refs.bib` (compiled outputs: `ece657_notes.bbl`, `ece657_notes.blg`, etc.)
- Shared include lists (avoid duplicated chapter lists across entrypoints):
  - Chapters: `book_chapters.tex`
  - Appendices: `book_appendices.tex`
  - Bibliography: `book_bibliography.tex`
- Unnumbered front matter:
  - Preface: `preface.tex` (`\section*{...}`)
  - Copyright / imprint: `copyright.tex` (no TOC entry)
  - Acknowledgments: `acknowledgments.tex` (`\section*{...}`)
  - Notation / Glossary: `notation.tex` (`\section*{...}`)
- Chapters 1–19 (published order; assembled by `book_chapters.tex`):

| Chapter | Title | Source file |
|---:|---|---|
| 1 | About This Book | `lecture_1_intro.tex` |
| 2 | Symbolic Integration and Problem-Solving Strategies | `lecture_2_part_i.tex` |
| 3 | Supervised Learning Foundations | `lecture_supervised.tex` |
| 4 | Classification and Logistic Regression | `lecture_2_part_ii.tex` |
| 5 | Introduction to Neural Networks | `lecture_3_part_i.tex` |
| 6 | Multi-Layer Perceptrons: Challenges and Foundations | `lecture_3_part_ii.tex` |
| 7 | Backpropagation Learning in Multi-Layer Perceptrons | `lecture_4_part_i.tex` |
| 8 | Radial Basis Function Networks (RBFNs) | `lecture_4_part_ii.tex` |
| 9 | Introduction to Self-Organizing Networks and Unsupervised Learning | `lecture_5_part_i.tex` |
| 10 | Hopfield Networks: Introduction and Context | `lecture_5_part_ii.tex` |
| 11 | Convolutional Neural Networks and Deep Training Tools | `lecture_6.tex` |
| 12 | Introduction to Recurrent Neural Networks | `lecture_7.tex` |
| 13 | Neural Network Applications in Natural Language Processing | `lecture_8_part_i.tex` |
| 14 | Transformers: Attention-Based Sequence Modeling | `lecture_transformers.tex` |
| 15 | Introduction to Soft Computing | `lecture_8_part_ii.tex` |
| 16 | Fuzzy Sets and Membership Functions: Foundations and Representations | `lecture_9.tex` |
| 17 | Fuzzy Set Transformations Between Related Universes | `lecture_10_part_i.tex` |
| 18 | Fuzzy Inference Systems: Rule Composition and Output Calculation | `lecture_10_part_ii.tex` |
| 19 | Introduction to Evolutionary Computing | `lecture_11.tex` |
- Unnumbered end matter:
  - Key Takeaways: `key_takeaways.tex` (`\section*{...}`)
- Appendices (assembled by `book_appendices.tex`):

| Appendix | Title | Source file |
|---:|---|---|
| A | Linear Systems Primer | `appendix_linear_systems.tex` |
| B | Kernel Methods and Support Vector Machines | `appendix_kernel_methods.tex` |
| C | Course Logistics | `appendix_logistics.tex` |
- Note: an older alternate Chapter 1 draft is archived at `archive/lecture_1.tex` and guarded with `\endinput`; it is **not** part of the main build.

Recent flow/layout work (2026-01-04)
-----------------------------------
- Chapter 3 (`lecture_supervised.tex`): smoothed the in-flow “short notation reminder”; tightened the underfit/overfit figure so labels stay inside the axis bounding box (EPUB robustness); made the ERM pipeline “best model only” callout easier to read; forced the “Proper scoring rules and calibration” box to stay unbroken across pages.
- Chapter 4 (`lecture_2_part_ii.tex`): removed the standalone “Synthetic Data and Optimization Geometry” subsection (flow breaker) and replaced it with an in-flow running-example paragraph; moved the convex quadratic GD toy to the logistic/optimization discussion; clarified the binary-first setup before introducing multiclass notation.

Figures, diagrams, and color guidance
-------------------------------------
- Figures blend vector TikZ (LSTM/GRU/attention/fuzzy blocks) with Matplotlib exports for empirical plots. If you edit data-driven charts, keep sources (Python scripts) near `scripts/` or inside the chapter.
- Figure house style + generation rules (Matplotlib/TikZ): `notes_output/FIGURE_STYLE_GUIDE.md`.
- Ebook-friendly color palettes appear in Figures 16, 28, 38, 48–53, 57, 61, etc.; captions still note whether a plot is schematic or empirical and mention reproducibility details (datasets, seeds, parameters).
- Figure/table numbers are global and can shift as floats are added/removed; prefer tracking by `\label{...}`.
- Figure refreshers (recent): Figure 2 is the transformation-tree TikZ in `notes_output/lecture_2_part_i.tex`; Figures 5 and 13 are the split-bar and dataset TikZ in `notes_output/lecture_supervised.tex`; Figures 54 and 58 are generated by `scripts/gen_fig64_embeddings.py` and `scripts/gen_fig68_analogy.py`, which write updated PDF/PNG assets to `assets/lec14/`.
- Current placement reference (from `ece657_notes.aux`): Figure 52 is `\label{fig:lec7-gru}` (GRU cell schematic) in `lecture_7.tex` (Chapter 12). Closely related: Figure 51 is `fig:lec7-lstm`.
- Historic `review/*.md` notes may refer to older figure numbers; treat them as context, but verify against the current build artifacts (`ece657_notes.aux`, `ece657_notes.lof`, `ece657_notes.lot`).
- Always produce a grayscale proof when a figure relies on color gradients, then store updated previews back in `notes_output/artifacts/previews/`.
- Caption style: avoid `Schematic:` by default; it often reads like placeholder text. Use `Schematic:` only when a reader could reasonably mistake the visual for an empirical result or a to-scale diagram. Use `Empirical:` when the figure is actually data/experiment-driven.

Recent figure work (2025-12-27)
-------------------------------
- Repo note: this git repo currently has no commits yet (`git log` fails). For safe iterative edits, make manual backups under `notes_output/artifacts/previews/candidate_figures/iter_backups/` before each change.
- Build command used for fast iteration: run `tectonic --reruns 0 ece657_notes.tex` from `notes_output/`.
- Page snapshot workflow (for side-by-side figure decisions):
  - Render a page to PNG: `pdftoppm -png -f <page> -l <page> -singlefile ece657_notes.pdf artifacts/previews/candidate_figures/<name>`
  - Store “before/after” comparisons in `notes_output/artifacts/previews/candidate_figures/`.
- Updated/iterated figures (with primary files/labels):
  - Figure 2 (transformation tree): `notes_output/lecture_2_part_i.tex` (TikZ rewrite for layout/overlap).
  - Figures 5 and 13 (supervised chapter): `notes_output/lecture_supervised.tex` (styling + fixed node linebreak/`align=center` issue).
  - Figure 19 (perceptron geometry plot): `notes_output/lecture_3_part_i.tex` (improved palette/grid/legend readability).
  - Figure 21 (backprop computational graph): `notes_output/lecture_4_part_i.tex`, `\label{fig:backprop-computational-graph}` (adopted the “cache box + legend + raised parameter nodes + curved grad taps” variant; latest page snapshot: `notes_output/artifacts/previews/candidate_figures/p131_fig21_latest.png`).
  - Figure 22 (two-layer MLP forward/backward flows): `notes_output/lecture_4_part_i.tex`, `\label{fig:lec4_backprop_flow}` (styling consistency pass; see `notes_output/artifacts/previews/candidate_figures/fig22_before.png` vs `notes_output/artifacts/previews/candidate_figures/fig22_after.png`).
  - Figure 26 (RBF center placement/overlap): `notes_output/lecture_4_part_ii.tex`, `\label{fig:rbf_centres}` (panelized redesign; see `notes_output/artifacts/previews/candidate_figures/fig26_before.png` vs `notes_output/artifacts/previews/candidate_figures/fig26_after.png`).
  - Figure 55 (Transformer reference schematic): `notes_output/lecture_transformers.tex`, `\label{fig:lec13_transformer_block}` (replaced the sprawling layout with 3 compact panels; improved the \(\mathbf{V}\rightarrow\)MatMul routing; latest page snapshot: `notes_output/artifacts/previews/candidate_figures/p262_fig55.png`).
  - Figure 56 (Transformer micro-views): `notes_output/lecture_transformers.tex`, `\label{fig:lec13_micro_figures}` (panel consistency + size; see `notes_output/artifacts/previews/candidate_figures/fig56_before.png` vs `notes_output/artifacts/previews/candidate_figures/fig56_after2.png`).
- Matplotlib-regenerated assets (lecture 14):
  - `scripts/gen_fig64_embeddings.py` writes `assets/lec14/lec14_embeddings_clusters.(pdf|png)` (Figure 54).
  - `scripts/gen_fig68_analogy.py` writes `assets/lec14/lec14_analogy_geometry.(pdf|png)` (Figure 58).
- Quick page anchors used during review (may shift with edits; use `pdftotext` to locate “Figure N:” first):
  - Fig 21 p131 (`notes_output/artifacts/previews/candidate_figures/p131_fig21_latest.png`)
  - Fig 55 p262 (`notes_output/artifacts/previews/candidate_figures/p262_fig55.png`)
  - Preface “Perspective” box (before “How to use this book”) p4 (`notes_output/artifacts/previews/candidate_figures/preface_p-004.png`)
  - Older anchors may be stale: `notes_output/artifacts/previews/candidate_figures/p130.png`, `notes_output/artifacts/previews/candidate_figures/p261.png`, etc.

Supporting scripts & bibliography
----------------------------------
- `scripts/generate_cover.py` crafts cover art and color palettes. Add future scripts to this directory and document how figures rely on them.
- `notes_output/refs.bib` holds bibliography entries. Keep it aligned with the `\cite` keys in the chapters; watch for duplicates (e.g., the two ViT entries). Maintain the same `.bib` file to avoid compile errors during Tectonic builds.
- **Citation policy (publishable standard):** use a single, consistent author-date citation system throughout (`\citet{...}`, `\citep{...}`) and a single, unified bibliography (from `notes_output/refs.bib`) at the end of the book.
  - Do not maintain per-chapter reference lists as manual `itemize` blocks; they drift and are not a professional publishing pattern.
  - If a chapter has a small set of core sources you want guaranteed in the unified bibliography, list them with `\nocite{...}` near the end of the chapter and optionally add a short “Suggested reading” sentence using `\citet{...}`.
  - Bibliography hard-pass policy is now: **DOI-first**, else **arXiv** (`eprint` + `archivePrefix=arXiv`), else canonical **URL fallback** for legacy/non-DOI sources.
  - Validate with:
    - `python3 notes_output/scripts/check_bib_style.py --bib notes_output/refs.bib --out notes_output/artifacts/qc/bib_style_report_hardpass_after.md`
    - `python3 notes_output/scripts/enrich_bib_metadata.py --bib notes_output/refs.bib --audit-doi --report notes_output/artifacts/qc/bib_doi_audit_report.md`

Build & publishing workflow
---------------------------
- Work inside `notes_output/`. For a clean, BibTeX-inclusive PDF build, run `tectonic -X compile --pass default --reruns 2 --keep-logs ece657_notes.tex` to regenerate `ece657_notes.pdf` (print/PDF output) along with auxiliary files (`ece657_notes.log`, `ece657_notes.aux`, etc.).
- For ebook distribution (Amazon KDP / Apple Books), build the reflowable EPUB using the isolated builder in `epub_builder/` and use the files under `epub_builder/dist/`.
- Key generated outputs (do not hand-edit; safe to delete/rebuild):
  - Print/PDF deliverable: `notes_output/ece657_notes.pdf`
  - PDF build logs + indices: `notes_output/ece657_notes.log`, `notes_output/ece657_notes.aux`, `notes_output/ece657_notes.toc`, `notes_output/ece657_notes.lof`, `notes_output/ece657_notes.lot`
  - EPUB deliverables (preferred): `epub_builder/dist/ece657_ebook_apple.epub` (Apple Books) and `epub_builder/dist/ece657_ebook_kindle.epub` (Kindle)
  - EPUB build artifacts (preferred): `epub_builder/artifacts/` (TikZ renders, logs, epubcheck output)
  - EPUB deliverables (legacy TeX4ht): `notes_output/artifacts/ebook/ece657_ebook_apple.epub`, `notes_output/artifacts/ebook/ece657_ebook_kindle.epub`
  - Release-check bundle (PDF+EPUB regression snapshots): `notes_output/artifacts/release_checks/manifest.json`, `notes_output/artifacts/release_checks/report.txt`, `notes_output/artifacts/release_checks/pdf/`, `notes_output/artifacts/release_checks/epub/`
  - Editorial QC report: `notes_output/artifacts/qc/publish_qc_report.md`
- Verify citations, the GRU figure, and the new preface text after each build; check the log for warnings about missing references or TikZ issues.
- Before a publish-ready export, run the editorial QC pipeline: `notes_output/scripts/run_editorial_qc.sh`. It rebuilds the PDF and writes an automated report to `notes_output/artifacts/qc/publish_qc_report.md` (TOC/LOF/LOT anomalies, overfull boxes, whitespace/style flags).
- For “don’t make me keep re-testing” publishing checks, run `bash notes_output/scripts/run_release_checks.sh`. It rebuilds PDF+EPUB, then extracts “critical pages” (PDF) and “critical sections” (EPUB: figures + pseudocode) into `notes_output/artifacts/release_checks/` and writes a manifest for quick regression checking.
- For **EPUB vs PDF visual regression**, use the builder QC script:
  - Run (Apple EPUB): `epub_builder/.venv/bin/python epub_builder/scripts/qc_epub_vs_pdf.py --epub epub_builder/dist/ece657_ebook_apple.epub --pdf notes_output/ece657_notes.pdf --aux notes_output/ece657_notes.aux --out epub_builder/artifacts/qc/pdf_vs_epub_$(date +%Y%m%d_%H%M%S) --max-eq 0`
  - Output: a manifest plus side-by-side crops under `epub_builder/artifacts/qc/.../compare/{fig,tab,eq}/`
  - Use this when fixing EPUB styling/structure so improvements are global and regressions are caught early.
- Editorial style decisions (dialect, dash style, spelling preferences) live in `notes_output/editorial_style.toml`; update this file first when changing house style so a new LLM can onboard quickly and apply consistent edits.
- The full workflow + checklist is documented in `notes_output/EDITORIAL_QC.md`.
- Mechanical helpers: `notes_output/scripts/fix_whitespace.py` (tabs/trailing whitespace) and `notes_output/scripts/apply_house_style.py` (house spelling normalization; run as `/usr/bin/python3 notes_output/scripts/apply_house_style.py --root notes_output`).
- Ebook metadata (title/author/language/identifier) is centralized in `notes_output/book_metadata.json` and applied during EPUB postprocessing. Set this to a real production identifier (ISBN/UUID/URL) before publishing.
- Sanity-check commands used during editorial passes:
  - ASCII-only check: `/usr/bin/python3 - <<'PY'\nimport pathlib, sys\nroot = pathlib.Path('notes_output')\nfor p in root.rglob('*.tex'):\n    data = p.read_bytes()\n    if any(b >= 128 for b in data):\n        print('Non-ASCII bytes found in', p)\n        sys.exit(1)\nprint('OK: notes_output/*.tex is ASCII-only')\nPY`
  - UK spelling sweep (should be empty under American style): `rg -n \"\\bvisualise\\w*\\b|\\bsummarise\\w*\\b|\\bnormalise\\w*\\b|\\boptimise\\w*\\b|\\bartefact\\w*\\b|\\bbehaviour\\w*\\b\" notes_output --glob '*.tex'`

Reflowable ebook (Kindle/Apple)
-------------------------------
- Goal: a **reflowable EPUB** suitable for Amazon KDP (Kindle) and Apple Books, without maintaining a second copy of the manuscript.
- Preferred build system: the standalone Pandoc builder project in `epub_builder/` (isolated build sandbox; no intermediates under `notes_output/`).
- Build commands (from repo root):
  - Apple: `python3 epub_builder/build.py --variant apple`
  - Kindle: `python3 epub_builder/build.py --variant kindle`
  - Both: `python3 epub_builder/build.py --variant both`
  - Higher-quality TikZ (bigger EPUBs): `python3 epub_builder/build.py --variant both --tikz-dpi 350`
  - Faster iteration (keep transient build outputs): `python3 epub_builder/build.py --variant both --no-clean`
- Outputs:
  - `epub_builder/dist/ece657_ebook_apple.epub`
  - `epub_builder/dist/ece657_ebook_kindle.epub`
- Notes:
  - Source-of-truth content remains the chapter files (`notes_output/lecture_*.tex`, appendices) shared with print/PDF.
- If you change figures, run the Apple build first; Kindle is slower because it rasterizes math for broad device compatibility.
  - Cross-references (important):
    - Chapters/figures/tables: the builder ensures visible text includes `Chapter`/`Figure`/`Table` (Pandoc otherwise tends to emit bare numbers).
    - Equations: the builder injects explicit anchors for `eq:*` labels and rewrites `\eqref{...}`/`\Cref{eq:*}` into links with the correct equation number.
    - Equation numbers are read from a LaTeX `.aux` file that the builder generates at build time (under `epub_builder/artifacts/tmp/aux/`). This avoids relying on an already-built PDF, and keeps EPUB numbering in sync with the current sources.
  - Visible numbering (EPUB polish):
    - Chapter headings are rewritten to include `Chapter N:` (and appendices as `Appendix A:`) when the corresponding `\label{chap:...}` / `\label{app:...}` is present.
    - Subsection/subsubsection headings are prefixed with their `.aux` number (e.g., `1.3 ...`) so EPUB readers show section numbers.
      - This requires headings to have explicit `\label{sec:...}` anchors in the LaTeX sources; the repo includes an idempotent label injector: `python3 epub_builder/scripts/add_missing_heading_labels.py`.
      - Headings that contain nested braces (e.g. `\texorpdfstring{...}{...}`) are handled by the builder’s brace-aware prefixing logic.
    - Figure/Table captions are prefixed with `Figure N.` / `Table N.` (from `.aux`) so readers show numbering.
    - Display equations do not have native MathML numbering; the builder adds a small right-aligned visible number line `(N)` after labeled display equations.
      - For consistency, `equation` environments should have a `\label{eq:...}`. The repo includes an idempotent label injector for unlabeled `equation` blocks: `python3 epub_builder/scripts/add_missing_equation_labels.py`.
  - Figure guarantee:
    - The builder runs in **strict figure mode** by default and will fail the build if any figure would be missing:
      - TikZ compilation failures abort the build.
      - Missing `\includegraphics{...}` assets abort the build.
      - The produced EPUB is inspected to ensure `<img>` references exist in the zip (prevents caption-only figures).

Legacy EPUB builder (TeX4ht/tex4ebook)
-------------------------------------
- The TeX4ht pipeline (`notes_output/scripts/build_ebook.sh`, based on `tex4ebook`) is retained for reference, but is not the preferred path.
- If you use it anyway, outputs go under `notes_output/artifacts/ebook/`.

What to do next (after large editorial changes)
----------------------------------------------
Goal: stabilize the manuscript (PDF + EPUB) and converge to “publishable” by tightening content drift and closing the remaining EPUB-specific blockers.

1) **Freeze structure, then iterate in small batches**
   - Avoid moving sections across chapters unless strictly necessary; prefer tightening and local rewrites.
   - After each batch, run `bash notes_output/scripts/run_release_checks.sh` and compare `notes_output/artifacts/release_checks/manifest.json`.
   - To add a PDF regression page for a specific figure/table, look up its page in `notes_output/ece657_notes.aux` (search for `\\newlabel{fig:...}` / `\\newlabel{tab:...}`); the second number is the PDF page.

2) **EPUB “blocker” triage (highest impact first)**
   - Verify that external images (from `notes_output/assets`) render in the Kindle EPUB and are not replaced by black rectangles.
   - Verify that pseudocode/code blocks remain readable and wrap correctly on narrow screens.
   - For any figure that still renders poorly in EPUB but is fine in PDF, prefer fixing the figure source (TikZ/pgfplots settings) over ebook-only hacks; use `\\ifdefined\\HCode` only as a last resort.

3) **Consistency sweeps**
   - Run a UK spelling sweep (should be empty under American style).
   - Run an ASCII/Unicode sweep on `.tex` sources (PDF text extraction is not the source of truth).
   - Audit repeated “Notation note” / operator-default boxes to ensure they agree and don’t contradict `notation.tex`.

4) **Narrative continuity check**
   - Confirm the four-strand ordering is respected when chapters recap: statistical/data-driven → biological/neural → behavioral/fuzzy → evolutionary.
   - Confirm each chapter opens with (i) a 1–2 sentence bridge, and (ii) a “Design motif” hook, without brittle “next chapter” wording (use `\\Cref{...}`).
5) **Chapter kit uniformity (end-of-chapter blocks)**
   - Default end-of-chapter kit (keep the titles exactly):
     - `Key takeaways` (tcolorbox)
     - `Exercises and lab ideas` (tcolorbox)
     - `Where we head next.` (paragraph)
   - Keep the bibliography centralized (book-wide references section); do not append per-chapter references paragraphs.
   - Do not reintroduce `\subsection*{Summary}` or per-chapter “Further Reading/References” lists. If a chapter genuinely needs an exception, document why.

Quick start (for the next editor/LLM)
------------------------------------
This repo produces two deliverables from the same `.tex` sources:
1) A print-quality PDF (`ece657_notes.pdf`).
2) A reflowable EPUB (`ece657_ebook*.epub`) for Apple Books / Kindle.

Tooling prerequisites (macOS notes)
----------------------------------
- PDF build:
  - `tectonic` (use `-X compile --pass default` for a clean BibTeX-inclusive build).
- EPUB build:
  - Preferred (`epub_builder/`): `pandoc`, `pdflatex`, `pdftoppm` (plus optional `epubcheck` for validation).
  - Legacy (`notes_output/scripts/build_ebook.sh`): `tex4ebook` (TeX4ht; typically comes with a full TeX Live / MacTeX install).
- EPUB validation:
  - `epubcheck` (recommended before publishing; install on macOS via `brew install epubcheck openjdk`).
- Optional visual QA (headless screenshots):
  - Playwright (offline rendering): `python3 -m venv notes_output/.venv_render && notes_output/.venv_render/bin/pip install playwright && notes_output/.venv_render/bin/python -m playwright install chromium webkit`

Start here (fast, reliable)
---------------------------
1) Build the PDF (clean, BibTeX-inclusive): from `notes_output/`, run `tectonic -X compile --pass default --reruns 2 --keep-logs ece657_notes.tex` and inspect `notes_output/ece657_notes.pdf`.
2) Build the EPUBs (preferred): from repo root, run `python3 epub_builder/build.py --variant both --clean` (use `--tikz-dpi 350` if TikZ figures look blurry on retina screens).
3) Run EPUBCheck (recommended before publishing): `epubcheck epub_builder/dist/ece657_ebook_apple.epub` and `epubcheck epub_builder/dist/ece657_ebook_kindle.epub`.
4) (Legacy) Run regression checks: `bash notes_output/scripts/run_release_checks.sh` (this uses the legacy TeX4ht EPUB pipeline).

EPUB variants (which file to open)
----------------------------------
- Preferred (Pandoc-based builder):
  - Apple Books: `epub_builder/dist/ece657_ebook_apple.epub`
  - Kindle: `epub_builder/dist/ece657_ebook_kindle.epub`
- Legacy (TeX4ht):
  - Apple Books: `notes_output/artifacts/ebook/ece657_ebook_apple.epub`
  - Kindle: `notes_output/artifacts/ebook/ece657_ebook_kindle.epub`
  - Raw TeX4ht output (debugging only): `notes_output/artifacts/ebook/ece657_ebook_raw.epub`

Important output artifacts (what to share / archive)
----------------------------------------------------
- Print/PDF:
  - Main PDF: `notes_output/ece657_notes.pdf`
  - Main PDF build log: `notes_output/ece657_notes.log`
  - Optional “with cover” preview (not for KDP print interior): `notes_output/artifacts/preview/ece657_notes_with_cover.pdf` (built by `bash notes_output/scripts/build_pdf_with_cover.sh`)
- Ebook/EPUB:
  - Preferred outputs: `epub_builder/dist/` (see “EPUB variants” above)
  - Preferred build artifacts: `epub_builder/artifacts/`
  - Legacy outputs: `notes_output/artifacts/ebook/`
  - Legacy cover input: `notes_output/BookCover.png` (used by the legacy TeX4ht ebook build script when present)
- Release/regression bundle:
  - Summary: `notes_output/artifacts/release_checks/report.txt`
  - Machine-readable manifest: `notes_output/artifacts/release_checks/manifest.json`
  - Snapshots: `notes_output/artifacts/release_checks/pdf/` and `notes_output/artifacts/release_checks/epub/`
- Validation:
  - Preferred: `epub_builder/artifacts/epubcheck/` (generated by `python3 epub_builder/build.py ...` when not using `--skip-validate`)
  - Legacy: `notes_output/artifacts/epubcheck/` (generated by `bash notes_output/scripts/run_epubcheck.sh`)

Production checklist (before upload)
-----------------------------------
1) Confirm publishing metadata in `notes_output/book_metadata.json` (title/author/publisher/rights/identifier).
2) (Legacy) Run the production gate: `bash notes_output/scripts/run_production_checks.sh` (this currently assumes the legacy TeX4ht EPUB build and `notes_output/BookCover.png`).
3) (Preferred builder) Run `epubcheck` on `epub_builder/dist/ece657_ebook_apple.epub` and `epub_builder/dist/ece657_ebook_kindle.epub`, then do manual reader QA.
4) Do visual QA in real readers:
   - Kindle Previewer (reflow, TOC navigation, math legibility, dark-mode figure backgrounds).
   - Apple Books app (inline math, display math, figure scaling, cover).
5) Check practical platform constraints:
   - Kindle file size: the Kindle EPUB rasterizes all math to PNG for reliability; verify the final `.epub` size is acceptable for KDP delivery and download UX.
   - Cover: ensure `notes_output/BookCover.png` meets KDP/Apple cover specs (resolution, aspect ratio, RGB). The production gate expects at least ~1600×2560px (override with `ALLOW_LOWRES_COVER=1` for drafts).

Ebook-specific guardrails (what tends to break)
-----------------------------------------------
- **Math rendering:** Apple Books can clip/scale display equations poorly. The Apple EPUB build keeps inline MathML but renders display math as SVG images for reliability.
- **Figures:** TeX4ht can generate images with transparent backgrounds; dark-mode readers may show large black blocks. Prefer opaque white backgrounds for pgfplots/TikZ figures intended as standalone images.
- **External image formats:** EPUB toolchains are inconsistent with PDF/SVG; prefer PNG for the ebook when needed (guarded via `\\ifdefined\\HCode ... \\else ... \\fi`).
- **Code/pseudocode:** long `verbatim`/`lstlisting`-style blocks can overflow on narrow screens; prefer wrapping-friendly styles and keep lines short where possible.
- **Visual QA:** the repo includes a headless screenshot step for quick regressions, but you still must validate the final EPUBs in Kindle Previewer and Apple Books before publishing.

Key narrative/style decisions (do not regress)
----------------------------------------------
- No companion resources exist; do not promise slides/bundles/code/solutions.
- American English in prose; ASCII-only `.tex` sources (no Unicode punctuation/diacritics in source).
- Chapter continuity uses explicit cross-references (`\\Cref{...}`), not “next chapter” sequencing language.
- “Design motif” hooks and short bridges at chapter openings are intentional; keep voice consistent and personal (lecture-derived), but avoid syllabus-style logistics in chapter bodies.
