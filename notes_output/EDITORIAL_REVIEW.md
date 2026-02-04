## Editorial review: flow, structure, and proposed changes (no source files modified)

**Status:** archived. This document predates the current Part structure and Chapter 13/14 ordering (NLP now precedes Transformers). Keep it only for historical context; do not execute the renumbering plan below. For the current order, see `notes_output/book_chapters.tex` and `notes_output/PART_II_EDITORIAL_REVIEW.md`.

This review evaluates the document’s narrative flow and coherence across lectures/chapters and proposes a concrete, minimal set of edits to improve organization and consistency. All recommendations are actionable but are collected here without changing any originals, per request.

### Important constraints (as provided)
- Filenames do not determine order; each top-level `\section{...}` is a chapter.
- Chapter numbering is by include order in `notes_output/book_chapters.tex`; avoid hardcoding chapter numbers in prose.
- Recommendations below therefore treat per-section numbering as authoritative and prefer `\Cref{chap:...}` over literal “Chapter 13/14”.

### Executive summary
- The content breadth is strong and well‑developed, with consistent pedagogy (Learning Outcomes, summary boxes, rich figures).
- **Correction**: Previous reports of a "duplicate MLP chapter" in `lecture_8_part_i.tex` were incorrect. That file contains the **Word Embeddings** chapter ("Neural Network Applications in NLP"), which is distinct and valuable.
- **Flow Issues (historical, since resolved):**
  - Chapter numbering in comments and drafts drifted from the include order during early part/TOC experiments.
  - Some early drafts left an apparent “gap” between the neural strand and the soft-computing strand.
- **Recommended actions (historical):** the renumbering plan below is preserved for traceability only and should not be executed on the current manuscript.

---

### Proposed Chapter Sequence (1–18)

This sequence respects the "Transformers = 13" constraint and ensures logical flow:

1.  Supervised Learning (`lecture_1.tex`)
2.  Symbolic Integration (`lecture_2_part_i.tex`)
3.  Classification (`lecture_2_part_ii.tex`)
4.  Intro Neural Networks (`lecture_3_part_i.tex`)
5.  MLP Foundations (`lecture_3_part_ii.tex`)
6.  Backpropagation (`lecture_4_part_i.tex`)
7.  RBFNs (`lecture_4_part_ii.tex`)
8.  **SOMs** (`lecture_5_part_i.tex`) — *Shift from 9 to 8*
9.  **Hopfield Networks** (`lecture_5_part_ii.tex`) — *Shift from 10 to 9*
10. **Deep Learning/CNNs** (`lecture_6.tex`) — *Shift from 11 to 10*
11. **RNNs** (`lecture_7.tex`) — *Shift from 12 to 11*
12. **Word Embeddings** (`lecture_8_part_i.tex`) — *Shift from 14 to 12*
13. **Transformers** (`lecture_transformers.tex`) — *Fixed as 13*
14. **Soft Computing Intro** (`lecture_8_part_ii.tex`) — *Shift from 15 to 14*
15. **Fuzzy Sets** (`lecture_9.tex`) — *Shift from 16 to 15*
16. **Fuzzy Transformations** (`lecture_10_part_i.tex`) — *Shift from 17 to 16*
17. **Fuzzy Inference** (`lecture_10_part_ii.tex`) — *Shift from 18 to 17*
18. **Evolutionary Computing** (`lecture_11.tex`) — *Assign as 18*

---

### File-by-File Action Plan

The following table lists specific lines in specific files that should be changed to implement this reordering and fix compilation issues.

#### 1. Main File (`ece657_notes.tex`)
**Issue**: `hyperref` is loaded too early (line 6), causing `\BKM@entry` errors with the `bookmark` package.
**Action**: Move package loading to the end of the preamble.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 6 | `\usepackage{hyperref}` | *Remove line* |
| 36 | `\usepackage{bookmark}` | *Remove line* |
| 95 | *(Empty line before `\begin{document}`)* | `\usepackage{hyperref}`<br>`\usepackage{bookmark}` |

#### 2. SOMs (`lecture_5_part_i.tex`)
**Issue**: Incorrect chapter number comment.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `% Chapter 9` | `% Chapter 8` |

#### 3. Hopfield Networks (`lecture_5_part_ii.tex`)
**Issue**: Incorrect chapter number comment.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `% Chapter 10` | `% Chapter 9` |

#### 4. Deep Learning (`lecture_6.tex`)
**Issue**: Incorrect chapter number comment.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `% Chapter 11` | `% Chapter 10` |

#### 5. RNNs (`lecture_7.tex`)
**Issue**: Incorrect chapter number comment.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `% Chapter 12` | `% Chapter 11` |

#### 6. Word Embeddings (`lecture_8_part_i.tex`)
**Issue**: Incorrect chapter number comment (currently 14). Needs to be 12 to precede Transformers.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `% Chapter 14` | `% Chapter 12` |

#### 7. Transformers (`lecture_transformers.tex`)
**Issue**: Missing chapter number comment.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `\section{Transformers...}` | `% Chapter 13`<br>`\section{Transformers...}` |

#### 8. Soft Computing Intro (`lecture_8_part_ii.tex`)
**Issue**: Incorrect chapter number comment (currently 15). Needs to be 14 to follow Transformers.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `% Chapter 15` | `% Chapter 14` |

#### 9. Fuzzy Sets (`lecture_9.tex`)
**Issue**: Incorrect chapter number comment.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `% Chapter 16` | `% Chapter 15` |

#### 10. Fuzzy Transformations (`lecture_10_part_i.tex`)
**Issue**: Incorrect chapter number comment.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `% Chapter 17` | `% Chapter 16` |

#### 11. Fuzzy Inference (`lecture_10_part_ii.tex`)
**Issue**: Incorrect chapter number comment.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `% Chapter 18` | `% Chapter 17` |

#### 12. Evolutionary Computing (`lecture_11.tex`)
**Issue**: Missing chapter number comment.

| Line(s) | Current Content | Proposed Change |
| :--- | :--- | :--- |
| 1 | `\section{Introduction...}` | `% Chapter 18`<br>`\section{Introduction...}` |

---

### Additional Recommendations

1.  **Standardize Scaffolding**: Ensure every lecture file starts with a `Learning Outcomes` box and ends with a `Key Takeaways` box. `lecture_6.tex` and `lecture_11.tex` are good examples; others may need these added.
2.  **Cross-References**: If any text explicitly says "see Chapter 14" (referring to Embeddings), it should be updated to "see Chapter 12" or, better yet, use `\cref{...}` if labels are available.
3.  **Graphics Paths**: The `\graphicspath` commands in each file are good practice and should be kept.

### Closing note
These adjustments retain all existing content while removing friction in the reader’s path: foundations → (consolidated) MLP/backprop → CNNs/RNNs → embeddings → Transformers → SOM/Hopfield → soft computing/fuzzy → evolutionary. The main changes are editorial (reordering and header normalization) and should be low‑risk to implement incrementally.
