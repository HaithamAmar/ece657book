# Part II Editorial Review (Draft)

Scope: **Part II** as it appears in `notes_output/book_chapters.tex` after collapsing the former Part III into Part II.

Goal: make Part II read like a single coherent journey where:
- each chapter has a **clear purpose** in the arc,
- within each chapter the internal structure is **linear** (basic → deeper → deeper),
- transitions feel **natural** (no “course logistics” voice; no meta commentary).

## Current composition (as built)

Part II currently includes:

1. Chapter 5: `lecture_3_part_i.tex` — *Introduction to Neural Networks*
2. Chapter 6: `lecture_3_part_ii.tex` — *Multi-Layer Perceptrons: Challenges and Foundations*
3. Chapter 7: `lecture_4_part_i.tex` — *Backpropagation Learning in Multi-Layer Perceptrons*
4. Chapter 8: `lecture_4_part_ii.tex` — *Radial Basis Function Networks (RBFNs)*
5. Chapter 9: `lecture_5_part_i.tex` — *Introduction to Self-Organizing Networks and Unsupervised Learning*
6. Chapter 10: `lecture_5_part_ii.tex` — *Hopfield Networks: Introduction and Context*
7. Chapter 11: `lecture_6.tex` — (CNN chapter; verify title in build output / ToC)
8. Chapter 12: `lecture_7.tex` — (RNN/sequence chapter; verify title)
9. Chapter 13: `lecture_8_part_i.tex` — *Neural Network Applications in Natural Language Processing*
10. Chapter 14: `lecture_transformers.tex` — *Transformers: Attention-Based Sequence Modeling*

## Arc coherence (Part-level)

### What works
- The story naturally escalates: **linear baselines → multilayer representations → training engine → alternative basis functions → unsupervised structure → associative memory → convolution → recurrence → attention/Transformers → NLP application**.

### What currently risks feeling “nonlinear”
- The placement of **RBFNs** (Chapter 8) between backprop and unsupervised chapters can read like a detour unless the chapter endings/introductions explicitly “close the loop” (what it adds, why it sits here).
- **Hopfield** (energy-based) can feel like a second detour unless the transition frames it as a complementary lens on recurrence/representation, not “another model.”
- The NLP chapter is now within Part II; it should open with a short bridge from the sequence material (RNNs) and close by setting up attention/Transformers as the scaling step.

## Chapter-level linearity checklists (editorial)

Below are “shape checks” per chapter: what the chapter should feel like, what to adjust if it doesn’t.

### Chapter 5 — Introduction to Neural Networks
**Desired shape**
- Motivation → neuron model → architecture vocabulary → what training means at a high level → what breaks (capacity, optimization, generalization) → where the next chapter begins.
**Watch-outs**
- Avoid too many historical asides before the reader sees the simplest forward computation.
**Transition target**
- End by motivating why we need multilayer representations and smooth activations (point directly to Chapter 6).

### Chapter 6 — MLPs: smallest trainable network
**Desired shape**
- Smallest network → loss → chain rule gradient → why non-differentiable thresholds block learning → smooth activations → preview of backprop bookkeeping.
**Watch-outs**
- Don’t introduce too many “implementation” details here; keep it conceptual and minimal.
**Transition target**
- End with “scaling this derivation” as the hook into Chapter 7.

### Chapter 7 — Backpropagation
**Desired shape**
- Re-state the goal (efficient gradients) → derive recursion → connect to computation graph + caching → training diagnostics (learning curves, early stopping) → close with practical training policies.
**Watch-outs**
- Avoid jumping to “deep learning tricks” before the recursion is fully established.
**Transition target**
- Move from “gradient-based representations” to “other representation families” (RBFs as an alternate basis; or to convolution as structured basis).

### Chapter 8 — RBFNs
**Desired shape**
- Geometric intuition (local bases) → architecture → training choices (centers/widths/weights) → regularization/model selection → when RBFs beat MLPs and when they don’t.
**Watch-outs**
- If this chapter reads as isolated, add a short “why this belongs here” bridge at the start and a “what it sets up” bridge at the end (unsupervised prototypes + SOM).

### Chapter 9 — SOM / unsupervised competitive learning
**Desired shape**
- Why unlabeled structure matters → prototype learning / competition → SOM mechanics → interpretation (U-matrix/component planes) → failure modes and diagnostics.
**Watch-outs**
- Ensure the chapter explicitly teaches “how to read SOM plots” (otherwise the figures feel ornamental).
**Transition target**
- Bridge to energy-based thinking / associative memory (Hopfield) as a different unsupervised lens.

### Chapter 10 — Hopfield
**Desired shape**
- Energy function idea → dynamics as descent → capacity + spurious minima → relation to modern attention/associative memory framing.
**Watch-outs**
- Keep the narrative aligned with Part II: treat Hopfield as a representation/dynamics story, not as a historical appendix.
**Transition target**
- Use Hopfield to motivate structured architectures (convolution) and sequence memory (RNNs).

### Chapter 11 — CNNs (needs a dedicated pass)
**Goal for this pass**
- Ensure it flows basic → deeper: convolution intuition → receptive fields → pooling → training practicalities → modern CNN usage patterns and failure modes.
**Potential structural improvements (to validate by reading full chapter)**
- Bring “what convolution buys you” before details (weight sharing / inductive bias).
- Keep implementation-level details (padding/stride shapes) grouped and short.

### Chapter 12 — RNNs / sequence modeling (needs a dedicated pass)
**Goal for this pass**
- Make recurrence feel inevitable: why sequence dependence breaks feedforward models → unrolling → BPTT → vanishing/exploding gradients → LSTM/GRU remedies → training policies.
**Potential structural improvements**
- Move “failure modes” (vanishing/exploding) earlier so LSTM/GRU feel like solutions to a pain the reader already felt.

### Chapter 13 — NLP applications
**Desired shape**
- Problem framing → embeddings as representation learning → objectives (CBOW/skip-gram, negative sampling) → evaluation + audits → deployment checklist.
**Transition target**
- Land the reader in Chapter 14 with “why attention scales this” without turning it into a marketing pitch.

### Chapter 14 — Transformers
**Desired shape**
- Attention as a replacement for recurrence bottlenecks → self-attention → positional encoding → training/inference differences → scaling + practical tooling (PEFT) → what it enables downstream.
**Watch-outs**
- Ensure the bridge does not assume the reader just came from embeddings; keep a short “what attention buys you” recap and point back to the NLP chapter when needed.

## Recommendations (next actionable edits)

1. Add/strengthen **end-of-chapter “Where we head next”** bridges for Part II chapters that currently “stop” without a hook.
2. Do a full read of **Chapter 11** and propose a concrete section order (basic → deeper) with minimal cutting/pasting.
3. Do a full read of **Chapter 12** and similarly propose/execute a section order pass.
4. Re-audit Part II ToC after edits to ensure heading hierarchy is meaningful and uncluttered.
