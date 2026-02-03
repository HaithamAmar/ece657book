# Chapter Template (House Standard)

This project uses a strict, repeated chapter structure to maintain a premium “graduate companion” feel and to support reflowable EPUB conversion.

The automated checker is `notes_output/scripts/chapter_format_audit.py` (run via `notes_output/scripts/run_editorial_qc.sh`).

## Required blocks (in every numbered chapter)

Each chapter file under `notes_output/lecture_*.tex` must contain the following structural elements:

### 1) Opening “Learning Outcomes” box

- A `tcolorbox` with `title={Learning Outcomes}` near the chapter start.
- Purpose: the reader knows what to learn before they commit time.

### 2) Early “Design motif” hook

- A `tcolorbox` with `title={Design motif}` near the chapter start.
- Purpose: reinforces the book’s unifying pattern vocabulary.

### 3) End-of-chapter kit

Near the end of the chapter:

- A `tcolorbox` with `title={Key takeaways}`
- A `tcolorbox` with `title={Exercises and lab ideas}`
- A paragraph heading `\paragraph{Where we head next.}`
- A paragraph heading `\paragraph{References.}`

## Authoring rules that protect continuity

- Never hardcode numbers in prose (e.g., “see Chapter 7” / “see (10)”); use labels + refs:
  - Chapters/sections/figures/tables/appendices: `\Cref{...}`
  - Equations: `\eqref{...}`
- Keep `.tex` sources ASCII-only (per `notes_output/ONBOARDING.md`).
- Use consistent box titles and punctuation (the audit expects exact titles).

## Notes for EPUB friendliness

- Prefer “display math” (`equation`/`align`/`\[...\]`) over `\(\displaystyle ...\)` to avoid reader clipping.
- Keep tables readable; wide tables should be rare and intentional (the production gatekeeper flags them by default).

