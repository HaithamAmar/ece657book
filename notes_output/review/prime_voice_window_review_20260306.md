# PRIME Voice Window Review

- **Reviewer:** PRIME
- **Date:** 2026-03-06
- **Scope:** book-wide voice-consistency sweep after the Chapter 14 Transformer polish

## Method

I attempted a source-level rolling-window review with:

`python3 notes_output/scripts/review_tex_editorial.py --root notes_output --report notes_output/review/prime_voice_window_review_20260306.md --model gpt-5-mini --include-regex '^(lecture_.*\.tex|lecture_supervised\.tex|lecture_transformers\.tex|key_takeaways\.tex|fl-intro\.tex|preface\.tex|notation\.tex)$'`

That automated pass could not complete because network access to the model endpoint was unavailable in this environment. I therefore ran a manual fallback sweep using heuristic searches over the `.tex` sources, followed by direct inspection of each hit in context.

## Heuristic patterns reviewed

The fallback sweep looked for phrasing that tends to break neutral textbook voice when it appears outside clearly marked authorial boxes:

- stage-direction language (`Another pause`)
- direct classroom address (`students often`, `why students should care`)
- first-person framing outside `Author's note` boxes (`I like`, `I find`, `I reach`)
- imperative meta-commentary in ordinary prose (`Keep them separate`)

## Fixes applied in this pass

### Chapter 14

- Replaced the off-voice decoding transition with neutral book prose in `notes_output/lecture_transformers.tex`.
- Kept the new hand-holding transitions, but removed stage-direction phrasing and classroom-address wording.
- Split the dense end-of-chapter tail more clearly by separating the skip-ahead note from the exercises box.
- Removed the classroom-facing box title `why students should care`.
- Normalized one stray first-person sentence in ordinary prose (`One intuition I find useful` -> `A useful intuition`).

### Cross-book cleanup

- `notes_output/lecture_7.tex`: changed `The second term is the one students often miss` to a neutral explanatory sentence.
- `notes_output/lecture_5_part_i.tex`: removed first-person framing from the three-stage SOM summary, the engineering recipe, and the variants summary.
- `notes_output/lecture_5_part_ii.tex`: removed first-person/second-person phrasing from the Hopfield significance paragraph.

## Findings after cleanup

### Acceptable and consistent

The following patterns remain, but they are not random drift:

- **Explicit `Author's note` boxes** with first-person voice:
  - `notes_output/lecture_3_part_ii.tex`
  - `notes_output/lecture_5_part_i.tex`
  - `notes_output/lecture_transformers.tex`
- **`If you are skipping ahead` boxes** across multiple chapters. These now read as a deliberate pedagogical device rather than accidental voice drift.
- **Front matter first-person** in `notes_output/preface.tex` and `notes_output/acknowledgments.tex`, where personal voice is appropriate.

### No longer acceptable as random drift

The specific off-voice category that triggered this pass — stage-direction or classroom-address prose appearing in ordinary technical exposition — is no longer showing up as a random pattern in the main chapter body text inspected here.

## Remaining watch items

These are not blockers, but they are the next places to watch if a stricter voice normalization pass is ever desired:

1. the repeated `If you are skipping ahead` box title, if you later want a less classroom-coded label;
2. first-person heuristics in front matter and explicit authorial boxes, if you ever decide to reduce author presence globally rather than only outside marked boxes.

## Conclusion

The book now reads more consistently under its own stated rule:

- neutral textbook voice in ordinary exposition;
- more personal or opinionated voice only where clearly signaled by an `Author's note` or equivalent pedagogical box.

I do not see evidence of the Chapter 14-style tone slip appearing randomly across the manuscript after this cleanup.
