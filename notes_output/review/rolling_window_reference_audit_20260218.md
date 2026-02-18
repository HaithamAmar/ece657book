# Rolling-Window Reference + Promise Audit (Part-by-Part)

- Date: 2026-02-18
- Goal: scan the manuscript in part-sized rolling windows (always including the Introduction) to cross-check
  forward/backward references across chapters and verify that the narrative promises made in the Introduction
  are paid off later.
- Constraint: do not remove numeric walkthroughs; only adjust numeric values when verified by Python.

## Method (repeatable)

For each part, read this rolling window:

- Always include: `lecture_1_intro.tex` (Introduction)
- Plus the part's chapters as listed in `book_chapters.tex`

Then:

1) Collect explicit cross-chapter pointers:
   - `\Cref{chap:*}`, `\Crefrange{chap:*}{chap:*}`, and “Where we head next.” paragraphs.
2) Collect implicit “promises”:
   - phrases like “later chapters…”, “we will revisit…”, “this returns in…”, “the next chapter…”.
3) Verify payoffs:
   - the referenced chapter/section exists (structural check),
   - the referenced topic actually appears where promised (semantic check),
   - forward pointers match the actual next chapters,
   - backward pointers remain true after later edits (no stale promises).

Programmatic spot-check (structural): parsed `lecture_1_intro.tex` for `chap:*` references and verified each
label is defined by a chapter included in `book_chapters.tex` (PASS; missing=0).

## Part I rolling window (Introduction + symbolic + supervised + logistic)

Window:
- `lecture_1_intro.tex`
- `lecture_2_part_i.tex` (symbolic integration)
- `lecture_supervised.tex` (linear regression)
- `lecture_2_part_ii.tex` (logistic regression)

Cross-chapter continuity checks:
- Introduction roadmap + reading paths are consistent with Part I chapter ordering and labels.
- “Where we head next.” handoffs are consistent and oriented around the book’s recurring loop:
  state/representation, actions/updates, objective, verification/audit.

Notes / potential enrichments:
- The Introduction’s camera-system case study is used to motivate later building blocks; later chapters
  do not explicitly “return to the camera” with a short payoff callout. This is not a broken promise,
  but adding 1–2 short callbacks (e.g., in the CNN and evolutionary chapters) could increase continuity.

## Part II rolling window (Introduction + perceptron/MLP/backprop + RBF/SOM/Hopfield + CNN/RNN/NLP/Transformers)

Window:
- `lecture_1_intro.tex`
- `lecture_3_part_i.tex`
- `lecture_3_part_ii.tex`
- `lecture_4_part_i.tex`
- `lecture_4_part_ii.tex`
- `lecture_5_part_i.tex`
- `lecture_5_part_ii.tex`
- `lecture_6.tex`
- `lecture_7.tex`
- `lecture_8_part_i.tex`
- `lecture_transformers.tex`

Cross-chapter continuity checks:
- “Where we head next.” paragraphs form a coherent chain: perceptron → MLP → backprop → RBF → SOM → Hopfield
  → CNN → RNN → NLP embeddings → Transformers → pivot to soft computing.
- Part II’s “rolling window” box in `book_chapters.tex` matches the repeated motifs actually used in these chapters:
  cached intermediates, gradient flow, masking discipline, and validation/audit habits.

Notes / potential enrichments:
- Several chapters use “preview vs formalization vs sanity-check” implicitly; Part II generally does this well.
  If desired, we can add one short “transfer cue” sentence at the start of the Hopfield chapter tying its
  associative-memory energy view to later attention-style retrieval (the analogy already appears in prose).

## Part III rolling window (Introduction + soft computing + fuzzy sets/relations/inference)

Window:
- `lecture_1_intro.tex`
- `lecture_8_part_ii.tex`
- `lecture_9.tex`
- `lecture_10_part_i.tex`
- `lecture_10_part_ii.tex`

Cross-chapter continuity checks:
- `lecture_8_part_ii.tex` explicitly closes Part II and previews the fuzzy trilogy structure; the trilogy chapters
  pay off that structure via consistent handoffs and repeated thermostat framing.
- Operator defaults and the “repetition is intentional” narrative (preview → algebra → end-to-end behavior)
  match the Part III “rolling window” box in `book_chapters.tex`.
- Forward pointer into Part IV (evolutionary tuning as a companion to fuzzy design) is explicit and consistent.

Notes / potential enrichments:
- If we want an even tighter Part III→IV bridge, we can add a short “tuning hook” sentence in `lecture_10_part_ii.tex`
  that explicitly names what will be tuned in Part IV (membership breakpoints, rule weights, penalty weights, etc.).

## Part IV rolling window (Introduction + evolutionary computing)

Window:
- `lecture_1_intro.tex`
- `lecture_11.tex`

Cross-chapter continuity checks:
- `lecture_11.tex` opening ties back to the book’s three earlier toolkits (Parts I–III) and positions evolutionary
  computing as the “budgeted optimizer” when smooth objectives/gradients or compact rule bases are inadequate.
- GA-loop repetition is now role-separated (preview vs formalization vs implementation checklist) without removing
  numeric walkthroughs.

Notes / potential enrichments:
- The Introduction notes swarm/decentralized update laws and says similar patterns appear in the evolutionary chapter.
  The evolutionary chapter currently frames the loop in prose/flowchart/pseudocode; adding one explicit “population update”
  equation (purely notational, not numeric) would make that payoff more concrete.

## Author material requests (optional)

If you want to enrich continuity beyond strict reference correctness, see:
- `notes_output/review/writeup_tasks_from_codex_20260218.md`

