# Terminology concordance (publisher-grade consistency)

Use this as the book-wide “single source of truth” for naming. Prefer the **canonical** term in prose and headings; treat alternatives as deprecated unless explicitly needed for historical context.

| Canonical term | Avoid / deprecated variants | Notes |
|---|---|---|
| book | notes, course notes, lecture notes | Use “book” in numbered chapters. |
| chapter | lecture | Use “chapter” for internal references. |
| loss function | cost function | “Objective” is OK when emphasizing minimization; otherwise “loss”. |
| objective | cost | Use when discussing optimization framing. |
| hypothesis class | model class, function class | Prefer “hypothesis class” when matching learning-theory framing. |
| model | hypothesis | Use “hypothesis” only in learning-theory context (ERM). |
| training set | training data | Both acceptable; prefer “training set” when paired with “validation/test”. |
| validation set | dev set | Use “validation set” consistently. |
| test set | hold-out set | Use “test set” consistently; “held-out set” acceptable once defined. |
| generalization | out-of-sample performance | Define once; then use “generalization”. |
| overfitting | memorization (unless defined) | “Memorization” can appear as an intuition, not as a synonym. |
| underfitting | high bias | Bias/variance language is OK but define. |
| regularization | penalty term | “Penalty” as an explanation; “regularization” as the concept. |
| calibration | probability calibration | Use “calibration” once defined. |
| reliability diagram | calibration plot | Prefer “reliability diagram” (with “calibration plot” in parentheses once). |
| feature | input variable, covariate | In ML chapters, “feature”; in stats chapters, “covariate” only if needed. |
| label | target, response variable | Use “label” (classification) and “target” (regression) deliberately. |
| parameter | weight | Use “weight” for neural networks, “parameter” for general models. |
| neuron | unit | “Unit” acceptable in a brief synonym note; default to “neuron”. |
| activation function | nonlinearity | “Nonlinearity” is acceptable as shorthand after definition. |
| gradient descent | GD | Define acronym once; then “gradient descent” preferred in prose. |
| empirical risk minimization | ERM | Define once; then “ERM” acceptable. |
| confusion matrix | confusion table | Use “confusion matrix”. |
| precision–recall | PR | Define once; then “PR” acceptable. |
| receiver operating characteristic | ROC | Define once; then “ROC” acceptable. |
| appendix | Appendix A/B/C | Appendices are lettered; never refer to “Appendix 22” style numbering. |

When in doubt: prefer the term used in `notes_output/notation.tex` and the chapter Learning Outcomes.

