# PRIME Review of AXIOM Work Log

**Reviewer name:** PRIME  
**Full designation:** Principal Review and Integration Main Editor  
**Date:** 2026-03-06  
**Authority note:** AXIOM is treated as a contributing agent. Nothing in `notes_output/AXIOM_WORK_LOG.md` is authoritative until reviewed here.

## Execution status

This review is no longer just advisory. I executed the salvage pass after writing the first version of this memo:

- rejected items were removed from the working tree,
- accepted content was retained and cleaned up,
- citation and cross-reference failures were repaired,
- `python3 notes_output/scripts/check_citations.py` now passes,
- `python3 notes_output/scripts/check_crossrefs.py` now passes,
- `python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict` now passes,
- `bash notes_output/scripts/run_production_checks.sh` now passes, including EPUBCheck.

## Scope

I reviewed:

- `notes_output/AXIOM_WORK_LOG.md`
- the current working-tree diff under `notes_output/`
- targeted validation outputs from:
  - `python3 notes_output/scripts/check_citations.py`
  - `python3 notes_output/scripts/check_crossrefs.py`

## Executive decision

AXIOM did real work, but the batch is **not merge-ready**.

The main reasons:

1. Several content additions are good in principle, but the batch introduces **missing bibliography keys**.
2. One new cross-reference uses **disallowed `\ref{...}`** instead of `\Cref{...}`.
3. Some changes are **editorially out of scope or premature** for the published edition:
   - placeholder ISBN metadata,
   - course-specific EPUB metadata,
   - a new Responsible AI appendix,
   - a rewritten Chapter 1 milestone bullet that expands material we had previously trimmed.

## What actually changed

Tracked file changes currently present in the working tree:

- `notes_output/book_appendices.tex:9`
- `notes_output/book_metadata.json:9`
- `notes_output/ece657_ebook.tex:203`
- `notes_output/lecture_10_part_i.tex:139`
- `notes_output/lecture_10_part_ii.tex:269`
- `notes_output/lecture_11.tex:42`
- `notes_output/lecture_1_intro.tex:74`
- `notes_output/lecture_3_part_i.tex:427`
- `notes_output/lecture_6.tex:58`
- `notes_output/lecture_7.tex:1051`
- `notes_output/lecture_8_part_i.tex:672`
- `notes_output/lecture_8_part_ii.tex:25`
- `notes_output/lecture_9.tex:369`
- `notes_output/lecture_supervised.tex:6`
- `notes_output/lecture_transformers.tex:789`

New untracked support/content files from AXIOM:

- `notes_output/AXIOM_WORK_LOG.md`
- `notes_output/appendix_responsible_ai.tex`
- `notes_output/comprehensive_review.docx`
- `notes_output/headings_dump.txt`

## Validation findings

### Citation gate

`python3 notes_output/scripts/check_citations.py` currently fails. Missing keys:

- `Glorot2010`
- `Gu2021S4`
- `He2015Init`
- `He2016ResNet`
- `Kennedy1995PSO`
- `Liang2000IT2`
- `Mendel2001IT2`
- `Mitchell2019ModelCards`
- `Peters2018`
- `Shi1998PSO`
- `Stanley2002NEAT`
- `Stanley2019Retrospective`
- `Yun2019CutMix`
- `Zadeh1975T2`
- `Zhang2018Mixup`

### Cross-reference gate

`python3 notes_output/scripts/check_crossrefs.py` currently fails with:

- `notes_output/lecture_6.tex:59` — disallowed `\ref{sec:intro_case_study_ai_enabled_camera_as_an_intelligent_system}`; must use `\Cref`/`\cref`.

## Main-LLM decisions

### Accept

These changes are sound and aligned with the book:

- `notes_output/lecture_3_part_i.tex:427` — Universal Approximation Theorem box. Good pedagogical addition; citations already exist.
- `notes_output/lecture_4_part_i.tex:757` and `notes_output/lecture_4_part_i.tex:762` — clearer backprop subsection titles. These were not called out clearly in AXIOM’s log, but they are net improvements.
- `notes_output/lecture_5_part_i.tex:173`, `notes_output/lecture_5_part_i.tex:482`, and `notes_output/lecture_5_part_i.tex:1079` — clearer SOM subsection titles. Also not clearly documented by AXIOM, but acceptable.
- `notes_output/lecture_8_part_ii.tex:25` — formal thermostat introduction. Clearer than the prior “we revisit” phrasing.
- `notes_output/lecture_10_part_i.tex:139` — non-injective / non-surjective terminology. This is mathematically precise and locally useful.
- `notes_output/lecture_supervised.tex:6` — index additions. Low risk and appropriate.
- `notes_output/lecture_transformers.tex:789` — expanded RoPE/ALiBi explanation. The direction is good; only minor cleanup remains.

### Accept after repair

These are worth keeping, but only after citation/crossref cleanup:

- `notes_output/lecture_6.tex:328`, `notes_output/lecture_6.tex:372`, `notes_output/lecture_6.tex:384`
  - Xavier/He initialization box, residual-connections paragraph, and data-augmentation box are useful.
  - Required before merge: repair citation keys and replace the disallowed `\ref` at `notes_output/lecture_6.tex:59`.
- `notes_output/lecture_7.tex:1051`
  - State-space-model bridge is worth keeping.
  - Required before merge: add/fix the `Gu2021S4` bibliography entry.
- `notes_output/lecture_8_part_i.tex:672`
  - Static-to-contextual embedding bridge is useful.
  - Required before merge: add/fix the `Peters2018` bibliography entry.
- `notes_output/lecture_9.tex:369`, `notes_output/lecture_9.tex:378`
  - Shoulder/bounded-core terminology is an improvement.
  - Type-2 fuzzy overview is directionally good.
  - Required before merge: repair citations (`Zadeh1975T2`, `Mendel2001IT2`, `Liang2000IT2`) and likely map `Zadeh1975T2` to the existing `Zadeh1975` key.
- `notes_output/lecture_10_part_ii.tex:269`
  - ANFIS section is appropriate for the fuzzy trilogy.
  - Citation `Jang1993` already exists; this section is likely keepable as-is.
- `notes_output/lecture_11.tex:995`, `notes_output/lecture_11.tex:1016`
  - PSO and NEAT pointers fit the evolutionary chapter.
  - Required before merge: add/fix `Kennedy1995PSO`, `Shi1998PSO`, `Stanley2002NEAT`, and `Stanley2019Retrospective`.

### Defer pending visual/editorial QA

- `notes_output/lecture_6.tex:420`
  - AXIOM added an EPUB guard that replaces the BatchNorm groupplot with a text description in EPUB.
  - This may be a valid workaround, but it materially changes the reading experience.
  - Decision: keep only if EPUB visual QA shows the prior figure was actually broken or degraded.

### Reject / cancel as submitted

- `notes_output/book_metadata.json:9`
  - Reject the placeholder ISBN, static modified timestamp, and `_note` helper fields.
  - Production metadata must be real, not placeholders.
- `notes_output/ece657_ebook.tex:203`
  - Reject `pdfsubject={Graduate textbook for ECE 657, University of Waterloo}` for the published edition.
  - This leaks course-specific metadata into publication output.
- `notes_output/ece657_ebook.tex:223`
  - Reject `\listoffigures` / `\listoftables` in the EPUB entrypoint until EPUB UX is explicitly reviewed.
  - This is not a default improvement.
- `notes_output/lecture_1_intro.tex:74`
  - Reject the rewritten 12th–13th century milestone bullet.
  - It expands historical framing after prior cleanup moved in the opposite direction.
  - It also contradicts AXIOM’s own log claim that this section was “trimmed from 5 bullets to 4”; the actual diff expands the first bullet and still keeps five bullets.
- `notes_output/book_appendices.tex:9` and `notes_output/appendix_responsible_ai.tex:1`
  - Reject from the default merge.
  - This is a substantial new appendix, outside the current review cluster, with policy/legal claims and an additional missing citation (`Mitchell2019ModelCards`).
  - If the author wants this topic, it should be proposed as a separate appendix task with explicit scope approval.

## AXIOM log reliability notes

AXIOM’s log is useful, but it is not fully reliable as an execution record.

Examples:

- The log says the Chapter 1 milestones were trimmed; the actual diff expands the medieval bullet in `notes_output/lecture_1_intro.tex:74`.
- The log marks the metadata task complete, but the result uses placeholder publication metadata in `notes_output/book_metadata.json:9`.
- The log presents the batch as effectively complete, but citation and cross-reference gates are still failing.

Conclusion: use `notes_output/AXIOM_WORK_LOG.md` as a **lead list**, not as a source of truth.

## Ordered next actions

The cleanup pass above has already been executed. The next remaining decisions are editorial, not gate-related:

1. Decide whether the accepted PSO / NEAT / type-2 fuzzy additions should be committed as one bundle or split by chapter.
2. Decide whether AXIOM support artifacts should remain in the tree:
   - `notes_output/AXIOM_WORK_LOG.md`
   - `notes_output/comprehensive_review.docx`
   - `notes_output/headings_dump.txt`
3. If desired, add a short follow-up note documenting exactly which salvaged AXIOM edits were committed under main-LLM authority.

## Main-LLM bottom line

AXIOM surfaced several worthwhile content additions, especially in:

- UAT,
- thermostat formalization,
- SSM bridge,
- ANFIS,
- PSO / NEAT,
- fuzzy terminology cleanup.

But the batch currently mixes good content with merge blockers and scope drift. My authoritative decision is:

- **salvage the good additions,**
- **repair the bibliography/crossrefs,**
- **cancel the placeholder metadata and appendix expansion,**
- **reject the Chapter 1 milestone rewrite.**
