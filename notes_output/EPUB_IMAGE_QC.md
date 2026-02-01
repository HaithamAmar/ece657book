# EPUB image quality audit (heuristic + model-assisted triage)

- Source JSON: `notes_output/artifacts/qc/epub_image_quality_20260201_184424.json`
- Total images: 75
- Flagged images: 0

## How to interpret flags

- `small_pixel_dimensions`: likely to appear soft when zoomed.
- `low_sharpness`: blurred / low-detail raster (often from low-DPI conversion).
- `content_touches_border`: potential cropping or insufficient padding.
- `mostly_blank`: likely missing render or transparent/blank export.

## Worst offenders (prioritized)

### `EPUB/media/file74.png`
- Size: 1600×2560 (4815964 bytes)
- Risk score: 8.0
- Flags: (none)
- Metrics: lap_var=0.003841, edge=0.0805, white=0.048, border_nonwhite=1.000

### `EPUB/media/file71.png`
- Size: 10993×3557 (404782 bytes)
- Risk score: 3.111
- Flags: (none)
- Metrics: lap_var=0.004607, edge=0.0041, white=0.976, border_nonwhite=0.001
- Ref: `fig:lec11-ga-flow` in `EPUB/text/ch023.xhtml`
- Caption: Figure 73. Schematic: GA flowchart showing the iterative process: initialization leads to fitness evaluation and a termination check. If not terminated, the algorithm proceeds through selection, crossover, mutation, and replacement, which then feeds the next generation’s fitness evaluation.

### `EPUB/media/file30.png`
- Size: 5009×2117 (115642 bytes)
- Risk score: 2.734
- Flags: (none)
- Metrics: lap_var=0.003037, edge=0.0053, white=0.975, border_nonwhite=0.000
- Ref: `fig:rbf_sigma_sweep` in `EPUB/text/ch012.xhtml`
- Caption: Figure 31. Schematic: How the width parameter (sigma) influences decision boundaries on a 2D toy dataset. Too-large sigma underfits, intermediate sigma captures the boundary, too-small sigma overfits with fragmented regions. Use Chapter 3 ’s validation curves to pick model size and regularization.

### `EPUB/media/file0.png`
- Size: 9643×2616 (434223 bytes)
- Risk score: 2.446
- Flags: (none)
- Metrics: lap_var=0.007404, edge=0.0070, white=0.975, border_nonwhite=0.000
- Ref: `fig:roadmap` in `EPUB/text/ch005.xhtml`
- Caption: Figure 1. Schematic: Roadmap (core supervised path; SOM/fuzzy; optimization/evolutionary).

### `EPUB/media/file58.png`
- Size: 12600×7200 (772364 bytes)
- Risk score: 2.223
- Flags: (none)
- Metrics: lap_var=0.000815, edge=0.0016, white=0.885, border_nonwhite=0.000
- Ref: `fig:lec7-embedding-clusters` in `EPUB/text/ch016.xhtml`
- Caption: Figure 59. Schematic: Toy 2D projection of word embeddings showing neighboring clusters (countries vs. capitals). Light hulls highlight clusters; arrows show that country-to-capital displacement vectors align, a visual check on analogy structure.

### `EPUB/media/file13.png`
- Size: 4059×3019 (143350 bytes)
- Risk score: 1.549
- Flags: (none)
- Metrics: lap_var=0.002986, edge=0.0031, white=0.973, border_nonwhite=0.000
- Ref: `fig:lec1_bayes` in `EPUB/text/ch008.xhtml`
- Caption: Figure 14. Schematic: Bayes-optimal boundary for two Gaussian classes with equal covariances and similar priors (LDA setting), which yields a linear separator. Unequal covariances produce a quadratic boundary. We place the boundary near the equal-posterior line (vertical, pink); left/right regions correspond to predicted classes R0 and R1.

### `EPUB/media/file3.png`
- Size: 6225×2638 (335016 bytes)
- Risk score: 0.704
- Flags: (none)
- Metrics: lap_var=0.003094, edge=0.0067, white=0.971, border_nonwhite=0.000
- Ref: `fig:lec1_l1_l2_geometry` in `EPUB/text/ch007.xhtml`
- Caption: Figure 4. Schematic: Why L1 promotes sparsity. Minimizing loss subject to an L2 constraint tends to hit a smooth boundary; an L1 constraint has corners aligned with coordinate axes, so tangency often occurs at a point where some coordinates are exactly zero.

### `EPUB/media/file1.png`
- Size: 8209×5943 (529102 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.002109, edge=0.0048, white=0.806, border_nonwhite=0.000
- Ref: `fig:lec3_transform_tree` in `EPUB/text/ch006.xhtml`
- Caption: Figure 2. Schematic: Transformation tree for the running example integral; badges [S] / [H] mark safe vs. heuristic moves; the dashed branch mirrors the sine substitution.

### `EPUB/media/file10.png`
- Size: 8400×3840 (528362 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.008654, edge=0.0103, white=0.774, border_nonwhite=0.000
- Ref: `fig:lec1-calibration-double-descent` in `EPUB/text/ch007.xhtml`
- Caption: Figure 11. Schematic: Calibration and capacity diagnostics. Left: reliability diagram with binned predicted probabilities vs. empirical accuracy; Expected Calibration Error (ECE) measures deviation from the diagonal. Right: illustrative double-descent risk vs. model size (log-scale on the x-axis); dashed line sketches a scaling-law trend used to choose capacity/regularization.

### `EPUB/media/file11.png`
- Size: 4119×1890 (92395 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006318, edge=0.0051, white=0.964, border_nonwhite=0.000
- Ref: `fig:lec1_ridge` in `EPUB/text/ch007.xhtml`
- Caption: Figure 12. Schematic: Ridge regularization shrinks parameter norms as the penalty strength increases.

### `EPUB/media/file12.png`
- Size: 3527×2740 (226376 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.005055, edge=0.0084, white=0.885, border_nonwhite=0.000
- Ref: `fig:lec1_dataset` in `EPUB/text/ch008.xhtml`
- Caption: Figure 13. Schematic: Synthetic binary dataset built from two anisotropic Gaussian clusters; shaded ellipses hint at the underlying density while the scattered samples are reused throughout the running examples.

### `EPUB/media/file14.png`
- Size: 4355×1759 (185422 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.010601, edge=0.0099, white=0.947, border_nonwhite=0.000
- Ref: `fig:lec2_sigmoid_bce` in `EPUB/text/ch008.xhtml`
- Caption: Figure 15. Schematic: The sigmoid maps logits to probabilities (left). The binary cross-entropy (negative log-likelihood) penalizes confident wrong predictions sharply (middle). Regularization typically shrinks parameter norms as the penalty strength increases (right).

### `EPUB/media/file15.png`
- Size: 3734×3199 (376987 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006100, edge=0.0111, white=0.931, border_nonwhite=0.000
- Ref: `fig:lec1_gd` in `EPUB/text/ch008.xhtml`
- Caption: Figure 16. Schematic: Gradient-descent iterates contracting toward the minimizer of a convex quadratic cost. Ellipses are level sets; arrows show the “steepest descent along contours” direction.

### `EPUB/media/file16.png`
- Size: 5400×4320 (382070 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.003412, edge=0.0061, white=0.504, border_nonwhite=0.000
- Ref: `fig:lec2-logistic-boundary` in `EPUB/text/ch008.xhtml`
- Caption: Figure 17. Schematic: Illustrative logistic-regression boundary. The dashed line marks the linear decision boundary at probability 0.5; labeled contours show how the posterior varies smoothly with margin, enabling calibrated decisions and adjustable thresholds.

### `EPUB/media/file17.png`
- Size: 3818×2005 (168482 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.009505, edge=0.0098, white=0.947, border_nonwhite=0.000
- Ref: `fig:lec1_mle_map` in `EPUB/text/ch008.xhtml`
- Caption: Figure 18. Schematic: MAP estimates interpolate between the prior mean and the data-driven MLE. As the sample size grows, the MAP curve approaches the true mean.

### `EPUB/media/file18.png`
- Size: 7920×3840 (623410 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006959, edge=0.0079, white=0.932, border_nonwhite=0.000
- Ref: `fig:lec1-roc-pr` in `EPUB/text/ch008.xhtml`
- Caption: Figure 19. Schematic: ROC and PR curves with an explicit operating point. Left: ROC curve with iso-cost lines; right: PR curve with a class-prevalence baseline and iso-F1 contours. Together they visualize threshold trade-offs and calibration quality.

### `EPUB/media/file19.png`
- Size: 4285×2194 (143939 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006843, edge=0.0061, white=0.501, border_nonwhite=0.000
- Ref: `fig:lec1_confusion` in `EPUB/text/ch008.xhtml`
- Caption: Figure 20. Schematic: Confusion matrix for a three-class classifier; diagonals dominate, indicating strong accuracy with modest confusion between classes B and C.

### `EPUB/media/file2.png`
- Size: 4425×1704 (204438 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.007796, edge=0.0094, white=0.959, border_nonwhite=0.000
- Ref: `fig:lec1_fit_regimes` in `EPUB/text/ch007.xhtml`
- Caption: Figure 3. Schematic: Underfitting and overfitting as a function of model complexity. Training error typically decreases with complexity, while validation error often has a U-shape. Regularization and model selection aim to operate near the minimum of the validation curve.

### `EPUB/media/file20.png`
- Size: 3252×2217 (161075 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.002151, edge=0.0078, white=0.958, border_nonwhite=0.000
- Ref: `fig:lec3-perceptron-geometry` in `EPUB/text/ch009.xhtml`
- Caption: Figure 21. Schematic: Perceptron geometry. Points on either side of the separating hyperplane receive different labels, and the signed distance to the boundary controls both the class prediction and the magnitude of the update during learning. Compare to Figure 17 in Chapter 4 : both share a linear separator, but logistic smooths the boundary into calibrated probabilities.

### `EPUB/media/file21.png`
- Size: 11113×1400 (259634 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006098, edge=0.0050, white=0.839, border_nonwhite=0.000
- Ref: `fig:mlp_minimal_chain` in `EPUB/text/ch010.xhtml`
- Caption: Figure 22. Schematic: The minimal neural network used in this chapter is a two-neuron chain. The first unit produces an intermediate signal, and the second unit maps that signal to the final output.

### `EPUB/media/file22.png`
- Size: 3737×2205 (199473 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.004490, edge=0.0115, white=0.928, border_nonwhite=0.000
- Ref: `fig:mlp_gd_surface` in `EPUB/text/ch010.xhtml`
- Caption: Figure 23. Schematic: Think of performance as a surface over the weights. Gradient descent moves in one vector step (blue), whereas coordinate-wise updates can zig-zag (orange).

### `EPUB/media/file23.png`
- Size: 4505×1747 (106077 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006736, edge=0.0077, white=0.962, border_nonwhite=0.000
- Ref: `fig:mlp_step_vs_sigmoid` in `EPUB/text/ch010.xhtml`
- Caption: Figure 24. Schematic: Hard thresholds block gradient-based learning because the derivative is zero almost everywhere. A smooth activation like the sigmoid provides informative derivatives across a wide range of inputs.

### `EPUB/media/file24.png`
- Size: 8146×3795 (409349 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.001840, edge=0.0049, white=0.864, border_nonwhite=0.000
- Ref: `fig:backprop-computational-graph` in `EPUB/text/ch011.xhtml`
- Caption: Figure 25. Schematic: Computational graph for a feedforward network. Backpropagation is reverse-mode AD: the forward sweep caches intermediate values; the reverse sweep propagates error signals (deltas) and accumulates gradients for weights and biases from those cached values.

### `EPUB/media/file25.png`
- Size: 3706×2356 (291967 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.003986, edge=0.0086, white=0.868, border_nonwhite=0.000
- Ref: `fig:lec4_backprop_flow` in `EPUB/text/ch011.xhtml`
- Caption: Figure 26. Schematic: Forward (blue) and backward (orange) flows for a two-layer MLP. The cached activations and the layerwise error terms (deltas) are exactly the quantities carried along these arrows; backward signals are computed with the next-layer weights and the activation derivative.

### `EPUB/media/file26.png`
- Size: 4190×3108 (181621 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.005380, edge=0.0059, white=0.964, border_nonwhite=0.000
- Ref: `fig:lec4-activations` in `EPUB/text/ch011.xhtml`
- Caption: Figure 27. Schematic: Canonical activation functions on a common axis. Solid curves show the activation; dashed curves show its derivative.

## Figures softer than PDF (from QC bundle)

- None detected by the current sharpness regression heuristic.

## Suggested fixes (global)

- Prefer PDF→PNG rasterization at high DPI for plots/diagrams when a `.pdf` exists.
- Keep TikZ extracted figures at high DPI (already enabled) and consider increasing figure physical size for very thin diagrams.
- Ensure images referenced by `\includegraphics{...png}` prefer sibling `.pdf` sources when available.

