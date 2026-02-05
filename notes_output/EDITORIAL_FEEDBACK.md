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
