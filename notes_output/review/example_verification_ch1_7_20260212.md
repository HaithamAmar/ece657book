# Example Verification Run (Chapters 1–7)

Date: 2026-02-12  
Method: deterministic numeric checks using `python3` (`numpy`) on representative chapter examples.

## Executed checks

1. **Chapter 1 (`lecture_1_intro.tex`)**  
   Transitivity statement check (`If A=B and B=C then A=C`) over integer triples in `[-3,3]`.
   - Triples tested: `343`
   - Premise-true cases: `7`
   - Violations: `0`

2. **Chapter 2 (`lecture_2_part_i.tex`)**  
   Integral worked example consistency:
   - Verified \( \frac{d}{dx}F(x)=4(1-x^2)^{-5/2} \) numerically on \(|x|<1\)
   - Max absolute derivative error: `6.79e-09`
   - Verified reduction-path primitive \( \tan y + \frac13\tan^3 y \) differentiates to \( \sec^4 y \)
   - Max absolute derivative error: `2.33e-09`

3. **Chapter 3 (`lecture_supervised.tex`)**  
   Linear-regression objective checks:
   - Gradient formula \(X^\top(X\beta-y)\) vs finite differences: max abs diff `8.32e-09`
   - Normal-equation residual \(||X^\top(X\hat\beta-y)||_2\): `1.09e-14`

4. **Chapter 4 (`lecture_2_part_ii.tex`)**  
   Toy boundary check for plotted coordinates in `fig:lec1_bayes`:
   - Boundary \(x_1=0.15\)
   - Misclassified class-\(\mathcal C_0\) points: `0`
   - Misclassified class-\(\mathcal C_1\) points: `0`

5. **Chapter 5 (`lecture_3_part_i.tex`)**  
   MP neuron logic-gate example:
   - AND (\(\theta=2\)): `[0,0,0,1]` (match)
   - OR (\(\theta=1\)): `[0,1,1,1]` (match)

6. **Chapter 6 (`lecture_3_part_ii.tex`)**  
   Two-neuron gradient sanity check:
   - \(p_1=0.6,\; y_1=0.645656,\; y_2=0.656031,\; P=0.059157\)
   - \(\delta_2=-0.077618,\; \delta_1=-0.017758\)
   - \(\nabla_{\mathbf{w}_1}P=[-0.017758,\,+0.017758]\)
   - \(\nabla_{w_2}P=-0.050115\)

7. **Chapter 7 (`lecture_4_part_i.tex`)**  
   Backprop brief numerical check (2–2–1, sigmoid + CE):
   - \(z^{(1)}=[-0.56,-0.62],\; a^{(1)}=[0.363547,0.349781]\)
   - \(z^{(2)}=0.164571,\; a^{(2)}=0.541050,\; \mathcal L=-\log a^{(2)}=0.614243\)
   - \(\delta^{(2)}=-0.458950,\; \delta^{(1)}=[-0.074335,0.041752]\)
   - \(\nabla_{W^{(2)}}=[-0.166850,-0.160532]\)
   - \(\nabla_{W^{(1)}}=\begin{bmatrix}-0.044601 & 0.025051\\0.089201 & -0.050103\end{bmatrix}\)

## Repro command (as run)

`python3` one-shot script (in shell) computing all seven checks with `numpy`; output values copied into this report and the audit tracker.
