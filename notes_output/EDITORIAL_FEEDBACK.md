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
  * Part II: Neural networks → deep learning → sequences (Ch 5–13)
  * Part III: NLP applications (Ch 14)
  * Part IV: Soft computing + fuzzy reasoning (Ch 15–18)
  * Part V: Evolutionary optimization (Ch 19)

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

Your Chapter 14 bias checks and deployment checklist are excellent because they are **practical, audit-oriented, and concrete**. 

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
7) Add mini “risk & audit” boxes beyond Chapter 14 so safety isn’t siloed. 

---

If you want, I can also produce a **redline-style checklist** you can apply mechanically during rearrangement (chapter-order QA + cross-reference QA + notation QA), but the notes above should already give you a clear, concrete editing plan.
