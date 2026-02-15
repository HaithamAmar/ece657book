# LLM Commentary Questions (Build + Editorial Continuity)

Purpose: this file is a handoff scaffold for a second LLM to act as a **commentator/editor**.
They should answer questions inline (under each question) with concrete recommendations, risks, and proposed experiments.

Scope: everything is relative to the repo root `ece657Book/`.

## Start here (the 5 files that matter most)

Read these first, in this order:
1. `notes_output/EPUB_PUBLISHING_QC.md` — current EPUB pipeline invariants + release checks.
2. `notes_output/PRODUCTION_ROADMAP.md` — editorial + production backlog and quality bar.
3. `notes_output/ONBOARDING.md` — project structure, guardrails, and where source truth lives.
4. `epub_builder/build.py` — the build entrypoint (aux generation, crossref rewrite, figure verification).
5. `epub_builder/lib/latex.py` — the LaTeX→EPUB transforms (crossrefs, headings, equation handling, math promotion).

If you only have time to inspect one output artifact:
- `epub_builder/dist/ece657_ebook_apple.epub` (Apple is the most predictable EPUB renderer).

---

## A) Build reliability and reproducibility

### Q1. What are the top 5 failure modes that could still cause "missing figures" in the EPUB, even if `epub_builder/build.py` passes?
- Context: We have a figure verification step, and TikZ pre-rendering, but the requirement is "guarantee all figures show".
- Ask: enumerate residual risks (Pandoc conversions, CSS hiding, broken links, reader quirks, SVG/PNG issues, etc.) and how to detect each.
- Output: a prioritized list + a specific test for each.

**Answer:**

1. **Diagnosis:** The build's `_verify_epub_figures` checks `<figure>` blocks for `<img>` tags and verifies that `src` targets exist in the zip. However, several failure modes live *outside* that check's scope.

2. **Recommendation — the 5 residual failure modes, prioritized:**

   **FM1. Pandoc silently drops `\includegraphics` inside unrecognized wrappers.**
   The `unwrap_graphics_wrappers` function handles `\resizebox` and `\scalebox`, but any *new* wrapper macro (e.g., `\adjustbox`, `\fbox`, custom macros) will cause Pandoc to emit an empty `<figure>` with only a `<figcaption>`. The current regex check catches `<figure>` missing `<img>`, but only if Pandoc still emits a `<figure>` — if Pandoc drops the entire float, there is no `<figure>` to flag.
   - **Test:** After the build, parse every `\label{fig:...}` from the `.aux` and verify each has a corresponding `<img>` element in the EPUB XHTML. Any fig label present in aux but absent from the EPUB is a dropped figure.

   **FM2. CSS or reader-level hiding (zero-dimension images, `display:none`, dark-mode inversion).**
   An image file can exist in the zip and be referenced by `<img>`, but render as invisible due to: (a) the image having essentially-zero content area (all-white PNG after trimming), (b) reader dark-mode inverting a white-on-transparent figure to invisible, or (c) a CSS rule inadvertently hiding it.
   - **Test:** Run the existing `audit_epub_images.py` with an additional check: for each PNG, verify pixel dimensions are > 50×50 and that the image is not > 95% single-color. For dark-mode, ensure all figure PNGs have an opaque white background (check alpha channel: `PIL.Image.open(f).mode` should not be `RGBA` with large transparent regions).

   **FM3. Pandoc version drift changing `<figure>` emission behavior.**
   Pandoc's LaTeX reader has changed figure handling between versions (e.g., 3.x vs 2.x). A newer Pandoc might wrap figures differently, nest them inside `<div>`, or change how `\caption` maps to `<figcaption>`. The `_verify_epub_figures` regex (`<figure\b.*?</figure>`) is DOTALL but assumes a specific nesting pattern.
   - **Test:** Pin the Pandoc version in the build checklist. Add a build-time assertion: `pandoc --version` output must match a known-good major.minor. Add a post-build count: the number of `<img>` tags in the EPUB should be >= the number of `fig:` labels in aux (allow >= because some images are unlabeled).

   **FM4. TikZ figures that compile to a valid but near-empty PNG.**
   `compile_tikz_block_to_png` (`lib/tikz.py`) returns `True` in two cases: (a) from a SHA-256 content cache hit (lines 107–114) without recompiling, or (b) after `pdflatex` exits 0 and `pdftoppm` produces a file. In case (b), the TikZ block can compile without error yet produce an essentially-blank page (e.g., a missing TikZ library causes silent fallback, or a `\pgfplotsset` call renders nothing). In case (a), a previously-cached blank PNG will persist indefinitely. The result is a valid PNG containing only whitespace.
   - **Test:** After TikZ compilation, check that each output PNG has meaningful content: at least N% non-white pixels (a simple histogram check with PIL). Threshold: > 0.5% non-white pixels. Flag as warnings, not hard failures, since some legitimate figures are sparse. Note: if a cache hit serves a blank PNG, you must also clear the `.sha256` sidecar file to force recompilation.

   **FM5. EPUB reader fails to render large PNGs (file-size or dimension limits).**
   At 1200–3000 DPI, some TikZ/asset PNGs can be 10+ MB or 6000+ pixels wide. Kindle's rendering engine may silently fail to display images above certain dimension thresholds (historically ~4096px on some Kindle hardware). Apple Books is more tolerant but still has practical limits.
   - **Test:** After the build, iterate over all PNGs in `EPUB/media/` and flag any with width or height > 4096px or file size > 5 MB. For Kindle, consider downscaling those specific images to 4096px max dimension as a post-processing step.

3. **Risk/Tradeoffs:** Adding these checks increases build time slightly (image analysis). The biggest risk is false positives from the "near-empty PNG" check on legitimately sparse diagrams. Keep it as a warning, not a hard gate.

4. **Experiment:** Run the "aux label vs EPUB img" cross-check on the current Apple EPUB. Count: (a) fig labels in aux, (b) `<img>` elements in EPUB. If (b) < (a), at least one figure is silently missing. Also: open the Kindle EPUB in Kindle Previewer and jump to the 5 largest-dimension PNGs — verify they render.

5. **Definition of done:** Every `\label{fig:...}` from the aux file has a corresponding visible `<img>` in the EPUB, all PNGs have non-trivial content, no image exceeds reader dimension limits, and the check runs as part of the standard build (not a separate manual step).

### Q2. What is the minimal "release checklist" that makes a build reproducible on a fresh machine?
- Context: scripts depend on `pandoc`, `pdflatex`, `pdftoppm`, plus optional QC deps (Playwright/Chromium, Pillow, NumPy, OpenCV).
- Ask: propose a minimal checklist (tools + versions + one-liner commands) to validate a fresh setup.
- Output: a short bullet list + suggested commands (no network assumptions unless necessary).

**Answer:**

1. **Diagnosis:** The current pipeline has no single "verify my environment" command. A fresh contributor must guess which tools are required and at which versions. The `_ensure_tools` function in `build.py` checks for `pandoc`, `pdflatex`, `pdftoppm` existence but not versions.

2. **Recommendation — minimal release checklist:**

   **Required tools (EPUB build):**
   - `pandoc` >= 3.1 (MathML output, EPUB3, LaTeX reader stability): `pandoc --version | head -1`
   - `pdflatex` (from TeX Live or MacTeX, full scheme for TikZ libraries): `pdflatex --version | head -1`
   - `pdftoppm` (from poppler-utils, for PDF→PNG rasterization): `pdftoppm -v 2>&1 | head -1`
   - `python3` >= 3.10 (f-strings, match statements in future code): `python3 --version`

   **Required tools (PDF build):**
   - `tectonic` >= 0.15 (BibTeX-inclusive compile): `tectonic --version`

   **Optional but recommended (QC + validation):**
   - `epubcheck` >= 5.0 (EPUB3 validation): `epubcheck --version 2>&1 | head -1`
   - Python venv with `playwright`, `pillow`, `numpy`, `opencv-python` (for visual QC scripts)

   **One-liner environment validation script** (propose as `epub_builder/scripts/check_env.sh`):
   ```bash
   #!/usr/bin/env bash
   set -e
   echo "=== EPUB Build Environment Check ==="
   for cmd in pandoc pdflatex pdftoppm python3; do
     command -v "$cmd" >/dev/null 2>&1 && echo "OK: $cmd ($($cmd --version 2>&1 | head -1))" || echo "MISSING: $cmd"
   done
   command -v tectonic >/dev/null 2>&1 && echo "OK: tectonic ($(tectonic --version 2>&1 | head -1))" || echo "OPTIONAL MISSING: tectonic (needed for PDF build)"
   command -v epubcheck >/dev/null 2>&1 && echo "OK: epubcheck" || echo "OPTIONAL MISSING: epubcheck"
   echo "=== Quick build smoke test ==="
   python3 epub_builder/build.py --variant apple --skip-validate --no-clean 2>&1 | tail -3
   echo "=== Done ==="
   ```

   **macOS-specific install commands (for reference, not baked into scripts):**
   ```bash
   brew install pandoc poppler epubcheck openjdk
   # TeX Live: brew install --cask mactex-no-gui  OR  use tectonic
   brew install tectonic
   ```

3. **Risk/Tradeoffs:** Pinning exact versions (e.g., `pandoc==3.1.12`) is more reproducible but harder to maintain. Recommend pinning major.minor and documenting known-good versions in a `VERSIONS.md` or in `ONBOARDING.md`. The main risk is Pandoc version drift — it has the most behavioral variation between releases.

4. **Experiment:** Clone the repo on a fresh macOS machine (or a clean Docker container with `texlive-full` + `poppler-utils` + `pandoc`). Run the check script. Then run `python3 epub_builder/build.py --variant apple --clean`. Verify the output EPUB opens in Apple Books.

5. **Definition of done:** A single command (`bash epub_builder/scripts/check_env.sh`) reports all required tools and their versions, flags any missing ones, and can optionally run a smoke build. The known-good tool versions are documented alongside the script.

### Q3. Are we overfitting the pipeline to the current book structure?
- Context: there are multiple entrypoints (`ece657_notes.tex`, `ece657_ebook.tex`, etc.), and the builder uses `.aux` as authoritative for numbering.
- Ask: identify assumptions that could break if the book grows (more appendices, changed heading hierarchy, new environments).
- Output: list assumptions + mitigation ideas.

**Answer:**

1. **Diagnosis:** The pipeline is tightly coupled to the current structure in several specific ways. This is pragmatic for shipping, but creates brittleness for growth.

2. **Recommendation — assumptions that would break, and mitigations:**

   | # | Assumption | What breaks | Mitigation |
   |---|-----------|-------------|------------|
   | 1 | **Label prefixes are `chap:`, `app:`, `sec:`, `fig:`, `tab:`, `eq:`** | A new prefix (e.g., `thm:`, `def:`, `algo:`, `lst:`) would fall through to bare `\ref{}` in `rewrite_crossrefs`, producing Pandoc-renumbered (wrong) output. | Add a registry of known prefixes in `latex.py` with a default handler. Log a warning for unrecognized prefixes so they are caught early. |
   | 2 | **Sections map to chapters** (`\section{...}\label{chap:...}`) | If the book adopts `\chapter{...}` (e.g., for a proper book class), `prefix_chapter_sections` would not fire because it matches `\section{`. | Make the heading-level detection configurable or pattern-match both `\chapter` and `\section` with `chap:` labels. |
   | 3 | **Two-pass `pdflatex` produces stable `.aux`** | If a new package requires 3+ passes (e.g., `glossaries`, `nomencl`, complex `hyperref` back-references), the `.aux` may have stale counters. The build silently falls back to the old `notes_output/ece657_notes.aux`. | Make the pass count configurable (already partially there with the `for _ in range(2)` loop). Add a post-aux sanity check: compare the number of `\newlabel` entries between passes — if it changed, run another pass. |
   | 4 | **`tcolorbox` styles are a closed set (`summarybox`, `pitfallbox`, `perspectivebox`)** | Adding a new tcolorbox style (e.g., `examplebox`, `theorembox`) produces raw LaTeX in EPUB instead of a styled blockquote. | Add an `else` branch in `_extract_title` that falls back to the style name itself as the title (capitalized). Log new styles so they can be mapped intentionally. |
   | 5 | **Flat `\input` nesting** | If a chapter file `\input`s a sub-file that itself `\input`s another (depth > 2), the recursive `_read` in `flatten_latex_inputs` handles this, but the `seen` set will skip it if the same file is included from two different chapters (intentional dedup). If a shared preamble fragment is included in multiple chapters, this is correct. But if actual content is shared, it will be missing from the second occurrence. | Distinguish between preamble includes (safe to dedup) and content includes (should not be deduped). One approach: only dedup files that do not contain `\section` or `\begin{figure}`. |
   | 6 | **Exactly 3 appendices (A, B, C)** | Adding appendix D would work if it follows the same `\section{...}\label{app:...}` pattern, but `\Crefrange{app:...}{app:...}` text says "Appendices" — this is fine. The real risk is if an appendix uses `\chapter` instead of `\section`. | Not a high-priority risk. Just ensure new appendices follow the existing pattern documented in `book_appendices.tex`. |
   | 7 | **No `\part{}` divisions** | Introducing `\part{}` (e.g., "Part I: Foundations") would confuse the heading hierarchy since `prefix_chapter_sections` assumes `\section` is the top-level heading. | If `\part` is ever needed, add a `strip_part_headings` or `handle_part_headings` step before `prefix_chapter_sections`. |

3. **Risk/Tradeoffs:** Over-generalizing the pipeline now adds complexity for hypothetical scenarios. The pragmatic approach is to keep the current tight coupling but add *detection*: log warnings for unrecognized patterns rather than silently producing bad output.

4. **Experiment:** Create a test branch with a dummy Chapter 20 and Appendix D. Run the EPUB build. Verify that numbering, cross-references, and the TOC are correct. This exercises most of the assumptions above.

5. **Definition of done:** The pipeline logs a warning (not a silent pass) for any label prefix, tcolorbox style, or heading pattern it does not explicitly handle. Adding a new chapter or appendix that follows the documented pattern produces correct EPUB output without code changes.

---

## B) Cross-references, numbering, and “reader trust”

### Q4. What is the best authoring policy to ensure cross-references are always correct and readable across PDF + EPUB?
- Context: we fixed several issues by adding labels and rewriting crossrefs based on `.aux`.
- Ask: define the authoring rules (what to label, what to avoid, how to name labels, when to use `\\Cref` vs `\\ref` vs `\\eqref`).
- Output: a compact "house style" policy.

**Answer:**

1. **Diagnosis:** The EPUB builder rewrites `\Cref`, `\cref`, `\eqref`, `\ref`, and `\Crefrange` into hyperlinked text with `.aux`-sourced numbers. The system works well when labels follow the expected prefix conventions. It breaks when: (a) a label uses an unexpected prefix, (b) an author uses bare `\ref` where the prose does not include the noun, or (c) a label is missing entirely and the author writes a hardcoded number.

2. **Recommendation — Cross-reference house style:**

   **What must be labeled:**
   - Every `\section` that represents a chapter: `\label{chap:short_name}`
   - Every `\section` that represents an appendix: `\label{app:short_name}`
   - Every `\subsection` and `\subsubsection`: `\label{sec:chap_topic}` (use the idempotent injector: `python3 epub_builder/scripts/add_missing_heading_labels.py`)
   - Every `\begin{figure}` containing content: `\label{fig:chap_description}`
   - Every `\begin{table}`: `\label{tab:chap_description}`
   - Every `\begin{equation}` (or numbered `align` line): `\label{eq:chap_description}` (use the injector: `python3 epub_builder/scripts/add_missing_equation_labels.py`)

   **Label naming convention:**
   - Format: `prefix:chapterslug_descriptor` (e.g., `fig:lec7_gru`, `eq:supervised_mse`, `sec:transformers_attention`)
   - Use lowercase, underscores, no spaces. Keep names stable across edits (do not include figure numbers in label names).

   **Which command to use:**
   | Context | Command | Example |
   |---------|---------|---------|
   | Referring to a chapter, section, figure, table, or appendix by name | `\Cref{...}` | `\Cref{chap:supervised}` → "Chapter 3" |
   | Referring to an equation | `\eqref{eq:...}` | `\eqref{eq:mse}` → "(3.1)" |
   | Referring to a range | `\Crefrange{...}{...}` | `\Crefrange{chap:intro}{chap:logistic}` → "Chapters 1–4" |
   | **Never use** | Bare `\ref{...}` without preceding noun | It may produce "see 14" with no context |
   | **Never use** | Hardcoded numbers in prose | "see Chapter 3" without `\Cref` — will drift |

   **Rules:**
   - **Always use `\Cref` (capital C) for sentence starts.** The EPUB builder handles both `\Cref` and `\cref` identically, but `\Cref` is safer for PDF (cleveref capitalizes the noun).
   - **Never write a number manually.** If you see "Figure 55" in prose without a `\Cref` or `\ref`, replace it.
   - **One label per logical entity.** Do not put two `\label{fig:...}` in the same `\begin{figure}` unless it genuinely contains two sub-figures with separate labels.

3. **Risk/Tradeoffs:** Strict `\Cref`-only policy means the PDF requires the `cleveref` package (already loaded). The EPUB builder rewrites everything anyway, so there is no EPUB-side risk. The main risk is authorial friction — always typing `\Cref{fig:...}` instead of "Figure~\ref{fig:...}" — but this is a net improvement for both outputs.

4. **Experiment:** Run `rg '\\ref\{' notes_output/*.tex | grep -v '\\[cC]ref\|\\eqref\|\\hyperref\|\\hyperlink\|\\label'` to find all bare `\ref` uses. Audit whether each has a preceding noun. Convert any "naked" refs to `\Cref`.

5. **Definition of done:** Zero bare `\ref{chap:...}`, `\ref{fig:...}`, `\ref{tab:...}`, or `\ref{app:...}` without an immediately preceding noun. Zero hardcoded cross-reference numbers in prose. All numbered entities have labels. The policy is documented in `ONBOARDING.md`.

### Q5. How should we handle **starred headings** (`\\section*`, `\\subsection*`) in EPUB navigation and numbering?
- Context: some headings are intentionally unnumbered; in EPUB, this can look inconsistent if overused.
- Ask: propose a policy: where starred headings are allowed, when they should become numbered, and TOC depth rules.
- Output: decision + rationale.

**Answer:**

1. **Diagnosis:** Starred headings are excluded from LaTeX numbering and from the `prefix_numbered_headings` logic (the code explicitly skips starred variants). In the EPUB TOC, Pandoc includes them as flat entries without numbers, which can look inconsistent when adjacent entries are numbered (e.g., "3.1 Supervised Learning" followed by "Summary" followed by "3.2 Regularization").

2. **Recommendation — starred heading policy:**

   **Where starred headings are allowed (exhaustive list):**
   - **Front matter only:** Preface (`\section*{Preface}`), Acknowledgments, Notation/Glossary, Copyright page.
   - **End matter:** Key Takeaways (`\section*{Key Takeaways}`).
   - **Within-chapter end-of-chapter kit:** These should use `\subsection*` (not `\section*`):
     - `\subsection*{Key takeaways}` (inside tcolorbox, so the heading itself is in the box title)
     - `\subsection*{Exercises and lab ideas}` (inside tcolorbox)
     - The "Where we head next" and "References" paragraphs do **not** need headings at all — they are short prose paragraphs, not sections.

   **Where starred headings should NOT be used:**
   - Inside chapter bodies. If a heading appears within the flow of a chapter and is not part of the end-of-chapter kit, it should be numbered. A heading like `\subsection*{A Note on Terminology}` inside Chapter 5 should either become `\subsection{A Note on Terminology}\label{sec:...}` or be demoted to bold paragraph text (`\paragraph{A Note on Terminology}`).

   **TOC depth rules:**
   - EPUB TOC should include: chapters (`\section`), subsections (`\subsection`), and no deeper.
   - `\subsubsection` entries should appear in chapter body flow but not in the EPUB navigation TOC (avoids clutter on e-readers with small screens).
   - Starred front/end matter sections should appear in the TOC (Pandoc includes them by default; this is correct).
   - Starred `\subsection*` entries (end-of-chapter kit) should NOT appear in the TOC. Pandoc's `--toc-depth=2` will include them if they are `\subsection*`; to suppress, either (a) pass `--toc-depth=2` and accept them, or (b) convert these to `\paragraph*` level so they fall below TOC depth.

   **Concrete recommendation:** Convert end-of-chapter kit headings from `\subsection*` to bold text inside the tcolorbox (the tcolorbox `title=` already provides the visual heading). This eliminates them from the EPUB TOC entirely and is more semantically correct.

3. **Risk/Tradeoffs:** Removing starred subsections from chapter bodies forces either numbering them (which increases the section count) or demoting them to `\paragraph` (which reduces their visual weight in PDF). For most cases, `\paragraph` is the right choice — these are asides, not structural sections.

4. **Experiment:** Search for starred headings inside chapter bodies: `rg '\\subsection\*' notes_output/lecture_*.tex`. For each, decide: promote to numbered, demote to `\paragraph`, or keep as-is (with documented justification). Build the EPUB and verify the TOC has no orphaned unnumbered entries between numbered ones.

5. **Definition of done:** The EPUB TOC contains only: (a) unnumbered front/end matter at the top level, and (b) numbered chapters and sections. No unnumbered entries appear interleaved with numbered entries within a chapter's TOC subtree.

### Q6. Equation numbering feels "random" to readers. Beyond labeling `equation` envs, what else must be done in the LaTeX sources?
- Context: many important expressions are inline, displaystyle-inline, or in non-numbered display math.
- Ask: propose how to detect "important but unnumbered" math and convert to a consistent scheme *without* renumbering the PDF unpredictably.
- Output: suggested audit method + rules for conversion.

**Answer:**

1. **Diagnosis:** The "random" feeling comes from three sources: (a) important equations using `\[...\]` (display, unnumbered) or `equation*` instead of `equation`, (b) `\(\displaystyle ...\)` inline math that visually looks like display math but has no number, and (c) numbered equations appearing sporadically rather than following a logical "definition → derivation → result" pattern. The EPUB makes this worse because the `add_visible_equation_numbers` function only shows numbers for labeled equations — so unlabeled display math appears as an unnumbered gap.

2. **Recommendation — audit method and conversion rules:**

   **Audit method (scripted, safe to run repeatedly):**
   ```bash
   # Find all display math that is NOT numbered:
   rg '\\\[' notes_output/lecture_*.tex --count   # \[...\] blocks
   rg '\\begin\{equation\*\}' notes_output/lecture_*.tex --count  # equation*
   rg '\\begin\{align\*\}' notes_output/lecture_*.tex --count     # align*

   # Find all displaystyle inline math:
   rg '\\displaystyle' notes_output/lecture_*.tex --count

   # Find all numbered equations:
   rg '\\begin\{equation\}' notes_output/lecture_*.tex --count
   rg '\\label\{eq:' notes_output/lecture_*.tex --count
   ```

   Then, for each chapter, produce a ratio: (numbered equations) / (total display math blocks). A healthy ratio is > 0.5 for a textbook. If a chapter has 20 display blocks and only 3 are numbered, the numbering will feel sparse and arbitrary.

   **Conversion rules (what to number vs. what to leave unnumbered):**

   | Pattern | Action |
   |---------|--------|
   | **Definitions** (e.g., "The loss function is defined as...") | Must be `equation` + `\label{eq:...}`. These are referenced later. |
   | **Key results** (e.g., "The gradient is therefore...") | Must be `equation` + `\label{eq:...}`. |
   | **Derivation steps** (multi-line chain leading to a result) | Use `align` with `\notag` on intermediate lines and `\label{eq:...}` on the final result only. This numbers only the conclusion. |
   | **Illustrative examples** (substituting specific values) | Use `\[...\]` (unnumbered). These are not referenced elsewhere. |
   | **Inline display** (`\(\displaystyle ...\)`) | Promote to `\[...\]` if it is on its own visual line. If it is genuinely inline (mid-sentence), keep as `\(...\)` without `\displaystyle`. |
   | **Trivial identities** (e.g., `a = a`) | Use `\[...\]` (unnumbered). |

   **Conversion procedure (safe, no renumbering):**
   - Converting `\[...\]` → `\begin{equation}\label{eq:...}\end{equation}` adds a *new* number at the end of the chapter's equation sequence. It does not change existing numbers.
   - Converting `equation*` → `equation` also adds a new number without shifting existing ones.
   - The only risk is if you change `align*` → `align` and add labels to *some* lines — this is also safe (new numbers appended).
   - **Never remove a `\label{eq:...}` from an existing numbered equation.** That would shift subsequent numbers and break cross-references.

3. **Risk/Tradeoffs:** Adding more equation numbers increases the total count, which can feel cluttered if overdone. The principle: number equations that are *referenced* or that a reader would plausibly want to locate again. Do not number every intermediate step. The risk of under-numbering (reader cannot find the equation the text refers to) is worse than the risk of over-numbering.

4. **Experiment:** Pick the chapter with the worst ratio (likely one of the fuzzy logic or evolutionary computing chapters, which may have fewer numbered equations). Promote the 3–5 most important unnumbered display blocks to `equation` + label. Rebuild PDF and EPUB. Verify: (a) existing equation numbers did not shift, (b) new numbers appear in the expected positions, (c) EPUB shows the new numbers via the `add_visible_equation_numbers` mechanism.

5. **Definition of done:** Every chapter has a "numbered equation audit" ratio > 0.4. Every equation that is referenced (by `\eqref` or prose) has a corresponding `\label{eq:...}`. No `\(\displaystyle ...\)` blocks remain that visually occupy their own line — they are all promoted to proper display math.

### Q7. How should we handle multi-line derivations (`align`, `aligned`, `cases`) so they don't clip and remain navigable?
- Context: EPUB MathML can overflow; Kindle rendering varies.
- Ask: propose a canonical strategy for: long lines, line breaks, equation references inside `cases`, and the "block math scroll container" safety net.
- Output: recommended LaTeX patterns + any EPUB-side CSS/HTML rules.

**Answer:**

1. **Diagnosis:** MathML rendering in EPUB readers has hard viewport limits. `align` and `cases` environments produce `<mtable>` structures in MathML that cannot line-break mid-row. When a single row exceeds the viewport width, it either clips (Apple Books) or shrinks the entire equation to microscopic size (some Kindle devices). The CSS `overflow-x: auto` on `math[display="block"]` in `epub.css` helps for Apple, but Kindle ignores CSS overflow on MathML elements.

2. **Recommendation — canonical strategy by environment:**

   **`align` / `align*` (multi-line derivations):**
   - Keep each line to a **maximum of ~60 characters of rendered math** (roughly: 3–4 fractions or one integral with limits). This is the empirical safe width for phone-width EPUB.
   - When a line is too long, break it using `\\` with `\quad` indentation on continuation lines:
     ```latex
     \begin{align}
       f(x) &= \text{first part} \notag \\
             &\quad + \text{second part} \label{eq:result}
     \end{align}
     ```
   - Label only the final result line (or the line that will be referenced).

   **`aligned` (inside `equation`):**
   - Use `aligned` when you want a single equation number for a multi-line block. Same line-length rule applies.
   - Avoid nesting `aligned` inside `cases` — this creates deeply nested `<mtable>` in MathML that most EPUB readers handle poorly.

   **`cases`:**
   - Keep case expressions short. If a case arm contains a long expression, factor it into a separate named variable defined before the cases block.
   - Do not put `\label` or `\eqref` inside `cases` arms — place the label on the surrounding `equation` environment.
   - If a cases block is still too wide, consider rewriting it as a bulleted list in prose with inline math for each case. This is more EPUB-friendly and often more readable.

   **Long single-line expressions:**
   - For expressions that cannot be broken (e.g., long product chains, matrix definitions), the CSS scroll container is the last resort. The current `epub.css` provides this via `math[display="block"] { overflow-x: auto; }`.
   - For Kindle specifically (which ignores CSS on MathML), the nuclear option is to render the equation as a high-DPI PNG image. This should be reserved for at most 5–10 "hero equations" per book. The builder could add a `% epub:rasterize` comment convention that triggers PNG rendering for specific display math blocks.

   **EPUB-side CSS/HTML (what already exists and what to add):**
   - `postprocess_epub_minimal` in `lib/epub.py` (lines 68–80) already wraps every `<math display="block">` element in a `<div class="math-block">` container. The CSS in `epub.css` (lines 48–52) targets `.math-block` with `overflow-x: auto`. This two-layer defense (CSS on `<math>` directly + CSS on the wrapping `<div>`) is already in place.
   - **What is still missing:** the `.math-block` CSS does not include `-webkit-overflow-scrolling: touch` (the `math[display="block"]` rule does, but the div wrapper does not). Add this to the `.math-block` rule for consistency:
     ```css
     .math-block {
       overflow-x: auto;
       overflow-y: hidden;
       -webkit-overflow-scrolling: touch;
     }
     ```
   - **For Kindle:** even this wrapping div may be ignored. The nuclear option (rasterize specific equations to PNG) remains the only reliable fix for Kindle devices that strip CSS overflow entirely.

3. **Risk/Tradeoffs:** Forcing line breaks on derivations that the author intended as single lines can change the mathematical meaning (e.g., breaking a chain of equalities might suggest the second line is a separate statement). Always preserve the `&=` alignment to signal continuation. The "rasterize specific equations" escape hatch adds build complexity and should be documented per-instance.

4. **Experiment:** Run the existing `audit_epub_layout.py` on the Apple EPUB with `--viewport-w 600` (phone width). Identify the top 10 overflowing math elements. For each, attempt the line-break fix in LaTeX sources. Rebuild and verify: (a) the equation renders fully within 600px, (b) the PDF layout is not degraded, (c) the equation number (if any) still appears correctly in EPUB.

5. **Definition of done:** The layout overflow audit reports zero math-related overflows at 600px viewport width. Every `cases` environment fits within phone width. No `aligned` is nested inside `cases`. The CSS scroll container is verified to activate on any remaining tight-fit expressions in Apple Books.

---

## C) Tables (EPUB-first design)

### Q8. What's the best approach for tables that are too wide for phone screens?
- Context: some tables become unreadable or microscopic in EPUB.
- Ask: propose a strict decision tree:
+ Keep as HTML table with scroll?
+ Split into multiple tables?
+ Convert to bullets/definitions?
+ Convert to a figure image?
- Output: a decision tree + 2–3 examples of "good" transformations.

**Answer:**

1. **Diagnosis:** EPUB readers cannot scroll tables horizontally the way a web browser can. When a table is too wide, readers either (a) shrink all columns to fit (making text microscopic), (b) clip the right edge, or (c) wrap cell contents aggressively (making the layout nonsensical). The current CSS sets `width: auto !important; max-width: 100%`, which helps but cannot fix fundamentally wide tables.

2. **Recommendation — decision tree:**

   ```
   Is the table ≤ 4 columns?
   ├─ YES → Is total content width ≤ ~50 characters per row?
   │        ├─ YES → Keep as HTML table (current pipeline handles it)
   │        └─ NO  → Can any column be abbreviated or split?
   │                 ├─ YES → Abbreviate/split, keep as table
   │                 └─ NO  → Convert to definition list (see below)
   └─ NO (5+ columns) → Is it a comparison/feature matrix?
                         ├─ YES → Transpose (items as rows, features as columns → items as rows, features as sub-items) → definition list
                         └─ NO  → Is it reference/lookup data?
                                  ├─ YES → Convert to a high-DPI figure image (last resort)
                                  └─ NO  → Split into multiple narrower tables
   ```

   **Example transformations:**

   **Example A: Comparison table (5 columns) → definition list**
   Before (table): `| Method | Pros | Cons | Complexity | Use case |`
   After (definition list):
   ```latex
   \begin{description}
     \item[Method A] \emph{Pros:} fast convergence. \emph{Cons:} sensitive to outliers.
       Complexity: $O(n)$. Best for: online learning.
     \item[Method B] ...
   \end{description}
   ```
   This reflows naturally on any screen width.

   **Example B: Hyperparameter table (3 columns, but wide content) → keep as table, abbreviate**
   Before: `| Hyperparameter | Typical Range | Effect on Model |`
   Fix: Shorten "Hyperparameter" to "Param", keep content concise (< 15 words per cell). This stays as a table.

   **Example C: Large notation reference table (6+ columns) → figure image**
   If a table is genuinely a reference chart (e.g., a full symbol glossary), render it as a high-DPI PNG from the PDF. In LaTeX, guard with:
   ```latex
   \ifdefined\HCode
     \includegraphics{table_notation_reference.png}
   \else
     \begin{table}...
   \fi
   ```
   (Note: the EPUB builder takes the `\else` branch since `\HCode` is not defined, so this guard would need adjustment — use a custom `\ifepub` flag or handle in the builder's preprocessing.)

3. **Risk/Tradeoffs:** Converting tables to definition lists changes the visual presentation significantly. For academic readers who expect tabular comparisons, this can feel less rigorous. The compromise: keep truly tabular data (numerical results, benchmarks) as tables with ≤ 4 columns, and convert qualitative comparison tables to definition lists. The figure-image fallback should be used sparingly (< 5 tables in the entire book) because images do not reflow and are inaccessible.

4. **Experiment:** Run `audit_epub_layout.py` at `--viewport-w 600` and extract all table-related overflow warnings. For each overflowing table, apply the decision tree. Rebuild and verify at phone width.

5. **Definition of done:** No table in the EPUB overflows at 600px viewport width. Tables with 5+ columns are either converted to definition lists or rendered as figure images with alt text. The decision for each converted table is documented in a comment in the LaTeX source.

### Q9. What table "house style" should the book use (both PDF and EPUB)?
- Context: we want a premium, consistent look.
- Ask: define rules for captions, column alignment, use of abbreviations, footnotes, and max columns.
- Output: a short house style.

**Answer:**

1. **Diagnosis:** Without a consistent table style, tables vary in: caption placement (above vs. below), rule style (full grid vs. booktabs vs. no rules), column alignment (centered vs. left vs. inconsistent), and caption phrasing. This inconsistency is more noticeable in EPUB where the reader's own stylesheet interacts with the table CSS.

2. **Recommendation — table house style:**

   **Structure:**
   - **Maximum columns:** 4 for EPUB safety. If the PDF genuinely needs 5+, provide an EPUB-specific alternative (see Q8).
   - **Caption placement:** Always above the table (use `\caption{...}` before `\begin{tabular}`). This is the academic convention and ensures the caption is visible before the reader scrolls through the table data.
   - **Caption format:** `Table N. Descriptive sentence.` (the builder prefixes `Table N.` automatically via `prefix_caption_numbers`). The author-written caption should be a complete sentence fragment, not starting with "Table" (to avoid "Table 5. Table of hyperparameters").

   **Typography:**
   - **Rules (lines):** Use `booktabs` style: `\toprule`, `\midrule`, `\bottomrule`. No vertical rules. No `\hline`. This renders cleanly in both PDF and EPUB (Pandoc converts `booktabs` rules to `border-bottom` CSS).
   - **Column alignment:**
     - Text columns: left-aligned (`l`).
     - Numeric columns: right-aligned (`r`) or decimal-aligned if available.
     - Headers: match the data column alignment (do not center headers over left-aligned data).
   - **Font size:** Standard body size. Do not use `\small` or `\footnotesize` to fit more columns — instead, reduce columns.

   **Content:**
   - **Abbreviations:** Define abbreviations in the table caption or in a table footnote, not in the table body. Example: caption says "...MLP = Multi-Layer Perceptron."
   - **Footnotes:** Use `\textsuperscript{a}` markers in cells with footnotes below the table (before `\end{table}`), not LaTeX `\footnote{}` (which behaves unpredictably inside floats and is lost in EPUB).
   - **Units:** Include units in column headers (e.g., "Accuracy (\%)"), not repeated in every cell.
   - **Empty cells:** Use "—" (em dash), not blank.
   - **Number formatting:** Consistent decimal places within a column. Use `\num{}` from `siunitx` if available, or manual consistency.

   **Labels:**
   - Every table must have `\label{tab:chap_descriptor}`.
   - Reference with `\Cref{tab:...}`.

3. **Risk/Tradeoffs:** `booktabs` requires the `booktabs` package (almost certainly already loaded). The main risk is that some existing tables use `|c|c|c|` grid style — converting to booktabs changes their appearance. This is a one-time migration cost that improves both PDF and EPUB.

4. **Experiment:** Audit all tables: `rg '\\begin\{tabular\}' notes_output/lecture_*.tex -c`. Check how many use vertical rules (`|`). Convert one representative table from grid style to booktabs. Compare PDF before/after and verify EPUB renders cleanly.

5. **Definition of done:** All tables use booktabs rules (no `\hline`, no `|`). All captions are above the table and follow the naming convention. No table exceeds 4 columns in the primary (EPUB-safe) version. The house style is documented in `editorial_style.toml` or `ONBOARDING.md`.

---

## D) Figures and diagrams (crispness, whitespace, and consistency)

### Q10. Some figures are high-resolution but still *feel* low quality (too much whitespace, thin strokes, small labels). How do we fix that globally?
- Context: QC indicates images aren't "low-res", but visual quality complaints persist.
- Ask: propose changes at the source level (TikZ styling defaults, matplotlib rcParams, font sizes, line widths, tight bounding boxes).
- Output: a "global style guide" + where it should live (LaTeX preamble, Python scripts, TikZ styles).

**Answer:**

1. **Diagnosis:** "High-res but low-quality" is almost always one of three problems: (a) the figure's *content area* is small relative to the bounding box (excess whitespace), (b) strokes and labels were sized for a full-page A4 layout and become too thin/small when scaled to a phone screen, or (c) the figure uses a light color palette that lacks contrast on small screens. The EPUB builder rasterizes at 1200 DPI, which produces a *large* PNG.

   **What the codebase already does well:**
   - The TikZ standalone preamble in `lib/tikz.py` (lines 22–29) and the ebook preamble `ece657_ebook.tex` (lines 149–156) both set `line width=0.9pt` globally for pgfplots axes, with `tick label style={font=\scriptsize}`, `label style={font=\small}`, and `grid style={gray!15}`. This is already above the TeX default of 0.4pt.
   - TikZ blocks are compiled with `\documentclass[tikz,border=2pt]{standalone}` (`lib/tikz.py` line 12), so bounding boxes are already tightly cropped with a 2pt margin.
   - The color palette (`cbBlue`, `cbOrange`, `cbGreen`, `cbPink`) is defined identically in both preambles and provides good contrast.

   **Where the problem likely persists:** The global pgfplots style only applies to `\begin{axis}` blocks. Standalone TikZ nodes, arrows, and shapes (outside pgfplots) still use the TeX default line width of 0.4pt unless overridden per-figure. This is likely the source of the "thin strokes" complaint.

2. **Recommendation — targeted fixes (not a full rewrite):**

   **TikZ non-axis defaults (add to both preambles, after the existing `\pgfplotsset`):**
   ```latex
   \tikzset{
     every picture/.append style={line width=0.8pt},
     every node/.append style={inner sep=3pt},
   }
   ```
   This raises the *non-pgfplots* line width from the 0.4pt default to 0.8pt (just below the 0.9pt used for axes, to avoid visual weight competition). Do not override `font=` globally for nodes — many TikZ figures set this per-node.

   **Matplotlib scripts — standardize via a shared import:**
   Current state: `scripts/gen_fig64_embeddings.py` uses per-script `plt.rcParams.update({'font.size': 13, 'font.family': 'serif', ...})` and `fig.tight_layout()` with `dpi=300` (not `bbox_inches='tight'`). Each script sets its own style independently.

   Create `scripts/figure_style.py`:
   ```python
   import matplotlib as mpl
   mpl.rcParams.update({
       'font.family': 'serif',
       'font.size': 13,                   # match existing gen_fig64 (was 13)
       'axes.labelsize': 14,              # match existing gen_fig64
       'axes.titlesize': 14,
       'lines.linewidth': 1.5,
       'axes.linewidth': 1.0,
       'figure.autolayout': True,
       'savefig.bbox': 'tight',
       'savefig.pad_inches': 0.05,
       'savefig.dpi': 300,
   })
   ```
   Then have each `gen_fig*.py` script do `import figure_style` at the top (or `from figure_style import *`). This standardizes without changing existing visual decisions.

   **Bounding box / whitespace:**
   - For TikZ: already handled by `standalone` with `border=2pt`. No action needed.
   - For Matplotlib: some scripts use `fig.tight_layout()` (e.g., `gen_fig64_embeddings.py` line 165) but call `fig.savefig(path)` without `bbox_inches='tight'` (line 168). This means tight_layout runs but savefig may add back default padding. Adding `savefig.bbox='tight'` to the shared rcParams fixes this globally.
   - For externally-sourced PNGs (under `assets/`): add a build step that trims whitespace using ImageMagick (`convert -trim +repage`) or a Python PIL equivalent. Cache the trimmed version in `epub_builder/artifacts/media/`.

   **Color / contrast:**
   - Minimum contrast ratio for labels: 4.5:1 against background (WCAG AA).
   - Avoid light yellow, light cyan, or pastel fills on white backgrounds for primary data.
   - The existing palette guidance (ebook-friendly) in `ONBOARDING.md` is correct; enforce it by code review.

   **Where these should live:**
   - TikZ defaults: `notes_output/tikz_defaults.tex` (included via `\input{tikz_defaults}` in the preamble). Alternatively, add to the existing preamble directly.
   - Matplotlib defaults: `scripts/figure_style.py` (imported by each generation script).
   - The rules themselves: document in `notes_output/FIGURE_STYLE_GUIDE.md` (or a section of `ONBOARDING.md`).

3. **Risk/Tradeoffs:** Thicker lines and larger fonts can cause layout shifts in tightly packed diagrams (e.g., the Transformer schematic, LSTM cell). These figures may need per-figure tuning after applying global defaults. Apply globals first, then iterate on the ~5 most complex figures. Changing matplotlib rcParams requires re-running all Python figure scripts, which should be safe if the scripts are idempotent.

4. **Experiment:** Apply the TikZ defaults to the preamble. Rebuild the EPUB. Open on an iPhone (or simulate 375px viewport). Compare the 5 most complained-about figures before and after. For matplotlib, regenerate Figure 54 and Figure 58 with the new rcParams and compare.

5. **Definition of done:** All TikZ figures (including non-pgfplots drawings) have line width >= 0.8pt (pgfplots axes already use 0.9pt). All Matplotlib figure scripts import a shared `figure_style.py` and use `savefig.bbox='tight'`. No figure PNG has > 15% whitespace border (as measured by a trim-check script). Visual spot-check at phone width shows all labels are readable without zooming.

### Q11. Should we move any figure classes to SVG in EPUB?
- Context: Apple Books generally supports SVG well; Kindle support is uneven.
- Ask: which figure types benefit (line-art, flowcharts) and what are the risks?
- Output: recommendation + an experiment plan to validate on Kindle.

**Answer:**

1. **Diagnosis:** SVG would benefit line-art figures (TikZ flowcharts, architecture diagrams, simple schematics) because they remain crisp at any zoom level and have smaller file sizes than high-DPI PNGs. However, the current pipeline rasterizes TikZ to PNG at 1200–3000 DPI, which is already very crisp. The marginal quality gain from SVG is small for most figures. The risk is Kindle compatibility — Amazon's rendering engine has historically had issues with complex SVGs (clipping paths, gradients, embedded fonts, nested `<use>` elements).

2. **Recommendation: Do not move to SVG at this stage.** The cost-benefit is unfavorable:

   **Figures that would benefit from SVG:**
   - Simple flowcharts (< 20 nodes, no gradients)
   - Decision trees
   - Block diagrams (e.g., pipeline schematics)
   - Simple line plots (if converted from TikZ/pgfplots)

   **Figures that would NOT benefit (or would break):**
   - pgfplots with gradients, colormaps, or fill patterns (SVG rendering varies)
   - TikZ figures using `pgfplots` with many data points (SVG file size explodes)
   - Figures with embedded LaTeX math labels (SVG must embed fonts or convert to paths, both fragile)
   - Matplotlib-generated plots (already rasterized; SVG export from matplotlib is large and inconsistent)

   **Why the current approach is adequate:**
   - At 1200 DPI, a typical TikZ figure produces a 3000×2000px PNG. On a Retina display at 375pt viewport, this is 8x density — effectively lossless.
   - PNG is universally supported across all EPUB readers, all Kindle hardware, and all platforms.
   - SVG adds a new class of debugging problems (font embedding, viewport sizing, reader-specific rendering bugs) for a marginal visual improvement.

   **When to revisit this decision:**
   - If file size becomes a KDP blocker (the book exceeds Amazon's delivery size limits). In that case, converting the simplest 10–15 TikZ figures to SVG could meaningfully reduce total EPUB size. But this is unlikely given 19 chapters.

3. **Risk/Tradeoffs:** The main risk of *not* using SVG is slightly larger file sizes. The main risk of *using* SVG is Kindle rendering failures that are difficult to detect automatically (they require visual QA on physical Kindle devices, not just Kindle Previewer on desktop).

4. **Experiment (if you decide to pursue SVG despite the recommendation):**
   - Pick 3 simple TikZ figures (e.g., a flowchart, a block diagram, a simple tree).
   - Modify `compile_tikz_block_to_png` to also produce SVG via `pdf2svg` or `dvisvgm`.
   - Build an Apple EPUB with the SVGs and a Kindle EPUB with the same SVGs.
   - Test Apple Books (macOS + iOS), Kindle Previewer (desktop), and a physical Kindle Paperwhite.
   - Compare: rendering fidelity, file size, and whether math labels render correctly.

5. **Definition of done (for the "no SVG" decision):** Document in `EPUB_PUBLISHING_QC.md` that the project uses PNG-only for EPUB figures, with the rationale. If a future contributor proposes SVG, they should run the experiment above first and demonstrate Kindle compatibility.

### Q12. What is the correct production approach for the **cover** for Apple + Kindle?
- Context: current cover is 1600×2560; thumbnails were previously inconsistent.
- Ask: propose a cover spec target (dimensions, DPI, format), plus how to embed it so both Apple Books and Kindle Previewer display it.
- Output: recommended spec + embedding rules.

**Answer:**

1. **Diagnosis:** The current cover at 1600×2560 meets the minimum for KDP (KDP recommends 1600px minimum on the short side for a 1:1.6 aspect ratio). However, Apple Books and OS-level thumbnail generators have different expectations for how the cover is embedded in the OPF. The builder already adds an EPUB2-style `meta name="cover"` and generates an `<img>`-based `cover.xhtml` (not SVG wrapper), which is good. The remaining issue is resolution for high-DPI displays and aspect ratio consistency.

2. **Recommendation — cover spec:**

   **Target dimensions:**
   - **2560×4096 pixels** (1:1.6 ratio). This is the "ideal" for both platforms:
     - KDP: recommends 2560×1600 minimum; 2560×4096 exceeds this.
     - Apple Books: displays well at any size but benefits from higher resolution on Retina iPads (2732×2048 screen).
   - If 2560×4096 is impractical (cover design tool limitations), **2400×3840** (same 1:1.6) is acceptable.
   - The current 1600×2560 is functional but will appear soft on iPad Pro.

   **Format:**
   - **JPEG** (not PNG) for the cover image embedded in the EPUB. Reason: JPEG compresses photographic/gradient content much better, keeping the EPUB file size down. A 2560×4096 PNG cover can be 5–10 MB; the same as JPEG at quality 92 is ~500 KB.
   - Keep the source as PNG (lossless) in the repo (`BookCover.png`). Convert to JPEG at build time for EPUB embedding.

   **Color space:**
   - **sRGB** (not CMYK, not Adobe RGB). Both Apple and Kindle expect sRGB for digital covers.

   **Embedding rules (both platforms):**
   - The OPF `<manifest>` must include the cover image with `properties="cover-image"` (EPUB3) AND `<meta name="cover" content="cover-image-id"/>` (EPUB2 fallback).
   - The `cover.xhtml` should contain a simple `<img>` (not an SVG wrapper). The builder already does this.
   - Pandoc's `--epub-cover-image` flag handles most of this correctly. The `postprocess_epub_minimal` step adds the EPUB2 meta. Verify that both are present after each build.
   - For Kindle specifically: KDP's processing re-generates the cover thumbnail from the embedded image. The aspect ratio must be exactly 1:1.6 (no extra whitespace or borders). If the source image has even 1px of transparency, KDP may render it as black — ensure the cover is fully opaque (no alpha channel).

   **Build-time steps:**
   - Generate JPEG from source PNG: `convert BookCover.png -quality 92 -colorspace sRGB BookCover_epub.jpg` (ImageMagick) or equivalent PIL script.
   - Update `book_metadata.json` to point `cover_image` to the JPEG.
   - Alternatively, add a step in `build.py` that converts PNG→JPEG on the fly if the source is PNG and the target is EPUB.

3. **Risk/Tradeoffs:** Using JPEG introduces minimal quality loss (at quality 92, it is visually indistinguishable from PNG). The main risk is forgetting to regenerate the JPEG after updating the source PNG. Automating the conversion in the build script eliminates this risk.

4. **Experiment:** Upscale the current 1600×2560 cover to 2560×4096 using PIL/Pillow (`Image.open(...).resize((2560, 4096), Image.LANCZOS)`) or ImageMagick (`convert BookCover.png -resize 2560x4096 -quality 92 BookCover.jpg`). Note: `scripts/generate_cover.py` is **not** a resizing tool — it calls the OpenAI Images API (`gpt-image-1`) to generate entirely new cover artwork at 1536×1024 (landscape), so it is not suitable for this task. Convert the upscaled PNG to JPEG at quality 92. Build the Apple and Kindle EPUBs. Verify: (a) Finder/Quick Look shows the cover thumbnail, (b) Apple Books shows the cover on the library shelf, (c) Kindle Previewer shows the cover on the title page and library view.

5. **Definition of done:** The cover image is >= 2560×4096 sRGB JPEG in the EPUB. Both Apple Books and Kindle Previewer display the cover correctly at the library level and on the title page. Finder/Quick Look shows the thumbnail. The conversion from source PNG to EPUB JPEG is automated in the build script.

---

## E) Editorial continuity (premium academic book standard)

### Q13. What are the biggest "editorial continuity" risks in a book derived from lecture notes?
- Context: the voice sometimes drifts (course phrasing, "today/next time", etc.).
- Ask: list likely continuity issues (terminology drift, repeated definitions, inconsistent notation).
- Output: a prioritized checklist for an editor.

**Answer:**

1. **Diagnosis:** Lecture-note-derived books have a characteristic set of continuity problems because each lecture was originally self-contained, prepared at different times, and aimed at a live audience. When assembled into a book, the seams show.

2. **Recommendation — prioritized editorial continuity checklist:**

   **Priority 1 (reader-facing, immediately noticeable):**

   | # | Risk | Detection method |
   |---|------|-----------------|
   | 1 | **Course/lecture voice leaking into chapter body** ("today we'll", "in the next lecture", "as discussed last time", "these notes", "your assignment") | `rg -i '(today|tonight|last time|next time|next lecture|last lecture|next class|these notes|this course|your assignment|the midterm|the exam|the lab|office hours)' notes_output/lecture_*.tex` |
   | 2 | **Repeated definitions** — the same concept (e.g., "overfitting", "gradient descent", "loss function") is formally defined in multiple chapters as if first introduced | Manual audit: for each key term, search `rg 'overfitting' notes_output/lecture_*.tex` and verify only one chapter gives the formal definition; subsequent chapters should say "recall from \Cref{...}" |
   | 3 | **Terminology drift** — the same concept has different names in different chapters (e.g., "cost function" in Ch. 3 vs. "loss function" in Ch. 5 vs. "objective" in Ch. 7; "features" vs. "inputs" vs. "covariates") | Create a terminology concordance: list 20 key terms and their canonical name. `rg` for variants. |
   | 4 | **Notation collisions** — same symbol means different things in different chapters (e.g., `\sigma` as activation function, standard deviation, and sigmoid; `W` as weight matrix vs. a different matrix) | Compare each chapter's "Notation note" box against `notation.tex`. Flag any `\sigma`, `\phi`, `W`, `x`, `y` that changes meaning without redefinition. |
   | 5 | **Forward references to content that doesn't exist** ("as we will see in the chapter on GANs", "the companion code repository") | `rg -i '(as we will see|we will cover|companion|code repository|slides|solution manual)' notes_output/lecture_*.tex` |

   **Priority 2 (structural, affects perceived quality):**

   | # | Risk | Detection method |
   |---|------|-----------------|
   | 6 | **Inconsistent chapter openings** — some chapters have a bridge paragraph + design motif, others jump straight into content | Read the first 10 lines of each `lecture_*.tex` and verify the pattern: bridge sentence → design motif hook → learning outcomes |
   | 7 | **Inconsistent chapter endings** — some have all four kit elements (Key takeaways, Exercises, Where we head next, References), others are missing pieces | `rg '\\begin\{tcolorbox\}.*summarybox\|Key takeaways\|Exercises' notes_output/lecture_*.tex` per chapter; verify all 4 elements |
   | 8 | **Depth inconsistency** — some chapters are 30 pages, others are 10; some have exercises, others don't | Check page counts per chapter from the PDF TOC |
   | 9 | **Citation style drift** — some chapters use `\citep{}`, others have informal "(Author, year)" in prose, others have per-chapter reference lists | `rg '\(.*\d{4}\)' notes_output/lecture_*.tex` to find informal citations; `rg '\\subsection\*\{Ref' notes_output/lecture_*.tex` to find rogue per-chapter lists |
   | 10 | **Tense inconsistency** — lecture voice tends to use present tense ("we now compute"), textbook voice uses a mix; jumps between "we" and passive voice within a paragraph | Spot-check: read one paragraph from each of chapters 2, 8, 14, 19. Flag tense/voice shifts within a single section. |

   **Priority 3 (subtle, matters for premium pricing):**

   | # | Risk | Detection method |
   |---|------|-----------------|
   | 11 | **Assumed prerequisites shift** — Chapter 2 assumes no ML background, Chapter 15 assumes familiarity with neural networks without signposting | Review the "bridge" paragraph of each chapter; verify it states what the reader should know |
   | 12 | **Example reuse without acknowledgment** — the same dataset or toy example appears in multiple chapters without a consistent running-example thread | Search for "Iris", "MNIST", "XOR", common toy names |
   | 13 | **Inconsistent figure/table cross-references** — some figures are discussed in detail, others are mentioned in passing and never referenced again | For each `\label{fig:...}`, verify at least one `\Cref{fig:...}` exists in the chapter body |

3. **Risk/Tradeoffs:** Fixing all of these in a single pass is a large editorial effort. Prioritize items 1–5 (they are automatable or semi-automatable) and items 6–7 (structural consistency). Items 10–13 are best done by a human editor in a dedicated read-through.

4. **Experiment:** Run the grep commands for items 1 and 5. If the hit count is > 20, there is significant lecture voice remaining. If < 5, the previous editorial passes have been effective and the focus should shift to items 2–4.

5. **Definition of done:** Zero hits for item 1 (course voice in chapter bodies). A published terminology concordance with 20+ terms. Every chapter has all 4 end-of-chapter kit elements. Notation consistency verified against `notation.tex` for all chapters.

### Q14. How should we standardize chapter structure to feel like a cohesive book?
- Context: we want consistent Learning Outcomes / Design motif / Exercises / References notes.
- Ask: propose a template policy (what each chapter should contain; what's optional).
- Output: a recommended chapter template + exceptions.

**Answer:**

1. **Diagnosis:** The current chapters vary in structure. Some have all four end-of-chapter elements; others are missing exercises or the "where we head next" paragraph. The opening structure also varies — some have a design motif box, others don't. This inconsistency is the single biggest signal that the book originated as lecture notes rather than being authored as a book.

2. **Recommendation — chapter template:**

   **Required elements (every numbered chapter, in this order):**

   ```
   \section{Chapter Title}\label{chap:slug}

   % --- OPENING (required) ---
   [1–2 sentence bridge from previous chapter, using \Cref{chap:previous}]

   \begin{tcolorbox}[perspectivebox, title={Design motif}]
     [Core question or framing metaphor for this chapter — 2–4 sentences]
   \end{tcolorbox}

   \textbf{Learning outcomes.} After this chapter, you will be able to:
   \begin{itemize}
     \item ...
     \item ... (3–5 items)
   \end{itemize}

   % --- BODY (chapter-specific) ---
   \subsection{...}\label{sec:...}
   ...

   % --- CLOSING (required, in this exact order) ---
   \begin{tcolorbox}[summarybox, title={Key takeaways}]
     \begin{itemize}
       \item ... (3–6 bullet points)
     \end{itemize}
   \end{tcolorbox}

   \begin{tcolorbox}[title={Exercises and lab ideas}]
     \begin{enumerate}
       \item ... (3–8 exercises, mix of conceptual and hands-on)
     \end{enumerate}
   \end{tcolorbox}

   \paragraph{Where we head next.}
   [1–2 sentences previewing the next chapter, using \Cref{chap:next}.]

   \paragraph{References.}
   [1–2 sentences pointing to seminal works, using \citet{...}.]
   \nocite{key1,key2}  % ensure key works appear in unified bibliography
   ```

   **Optional elements (use when appropriate):**
   - **"Notation note" box** — use at the start of a section that introduces new symbols, only if the notation differs from `notation.tex` or is chapter-specific.
   - **"Pitfall" box** — use for common misconceptions. At most 2 per chapter to avoid diluting their impact.
   - **"Perspective" box** — use for historical context or cross-disciplinary connections. At most 1 per chapter.
   - **"Running example" thread** — if a chapter uses a worked example throughout, name it and reference it consistently.

   **Exceptions (documented, not ad-hoc):**
   - **Chapter 1 (About This Book):** No bridge paragraph (it is the first chapter). May have a longer design motif that serves as the book's framing. May omit exercises (it is an introduction).
   - **Key Takeaways (end matter):** No chapter structure — it is a standalone summary section.
   - **Appendices:** Follow the same template but may omit the "Where we head next" paragraph (appendices are not sequential). Exercises are optional for appendices.

3. **Risk/Tradeoffs:** Enforcing a rigid template can feel formulaic if the content doesn't naturally fit (e.g., a chapter that is purely mathematical derivation may not have natural "lab ideas"). The template should be a guideline with documented exceptions, not a straitjacket. The key is consistency in the *order* and *presence* of elements, not in their length.

4. **Experiment:** Create a checklist matrix: chapters (rows) × template elements (columns). Fill it in by scanning each `lecture_*.tex` file. Identify which chapters are missing which elements. Fix the 3 most-deficient chapters first and verify the book feels more cohesive.

5. **Definition of done:** Every numbered chapter (1–19) has: bridge, design motif, learning outcomes, key takeaways, exercises, "where we head next", and references. Appendices have all except "where we head next". The template is documented in `ONBOARDING.md`.

### Q15. What is the standard for "academic integrity" of claims and citations in this manuscript?
- Context: citations exist, but the aux compile used for EPUB numbering does not run BibTeX; we also want a premium product.
- Ask: propose a policy for:
  - what must be cited,
  - how to handle uncited historical claims,
  - and how to keep `refs.bib` healthy (dedupe keys, completeness).
- Output: a policy + suggested automated checks.

**Answer:**

1. **Diagnosis:** Lecture notes often make historical claims casually ("Rosenblatt proposed the perceptron in 1958") without formal citations, because the lecturer assumes shared context. In a published book, every factual claim about a specific person, date, or result must be traceable to a citation. The EPUB pipeline does not run BibTeX (the aux compile is numbering-only), so citations in the EPUB appear as hyperlinked text generated by the PDF's `.bbl`, not generated fresh — meaning stale or missing `.bbl` entries will silently produce "[?]" in the EPUB.

2. **Recommendation — citation policy:**

   **What must be cited:**
   - Every **attribution** ("X proposed Y", "Y was introduced by Z"): cite the original paper.
   - Every **quantitative claim** ("achieves 95% accuracy on ImageNet"): cite the source.
   - Every **theorem, algorithm, or named result** used in the book: cite the original formulation or a standard reference.
   - Every **figure or table** that reproduces or adapts data from another source: cite in the caption ("Adapted from \citet{...}").
   - Every **non-obvious factual claim** ("ReLU solves the vanishing gradient problem"): cite evidence or qualify the claim ("ReLU mitigates vanishing gradients in practice \citep{...}").

   **What does NOT need citation:**
   - Widely known mathematical facts (chain rule, Bayes' theorem) — unless attributing the name.
   - The book's own definitions, notation, and examples.
   - General pedagogical framing ("In this chapter, we explore...").

   **How to handle uncited historical claims:**
   - **Search `refs.bib` for the key.** If a BibTeX entry exists but is not `\cite`d, add `\citet{key}` or `\nocite{key}`.
   - **If no BibTeX entry exists:** add one to `refs.bib`. Use the canonical publication (not a secondary source or Wikipedia). Prefer journal/conference publications over arXiv when both exist.
   - **If the claim is vague or potentially inaccurate** ("neural networks were first proposed in the 1940s"): verify against the original source and tighten the claim ("McCulloch and Pitts introduced a mathematical model of the neuron \citep{McCullochPitts1943}").

   **Keeping `refs.bib` healthy — automated checks:**

   ```bash
   # 1. Find all \cite keys used in sources:
   rg '\\cite[tp]?\{([^}]+)\}' notes_output/*.tex -o --no-filename \
     | sed 's/\\cite[tp]\?{//;s/}//' | tr ',' '\n' | sort -u > /tmp/cited_keys.txt

   # 2. Find all keys defined in refs.bib:
   rg '^@' notes_output/refs.bib -o | wc -l  # total entries
   rg '^\s*@\w+\{(\w+),' notes_output/refs.bib -o --no-filename \
     | sed 's/@.*{//;s/,//' | sort -u > /tmp/bib_keys.txt

   # 3. Cited but missing from bib (will produce [?]):
   comm -23 /tmp/cited_keys.txt /tmp/bib_keys.txt

   # 4. In bib but never cited (dead entries, not harmful but cluttering):
   comm -13 /tmp/cited_keys.txt /tmp/bib_keys.txt

   # 5. Duplicate keys in refs.bib:
   rg '^\s*@\w+\{(\w+),' notes_output/refs.bib -o --no-filename \
     | sed 's/@.*{//;s/,//' | sort | uniq -d
   ```

   **For the EPUB specifically:**
   - The aux compile does not run BibTeX, so citations in EPUB are only correct if `ece657_notes.bbl` was generated from a recent PDF build. The build should either: (a) run BibTeX as part of the EPUB aux compile, or (b) copy the most recent `.bbl` from `notes_output/` into the aux temp directory before the pdflatex passes. Option (b) is simpler and more reliable.
   - Add a post-build check: search the EPUB XHTML for `[?]` strings, which indicate unresolved citations.

3. **Risk/Tradeoffs:** Being strict about citations adds editorial work but significantly increases the book's credibility and usefulness as a reference. The risk of over-citation (cluttering prose with citations) is low for a textbook — academic readers expect thorough citation. The main practical risk is that adding new BibTeX entries can introduce key collisions or formatting errors in `refs.bib`.

4. **Experiment:** Run check #3 above (cited but missing from bib). If the list is non-empty, those citations are currently producing "[?]" in the PDF. Fix those first. Then run a search for uncited historical claims: `rg '(proposed|introduced|discovered|invented|developed) (by|in \d{4})' notes_output/lecture_*.tex` and verify each has a citation.

5. **Definition of done:** Zero `[?]` citations in PDF or EPUB. Every historical attribution has a `\citet` or `\citep`. Zero duplicate keys in `refs.bib`. The citation health checks run as part of the editorial QC pipeline (`run_editorial_qc.sh`).

---

## F) Tooling and future-proof documentation

### Q16. What documentation is still missing for a future LLM/human to confidently maintain this project?
- Context: we have `ONBOARDING.md`, `EPUB_PUBLISHING_QC.md`, image/layout audits, and now a production roadmap.
- Ask: identify documentation gaps (release tagging, KDP upload steps, test matrix, style guides, "how to add a chapter safely").
- Output: list of missing docs + proposed file names/locations.

**Answer:**

1. **Diagnosis:** The existing documentation is strong on *what* the project is and *how to build*. It is weak on *how to change things safely*, *how to release*, and *what decisions were made and why*. A new contributor (human or LLM) can build the EPUB but would not know how to add a chapter, cut a release, or upload to KDP without asking questions.

2. **Recommendation — missing documentation, in priority order:**

   | # | Gap | Proposed file | Content |
   |---|-----|--------------|---------|
   | 1 | **How to add a chapter safely** | `notes_output/HOWTO_ADD_CHAPTER.md` | Step-by-step: create `.tex` file, add to `book_chapters.tex`, add `\label{chap:...}`, run label injectors, rebuild PDF + EPUB, verify numbering didn't shift for existing chapters, update `ONBOARDING.md` chapter table. |
   | 2 | **Release and tagging process** | `notes_output/RELEASE_PROCESS.md` | When to tag (before KDP upload), naming convention (`v1.0.0-rc1`, `v1.0.0`), what artifacts to archive (PDF, both EPUBs, epubcheck output, QC reports), where to store them (git tag + GitHub release, or `artifacts/releases/`). |
   | 3 | **KDP + Apple Books upload guide** | `notes_output/PUBLISHING_UPLOAD.md` | Step-by-step for KDP: login, create new book, upload interior PDF, upload cover, set metadata, pricing, preview. Same for Apple Books Connect. Include common gotchas (KDP cover rejection, file size limits, metadata mismatches). |
   | 4 | **Decision log (ADR-style)** | `notes_output/DECISIONS.md` | Record of key technical decisions: why Pandoc over TeX4ht, why PNG over SVG, why `.aux`-based numbering, why MathML for Apple and rasterized math for Kindle, etc. Format: date, decision, context, alternatives considered, outcome. |
   | 5 | **Figure style guide** | `notes_output/FIGURE_STYLE_GUIDE.md` | (Content from Q10 answer): TikZ defaults, matplotlib rcParams, minimum line widths, font sizes, bounding box rules, color palette. |
   | 6 | **Test matrix** | `notes_output/TEST_MATRIX.md` | What to test, on which devices/readers, for each release: Apple Books (macOS, iOS), Kindle Previewer (desktop), Kindle Paperwhite (physical), Kindle app (iOS/Android). Checklist: cover, TOC, 3 figure-heavy pages, 3 math-heavy pages, 1 table-heavy page. |
   | 7 | **Terminology concordance** | `notes_output/TERMINOLOGY.md` | Canonical names for 20–30 key terms, plus deprecated variants that should not appear. (From Q13.) |
   | 8 | **Troubleshooting guide** | `notes_output/TROUBLESHOOTING.md` | Common build failures and fixes: "TikZ block fails to compile" → check logs in `artifacts/tikz_logs/`. "Equation shows [?]" → rebuild PDF first to regenerate `.bbl`. "Cover not showing in Finder" → verify EPUB2 meta in OPF. |

3. **Risk/Tradeoffs:** Creating too many documentation files increases the maintenance burden and the risk that docs become stale. Mitigate by: (a) keeping each doc short (1–2 pages), (b) cross-linking from `ONBOARDING.md` as the single entry point, (c) adding a "last verified" date at the top of each doc.

4. **Experiment:** Start with docs #1 and #2 (add chapter + release process) since they have the highest impact for a new contributor. Write them based on the current workflow. Have a second person (or LLM) attempt to follow them literally and note where the instructions are ambiguous.

5. **Definition of done:** `ONBOARDING.md` links to all supplementary docs. A new contributor can add a dummy Chapter 20, build PDF + EPUB, and tag a release by following the documentation alone, without asking questions.

### Q17. What is the best regression strategy to prevent "one-off fixes" from reintroducing inconsistencies?
- Context: we've fixed specific cases (appendix numbering, chapter refs, equation labels, math clipping).
- Ask: propose a regression suite strategy (scripts, expected artifacts, how to diff outputs) that scales.
- Output: a concrete regression plan with acceptance criteria.

**Answer:**

1. **Diagnosis:** The project has accumulated a set of specific fixes (appendix refs showing as "Appendix 22", display math clipping, missing equation numbers, etc.) that were debugged individually. Without a regression suite, any of these could reappear when: (a) the LaTeX sources change, (b) the builder code is refactored, (c) Pandoc is upgraded, or (d) new chapters/content are added. The existing `run_release_checks.sh` produces snapshots but does not *compare* against a known-good baseline.

2. **Recommendation — regression suite strategy:**

   **Layer 1: Preprocessor unit tests (fast, runs in seconds)**

   Create `epub_builder/tests/test_latex_transforms.py` with pytest:
   ```
   - test_rewrite_crossrefs_chapter: input with \Cref{chap:foo} → output contains "Chapter 3"
   - test_rewrite_crossrefs_appendix: input with \Cref{app:foo} → output contains "Appendix A" (not "Appendix 22")
   - test_rewrite_crossrefs_equation: input with \eqref{eq:bar} → output contains "(4.1)"
   - test_rewrite_crefrange: input with \Crefrange{chap:a}{chap:b} → output contains "Chapters 1–4"
   - test_promote_displaystyle: input with \(\displaystyle long_expr\) → output uses \[...\]
   - test_promote_long_inline: input with \( very_long_expr \) → output uses \[...\]
   - test_prefix_chapter_sections: input with \section{Title}\label{chap:x} → output has "Chapter N: Title"
   - test_prefix_caption_numbers: input with figure + \label{fig:x} → output has "Figure N."
   - test_tcolorbox_transform: input with tcolorbox → output uses quote
   - test_tikz_extraction: input with nested tikzpicture → correct block boundaries
   ```

   Each test uses a minimal LaTeX snippet and a mock `aux_numbers` dict. These tests are the most valuable regression protection because they run instantly and cover the exact transformations that have broken before.

   **Layer 2: EPUB structural assertions (medium, runs in ~30 seconds)**

   Create `epub_builder/tests/test_epub_structure.py` that runs against a pre-built EPUB:
   ```
   - test_no_raw_tikzpicture: no XHTML file contains \begin{tikzpicture}
   - test_no_pandoc_bare_refs: no data-reference="chap:" or "fig:" attributes
   - test_all_fig_labels_have_images: every fig: label from aux has an <img> in EPUB
   - test_no_question_mark_refs: no "(?" or "Chapter ?" or "Figure ?" in text content
   - test_no_bracket_question_refs: no "[?]" in text (unresolved citations)
   - test_cover_present: EPUB contains cover.xhtml with an <img>
   - test_equation_numbers_present: for each eq: label in aux, a corresponding "(N)" appears in EPUB
   - test_appendix_letters: appendix references use A/B/C, not numbers > 19
   ```

   **Layer 3: Golden-file diff (slow, runs after full build)**

   After each release candidate build:
   1. Extract all text from the EPUB: `zipinfo -1 *.epub | grep xhtml | while read f; do unzip -p *.epub "$f" | sed 's/<[^>]*>//g'; done > epub_text.txt`
   2. Compare against the previous golden file: `diff epub_text_golden.txt epub_text.txt`
   3. Any diff must be reviewed: is it an intentional content change, or a regression?

   Store golden files in `epub_builder/tests/golden/` (gitignored, or committed for release candidates only).

   **Layer 4: Visual regression (manual, per-release)**

   Use the existing `qc_epub_vs_pdf.py` to produce side-by-side crops. Compare against the previous release's crops. This catches CSS/layout regressions that text diffs miss.

   **Acceptance criteria for each layer:**

   | Layer | Pass criteria | When to run |
   |-------|--------------|-------------|
   | 1. Unit tests | All tests pass | Every code change to `lib/latex.py` |
   | 2. Structural | All assertions pass | Every EPUB build |
   | 3. Golden diff | Diff is empty or all changes are documented | Before each release tag |
   | 4. Visual | No unexpected visual changes | Before each KDP/Apple upload |

3. **Risk/Tradeoffs:** The golden-file approach is fragile — any content edit produces a diff that must be manually reviewed. This is acceptable for a book (content changes are infrequent and intentional) but would not scale for a rapidly-changing project. The unit tests are the highest-ROI investment; they are fast, stable, and directly protect against the specific bugs that have already occurred.

4. **Experiment:** Implement Layer 1 (unit tests) for the 5 most important transforms. Run them. Then deliberately introduce a regression (e.g., comment out the `app:` handling in `rewrite_crossrefs`). Verify the test catches it.

5. **Definition of done:** Layer 1 tests exist and run via `pytest epub_builder/tests/`. Layer 2 assertions run as part of every `build.py` invocation (extend `_verify_epub_figures` or add a new verification function). The test suite is documented in `ONBOARDING.md`. A CI-friendly entry point exists (even if CI is not set up yet).

---

## Answer format (for the commentator LLM)

For each question:
1. **Diagnosis** (what’s likely happening / why it matters)
2. **Recommendation** (policy-level and implementation-level)
3. **Risk/Tradeoffs**
4. **Experiment** (how to validate quickly)
5. **“Definition of done”** (clear success criteria)
