# Rights / Attribution Inventory (Compiled Manuscript)

- Date: 2026-02-28
- Branch: codex/publishability-qa

## Scope
This inventory is generated from the LaTeX entrypoint `notes_output/ece657_notes.tex` and all transitively included `\input{...}` files. Files not included in the compiled manuscript are listed separately at the end.

## Summary Counts

- Figures: 77
  - With `\includegraphics`: 8
  - TikZ/pgfplots-only (no raster include): 68
  - Captions with an explicit `Source:` line: 8
- Tables: 11
- Code blocks (`verbatim`): 15

## Flagged Items (MED/HIGH Risk)

No MED/HIGH rights-risk items detected in the compiled manuscript based on these heuristics:
- raster/vector includes via `\includegraphics` without a `Source:` line in the caption
- captions that cite a non-author source for included raster content

## Recommended "Redraw / Permission-Safety" Candidates

- (Not compiled) `notes_output/fl-intro.tex` contains multiple `\includegraphics{Figures/...}` calls; if this file is ever included in the book, those figures should be re-audited for permissions and likely redrawn/replaced.

## Optional: caption clarifications to reduce permissions back-and-forth

These are not red flags (the drawings are TikZ/pgfplots), but publishers sometimes ask for an explicit
"author-generated schematic" statement for canonical architecture diagrams even when they are redrawn.

- `notes_output/lecture_transformers.tex`: Figures `fig:lec13_transformer_block`, `fig:lec13_micro_figures`,
  `fig:lec13_masks`. Suggested caption suffix: `\textit{Source: author-generated schematic; inspired by \citet{Vaswani2017}.}`
  (and optionally cite \citet{Su2021RoPE} for RoPE and \citet{Hu2022LoRA} for LoRA in the micro-views figure).
- `notes_output/lecture_7.tex`: Figures `fig:lec7-lstm`, `fig:lec7-gru` already cite the original papers; optional to add
  `\textit{Source: author-generated schematic.}` if you want the same explicit style used for raster figures.

## Inventory (Figures)

### `notes_output/key_takeaways.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:big-picture-map | tikz/pgfplots | no | LOW | Unified design\hyp{}space map of the book. Each family is a design point defined by (representation, update/search oper… |
### `notes_output/lecture_10_part_i.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec10-extension | tikz/pgfplots | no | LOW | Mapping a fuzzy set through the function ``y = x-squared''. The membership at an output value y is the supremum over al… |
| fig:alpha-cut-nonmonotone | tikz/pgfplots | no | LOW | Alpha-cuts under the non-monotone map ``y = x-squared''. A symmetric triangular fuzzy set on X maps to a right-skewed f… |
| fig:lec10_projection_matrix | figure | no | LOW | Illustrative fuzzy relation table (left) together with its projections onto the error universe (middle) and the rate-of… |
### `notes_output/lecture_11.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec11-ea-micro | tikz/pgfplots | no | LOW | Evolutionary micro-operators. Left: fitter individuals get sampled more often (roulette/tournament). Middle: crossover… |
| fig:lec11-ga-progress | tikz/pgfplots | no | LOW | Illustrative GA run showing the best and mean normalized fitness over 50 generations. Flat regions motivate ``no improv… |
| fig:lec11-ga-flow | tikz/pgfplots | no | LOW | GA flowchart showing the iterative process: initialization leads to fitness evaluation and a termination check. If not… |
| fig:lec11-pareto | includegraphics | yes | LOW | Sample Pareto front for two objectives. NSGA-II keeps all non-dominated points (blue) while pushing dominated solutions… \| assets: lec19_pareto |
### `notes_output/lecture_1_intro.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:roadmap | tikz/pgfplots | no | LOW |  |
### `notes_output/lecture_2_part_i.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec3_transform_tree | tikz/pgfplots | no | LOW | Transformation tree for the running example integral. Badges \textbf{[S]}/\textbf{[H]} mark safe vs.\ heuristic moves;… |
### `notes_output/lecture_2_part_ii.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec1_dataset | tikz/pgfplots | no | LOW | Synthetic binary dataset built from two anisotropic Gaussian clusters; shaded ellipses hint at the underlying density w… |
| fig:lec1_bayes | tikz/pgfplots | no | LOW | Bayes-optimal boundary for two Gaussian classes. Equal covariances and similar priors (LDA setting) yield a linear sepa… |
| fig:lec2_sigmoid_bce | tikz/pgfplots | no | LOW | The sigmoid maps logits to probabilities (left). The binary cross\hyp{}entropy (negative log\hyp{}likelihood) penalizes… |
| fig:lec1_gd | tikz/pgfplots | no | LOW | Gradient-descent iterates contracting toward the minimizer of a convex quadratic cost (schematic). Ellipses are level s… |
| fig:lec2-logistic-boundary | includegraphics | yes | LOW | Illustrative logistic-regression boundary. The dashed line marks the linear decision boundary at probability 0.5; label… \| assets: assets/lec2_part2/lec2_logistic_boundary.png, assets/lec2_part2/lec2_logistic_boundary.pdf |
| fig:lec1_mle_map | tikz/pgfplots | no | LOW | MAP estimates interpolate between the prior mean and the data-driven MLE. As the sample size grows, the MAP curve appro… |
| fig:lec1-roc-pr | includegraphics | yes | LOW | ROC and PR curves with an explicit operating point. Left: ROC curve with iso-cost lines; right: PR curve with a class-p… \| assets: assets/lec2_part2/lec2_roc_pr.png, assets/lec2_part2/lec2_roc_pr.pdf |
| fig:lec1_confusion | tikz/pgfplots | no | LOW | Confusion matrix for a three-class classifier; diagonals dominate, indicating strong accuracy with modest confusion bet… |
### `notes_output/lecture_3_part_i.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec3-perceptron-geometry | tikz/pgfplots | no | LOW | Perceptron geometry. Points on opposite sides of the separating hyperplane receive different labels, and signed distanc… |
### `notes_output/lecture_3_part_ii.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:mlp_minimal_chain | tikz/pgfplots | no | LOW | The minimal neural network used in this chapter is a two-neuron chain. The first unit produces an intermediate signal,… |
| fig:mlp_gd_surface | tikz/pgfplots | no | LOW | Think of performance as a surface over the weights. Gradient descent moves in one vector step (blue), whereas coordinat… |
| fig:mlp_step_vs_sigmoid | tikz/pgfplots | no | LOW | Hard thresholds block gradient-based learning because the derivative is zero almost everywhere. A smooth activation lik… |
### `notes_output/lecture_4_part_i.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:backprop-computational-graph | tikz/pgfplots | no | LOW | Computational graph for a feedforward network. Backpropagation is reverse\hyp{}mode automatic differentiation (AD): the… |
| fig:lec4_backprop_flow | tikz/pgfplots | no | LOW | Forward (blue) and backward (orange) flows for a two-layer MLP. Cached activations and layerwise deltas travel along th… |
| fig:lec4-activations | tikz/pgfplots | no | LOW | Canonical activation functions on a common axis. Solid curves show the activation; dashed curves show its derivative. |
### `notes_output/lecture_4_part_ii.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:rbf_architecture_weights | tikz/pgfplots | no | LOW | RBFN architecture. Inputs feed fixed radial units parameterized by centers and widths; a linear readout with weights an… |
| fig:rbf_gaussian_bumps | tikz/pgfplots | no | LOW | Localized Gaussian basis functions (dashed) and their weighted sum (solid). Overlapping bumps allow RBF networks to int… |
| fig:rbf_centres | tikz/pgfplots | no | LOW | Center placement and overlap (schematic). K-means prototypes tend to tile the data manifold more evenly than random pic… |
| fig:rbf_xor_feature_map | tikz/pgfplots | no | LOW | XOR before and after an RBF feature map. Left: in \((x_1,x_2)\), no single line separates the labels. Right: in \((g_1,… |
| fig:rbf_sigma_sweep | tikz/pgfplots | no | LOW | Schematic illustration of how the width parameter \(\sigma\) influences decision boundaries: too-large \(\sigma\) under… |
| fig:rbf_primal_dual | tikz/pgfplots | no | LOW | Primal (finite basis) vs.\ dual (kernel ridge) viewpoints. Using as many centers as data points recovers the dual form;… |
| fig:rbf_boundary | tikz/pgfplots | no | LOW | Effect of \(\sigma\) on an RBFN XOR boundary (4 centers at the data corners, ridge \(\lambda=10^{-3}\), threshold 0.5).… |
### `notes_output/lecture_5_part_i.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec5-learning-rate | tikz/pgfplots | no | LOW | Learning-rate scheduling intuition (schematic). On a smooth objective (left), large initial steps quickly cover ground… |
| fig:lec5-mds-projection | tikz/pgfplots | no | LOW | Classical MDS intuition (schematic). Projecting a cube onto a plane via an orthogonal map yields a square (left), where… |
| fig:lec5-gaussian-neighborhood | tikz/pgfplots | no | LOW | Gaussian neighborhood weights in SOM training (schematic). Early iterations use a broad kernel so many neighbors adapt;… |
| fig:lec5-bias-variance | tikz/pgfplots | no | LOW | Illustrative bias--variance trade-off when sweeping SOM capacity (number of units or kernel width). The optimum appears… |
| fig:lec5-regularization | tikz/pgfplots | no | LOW | Regularization smooths an objective surface (schematic). Coupling neighboring prototypes (right) yields wider, flatter… |
| fig:lec5-crossentropy | tikz/pgfplots | no | LOW | Illustrative objective surface combining quantization error and an entropy-style regularizer (a modern SOM variant; for… |
| fig:lec5-early-stopping | tikz/pgfplots | no | LOW | Illustrative validation curves used to identify an early\hyp{}stopping knee. When both quantization and topographic err… |
| fig:lec5-softmax-regions | tikz/pgfplots | no | LOW | Voronoi-like regions induced by fixed prototypes in input space (left) and the corresponding soft assignments after sha… |
| fig:lec5-som-lattice-umatrix | tikz/pgfplots | no | LOW | Left: a 5-by-5 SOM grid with the best matching unit (blue) and neighbors inside the Gaussian-kernel radius (green). Rig… |
| fig:lec5-som-component-planes | tikz/pgfplots | no | LOW | Component planes for three features on a trained SOM (toy data). Each plane maps one feature across the grid; aligned b… |
| fig:som_neighborhood | tikz/pgfplots | no | LOW | SOM grid with the best-matching unit (BMU) highlighted in blue and a dashed neighborhood radius indicating which protot… |
### `notes_output/lecture_5_part_ii.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:hopfield-energy-descent | tikz/pgfplots | no | LOW | Hopfield energy decreases monotonically under asynchronous updates. Starting from a noisy probe \(\mathbf{s}^{(0)}\), s… |
| fig:hopfield-basins-schematic | tikz/pgfplots | no | LOW | Energy-landscape intuition (schematic). Hopfield recall is a descent process toward a nearby basin (a stored memory), b… |
### `notes_output/lecture_6.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:cnn_receptive_field_growth | tikz/pgfplots | no | LOW | Receptive field growth across depth. Even with small \(3\times3\) kernels, stacking layers expands the spatial context… |
| fig:lec6-dropout | includegraphics | yes | LOW | Illustrative dropout effect on training/validation curves. Compared to a no\hyp{}dropout baseline, validation curves fl… \| assets: lec6_dropout_curves |
| fig:lec6-bn | tikz/pgfplots | no | LOW | Batch normalization normalizes per-channel activations and then applies a learned scale and shift, which stabilizes tra… |
| fig:lec6-optimizers | tikz/pgfplots | no | LOW | Representative training curves for SGD with momentum versus Adam on the same CNN. The point is the typical shape: Adam… |
### `notes_output/lecture_7.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec7-boundaries | tikz/pgfplots | no | LOW | Decision boundaries for logistic regression (left) versus a shallow MLP (right). Linear models carve a single hyperplan… |
| fig:lec7-loss-hyperparams | tikz/pgfplots | no | LOW | Binary cross-entropy geometry (left), effect of learning-rate schedules on loss (middle), and the typical training/vali… |
| fig:lec7-rnn-unrolled | tikz/pgfplots | no | LOW | Unrolling an RNN reveals repeated application of the same parameters across time steps. This view motivates backpropaga… |
| fig:lec7-bptt | tikz/pgfplots | no | LOW | Backpropagation through time (BPTT): unrolled forward pass (black) and backward gradients (pink) through time. |
| fig:lec7-vanishing | includegraphics | yes | LOW | Vanishing (blue) versus exploding (orange) gradients on a log scale. The gray strip highlights the stability band; the… \| assets: lec7_vanish_explode |
| fig:lec7-clipping | tikz/pgfplots | no | LOW | Gradient norms (left) explode without clipping (orange) but remain bounded when the global norm is clipped at tau (gree… |
| fig:lec7-teacher-forcing | tikz/pgfplots | no | LOW | Teacher forcing vs.\ inference in a sequence-to-sequence decoder. Gold arrows show supervised targets; orange arrows hi… |
| fig:lec7-lstm | tikz/pgfplots | no | LOW | Long Short-Term Memory (LSTM) cell \citep{Hochreiter1997,Gers2000}. |
| fig:lec7-gru | tikz/pgfplots | no | LOW | Gated Recurrent Unit (GRU) cell \citep{Cho2014}. |
| fig:lec7-attention | tikz/pgfplots | no | LOW | Attention heatmap for a translation model. Rows are target tokens (decoder steps) and columns are source tokens (encode… |
### `notes_output/lecture_8_part_i.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec8-embedding-clusters | includegraphics | yes | LOW | Analogy geometry in embedding space. The offset ``v(king) - v(man) + v(woman) approx v(queen)'' forms a parallelogram;… \| assets: lec14_analogy_geometry |
### `notes_output/lecture_9.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec9-grade-trapezoids | tikz/pgfplots | no | LOW | Trapezoidal membership functions for grades C and B with the overlapping region shaded. Scores near 78--82 partially sa… |
| fig:lec9-membership-overlap | tikz/pgfplots | no | LOW | Overlapping membership functions for the ``Small'', ``Medium'', and ``Large'' weight labels. The shaded overlaps captur… |
| fig:tnorm-surfaces | includegraphics | yes | LOW | Fuzzy AND surfaces comparing minimum versus product t\hyp{}norms; analogous OR surfaces show similar differences. Choic… \| assets: lec16_fuzzy_and |
| fig:fuzzy-end-to-end | tikz/pgfplots | no | LOW | End-to-end fuzzy inference example. (A) Consequent membership functions with clipping levels from firing strengths at T… |
### `notes_output/lecture_supervised.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec1_fit_regimes | tikz/pgfplots | no | LOW | Schematic underfitting and overfitting as a function of model complexity. Training error typically decreases with compl… |
| fig:lec1_l1_l2_geometry | tikz/pgfplots | no | LOW | Why L1 promotes sparsity (geometry). Minimizing loss subject to an L2 constraint tends to hit a smooth boundary; an L1… |
| fig:lec1_lasso_path | tikz/pgfplots | no | LOW | Illustrative lasso path as the regularization strength increases. Coefficients shrink, and some become exactly zero, yi… |
| fig:lec1_class_losses | tikz/pgfplots | no | LOW | Classification losses as functions of the signed margin \(z\). The curves highlight how different losses treat confiden… |
| fig:lec1_reg_losses | tikz/pgfplots | no | LOW | Regression losses versus prediction error. The Huber loss transitions from quadratic to linear, reducing sensitivity to… |
| fig:lec1_splits | tikz/pgfplots | no | LOW | Dataset partitioning into training, validation, and test segments. Any resampling scheme should preserve disjoint evalu… |
| fig:lec1_pipeline | tikz/pgfplots | no | LOW | Mini ERM pipeline (split once, iterate train/validate, then test only the best model on the held-out set). This keeps t… |
| fig:lec1_learning_curves | tikz/pgfplots | no | LOW | Illustrative learning curves reveal under/overfitting: the validation curve flattens while additional data continue to… |
| fig:lec1-calibration-double-descent | includegraphics | yes | LOW | Calibration and capacity diagnostics. Left: reliability diagram with binned predicted probabilities vs.\ empirical accu… \| assets: assets/lec1/lec1_reliability_double |
| fig:lec1_ridge | tikz/pgfplots | no | LOW | Ridge regularization shrinks parameter norms as the penalty strength increases. This controls variance without forcing… |
### `notes_output/lecture_transformers.tex`

| ID | Type | Source line | Risk | Notes |
| --- | --- | --- | --- | --- |
| fig:lec13_transformer_block | tikz/pgfplots | no | LOW | Reference schematic for the Transformer. Left: scaled dot-product attention. Center: multi-head concatenation with an o… |
| fig:lec13_micro_figures | tikz/pgfplots | no | LOW | Transformer micro-views. Left: positional encodings (sinusoidal/rotary) add order information. Center: KV cache stores… |
| fig:lec13_masks | tikz/pgfplots | no | LOW | Attention masks as heatmaps (queries on rows, keys on columns). Left: padding mask zeroes out attention to padded \emph… |

## Inventory (Tables)

### `notes_output/key_takeaways.tex`

| ID | Caption | Risk | Notes |
| --- | --- | --- | --- |
| tab:big-picture-models |  | LOW | OK |
### `notes_output/lecture_10_part_i.tex`

| ID | Caption | Risk | Notes |
| --- | --- | --- | --- |
| tab:tnorms | Popular t\hyp{}norms and their typical roles. Reference when choosing a default conjunction operator and understanding… | LOW | OK |
### `notes_output/lecture_11.tex`

| ID | Caption | Risk | Notes |
| --- | --- | --- | --- |
| tab:ga-toy | Toy GA generation on a bounded interval. One crossover and mutation illustrate how the fitness function guides selectio… | LOW | OK |
### `notes_output/lecture_2_part_i.tex`

| ID | Caption | Risk | Notes |
| --- | --- | --- | --- |
| line 522 | Table: Transformation toolkit (safe vs.\ heuristic). Preconditions keep domains/branches explicit (e.g., restrictions l… | LOW | OK |
### `notes_output/lecture_2_part_ii.tex`

| ID | Caption | Risk | Notes |
| --- | --- | --- | --- |
| line 546 | Handling class imbalance for logistic models (\Cref{chap:logistic} reference table). A compact menu of resampling, weig… | LOW | OK |
### `notes_output/lecture_5_part_ii.tex`

| ID | Caption | Risk | Notes |
| --- | --- | --- | --- |
| tab:hopfield-deltaE | Single-neuron flips from \((1,1,-1)\); all raise the energy, so the state is a local minimum. | LOW | OK |
### `notes_output/lecture_8_part_i.tex`

| ID | Caption | Risk | Notes |
| --- | --- | --- | --- |
| tab:word_feature_vectorization | Feature-based word vectorization example. Each word is mapped to a vector of graded semantic features; fractional entri… | LOW | OK |
### `notes_output/lecture_8_part_ii.tex`

| ID | Caption | Risk | Notes |
| --- | --- | --- | --- |
| tab:fuzzy-vs-prob | Fuzzy vs.\ probabilistic reasoning. Distinguishes randomness (probability) from graded concepts (fuzziness) when interp… | LOW | OK |
| tab:boolean-vs-fuzzy | Boolean vs.\ fuzzy operators. Mapping from crisp logic rules to graded operators for fuzzy inference. | LOW | OK |
### `notes_output/lecture_9.tex`

| ID | Caption | Risk | Notes |
| --- | --- | --- | --- |
| tab:fuzzy-operators | Typical operator choices in fuzzy inference and their qualitative effects. Here the t\hyp{}norm implements fuzzy AND, t… | LOW | OK |
### `notes_output/lecture_supervised.tex`

| ID | Caption | Risk | Notes |
| --- | --- | --- | --- |
| line 265 | Common losses and typical use (reference for \Crefrange{chap:supervised}{chap:perceptron}). Match the loss to your mode… | LOW | OK |

## Inventory (Code Blocks)

### `notes_output/lecture_10_part_i.tex`

| Location | Context (2 lines before) | Notes |
| --- | --- | --- |
| line 550 | \begin{tcolorbox}[summarybox, title={Max--min composition as ``fuzzy matrix multiply''}] Given \(R_1 \in [0,1]^{\|X\|\tim… | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
### `notes_output/lecture_10_part_ii.tex`

| Location | Context (2 lines before) | Notes |
| --- | --- | --- |
| line 207 | \noindent \begin{tcolorbox}[summarybox, title={Pipeline at a glance (Mamdani/Larsen)}] | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
### `notes_output/lecture_11.tex`

| Location | Context (2 lines before) | Notes |
| --- | --- | --- |
| line 819 | The GA can be expressed in pseudocode as follows. Treat this as the ``minimum viable'' skeleton; a production implement… | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
### `notes_output/lecture_2_part_i.tex`

| Location | Context (2 lines before) | Notes |
| --- | --- | --- |
| line 468 | \begin{tcolorbox}[summarybox, breakable, title={Transformation-tree search (pseudocode)}] \footnotesize | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
### `notes_output/lecture_4_part_i.tex`

| Location | Context (2 lines before) | Notes |
| --- | --- | --- |
| line 102 | \begin{tcolorbox}[summarybox, title={Mini example (aligned with this chapter): mean squared error (MSE) backprop on a t… | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
| line 266 | \begin{tcolorbox}[summarybox, title={Implementation pattern (modern practice): softmax + cross-entropy}] \footnotesize | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
### `notes_output/lecture_4_part_ii.tex`

| Location | Context (2 lines before) | Notes |
| --- | --- | --- |
| line 546 | \begin{tcolorbox}[summarybox, title={Practical RBFN training (pseudocode)}] | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
### `notes_output/lecture_6.tex`

| Location | Context (2 lines before) | Notes |
| --- | --- | --- |
| line 427 | \textbf{Mixed precision.} Modern CNN stacks often run activations/gradients in FP16 or BF16 while keeping master weight… | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
| line 437 | \begin{tcolorbox}[summarybox, title={MLP/CNN block pseudocode (schematic)}] \footnotesize | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
### `notes_output/lecture_7.tex`

| Location | Context (2 lines before) | Notes |
| --- | --- | --- |
| line 337 | \begin{tcolorbox}[summarybox, title={Truncated BPTT in practice}] Unroll \(K\) steps, accumulate loss, backprop through… | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
| line 352 | \begin{tcolorbox}[summarybox, title={Simple (ungated) RNN cell (forward + BPTT)}] | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
| line 821 | \begin{tcolorbox}[summarybox, title={Implementation checklist: masks, clipping, pitfalls}] \textbf{Minimal training loo… | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
### `notes_output/lecture_9.tex`

| Location | Context (2 lines before) | Notes |
| --- | --- | --- |
| line 322 | \paragraph{Quick plotting snippet.} With \texttt{scikit-fuzzy} or plain \texttt{matplotlib} you can visualize overlaps… | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
### `notes_output/lecture_transformers.tex`

| Location | Context (2 lines before) | Notes |
| --- | --- | --- |
| line 591 | \begin{tcolorbox}[summarybox, breakable, title={Implementation sketch: block pseudocode, training defaults, and one ste… | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |
| line 608 | \medskip \noindent\textbf{One training step (decoder-only, causal mask).} | VERIFY ORIGINALITY if copied; otherwise OK (author-written snippet) |

## Non-Compiled Files With `\includegraphics` (Heads-up)

- `notes_output/fl-intro.tex:291`: `\centerline{\includegraphics[height=6.8cm]{Figures/Intelligent_Machine}}`
- `notes_output/fl-intro.tex:303`: `\centerline{\includegraphics[height=6.8cm]{Figures/Intelligent_Machine_1}}`
- `notes_output/fl-intro.tex:388`: `\centerline{\includegraphics[height=3.8cm]{Figures/AI_ML_DL}}`
- `notes_output/fl-intro.tex:426`: `\includegraphics[scale=0.4]{structural_typestree.pdf}`
- `notes_output/fl-intro.tex:548`: `\includegraphics[scale=0.4]{reg1}`
- `notes_output/fl-intro.tex:554`: `\includegraphics[scale=0.4]{reg2}`
- `notes_output/fl-intro.tex:562`: `\includegraphics[scale=0.4]{reg3}`
- `notes_output/fl-intro.tex:580`: `\includegraphics[scale=0.4]{reg4}`
- `notes_output/fl-intro.tex:610`: `\includegraphics[scale=0.7]{reg5}`
- `notes_output/fl-intro.tex:736`: `\includegraphics[scale=0.4]{reg6}`
- `notes_output/fl-intro.tex:742`: `\includegraphics[scale=0.4]{reg7}`
- `notes_output/fl-intro.tex:797`: `\includegraphics[scale=0.4]{reg8}`
- `notes_output/fl-intro.tex:840`: `\includegraphics[scale=0.6]{logit}`
- `notes_output/fl-intro.tex:873`: `\includegraphics[scale=0.65]{logitvsregr}`
