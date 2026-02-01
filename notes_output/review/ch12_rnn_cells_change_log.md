# Chapter 12 (RNN): LSTM/GRU Cell Figure Cleanup

## Scope
- Source file: `notes_output/lecture_7.tex`
- Figures:
  - Fig. 51 (`fig:lec7-lstm`) — LSTM cell
  - Fig. 52 (`fig:lec7-gru`) — GRU cell

## What was wrong (visual/diagrammatic)
- Several wires were routed through/along other nodes or along the same “bus” region, creating **apparent false connections** (it looked like blocks were connected when they weren’t).
- In the LSTM figure, the \(c_t\rightarrow\tanh(\cdot)\) route entered the \(\tanh\) block from the left while the block itself displayed “tanh” with a leftward arrow, producing a **visually confusing, back-pointing signal flow**.
- In the GRU figure, the \(z_t\) split (to gate both branches) and the \(1-z_t\) handling created **crossed/overlapping orthogonal routes**, plus the top routing ran into the small grey legend text.

## What changed
- **LSTM (Fig. 51):** re-routed the \(c_t\rightarrow\tanh(\cdot)\) wire to enter the \(\tanh\) block from above, avoiding the “backwards-looking” arrow impression.
- **GRU (Fig. 52):** re-laid out the gates and re-routed wires so no segment passes through node interiors; replaced the explicit `1-z_t` block with clear branch labels on the corresponding gating wires; moved the legend text to avoid overlap.

## Build + verification
- Clean build output directory (kept consistent): `notes_output/build/`
- PDF: `notes_output/build/ece657_notes.pdf`
- Rendered pages (250 DPI): `notes_output/build/ch12_zoom/`

## Screenshots (before/after)
- LSTM
  - Before: `screenshots/ch12_rnn_cells/fig51_lstm_before.png`
  - After: `screenshots/ch12_rnn_cells/fig51_lstm_after.png`
- GRU
  - Before: `screenshots/ch12_rnn_cells/fig52_gru_before.png`
  - After: `screenshots/ch12_rnn_cells/fig52_gru_after.png`

## Screenshots (v2)
- LSTM
  - Before: `screenshots/ch12_rnn_cells/fig51_lstm_before_v2.png`
  - After: `screenshots/ch12_rnn_cells/fig51_lstm_after_v2.png`
- GRU
  - Before: `screenshots/ch12_rnn_cells/fig52_gru_before_v2.png`
  - After: `screenshots/ch12_rnn_cells/fig52_gru_after_v2.png`

## Screenshots (v3)
- LSTM
  - Before: `screenshots/ch12_rnn_cells/fig51_lstm_before_v3.png`
  - After: `screenshots/ch12_rnn_cells/fig51_lstm_after_v3.png`
- GRU
  - Before: `screenshots/ch12_rnn_cells/fig52_gru_before_v3.png`
  - After: `screenshots/ch12_rnn_cells/fig52_gru_after_v3.png`

## Screenshots (v4)
- Before (combined page): `screenshots/ch12_rnn_cells/fig51_52_before_v4.png` (see separate `fig51_lstm_before_v4.png`, `fig52_gru_before_v4.png`)
- After (combined page): `screenshots/ch12_rnn_cells/fig51_52_after_v4.png`

## Screenshots (v5+)
- v5 (combined page): `screenshots/ch12_rnn_cells/fig51_52_after_v5.png` (before: `screenshots/ch12_rnn_cells/fig51_52_before_v5.png`)
- v6 (combined page): `screenshots/ch12_rnn_cells/fig51_52_after_v6.png` (before: `screenshots/ch12_rnn_cells/fig51_52_before_v6.png`)
- v7 (combined page): `screenshots/ch12_rnn_cells/fig51_52_after_v7.png` (before: `screenshots/ch12_rnn_cells/fig51_52_before_v7.png`)
- v8 (combined page): `screenshots/ch12_rnn_cells/fig51_52_after_v8.png` (before: `screenshots/ch12_rnn_cells/fig51_52_before_v8.png`)
- v9 (combined page): `screenshots/ch12_rnn_cells/fig51_52_after_v9.png` (before: `screenshots/ch12_rnn_cells/fig51_52_before_v9.png`)
- v10 (combined page): `screenshots/ch12_rnn_cells/fig51_52_after_v10.png` (before: `screenshots/ch12_rnn_cells/fig51_52_before_v10.png`)
- v11 (combined page): `screenshots/ch12_rnn_cells/fig51_52_after_v11.png` (before: `screenshots/ch12_rnn_cells/fig51_52_before_v11.png`)
- v12 (combined page): `screenshots/ch12_rnn_cells/fig51_52_after_v12.png` (before: `screenshots/ch12_rnn_cells/fig51_52_before_v12.png`)
