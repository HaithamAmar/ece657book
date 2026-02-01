# High-Priority QA/Polish Plan (Ch.1–19)

This file tracks the concrete edits to apply before finalizing the book. Items are grouped by theme and chapter, with boxes you can tick as they’re completed.

## Notation & Conventions
- [x] Unify error-symbol: use `\delta^{(l)}` for layerwise error signals everywhere (figures, pseudocode, text). Reserve `∆` for finite differences only.
- [x] Embeddings: standardize row-embedding convention `E ∈ ℝ^{|V|×d}`, lookups via `e = E^\top x`, and output matrix name `W_{out}` (remove lingering `Ex`, `W'`, `Who`, `WO` variants).
- [x] Column-vector reminder: reiterate the column-major shape note near the start of CNN/RNN chapters (Ch.11, Ch.12) to avoid row/col confusion.
- [x] Fuzzy trilogy defaults: add one boxed “Operator defaults used in Ch.16–18” (∧=min, ∨=max, complement 1−µ; De Morgan on standard complement) and reference it in 17/18 instead of restating.

## Numeric Clarifications
- [x] Fuzzy centroid example (Ch.18 thermostat): recompute exact centroid for truncated Medium (α=0.3) and High (α=2/15 ≈0.133) triangles; harmonize text/figure to the numeric result (≈0.58–0.60) and state grid resolution used (e.g., 10k trapezoidal points).
- [x] GA toy (Ch.19): add one small table: initial x values → f(x); selected parents; one crossover example; one mutation; new x values → f(x), mirroring the SOM numeric snippet style.

## Figures (print/accessibility/high impact)
- [x] Fig. 6 learning curves: add distinct markers/linestyles for grayscale.
- [x] Fig. 7 double descent: annotate log–log axes (e.g., “parameters (log10)”), darken dashed scaling trend; add markers for grayscale.
- [x] Fig. 13 GD trajectory: add arrowheads on the path to show direction.
- [x] Fig. 16 logistic boundary: add probability colorbar label “π(x)”.
- [x] Fig. 20/21/22 computational graphs: bump font size for Z^(l), A^(l); ensure clear cache/error labels.
- [x] Fig. 28 RBF XOR: add axis ticks (0.0, 0.5, 1.0) and colorbar ticks matching output range.
- [x] Fig. 34 SOM objective: add parenthetical in caption “(e.g., −∑ p log p over unit usage)” to clarify entropy-style term.
- [x] Fig. 37–38 SOM: add note for grayscale “bright = large distance”; ensure colorbar present on U-matrix.
- [x] Fig. 48–50 RNN: label clipping threshold τ on plots where relevant.
- [x] Fig. 53 attention heatmap: add token labels on axes (one example row/col) and ensure colorbar ticks readable.
- [x] Fig. 55 transformer block: retain “pre-LN”; optionally dotted alternative for post-LN.
- [x] Fig. 57 masks: add “queries on rows, keys on columns” inside figure.
- [x] Fig. 58 analogy: add note “2D PCA projection; directions approximate.”
- [x] Heatmaps/lines palette: use color-blind-safe scheme for attention, U-matrix/component planes, PR/ROC; add markers/linestyles for grayscale.

## Fuzzy Trilogy Specifics
- [x] Remove/replace ratio-based inclusion `incl(A,B)=inf µA/µB` (0/0=1) in §16.23; keep implicator-based definition in §16.25.
- [x] Involution statement (§16.15): fix to `C(C(µ_A(x))) = µ_A(x)` (or µĀ̄ = µA) with standard complement.
- [x] Algebraic sum (§16.12): label S_sum(x,y)=x+y−xy and note membership ≤1.
- [x] Composition: consider adding one-line max–product variant alongside max–min pseudocode.
- [x] Add typical grid sizes in §17.8 “Computation and discretisation tips” (e.g., 200–500 points/axis).

## Hopfield / Attention / Modern Notes
- [x] Hopfield: add a 1–2 row table showing single flips with ∆E to illustrate monotone descent; add one line linking softmax energy to `log ∑ exp(β s^T m_μ)` (β inverse temperature) to clarify modern Hopfield ≈ attention.

## Evolutionary Computing (Ch.19)
- [x] Add “defaults that work” box: DE (F ∈ [0.5,0.8], Cr ∈ [0.7,0.9], pop ≈10–20×D) and CMA-ES (λ≈4+⌊3 ln D⌋, σ0≈0.3×range).
- [x] Consider a tiny numeric table for GA as noted above.

## Copyedit / Production
- [ ] Pick US vs UK spelling and harmonize (normalization/behavior/center).
- [ ] Use non-breaking hyphens for cross-entropy, early-stopping, t-/s-norm, mini-batch.
- [ ] Equation punctuation: end sentences with periods where appropriate.
- [ ] Cross-refs: replace vague ranges (“Ch. 14–18”) with section pointers where useful (e.g., “see §18.4”).
- [x] Symbols overload: add one-liner that µ denotes membership in fuzzy chapters vs mean elsewhere; σ is sigmoid vs std. dev., resolved by context/arguments.

## Optional (not required unless time permits)
- [ ] Add List of Algorithms and back-of-book index.
- [ ] Add repo links to code that regenerates key figures (learning curves, ROC/PR, GD path, attention, SOM, fuzzy centroid, GA).
- [ ] Add brief SVM bridge or 2-D conv/pooling example (appendix/box).

Status: To be filled as items are completed. This file is the source of truth for the remaining polish passes. 
