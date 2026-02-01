# Scientific QA Action Items

## Outline & Logistics (Chunks 3, 13–20)
- Fix the duplicate heading “Learning Paradigms in Neural Networks” listed for both 4.6 and 4.7 in the table of contents.
- Reconcile the conflicting statements about assignment group formation (pre-assigned versus student-selected) and clarify whether individual submissions are allowed.
- Expand administrative notes to cover quiz availability windows, accessibility accommodations, late submission policies, and clearly define terms such as “discussion sessions” and “reading week.”

## Foundations & Historical Context (Chunks 14–20)
- Tighten the definitions of “signal,” “system,” and related terminology by specifying domains/codomains and formal properties.
- Correct the historical claim that formal logic emerged in the 13th century; cite 19th/20th-century developments (Boole, Frege, Peano, Russell).
- Differentiate inductive reasoning from conditional logic and ensure terminology around meta-cognition, regret, and self-defined objectives is precise.

## Calculus Refresher (Chunks 21–22)
- Restore missing integral signs/limits in the “Safe Transformations” list and verify every rule is written with the proper notation.
- Fix the trigonometric heuristic example by replacing the false statement “cos x = tan x” with “sin x / cos x = tan x,” and rewrite the secant substitution steps with correct algebra.

## Regression & Classification Math (Chunks 23–27)
- Rewrite the MSE objective (Eq. 21) with the squared residual term and clean summation/index notation; state the minimization variable explicitly.
- Clarify the standard deviation notation in Eq. 25 and state σX = √Var(X), σY = √Var(Y).
- Reinforce that the Naive Bayes factorization relies on conditional independence given the class.
- Define the noise model ε in Eq. 42 (e.g., zero-mean, iid) and explicitly show how Bayes’ rule sums over classes in Eq. 43.
- Correct the logistic sigmoid definition (section 3.10) to σ(z) = 1 / (1 + e^{−z}) and standardize parameter symbols across sections.

## Neural Network Primer (Chunks 28–37)
- Replace placeholder references (e.g., “Section ??”) with real section numbers and ensure RNN update equations have unambiguous parentheses.
- Consistently denote activations, weighted sums, and layer indices (a^{(ℓ)}, z^{(ℓ)} etc.) across perceptron and multilayer derivations.
- State the loss function before presenting gradients/backprop equations and remind the reader of key update formulas (e.g., Eq. 172).
- Finish incomplete discussions (e.g., RBF projection in §7.11) and cite the universal approximation guarantee conditions.

## Unsupervised & Recurrent Models (Chunks 40–46)
- Complete fragmentary sentences (e.g., SOM dimensionality reduction paragraph) and separate dot-product vs. distance-based similarity metrics.
- Use one winner-neuron symbol (j* or i*) throughout and annotate the neighborhood function definition with the meaning of the indicator.
- Clarify the “six procedural steps” in SOM training or provide a reference.
- Update Hopfield energy discussions to respect the {0,1} state encoding (or convert to {−1,+1}) and add the missing weight matrix illustration in the worked example.

## Backprop Depth & Training Stability (Chunks 47–48)
- Expand Eq. 173 into a concrete product of weight matrices and activation derivatives rather than a shorthand W·f′^{L−1}.
- Adjust the AlexNet historical note: cite the original Top-1 accuracy (~62.5%) and Top-5 (~84.7%) with a reference.

## Convolutional Nets (Chunks 49–55)
- Distinguish rigorously between convolution and cross-correlation, and explain why modern CNNs implement the latter.
- Spell out pooling output-size formulas using the floor operator and general stride/padding variables.
- Fix equation cross-references that jump ahead (e.g., mention Eq. 209/217 only after they appear) and tighten notation for concatenated hidden states.

## Representation Learning (Chunks 56–62)
- Define vocabulary size |V| before using it and clarify cosine similarity notation in analogy examples.
- Explicitly describe “self-supervised” training in language modeling and correct truncated sentences (chunk 61).
- Justify or revise the “log X” SVD discussion—specify whether the log is elementwise and how zeros are handled.

## Fuzzy Logic Chapters (Chunks 63–75)
- Finish the missing definition of “Imprecision” and align terminology across imprecision, uncertainty, and fuzziness.
- Rewrite fuzzy membership functions (triangular, trapezoidal, grade C example) with complete, piecewise expressions.
- Declare operator symbols (∧, ∨, ⊗, ⊕) before use and avoid overloading logical notation with min/max without explanation.
- Verify relational compositions and projections specify their quantification domain (e.g., sup_{y ∈ Y}).

## Evolutionary Computation (Chunks 76–81)
- Define the feasible domain D in optimization problems and separate heuristic guidance from convergence guarantees.
- Formalize crossover/mutation operator notation with parent/offspring indices and explain how invalid chromosomes (e.g., zero encoding) are handled.
- Provide a concrete example of a genetic programming fitness evaluation and clarify what “recursive and modular programs” means in practice.

