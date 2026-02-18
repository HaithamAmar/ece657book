# Scientific QA Report

- Source PDF: `notes_output/ece657_notes.pdf`
- Total chunks: 1

## Chunk 1/31
- Character range: 0–22042

```text
Modern Intelligent Systems: A Graduate Companion
  Neural Networks, Fuzzy Logic, and Evolutionary Optimization

                        Haitham Amar

                      First edition, 2026
Modern Intelligent Systems: A Graduate Companion
Neural Networks, Fuzzy Logic, and Evolutionary Optimization

Copyright (c) 2026 Haitham Amar
All rights reserved.

No part of this book may be reproduced or transmitted in any form or by any means,
electronic or mechanical, including photocopying, recording, or any information storage
and retrieval system, without prior written permission of the copyright holder, except
where permitted by law.

This book is provided for educational purposes. The author makes no warranties of any
kind and assumes no responsibility for errors or omissions or for damages resulting from
the use of the information contained herein.

First edition, 2026
Published by Haitham Amar
Typeset in LaTeX.
Modern Intelligent Systems



Preface
Over time, through teaching courses that engage artificial intelligence both
directly—through machine learning and neural networks—and indirectly, at the
level of data collection and system design, a recurring gap became apparent.
While the literature offers many excellent treatments of individual techniques,
it rarely provides a coherent path that guides students from the foundational
notions of intelligence to the most advanced models used today. What is often
missing is a unified narrative that connects intuition, mathematical formulation,
and practical deployment across the diverse tools that constitute intelligent sys-
tems.
    Courses in machine learning tend to emphasize neural networks and deep
learning; others focus on optimization and operations research, from classical
search strategies to genetic algorithms. Each approach is valuable, yet time
constraints and disciplinary boundaries often force a narrowing of scope, sacri-
ficing breadth for depth or vice versa. In one course in particular, a broader
framework emerged—one that treated these methods not as isolated topics, but
as complementary responses to recurring modeling challenges. That framework,
though not originally mine, proved invaluable: it allowed students to situate
linear regression, neural networks, transformers, fuzzy inference systems, and
evolutionary algorithms within a single, coherent perspective on intelligent sys-
tem design. This book is an attempt to make that perspective explicit and
durable.
    This book has evolved into a concise graduate companion that blends the
original chapter voice of ECE 657 with laboratory-style checklists and reflective
prompts. The chapters move from supervised learning foundations to fuzzy
logic and evolutionary computing, mirroring the trajectory of the original course
material while adding connective tissue so that a reader can revisit the material
years later without hunting for missing context.

Origins in ECE 657
In 2019, I was asked to teach ECE 657 at the University of Waterloo. At the time,
the course leaned heavily toward soft computing, and fuzzy inference systems
had constituted a large portion of the material in earlier offerings. Prof. Karray,
who built the course, felt it was time to broaden its scope beyond that single


                                        3
Modern Intelligent Systems


paradigm, and he was generous enough to let me reshape the arc of the course.
    Over the following years, I came to view fuzzy inference systems as one im-
portant piece in a larger mosaic rather than the organizing principle. I iterated
on the syllabus—moving topics, adding and removing chapters, and tightening
mathematical through-lines—toward a narrative that is coherent, broad in cov-
erage, and implementable by an engineer.
    In the first edition (2026), the field is in the era of large language models,
and this book covers them (see Chapters 13 and 14). But it also emphasizes
other ideas and toolkits that may underwrite future breakthroughs in intelligent
systems: careful probabilistic thinking and diagnostics, principled optimization,
sequence modeling beyond any single architecture, and hybrid reasoning ap-
proaches that have repeatedly re-emerged in new forms.
    The material has since been rewritten to stand alone as a book. Any offering-
specific details (schedules, grading, local policies) now live in Appendix C (espe-
cially Using this book in ECE 657 ); readers outside that course can ignore the
appendix entirely.
 Perspective
 This book prioritizes ideas that survived multiple paradigm shifts. It
 emphasizes principles that remain useful even as architectures and tooling
 change.

    For a practical reader’s guide—roadmap, prerequisites, and suggested read-
ing paths—see the final sections of Chapter 1. Notation and reading conventions
are collected up front in Notation and Conventions.
    The result is a self-contained reference for researchers and engineers who want
a rigorous but narrative-friendly treatment of neural networks, soft computing,
and hybrid reasoning systems.




                                        4
Modern Intelligent Systems



Acknowledgments
This book grew out of teaching and revising the ECE 657 material over multiple
offerings. I am grateful to the students whose questions and feedback repeatedly
exposed where explanations were brittle and where the narrative needed better
bridges between intuition, math, and practice.
I also thank colleagues who shared perspectives on how these topics fit together
as an engineering discipline rather than as isolated techniques. Any remaining
errors and omissions are my responsibility.




                                       5
Modern Intelligent Systems                                                 Contents



Contents

Preface                                                                          3

Acknowledgments                                                                  5

Notation and Conventions                                                        30


Part I: Foundations and the ERM toolbox                                         33

1 About This Book                                                               33
  1.1  Historical Foundations of Intelligent Systems . . . . . . . .            33
  1.2  Defining Artificial Intelligence and Intelligent Systems . . .           36
  1.3  Intelligent Systems . . . . . . . . . . . . . . . . . . . . . . .        37
  1.4  Case Study: AI-Enabled Camera as an Intelligent System .                 39
  1.5  Levels and Architectures of Intelligent Systems . . . . . . .            41
  1.6  Intelligent Systems and Intelligent Machines . . . . . . . . .           44
  1.7  Levels, Meta-cognition, and Safety . . . . . . . . . . . . . .           46
  1.8  Audience, Prerequisites, and Scope . . . . . . . . . . . . . .           47
  1.9  Roadmap and Reading Paths . . . . . . . . . . . . . . . . .              48
  1.10 Using and Navigating This Book . . . . . . . . . . . . . . .             49

2 Symbolic Integration and Problem-Solving Strategies                           50
  2.1  Context and Motivation . . . . . . . . . . . . . . . . . . . .           51
  2.2  Problem Decomposition and Transformation . . . . . . . .                 52
  2.3  Limitations of Safe Transformations . . . . . . . . . . . . .            53
  2.4  Heuristic Transformations . . . . . . . . . . . . . . . . . . .          53
  2.5  Summary of the Approach . . . . . . . . . . . . . . . . . . .            55
  2.6  Heuristic Transformations: Revisiting the Integral with 1 − x2           56
  2.7  Example: Solving an Integral via Transformation Trees . .                58
  2.8  Transformation Trees and Search Strategies . . . . . . . . .             59
  2.9  Algorithmic Outline for Symbolic Problem Solving . . . . .               60
  2.10 Discussion: What this example illustrates . . . . . . . . . .            65




                                       6
Modern Intelligent Systems                                                  Contents


3 Supervised Learning Foundations                                                67
  3.1  Problem Setup and Notation . . . . . . . . . . . . . . . . .              70
  3.2  Fitting, Overfitting, and Underfitting . . . . . . . . . . . .            70
  3.3  Empirical Risk Minimization and Regularization . . . . . .                71
  3.4  Elastic-net paths and cross-validation . . . . . . . . . . . .            74
  3.5  Common Loss Functions . . . . . . . . . . . . . . . . . . . .             75
  3.6  Model Selection, Splits, and Learning Curves . . . . . . . .              77
  3.7  Linear regression: a first full case study . . . . . . . . . . .          82

4 Classification and Logistic Regression                                         86
  4.1    From regression to classification . . . . . . . . . . . . . . .         87
  4.2    Classification problem statement . . . . . . . . . . . . . . .          88
  4.3    Bayes Optimal Classifier . . . . . . . . . . . . . . . . . . . .        88
  4.4    Logistic Regression: A Probabilistic Discriminative Model .             91
  4.5    Probabilistic Interpretation: MLE and MAP . . . . . . . .               94
  4.6    Confusion Matrices and Derived Metrics . . . . . . . . . . .            95


Part II: Neural networks, sequence modeling, and NLP                           100

5 Introduction to Neural Networks                                               100
  5.1   Biological Inspiration . . . . . . . . . . . . . . . . . . . . .        100
  5.2   From Biological to Artificial Neural Networks . . . . . . . .           101
  5.3   Outline of Neural Network Study . . . . . . . . . . . . . . .           102
  5.4   Neural Network Architectures . . . . . . . . . . . . . . . . .          103
  5.5   Activation Functions . . . . . . . . . . . . . . . . . . . . . .        104
  5.6   Learning Paradigms in Neural Networks . . . . . . . . . . .             106
  5.7   Fundamentals of Artificial Neural Networks . . . . . . . . .            107
  5.8   Mathematical Formulation of the Neuron Output . . . . . .               108
  5.9   McCulloch-Pitts neuron: examples and limits . . . . . . . .             109
  5.10 From MP Neuron to Perceptron and Beyond . . . . . . . .                  110

6 Multi-Layer Perceptrons: Challenges and Foundations                           116
  6.1   From a single unit to the smallest network . . . . . . . . . .          117
  6.2   Performance: what are we trying to improve? . . . . . . . .             119
  6.3   Gradient descent: how do weights move? . . . . . . . . . .              120


                                        7
Modern Intelligent Systems                                                   Contents


   6.4     Why hard thresholds block learning . . . . . . . . . . . . .          121
   6.5     Differentiable activations and the sigmoid trick . . . . . . .        122
   6.6     Deriving weight updates for the two- neuron network . . . .           123
   6.7     From two neurons to multi- layer networks . . . . . . . . .           125
   6.8     Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . .       126

7 Backpropagation Learning in Multi-Layer Perceptrons                            128
  7.1  Context and Motivation . . . . . . . . . . . . . . . . . . . .            128
  7.2  Problem Setup . . . . . . . . . . . . . . . . . . . . . . . . .           129
  7.3  Loss and Objective . . . . . . . . . . . . . . . . . . . . . . .          129
  7.4  Challenges in Weight Updates . . . . . . . . . . . . . . . .              130
  7.5  Notation for Layers and Neurons . . . . . . . . . . . . . . .             130
  7.6  Forward Pass Recap . . . . . . . . . . . . . . . . . . . . . .            131
  7.7  Backpropagation: Recursive Computation of Error Terms .                   133
  7.8  Backpropagation Algorithm: Detailed Derivation . . . . . .                136
  7.9  Backpropagation for Hidden Layers . . . . . . . . . . . . .               137
  7.10 Batch and Stochastic Gradient Descent . . . . . . . . . . .               138
  7.11 Backpropagation Algorithm: Brief Numerical Check . . . .                  140
  7.12 Training Procedure and Epochs in Multi-Layer Perceptrons                  143
  7.13 Role and Design of Hidden Layers . . . . . . . . . . . . . .              144
  7.14 Case Study: Learning the Function y = x sin x . . . . . . .               145
  7.15 Applications of Multi-Layer Perceptrons . . . . . . . . . . .             146
  7.16 Limitations of Multi-Layer Perceptrons . . . . . . . . . . .              147
  7.17 Conclusion of Multi-Layer Perceptron Derivations . . . . .                147

8 Radial Basis Function Networks (RBFNs)                                         152
  8.1   Overview and Motivation . . . . . . . . . . . . . . . . . . .            153
  8.2   Architecture of RBFNs . . . . . . . . . . . . . . . . . . . .            154
  8.3   Radial Basis Functions . . . . . . . . . . . . . . . . . . . . .         157
  8.4   Key Properties and Advantages . . . . . . . . . . . . . . . .            158
  8.5   Transforming Nonlinearly Separable Data into Linearly Sep-
        arable Space . . . . . . . . . . . . . . . . . . . . . . . . . .         158
  8.6   Finding the Optimal Weight Vector w . . . . . . . . . . . .              159
  8.7   The Role of the Transformation Function g(·) . . . . . . . .             160
  8.8   Examples of Kernel Functions . . . . . . . . . . . . . . . . .           160


                                        8
Modern Intelligent Systems                                                      Contents


   8.9     Interpretation of the Width Parameter σ . . . . . . . . . .              161
   8.10    Effect of σ on Classification Boundaries . . . . . . . . . . .           162
   8.11    Radial Basis Function Networks: Parameter Estimation and
           Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       163
   8.12    Remarks on Radial Basis Function Networks . . . . . . . .                167
   8.13    Preview: Unsupervised and Localized Learning . . . . . . .               170

9 Self-Organizing Networks                                                          172
  9.1   Overview of Self-Organizing Networks . . . . . . . . . . . .                173
  9.2   Clustering: Identifying Similarities and Dissimilarities . . .              174
  9.3   Dimensionality Reduction: Simplifying High-Dimensional
        Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          176
  9.4   Dimensionality Reduction and Feature Mapping . . . . . .                    178
  9.5   Self-Organizing Maps (SOMs): Introduction . . . . . . . . .                 178
  9.6   Conceptual Description of SOM Operation . . . . . . . . .                   180
  9.7   Mathematical Formulation of SOM . . . . . . . . . . . . . .                 181
  9.8   Kohonen Self-Organizing Maps (SOMs): Network Architec-
        ture and Operation . . . . . . . . . . . . . . . . . . . . . . .            182
  9.9   Example: SOM with a 3×3 Output Map and 4-Dimensional
        Input . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           184
  9.10 Key Properties of Kohonen SOMs . . . . . . . . . . . . . .                   185
  9.11 Winner-Takes-All Learning and Weight Update Rules . . .                      185
  9.12 Numerical Example of Competitive Learning . . . . . . . .                    187
  9.13 Winner-Takes-All Learning Recap . . . . . . . . . . . . . .                  188
  9.14 Regularization and Monitoring During SOM Training . . .                      189
  9.15 Limitations of Winner-Takes-All and Motivation for Coop-
        eration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         192
  9.16 Cooperation in Competitive Learning . . . . . . . . . . . .                  193
  9.17 Example: Neighborhood Update Illustration . . . . . . . .                    195
  9.18 Summary of Cooperative Competitive Learning Algorithm .                      196
  9.19 Wrapping Up the Kohonen Self-Organizing Map (SOM)
        Derivations . . . . . . . . . . . . . . . . . . . . . . . . . . .           196
  9.20 Applications of Kohonen Self-Organizing Maps . . . . . . .                   199




                                          9
Modern Intelligent Systems                                               Contents


10 Hopfield Networks: Introduction and Context                               203
   10.1 From Feedforward to Recurrent Neural Networks . . . . . .            204
   10.2 Hopfield’s breakthrough . . . . . . . . . . . . . . . . . . . .      205
   10.3 Network Architecture and Dynamics . . . . . . . . . . . . .          206
   10.4 Encoding conventions . . . . . . . . . . . . . . . . . . . . .       207
   10.5 Energy Function and Stability . . . . . . . . . . . . . . . .        208
   10.6 Hopfield Network States and Energy Function . . . . . . .            208
   10.7 Energy Minimization and Stable States . . . . . . . . . . .          209
   10.8 Example: Energy Calculation and State Updates . . . . . .            210
   10.9 Energy Function and Convergence of Hopfield Networks . .             211
   10.10 Asynchronous vs. Synchronous Updates in Hopfield Networks           215
   10.11 Storage Capacity of Hopfield Networks . . . . . . . . . . . .       216
   10.12 Improving Storage Capacity via Weight Updates . . . . . .           216
   10.13 Example: Weight Calculation for a Single Pattern . . . . .          217
   10.14 Finalizing the Hopfield Network Derivation and Discussion           218

11 Convolutional Neural Networks and Deep Training Tools                     223
   11.1 Motivation and map . . . . . . . . . . . . . . . . . . . . . .       224
   11.2 Why fully connected layers break on images . . . . . . . . .         225
   11.3 Sparse connectivity and parameter sharing . . . . . . . . .          227
   11.4 Convolution and pooling mechanics . . . . . . . . . . . . .          228
   11.5 Pooling as nonparametric downsampling . . . . . . . . . . .          229
   11.6 Channels and feature maps . . . . . . . . . . . . . . . . . .        230
   11.7 Training Neural Networks: Gradient-Based Optimization .              231
   11.8 Vanishing and Exploding Gradients in Deep Networks . . .             232
   11.9 Strategies to Mitigate Vanishing and Exploding Gradients .           234

12 Introduction to Recurrent Neural Networks                                 241
   12.1 Motivation for Recurrent Neural Networks . . . . . . . . . .         242
   12.2 Key Idea: State and Memory in RNNs . . . . . . . . . . . .           243
   12.3 Comparison with Feedforward Networks . . . . . . . . . . .           244
   12.4 Recap: Feedforward Building Blocks . . . . . . . . . . . . .         245
   12.5 Input–output configurations and mathematical formulation             248
   12.6 Mathematical Formulation of a Simple RNN Cell . . . . . .            249




                                      10
Modern Intelligent Systems                                                 Contents


   12.7  Recurrent Neural Network (RNN) Architectures and Loss
         Computation . . . . . . . . . . . . . . . . . . . . . . . . . .       249
   12.8 Stabilizing Recurrent Training . . . . . . . . . . . . . . . .         253
   12.9 From recurrent state to attention . . . . . . . . . . . . . . .        257
   12.10 Wrapping Up the Derivations . . . . . . . . . . . . . . . . .         258

13 Neural Network Applications in Natural Language Process-
   ing                                                                         263
   13.1 Context and Motivation . . . . . . . . . . . . . . . . . . . .         264
   13.2 Warm-up: from symbols to vectors . . . . . . . . . . . . . .           265
   13.3 Key Insight: Distributional Hypothesis . . . . . . . . . . . .         267
   13.4 Contextual Meaning and Feature Extraction . . . . . . . .              267
   13.5 Word2Vec at a glance . . . . . . . . . . . . . . . . . . . . .         268
   13.6 From lookup to objective: compact derivation path . . . . .            269
   13.7 Word2Vec objectives in detail . . . . . . . . . . . . . . . . .        272
   13.8 Eﬀicient Training of Word Embeddings: Hierarchical Soft-
         max and Negative Sampling . . . . . . . . . . . . . . . . . .         275
   13.9 Local Context vs. Global Matrix Factorization Approaches               277
   13.10 Global Word Vector Representations via Co-occurrence
         Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . .    278
   13.11 Finalizing the Word Embedding Derivations . . . . . . . . .           281
   13.12 Bias in Natural Language Processing . . . . . . . . . . . . .         284
   13.13 Responsible deployment checklist . . . . . . . . . . . . . . .        286

14 Transformers: Attention-Based Sequence Modeling                             289
   14.1 Why transformers after RNNs? . . . . . . . . . . . . . . . .           290
   14.2 Scaled Dot-Product Attention . . . . . . . . . . . . . . . . .         291
   14.3 Multi-Head Attention (MHA) . . . . . . . . . . . . . . . . .           292
   14.4 Positional Information . . . . . . . . . . . . . . . . . . . . .       293
   14.5 Masks and Training Objectives . . . . . . . . . . . . . . . .          294
   14.6 Encoder/Decoder Stacks and Stabilizers . . . . . . . . . . .           294
   14.7 Long Contexts and Eﬀicient Attention . . . . . . . . . . . .           296
   14.8 Fine-Tuning and Parameter-Eﬀicient Adaptation . . . . . .              297
   14.9 Decoding and Evaluation . . . . . . . . . . . . . . . . . . .          297
   14.10 Alignment (Brief) . . . . . . . . . . . . . . . . . . . . . . .       298


                                       11
Modern Intelligent Systems                                               Contents
```

### Findings
No issues spotted
