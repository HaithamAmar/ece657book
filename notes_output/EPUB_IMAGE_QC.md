# EPUB image quality audit (heuristic + model-assisted triage)

- Source JSON: `epub_builder/artifacts/qc/epub_image_quality_20260202_095526.json`
- Total images: 75
- Flagged images: 0

## How to interpret flags

- `small_pixel_dimensions`: likely to appear soft when zoomed.
- `low_sharpness`: blurred / low-detail raster (often from low-DPI conversion).
- `content_touches_border`: potential cropping or insufficient padding.
- `mostly_blank`: likely missing render or transparent/blank export.

## Worst offenders (prioritized)

### Cover image
- Media: `EPUB/media/file74.jpg`
- Size: 2560×4096 (1892333 bytes)

### `EPUB/media/file71.png`
- Size: 10993×3557 (404782 bytes)
- Risk score: 3.111
- Flags: (none)
- Metrics: lap_var=0.004607, edge=0.0041, white=0.976, border_nonwhite=0.001
- Ref: `fig:lec11-ga-flow` in `EPUB/text/ch023.xhtml`
- Caption: Figure 73. Schematic: GA flowchart showing the iterative process: initialization leads to fitness evaluation and a termination check. If not terminated, the algorithm proceeds through selection, crossover, mutation, and replacement, which then feeds the next generation’s fitness evaluation.

### `EPUB/media/file58.png`
- Size: 12600×7200 (772364 bytes)
- Risk score: 2.223
- Flags: (none)
- Metrics: lap_var=0.000815, edge=0.0016, white=0.885, border_nonwhite=0.000
- Ref: `fig:lec7-embedding-clusters` in `EPUB/text/ch016.xhtml`
- Caption: Figure 59. Schematic: Toy 2D projection of word embeddings showing neighboring clusters (countries vs. capitals). Light hulls highlight clusters; arrows show that country-to-capital displacement vectors align, a visual check on analogy structure.

### `EPUB/media/file13.png`
- Size: 4031×2996 (142682 bytes)
- Risk score: 1.351
- Flags: (none)
- Metrics: lap_var=0.003031, edge=0.0031, white=0.973, border_nonwhite=0.000
- Ref: `fig:lec1_bayes` in `EPUB/text/ch008.xhtml`
- Caption: Figure 14. Schematic: Bayes-optimal boundary for two Gaussian classes with equal covariances and similar priors (LDA setting), which yields a linear separator. Unequal covariances produce a quadratic boundary. We place the boundary near the equal-posterior line (vertical, pink); left/right regions correspond to predicted classes R0 and R1.

### `EPUB/media/file0.png`
- Size: 9677×2603 (428000 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.007148, edge=0.0071, white=0.965, border_nonwhite=0.000
- Ref: `fig:roadmap` in `EPUB/text/ch005.xhtml`
- Caption: Figure 1. Schematic: Roadmap (core supervised path; SOM/fuzzy; optimization/evolutionary).

### `EPUB/media/file1.png`
- Size: 8209×5946 (529064 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.002109, edge=0.0048, white=0.805, border_nonwhite=0.000
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
- Size: 4091×1868 (89848 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006437, edge=0.0052, white=0.963, border_nonwhite=0.000
- Ref: `fig:lec1_ridge` in `EPUB/text/ch007.xhtml`
- Caption: Figure 12. Schematic: Ridge regularization shrinks parameter norms as the penalty strength increases.

### `EPUB/media/file12.png`
- Size: 3505×2718 (226371 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.005125, edge=0.0085, white=0.884, border_nonwhite=0.000
- Ref: `fig:lec1_dataset` in `EPUB/text/ch008.xhtml`
- Caption: Figure 13. Schematic: Synthetic binary dataset built from two anisotropic Gaussian clusters; shaded ellipses hint at the underlying density while the scattered samples are reused throughout the running examples.

### `EPUB/media/file14.png`
- Size: 4333×1726 (184955 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.010865, edge=0.0102, white=0.946, border_nonwhite=0.000
- Ref: `fig:lec2_sigmoid_bce` in `EPUB/text/ch008.xhtml`
- Caption: Figure 15. Schematic: The sigmoid maps logits to probabilities (left). The binary cross-entropy (negative log-likelihood) penalizes confident wrong predictions sharply (middle). Regularization typically shrinks parameter norms as the penalty strength increases (right).

### `EPUB/media/file15.png`
- Size: 3712×3177 (376753 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006153, edge=0.0113, white=0.930, border_nonwhite=0.000
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
- Size: 3790×1977 (168522 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.009711, edge=0.0101, white=0.946, border_nonwhite=0.000
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
- Size: 4252×2167 (143386 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.007008, edge=0.0062, white=0.491, border_nonwhite=0.000
- Ref: `fig:lec1_confusion` in `EPUB/text/ch008.xhtml`
- Caption: Figure 20. Schematic: Confusion matrix for a three-class classifier; diagonals dominate, indicating strong accuracy with modest confusion between classes B and C.

### `EPUB/media/file2.png`
- Size: 4414×1693 (204457 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.007873, edge=0.0095, white=0.959, border_nonwhite=0.000
- Ref: `fig:lec1_fit_regimes` in `EPUB/text/ch007.xhtml`
- Caption: Figure 3. Schematic: Underfitting and overfitting as a function of model complexity. Training error typically decreases with complexity, while validation error often has a U-shape. Regularization and model selection aim to operate near the minimum of the validation curve.

### `EPUB/media/file20.png`
- Size: 3236×2210 (160193 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.002167, edge=0.0079, white=0.958, border_nonwhite=0.000
- Ref: `fig:lec3-perceptron-geometry` in `EPUB/text/ch009.xhtml`
- Caption: Figure 21. Schematic: Perceptron geometry. Points on either side of the separating hyperplane receive different labels, and the signed distance to the boundary controls both the class prediction and the magnitude of the update during learning. Compare to Figure 17 in Chapter 4 : both share a linear separator, but logistic smooths the boundary into calibrated probabilities.

### `EPUB/media/file21.png`
- Size: 11015×1400 (258842 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006243, edge=0.0050, white=0.830, border_nonwhite=0.000
- Ref: `fig:mlp_minimal_chain` in `EPUB/text/ch010.xhtml`
- Caption: Figure 22. Schematic: The minimal neural network used in this chapter is a two-neuron chain. The first unit produces an intermediate signal, and the second unit maps that signal to the final output.

### `EPUB/media/file22.png`
- Size: 3737×2199 (199166 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.004503, edge=0.0115, white=0.928, border_nonwhite=0.000
- Ref: `fig:mlp_gd_surface` in `EPUB/text/ch010.xhtml`
- Caption: Figure 23. Schematic: Think of performance as a surface over the weights. Gradient descent moves in one vector step (blue), whereas coordinate-wise updates can zig-zag (orange).

### `EPUB/media/file23.png`
- Size: 4494×1725 (104574 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006836, edge=0.0078, white=0.961, border_nonwhite=0.000
- Ref: `fig:mlp_step_vs_sigmoid` in `EPUB/text/ch010.xhtml`
- Caption: Figure 24. Schematic: Hard thresholds block gradient-based learning because the derivative is zero almost everywhere. A smooth activation like the sigmoid provides informative derivatives across a wide range of inputs.

### `EPUB/media/file24.png`
- Size: 8141×3787 (410008 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.001814, edge=0.0051, white=0.861, border_nonwhite=0.000
- Ref: `fig:backprop-computational-graph` in `EPUB/text/ch011.xhtml`
- Caption: Figure 25. Schematic: Computational graph for a feedforward network. Backpropagation is reverse-mode AD: the forward sweep caches intermediate values; the reverse sweep propagates error signals (deltas) and accumulates gradients for weights and biases from those cached values.

### `EPUB/media/file25.png`
- Size: 3695×2345 (292262 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.004016, edge=0.0086, white=0.867, border_nonwhite=0.000
- Ref: `fig:lec4_backprop_flow` in `EPUB/text/ch011.xhtml`
- Caption: Figure 26. Schematic: Forward (blue) and backward (orange) flows for a two-layer MLP. The cached activations and the layerwise error terms (deltas) are exactly the quantities carried along these arrows; backward signals are computed with the next-layer weights and the activation derivative.

### `EPUB/media/file26.png`
- Size: 4185×3085 (180942 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.005339, edge=0.0059, white=0.964, border_nonwhite=0.000
- Ref: `fig:lec4-activations` in `EPUB/text/ch011.xhtml`
- Caption: Figure 27. Schematic: Canonical activation functions on a common axis. Solid curves show the activation; dashed curves show its derivative.

### `EPUB/media/file27.png`
- Size: 4793×3196 (377635 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.005026, edge=0.0067, white=0.914, border_nonwhite=0.000
- Ref: `fig:rbf_architecture_weights` in `EPUB/text/ch012.xhtml`
- Caption: Figure 28. Schematic: RBFN architecture. Inputs feed fixed radial units parameterized by centers and widths; a linear readout with weights (and bias) is trained by a regression or classification loss. Only the output weights are typically learned; centers/widths come from k-means or spacing heuristics.

### `EPUB/media/file28.png`
- Size: 3786×1642 (207357 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.010415, edge=0.0114, white=0.926, border_nonwhite=0.000
- Ref: `fig:rbf_gaussian_bumps` in `EPUB/text/ch012.xhtml`
- Caption: Figure 29. Schematic: Localized Gaussian basis functions (dashed) and their weighted sum (solid). Overlapping bumps allow RBF networks to interpolate complex signals smoothly.

### `EPUB/media/file29.png`
- Size: 3482×3387 (267552 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.001153, edge=0.0073, white=0.171, border_nonwhite=0.000
- Ref: `fig:rbf_centres` in `EPUB/text/ch012.xhtml`
- Caption: Figure 30. Schematic: Center placement and overlap. Top: K-means prototypes roughly tile the data manifold, giving even overlap; bottom: random centers can leave gaps or excessive overlap, influencing the width (sigma) choice and conditioning.

### `EPUB/media/file3.png`
- Size: 6220×2625 (333872 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.003024, edge=0.0067, white=0.969, border_nonwhite=0.000
- Ref: `fig:lec1_l1_l2_geometry` in `EPUB/text/ch007.xhtml`
- Caption: Figure 4. Schematic: Why L1 promotes sparsity. Minimizing loss subject to an L2 constraint tends to hit a smooth boundary; an L1 constraint has corners aligned with coordinate axes, so tangency often occurs at a point where some coordinates are exactly zero.

### `EPUB/media/file30.png`
- Size: 5012×2111 (116828 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.003043, edge=0.0054, white=0.966, border_nonwhite=0.000
- Ref: `fig:rbf_sigma_sweep` in `EPUB/text/ch012.xhtml`
- Caption: Figure 31. Schematic: How the width parameter (sigma) influences decision boundaries on a 2D toy dataset. Too-large sigma underfits, intermediate sigma captures the boundary, too-small sigma overfits with fragmented regions. Use Chapter 3 ’s validation curves to pick model size and regularization.

### `EPUB/media/file31.png`
- Size: 3996×1818 (228902 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.008045, edge=0.0111, white=0.955, border_nonwhite=0.000
- Ref: `fig:rbf_primal_dual` in `EPUB/text/ch012.xhtml`
- Caption: Figure 32. Schematic: Primal (finite basis) vs. dual (kernel ridge) viewpoints. Using as many centers as data points recovers the dual form; using fewer centers corresponds to a Nyström approximation. The same trade-off appears in kernel methods through the choice of kernel and effective rank.

### `EPUB/media/file32.png`
- Size: 4151×3915 (193505 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.005104, edge=0.0062, white=0.512, border_nonwhite=0.000
- Ref: `fig:rbf_boundary` in `EPUB/text/ch012.xhtml`
- Caption: Figure 33. Schematic: RBFN decision boundary on the XOR toy for a model with 4 centers, width sigma = 0.8, and ridge lambda = 1e-3. Shading indicates the predicted class under a 0.5 threshold; the black contour marks the 0.5 boundary. Training points are overlaid (class 0: open circles; class 1: filled squares). See Figure 31 for how sigma changes this boundary.

### `EPUB/media/file33.png`
- Size: 4543×2136 (267682 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.009288, edge=0.0111, white=0.946, border_nonwhite=0.000
- Ref: `fig:lec5-learning-rate` in `EPUB/text/ch013.xhtml`
- Caption: Figure 34. Schematic: Learning-rate scheduling intuition. On a smooth objective (left), large initial steps quickly cover ground and roughly align prototypes, while a decaying step-size refines the solution near convergence. Right: common exponential and multiplicative decays used in SOM training.

### `EPUB/media/file34.png`
- Size: 4082×1557 (94792 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.007750, edge=0.0075, white=0.957, border_nonwhite=0.000
- Ref: `fig:lec5-mds-projection` in `EPUB/text/ch013.xhtml`
- Caption: Figure 35. Schematic: Classical MDS intuition. Projecting a cube onto a plane via an orthogonal map yields a square (left), whereas an oblique projection along a body diagonal produces a hexagon (right). The local adjacency of vertices is preserved even though metric structure is distorted.

### `EPUB/media/file35.png`
- Size: 3661×2131 (193269 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.009830, edge=0.0092, white=0.952, border_nonwhite=0.000
- Ref: `fig:lec5-gaussian-neighborhood` in `EPUB/text/ch013.xhtml`
- Caption: Figure 36. Schematic: Gaussian neighborhood weights in SOM training. Early iterations use a broad kernel so many neighbors adapt; later iterations shrink the neighborhood width sigma(t) so only units near the BMU update.

### `EPUB/media/file36.png`
- Size: 4588×2414 (239699 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.008224, edge=0.0098, white=0.944, border_nonwhite=0.000
- Ref: `fig:lec5-bias-variance` in `EPUB/text/ch013.xhtml`
- Caption: Figure 37. Schematic: Bias–variance trade-off when sweeping SOM capacity (number of units or kernel width). The optimum appears near the knee where bias and variance intersect.

### `EPUB/media/file37.png`
- Size: 4670×2284 (482766 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.007130, edge=0.0063, white=0.857, border_nonwhite=0.000
- Ref: `fig:lec5-regularization` in `EPUB/text/ch013.xhtml`
- Caption: Figure 38. Schematic: Regularization smooths the loss surface. Coupling neighboring prototypes (right) yields wider, flatter basins than the jagged unregularized landscape (left).

### `EPUB/media/file38.png`
- Size: 4306×2166 (326546 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.008967, edge=0.0108, white=0.888, border_nonwhite=0.000
- Ref: `fig:lec5-crossentropy` in `EPUB/text/ch013.xhtml`
- Caption: Figure 39. Schematic: Quantization error combined with an entropy-style regularizer (modern SOM variant; for example, a negative sum of p log p over unit usage). Valleys arise when prototypes cover the space evenly; ridges highlight collapse or poor topological preservation.

### `EPUB/media/file39.png`
- Size: 4621×2398 (201289 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.008114, edge=0.0089, white=0.946, border_nonwhite=0.000
- Ref: `fig:lec5-early-stopping` in `EPUB/text/ch013.xhtml`
- Caption: Figure 40. Schematic: Validation curves used to identify an early-stopping knee. When both quantization and topographic errors flatten (shaded band), further training risks map drift.

### `EPUB/media/file4.png`
- Size: 5581×1974 (255097 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.009613, edge=0.0105, white=0.944, border_nonwhite=0.000
- Ref: `fig:lec1_lasso_path` in `EPUB/text/ch007.xhtml`
- Caption: Figure 5. Schematic: A typical lasso path as the regularization strength increases. Coefficients shrink, and some become exactly zero, yielding sparse models.

### `EPUB/media/file40.png`
- Size: 3870×2268 (113871 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.008091, edge=0.0093, white=0.406, border_nonwhite=0.000
- Ref: `fig:lec5-softmax-regions` in `EPUB/text/ch013.xhtml`
- Caption: Figure 41. Schematic: Voronoi-like regions induced by SOM prototypes (left) and the corresponding softmax confidence after shrinking the neighborhood kernel (right). Softer updates blur the decision frontiers and reduce jagged mappings between adjacent neurons.

### `EPUB/media/file41.png`
- Size: 5740×2399 (247577 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.003984, edge=0.0060, white=0.817, border_nonwhite=0.000
- Ref: `fig:lec5-som-lattice-umatrix` in `EPUB/text/ch013.xhtml`
- Caption: Figure 42. Schematic: Left: a 5-by-5 SOM lattice with best matching unit (blue) and neighbors within the Gaussian-kernel radius (green). Right: a toy U-Matrix (colormap chosen to remain interpretable in grayscale) showing average distances between neighboring codebook vectors; higher distances indicate likely cluster boundaries.

### `EPUB/media/file42.png`
- Size: 4364×1480 (232797 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.021325, edge=0.0240, white=0.497, border_nonwhite=0.000
- Ref: `fig:lec5-som-component-planes` in `EPUB/text/ch013.xhtml`
- Caption: Figure 43. Schematic: Component planes for three features on a trained SOM (toy data). Each plane maps one feature’s value across the map; aligned bright/dark regions across planes reveal correlated features, complementing the U-Matrix in Figure 42 . Interpret brightness comparatively within a plane rather than as an absolute calibrated scale.

### `EPUB/media/file43.png`
- Size: 2401×1903 (185733 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.012518, edge=0.0133, white=0.911, border_nonwhite=0.000
- Ref: `fig:som_neighborhood` in `EPUB/text/ch013.xhtml`
- Caption: Figure 44. Schematic: SOM lattice with the best-matching unit (BMU) highlighted in blue and a dashed neighborhood radius indicating which prototype vectors receive cooperative updates.

### `EPUB/media/file44.png`
- Size: 4021×1806 (141066 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006019, edge=0.0091, white=0.955, border_nonwhite=0.000
- Ref: `fig:hopfield-energy-descent` in `EPUB/text/ch014.xhtml`
- Caption: Figure 45. Schematic: Hopfield energy decreases monotonically under asynchronous updates. Starting from a noisy probe state s(0), successive single-neuron flips move downhill until the stored memory s(2) is recovered.

### `EPUB/media/file45.png`
- Size: 4800×3120 (247398 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.007770, edge=0.0077, white=0.924, border_nonwhite=0.000
- Ref: `fig:lec6-dropout` in `EPUB/text/ch015.xhtml`
- Caption: Figure 46. Schematic: Dropout effect on training/validation curves. Compared to a no-dropout baseline, validation curves flatten and generalization improves.

### `EPUB/media/file46.png`
- Size: 4512×2007 (235124 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.010969, edge=0.0109, white=0.944, border_nonwhite=0.000
- Ref: `fig:lec6-bn` in `EPUB/text/ch015.xhtml`
- Caption: Figure 47. Schematic: Batch normalization transforms per-channel activations toward zero mean and unit variance prior to the learned affine re-scaling, stabilizing training.

### `EPUB/media/file47.png`
- Size: 4050×2286 (163639 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.007281, edge=0.0074, white=0.957, border_nonwhite=0.000
- Ref: `fig:lec6-optimizers` in `EPUB/text/ch015.xhtml`
- Caption: Figure 48. Schematic: Representative training curves for SGD with momentum versus Adam on the same CNN.

### `EPUB/media/file48.png`
- Size: 4340×2233 (172505 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.009865, edge=0.0088, white=0.946, border_nonwhite=0.000
- Ref: `fig:lec7-boundaries` in `EPUB/text/ch016.xhtml`
- Caption: Figure 49. Schematic: Decision boundaries for logistic regression (left) versus a shallow MLP (right). Linear models carve a single hyperplane, whereas hidden units can warp the boundary to follow non-convex manifolds such as the moons dataset.

### `EPUB/media/file49.png`
- Size: 4883×2158 (281205 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.012336, edge=0.0118, white=0.943, border_nonwhite=0.000
- Ref: `fig:lec7-loss-hyperparams` in `EPUB/text/ch016.xhtml`
- Caption: Figure 50. Schematic: Binary cross-entropy geometry (left), effect of learning-rate schedules on loss (middle), and the typical training/validation divergence that motivates early stopping (right).

### `EPUB/media/file5.png`
- Size: 4224×1909 (191421 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.008667, edge=0.0087, white=0.951, border_nonwhite=0.000
- Ref: `fig:lec1_class_losses` in `EPUB/text/ch007.xhtml`
- Caption: Figure 6. Schematic: Classification losses as functions of the signed margin z.

### `EPUB/media/file50.png`
- Size: 4950×1893 (143614 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.008316, edge=0.0082, white=0.960, border_nonwhite=0.000
- Ref: `fig:lec7-rnn-unrolled` in `EPUB/text/ch016.xhtml`
- Caption: Figure 51. Schematic: Unrolling an RNN reveals repeated application of the same parameters across time steps. This view motivates backpropagation through time (BPTT), which accumulates gradients through every copy before updating the shared weights.

### `EPUB/media/file51.png`
- Size: 4427×1872 (169738 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.008419, edge=0.0107, white=0.953, border_nonwhite=0.000
- Ref: `fig:lec7-bptt` in `EPUB/text/ch016.xhtml`
- Caption: Figure 52. Schematic: Backpropagation through time (BPTT): unrolled forward pass (black) and backward gradients (pink) through time.

### `EPUB/media/file52.png`
- Size: 4800×3120 (231418 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.007396, edge=0.0131, white=0.794, border_nonwhite=0.000
- Ref: `fig:lec7-vanishing` in `EPUB/text/ch016.xhtml`
- Caption: Figure 53. Schematic: Vanishing (blue) versus exploding (orange) gradients on a log scale. The gray strip highlights the stability band; the inset reminds readers that repeated Jacobian products either shrink gradients (thin blue arrows) or amplify them (thick orange arrows).

### `EPUB/media/file53.png`
- Size: 4982×1737 (235847 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.011702, edge=0.0155, white=0.915, border_nonwhite=0.000
- Ref: `fig:lec7-clipping` in `EPUB/text/ch016.xhtml`
- Caption: Figure 54. Schematic: Gradient norms (left) explode without clipping (orange) but remain bounded when the global norm is clipped at tau (green). Training loss (right) stabilizes as a result.

### `EPUB/media/file54.png`
- Size: 8535×2320 (223735 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.006139, edge=0.0053, white=0.814, border_nonwhite=0.000
- Ref: `fig:lec7-teacher-forcing` in `EPUB/text/ch016.xhtml`
- Caption: Figure 55. Schematic: Teacher forcing vs. inference in a sequence-to-sequence decoder. Gold arrows show supervised targets; orange arrows highlight autoregressive feedback that motivates scheduled sampling.

### `EPUB/media/file55.png`
- Size: 7454×4641 (405762 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.005049, edge=0.0037, white=0.836, border_nonwhite=0.000
- Ref: `fig:lec7-lstm` in `EPUB/text/ch016.xhtml`
- Caption: Figure 56. Schematic: Long Short-Term Memory (LSTM) cell .

### `EPUB/media/file56.png`
- Size: 9343×3416 (400176 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.005310, edge=0.0044, white=0.905, border_nonwhite=0.000
- Ref: `fig:lec7-gru` in `EPUB/text/ch016.xhtml`
- Caption: Figure 57. Schematic: Gated Recurrent Unit (GRU) cell .

### `EPUB/media/file57.png`
- Size: 4923×3181 (299546 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.009695, edge=0.0093, white=0.437, border_nonwhite=0.000
- Ref: `fig:lec7-attention` in `EPUB/text/ch016.xhtml`
- Caption: Figure 58. Schematic: Attention heatmap for a translation model. Rows are target tokens (decoder steps) and columns are source tokens (encoder positions). Each cell is an attention weight; the dot in each row marks the source position receiving the most attention.

### `EPUB/media/file59.png`
- Size: 6811×3177 (482387 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.004210, edge=0.0125, white=0.732, border_nonwhite=0.000
- Ref: `fig:lec13_transformer_block` in `EPUB/text/ch017.xhtml`
- Caption: Figure 60. Schematic: Reference schematic for the Transformer. Left: scaled dot-product attention. Center: multi-head concatenation with an output projection. Right: pre-LN encoder block combining attention, FFN, and residual connections; a post-LN variant simply moves each LayerNorm after its residual add (dotted alternative, not shown).

### `EPUB/media/file6.png`
- Size: 4224×1880 (205365 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.008813, edge=0.0094, white=0.947, border_nonwhite=0.000
- Ref: `fig:lec1_reg_losses` in `EPUB/text/ch007.xhtml`
- Caption: Figure 7. Schematic: Regression losses versus prediction error. The Huber loss transitions from quadratic to linear to reduce sensitivity to outliers.

### `EPUB/media/file60.png`
- Size: 7781×2120 (326598 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.003888, edge=0.0083, white=0.330, border_nonwhite=0.000
- Ref: `fig:lec13_micro_figures` in `EPUB/text/ch017.xhtml`
- Caption: Figure 61. Schematic: Transformer micro-views. Left: positional encodings (sinusoidal/rotary) add order information. Center: KV cache stores past keys/values so decoding a new token reuses prior context. Right: LoRA inserts low-rank adapters (B A) on top of a frozen weight matrix W for parameter-efficient tuning.

### `EPUB/media/file61.png`
- Size: 4840×1932 (184471 bytes)
- Risk score: 0.0
- Flags: (none)
- Metrics: lap_var=0.012343, edge=0.0116, white=0.434, border_nonwhite=0.000
- Ref: `fig:lec13-masks` in `EPUB/text/ch017.xhtml`
- Caption: Figure 62. Schematic: Attention masks visualized as heatmaps (queries on rows, keys on columns). Left: padding mask zeroes attention into padded positions of a shorter sequence in a packed batch. Right: causal mask enforces autoregressive flow by blocking attention to future tokens.

## Figures softer than PDF (from QC bundle)

- None detected by the current sharpness regression heuristic.

## Suggested fixes (global)

- Prefer PDF→PNG rasterization at high DPI for plots/diagrams when a `.pdf` exists.
- Keep TikZ extracted figures at high DPI (already enabled) and consider increasing figure physical size for very thin diagrams.
- Ensure images referenced by `\includegraphics{...png}` prefer sibling `.pdf` sources when available.

