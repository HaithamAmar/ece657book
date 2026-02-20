# Part II Rollover Editorial Scan (Global Issues + Starting Chapter Packet)

- Date: 2026-02-20
- Scope: Part II as included in `notes_output/book_chapters.tex`, read as a rolling window (keeping `lecture_1_intro.tex` in mind as the global contract and the Part II bridge box in `book_chapters.tex` as the intended reading lens).
- Goal: identify cross-chapter issues that should be handled *globally* before/while editing individual chapters; then start Chapter 5 (`lecture_3_part_i.tex`) with concrete, author-editable insert drafts.
- Constraint: do not add or change numeric walkthrough values unless verified in Python and wired into the existing numeric/strict validation harness.

## A. Global Part II issues (apply across chapters)

### A1. Continuity contract (what Part II promises and how to pay it off)

Part II is already framed (in `book_chapters.tex`) as: same ERM loop, but the main failure modes become computation-graph issues (shapes/caching/gradient flow) and leakage/masking issues for sequences. The editorial opportunity is to ensure each chapter opening/closing does two things:

- Names what transfers from the previous chapter ("what you already know").
- Names what will transfer to the next chapter ("what you will reuse").

Action pattern to apply (chapter-by-chapter):
- Add/strengthen a 2--4 sentence "handoff paragraph" near the top (or a short `summarybox`) that explicitly says:
  - what stays the same (ERM contract),
  - what changes (architecture + its failure modes),
  - what to log/check (audit hooks).

### A2. Global pedagogy: ensure each chapter earns at least one "concrete trace"

Part II is strong on equations and figures, but the book's teaching goal is best served when each chapter also has at least one concrete, student-verifiable trace:

- A tiny numeric forward pass + loss + gradient trace (even with toy dimensions), OR
- A code-level shape ledger that is paired with a worked mini-example (not just shapes), OR
- A short "what to plot / what will break" diagnostic checklist that references a specific figure/example in the chapter.

Gap to track (do not fix blindly):
- Some chapters have strong narrative/figures but no small numeric trace. Adding such traces is valuable but must be verified and (ideally) added to the numeric harness.

### A3. Notation consistency: "row-major deep-learning convention" and symbol reuse

Multiple Part II chapters introduce shape conventions. This is useful, but it can become repetitive. Global editorial preference:

- Keep one strong "row-major convention" explanation early in Part II (Chapter 5 and/or Chapter 7) and then:
  - later chapters should reference it briefly rather than re-deriving it.

Related:
- Prefer consistent naming for tensors/vectors across Part II (e.g., bold for vectors/matrices; consistent use of \(Z\)/\(A\) or \(z\)/\(a\) for pre-activations/activations).

### A4. TOC fragmentation (micro-subsections)

Part II has a small set of subsections/subsubsections that are currently too short to stand alone. Editorial policy choice:

- If the heading is something a reader will search for ("Fine-tuning", "Alignment", "Word2Vec objectives"), prefer *ENRICH* (keep as `\subsection` and expand).
- If the heading is only a bridge sentence (pure signposting), prefer *DEMOTE* to `\paragraph` (keep the label if referenced) to reduce TOC noise.

Current micro-section candidates (Part II scan; re-check after edits):
- `lecture_3_part_i.tex`: "Outline of Neural Network Study"
- `lecture_6.tex`: "Pooling as nonparametric downsampling"
- `lecture_8_part_i.tex`: "Word2Vec objectives in detail"
- `lecture_5_part_i.tex`: "Winner-Takes-All Learning Recap" (borderline; could be enriched or demoted depending on desired TOC granularity)

### A5. Caption/prose templating fatigue ("Use it when ...")

Many Part II figure captions end with "Use it when ...". This is pedagogically useful, but overuse reads templated.

Global guideline:
- Keep "Use it when ..." as a tool, but vary it occasionally ("Use this figure to ...", "Read this as ...", "This helps when ...") to reduce repetition without losing the instruction.

### A6. Cross-chapter "audit hooks" vocabulary

Part II benefits from a consistent, repeated set of audit hook phrases:
- shapes and caches, masking/leakage, calibration, slices, learning curves, ablations.

Action:
- When editing each chapter, ensure the final "Common pitfalls" and "Minimum viable mastery" mention at least one audit hook that matches that chapter's core risk.

## B. Start-of-Part-II: Chapter 5 (`lecture_3_part_i.tex`) packet

### B1. Likely reader friction points

1) The biology preface is fine, but it runs long before the "computational contract" becomes explicit (weighted sums, thresholds, loss, updates). Consider a short bridge sentence that reframes biology as abstraction *and* points to the engineering loop.
2) "Outline of Neural Network Study" is short and slightly redundant with the opening paragraph. This is a good place to either:
   - (ENRICH) turn it into a clear Part II mini-roadmap, OR
   - (DEMOTE) turn it into a paragraph to reduce TOC fragmentation.
3) The chapter already has strong worked geometry and Adaline update material; the main editorial job is to tighten continuity and reduce "chapter as lecture transcript" feel (where applicable).

### B2. Draft insert (author-editable): Part II local roadmap box (preferred ENRICH)

Insertion point:
- In `lecture_3_part_i.tex`, replace/transform the existing `\subsection{Outline of Neural Network Study}` block.

Draft (for author edit):

```
\begin{tcolorbox}[summarybox, title={How this chapter fits into Part II}]
This chapter starts Part II by introducing the smallest trainable building blocks: a single neuron, a hard-threshold perceptron, and the first update rules (mistake-driven and gradient-driven). The point is not biology; the point is a computation you can write down, debug, and improve.

Three payoffs to keep in view as you read Part II:
\begin{itemize}
  \item \textbf{From units to systems:} \Cref{chap:mlp} chains these units into multilayer networks; \Cref{chap:backprop} shows how to compute all gradients efficiently (the training engine).
  \item \textbf{From boundaries to representations:} later architectures (CNNs, recurrence, attention) change what patterns are easy to represent and what information can flow.
  \item \textbf{From loss to decisions:} keep the ERM contract: define the objective, optimize, then audit (learning curves, calibration, and slice checks).
\end{itemize}
\end{tcolorbox}
```

### B3. Alternative (if you prefer DEMOTE): paragraph handoff only

```
\paragraph{Where this fits in Part II.}
This chapter starts the neural strand with perceptrons and activation functions. \Cref{chap:mlp} then develops multilayer perceptrons and the backpropagation machinery needed to train them; \Cref{chap:rnn} returns to sequence models with recurrent connections. Keep the Part II reading lens in mind: the ERM loop stays the same, but the main failure modes shift to shapes/caching and (later) masking/leakage.
```

