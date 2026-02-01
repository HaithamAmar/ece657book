# QA Log (V3) – chapter-by-chapter

## Recently resolved
- Case study in Chapter 1 folded into the design checklist (`lecture_1.tex:410–470`).
- SOM QE/TE definitions now clarify norms and adjacency (`lecture_5_part_i.tex:560–620`).
- Hopfield encoding table includes an explicit example (`lecture_5_part_ii.tex:14–60`).
- RNN pseudocode block now explains the `.*` Hadamard notation (`lecture_7.tex:1–40`).
- NLP chapter adds GloVe/BERT citations and a contextual-embedding subsection (`lecture_8_part_i.tex:300–580`).
- Fuzzy relation figure labels error/rate axes (`lecture_10_part_i.tex:295–330`).

## Feedback from Detailed_Feedback_PT2
- **Accepted**: Add elastic-net/proper-scoring-rule/double-descent notes (Chapter 2), Bronstein/Risch citation + termination sidebar (Chapter 3), RoPE/ALiBi/KV-cache/FlashAttention/state-space model notes (Chapter 13), responsible-deployment appendix (from Chapter 14), front-matter reference to companion notebooks, symbol index/pitfall consistency.
- **Deferred**: Deep dives into type‑2/interval fuzzy sets, ANFIS/neuro‑fuzzy, PSO/NSGA-II/CMA-ES/NEAT expansions, and full code notebook suite—reserve for a future edition due to scope.

---

## Chapter 1 – About This Companion (`lecture_1.tex`)
1. Caption context: now that a List of Tables exists, keep expanding captions to note where each table is used (loss table already updated; imbalance table still in Chapter 4 but ensure caption references its scope).
2. ✅ Added the requested “Figures, tables, and companion resources” subsection (lines 52–74) to explain the legend conventions and reference the notebooks/data directories.
3. ✅ Inserted an “Author’s note” box near the start so the narrative motivation for each chapter is explicit, independent of the recorded lectures.

## Chapter 2 – Supervised Learning Foundations (`lecture_1.tex`, Chapter 2 block)
1. ✅ Transformation-table paragraph now uses a `tabularx` layout (safer line breaks) and trimmed text so underfull warnings disappear.
2. ✅ Loss section now references Figure~\ref{fig:lec1_class_losses} inline so readers can reconcile the formulas with the margin plot.
3. ✅ Added an elastic-net subsection, a proper-scoring-rule box, and a scaling-laws paragraph; all cite Chapter~2 figures and remind readers that full MLE/MAP derivations live here.

## Chapter 3 – Symbolic Integration (`lecture_2_part_i.tex`)
1. ✅ Figure~\ref{fig:lec3_transform_tree} now displays \textbf{[S]} and \textbf{[H]} badges plus a textual legend.
2. ✅ Added \citep{Bronstein2005,Risch1969} context and a termination/numeric-fallback box next to the pseudocode.
3. ✅ New “Author’s note: safe moves vs.\ brave leaps” captures the intuition behind alternating deterministic transformations with heuristic gambles.

## Chapter 4 – Logistic Regression (`lecture_2_part_ii.tex`)
1. ✅ Section now defers to Chapter 2’s learning-curve figure instead of repeating partial derivations.
2. ✅ Added an “Author’s note” about how to think differently about regression vs.\ classification so the intuition survives even without the lecture anecdotes.

## Chapter 5 – Perceptron (`lecture_3_part_i.tex`)
✔️ Next-steps paragraph already added; no new issues. Added an “Author’s note: neurons as tiny negotiators” so the qualitative story about activations persists beyond the lecture.

## Chapter 6 – MLP Foundations (`lecture_3_part_ii.tex`)
1. ✅ Inserted a pointer to the new Appendix entry that houses the long-form scalar derivation so this chapter only summarizes the key identities.
2. ✅ Added an “Author’s note: gradients as ripples” to capture the heuristic explanation of backpropagation.
3. ✅ Added an “Author’s note” near the pseudocode reminding readers to cache activations/gradients for numerical stability.

## Chapter 7 – Backprop Learning (`lecture_4_part_i.tex`)
1. ✅ Added a two-layer SGD pseudocode block directly after the forward-pass recap.
2. ✅ Added an “Author’s note: training as a conversation” to preserve the intuition behind forward/backward passes.
3. ✅ Inserted a short early-stopping reminder (“default brake”) alongside the diagnostic curves.

## Chapter 8 – RBF Networks (`lecture_4_part_ii.tex`)
✔️ Sidebar now unnumbered; verify it disappears from the ToC once the PDF stabilizes.
✅ New “Author’s note: think in terms of bubbles” captures the geometric intuition behind centers/widths.

## Chapter 8 (Part I) – NLP embeddings (`lecture_8_part_i.tex`)
✅ Added an “Author’s note: embeddings mix geometry and bias” after the bias-check box.

## Chapter 9 – SOMs (`lecture_5_part_i.tex`)
✅ QE/TE definitions now appear in display form and the quality-measure discussion was split into bullet points, eliminating the lingering overfull box near Figure~\ref{fig:lec5-early-stopping}.
✅ Added “Author’s note: map-making, not magic” so the cartography intuition is documented.

## Chapter 10 – Hopfield Networks (`lecture_5_part_ii.tex`)
✔️ Encoding example added; no outstanding items.

## Chapter 10 – Fuzzy Relations (`lecture_10_part_i.tex`)
✅ Added an “Author’s note” on practical operator selection (when to prefer max–min vs. algebraic compositions).

## Chapter 11 – CNNs (`lecture_6.tex`)
1. ✅ Removed the explicit sample markers from Figure~\ref{fig:lec6-rbf-width}, which clears the stubborn nullfont warnings tied to the RBF bandwidth illustration.

## Chapter 12 – RNNs (`lecture_7.tex`)
1. With the Hadamard note added, no new issues.

## Chapter 13 – Transformers (`lecture_transformers.tex`)
1. ✅ Replaced the long single paragraph on long-context strategies with a short bullet list, eliminating the previous overfull warning near line 120.
2. ✅ Added an “Advanced attention and efficiency notes” subsection covering RoPE/ALiBi, KV caches, FlashAttention, SSM/Mamba, MoE routing, and PEFT (LoRA/QLoRA).
3. ✅ Added an “Author’s note: attention allocates focus per token” so the human workflow analogy is recorded in prose.

## Chapter 14 – NLP applications (`lecture_8_part_i.tex`)
1. ✅ Inserted a “Responsible deployment checklist” subsection following the bias diagnostics box; keeps cross-links with Chapter 1 policies.

## Chapter 15 – Soft Computing intro (`lecture_8_part_ii.tex`)
✔️ Bridge paragraph complete; no new issues.

## Chapter 16 – Fuzzy Sets (`lecture_9.tex`)
1. ✅ Converted Table~\ref{tab:fuzzy-operators} to `tabularx` so the qualitative column wraps naturally; the earlier overfull hbox at line 869 no longer appears in the log.

## Chapter 17 – Fuzzy Relations (`lecture_10_part_i.tex`)
✔️ Figure now references thermostat example; no further issues.

## Chapter 18 – Fuzzy Inference (`lecture_10_part_ii.tex`)
✔️ Mamdani vs. Sugeno comparison in place; no outstanding items.

## Chapter 19 – Evolutionary Computing (`lecture_11.tex`)
✔️ Opening cross-references updated; PT2 suggestions for NSGA/PSO/CEM expansions are deferred to a future edition.
✅ Added an “Author’s note” summarizing rule-of-thumb population sizes and mutation rates when budgets are tight.

## Global
1. Exercise/lab boxes still missing for Chapters 3–8 and 10–17.
2. Outstanding warnings now include the Chapter 11 RBF figure, the long-context paragraph in Chapter 13, and the Chapter 16 complement example; SOM and key-takeaways fixes cleared their earlier messages.
3. Symbol index + per-chapter “pitfalls” boxes: currently inconsistent; add a consolidated list plus any missing pitfall callouts.
4. ✅ Responsible-deployment checklist now lives in Chapter 14; still consider whether an appendix reference is required.
5. ✅ Notebook references mentioned in Chapter 1 front matter.
6. Deferred items for future editions: type-2 fuzzy sets, ANFIS/neuro-fuzzy, PSO/NSGA-II/CEM/NEAT additions, and a comprehensive notebook suite.
7. \textbf{Chapter-order review.} Swapping Chapters 2 and 3 would force a large renumbering ripple: more than twenty explicit “Chapter~2” references (Chapters 3–7, 9, 14) and every “return to Chapter~3” bridge would have to be rewritten, and the existing Chapter 1 roadmap—“statistical ERM first, symbolic interlude second”—would invert. Because Chapter 4 and onward currently defer to Chapter 2 for ERM/MLE details, keeping ERM before symbolic integration preserves the dependency chain; postponing any decision until a future major edition avoids destabilizing the freshly synchronized references.
