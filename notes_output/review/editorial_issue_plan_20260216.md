# Editorial Issue Plan (Global-First)

- Source report: `/Users/Haitham.Amar/Documents/ece657Book/notes_output/review/report_llm_editorial_tex_chapters_20260216.md`
- Output plan: `/Users/Haitham.Amar/Documents/ece657Book/notes_output/review/editorial_issue_plan_20260216.md`

## Execution queue (P0/P1/P2) and progress (2026-02-17)

### P0 (correctness / broken structure)
- [x] Fix malformed subsection title + duplicate label in `lecture_3_part_ii.tex`.
- [x] Resolve layer-indexing contradiction (l=1..L vs l=0..L) in `lecture_4_part_i.tex`.
- [x] Resolve Mamdani clipping vs scaling contradiction + remove stray line break in `lecture_10_part_ii.tex`.
- [x] Complete truncated sentences in `lecture_11.tex` (fitness/exploration, crossover, GP summary).
- [x] Scan other `lecture_*.tex` files for mid-sentence truncations and malformed labels (fixed fragment in `lecture_9.tex`; no other truncations found in regex scan).
- [x] Re-verified `lecture_9.tex` fragment ("Consider two fuzzy sets") is replaced with a reference sentence; no occurrences remain (2026-02-17).

Build notes (2026-02-17):
- Release checks run. Playwright-based PDF-vs-EPUB spot-check and EPUB layout audit failed due to Chromium launch permission (TargetClosedError). Remaining EPUB checks completed and reported OK.
- Release checks re-run after P1 updates. Playwright PDF-vs-EPUB spot-check and EPUB layout audit still failed (Chromium permission); remaining checks OK.
- Release checks re-run after P1 notation sweep (x/X + vector bolding). Playwright PDF-vs-EPUB spot-check and EPUB layout audit still failed (Chromium permission); remaining checks OK.
- Release checks re-run after P1 x/X casing sweep in `lecture_8_part_i.tex`. Playwright PDF-vs-EPUB spot-check and EPUB layout audit still failed (Chromium permission); remaining checks OK.
- Release checks re-run after P1 vector bolding updates in `lecture_1_intro.tex`, `lecture_3_part_ii.tex`, `lecture_5_part_ii.tex`. PDF-vs-EPUB spot-check and EPUB layout audit completed; remaining checks OK.
- Release checks re-run after P1 vector/matrix notation consistency updates in `lecture_3_part_i.tex` and `lecture_8_part_i.tex`. All checks completed; warning gate passed.
- Release checks re-run after P1 W/A/Z/b notation sweep in `lecture_3_part_ii.tex`, `lecture_4_part_i.tex`, and `lecture_6.tex`. All checks completed; warning gate passed.
- Release checks re-run after P1 \(\delta\)/\(D\)/\(K\)/\(\Phi\) notation sweep in `lecture_3_part_ii.tex`, `lecture_4_part_i.tex`, `lecture_4_part_ii.tex`, and `lecture_6.tex`. All checks completed; warning gate passed.
- Release checks re-run after P1 \(\Sigma\) notation sweep in `lecture_8_part_i.tex`. All checks completed; warning gate passed.
- Release checks re-run after P1 dedup follow-up reference sentences in `lecture_10_part_i.tex` and `lecture_11.tex`. All checks completed; warning gate passed.
- Release checks re-run after P1 dedup updates in `lecture_1_intro.tex` and `lecture_2_part_i.tex`. All checks completed; warning gate passed.
- Release checks re-run after P1 dedup updates in `lecture_2_part_ii.tex` and `lecture_3_part_i.tex`. All checks completed; warning gate passed.
- Release checks re-run after P1 dedup updates in `lecture_3_part_ii.tex` and `lecture_4_part_i.tex`. All checks completed; warning gate passed.
- Release checks re-run after P1 dedup updates in `lecture_4_part_ii.tex` and `lecture_5_part_i.tex`. All checks completed; warning gate passed.
- Release checks re-run after P1 dedup updates in `lecture_5_part_ii.tex` and `lecture_6.tex`. All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after P1 dedup updates in `lecture_7.tex` and `lecture_8_part_i.tex`. All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after P1 dedup updates in `lecture_8_part_ii.tex` and `lecture_9.tex`. All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after P1 dedup updates in `lecture_10_part_ii.tex`, `lecture_transformers.tex`, and `lecture_11.tex`. All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after P0 truncation scan fix in `lecture_9.tex`. All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after key-takeaways cleanup + fuzzy/evo consistency edits (`key_takeaways.tex`, `lecture_10_part_i.tex`, `lecture_10_part_ii.tex`, `lecture_11.tex`). All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after key-takeaways templating consolidation + lecture_10_part_i projection/composition tightening + lecture_11 selection/crossover consolidation. All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after restoring fuzzy/GA numeric walkthroughs and programmatic verification updates (`lecture_9.tex`, `lecture_10_part_i.tex`, `lecture_10_part_ii.tex`, `lecture_11.tex`). All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after adding fuzzy/GA numeric walkthroughs (grade overlap numeric check, union/intersection example, cylindrical extension matrix, roulette selection probability walkthrough). All checks completed; warning gate passed. EPUBCheck passed.
- Programmatic verification notes: rechecked fuzzy/GA numeric values (thermostat centroids, extension/composition, GA fitness list, grade overlap). Values consistent with rounded figures in text.
- Release checks re-run after P1 consistency edits in fuzzy inference chapters (`lecture_10_part_i.tex`, `lecture_10_part_ii.tex`): standardized preimage spelling, aligned rate/notation in examples, and clarified aggregation notation without removing walkthroughs. All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after P1 dedup/signposting edits (`lecture_11.tex` workflow re-signposting; trimmed duplicate selection preview) and soft-computing motivation consolidation (`lecture_8_part_ii.tex`). All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after restoring the early GA selection numeric preview in `lecture_11.tex` (kept for pedagogy) while retaining the detailed roulette example. All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after P1 dedup trims in `lecture_11.tex` (selection/crossover preview tightened, numeric examples kept) and caption tone tweaks in `lecture_8_part_ii.tex`. All checks completed; warning gate passed. EPUBCheck passed.
- Release checks re-run after further P1 dedup in `lecture_11.tex` (trimmed redundant operator prose, kept numeric walkthroughs); `lecture_8_part_ii.tex` scan found no remaining "Use it when" caption phrasing. All checks completed; warning gate passed. EPUBCheck passed.
- P1 consistency follow-up (2026-02-18): trimmed GA recap workflow repetition in `lecture_11.tex`; re-toned table captions in `lecture_8_part_ii.tex` to reduce template phrasing. (Build verified in later release checks.)
- Numeric example verification sweep (2026-02-18): ran `notes_output/scripts/validate_math_examples_and_graphs.py --strict` across all chapters; 18/18 checks passed. Artifacts saved under `notes_output/artifacts/qc/math_graph_validation_latest.md` and `.json`.
- Release checks re-run after numeric-example sweep + P1 edits (2026-02-18). All checks completed; warning gate passed. EPUBCheck passed. Warnings persist: underfull hbox (`lecture_10_part_i.tex:209`, `lecture_10_part_ii.tex:256`, `ece657_notes.bbl:657`, LOF entries); overfull vbox (`lecture_6.tex:418`, `lecture_9.tex:1189`). Chapter format audit flagged course-voice phrasing ("Lecture") in `lecture_10_part_i.tex`.
- Course-voice phrasing fix (2026-02-18): removed "Lecture" phrasing in chapter comments within `lecture_10_part_i.tex`. (Build verified in later release checks.)
- Release checks re-run after course-voice phrasing fix (2026-02-18). All checks completed; warning gate passed. EPUBCheck passed. Warnings persist: underfull hbox (`lecture_10_part_i.tex:209`, `lecture_10_part_ii.tex:256`, `ece657_notes.bbl:657`, LOF entries); overfull vbox (`lecture_6.tex:418`, `lecture_9.tex:1189`). Chapter format audit now passes all chapters (no course-voice phrasing flagged).
- Rolling-window pass started (2026-02-18), Part I first: applied "rewrite repetition, do not delete pedagogy" edits in `lecture_2_part_i.tex`, `lecture_supervised.tex`, and `lecture_2_part_ii.tex` so repeated ideas now serve distinct roles (independent verification, search-logic template, and transition/signposting). (Build verified in later release checks.)
- Rolling-window Part I re-pass (2026-02-18): strengthened continuity richness in chapter introductions and closing handoffs (`lecture_1_intro.tex`, `lecture_2_part_i.tex`, `lecture_supervised.tex`, `lecture_2_part_ii.tex`) with explicit "what transfers later" cues (neural, fuzzy, and evolutionary chapters) while keeping pedagogical repetition via rewrites instead of deletions. (Build verified in later release checks.)
- Rolling-window Part II continuity enrichments (2026-02-18): consulted `merged_lectures_fixed.md` and the `lecture8part2` extraction; added a Part II rolling-window orientation box in `book_chapters.tex`, inserted the "two interleaved triangles" non-separability intuition in `lecture_3_part_i.tex`, and added the "controlled ripple effect" backprop intuition in `lecture_4_part_i.tex`. Also fixed a regressed malformed subsection header + duplicate label in `lecture_3_part_ii.tex`.
- Release checks re-run after Part II rolling-window edits (2026-02-18). All checks completed; warning gate passed. EPUBCheck passed.
- Attention numeric walkthrough (2026-02-18): added a 2-token causal self-attention worked example in `lecture_transformers.tex` and added a programmatic check (`check_tiny_causal_attention`) to the numeric example harness.
- Release checks re-run after attention worked example + numeric check (2026-02-18). All checks completed; warning gate passed. EPUBCheck passed.
- CNN numeric walkthrough (2026-02-18): added a 1D cross-correlation worked example with explicit stride/padding values in `lecture_6.tex` and kept it aligned with the existing programmatic check (`check_stride_pad`).
- Release checks re-run after CNN numeric walkthrough (2026-02-18). Warning gate passed. EPUBCheck passed. Note: PDF-vs-EPUB spot-check bundle emitted a Playwright timeout (non-fatal) while scrolling an element into view; release artifacts were still written and gatekeeper EPUB audits passed.
- Part II continuity reinforcement (2026-02-18): added prototype/template continuity note at the start of `lecture_6.tex` and parameter-sharing continuity note at the start of `lecture_7.tex`.
- Release checks re-run after Part II continuity reinforcement (2026-02-18). All checks completed; warning gate passed. EPUBCheck passed. Warnings persist (underfull hbox in LOF/Bib; overfull vbox in `lecture_6.tex`/`lecture_9.tex`).
- Rolling-window Part III start (2026-02-18): added a Part III rolling-window orientation box in `book_chapters.tex` (explicitly framing repetition as preview\(\rightarrow\)formalization\(\rightarrow\)sanity-check). Updated `lecture_8_part_ii.tex` closing to better preview the fuzzy trilogy without deleting pedagogy, and tightened `lecture_9.tex` continuity + fixed malformed subsection headers for t\hyp{}norms/t\hyp{}conorms (label cleanup).
- Release checks re-run after Part III rolling-window start (2026-02-18). All checks completed; warning gate passed. EPUBCheck passed. Warnings persist (underfull hbox in LOF/Bib; overfull vbox in `lecture_6.tex`/`lecture_9.tex`).
- Rolling-window Part III continuation (2026-02-18): strengthened continuity framing at the start of `lecture_10_part_i.tex` (transfer layer vs.\ set primitives) and tightened the `lecture_10_part_ii.tex` handoff to evolutionary tuning without removing numeric walkthroughs.
- Release checks re-run after Part III continuation (2026-02-18). All checks completed; warning gate passed. EPUBCheck passed. Warnings persist (underfull hbox in LOF/Bib; overfull vbox in `lecture_6.tex`/`lecture_9.tex`).
- Release checks re-run after Part IV rolling-window start + GA numeric verification alignment (2026-02-18): added a Part IV rolling-window reading guide in `book_chapters.tex`, clarified GA fitness scaling in `lecture_11.tex`, and made the fixed-point one-point crossover example verifiable (bitstrings + decoded values). Expanded the numeric harness to verify GA toy \(f(x)\) values and crossover mapping (`check_ga_fx_values`, `check_ga_fixedpoint_crossover`). All checks completed; warning gate passed. EPUBCheck passed. Warnings persist (underfull hbox in LOF/Bib and `lecture_11.tex:399`; overfull vbox in `lecture_6.tex`/`lecture_9.tex`).
- Release checks re-run after deeper Part IV rewrite-repetition sweep (2026-02-18): rewrote repeated GA-loop descriptions in `lecture_11.tex` so each instance serves a distinct pedagogical role (preview vs.\ formalization vs.\ implementation checklist), without removing numeric walkthroughs. All checks completed; warning gate passed. EPUBCheck passed. Warnings persist: underfull hbox (`lecture_10_part_i.tex:212`, `lecture_10_part_ii.tex:256`, `lecture_11.tex:400`, LOF/Bib); overfull vbox (`lecture_6.tex:436`, `lecture_9.tex:1187`).
- Rolling-window cross-chapter reference audit started (2026-02-18): created `rolling_window_reference_audit_20260218.md` (part-by-part scans always including `lecture_1_intro.tex`) plus optional author continuity write-up tasks in `writeup_tasks_from_codex_20260218.md`.
- Fuzzy\(\rightarrow\)evolutionary continuity bridge (2026-02-18): strengthened the end-of-trilogy handoff in `lecture_10_part_ii.tex` and added an explicit paradigm contrast paragraph near the start of `lecture_11.tex` (fuzzy as behavioral/auditable reasoning vs.\ evolutionary search as an algorithmic adaptation process; not a claim of biological faithfulness). Release checks re-run; warning gate passed. EPUBCheck passed.
- Fuzzy\(\rightarrow\)evolutionary transition wording refinement (2026-02-18): made the ``nature-inspired'' motivation more concrete by explicitly framing GA as an algorithmic echo of natural evolution and adding a Karl Sims\hyp{}style emergence intuition in both the Part III handoff (`lecture_10_part_ii.tex`) and Part IV opening (`lecture_11.tex`). Release checks re-run; warning gate passed. EPUBCheck passed.
- Part IV enrichment from ECE457A slide material (2026-02-19): integrated a high-level vignette (robot locomotion + ML/LLM pipeline tuning + jet-nozzle physical-experiment analogy) into `lecture_11.tex` and added a compact ES box (step-size adaptation, 1/5 success rule, self-adaptation) under the real-coded strategies section. Ignored local PPTX text extracts via `.gitignore`. Release checks re-run; warning gate passed. EPUBCheck passed.
- Release checks re-run after GA chapter notation + example consistency cleanup (2026-02-19): avoided \(\mathbf{x}\) reuse by renaming the crossover mask to \(\mathbf{u}\), standardized mutation notation (\(p_m\), chromosome \(\mathbf{c}\in\{0,1\}^L\)), aligned the constrained GA example's encoding/selection narrative, and fixed mis-indented constraint-handling list items in `lecture_11.tex`. All checks completed; warning gate passed. EPUBCheck passed. PDF-vs-EPUB spot-check bundle completed after clearing disk space (previous run hit ``No space left on device'').
- Release checks re-run after notation/preface/transformers global polish (2026-02-19): clarified the global notation table in `notation.tex` (disambiguated \(y_{\text{reg}}\) vs.\ \(y_{\text{bin}}\), tightened function-argument conventions, clarified \(\mathbf{1}\)/\(\mathbf{I}\), merged redundant reading-aids boxes), tightened voice and tense in `preface.tex`, and reduced template fatigue in `lecture_transformers.tex` (varied figure caption openers, clarified causal-mask indexing, merged adjacent implementation boxes, improved typography like ``tokens/s'' and range formatting). All checks completed; warning gate passed. EPUBCheck passed.
- Rolling-window authenticity scrub (2026-02-19): removed a small number of sentences/labels that read like time-bound or repo-internal notes rather than book prose (e.g., removed ``(2024 snapshot)'' phrasing and a source-tree path reference in `lecture_transformers.tex`; replaced with evergreen wording, updated cross-references/labels accordingly). Also tightened a vignette phrase in `lecture_11.tex` (replaced ``prompt/toolchain variant'' with a more general ``system configuration variant''). Release checks re-run; warning gate passed. EPUBCheck passed.
- Authenticity cleanup follow-up (2026-02-19): removed meta parentheticals that read like implementation notes (e.g., ``Verified by the book's numeric example harness'') from `lecture_transformers.tex` and `lecture_6.tex`. Quick regex scan for common LLM/assistant artifacts (``as an AI'', tool references, apology/disclaimer phrasing) found no other occurrences in the TeX sources. Release checks re-run; warning gate passed. EPUBCheck passed.

### P1 (global consistency / cross-ref hygiene)
- [x] Notation consistency sweeps (vector bolding; objective symbol; x/X casing) across chapters. (Progress: objective symbol standardized in `lecture_11.tex`; vector/matrix notation normalized in `lecture_3_part_i.tex` and `lecture_8_part_i.tex`; W/A/Z/b notation normalized in `lecture_3_part_ii.tex`, `lecture_4_part_i.tex`, and `lecture_6.tex`; \(\delta\)/\(D\)/\(K\)/\(\Phi\) notation normalized in `lecture_3_part_ii.tex`, `lecture_4_part_i.tex`, `lecture_4_part_ii.tex`, and `lecture_6.tex`; \(\Sigma\) notation normalized in `lecture_8_part_i.tex`; vector bolding sweep applied in `lecture_supervised.tex`, `lecture_4_part_i.tex`, `lecture_7.tex`, `lecture_8_part_i.tex`, `lecture_1_intro.tex`, `lecture_3_part_ii.tex`, `lecture_5_part_ii.tex` after manual pass beyond co-occurrence section. y/\hat{y} sweep found no vector/scalar mismatches. H/G/J/\(\Lambda\)/\(\Psi\) sweep found no vector/scalar mismatches. Data-matrix \(X\) standardized to \(\mathbf{X}\) in `lecture_supervised.tex` and `lecture_2_part_ii.tex`; regex scan found no other x/X casing conflicts.)
- [x] Cross-reference macro consistency (\Cref vs \cref) and label convention normalization.
- [x] Deduplicate repeated definitions/boxes (notably `lecture_10_part_i.tex`, `lecture_11.tex`).
- [x] Terminology consistency across examples (e.g., rate rising/falling; r vs \dot{e}).
- [x] Normalize operator terminology (t\hyp{}norm/t\hyp{}conorm/s\hyp{}norm) and hyphenation.

### P2 (typography / style polish)
- [x] List punctuation and parallelism; remove fragments and telegraphic phrasing.
- [x] Title capitalization consistency; reduce repeated headings.
- [x] Caption phrasing polish and figure lead-ins; reduce template fatigue.
- [x] Tone smoothing (avoid informal contractions and imperative instructions).

## Global sweeps (run these once, then apply locally)

### [DEDUP] Redundancy / repeated definitions
- Approach: Identify repeated definitions or duplicated paragraphs and consolidate into one canonical statement with cross-references. Use `rg -n "definition|recall|note|summary" notes_output/lecture_*.tex` and manually compare overlapping blocks; prefer a single authoritative block per concept.

### [TRANS] Abrupt transitions / missing bridges
- Approach: Insert 1–2 sentence bridges at section boundaries where a new topic/figure starts abruptly. Scan for headings or figures immediately following unrelated content without a linking sentence.

### [NOTATION] Notation / symbol consistency
- Approach: Choose and enforce a single convention per chapter (bold vs plain vectors, variable case, loss notation). Run a per-chapter sweep for mixed symbols (e.g., `\mathbf{}` vs plain).

### [MATHFMT] Math typesetting clarity
- Approach: Normalize function names (`\sin`, `\tan`, `\exp`), parentheses, and math mode. Replace plain text in display math with proper LaTeX. Check for broken `\subsection` or equation formatting.

### [LIST] List punctuation and parallelism
- Approach: Standardize bullet punctuation and verb parallelism. Use a consistent style across chapter checklists and key takeaways.

### [PUNCT] Punctuation/spacing and hyphenation
- Approach: Fix inconsistent spacing (before parentheses, around dashes) and normalize hyphenation (e.g., Newton–Raphson). Apply a consistent punctuation policy across bullets and prose.

### [TITLE] Heading/title consistency
- Approach: Ensure headings are unique and consistently capitalized. Remove duplicate section titles and unify title-case vs sentence-case usage.

### [BOX] Box density / template fatigue
- Approach: Reduce adjacent or repetitive boxes by merging or converting to prose. Keep one box per concept cluster where possible.

### [SPELL] Spelling variant
- Approach: Pick US or UK spelling and apply uniformly (e.g., “catalogues” vs “optimization”).

### [STYLE] Tone and word choice
- Approach: Replace informal or awkward phrasing with formal prose. Avoid conversational fragments.

### [LABEL] Label/cross-ref hygiene
- Approach: Repair malformed labels and ensure consistency with chapter label conventions.

### [PLACEHOLDER] Incomplete fragments / TODOs
- Approach: Remove or complete rhetorical questions and fragment lines.

### [VISUAL] Non-TikZ visual alignment
- Approach: Manually verify captions vs figures for files with `\includegraphics` (PDF/EPUB crop check).

## File-by-file issue list (all issues tagged)

### fl-intro.tex
- [TRANS] Lines 1–8: No narrative lead-in between the part/author slide and the Outline frame; flow is abrupt (part title → author → partpage → outline with no segue).
- [MATHFMT] Lines 10, 29, 63, 87, 125, 142, 154, 170, 185, 195, 207, 226, 238, 260, 274, 296, 306 (and similar): Repetitive "%%%%%%%%%%%%%%%%%%%%%%%%% New frame %%%%%%%%%%%%%%%%%%%%%%%%%" comment blocks throughout — noisy and repetitive; consider reducing or making a single consistent separator.
- [LIST] Lines 15–26: Inconsistent punctuation and spacing in the Instructor/TA lines: hyphen used as separator with inconsistent spacing ("Haitham Amar- hamar...", "Md Milon Islam- m46islam...", vs "Islam Mohamed Nasr - immnasr..."). Also no punctuation at the end of many bullets.
- [LIST] Line 19–22: Nested item "Lectures: In-Person format." then nested bullet for day/time — awkward nesting and capitalization ("In-Person" inconsistent). Time/location bullet lacks punctuation.
- [MATHFMT] Lines 33–41: Bullet list punctuation inconsistent (some bullets end with nothing, some are fragments). Tone shifts to informal instructions without transitional phrasing.
- [PUNCT] Lines 46–59: Evaluation frame: inconsistent title punctuation ("Work load and Evaluation- Subject to change" — dash usage). Content ambiguity: "Exams 60\%" then nested "Final Exam  60\%: Format (In-Person)" suggests only a final exam but is unclear; also double space before 60\% in line 55.
- [MATHFMT] Lines 50–52: Awkward phrasing: "Students are highly encouraged to work and solve them" (redundant) and "The assignments are going to require group effort. Please join a group ASAP." (informal 'ASAP', abrupt command).
- [OTHER] Lines 65–82: Large commented-out block — leaves ambiguity about whether multiple-exam option is omitted intentionally; consider clarifying or removing.

- [MATHFMT] Lines 92–106: Required background bullets inconsistent in capitalization and punctuation. "Math and Linear Algebra:" list mixes topics without parallel structure. "solving system of linear equations" missing article ("solving systems" or "solving a system").
- [PUNCT] Line 101–104: Parenthetical note style inconsistent and informal: "(not required, we will define or review these, but it would help)" — punctuation and capitalization inconsistent.
- [MATHFMT] Line 113–121: Sentence at line 120 is awkward: "If you find useful resources, add to them the resources discussion forum on LEARN." (word order confusing).
- [MATHFMT] Lines 128–141: Tone and formatting inconsistent: use of inline comment after Mendeley entry, \note immediately following, and a raw URL styled inside \alert{\uline{...}} — inconsistent emphasis and informal phrasing.
- [STYLE] Lines 146–152: Tool recommendation: "python" not capitalized; parenthetical "The de facto ..." awkward capitalization; note at line 149 is terse and informal ("The coders, apps, startups, Google etc.").
- [MATHFMT] Line 159: Long comma-separated list with inconsistent capitalization and style ("fuzzy logic, artificial neural networks, machine learning, AI, system's optimization, ..."). Problem: "system's optimization" uses a possessive where likely plural ("systems optimization") is intended.
- [OTHER] Lines 176–183: Definition block: grammatical error at line 181 — "an intelligent system is one that generate hypotheses" should be "generates".
- [MATHFMT] Lines 188–192: Quotation style inconsistent: uses straight double quotes around "intelligent" (typographic style issue) and very long sentence; consider rephrasing for clarity.
- [MATHFMT] Lines 199–204: History bullets use math mode for centuries ($12^{th}$, $19^{th}$) and inconsistent dash usage ("--"). Also double space after "He  described" and missing commas/clauses ("one of which was a humanoid automata" lacks comma before relative clause).
- [TRANS] Lines 209–222: History (Cont.) bullets contain fragments and informal language ("Deep Learning: Lots of cool and practical applications,") and an isolated raw Vimeo URL on its own line — abrupt and stylistically inconsistent.
- [LIST] Lines 230–245: Feature/capabilities blocks contain long, dense sentences and long semicolon-separated lists that hamper readability; consider breaking into separate bullets for clarity.
- [LIST] Lines 249–271: Example/Example (Cont.) pairs: inconsistent capitalization and punctuation in list items; style could be made parallel (e.g., nouns vs noun phrases).
- [STYLE] Lines 277–285: Intelligent Machines definition has a very long, convoluted sentence ("As much as neurons themselves...") that is awkward and grammatically clumsy; "As much as" is imprecise (likely "Just as").
- [VISUAL] Lines 289–305: Two frames include graphics with no captions or textual lead-ins; abrupt transitions from prose to figures.
- [MATHFMT] Lines 309–316 and 319–320: Repeated frame title "What is an intelligent System" (capitalization inconsistent: "System" vs elsewhere "system"); the integral example frame ends with "Let's see if this is true?" which is informal/awkward, and the following frame "Safe transformations:" (line 319–320) is an incomplete fragment / abrupt continuation — transition breaks and leaves content hanging.
- [TITLE] If you want, I can produce a prioritized short edit script with suggested rewrites for the most problematic sentences/frames.
- [MATHFMT] 321–327: Inconsistent math-mode usage and spacing in the list of integral rules (e.g., \Sum vs \sum, some items inside $...$, line 325 uses bare \int without $...$). This makes the display inconsistent and may confuse readers.
- [NOTATION] 335, 360: Duplicate slide titles "What is an intelligent System" appear back-to-back; consider merging or varying titles (and "System" capitalization is inconsistent with typical title case).
- [OTHER] 336: Double space in "Heuristic  transformations:".
- [MATHFMT] 338–343: Inconsistent formatting of list items (A) uppercase, B) math-mode, c) lowercase). Also nested items mix math-mode and plain text; standardize style.
- [MATHFMT] 346: The substitution rule is presented unclearly (math and text mixed). The formula uses \text{tan x} inside math mode rather than \tan and the mapping is likely incomplete/ambiguous — clarify and typeset consistently.
- [OTHER] 347: "Use roles such as" is likely the wrong word; use "rules" or "identities" (e.g., trigonometric identities).
- [MATHFMT] 349–351: Substitution suggestions ("1 - x^2 → x = \text{sin y }", "1 + x^2 → x = \text{tan y}") are terse and phrased awkwardly; reword as explicit substitution suggestions (e.g., "For integrands with 1 - x^2, try x = sin y") and use \sin, \tan for math-mode functions.
- [MATHFMT] 360–377: Capitalization inconsistency in items (e.g., "Safe transformations." vs "heuristic transformations."). Also the two rhetorical questions ("What is a Goal Tree?" and "What is a functional composition depth?") are left as placeholders with no explanation — they interrupt the flow.
- [MATHFMT] 382–390: The block text uses typographic quotes ``learn'' (LaTeX style) but surrounding prose otherwise uses straight quotes; consider consistent quotation style. Sentence in the block is long and could be tightened for clarity (minor).
- [MATHFMT] 393–401: "Inspirations " (trailing space in title). List items inconsistent: "Experts Based systems" is awkward — prefer "expert systems" or "expert-based systems"; capitalization across list items is inconsistent.
- [MATHFMT] 408–416: Awkward phrasing in bullets: "Perform intelligence sequences of decision making" is unclear — consider "perform sequences of intelligent decision-making"; "Do in a fast and efficient way" should be "Do so in a fast and efficient way."
- [VISUAL] 421–427: "Work with Machine learning algorithms" — inconsistent capitalization ("Machine" should be lowercase). The figure environment and captioning are missing/minimal; consider providing a caption or linking text to the figure.
- [OTHER] 432–438: First two sentences are repetitive ("We have data (samples). This data is a sample of a population..."). The definition of "Inferential Analysis (predictive)" is wordy and has an unclear sentence "That is observed and unobserved." Rephrase for clarity. Also "We can not" should be "We cannot" (line 436).
- [MATHFMT] 442–446: Title "Major Categories of Predictive modeling" — inconsistent capitalization of "modeling." The list items are terse; consider parallel phrasing ("Regression: maps inputs to a real-valued output." / "Classification: maps inputs to a categorical output.").
- [MATHFMT] 471–492: Many slides titled "Simple Linear Regression" in succession — repetitive slide titling makes narrative feel templated; consider grouping content or varying subheadings. Line 487: Celsius–Fahrenheit formula is typeset as \frac{5}{9}\text{Fahr}-32 which is ambiguous/wrong as written; it should be C = (5/9)(F − 32) — add parentheses and use standard notation (\text{C}, \text{F} or C, F).
- [MATHFMT] 494–506: "when there is not mathematical formula" (line 496) should be "when there is no mathematical formula." The example paragraph is broken across lines and could be tightened; variable naming case (Mort vs lat) and punctuation around parenthetical units are awkward.
- [MATHFMT] 511–517: Inconsistent variable capitalization: the text uses both lowercase x and uppercase X/Y (e.g., "Let $(x_{1}, Y_{1}),\ldots$" then formula uses X_i and \bar{X}). This inconsistency makes the covariance definition confusing.
- [MATHFMT] 522–528: "Next we use the Correlation definition as follows" is awkward; use "Next, define the correlation as:" or similar. "estimates of standard deviations" could be clearer as "sample standard deviations" or "estimates of the standard deviations."
- [MATHFMT] 531–542: Typo "slop" → "slope" (line 538). Capitalization "(The slop..." should be "(the slope...)." Also the explanation for non-linear relation is simplistic/ambiguous ("If Cor(Y, X) is close to zero, it means that we do not have any linear relation.") — consider softening or clarifying, though this borders on technical correction.
- [MATHFMT] 569–573: Two sentences repeat the same idea about the regression line; consider combining/condensing to avoid redundancy.
- [LIST] 586–599: Structure when introducing the least-squares criterion is slightly clumsy: a dangling "Suppose" followed by enumerated definitions, then the minimization statement. The phrase "is minimum where \hat{y}_{i} denotes the predicted response" is a run-on and would read clearer as "We choose \beta_0,\beta_1 to minimize Q = ... , where \hat{y}_i denotes the predicted response."
- [MATHFMT] 614–624: "Assume the probability of observing data X and Y, given that there is some true relationship $Ex[y]=\beta_{1}X+\beta_{0}$ is given by Gaussian distribution." — awkward and ungrammatical. Suggest rephrasing and consistent notation (e.g., "Assume E[Y|X]=\beta_1 X + \beta_0 and that conditional errors are Gaussian: p(y|x,\theta)=N(\beta^T x,\sigma^2)").
- [MATHFMT] 625–640: MLE slide uses double backslashes for line breaks (lines 635–637) that interrupt reading; consider using complete sentences and one clean equation for the likelihood. Also ensure consistent notation f(x_i|\theta) vs f(x_i,\theta).
- [MATHFMT] Overall: the excerpt contains many small consistency and phrasing issues (variable capitalization, math typesetting, list capitalization/parallelism), several incomplete placeholders/questions, and repetitive slide titling/templating that disrupt narrative flow. Address the flagged lines to improve clarity and cohesion.
- [SPELL] Line 641: Typo "mulitply" → "multiply". Also the note text is a fragment with a question ("Show description of bayes and likelihood?") — consider rewriting as a clear TODO or removing from final text.
- [OTHER] Line 646: Style/grammar — "MLE=The value of parameter..." is terse and inconsistent. Use "MLE = the value of the parameter θ that maximizes the likelihood L" (add spaces around '=' and the article "the").
- [MATHFMT] Line 648: Logical/phrasing issue — "you can maximize each one separately or attempt to find a multi-dimensional maxima." (a) avoid informal "you"; (b) "maxima" is plural — use "maximum" or rephrase ("find a multi-dimensional maximum"); (c) the claim "maximize each one separately" is misleading and should be clarified or removed.
- [MATHFMT] Lines 650–655: Punctuation — missing comma after introductory clause ("since ... , we can use"). Also equation styling: using "\log L" then switching to "\ell" without introducing the notation can confuse readers.
- [DEDUP] Line 659: Stray brace "}" at start of line looks out of place relative to surrounding frames — verify grouping/bracing (may indicate template mismatch).
- [PUNCT] Line 662: Formatting/spacing — "Multivariate normal distribution(dimension=n)" needs a space before "(" and could be rephrased to "Multivariate normal distribution (dimension n)".
- [MATHFMT] Line 664: Notation style — using "\text{exp}\left(...\right)" is inconsistent with standard "\exp(...)" and visually awkward.
- [MATHFMT] Line 669: Notation/formatting — uses "exp^{...}" (superscript) instead of "\exp(...)" or "e^{...}". Also the jump from the multivariate PDF to Eq. (7) ("hence:") lacks a clear transitional sentence explaining assumptions (e.g., iid scalar Gaussian noise).
- [MATHFMT] Across lines 669–686 and elsewhere: Inconsistent capitalization of variable names (e.g., X_i vs x_i) — this alternation is confusing; pick one convention and apply consistently.
- [PUNCT] Line 680–683: Punctuation — "where $\mathcal{D}$, denotes the training set." Remove comma after $\mathcal{D}$.
- [PUNCT] Line 684: Spacing/punctuation — "write(assuming training examples are i.i.d)" needs a space and punctuation: "write (assuming training examples are i.i.d.)".
- [MATHFMT] Line 686: Repeats the "exp^{...}" formatting issue noted above.
- [TRANS] Line 699–701: Flow — short bullets state generic facts but lack transitions from MLE derivation to remarks; consider adding a brief linking sentence that ties the multiplication rule to the Gaussian noise assumption.
- [LABEL] Line 709: Terminology/phrasing — label "{\color{red}Square \ error}" and the phrase "minimize the negative square error" are awkward. Recommend: "minimize the negative log-likelihood, which (for Gaussian noise) is proportional to the sum of squared errors." Also using colored text in math may be inappropriate for print.
- [STYLE] Line 722: Content/clariy — "Note that the derivative is defined as long as β0 and β1 can take on continuous values." This is awkward/technically odd. Better: "The derivatives exist when β0 and β1 are allowed to vary continuously (i.e., are real-valued)."
- [MATHFMT] Lines 727–734: Typos and wording — "caret" (line 731) should be "carat". The example text is broken into many short lines; consider merging into a single clear paragraph: dataset size, variables, and observed correlation.
- [LABEL] Lines 746 & 801: Notational style — use of "*" for multiplication and colored plain-text labels ("Predicted Price", "Carat", "Girth", etc.) is informal and inconsistent. Use standard math notation and consistent capitalization (e.g., Predicted Price = 3721 · Carat − 259.6).
- [NOTATION] Line 752–761: Grammar and typo — "Now assume instead of having one variable as predictor we have a set of variables..." needs commas and smoothing. Line 760: "The we call a multivariable regression model." → "Then we call this a multivariable regression model" or "This is called a multivariable regression model."
- [NOTATION] Lines 778–786: List formatting inconsistent (some items end with periods, some do not). Use consistent punctuation for list entries. Also use consistent variable formatting (x1 vs x_1).
- [LABEL] Lines 796–803: Same stylistic issues as earlier for the regression plane equation (multiplication symbol, colored labels).
- [NOTATION] Lines 812–816: Repetition/redundancy — several bullet points restate differences between regression and classification in quick succession; tighten to avoid repetition and ensure consistent variable notation (use $y$ everywhere).
- [MATHFMT] Line 823–826: Tone and grammar — sentence starting "It's a form..." uses contraction ("It's") in a formal text; prefer "It is". Line 825 starts with "Addresses..." missing subject — should be "It addresses...".
- [PUNCT] Line 826: Punctuation — "coded 1-positive and 0 negative." Rephrase to "coded as 1 (positive) and 0 (negative)".
- [MATHFMT] Lines 833–838 and 879–895: Repetition — the probability expressions and their factorizations are presented multiple times across consecutive slides with minor variations; this is repetitive templating. Consolidate the derivation into a single coherent presentation to avoid redundancy.
- [DEDUP] Line 842: Wordiness/repetition — "we have relaxed it so that we have a smooth curve" — avoid repeating "have": e.g., "we replace the step function with a smooth curve, allowing differentiation."
- [MATHFMT] Lines 848–867: Sentence fragment and awkward phrasing — line 850 "Since the model is probabilistic." is a fragment; merge with following bullets. Line 854 "This allows to have two possible of outputs" → "This allows two types of outputs:"; item 2 ("Probabilistic output...") is awkward — rephrase to "Probabilistic: the model outputs class probabilities (e.g., P(y=1), P(y=0))."
- [MATHFMT] Lines 884–895: Equation clarity — the log-likelihood derivation is presented inconsistently (some terms duplicated and later simplified). The intermediate dmath* line is cluttered; consider a clearer step-by-step derivation and consistent use of log vs log(·) and of vector/matrix notation.
- [MATHFMT] Lines 891–895 and 919–923: Notational inconsistency — gradients/Hessians mix transposes and scalar/vector notation (x_i vs x_i^T, P(1-P) notation). This can confuse readers; standardize vector/matrix notation and explicitly define P and how it is used (diagonal matrix vs vector).
- [MATHFMT] Line 896: Tone — "How to solve for β?" is a rhetorical question; in a textbook prefer an explicit transitional sentence (e.g., "We now solve for β using Newton–Raphson.").
- [MATHFMT] Lines 902–931: Inconsistent hyphenation and spacing — "Newton- Raphson" has a space after the hyphen; use "Newton–Raphson" (en-dash or hyphen without extra space). Line 931 presents an update formula as scalar division of gradient by Hessian; for vector/matrix case this is misleading — clarify with matrix inverse or linear solve notation (e.g., β_new = β_old − H^{-1} g).
- [MATHFMT] General/style: Frame titles repeat (multiple "Theory of Linear Regression", repeated "Logistic Regression") which reduces navigability; consider more specific subtitles for consecutive slides. Also inconsistent capitalization in frame titles ("Multivariable regression" vs "Simple Linear Regression") — choose and apply a consistent title-case convention.
- [MATHFMT] General/punctuation: Many bullets end or do not end with periods inconsistently; standardize sentence punctuation across bullets.
- [LABEL] General/accessibility: Use of colored text in equations may not print well or be accessible; rely on typography and labeling instead of color for emphasis.
- [OTHER] If you want, I can produce a concise edited rewrite of any specific slide or group of slides (e.g., the MLE-to-linear-regression sequence) implementing the above fixes.
- [VISUAL] Visual check note: `fl-intro.tex` contains `\includegraphics`; verify caption/prose alignment against rendered figure crops.

### key_takeaways.tex
- [LIST] Lines 9: Parallelism break — "reuses the \Cref{chap:supervised} toolkit to build probabilistic classifiers, emphasize ROC/PR analysis, and reason about ..." mixes "to build" (infinitive) with base-form verbs "emphasize" and "reason." Make the verb forms parallel (e.g., "to build ..., to emphasize ..., and to reason ..." or "builds ..., emphasizes ..., and reasons ...").
- [DEDUP] Lines 6–24: Highly repetitive templating — each chapter blurb follows the same long "verb + list" pattern. This produces a monotonous rhythm; consider shortening some items or varying sentence openings/structure to improve readability.
- [VISUAL] Line 6: Word choice — "points to the notation/figure conventions" is slightly vague/awkward. Consider "summarizes," "describes," or "lists" instead of "points to."
- [VISUAL] Lines 109 and 113: Redundancy — the figure caption (line 109) and the following sentence (line 113) both state that the figure is a visual map. Consider deleting or rewording line 113 to avoid repetition.
- [VISUAL] Lines 119 and 138: Redundancy — the table caption (line 119) and the closing sentence (line 138) both repeat that the table is a compact lookup. Consider tightening one of these to avoid echoing the same instruction.
- [VISUAL] Lines 92 vs. 128: Inconsistent terminology/abbreviation — figure uses "seq.\ models" (line 92) while table uses "sequence models" (line 128). Pick one form and use it consistently.
- [MATHFMT] Line 10: Spelling variant — "catalogues" uses British spelling while elsewhere (e.g., "optimization" on line 12) reads American. Standardize on one variant across the manuscript.
- [LIST] Line 33: Slight antecedent ambiguity — "These illustrate early steps..." — it's mildly unclear whether "These" refers to the listed examples or to "Algorithms that reason about their own learning loops." Consider replacing "These" with a clearer noun ("These examples" or "This level") for clarity.
- [VISUAL] Line 109 (caption) and lines 119/125 (table caption/rows): Tone repetition — both the figure and the table captions use "Use this when..." instructions. Consider varying the call-to-action wording to avoid repetition across nearby elements.

### lecture_10_part_i.tex
- [MATHFMT] Lines 37–41 and 59: Operator defaults are stated more than once (box at 37–39, repeated in the "Notation." paragraph at 41, and a commented reminder at 59). Consider consolidating to a single authoritative statement to avoid repetition.
- [LABEL] Lines 77–81, 126–129, 250–254: The extension-principle formula (sup over preimages) and its explanation are repeated verbatim in three places. This is redundant — consolidate or move to one definition and reference it elsewhere.
- [TRANS] Lines 106–108: Incomplete sentence — "Consider the universe \( X = \mathbb{R} \) and the fuzzy set \( A \)" ends abruptly with no continuation or definition of A.
- [PUNCT] Lines 89 vs. 183 (and elsewhere): Inconsistent hyphenation for "preimage"/"pre-image"/"pre-images" (line 89 uses "pre-image", line 183 uses "pre-images"). Pick one spelling and apply it consistently.
- [MATHFMT] Lines 11, 41, 95, 218: Inconsistent formatting/capitalization for the t-norm term: occurrences use "t\hyp{}norm", "T-norm", and "t-norm". Standardize to one form across the chapter.
- [MATHFMT] Line 199: Unusual use of \allowbreak in running text ("...respectively.\allowbreak"). This interrupts the prose and looks like a typesetting fix left in source; remove or document reason.
- [VISUAL] Lines 182 and 316: Duplicate comment "% Avoid inline math in captions; it wraps poorly in some EPUB renderers." The same comment appears twice; keep one instance.
- [DEDUP] Lines 286–287: Duplicate \addplot lines in the TikZ picture (both plotting domain=-2:0 with {0}). Probably an accidental copy/paste — remove the redundant command.
- [VISUAL] Line 183: Caption uses informal "+/-" ("x = +/-1"); prefer the LaTeX ± notation (\pm) or a spelled-out form for consistency with the rest of the text.
- [VISUAL] Line 317: Awkward phrasing in caption: "whose images union to the output alpha-cut." Consider rephrasing to "whose images' union equals the output alpha‑cut" or "whose images together form the output alpha‑cut" for clarity.
- [TRANS] General: Several short paragraphs restate the same intuition (e.g., why mu_B should be supremum) across multiple subsections. This produces a choppy, repetitive flow; consider consolidating intuition/remarks into one focused block immediately after the formal definition (lines ~74–95) and then cross-referencing it from examples/recap.
- [MATHFMT] If you want, I can draft a suggested consolidation (single-definition + one intuition paragraph + pointers to examples) to replace the repeated fragments.
- [DEDUP] Lines 324 vs 380: "Projection of Fuzzy Relations" appears as both a subsection title (line 324) and a paragraph heading (line 380). This is redundant and disrupts flow—remove or retitle the second occurrence.
- [MATHFMT] Lines 384–389 and 486–487: The projection onto X is defined twice (first at lines 384–389, then repeated at 486–487). Consider keeping a single, clearly placed definition and cross-referencing it instead of repeating.
- [DEDUP] Lines 514–518 and 591–603: Composition of relations (max–min / sup–min) is given twice in quick succession with only minor wording changes. This repetition interrupts narrative flow; consolidate into one canonical definition and move the generalization/variants immediately after it.
- [MATHFMT] Lines 530–556 and 610–636: Two separate composition examples are presented back-to-back. The second example repeats the same idea with different numbers. Either combine examples, make their distinct pedagogical purpose explicit, or remove the redundancy.
- [VISUAL] Line 349 (table caption): Tone is informal/imperative ("Use it when choosing..."). For a graduate textbook prefer neutral phrasing (e.g., "Recommended uses" or "Typical uses").
- [MATHFMT] Lines 355–357 vs line 569: In the table you use "t\hyp{}conorm" (line 355) but in the tcolorbox you ask readers to "Swap ... and \(\max\) for the corresponding s\hyp{}norm" (line 569). This introduces inconsistent terminology (t-conorm vs s-norm). Choose one term and define it on first use.
- [VISUAL] Line 440 (figure caption): The caption refers to "the error universe (middle) and the rate-of-change universe (right)" and to "the running thermostat example" that is not introduced nearby. This is potentially confusing—either introduce these universes earlier or generalize the caption to match the figure content.
- [VISUAL] Lines 441, 466, 571: Labels/comments refer to "lec17" / "Chapter 17" while the file is lecture_10_part_i.tex. Inconsistent labeling/metadata (figure label, chapter comments) may confuse cross-references or reviewers—standardize numbering/labels.
- [MATHFMT] Lines 364–378 (Cartesian product example): The example lists membership vectors \mu_A and \mu_B without indexing; the explanation of which row/column corresponds to which element appears only at line 378. Move or repeat the indexing clarification earlier (immediately after the vector definitions) to improve clarity.
- [MATHFMT] Line 471: "Two operators do the heavy lifting" — the word "operators" may be ambiguous (you later describe operations such as cylindrical extension and projection). Consider using "operations" or "procedures" to avoid confusion with algebraic operators (e.g., t-norms).
- [NOTATION] Line 624: "where rows correspond to \(X\) or \(Y\) elements and columns to \(Y\) or \(Z\) elements respectively." This is ambiguous. Clarify which relation each matrix refers to (e.g., "rows of R1 correspond to X, columns to Y; rows of R2 correspond to Y, columns to Z").
- [MATHFMT] Line 378: "Keeping that indexing explicit avoids ambiguity when reading off the projected membership values." Suggest making this instruction more directive (e.g., "Make the indexing explicit to avoid ambiguity") or moving it to immediately follow the example's definitions (see point above).
- [VISUAL] Line 439 (inline comment in source): "% Avoid inline math in captions; it wraps poorly in some EPUB renderers." This is an author note embedded inside the figure environment. Consider moving such implementation notes to a separate author comment block or the document preamble to avoid polluting figure code.
- [VISUAL] Tone/register: A few informal phrasings appear (e.g., tcolorbox title "fuzzy matrix multiply", imperative table caption). Consider smoothing register to match academic/textbook style consistently.
- [DEDUP] If you want, I can mark suggested consolidation points directly in the source (showing where to remove/merge duplicate definitions and examples).
- [MATHFMT] 656–659 (Distributivity item): the bullet ends with the displayed equation but no concluding punctuation/sentence. Other bullets end with a sentence/period — add a short concluding phrase or a period for consistency.
- [LABEL] 661 (De Morgan's Laws and Inclusion): the item is terse and vague compared with the others. Consider adding a brief statement or a reference/example to clarify what "inclusion" means in this context.
- [DEDUP] 668–678 vs. 680–684 (Redundancy): the tcolorbox "Author's note" (680–682) gives the same practical advice that is immediately restated in prose (684). Remove one or merge to avoid repetition.
- [MATHFMT] 686–707 and 709–718 (Placement/mismatch of summary boxes): the "Key takeaways" / "Minimum viable mastery" / "Common pitfalls" box (686–707) and the "Exercises and lab ideas" box (709–718) summarize/advise primarily about the extension principle / transfer-and-aggregate pattern, but they appear directly after a short section on composition operators. The summaries feel out of place here — consider moving them to the section on the extension principle or making their scope explicit.
- [DEDUP] 680, 686, 709 (Repetitive templating): three summary-style tcolorbox blocks appear back-to-back. This creates visual and rhetorical repetition; consider consolidating into one structured box with subsections, or spacing them with a short transition.
- [MATHFMT] 680 (tcolorbox title capitalization): inconsistent capitalization in titles — "Author's note: choosing an operator family" uses sentence-style capitalization while "Key takeaways" and "Exercises and lab ideas" use title/sentence mixing. Adopt a consistent title-style convention across boxes.
- [LABEL] 684 vs. 720 (Inconsistent cross-reference macros): line 684 uses \Cref while line 720 uses \crefrange (lowercase c). Use one macro consistently (prefer \Cref for sentence-initial refs) to ensure uniform formatting.
- [TRANS] 720 (Transition sentence tone): "Where we head next." followed by a long sentence is slightly abrupt. Consider a smoother transition (e.g., "Next: operationalizing these tools in \Cref{chap:fuzzyinference}.") to improve narrative flow.

### lecture_10_part_ii.tex
- [MATHFMT] Line 247: stray LaTeX linebreak "\\" at the end of the sentence — remove it (interrupts paragraph flow).
- [MATHFMT] Lines 247 vs. 85 (content tension): Mamdani is earlier described (line 85) as using "min-implication (clipping)" yet line 247 groups Mamdani with "scaled fuzzy consequents" (suggesting scaling/Larsen). This is a contradictory description; pick one formulation or clarify that Mamdani normally clips while Larsen scales.
- [LABEL] Inconsistent example terminology for the input "rate": - Lines 20 and 263 use the label "rate is Falling". - The worked example (rules and membership functions) uses "Rising" and "Stable" (lines 163, 161 and rules at 179–181). Suggest unifying the example phrasing to avoid reader confusion.
- [MATHFMT] Inconsistent variable names for the second input: - Worked example uses r for rate (lines 150–151, 161–169). - Sugeno example uses \dot{e} (line 250). Choose one notation or explicitly state their equivalence.
- [MATHFMT] Inconsistent notation for the aggregated output fuzzy set: - Equation uses \mu_{B_{\text{agg}}}(y) (line 95). - Later prose / code use mu_{\text{out}}(u) (line 200) and mu_Bagg(y) in the verbatim pipeline (line 217). Recommend standardizing to a single symbol across prose, equations, and code snippets.
- [DEDUP] Repetitive/fragmenting use of boxed environments: many tcolorbox/pitfallbox/summarybox interruptions (e.g., blocks at lines 7–13, 15–17, 25–27, 37–39, 85–87, 113–121, 137–142, 210–223, 225–233, 235–242, 266–287, 289–298). These frequent asides repeatedly break the main narrative; consider consolidating some boxes or moving less-critical notes to appendices/footnotes to improve flow.
- [LIST] Lines 257–262: use of {\raggedright ... } wrapping the itemize block is unusual and inconsistent with surrounding lists (other itemize environments are not wrapped). Either remove the raggedright wrapper or apply consistently.
- [LABEL] Notation/labeling consistency in the pipeline pseudocode (verbatim, lines 212–221): identifiers use different styles (alpha_j, mu_Bj_prime, mu_Bagg) than the main text/equations (α_j, \mu_{B'_j}, \mu_{B_{\text{agg}}}). Align pseudocode names with the mathematical notation used elsewhere for clarity.
- [MATHFMT] Minor clarity/punctuation: line 100 "Other aggregations" paragraph is a single sentence with multiple clauses; consider splitting into two sentences for readability (it currently packs caution, consequence, and recommendation into one long sentence).
- [DEDUP] Repeated headings/phrases: "Common pitfalls" appears multiple times (boxes at lines 235–242 and again at lines 281–286). Either merge or retitle the later occurrence to avoid perceived duplication.
- [OTHER] No other concrete editorial issues found in the inspected range.

### lecture_11.tex
- [LIST] Line 5: Ungrammatical/uneven parallelism after the colon — "built three complementary toolkits: optimize models ..., learn representations ..., and encode ..." Either use infinitives ("to optimize, to learn, and to encode") or gerunds ("optimizing, learning, and encoding") for parallel structure.
- [DEDUP] Lines 2 and 106: Repetition of section title — the top-level section is "Introduction to Evolutionary Computing" (line 2) and there is a subsection with the same title at line 106. Consider renaming the subsection or removing the duplicate title to avoid confusion.
- [MATHFMT] Lines 56–61 and 96–102: Redundant content — both blocks list "Challenges" / "Issues with Traditional Methods" and largely overlap. Consider consolidating these into a single, non-repetitive list.
- [DEDUP] Lines 175–181 and 179–181 (overlap): Repetitive tcolorbox content — the hyperparameter/heuristics boxes and the "Author's note" repeat similar guidance about population size and mutation. Trim or merge to avoid duplicating heuristics/advice.
- [NOTATION] Lines 42 and 46: Minor clarity — "Vectors of candidate solutions are written as \(\mathbf{x}\), objective values as \(f(\mathbf{x})\), and population members as individuals/chromosomes depending on encoding." Wording is awkward; recommend "population members (individuals or chromosomes, depending on encoding)" for clarity.
- [MATHFMT] Lines 188–192 and elsewhere: Excessive manual line breaks in boxed text — boxes use "\\" and manual line breaks (e.g., lines 188–191) which fragments sentences. Prefer letting the box typeset paragraphs naturally or use complete sentences for readability.
- [MATHFMT] Lines 132–135: Forced line break inside a paragraph via "\\" (in the sloppypar). Remove the explicit line break and merge the sentences for smoother flow: the break interrupts the prose rhythm.
- [MATHFMT] Lines 279–280: Ambiguity / biological mismatch — "Each gene or chromosome corresponds to a phenotype, representing a candidate solution..." This conflates gene/chromosome roles. Clarify that chromosomes map to phenotypes (candidate solutions) and genes map to components/traits of that phenotype.
- [MATHFMT] Lines 189, 303, 315 vs earlier (e.g., lines 42, 46): Notational inconsistency — objective function is sometimes denoted \(f(\mathbf{x})\) and elsewhere as \(J(\mathbf{x})\). Choose one symbol (or explicitly state the equivalence) to avoid reader confusion.
- [MATHFMT] Line 133–134 and nearby: Slightly telegraphic phrasing in biological explanation ("Segments of genetic material are exchanged between paired chromosomes.\\ Recombination increases genetic diversity.") — besides the forced line break, consider combining into a single flowing sentence for clarity.
- [VISUAL] Line 253 (figure caption): Awkward phrasing — "Use it when mapping an implementation to the canonical operator loop." Recommend "Use this figure when mapping an implementation to the canonical operator loop" or rephrase to be more explicit.
- [DEDUP] General/template observation: The document uses many small "summarybox"/"Author's note"/"at a glance" boxes in close succession (lines 9–19, 35–37, 42–44, 175–181, 188–192). Several boxes overlap in content or tone. Consider consolidating or varying box purposes to avoid repetitive templating and to improve narrative pacing.
- [OTHER] If you want, I can propose edited wording for any of the flagged lines/sentences.
- [MATHFMT] Lines 332–334: Sentence truncated — "balancing exploitation of high-fitness regions and exploration via mutation and" stops mid-sentence. Also a comment on line 334 ("% Continuing...") immediately follows the fragment and breaks the flow. Complete the sentence and remove or relocate the comment.
- [TRANS] Lines 581–583: Another truncated sentence — "This operator allows mixing of genetic" — stops abruptly. Finish the sentence with the intended noun (e.g., "information", "material", "components") and add punctuation.
- [MATHFMT] Repetition / duplicated material (causes inconsistent flow): - Selection is presented twice in quick succession: initial brief subsection at lines 445–456 and a much longer, overlapping treatment at lines 471–509 (plus ranking/details at 511–543). Merge or remove duplicative material to avoid redundancy and possible inconsistencies. - Crossover is likewise duplicated: a short "Crossover" block at lines 457–467, a detailed "One-Point Crossover" at 559–579, and then another "Crossover Operators" discussion at 583–611 (including a repeated single-/multi-point explanation at 588–599 and 601–608). Consolidate these into a single, coherent crossover section.
- [MATHFMT] Section-heading redundancy: Multiple headings/subheadings (Selection / Selection in Genetic Algorithms, Crossover / Crossover Operators) repeat the same concepts with slightly different phrasing — this makes navigation and cross-referencing confusing. Consider unifying headings and removing overlap.
- [MATHFMT] Line 334 (comment) placement interrupts narrative — the "% Continuing Chapter 19 notes..." comment sits amid prose fragments; move comments to preamble or between logical blocks so they don't break sentences.
- [OTHER] Minor clarity issue (lines 399–412): The constraint is "0 < x ≤ 15" (line 405) but line 410 says "bounded between 0 and 15" (which can imply inclusivity). For precision, restate as "0 < x ≤ 15" or "x in (0,15]" to match the constraint, so encoding rationale is unambiguous.
- [OTHER] Ambiguity about fitness for minimization (line 423): "The fitness function corresponds to the objective function f(x)" is potentially misleading for a minimization problem. Clarify how fitness is derived from the minimization objective (e.g., use negative objective, reciprocal, or a scaling/penalty scheme).
- [MATHFMT] Tangential digression / tone (lines 617–618): The biological anecdotes (polar bears, elephants) are vivid but feel abrupt in a technical exposition. Either shorten them, better tie them to the algorithmic point being made, or move to a brief illustrative sidebar.
- [TRANS] Punctuation/spacing: several places end abruptly without terminal punctuation due to the truncated sentences noted above (lines 332, 581). Ensure sentences terminate properly and that paragraph breaks do not split sentences.
- [TITLE] If you want, I can propose a concrete merged structure for the Selection and Crossover sections and supply corrected sentences for the truncated lines.
- [MATHFMT] Lines 655: Awkward phrasing / repetition — "balancing exploration and exploitation and for avoiding premature convergence." Suggest: "balancing exploration and exploitation, and avoiding premature convergence."
- [MATHFMT] Lines 860–863 (tcolorbox titled "Defaults that work (DE/CMA-ES)"): - Two bolded entries are run together as inline sentences rather than as separate items (no visual separation). Consider using an itemize/list or at least a paragraph break so they don't read as a single run-on line. - Line 861: missing article — "start with population \(10\!-\!20\times D\)" → "start with a population of \(10\!-\!20\times D\)".
- [MATHFMT] Lines 762–773, 777–836, 868–883, 949–960: Repetitive templating / redundancy — the same GA workflow is presented as an enumerated list (762–773), a flowchart (777–836), pseudocode (868–883) and then recapped in prose (949–960). This repetition makes the section long and somewhat circular; consider consolidating or explicitly signposting that these are the same material in different formats.
- [VISUAL] Lines 754 and 834 (figure captions): both captions use the phrase "Use it when ..." in close succession. This repeated admonition feels redundant; vary or remove to avoid repetitive tone.
- [MATHFMT] Lines 898–905 (GA Parameters): Narrative inconsistency — earlier sections discuss probabilistic selection; here "Selection: All chromosomes are selected for crossover or mutation (no explicit selection probability)" contradicts the typical probabilistic selection description. Either justify this choice or rephrase to avoid confusing readers.
- [MATHFMT] Line 923: Unclear rationale — "Chromosomes decoding to \(x=0\) are discarded or repaired." This conflicts with the stated feasible interval \(0\le x\le0.5\) (0 is feasible). Explain why x=0 is discarded or clarify whether this is an implementation detail (e.g., avoid degenerate encoding).
- [TITLE] Lines 933–942 (tcolorbox "Constraint handling playbook"): - Lines 940–942: The paragraph titled "Reproducibility and fair comparison" appears inside this tcolorbox (no visual separator). This looks like an accidental placement; move the paragraph outside the boxed playbook or clearly separate it.
- [LABEL] Minor phrasing / style: - Line 674–676: "Because GAs rely on heuristic search without a global optimality guarantee, they often converge prematurely..." The opening "Because..." sentence is long and could be tightened for readability. - Line 828 (flowchart label): "yes / stop" — stylistically prefer "yes / stop" → "yes / stop" is inconsistent punctuation; consider "Yes — stop" or "Yes / Stop" for consistency with other labels.
- [DEDUP] If you want, I can propose concise rewordings for the flagged sentences/blocks and suggest a pared-down structure to remove redundant sections.
- [MATHFMT] Line 980: Missing comma after introductory phrase — "In practice many teams..." should be "In practice, many teams...".
- [LABEL] Lines 979–981: Potentially confusing cross-reference — the phrase "reuse the constraint-handling policies in the preceding box" reads as if the box has already appeared, but the visible summary/lab tcolorboxes occur later (lines 1135–1167). Verify the intended reference or adjust wording.
- [PUNCT] Line 1005: Trailing period inside displayed math: "(x_1 \times x_3) + (x_1 + x_4)." — move the period outside the math or remove it.
- [PLACEHOLDER] Lines 1059–1060: Incomplete sentence — "Genetic programming generalizes genetic" is cut off and leaves the paragraph hanging. Complete or remove this fragment.
- [MATHFMT] Repetition / templating (suggest consolidation): - Genetic operators (selection/crossover/mutation) are defined multiple times: lines 1010–1013, 1074–1077, and 1091–1093. Consider consolidating or cross-referencing rather than repeating. - GP representation and basic points are repeated: lines 996–1001 and again at 1088–1097. These sections overlap substantially; tighten to avoid redundancy. - Recap section (lines 1066–1081) largely reiterates content just covered; consider shortening the recap or making it more synthetic.
- [NOTATION] Line 1121: Inconsistent heading capitalization/style — "\paragraph{Metrics and variants}" uses sentence-style capitalization while most other paragraph headings use title case (e.g., "Problem Setup", "Genetic Operators in GP"). Make heading styles consistent.
- [VISUAL] Visual check note: `lecture_11.tex` contains `\includegraphics`; verify caption/prose alignment against rendered figure crops.

### lecture_1_intro.tex
- [MATHFMT] Repetitive phrasing / redundant content: - The three-pillar motif (perception — reasoning/decision-making — action) is repeated many times in short succession (e.g., lines 161–167, 171–175, 182–191, 195, 206–211, 266–267). Consider consolidating or varying presentation to avoid reader fatigue. - Two capability lists cover essentially the same ground (bulleted list at 206–211 and enumerated list at 276–288). Either merge them or clarify how they differ.
- [LABEL] Inconsistent terminology: - The component label "Reasoning and Decision-Making" is used in the component description (lines 163–166) but the autonomous-vehicle example uses "Thinking" (line 173). Pick one term and use it consistently. - "meta-cognitive" (line 217) vs more common "metacognitive" — choose a single spelling/hyphenation throughout.
- [LABEL] Narrative flow / transitions: - Several long, complex sentences interrupt flow and would benefit from being split. Notable examples: lines 94–103 (core definition paragraph), lines 121–127 (value-centric roles and examples), line 193 (long run-on listing many chapter references), and line 217 (levels-of-intelligence sentence). Shorter sentences would improve readability.
- [MATHFMT] Punctuation / spacing: - Missing comma after a fronted adverbial clause: add a comma in "Once they are in place we can reason..." → "Once they are in place, we can reason..." (line 156). - Unusual placement of a percent character before the footnote: a percent is present at the end of line 136 before \footnote on line 139. This is a source-level trick to suppress whitespace but may confuse readers/editors inspecting the LaTeX source.
- [LABEL] Minor editorial/wording suggestions: - The opening definition of AI (lines 90–93) is slightly wordy and repeats the "applications vs. field" contrast; consider a tighter phrasing to improve punch and clarity. - Capitalization consistency for level labels: the text uses "level 1"/"level 2" (line 217) but elsewhere uses "Levels" (title). Standardize to "Level 1" (capital L) or "level 1" consistently.
- [MATHFMT] Formatting/templating oddity: - The small terminology itemize block appears to have inconsistent indentation in the source (lines 304–308): the second \item is indented more than the first. This is a minor source-formatting inconsistency worth cleaning.
- [MATHFMT] Lines 326–327: Forced line break ("\\") immediately after the colon looks like a typesetting hack; prefer a normal paragraph break or run-on sentence. Also: "self\hyp{}monitoring of one's own decision process" is redundant (self-monitoring vs. "one's own"); consider "self-monitoring of the decision process" or "monitoring its own decisions."
- [BOX] Line 330: Forced line break ("\\") inside the tcolorbox is unnecessary. Remove for cleaner source.
- [MATHFMT] Line 330: The authorial aside uses "in my view" — this shifts tone to a personal voice inside an otherwise neutral text. If intentional keep it; otherwise consider rephrasing to maintain consistent authorial tone.
- [OTHER] Lines 344–345: "improve its own utility autonomously and rapidly" is ambiguous — does this mean increase its objective value, change its utility function, or something else? Also "degrades another's" is elliptical (possessive without noun). Suggested rewrite: "improving one agent's utility can degrade another agent's utility" or "improving one objective can degrade another objective."
- [NOTATION] Lines 365–368 (itemize entries): inconsistent end punctuation in the two bullets (one ends with ");" the other with ")."). Itemized lists should use a consistent convention (no punctuation, periods, or semicolons).
- [DEDUP] Lines 370–372: Slight repetition — the phrase "rather than treating each technique in isolation" (line 370) and "rather than treating deep networks in isolation" (line 372) are close in meaning. Consider consolidating or varying wording to avoid redundancy.
- [OTHER] Line 374: The paragraph begins with extra indentation in the source. This disrupts source-file consistency (other paragraphs are not indented). Remove leading spaces for consistency.
- [LABEL] Line 358 vs. lines 430–433: Multiple near-duplicate references to the "Notation and Conventions" / "front matter" appear in quick succession (Reader's guide, Using and Navigating, Conventions and reading aids). Consider consolidating to avoid repetitive signposting.
- [TRANS] Line 426: "check where it sits on the Roadmap." The pronoun "it" is loosely defined; use "the chapter" for clarity.
- [VISUAL] Line 428: "follow cross-referenced figures\slash equations" — mixing LaTeX \slash with text is slightly visually awkward. Prefer "figures and equations" or "figures/equations" for clarity and consistency.
- [NOTATION] Line 459: Header-style bold "If you are skipping ahead." ends with a period. Other headings (e.g., \paragraph titles) do not use terminal punctuation. Make heading punctuation consistent (prefer no period).
- [PUNCT] Line 462: Similar to above, the running paragraph title "Where we head next." uses a trailing period while other \paragraph headings do not. Normalize heading punctuation across the file.
- [OTHER] No other editorial issues spotted in the requested range.

### lecture_2_part_i.tex
- [MATHFMT] Line 7: Sentence fragment / voice. "We study symbolic problem solving through \emph{integration-by-transformation}: preserve meaning while rewriting an expression..." — change to "which preserves meaning while rewriting…" or otherwise make the verb form parallel to "study".
- [STYLE] Line 45: Word choice. "reduce the problem into manageable subproblems" — prefer "reduce the problem to manageable subproblems".
- [MATHFMT] Line 49: Unclear notation / possible ambiguity. The expression "if \(u=\phi(x)\) and \(F_u\) is an antiderivative of \(T[g](u)\), then \(F_u\!\circ\!\phi\) differentiates back to \(g(x)\)" introduces T[g](u) without explanation and mixes symbols (g, T, F_u) in a way that may confuse readers. Either define T and the role of g or rephrase with simpler notation.
- [MATHFMT] Line 65: Long, packed sentence and terminology. The sentence about the Beta function is long and slightly awkward ("the Beta identity applies to that definite integral on \([0,1]\), and it is therefore customary to fall back on it…"). Consider splitting into two sentences and replace "Beta identity" with "Beta-function identity" or "Beta function" for clarity.
- [MATHFMT] Line 93: Inconsistent/example detail. The item "Recognizing patterns such as functions of \(10x\) or other scaled arguments…" uses a specific numeric example (10) whereas earlier the text uses generic scale `c`. Consider using a consistent generic example (e.g., \(f(cx)\)) to avoid the apparent arbitrariness of "10x".
- [MATHFMT] Lines 102–106: Minor redundancy. After showing \(\int \tan x \, dx = -\ln|\cos x| + C\) the clause "which is a standard integral with the constant of integration explicitly noted" is unnecessary; you can remove or compress it.
- [MATHFMT] Line 135: Undefined acronym. "AST" appears without expansion. Expand on first use (e.g., "AST (abstract syntax tree) nodes").
- [MATHFMT] Lines 147 vs. 166: Inconsistent domain notation. Line 147 restricts to \(|x| < 1\), while line 166 says "we take \(y=\arcsin x\) with \(y\in[-\frac{\pi}{2},\frac{\pi}{2}]\) so that the substitution remains bijective on the domain \(|x| \le 1\)". Choose either strict (<1) or inclusive (≤1) and be consistent (note the integrand is singular at ±1).
- [NOTATION] Lines 200–207 vs. 128–136: Repetition of cost/heuristic discussion. The cost-metric idea (tree depth, nonlinearity, symbol count) is introduced in two nearby places with slightly different wording; consider consolidating the heuristic/cost discussion to avoid repetition.
- [MATHFMT] Line 233: Awkward phrasing. "Outside \((-1,1)\) the principal-branch integrand is complex-valued; a real continuation rewrites the integral as \(\int 4(x^2-1)^{-5/2}dx\) with \(x=\cosh t\)." Suggest "principal branch" (no hyphen) and rephrase for clarity, e.g., "On |x|>1 the principal-branch integrand becomes complex; to obtain a real-valued continuation one may rewrite the integrand as … and substitute \(x=\cosh t\)."
- [OTHER] If you'd like, I can provide suggested rewrites for any of the above lines.
- [DEDUP] Duplicate TikZ blocks: The entire diagram and legend are essentially duplicated (first block around lines 324–342, second around 408–426). Consider consolidating to avoid maintenance drift and reduce repetitive templating.
- [LABEL] Legend text missing article / slight awkward phrasing (both copies): line 341 and line 425: "Labels \textbf{[S]} and \textbf{[H]}\\indicate strategy" — add "the" or rephrase ("indicate the strategy" or "indicate strategies").
- [DEDUP] Repeated content about backtracking: lines 451–456 — the bulleted items (lines 453–455) and the following sentence (line 456) restate the same point. Merge or remove redundancy.
- [LIST] Odd placement of \raggedright inside itemize: line 446. That command inside the list is unusual and may affect layout unpredictably; apply ragged-right to the environment or remove if unintended.
- [NOTATION] Inconsistent notation for the integrand: lines 464/467 (and pseudocode) use f0, line 520 uses \(f_0\), but line 526 uses f. Make notation consistent (f0 or f_0 throughout).
- [MATHFMT] Inconsistent spelling: line 542 uses "Rationalising" (‑ising) while line 553 uses "recognize" (‑ize). Choose consistent spelling (US vs UK) across the chapter.
- [TRANS] Long, dense sentence reduces clarity: line 518 ("The pseudocode mirrors the narrative: ... return a clear status/history/domain either way.") — consider splitting into two sentences for readability.
- [MATHFMT] Heading punctuation inconsistent: some \paragraph headings include a trailing colon (e.g., line 436 "Example:"; line 444 "Safe vs. Heuristic Transformations:") while others use a period or no punctuation (line 575 "Connection to statistical learning." and line 613 "Where we head next."). Standardize heading punctuation.
- [NOTATION] Awkward inline bold note punctuation: line 609 uses "\noindent\textbf{If you are skipping ahead.}" — the sentence-ending period inside a bold lead-in feels odd; use a colon or reword ("If you are skipping ahead:").
- [VISUAL] Table caption redundancy and phrasing: line 534 begins with "Table: Transformation toolkit..." — starting a table caption with "Table:" is redundant (LaTeX already labels it). Also the parenthetical about preconditions is long; consider tightening for clarity.
- [VISUAL] Minor: duplicated comment about avoiding inline math in captions appears twice (lines 430 and 533). Not harmful but redundant; consider keeping a single guidance comment.

### lecture_2_part_ii.tex
- [OTHER] Line 3: Pronoun ambiguity — "places it on the core supervised path." It's unclear what "it" refers to (the chapter, the toolkit, or the extension). Consider replacing "it" with a specific noun.
- [DEDUP] Lines 5–16, 24–30, 197–202, 222–224: Repetitive templating — many short tcolorbox "summarybox"/notes appear in quick succession. This fragments the narrative and leads to repeated high‑level content (objectives/motifs/notes). Consider consolidating or varying box content/placement.
- [MATHFMT] Lines 35–38 vs. 206–207: Redundant statements — both places define the binary classification goal / probability π(x). These repeat the same idea and interrupt flow; merge or remove one instance.
- [NOTATION] Line 22: Notation clarity — "switching to \(y_{\pm1}=2y-1\)" is terse and might confuse readers unfamiliar with this shorthand. Consider writing "we may use y_{±1}=2y−1 (i.e., map {0,1} to {−1,+1}) when convenient."
- [MATHFMT] Lines 210–220 and 222–224: Repetition — the Author's note (222–224) restates the linear‑logit explanation already given in 210–220. This is useful as an aside but feels redundant immediately after the formal development; consider moving or shortening the note.
- [VISUAL] Lines 105–123 vs. 178: Inconsistent class labeling — the plots and legend use "Class $\mathcal C_0$ / $\mathcal C_1$" (lines 105, 109, 117, 123), but the caption (line 178) refers to predicted classes "R0 and R1". Use consistent labels/formatting across figures and captions.
- [VISUAL] Line 132–134 and Line 183: Disjoint figure references — the text refers to figures (\Cref{fig:lec2_sigmoid_bce} at line 132 and \Cref{fig:lec1_mle_map} at line 183) with little connective exposition. The sentence at line 183 ("...provides the low-data MAP-versus-MLE comparison used in this discussion.") sits isolated between blocks; integrate these references more smoothly into the surrounding narrative so the reader understands why each figure is introduced.
- [MATHFMT] Line 178: Minor phrasing — "left/right regions map to predicted classes R0 and R1." Consider "the left and right regions correspond to predicted classes R0 and R1" for grammatical clarity.
- [VISUAL] General: small stylistic consistency points — inline math in captions/legend (various places) is sometimes plain text (e.g., "R0") and sometimes TeX math (\(\mathcal C_0\)); choose a consistent style for class names in figures and captions.
- [VISUAL] Repetitive caption phrasing: many figure captions end with the near-identical sentence "Use it when …" (lines 371, 384, 441, 473, 524, 552). Consider varying or moving this guidance to a single explanatory note to avoid templated repetition.
- [VISUAL] Repeated source comment: the inline comment "% Avoid inline math in captions; it wraps poorly in some EPUB renderers." appears multiple times (lines 383, 440, 472). Either keep it once or remove duplicates.
- [VISUAL] Inconsistent figure-label prefixes: labels mix "lec1" and "lec2" (e.g., \label{fig:lec1_gd} line 372, \label{fig:lec2-logistic-boundary} line 385, \label{fig:lec1_mle_map} line 442, \label{fig:lec1-roc-pr} line 474, \label{fig:lec1_confusion} line 525). This inconsistency can confuse cross-references and maintenance.
- [MATHFMT] Missing comma after introductory clause (punctuation): line 463 reads "On highly imbalanced problems accuracy and AUROC can be misleading;…" — add a comma after "problems".
- [MATHFMT] Sentence fragments in table cells (clarity): table entries contain fragments rather than full sentences, e.g. "Useful when collecting more data is difficult." (line 558) and "Helps tree ensembles and linear models; pair with cross-validation to avoid overfitting." (line 559). Consider rephrasing to full sentences or combining with the prior clause for readability.
- [NOTATION] Inconsistent title capitalization in summary boxes: tcolorbox titles use mixed styles (e.g., "Risk \& audit" line 451, "Imbalance and thresholds" line 477, "Key takeaways" line 530, "Probability calibration" line 546). Pick and apply a consistent capitalization convention (Title Case or Sentence case).
- [LABEL] Heading/label punctuation: the boxed note "If you are skipping ahead." ends with a period but introduces a list — it should be "If you are skipping ahead:" (line 572).
- [MATHFMT] Awkward paragraph heading and phrasing: "\paragraph{Where we head next.}" uses a period (line 576) where a colon would be more appropriate, and the sentence "stacking nonlinear units then removes that linear ceiling and sets up multilayer networks plus backpropagation." is slightly awkward — consider rephrasing to "stacking nonlinear units removes that linear ceiling and sets up multilayer networks and backpropagation."
- [MATHFMT] Dense sentence that would benefit from splitting (clarity): the explanation of macro vs micro averaging (lines 461–462) is long and packed; splitting into two sentences would improve readability.
- [VISUAL] Slightly awkward table-caption wording: "(\Cref{chap:logistic} reference table)." (line 552) reads a bit clumsy — consider "reference table in \Cref{chap:logistic}" for smoother phrasing.
- [OTHER] If you want, I can provide suggested rewordings for any of the flagged lines.
- [VISUAL] Visual check note: `lecture_2_part_ii.tex` contains `\includegraphics`; verify caption/prose alignment against rendered figure crops.

### lecture_3_part_i.tex
- [MATHFMT] Line 22: Repetitive adjective use — "simple" appears three times in one sentence ("simple but powerful idea... many simple units... many simple connections"); consider rephrasing to avoid redundancy.
- [DEDUP] Lines 4 and 76–78: Redundant statements — both describe that the chapter introduces perceptrons/activation functions. Consider merging or deleting one to tighten the introduction/outline.
- [MATHFMT] Lines 199–213 vs. 276–283 (and 254–267): Duplication — the weighted-sum + threshold neuron is defined multiple times (Eqns. 199–202/206–213 and again 276–283 and summarized at 254–267). Consider consolidating these repetitions into a single, canonical presentation to improve flow.
- [MATHFMT] Lines 126–132 vs. 262–267 vs. 171–173: Contradictory convention for threshold at zero — the "Step Function (Heaviside)" item (lines 128–131) defines f(0)=0 (via x ≤ 0 → 0), the McCulloch–Pitts Heaviside (lines 262–267) sets f(0)=1 (z ≥ 0 → 1), and the notation tcolorbox (lines 171–173) declares H(0)=1. These conflict; pick and state a single convention consistently and update the examples/comments accordingly.
- [MATHFMT] Line 35 vs. line 120: Inconsistent quotation style — line 35 uses TeX-style quotes (``fires''), line 120 uses ASCII quotes ("fire"). Use a consistent quoting style (prefer LaTeX ``...''/'' for book text).
- [MATHFMT] Lines 28–33 / 41–46 / 217–221 / 298–302: Inconsistent bullet-list style/content density — some short lists are fine, but the structure repeats similar biological-to-abstract points in multiple places. Consider combining closely related short lists (e.g., the neuron parts list and the "Complexities and Unknowns" items) or adding brief transitions to justify separate lists.
- [MATHFMT] Lines 288–291: Informal bulleting style for logic-gate examples — examples use hyphen bullets (plain text) whereas surrounding material uses itemize/enumerate environments. For consistency and LaTeX semantics consider turning these into an itemize environment.
- [MATHFMT] Line 100: Minor clarity — the sentence introducing the "row-major (deep-learning) convention" is dense (many symbols and conventions in one paragraph). Consider splitting into two sentences or adding a short lead-in to help readers absorb notation (explicitly emphasize that capital/lowercase A/a denote batch/single example).
- [PUNCT] Line 184: Slightly long sentence — "Beyond competitive learning, unsupervised methods encompass... any setting where structure is inferred directly from the inputs." Consider breaking at the em dash or simplifying the tail for readability.
- [MATHFMT] Line 311 onward (intro to perceptron): Slightly abrupt segue from MP discussion to perceptron. A one-sentence connector emphasizing what changes (continuous inputs, learning algorithm) would smooth the transition (the paragraph does say this, but moving it earlier or making it explicit as the immediate bridge would help).
- [NOTATION] If you want, I can produce a marked-up version of the snippet with suggested edits (merged sections, consistent Heaviside convention, and quote fixes).
- [LABEL] Inconsistent cross-reference macro capitalization (mix of \cref, \Cref, \Crefrange): lines 328 (\cref), 341 (\Cref), 379 (\Cref), 428 (\Cref), 465 (\Crefrange), 483 (\Cref), 487 (\Cref). Pick one convention and apply throughout.
- [NOTATION] Notation rendered in plain text instead of math-mode / inconsistent styling in the proof sketch: - Line 345: "Let w(t)" — use math-mode and boldface (e.g., \mathbf{w}^{(t)}). - Line 350: "w*" and "gamma" in running text; should be \mathbf{w}^\star and \gamma. - Line 358: "T*gamma" uses asterisk-style multiplication rather than T\gamma; switch to math-mode.
- [DEDUP] Redundant repetition of the perceptron update: the same update appears multiple times (line 328, lines 336–337, and again at line 339). Consider consolidating to avoid repetition.
- [MATHFMT] Minor punctuation/spacing: - Line 328: stray space before the inline math \( \mathbf{w}\leftarrow ...\) (extra space after open parenthesis). - Line 341: missing comma — "When the data are not separable the algorithm..." → add comma after "not separable".
- [VISUAL] Ambiguous antecedent / pronoun in figure caption (line 428): "Use it when relating margin geometry..." — unclear whether "it" refers to the perceptron, the logistic model, or the figure. Rephrase to make the referent explicit.
- [OTHER] Potentially misleading statement about Adaline (line 449): "The perceptron and Adaline models are limited to linearly separable problems." This could confuse readers — Adaline (least-squares) does not require separability in the same sense as the perceptron. Rephrase to clarify the intended limitation.
- [LABEL] Ambiguous / misstated cross-entropy expression in Perceptron vs. logistic box (line 451): -\sum_i y_i\log\sigma(s_i)+(1-y_i)\log(1-\sigma(s_i)) — the leading minus appears to apply only to the first term as written. Add grouping brackets so the negative applies to both terms: -\sum_i[ y_i\log\sigma(s_i) + (1-y_i)\log(1-\sigma(s_i)) ]. Also clarify the label encoding used for this formula (y in {0,1}) since the chapter otherwise often uses y in {-1,+1}.
- [MATHFMT] Inconsistent notation / prose style in the proof steps: some step headings and sentences use informal ASCII-style symbols (e.g., "w*", "gamma", "T*gamma") instead of consistent LaTeX math. Apply math-mode consistently in numbered steps (lines 350–358).
- [LIST] Small stylistic nit: heading punctuation inconsistency — some paragraph headings end with a period (e.g., line 330 "Perceptron update from the signed margin.") while others (line 433 "Adaline model") do not. Consider making heading punctuation consistent.

### lecture_3_part_ii.tex
- [LABEL] Lines 262–264: The subsection header is broken and contains misplaced/duplicate \label commands: - Line 262: "\subsection{Deriving weight updates for the two\hyp{}" is cut mid-title. - Line 263: "\label{sec:mlp_deriving_weight_updates_for_the_two}neuron network}" finishes the title after the label—this is malformed. - Line 264: A second \label with a long duplicated name appears. Recommendation: merge into a single, correctly placed construct, e.g. \subsection{Deriving weight updates for the two‑neuron network}\label{...}.
- [MATHFMT] Line 36: "objective\(\rightarrow\)audit workflow" inserts a math-mode arrow inside running text. This produces atypical spacing and looks out of place; prefer a text arrow or plain punctuation (e.g., "objective→audit workflow" or "objective→audit workflow" using a text symbol) or rephrase.
- [DEDUP] Lines 8–17, 19–21, 115–117, 249–251, 318–320: The repeated use of small boxed "Author's note"/"summarybox" elements (and similar boxed pedagogy) interrupts narrative flow. Consider reducing frequency or consolidating some notes to avoid templated repetition and flow breaks.
- [VISUAL] Lines 81, 178, 228: The same code comment "% Avoid inline math in captions; it wraps poorly in some EPUB renderers." is repeated in each figure environment. This duplicated comment in the source is redundant; either keep one global comment near figure/style guidance or remove repeats to reduce noise.
- [LIST] Line 59: "We will reuse \Cref{fig:mlp_minimal_chain} as the bookkeeping diagram when we apply the chain rule." Minor stylistic nit: consider "when applying the chain rule" (remove "we") for slightly tighter prose.
- [MATHFMT] Line 36 and line 37–41 (short paragraph transition): The sentence "How this chapter fits the workflow." followed by "The same objective→audit workflow from the supervised toolkit still applies; what changes is the representation." is concise but a little abrupt. Consider a one-sentence transition that explicitly names the workflow steps to orient readers who skip earlier chapters.
- [MATHFMT] Line 6: Opening sentence "In this chapter we keep the story linear and concrete." reads well, but "linear and concrete" could be misread (linear as opposed to nonlinear). If the intent is "kept simple and concrete", consider rephrasing to avoid potential ambiguity with "linear".
- [MATHFMT] General: several boxed pedagogical notes (summarybox, Author's note) appear close to one another and sometimes duplicate the same point (e.g., forward-pass caching appears in both main text and a box). Consider consolidating overlapping content to streamline exposition and avoid repetition.
- [LABEL] Lines 333–335: The subsection heading is split awkwardly across lines with a \label inserted inside the title braces (line 334). There is also a second, stray/duplicate \label on line 335. This is confusing and may break referencing/TOC behaviour — keep a single \label immediately after the \subsection command (outside the title text) or at least remove the duplicate.
- [DEDUP] Lines 350–366 vs. 368–382 (and 359–366): Repetitive templating — the main "Summary" bullets (350–357) repeat much of the same content that appears again in the "Derivation closure" box (359–366) and the "Key takeaways" box (368–374). Specific duplicates: the two-neuron/backprop pattern appears at lines 356 and 373; the hard-threshold vs smooth-activation point appears at lines 354 and 372. Consider consolidating or pruning to reduce redundancy.
- [MATHFMT] Lines 351, 356, 373, 387: Inconsistent hyphenation/markup for the same terms. The text alternates between "two\hyp{}neuron" (lines 351, 356, 387) and the literal "two-neuron" (line 373). Similarly "multi\hyp{}layer" appears earlier. Choose one convention (preferably a single macro or literal hyphen) and apply it consistently.
- [NOTATION] Lines 344, 359, 368, 384: Inconsistent capitalization/style in tcolorbox titles ("Author's note: what backprop adds" vs "Derivation closure: implement, cache, fail-fast" vs "Key takeaways" vs "Exercises and lab ideas"). Pick a consistent title-case or sentence-case convention.
- [MATHFMT] Line 362: Awkward phrasing — "so each gradient term is a local reuse, not a re-derivation." The article "a" makes the phrase clumsy; consider rewording (e.g., "so each gradient term is reused locally rather than re-derived").
- [OTHER] Line 330: The adverb "slightly" ("gradient descent increases $w_2$ slightly") is vague. If precision is desired, quantify the change (or remove the qualifier).
- [NOTATION] Lines 391–392: The bold lead-in "\textbf{If you are skipping ahead.}" is a sentence fragment; consider merging into the following sentence ("If you are skipping ahead, be able to read...") for grammatical flow.
- [OTHER] No other concrete editorial issues spotted in the provided range.

### lecture_4_part_i.tex
- [NOTATION] Inconsistent layer indexing: - Line 32 states layers are indexed by l = 1,...,L (input not included). - Line 62 says l = 0 is the input layer. (Conflict between these two descriptions; pick one convention and apply consistently.)
- [NOTATION] Inconsistent definition of weight superscript: - Line 32: "weights connecting neuron i in layer l-1 to neuron j in layer l are denoted by w_{ij}^{(l)}." - Line 137: "weights connecting layer l to layer l+1 ... w_{ij}^{(l)}." - (These two usages imply different meanings for the superscript (l). Choose one convention and make it consistent.)
- [MATHFMT] Incomplete sentence / abrupt cut: - Lines 86–87: "The output layer activations $a_k^{(L)}$ are compared to the" - (Sentence is unfinished; add the missing phrase, e.g., "targets" or rework the sentence.)
- [LABEL] Redundant / repeated derivation: - The core output-layer and weight-gradient derivations are presented twice: - First pass: chain-rule derivation and δ definitions around lines 153–177 and 187–229. - Second pass: "Detailed Derivation" repeating essentially the same material from lines 237–304 (including eqs. 243–304). - (This duplication interrupts narrative flow; consolidate the two derivations or cross-reference the earlier one.)
- [NOTATION] Mixed notation for activation and activation-derivative symbols: - Examples: line 37 uses f(·); line 199 uses φ'; line 264 says "Assuming the activation function f is the sigmoid"; line 229 refers to "sigmoid activations φ". - (Unify the symbol for the activation function across the section.)
- [MATHFMT] Mixed names for neuron outputs / activations: - Lines 32–83 use a_j^{(l)} for activations; lines 237–319 introduce o_k, a_k, x_j, sometimes interchangeably (e.g., line 237 "output o_k and activation a_k"). - Line 316–319 uses o_j(1−o_j) while earlier material uses a_j and φ'. - (Pick a single symbol for activation/outputs (e.g., a) and use it consistently; avoid introducing o and a for the same quantity.)
- [MATHFMT] Possible incorrect wording causing ambiguity: - Line 182: "The term \(\delta_j^{(l+1)}\) measures how sensitive the error is to changes in the net input \( a_j^{(l+1)} \)." - (Here "net input" should be z_j^{(l+1)}, not a_j^{(l+1)}; this is a clarity/notation bug.)
- [MATHFMT] Awkward phrasing / unclear metaphor: - Line 27: "making it practical to learn hidden representations (not just tune a final linear layer) while keeping the same validation\(\rightarrow\)audit discipline (learning curves, early stopping, and slice checks)." - (The "validation→audit discipline" phrasing is unclear—consider rephrasing to "maintaining the same validation/audit discipline" or similar.)
- [BOX] Small clarity suggestion in Design motif box: - Line 16: "The organization (cache forward values, then sweep backward) is the algorithm." - (Consider "cache forward-pass values" or "cache forward-pass intermediates" to make "forward values" more specific.)
- [LABEL] Minor stylistic consistency: - Equation/term naming alternates between "squared-error", "squared\hyp{}error", and "SE"; consider consistent terminology and labels across the section.
- [NOTATION] If you want, I can provide a concise rewrite of the repeated derivation, unify notation, and fix the incomplete sentence to restore flow.
- [MATHFMT] Inconsistent weight-indexing convention (possible notation clash): earlier you state "weight update for weights \(w_{ij}\) feeding into neuron \(j\)" (line 323) but later use \(w_{kj}\) and explicitly say " \(w_{kj}\) denotes the weight from neuron \( j \) to neuron \( k \)" (lines 515–518). These two descriptions imply different index meanings and are likely to confuse readers — reconcile the index order/description. (Lines: 323; 515–518)
- [MATHFMT] Sentence fragmentation / punctuation error around the sigmoid derivative: the sentence "where \( e_j \) is the error at neuron \( j \), and \[\sigma'(z) = \sigma(z)(1 - \sigma(z)).\] is the derivative of the sigmoid function." incorrectly splits across the displayed equation so that "is the derivative…" becomes a sentence fragment. Rework punctuation/ordering. (Lines: 502–506)
- [NOTATION] Inconsistent notation for activations: the numerical example uses \(a^{(1)}, a^{(2)}\) (lines 459–462) while the squared-error aside switches to \(y, y_j, y_{\text{out}}\) (lines 486–511, 497–515). This inconsistency can confuse readers; choose one symbol set or note the equivalence where the aside begins. (Lines: 456–462; 486–515)
- [DEDUP] Repetitive/fragmented "remarks" and summary patterns: the material uses many small boxed summaries and "Remarks"/"Aside" paragraphs (e.g., summary box at 344–346, checklist box at 437–445, mini-batch box at 559–571, Remarks at 573–579 and again at 596–601). The repetition fragments the narrative flow; consider consolidating or ordering these elements so related commentary appears together. (Examples: 344–346; 437–445; 559–571; 573–579; 596–601)
- [MATHFMT] Minor clarity/wording issue in optimizer note: "momentum and Adam/AdamW from \Cref{chap:cnn} accelerate convergence. Add L2 weight decay to the gradient or decouple it (AdamW) to avoid biasing adaptive steps." (line 344–346) — phrasing is slightly terse/ambiguous (e.g., "Add L2 weight decay to the gradient" reads awkwardly). Consider clearer phrasing; as written it may momentarily slow reader comprehension. (Lines: 344–346)
- [MATHFMT] Small redundancy in the epoch procedure: steps list for one epoch explicitly starts with "Present the first input pattern…" then step 5 says "Repeat steps 1–4 for all training patterns." The phrasing is functional but slightly clunky; the loop could be expressed more directly to improve flow. (Lines: 586–592)
- [MATHFMT] If you want, I can propose concise rephrasings for any of the flagged items.
- [MATHFMT] Line 659: Awkward parenthetical and long sentence. "As a representative example (illustrative; depends on initialization and the training recipe), ..." reads clunky — consider rephrasing the parenthetical (or moving caveat after the sentence) and splitting the long sentence for clarity.
- [DEDUP] Lines 683–687: Inconsistent indentation/templating of \item entries in the "Limitations" list (first \item is less indented than the next two). This looks like unintended nesting/formatting drift in the source.
- [MATHFMT] Line 676 vs 827 (and elsewhere): Inconsistent heading/title casing. "Summary:" (line 676) and "Applications of Multi-Layer Perceptrons" (line 661) use Title Case, while "Comparing canonical nonlinearities" (line 827) uses sentence case; pick a consistent style.
- [MATHFMT] Line 811–813: Passive voice: "An example was provided illustrating..." Prefer active voice ("We provided an example..." or "The following example illustrates...") for clearer exposition.
- [MATHFMT] Line 887: Minor clarity issue about ReLU derivative: "(take \(0\) at the origin)" — better to state explicitly that the derivative is undefined at 0 and that 0 is adopted by convention (or state the convention used) to avoid ambiguity.
- [MATHFMT] Line 889–891: Long, compound sentence with several ideas (saturation, dying ReLUs, remedies). Consider splitting into two sentences for readability (one diagnosing the issue, one listing remedies).
- [MATHFMT] Lines 898 & 906: Inconsistent hyphenation of "learning-rate" (line 898 uses "learning\hyp{}rate", line 906 uses "Learning-rate"). Standardize hyphenation/markup for "learning-rate" throughout.
- [MATHFMT] Lines 928–934: Inconsistent item nesting in the "Exercises and lab ideas" tcolorbox. The third \item ("Re-derive one core equation...") appears indented as a subitem but reads like a top-level exercise. Check intended nesting and adjust.
- [BOX] Line 895–909 (Key takeaways box): Tone/register is slightly informal in spots ("Minimum viable mastery", "audits matter"); consider tightening language to match the rest of the chapter’s formal register.
- [VISUAL] Line 806 (figure caption) and line 882 (activation figure caption): Imperative phrasing ("Use it when implementing backprop...", "Use it when choosing an activation...") is fine but slightly prescriptive for a caption; consider rewording to descriptive captions (e.g., "Shows forward/backward flows..." / "Activation functions and their derivatives.") for consistency.
- [TRANS] Line 936 and 938–939: Sentence fragments / punctuation: "If you are skipping ahead." and "Where we head next." are sentence fragments followed by the actual instruction/sentence. Combine or re-punctuate (for example: "If you are skipping ahead, keep one practical habit: ..." and "Where we head next: \Cref{chap:rbf} introduces ...") to improve flow.
- [MATHFMT] Line 659 and elsewhere: Numeric formatting: "2{,}000" uses an explicit LaTeX comma macro; scan for consistent numeric formatting conventions throughout the chapter (some numbers are plain "5", "0.1\%", etc.). (Not strictly an error here but worth standardizing.)
- [TRANS] These points are limited to editorial/narrative and formatting issues observed in the requested range.

### lecture_4_part_ii.tex
- [LABEL] Repetition / redundancy - Lines 27–34 vs. 46–55 vs. 167–171: the architecture (three layers / what each layer does) is described multiple times in close succession. Consider consolidating to avoid duplication. - Lines 48–50 vs. 253–257: the design-matrix / Phi notation is introduced twice. Merge or cross-reference the earlier boxed notation to avoid repeating identical definitions. - Lines 226–237 vs. 272–275: the role/definition of the transformation g(·) and examples of transformed points are repeated. Either consolidate or clearly signpost that the later section is a worked example.
- [LIST] Inconsistent formatting of short lists - Lines 22–25 and many places use itemize environments, but Lines 230–236 and 239–245 use bare dash-prefixed lines for the “Example Setup” and “Assumptions.” Replace the dash lines with an itemize/enumerate environment for consistency.
- [VISUAL] Narrative / transition awkwardness - Line 38: "here we keep the bases explicit, then connect to the dual/kernel view later in the chapter." The comma + "then" construction reads slightly informal/awkward. Suggest "and then connect" or "and later connect". - Lines 95–99: the flow from the captioned architecture figure into "A picture to keep in mind" is fine, but the chapter returns to very similar descriptive material later (see repetition note). Consider reordering so the high-level description appears once, then figures/intuition immediately follow.
- [NOTATION] Punctuation / sentence-fragment issues after displays - Lines 179–186 (display of G(x)) followed by Line 187: sentence begins "where each G_i(...)" with a lowercase "where" after the display. Either attach the clause to the preceding sentence (comma + "where...") or capitalize "Where" to start a new sentence. - Similar style note where displays are followed by continuation clauses; scan for consistent treatment.
- [MATHFMT] Typo / malformed punctuation - Line 284: "overlap with height \(\exp(-\bar{r}^2/(2\sigma^2))\approx 0.5\)--0.7;" — the fragment "0.5\)--0.7" is malformed. Likely intended "≈ 0.5–0.7" (use an en-dash or range markup) or "≈ 0.5–0.7" inside math; fix the stray backslash/parenthesis and dash.
- [VISUAL] Inconsistent spelling - Line 41 and many locations: "centers" (US spelling). Line 127 uses "centres" (British). Line 160 caption returns to "centers." Pick one spelling and standardize.
- [VISUAL] Repetitive caption templating / voice - Figures’ captions repeatedly end with "Use it when ..." (Lines 91, 122, 160). This repeated phrasing becomes a templated refrain; vary the phrasing or shorten captions to avoid repetitive voice.
- [LABEL] Minor clarity / style suggestions - Line 216: the "Universal approximation" bullet includes citations inline; consider a slightly expanded sentence or smoother transition before the citation for readability. - Line 301: the boxed "Author's note" references \Cref{fig:rbf_sigma_sweep} which is not present in this snippet. Ensure that the forward reference exists and is introduced before the note if readers might skip ahead.
- [VISUAL] If you want, I can propose a compact reordered outline that removes the duplications and standardizes list/caption phrasing.
- [MATHFMT] Lines 391–394: sentence fragment — the displayed equation (line 389–394) is followed by "where" starting a new sentence fragment ("where ..."); this should be attached to the preceding sentence or rephrased for grammatical completeness.
- [SPELL] Lines 414 vs. 452: inconsistent spelling of the same concept — "Regularization" (line 414, American) vs. "regulariser" (line 452, British). Pick one spelling and use it consistently.
- [VISUAL] Lines 352, 561: the same authorial comment "Avoid inline math in captions; it wraps poorly in some EPUB renderers." appears twice. Consider removing the duplicated comment.
- [VISUAL] Figure-caption phrasing repetition / templating: captions end with author-directed advice ("Use it when ...") in multiple figures (lines 353, 448, 562). This repeated instructional template feels formulaic and breaks the flow of captions; consider varying or removing these asides.
- [VISUAL] Lines 353, 562, 448: inconsistent presentation of σ in captions — sometimes spelled out as "sigma" (plain text) instead of using the math symbol \(\sigma\) used in the body. Either consistently use the symbol or adopt a clear caption convention (the inline-math comment suggests avoiding math in captions; if so, make that consistent).
- [MATHFMT] Lines 359, 588–590: inconsistent heading/title casing and punctuation. Examples: "\paragraph{Notation note.}" (line 359, lower-case 'note' + period), "\subsection*{Optional sidebar: Wiener filter refresher}" (line 588), and "Sidebar: why include Wiener filtering here?" (line 590, lower-case 'why'). Choose a consistent style (sentence case vs Title Case) and punctuation for these small headings.
- [OTHER] Lines 396–397 and 452–456: inconsistent indentation/leading spaces in source (some paragraphs/blocks are indented while surrounding text is not). This is an editorial/formatting noise that makes the source harder to scan.
- [NOTATION] Lines 481–493 vs. surrounding prose: inconsistent notation between pseudocode and body. The verbatim pseudocode uses "phi" and "Phi" in a plain-text style (line 491), while the main text uses \(\varphi_i(\cdot)\) and \(\Phi\). This may confuse readers—consider matching notation more closely between prose and pseudocode.
- [LABEL] Line 353: slight pronoun ambiguity — "Validation curves ... guide model size and regularization; they also motivate tuning sigma ..." The pronoun "they" could be clearer if it explicitly referenced "validation curves."
- [OTHER] If you want, I can suggest specific rewordings for any of the above items.
- [NOTATION] Line 648: Paragraph title "Optional: why adaptive filtering comes next" uses sentence-style lowercase ("why") inconsistent with the Title Case used elsewhere. Suggest "Optional: Why Adaptive Filtering Comes Next".
- [NOTATION] Line 684: Paragraph title "Where we head next." ends with a period and uses inconsistent capitalization. Remove the terminal period and use consistent Title Case (e.g., "Where We Head Next").
- [MATHFMT] Lines 646 & 655: Minor repetition of the word "frequency" in "frequency-selective operator that emphasizes frequencies..." (line 646). Consider tightening to avoid redundancy (e.g., "emphasizes components" or rephrasing).
- [OTHER] Line 661: Phrase "regularization cures conditioning." is colloquial and vague. Prefer "regularization improves numerical conditioning" or "regularization remedies ill‑conditioning."
- [STYLE] Line 668: "without regularization, solves can be numerically unstable" — the noun "solves" is awkward/ambiguous. Replace with "solutions", "linear solves", or "solving linear systems" depending on intent (e.g., "the solution can be numerically unstable" or "linear solves can be numerically unstable").
- [MATHFMT] Line 681: The bold lead-in "\textbf{If you are skipping ahead.}" ends with a period and then continues with explanatory text. Better typographically as a lead-in with a colon: "\textbf{If you are skipping ahead:}".
- [MATHFMT] Lines 657–673 (boxed headings): Inconsistent capitalization/style across boxed headings and subheadings ("Key takeaways", "Minimum viable mastery", "Common pitfalls", "Exercises and lab ideas"). Adopt a single convention (Title Case or sentence case) and apply it consistently.
- [LABEL] Line 675: "two-moons dataset" — consider consistent naming convention (many references use "two moons" without the hyphen). This is optional.
- [PUNCT] Line 676: Inconsistent thousands formatting in "N\in\{200,2000,20\,000\}" (commas for some numbers, thinspace for 20,000). Use a consistent style for thousands separators.

### lecture_5_part_i.tex
- [MATHFMT] Repetition — dimensionality-reduction material appears twice: lines 117–166 ("Dimensionality Reduction: Simplifying High-Dimensional Data") and lines 169–181 ("Dimensionality Reduction and Feature Mapping") substantially overlap. Consider merging or removing one section to avoid redundancy.
- [LABEL] Repetition — BMU / winner definition is duplicated in three places: lines 225–227 (eq. (eq:bmu)), lines 259–262, and lines 316–319 (eq. (eq:winner_neuron)). Keep a single canonical definition and reference it elsewhere.
- [DEDUP] Repetition — high-level architecture / input–output description is repeated: lines 201–206 ("Conceptually, the SOM consists of two stages:") and lines 303–309 ("Network Structure"). Consolidate to avoid repeating the same bullet points.
- [DEDUP] Repetitive templating — many short summary tcolorboxes state overlapping points (Learning Outcomes: 9–15; Design motif: 17–19; Historical intuition: 33–35; Author's note: 37–39; SOM at a glance: 188–193). These are useful but feel repetitive; consider consolidating or ensuring each box has a clearly distinct purpose.
- [VISUAL] Inconsistent math typography in captions/commentary: line 290 comments to "Avoid inline math in captions" but the figure caption at line 291 uses plain "sigma(t)" rather than \sigma(t) or otherwise consistent math formatting. Be consistent with the stated policy (either avoid math in captions or use LaTeX math consistently).
- [MATHFMT] Long, dense sentences hurting clarity: - Line 165 (single long sentence describing PCA/MDS/t-SNE/UMAP/SOM) — consider breaking into two sentences for readability. - Line 230 (sentence explaining choice of norm and alternative metrics) is long and contains several parenthetical remarks; consider splitting and simplifying.
- [VISUAL] Minor punctuation/spacing consistency: - Line 5: "Cref{chap:rbf}" — missing backslash? (Probably \Cref used elsewhere; ensure consistent capitalization of \Cref vs Cref.) — if this is intentional it's fine; confirm consistent macro usage across the file. - Lines 61–64: tikz \node labels "large steps"/"small steps" are placed inline with text; they may overlap in figure rendering — not a prose issue per se but can affect clarity in the PDF. (If you prefer strictly prose issues, remove this bullet.)
- [VISUAL] Stylistic/instructional phrasing in figure captions: captions at lines 76 and 158 end with "Use it when ...". That imperative tone is repeated and feels more like author notes than standard captions; consider rephrasing captions to state the point succinctly and move "use when" advice to the main text or margin notes.
- [LABEL] Minor wording awkwardness: - Line 301: "Building on the inspiration from perceptrons, Kohonen Self-Organizing Maps (SOMs) introduce..." — "the" before "inspiration" is slightly awkward; consider "Building on inspiration from perceptrons," or "Inspired by perceptrons, Kohonen...". - Line 95: "represented only by their feature vectors without labels." Consider rephrasing for flow: "represented only by their feature vectors (no labels)."
- [DEDUP] If you want, I can propose concrete edits (merged text and rewordings) for any of the duplicated sections or the long sentences listed above.
- [PUNCT] Line 327: Sentence ends with a comma immediately before an itemize environment ("...,") — use a colon or restructure the sentence for clearer punctuation.
- [PUNCT] Line 353: Extra space after the opening inline-math delimiter: "\( \mathbf{w}_i^\top \mathbf{x}\)". Remove the leading space for consistent inline-math spacing.
- [MATHFMT] Lines 349–352 vs. 402–412: The dot-product / distance similarity definitions are repeated verbatim in two places; consider consolidating to avoid redundancy.
- [MATHFMT] Lines 350 vs. 372: Inconsistent transpose notation — equation uses \top (line 350) whereas the bullet uses ^T (line 372). Pick one notation and use it consistently.
- [LABEL] Lines 325 (eq:som_weight_update) and 513 (eq:wta_weight_update): The weight-update rule is presented twice in close succession (full SOM update and WTA update) with little distinction; either cross-reference the first instance or consolidate to reduce repetition.
- [DEDUP] Lines 386–390 vs. 458–471 and 502–515: Material on WTA/competitive learning is duplicated across multiple subsections ("Key Properties", "Winner-Takes-All Learning and Weight Update Rules", and "Winner-Takes-All Learning Recap"). The "Recap" (starting line 502) appears after a numerical example (lines 473–496), which is an awkward ordering — consider merging the recap with the initial treatment or moving it before the example.
- [DEDUP] Lines 391 and 500: The comment "% Chapter 9 (continued)" appears twice; remove the redundant occurrence.
- [MATHFMT] Lines 353 and 498: Inconsistency in vector orientation/representation — earlier you state "\(\mathbf{w}_i\) and \(\mathbf{x}\) are column vectors" (line 353), but the initial weight matrix \mathbf{W}(0) is presented with each row containing \(\mathbf{w}_j(0)\) (line 498). Clarify the convention or explicitly state that the matrix rows are shown for compactness.
- [MATHFMT] Line 427 / 441 and elsewhere: Multiple displayed equations are followed by sentence fragments beginning with "where..." in lower case. This is acceptable, but stylistically inconsistent — either make these standalone sentences (capitalize "Where") or ensure they read as continuations (use commas) for uniform style.
- [VISUAL] Lines 552, 595, 625 (figure captions): Tone is somewhat informal / imperative ("Use it when..."); consider switching to a more formal descriptive voice suited to a textbook.
- [VISUAL] Line 624 comment vs. caption (line 625): Comment advises avoiding inline math in captions, but the caption immediately follows with "p log p" in plain text — consider typesetting the expression consistently (e.g., \(p\log p\)) or rephrasing to avoid ambiguity.
- [MATHFMT] Line 636 (tcolorbox start): Opening sentence reads colloquially ("pick a best-matching unit (BMU), nudge it and its neighbors, move on."). Consider more formal phrasing for a textbook (e.g., "select the BMU, update it and its neighbors, then proceed to the next sample.").
- [LABEL] Overall: Several nearby sections reintroduce the same core concepts (similarity measures, BMU selection, weight update, learning-rate decay). Consider tightening the narrative by introducing each concept once (with a clear cross-reference) and removing near-duplicate expositions to improve flow and reduce repetition.
- [TITLE] If you want, I can propose a concrete reordering / consolidation plan (which sections to merge and what sentences to keep/remove) to address the redundancies.
- [PUNCT] Line 651: Paragraph title punctuation inconsistent — "\paragraph{Stopping criteria.}" includes a trailing period. Other paragraph titles (e.g., lines 801, 807) do not. Make heading punctuation consistent (keep or drop trailing periods).
- [LABEL] Lines 716 vs 807: Inconsistent cref capitalization — you use \Cref at line 716 and \cref at line 807. Pick one style for cross-references for consistency.
- [MATHFMT] Line 803: Missing comma after introductory phrase: "In practice the neighborhood..." → "In practice, the neighborhood..."
- [VISUAL] Lines 702, 791, 893: Repetitive caption phrasing and ambiguous pronoun "it". Each caption ends with "Use it when ...". This is repetitive and the referent ("it") can be ambiguous — prefer "Use this figure/criterion/plot when ..." and vary phrasing across captions.
- [MATHFMT] Line 702: Awkward phrasing: "Use it when deciding where to stop training based on stability, not only final error." Consider "based on stability rather than on final error" for clarity.
- [MATHFMT] Line 893: Minor grammatical omission: "Use it when reading U-Matrices as boundary hints, not absolute distances." → add "as": "not as absolute distances."
- [VISUAL] Lines 759, 778, 916 (and elsewhere): Inconsistent capitalization/style in figure titles (e.g., "Hard BMU regions", "Soft assignments", "Plane: pixel 1"). Decide on a capitalization convention (Title Case vs sentence case) and apply it consistently for figure titles.
- [MATHFMT] Lines 918–944 (and similar matrix tables at 862–887, 946–960): Inconsistent indentation/whitespace in the numeric tables. The mixed indentation makes the LaTeX source harder to scan/edit; align or normalize indentation for readability.
- [NOTATION] Repetitive templating in the TikZ/pgfplots blocks (multiple near-identical matrix plots and data tables): consider factoring repeated plot settings or data into a macro or external data file to reduce duplication and simplify maintenance (e.g., the matrix-plot table blocks at lines ~862–887 and ~918–944).
- [VISUAL] Line 892: There is an inline comment "% Avoid inline math in captions; it wraps poorly in some EPUB renderers." If this is an editor's note for collaborators keep it; otherwise consider removing or converting to a TODO so it doesn't remain as stray commentary in final source.
- [MATHFMT] Repetition / redundant exposition: - The weight-update and neighborhood-function formulas are presented multiple times with little added value (first at 1016–1020, then restated at 1094–1098, and again at 1110–1114). Consider consolidating to a single clear presentation and referring back to it. - The procedural training steps are repeated in several forms: the short enumerated list (1083–1088), the detailed pseudocode tcolorbox (1138–1152), and the “Stages vs. Steps” discussion (1171–1178). These overlap heavily — streamline to avoid templated repetition.
- [MATHFMT] Inconsistent notation and style: - Vector vs scalar notation is inconsistent. The main update equations use bold vectors (e.g., 1018, 1096) but the “Minimum viable mastery” item uses scalar/unbolded notation (1233). Choose one convention and apply it consistently. - Neighborhood-function indexing varies: h_{j c}(t) (1018), h_{j, c}(t) (1096), and h_{ci}(t) (1233). Standardize the subscript formatting and ordering.
- [NOTATION] Spelling inconsistency: - “stabilizes” vs “stabilises”: American spelling with -z at 1087 and British spelling with -s at 1168. Pick one spelling convention globally.
- [VISUAL] Caption tone / voice: - Figure captions include imperative instructions (“Use it when diagnosing…” at 1012 and “Use it when visualizing…” at 1073). Captions are usually descriptive; consider rephrasing to a neutral description or moving directives into the main text.
- [MATHFMT] Minor punctuation / phrasing issues: - Missing conjunction and spacing in the tcolorbox step: “Decay \(\alpha(t),\sigma(t)\).” at 1165 — better: “Decay \(\alpha(t)\) and \(\sigma(t)\).” - Recipe fragment lacks parallel structure at 1206: “\(\sigma_0\) equal to the map radius, decaying to 1--1.5 cells.” Consider “Set \(\sigma_0\) equal to the map radius, and decay it to 1–1.5 cells.” - Awkward phrasing at 1221: “stop when QE/TE on a validation split flatten.” Consider “stop when QE and TE on a validation split flatten out” or “...reach a plateau.”
- [LABEL] Dense / run-on sentence with multiple references: - Line 1214 packs several chapter references and ideas into one sentence; split for clarity: “SOMs learn prototypes like the centers in \Cref{chap:rbf}, but add a topographic prior. Quality diagnostics (QE/TE) can be tracked with the validation-curve tools in \Cref{chap:supervised}. For task-driven embeddings see \Cref{chap:cnn,chap:nlp}; \Cref{chap:hopfield} contrasts retrieval dynamics.”
- [MATHFMT] Miscellaneous clarity suggestion: - The “Stages vs. Steps” section (1175–1187) repeats the stage names already mentioned earlier (1139–1152 / 1171). If you keep both, make the second occurrence explicitly referential (e.g., “As summarized above, the three conceptual stages are: ...”) to improve narrative flow.
- [MATHFMT] If you want, I can propose a concise reorganization that merges the duplicated formulas and procedural steps into a single streamlined presentation.

### lecture_5_part_ii.tex
- [MATHFMT] Repetition / redundant material - Lines 130–137 and 141–156: The energy function is introduced twice in quick succession (section "Energy Function and Stability" and then "Hopfield Network States and Energy Function") with overlapping text. Consolidate into a single, canonical presentation. - Lines 281–285 repeat the energy definition again later ("Energy Function and Convergence..."). Consider defining E once and referring back to it to avoid duplication. - Lines 46, 14–16, and 37–44 (three tcolorbox summaryboxes) restate the same design intuition about symmetry/stability multiple times. These boxes are useful, but their content overlaps; either merge or make each box serve a clearly distinct purpose.
- [LABEL] Structural / narrative flow - Lines 4–24: The transition from SOMs (line 4) to Hopfield networks is abrupt; a one-sentence bridge summarizing why Hopfield is the next logical topic (e.g., contrasting goals or applications) would improve flow. - Lines 176–194 / 190–194: The pseudo-code box (lines 180–192) appears before the formal derivation of ΔE (lines 293–314). This forward reference is functional, but it interrupts the logical flow; consider moving the pseudo-code after the ΔE derivation or adding a short forward pointer explaining that a formal proof follows. - Lines 80 vs. 61: The indexing convention for w_{ij} is stated twice (line 61 and again line 80). Keep one clear statement (preferably the concise one at line 61) and remove the later repetition.
- [LABEL] Cross-references / ordering issues - Line 191 references \eqref{eq:deltaE} and \eqref{eq:energy_function} before those equations are defined in the text. Forward equation references are acceptable in LaTeX, but they can confuse readers; consider reordering or adding a parenthetical note ("see Sec. ... below") so the reader knows the formal proof is forthcoming. - Multiple similar equation labels exist (e.g., eq:hopfield_energy_general at line 136 and eq:energy_function at line 283) for essentially the same formula. This risks confusion—use a single label for the canonical energy equation.
- [VISUAL] Punctuation / typographic consistency - Line 21: "static input\(\rightarrow\)output mappings" uses an inline math arrow without surrounding spaces; prefer a textual arrow or spaced notation ("input → output" or "input→output") for readability. - Line 21: "feedback\hyp{}driven" uses a \hyp{} construct while later uses of hyphenation use plain hyphens or em-dashes (line 23 uses ---). Standardize hyphen/em-dash usage across the chapter. - Quotation marks are inconsistent: - Line 15 uses ``feedback'' (typographic quotes), - Line 101 uses straight double quotes around "fires". Replace straight quotes with TeX typographic quotes (`` ... '') for consistency. - Lines 236 and 268: Both captions include the parenthetical note "% Avoid inline math in captions; it wraps poorly in some EPUB renderers." This comment appears twice; remove one or place it in a single location.
- [MATHFMT] Clarity / prose precision - Line 80: "so column indices correspond to presynaptic neurons." This is correct but terse; some readers may find "column index j corresponds to presynaptic neuron j (weight from j to i)" clearer—consider rephrasing to make the mapping explicit. - Line 138: "so removing it would scale the energy by two." This is mathematically correct but may invite questions about consequences; consider briefly noting that scaling the energy does not affect attractors/ordering (if that is the intended implication) or remove the remark if unnecessary. - Line 210–213: The inline arithmetic in the example is compact; adding a brief intermediate line or comment could help readers follow the numerical steps (optional).
- [NOTATION] Minor formatting / housekeeping - Lines 139 and 274: The comment "% Chapter 10 (continued)" appears twice in the source; remove redundant comments. - Table (lines 116–126): The indicator in the {0,1} update rule is written as \mathbf{1}[...]; choose one notation (e.g., \mathbb{I} or \mathbf{1}) and use it consistently throughout the book.
- [MATHFMT] If you want, I can produce a suggested reordering (single canonical energy definition, then ΔE proof, then pseudo-code and example) and a tightened list of merged tcolorbox texts to replace the current overlapping boxes.
- [MATHFMT] Repetition: the neuron update rule and/or energy-change derivation are restated multiple times. See the initial ΔE derivation and numeric check (lines 322–327), the explicit update rule (lines 347–354) and case analysis (360–367), and another restatement of the update and energy (lines 466–476). Consider consolidating to avoid redundancy.
- [OTHER] Contradiction / unclear allowance of synchronous updates: the text emphasizes that asynchronous updates guarantee monotonic energy decrease (line 373) and later argues synchronous updates can cause oscillations (lines 375–386), yet the statement "The network dynamics evolve asynchronously or synchronously according to the update rule" (line 465) reads as if synchronous updates are an equally valid option. Reword to avoid implying equivalence.
- [MATHFMT] Ambiguous phrasing: "Because the update chooses the sign of \( s_i^{\text{new}} \) to agree with the bracketed term" (line 366) — the phrase "agree with the bracketed term" is vague. Specify "agree with the sign of the bracketed expression" or similar.
- [MATHFMT] Vague sentence: "Revisiting states before all others have been updated can cause instability." (line 391) — what does "revisiting states" mean in this context? Clarify whether this refers to updating the same neuron multiple times within a sweep, or to choosing a non-deterministic update ordering.
- [DEDUP] Exact duplication: two consecutive sentences repeat the same information about off-diagonal entries and give identical examples (lines 517–518). Remove one of these redundancies.
- [MATHFMT] Inconsistent presentation of the energy function: the Lyapunov energy is given without thresholds in one place (lines 472–476: E = −½ ∑ w_{ij} s_i s_j) but later the energy used in the example includes threshold terms (line 524: E = −½ ∑ w_{ij} s_i s_j + ∑ θ_i s_i). Either state the general form once (including thresholds and the earlier special-case omission) or explicitly note when thresholds are being omitted for simplicity.
- [DEDUP] Repeated statistic / redundancy: the capacity result p ≈ 0.138 n is stated multiple times across the section (lines 398–402, 434–435, 493–494, 528–529). Consider introducing the number once with the relevant caveats and then referencing it, rather than restating it verbatim.
- [MATHFMT] Minor stylistic note: the section title "Continuous Hopfield / dense associative memory." (line 338) uses a slash; consider a clearer phrasing ("Continuous Hopfield (dense associative memory)") for consistency with other headings.

### lecture_6.tex
- [MATHFMT] Redundant/duplicative content - Lines 7 and 23: the phrase about "moving a large fraction of the 'bias' into architecture" (and the weight-sharing/locality rationale) is repeated almost verbatim. Consolidate to avoid redundancy. - Lines 124–126 and 284: two separate "notation" notes about σ/σ² appear; they overlap and are slightly inconsistent in wording. Combine into a single, clear notation remark to avoid reader confusion. - Lines 242–256 and 252–266: the high-level point about vanishing/exploding gradients is introduced twice in quick succession (section lead-in and again in the dedicated subsection). Remove the earlier teaser or shorten one of the repeats.
- [LABEL] Narrative / transition issues - Lines 5–9: the opening contrast with Hopfield networks is abrupt. The sentence "The second thread in this chapter is pragmatic." references "second" without a clear first-thread enumeration. Either explicitly name the two threads (architectural bias vs. pragmatic training) up front or smooth the transition. - Line 31: "In practice, this is also where 'deep learning' stopped being a promise..." reads colloquial and slightly vague. Consider a more formal phrasing and tighten the causal linkage to datasets/accelerators. - Line 221 → 223: the jump from architectural motivation to training is fine, but a short signpost sentence summarizing what will be covered in the training section would improve flow.
- [MATHFMT] Punctuation / sentence-fragment issues - Line 233: "where $\eta$ is the learning rate." begins a new sentence with a lowercase "where." Capitalize or integrate it with the preceding sentence (e.g., "…;\; where η is the learning rate.") to avoid a sentence fragment. - Line 264: after the displayed chain-rule equation the following sentence starts "where W represents..." with a lowercase "where." Capitalize or rephrase; also the sentence mentions f' even though the equation used D^{(ℓ)} (see next line) — see next point. - Line 302: forced line break "\\" inside the paragraph (in the sloppypar block). Avoid explicit line breaks in running text.
- [VISUAL] Clarity / consistency problems - Line 261–266: the explanatory text around equation (261) is slightly inconsistent: the equation uses D^{(ℓ)} but the immediate prose refers to f' (and then defines D in the next sentence). Define D immediately or reword the explanatory sentence so symbols match the equation in place. - Line 120 (shape reminder) vs. earlier notation notes: notation about tensor/layout is useful but scattered; consider consolidating all notation/shape conventions in one place (or cross-referencing) to reduce cognitive load. - Line 215 (figure caption): ends with "Use it when explaining why depth can replace very large kernels." That reads like a drafting note to the instructor/author rather than a caption for readers. Remove or rephrase for the final text. - Lines 11–20, 22–24, 120–122, 135–137, 173–175, 182–184, 286–293: many small tcolorbox "summarybox"/"Author's note" boxes are scattered. This repetitive templating interrupts flow; consider consolidating some boxes or varying presentation to avoid clutter.
- [MATHFMT] Minor stylistic / formatting suggestions - Lines 58 and 77 (and other inline math numbers): commas inside displayed/inline math (e.g., 70,656; 7,065,600) are visually inconsistent with typical math typesetting. Use \, or avoid commas in math mode for consistency. - Line 300–304 (weight initialization): "Set var ≈\,1/n (fan‑in n)." is terse and slightly ambiguous — prefer "set Var[w] ≈ 1/n (fan‑in n)" or "set variance ≈ 1/n" for clarity. - Line 31 and elsewhere: repeated mentions of "the same gradient-based training loop" appear multiple times (lines 7, 116, 118). Consider trimming one or two repetitions to tighten prose.
- [VISUAL] If you want, I can produce an edited pass that merges the duplicate notes, fixes the sentence-fragment capitalization, removes the instructional caption fragment, and normalizes the numeric and notation formatting.
- [VISUAL] Line 322 vs. 352–372: The standalone sentence at 322 ("Batch normalization normalizes...") is effectively duplicated by the fuller "Batch normalization." paragraph and figure that follow. Remove or merge the short sentence to avoid repetition.
- [MATHFMT] Lines 324–327: The \paragraph{Gradient clipping} heading has only a single-sentence paragraph beneath it. Either merge this into a neighboring paragraph or expand with a brief example/diagnostic to avoid an abrupt, staccato feel.
- [VISUAL] Line 346 and line 350: The figure caption (346) and the following sentence (350) repeat the same point ("dropout diagnostic view"). Delete or consolidate the post-figure sentence to avoid redundancy.
- [MATHFMT] Lines 337 and 437: Advice to "report seed..." / publish seed appears twice (run-to-run variance and Derivation closure boxes). Combine or reword one instance to avoid duplicative auditing instructions.
- [MATHFMT] Lines 330, 394, 405, 432, 441, 465, 449, 457: Inconsistent heading/title casing and punctuation in tcolorbox sections. Examples: - "Risk \& audit" (line 330) uses lower-case "audit"; - "Practical optimizer notes" (line 394) uses sentence title-style; - "Key takeaways" (line 441) uses title-style; - Sub-headings "Minimum viable mastery." and "Common pitfalls." (lines 449, 457) include trailing periods. Recommend adopting a single style (title case or sentence case) and consistent use (or omission) of terminal periods for all box titles/headings.
- [VISUAL] Lines 346, 370, 389: Multiple figure captions use the repetitious templated phrasing "Use it when...". This creates stylistic monotony. Vary caption verbs/detail or reserve "Use it when" for only the most actionable figures.
- [MATHFMT] Line 352: The phrase "whitening the distribution" may confuse readers (batch normalization does not perform full whitening). Consider using "normalizing" or otherwise clarifying the intended meaning to avoid potential misinterpretation.
- [MATHFMT] Line 474: Awkward phrasing "carry almost unchanged into \Crefrange{...}" — rephrase for clarity, e.g., "remain almost unchanged in ..." or "carry over into ... with little change."
- [TRANS] Line 477: The transition heading "Where we head next." is slightly informal and inconsistent with the rest of the chapter closers. Consider "Next" or "Next topic" (or match the style used elsewhere for chapter transitions).
- [VISUAL] Visual check note: `lecture_6.tex` contains `\includegraphics`; verify caption/prose alignment against rendered figure crops.

### lecture_7.tex
- [NOTATION] Inconsistent vector/matrix typography: bold vs plain variables appear mixed. Examples: lines 53–65 use \mathbf{x}_t, \mathbf{h}_t, \mathbf{y}_t; lines 246–251 use plain x_t, h_t, y_t; lines 264–267 return to \mathbf{h}_t, \mathbf{x}_t. (Pick one convention and apply consistently.)
- [MATHFMT] Inconsistent naming/capitalization for normalization/residual terminology: "LayerNorm" vs "layer norm" vs "Layer Normalization" (lines 106, 225–226). Also "residual links" (line 225) vs the more common "residual connections" — choose one term and capitalisation style.
- [MATHFMT] Repeated roadmap/flow statements fragment narrative flow: "Design motif" (15–17), "Chapter flow." (41–42) and "Roadmap." (96–97) all state the chapter order/plan. Consider consolidating to a single clear roadmap to avoid redundancy.
- [MATHFMT] Awkward or unclear phrasing that hurts readability: - "Optional reminders are kept near the chapter close" (line 42) — phrasing is odd; consider "near the chapter's end" or similar. - "revive the vanishing/exploding gradient issues" (line 73) — "revive" feels imprecise; consider "reintroduce" or "exacerbate". - "evaluation lens" (line 76) — unusual collocation; consider "evaluation framework" or "evaluation perspective". - Long, dense sentence defining BCE (line 163) — this would read better split into two sentences (definition of the per-example loss, then a short note clarifying "logit" and sigmoid).
- [MATHFMT] Missing/awkward comma: "In the simplest formulation there are three learned matrices:" (line 71) would read more naturally with a comma after the introductory phrase: "In the simplest formulation, there are three learned matrices:".
- [DEDUP] Repetitive short summary boxes fragment flow: numerous small tcolorbox "summarybox" inserts (lines 7–13, 15–17, 92, 166, 225, 253) sometimes contain one short sentence. These repeatedly interrupt the derivation/narrative; consider reducing frequency or grouping related notes to improve continuity.
- [MATHFMT] Minor formatting inconsistency in inline math punctuation: example uses braces in y{=}1 at line 163, whereas elsewhere plain "=" is used. (Use a single style for inline comparisons.)
- [OTHER] No issues spotted.
- [MATHFMT] 326–328: Mild redundancy — the sentence in 326 (“the backward pass computes gradients ... by backpropagating errors through time”) repeats the explanation immediately restated in 328 (“BPTT unfolds the RNN ...”). Consider combining/simplifying to avoid repetition.
- [MATHFMT] 328: Informal phrasing — “piggyback across every copy” reads colloquial for a technical text. Consider “across each unrolled copy” or “across time steps” for clarity.
- [MATHFMT] 333–342 vs. 348–368: Inconsistent code conventions between the two code blocks - 333–342 uses Python-like syntax (for t in range(T):, h0 vs h_0) and variable naming; 348–368 uses pseudocode/math-style indexing (for t = 1..T:, h_0 = 0) and different comment styles. - Suggest standardizing the code style (either all Python-like or all pseudocode) and consistent variable naming (h0 vs h_0, yhat vs \hat{y}) for reader ease.
- [MATHFMT] 346–370 (code block): Mixing of ASCII/math notation inside verbatim (e.g., h_t^T, .* ) may confuse readers expecting one convention. If the “Code–math dictionary” (373–374) is intended to resolve this, consider moving or cross-referencing it immediately before/after the code blocks.
- [NOTATION] 372–374: The “Code--math dictionary.” header uses an em-dash/double-hyphen style; consider making header punctuation consistent with other subsection titles (e.g., “Code–math dictionary” with an en-dash or plain title case).
- [MATHFMT] 404–408: Very long, dense sentence explaining Jacobian structure and norms. Consider breaking into two sentences for readability (e.g., separate the formula/definition from the implication about spectral norms causing vanishing/exploding).
- [MATHFMT] 409: “...often fail to preserve dependencies beyond roughly 5--10 steps in language tasks, which is why gated cells became the default...” — the causal phrasing (“which is why”) is slightly informal/hand-wavy. Consider rewording to something more neutral (e.g., “...which motivated the adoption of gated cells for longer-range dependencies.”).
- [VISUAL] 413 vs. 397 vs. 519 vs. 592: Repetitive caption template — multiple figure captions end with similar “Use it when ...” sentences (figures at 397, 413, 519, 592). This repeated phrasing feels templated; vary the phrasing or remove in some captions to improve tone and reduce repetition.
- [VISUAL] 518–519: Inconsistent notation in caption — the legend/axis uses $\tau$ (math mode) but the caption text uses plain “tau”. Make variable formatting consistent (prefer math mode: $\tau$).
- [LABEL] 435–436: Tone shift / informal admonition inside a summary box — “Author's note: do not fight vanilla RNNs.” This imperative, conversational tone stands out from the surrounding technical prose. Consider rephrasing more neutrally or moving to an editorial aside with different labeling.
- [MATHFMT] 597: Long sentence describing LSTM/GRU behavior (many clauses). Consider splitting into two sentences to improve clarity (one sentence on LSTM gates and memory equations, one on GRU behavior).
- [OTHER] 597 (also general): The slash usage “\(h_{t-1}\) / \(c_{t-1}\)” is spaced; for prose clarity prefer “h_{t-1} and c_{t-1}” or “h_{t-1}/c_{t-1}” without spaces, depending on house style.
- [VISUAL] Overall suggestions: tighten a few long sentences, standardize code formatting/notation across examples, reduce recurring caption template, and neutralize a couple of informal phrasings/tones.
- [VISUAL] Duplicate caption templating: both the LSTM and GRU figures repeat identical caption blocks inside an ifdefined\HCode conditional. Consolidate or wrap the caption in a macro to avoid the duplicated text (LSTM: 685–689; GRU: 794–798).
- [MATHFMT] Missing punctuation after bold heading: the "Pitfalls checklist" heading is followed immediately by prose without a colon or dash. Add ":" or similar for clarity (line 828).
- [OTHER] Spurious space inside math subscript: "w_{1: t-1}" has an extra space after the colon; prefer "w_{1:t-1}" for consistency (line 915).
- [PUNCT] Comma for readability before coordinating "but": in the tcolorbox summary the two sentences omit a comma before "but" and read slightly run-on. Add commas for readability: - "simplest and parameter\hyp{}efficient, but most prone..." (line 809) - "highest parameter count, but most robust..." (line 811)
- [MATHFMT] Long/complex sentence that would benefit from splitting: the sentence beginning "Explicitly, repeatedly substituting \Cref{eq:rnn_hidden_state} reveals that ..." is dense; consider splitting into two sentences to improve clarity (line 920).
- [LIST] Dense inline list under "Pitfalls checklist": the list of pitfalls on line 828 is a long comma/semicolon-separated run-on. Consider converting to a bulleted list or inserting clearer separators to improve scannability (line 828).
- [VISUAL] Inconsistent capitalization in diagram labels: the affine block is labeled "Affine" in the LSTM diagram (line 644) but "affine" in the GRU diagram (lines 725, 732). Make capitalization consistent across figures.
- [OTHER] If you want, I can produce precise rewrites for the flagged sentences/lines.
- [MATHFMT] Line 988: Punctuation — missing comma after the parenthetical. "...for noise scales $\sigma^2$) it refers to a standard deviation." → insert a comma after the closing parenthesis or rephrase (e.g., "...$\sigma^2$), it refers..." or "...$\sigma^2$. In that case, it refers...").
- [PUNCT] Line 986: Word form — "elementwise" is used; consider hyphenating for consistency/readability ("element-wise").
- [LABEL] Lines 1030, 1034 (also 1029): Repetition/flow — the transformer chapter is referenced multiple times in close succession (inside the tcolorbox at 1030 and again at 1034). Consolidate or vary wording to avoid repetition.
- [MATHFMT] Lines 965–989, 998–1019, 1021–1031: Repetitive templating — three adjacent tcolorbox summary sections (compact equations, key takeaways, exercises) create dense, similarly styled blocks. Consider merging some boxes or varying presentation to improve visual/narrative flow.
- [MATHFMT] Line 991–996: Paragraph structure/flow — the "Optional refresher" mixes convolution padding formula and autoencoder intuition in one paragraph. Consider splitting into two short paragraphs (one for padding/formula, one for autoencoder intuition) for clarity.
- [MATHFMT] Line 1002: Clarity/wording — "Stability tools (clipping, gating, attention) enable long-range dependency modeling." reads slightly awkwardly and groups "attention" with stability tools. Consider rephrasing to "Stability tools (clipping, gating) and mechanisms like attention help model long-range dependencies" or similar, to improve precision and flow.
- [NOTATION] Line 1006, 1013, 1029 vs. tcolorbox titles (e.g., line 998): Inconsistent heading punctuation/capitalization — some inline bold headings end with periods ("Minimum viable mastery.", "Common pitfalls.", "If you are skipping ahead.") while tcolorbox titles do not. Apply a consistent style (either sentence punctuation or none) across headers.
- [VISUAL] Visual check note: `lecture_7.tex` contains `\includegraphics`; verify caption/prose alignment against rendered figure crops.

### lecture_8_part_i.tex
- [DEDUP] Lines 176 & 264: duplicate comment "% Chapter 13 (continued)". Remove one occurrence to avoid noisy/repetitive templating.
- [MATHFMT] Lines 151–153 and 240–242: examples ("to buy an automatic car", and the context word list) are typeset in display-math (\[ ... \]) even though they are plain text. Consider using inline text or \texttt/\text{...} outside display math for cleaner spacing and punctuation.
- [MATHFMT] Line 185: straight double quotes around "want" are inconsistent with LaTeX quoting elsewhere (e.g., ``pretty image''). Use proper TeX quotes (``want'') for consistency.
- [MATHFMT] Lines 197–199, 205, 259–263, 281, 313, etc.: inconsistent notation for matrices/vectors — sometimes plain italic W, sometimes \mathbf{W}. Similarly \mathbf{W}_{\text{out}} vs W_{\text{out}} appears inconsistently. Standardize on one style (e.g., bold for matrices, italic/sans for scalars) and apply consistently.
- [MATHFMT] Lines 221–229: inconsistent notation for the predicted distribution / its components — \hat{\mathbf{y}}_j is introduced (line 222) but the loss (line 229) uses \hat{y}_j and \hat{\mathbf{y}} interchangeably. Pick a single convention (\hat{y}_j or \hat{\mathbf{y}}_j) and use it consistently.
- [NOTATION] Lines 129, 156, 301 (and elsewhere): inconsistent heading capitalization/formatting for "skip-gram" vs "Continuous Bag of Words (CBOW)". Either Title Case both headings (e.g., "Skip-gram") or keep both lowercase for consistency.
- [MATHFMT] Lines 70–71: phrasing "each word would already be a vector:" is slightly informal/awkward. Consider "each word would be represented as a vector:" for clarity.
- [MATHFMT] Lines 295–296: mildly repetitive phrasing about \mathbf{W}_{\text{out}} starting as \mathbf{W}^\top and then optionally being tied to \mathbf{W}^\top. This is fine, but you could tighten to avoid near-duplicate statements (e.g., state once that implementations may tie input/output embeddings to \mathbf{W}^\top).
- [MATHFMT] Line 57: use of \par inside the bold "Synonyms." paragraph is unusual stylistically (breaks paragraph manually). Either keep consistent paragraph breaks or remove the explicit \par.
- [MATHFMT] If you want, I can produce a cleaned-up version of the LaTeX with these fixes applied.
- [LABEL] Repeated content / duplication - Weighting function and objective repeated: nearly identical definitions appear at 534–541 (f(x) piecewise) and again at 577–583; the weighted least-squares objective appears at 521–525 and is repeated at 571–574. Consider consolidating to avoid redundancy. - Negative-sampling recipe repeated in different forms: compact recipe box (341–345) and brief bullets (351–354) vs. full negative-sampling section and loss (367–395). These restatements are redundant; unify or cross-reference.
- [NOTATION] Inconsistent notation that harms clarity - Vector symbols change across nearby sections: earlier softmax/skip-gram uses h and u (lines 336–338, 321–325), negative-sampling section uses v and v' (384–395), and later PMI relation uses v and u again (408–411). This inconsistent naming of target/context vectors may confuse readers (lines 321–338; 384–395; 408–411).
- [NOTATION] Variable-name inconsistency (capitalization) - Co-occurrence counts are introduced as X_{ij} (lines 441–446), but later the same quantity is denoted x_{ik}/x_{ij} (lines 551–564, 571–574). Inconsistent use of X vs. x appears across the objective and derivation; pick one and use it consistently.
- [VISUAL] Grammar / punctuation - Line 380: "Negative draws occasionally colliding with real context words is harmless." — subject–verb disagreement; should be "are harmless" or rephrased for clarity. - Figure caption (line 470) includes an instruction sentence ("Use it when checking...") that reads more like advice than a descriptive caption and is stylistically out of place for a caption.
- [VISUAL] Figure / caption issues - The included image file name (lec14_analogy_geometry) does not match the figure label (fig:lec8-embedding-clusters) — potential source-of-truth mismatch (lines 468, 471). - The comment immediately above the caption warns "Avoid inline math in captions" (line 469) but the caption itself contains math-like content presented as inline text ("v(king) - v(man) + v(woman) approx v(queen)") and uses the plaintext "approx" rather than LaTeX math (\approx). Either move the math into an external figure text block or typeset it properly and remove the contradictory comment.
- [LIST] Inconsistent list formatting / style - Several lists use bare hyphens (e.g., lines 624–626 and 638–640) while other places use itemize environments (e.g., lines 351–354, 423–426). Pick one consistent style for lists and headings.
- [MATHFMT] Tone / register shifts - Informal wording appears in places that otherwise use a formal technical register: "Tiny worked example" (line 398) and the colloquial transition "Before moving from geometry to governance, keep the boundary clear:" (lines 605–606). Consider more formal phrasing for a graduate text.
- [VISUAL] Minor clarity / phrasing suggestions - Line 347–351: the sentence "This is computationally expensive..." follows directly after a boxed recipe — the transition feels abrupt; consider a brief signpost linking the box to the following discussion. - Line 470 caption contains procedural advice ("Use it when checking whether embedding offsets encode consistent relations and reveal bias directions.") — consider moving this guidance into the main text where it can be expanded and justified.
- [NOTATION] If you want, I can produce a concise edited version of the paragraphs flagged above (with unified notation and variable names) to illustrate how to resolve the inconsistencies.
- [LIST] Line 641: Leading hyphen + italicized fragment ("- \textit{Regularization} ...") reads like a stray list item or sentence fragment. Either integrate into the preceding list/environment or convert to a full sentence for clarity.
- [PUNCT] Lines 670, 673, 711: Inconsistent terminal punctuation for headings/paragraph titles — some end with a period ("Contextual embeddings and transformers.", "Wrap-up", "Where we head next.") while others do not ("Cross-Lingual Challenges"). Normalise heading punctuation (prefer no terminal periods).
- [NOTATION] Line 656 (tcolorbox title): Inconsistent title capitalization/style. "Author's note: embeddings mix geometry and bias" uses sentence case while other box titles use title case (e.g., "Practical bias checks", "Key takeaways"). Make box titles consistent.
- [MATHFMT] Line 657: Repetition of the verb "capture" in "Embedding spaces faithfully capture geometry (...) precisely because they also capture the biases..." is stylistically awkward; consider rephrasing to avoid the duplicate verb.
- [OTHER] Lines 675–676: Tense inconsistency in the wrap-up. "This chapter has developed..." (present perfect) followed by "It also emphasized..." (simple past). Use a consistent tense (e.g., both present perfect or both simple past).
- [MATHFMT] Line 708: Sentence fragment / punctuation error: "If you are skipping ahead. You can treat..." should be a single sentence (comma instead of period) or rewritten as two independent clauses.
- [DEDUP] Line 665–666 and 665/667 proximity: Slight repetition of "redact"/"redaction" and "restrict"/"accompany" ideas across privacy/security and monitoring bullets. Consider tightening wording to avoid closely repeated terms (e.g., merge or rephrase related privacy/security actions).
- [MATHFMT] Line 656–658: Tone shifts toward informal phrasing ("so put that ability to work before shipping a model."). For a graduate-level textbook, consider a more formal alternative (e.g., "use that capability before deployment").
- [OTHER] Line 712: Minor wording clarity: "attention replaces recurrent state" could read better as "attention replaces the recurrent state" or "recurrent states" depending on intended meaning — check for grammatical number agreement.
- [VISUAL] Visual check note: `lecture_8_part_i.tex` contains `\includegraphics`; verify caption/prose alignment against rendered figure crops.

### lecture_8_part_ii.tex
- [DEDUP] Lines 49–66 vs. 127–136: Near-verbatim repetition. The subsections "Soft Computing: Motivation and Definition" (lines 49–66) and "Soft Computing: Motivation and Overview" (lines 127–136) restate the same points (coalition of methods, tractability/robustness/low-cost, list of constituents). Consolidate or remove one to avoid redundancy and improve narrative flow.
- [DEDUP] Lines 111–124 vs. 122–124: Immediate repetition. The prose distinguishing uncertainty/imprecision/fuzziness (lines 111–121) is reiterated almost verbatim inside the tcolorbox (lines 122–124). Either shorten the paragraph or keep the boxed summary only.
- [LABEL] Lines 59–66, 98–106, 130–136: Inconsistent role for probabilistic methods. Probabilistic reasoning appears both as a constituent of soft computing (lines 59–66 and 98–106) and as part of the separate "statistical strand" (lines 66 and 134). This creates a conceptual inconsistency—clarify whether probabilistic methods are treated inside this block or only referenced as complementary.
- [MATHFMT] Lines 52 and 241 (and surrounding): Chronology/attribution ambiguity. Line 52 states "Soft computing, introduced by \citet{Zadeh1994,Zadeh1997} after his 1965 fuzzy sets paper," while line 241 says "Lotfi Zadeh, in the late 1960s, observed...". The historical thread is confusing (Zadeh's 1965 paper vs. later uses). Rephrase to make the timeline explicit (e.g., Zadeh introduced fuzzy sets in 1965 and later popularized the term "soft computing" in the 1990s).
- [LABEL] Lines 139–154 and 159–173 (Tables): Table clarity problem. In the "Boolean operators vs. fuzzy operators" table (lines 164–172) the columns are labeled "Boolean logic" and "Fuzzy logic" but the entry under Boolean logic for AND is "\min(a,b)" (line 168), which is a fuzzy operator; this is potentially misleading. Verify column entries vs. headers and correct the mapping (or add a clarifying note that min/max coincide with Boolean operators for {0,1} values).
- [MATHFMT] Lines 175–186 / 188–205: Transition and balance. The jump from the table(s) straight into the "Fuzzy Logic" narrative is abrupt. Also the "Neural Networks" subsection (lines 219–229) contains an equation and a compact explanation, whereas "Genetic Algorithms" and "Probabilistic Reasoning" (lines 230–236) are one-paragraph stubs. Consider smoothing transitions and balancing subsection lengths or merging short paragraphs under a single comparison heading to improve flow.
- [MATHFMT] Lines 5–8 and lines 17–19: Repetitive phrasing. The design motif (lines 17–19) repeats ideas already introduced in the opening paragraph (lines 5–8) about making vagueness explicit and tuning with optimization. Either tighten the motif to be a pithy restatement or eliminate overlap.
- [MATHFMT] Lines 125 and 261: Comment duplication. The inline comment "% Chapter 15 (continued)" appears twice. If kept as a marker, one instance is sufficient.
- [LIST] Line 117: Minor formatting/indentation. The item for "Fuzziness" (line 117) lacks the blank line that separates it from the previous bullet, leading to inconsistent vertical spacing in the source. (Cosmetic but easy to fix.)
- [DEDUP] General: Some subsections reiterate the same trio of goals (tractable/robust/low-cost) multiple times (e.g., lines 52–57, 130–136). Consider stating those guiding principles once and referring back to them to reduce repetitive templating.
- [PUNCT] Lines 389: Sentence ends with "representing partial truth" but has no terminal punctuation (period). Add punctuation or continue the sentence cleanly.
- [MATHFMT] Lines 328–331: The displayed align (eq. 3) mixes implication symbols (\implies) and a bare \Rightarrow in a way that's unclear (also includes both a comma and a trailing comma). Consider a clearer, single convention for premises ⇒ conclusion (e.g., "P → Q, P ⊢ Q") and remove the stray punctuation.
- [MATHFMT] Lines 345–350 and 362–365 (and generally): Notational inconsistency — implication/entailment is represented variously as \implies, \Rightarrow, and \vdash throughout nearby examples. Recommend choosing and using one convention consistently (distinguish implication vs. entailment explicitly in prose).
- [MATHFMT] Line 350: "This rule affirms the consequent by affirming the antecedent." The phrasing risks confusion because "affirming the consequent" is a standard name for a logical fallacy. Reword to avoid implying the fallacy (e.g., "This rule derives the consequent from the affirmed antecedent").
- [MATHFMT] Lines 366–367: "This rule denies the antecedent by denying the consequent. However, as noted, this inference can sometimes be risky or invalid in practical scenarios..." — similar ambiguity: "denying the antecedent" is also the name of a fallacy; and saying the rule is "risky or invalid" contradicts the usual logical validity of modus tollens. Either clarify that you mean practical/empirical premises may be suspect (so conclusions may be unreliable), or rephrase to avoid implying that the logical rule itself is invalid.
- [DEDUP] Lines 412–418 and 466–470: The definition of membership/characteristic functions is repeated verbatim (crisp vs. fuzzy set definition appears again in the recap). Consider consolidating or shortening the recap to avoid literal repetition.
- [MATHFMT] Lines 432–436, 455, and 526: Multiple forward/preview pointers about the thermostat running example and chapter ranges appear in close succession (intro, "Forward pointer," and "Where we head next."). These are repetitive; consolidate into a single forward pointer to improve narrative flow.
- [LABEL] Lines 432–434: The sentence ends with "here keep the intuition that fuzzy labels overlap and map a universe of discourse into \([0,1]\)." Tone is slightly informal ("here keep the intuition"); consider tightening to "Here we keep the intuition that..." or "Maintain the intuition that...".
- [TRANS] Line 391: Comment "% Chapter 15 (continued)" appears in the middle of the flow. If this is internal authoring metadata, consider removing or moving to source control notes to avoid cluttering the compiled output.
- [DEDUP] Lines 445–456 and 492–506: Similar summaries/key-takeaways and "minimum viable mastery" sections repeat themes already stated in prose above. Consider trimming redundancy or merging overlapping bullets to tighten the conclusion.
- [NOTATION] Minor punctuation: Line 422 uses a semicolon between class sets; that is stylistically odd for set examples — not incorrect, but consider a comma for consistency with earlier notation.

### lecture_9.tex
- [MATHFMT] Line 22: The units formatting \([-5,5]^\circ\text{C}\) is awkward — the degree symbol is typeset as a superscript of the interval rather than as a unit attached to the quantity. Consider something like \([-5,5]\ \mathrm{^\circ C}\) or \([-5,5]~^\circ\mathrm{C}\) for clearer typesetting and spacing.
- [OTHER] Lines 108–112 vs. 130–139: Triangular membership is defined twice (once with the max(...) form, then again with a piecewise definition). This is repetitive; keep one canonical definition or consolidate the two and remove duplication.
- [DEDUP] Lines 52–63 vs. 123–139: The chapter repeats the basic definition/role of membership functions in multiple places (section headings and short paragraphs reiterate the same idea). Consider merging or shortening one of these repetitions to improve narrative flow.
- [MATHFMT] Lines 99–106: The continuous-set notation A = ∫ μ_A(x) / x is used and only clarified two lines later. Either move the interpretive sentence immediately after the equation or replace the symbolic integral with a clearer phrase (e.g., “the continuous collection {(x, μ_A(x)) : x ∈ X}”), since the integral notation may confuse readers.
- [NOTATION] Lines 144–154 (trapezoidal MF parameters and piecewise conditions): Parameter constraint is stated as a < b ≤ c < d but piecewise conditions use b < x ≤ c for the flat top. This leaves the b = c case awkward. Make the inequality conventions consistent (e.g., use b ≤ c and the plateau as b ≤ x ≤ c).
- [MATHFMT] Lines 130–139 and 146–153 (and other MF piecewise definitions): Inequality endpoint conventions vary across examples (some use ≤ on left or right endpoints inconsistently). Recommend standardizing inclusive/exclusive endpoints across all piecewise MF definitions to avoid confusion about values exactly at breakpoints.
- [MATHFMT] Line 55 (and 119): The word “uncertainty” is used alongside “fuzziness” (line 55) and the boxed recap (line 119) distinguishes imprecision vs. fuzziness. This could confuse readers: consider explicitly avoiding the loose term “uncertainty” when referring to fuzziness, or rephrase to make the distinction to imprecision/probability clearer.
- [VISUAL] Line 213 vs. line 249 (and figure): The textual description and the caption refer to different score ranges for overlap. The caption says “Scores near 78--82” but the plotted overlap domain is 75–80 (and the text previously mentions 79 and 78–82 inconsistently). Harmonize the numeric ranges in the text, caption, and plot.
- [LIST] Line 258: The “crisp partition” listed as [0,10],[11,20],[21,30] has gaps (10–11 and 20–21). If that is intentional (integers only) clarify it; otherwise make the intervals contiguous (e.g., [0,10],[10,20],[20,30]) to avoid an apparent error.
- [LABEL] Line 119: Macro capitalization is inconsistent: earlier you use \Cref/\Crefrange (lines 5, 22) but here use \cref. Consider standardizing the cref macro usage for consistency in cross-reference formatting.
- [VISUAL] Line 248 (comment) vs. caption content: The source comment warns “Avoid inline math in captions,” but the caption still contains inline numeric ranges (78--82). Either remove inline math from the caption or adjust the comment to reflect that simple numeric ranges are fine.
- [OTHER] Line 320: A verbatim environment is opened (\begin{verbatim}) but in this snippet it is not closed within the shown range. If the environment continues later, ensure it is properly closed; otherwise this will break compilation.
- [MATHFMT] Line 332: \end{verbatim} appears in this excerpt but no matching \begin{verbatim} is visible in the provided range — check for a missing or misplaced begin or move the end to the correct location.
- [TITLE] Lines 507–512: Section "Example: Union and Intersection of Fuzzy Sets" is incomplete — it contains only "Consider two fuzzy sets" with no example or continuation.
- [MATHFMT] Lines 597–601: "Examples of Operators" contains a single, unfinished bullet ("Equality operator: Checks if two fuzzy sets are equal by comparing membership functions.") and then stops. Either expand the list or remove the subsection.
- [MATHFMT] Lines 427–431 and 609–616 (also 621–627): The standard/complement operator is defined twice (first at 427–431, then again under "Standard Complement" and "Parameterized Complement Operators"). This duplication is repetitive — consolidate definitions and move parameterized forms to one place.
- [VISUAL] Lines 447 and 602: Inline comments say "% Chapter 16 (continued)" inside a file named lecture_9.tex — numbering/comments appear inconsistent. Also the figure filename lec16_fuzzy_and (line 632) suggests a mismatch between lecture/chapter numbers; verify and correct labels/filenames/comments for consistency.
- [MATHFMT] Lines 362–366: "Open and Closed Fuzzy Sets" uses a dash list (- ...) instead of a LaTeX itemize environment, while the rest of the document uses itemize/tcolorbox for lists. Consider using a consistent list environment for typography and spacing consistency.
- [MATHFMT] Lines 418 and 523 (and elsewhere): Repetitive phrasing: multiple sentences begin with "This generalizes..." (e.g., for union, Cartesian product). Consider varying wording or consolidating the recurring explanatory sentence to reduce repetition.
- [MATHFMT] Line 611: Under the "Standard Complement" heading the paragraph starts with a lowercase "the standard fuzzy negation…" — inconsistent sentence-initial capitalization. Capitalize sentence starts.
- [VISUAL] Lines 631–638: The figure caption is duplicated in the \ifdefined\HCode / \else branches with identical text (and a note about avoiding inline math). Consider consolidating the caption text to avoid repetition and simplify maintenance.
- [MATHFMT] Line 408: "use the local chapter meaning" is slightly awkward phrasing — consider rewording for clarity, e.g., "use the meaning local to the chapter" or "use the local (chapter) convention."
- [DEDUP] Lines 449–452: "Reminder on basic operators" restates the definitions already given in \Crefrange{eq:fuzzy_union}{eq:fuzzy_complement} and then repeats their practical roles. This is redundant; either remove or merge into the earlier discussion to improve narrative flow.
- [LABEL] Lines 653–655: The \label is inserted inside the subsection title ("Triangular norms (t\hyp{} \label{…}norms)"); this breaks the title and looks like a templating error. Also note the immediately following, very long duplicate label (line 655) — remove the in-title label and the redundant/overly verbose label.
- [LABEL] Lines 710–712: Same problem as above for "Triangular conorms" — a \label occurs inside the subsection title and there is a redundant/verbose second label (line 712).
- [DEDUP] Lines 660–682 vs. 740–749 (and surrounding): Repetition of axioms/definitions — the t‑norm/t‑conorm properties are restated almost verbatim in the later "T‑Norms and S‑Norms: Complementarity and Properties" subsection. Consider consolidating to avoid redundancy and improve narrative flow.
- [MATHFMT] Lines 816–819: Sentence fragment/flow issue — the display for incl(A,B) is followed by a lowercase fragment "for discrete universes (integrals for continuous, assuming finite mass)." That fragment should be attached to the preceding sentence or rephrased as a full sentence.
- [MATHFMT] Line 819: Inconsistent/incorrect explanation — the text says "implicator-based grades avoid division by small \(\mu_B\) and behave well when \(B\) has zeros," but the aggregate measure shown divides by \(\sum \mu_A(x)\) (i.e., risk of division by small \(\mu_A\)). This is a substantive mismatch and should be corrected or clarified.
- [STYLE] Line 752: Wording ambiguity — "the complement of \(\mu_A\)" is awkward. Prefer "the complement of the set A (i.e., the complement membership function \(\mu_{A^c}(x)\))" for clarity.
- [OTHER] Lines 907 and 923: Inconsistent wording about parameter ranges — line 907 calls the parameters "non-negative" but immediately constrains them to \(\alpha,\beta \ge 1\) (not merely non‑negative). Later (line 923) they are referred to as "positive". Use consistent wording (e.g., "parameters ≥ 1" or "positive, ≥1") throughout.
- [LABEL] Lines 940–951: The informal examples use \text{dilate} and \text{contract} but do not reference the formal definitions (Eqs. (909)–(911)). Consider linking these examples to the earlier equations to improve coherence.
- [LABEL] Line 928: Stray comment "% Chapter 16: Closure and Final Remarks ..." appears in the source. If this is not intended for readers, either remove or update to the correct chapter/reference.
- [NOTATION] Minor stylistic consistency: the document alternates between "t\hyp{}norm", "t‑norm", "t\hyp{}conorm", "s‑norm" etc. (throughout). For readability, pick one consistent typographic convention for these terms.
- [VISUAL] Inconsistent hyphenation/notation for "t‑norm" / "s‑norm": used as t\hyp{}norm/s\hyp{}norm in the running text (e.g., 1024, 1036, 1187) but as plain "t‑norm"/"s‑norm" in the table caption (1032). Pick one style and apply consistently.
- [LABEL] Display math used for a short list of labels (inputs/outputs): the displayed equations for "Age (x), Exercise Level (e)" and "Health Status (h)" (1008–1015) read awkwardly. These would be clearer inline or as a short sentence rather than separate display math.
- [MATHFMT] Inconsistent terminology/notation for fuzzy modifiers: the phrase "contract μ_old to get μ_too old" (987) versus the explicit function call "dilate(μ_old(x))" (996). Also, one is verbal ("contract") and the other uses a verb-as-function ("dilate(...)") — unify terminology and notation for modifiers (dilation/contraction, contraction/dilation, or specific operator names).
- [VISUAL] Table caption is partly prescriptive and contains an ambiguous pronoun ("Use it when...") rather than a concise descriptive caption (1032). Consider rephrasing to describe contents/results rather than instructing use; the pronoun "it" is vague.
- [VISUAL] Figure caption mixes inconsistent formatting and imperative phrasing (1156): "T = 27 deg C" and "s* approx 0.58" are plain text while the rest of the document uses proper LaTeX math/degree notation (e.g., 1076). Also the caption includes "Use it when sanity-checking..." — captions should be descriptive rather than directive.
- [LABEL] Redundant/duplicated plot labels: identical numeric labels for the clipping levels (0.3 and 0.133) are placed at both left and right in the plot (1127–1130). This is visually redundant and could be simplified.
- [LABEL] Minor wording inconsistency in the example label vs. description: item title "Not young and not old:" (980) vs. the explanatory sentence "neither young nor old" (984). Consider using a single consistent phrasing (e.g., "Neither young nor old") for clarity.
- [VISUAL] Visual check note: `lecture_9.tex` contains `\includegraphics`; verify caption/prose alignment against rendered figure crops.

### lecture_supervised.tex
- [MATHFMT] Line 6–7: The pair of sentences is abrupt/elliptical: "When a mapping is known, we use the formula: Celsius and Fahrenheit are linked by a simple rule, and many physical laws give direct input--output relationships. The problems that motivate machine learning do not." The second sentence reads as a fragment — "do not" what? Suggest completing to "do not have such known mappings" or similar.
- [NOTATION] Line 31: The notation mixes a general hat convention and a linear-model-specific identity in one bullet: "\(\hat{y}_i = h_\theta(\mathbf{x}_i)\), \(\hat{\mathbf{y}}=X\mathbf{w}\)". The second equality applies only for linear models; consider qualifying it to avoid confusion.
- [NOTATION] Lines 40, 251, 259: Loss-argument conventions are inconsistent. Earlier you use \(\ell(\hat{y},y)\) (line 40), then define classification losses as \(\ell_{\text{hinge}}(y,z)\) (line 251) and regression losses as \(\ell_{\text{sq}}(e)\) (line 259). Add a brief clarifying sentence stating that loss arguments will be written in the most natural reduced variable (prediction/residual/margin) to avoid reader confusion.
- [NOTATION] Lines 142, 146, 150–158, 236 (and elsewhere): Inconsistent capitalization of regularizer names — "Ridge", "ridge"; "Lasso"/"lasso"; "elastic net"/"elastic-net". Example: section header "Ridge and lasso." (line 142) vs bullets "Ridge (L2)" and "Lasso (L1)" (lines 145–146) and "elastic net" (line 236). Pick one convention (e.g., "Ridge / Lasso / Elastic Net") and apply it consistently.
- [MATHFMT] Lines 157 vs. 236: Inconsistent hyphenation of "elastic net" — appears as both "elastic-net" (line 157) and "elastic net" (line 236). Standardize the spelling.
- [VISUAL] Lines 114, 197, 230, 267, 308 (multiple figure/table captions): Repetitive templating of the final sentence "Use it when ..." across many captions and the table. This repeated phrase becomes formulaic; consider varying phrasing or reserving the "Use it when" guidance for the most essential figures/tables.
- [VISUAL] Lines 272–276 (table) vs. 298–303 (figure legend): Inconsistent capitalization/style of loss names across table and figure legends ("Squared error", "Absolute error", "Huber" in the table vs. "Hinge", "Logistic", "Squared hinge" in the legend). Normalize capitalization (title case vs. sentence case) for loss names across captions, legends, and table entries.
- [NOTATION] Lines 30–33 (itemize bullets): Minor spacing inconsistency inside inline math: e.g., "\(y_i\in\mathbb{R}\)" (no spaces) vs "\(y_i \in \{0,1\}\)" (with spaces). This is stylistic, but inconsistent spacing around relation symbols (\in, =) appears in a few places; consider a consistent style for readability in source (e.g., include a space around binary relations).
- [STYLE] Line 125: The phrase "the chapter's opening promises" is slightly informal/colloquial; consider rewording to "earlier claims" or "the chapter's opening claims" for tighter prose.
- [DEDUP] Line 150 (tcolorbox title): You reuse the "summarybox" / "Design motif" boxed templates frequently. The boxes are useful, but their frequent, similar structure contributes to a templated feel. If possible, vary the micro-format or reserve boxed summaries for higher-level takeaways to reduce repetitiveness.
- [OTHER] No issues spotted.
- [VISUAL] Repetitive caption phrasing: many figure captions end with the same "Use it when ..." instruction. Instances: figs at lines 341, 399, 427, 481, 513, 538. Suggest vary wording or reserve this operational tip to one place to avoid formulaic repetition.
- [NOTATION] Inconsistent capitalization of boxed titles (tcolorbox): mixed title case and sentence case across boxes. Examples: "Risk \& audit" (line 356) vs "Proper scoring rules and calibration" (line 367) vs "A concrete toy task" (line 405) vs "Data-leakage checklist" (line 485) vs "Bias--variance at a glance" (line 494) vs "Key takeaways" (line 618). Pick one convention.
- [VISUAL] Forward reference + awkward phrasing: you reference \Cref{fig:lec1-calibration-double-descent} "in this aside" at line 432, but the aside and the figure actually appear later (aside at 504, figure at 510). Either move the reference or reword to avoid confusing the reader about chronology.
- [VISUAL] Redundant / close repetition between figure captions and surrounding prose: e.g., Fig. lec1_splits caption (line 399) is restated immediately in text (line 403); likewise the learning-curves caption (line 481) and the subsequent sentence(s) (lines 434–435/502). Consider trimming one or rephrasing transitions to avoid repetition.
- [MATHFMT] Inconsistent capitalization/terminology for dataset splits: sometimes "train/validation/test" (lowercase, lines 354–355), sometimes "Train/Validation/Test" in the diagram nodes (lines 393–395) or "training, validation, and test" (line 354). Choose a consistent style (sentence case vs. Title Case) and apply throughout.
- [DEDUP] Overuse of small summary boxes interrupts narrative flow and repeats topics: e.g., "Risk & audit" (lines 356–365) overlaps with later "Data-leakage checklist" (485–492) and "Key takeaways" (618–632). Consider consolidating or reordering boxes to reduce fragmentation and repetition.
- [TITLE] Tone/register inconsistency in short headings: some are informal/casual ("Ridge and lasso in one line." at line 612; "A concrete toy task" at 405). Decide on a uniform register (formal vs. conversational) and adjust.
- [VISUAL] Minor clarity: sentence in Fig. lec1_learning_curves caption (line 481) — "the validation curve flattens while additional data continue to decrease training error only marginally." Better: "the validation curve flattens while additional data decrease the training error only marginally." (adds "the" and tightens syntax).
- [MATHFMT] Slight wording duplication near start of subsection (lines 350–355): the same idea about roles of train/validation/test is expressed multiple times in adjacent sentences. Consider combining two sentences for tighter flow.
- [VISUAL] Source comment left in code: a comment beside the ridge figure (line 537) reads "% Avoid inline math in captions; it wraps poorly in some EPUB renderers." It's fine as an author note, but ensure such comments are intentional and won't be overlooked during final copy-edit.
- [MATHFMT] Lines 641 & 645: Both paragraph headings end with a period ("If you are skipping ahead." / "Where we head next."). Headings usually omit terminal punctuation; consider removing the periods for consistency with standard heading style.
- [MATHFMT] Line 641: "Keep the ERM loop and split hygiene close:" is slightly colloquial/ambiguous. Consider rephrasing to something clearer (e.g., "Keep the ERM loop and data-split hygiene in mind" or "Keep the ERM loop and train/validation/test split hygiene in mind").
- [PUNCT] Line 641: Mixed use of slashes (loss/regularizer, train/val/test) reduces readability. Prefer "loss and regularizer" and either spell out "train/validation/test" or choose a consistent slash/dash style (e.g., train–validation–test).
- [OTHER] Line 641: "neural chapters" is vague; consider "chapters on neural networks" or "neural-network chapters" for clarity.
- [PUNCT] Line 645: "cross\hyp{}entropy" is an unusual construction here. If the intent is a hyphenated word, use a normal hyphen ("cross-entropy") unless \hyp{} is required for a specific reason; verify the macro is available and produces the desired output.
- [MATHFMT] Line 645: "ROC/PR curves" again uses a slash; for clarity prefer "ROC and PR curves" or expand PR at first use to "precision–recall (PR) curves" if PR has not been previously defined.
- [VISUAL] Visual check note: `lecture_supervised.tex` contains `\includegraphics`; verify caption/prose alignment against rendered figure crops.

### lecture_transformers.tex
- [VISUAL] Line 255: Reference uses \Cref{fig:lec13-masks} while earlier figures use labels with underscores (e.g., fig:lec13_transformer_block, fig:lec13_micro_figures). Inconsistent label naming may cause broken cross-references or confusion—use a consistent convention (underscores vs. hyphens).
- [TRANS] Lines 6–19, 25–33, 37–39, 49–55, 299–311, 313–320: Frequent small tcolorbox "summarybox" inserts interrupt narrative flow. Consider reducing or grouping some boxes (e.g., combine short adjacent notes) to improve reading continuity.
- [VISUAL] Lines 172 and 250: Both figure captions begin with "Schematic:" — repetitive phrasing. Vary caption openers to avoid template repetition.
- [VISUAL] Line 176: Sentence "Cref{fig:lec13_micro_figures} is the compact visual bridge for positional encoding, KV cache reuse, and LoRA adapters." reads awkwardly (missing backslash before Cref; likely \Cref). Also "compact visual bridge" is vague—consider rephrasing to state explicitly what the figure clarifies.
- [VISUAL] Lines 257–270 (micro example): Transition into the micro example is abrupt. Add a short lead-in sentence saying which concept the toy example is intended to illustrate (e.g., masking behavior, attention weight shape) to help readers connect it to the preceding figures/text.
- [MATHFMT] Lines 258–259: "sets all logits \emph{above} the diagonal to \(-\infty\)" is ambiguous about matrix indexing (which axis is time). Given earlier conventions about rows/columns, make explicit the masking rule in index form (e.g., mask entries with j>i) to avoid reader confusion.
- [PUNCT] Line 50: "FFN inner widths typically 2--4\(\times d_{\text{model}}\)." Spacing/formatting is awkward (digit-range immediately adjacent to a math \times). Consider "2–4 × d_{model}" or "2–4×d_{model}" for clarity and consistent typography.
- [PUNCT] Line 314: Numeric formatting is inconsistent: "LR \(\sim10^{-3}\) for small models, \(1{-}2\times10^{-4}\) for mid-size." Prefer consistent spacing and range formatting, e.g. "\(\sim 10^{-3}\)" and "\(1\text{–}2\times 10^{-4}\)" (use an en-dash for ranges).
- [LIST] Line 23: Long sentence with multiple clauses ("The RNN chapter... information must travel... training cannot... and gradients can still..."). Consider breaking into two sentences for readability or add semicolons to clarify the list structure.
- [MATHFMT] Minor: small punctuation/spacing inconsistencies in math prose (e.g., "h\cdot d_k = d_{\text{model}}" vs. other uses of multiplication). Consider standardizing on either \cdot or implicit multiplication and consistent spacing throughout.
- [VISUAL] Line 447 (figure caption): "zeroes attention into padded positions" is awkward/unclear. Suggest "zeroes out attention to padded positions" or "masks attention to padded positions".
- [OTHER] Line 341 (item about FlashAttention): phrase "so the quadratic pattern remains exact" is vague. Clarify whether you mean "quadratic computation pattern" or "quadratic memory/compute cost" so the reader knows what "pattern" refers to.
- [MATHFMT] Line 484 (Practitioner box, "Pitfalls"): the abbreviation "lr" is unexplained. Expand to "learning rate (LR)" for clarity. Also "over-length inputs" is awkward — consider "overly long inputs" or "inputs longer than the model's context length".
- [OTHER] Line 478 (table, Equivariance row): parenthetical "cf. conv translation equivariance" is terse/unclear. Spell out "convolutional translation equivariance" (or rephrase) for readers unfamiliar with the abbreviation "conv".
- [OTHER] Line 509 (Common pitfalls): "inconsistent tokenization between train and evaluation." — change "train" to "training" for grammatical consistency ("training and evaluation").
- [STYLE] Line 519 (Exercises): "tokens/sec" is an informal unit. Pick a consistent style used elsewhere (e.g., "tokens/s" or "tokens per second").
- [TRANS] (No issues were raised about mathematics correctness; I focused only on narrative/clarity and punctuation/wording.)

### notation.tex
- [NOTATION] Redundant statements about symbol overloading: lines 4 and 54 repeat the same point (that some symbols are reused/overloaded). Consider merging or removing one to avoid repetition.
- [LABEL] Duplicate use of "y" in the symbol table: lines 16–17 list y as both a continuous regression target and a binary class label. This is likely to confuse readers; either differentiate (e.g., y_reg, y_class) or add a clarifying note in the table.
- [MATHFMT] Inconsistent argument notation for functions/activations in the table: - Lines 21 and 36 use "(\cdot)" in the left column but the formula in line 21 uses variable z. Line 23 writes ReLU(z). Pick one convention (e.g., always use (\cdot) in the symbol column and a consistent dummy variable in the formula) to avoid small but distracting inconsistencies.
- [MATHFMT] Inconsistent typographic/math formatting in the table: - Line 33 ("KV cache") is not in math mode while almost all other symbols are. - Several table entries omit a space after commas in the left column (e.g., lines 24, 31); others have extra leading spaces (lines 44–46). Standardize spacing and math-mode use across rows.
- [MATHFMT] Ambiguous mapping in the table: line 47 lists "$\mathbf{1}$, $\mathbf{I}$ & All-ones vector and identity matrix" but does not explicitly map which symbol is which. Make it explicit: "$\mathbf{1}$ — all-ones vector; $\mathbf{I}$ — identity matrix."
- [MATHFMT] Mismatch between wording and examples: line 60 says "plain roman symbols (\(x, y,\sigma\)) denote scalars" but the examples are shown in math italic, not roman. Reword ("plain symbols") or typeset the examples in roman if you mean roman font.
- [LABEL] Slightly abrupt transition after the table: the text at line 54 reiterates notation-overload guidance but does not explicitly reference the table above. Consider a linking sentence such as "Table X lists the most commonly used symbols" to improve flow.
- [MATHFMT] Potentially surprising convention needs brief justification: line 64 states "We use row embeddings by convention..." Readers commonly see column-embedding conventions; add a brief rationale or note to prevent confusion.
- [MATHFMT] Minor clarity suggestion: line 62 says "we avoid bare \(T\) to reduce ambiguity." "Bare T" may be slightly ambiguous phrasing—consider "we avoid using a plain superscript T" or similar wording.
- [TRANS] Consolidation suggestion: there are three adjacent tcolorbox blocks (lines 71–76, 78–86, 88–90). Consider whether all three are necessary as separate boxes or whether some could be combined to reduce repetitive framing and improve reading flow.
- [OTHER] No issues spotted with mathematics-as-prose that would introduce ambiguity beyond the items above.

### preface.tex
- [STYLE] Line 3: Very long, passive sentence ("a recurring gap became apparent"). Consider splitting into two sentences and switching to active voice ("I noticed a recurring gap") to improve clarity and engagement.
- [MATHFMT] Lines 7–11: Awkward phrasing: "the original chapter voice of ECE~657" is unclear. Consider rephrasing to something like "the original voice of the ECE~657 course" or "the course's original chapter voice."
- [TRANS] Lines 7, 22, 28: Repetitive opening. Several successive paragraphs/sentences begin with "This book" (7, 22, 28). Vary openings to improve narrative rhythm.
- [MATHFMT] Line 11: Colloquial phrase "hunting for missing context" feels informal for a preface; consider a more formal alternative ("searching for missing context" or "recovering missing context").
- [STYLE] Line 16: Awkward/ambiguous phrase "implementable by an engineer." Consider "usable by practicing engineers" or "implementable in engineering practice."
- [LABEL] Line 18: Tense/temporal phrasing awkward: "In the first edition (2026), the field is in the era of large language models…" Either make tense consistent ("At the time of the first edition (2026), the field was…") or clarify that 2026 is the reference point.
- [MATHFMT] Line 20: Colloquial "now live in" and abrupt "readers outside that course can ignore the appendix entirely." Consider more formal wording ("are located in \Cref{app:course_logistics}; readers not taking the course need not consult the appendix") and soften "ignore."
- [STYLE] Line 26: Slightly informal "collected up front." Consider "collected at the front of the book" or "presented up front."
- [OTHER] Line 16 (small wording): "adding and removing chapters" is a bit repetitive; "adding or removing chapters" is tighter.
- [MATHFMT] No punctuation/spacing errors (LaTeX dashes and ~ usage appear correct).

## Summary (from source report)

- Files with actionable editorial issues: `23`
- Files with no issues spotted: `0`

## 2026-02-20 continuity enrichment scan (author input requests)

- Ran a rolling-window continuity scan (Part-by-Part, anchored on `lecture_1_intro.tex`) to identify places where
  additional authorial bridges would strengthen introductions and section-to-section connections.
- Logged concrete write-up tasks + micro-section flags (TOC noise / tiny subsections) in:
  `notes_output/review/writeup_tasks_from_codex_20260218.md`.
- Implemented the first bridge: added a Part II transition box to `notes_output/book_chapters.tex` (right after the
  Part II "How to read" rolling-window box) to improve continuity into the neural-network chapters.
- Implemented the second bridge: added a Part III transition box to `notes_output/book_chapters.tex` (right after the
  Part III "How to read" rolling-window box) to frame fuzzy reasoning as auditable specification and to set expectations
  for intentional repetition (preview -> algebra -> behavior).
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after adding the Part III bridge.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK). Non-gating TeX warnings remain
  (underfull hbox in LOF/Bib; overfull vbox in `lecture_6.tex` and `lecture_9.tex`).

## 2026-02-20 micro-section consolidation (in-chapter TOC hygiene)

- `notes_output/lecture_10_part_i.tex`: consolidated three tiny wrap-up subsections (Recap/Motivation, Generalization,
  Example Calculation) into paragraphs inside the Properties section, preserving labels to avoid breaking any references.
- Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edit: PASS.
- `notes_output/lecture_11.tex`: expanded the umbrella "Genetic Operators" subsection and the "Selection" subsection
  intro so they stand on their own (instead of acting as one-line jump points), keeping the existing substructure.
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the `lecture_11.tex` operator-section edits.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).
- `notes_output/lecture_8_part_ii.tex`: demoted the one-sentence "Fuzzy Logic as a New Mathematical Language" subsection
  to a labeled paragraph directly before the Motivation/Intuition subsection to reduce TOC noise while preserving the
  transition sentence and label.
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the `lecture_8_part_ii.tex` micro-section edit.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK). Note: the "PDF vs EPUB spot-check
  bundle (Apple)" step logged a transient Playwright `Page.goto` timeout on one XHTML page but the overall script still
  exited successfully and all production gates passed.
- `notes_output/lecture_9.tex`: demoted the short "Graphical Interpretation" subsection to a labeled paragraph and
  expanded the "Closure of Membership Function Derivations" subsection so it stands as a real closing handoff into
  fuzzy relations/composition (transfer cues + audit checklist; no numeric changes).
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the `lecture_9.tex` edits.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).
- `notes_output/lecture_2_part_i.tex`: demoted two tiny TOC subsections ("Limitations of Safe Transformations" and
  "Example: Solving an Integral via Transformation Trees") into labeled paragraphs to reduce TOC noise, and expanded
  the limitations paragraph to better motivate the switch from safe to heuristic moves (no math changes).
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the `lecture_2_part_i.tex` edits.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).
- `notes_output/lecture_5_part_ii.tex`: demoted the one-line "Hopfield Network States and Energy Function" subsection to a
  labeled paragraph and expanded the intro of the convergence subsection to make the proof's assumptions and role explicit.
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the `lecture_5_part_ii.tex` edits.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).
- `notes_output/lecture_transformers.tex`: expanded the "Fine-Tuning and Parameter-Efficient Adaptation" and "Alignment"
  subsections so they read as substantive book prose rather than one-line notes; added explicit audit hooks (no numeric changes).
- `notes_output/lecture_4_part_i.tex`: demoted the short "Challenges in Weight Updates" subsection to a labeled paragraph,
  added a one-sentence bridge to backprop's \(\delta\) intuition, and fixed a truncated sentence in the forward-pass recap.
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the Transformer/backprop edits.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).

## 2026-02-20 Part II rollover editorial scan (global issues)

- Wrote a Part II rollover analysis (global continuity + TOC fragmentation policy + start-of-Part-II chapter packet) to:
  `notes_output/review/part_ii_rollover_editorial_20260220.md`.

- `notes_output/lecture_3_part_i.tex`: inserted the approved Part II local roadmap box as a labeled paragraph
  (`\paragraph{Where this fits in Part II.}`) to reduce TOC fragmentation while preserving the existing label
  `sec:perceptron_outline_of_neural_network_study`.
- `notes_output/lecture_3_part_i.tex`: added a worked, numeric OR-gate perceptron update trace (kept compact and
  mistake-driven) and wired it into strict validation via a QC comment block + Python check.
- 2026-02-20: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the perceptron
  OR-gate walkthrough addition. Result: PASS.
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the `lecture_3_part_i.tex` perceptron
  OR-gate walkthrough + roadmap paragraph/label change. Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits
  + EPUBCheck all OK).
- 2026-02-20: Re-ran `bash notes_output/scripts/run_production_checks.sh` after a minor wording clarification inside the
  perceptron OR-gate box (explicit \(\ge 0\) prediction rule). Result: PASS.
- 2026-02-20: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after small Part II
  Chapter 5 polish (Learning Outcomes cross-ref + shapes/dimensions concrete check). Result: PASS.
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the latest Part II Chapter 5 edits.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).

- `notes_output/lecture_3_part_ii.tex`: adjusted the chapter opening and workflow paragraph to use book voice (no meta
  ``Part II contract'' phrasing) while still making the objective\(\rightarrow\)optimize\(\rightarrow\)verify loop explicit.
- 2026-02-20: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the wording pass in
  `lecture_3_part_ii.tex`. Result: PASS.
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the wording pass in `lecture_3_part_ii.tex`.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).

- `notes_output/lecture_3_part_ii.tex`: rewrote the templated boxes (Learning Outcomes / Design motif / Author's notes /
  Key takeaways / Exercises) to read in a more natural book voice and to be more specific to the two-neuron chain and
  fail-fast verification habits (kept all math unchanged).
- 2026-02-20: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the template/voice
  rewrite in `lecture_3_part_ii.tex`. Result: PASS.
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the template/voice rewrite in
  `lecture_3_part_ii.tex`. Result: PASS.

- `notes_output/lecture_3_part_ii.tex`: reduced the over-emphasis on backpropagation framing throughout the chapter
  (kept a single explicit handoff in ``Where we head next.''), and removed the banned course-voice phrase ``next chapter''.
- 2026-02-20: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the backprop
  de-emphasis rewrite in `lecture_3_part_ii.tex`. Result: PASS.
- 2026-02-20: Ran `bash notes_output/scripts/run_production_checks.sh` after the backprop de-emphasis rewrite in
  `lecture_3_part_ii.tex`. Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).
- 2026-02-20: Ran `python3 notes_output/scripts/chapter_format_audit.py --write` to confirm the course-voice warning was
  cleared. Result: PASS (no ``next chapter'' warning).

## 2026-02-21 Part II Chapter 6 (MLP) voice pass

- `notes_output/lecture_3_part_ii.tex`: replaced 10 key paragraphs with author-edited book-voice prose (unit-to-chain
  framing, network intuition, checklist, bias explanation, squared-error intuition, geometry/step-size intuition,
  threshold/differentiability motivation, sigmoid derivative sketch, and the end-of-chapter handoff).
- `notes_output/lecture_3_part_ii.tex`: removed the LLM-y ``Use it when ...'' sentence from three figure captions
  (`fig:mlp_minimal_chain`, `fig:mlp_gd_surface`, `fig:mlp_step_vs_sigmoid`).
- 2026-02-21: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the paragraph/caption
  voice pass in `lecture_3_part_ii.tex`. Result: PASS.
- 2026-02-21: Ran `bash notes_output/scripts/run_production_checks.sh` after the paragraph/caption voice pass in
  `lecture_3_part_ii.tex`. Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).

## 2026-02-21 Part II Chapters 5--6 boundary micro-tweaks

- `notes_output/lecture_3_part_i.tex`: adjusted Part II roadmap phrasing to avoid course-voice ``next ...'' framing
  (``How the next chapters build.'' $\rightarrow$ ``How the rest of Part II builds.''), and softened ``next section''
  to ``section that follows''.
- `notes_output/lecture_3_part_i.tex`: removed the LLM-y ``Use it when ...'' sentence from the perceptron-geometry
  figure caption (`fig:lec3-perceptron-geometry`).
- 2026-02-21: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the boundary
  micro-tweaks. Result: PASS.

## 2026-02-21 Part II Chapter 7 (Backprop) initial sweep

- `notes_output/lecture_4_part_i.tex`: rewrote `\paragraph{Challenges in weight updates}` to emphasize credit assignment
  and the chain-rule sensitivity story in book voice (enrichment, not deletion).
- `notes_output/lecture_4_part_i.tex`: removed the LLM-y ``Use it when ...'' sentence from three figure captions
  (`fig:backprop-computational-graph`, `fig:lec4_backprop_flow`, `fig:lec4-activations`).
- 2026-02-21: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the Chapter 7 edits.
  Result: PASS.
- 2026-02-21: Ran `bash notes_output/scripts/run_production_checks.sh` after the Chapter 7 edits.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).

## 2026-02-21 Part II Chapter 7 (Backprop) mini-example split + verification

- `notes_output/lecture_4_part_i.tex`: split the early ``Mini example'' box into two pedagogical roles:
  (i) a minimal MSE-aligned backprop step (consistent with the main derivation), and (ii) a later
  ``modern practice'' implementation pattern box (softmax + cross-entropy, dropout, weight decay).
- `notes_output/lecture_4_part_i.tex`: replaced the placeholder ``Example Execution'' paragraph with a short,
  book-voice prompt to run the numeric trace and a finite-difference check.
- `notes_output/scripts/validate_math_examples_and_graphs.py`: added `chapter4_softmax_ce_grad`, a finite-difference
  gradient check that verifies the softmax+cross-entropy identity \(\delta^{(L)} = ( \hat{Y} - Y )/B\) (with ReLU and
  L2 penalty) for a tiny network.
- 2026-02-21: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the example split
  and new check. Result: PASS.
- 2026-02-21: Ran `bash notes_output/scripts/run_production_checks.sh` after fixing an overfull line in the verbatim code
  box (warning gate). Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).

## 2026-02-21 Part II Chapter 7 (Backprop) activation + convergence voice sweep

- `notes_output/lecture_4_part_i.tex`: rewrote ``Remarks on Convergence and Practical Considerations'' and the short
  activation-comparison lead-in to reduce templated phrasing while keeping the same technical intent.
- `notes_output/lecture_4_part_i.tex`: removed course-voice ``this closes... next we...'' phrasing after the activation
  trade-offs paragraph; replaced with book voice that points into the closing stability/takeaway boxes.
- `notes_output/lecture_4_part_i.tex`: fixed a minor list formatting indentation issue in ``Exercises and lab ideas''.
- 2026-02-21: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the voice sweep.
  Result: PASS.
- 2026-02-21: Ran `bash notes_output/scripts/run_production_checks.sh` after the voice sweep.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).

## 2026-02-21 Part II Chapter 7 (Backprop) box de-templating pass (start-to-end)

- `notes_output/lecture_4_part_i.tex`: rewrote the chapter's tcolorbox content (design motif, intuition, shape ledger,
  optimizer notes, debugging checklist, mini-batch regularization recipe, key takeaways, early stopping, derivation
  closure, exercises) into a more specific, book-voice style while preserving math and cross-refs.
- 2026-02-21: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the box rewrite.
  Result: PASS.
- 2026-02-21: Ran `bash notes_output/scripts/run_production_checks.sh` after the box rewrite.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).

## 2026-02-21 Part II Chapter 7 (Backprop) mid/late chapter de-templating + verification hygiene

- `notes_output/lecture_4_part_i.tex`: rewrote the opening paragraph and several mid/late sections (momentum update,
  epochs/training procedure, hidden-layer design, case-study framing, applications summary, conclusion lead-in) to reduce
  transcript/template tone.
- `notes_output/lecture_4_part_i.tex`: removed an unverified empirical performance claim in the \(y=x\sin x\) case study
  (replaced with reproducibility guidance instead of quoting a single MAE number).
- 2026-02-21: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the mid/late sweep.
  Result: PASS.
- 2026-02-21: Ran `bash notes_output/scripts/run_production_checks.sh` after the mid/late sweep.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).

## 2026-02-21 Part II Chapter 7 (Backprop) tail cohesion pass (case study/applications/limitations/conclusion)

- `notes_output/lecture_4_part_i.tex`: rewrote ``Limitations'' to tie directly to the earlier shape ledger, gradient
  checks, and activation diagnostics (so the limitations read as actionable failure modes, not generic warnings).
- `notes_output/lecture_4_part_i.tex`: tightened the ``Conclusion'' recap prose (kept the matrix-form equations and
  labels intact) and reduced duplication by pointing the key-takeaway box back to the recap equations.
- 2026-02-21: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the tail sweep.
  Result: PASS.
- 2026-02-21: Ran `bash notes_output/scripts/run_production_checks.sh` after the tail sweep.
  Result: PASS (PDF build + EPUB builds + Apple gatekeeper audits + EPUBCheck all OK).

## 2026-02-21 Part II Chapter 5 (Perceptron) author-voice paragraph swap

- `notes_output/lecture_3_part_i.tex`: replaced ``Complexities and Unknowns'' with an author-voice paragraph that
  clarifies the biology\(\rightarrow\)engineering abstraction (what we keep vs.\ what we ignore) and anchors it with a
  circuit-design analogy.
- 2026-02-21: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the swap. Result: PASS.

## 2026-02-21 Part II Chapter 11 (CNN) data/compute/overfitting framing polish

- `notes_output/lecture_6.tex`: rewrote the CNN ``Data requirements'' block to treat the ``10x parameters'' heuristic as
  a warning sign (not a law), and to explicitly connect sample efficiency to inductive bias (convolutions), regularization,
  augmentation, and pretraining.
- `notes_output/lecture_6.tex`: tightened the computational/storage paragraph to keep it architecture-first (what dense
  layers cost vs.\ what convolution buys) without drifting into generic ``hardware'' notes.
- `notes_output/lecture_6.tex`: rewrote the overfitting paragraph into concrete audits (train/val gap, calibration, and
  slice checks) rather than treating ``high training accuracy'' as evidence.
- 2026-02-21: Ran `bash notes_output/scripts/run_production_checks.sh` after the CNN edits. Result: PASS (release checks,
  Apple gatekeeper audits, and EPUBCheck all OK).

## 2026-02-22 Part II Chapter 7 (Backprop) self-sufficiency clarifications (error + notation)

- `notes_output/lecture_4_part_i.tex`: made the squared-error setup explicit by defining the error \(e_k=a_k^{(L)}-t_k\),
  \(\mathbf{e}=\mathbf{a}^{(L)}-\mathbf{t}\), and stating \(\partial \mathcal{L}/\partial a_k^{(L)}=e_k\) (so the start of
  the backward pass is not implicit). Added a short note about sum-vs-mean loss scaling over a mini-batch.
- `notes_output/lecture_4_part_i.tex`: removed a \(\phi\) vs.\ \(f\) activation-function notation mismatch by standardizing
  the scalar and matrix-form recaps to use \(f\) (and \(f^{(l)}\) for layer-specific activations).
- `notes_output/lecture_4_part_i.tex`: clarified a few implementation assumptions: numerically stable softmax phrasing,
  batch/SGD update wording, and the meaning of the update-step index \(n\) in the momentum update.
- `notes_output/lecture_4_part_i.tex`: de-templated several narrative blocks (opening framing, reverse-mode summary,
  optimizer notes, applications/limitations/conclusion bridge, and the closing RBF pointer) to reduce course-voice/LLM-y
  phrasing and keep the emphasis on concrete debugging habits. Also reduced overuse of the word ``bookkeeping''.
- 2026-02-22: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the clarity edits.
  Result: PASS.
- 2026-02-22: Ran `bash notes_output/scripts/run_production_checks.sh` after the de-templating edits (fixed a transient
  overfull verbatim line and restored the required ``Where we head next.'' paragraph title). Result: PASS (release checks,
  Apple gatekeeper audits, and EPUBCheck all OK).

## 2026-02-22 Part II Chapter 7 (Backprop) figure placement + micro-de-templating

- `notes_output/lecture_4_part_i.tex`: moved the activation-comparison block (Remarks on Convergence + Figure 27 +
  trade-offs) earlier in the chapter (immediately before the case study) so readers see the diagnostic picture before it
  is referenced in the Limitations section. This also fixes the EPUB anchor order (Figure 27 no longer appears far after
  its first mention).
- `notes_output/lecture_4_part_i.tex`: inserted `\FloatBarrier` after Figures 26 and 27 to reduce float drift (so they do
  not end up at the end of the chapter in PDF/EPUB).
- `notes_output/lecture_4_part_i.tex`: applied small phrasing fixes to remove remaining template tone (``we now focus'' to
  ``the next step is'', softened an SGD claim, and adjusted ``we will revisit'' to ``later chapters return'').
- 2026-02-22: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the figure moves.
  Result: PASS.
- 2026-02-22: Ran `bash notes_output/scripts/run_production_checks.sh` after the figure moves. Result: PASS (release checks,
  Apple gatekeeper audits, and EPUBCheck all OK).

## 2026-02-22 Part II Chapter 8 (RBFNs) EPUB figure-order hygiene + caption cleanup

- `notes_output/lecture_4_part_ii.tex`: removed ``Use it when ...'' caption tails and tightened captions into plain book
  prose (kept the instructional intent without meta language).
- `notes_output/lecture_4_part_ii.tex`: reduced EPUB float drift by inserting `\FloatBarrier` after the chapter's major
  figures (architecture, Gaussian-bump intuition, center placement, sigma sweep, primal/dual summary, XOR boundary).
- `notes_output/lecture_4_part_ii.tex`: fixed a \(\phi\)/\(\varphi\) mismatch in the Gaussian-bumps figure legend to match
  the chapter's \(\varphi_i(\cdot)\) basis notation.
- `notes_output/lecture_4_part_ii.tex`: moved long-range figure references into the local neighborhood of the figure (e.g.,
  primal/dual and XOR boundary), so hyperlinks and anchors are consistent in EPUB.
- 2026-02-22: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-22: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-22 Part II Chapter 8 (RBFNs) de-templating + XOR narrative thread + Wiener sidebar collapse

- `notes_output/lecture_4_part_ii.tex`: rewrote the opening roadmap/motivation blocks to reduce template tone and align the
  narrative with the chapter's core idea: nonlinear representation (kernel-like radial features) plus a linear readout.
- `notes_output/lecture_4_part_ii.tex`: introduced an explicit XOR running thread early in the chapter to anchor intuition:
  the hidden layer performs the transformation; the output weights define the separating border in the transformed space.
- `notes_output/lecture_4_part_ii.tex`: renamed ``Author's note'' headings to read like book prose (kept the content).
- `notes_output/lecture_4_part_ii.tex`: collapsed the Wiener-filter refresher from a full derivation into a single boxed
  paragraph mapping Wiener normal equations to the RBF design-matrix solve (so it is easy to ignore without losing the
  main thread). Removed now-unused Wiener equation labels.
- `notes_output/lecture_4_part_ii.tex`: added a before/after XOR figure that places input-space geometry next to the
  transformed \((g_1,g_2)\) feature space (with one explicit separating border), to visually drive home the
  ``transform-then-separate'' story. The numeric coordinates and the separator were verified in Python.
- `notes_output/scripts/validate_math_examples_and_graphs.py`: extended the Chapter 8 RBF transform check to verify all four
  XOR corners in feature space (including the off-diagonal coincidence) and to confirm a valid separating border
  (\(g_1+g_2=1.3\), i.e., \(w=[1,1]\), \(b=-1.3\)).
- 2026-02-22: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-22: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-22 Part II Chapter 8 (RBFNs) XOR boundary sigma sweep (figure truthfulness)

- `notes_output/lecture_4_part_ii.tex`: replaced the single XOR boundary plot with a 3-panel sigma sweep
  (\(\sigma=2.0,0.8,0.25\)) so the figure explicitly supports the text claim: broad bases wash out locality, balanced
  widths separate cleanly, and overly local widths create island-like decision regions.
- `notes_output/scripts/gen_rbf_xor_sigma_sweep_tables.py`: added a deterministic generator for the PGFPlots tables used in
  the 3-panel XOR boundary figure (class-region tables + 0.5 contour tables).
- `notes_output/rbf_xor_sigma*_boundary_class_table_with_breaks.dat`, `notes_output/rbf_xor_sigma*_contour_0p5.dat`:
  committed the generated data tables for \(\sigma=2.0,0.8,0.25\).
- `notes_output/scripts/validate_math_examples_and_graphs.py`: added a strict check that recomputes the model and asserts
  the committed sigma-sweep class tables match the model on the full 29x29 grid; also asserts the intended qualitative
  properties (low contrast at \(\sigma=2.0\), high contrast at \(\sigma=0.8\), island-like regions at \(\sigma=0.25\)).
- 2026-02-22: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-22: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-23 Part II Chapter 8 (RBFNs) additional figure truthfulness sweeps

- `notes_output/lecture_4_part_ii.tex`: marked the \(\sigma\)-sweep sketch as explicitly schematic (removed the misleading
  ``two-moons'' label) and pointed readers to the computed XOR sigma-sweep figure for an actual boundary.
- `notes_output/scripts/validate_math_examples_and_graphs.py`: added strict checks for two analytic figures:
  (i) the Gaussian-bumps intuition plot verifies the ``sum'' curve equals the sum of the displayed basis functions, and
  (ii) the XOR feature-map before/after figure verifies the plotted coordinates and separating border match the analytic
  mapping in the text.
- 2026-02-23: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-23: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-23 Part II Chapter 8 (RBFNs) notation consistency in conceptual figures (center symbols)

- `notes_output/lecture_4_part_ii.tex`: harmonized the center symbol across the chapter by replacing mixed center notation
  (\(\boldsymbol{\mu}_i\), \(\mathbf{v}_i\)) with \(\mathbf{c}_i\) in text and figures (XOR setup, transformation
  parameters, kernel examples, and parameter-estimation/training discussion).
- `notes_output/lecture_4_part_ii.tex`: tightened figure labels in the primal/dual schematic to match the chapter's
  notation (\(\boldsymbol{\Phi}\), \(\mathbf{w}\), \(\mathbf{K}\), \(\boldsymbol{\alpha}\), \(\mathbf{y}\)), and clarified
  that the center-placement figure is schematic (receptive-field overlap illustration, not a scale-accurate plot).
- 2026-02-23: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-23: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-23 Chapters 1--4 figure caption voice + truthfulness markers (pre-Ch8 sweep)

- `notes_output/lecture_1_intro.tex`: rewrote the roadmap caption to remove template-style ``Use it when...'' phrasing while
  keeping the intent (dependency/prerequisite map for readers jumping ahead).
- `notes_output/lecture_2_part_i.tex`: tightened the transformation-tree caption to read like book prose and emphasize the
  role of the tree for diagnosing branching/backtracking (without meta ``use it when'' language).
- `notes_output/lecture_supervised.tex`: removed ``Use it when...'' from figure/table captions; marked clearly illustrative
  plots as schematic/illustrative where appropriate (under/overfit regime, learning curves); kept captions focused on what
  each diagram concretely shows.
- `notes_output/lecture_2_part_ii.tex`: removed ``Use it when...'' from captions; clarified which diagnostics are schematic
  (GD geometry) vs.\ illustrative (logistic boundary, MAP vs.\ MLE) without changing the math.
- 2026-02-23: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-23: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-23 Chapters 3/6/7/8 micro-fragmentation cleanup (run-in paragraph heads)

- `notes_output/lecture_supervised.tex`: removed tiny run-in paragraph heads (``Model.'', ``Objective.'', ``Closed form...'')
  in the linear-regression case study and merged them into contiguous book prose with light spacing cues.
- `notes_output/lecture_3_part_ii.tex`: replaced micro run-in paragraph heads (``Second layer.'', ``First layer.'', ``Error
  terms...'') with natural lead-in sentences so the derivation reads as a single flow without choppy headings.
- `notes_output/lecture_4_part_i.tex`: removed a micro run-in paragraph head (``Chain rule decomposition'') and folded the
  transition into the surrounding derivation; kept interpretation as an inline bold lead-in.
- `notes_output/lecture_4_part_ii.tex`: removed a micro run-in paragraph head (``Normal Equations for the Weights:'') so the
  normal-equations derivation reads as one continuous argument.
- 2026-02-23: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-23: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-23 Chapters 1/4/5/6/8 voice pass (author notes + opening roadmap phrasing)

- `notes_output/lecture_1_intro.tex`: rewrote the Level~4 ``subject of its own thought'' author note in a clearer first-person
  voice (kept it explicitly opinionated).
- `notes_output/lecture_2_part_ii.tex`: rewrote the Design motif and the ``why logistic/why regression'' author note to match a
  book voice while keeping the intent.
- `notes_output/lecture_3_part_i.tex`: softened ``contract'' language to ``what stays the same'' and tightened the perceptron
  expressivity author note (kept the stance, improved cadence).
- `notes_output/lecture_3_part_ii.tex`: rewrote the MLP author notes (objective choice, caching derivatives, scaling up) to read
  as intentional author commentary rather than templated notes; removed speculative AGI/ASI claims while keeping the core
  engineering point.
- `notes_output/lecture_4_part_ii.tex`: removed the ``How to read this chapter'' paragraph header and rewrote the opening block
  as plain narrative orientation within the overview.
- 2026-02-23: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-23: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-23 Chapters 1--8 completion sweep (fig truthfulness + numeric verification coverage)

- `notes_output/scripts/validate_math_examples_and_graphs.py`: added a strict verification for the Chapter 2 symbolic-integration
  vignette (Beta-template fallback). The check recomputes the perturbed Beta integral numerically and asserts the displayed
  value (\(\approx 0.0915453885\)) is correct, and that the stated Beta closed form \(B(3/2,2)=4/15\) matches.
- 2026-02-23: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.

## 2026-02-23 Chapter 9 (SOMs) figure truthfulness + numeric example completion

- `notes_output/lecture_5_part_i.tex`: removed remaining template-y ``Use it when...'' caption phrasing; tightened figure captions
  to mark schematic/toy intent where appropriate; resolved centroid symbol collision in the K-means warm-up
  (\(\mathbf{v}_k\rightarrow\mathbf{m}_k\)); completed the competitive-learning numeric example with one explicit winner selection
  and winner-only update step.
- `notes_output/scripts/validate_math_examples_and_graphs.py`: added a strict QC-backed validator (`som_competitive_learning_example`)
  for the competitive-learning numeric walkthrough.
- 2026-02-23: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-23: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-24 Chapter 9 (SOMs) enrichment + author-voice threading (opening-to-closing pass)

- `notes_output/lecture_5_part_i.tex`: re-voiced the opening bridge and SOM overview into book voice; replaced ``lattice'' with
  ``grid'' throughout the reader-facing prose/figures; strengthened the clustering warm-up with an engineering-motivated example
  and explicitly threaded k-means \(\rightarrow\) SOM; clarified ``topographic mapping'' without over-promising; reframed the
  Kohonen architecture subsection as a distinct ``network diagram'' view (without repeating earlier derivations verbatim);
  added an author note on distance/preprocessing as part of the model; tightened the applications/variants/recipes wrap-up to
  read less like generic notes and more like a practitioner summary.
- `notes_output/review/writeup_tasks_from_codex_20260218.md`: added a new write-up task requesting two SOM application vignettes
  in the author’s voice (to further enrich the Applications section without guessing intent).
- 2026-02-24: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-24: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-24 Chapter 9 (SOMs) lecture-material alignment (QE/TE + tool-choice + WTA->cooperation)

- `notes_output/lecture_5_part_i.tex`: added a strict numeric walkthrough contrasting QE vs TE (with a deliberate topographic
  ``tear'' example); rewrote the \(3\times 3\) SOM example to remove checklist repetition and point back to the verified tiny
  update; strengthened the WTA limitations section with the explicit ``prototypes vs map'' failure mode and the role of the
  \(\sigma(t)\) schedule; added an author note box on when SOMs are the wrong tool; inserted two website-oriented application
  examples (sessions and pages) in the Applications section.
- `notes_output/scripts/validate_math_examples_and_graphs.py`: added a strict validator (`som_qe_te_example`) for the QE/TE
  numeric check (QC-backed from the TeX source).
- `notes_output/lecture_5_part_i.tex`: added the explicit neighborhood-width schedule \(\sigma(k)=\sigma_0 e^{-k/\tau}\) near the
  Gaussian neighborhood definition to match the handnotes.
- 2026-02-24: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-24: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-24 Chapter 9 (SOMs) EPUB chapter numbering fix

- `notes_output/lecture_5_part_i.tex`: removed the optional short-title argument from the Chapter 9 `\\section[...]` heading.
  The EPUB navigation document (`EPUB/nav.xhtml`) uses that short title, which previously suppressed the ``Chapter 9:'' prefix
  in the reader's table of contents. After this change the ToC entry renders as
  ``Chapter 9: Introduction to Self-Organizing Networks and Unsupervised Learning''.
- 2026-02-24: Ran `bash notes_output/scripts/run_production_checks.sh` after the edit. Result: PASS (EPUB nav/ToC updated,
  PDF/EPUB builds and EPUBCheck all OK).

## 2026-02-24 Chapter 10 (Hopfield) numeric truthfulness + QC-backed example

- `notes_output/lecture_5_part_ii.tex`: removed remaining template-y ``Use it when...'' phrasing in the Hopfield example
  captions; added a QC block for the 3-neuron energy example and tightened the narrative so the energy-descent figure matches
  the stated one-flip recovery; corrected the synchronous-update caveat to use a true 2-cycle under the update rule (instead of
  an arbitrary flip story); reduced duplicate prose in the Hebbian weight example.
- `notes_output/scripts/check_numeric_examples.py`: made the Hopfield numeric check QC-backed by parsing the TeX QC block
  (`hopfield_energy_example`) rather than relying on hard-coded values; also verifies one asynchronous update from a noisy probe.
- 2026-02-24: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-24: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-24 Chapter 10 (Hopfield) pedagogy enrichment + additional QC-backed example

- `notes_output/lecture_5_part_ii.tex`: added an ``engineering lens'' box to reinforce reading \(E(\mathbf{s})\) as an objective;
  added a schematic basin-of-attraction figure and a short ``applications lens'' box (associative recall + optimization framing);
  expanded the single-pattern Hebbian example to show the explicit outer product, the normalized weight matrix, and a fixed-point
  sanity check (\(\operatorname{sign}(Wb)=b\)).
- `notes_output/scripts/check_numeric_examples.py`: extended the Hopfield check to parse a second QC block
  (`hopfield_single_pattern_weights`) and verify the displayed \(4\times 4\) Hebbian weight matrix and local-field vector.
- 2026-02-24: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-24: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-24 Chapter 10 (Hopfield) de-sliding + notation unification + recall trace

- `notes_output/lecture_5_part_ii.tex`: unified stored-pattern notation to \(\mathbf{\xi}\) throughout the Hebbian and example
  sections (previously mixed \(\mathbf{b}\) and \(\mathbf{\xi}\)); rewrote several slide-like bullet clusters into book-voice
  prose (general RNN challenges, Hopfield constraints, and limitations); added a compact two-flip recall trace (two-bit-corrupted
  probe \(\rightarrow\) stored pattern) immediately after the single-pattern Hebbian weight derivation.
- `notes_output/scripts/check_numeric_examples.py`: extended the Hopfield single-pattern QC check to validate the two-step
  asynchronous recall trace (local fields, updated states, and energies).
- 2026-02-24: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-24: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-24 Chapter 10 (Hopfield) collaborative rewrite pass + QC-backed memory recovery

- `notes_output/lecture_5_part_ii.tex`: applied the approved ``before \(\rightarrow\) after'' rewrites: removed the meta
  ``handoff'' label, tightened the energy-view roadmap sentence, rewrote the later memory-recovery example to be an explicit
  one-flip trace (local field + energy drop), and re-voiced the ``historical significance'' and ``connections'' paragraphs into
  book voice.
- `notes_output/lecture_5_part_ii.tex`: added a QC block (`hopfield_memory_recovery_4n`) for the later 4-neuron one-flip recall
  example to ensure the matrix/local-field/energy claims remain truthful.
- `notes_output/scripts/check_numeric_examples.py`: extended the Hopfield QC checker to parse and verify that QC block.
- 2026-02-24: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-24: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-24 Chapter 10 (Hopfield) final de-sliding sweep (example narration + capacity prose)

- `notes_output/lecture_5_part_ii.tex`: rewrote the 3-neuron ``state update attempts'' list into narrative prose while keeping
  the numeric values and pointing to \Cref{tab:hopfield-deltaE}; de-slid the storage-capacity subsection by folding the
  ``classical result'' and ``inefficiency'' fragments into one cohesive paragraph; removed the standalone ``Conclusion:'' label
  in the async-vs-sync subsection; tightened the continuous-Hopfield bridge to avoid over-claiming while preserving the
  attention intuition.
- 2026-02-24: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-24: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-25 Chapter 10 (Hopfield) terminology + continuity + exercise upgrade + EPUB placement spot-check

- `notes_output/lecture_5_part_ii.tex`: added a compact terminology/diagnostics box defining attractor, basin, spurious state,
  and overlap \(m^{(\mu)}\); strengthened the SOM\(\rightarrow\)Hopfield and Hopfield\(\rightarrow\)CNN continuity by explicitly
  contrasting the diagnostics (U-matrix/component planes vs energy/overlap, then energy/overlap vs training/validation curves);
  upgraded the lab exercise to require energy+overlap plots under a reproducible corruption protocol (fixed seed).
- `notes_output/lecture_5_part_ii.tex`: renamed the Hopfield single-pattern QC tag from `b` to `xi` for consistency with the
  reader-facing notation.
- `notes_output/scripts/check_numeric_examples.py`: updated the QC parser to accept either `b` or `xi` tags for that block.
- 2026-02-25: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-25: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-26 Chapter 12 (RNN) de-slide pass (remove ``vanilla'' + reduce early ``context'' phrasing)

- `notes_output/lecture_7.tex`: replaced the slide-like ``Summary'' line with a short ``What recurrence buys you'' paragraph
  (feedforward vs.\ history features, versus state carried forward).
- `notes_output/lecture_7.tex`: rewrote the roadmap and ``Simple RNN at a glance'' block into book-voice prose (kept all the
  objective/knobs/pitfalls content without checklist bullets).
- `notes_output/lecture_7.tex`: converted the input--output configuration bullets into a single paragraph and removed the
  premature ``context vector'' language (replaced with a conditioning signal / encoder output phrasing).
- `notes_output/lecture_7.tex`: rewrote the ``RNN vs.\ GRU vs.\ LSTM'' comparison into prose and removed ``vanilla''
  terminology in favor of ``simple (ungated)''.
- `notes_output/lecture_7.tex`: converted the semicolon-style pitfalls line into an itemized ``Common pitfalls'' list.
- `notes_output/lecture_7.tex`: rewrote the late ``From corpus to next-token model'' checklist into prose; removed repeated
  ``bookkeeping'' phrasing and used ``prefix/history'' language where ``context'' felt premature in this chapter.
- 2026-02-26: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-26: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-26 Chapter 1 + Chapter 14: model/world-model lens insertion

- `notes_output/lecture_1_intro.tex`: added a short, stable definition of ``model'' near the start of the book so later
  chapters can reuse the same contract (mapping information to predictions; distributions when appropriate).
- `notes_output/lecture_transformers.tex`: added an author-voice perspective box introducing ``world model'' as an
  aspirational concept and stating the ``LMs do not guarantee a world model'' claim explicitly as opinion.
- 2026-02-26: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-26: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-26 Terminology note: define ``vanilla'' once (plain baseline) at first appearance

- `notes_output/lecture_6.tex`: defined ``vanilla'' as the common ML shorthand for ``plain/unmodified baseline'' (here:
  plain SGD) so students recognize the term when they encounter it in code/papers.
- 2026-02-26: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edit. Result: PASS.
- 2026-02-26: Ran `bash notes_output/scripts/run_production_checks.sh` after the edit. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-26 Chapter 11 (CNN) pedagogy completion (equivariance/invariance + losses/metrics + receptive-field quick check)

- `notes_output/lecture_6.tex`: aligned the learning-outcomes box with the chapter's delivered content (loss/metric intent,
  CNN-as-features lens, and stability failure signatures).
- `notes_output/lecture_6.tex`: defined translation equivariance vs.\ invariance at first use and tied invariance to pooling
  and downsampling.
- `notes_output/lecture_6.tex`: reduced slide-like micro-fragmentation in the ``fully connected layers break on images''
  section by rewriting the opener as continuous prose while preserving the numeric parameter-count derivation.
- `notes_output/lecture_6.tex`: added a short ``Losses, metrics, and the CNN as features viewpoint'' box to connect
  cross-entropy vs.\ regression losses, calibration, and the soft-margin/hinge geometry from \Cref{chap:supervised}.
- `notes_output/lecture_6.tex`: added a compact ``Quick check'' box to reinforce receptive-field growth for stacked \(3\times3\)
  kernels (3, 5, 7, ...).
- 2026-02-26: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-26: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).
- EPUB placement spot-check: in `EPUB/text/ch016.xhtml`, the Hopfield figures appear near their first references (energy-descent
  and basin-schematic figures are inline with links in the surrounding paragraphs; no float drift observed for Chapter 10).

## 2026-02-26 Part II (up to RNN) terminology + de-slide polish

- `notes_output/lecture_7.tex`: reduced language-model-first framing so the RNN chapter reads as general sequence modeling
  (next-step prediction as the generic task; language modeling moved into an explicitly labeled optional preview, with a
  forward pointer to \Cref{chap:nlp} for tokenization/embeddings/perplexity).
- `notes_output/lecture_7.tex`: removed the last ``Vanilla'' phrasing (renamed the BPTT pseudocode box to ``Simple (ungated)'')
  and tightened the ``steps/representations'' terminology paragraph to emphasize \(\mathbf{x}_t\) as the generic numeric input.
- `notes_output/lecture_6.tex`: replaced ``bookkeeping'' phrasing with more direct ``accounting'' language in the convolution
  terminology note, the dimensionality example box title, and the common-pitfall bullet (keeps the same meaning, less jargon).
- `notes_output/lecture_3_part_i.tex`, `notes_output/lecture_3_part_ii.tex`: similarly replaced repeated ``bookkeeping'' uses
  with ``accounting''/``tracking'' to reduce drift and keep a consistent engineering tone across Part II.
- EPUB sanity: the current `epub_builder/dist/*` navigation TOCs include ``Chapter 9'' (SOM) correctly; a missing ``9'' in a
  reader is likely an older/cached EPUB.
- 2026-02-26: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-26: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-26 Part I (Chapters 1--4) slide-to-prose + define-at-first-use polish

- `notes_output/lecture_1_intro.tex`: converted the autonomous-vehicle component bullets into continuous prose (same content,
  less slide-like) and expanded common acronyms at first mention in the camera-system checklist (CMOS/DSP/MPC). Kept the
  example concrete while making it read as book narrative.
- `notes_output/lecture_2_part_i.tex`: expanded AST at first use (abstract syntax tree) in the cost-heuristic paragraph.
- `notes_output/lecture_supervised.tex`: expanded ERM and i.i.d. at first use to reduce cognitive load in later chapters.
- `notes_output/lecture_2_part_ii.tex`: expanded LDA/IRLS at first use; clarified logits/BCE wording; converted the Bayes
  ``Challenges in Practice'' bullets into a tight prose paragraph; added a one-time abbreviation note (ROC/PR/AUC/ECE/AUROC/
  AUPRC) immediately before the Risk \& audit box.
- 2026-02-26: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-26: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-25 Chapter 10 (Hopfield) debug checklist + non-template modern-Hopfield tightening

- `notes_output/lecture_5_part_ii.tex`: added a short implementation checklist (symmetry/diagonal, energy convention, async vs
  sync updates, \(\operatorname{sign}(0)\) convention, and the expected diagnostics); tightened the modern-Hopfield/attention
  bridge language to clearly separate the geometric intuition from the classical Lyapunov guarantee.
- 2026-02-25: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-25: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-25 Chapter 11 (CNN) de-templating + caption cleanup + QC-backed numeric sanity checks

- `notes_output/lecture_6.tex`: de-templated the training-loop intro to align with the book voice (kept the GD contract but
  made the weight-sharing implication explicit); tightened the vanishing/exploding gradient discussion (removed a confusing
  one-line ``where'' clause; made consequences more concrete); rewrote the weight-initialization and BN blurbs into
  engineering prose; strengthened the gradient-clipping note as a safety valve; re-voiced the ``Derivation closure'' box
  and renamed ``Minimum viable mastery'' to ``A good checkpoint''.
- `notes_output/lecture_6.tex`: removed ``Use it when ...'' template phrasing from CNN figures (receptive field, dropout, BN,
  optimizer curves) and replaced with natural caption sentences.
- `notes_output/lecture_6.tex`: normalized the flattening example to a canonical \(256\times256\) image and updated all
  derived numbers (vector length, first-layer parameter count, and the back-of-the-envelope sample warning).
- `notes_output/lecture_6.tex`: added QC comment blocks for (i) flattening parameter counts, (ii) the 1D stride/padding
  cross-correlation worked example, and (iii) the 50x50x30 bookkeeping example (conv/pool/flatten sizes).
- `notes_output/scripts/check_numeric_examples.py`: added QC-backed CNN checks to parse and validate those blocks.
- `notes_output/scripts/validate_math_examples_and_graphs.py`: extended the strict numeric pack to include the CNN QC checks.
- 2026-02-25: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-25: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-25 Chapter 11 (CNN) numeric + subtle-math consistency audit

- `notes_output/lecture_6.tex`: aligned the sample-scale sanity-check estimate with the exact flattening parameter count
  (now \(10\times 6{,}553{,}600 \approx 65{,}536{,}000\), consistent with the earlier parameter-count equation and the QC
  block); removed a misleading ``gradient of weights chains like ...'' formula and replaced it with a correct error-signal
  recursion \(\boldsymbol{\delta}^{(\ell-1)}=(W^{(\ell)})^\top \boldsymbol{\delta}^{(\ell)}\odot f'(z^{(\ell-1)})\) to avoid
  subtle but important mathematical drift in the vanishing/exploding explanation.
- 2026-02-25: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-25: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-25 Chapter 11 (CNN) terminology + voice polish (receptive field + training loop)

- `notes_output/lecture_6.tex`: defined ``receptive field'' at its first use (what portion of the input can influence a unit)
  and briefly motivated the term as an engineering borrowing from sensory systems; tightened the training-loop paragraph to
  avoid anthropomorphic phrasing while keeping the key weight-sharing point.
- 2026-02-25: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-25: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-25 Chapter 11 (CNN) final de-templating polish

- `notes_output/lecture_6.tex`: removed remaining bloggy/template-y phrasing (``rhymes with'', ``promise'' framing, and
  ``engineering payoff is simple'') and replaced with a more direct book voice while preserving meaning.
- 2026-02-25: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-25: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-25 Chapter 12 (RNN) video-aligned de-templating + BPTT numeric check

- `notes_output/lecture_7.tex`: rewrote the motivation opener in a more assumption-driven, book voice (i.i.d.\ breaks on
  sequences; order carries information; the engineering fix is state + parameter sharing across time), aligned to the
  Lecture 7 board framing and examples (predictive text + time series) without adding dated or transcript-y phrasing.
- `notes_output/lecture_7.tex`: removed ``Use it when ...'' template phrasing from all Chapter 12 figure captions.
- `notes_output/lecture_7.tex`: converted the Hopfield aside into an explicit boxed historical note with a clean cross-ref to
  \Cref{chap:hopfield} and a short diagnostics contrast (energy/overlap vs.\ likelihood/perplexity + gradient health).
- `notes_output/lecture_7.tex`: replaced the slide-like ``Summary of the Modeling Pipeline'' enumeration with a minimal
  checklist box whose role is distinct from the earlier derivation/implementation boxes.
- `notes_output/lecture_7.tex`: replaced the out-of-scope convolution-size refresher with a short padding-mask reminder and an
  encoder/decoder bridge sentence that points forward to \Cref{chap:transformers}.
- `notes_output/lecture_7.tex`: added a tiny two-step scalar RNN numeric walkthrough showing how shared weights accumulate
  gradient contributions across time; included a QC comment block (`chapter12_bptt_two_step`).
- `notes_output/scripts/check_numeric_examples.py`: added `check_chapter12_bptt_two_step()` (analytic + finite-difference).
- `notes_output/scripts/validate_math_examples_and_graphs.py`: extended the strict numeric pack to validate the RNN QC block.
- 2026-02-25: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-25: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-26 Chapters 5--8 (Perceptron \textrightarrow{} MLP \textrightarrow{} Backprop \textrightarrow{} RBF) slide-fragment + definition-at-first-use sweep

- `notes_output/lecture_3_part_i.tex`: converted the AND/OR MP-neuron pseudo-bullets into a proper itemize block; expanded
  ERM at first use in the Part II roadmap box (empirical risk minimization).
- `notes_output/lecture_3_part_ii.tex`: expanded MLP at first use in the exercises (multi-layer perceptron).
- `notes_output/lecture_4_part_i.tex`: expanded MLP at first use in the opening paragraph; expanded MSE in the mini-example
  title (mean squared error); replaced ``reverse-mode AD'' with ``reverse-mode automatic differentiation (AD)'' and removed
  the unexplained ``TF'' abbreviation (TensorFlow spelled out); kept the verbatim softmax comment consistent (``cross-entropy''
  instead of ``CE'').
- `notes_output/lecture_4_part_ii.tex`: expanded SVMs at first use (support vector machines); tightened k-means wording;
  converted the XOR feature-map assumptions dashes into an itemize block; defined ``receptive field'' at first use; made
  the Nystr\"om reference explicit in one sentence; replaced ``CE/hinge'' with ``cross-entropy or hinge'' in training notes.
- 2026-02-26: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-26: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-26 Chapters 9--10 (SOM \textrightarrow{} Hopfield) slide-fragment + definition-at-first-use sweep

- `notes_output/lecture_5_part_i.tex`: expanded QE/TE and U-matrix at first use in the learning outcomes (quantization error,
  topographic error, unified distance matrix); rewrote the ``key characteristics'' bullet cluster into cohesive prose;
  tightened the ``basic architecture'' block into a single paragraph; expanded t-SNE/UMAP, CTR, and GTM at first use; added a
  short FAISS gloss in the complexity note.
- `notes_output/lecture_5_part_ii.tex`: defined ``Lyapunov energy'' at first use (a scalar that decreases under updates) and
  converted the bolded ``Limitations'' slide-like cluster into a proper itemize list while preserving content.
- 2026-02-26: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-26: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-26 Chapters 11--13 (CNN \textrightarrow{} RNN \textrightarrow{} NLP bridge) slide-fragment + definition-at-first-use sweep

- `notes_output/lecture_6.tex`: expanded ERM/MSE/BN/ECE/GPU at first use (empirical risk minimization, mean squared error,
  batch normalization, expected calibration error, graphics processing units); removed the slang ``vanilla SGD'' phrasing;
  expanded RGB and NaN once where used in training-debug bullets.
- `notes_output/lecture_7.tex`: expanded RNN at first use (recurrent neural networks); tightened the masked-loss pseudocode to
  keep the cross-entropy shorthand explicit without introducing long, overfull verbatim lines; defined cross-entropy (CE) and
  negative log-likelihood (NLL) at first abbreviation use inside the chapter.
- `notes_output/lecture_8_part_i.tex`: de-templated the early roadmap into book voice; standardized the embedding-table symbol
  from \(\mathbf{E}\) to \(\mathbf{W}\) and aligned the surrounding math; collapsed a micro-fragmented ``network architecture''
  stretch into cohesive prose while preserving the equations; added a toy analogy arithmetic box tied to the feature table; and
  rewrote the debiasing-techniques paragraph into compact prose while keeping the same content. Added a strict numeric check in
  `notes_output/scripts/validate_math_examples_and_graphs.py` that parses \Cref{tab:word_feature_vectorization} from the TeX
  source and asserts the identity \(\mathbf{v}(\text{king})-\mathbf{v}(\text{man})+\mathbf{v}(\text{woman})=\mathbf{v}(\text{queen})\).
- 2026-02-26: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-26: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-26 Chapter 14 (Transformers) rewrite: seq2seq \textrightarrow{} attention narrative + model-family framing

- `notes_output/lecture_transformers.tex`: rewrote the opening to start from the encoder--decoder bottleneck (translation as
  the running thread), then motivated attention as a weighted average before introducing the scaled dot-product formula.
- `notes_output/lecture_transformers.tex`: added an explicit self-attention vs.\ cross-attention subsection and aligned the
  narrative so Q/K/V intuition comes before the heavier equations.
- `notes_output/lecture_transformers.tex`: replaced the earlier worked example with a single 2-token causal self-attention
  walkthrough consistent with the strict numeric validator (and reformatted the display math to avoid overfull warnings).
- `notes_output/lecture_transformers.tex`: added sinusoidal positional encoding equations (\Cref{eq:transformers_sinusoidal_pe})
  and tightened the positional/relative/rotary discussion to stay medium-depth and book-voice.
- `notes_output/lecture_transformers.tex`: moved the masks figure (\Cref{fig:lec13_masks}) into the masks section and ensured
  it is referenced (figure/table reference coverage gate).
- `notes_output/lecture_transformers.tex`: aligned the embedding-table symbol in the code--math dictionary from \(\mathbf{E}\)
  to \(\mathbf{W}\) to match Chapter 13 notation.
- `notes_output/review/writeup_ch14_voice_blocks.md`: added a scratchpad scaffold for voice-heavy blocks so you can iterate on
  the phrasing without editing TeX directly.
- 2026-02-26: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-26: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).

## 2026-02-28 Chapter 14 (Transformers) dictation integration: seq2seq attention equations + verified retrieval analogy

- `notes_output/lecture_transformers.tex`: expanded the encoder--decoder bridge with explicit cross-attention equations
  (score/weights/context) and the translation factorization \(p(\mathbf{y}\mid\mathbf{x})=\prod_t p(y_t\mid y_{<t},\mathbf{x})\),
  keeping the narrative aligned with Chapter 12--13 sequence/embedding conventions.
- `notes_output/lecture_transformers.tex`: added a compact ``keys/values weighted retrieval'' intuition box (explicitly marked
  as an analogy) and tightened Q/K/V + multi-head notation so the projection dimensions are consistent.
- `notes_output/scripts/validate_math_examples_and_graphs.py`: added a strict numeric check (`chapter14_kv_weighted_retrieval`)
  that recomputes the analogy values/weights and asserts the displayed result.
- 2026-02-28: Ran `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` after the edits. Result: PASS.
- 2026-02-28: Ran `bash notes_output/scripts/run_production_checks.sh` after the edits. Result: PASS (release checks, Apple
  gatekeeper audits, and EPUBCheck all OK).
