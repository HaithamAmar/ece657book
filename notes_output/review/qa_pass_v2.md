# QA Log (V2)

## Previously flagged items now resolved
- **Chapter 1 cross-reference drift** (logistic pointer) now references Chapters 2 & 4 correctly (`lecture_1.tex:919`).
- **Chapter 1 design duplication** reduced to a single checklist summarizing problem/representation/constraints (`lecture_1.tex:360–400`).
- **Chapter 3 intro bridge** rewrites the “previous chapter” paragraph to cite Chapter 2 and frame the symbolic case study.
- **Transformation-tree figure legend** now explicitly labels safe (blue) vs heuristic (orange) branches in caption (`lecture_2_part_i.tex:241–264`).
- **Chapter 4 → 5 transition** now includes a “Looking ahead” paragraph (`lecture_2_part_ii.tex:392`) and the regression recap has been collapsed to a single paragraph (`lecture_2_part_ii.tex:24–40`).
- **Legacy chapter markers** in Chapters 15–19 have been updated to the correct numbers.
- **Chapter 6 dimension reminder** clarifies how the matrix equations subsume the scalar example (`lecture_3_part_ii.tex:360–376`).
- **Backprop flow figure** is explicitly referenced in text (`lecture_4_part_i.tex:523–540`).
- **RNN pseudocode** now inserted (`lecture_7.tex:12–35`), and QE/TE definitions precede the SOM validation plot (`lecture_5_part_i.tex:560–620`).
- **Soft-computing running example** and thermostat bridge are in place (`lecture_8_part_ii.tex:12–25`).
- **Hopfield encoding correspondence**, Wiener optional note, fuzzy projection matrix, and Chapter 19 cross-references have been added (`lecture_5_part_ii.tex:1–60`, `lecture_4_part_ii.tex:298`, `lecture_10_part_i.tex:295–330`, `lecture_11.tex:12–30`).
- **Redundant De Morgan discussion** reduced to a reminder paragraph (`lecture_9.tex:300–320`), and a List of Tables now appears in the main document (`ece657_notes.tex:60`).

The remaining issues below are the ones still outstanding after the new editorial pass.

## Chapters 1–3 (lecture_1.tex, lecture_2_part_i.tex)

1. **Section overlap still inflates Chapter 1**  
   - **Location:** `lecture_1.tex:360–520`.  
   - **Issue:** Sections 1.9–1.11 repeat full “problem definition → representation → components” narratives twice (road vehicle example, camera case, then “Intelligent System Features”). The request in General_Overview_V2 to consolidate overlapping definitions (AI, intelligent systems, intelligent machines) remains unresolved.  
   - **Impact:** Chapter 1 is longer than necessary, obscuring the new taxonomy and making it harder to find the formal definition.  
   - **Fix:** Merge the duplicated paragraphs into a single “Working vocabulary” section and cross-reference the new Section 1.9 as originally planned.

2. **Transformation-tree figure lacks textual legend reference**  
   - **Location:** `lecture_2_part_i.tex:241–264`.  
   - **Issue:** The safe/heuristic legend in Figure \ref{fig:lec3_transform_tree} is implemented via nodes rather than a semantic legend entry, so screen readers and the List of Figures do not announce the meaning of the blue/dashed boxes.  
   - **Fix:** Convert the legend into a `\matrix` with `\legend` keys or add an explicit caption sentence (“Blue nodes = safe transformations; dashed = heuristic/backtracking”) so readers without color cues can follow the diagram.

3. **Part B recap still references Chapter numbering ambiguously**  
   - **Location:** `lecture_2_part_i.tex:332–352`.  
   - **Issue:** The text says “Full derivations live in Chapter 2 (supervised learning foundations) and Chapter 4 (logistic regression)” but does not cite section numbers. Readers jumping from Chapter 3 still have to hunt for the right subsections.  
   - **Fix:** Replace with explicit pointers (“see Chapter 2, Sec. 2.3 for ERM and Chapter 4, Sec. 4.2 for logistic MLE”) or hyperlink the exact sections.

## Chapters 4–6 (lecture_2_part_ii.tex, lecture_3_part_i.tex, lecture_3_part_ii.tex)

1. **Linear-regression recap reinstated in Chapter 4**  
   - **Location:** `lecture_2_part_ii.tex:24–120`.  
   - **Issue:** The chapter still walks through the full SSE derivation, correlation diagnostics, and learning-curve discussion before introducing logistic regression—the exact duplication General_Overview_V2 warned against.  
   - **Fix:** Compress this block to a short paragraph referencing Chapter 2 and jump directly to logistic-specific content.

2. **Scalar vs. vector derivations remain duplicated**  
   - **Location:** `lecture_3_part_ii.tex:202–320`.  
   - **Issue:** Chapter 6 still alternates between scalar chain-rule examples and the matrix form, leaving students to reconcile two notational systems. The requested single matrix-calculus derivation plus a boxed single-neuron example has not been produced.  
   - **Fix:** Collapse the repeated gradients into one matrix derivation (with clear dimensions) and move the scalar walk-through to a brief worked example or appendix.

3. **Chapter 6 lacks a reference to the new pseudocode figure**  
   - **Location:** `lecture_4_part_i.tex:503–535`.  
   - **Issue:** The new backprop flow diagram is inserted, but the surrounding prose does not call it out (“see Figure…”). Readers scanning the text can miss the intended geometry reference.  
   - **Fix:** Add a sentence before the figure explicitly pointing to it and summarizing the takeaway (forward caches vs backward deltas).

## Chapters 7–9 (lecture_4_part_i.tex, lecture_4_part_ii.tex, lecture_5_part_i.tex)

1. **Chapter 7 still lacks code-level guidance**  
   - **Location:** `lecture_4_part_i.tex` (entire chapter).  
   - **Issue:** Despite the new conceptual figure, there is no pseudocode block for the 2-layer example, contrary to the V2 request for “short, consistent pseudocode boxes.”  
   - **Fix:** Add a 10–12 line code block (forward/backward for a tiny network) similar to the style adopted in Chapter 6.

2. **Wiener filter sidebar not marked optional in text**  
   - **Location:** `lecture_4_part_ii.tex:300–372`.  
   - **Issue:** The caption mentions the Wiener recap is “optional,” but the main body never signals that readers can skip it, so it still interrupts the RBF narrative.  
   - **Fix:** Add an explicit inline pointer (“Optional sidebar—skip if you only need the RBF training recipe”) or move to Appendix A as originally suggested.

3. **SOM chapter lacks inline legend for QE/TE plots**  
   - **Location:** `lecture_5_part_i.tex:600–640`.  
   - **Issue:** Figure captions discuss quantization error (QE) and topographic error (TE), but the text never defines the acronyms before the figure.  
   - **Fix:** Introduce QE/TE definitions in prose (with equations) before referencing the plot.

## Chapters 10–12 (lecture_5_part_ii.tex, lecture_6.tex, lecture_7.tex)

1. **Hopfield chapter still references both \(\{-1,+1\}\) and \(\{0,1\}\) encodings without tying them together**  
   - **Location:** `lecture_5_part_ii.tex:40–180`.  
   - **Issue:** Energy definitions oscillate between the two encodings with only brief notes; readers must manually convert bias terms. This was flagged in the previous QA and persists.  
   - **Fix:** Add a dedicated subsection or table summarizing both encodings and how to translate weights/biases.

2. **CNN/MLP chapter retains nullfont warnings**  
   - **Location:** `lecture_6.tex:520–531`.  
   - **Issue:** The tikz axis labels still contain literal “0.1pt” annotations that render as missing characters (see tectonic warnings).  
   - **Fix:** Replace “0.1pt” text in node labels with math-mode text or remove the units.

3. **RNN chapter lacks pseudocode / training recipe**  
   - **Location:** `lecture_7.tex` (entire file).  
   - **Issue:** There is no compact pseudocode box for the vanilla RNN cell or BPTT despite the V2 request. The chapter remains purely descriptive.  
   - **Fix:** Add a small pseudocode snippet (forward, hidden-state update, BPTT loop) and explicitly mention gradient clipping/normalization.

## Chapters 13–15 (lecture_transformers.tex, lecture_8_part_i.tex, lecture_8_part_ii.tex)

1. **Transformer figure causes overfull warning**  
   - **Location:** `lecture_transformers.tex:60–84`.  
   - **Issue:** Even after resizing, the figure still pushes an overfull hbox (tectonic warning at line 121).  
   - **Fix:** Reduce the figure width further or break the caption across two lines to avoid the 11 pt overflow.

2. **NLP chapter cites only word2vec for embeddings**  
   - **Location:** `lecture_8_part_i.tex:150–380`.  
   - **Issue:** GloVe/fastText or contextual embedding references are absent, even though the prose compares these methods implicitly.  
   - **Fix:** Add citations (Pennington et al., Bojanowski et al., BERT) where the text discusses these techniques.

3. **Soft-computing chapter still lacks a closing bridge to Chapters 16–18**  
   - **Location:** `lecture_8_part_ii.tex:250–320`.  
   - **Issue:** The new running example is helpful, but the chapter ends without pointing readers to the fuzzy-set formalism immediately ahead.  
   - **Fix:** Append a short “Next steps” paragraph linking to Chapters 16–18 and explaining what components of the thermostat example will be formalized next.

## Chapters 16–19 (lecture_9.tex, lecture_10_part_i.tex, lecture_10_part_ii.tex, lecture_11.tex)

1. **De Morgan discussion still repeats verbatim**  
   - **Location:** `lecture_9.tex:269–320` and again at `lecture_9.tex:300–340`.  
   - **Issue:** The union/intersection/complement explanation appears twice (once in general terms, once in a formal subsection).  
   - **Fix:** Keep only one instance and reference it later to reduce redundancy.

2. **Fuzzy relation chapter lacks matrix-style illustration requested in V2**  
   - **Location:** `lecture_10_part_i.tex:180–320`.  
   - **Issue:** There are no heatmaps or matrix visuals for the relation → projection → composition pipeline, even though the V2 notes called that out as a “nice-to-have.”  
   - **Fix:** Add a simple `pgfplots` heatmap or table showing a relation, its projection, and the max–min composition result.

3. **Evolutionary computing chapter still lacks cross-references to earlier paradigms**  
   - **Location:** `lecture_11.tex:12–70`.  
   - **Issue:** The introduction mentions “neural networks” and “fuzzy logic” but does not cite which chapters contained those materials.  
   - **Fix:** Add explicit chapter references (e.g., “Chapters 7–12”) so readers can navigate backwards easily.

## Global / Editorial

1. **Exercises/lab boxes added only for a subset of chapters** – Chapters 3–8, 10–17 still lack the “handful of exercises or lab checklists” requested in General_Overview_V2.  
2. **List of Tables is still missing** – With multiple summary tables (losses, imbalance tactics, t-norms), the PDF would benefit from a `\listoftables` entry as suggested.  
3. **Consistent pseudocode coverage** – Only a few chapters now include pseudocode boxes (Chapters 6 and 13). The remaining algorithms (RNN cell, CNN block, Mamdani inference) still lack the short, consistent snippets mentioned in the global notes.  
4. **Build warnings persist** – Tectonic continues to emit `nullfont` warnings (lecture_6) and overfull boxes (Transformer figure, key_takeaways table). These need cleanup to ensure final PDF quality.
