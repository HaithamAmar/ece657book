# Editorial Feedback Log

Use this file to record editorial feedback as you read the **PDF** and **EPUBs**. Keep entries concrete, reproducible, and easy to route to either:
- **Source fixes** (`notes_output/*.tex`) when intent/labels/wording are wrong, or
- **Pipeline fixes** (`epub_builder/`) when conversion/styling/packaging is wrong.

## How to reference builds (always include)

- PDF: `notes_output/ece657_notes.pdf`
- Apple EPUB: `epub_builder/dist/ece657_ebook_apple.epub`
- Kindle EPUB: `epub_builder/dist/ece657_ebook_kindle.epub`
- Release bundle (snapshots + audits): `notes_output/artifacts/release_checks/`
  - PDF vs EPUB crops: `notes_output/artifacts/release_checks/pdf_vs_epub_apple/compare/`
  - Image quality report: `notes_output/artifacts/release_checks/epub_image_quality.md`
  - Layout overflow report: `notes_output/artifacts/release_checks/epub_layout_audit_1000w.md`
  - Table audit report: `notes_output/artifacts/release_checks/epub_table_audit.md`

## Forward plan

- Execution backlog for publish-grade EPUB work: `notes_output/EPUB_EXECUTION_PLAN.md`

## Entry template (copy/paste)

### [YYYY-MM-DD] Item: <short title>

- **Severity:** blocker / major / minor / polish
- **Surface:** PDF / Apple EPUB / Kindle EPUB / All
- **Location:**
  - Chapter/Appendix: <e.g., Chapter 7>
  - Section heading: <optional>
  - Label(s): <e.g., `fig:roadmap`, `eq:bayes_theorem`, `tab:...`, `chap:...`, `sec:...`, `app:...`>
  - PDF page: <number>
  - EPUB file: <e.g., `EPUB/text/ch003.xhtml`> (optional; XHTML filenames may vary by build)
- **What you see (symptom):** <1–3 sentences>
- **What it should be (expected):** <1–3 sentences>
- **Evidence / artifacts:**
  - Screenshot(s): <paste/attach externally; optionally note path if saved>
  - Crop(s) from release bundle: <path(s) under `notes_output/artifacts/release_checks/...`>
- **Likely root cause (guess):** source / pipeline / reader-specific
- **Proposed fix:**
  - Source edit: <file + intent>
  - EPUB pipeline: <file + intent>
- **Regression check:** what to re-run to confirm
  - `bash notes_output/scripts/run_release_checks.sh`
  - `bash notes_output/scripts/run_production_checks.sh`

## Quick categories (use consistent wording)

- **References/numbering:** Chapter/Section/Figure/Table/Equation/Appendix numbering, missing “Chapter”, wrong link targets.
- **Equations:** missing numbers, inline clipping, unreadable scaling, bad line breaks.
- **Figures:** missing, blurry/low DPI, wrong figure shown, excessive whitespace/cropping.
- **Tables:** microscopic, overflow, misaligned columns, needs redesign into smaller tables/lists.
- **Typography/layout:** inconsistent heading hierarchy, spacing, callout styling, hyphenation artifacts.
- **Metadata/cover:** cover thumbnail missing, wrong title/author, identifiers/rights.
- **Accessibility:** missing alt text, heading hierarchy broken, table headers not semantic.

## Known guardrails (so feedback is actionable)

- Do not hardcode “Chapter 7” / “Figure 12” in prose; use `\\Cref{...}` / `\\eqref{...}` and labels.
- Every numbered equation-like environment must have `\\label{eq:...}` (enforced by `notes_output/scripts/check_equations.py`).
- The production gatekeeper uses Apple EPUB audits and fails on:
  - flagged images,
  - overflow issues,
  - wide tables (>= 5 columns), **except** the allowlisted word-vectorization table (caption contains “Feature-based word vectorization”).

## Production/pipeline fix log (keep this short and factual)

### [2026-02-10] Item: Chapter openings (avoid box-dump; narrative bridge first) + running-example de-boxing (Parts II-III) — DONE

- **Severity:** major (reader flow + consistency)
- **Surface:** PDF + Apple EPUB + Kindle EPUB
- **What changed (source):**
  - `notes_output/lecture_1_intro.tex`
    - Inserted narrative bridge before the first callout so the book does not open with a box.
  - `notes_output/lecture_3_part_i.tex`
    - Same treatment for Chapter 5: narrative bridge now precedes Learning Outcomes.
  - `notes_output/lecture_8_part_i.tex`
    - Chapter 13 no longer opens with Learning Outcomes; the bridge from RNNs is now the first prose.
    - Converted early "Chapter map" and "Notation handoff" callouts into normal prose paragraphs to avoid a box-heavy front section.
  - `notes_output/lecture_transformers.tex`
    - Chapter 14 now opens with a narrative bridge, then Learning Outcomes and Design motif.
    - Moved `Risk & audit` to after the first subsection starts; moved the attention author's note to the first attention subsection so it lands next to the math it comments on.
  - `notes_output/lecture_8_part_ii.tex`
  - `notes_output/lecture_9.tex`
  - `notes_output/lecture_10_part_i.tex`
  - `notes_output/lecture_10_part_ii.tex`
    - Converted the early "Running example checkpoint" boxes into plain prose paragraphs so these chapters start with at most two scaffolding boxes (Learning Outcomes, Design motif).
- **What changed (QC tooling):**
  - `notes_output/scripts/advanced_editorial_audit.py`
    - Added new opening-flow checks (`opens-with-box`, `prose-words-before-first-box`) and a heuristic short-subsection detector (<90 words).
- **Evidence / artifacts:**
  - Before: `notes_output/artifacts/qc/advanced_editorial_audit_20260210_081337.md`
  - After: `notes_output/artifacts/qc/advanced_editorial_audit_20260210_082008.md`
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` (must stay green).

### [2026-02-09] Item: Minimal editorial tightening pass (Chapters 13-14 flow coherence) — DONE

- **Severity:** polish (cohesion/readability)
- **Surface:** PDF + Apple EPUB + Kindle EPUB
- **What changed (source):**
  - `notes_output/lecture_8_part_i.tex`
    - Renamed duplicated Word2Vec section titles to clarify progression:
      - `Word2Vec: Two Architectures` -> `Word2Vec at a glance`
      - `Word Embeddings: Continuous Bag of Words (CBOW) and skip-gram models` -> `Word2Vec objectives in detail`
      - Detailed subheads now explicitly mark objective derivations (`CBOW objective (detailed form)`, `skip-gram objective (detailed form)`).
    - Added one bridge sentence between the conceptual and detailed Word2Vec sections to reduce perceived repetition.
  - `notes_output/lecture_transformers.tex`
    - Tightened the attention shape-convention callback to reference both the RNN and NLP chapters (`\Cref{chap:rnn,chap:nlp}`), reflecting the current chapter ordering and avoiding stale single-chapter anchoring.
- **Deferred by intent (unchanged in this pass):**
  - Wide/clipped Chapter 2 transformation-toolkit table treatment remains deferred pending separate design decision.
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` (must stay green).

### [2026-02-09] Item: Wording-level continuity pass across Chapters 11-14 (no structural change) — DONE

- **Severity:** polish (narrative continuity)
- **Surface:** PDF + Apple EPUB + Kindle EPUB
- **What changed (source):**
  - `notes_output/lecture_6.tex`
    - Tightened opening/closing bridge language so Chapter 11 now hands off explicitly to the Chapter 12->14 sequence thread without introducing architecture content early.
  - `notes_output/lecture_7.tex`
    - Refined opening and chapter handoff language so RNNs lead naturally into representation learning (`chap:nlp`) and then attention (`chap:transformers`).
  - `notes_output/lecture_8_part_i.tex`
    - Reworded intro and closing transition to emphasize representation as the connective layer between recurrent and attention models.
  - `notes_output/lecture_transformers.tex`
    - Reworded intro and exit paragraph to frame Chapter 14 as the endpoint of the neural sequence thread before the soft-computing pivot.
- **Not changed by design:** section order, labels, equations, figures, and chapter structure.
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` (must stay green).

### [2026-02-03] Item: `adjustbox` option text leaking into EPUB (“max width=,center”) — FIXED

- **Severity:** major
- **Surface:** Apple EPUB (and likely Kindle EPUB)
- **Location:**
  - Label(s): `fig:lec11-ga-flow` (also applicable to the Key Takeaways taxonomy figure)
  - Release crop: `notes_output/artifacts/release_checks/pdf_vs_epub_apple/compare/fig/fig_lec11-ga-flow.png`
- **What you see (symptom):** the EPUB renders literal text like `max width=,center` above the figure.
- **Likely root cause:** Pandoc doesn’t understand the `adjustbox` environment and leaks its argument into the output.
- **Fix applied (pipeline):** unwrap `\begin{adjustbox}{...}...\end{adjustbox}` before Pandoc in `epub_builder/lib/latex.py` (`unwrap_graphics_wrappers`).
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` (should be green; OCR of the crop should not find “max width”).

### [2026-02-03] Item: End-of-chapter closure kit (mastery/pitfalls/skip-ahead) + targeted reintegration — DONE

- **Severity:** polish (production value)
- **Surface:** PDF + Apple EPUB + Kindle EPUB
- **What changed (source):**
  - Added consistent `Minimum viable mastery` + `Common pitfalls` inside the existing `Key takeaways` box in all remaining chapters (keeps the required chapter template titles intact).
  - Added a short `If you are skipping ahead` paragraph inside the existing `Exercises and lab ideas` box (keeps `Where we head next` / `References` order intact).
  - Relocated Chapter 9 (SOM) `Key takeaways` to the chapter end (before exercises) so the wrap-up is actually a wrap-up.
  - Reintegrated high-value historical framing with two compact boxes:
    - `notes_output/lecture_6.tex` (CNNs): why deep learning became practical
    - `notes_output/lecture_7.tex` (RNNs): from gating to attention
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` (should be green; chapter template audit 19/19 PASS).

### [2026-02-04] Item: Swap Chapter 13/14 ordering (NLP before Transformers) — DONE

- **Severity:** major (continuity + TOC meaning)
- **Surface:** PDF + Apple EPUB + Kindle EPUB
- **What changed (source):**
  - Reordered Part II includes so `chap:nlp` (NLP applications) comes before `chap:transformers`.
  - Updated chapter bridges and reading paths so forward pointers remain forward:
    - `notes_output/lecture_1_intro.tex` (reading paths)
    - `notes_output/lecture_7.tex` / `notes_output/lecture_8_part_i.tex` / `notes_output/lecture_transformers.tex` (Where we head next)
    - `notes_output/lecture_8_part_ii.tex` and `notes_output/lecture_11.tex` (strand references)
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` (chapter audit PASS; EPUB audits + EPUBCheck OK).

### [2026-02-03] Item: Chapters not split into separate EPUB spine items — FIXED

- **Severity:** major
- **Surface:** Apple EPUB + Kindle EPUB
- **What you see (symptom):** multiple chapters were “connected” inside a single XHTML file (TOC jumped to anchors inside one file rather than opening a new chapter unit).
- **Likely root cause:** Pandoc default chunking didn’t split at our chapter heading level when `\part*{...}` is present.
- **Fix applied (pipeline):** force chunking at heading level 3 in `epub_builder/build.py` (`--split-level=3`).
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` and verify `EPUB/text/ch*.xhtml` count increases and TOC chapter links point to different `chNNN.xhtml` files.

### [2026-02-03] Item: EPUB heading hierarchy too small (headers not larger than body) — FIXED

- **Severity:** major
- **Surface:** Apple EPUB + Kindle EPUB
- **What you see (symptom):** section/chapter headings appear too close to body text size (weak hierarchy).
- **Fix applied (pipeline/CSS):** added explicit `h1..h6` sizing in `epub_builder/epub.css` (Pandoc embeds this into `EPUB/styles/stylesheet1.css`).
- **Regression check:** open the EPUB in Apple Books and verify `h3` chapter headers and `h4` section headers are visually larger than paragraphs.

### [2026-02-04] Item: TOC front matter nested under a redundant title entry; OPF missing publisher/rights/stable identifier — FIXED

- **Severity:** major (navigation + store-grade metadata)
- **Surface:** Apple EPUB + Kindle EPUB
- **What you see (symptom):**
  - The EPUB TOC nests Preface/Acknowledgments/Notation under a top-level entry that repeats the book title, making the TOC harder to scan.
  - The OPF metadata omitted `dc:publisher` / `dc:rights` and used a build-variant UUID identifier rather than the stable `book_metadata.json` identifier.
- **Fix applied (pipeline):**
  - `epub_builder/build.py`: pass `identifier`, `publisher`, and `rights` from `notes_output/book_metadata.json` to Pandoc so they appear as `dc:*` in `EPUB/content.opf`.
  - `epub_builder/lib/epub.py`: flatten the title-wrapper TOC item so Preface/Acknowledgments/Notation become top-level TOC entries.
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh`, then confirm:
  - `EPUB/nav.xhtml` starts with Preface/Acknowledgments/Notation as top-level items.
  - `EPUB/content.opf` contains `dc:identifier` equal to `book_metadata.json:identifier` and includes `dc:publisher` + `dc:rights`.

### [2026-02-03] Item: “Transformation toolkit” table caption mislabeled + table rendering risk — FIXED

- **Severity:** major
- **Surface:** Apple EPUB + Kindle EPUB
- **Location:** `notes_output/lecture_2_part_i.tex:532` (table in Chapter 2)
- **What you see (symptom):** caption starts with “Schematic:” even though it’s a table; some readers rendered the table poorly (too narrow).
- **Fix applied (source):** changed caption prefix to “Table:” in `notes_output/lecture_2_part_i.tex`.
- **Fix applied (pipeline):**
  - strip inline table/col `width:` styles in `epub_builder/lib/epub.py` so reader CSS controls responsiveness,
  - normalize any remaining table captions `Schematic:` → `Table:` in EPUB postprocess.
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh`, and verify the table appears with readable columns in Apple Books.

### [2026-02-03] Item: “Transformation toolkit” table still appears clipped in Apple Books — MITIGATED

- **Severity:** major
- **Surface:** Apple EPUB (reader-specific rendering)
- **What you see (symptom):** first column text appears clipped (“Constant actor”, “.linear …”), suggesting the table is being center-cropped rather than wrapped/scrolled.
- **Likely root cause:** Apple Books table rendering + hyphenation/centering interactions can clip wide tables instead of enabling scroll.
- **Mitigation attempt (CSS):** tried left-aligned scroll-table styling in `epub_builder/epub.css`; this made Apple Books rendering worse (letters stacked vertically).
- **Status:** deferred. Prefer a robust, reader-proof representation for this specific table (e.g., render as a figure image, or redesign as two compact bullet lists) after higher-priority editorial items.
- **Regression check:** rebuild and open the Apple EPUB; verify the left edge is visible and words don’t lose leading letters.

### [2026-02-03] Item: “Continuity thread” callouts are too explicit — FIXED

- **Severity:** major
- **Surface:** PDF + Apple EPUB + Kindle EPUB
- **What you see (symptom):** headings like “Continuity thread: …” read as meta-instructions and break narrative immersion.
- **Fix applied (source):** removed/renamed those callouts and rephrased to keep the recurring example implicit and chapter-local:
  - `notes_output/lecture_supervised.tex:38`
  - `notes_output/lecture_2_part_ii.tex:28`
  - `notes_output/lecture_3_part_ii.tex:32`
  - `notes_output/lecture_4_part_i.tex:23`
- **Regression check:** rebuild EPUBs and confirm `Continuity thread` does not appear anywhere in `EPUB/text/*.xhtml`.

### [2026-02-04] Item: Advanced editorial audit pass (chapter-by-chapter + book-level) — COMPLETE (report + next plan)

- **Severity:** major (editorial direction + future-proofing)
- **Surface:** All
- **Evidence / artifacts:** generated by `python3 notes_output/scripts/advanced_editorial_audit.py --write` (latest run wrote `notes_output/artifacts/qc/advanced_editorial_audit_20260204_183209.md`).
- **What this audit checks:** per-chapter structural metrics (heading depth, float counts, schematic-caption usage, NLP-term usage) to support narrative coherence review after rearrangements.
- **Key findings (net-new):**
  - **TOC is now correctly nested** (Parts → Chapters, Back matter contains Key Takeaways + Appendices) and front matter entries are top-level in the EPUB TOC (`EPUB/nav.xhtml`).
  - **Schematic caption overuse is no longer a global pattern:** only Chapter 14 (Transformers) retains “Schematic:” captions (3 total), which is appropriate for purely conceptual diagrams.
  - **NLP references are present and consistent** across Part II: `chap:nlp` is referenced from `chap:rnn` and `chap:transformers`, and the “strand transition” paragraph in Chapter 15 anchors the shift out of neural sequence models.
  - **Structural hotspots (watch-outs):**
    - Chapter 9 title contains a hard line break (`\\`), which renders as a `<br/>` in the EPUB TOC; consider simplifying the title to a single line for TOC cleanliness.
    - Chapters 16 and 19 are the most fragmented by heading count; if they feel “list-like” in reading, consolidate micro-headings into fewer higher-signal sections.
- **Deferred (by editorial direction):**
  - The clipped “Transformation toolkit (safe vs.\ heuristic)” table remains deferred until explicitly revisited.
  - Transformers chapter restructuring is deferred; only continuity references are maintained.
- **Next steps (proposed order, post-WP1/WP2/WP4):**
  1. **TOC cleanliness:** remove hard line breaks in chapter titles (notably Chapter 9) so EPUB TOC entries render as single lines.

## Editorial standards (structure + flow)

These standards are meant to be enforceable (by habit and by audits). When in doubt, prefer reader flow over packaging convenience.

### Chapter opening ritual

- Start with **prose first**: 2 to 4 paragraphs bridging from the previous chapter or part.
- The **first box encountered** should be `Learning Outcomes`, then `Design motif`.
- Avoid a box-dump: target **<= 2 boxes** before the first substantive subsection begins.
- Any heavier callouts (`Risk & audit`, `Notation handoff`, chapter maps, long "how to read" guides) should appear **after** the reader has met the main idea and can use the box immediately.

### Headings and linearity

- Prefer fewer, higher-signal subsections over many micro-subsections.
- Avoid subsections with < ~90 words of payload; demote to `\\paragraph{...}` or merge with the adjacent subsection.
- Avoid duplicate or near-duplicate subsection titles inside the same chapter.
- Avoid sudden tangents: detours should be labeled by placement and framing (a short bridge sentence), not by meta-instruction headings.

### Boxes (callouts)

- Boxes should be actionable at point-of-use; do not aggregate "reference" boxes at the top of a chapter.
- Do not stack multiple heavy boxes back-to-back without intervening prose (1 to 2 sentences is enough).
- Use `Risk & audit` sparingly and never as the first screen of a chapter.

### Vocabulary consistency

- Keep "roadmap" language mostly in Chapter 1 and part dividers; chapters should reference earlier material without repeating the same navigation phrasing.

## Quality snapshot (2026-02-10)

This is a structural/editorial assessment based on the latest audits plus spot-checking the chapter openings.

- **Chapter openings:** now consistent across all chapters (no chapter opens with a box; the first box is Learning Outcomes). See `notes_output/artifacts/qc/advanced_editorial_audit_20260210_082008.md`.
- **Box density:** openings now top out at two boxes; heavier callouts are pushed later into the chapter where they are actionable.
- **Navigation redundancy (remaining):** Chapter 12 still contains both a chapter-map box and an "Outline of this chapter" subsection (audit flags it as redundant). Consider keeping only one.
- **Micro-subsections (remaining):** multiple chapters contain very short subsections (<90 words), which tends to read as "outline-y" rather than narrative. The audit now lists these per chapter to drive a targeted merge/demotion pass.

  2. **Risk \& audit parity:** add a `Risk \& audit` box to Chapter 13 (NLP) to match Chapters 3/4/11 and keep the ERM+audit spine visible into embeddings/bias/deployment.
  3. **Part II coherence (plan first, then execute):** write a concrete rearrangement plan for Chapters 11–12 (CNN/RNN) that moves from “basic → deeper → deepest,” without deleting content (only relocate/merge), then implement with regression checks.
  4. **Fragmentation reduction:** review Chapters 16 and 19 for micro-heading overload; consolidate where it improves narrative flow without losing rigor.

### [2026-02-04] Item: Chapter 9 TOC title line break + Chapter 13 (NLP) Risk \& audit parity — DONE

- **Update (2026-02-05):** Chapter 9 TOC wrapping is now addressed at the source by giving the `\section` a short optional TOC title in `notes_output/lecture_5_part_i.tex` (keeps the on-page chapter title unchanged, but produces a cleaner TOC entry in PDF/EPUB).

### [2026-02-05] Item: Move “Representing Words for RNN Inputs” out of Chapter 12 into Chapter 13 (NLP) — DONE

- **Severity:** major (narrative coherence)
- **Surface:** PDF + Apple EPUB + Kindle EPUB
- **What changed (source):**
  - Removed the word-representation/embedding bridge section from `notes_output/lecture_7.tex` (RNNs) so Chapter 12 can end cleanly on sequence modeling + training dynamics.
  - Added a Chapter 13 lead-in section `Warm-up: from symbols to vectors` in `notes_output/lecture_8_part_i.tex` so embeddings/feature-geometry are introduced where they belong (before CBOW/skip-gram objectives).
  - Preserved the graded-feature word-vectorization table (allowlisted by the EPUB table audit) exactly, including its fractional entries.
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` (should remain green; Table QC should still allow exactly the one wide table).

### [2026-02-05] Item: Prevent EPUB preprocessing from corrupting TikZ line breaks (`\\[-2pt]`) as display math (`\\[...\\]`) — FIXED

- **Severity:** blocker (EPUB build failure risk + silent corruption risk)
- **Surface:** Apple EPUB + Kindle EPUB
- **What you see (symptom):** Pandoc errors like “unexpected `\\end{quote}`” caused by upstream LaTeX corruption; or malformed fragments such as `\\]-2pt]...` appearing near TikZ nodes.
- **Likely root cause:** EPUB pipeline passes that scan for display math `\\[ ... \\]` were also matching TikZ line breaks `\\\\[<len>]`.
- **Fix applied (pipeline):**
  - Added guards in `epub_builder/lib/latex.py` to skip `\\[`/`\\]` when they are part of `\\\\[<len>]` / `\\\\]` sequences, without dropping text.
  - Added the same guardrail in `notes_output/scripts/check_equations.py` so equation hygiene does not false-positive on TikZ line breaks.
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` and confirm EPUB builds + audits + EPUBCheck pass.

### [2026-02-05] Item: Reintroduce a minimal RNN sentiment use-case as a natural lead-in to embeddings — DONE

- **Severity:** polish (continuity)
- **Surface:** PDF + Apple EPUB + Kindle EPUB
- **What changed (source):**
  - Added a short worked example in the RNN wrap-up showing sentiment as a many-to-one decision (`notes_output/lecture_7.tex`, label `sec:rnn_sentiment_worked_example`).
  - Added a one-line callback in the Chapter 13 warm-up so the reader sees the same problem again, now with vector geometry (`notes_output/lecture_8_part_i.tex`).
- **Intent:** keep the example motivating without turning Chapter 12 into a second embeddings chapter.
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` (should remain green).

- **Severity:** polish (presentation + template consistency)
- **Surface:** PDF + Apple EPUB + Kindle EPUB
- **What changed (source):**
  - Chapter 9 title no longer uses an explicit `\\\\` line break (improves EPUB TOC scanability): `notes_output/lecture_5_part_i.tex`.
  - Added a `Risk \& audit` box to Chapter 13 (NLP) to match Chapters 3/4/11: `notes_output/lecture_8_part_i.tex`.
- **Regression check:** `bash notes_output/scripts/run_production_checks.sh` (chapter audit + EPUB audits must stay green).

Below is **chapter-by-chapter editorial feedback** plus **book-level guidance**. I’m basing this on the book’s stated intent and structure (preface + roadmap + chapter template), the full table of contents, and sampled passages from multiple chapters (including “Key takeaways” sections, learning outcomes, and representative technical pages).   

---

## Book-level editorial feedback

### 1) The book’s *promise* is strong — make the “unified narrative” impossible to miss

You explicitly position the book as a stand-alone, rigorous-but-readable “graduate companion” that spans **(a) modern LLM-era methods** and **(b) durable principles + alternative paradigms (optimization, probabilistic thinking, hybrid reasoning)**. 

**What to improve**

* **Lock the throughline into a single repeated sentence** that appears:

  1. end of Preface,
  2. start of Chapter 1,
  3. the opening “Design motif” box of each major part.
     Your roadmap already hints at a dependency-graph design rather than linear flow; lean into that and standardize how you “route” the reader. 
* Add a **Part structure** (even if you keep chapter numbering). Right now the ToC reads like a continuous list; the mental model becomes clearer if you group:

  * Part I: Foundations + ERM toolbox (Ch 1–4)
  * Part II: Neural networks → sequences → NLP → attention (Ch 5–14)
  * Part III: Soft computing + fuzzy reasoning (Ch 15–18)
  * Part IV: Evolutionary optimization (Ch 19)

### 2) Your recurring chapter template is a major strength — enforce it aggressively

You tell readers to use: **Learning Outcomes → Summary & Common Pitfalls → Pseudocode → Exercises**. 

**What to improve**

* Make the template **visually identical** across chapters (same order, same box styles, same “Where we head next” bridge).
* Ensure **every chapter** ends with:

  1. “Where we head next” (2–6 sentences that explicitly name the next chapter),
  2. “Dependency note” (what concepts this chapter assumed),
  3. “Minimum viable mastery” checklist (3–7 bullets).

### 3) Rearrangement watch-outs: cross-references are the first thing that break

Because you explicitly frame the roadmap as a dependency graph and give multiple reading paths , rearrangement creates failure modes:

**QA checklist after any rearrangement**

* Chapter numbers in text (“see Chapter X”) match the ToC.
* Figure numbers referenced in text match figure captions.
* “As we’ll see later” pointers actually land soon enough.
* Notation collisions (same symbol reused differently) get a “Notation note” callout (you already do this well in places). 

### 4) Notation: you’re close — now standardize the *exceptions*

The Notation & Conventions section is doing the right thing: collecting reusable conventions up front. 
You also add local “Notation notes” (e.g., σ as sigmoid vs σ² as variance). 

**What to improve**

* Create a **one-page “Notation collision index”** (Symbol → meaning by chapter). This prevents silent confusion when chapters are read out of order.
* Standardize **vector/matrix typography** (bold vs arrows, caps vs lower case) and keep it consistent in captions and pseudocode too (not just equations).

### 5) Responsible deployment + bias sections: keep them integrated, not siloed

Your NLP chapter’s bias checks and deployment checklist are excellent because they are **practical, audit-oriented, and concrete**.

**What to improve**

* Pull a **mini “risk & audit” box** (3–6 bullets) into the end of Chapters 3, 4, 11, 13—not just 14—so it doesn’t feel like a one-off ethics appendix.

---

## Chapter-by-chapter editorial feedback

### 1. About This Book

(Foundations, definitions, levels, safety, audience/prereqs, roadmap, navigation.) 

**Strengths**

* Strong operational definition of meta-cognition as bounded self-correction and auditability. 
* Clear reading-path framing. 

**Edits to prioritize**

* **Tighten definitions**: “AI”, “intelligent systems”, “intelligent machines” are conceptually adjacent—make a single comparison table that you reuse later.
* **Safety section**: end it with one concrete “design pattern” that reappears later (e.g., “monitor → detect drift → rollback”), so it feels engineered, not advisory.

**Rearrangement watch**

* This chapter is your “router.” If any later chapters move, update Figure 1 and the listed reading paths immediately. 

---

### 2. Symbolic Integration and Problem-Solving Strategies

(Transformation search; safe vs heuristic moves; backtracking; transformation trees; Risch aside.)  

**Strengths**

* The “system-level pattern” is crystal: representation → meaning-preserving moves → heuristic branching → goal test. 
* The transformation-tree framing is a strong bridge to intelligence as search. 

**Edits to prioritize**

* **Reduce “integration-tricks gravity.”** Readers may get pulled into calculus details and miss the meta-point. Make each worked integral explicitly answer:
  “What was the state? What was the action? What was the heuristic? What was the goal test?”
* Add a closing section: **“Transfer: from integrals to intelligent systems.”** Map directly to later chapters (e.g., “safe move ≈ convex step”, “heuristic branch ≈ model class choice”, “goal test ≈ validation metric”).

**Rearrangement watch**

* This chapter is unusual early in an ML sequence. Your Chapter 1 justification is good , but it will still feel “why is this here?” unless every chapter later echoes the same vocabulary (“safe vs heuristic”, “backtracking”, “residual check”).

---

### 3. Supervised Learning Foundations

(ERM pipeline; regression; likelihood → loss; GD; regularization; diagnostics; transition to classification.) 

**Strengths**

* Excellent “loss as grading rubric” framing and explicit bridge from likelihood to squared error. 
* Good forward pointer to classification metrics and calibration. 

**Edits to prioritize**

* Move **data leakage and split hygiene** into “Common Pitfalls” as a top-3 item (before overfitting even).
* Add a **single running dataset** that persists into Chapters 4–7 (even if toy). Right now, examples are good, but continuity will tighten the narrative.

**Rearrangement watch**

* If Chapter 3 moves relative to Appendix B (kernels/SVM), ensure you don’t introduce kernel ideas too late. Appendix B is currently a “hidden gem” that many readers won’t naturally discover. 

---

### 4. Classification and Logistic Regression

(Bayes optimal; generative vs discriminative; logistic; diagnostics; ROC/PR; multiclass extension.) 

**Strengths**

* Starting with Bayes optimal is the right conceptual anchor. 
* You acknowledge why it’s not used directly—good engineering realism. 

**Edits to prioritize**

* Make **thresholding and costs** explicit earlier: “probabilities are not decisions.”
* Expand “calibration” into a first-class diagnostic (since you later use it in responsible deployment). 

**Rearrangement watch**

* Ensure the notation switch y∈{0,1} vs y±1 stays consistent with any later margin-based discussions. 

---

### 5. Introduction to Neural Networks

(Neurons; perceptrons; activations; representation; learning paradigms.)

**Edits to prioritize**

* This chapter should be **conceptual and minimal**. Anything that becomes “derivation heavy” belongs in 6–7.
* Add a “Bridge to backprop” page: *what backprop computes, why it’s efficient, and what assumptions it needs*.

**Rearrangement watch**

* Watch redundancy with Chapter 11’s “deep learning” intro. Consider renaming Chapter 11 so Chapter 5 remains “the intro,” and Chapter 11 becomes “CNNs + deep training tooling.”

---

### 6. Multi-Layer Perceptrons: Challenges and Foundations

(Why depth; XOR; differentiability; setup for gradients/backprop.)

**Edits to prioritize**

* Add a **single diagram** that you reuse in Chapter 7 (same node labels). Readers build “graph memory” fast.
* Ensure vanishing/exploding gradients are *previewed* here but treated fully later (11/12). Otherwise you’ll repeat.

---

### 7. Backpropagation Learning in Multi-Layer Perceptrons

(Derivation; deltas; algorithm; numeric checks; worked case study.)

**Edits to prioritize**

* Keep one “derivation spine” and push alternative derivations into side boxes. The biggest editorial risk in backprop chapters is “too many derivations; reader loses the thread.”
* Add one explicit “finite-difference gradient check” recipe as an exercise (you already emphasize mechanical checks elsewhere—this would mirror Chapter 2’s residual check spirit). 

---

### 8. Radial Basis Function Networks

(RBF interpolation/learning; also includes adaptive filtering topics per ToC.) 

**Edits to prioritize**

* Editorially, this chapter risks feeling like **two chapters** (RBFs + filtering). Either:

  * split into 8A (RBF networks) and 8B (adaptive filtering), **or**
  * add a strong bridge: “both are linear-in-parameters once bases are fixed → least squares/Wiener view.”
* Make explicit how RBFs relate to kernels (Appendix B) so the reader sees the triangle: **RBF features ↔ kernels ↔ SVMs**. 

---

### 9. Competitive Learning and Self-Organizing Maps

(Competitive learning; SOM; topology preservation.) 

**Edits to prioritize**

* Add more **visual narrative** (before/after maps; neighborhood function effect). This topic benefits unusually well from diagrams.
* “Common Pitfalls” should include: dead units, learning-rate schedules, and interpreting the map (what it does *not* guarantee).

---

### 10. Hopfield Networks

(Associative memory; energy; convergence.) 

**Edits to prioritize**

* Emphasize the **energy lens** as a reusable concept that echoes optimization themes (and helps the book feel unified).
* Add one short “capacity vs noise” empirical lab idea.

---

### 11. Convolutional Neural Networks and Deep Training Tools

(From content, this is essentially your **CNN + deep training stability toolkit**: dropout, BN, optimizers, gradient issues.) 

**Edits to prioritize**

* **Rename for accuracy** (e.g., “Convolutional Neural Networks and Deep Training Tools”). Otherwise readers will expect a general DL intro and you’ll repeat Chapter 5.
* You already have strong training-stability content (dropout/BN).  Add a “shape & parameter counting” mini-table for CNN layers (this is the #1 pain point for new readers).

**Rearrangement watch**

* You note a chapter-specific notation collision here.  If chapters move, ensure these notes remain near first use.

---

### 12. Recurrent Neural Networks and Sequence Learning

(RNNs, BPTT, GRU/LSTM; also includes autoencoders/VAEs per ToC.) 

**Edits to prioritize**

* This is another chapter that risks becoming “too broad.” Consider splitting:

  * 12: RNNs + gated sequence models + stability
  * 12B (or 11B): Autoencoders/VAEs
* Add a single recurring sequence example (time series or text) that you reuse through BPTT → GRU/LSTM → attention preview.

---

### 13. Transformers: Attention-Based Models for Sequence Processing

(Self-attention; scaled dot-product; multi-head; positional encoding; efficient attention.) 

**Edits to prioritize**

* Add a **shape legend** (batch × length × d_model) at the start and reuse it in every attention equation. This is the biggest clarity multiplier in transformer chapters.
* Include one “masking” worked example: causal vs padding masks.

---

### 14. NLP: Applications and Language Modeling

(n-grams → embeddings → word2vec/GloVe → bias/debiasing → responsible deployment; then contextual embeddings tie-back to transformers.) 

**Strengths**

* The bias section is not hand-wavy; it gives practical evaluation and monitoring steps. 

**Edits to prioritize**

* Reorder slightly so the chapter ends with a strong modern synthesis: **static embeddings → bias → contextual embeddings/Transformers** (you already start this). 
* Add a short “what to deploy when” guide: when static embeddings are enough vs when you must fine-tune a transformer (cost/latency/stakes).

---

### 15. Introduction to Soft Computing

(Defines soft computing; fuzzy sets; why this paradigm matters.) 

**Edits to prioritize**

* Use one **running real-world example** (e.g., control rule set, decision support) that carries through Chapters 16–18.
* Make the “why now?” bridge explicit: connect back to your dual emphasis (deep/kernels vs interpretability/optimization). 

---

### 16. Fuzzy Sets and Membership Functions

### 17. Fuzzy Set Transformations Between Related Universes

### 18. Fuzzy Inference Systems

(These three should read like a *single coherent arc*.) 

**Edits to prioritize across 16–18**

* Standardize a **single inference pipeline figure** that appears in all three chapters.
* Put “Common Pitfalls” front-and-center: rules that conflict, membership scaling errors, defuzzification choices that silently change behavior.
* Add a compact “debugging checklist” for inference outputs (unit tests for rules, monotonicity checks, edge-case membership behavior).

---

### 19. Evolutionary Computing

(GA operators; fitness; constraints; multi-objective; NSGA-II; genetic programming.) 

**Edits to prioritize**

* Add a **reproducibility box**: seeds, variance across runs, reporting median + spread, and early stopping criteria.
* Ensure the bridge to earlier optimization is explicit: “when gradients are unavailable/unreliable, here’s the alternative.”

---

## Appendices (editorial positioning)

### Appendix A: Linear Systems Primer

It’s directly referenced as a support for sequence/control-oriented parts. 
**Improve discoverability**: add “See Appendix A” callouts in Chapter 10/12 wherever LTI intuition matters.

### Appendix B: Kernel Methods and SVMs

High value, but it risks being “out of sight, out of mind.” 
**Editorial fix**: in Chapters 3–4, add explicit “Kernel detour” boxes with page references into Appendix B.

### Appendix C: Using this book in ECE 657

You correctly isolate offering-specific details here. 
**Editorial note**: keep it cleanly optional; don’t let main chapters rely on it.

---

## Highest-impact next edits (if you want a punch list)

**P0 (must fix for coherence)**

1. Add Part structure + enforce chapter template everywhere. 
2. Resolve “Chapter 11 naming/role” to avoid redundancy with Chapter 5.
3. Decide whether Chapter 8 and Chapter 12 are **single chapters or split chapters** (scope control).
4. Add explicit “Where we head next” bridges at the end of *every* chapter (you already do it well in Chapter 1 → 2). 

**P1 (big quality lift)**
5) Add a one-page notation collision index (symbol → meaning by chapter). 
6) Make one running dataset/example persist across 3→4→6→7 (continuity). 
7) Add mini “risk & audit” boxes beyond the NLP/deployment chapter so safety isn’t siloed.

---

If you want, I can also produce a **redline-style checklist** you can apply mechanically during rearrangement (chapter-order QA + cross-reference QA + notation QA), but the notes above should already give you a clear, concrete editing plan.


Yep — **this version is materially stronger** and it fixes several of the coherence risks I flagged earlier.

What I’m reacting to here is the *new front matter + TOC architecture* (explicit Parts, clearer chapter naming, explicit Appendix D “Notation collision index,” and better “reading aids” framing). 

## What you improved (and why it works)

### 1) The book now reads like a designed system, not a pile of chapters

You added explicit **Part structure** (“Foundations and the ERM toolbox,” then “Neural networks, sequence modeling, and NLP,” then fuzzy, then evolutionary). That’s exactly what a reader needs to *feel progress* rather than “topic hopping.” 

### 2) You fixed the biggest earlier issue: Chapter 11’s identity

It’s now titled **“Convolutional Neural Networks and Deep Training Tools”**, which prevents redundancy with “Introduction to Neural Networks.” That’s a big clarity win: the title matches the contents. 

### 3) You added the right “glue”: Notation + reading aids + editorial heuristics

You’ve got:

* a **Notation and Conventions** section that explicitly acknowledges symbol overloads,
* “Reading Aids,” and
* an explicit promise of consistency (“edited with four recurring questions…”).
  That signals editorial discipline and reduces reader anxiety. 

### 4) You implemented the “notation collision index”

Appendix D exists and is referenced as the place where overloads are resolved. That directly addresses a common technical-book failure mode. 

---

## What still needs tightening (high-impact)

### A) Part numbering/label consistency

Status (2026-02-05): Parts are now continuous and reader-facing: NLP is folded into Part II, and later Parts are renumbered accordingly. Keep this stable unless there is a very high-value reorganization, because Part labels become “mental bookmarks” once a reader starts referencing the TOC.

### B) Scope creep inside a few chapters is still visible from the TOC
 
Two chapters look like “containers” that may become too broad:

* **NLP chapter** (embeddings + evaluation + bias/deployment + contextual models),
* **Transformers chapter** (architecture + masking + inference + deployment heuristics).
   This can still work — but only if each has a **strong internal spine** and you’re ruthless about what’s “core” vs “reference.” 
   **Fix:** Put a short **“Chapter map” box** at the start of 12 and 14:
* “Core path (must read)” vs “Detours (optional)”.

### C) Make “Key Takeaways” global, not only at the end of Part V

I see “Key Takeaways” as a standalone entry near the end of the Evolutionary section. 
If you want the *book* to feel engineered, either:

* add “Key takeaways” at the end of **every Part**, or
* rename the final one to “Book-wide takeaways” so it doesn’t feel inconsistent.

### D) Rearrangement hazard: cross-chapter bridge promises must be enforced everywhere

Your Chapter 1 intro and “roadmap” are strong, but rearrangement breaks books when:

* “see Chapter X” becomes wrong,
* figure references drift,
* notation reuse changes.
  You already have the infrastructure to prevent this (Notation notes + Appendix D). 
  **Fix (workflow, not book content):** keep a **rearrangement QA checklist** in the internal release docs (e.g., `notes_output/RELEASE_PLAYBOOK.md` / `notes_output/PRODUCTION_ROADMAP.md`) rather than in the reader-facing appendices:
* Every cross-reference validated
* Figure/table numbers regenerated
* Notation collisions rechecked
* Chapter openings: assumed prerequisites updated
  This is the practical move that separates “draft” from “publishable,” but it should live with the publishing workflow.

---

## One concrete “next edit” that will noticeably raise quality

Add a *standardized end-of-chapter closure block* (same format every time):

1. **Minimum mastery (3–7 bullets)**
2. **Common pitfalls (3–6 bullets)**
3. **Where we go next (2–5 sentences, explicit chapter name)**
4. **If you’re skipping ahead… (one paragraph: what you must know)**

Your “Reading Aids” already promises this kind of navigability — now make it real everywhere. 

---

If by “how about this” you meant something more specific (e.g., a particular chapter you just rearranged), tell me **which chapter numbers changed** and I’ll sanity-check the *narrative continuity* and *dependency logic* for that exact rearrangement.


Here’s a **hard-nosed editorial review** of *Modern Intelligent Systems: A Graduate Companion* based on the current PDF structure, the chapter scaffolding (Learning Outcomes / Design motif / Risk & audit / Pitfalls / Exercises), and representative passages across parts and appendices. 

## Book-level feedback (structure, voice, “sloppiness traps”)

**1) Your core differentiator is clear — but you sometimes under-sell it.**
The book’s organizing promise is: *“unified narrative connecting intuition → math → deployment across model families”* (Preface + Chapter 1 framing). Lean into this by enforcing a repeated *bridge paragraph* at the start of every chapter: “What question does this tool answer that the previous tool couldn’t?” You already do this in places (e.g., Ch2 ties to operational intelligence vocabulary ), but it’s not yet “ritualized” everywhere.

**2) The “ERM + audit” spine is your strongest pedagogical backbone. Don’t let later chapters drift.**
Ch3’s workflow and warnings about leakage/test peeking are excellent . Make sure every later chapter *explicitly* re-attaches to:

* what is optimized,
* what is held out,
* what failure looks like,
* what diagnostic is mandatory.
  Right now, that consistency is good in Ch4  and Ch9 , but it should be non-negotiable everywhere (especially Transformers + Evolutionary).

**3) Notation discipline is strong — but you’re still at risk of “local symbol amnesia.”**
Appendix D (“notation collision index”) is a great move . The sloppy failure mode is: a reader jumps into Ch11/Ch14 and forgets what σ meant elsewhere. You already add “Notation note” in places (e.g., Ch11) . Recommendation: enforce a **1–2 line “Notation note”** anywhere a collision is plausible, even if you think it’s obvious.

**4) Watch “schematic overload”: figures are helpful, but captions must carry the burden.**
Your List of Figures shows lots of “Schematic:” visuals. That’s fine — but schematics become fluff if they don’t state: *what decision this figure helps a practitioner make.* Some already do (ROC/PR operating point ; SOM QE/TE ). Make that a rule: every schematic caption must end with “Use this when…”

**5) The book-wide “Key Takeaways” section is useful, but it risks duplicating chapter endings.**
The back-matter Key Takeaways summary is strong , but you should prevent redundancy by making chapter-end “Key takeaways” more tactical (“minimum viable mastery + pitfalls”), while back-matter stays purely navigational (“what lives where”).

---

# Chapter-by-chapter editorial feedback (actionable, sloppiness-focused)

## Preface + Acknowledgments

* **What works:** Clear origin story and scope; good “why this book exists.”
* **Sloppiness risks:** Phrases like “as of this writing” date the book quickly — either commit to a “2026 snapshot” label or rewrite to be timeless.
* **Action:** Add a single paragraph: “What this book is *not*” (not a full DL cookbook; not a pure math text; not a survey of every architecture).

---

## Chapter 1 — About This Book

You set the operating vocabulary (representation/actions/objectives/audit) and the roadmap.

* **What works:** Strong scaffolding, exercises, and “where we head next.”
* **Sloppiness risks:**

  1. Historical sketch can become a “name parade” if not tied to the operational definition.
  2. “Levels of intelligence” can feel like opinion unless you pin it to repeated usage later.
* **Actions:**

  * End Ch1 with a **one-page “Reader contract”**: what you promise (rigor + diagnostics + deployment cautions) and what you demand (do the audits).
  * Add explicit forward pointers: “You will see this audit lens again in Ch3, Ch4, Ch9…” (you already hint at this—make it explicit and repetitive).

---

## Chapter 2 — Symbolic Integration and Problem-Solving Strategies

This chapter is a clever “small system” demonstration of representation + safe moves + heuristic branching + goal tests. 

* **What works:** Design motif (differentiate and check residual) is perfect. 
* **Sloppiness risks:** Readers may ask, “Why is this in an AI book?” if the bridge to later ML is not hammered.
* **Actions:**

  * Add a short “mapping table”: transformation tree concepts ↔ ML equivalents (search space ↔ hypothesis space; goal test ↔ validation loss; heuristics ↔ inductive bias).
  * Explicitly state: this chapter is the *template* for “intelligent behavior,” not a detour.

---

## Chapter 3 — Supervised Learning Foundations

This is the backbone: ERM, splits, learning curves, calibration, scoring rules.

* **What works:** Split hygiene + proper scoring rules + calibration monitoring are unusually well integrated for a “foundations” chapter. 
* **Sloppiness risks:**

  * “ERM/MLE/MAP” can become acronym soup if you don’t repeatedly restate the narrative: *we choose a loss because it corresponds to an assumption + a use-case.*
* **Actions:**

  * Add a micro-checklist box: “Before you trust any reported result…” (leakage, peeking, calibration, slice checks).
  * Consider tightening: keep one canonical workflow figure and refer back rather than re-explaining.

---

## Chapter 4 — Classification and Logistic Regression

Good “swap the likelihood, keep the workflow.”

* **What works:** ROC/PR operating point framing, imbalance guidance, calibration callouts.
* **Sloppiness risks:**

  * Many texts stop at AUC — you don’t, which is great — but then you must be consistent later: CNN/RNN/Transformer chapters should also remind readers “ranking ≠ calibrated probabilities.”
* **Actions:**

  * Ensure the multiclass extension promise (“softmax regression”) is either fully delivered or de-scoped; don’t leave it half-implicit.

---

## Chapter 5 — Introduction to Neural Networks (Perceptron/Adaline framing)

* **What works:** Clear contrast: perceptron hard decisions vs logistic calibrated probabilities. 
* **Sloppiness risks:** Perceptron convergence guarantees can mislead if readers forget separability assumptions.
* **Actions:**

  * Put the separability assumption in a bold “If this is false, stop” box.
  * When you mention pitfalls (feature scaling, non-separable data) , tie them back to Ch3 diagnostics: “learning curves / validation behavior will reveal this.”

---

## Chapter 6 — MLP Foundations (two-neuron to multi-layer)

* **What works (from the book-wide summary):** You frame forward/backward pass mechanics and numerical stability. 
* **Sloppiness risks:** This is where derivations can become “algebra theater” unless every block ends with: what to implement, what to cache, what breaks.
* **Actions:**

  * Add a “minimum implementable training loop” pseudocode that mirrors Ch7 later, to reduce duplication and cognitive load.

---

## Chapter 7 — Backpropagation Learning in MLPs

* **What works (from the summary):** You convert derivatives into SGD/mini-batch practice and tie to Ch3 diagnostics. 
* **Sloppiness risks:** Readers often get lost in indices; backprop is where notation sloppiness is fatal.
* **Actions:**

  * Enforce consistent symbol roles (layer index vs time index). Point readers to Appendix D whenever ambiguity is likely. 
  * Add one explicit “shape table” (dimensions of each variable) as a recurring device.

---

## Chapter 8 — Radial Basis Function Networks

* **What works:** Excellent intuition about σ controlling locality; you explicitly warn under/overfit and recommend validation selection. 
* **Sloppiness risks:** σ is overloaded across the book; you handled it with a notation note (good). 
* **Actions:**

  * Add a small “practitioner recipe” box: choose centers (k-means), sweep σ and ridge λ, evaluate with Ch3 validation curves.

---

## Chapter 9 — Self-Organizing Maps

* **What works:** QE/TE diagnostics, early stopping idea, and explicit practical pitfalls.
* **Sloppiness risks:** SOMs are easy to present as “cool maps” without honest limits; you already warn about over-interpreting single runs. 
* **Actions:**

  * Add one paragraph: when SOM is the wrong tool (task is predictive; embedding must be supervised; scaling issues dominate).

---

## Chapter 10 — Hopfield Networks

* **What works (from the summary):** Energy framing + update regime comparisons. 
* **Sloppiness risks:** Energy-based models are trendy again; readers might assume Hopfield = modern EBMs unless you delineate.
* **Actions:** Add a “Then vs now” sidebar: classical Hopfield assumptions vs modern energy-based memory / transformer-as-retrieval analogies (high level, not a detour).

---

## Chapter 11 — CNNs and Deep Training Tools

* **What works:** The vanishing/exploding gradient explanation and mitigation list is solid; includes BN, clipping, dropout. 
* **Sloppiness risks:** This chapter can become a grab bag of “training tricks.” The danger is losing the organizing lens.
* **Actions:**

  * Structure “tools” as answers to *specific failure signatures* (e.g., “loss NaNs → clipping; val gap → regularization; slow convergence → normalization/init”).
  * Keep the notation note style (you already do) whenever σ appears. 

---

## Chapter 12 — RNNs

* **What works (from the summary):** BPTT, gating, teacher forcing, and ties back to diagnostics. 
* **Sloppiness risks:** Readers confuse “sequence length” with “layers” with “time index.”
* **Actions:**

  * Add a single canonical diagram labeling: *t vs l vs n*, and reuse it in Transformers to reinforce continuity.

---

## Chapter 13 — NLP Applications + Embeddings + Bias

* **What works:** You directly address bias and provide practical checks + deployment checklist. 
* **Sloppiness risks:** Bias sections often become moralizing or vague. Yours is concrete — keep it that way. But don’t leave “Documentation.” dangling as an incomplete bullet (it appears cut off in the snippet). 
* **Actions:**

  * Make the “Responsible deployment checklist” a numbered checklist with a consistent template (Purpose, Data, Privacy, Monitoring, Documentation…) so it reads like something teams actually adopt. 
  * Ensure citations are consistent for debiasing techniques you name (Bolukbasi et al., etc.).

---

## Chapter 14 — Transformers

* **What works (from TOC):** You cover attention, positional info, masks, efficiency, fine-tuning, decoding, and a brief alignment section.
* **Sloppiness risks:** This chapter is where books go wrong by mixing *architecture explanation* with *systems lore* without clearly separating what is essential vs “2024 snapshot.”
* **Actions:**

  * Split into two explicitly labeled layers:

    1. **Core invariant** (attention, masking, residual + LN, positional encoding, decoding basics).
    2. **Snapshot / engineering notes** (efficient attention variants, LoRA, long-context tricks).
  * Make sure “Alignment (Brief)” does not read like handwaving — either cleanly scope it (“what alignment is, what it is not”) or move it to an appendix.

---

## Chapter 15 — Introduction to Soft Computing

* **What works (from TOC):** Clear separation of imprecision vs uncertainty vs fuzziness.
* **Sloppiness risks:** Soft computing chapters can feel like a second book stapled on unless you keep connecting back to “why this is still useful in 2026+.”
* **Actions:**

  * Add a short bridge: “Fuzzy logic is not probability; it is a language for graded concepts” and point to your comparison tables. (Your book already emphasizes that distinction in the tables list.)

---

## Chapter 16 — Fuzzy Sets and Membership Functions

* **What works:** Strong operator coverage + end-to-end Mamdani example is a big pedagogical win.
* **Sloppiness risks:** Readers drown in operators unless you keep pointing to “what choices matter in practice.”
* **Actions:**

  * Add “default recommendations” (which t-norm/s-norm to start with and why), then label alternatives as advanced.

---

## Chapter 17 — Transformations Between Universes (Extension principle)

* **What works:** This is the kind of chapter most books skip; it strengthens the mathematical legitimacy of fuzzy reasoning.
* **Sloppiness risks:** This is high abstraction; without consistent mini-examples, readers detach.
* **Actions:**

  * Keep one running example alive through the whole chapter (and remind what the reader should track).

---

## Chapter 18 — Fuzzy Inference Systems

* **What works:** Mamdani vs Sugeno/Takagi–Sugeno distinction is essential and timely for “hybrid systems.”
* **Sloppiness risks:** “Rule composition” can become procedural without interpretation.
* **Actions:**

  * Add a section: “How inference fails” (rule explosion, conflicting rules, membership miscalibration), with a diagnostic checklist.

---

## Chapter 19 — Evolutionary Computing

* **What works:** You treat constraints + multi-objectives as first-class and emphasize reproducibility across runs (excellent). 
* **Sloppiness risks:** GA chapters often become cookbook operator lists without principled tuning guidance.
* **Actions:**

  * Enforce one unifying concept: **exploration vs exploitation** and tie every operator choice back to it. Your takeaways already gesture at this — amplify it. 
  * Add a “reporting standard” box (seeds, distributions, multiple runs) — you already imply it; make it formal. 

---

# Appendices (A–D) + Back Matter

## Appendix C — Course Logistics

Good that you moved offering-specific details out of the main flow. 

* **Editorial action:** Add a bold line early in the book: “Appendix C is ignorable unless you’re in ECE 657.”

## Appendix D — Notation collision index

This is a legit quality marker. 

* **Editorial action:** Reference it more aggressively in-chapter (“If you’re reading out of order, see Appendix D”).

## Back matter — Key Takeaways

The condensed map is strong and helps navigation. 

* **Editorial action:** Ensure each chapter’s own closing section doesn’t clone these.

---

## The highest-impact “anti-sloppiness” upgrades (if you do only 5 things)

1. Add a **chapter-opening bridge paragraph** everywhere: “What problem this solves that the prior chapter didn’t.”
2. Enforce a **universal audit checklist**: objective → split hygiene → metric → calibration → slice tests.
3. Make **notation notes mandatory** at first collision risk; point to Appendix D. 
4. Make every schematic caption end with **“Use this when…”** (decision-oriented visuals).
5. Split Transformers into **Invariant Core vs Snapshot Notes** to prevent rapid dating.

If you want, I can also produce a **one-page “Book Consistency Rubric”** you (or an editor) can apply chapter-by-chapter to mechanically detect drift, redundancy, and missing bridges—so the rearrangement doesn’t reintroduce sloppiness.


Editorial Recommendations & Rating

Modern Intelligent Systems: A Graduate Companion (First edition, 2026)

Date: February 05, 2026
Prepared for: Haitham Amar

Scope and how to read this document
This file consolidates the recommendations I provided in-chat into a single, client-ready set of actions. It focuses on editorial cohesion, technical clarity, and reader experience—especially the kinds of issues that create a perception of sloppiness (notation drift, redundancy, weak transitions, inconsistent structure, and time-stamped/stale sections).
Note: The assessment is based on the book-level framing (Preface, Chapter 1 guidance), chapter structure signals (Learning Outcomes / Design motif / Risk & audit / Key takeaways), and the visible chapter/appendix organization. If you want a full line-edit, treat this as the blueprint for that pass.
Current rating (as-is)
Graduate companion / course-adjacent technical book: 7.8 / 10
Standalone commercial book for a broad market: 6.9 / 10
The book is publishable and intellectually substantial. Your recent changes materially improved cohesion and stand-alone readability. The remaining gap to an 8.5–9/10 is mostly editorial discipline (consistency and pruning), not missing technical content.
What you improved relative to prior feedback (keep)
•	Stronger “book contract”: the Preface now explicitly frames a unified narrative and added connective tissue so it reads as a book, not just notes.
•	Clear reading paths and navigation guidance (roadmaps, who-should-read-what scaffolding).
•	More consistent pedagogy: repeated structural elements (learning outcomes, design motif, risk & audit, exercises, key takeaways).
•	Course logistics moved out of the core into Appendix C, reducing “course-note bleed” for general readers.
•	Notation discipline strengthened with a dedicated notation collision index (Appendix D).
•	Part IV improved with explicit multi-objective optimization coverage and reproducibility posture.
Top priority fixes (highest ROI, minimal rewrite)
Remove/contain staleness signals
•	Any section labeled as a dated “snapshot” should be framed as historical context, moved to a boxed aside, or updated to the edition year.
Enforce chapter-level structure everywhere
•	Every chapter should consistently begin with context + prerequisites + outcomes, and end with summary + pitfalls + exercises/lab ideas + next steps.
Kill redundancy across Part II (RNNs / embeddings / NLP)
•	Keep embeddings primarily in Chapter 13; keep Chapter 12 focused on recurrent computation and training pathologies; keep Chapter 14 focused on attention and modern sequence modeling.
Global notation and cross-reference sweep
•	After rearrangements, ensure symbols, equation references, and section references are correct and stable across the whole PDF.
Typography/export hygiene
•	Eliminate any visible encoding/hyphenation artifacts introduced by PDF export; these are small but disproportionately damage perceived quality.
Chapter-by-chapter recommendations
Chapter 1: About This Book
What works
•	Strong operational framing for “intelligence” and auditability; good place to set reader expectations.
Where sloppiness will bite
•	Risk: taxonomy becomes decorative unless visibly reused later; risk of over-long meta discussion.
Recommended edits
•	Add a one-page “reader contract” (what is required vs optional).
•	Add a simple table mapping Parts/chapters to the book taxonomy/levels, and refer back to it later.
Chapter 2: Symbolic Integration and Problem-Solving Strategies
What works
•	Clear learning outcomes around safe vs heuristic transformations; strong “check by differentiating” motif.
Where sloppiness will bite
•	Risk: reads like a calculus detour if the “search/transform” framing is not explicit enough.
Recommended edits
•	Add a boxed bridge: transformation trees as search (state/action/goal test).
•	Include one non-integral transformation example (e.g., algebraic simplification or rewrite rules) to generalize the lesson.
Chapter 3: Supervised Learning Foundations
What works
•	Excellent ‘Data → model → objective → audit’ mindset; solid guardrails against leakage and test peeking.
Where sloppiness will bite
•	Risk: notation and evaluation concepts introduced here must be reused later or they feel forgotten.
Recommended edits
•	Add a concise end-of-chapter notation snapshot and an “audit checklist” that later chapters can reference.
Chapter 4: Classification and Logistic Regression
What works
•	Good risk/audit posture (thresholding, imbalance, calibration); strong practical orientation.
Where sloppiness will bite
•	Risk: mixing theory and deployment guidance can feel messy unless formatting is consistent.
Recommended edits
•	Standardize the chapter’s “audit boxes” as a template for later deep learning chapters.
Chapter 5: Introduction to Neural Networks
What works
•	Clean pivot from linear models to nonlinear representation; sets up MLP depth reasoning.
Where sloppiness will bite
•	Risk: can become history/overview without serving the backprop chapters.
Recommended edits
•	Introduce a running toy example that persists through Chapters 5–7 to ground abstractions.
Chapter 6: Multi-Layer Perceptrons: Challenges and Foundations
What works
•	Good place to explain why multilayer learning is nontrivial and what breaks naïve approaches.
Where sloppiness will bite
•	Risk: notation soup; derivations without interpretation anchors.
Recommended edits
•	Add a derivation map and consistent shape annotations near equations.
Chapter 7: Backpropagation Learning in Multi-Layer Perceptrons
What works
•	Correctly isolated as its own chapter; essential for the book’s credibility.
Where sloppiness will bite
•	Risk: scalar/vector/index notation switching; silent shape assumptions.
Recommended edits
•	Add forward/backward pseudocode and a single canonical notation scheme; reference it later instead of re-deriving.
Chapter 8: Radial Basis Function Networks (RBFNs)
What works
•	Good bridge to kernels and function approximation.
Where sloppiness will bite
•	Risk: readers may not know when to prefer RBFN vs kernel methods.
Recommended edits
•	Add a decision checklist (data size, interpretability, training cost, approximation needs).
Chapter 9: Competitive Learning and Clustering
What works
•	Nice transition into self-organization and unsupervised thinking.
Where sloppiness will bite
•	Risk: becomes an algorithm catalog without a strong organizing principle.
Recommended edits
•	Add a ‘design motif’ similar to Chapter 3 (representation + neighborhood + distortion objective + stability).
Chapter 10: Hopfield Networks
What works
•	Good energy/minima intuition; useful conceptual bridge to energy-based thinking.
Where sloppiness will bite
•	Risk: feels like a historical detour.
Recommended edits
•	Add a short “why it still matters” section (associative memory, attractors, energy formulations reappearing).
Chapter 11: Convolutional Neural Networks and Deep Training Tools
What works
•	Right placement before sequence models; useful to combine architecture and training pathology.
Where sloppiness will bite
•	Risk: two chapters stapled together.
Recommended edits
•	Split internally as 11A (CNN mechanics) and 11B (deep training pathologies), and cross-link to Chapter 3 audit tools.
Chapter 12: Introduction to Recurrent Neural Networks
What works
•	Correctly introduces state and recurrence for sequences.
Where sloppiness will bite
•	Risk: redundancy with Chapter 13 if embeddings and representation learning are repeated here.
Recommended edits
•	Keep embeddings mostly in Chapter 13; make Chapter 12 end with a clear handoff to representation learning.
Chapter 13: Neural Network Applications in Natural Language Processing
What works
•	Good place to centralize embeddings, NLP evaluation, and responsible deployment checklists.
Where sloppiness will bite
•	Risk: section content can age quickly unless you distinguish timeless principles from time-sensitive architectures.
Recommended edits
•	Label sections as ‘timeless’ vs ‘snapshot’, and ensure embedding content is not duplicated in Chapter 12.
Chapter 14: Transformers: Attention-Based Sequence Modeling
What works
•	Modern and relevant coverage; critical for the book’s current-market credibility.
Where sloppiness will bite
•	Risk: dated snapshot notes can read as staleness; alignment sections can feel like placeholders if too brief.
Recommended edits
•	Move dated material into boxed ‘as-of’ sections or update to edition year; define what ‘alignment’ means in this book and bound it to one clear page.
Chapter 15: Introduction to Soft Computing
What works
•	Good conceptual pivot to fuzzy and evolutionary methods.
Where sloppiness will bite
•	Risk: feels like a new book starting.
Recommended edits
•	Add a one-page map that ties Part III and IV back to the ‘representation/objective/audit’ contract from Part I.
Chapter 16: Fuzzy Sets and Membership Functions
What works
•	Thorough foundation; good operator tables and Mamdani example potential.
Where sloppiness will bite
•	Risk: operator/notation drift across fuzzy chapters.
Recommended edits
•	Standardize operator choices and explicitly link them to qualitative behavior (conservatism vs permissiveness).
Chapter 17: Fuzzy Set Transformations / Extension Principle
What works
•	Strong engineering treatment (discretization, computational guidance).
Where sloppiness will bite
•	Risk: rules of thumb can feel like unsourced lore.
Recommended edits
•	Label heuristics as heuristics and add 1–2 canonical citations; add a ‘when to use alpha-cuts’ decision box.
Chapter 18: Fuzzy Inference Systems
What works
•	Core pipeline chapter for real implementations.
Where sloppiness will bite
•	Risk: too descriptive without a procedural algorithm readers can implement.
Recommended edits
•	Add a one-page stepwise algorithm (fuzzify → rules → aggregate → defuzzify → validate) and a failure-mode audit.
Chapter 19: Introduction to Evolutionary Computing
What works
•	Strong reproducibility posture; multi-objective coverage is valuable.
Where sloppiness will bite
•	Risk: stochastic methods can become hand-wavy if reporting discipline is not enforced.
Recommended edits
•	Add a reproducibility template: budgets, seeds, stopping, variance reporting, constraints, and baselines.
Recommended pricing posture (as-is)
If you publish without further changes, price to match ‘strong graduate companion’ rather than ‘premium textbook.’ A mid-range price avoids triggering expectations of a fully copyedited, professionally typeset, publisher-grade textbook.
Suggested as-is price anchors:
•	Paperback: $49.99 USD
•	eBook: $19.99 USD
•	Hardcover (optional): $79.99 USD
Next-step options
•	Option A (fast): Apply the top-priority fixes only (Part II redundancy + snapshot framing + structure sweep + export hygiene).
•	Option B (best ROI): Do Option A + a targeted line-edit of Chapters 1, 3, 4, 14, and 19 (these drive first impressions and adoption).
•	Option C (textbook-ready): Full consistency pass + professional copyedit + standardized figures/tables + instructor resources.

## Caption Style Guide (Canonical, Short)

Use these rules for all future caption edits so style stays consistent across PDF and EPUB.

1. Start with the artifact type and purpose:
   - Figures: describe what is shown and the decision/interpretation it supports.
   - Tables: describe what is summarized/compared (never prefix table captions with `Schematic:`).
2. Keep structure compact: context sentence(s) + one practical usage sentence.
3. Use one closing action cue only: `Use it when ...`
4. Keep wording concrete and non-promotional; avoid filler adjectives.
5. Preserve technical fidelity:
   - Do not change labels, equation references, symbols, or units in a wording pass.
   - Keep cross-references (`\\Cref{...}`) intact.
6. Prefer short, plain wording over long clause chains:
   - Use semicolons sparingly.
   - Split overloaded captions into two clean sentences when possible.
7. Target consistency:
   - similar figure families should have similar caption rhythm,
   - but avoid copy-paste repetition across chapters.

Quick lint checklist before merge:
- No `Use this when ...` remains (use `Use it when ...`).
- No table caption starts with `Schematic:`.
- No caption text implies a structural/content move in a wording-only pass.

## [2026-02-10] Book-wide tightening pass (points 2-8, minimal-change execution)

### Scope executed
- Added derivation-to-implementation closure boxes in Chapters 6, 7, and 11 to make each chapter end with the same practical loop: implement equations, cache intermediates, and fail-fast diagnostics.
- Standardized notation handoff cues across Chapters 6, 7, 11, 13, and 16-19, each explicitly pointing to Appendix D (`\Cref{app:notation_collisions}`).
- Strengthened risk/audit framing in Chapters 18 and 19, while preserving existing strong risk boxes in Chapters 3, 4, 11, and 13.
- Added a dedicated reproducibility appendix (Appendix E) and cross-linked it from supervised, deep-learning, and evolutionary chapters.

### Files changed in this pass
- `notes_output/lecture_3_part_ii.tex`
- `notes_output/lecture_4_part_i.tex`
- `notes_output/lecture_6.tex`
- `notes_output/lecture_7.tex`
- `notes_output/lecture_8_part_i.tex`
- `notes_output/lecture_9.tex`
- `notes_output/lecture_10_part_i.tex`
- `notes_output/lecture_10_part_ii.tex`
- `notes_output/lecture_11.tex`
- `notes_output/lecture_supervised.tex`
- `notes_output/book_appendices.tex`
- `notes_output/appendix_reproducibility_standards.tex` (new)

### Why this was minimal-change
- No chapter reordering or section movement.
- No major equation rewrites or figure/table structural edits.
- Changes are additive framing and cross-link normalization around existing content.

### Proposed next micro-pass (optional, wording-only)
1. Harmonize opening bridge sentence length in Chapters 15-19 (target 2-3 lines each).
2. Tighten any repeated “roadmap” phrasing in adjacent chapters.
3. Run one final chapter-format + production-check bundle before tagging a release candidate.

## [2026-02-10] Chapter-opening flow pass (box-heavy openings; Chapter 11 training box)

### Editorial intent
- Start chapters with a narrative bridge (no boxes).
- Keep `Learning Outcomes` as the first *box* the reader encounters.
- Avoid front-loading multiple heavy boxes (risk/audit, long maps, numeric sidebars).
- Place boxes where they are actionable (near the section that uses them), rather than aggregating them at the top.
- No deletions: content is preserved via reordering and relocation.

### What changed (high-level)
- Moved early non-essential boxes out of chapter openings for Chapters 2-4 and 6-12.
- Converted some early boxes that were purely navigational into regular prose (e.g., Chapter 11 "How to read this chapter") to reduce box density.
- Repositioned Chapter 11's "Training failure signatures (symptom -> likely fixes)" box to appear after the reader has seen the vanishing/exploding gradient mechanics.

### Measurable before/after
- Evidence: `notes_output/artifacts/qc/advanced_editorial_audit_20260209_225702.md` (before) vs `notes_output/artifacts/qc/advanced_editorial_audit_20260209_231834.md` (after).
- After this pass, the only chapters with >2 opening boxes are:
  - Chapter 14 (`lecture_transformers.tex`) (intentionally deferred; likely rewritten)
  - Chapters 15-18 (each includes a single "Running example checkpoint" box alongside Learning Outcomes + Design motif)

### Notes (residual)
- This pass improves the chapter-opening reading rhythm, but it does not address deeper structural questions (section ordering, redundancy, level of detail) within each chapter.
- The next editorial work should separate "structure" (moving sections) from "wording-only" polishing to avoid mixing scopes.

## [2026-02-10] Chapter 11 restructure (CNN) for pedagogical order

### Goals
- Reduce outline-fragmentation from micro-subsections while keeping all content.
- Keep the opening narrative-first (no immediate box dump) and delay boxes until they are actionable.
- Remove duplicated ``Historical context'' scaffolding and make the chapter read as one linear arc: pain point -> inductive bias -> mechanics -> depth context -> training toolkit.

### Changes made
- Chapter 11 (`notes_output/lecture_6.tex`):
  - Renamed the early scaffold subsection to `Motivation and map`.
  - Moved `Learning Outcomes` to occur after the map and before the first technical subsection (still early, but not the first thing the reader sees).
  - Repositioned the `Design motif` box to follow the dense-layer failure analysis (so it lands after the motivating pain point).
  - Moved the ``convolution vs. cross-correlation'' note into the convolution mechanics section (no longer adjacent to pooling notes).
  - Demoted three micro-subsections into `\paragraph{...}` blocks with preserved labels:
    - `sec:cnn_convolutional_hyperparameters_what_you_choose_up_front`
    - `sec:cnn_from_feature_maps_to_classifiers`
    - `sec:cnn_multi_branch_convolution_blocks_inception_idea`
  - Renamed the 2012 historical block to `Why deep learning became practical (2012)` (label preserved).
  - Moved `Risk & audit` later so it no longer interrupts the ``2012 -> training'' transition.
  - Demoted `Deep Network Optimization Challenges` into a paragraph (label preserved), immediately upstream of the vanishing/exploding gradients section.

### Validation (must stay green)
- Production gate: `bash notes_output/scripts/run_production_checks.sh` (green after restructure).
- Audits:
  - `notes_output/artifacts/qc/chapter_format_audit_20260210_090215.md`
  - `notes_output/artifacts/qc/advanced_editorial_audit_20260210_091310.md`

## [2026-02-10] Visual editorial inspection (full-page pass, Chapters 11-13)

### Method
- Generated full-page screenshots directly from the current print PDF:
  - Chapter 11 pages 222-240 -> `notes_output/artifacts/editorial_visual/ch11/`
  - Chapter 12 pages 241-263 -> `notes_output/artifacts/editorial_visual/ch12/`
  - Chapter 13 pages 264-289 -> `notes_output/artifacts/editorial_visual/ch13/`
- Read each page as a reader (not a regex pass), looking for:
  - narrative flow breaks,
  - heading rhythm and section granularity,
  - box clustering and attention disruption,
  - figure/table placement and local context,
  - transition quality between concepts.

### Chapter 11 (CNN) - visual findings
- **Improved:** The chapter now reads in a mostly linear order (motivation -> mechanics -> training stability), with fewer abrupt micro-section jumps.
- **Issue (medium):** The opening still starts with a carry-over block from Chapter 10 (page 222), then chapter start on same page. This weakens the visual "new chapter" reset.
- **Issue (medium):** Pages 237-239 are box-dense (`Practical optimizer notes`, pseudocode, derivation closure) and can feel like checklist stacking.
- **Issue (low):** `Training Neural Networks: Gradient-Based Optimization` remains generic and visually similar to prior chapters; it can be trimmed/reframed as a brief bridge rather than a full subsection.
- **Issue (low):** Page 239 ends with a single box and large whitespace; acceptable in print, but weak as a reading beat.

### Chapter 12 (RNN) - visual findings
- **Issue (high):** Heading flow is still fragmented by utility blocks (`Chapter map`, `Simple RNN at a glance`, `Optional reminders`, code boxes) before the core derivation is fully established (pages 243-247).
- **Issue (high):** Section `12.4 Outline of this chapter` appears late (page 245), after substantial technical content; this is backward pedagogically.
- **Issue (medium):** Several short "note-like" boxes in sequence (pages 249, 255, 258) create scanning fatigue; some should be merged or demoted to paragraphs.
- **Issue (medium):** RNN-to-attention bridge is present but visually buried (pages 258-259). It should be elevated as an explicit transition subsection heading.
- **Issue (low):** Some pages feel text-heavy without cadence breaks (e.g., pages 252, 254, 260), where one strategic figure/callout anchor would improve pacing.

### Chapter 13 (NLP embeddings) - visual findings
- **Issue (high):** Concept order still oscillates between introductory and detailed derivations:
  - broad framework statements appear, then deep CBOW math, then higher-level framing returns.
  - this is readable, but visually signals "looping back" rather than "progressing forward."
- **Issue (high):** Duplicate-density feel in the middle (pages 270-276): many closely related objective equations/subsections with minimal visual hierarchy changes.
- **Issue (medium):** The chapter carries both strategic framing and implementation detail well, but transition markers between these modes are not visually strong enough.
- **Issue (medium):** Bias/deployment section (pages 285-288) is valuable but arrives as a sharp style shift; benefits from a short bridge sentence that closes the math arc before governance arc starts.
- **Issue (low):** End section (`13.18 Contextual embeddings and transformers`) is concise and useful, but currently feels like an appendix stub; should either be expanded slightly or explicitly labeled as a forward pointer.

### Cross-chapter reader experience (11 -> 12 -> 13)
- **Strength:** The macro progression (vision architecture -> sequence dynamics -> representation geometry) is coherent.
- **Primary gap:** Section granularity and box cadence are still inconsistent between Chapters 12 and 13.
- **Primary risk:** Too many "utility" boxes near local intros can dilute the core storyline and reduce momentum.

### Recommended next editorial pass (visual-first, minimal movement)
1. **Chapter 12 flow normalization**
   - Move/demote `Outline of this chapter` so it appears before technical derivations (or remove as a heading and integrate into intro prose).
   - Merge adjacent utility boxes where possible into one "Implementation checklist" block.
   - Promote a clear `From RNN limits to attention` transition heading.
2. **Chapter 13 narrative linearization**
   - Group the CBOW/skip-gram objective sequence into one contiguous derivation run with fewer heading level changes.
   - Add one short bridge before bias/deployment to signal "from geometry to governance."
   - Keep technical content intact; only adjust heading/bridge prose to reduce perceived repetition.
3. **Chapter boundary polish**
   - Enforce a stronger chapter-start reset so new chapters do not visually start beneath prior chapter closeout material.

### Quality assessment after this visual pass
- Chapter 11: **8.8/10** (strongly improved order; minor pacing/box density issues remain).
- Chapter 12: **7.9/10** (content quality high, but ordering and box rhythm still feel instructional rather than book-like).
- Chapter 13: **8.1/10** (valuable coverage, but mid-chapter derivation flow can be made more monotonic and reader-forward).

## [2026-02-10] Implemented pass: visual-first, minimal movement (Ch. 12 + Ch. 13)

### Scope executed (single edit batch)
- **Chapter 12 (`lecture_7.tex`)**
  - Replaced early map box with concise prose (`Chapter flow`) to reduce box-heavy opening.
  - Removed late `Outline of this chapter` subsection and integrated flow as a short roadmap paragraph near the opening.
  - Merged stability notes into one box (`Stability defaults in practice`) and merged implementation boxes into one (`Implementation checklist: masks, clipping, pitfalls`).
  - Promoted an explicit transition heading: `From recurrent state to attention`.
  - Moved optional reminders/coding utility material later so derivation arc is less interrupted.
- **Chapter 13 (`lecture_8_part_i.tex`)**
  - Reframed derivation arc heading to `From lookup to objective: compact derivation path`.
  - Demoted micro-subsections to paragraph heads where they were creating heading churn:
    - `Neural network architecture for word embeddings`
    - `Context window and sequential input`
    - `Interpretation of the weight matrix W`
  - Removed low-value empty heading (`Interpretation and Remarks`).
  - Added an explicit bridge from math/geometry to governance/bias sections.

### Guardrails honored
- No content movement across chapters.
- No objective/formula deletions in the derivation core.
- Kept labels where practical; no cross-reference regressions observed in gate checks.

### Validation snapshot
- Ran: `bash notes_output/scripts/run_production_checks.sh`
- Result: green release checks + EPUB audits + EPUBCheck pass.
- Key artifacts refreshed:
  - `notes_output/artifacts/qc/chapter_format_audit_20260210_104148.md`
  - `notes_output/artifacts/release_checks/report.txt`
  - `notes_output/artifacts/release_checks/epub_layout_audit_1000w.md`
  - `notes_output/artifacts/release_checks/epub_table_audit.md`
  - `notes_output/artifacts/release_checks/epub_image_quality.md`

## [2026-02-10] Chapter 11 continuity fix: remove 2012 non-sequitur block

### Editorial intent
- Eliminate the stand-alone subsection `Why deep learning became practical (2012)` that interrupted the CNN mechanics arc.
- Keep the historical signal, but only as one integrated sentence in the architecture-to-training transition.

### Change applied
- File: `notes_output/lecture_6.tex`
  - Removed the subsection + historical tcolorbox + SVM refresher detour.
  - Updated the chapter map bullet (`Going deeper`) to remove explicit "2012 shift" framing.
  - Added one concise bridging sentence after multi-branch discussion: data + GPU maturity made CNN architectural priors decisive at scale.

### Validation
- Re-ran `bash notes_output/scripts/run_production_checks.sh`.
- Gate status: green (chapter format pass, equation hygiene pass, image/table/layout audits pass, EPUBCheck pass).

## [2026-02-10] Release-blocker gate implementation (P0 policy pass)

### What was implemented
- Added a strict TeX warning gate:
  - `notes_output/scripts/check_build_warnings.py`
  - Fails on undefined references/citations summaries, undefined cite/ref lines, pdfTeX/driver warnings, and overfull hbox above threshold (`--max-overfull-pt`, default `3.0`).
  - Writes: `notes_output/artifacts/qc/build_warning_gate.md`.
- Added figure/table coverage audit:
  - `notes_output/scripts/check_ref_coverage.py`
  - Fails when any `fig:` / `tab:` label has zero references.
  - Optional strict-order mode (`--strict-order`) also checks before/after references inside the same file.
  - Writes: `notes_output/artifacts/qc/ref_coverage_report.md`.
- Added bibliography style policy audit:
  - `notes_output/scripts/check_bib_style.py`
  - Enforces required fields for `article` / `inproceedings` / `book`; validates DOI/arXiv metadata consistency.
  - Writes: `notes_output/artifacts/qc/bib_style_report.md`.
- Wired the three audits into:
  - `notes_output/scripts/run_editorial_qc.sh`
  - Draft bypass flags:
    - `ALLOW_TEX_WARNINGS=1`
    - `ALLOW_REF_COVERAGE_GAPS=1`
    - `STRICT_REF_ORDER=1` (optional stronger mode)
    - `MAX_OVERFULL_PT=<float>` (threshold override)

### Current results against P0
- `check_build_warnings.py`: **PASS**
- `check_bib_style.py`: **PASS with warnings** (`93` warnings; no hard errors)
- `check_ref_coverage.py` (blocking mode): **FAIL**
  - Labels scanned: `83`
  - Unreferenced labels: `32`
  - Report: `notes_output/artifacts/qc/ref_coverage_report.md`
  - Representative unreferenced labels:
    - `fig:lec1_splits`
    - `fig:lec2_sigmoid_bce`
    - `fig:lec6-dropout`
    - `fig:lec7-rnn-unrolled`
    - `fig:lec13-masks`
    - `tab:word_feature_vectorization`
    - `tab:ga-toy`
    - `tab:fuzzy-operators`

### Interpretation
- The new gate correctly surfaced a real release risk: a non-trivial set of figures/tables are currently not referenced in body prose.
- The bibliography is structurally valid, but style normalization is still pending (warnings list captured for batch cleanup).

### Next closeout actions
1. Fix all `32` unreferenced `fig:/tab:` labels (minimal prose insertions near first mention points).
2. Re-run `bash notes_output/scripts/run_editorial_qc.sh` with blocker mode (no bypass flags).
3. Triage `bib_style_report.md` warnings into one normalization pass.

## [2026-02-10] Strict-order closure pass (minimal prose, no structural movement)

### Scope
- Applied one-line strict-order closure references for all labels flagged in:
  - `notes_output/artifacts/qc/ref_coverage_report_strict.md`
- Rule used:
  - Add a minimal post-appearance sentence after each flagged figure/table environment.
  - If strict mode still lacked a pre-appearance mention, add one minimal pre-sentence immediately before the same environment.
- No section reorder, no content relocation, no formula edits.

### Verification
- `python3 notes_output/scripts/check_ref_coverage.py --root notes_output --strict-order` -> **PASS**
- `STRICT_REF_ORDER=1 bash notes_output/scripts/run_editorial_qc.sh` -> **PASS**
- `python3 notes_output/scripts/check_crossrefs.py` -> **PASS**

### Artifacts
- `notes_output/artifacts/qc/ref_coverage_report_strict.md`
- `notes_output/artifacts/qc/publish_qc_report.md`
- `notes_output/artifacts/qc/chapter_format_audit_20260210_161156.md`

### Remaining non-blocker
- Bibliography style audit remains warning-only (`93` warnings):
  - `notes_output/artifacts/qc/bib_style_report.md`

## [2026-02-10] Dedicated camera-ready typography + references consistency sweep

### Scope
- Normalized chapter-end `References.` wording to one policy sentence across chapter files.
- Repaired the remaining outlier in `lecture_4_part_i.tex` so `\nocite{...}` precedes the shared `References.` paragraph.
- Ran a safe punctuation pass over plain-prose lines only (lines without LaTeX command markers), targeting:
  - spaces before commas,
  - missing spaces after commas,
  - joined digit-word forms like `1to` -> `1 to`.
- Confirmed no mixed manual/auto reference prefixes (`Figure \Cref`, `Table \Cref`, etc.) and no `Figure Figure` artifacts in source.

### Validation
- Ran strict gate:
  - `cd notes_output && STRICT_REF_ORDER=1 ./scripts/run_editorial_qc.sh`
- Result: **PASS** on chapter format, equations, strict reference order, and publish QC report generation.
- Bibliography style remains warning-only (`93` warnings), unchanged from prior state.

### Artifacts
- `notes_output/artifacts/qc/chapter_format_audit_20260210_180937.md`
- `notes_output/artifacts/qc/publish_qc_report.md`
- `notes_output/artifacts/qc/bib_style_report.md`

## [2026-02-10] Chapter-end references policy decision (book-wide)

### Decision
- Adopted **remove** as the chapter-end references policy for all chapters:
  - Removed repeated `\paragraph{References.}` text from chapter tails.
  - Kept bibliography centralized in the global references section.

### Contract updates
- Updated chapter-kit policy in `ONBOARDING.md` to remove chapter-end references paragraph from the required kit.
- Updated `scripts/chapter_format_audit.py` to stop enforcing a `References.` paragraph near chapter end.

### Validation
- `cd notes_output && STRICT_REF_ORDER=1 ./scripts/run_editorial_qc.sh` -> **PASS**
- Chapter format audit: `notes_output/artifacts/qc/chapter_format_audit_20260210_182429.md`

## [2026-02-11] Print-production 7-check pass (mechanical gate)

### Run context
- Timestamp: `2026-02-11 10:04:11 EST`
- PDF audited: `notes_output/ece657_notes.pdf` (`448` pages, `7 x 10 in`)
- Primary command: `bash notes_output/scripts/run_production_checks.sh` (completed)

### Check 1: Trim size, margins, gutter
- **PASS (with caution for long spine)**.
- Source settings:
  - `notes_output/ece657_notes.tex:1` -> `\documentclass[11pt,twoside]{article}`
  - `notes_output/ece657_notes.tex:4-9` -> `paperwidth=7in`, `paperheight=10in`, `inner=1in`, `outer=0.75in`, `top=0.75in`, `bottom=0.8in`
- For a `448`-page print run, inner margin is acceptable but should be printer-validated against exact binding/gutter requirements.

### Check 2: Font size and readability
- **PASS (body/caption), WATCH (plot micro-text)**.
- Evidence:
  - Body: `11pt` (`notes_output/ece657_notes.tex:1`)
  - Captions: `\usepackage[font=small,labelfont=bf]{caption}` (`notes_output/ece657_notes.tex:42`)
  - Plot ticks/legends: `\scriptsize` in global pgfplots style (`notes_output/ece657_notes.tex:110-113`)
- Recommendation: keep current body/caption sizes; monitor dense plot pages in physical proof.

### Check 3: Figure resolution/vector quality
- **PASS**.
- `pdfimages -list notes_output/ece657_notes.pdf` reported no embedded raster images (`images=0`), indicating vector-first figure output in current PDF.

### Check 4: Contrast and grayscale survivability
- **WARN**.
- Evidence:
  - Color-explicit captions still exist (for example: `notes_output/lecture_7.tex:415`, `notes_output/lecture_11.tex:1136`, `notes_output/lecture_4_part_i.tex:813`).
  - Light-gray usage present down to `gray!3` (`gray_refs=140`, `min_pct=3`, `lt8pct=11`).
- Interpretation: print on non-premium paper can weaken low-contrast fills and color-only distinctions.

### Check 5: Line weights / hairlines
- **WARN**.
- Evidence from source audit:
  - `line width` range: `0.35pt` to `1.40pt` (`58` explicit width settings).
  - `<0.5pt`: `4` occurrences (mostly marker outlines), `<0.7pt`: `9` occurrences.
- Recommendation: increase sub-0.5pt strokes to >=0.5pt on plot markers and fine diagram edges for safer print reproduction.

### Check 6: Black/gray consistency
- **WARN**.
- Global defaults are consistent, but multiple very light grays appear (including `gray!3` and `gray!5` fills).
- Recommendation: in print profile, normalize ultra-light backgrounds and gridlines to a slightly darker floor where readability is critical.

### Check 7: Fonts embedded + print profile
- **PARTIAL PASS**.
- `pdffonts` shows all listed fonts embedded (`emb=yes`).
- PDF metadata:
  - `Tagged: no` (from `pdfinfo`)
  - No detected PDF/X marker string (`GTS_PDFXVersion` not found in string scan).
- Tooling note: `qpdf` and `exiftool` are not installed in this environment, so deeper profile checks were limited.
- Conclusion: embedding is good; explicit PDF/X conformance is not yet established.

### Gate summary
- Pass: 3 (`trim/layout`, `font baseline`, `vector image output`)
- Warn: 3 (`grayscale contrast`, `hairline widths`, `light-gray consistency`)
- Partial pass: 1 (`fonts embedded but PDF/X not confirmed`)

### Related build gate outcomes (same run)
- Build warning gate: **PASS**
- Crossref/label hygiene: **PASS** (`675` labels scanned)
- Figure/table reference coverage: **PASS** (`83` labels)
- Chapter template audit: **PASS** (`19/19`)
- Bibliography style audit: **WARN** (`93` warnings, `0` errors): `notes_output/artifacts/qc/bib_style_report.md`

## [2026-02-11] Deterministic proof-to-code integrity pass

### Objective
- Add a deterministic academic-integrity gate that tests whether core mathematical derivations are implementable and numerically correct when coded.

### Implementation
- Added executable checker:
  - `notes_output/scripts/verify_proof_integrity.py`
- Report outputs:
  - `notes_output/artifacts/qc/proof_integrity_report.md`
  - `notes_output/artifacts/qc/proof_integrity_report.json`

### Coverage (current deterministic subset)
- Bayes posterior equation consistency (`eq:bayes_theorem`)
- Logistic NLL gradient vs finite differences (`eq:lec2_logistic_grad`)
- Two-neuron chain worked values + gradient equations (`eq:grad_w1`, `eq:grad_w2`, `eq:delta1`, `eq:delta2`)
- Hopfield energy descent identity (`eq:energy_function`, `eq:deltaE`, `eq:hopfield_update_rule`)
- CNN stride/padding output-size formula (worked chapter formula)
- RNN BPTT gradients vs finite differences (`eq:simple_rnn_hidden`, `eq:simple_rnn_output`)
- Fuzzy De Morgan and t/s-norm complementarity (`eq:fuzzy_union`, `eq:fuzzy_intersection`, `eq:fuzzy_complement`, `eq:tnorm-snorm-complement`)
- Fuzzy relation composition example (`eq:fuzzy_composition`)
- Word2Vec negative-sampling gradients (`eq:neg-sample-prob`, `eq:neg-sample-loss`)
- GA selection probability normalization (`eq:selection_probability`, `eq:linear_ranking`)

### Run and result
- Command:
  - `python3 notes_output/scripts/verify_proof_integrity.py`
- Result:
  - **PASS** (`11/11` checks)
  - No missing linked equation labels in audited subset.

## [2026-02-11] DOI/arXiv closure + blind-review recommendation closure (resume pass)

### Scope completed in this pass
- Closed the remaining bibliography hard-pass warnings while removing incorrect DOI auto-matches.
- Applied technical blind-review recommendation to scope cross-reference checks to release sources when invoked from repo root.
- Applied editorial blind-review recommendation for Chapter 13 micro-density cleanup (minimal heading-level merge, zero content movement).

### Files changed
- `notes_output/refs.bib`
- `notes_output/scripts/check_bib_style.py`
- `notes_output/scripts/enrich_bib_metadata.py`
- `notes_output/scripts/check_crossrefs.py`
- `notes_output/lecture_8_part_i.tex`

### Bibliography corrections
- Replaced known-bad DOI matches from the previous automated enrichment pass:
  - `CoxRaja2011` DOI corrected to `10.1609/aimag.v32i1.2304`.
  - `Zadeh1965` DOI corrected to `10.1016/S0019-9958(65)90241-X`.
  - Removed incorrect DOI injections and switched to canonical arXiv IDs where appropriate (`Krizhevsky2012`, `Vaswani2017`, `Brown2020`, `Lan2020`, `Simonyan2014`).
  - Added DOI for `Graves2006`: `10.1145/1143844.1143891`.
  - Added arXiv for `LevyGoldberg2014`: `1405.4053`.
- For legacy items without reliable DOI/arXiv, added URL fallbacks where available and documented explicit metadata exceptions in the checker policy (`MacQueen1967`, `DebAgrawal1995`, `Zitzler2002`, `Fritzke1994GrowingNeuralGas`, `Zadeh1997`).

### Script/policy updates
- `check_bib_style.py`
  - Enforces DOI canonical form (fails if DOI field is a URL).
  - Uses DOI-first, arXiv-second, URL-fallback policy.
  - Supports documented exception keys for legacy references lacking DOI/arXiv.
- `enrich_bib_metadata.py`
  - Added `--audit-doi` mode to verify DOI title/author/year consistency against Crossref metadata.
  - Added `--inspect-key <bibkey>` mode to inspect Crossref candidates for manual triage.
  - Tightened DOI audit logic to reduce false positives for abbreviated titles.
- `check_crossrefs.py`
  - Auto-detects `notes_output/` as release root when run from repository root to avoid false failures from non-release trees.

### Editorial micro-pass (Reviewer E P1)
- `lecture_8_part_i.tex`:
  - `\subsection{Problem Statement}` -> `\paragraph{Problem statement.}`
  - `\subsection{Contextual embeddings and transformers}` -> `\paragraph{Contextual embeddings and transformers.}`
  - This removes two interruption-style mini-sections while preserving text and equation flow.

### Validation run results
- `python3 notes_output/scripts/check_crossrefs.py` -> **PASS** (`675` labels)
- `python3 notes_output/scripts/check_ref_coverage.py --root notes_output --strict-order` -> **PASS** (`83` labels)
- `python3 notes_output/scripts/check_citations.py --notes notes_output --bib notes_output/refs.bib` -> **PASS** (`102` cited keys)
- `python3 notes_output/scripts/check_bib_style.py --bib notes_output/refs.bib --out notes_output/artifacts/qc/bib_style_report_hardpass_after.md` -> **PASS** (`0` errors, `0` warnings)
- `python3 notes_output/scripts/verify_proof_integrity.py` -> **PASS** (`11/11`)
- `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` -> **PASS** (`8/8`)
- `bash notes_output/scripts/run_editorial_qc.sh` -> **PASS** (chapter format 19/19, equations, crossrefs, ref coverage, bib style, publish QC generation)

### Artifacts generated/updated
- `notes_output/artifacts/qc/bib_style_report_hardpass_after.md`
- `notes_output/artifacts/qc/bib_doi_audit_report.md`
- `notes_output/artifacts/qc/proof_integrity_report.md`
- `notes_output/artifacts/qc/math_graph_validation_20260211_190432.md`
- `notes_output/artifacts/qc/chapter_format_audit_20260211_191037.md`
- `notes_output/artifacts/qc/publish_qc_report.md`

### Publish decision (current checkpoint)
- **Decision:** `PUBLISH-CANDIDATE`.
- **Reason:** All blocking technical gates now pass in this environment (crossrefs, citation hygiene, strict-order reference coverage, equation checks, proof integrity, math/graph validation, bibliography style hard-pass).
- **Remaining non-blocking note:** run final manual print-device proof (trim/gutter and grayscale readability) on target printer profile before external distribution.
