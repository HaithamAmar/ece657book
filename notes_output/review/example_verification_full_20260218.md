# Example Verification Run (All Chapters)

Date: 2026-02-18  
Method: deterministic numeric checks using `python3` (`numpy`) via `notes_output/scripts/validate_math_examples_and_graphs.py --strict`.

## Summary

- Checks run: 18
- Passed: 18
- Failed: 0
- Artifact (latest): `notes_output/artifacts/qc/math_graph_validation_latest.md` + `.json`
- Timestamp in artifact: `2026-02-17T20:42:13.765568`

## Coverage map (chapter file → numeric example verified)

- `lecture_1_intro.tex`: transitivity sanity check (integer triples).
- `lecture_2_part_i.tex`: integral derivative check for the worked example.
- `lecture_2_part_ii.tex`: sigmoid/BCE curve sanity (monotonicity + shape).
- `lecture_supervised.tex`: learning-curve table monotonicity (train/val) and gap.
- `lecture_3_part_i.tex`: MP neuron AND/OR truth tables.
- `lecture_3_part_ii.tex`: two-neuron backprop numeric step (p1/y1/y2, deltas, gradients).
- `lecture_4_part_i.tex`: 2–2–1 backprop numeric check (forward values, loss, deltas, gradients).
- `lecture_4_part_ii.tex`: RBF transform example (g1/g2 at (0,0) and (1,1)).
- `lecture_5_part_i.tex`: SOM tiny numeric update (BMU, neighborhood weight, updated weights).
- `lecture_5_part_ii.tex`: Hopfield 3-neuron energy example (energies + deltas).
- `lecture_6.tex`: batch-norm + optimizer-curve numeric checks.
- `lecture_7.tex`: gradient-clipping figure + attention heatmap consistency.
- `lecture_8_part_i.tex`: SGNS toy loss (signs and numeric value).
- `lecture_8_part_ii.tex`: CNN soft-computing probability example sums to 1.
- `lecture_9.tex`: overlapping membership labels at x=22 (0.6 / 0.4).
- `lecture_10_part_i.tex`: max–min composition + alpha-cut mapping checks.
- `lecture_10_part_ii.tex`: Mamdani centroid check (T=27°C).
- `lecture_11.tex`: roulette selection probabilities + GA population bounds + GA progress figure.
- `lecture_transformers.tex`: micro attention example (Q=K=V=I2, causal mask).

## Repro command

`python3 notes_output/scripts/validate_math_examples_and_graphs.py --strict`
