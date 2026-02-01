# Figure Fixes Change Log

This log records figure/layout fixes applied in the LaTeX sources along with the rendered-page screenshots captured from the compiled PDF.

## 2025-12-19 — Figures 38, 46, 52 (layout + print robustness)

### Figure 46 — RNN unrolling schematic
- Source: `notes_output/lecture_7.tex` (`\label{fig:lec7-rnn-unrolled}`)
- Changes:
  - Anchor the brace to node corners (no hard-coded coordinates).
  - Combine the two annotations into one clearer label on the brace.
  - Reduce redundant recurrence labeling (keep one `\mathbf{W}_{hh}` label).
- Render proof:
  - PDF page: 232
  - Screenshot: `notes_output/review/screenshots/fig_fixes_2025-12-19/p232_fig46.png`

### Figure 52 — GRU cell schematic
- Source: `notes_output/lecture_7.tex` (`\label{fig:lec7-gru}`)
- Changes:
  - Increase vertical lane spacing (`h_{t-1}` / `x_t` paths) to reduce near-tangent wires and accidental “connections”.
- Render proof:
  - PDF page: 239
  - Screenshot: `notes_output/review/screenshots/fig_fixes_2025-12-19/p239_fig52.png`

### Figure 38 — SOM component planes
- Source: `notes_output/lecture_5_part_i.tex` (`\label{fig:lec5-som-component-planes}`)
- Changes:
  - Remove per-panel colorbars (they were shrinking plots and causing tick overlap).
  - Switch to a grayscale colormap with a fixed global scale (`0` to `0.7`) for print robustness.
  - Increase per-cell numeric label readability.
- Render proof:
  - PDF page: 181
  - Screenshot: `notes_output/review/screenshots/fig_fixes_2025-12-19/p181_fig38.png`

## 2025-12-19 — Figures 28, 51–52, 38 (layout stability + print polish)

### Figures 51–52 — Keep LSTM/GRU cells together
- Source: `notes_output/lecture_7.tex` (`\label{fig:lec7-lstm}`, `\label{fig:lec7-gru}`)
- Changes:
  - Force top placement for both floats (`[!t]`) and insert a `\FloatBarrier` after Figure 52 so the following non-float tcolorboxes cannot jump ahead of a deferred figure.
- Render proof:
  - PDF pages: 239–240
  - Screenshots: `notes_output/review/screenshots/fig_fixes_2025-12-19_v16/p-239.png`, `notes_output/review/screenshots/fig_fixes_2025-12-19_v16/p-240.png`

### Figure 28 — RBFN XOR decision boundary (legend + contrast)
- Source: `notes_output/lecture_4_part_ii.tex` (`\label{fig:rbf_boundary}`)
- Changes:
  - Remove legend (it could occlude corner points at some scales) and encode classes via marker shapes in the caption.
  - Increase region contrast in grayscale and soften gridlines for print.
- Render proof:
  - PDF page: 155
  - Screenshot: `notes_output/review/screenshots/fig_fixes_2025-12-19_v16/p155-155.png`

### Figure 38 — SOM component planes (readability at print size)
- Source: `notes_output/lecture_5_part_i.tex` (`\label{fig:lec5-som-component-planes}`)
- Changes:
  - Increase subplot sizes slightly and remove per-cell numeric overlays (too small at 7×10 trim).
- Render proof:
  - PDF page: 182
  - Screenshot: `notes_output/review/screenshots/fig_fixes_2025-12-19_v16/p182-182.png`
