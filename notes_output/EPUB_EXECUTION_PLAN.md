# EPUB Execution Plan (Publishing-Grade)

This plan is the **forward-looking backlog** for taking the current EPUB pipeline and manuscript to a **publishable, high-production-value** release. It is written so a future LLM/editor can pick up work without re-discovering context.

## Current state (baseline)

- Production/regression checks: `bash notes_output/scripts/run_production_checks.sh` is currently **green**.
- EPUB outputs:
  - Apple: `epub_builder/dist/ece657_ebook_apple.epub`
  - Kindle: `epub_builder/dist/ece657_ebook_kindle.epub`
- Chapter separation: each `chap:*` label is now a separate spine XHTML item (enforced by `epub_builder/scripts/verify_epub_structure.py`).

## Work Package 1 — Navigation & packaging polish (P0)

1. **Verify chapter boundaries visually**
   - Open Apple + Kindle EPUBs; confirm each chapter begins at a clear boundary and is navigable via TOC.
   - Acceptance: chapters do not “flow” invisibly from previous chapter; TOC jump lands at chapter start.

2. **TOC hygiene**
   - Keep ToC limited to Parts + Chapters (no “Example:” / micro-headings).
   - Acceptance: TOC is short and high-signal; no junk headings.

3. **Cover + metadata audit**
   - Confirm cover shows as thumbnail in Finder/Books and inside EPUB.
   - Acceptance: cover thumbnail appears reliably; `book_metadata.json` passes.

## Work Package 2 — Typography, layout, and reader ergonomics (P0)

1. **Heading hierarchy**
   - Maintain consistent visual hierarchy (chapter/section headings larger than body text).
   - Acceptance: spot-check multiple chapters/sections in Apple Books and Kindle Previewer.

2. **Pagination oddities (blank/near-blank pages)**
   - Identify recurring causes: large tables/images, keep-together behaviors, large margins on headings.
   - Fix in CSS first; fix in LaTeX second (avoid per-instance hacks).
   - Acceptance: no obviously “empty” screens around headings/tables in common readers.

3. **Long math clipping**
   - Keep block math scrollable (current pipeline wraps MathML in `.math-block`).
   - Acceptance: no truncated block equations in Apple Books at common font sizes.

4. **TOC/title hygiene (EPUB)**
   - Avoid manual line breaks (`\\\\`) inside chapter titles; they render as `<br/>` in `EPUB/nav.xhtml` and make the TOC look less polished.
   - Acceptance: chapter titles are single-line in the TOC across Apple Books + Kindle Previewer.

## Work Package 3 — Tables (P0)

1. **Caption taxonomy**
   - Tables use `Table:` and figures use `Figure:` as the label prefix; avoid `Schematic:` by default and only use it when a reader could reasonably mistake the visual for an empirical result or a to-scale diagram.
   - Acceptance: table captions read like tables (not “schematics”).

2. **Wide/important tables**
   - Preserve the “Feature-based word vectorization” table (graded/fractional values are intentional).
   - Acceptance: it remains readable (horizontal scroll container OK), and audits remain green.

## Work Package 4 — Source-level editorial coherence (P1)

1. **Informal citations**
   - Eliminate “Breakthrough (1982)” style citations; use `\\citet{...}` / `\\citep{...}`.
   - Acceptance: `notes_output/scripts/check_citations.py` reports no informal citations.

2. **Running example thread**
   - Use one recurring toy task (e.g., two\hyp{}moons / two\hyp{}cluster boundary) **without announcing it as a “thread”**.
   - Technique:
     - In each chapter, introduce the task only insofar as it motivates the chapter’s method (local context, no meta commentary).
     - In later chapters, refer back briefly in a way that feels like a natural “oh, this tool changes what we can do”, not an explicit “continuity program”.
   - Acceptance: reader feels continuity implicitly; no “Continuity thread:” headings; no new crossref issues.

3. **Risk & audit boxes**
   - Add consistent 3–6 bullet “Risk & audit” boxes to selected chapters beyond the NLP/deployment chapter (per editorial direction).
   - Acceptance: consistent styling and tone; renders correctly in EPUB.

4. **Part II deep editorial pass (CNN/RNN coherence)**
   - Create a rearrangement plan for Chapters 11–12 that preserves all material but improves the learning arc (“basic → deeper → deepest”), then implement with crossref + equation + citation checks.
   - Acceptance: no new `check_crossrefs.py` / `check_equations.py` / `check_citations.py` violations; EPUB regression remains green; chapter reads linearly without “teleporting” prerequisites.

5. **Fragmentation reduction (long chapters)**
   - Review heading density in Chapters 16 (Fuzzy sets) and 19 (Evolutionary) and consolidate micro-headings where it improves flow without reducing rigor.
   - Acceptance: TOC remains high-signal; chapters remain skimmable; no template drift.

## Work Package 5 — Automation & regression hardening (P1)

1. **Expand structural gatekeeper checks**
   - Keep `epub_builder/scripts/verify_epub_structure.py` aligned with publishing requirements.
   - Acceptance: failures are actionable (file + symptom) and avoid false positives.

2. **Issue tracking discipline**
   - Every fix gets an entry in `notes_output/EDITORIAL_FEEDBACK.md` with “symptom → root cause → fix → regression”.
   - Acceptance: future changes remain reversible and testable.
