# QA Log

## Chapters 1–3 (lecture_1.tex, lecture_2_part_i.tex)

1. **Incorrect cross-reference for logistic content**  
   - **Location:** lecture_1.tex:876–884 (“Chapters~2 and~3 work through maximum-likelihood … for linear and logistic regression”).  
   - **Issue:** Chapter 3 is actually the symbolic-integration/search case study; the logistic regression material now lives in Chapter 4 (lecture_2_part_ii.tex). The pointer leaves readers looking in the wrong place.  
   - **Recommendation:** Update the sentence to reference Chapter 2 for linear MLE/MAP and Chapter 4 for logistic regression, or split the pointer to the precise sections.

2. **Chapter 3 introduction references the wrong “previous chapter”**  
   - **Location:** lecture_2_part_i.tex:4–10 (“In the previous chapter, we introduced the fundamental question of what constitutes an intelligent system, particularly in the context of symbolic problem solving.”).  
   - **Issue:** The chapter immediately before Chapter 3 is the “Supervised Learning Foundations” chapter, not the Chapter 1 philosophical discussion. The opening paragraph therefore mis-describes what readers just studied and makes the transition jarring.  
   - **Recommendation:** Rephrase the opening to acknowledge the Chapter 2 supervised-learning recap and explicitly motivate why we now pivot to symbolic problem solving (or move the paragraph to Chapter 1 if it is meant to reference that material).

3. **Missing bridge between Chapters 2 and 3**  
   - **Location:** End of lecture_1.tex (just before the `% Chapter 2` marker) and the opening of lecture_2_part_i.tex.  
   - **Issue:** Chapter 2 ends with bias–variance diagnostics and immediately jumps to the symbolic integration case study with no closing summary that cues the shift from statistical learning to symbolic AI/search. The abrupt jump reinforced the confusion noted above, and it weakens the narrative promised in Chapter 1’s roadmap.  
   - **Recommendation:** Add a short “What’s next” paragraph at the end of Chapter 2 (or the start of Chapter 3) that contrasts statistical ERM methods with symbolic transformation search, so readers understand why the next chapter studies symbolic integration.

4. **Transition note for Part B recap**  
   - **Location:** lecture_2_part_i.tex:309–338 (Part B recap).  
   - **Observation:** The recap itself is accurate, but the prose promises “full derivations in Chapter 2/4.” Verify those sections remain intact (they do) and consider explicitly pointing to the section numbers (e.g., “Chapter 2, Sec. 2.3”). No action needed unless section numbering changes.

## Chapters 4–6 (lecture_2_part_ii.tex, lecture_3_part_i.tex, lecture_3_part_ii.tex)

1. **Incorrect “previous chapter” reference at start of Chapter 4**  
   - **Location:** lecture_2_part_ii.tex:10–22.  
   - **Issue:** Chapter 4 opens with “In the previous chapter, we focused on regression …” but the immediately preceding chapter is now Chapter 3 (symbolic integration/search). The statement confuses readers because Chapter 3 does not cover regression.  
   - **Recommendation:** Rewrite the opening to acknowledge the intervening symbolic-integration chapter (e.g., “Earlier we developed the supervised-learning toolkit; after the symbolic-search case study we now return to statistical models”) or move the regression recap to the bridge at the end of Chapter 2.

2. **Chapter 4 restates Chapter 2 almost verbatim**  
   - **Location:** lecture_2_part_ii.tex:13–210 (regression recap block).  
   - **Issue:** The entire linear-regression treatment (covariance, SSE, learning curves) reappears before classification. It duplicates Chapter 2 instead of summarizing, making navigation harder and contradicting Chapter 1’s promise that full derivations live in Chapter 2.  
   - **Recommendation:** Compress this block to a short refresher or replace it with explicit references to Chapter 2 sections; otherwise readers re-learn the same material and lose the narrative flow promised in the roadmap.

3. **No bridge from Chapters 4→5**  
   - **Location:** End of lecture_2_part_ii.tex (after ROC/PR/calibration boxes).  
   - **Issue:** The chapter ends abruptly after evaluation metrics; there is no closing paragraph previewing the neural-network material that follows. This makes the transition into Chapter 5 (history/perceptron) feel unmotivated.  
   - **Recommendation:** Add a short “Next: Perceptrons and neural architectures” paragraph explaining that the following chapter builds nonlinear classifiers from neurons/backprop, tying back to the limitations of logistic regression.

4. **Chapter 5 references “previous chapters” without context**  
   - **Location:** lecture_3_part_ii.tex:3–9.  
   - **Issue:** Chapter 6’s opening line “In the previous chapters, we introduced the perceptron …” is correct, but Chapter 5 (lecture_3_part_i) itself lacks a closing pointer to Chapter 6/backprop. The summary simply repeats takeaways.  
   - **Recommendation:** At the end of lecture_3_part_i.tex add a short forward-looking sentence (“Next we generalize to multi-layer perceptrons and derive backpropagation”) to smooth the hand-off to Chapter 6.

5. **Logistic pointers in Chapter 4 still reference Chapter 3 for derivations**  
   - **Location:** lecture_2_part_i.tex:310–337 (Part B recap note) and lecture_1.tex:876–884.  
   - **Issue:** Even after reinserting the regression recap, the text continues to promise “see Chapters 2 and 3 for MLE/MAP and logistic derivations,” but Chapter 3 is now the symbolic-search case study.  
   - **Recommendation:** Update all such references so Chapter 2 covers linear MLE/MAP and Chapter 4 covers logistic regression; Chapter 3 should no longer be listed in those pointers.

## Chapters 7–9 (lecture_4_part_i.tex, lecture_4_part_ii.tex, lecture_5_part_i.tex)

1. **Chapter labels and cross-references drift (Chapter 7 annotated as “Chapter 4 Part I”)**  
   - **Location:** lecture_4_part_i.tex:491–573.  
   - **Issue:** Within Chapter 7, the text references “Chapter 4 Part I/Part II,” reflecting an older numbering scheme. This is confusing because Chapter 4 is logistic regression, while the file is now Chapter 7.  
   - **Recommendation:** Update those internal references to “Chapter 7 Part I/II” (or simply “this chapter”) so the numbering matches the `% Chapter 7` header and the global ToC.

2. **No bridge from Chapter 7 MLPs to Chapter 8 RBFNs**  
   - **Location:** End of lecture_4_part_i.tex / beginning of lecture_4_part_ii.tex.  
   - **Issue:** Chapter 7 closes with backprop derivations but offers no “what’s next” paragraph that motivates the switch to RBF networks; Chapter 8 opens abruptly with “In the previous chapter … MLPs.”  
   - **Recommendation:** Add a short closing paragraph in Chapter 7 explaining why radial-basis networks are a complementary architecture (e.g., fixed-hidden-layer basis expansion vs. fully trainable MLP) and preview the kernel link.

3. **Chapter 8 still references “Chapter 4 Part II”**  
   - **Location:** lecture_4_part_ii.tex:1 (comment) and lines referencing “Part II.”  
   - **Issue:** Like Chapter 7, Chapter 8’s header comment and in-text references use the old chapter numbering.  
   - **Recommendation:** Update comments/labels to “% Chapter 8” (already there) and ensure any textual references (if present) say “Chapter 8” rather than “Chapter 4 Part II.”

4. **SOM chapter lacks forward pointer to Hopfield content**  
   - **Location:** End of lecture_5_part_i.tex.  
   - **Issue:** Chapter 9 covers SOMs and unsupervised learning, then stops without previewing Hopfield networks or the upcoming connectionist energy-based models. Readers may not realize Chapter 10 continues the unsupervised theme with associative memory.  
   - **Recommendation:** Add a “Next Steps” paragraph at the end of Chapter 9 linking to Hopfield networks and how they contrast with SOMs.

5. **Flow from supervised (Ch. 7–8) to unsupervised (Ch. 9) lacks narrative**  
   - **Observation:** The transition from RBFNs (supervised) to SOM/Hopfield (unsupervised) is abrupt; Chapter 8 concludes with kernel links but doesn’t mention clustering or unsupervised learning.  
   - **Recommendation:** Insert a bridging paragraph eithdo er at the end of Chapter 8 or the start of Chapter 9 explaining that the next chapter pivots to unsupervised/self-organizing methods, linking back to the roadmap in Chapter 1.

## Chapters 10–12 (lecture_5_part_ii.tex, lecture_6.tex, lecture_7.tex)

1. **Chapter numbering drift in Hopfield section**  
   - **Location:** lecture_5_part_ii.tex:1–5.  
   - **Issue:** The `% Chapter 10` marker matches the ToC, but several later references (e.g., “Part of Chapter 4 Part I”) remain elsewhere in the document. Verify no residual “Part I/II” references remain in this chapter; update to Chapter 10 terminology throughout.

2. **Transition from SOMs to Hopfield not explicit**  
   - **Location:** Junction between lecture_5_part_i.tex and lecture_5_part_ii.tex.  
   - **Issue:** Chapter 9 ends without steering readers to the associative-memory perspective, and Chapter 10 opens without referencing the SOM content, so the change in focus may feel abrupt.  
   - **Recommendation:** Add a one- or two-sentence reminder at the start of Chapter 10 (“Having covered self-organizing maps, we now study Hopfield networks as energy-based associative memories …”) to anchor the shift.

3. **Deep learning chapter (Chapter 11) still references SVM section as if earlier**  
   - **Location:** lecture_6.tex learning outcomes and kernel section.  
   - **Issue:** The Chapter 11 learning outcomes include “Recall SVM soft-margin intuition … relate to kernels” but there is no explicit forward/back reference to the prior chapter that covered SVMs; the CNN chapter dumps SVM review midstream.  
   - **Recommendation:** insert a short reminder near the kernel section pointing back to the earlier SVM chapter (Chapter 6) so readers know where that content lives.

4. **RNN chapter (Chapter 12) lacks explicit bridge from Chapter 11**  
   - **Location:** Start of lecture_7.tex.  
   - **Issue:** Chapter 12 begins with “In previous chapters, we have extensively studied feedforward neural networks …” but Chapter 11’s conclusion doesn’t explicitly set up RNNs. A short “Next: RNNs” paragraph at the end of Chapter 11 would smooth the transition.  
   - **Recommendation:** Add a closing paragraph in lecture_6.tex summarizing the limitations of feedforward/CNN models on sequences and previewing RNNs (Chapter 12).

5. **References/citations for historical context**  
   - **Observation:** The Hopfield chapter mentions Hopfield (1982) but does not cite an actual reference; similarly, the deep learning chapter references LeNet/AlexNet history with \citet{Krizhevsky2012} but may need explicit citation for Hopfield.  
   - **Recommendation:** Ensure `refs.bib` has a Hopfield citation and that lecture_5_part_ii.tex cites it (e.g., `\citet{Hopfield1982}`) to maintain consistency with earlier chapters.

## Chapter 13 (lecture_transformers.tex)

1. **Missing bridge from Chapter 12 (RNNs)**  
   - **Location:** Opening paragraph.  
   - **Issue:** The chapter immediately states attention formulas without reminding readers why transformers are introduced after the RNN limitations discussed in Chapter 12.  
   - **Recommendation:** Add a short introductory paragraph summarizing the shortcomings of RNNs (sequential processing, vanishing gradients, limited receptive field) and explicitly state that transformers address these issues via attention and parallelism.

2. **Shapes and conventions under-specified**  
   - **Location:** Scaled dot-product attention section.  
   - **Issue:** The text mentions \(n_q\) and \(n_k\) but does not state whether rows are batch- or sequence-major; readers may confuse conventions when comparing to earlier chapters.  
   - **Recommendation:** Add one sentence clarifying the batch/sequence layout and relate it to the Chapter 12 notation for RNN inputs.

3. **No cross-reference to subsequent NLP chapter**  
   - **Issue:** Chapter 13 ends without pointing to Chapter 14’s NLP applications, which rely on transformer encoders/decoders.  
   - **Recommendation:** Add a closing paragraph linking this architectural chapter to the upcoming NLP applications.

## Chapter 14 (lecture_8_part_i.tex)

1. **Legacy “Chapter 8 Part I” comments**  
   - **Location:** `% Chapter 8 Part I (continued)` markers.  
   - **Issue:** Old comments make it appear as though the file still belongs to Chapter 8, conflicting with the `% Chapter 14` header.  
   - **Recommendation:** Update or remove those comments to reflect Chapter 14 numbering.

2. **No forward pointer to Chapter 15**  
   - **Location:** End of Chapter 14 (after embedding/SGNS sections).  
   - **Issue:** The chapter ends abruptly after discussing word embeddings; there is no paragraph that tells readers the next chapter pivots to soft computing.  
   - **Recommendation:** Add a “Next: Soft Computing” paragraph to cue the transition.

3. **Citation scope**  
   - **Issue:** Chapter cites \citet{Mikolov2013} but does not reference earlier linguistic sources (e.g., Firth) or fastText/GloVe.  
   - **Recommendation:** Consider adding references to the distributional hypothesis origin or other embedding methods if discussed.

## Chapter 15 (lecture_8_part_ii.tex)

1. **Legacy “Chapter 8 Part II” comments**  
   - **Issue:** Similar to Chapter 14, multiple `% Chapter 8 Part II …` markers persist.  
   - **Recommendation:** Update to Chapter 15 to prevent confusion.

2. **Transition from neural to soft computing not explicit**  
   - **Location:** Opening paragraphs.  
   - **Issue:** The chapter says “In the previous chapters, we have focused on neural networks…” but does not reference Chapter 14 explicitly or explain why soft computing follows NLP in the roadmap.  
   - **Recommendation:** Add a short paragraph referencing the Chapter 1 roadmap and explaining that soft computing provides complementary methods to neural approaches.

3. **Forward pointer to fuzzy chapters**  
   - **Issue:** Chapter 15 introduces soft computing broadly but does not direct readers to the detailed fuzzy chapters (16–18).  
   - **Recommendation:** Conclude with a paragraph pointing to Chapters 16–18 for fuzzy sets/inference.

## Chapter 16 (lecture_9.tex)

1. **Legacy “Chapter 9” comments**  
   - **Issue:** Lines such as `% Chapter 9 (continued)` remain in the file, which can confuse navigation.  
   - **Recommendation:** Update or remove the legacy comments to reflect Chapter 16.

2. **Incomplete “Next Steps” previously fixed**  
   - **Status:** The dangling “Next Steps” section now has a sentence pointing to Chapter 17, which is good. Verify that similar sections earlier in the chapter also have complete text.

3. **Flow from soft computing to fuzzy sets**  
   - **Observation:** Ensure the opening paragraph references Chapter 15 explicitly so readers understand the pivot from soft computing overview to concrete fuzzy set operations.

## Chapter 17 (lecture_10_part_i.tex)

1. **Legacy “Chapter 10 Part I” references**  
   - **Issue:** The file still contains multiple `% Chapter 10 Part I (continued)` comments and even “Chapter 10 Part I: Closure…” headings.  
   - **Recommendation:** Replace these with “Chapter 17” labels.

2. **Missing bridge to Chapter 18**  
   - **Location:** End of Chapter 17.  
   - **Issue:** The chapter ends with key takeaways but does not preview the rule composition/defuzzification chapter that follows.  
   - **Recommendation:** Add a closing paragraph that directs readers to Chapter 18 for rule composition and defuzzification.

## Chapter 18 (lecture_10_part_ii.tex)

1. **Legacy numbering**  
   - **Issue:** Ensure no residual “Chapter 10” comments remain.  
   - **Recommendation:** Update to Chapter 18 consistently.

2. **No bridge to Chapter 19**  
   - **Location:** End of Chapter 18.  
   - **Issue:** The chapter concludes with key takeaways but does not set up the transition to evolutionary computing.  
   - **Recommendation:** Add a closing sentence pointing to Chapter 19’s evolutionary computing content.

## Chapter 19 (lecture_11.tex)

1. **Multiple “Chapter 11” references**  
   - **Location:** Several sections (e.g., “Continuing Chapter 11 notes…”).  
   - **Issue:** These references mislabel the chapter and will mislead readers and any auto-generated ToC.  
   - **Recommendation:** Update all “Chapter 11” mentions to “Chapter 19” or remove them.

2. **Backward references lack explicit chapter numbers**  
   - **Issue:** The opening recap mentions neural networks and fuzzy logic but not the chapters they correspond to.  
   - **Recommendation:** Add explicit references (e.g., “Chapters 7–12”) when recapping prior paradigms.

3. **Forward pointer (if any) missing**  
   - **Observation:** If there is an appendix or key takeaways after Chapter 19, a closing paragraph should cue readers. Consider adding a summary that ties evolutionary computing back to the Chapter 1 taxonomy.

## Chapter 19 (lecture_11.tex)

1. **Legacy “Chapter 11” references inside Chapter 19 file**  
   - **Location:** lecture_11.tex:256, 383, 550, 751, 856.  
   - **Issue:** Multiple sections still say “Chapter 11 (continued)” even though the file is Chapter 19, which will confuse readers and automated tooling.  
   - **Recommendation:** Update those headings/references to “Chapter 19” (or remove the legacy notes) to keep numbering consistent.

2. **No backward references to fuzzy chapters**  
   - **Observation:** Chapter 19 opens with a generic review of neural/fuzzy content but doesn’t cite the relevant chapters or sections, missing an opportunity to remind readers where those topics were covered.  
   - **Recommendation:** Add explicit references (e.g., “Chapters 7–12”) when recapping previous paradigms so readers can navigate back if needed.
