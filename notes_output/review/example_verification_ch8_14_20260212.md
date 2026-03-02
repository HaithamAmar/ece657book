# Example Verification Run (Chapters 8–14)

Date: 2026-02-12  
Method: deterministic numeric checks using `python3` (`numpy`) on one representative example per chapter.

## Executed checks

1. **Chapter 8 (`lecture_4_part_ii.tex`)**  
   RBF transformation example (\(\sigma^2=1,\mathbf v_1=(0,0),\mathbf v_2=(1,1)\)):
   - \((0,0)\mapsto (g_1,g_2)=(1,e^{-1})\)
   - \((1,1)\mapsto (e^{-1},1)\)
   Both match the text exactly.

2. **Chapter 9 (`lecture_5_part_i.tex`)**  
   Competitive-learning numerical setup consistency:
   - Learning-rate schedule \(\alpha(t)=0.3\cdot0.5^t\): verified positive and strictly decreasing for tested \(t\).
   - WTA update identity verified numerically: \(\mathbf w^+=(1-\alpha)\mathbf w+\alpha\mathbf x\) (convex combination).

3. **Chapter 10 (`lecture_5_part_ii.tex`)**  
   Hopfield energy worked example:
   - \(E(1,1,-1)=-5\)
   - \(E(-1,1,-1)=9\)
   - \(E(1,-1,-1)=-3\)
   - \(E(1,1,1)=-1\)
   - \(\Delta E=[+14,+2,+4]\)  
   Matches text/table exactly.

4. **Chapter 11 (`lecture_6.tex`)**  
   Sigmoid-derivative example:
   - Numerical max of \(\sigma'(x)\) is \(0.2499999994\) at \(x\approx0\), consistent with theoretical max \(0.25\).
   - Confirms the chapter’s vanishing-gradient scaling intuition (\(\sim 0.25^L\)).

5. **Chapter 12 (`lecture_7.tex`)**  
   Many-to-one sentiment equation instantiation:
   - Instantiated \( \mathbf h_t=f(\mathbf h_{t-1},\mathbf x_t)\), \( \hat y=\sigma(\mathbf w^\top \mathbf h_T+b)\) on a toy sequence.
   - Computed \(\hat y=0.56978\), confirming output remains a valid probability in \((0,1)\).

6. **Chapter 13 (`lecture_8_part_i.tex`)**  
   Tiny SGNS worked example (skip-gram, \(k=2\)):
   - Objective \(L=\log\sigma(d_{pos})+\sum_i\log\sigma(-d_{neg,i})\) checked.
   - Derivative signs verified: \(\partial L/\partial d_{pos}>0\), \(\partial L/\partial d_{neg}<0\), matching the text’s “pull positive / push negatives” statement.

7. **Chapter 14 (`lecture_transformers.tex`)**  
   Micro attention example (\(Q=K=V=I_2,\; d_k=2\), causal mask):
   - Attention row 1: \([1,0]\)
   - Attention row 2: \([0.33023845,\,0.66976155]\)
   - Since \(V=I_2\), output equals attention-weight matrix.  
   Matches chapter derivation.

## Repro command (as run)

`python3` one-shot script (in shell) computing all seven checks with `numpy`; output values copied into this report and `/Users/Haitham.Amar/Documents/ece657Book/notes_output/review/example_integrity_audit.md`.
