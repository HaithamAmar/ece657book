# Example Integrity Audit

This file tracks worked-example verification. Each entry lists a specific example and its verification status.

Status legend: `Verified` / `Pending` / `Needs Fix`.

## lecture_1_intro.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_1_intro.tex:42` | Formal reasoning example: `If A = B and B = C, then A = C.` | Deterministic truth-table check on integer triples (343 cases): 0 violations when premises hold. |
| Pending | `lecture_1_intro.tex:151` | \item \textbf{Problem definition.} State the task in operational terms. Example: ``Detect stop signs quickly enough to enable safe braking.'' The definition should tell us which of the three value-centric roles dominates (here: understanding the present, plus explaining why braking events occur). |  |
| Pending | `lecture_1_intro.tex:169` | \paragraph{Example: Autonomous Vehicle} |  |
| Pending | `lecture_1_intro.tex:230` | \paragraph{Example: Swarm Intelligence} |  |

## lecture_2_part_i.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Pending | `lecture_2_part_i.tex:67` | \paragraph{Example: Applying Safe Transformations} |  |
| Pending | `lecture_2_part_i.tex:96` | \paragraph{Example: Trigonometric Heuristics} |  |
| Verified | `lecture_2_part_i.tex:239` | \subsection{Example: Solving an Integral via Transformation Trees} | Numerical derivative check validates \(F'(x)=4(1-x^2)^{-5/2}\) on \(|x|<1\) (max abs err \(6.79\times10^{-9}\)); reduction path \(\frac{d}{dy}\left[\tan y+\frac13\tan^3y\right]=\sec^4y\) (max abs err \(2.33\times10^{-9}\)). |
| Pending | `lecture_2_part_i.tex:437` | \paragraph{Example:} For the integral problem, the root node is the original integral. From there, we branch into applying different substitutions or algebraic manipulations, such as |  |
| Pending | `lecture_2_part_i.tex:549` | \paragraph{Worked example: Beta template vs.\ numeric fallback} |  |

## lecture_supervised.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_supervised.tex:551` | \subsection{Linear regression: a first full case study} | Verified objective gradient and closed form: \(\nabla_\beta L=X^\top(X\beta-y)\) matches finite differences (max abs diff \(8.32\times10^{-9}\)); normal equations residual \(\|X^\top(X\hat\beta-y)\|_2=1.09\times10^{-14}\). |

## lecture_2_part_ii.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_2_part_ii.tex:24` | \begin{tcolorbox}[summarybox, title={Worked example: a toy decision boundary}] | Verified against plotted coordinates in \Cref{fig:lec1_bayes}: vertical boundary \(x_1=0.15\) separates all 30 listed points (0/30 misclassified). |

## lecture_3_part_i.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_3_part_i.tex:286` | \paragraph{Example: AND and OR gates} | MP-neuron truth tables verified: with \(w_1=w_2=1\), \(\theta=2\) yields AND \([0,0,0,1]\); \(\theta=1\) yields OR \([0,1,1,1]\). |

## lecture_3_part_ii.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_3_part_ii.tex:330` | \begin{tcolorbox}[summarybox, title={Worked example: one numerical gradient step (sanity check)}] | Recomputed values match rounded text: \(p_1=0.6,\; y_1\approx0.6457,\; y_2\approx0.6560,\; P\approx0.05916,\; \delta_2\approx-0.07762,\; \delta_1\approx-0.01776,\; \nabla_{w_2}P\approx-0.05011\). |

## lecture_4_part_i.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_4_part_i.tex:454` | \subsection{Backpropagation Algorithm: Brief Numerical Check} | Full 2--2--1 CE pass verified numerically: \(z^{(1)}=[-0.56,-0.62],\; a^{(2)}\approx0.54105,\; \mathcal L\approx0.61424,\; \delta^{(2)}\approx-0.45895,\; \delta^{(1)}\approx[-0.07433,0.04175]\), with gradients matching listed values to rounding. |
| Pending | `lecture_4_part_i.tex:819` | \paragraph{Example Execution} |  |

## lecture_4_part_ii.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_4_part_ii.tex:237` | \paragraph{Example Setup:} | RBF mapping check with \(\sigma^2=1,\; \mathbf v_1=(0,0),\mathbf v_2=(1,1)\): \((0,0)\mapsto(1,e^{-1})\) and \((1,1)\mapsto(e^{-1},1)\), matching text exactly. |

## lecture_5_part_i.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Pending | `lecture_5_part_i.tex:96` | \paragraph{Example:} Consider three types of geometric shapes (triangles, circles, and squares) represented only by their feature vectors without labels. Clustering aims to group these shapes into clusters corresponding to their types based on similarity in features, even though the network does not know the labels. |  |
| Pending | `lecture_5_part_i.tex:128` | \paragraph{Example:} Consider a three-dimensional cube. Depending on its orientation, a linear projection (matrix multiplication by \(P: \mathbb{R}^3 \rightarrow \mathbb{R}^2\) with matrix representation in \(\mathbb{R}^{2 \times 3}\)) onto a two-dimensional plane can look like different shapes: a square arises from an orthogonal projection onto a face, whereas a hexagon appears under an oblique projection along a body-diagonal. This highlights that while the combinatorial adjacency (which vertices are connected) is preserved under such a projection, Euclidean lengths and angles are inevitably distorted. \Cref{fig:lec5-mds-projection} illustrates these two views. |  |
| Pending | `lecture_5_part_i.tex:339` | \subsection{Example: SOM with a \texorpdfstring{\(3 \times 3\)}{3x3} Output Map and 4-Dimensional Input} |  |
| Verified | `lecture_5_part_i.tex:476` | \subsection{Numerical Example of Competitive Learning} | Verified schedule and update mechanics: \(\alpha(t)=0.3\cdot0.5^t\) is positive/decreasing; WTA update remains convex combination \( \mathbf w_c^+ = (1-\alpha)\mathbf w_c+\alpha\mathbf x \) (checked numerically with \(\alpha=0.3\)). |
| Pending | `lecture_5_part_i.tex:1064` | \subsection{Example: Neighborhood Update Illustration} |  |

## lecture_5_part_ii.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_5_part_ii.tex:196` | \subsection{Example: Energy Calculation and State Updates} | Recomputed Hopfield energies match text/table exactly: \(E(1,1,-1)=-5\), \(E(-1,1,-1)=9\), \(E(1,-1,-1)=-3\), \(E(1,1,1)=-1\), so \(\Delta E=[+14,+2,+4]\). |
| Pending | `lecture_5_part_ii.tex:436` | \subsection{Example: Weight Calculation for a Single Pattern} |  |
| Verified | `lecture_5_part_ii.tex:501` | \paragraph{Example: Memory Recovery} | Verified via `notes_output/scripts/verify_hopfield_memory.py`: weight matrix equals \\(1/n\\) outer product with zero diagonal, asynchronous updates from `[-1,-1,1,1]` converge to `[-1,-1,1,-1]` while energy drops from 0 to -1.5. |

## lecture_6.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_6.tex:274` | \paragraph{Example: Activation function derivatives} | Deterministic sweep confirms sigmoid derivative max is \(0.25\) at \(x\approx0\), supporting the \(0.25^L\) vanishing-gradient rule-of-thumb in this section. |

## lecture_7.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_7.tex:947` | \subsubsection{Worked example: sentiment as a many-to-one decision} | Instantiated many-to-one recurrence \( \mathbf h_t=f(\mathbf h_{t-1},\mathbf x_t) \), \( \hat y=\sigma(\mathbf w^\top\mathbf h_T+b) \): computed \(\hat y=0.5698\in(0,1)\), consistent with probability interpretation. |

## lecture_8_part_i.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Pending | `lecture_8_part_i.tex:107` | \paragraph{Example:} The word \emph{pretty} can have different meanings depending on context: |  |
| Pending | `lecture_8_part_i.tex:151` | \paragraph{Example:} Consider the sentence |  |
| Pending | `lecture_8_part_i.tex:376` | \paragraph{Example:} Consider the sentence: |  |
| Verified | `lecture_8_part_i.tex:399` | \paragraph{Tiny worked example (skip-gram with \(k=2\)).} | Verified SGNS gradient signs from objective in \eqref{eq:neg-sample-loss}: positive-pair dot product gets positive push; sampled negative dots get negative pushes (\(\partial L/\partial d_{pos}>0,\; \partial L/\partial d_{neg}<0\)). |
| Pending | `lecture_8_part_i.tex:440` | \paragraph{Example: Co-occurrence Matrix} |  |

## lecture_transformers.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_transformers.tex:258` | \paragraph{Micro attention example (2 tokens, causal mask).} | Recomputed exact attention with \(Q=K=V=I_2,\;d_k=2\): row1 \([1,0]\), row2 \([0.330238,0.669762]\), and output equals weights because \(V=I\), matching derivation. |

## lecture_8_part_ii.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Pending | `lecture_8_part_ii.tex:423` | \paragraph{Example:} Consider two classes: |  |
| Pending | `lecture_8_part_ii.tex:435` | \subsubsection*{Example: Sizes as fuzzy sets} |  |
| Pending | `lecture_8_part_ii.tex:483` | \paragraph{Example: Height Classification} |  |

## lecture_9.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_9.tex:27` | \subsection{Motivating example: designing a membership function from measurements} | Verified: piecewise shoulder yields μ_Cold(-2)=0.5 with breakpoints -4/0. |
| Pending | `lecture_9.tex:57` | \paragraph{Example:} Consider the fuzzy set \textit{Slow Speed} defined over the universe of speeds \( X \subseteq \mathbb{R} \). The membership function \(\mu_{\text{Slow}}(x)\) might assign high membership values to speeds near 20 km/h and gradually decrease as speed increases, reflecting the gradual transition from "slow" to "not slow." |  |
| Pending | `lecture_9.tex:87` | \paragraph{Example:} Suppose \( X = \{1, 2, 3, 4, 5\} \) and the membership function values are: |  |
| Pending | `lecture_9.tex:108` | \paragraph{Example:} Consider a triangular membership function centered at \( c \) with base width \( w \): |  |
| Pending | `lecture_9.tex:183` | \paragraph{Example: Grading System as Fuzzy Sets} |  |
| Pending | `lecture_9.tex:257` | \subsection{Example: Overlapping weight labels}\label{sec:weight-membership} |  |
| Pending | `lecture_9.tex:509` | \subsection{Example: Union and Intersection of Fuzzy Sets} |  |
| Pending | `lecture_9.tex:527` | \paragraph{Example:} Suppose |  |
| Pending | `lecture_9.tex:1051` | \subsection{Worked Example: Mamdani Fuzzy Inference (End-to-End)} |  |

## lecture_10_part_i.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Pending | `lecture_10_part_i.tex:103` | \subsection{Example Setup} |  |
| Pending | `lecture_10_part_i.tex:113` | \paragraph{Example: Mapping via \( y = x^2 \)} |  |
| Pending | `lecture_10_part_i.tex:144` | \begin{tcolorbox}[summarybox, title={Worked example: monotone map (Celsius \(\to\) Fahrenheit)}] |  |
| Pending | `lecture_10_part_i.tex:221` | \textbf{Example:} Compute \(\mu_B(0)\). |  |
| Pending | `lecture_10_part_i.tex:228` | \textbf{Example:} Compute \(\mu_B(1)\). |  |
| Pending | `lecture_10_part_i.tex:449` | \paragraph{Example (continued)} |  |
| Pending | `lecture_10_part_i.tex:611` | \subsection{Example Calculation of Composition} |  |

## lecture_10_part_ii.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Verified | `lecture_10_part_ii.tex:144` | \subsection{Worked example: thermostat inference with numbers} | Verified numerically: u*≈0.577268 with Mamdani min/max, step 1e-4. |

## lecture_11.tex
| Status | Location | Example | Notes |
| --- | --- | --- | --- |
| Pending | `lecture_11.tex:378` | \subsubsection{Example: Binary Encoding of Parameters} |  |
| Pending | `lecture_11.tex:397` | \subsubsection{Example Problem: Minimization with Constraints} |  |
| Pending | `lecture_11.tex:849` | Step & Example bitstrings & Decoded \(x\) & Fitness \(f(x)\) \\ |  |
| Pending | `lecture_11.tex:889` | \subsection{Example: GA for a Constrained Optimization Problem} |  |
| Pending | `lecture_11.tex:1057` | \paragraph{Example: Robot Obstacle Avoidance} |  |
