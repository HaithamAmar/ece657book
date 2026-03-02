# Scientific QA Report

- Source PDF: `notes_output/ece657_notes.pdf`
- Total chunks: 12

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
No issues spotted.

## Chunk 2/31
- Character range: 22044–44623

```text
14.11 Advanced attention and eﬀiciency notes (2024 snapshot) . .          298
   14.12 RNNs vs. Transformers: When and Why . . . . . . . . . .             299


Part III: Soft computing and fuzzy reasoning                                302

15 Introduction to Soft Computing                                            302
   15.1 Hard Computing: The Classical Paradigm . . . . . . . . . .           303
   15.2 Soft Computing: Motivation and Definition . . . . . . . . .          304
   15.3 Why Soft Computing? . . . . . . . . . . . . . . . . . . . . .        305
   15.4 Relationship Between Hard and Soft Computing . . . . . .             305
   15.5 Overview of Soft Computing Constituents . . . . . . . . . .          305
   15.6 Distinguishing Imprecision, Uncertainty, and Fuzziness . . .         306
   15.7 Soft Computing: Motivation and Overview . . . . . . . . .            307
   15.8 Fuzzy Logic: Capturing Human Knowledge Linguistically .              308
   15.9 Comparison with Other Soft Computing Paradigms . . . .               309
   15.10 Zadeh’s Insight and the Birth of Fuzzy Logic . . . . . . . .        310
   15.11 Challenges in Fuzzy Logic Systems . . . . . . . . . . . . . .       311
   15.12 Mathematical Languages as Foundations for Fuzzy Logic .             311
   15.13 Fuzzy Logic as a New Mathematical Language . . . . . . .            314
   15.14 Fuzzy Logic: Motivation and Intuition . . . . . . . . . . . .       314
   15.15 From Crisp Sets to Fuzzy Sets . . . . . . . . . . . . . . . .       315
   15.16 Wrapping Up Fuzzy Sets and Fuzzy Logic . . . . . . . . . .          316

16 Fuzzy Sets and Membership Functions: Foundations and
   Representations                                                           320
   16.1 Motivating example: designing a membership function from
         measurements . . . . . . . . . . . . . . . . . . . . . . . . . .    321
   16.2 Fuzzy sets and the universe of discourse . . . . . . . . . . .       322
   16.3 Membership Functions: Definition and Interpretation . . .            322
   16.4 Discrete vs. Continuous Universes of Discourse . . . . . . .         323
   16.5 Crisp Sets versus Fuzzy Sets . . . . . . . . . . . . . . . . .       324
   16.6 Membership Functions in Fuzzy Sets . . . . . . . . . . . . .         324
   16.7 Comparison of Membership Functions . . . . . . . . . . . .           326
   16.8 Example: Overlapping weight labels . . . . . . . . . . . . .         328
   16.9 Fuzzy Sets: Core Concepts and Terminology . . . . . . . .            329

                                      12
Modern Intelligent Systems                                                     Contents


   16.10   Probability vs. Possibility . . . . . . . . . . . . . . . . . . .       330
   16.11   Fuzzy Set Operations . . . . . . . . . . . . . . . . . . . . .          332
   16.12   Graphical Interpretation . . . . . . . . . . . . . . . . . . . .        334
   16.13   Additional Fuzzy Set Operations . . . . . . . . . . . . . . .           334
   16.14   Example: Union and Intersection of Fuzzy Sets . . . . . . .             335
   16.15   Cartesian Product of Fuzzy Sets . . . . . . . . . . . . . . .           335
   16.16   Properties of Fuzzy Set Operations . . . . . . . . . . . . . .          336
   16.17   Fuzzy Set Operators . . . . . . . . . . . . . . . . . . . . . .         337
   16.18   Complement Operators in Fuzzy Logic . . . . . . . . . . . .             337
   16.19   Triangular norms (t- norms) . . . . . . . . . . . . . . . . . .         338
   16.20   Triangular conorms (t- conorms / s-norms) . . . . . . . . .             340
   16.21   T-Norms and S-Norms: Complementarity and Properties .                   341
   16.22   Examples of common t- norm/s-norm pairs . . . . . . . . .               342
   16.23   Fuzzy Set Inclusion and Subset Relations . . . . . . . . . .            342
   16.24   Degree of Inclusion . . . . . . . . . . . . . . . . . . . . . . .       343
   16.25   Set Operations and Inclusion Properties . . . . . . . . . . .           343
   16.26   Grades of Inclusion and Equality in Fuzzy Sets . . . . . . .            344
   16.27   Dilation and Contraction of Fuzzy Sets . . . . . . . . . . .            345
   16.28   Closure of Membership Function Derivations . . . . . . . .              346
   16.29   Implications for Fuzzy Inference Systems . . . . . . . . . .            348
   16.30   Worked Example: Mamdani Fuzzy Inference (End-to-End)                    349

17 Fuzzy Set Transformations Between Related Universes                             353
   17.1 Context and Motivation . . . . . . . . . . . . . . . . . . . .             354
   17.2 Problem Statement . . . . . . . . . . . . . . . . . . . . . . .            355
   17.3 Intuition and Challenges . . . . . . . . . . . . . . . . . . . .           355
   17.4 Formal Definition of the Transformed Membership Function                   356
   17.5 Interpretation . . . . . . . . . . . . . . . . . . . . . . . . . .         356
   17.6 Example Setup . . . . . . . . . . . . . . . . . . . . . . . . .            357
   17.7 Transformation of Fuzzy Sets Between Universes . . . . . .                 357
   17.8 Extension Principle Recap and Projection Operations . . .                  360
   17.9 Projection of Fuzzy Relations . . . . . . . . . . . . . . . . .            361
   17.10 Dimensional Extension and Projection in Fuzzy Set Opera-
         tions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       364
   17.11 Fuzzy Inference via Composition of Relations . . . . . . . .              365


                                         13
Modern Intelligent Systems                                                  Contents


   17.12   Recap and Motivation . . . . . . . . . . . . . . . . . . . . .       367
   17.13   Generalization of Fuzzy Relation Composition . . . . . . .           368
   17.14   Example Calculation of Composition . . . . . . . . . . . . .         368
   17.15   Properties of Fuzzy Relation Composition . . . . . . . . . .         369
   17.16   Alternative Composition Operators . . . . . . . . . . . . . .        369

18 Fuzzy Inference Systems: Rule Composition and Output Cal-
   culation                                                                     372
   18.1 Context and Motivation . . . . . . . . . . . . . . . . . . . .          373
   18.2 Rule Antecedent Composition . . . . . . . . . . . . . . . . .           374
   18.3 Rule Consequent and Output Fuzzy Set . . . . . . . . . . .              375
   18.4 Aggregation of Multiple Rules . . . . . . . . . . . . . . . . .         376
   18.5 Summary of the Fuzzy Inference Process . . . . . . . . . . .            376
   18.6 Worked example: thermostat inference with numbers . . . .               378
   18.7 Mamdani vs. Sugeno/Takagi–Sugeno systems . . . . . . . .                381


Part IV: Evolutionary optimization                                             385

19 Introduction to Evolutionary Computing                                       385
   19.1 Context and Motivation . . . . . . . . . . . . . . . . . . . .          386
   19.2 Philosophical and Historical Background . . . . . . . . . . .           386
   19.3 Problem Setting: Optimization . . . . . . . . . . . . . . . .           387
   19.4 Illustrative Example . . . . . . . . . . . . . . . . . . . . . .        387
   19.5 Why Not Brute Force? . . . . . . . . . . . . . . . . . . . . .          388
   19.6 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . .         388
   19.7 Challenges in Continuous Optimization and Motivation for
         Evolutionary Computing . . . . . . . . . . . . . . . . . . .           388
   19.8 Introduction to Evolutionary Computing . . . . . . . . . .              389
   19.9 Biological Inspiration: Evolutionary Concepts . . . . . . . .           390
   19.10 Implications for Genetic Algorithms . . . . . . . . . . . . .          390
   19.11 Summary of Biological Mechanisms Modeled in GAs . . . .                391
   19.12 Genetic Algorithms: Modeling Chromosomes . . . . . . . .               392
   19.13 Mapping Genetic Algorithms to Optimization Problems . .                395
   19.14 Encoding in Genetic Algorithms . . . . . . . . . . . . . . .           396
   19.15 Population Initialization and Size . . . . . . . . . . . . . . .       399

                                       14
Modern Intelligent Systems                                                Contents


   19.16   Genetic Operators . . . . . . . . . . . . . . . . . . . . . . .    399
   19.17   Selection in Genetic Algorithms . . . . . . . . . . . . . . . .    400
   19.18   Crossover Operator . . . . . . . . . . . . . . . . . . . . . . .   402
   19.19   Crossover Operators in Genetic Algorithms . . . . . . . . .        403
   19.20   Mutation Operator . . . . . . . . . . . . . . . . . . . . . . .    404
   19.21   Summary of Genetic Operators and Their Probabilities . .           405
   19.22   Known Issues in Genetic Algorithms . . . . . . . . . . . . .       406
   19.23   Convergence Criteria . . . . . . . . . . . . . . . . . . . . . .   407
   19.24   Summary of Genetic Algorithm Workflow . . . . . . . . . .          408
   19.25   Pseudocode Representation . . . . . . . . . . . . . . . . . .      410
   19.26   Example: GA for a Constrained Optimization Problem . .             410
   19.27   Genetic Algorithms: Iterative Process and Convergence . .          413
   19.28   Beyond canonical GAs: real-coded strategies . . . . . . . .        414
   19.29   Genetic Programming (GP) . . . . . . . . . . . . . . . . . .       414
   19.30   Wrapping Up Genetic Algorithms and Genetic Programming             416
   19.31   Multi-objective search and NSGA-II . . . . . . . . . . . . .       418


Back matter                                                                   422

Key Takeaways                                                                 423

A Linear Systems Primer                                                       439

B Kernel Methods and Support Vector Machines                                  442

C Course Logistics                                                            444
  C.1  Using this book in ECE 657 . . . . . . . . . . . . . . . . . .         444

D Notation collision index                                                    445

E Reproducibility and Reporting Standards                                     446




                                        15
Modern Intelligent Systems                                           List of Figures



List of Figures
   1    Roadmap (core supervised path; SOM/fuzzy; optimiza-
        tion/evolutionary). Use it when choosing a reading path and
        locating prerequisites before jumping ahead. . . . . . . . . . .         48
   2    Transformation tree for the running example integral; badges
        [S]/[H] mark safe vs. heuristic moves; the dashed branch mir-
        rors the sine substitution. Use it when diagnosing where a
        solve attempt branched and why backtracking was required. .              60
   3    Underfitting and overfitting as a function of model complexity.
        Training error typically decreases with complexity, while val-
        idation error often has a U-shape. Regularization and model
        selection aim to operate near the minimum of the validation
        curve. Use it when deciding whether to add capacity, add
        data, or add regularization. . . . . . . . . . . . . . . . . . . .       71
   4    Why L1 promotes sparsity. Minimizing loss subject to an L2
        constraint tends to hit a smooth boundary; an L1 constraint
        has corners aligned with coordinate axes, so tangency often
        occurs at a point where some coordinates are exactly zero.
        Use it when choosing between L1 and L2 penalties for feature
        selection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     74
   5    A typical lasso path as the regularization strength increases.
        Coeﬀicients shrink, and some become exactly zero, yielding
        sparse models. Use it when interpreting how penalty strength
        trades accuracy for sparsity. . . . . . . . . . . . . . . . . . . .      74
   6    Classification losses as functions of the signed margin z. Use it
        when comparing how different losses treat confident mistakes
        and near-boundary points. . . . . . . . . . . . . . . . . . . . .        76
   7    Regression losses versus prediction error. The Huber loss tran-
        sitions from quadratic to linear to reduce sensitivity to outliers.
        Use it when choosing a loss that is robust to heavy-tailed noise.        77




                                       16
Modern Intelligent Systems                                           List of Figures


   8    Dataset partitioning into training, validation, and test seg-
        ments. Any resampling scheme should preserve disjoint evalu-
        ation data; when classes are imbalanced, shuffle within strata
        so each split reflects the overall class mix. Use it when de-
        signing splits that support trustworthy model selection and
        reporting. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     79
   9    Mini ERM pipeline (split once, iterate train/validate, then
        test only the best model on the held-out set). Use it when
        enforcing a clean separation between tuning and final reporting.         79
   10   Learning curves reveal under/overfitting: the validation curve
        flattens while additional data continue to decrease training er-
        ror only marginally. A shaded patience window marks when
        early stopping would halt if no validation improvement occurs.
        Use it when deciding whether you need more data, more ca-
        pacity, or different regularization. . . . . . . . . . . . . . . . .     80
   11   Calibration and capacity diagnostics (reliability and double
        descent) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     81
   12   Ridge regularization shrinks parameter norms as the penalty
        strength increases. Use it when tuning weight decay to control
        variance without forcing sparsity. . . . . . . . . . . . . . . . .       82
   13   Synthetic binary dataset. . . . . . . . . . . . . . . . . . . . .        90
   14   Bayes-optimal boundary for two Gaussian classes. Equal co-
        variances and similar priors (LDA setting) yield a linear sep-
        arator; unequal covariances yield a quadratic boundary. The
        boundary is near the equal-posterior line (vertical, pink); left-
        /right regions map to predicted classes R0 and R1. Use it
        when contrasting linear vs. quadratic boundaries under differ-
        ent generative assumptions. . . . . . . . . . . . . . . . . . . .        90
   15   The sigmoid maps logits to probabilities (left). The binary
        cross-entropy (negative log-likelihood) penalizes confident
        wrong predictions sharply (middle). Regularization typically
        shrinks parameter norms as the penalty strength increases
        (right). Use it when choosing a baseline probabilistic classifier
        and diagnosing overconfidence. . . . . . . . . . . . . . . . . .         93



                                       17
Modern Intelligent Systems                                             List of Figures


   16   Gradient-descent iterates contracting toward the minimizer of
        a convex quadratic cost. Ellipses are level sets; arrows show
        the “steepest descent along contours” direction. Use it when
        visualizing why conditioning slows gradient descent. . . . . .             93
   17   Illustrative logistic-regression boundary. The dashed line
        marks the linear decision boundary at probability 0.5; labeled
        contours show how the posterior varies smoothly with margin,
        enabling calibrated decisions and adjustable thresholds. Use
        it when explaining why logistic outputs support threshold
        tuning. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      94
   18   MAP estimates interpolate between the prior mean and the
        data-driven MLE. As the sample size grows, the MAP curve
        approaches the true mean. Use it when explaining how priors
        matter most in low-data regimes. . . . . . . . . . . . . . . . .           95
   19   ROC and PR curves with an explicit operating point. Left:
        ROC curve with iso-cost lines; right: PR curve with a class-
        prevalence baseline and iso-F1 contours. Together they visu-
        alize threshold trade-offs and calibration quality. Use it when
        selecting an operating point under class imbalance and asym-
        metric costs. . . . . . . . . . . . . . . . . . . . . . . . . . . . .      96
   20   Confusion matrix for a three-class classifier; diagonals dom-
        inate, indicating strong accuracy with modest confusion be-
        tween classes B and C. Use it when diagnosing which error
        types dominate in multiclass settings. . . . . . . . . . . . . .           97
   21   Perceptron geometry. Points on opposite sides of the sepa-
        rating hyperplane receive different labels, and signed distance
        to the boundary controls both prediction and update magni-
        tude. Compare with Figure 17 in Chapter 4: both are linear
        separators, but logistic smooths the boundary into calibrated
        probabilities. Use it when relating margin geometry to update
        size and convergence. . . . . . . . . . . . . . . . . . . . . . . .       113




                                         18
Modern Intelligent Systems                                            List of Figures


   22   The minimal neural network used in this chapter is a two-
        neuron chain. The first unit produces an intermediate signal,
        and the second unit maps that signal to the final output. Use it
        when tracking variables and gradients in a toy network before
        scaling to deeper models. . . . . . . . . . . . . . . . . . . . .        119
   23   Think of performance as a surface over the weights. Gradient
        descent moves in one vector step (blue), whereas coordinate-
        wise updates can zig-zag (orange). Use it when building intu-
        ition for why gradient directions reduce loss more eﬀiciently
        than axis-aligned steps. . . . . . . . . . . . . . . . . . . . . .       121
   24   Hard thresholds block gradient-based learning because the
        derivative is zero almost everywhere. A smooth activation
        like the sigmoid provides informative derivatives across a wide
        range of inputs. Use it when motivating why smooth nonlin-
        earities enable gradient-based training. . . . . . . . . . . . . .       122
   25   Computational graph for backpropagation (reverse-mode AD)                139
   26   Forward (blue) and backward (orange) flows for a two-layer
        MLP. Cached activations and layerwise deltas travel along
        these arrows; backward signals use next-layer weights and ac-
        tivation derivatives. Use it when implementing backprop to
        confirm what to cache and where gradients flow. . . . . . . .            148
   27   Canonical activation functions on a common axis. Solid curves
        show the activation; dashed curves show its derivative. Use it
        when choosing an activation and checking whether its deriva-
        tive will saturate or die out. . . . . . . . . . . . . . . . . . . .     150
   28   RBFN architecture. Inputs feed fixed radial units parame-
        terized by centers and widths; a linear readout with weights
        and bias is trained by a regression or classification loss. Only
        the output weights are typically learned, while centers/widths
        come from k-means or spacing heuristics. Use it when sepa-
        rating representation design (centers/widths) from supervised
        readout training. . . . . . . . . . . . . . . . . . . . . . . . . .      155




                                        19
Modern Intelligent Systems                                             List of Figures


   29   Localized Gaussian basis functions (dashed) and their
        weighted sum (solid). Overlapping bumps allow RBF net-
        works to interpolate complex signals smoothly. Use it when
        building intuition for locality and smooth interpolation in
        basis-function models. . . . . . . . . . . . . . . . . . . . . . .        156
   30   Center placement and overlap. Top: K-means prototypes
        roughly tile the data manifold, giving even overlap; bottom:
        random centers can leave gaps or excessive overlap, influenc-
        ing the width (sigma) choice and conditioning. Use it when
        choosing how to place centers before tuning the width param-
        eter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     157
   31   How the width parameter (sigma) influences decision bound-
        aries on a 2D toy dataset. Too-large sigma underfits, inter-
        mediate sigma captures the boundary, too-small sigma over-
        fits with fragmented regions. Validation curves in Chapter 3
        guide model size and regularization; they also motivate tuning
        sigma to balance smoothness against boundary fidelity. . . . .            162
   32   Primal (finite basis) vs. dual (kernel ridge) viewpoints. Using
        as many centers as data points recovers the dual form; using
        fewer centers corresponds to a Nyström approximation. The
        same trade-off appears in kernel methods through the choice
        of kernel and effective rank. Use it when deciding whether to
        train a finite basis model or switch to a kernel viewpoint. . .           166
   33   RBFN decision boundary on XOR with 4 centers, sigma =
        0.8, and ridge lambda = 1e-3. Shading indicates the predicted
        class under a 0.5 threshold; the black contour marks the 0.5
        boundary. Training points are overlaid (class 0: open circles;
        class 1: filled squares). See Figure 31 for sigma effects. Use it
        when checking whether center count and width are suﬀicient
        for a non-linear boundary. . . . . . . . . . . . . . . . . . . . .        168




                                         20
Modern Intelligent Systems                                             List of Figures
```

### Findings
No issues spotted

## Chunk 3/31
- Character range: 44629–70783

```text
34   Learning-rate scheduling intuition. On a smooth objective
        (left), large initial steps quickly cover ground and roughly align
        prototypes, while a decaying step-size refines the solution near
        convergence. Right: common exponential and multiplicative
        decays used in SOM training. Use it when choosing a schedule
        that converges without freezing too early. . . . . . . . . . . .          175
   35   Classical MDS intuition. Projecting a cube onto a plane
        via an orthogonal map yields a square (left), whereas an
        oblique projection along a body diagonal produces a hexagon
        (right). The local adjacency of vertices is preserved even
        though metric structure is distorted. Use it when interpreting
        low-dimensional embeddings as geometry-preserving only in
        limited ways. . . . . . . . . . . . . . . . . . . . . . . . . . . .       177
   36   Gaussian neighborhood weights in SOM training. Early iter-
        ations use a broad kernel so many neighbors adapt; later iter-
        ations shrink the neighborhood width sigma(t) so only units
        near the BMU update. Use it when tuning sigma(t) to trade
        global ordering for local refinement. . . . . . . . . . . . . . .         182
   37   Bias–variance trade-off when sweeping SOM capacity (number
        of units or kernel width). The optimum appears near the knee
        where bias and variance intersect. Use it when selecting map
        size/capacity via validation curves rather than aesthetics. . .           189
   38   Regularization smooths the loss surface. Coupling neighboring
        prototypes (right) yields wider, flatter basins than the jagged
        unregularized landscape (left). Use it when explaining why
        regularization can improve stability and generalization. . . . .          190
   39   Quantization error combined with an entropy-style regularizer
        (modern SOM variant; for example, a negative sum of p log p
        over unit usage). Valleys arise when prototypes cover the space
        evenly; ridges highlight collapse or poor topological preserva-
        tion. Use it when diagnosing prototype collapse versus healthy
        coverage. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     191




                                         21
Modern Intelligent Systems                                              List of Figures


   40   Validation curves used to identify an early-stopping knee.
        When both quantization and topographic errors flatten
        (shaded band), further training risks map drift. Use it when
        deciding where to stop training based on stability, not only
        final error. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     192
   41   Voronoi-like regions induced by SOM prototypes (left) and the
        corresponding softmax confidence after shrinking the neighbor-
        hood kernel (right). Softer updates blur the decision frontiers
        and reduce jagged mappings between adjacent neurons. Use
        it when interpreting a prototype map as a piecewise-constant
        partition of feature space. . . . . . . . . . . . . . . . . . . . .        193
   42   Left: a 5-by-5 SOM lattice with best matching unit (blue) and
        neighbors inside the Gaussian-kernel radius (green). Right: a
        toy U-Matrix (grayscale-safe colormap) showing average dis-
        tances between neighboring codebook vectors; larger distances
        indicate likely cluster boundaries. Use it when reading U-
        Matrices as boundary hints, not absolute distances. . . . . . .            194
   43   Component planes for three features on a trained SOM (toy
        data). Each plane maps one feature across the grid; aligned
        bright/dark regions reveal correlated features and complement
        the U-Matrix in Figure 42. Interpret brightness comparatively
        within a plane rather than as an absolute scale. Use it when
        diagnosing which input features drive map organization. . . .              195
   44   SOM lattice with the best-matching unit (BMU) highlighted
        in blue and a dashed neighborhood radius indicating which
        prototype vectors receive cooperative updates. Use it when
        visualizing the cooperative update neighborhood around the
        BMU. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         196
   45   Hopfield energy decreases monotonically under asynchronous
        updates. Starting from a noisy probe state s(0), successive
        single-neuron flips move downhill until the stored memory s(2)
        is recovered. Use it when explaining why asynchronous up-
        dates converge under Hopfield’s symmetry constraints. . . . .              212




                                         22
Modern Intelligent Systems                                              List of Figures


   46   Receptive field growth across depth. Even with small 3 × 3
        kernels, stacking layers expands the spatial context seen by
        deeper units. Use it when explaining why depth can replace
        very large kernels. . . . . . . . . . . . . . . . . . . . . . . . .        231
   47   Dropout effect on training/validation curves (validation flat-
        tening) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      236
   48   Batch normalization transforms per-channel activations to-
        ward zero mean and unit variance prior to the learned
        aﬀine re-scaling, stabilizing training. Use it when diagnosing
        unstable training from drifting activation scales. . . . . . . .           237
   49   Representative training curves for SGD with momentum ver-
        sus Adam on the same CNN. Use it when comparing optimizer
        behavior under the same model and data. . . . . . . . . . . .              238
   50   Decision boundaries for logistic regression (left) versus a shal-
        low MLP (right). Linear models carve a single hyperplane,
        whereas hidden units can warp the boundary to follow non-
        convex manifolds such as the moons dataset. Use it when di-
        agnosing whether representation capacity (not optimization)
        limits a classifier. . . . . . . . . . . . . . . . . . . . . . . . . .     246
   51   Binary cross-entropy geometry (left), effect of learning-rate
        schedules on loss (middle), and the typical training/valida-
        tion divergence that motivates early stopping (right). Use it
        when choosing a learning-rate schedule and interpreting early-
        stopping signals. . . . . . . . . . . . . . . . . . . . . . . . . .        247
   52   Unrolling an RNN reveals repeated application of the same
        parameters across time steps. This view motivates backprop-
        agation through time (BPTT), which accumulates gradients
        through every copy before updating the shared weights. Use
        it when translating a recurrent cell into an explicit computa-
        tion graph for training. . . . . . . . . . . . . . . . . . . . . . .       249
   53   Backpropagation through time (BPTT): unrolled forward pass
        (black) and backward gradients (pink) through time. Use it
        when reasoning about truncation windows and why long his-
        tories strain gradient flow. . . . . . . . . . . . . . . . . . . . .       252



                                         23
Modern Intelligent Systems                                              List of Figures


   54   Vanishing (blue) versus exploding (orange) gradients on a log
        scale. The gray strip highlights the stability band; the inset
        reminds readers that repeated Jacobian products either shrink
        gradients (thin blue arrows) or amplify them (thick orange
        arrows). Use it when diagnosing why long-range dependencies
        fail to train. . . . . . . . . . . . . . . . . . . . . . . . . . . . .     253
   55   Gradient norms (left) explode without clipping (orange) but
        remain bounded when the global norm is clipped at tau
        (green). Training loss (right) stabilizes as a result. Use it
        when setting clipping thresholds to stabilize training without
        freezing learning. . . . . . . . . . . . . . . . . . . . . . . . . .       254
   56   Teacher forcing vs. inference in a sequence-to-sequence de-
        coder. Gold arrows show supervised targets; orange arrows
        highlight autoregressive feedback that motivates scheduled
        sampling. Use it when diagnosing train/test mismatch from
        teacher forcing. . . . . . . . . . . . . . . . . . . . . . . . . . .       255
   57   Long Short-Term Memory (LSTM) cell (Hochreiter and
        Schmidhuber, 1997; Gers et al., 2000). Use it when mapping
        gates and the cell state to the gradient-flow path. . . . . . . .          256
   58   Gated Recurrent Unit (GRU) cell (Cho et al., 2014). Use it
        when comparing gating to vanilla recurrence and to LSTM-
        style memory. . . . . . . . . . . . . . . . . . . . . . . . . . . .        256
   59   Attention heatmap for a translation model. Rows are target
        tokens (decoder steps) and columns are source tokens (encoder
        positions). Each cell is an attention weight; the dot in each
        row marks the source position receiving the most attention.
        Use it when checking whether attention aligns to the intended
        source context. . . . . . . . . . . . . . . . . . . . . . . . . . .        258
   60   Analogy geometry in embedding space. The offset “v(king) -
        v(man) + v(woman) approx v(queen)” forms a parallelogram;
        a similar gender direction shifts “doctor” toward “nurse.” Solid
        and dashed vectors highlight the shared relational direction.
        Points are shown after 2D PCA, so directions are approximate.
        Use it when checking whether embedding offsets encode con-
        sistent relations and reveal bias directions. . . . . . . . . . . .        280

                                         24
Modern Intelligent Systems                                             List of Figures


   61   Schematic: Reference schematic for the Transformer. Left:
        scaled dot-product attention. Center: multi-head concatena-
        tion with an output projection. Right: pre-LN encoder block
        combining attention, FFN, and residual connections; a post-
        LN variant simply moves each LayerNorm after its residual
        add (dotted alternative, not shown). . . . . . . . . . . . . . .          293
   62   Schematic: Transformer micro-views. Left: positional encod-
        ings (sinusoidal/rotary) add order information. Center: KV
        cache stores past keys/values so decoding a new token reuses
        prior context. Right: LoRA inserts low-rank adapters (B A)
        on top of a frozen weight matrix W for parameter-eﬀicient
        tuning. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     294
   63   Schematic: Attention masks visualized as heatmaps (queries
        on rows, keys on columns). Left: padding mask zeroes atten-
        tion into padded positions of a shorter sequence in a packed
        batch. Right: causal mask enforces autoregressive flow by
        blocking attention to future tokens. . . . . . . . . . . . . . . .        297
   64   Trapezoidal membership functions for grades C and B with
        the overlapping region shaded. Scores near 78–82 partially
        satisfy both grade definitions. Use it when designing overlap-
        ping grade/linguistic bins so boundary cases behave smoothly.             327
   65   Overlapping membership functions for Small/Medium/Large
        labels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      329
   66   Fuzzy AND surfaces comparing minimum versus product
        t-norms; analogous OR surfaces show similar differences.
        Choices here influence rule aggregation in Chapter 18. Use
        it when deciding whether conjunction should behave like a
        conservative minimum or a multiplicative attenuation. . . . .             339
   67   End-to-end fuzzy inference example. (A) Consequent mem-
        bership functions with clipping levels from firing strengths at
        T = 27 deg C. (B) Aggregated output set (max of truncated
        consequents) and a centroid marker near s* approx 0.58. Use
        it when sanity-checking clipping, aggregation, and centroid de-
        fuzzification end to end. . . . . . . . . . . . . . . . . . . . . .       351



                                        25
Modern Intelligent Systems                                         List of Figures


   68   Mapping a fuzzy set through the function “y = x-squared”.
        The membership at an output value y is the supremum over
        all pre-images x that map to y; shared images such as x = +/-
        1 map to y = 1 using the maximum membership. Use it when
        applying the extension principle to a non-invertible function.        359
   69   Alpha-cuts under the non-monotone map “y = x-squared”. A
        symmetric triangular fuzzy set on X maps to a right-skewed
        fuzzy set on Y. Each alpha-cut on A splits into two intervals
        whose images union to the output alpha-cut. Use it when prop-
        agating a fuzzy set through a non-monotone map via alpha-cuts.        362
   70   Illustrative fuzzy relation table (left) together with its projec-
        tions onto the error universe (middle) and the rate-of-change
        universe (right). These are the exact quantities used in the
        running thermostat example before composing rules. Use it
        when building rule antecedents from a relation and checking
        which universes each projection lives on. . . . . . . . . . . . .     364
   71   Evolutionary micro-operators. Left: fitter individuals get sam-
        pled more often (roulette/tournament). Middle: crossover
        splices parents by a mask (one-point shown). Right: con-
        straint handling routes offspring through repair/penalty/fea-
        sibility before evaluation. Use it when mapping an implemen-
        tation to the canonical operator loop. . . . . . . . . . . . . .      394
   72   Illustrative GA run showing the best and mean normalized fit-
        ness over 50 generations. Flat regions motivate “no improve-
        ment” stopping rules, while steady separation between best
        and mean indicates ongoing selection pressure. Use it when
        diagnosing premature convergence versus ongoing exploration.          408
   73   GA flowchart showing the iterative process: initialization leads
        to fitness evaluation and a termination check. If not termi-
        nated, the algorithm proceeds through selection, crossover,
        mutation, and replacement, which then feeds the next gen-
        eration’s fitness evaluation. Use it when verifying that your
        implementation preserves the intended control flow. . . . . . .       409




                                      26
Modern Intelligent Systems                                           List of Figures


   74   Sample Pareto front for two objectives. NSGA-II keeps all non-
        dominated points (blue) while pushing dominated solutions
        (orange) toward the front via selection, yielding a spread of
        trade-offs in one run. Use it when interpreting multi-objective
        results as trade-offs, not a single optimum. . . . . . . . . . . .      419
   75   Map of model families . . . . . . . . . . . . . . . . . . . . . .       427




                                       27
Modern Intelligent Systems                                              List of Tables



List of Tables
   1    Table: Transformation toolkit (safe vs. heuristic). Precondi-
        tions keep domains/branches explicit (e.g., restrictions like “x
        in (-1,1)” for square-root expressions); principal branches un-
        less noted. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      64
   2    Common losses and typical use (reference for Chapters 3 to 5).
        Use it when matching a loss to a modeling assumption and a
        downstream decision metric. . . . . . . . . . . . . . . . . . . .          76
   3    Handling class imbalance for logistic models (Chapter 4 refer-
        ence table). Use it when choosing resampling, weighting, and
        thresholding strategies for rare positives. . . . . . . . . . . . .        98
   4    Single-neuron flips from (1, 1, -1); all raise the energy, so the
        state is a local minimum. Use it when checking stability of a
        stored pattern under single-bit perturbations. . . . . . . . . .          211
   5    Feature-based word vectorization example. Each word is
        mapped to a vector of graded semantic features; fractional
        entries (e.g., 0.5) indicate mixed usage across contexts. Use
        it when building intuition for how discrete symbols become
        vectors that downstream models can consume. . . . . . . . .               266
   6    Fuzzy vs. probabilistic reasoning at a glance. Use it when de-
        ciding whether your uncertainty is about randomness (proba-
        bility) or about graded concepts (fuzziness). . . . . . . . . . .         308
   7    Boolean operators vs. fuzzy operators at a glance. Use it when
        translating crisp logic rules into graded operators for fuzzy
        inference. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      308
   8    Typical operator choices in fuzzy inference and their qualita-
        tive effects. Here the t-norm implements fuzzy AND, the s-
        norm implements fuzzy OR, and the implication shapes conse-
        quents. Use it when choosing default operators for a Mamdani-
        style pipeline and predicting qualitative behavior. . . . . . . .         349
   9    Popular t-norms and their typical roles. Use it when choosing
        a default conjunction operator and understanding its qualita-
        tive behavior. . . . . . . . . . . . . . . . . . . . . . . . . . . .      363



                                         28
Modern Intelligent Systems                                             List of Tables


   10   Toy GA generation on a bounded interval. One crossover and
        mutation illustrate how the fitness function guides selection
        before the next generation. Use it when explaining how varia-
        tion operators interact with selection pressure. . . . . . . . .         409
   11   Big-picture view of model families across the taxonomy and
        learning paradigms. Each entry represents a family introduced
        in the book; supervision labels indicate the dominant training
        signal rather than strict exclusivity. Use this when you want
        to locate which model family matches a needed capability and
        what learning signal it relies on. . . . . . . . . . . . . . . . . .     428




                                        29
Modern Intelligent Systems                                             List of Tables



Notation and Conventions
Symbol overloads. A small number of symbols are intentionally reused across
chapters (for example, σ(·) as the sigmoid nonlinearity versus σ as a width/s-
cale parameter). For a one-page index of the most common collisions and the
disambiguation rule used in this book, see Appendix D.

     Symbol            Description
     x ∈ Rn            Input vector (features)
     y∈R               Regression target (continuous)
     y ∈ {0, 1}        Binary class label (Bernoulli outcome)
     ŷ                Model prediction
     D                 Dataset or feasible domain
     L                 Loss function (objective)
     σ(·)              Sigmoid function 1/(1 + e−z )
     tanh(·)           Hyperbolic tangent activation
     ReLU(z)           max(0, z) activation
     W, b              Weights and biases (parameters)
     ht , c t          Hidden and cell states (RNN/LSTM)
     n                 Sequence length (tokens)
     dmodel            Model (embedding) width
     h                 Number of attention heads
     dk , d v          Per-head key/query and value widths
     Q, K, V           Query, key, value matrices
     WiQ , WiK , WiV   Per-head projection matrices
     WO                Output projection after concatenating heads
     KV cache          Stored past keys/values for decoding
     µA (x)            Membership of x in fuzzy set A
     T, S              t-norm (AND) and s-norm (OR)
     softmax(·)        Normalized exponential mapping
     k · k2            Euclidean norm
     ∇                 Gradient operator
     η                 Learning rate
     λ                 Regularization strength
     k                 Number of clusters/classes/neighbors (context-dependent)
     E[·]              Expectation
     Var[·]            Variance
     diag(·)           Diagonal matrix formed from a vector
                       Hadamard (elementwise) product
     ϕ(·)              Feature map; in kernels, k(x, z) = ϕ(x)⊤ ϕ(z)
     1, I              All-ones vector and identity matrix


                                         30
Modern Intelligent Systems                                          List of Tables


    This section collects book-wide notation, conventions, and a few reading
aids. Symbols may be locally redefined within a chapter when explicitly stated.
Where symbols are overloaded (e.g., σ as sigmoid vs. standard deviation), the
local meaning is made explicit in context.

Conventions
Throughout the book we follow a consistent notational style:
  • Bold lowercase (x, w) denote vectors; bold uppercase (W, X) denote ma-
    trices; plain roman symbols (x, y, σ) denote scalars.

  • Random variables are written in uppercase (X, Y ) when needed, with low-
    ercase (x, y) for their realizations.

  • Transpose is always indicated by the superscript ·⊤ , as in W⊤ x; we avoid
    bare T to reduce ambiguity.

  • The logistic sigmoid is written as σ(z) = 1/(1 + e−z ); the same letter σ
    without an argument (e.g., σ 2 ) denotes a standard deviation. The intended
    meaning is clear from whether an argument is present. In fuzzy chapters,
    µA (x) denotes membership rather than a mean; context and arguments
    disambiguate overloaded symbols.

  • Embedding matrices are written in bold (E, W, U) and should not be con-
    fused with the expectation operator E[·]; when expectations appear, they
    are always typeset with the blackboard bold E. We use row embeddings
    by convention: a one-hot row vector x ∈ {0, 1}1×|V | selects a row via
    xE ∈ R1×d .

  • Feature maps in kernel methods are written as ϕ(·); we reserve φ(·) for
    radial-basis kernels. When probability density functions are needed, we
    write them as p(·) (or pX (·) when the variable must be explicit). The
    corresponding design matrix Φ collects feature-map evaluations on data.
These conventions are occasionally restated in local “Notation note” boxes where
multiple meanings could collide (e.g., in chapters on statistics or recurrent net-
works). As a practical guide: row vectors are written as 1 × n objects, column
vectors as n × 1; a design matrix collects one data point per row (features in
columns), so data matrices are row-major N × d.


                                       31
Modern Intelligent Systems                                          List of Tables


Reading Aids
 How to read the visuals
    • Legends and icons: Every figure caption states what each color or
      line style represents (safe vs. heuristic transformations, training vs.
      validation curves, etc.).

    • Tables and references: Table captions mention the chapter(s) they
      support so you can quickly jump back when a later chapter references
      them.

 Editorial heuristics: four recurring questions
 Each chapter has been edited with four recurring questions in mind:
    • What is the core scientific idea, and how does it relate to earlier
      material?

    • Which methodological cautions should a practitioner keep close at
      hand?

    • How do the accompanying figures or derivations anchor those ideas
      visually?

    • Where does the topic sit within the broader landscape of intelligent
      systems?

 Author’s note: intuition before algebra
 The math that follows is intentionally tight, but the spirit of this book is to
 keep the reason for each tool front and center. When I introduce a method,
 I start from the question an engineer would actually be wrestling with and
 then introduce the equations needed to make it precise. Read each chapter
 with that heuristic in mind: first ask what story the technique lets you tell,
 then check that the derivations honor that story.




                                       32
Modern Intelligent Systems                                                       1



Part I: Foundations and the ERM
toolbox
1 About This Book
Intelligent systems are engineered artifacts that perceive, reason, and act under
constraints. This chapter sets the shared vocabulary (historical context, core def-
initions, recurring design themes), and Figure 1 shows how the strands connect
and where to enter.
  Learning Outcomes
 After this chapter, you should be able to:
      • Explain what this book means by an intelligent system (and how that
        differs from an intelligent machine).

      • Place modern AI ideas in a brief historical context (logic,
        computation, and learning).

      • Use the book’s organizing lenses (system components, levels of
        intelligence) to interpret later chapters.

      • Navigate the book structure and reading paths using the roadmap
        figure.

   Use this chapter as a standing reference: later tools reuse the same system
vocabulary and the same habit of checking assumptions against constraints.
  Design motif
 We treat “intelligence” operationally: specify what a system represents,
 what actions it can take, and how it checks itself against objectives and
 constraints.
```

### Findings
No issues spotted.

## Chunk 4/31
- Character range: 70789–101588

```text
1.1    Historical Foundations of Intelligent Systems
A brief historical sketch helps place intelligent systems within a longer tradition
that runs from early mechanical devices, through symbolic logic and computa-
tion, to modern machine learning.



                                        33
Modern Intelligent Systems                                                       1


Mechanical Automata and Scholastic Logic In the 12th–13th centuries,
engineers such as Al-Jazari designed programmable water clocks and mechanical
automata whose gears, cams, and valves executed fixed sequences of actions. Al-
though these devices lacked learning or internal models, they embodied the idea
that artifacts could sense (via floats and levers), transform signals mechanically,
and act on their environment. In parallel, medieval scholars such as Ibn Sīnā and
Thomas Aquinas refined Aristotelian syllogistic logic, systematizing patterns of
valid inference even though a fully symbolic notation did not yet exist.

The Mechanical Computer and Early Programming In the 19th cen-
tury, Charles Babbage designed the mechanical computer now known as the
Analytical Engine. Ada Lovelace is often cited as one of the first programmers;
her notes on the Analytical Engine include an algorithm for computing Bernoulli
numbers and helped establish programming as a discipline.
    An important (and still practical) lesson from this era is the “garbage in,
garbage out” principle: if incorrect input is provided to a computational system,
the output will also be incorrect. In modern terms, this is a reminder that data
quality and validation are part of the intelligence pipeline, not an afterthought.

Mathematical Logic and Formal Reasoning The symbolic formalism
used in modern AI emerged in the 19th and early 20th centuries. Works by
George Boole (1847), Gottlob Frege (1879), Giuseppe Peano (1889), and later
Bertrand Russell and Alfred North Whitehead (1910–1913) introduced algebraic
and predicate-calculus notations that underpin automated reasoning. Formal
inference rules such as:



                       If A = B and B = C, then A = C.                       (1.1)

    This exemplifies the transitivity of equality—an example of a valid inference
rule operating on equality relations—and provides a basis for reasoning systems
that manipulate symbols according to formal rules.

The Turing Test and the Birth of AI The mid-20th century marked a
pivotal moment with Alan Turing’s proposal of the Turing Test in 1950. This


                                        34
Modern Intelligent Systems                                                     1


test was designed to assess a machine’s ability to exhibit intelligent behavior
indistinguishable from that of a human. The Turing Test shifted the focus from
mechanical computation to the broader question of machine intelligence.

Early Machine Learning and Symbolic AI Following the Turing Test,
research into machine learning and symbolic AI accelerated. In the 1950s, the
perceptron model was introduced as an early neural network capable of binary
classification. Around the same time, James Slagle developed an early influen-
tial AI program: a symbolic integration system capable of performing calculus
operations symbolically rather than numerically. This line of work anticipated
themes later formalized in decision procedures for elementary integration (Risch,
1969) and demonstrated that machines could manipulate abstract symbols to
solve problems, a core idea in symbolic AI.

Summary of Key Historical Milestones
  • 12th–13th Centuries: Mechanical automata (e.g., Al-Jazari) and
    scholastic refinements of syllogistic logic.

  • 19th Century: Charles Babbage’s Analytical Engine and Ada Lovelace’s
    pioneering programming notes; Boole and contemporaries formalize sym-
    bolic logic.

  • Early 20th Century: Frege, Peano, Russell, and Whitehead develop
    predicate calculus and logicist foundations.

  • 1950: Alan Turing’s Turing Test frames the question of machine intelli-
    gence.

  • 1950s: Development of early machine learning models (perceptrons) and
    symbolic AI programs (e.g., Slagle’s integration system).
   This historical arc sets the stage for contemporary intelligent systems: pro-
grammable artifacts whose behavior is grounded in formal models, implemented
on digital hardware, and increasingly trained or tuned from data. The sections
that follow make the working definitions and modeling assumptions explicit.




                                       35
Modern Intelligent Systems                                                      1


1.2   Defining Artificial Intelligence and Intelligent Systems
Artificial Intelligence (AI) is often misunderstood as merely a collection of pop-
ular applications such as image recognition or voice detection. However, these
are just subsets of a much broader field. Instead of defining AI by its famous
applications, it is more accurate to view AI as a body of collective algorithms,
research, and engineering practice aimed at enabling machines to perceive their
environment, perform inference, and take purposeful actions.

Core Definition of AI Following the agent-centric view of Russell and Norvig
(2021), artificial intelligence studies computational agents that map percepts to
actions through algorithms operating over explicit representations (state graphs,
feature vectors, logical predicates, or probabilistic models) subject to domain
constraints (physical limits, safety rules, resource budgets). See also Poole and
Mackworth (2017) for a complementary treatment focused on agent architec-
tures. Each model we study is evaluated on whether its assumptions support
competent perception (information acquisition), reasoning and decision-making
(information processing), and action (environment intervention), where a percept
denotes the data received at a decision epoch (a discrete sensing-and-decision
instant; e.g., sensor readings, feature vectors, linguistic tokens) and an action
denotes the command issued to the environment or downstream system.
    Many model-based systems generate hypotheses and test them, yet the
field also includes purely reactive controllers (e.g., subsumption architectures
in behavior-based robotics or PID loops) that optimize behavior without ex-
plicit hypothesis testing. Classic behavior-based robotics research (Brooks,
1986; Arkin, 1998) treats such controllers as intelligent agents. They satisfy the
perception–action cycle even in the absence of symbolic reasoning. We flag them
as boundary cases: they remain control-theoretic constructs, yet they highlight
the continuum between classical control and adaptive AI systems. Throughout
this book we discuss both deliberative reasoning (planning, inference, search)
and reflexive intelligence (engineered feedback loops that achieve goals without
symbolic reasoning), and we try to make clear which lens is being used in a
given chapter.
    For now, if we adopt a value-centric view of AI, we can characterize intelli-
gent systems by the kinds of questions they help us answer. In practice, three


                                       36
Modern Intelligent Systems                                                      1


capabilities dominate:
   • Explaining the past,

   • Understanding the present, and

   • Predicting the future.
Framed this way, the parallel with human intelligence becomes explicit: both
artificial systems and humans are judged by how well they can reconstruct what
has happened, make sense of what is happening, and anticipate what is likely to
happen next. For example, humans use memory and narrative to explain past
events, situational awareness to understand ongoing interactions, and mental
models to predict likely outcomes. Analytic systems that perform root-cause
analysis in power grids or credit-risk models in finance primarily explain the
past; monitoring systems such as anomaly detectors and online recommendation
engines focus on understanding the present; time-series forecasters and large lan-
guage models that predict the next token or utterance instantiate the predicting
the future role. Modern AI architectures often blend these roles, but keeping the
three questions in mind provides a useful lens for interpreting model behavior.
    To connect this value-centric lens to concrete designs, we now make more
precise what we mean by an intelligent system and how a design begins with a
clearly stated problem and representation.

1.3   Intelligent Systems
An intelligent system is an artificial entity composed of both software and hard-
ware components that:
   • Acquire, store, and apply knowledge,

   • Perceive and interpret environmental data to maintain situational aware-
     ness,

   • Make decisions and act based on incomplete or imperfect information.
    In contrast, an intelligent machine is usually a single embodied device (for
example, a robot arm on a factory line) whose sensing, reasoning, and actuation
are co-located. Intelligent systems can comprise multiple cooperating machines
plus cloud services; intelligent machines are one concrete realization within that
broader system-of-systems view.


                                       37
Modern Intelligent Systems                                                                 1


    This working definition is consistent with those used in cyber-physical sys-
tems literature and the IEEE Standards Association’s descriptions of intelligent
agents, emphasizing perception, cognition, and action as the three pillars of
autonomy.1
    Here, “knowledge” encompasses encoded data sets, learned model parame-
ters, rule bases, and semantic ontologies that the system can query or update
during operation. The hardware enables interaction with the environment (e.g.,
sensors, actuators), while the software performs reasoning and decision-making.

1.3.1    From value-centric questions to concrete designs
The three value-centric questions (“explain the past, understand the present,
predict the future”) only become actionable once a designer fixes a problem
statement, a representation, and the constraints under which the system oper-
ates. Rather than treating these as separate case studies, we fold them into
a compact design checklist that we reuse whenever it helps structure a design
discussion:
   1. Problem definition. State the task in operational terms. Example:
      “Detect stop signs quickly enough to enable safe braking.” The definition
      should tell us which of the three value-centric roles dominates (here: un-
      derstanding the present, plus explaining why braking events occur).

   2. Representation. Decide how the world will be encoded numerically.
      Stop-sign detection uses camera images (matrices of intensities) plus meta-
      data such as lane boundaries or GPS position; a financial recommender
      might rely on structured tabular data.

   3. Objectives and constraints. Specify the metric to optimize (e.g., mini-
      mize false negatives) and the hard constraints (minimum stopping distance,
      latency budgets, regulatory rules). Practical implementations refine these
      with regions of interest, masking, or sensor fusion (LiDAR + camera) so
      the classifier only runs where a stop sign could plausibly appear.
    These three ingredients determine what the intelligent system must sense,
infer, and control. Once they are in place we can reason about the interacting
components that implement the perception → reasoning → action loop.
   1
     Compare with the IEEE Global Initiative on Ethics of Autonomous and Intelligent Systems,
Ethically Aligned Design, 1st ed., 2019.


                                             38
Modern Intelligent Systems                                                  1


1.3.2    Components of AI Systems: Thinking, Perception, and Action
AI systems can be decomposed into three interrelated components:
Perception: How the system senses and interprets environmental data, extract-
    ing features or state estimates.

Reasoning and Decision-Making: How the system combines models and
    control policies with learned value functions to plan actions or react in
    real time.

Action: How the system executes decisions to affect the environment.

Example: Autonomous Vehicle
  • Perception: Camera captures images, which are converted into numerical
    arrays.

  • Thinking: Algorithms classify objects (e.g., stop signs, pedestrians) and
    predict future states.

  • Action: Vehicle control systems adjust steering, acceleration, or braking
    accordingly.

1.4     Case Study: AI-Enabled Camera as an Intelligent System
The design checklist above becomes concrete when we dissect a deployed system.
Consider a networked camera that detects humans and escalates alarms in an
industrial plant.




                                     39
Modern Intelligent Systems                                                       1


  Checklist instantiated for the camera system
  Problem + value role
      Detect humans entering restricted zones (understand the present)
      and log footage for later audits (explain the past).

  Representation
      Images are streamed as H × W × 3 tensors; regions of interest and
      background models are maintained to suppress noise.

  Objectives/constraints
      Maintain < 200 ms end-to-end latency and < 1% false negatives;
      respect privacy/retention policies.

  Hardware (perception/action)
      CMOS sensor, on-board DSP/accelerator, motorized pan/tilt for
      re-targeting.

  Software (reasoning)
       YOLOv8-style detector fine-tuned on site-specific data, fused with
       Kalman filters for track smoothing and MPC logic that commands
       the pan/tilt actuator or triggers alerts.

  Integration
       Edge inference handles immediate reactions; metadata is sent to a
       cloud analytics service that enriches logs and retrains models
       (predicting the future by anticipating recurrent intrusion times).

    This decomposition highlights the same three pillars—perception, reasoning,
and action—while adding the operational nuance (latency budgets, privacy con-
straints) that graduate-level systems must address. Many later chapters discuss
building blocks that could be used in such a pipeline: convolutional networks
(Chapter 11) for visual detection, recurrent models (Chapter 12) for temporal
smoothing and sequence prediction, supervised learning and calibration (Chap-
ters 3 to 4) for reliable scoring and threshold selection, fuzzy controllers (Chap-
ters 16 to 18) for rule-based escalation policies, and evolutionary algorithms
(Chapter 19) for tuning design choices such as placement, thresholds, or hyper-
parameters.


                                        40
Modern Intelligent Systems                                                       1


   An intelligent system is therefore not just the hardware or the software alone,
but the system of components working together to perceive, reason, and act
under explicit objectives.

1.5   Levels and Architectures of Intelligent Systems
Having introduced working definitions and concrete examples, we now summa-
rize capabilities and architectural patterns that reappear across the book.

What Constitutes Intelligence in Systems?            Intelligence in systems is of-
ten characterized by the ability to:
  • Perceive and interpret inputs from the environment.

  • Reason and make decisions based on available information.

  • Learn from experience to improve performance.

  • Act autonomously to achieve goals.
   These capabilities can be realized in various architectures, ranging from con-
nectionist models (e.g., neural networks) to symbolic systems and hybrid ap-
proaches.

Levels of Intelligence (as an organizing lens) Intelligence is not neces-
sarily binary (intelligent vs. non-intelligent); rather, deployed systems combine
different degrees of reactivity, deliberation, and adaptation. For the purposes of
this book we use a four-layer shorthand—reactive systems (level 1), deliberative
planners (level 2), adaptive learners (level 3), and meta-cognitive agents that
reason about their own policies (level 4)—as an informal organizing lens rather
than a strict hierarchy. It is compatible with domain-specific taxonomies (e.g.,
SAE Levels 0–5 for automated driving). The closing Key Takeaways return to
it with representative algorithms from later chapters.

Connectionist vs. agent-based/decentralized approaches Two broad
paradigms in intelligent system design are:
  • Connectionist Models: Systems structured as interconnected process-
    ing units (e.g., neural networks) with defined input-output stages.


                                       41
Modern Intelligent Systems                                                         1


  • Agent-based or decentralized systems: Collections of agents or mod-
    ules that operate semi-independently, often with only local communication,
    such as swarm intelligence or evolutionary algorithms.
   Both approaches have merits and limitations, and hybrid models often com-
bine elements of each.

Example: Swarm Intelligence Swarm systems consist of multiple agents
solving subproblems independently but collectively achieving a global objective.
Each agent follows simple rules without a global world model, yet the emergent
behavior can be intelligent. This contrasts with monolithic systems possessing
explicit internal representations.
    Swarm intelligence can be formalized via decentralized update laws of the
                                        
form xi (t + 1) = f xi (t), {xj (t)}j∈Ni , where each agent i interacts only with its
neighborhood Ni . Similar update patterns appear again in Chapter 19, but we
do not focus on stability proofs in this book.

Examples of Input and Output Variables in Dynamic Systems To
ground these ideas, consider input/output sketches from systems readers often
encounter in labs or industry. Each pairs raw sensory cues with actuator or
decision outputs.
  • Autonomous quadrotor:

        – Inputs: Inertial measurement unit (IMU) rates, barometer/altimeter,
          camera or LiDAR features, GPS fixes.
        – Outputs: Motor thrust commands and attitude setpoints that regu-
          late yaw/pitch/roll and track waypoints.

  • Smart microgrid:

        – Inputs: Load forecasts, solar/wind availability, electricity prices,
          state-of-charge estimates for batteries.
        – Outputs: Dispatch setpoints (generator outputs, battery charge/dis-
          charge, demand-response signals) that balance stability, cost, and
          emissions.

  • Building HVAC controller:

                                        42
Modern Intelligent Systems                                                       1


        – Inputs: Zone temperature/CO2 /humidity sensors, occupancy esti-
          mates, outdoor weather feeds.
        – Outputs: Fan speeds, damper positions, valve openings, heat-pump
          setpoints—tunable levers to meet comfort and energy targets.

  • Robot-assisted surgery:

        – Inputs: Endoscopic vision, force/torque sensing at instruments, sur-
          geon console commands.
        – Outputs: Precise tool trajectories, force limits, and safety interlocks
          that respect tissue constraints.

   These vignettes echo a common pattern: intelligent systems fuse hetero-
geneous sensors to produce calibrated control or decision signals under safety,
comfort, or performance constraints.
 Emotions as Utility Signals
 From a design perspective, emotions can be viewed abstractly as changes in
 an agent’s internal utility or value function: positive affect corresponds to
 utility gains, negative affect to losses, and social emotions to comparisons
 between agents’ utilities. Artificial systems can mimic this by modulating
 learning rates, exploration pressure, or safety margins in response to
 internal “frustration” or “satisfaction” signals without presupposing rich
 phenomenology. This book treats this view strictly as a modeling device
 for embedding motivational signals into controllers; affective computing
 and cognitive science work with much richer state representations than we
 use here.


Key Characteristics of Intelligent Systems Building on the examples
above, we summarize the essential capabilities that characterize an intelligent
system:
  1. Sensory Perception: The system must be able to receive and interpret
     inputs from its environment, which may be in various forms such as nu-
     merical data, images, sounds, or tactile signals.

  2. Pattern Recognition and Learning: The system should identify pat-


                                       43
Modern Intelligent Systems                                                        1


      terns within the input data, including hidden or subtle features, and im-
      prove its performance over time by learning from experience.

  3. Knowledge Retention: Acquired knowledge must be stored and utilized
     for future decision-making.

  4. Inference from Incomplete Information: The system should be ca-
     pable of drawing conclusions and making decisions even when presented
     with partial or approximate data.

  5. Adaptability: It must handle unfamiliar or novel situations by generaliz-
     ing from prior knowledge and adapting its behavior accordingly.

  6. Inductive Reasoning: The system should be able to generalize patterns
     from observed examples—i.e., infer general rules or hypotheses from spe-
     cific data instances (e.g., learn a classifier from labeled data). This differs
     from applying pre-written conditional logic; induction discovers the rules,
     whereas conditional statements merely execute them.

Intelligent Systems as Decision Makers At the core, intelligent systems
perform a mapping from inputs to outputs, where the outputs represent decisions
or actions influenced by the system’s internal understanding or model of the
environment. Formally, if we denote the input vector by x ∈ X and the output
vector by y ∈ Y, then an intelligent system implements a function

                                   y = f (x; θ),                              (1.2)

where θ represents internal parameters or knowledge that may evolve over time
through learning. This abstraction is shared by the diverse examples seen so
far: they all ingest data, transform it through a parameterized mapping, and
emit decisions or control signals. In this book we primarily use the system-level
language (mapping under constraints), and we use “machine” when embodiment
and actuation are the point. Because the chapter alternates between these view-
points, we briefly clarify terminology and the limits of the language we use.

1.6   Intelligent Systems and Intelligent Machines
Terminology Clarification


                                        44
Modern Intelligent Systems                                                       1


  • Intelligent System: A computational system (encompassing its hard-
    ware, software, and data interfaces) that perceives its environment, pro-
    cesses information, and acts autonomously or semi-autonomously (with
    limited human oversight or shared control).

  • Intelligent Machine: A physical instantiation of an intelligent system,
    often embodied as a robot or automated device.
    The terms are related but not identical; intelligent machines are a subset of
intelligent systems, typically emphasizing the physical embodiment.

Behavior, Not Components The word intelligent is inevitably anthropocen-
tric: in practice, we judge intelligence through observed behavior and perfor-
mance under constraints. Motors, sensors, and circuits are enabling components,
but they are not “intelligent” on their own. Intelligence emerges from how the
full system processes inputs, maintains state, and selects actions.
    Intelligence is also not synonymous with optimality. Many deployed systems
are approximate, noisy, or biased, yet they can still be meaningfully analyzed
and improved as goal-directed agents. In this book, “intelligent” is therefore used
in an engineering sense: a system that maps percepts to actions with a design
intent, and that can be evaluated against explicit objectives and constraints.

Examples Robots developed by Boston Dynamics (e.g., quadrupeds) illus-
trate how feedback control, state estimation, and trajectory planning can pro-
duce behaviors that humans interpret as intelligent (balance recovery, robust
locomotion, disturbance rejection) even though the system has no intrinsic un-
derstanding or feelings. Voice-activated assistants and robots provide a second
common example: they appear intelligent because they can condition actions on
language inputs, maintain limited context, and complete tasks that align with
user intent.

Consciousness and Intelligence While machines can exhibit intelligent be-
haviors, the question of whether they possess consciousness or self-awareness
remains open and is a subject of ongoing research and philosophical debate.
    In this book we treat consciousness operationally:
we focus on meta-cognition (self-monitoring of one’s own decision process) rather


                                        45
Modern Intelligent Systems                                                        1


than phenomenal awareness. This keeps the discussion tied to observable, des-
ignable behaviors rather than philosophical claims.
  Author’s note: “subject of its own thought”
 Strong machine intelligence, in my view, means a system can make itself
 the subject of its own thought. It keeps self-models (confidence monitors,
 policy auditors, explanation traces) to critique and revise its reasoning, not
 just its predictions.
 The rest of this book uses the simpler four-layer taxonomy (reactive →
 deliberative → adaptive → meta-cognitive), but the “subject of its own
 thought” view motivates why Level 4 systems need special care in design
 and governance.


1.7   Levels, Meta-cognition, and Safety
This book uses levels of intelligence as an organizing lens rather than a formal
taxonomy. The four levels introduced above (reactive, deliberative, adaptive,
and meta-cognitive) are meant to clarify what a system can do, what it must
represent, and what kinds of failures are plausible. For a working definition of
AI and intelligent systems, see Section 1.3.

Meta-cognition (Operational View) In this book, meta-cognition refers
to a controller’s ability to monitor, assess, and revise its own reasoning policies.
In practice this can look like confidence monitors, audits of decision traces, and
bounded self-correction loops rather than unconstrained self-modification.

Implications and Risks If a system can improve its own utility au-
tonomously and rapidly, it may induce competitive dynamics in which im-
proving one utility degrades another’s. This occurs in multi-agent settings
(competing organizations or robots) and in multi-objective optimization when
safety objectives conflict with performance. These scenarios motivate conserva-
tive design and governance, especially as systems move from adaptive learning
to self-monitoring and policy revision.

Designing Safe Intelligent Systems           One practical mitigation is to build
systems that:

                                        46
Modern Intelligent Systems                                                      1


   • Keep auditable records of their decisions and updates.

   • Perform self-inspection and error analysis.

   • Backtrack and self-correct within explicit, designer-defined bounds.
Such systems can improve without uncontrolled self-modification: policy up-
dates are gated by testable criteria, and any self-editing of code or reward func-
tions proceeds only through approved interfaces.

Reader’s guide. The remainder of this chapter is practical: who the book is for,
how chapters fit together, and how to navigate recurring structure. Notation
and reading conventions are collected in the front matter (see Notation and
Conventions).

1.8   Audience, Prerequisites, and Scope
This material has been rewritten to stand on its own as a book. It surveys the
design and analysis of intelligent systems along two main strands:
   • data-driven models for prediction and decision making (linear models, ker-
     nels, deep networks, sequence models, Transformers);

   • soft-computing and search methods (self-organizing maps, fuzzy systems,
     evolutionary and genetic algorithms).
The emphasis is on breadth with enough mathematical depth that you can relate
ideas across chapters rather than treating each technique in isolation.
    The book also maintains a deliberate dual emphasis: representation learning
with neural and kernelized models on one hand, and soft-computing approaches
(fuzzy systems and evolutionary optimization) on the other. This balance keeps
robustness, interpretability, and optimization themes all in view rather than
treating deep networks in isolation.
    The assumed background is undergraduate calculus and linear algebra (vec-
tors, matrices, eigenvalues) and basic probability and statistics. No prior dedi-
cated AI or machine-learning course is assumed: key ideas such as losses, opti-
mization, gradient descent, backpropagation, kernels, fuzzy operators, and evo-
lutionary operators are introduced from first principles when they first appear.
Familiarity with signals and systems, and with linear time-invariant (LTI) mod-
els in particular, is helpful for the sequence-modeling and control-oriented parts


                                       47
Modern Intelligent Systems                                                           1


of the book; Appendix A (Linear Systems Primer) provides a concise refresher.

1.9    Roadmap and Reading Paths
Figure 1 summarizes the narrative arc of the book: a core supervised path
(linear and logistic regression to MLPs to CNNs to RNNs), a branch through
competitive learning and fuzzy inference for rule-based reasoning, and a parallel
thread on optimization culminating in evolutionary computing. Early on, Chap-
ter 2 provides a complementary symbolic-search perspective so we can contrast
“intelligence via transformations” with ERM-based modeling. Chapters cross-
reference one another so you can skim the path most relevant to your project
and return for foundational refreshers as needed.
    Readers arrive with different goals. The roadmap is intentionally a depen-
dency graph rather than a single linear track; the following paths are common
starting points:
   1. ML-focused path: Chapters 3 to 4 → Chapters 6 to 7 → Chapters 11
      to 13 → Chapter 14.
```

### Findings
Issues flagged in Chunk 4/31:

1. Narrative Flow and Transition Quality:
   - The transition from the historical overview (Section 1.1) to the definitions of AI and intelligent systems (Sections 1.2 and 1.3) is somewhat abrupt. A brief bridging paragraph summarizing how the historical foundations motivate the need for precise definitions could improve flow.
   - The jump from the general definition of AI to the value-centric lens (explaining past, understanding present, predicting future) in Section 1.2 feels slightly sudden. Introducing this lens with a clearer rationale or example before listing the three capabilities would help reader orientation.

2. Reader Orientation:
   - The introduction of the “value-centric” view in Section 1.2 could be better signposted as a conceptual framework to help readers understand AI’s practical goals.
   - The “Author’s note” in Section 1.6 on “subject of its own thought” interrupts the formal tone and flow. It might be better placed as a boxed aside or footnote to maintain narrative consistency.

3. Repetitive Templating:
   - The repeated use of bullet points to list capabilities, definitions, and examples is effective but could be varied with occasional prose summaries to avoid a templated feel.
   - The phrase “perception, reasoning, and action” recurs frequently. While central, consider varying phrasing or consolidating mentions to reduce redundancy.

4. Punctuation and Spacing:
   - In Section 1.1, the line “Formal inference rules such as:” is followed by a displayed formula but lacks a complete sentence or colon usage that clearly introduces the formula. Consider rephrasing to “For example, the transitivity of equality is expressed as:”
   - In the formula line “If A = B and B = C, then A = C. (1.1)”, the period should be outside the equation number: “If A = B and B = C, then A = C (1.1).”
   - In Section 1.3.1, the bullet “Representation” includes “Stop-sign detection uses camera images (matrices of intensities) plus metadata such as lane boundaries or GPS position;” — “metadata” should be one word.
   - In Section 1.5, the line “Swarm intelligence can be formalized via decentralized update laws of the form xi (t + 1) = f xi (t), {xj (t)}j∈Ni , where each agent i interacts only with its neighborhood Ni .” has inconsistent spacing around parentheses and commas; also, the function notation is unclear and could be better formatted for clarity.
   - In Section 1.5, the bullet “Smart microgrid:” has a line break in “charge/dis- charge,” which should be “charge/discharge” without a hyphen or line break.
   - In Section 1.6, the phrase “voice-activated assistants and robots provide a second common example: they appear intelligent because they can condition actions on language inputs, maintain limited context, and complete tasks that align with user intent.” is a long sentence that could benefit from a comma after “inputs” for clarity.

5. Clarity of Prose:
   - The sentence in Section 1.2: “Many model-based systems generate hypotheses and test them, yet the field also includes purely reactive controllers (e.g., subsumption architectures in behavior-based robotics or PID loops) that optimize behavior without explicit hypothesis testing.” is complex and could be split for clarity.
   - The explanation of “emotions as utility signals” in Section 1.5 is somewhat dense and abstract. A brief example or simpler phrasing would aid comprehension.
   - The “Reader’s guide” at the end of Section 1.7 is very brief and could be expanded or integrated more smoothly into the narrative.
   - The last sentence in Section 1.9 ends abruptly with “1. ML-focused path: Chapters 3 to 4 → Chapters 6 to 7 → Chapters 11 to 13 → Chapter 14.” It appears incomplete or cut off.

No other significant issues were found.

## Chunk 5/31
- Character range: 101591–132196

```text
2. Control/systems path: Chapters 1 to 3 → Chapter 10 → Chapters 15
      to 18 → Chapter 19.

   3. Soft-computing path: Chapters 1 to 3 → Chapters 15 to 18 with op-
      tional detours to Chapter 6 and Chapter 19.

                                         Optimization     Evolutionary
                                          (GD/Reg)         (GA/GP)



       Linear              Logistic          MLP             CNN             RNN
      Regression          Regression      (Backprop)      (Conv/Pool)       (BPTT)



                                            SOM           Fuzzy Sets
                                         (Competitive)    & Inference


                   Figure 1: Roadmap (core supervised path; SOM/fuzzy;
                   optimization/evolutionary). Use it when choosing a
                   reading path and locating prerequisites before jumping
                   ahead.




                                             48
Modern Intelligent Systems                                                  1


1.10   Using and Navigating This Book
  • Before each chapter: skim the Learning Outcomes and check where it
    sits on the Roadmap.

  • While reading: follow cross-referenced figures/equations and pause at
    the short checkpoints and worked examples.

  • After each chapter: review the Summary and Common Pitfalls; revisit
    the pseudocode and attempt the Exercises.

  • Keep the front matter close: the Notation and Conventions section
    defines symbols reused throughout the book; cross-references point back
    to it when conventions matter.
Conventions and reading aids. The front matter summarizes notation and
common conventions, and it also includes a short guide to reading figures and
recurring box styles.

 Key takeaways
 Minimum viable mastery
    • Intelligent systems integrate perception, decision, and action; we
      study both model-based and control-based realizations.

    • The system–machine distinction is mostly about embodiment:
      intelligent machines are physical instances of intelligent systems.

    • “Levels” are an organizing lens, and meta-cognition is treated
      operationally (self-monitoring and bounded self-correction), not
      philosophically.

 Common pitfalls
    • Treating the roadmap as a single linear syllabus rather than a
      dependency graph of prerequisites.

    • Confusing “probability” with “decision”: many later failures come
      from thresholds and costs, not from modeling.

    • Letting notation drift: keep Appendix D close when symbols are
      reused in different chapters.


                                      49
Modern Intelligent Systems                                                      2


 Exercises and lab ideas
    • Pick one engineered system you know (e.g., a recommender, a robot,
      a control loop) and identify its percepts, internal representation, and
      actions.

    • For one section of this chapter, rewrite the core definition in your
      own words and list one concrete failure mode the definition helps you
      anticipate.

    • Choose a reading path using Figure 1, and write down which two
      chapters you will skim first (and why).

 If you are skipping ahead. Keep the operational vocabulary
 (representation, actions, objective/goal test, and audit/checks) and the
 roadmap (Figure 1) in mind; later chapters assume these as the organizing
 lens for both symbolic and data-driven tools.


Where we head next. Chapter 2 grounds this vocabulary in a compact
case study: symbolic integration as transformation search. The example shows
decomposition, safe rewrites, heuristic branching, backtracking, and residual
checks in one place; those same capabilities reappear later in data-driven set-
tings.


2 Symbolic Integration and Problem-Solving Strate-
  gies
Chapter 1 treated “intelligence” operationally: represent a problem, choose ac-
tions, and verify or correct under constraints. Here we make that concrete with
a deliberately small example—symbolic integration—where the system’s actions
are algebraic transformations. Figure 1 places this symbolic strand alongside
the data-driven path.
    We study symbolic problem solving through integration-by-transformation:
preserve meaning while rewriting an expression into a form that exposes a solu-
tion. The goal is not a catalog of tricks, but the system pattern: explicit repre-
sentations, meaning-preserving actions, heuristic branching with backtracking,


                                       50
Modern Intelligent Systems                                                            2


and a goal test that certifies correctness.
    We separate transformations into two tiers: reliable moves that never change
the antiderivative class (factoring constants, linear substitutions, polynomial
division) and heuristic moves that may succeed only for certain structures. A
practical policy is to exhaust safe steps first, then branch judiciously through
the heuristic catalog while keeping enough state to backtrack.
 Learning Outcomes
      • Decompose symbolic integration problems into safe vs. heuristic
        transformations and understand when each is appropriate.

      • Trace the transformation-tree search (state save/restore, heuristics,
        termination) and connect it to broader notions of intelligent problem
        solving.

      • Contrast symbolic transformation search with data-driven modeling
        pipelines and identify what each paradigm contributes.

 Design motif
 Meaning-preserving moves plus a mechanical check: if F (x) is proposed as
 an antiderivative of f (x), then differentiating should recover the integrand
 on the declared domain, i.e., F ′ (x) = f (x) (equivalently, F ′ (x) − f (x) = 0).


2.1    Context and Motivation
Consider the task of solving an integral of the form
                                   Z
                                     f (x) dx,

where f (x) may be a complicated function. Traditional approaches often rely
on consulting integral tables or applying well-known formulas. For example,
integrals such as            Z
                                1
                                  dx = ln |x| + C.
                                x
These are straightforward and can be solved by direct lookup or simple substi-
tution.
    However, many integrals encountered in practice do not match any entry in


                                        51
Modern Intelligent Systems                                                       2


standard integral tables, nor do they succumb easily to elementary techniques.
The integration-by-transformation view treats this as a search problem: propose
meaning-preserving rewrites, backtrack when a branch gets harder, and verify
candidates mechanically by differentiation.
 Aside: the Risch algorithm
 The Risch algorithm (Risch, 1969) decides whether an elementary
 antiderivative exists for a large class of integrands by reducing the problem
 to algebra over differential fields. Unfortunately its implementation is
 intricate, requires case explosions, and still leaves many useful
 nonelementary functions unresolved. Practical computer algebra systems
 therefore augment Risch-style decision procedures with heuristic
 transformations—the focus of this chapter—to keep runtimes bounded and
 to return human-readable answers when possible.


2.2   Problem Decomposition and Transformation
A key insight in tackling complex integrals is to reduce the problem into manage-
able subproblems. This involves applying transformations to rewrite the integral
into a form that is either directly solvable or closer to known forms.

Safe Transformations We define safe transformations as invertible substitu-
tions that allow back-substitution: if u = ϕ(x) and Fu is an antiderivative of
T [g](u), then Fu◦ϕ differentiates back to g(x). Safe transformations are algebraic
substitutions or factorings that survive reversal. Examples include:
  • Constant factor extraction: If G is an antiderivative of g, then ag has
                                                 d
    antiderivative aG; differentiating confirms dx [aG(x)] = ag(x).

  • Linear substitution: Let u = ax + b with a 6= 0. Differentiating gives
    du = a dx and hence dx = du
                              a ; substituting shows that
                             Z                       Z
                                                 1
                                 f (ax + b) dx =         f (u) du.
                                                 a

      This is the standard change-of-variables formula.

  • Polynomial division: If p(x) and q(x) are polynomials with deg p ≥


                                         52
Modern Intelligent Systems                                                       2


      deg q, then perform polynomial division:

                                  p(x)          r(x)
                                       = s(x) +      ,
                                  q(x)          q(x)

      where deg r < deg q. Linearity of integration lets us integrate s(x) term-by-
                                       r(x)
      term, while the proper fraction q(x)  can be addressed via partial fractions
      or further substitutions, yielding an equivalent antiderivative.
    These transformations are safe because they always preserve the integral’s
value and simplify the problem without introducing ambiguity. When a substi-
                                                    R1
tution transforms an integral over x ∈ [0, 1] into 0 ub (1 − u)c du with b, c > −1,
the resulting definite integral evaluates to a Beta function B(b+1, c+1); the Beta
identity applies to that definite integral on [0, 1], and it is therefore customary
to fall back on it when an elementary antiderivative is unavailable.

Example: Applying Safe Transformations Suppose we have an integral
of the form            Z
                         a · xb (1 − x)c dx,

where a, b, c are constants. A safe transformation might be to factor out the
constant a and then consider substitutions or binomial expansions that reduce
the powers to known integrals (e.g., Beta-function evaluations when b and c are
integers).

2.3   Limitations of Safe Transformations
After exhaustively applying all safe transformations, we may still encounter in-
tegrals that do not match any known solvable form. At this point, the system
must decide whether the problem is solvable by known methods or if alternative
strategies are necessary.

2.4   Heuristic Transformations
When safe transformations fail to yield a solution, we turn to heuristic transfor-
mations, which are not guaranteed to succeed but often provide a path forward.
These heuristics are based on experience, pattern recognition, and mathematical
intuition.



                                        53
Modern Intelligent Systems                                                        2


Definition Heuristic transformations are problem-solving tricks or strategies
that attempt to rewrite the integral into a solvable form by exploiting structural
properties of the integrand. They may involve:
   • Trigonometric identities and substitutions, e.g., using relationships among
     sin x, cos x, tan x, cot x, sec x, and csc x.

   • Algebraic manipulations that simplify complicated expressions.

   • Variable substitutions that transform the integral into a standard form.

   • Recognizing patterns such as functions of 10x or other scaled arguments
     and applying appropriate scaling substitutions (e.g., if the integrand con-
     tains f (cx), introduce u = cx so that the scale factor is absorbed).

Example: Trigonometric Heuristics Consider an integral involving sine
and cosine:               Z
                             sin x
                                   dx.
                            cos x
Recognizing that sin x/ cos x = tan x, we can rewrite the integral as
                         Z
                            tan x dx = − ln | cos x| + C.

which is a standard integral with the constant of integration explicitly noted.
   Similarly, if the integrand involves expressions like sin2 x + cos2 x, we can use
the Pythagorean identity to simplify.

Heuristics as a Form of Intelligence The use of heuristic transformations
reflects a form of mathematical intelligence: the ability to recognize patterns,
apply non-obvious substitutions, and creatively manipulate expressions to reach
a solution. Unlike safe transformations, heuristics may fail or lead to dead ends,
but they expand the problem-solving repertoire beyond mechanical procedures.




                                        54
Modern Intelligent Systems                                                       2


  Absolute values and branches
      • Square roots: specify the sign/branch. If you drop | · |, restrict the
        substitution intervalpso the sign is fixed (e.g., cos y ≥ 0 on
        y ∈ (−π/2, π/2) so 1 − sin2 y = cos y).

      • Logarithms: default to log |f (x)| unless you guarantee f keeps one
        sign on the declared domain.

      • Arctrig/hyperbolic inverses: state principal values and any
        periodicity you rely on for back-substitution.


2.5    Summary of the Approach
The overall strategy for symbolic integration can be summarized as follows:
   1. Apply all safe transformations to simplify the integral and attempt to
      match known solvable forms.

   2. Re-evaluate the transformed integrand to identify structural cues
      (symmetry, polynomial degree, trigonometric patterns).

   3. Choose among multiple transformation paths by comparing simple
      cost heuristics such as expression-tree depth, number of nonzero coeﬀi-
      cients, or anticipated integration rules.

   4. Fallback to heuristics and backtracking when safe transformations
      stall, maintaining a stack of previous states to enable systematic explo-
      ration.

Cost heuristic. Score candidates by a triple: tree depth, number of nonlinear
operators, and symbol count. The nonlinearity term counts transcendental nodes
(e.g., trigonometric, exponential, logarithmic), while the symbol count tallies
AST nodes excluding simple literals such as −1, 0, 1. Prefer branches that reduce
or preserve this triple, and break ties toward rules with known templates (e.g.,
partial fractions, reduction formulas).




                                       55
Modern Intelligent Systems                                                      2


2.6   Heuristic Transformations: Revisiting the Integral with 1 −
      x2
Recall the integral under consideration:
                               Z
                                       4
                                               dx.                           (2.1)
                                  (1 − x2 )5/2

    For real-valued integration we restrict attention to |x| < 1, ensuring the
denominator (1 − x2 )5/2 is well-defined and nonzero on the interval of interest.
    When encountering expressions involving 1 − x2 , a classical heuristic substi-
tution is:
                                    x = sin y,

which leverages the Pythagorean identity:

                               1 − sin2 y = cos2 y.

   Applying this substitution transforms the integral into a trigonometric form
that is often easier to handle.

Step 1: Substitution and Differential Set

                        x = sin y   =⇒      dx = cos y dy.
                                      
We take y = arcsin x with y ∈ − π2 , π2 so that the substitution remains
                                                                    p bijective
on the domain |x| ≤ 1, and note cos y ≥ 0 on this interval so that 1 − sin2 y =
cos y is consistent with the chosen branch.
    Substituting into (2.1) and using dx = cos y dy yields
                   Z                   Z
                          4                       4
                                  dx =                     cos y dy
                     (1 − x )
                            2 5/2          (1 − sin2 y)5/2
                                       Z
                                             4 cos y
                                     =                 dy
                                           (cos2 y)5/2
                                         Z
                                     = 4 cos−4 y dy
                                         Z
                                     = 4 sec4 y dy.



                                       56
Modern Intelligent Systems                                                     2


The intermediate step cos y · cos−5 y = cos−4 y is made explicit so the exponent
arithmetic is transparent.
    Thus, the integral reduces to
                                   Z
                                  4 sec4 y dy.                              (2.2)


Step 2: Choosing the Next Transformation At this stage, two common
safe transformations are available:
  • Express sec4 y in terms of tan y, using the identity sec2 y = 1 + tan2 y, and
    then perform substitution u = tan y with du = sec2 y dy.

  • Use reduction formulas for powers of secant directly, e.g.,
             Z                                     Z
                   n        secn−2 y tan y n − 2
                 sec y dy =               +            secn−2 y dy,   n > 1.
                                n−1         n−1

Standard reduction formulas provide a deterministic alternative if the substitu-
tion path is judged too costly.
    The choice between these paths is nontrivial, especially for an automated
system. Humans often pick the substitution u = tan y intuitively because it
simplifies the integral, but a machine requires a deterministic decision rule.

Step 3: Functional Composition and Path Selection To automate the
choice, the system evaluates the functional composition of the integral expres-
sions along each path (e.g., measuring expression-tree depth, symbolic coeﬀicient
growth, or the number of distinct functions involved):
  • Path 1: Substitution u = tan y reduces the integral to a polynomial in u,
    which is straightforward to integrate.

  • Path 2: Direct reduction of sec4 y may involve more complex recursive
    steps.
    From a cost perspective, Path 1 is cheaper and more direct, so the system
prioritizes it. However, if this path fails to yield a solution, the system must
backtrack and attempt Path 2.




                                       57
Modern Intelligent Systems                                                       2


Two safe options from here
   • (a) Substitution u = tan y. Since sec4 y dy = sec2 y (sec2 y dy) and
     sec2 y = 1 + tan2 y, set u = tan y, du = sec2 y dy:
                          Z               Z
                        4 sec4 y dy = 4 (1 + u2 ) du
                                               3
                                                  
                                     = 4 u + u3 + C

                                      = 4 tan y + 43 tan3 y + C.

   • (b) Reduction formula. For even n > 1,
                 Z                                   Z
                               secn−2 y tan y n − 2
                     secn y dy =             +          secn−2 y dy.
                                   n−1         n−1
                                      R
      Applying this with n = 4 gives sec4 y dy = tan y + 31 tan3 y + C, repro-
      ducing the same primitive without the u-substitution.

                                                     x
Back-substitution and check Using tan y = √                , both paths yield:
                                                   1 − x2
                                                        
                                  2 −1/2        x3
                 F (x) = 4 x(1 − x )     +                 + C.
                                           3(1 − x2 )3/2

Differentiating term by term shows F ′ (x) = 4(1 − x2 )−5/2 on |x| < 1. Outside
(−1, 1) the principal-branch integrand is complex-valued; a real continuation
                        R
rewrites the integral as 4(x2 − 1)−5/2 dx with x = cosh t.

                                         R
Pattern rule For integrals of the form (1−x2 )−k−1/2 dx, the substitution x =
                      R
sin y reduces them to sec2k y dy; apply the even-power reduction accordingly.
This is why the 1 − x2 pattern triggers the trigonometric branch.

2.7   Example: Solving an Integral via Transformation Trees
The worked integral above shows how the search explored multiple branches
(e.g., x = sin y vs. x = tanh u) while respecting the declared domain. Heuristic
branches that do not fit the domain are pruned; competing safe branches (substi-
tution vs. reduction) converge to the same antiderivative. The key insight is that



                                       58
Modern Intelligent Systems                                                        2


solving integrals can be viewed as traversing a decision tree of transformations,
with goal tests supplied by residual checks and domain conditions.

2.8   Transformation Trees and Search Strategies
Definition: A transformation tree is a conceptual structure representing
all possible sequences of transformations applied to an expression in an attempt
to solve or simplify it.
  • Each node corresponds to a state of the expression.

  • Edges correspond to transformations (safe or heuristic).

   • Leaves correspond to either solved expressions or dead ends (no solution).
                                                  R
    Figure 2 shows the actual tree explored for (1−x42 )5/2 dx. Solid branches de-
note safe algebraic steps (guaranteed progress), while dashed branches illustrate
heuristic substitutions that may fail and trigger backtracking. Computer algebra
systems follow similar playbooks (Bronstein, 2005; Risch, 1969): a Risch-style
decision core handles provably solvable cases, while a curated bank of heuris-
tics (pattern rewrites, rational substitutions, special-function fallbacks) explores
auxiliary branches with explicit depth/time budgets.

Example: For the integral problem, the root node is the original integral.
From there, we branch into applying different substitutions or algebraic manip-
ulations, such as

         Apply substitution u = tan(x) ⇒ integration by parts
                                          ⇒ inverse trig identities ⇒ · · ·

Safe vs. Heuristic Transformations:
  • Safe transformations are guaranteed to preserve equivalence and
    progress towards a solution.

  • Heuristic transformations may or may not lead to a solution; they
    are attempts that carry risk but can be beneficial.

Backtracking: If a branch leads to no solution, the system must backtrack to
a previous node and try alternative transformations. This requires the ability

                                        59
Modern Intelligent Systems                                                                                               2


                                                               Z                       [S]
                                                                        4
                                                                                dx
                                                                   (1 − x2 )5/2




                                                        [S]
                                    Factor constants                                                                   [H]
                                    restrict |x| < 1                                               Let u = 1 − x2




                                                                      [H]                                              [H]
                                          [H]     Try x = tanh u                                    Heuristic stalls
                   Substitute x = sin y
                                                  (hyperbolic twin)                                   backtrack




                          [S]               R         [S]
      Use dx = cos y dy          Reduce to 4 sec4 y dy




                                                                                             Labels [S] and [H]
                                                Safe move[S]            Heuristic[H]
                                                                                             indicate strategy



          Figure 2: Transformation tree for the running example integral; badges
         [S]/[H] mark safe vs. heuristic moves; the dashed branch mirrors the sine
         substitution. Use it when diagnosing where a solve attempt branched and
                               why backtracking was required.


to:
      • Freeze the current state before branching.

      • Restore previous states upon failure (e.g., by pushing serialized expression
        trees and associated metadata onto a stack for later reinstatement).
In practice this corresponds to pushing serialized expression trees (i.e., deep
copies of the tree structure together with any transformation metadata) onto a
stack so they can be reinstated after unsuccessful exploratory steps.

2.9      Algorithmic Outline for Symbolic Problem Solving
The general algorithm for solving symbolic problems such as integrals can be
summarized as follows:


                                                        60
Modern Intelligent Systems                                                 2


  1. Define the goal: For example, express the integral in terms of known
     functions from a table.

  2. Enumerate transformations: List all possible safe and heuristic trans-
     formations applicable to the current expression.

  3. Apply safe transformations: Attempt all safe transformations and
     check if the problem is solved.

  4. If not solved, apply heuristic transformations: Attempt heuristic
     transformations to explore alternative paths; common template hits in-
           R                                     R
     clude f ′ (x)/f (x) dx → log |f (x)| + C and r′ (x)er(x) dx → er(x) + C.

  5. Branch and backtrack: For each transformation, branch the search tree.
     If a branch fails, backtrack and try other branches.

  6. Use heuristics to guide search: For example, use functional composi-
     tion depth or cost metrics to prioritize branches.

  7. Terminate cleanly: Stop when a closed-form antiderivative is found, or
     when depth/time budgets are exceeded without success; optional numeric
     residual tests can accept approximate solutions.

Note: This approach resembles a greedy search with backtracking, but it does
not guarantee an optimal or even successful solution in all cases.
 Transformation-tree search (pseudocode)
 function SolveIntegral(f0,
                        domain=(-1,1),
                        depth_limit=8,
                        time_limit=2s,
                        eps_abs=1e-6,
                        eps_rel=1e-6,
                        samples=24):
     stack <- [(f0, domain, empty_history, depth=0)]
     start <- clock()
     best <- {status="fail",
               F=None,
               residual=None,
               history=[],
               domain=domain}



                                      61
Modern Intelligent Systems                                                           2


      while stack not empty:
          current, dom, history, depth <- pop(stack)
          if clock() - start > time_limit
             or depth > depth_limit:
              continue
          if passes_residual_test(current, f0, dom,
                                   eps_abs, eps_rel, samples):
              res = residual(current, f0, dom, samples)
              return {status="closed_form",
                       F=current,
                       residual=res,
                       history=history,
                       domain=dom}
          safe, heuristic <- enumerate_transforms(current, dom)
          for T in safe:
              g, new_dom <- apply(T, current, dom)
              push(stack,
                   (g, new_dom, history + [T], depth+1))
          for H in heuristic (ordered by cost)
               when depth+1 <= depth_limit:
              g, new_dom <- apply(H, current, dom)
              push(stack,
                   (g, new_dom, history + [H], depth+1))
      return best


 The pseudocode mirrors the narrative: record the original integrand f0 ,
 track the current domain/branch, apply safe transforms eagerly, explore
 heuristic branches within time/depth budgets, and only accept a candidate
 antiderivative once a sampled residual check (absolute or relative) passes
 on points inside the declared domain; return a clear status/history/domain
 either way.

 Residual test implementation. At each candidate F , sample K points
 inside the current domain but away from singularities and branch points,
 and form R = maxi |F ′ (xi ) − f0 (xi )|. Accept if R ≤ εabs or
 R/(1 + maxi |f0 (xi )|) ≤ εrel . Automatic differentiation or a high-order finite
                          √
 difference (step h = O( εmachine )) keeps the check numerically stable. As
 substitutions shrink the domain, shrink the sample set and log the updated
 interval alongside the history.


                                        62
Modern Intelligent Systems                                                            2


 Termination policies and numeric fallbacks
    • Budgeting: Cap depth, number of heuristic branches, and runtime
      (e.g., depth limit D = 8, two-second wall clock). When limits are
      reached, report “no elementary antiderivative within budget D”
      rather than looping forever.

    • Residual checks: Differentiate candidate antiderivatives
      symbolically and numerically. Sample points inside the declared
      domain (away from poles) and accept only if
      maxi |F ′ (xi ) − f (xi )| ≤ εabs or the relative tolerance passes; otherwise
      prune or refine before returning.

    • Numeric escape hatch: Switch to adaptive quadrature (e.g.,
      Gauss–Kronrod) once symbolic attempts fail; return both the
      numeric estimate and the failed transformation history so users can
      adjust heuristics, noting that the numeric value is not a closed form.

    • Domain reminders: When substitutions shrink domains (e.g.,
      x = sin y enforces |x| ≤ 1), log the restriction and branch choice so
      the numeric fallback samples within the valid range and the report is
      reproducible.
```

### Findings
- The initial list of reading paths (Control/systems path and Soft-computing path) uses arrows (→) inconsistently with spacing and line breaks, which slightly disrupts flow. Consider reformatting for clarity and consistency.

- The figure caption for Figure 1 is somewhat terse and could better orient the reader by briefly explaining the diagram’s components or purpose beyond just "Use it when choosing a reading path and locating prerequisites before jumping ahead."

- In the bullet list under "Using and Navigating This Book," the phrase "Keep the front matter close" is slightly informal; consider rephrasing to "Refer to the front matter frequently" for a more formal tone.

- The "Key takeaways" section uses a nested bullet style that is somewhat inconsistent (e.g., "Minimum viable mastery" is not clearly distinguished as a heading or bullet). Clarify hierarchy or formatting.

- The "Common pitfalls" section includes the phrase "keep Appendix D close," which is informal; consider "refer to Appendix D frequently."

- In the "Exercises and lab ideas," the phrase "Pick one engineered system you know" is informal; consider "Select an engineered system you are familiar with."

- The transition from the introductory material to Chapter 2 is abrupt. The sentence "Where we head next..." could be better integrated with a clearer transition or subheading.

- The phrase "Chapter 1 treated 'intelligence' operationally" assumes the reader remembers Chapter 1 well; a brief recap or pointer would help orientation.

- The explanation of safe transformations is dense and could benefit from clearer subheadings or numbered lists to improve readability.

- The example integral expressions sometimes use inline math with inconsistent spacing around integral signs and limits (e.g., "∫ 1 dx/x = ln|x| + C" vs. "∫ f(x) dx"). Standardize integral notation spacing.

- The "Aside: the Risch algorithm" is informative but interrupts flow; consider placing it in a sidebar or footnote.

- The explanation of polynomial division includes a formula with unclear formatting: "p(x)/q(x) = s(x) + r(x)/q(x)"—the fraction formatting is inconsistent and could be clearer.

- The paragraph starting with "These transformations are safe because..." contains a long sentence with embedded notation that is hard to parse; consider breaking it into shorter sentences.

- The example applying safe transformations is somewhat abstract; adding a concrete numeric example would improve clarity.

- The "Limitations of Safe Transformations" section is brief and could better connect to the following heuristic transformations section with a clearer transition.

- The heuristic transformations section lists examples but lacks consistent formatting (bullets vs. inline). Standardize for clarity.

- The example of the integral involving sin x / cos x is helpful but the equation "∫ tan x dx = -ln|cos x| + C" is presented without intermediate steps; adding a brief derivation would aid understanding.

- The "Heuristics as a Form of Intelligence" paragraph is somewhat philosophical and could be better linked to the practical algorithmic content.

- The "Absolute values and branches" section uses bullet points but the first bullet is a fragment ("Square roots: specify the sign/branch."); consider rephrasing for grammatical completeness.

- The explanation of the Beta function and domain restrictions is dense and could be clarified with a brief example or figure.

- The stepwise worked example of the integral with substitution x = sin y is detailed but includes some formatting inconsistencies, such as the use of " " symbols after "dx = cos y dy." These appear to be artifacts and should be removed.

- The explanation of the substitution domain and branch choices is good but could be more explicitly connected to the earlier discussion of domain restrictions.

- The intermediate algebraic steps (e.g., cos y · cos^{-5} y = cos^{-4} y) are helpful but could be better highlighted or boxed for emphasis.

- The two safe options for further integration (substitution u = tan y and reduction formula) are presented with formulas that have inconsistent spacing and notation (e.g., "4 (1 + u^2) du" vs. "tan y + 31 tan^3 y + C" where "31" likely should be "3/1" or "3/1" is a typo).

- The back-substitution formula for F(x) includes notation "√ x / (1 - x^2)" that is ambiguous; clarify the square root placement and fraction.

- The paragraph about differentiating term by term to verify correctness is good but could be expanded slightly to explain the process for readers less familiar with symbolic differentiation.

- The "Pattern rule" paragraph is dense and could be better separated or highlighted as a boxed note.

- The description of transformation trees and search strategies is clear but the figure reference (Figure 2) would benefit from a more descriptive caption explaining the figure’s components and how to interpret the [S]/[H] labels.

- The pseudocode is well aligned with the narrative but would benefit from consistent indentation and spacing for readability (e.g., the "for H in heuristic (ordered by cost)" line is awkwardly broken).

- The pseudocode uses a mix of symbols and words (e.g., "<-" and "=") inconsistently; standardize assignment operators.

- The residual test implementation is detailed but could be clearer by separating the explanation of absolute and relative tolerances into distinct sentences.

- The "Termination policies and numeric fallbacks" section is comprehensive but could be better organized with subheadings or bullet points for each policy.

- Overall, the chunk is dense with technical content and would benefit from more frequent subheadings, clearer transitions between sections, and consistent formatting of mathematical expressions and code.

No other concrete issues spotted.

## Chunk 6/31
- Character range: 132201–162701

```text
Worked example: Beta template vs. numeric fallback Consider the
Beta integral
                              Z 1
                  I(a, b) =         xa−1 (1 − x)b−1 dx,   a, b > 0.
                               0

Safe transformations (factor constants, recognize the Beta template) immedi-
ately identify the elementary value B(a, b) = Γ(a)Γ(b)/Γ(a + b). By contrast,
the perturbed integral
                        Z 1
                              xa−1 (1 − x)b−1 log(1 + x) dx
                          0

fails the template check after all safe moves. The solver therefore (i) records
the unmet template, (ii) pushes a heuristic branch such as differentiation under


                                            63
Modern Intelligent Systems                                                              2


   Table 1: Table: Transformation toolkit (safe vs. heuristic). Preconditions keep
    domains/branches explicit (e.g., restrictions like “x in (-1,1)” for square-root
                   expressions); principal branches unless noted.

                       Safe                              Heuristic
                       R              R
 Constant factor         a g(x) dx = a g(x) dx (no       Completing the square
                       domain change).                   before attempting trig
                                                         substitutions; track any
                                                         resulting branch cuts.
 Linear substitution   u = ax + b, dx = du/a with        Trigonometric substitutions
                       a 6= 0, invertible on the         x = sin u, x = tan u, t =
                       stated interval.                  tan(x/2) with domains
                                                         u ∈ (− π2 , π2 ) or stated
                                                         principal branches.
 Polynomial            Split improper rational           Rationalising substitutions
 division / partial    functions into polynomial +       such as x = 1/u or x = u2 to
 fractions             proper fraction where             expose hidden symmetry;
                       denominators stay nonzero         avoid zeros/poles introduced
                       on
                       R the    domain.                  by the map.
 Log-derivative          f ′ (x)/f (x) dx =              Template lookups
 pattern               log |f (x)| + C when f (x) 6= 0   (Beta/Gamma forms with
                       on the domain.                    parameter sign conditions,
                                                         exponential-times-
                                                         polynomial motifs, etc.).


the integral sign, and (iii) if the branch exceeds time/depth budgets, falls back
to adaptive quadrature with the reported residual |Inumeric − Icandidate |. This
concrete pattern—try Beta/Gamma reduction, else return a certified numeric
answer—embodies the policy described in the termination box.

Failure path with certified numeric residual. Setting a = 32 , b = 2 in the
perturbed integral above illustrates the full fallback. Safe moves reduce the plain
Beta integral to B(3/2, 2) = 4/15, but the extra log(1 + x) term triggers every
heuristic branch (integration by parts, differentiation under the integral sign,
series expansion) without yielding a closed form before the default depth limit
D = 8. The solver then hands the integrand to an adaptive Gauss–Kronrod
routine, which returns Inumeric ≈ 0.0915453885 with an internal error certificate
< 3 × 10−7 ; this is a certified quadrature value rather than a closed form. The




                                          64
Modern Intelligent Systems                                                        2


residual check
                       |Inumeric − Iprevious refine | ≤ 3 × 10−7

is attached to the report along with the failed transformation history, making it
explicit that no elementary antiderivative was located within the allotted budget
even though a numerically reliable answer exists.

2.10    Discussion: What this example illustrates
Under the operational framing in Chapter 1, the integrator exhibits several in-
gredients associated with intelligent problem solving: it maintains an explicit
state (the current expression), chooses actions (transformations), manages con-
tingencies (branching and backtracking), and verifies results with a crisp goal
test (differentiate and check the residual). At the same time, it is limited: it
does not learn new transformations from data, and its effectiveness depends on
a human-designed library of moves and heuristics.
                                                                              R
    Not every heuristic is helpful. For instance, applying x = tan y to (1 +
x2 )3/2 dx looks attractive because 1 + tan2 y = sec2 y, yet it transforms the prob-
          R
lem into sec5 y dy, which is more complicated than the original integral. In a
transformation-tree implementation this branch simply backtracks and explores
alternatives (e.g., x = tanh u for |x| < 1 or x = cosh u for |x| > 1), underscoring
why explicit search discipline and residual checks are essential.
    This contrast helps position the data-driven chapters that follow, where the
system’s “actions” are parameter updates guided by loss functions and validation
checks.

Connection to statistical learning. Symbolic integration is a clean play-
ground for thinking about representations, action sequences, and verification.
In data-driven modeling, the objects change (datasets, models, and losses), but
the system-level pattern is similar: choose a hypothesis class, optimize an objec-
tive under resource constraints, and validate that the result generalizes.




                                          65
Modern Intelligent Systems                                                      2


 Connection: transformation search vs. empirical risk minimization
    • Goal test: residual check maxx∈S |F ′ − f | ≤ ε vs. performance on
      held-out data.

    • Inductive bias: safe/heuristic precedence vs. model class and
      regularization that shape what is learnable.

    • Budget: depth/time limits vs. compute/epoch budgets and early
      stopping.

 Key takeaways
 Minimum viable mastery
    • Symbolic integration is a compact example of a goal-driven system:
      represent state, apply meaning-preserving actions, and verify
      outcomes.

    • Safe moves encode guaranteed transformations; heuristic moves trade
      certainty for coverage and require backtracking discipline.

    • Residual checks act as a crisp goal test: differentiate a candidate and
      measure whether it agrees with the original integrand on the declared
      domain.

 Common pitfalls
    • Losing the system-level point in calculus detail: always name the
      state, action, heuristic, and goal test.

    • Ignoring domains/branches: substitutions can shrink domains,
      introduce branch cuts, and invalidate a “correct” algebraic rewrite.

    • Treating heuristics as proofs: heuristic branches must be verified (or
      backtracked), not trusted.




                                      66
Modern Intelligent Systems                                                      3


  Exercises and lab ideas
    • Implement a minimal example from this chapter and visualize
      intermediate quantities (plots or diagnostics) to match the
      pseudocode.

    • Stress-test a key hyperparameter or design choice discussed here and
      report the effect on validation performance or stability.

    • Re-derive one core equation or update rule by hand and check it
      numerically against your implementation.

  If you are skipping ahead. Keep the pattern vocabulary: safe vs.
  heuristic moves, explicit budgets, and residual/verification checks. The
  data-driven chapters reuse the same discipline (objective, constraints, and
  validation) even though the “actions” become parameter updates.



Where we head next. For the data-driven thread (datasets, objectives, di-
agnostics, classification), continue to Chapters 3 and 4. For nonlinear function
classes and nonconvex training dynamics, continue through Chapters 5 to 6 and
the chapters that follow.


3 Supervised Learning Foundations
Chapter 2 illustrated a non-statistical lens: solve problems by transformation
search, with explicit goal tests. Here we shift to the data-driven lens. Figure 1
marks this as the core supervised strand.
    When a mapping is known, we use the formula: Celsius and Fahrenheit are
linked by a simple rule, and many physical laws give direct input–output rela-
tionships. The problems that motivate machine learning do not. The mapping is
unknown, messy, or only partially understood, so we settle for an approximation.
That approximation might be statistical (learned from data), rule-based (en-
coded from experience), biologically inspired (neural computation), behavioral
(fuzzy rules), or evolutionary (search over candidate solutions). This chapter
focuses on the statistical, data-driven strand: supervised learning.
    In this lens, supervised learning is prediction and inference: given evidence


                                       67
Modern Intelligent Systems                                                          3


x, estimate an output y that you can act on or audit. Other modeling goals exist
(summarizing structure, compressing representations, discovering clusters), but
supervised learning is the cleanest place to learn how to fit models, compare
alternatives, and check whether apparent success is real or just memorization.
    Supervised learning begins with three commitments: choose a functional
form that can plausibly approximate the mapping, collect paired examples of
inputs and outputs, and define a quantitative measure of “how wrong” a predic-
tion is. Once those are in place, training adjusts model parameters so predictions
align with observed outputs.
    The word fitting is meant literally. In classical curve fitting—and in practical
settings like sensor calibration—we choose parameters so a predicted curve (or
surface) passes near measured points. Keep the camera thread from Chapter 1
in mind: a camera system is useful because it can predict something actionable
from what it senses. A simple example is exposure calibration: we collect scenes
with known reference targets, measure raw sensor readouts x, and learn parame-
ters that map those readouts to a correction y so the system produces consistent
brightness across conditions. The same pattern repeats at higher levels (object
detection scores, tracking signals, alert decisions): the details change, but the
core act is the same—use paired input/output examples to fit parameters that
make predictions reliable.
    This chapter builds the supervised-learning toolkit around that central act.
We first make the pieces explicit (data, models, and losses), then show what
training looks like when it succeeds and when it fails (underfitting vs. overfitting).
Next we formalize ERM and the main “anti-memorization” tools (regularization
and validation). Finally, we work through linear regression as the first fully
transparent case study where the entire pipeline is visible end to end.




                                         68
Modern Intelligent Systems                                                        3


  Learning Outcomes
     • Formalize datasets, hypotheses, and empirical risk minimization
       (ERM) with consistent notation used in Chapters 3 to 4.

     • Compare common regression/classification losses and regularizers,
       understanding when to prefer each.

     • Diagnose under/overfitting with data splits, learning curves, and
       bias–variance reasoning; use these diagnostics to guide model
       selection and regularization.

  Design motif
  Data → model → objective → audit. This workflow shows up repeatedly in
  later chapters, even when the models become deeper and the optimization
  less forgiving.

Before we turn the “fitting” story into equations, let us fix the handful of symbols
we will reuse for several pages. The goal is not to introduce new notation, but
to keep the derivations readable while the ideas are still new.
   • Data X ∈ RN ×d with rows x⊤   i ; targets yi ∈ R for regression and yi ∈ {0, 1}
     for binary classification. The aﬀine map y±1 = 2y −1 switches to {−1, +1}
     when margin-based expressions are convenient.

   • Parameters θ (model-specific), weights w ∈ Rd ; predictions carry hats:
     ŷi = hθ (xi ), ŷ = Xw.

   • The loss ℓ(ŷ, y) is the teacher’s grading rubric; the objective aggregates
     losses over data and adds regularization. Parameters are learned from
     data; hyperparameters (e.g., λ in regularization) are chosen by validation.

   • Noise uses ε; residuals use e = y − ŷ. Vectors are bold lowercase, matrices
     bold uppercase; scalars are italic.

   • Bias absorption (when used): augmented feature x̃ = [x; 1] with corre-
     sponding augmented weights.




                                        69
Modern Intelligent Systems                                                        3


3.1   Problem Setup and Notation
We observe a dataset D = {(xi , yi )}N
                                     i=1 drawn i.i.d. from an unknown distribu-
tion P on the input–output space X × Y. A hypothesis (model) hθ : X → Y
with parameters θ produces predictions ŷi = hθ (xi ). A pointwise loss function
ℓ(ŷ, y) measures the penalty incurred by predicting ŷ when the true label is y.
     The population risk and empirical risk associated with hθ are
                                                         
                             R(hθ ) = E(x,y)∼P ℓ hθ (x), y ,                  (3.1)
                                      1 X               
                                         N
                        R̂N (hθ ) =       ℓ hθ (xi ), yi .                    (3.2)
                                      N
                                         i=1

Because P is unknown, learning algorithms minimize empirical proxies of R(hθ ).
This is the formal version of the “educated guess” idea: we posit a model family
hθ , then use data to choose parameter values that make its predictions behave
like the measured input–output pairs. In practice we do this on a training set
(the data used to fit parameters), and we reserve held-out data to check whether
the fitted model is trustworthy; Section 3.6 makes these evaluation protocols
precise.

3.2   Fitting, Overfitting, and Underfitting
Fitting is the act of choosing parameters θ so a model’s predictions match ob-
served data. Concretely, we pick a loss ℓ, evaluate it on examples (xi , yi ), and
use an optimization method to search for parameters that make the aggregate
loss small. This is what practitioners usually mean by training.
    It helps to picture training as repeated adjustment under feedback. You make
a prediction, measure the mistake with a loss, update parameters to reduce that
mistake, and repeat. In sensor calibration, this feels familiar: if your measured
output is consistently off, you change a gain or offset; if it is noisy, you adjust
how aggressively you trust any one reading. Supervised learning packages that
intuition into a general recipe that can be reused across problems.
    The goal is not to “fit the training set” as an end in itself. A good fit is one
that holds up on new data: the fitted model should behave sensibly on inputs it
has not seen. When fitting fails, it tends to fail in one of two recognizable ways.




                                          70
Modern Intelligent Systems                                                           3


Underfitting. The model family is too rigid for the task, the features do not
contain enough information, or the optimization did not do its job. This is the
student who cannot solve the practice problems before the exam: the mismatch
is obvious even on the training set. The remedy is to change the representation
or the hypothesis class, improve the data, or fix the optimization.

Overfitting. The model is flexible enough to match the training set by mem-
orizing its quirks. This is the student who memorizes the worked examples so
well that a small twist on the exam causes failure. Overfitting can look like
success until you test on held-out data.

What we aim for. We want a well-fitted model: low training error and com-
parable validation/test error. The tools below are designed to keep that distinc-
tion visible: objectives (losses and regularizers), validation protocols (splits and
cross-validation), and diagnostics (learning curves and bias–variance reasoning).

                             underfit
                              Training error           good fit        overfit
            Error on data




                            (high bias) error
                              Validation                           (high variance)




                                                best validation


                                                Model complexity

        Figure 3: Underfitting and overfitting as a function of model complexity.
        Training error typically decreases with complexity, while validation error
      often has a U-shape. Regularization and model selection aim to operate near
       the minimum of the validation curve. Use it when deciding whether to add
                        capacity, add data, or add regularization.

   Figure 3 is the baseline bias-variance diagnostic used throughout the chapter.

3.3    Empirical Risk Minimization and Regularization
To make the informal idea of “fitting” mathematically precise, we choose an
objective and minimize it. The supervised-learning baseline is empirical risk
minimization: minimize the average loss on the training data.



                                                       71
Modern Intelligent Systems                                                           3


    This is the first place where the chapter’s opening promises become concrete.
If we do not know the true input–output law, we still need a disciplined way to
compare candidate models and to say whether one parameter choice is better
than another. The loss plays the role of the teacher’s rubric, and ERM is the
simplest way to aggregate that rubric over many examples: instead of arguing
about one example at a time, we ask for parameters that perform well on average
across the dataset.
    The empirical risk minimizer (ERM) selects

                             θ̂ERM = arg min R̂N (hθ ).                           (3.3)
                                             θ

To mitigate overfitting, we often add a regularizer Ω(θ) with strength λ ≥ 0:

         θ̂λ = arg min R̂N (hθ ) + λ Ω(θ),       Ω(θ) ∈ {kθk22 , kθk1 , . . .}.   (3.4)
                    θ

Regularization is not an arbitrary penalty. It is the mathematical version of a
teaching move: if a student can memorize every worked example, you change
the exercises so memorization is less effective and understanding is rewarded.
Regularization plays the same role. It makes some parameter settings expensive,
which pushes learning toward explanations that generalize better.
    In supervised learning, this matters because a model can drive training loss
down in ways that do not survive contact with new data. Regularization is one
of the main tools we use to “push back” against memorization: we still fit the
data, but we also express a preference for solutions that are stable, simple, or
structured in ways that match the problem.

Ridge and lasso. Two penalties show up so often that they have become part
of the basic vocabulary:
  • Ridge (L2) adds kθk22 , which shrinks weights smoothly and stabilizes
    solutions when features are correlated.

  • Lasso (L1) adds kθk1 , which tends to set some weights to exactly zero,
    yielding sparse models and a form of feature selection.
The difference is easiest to remember geometrically: L2 has round level sets,
while L1 has corners, and corners create exact zeros.


                                        72
Modern Intelligent Systems                                                     3


 Regularization: L1/L2 and scaling
    • Why regularize? Flexible models can fit training data by effectively
      memorizing idiosyncrasies (noise, quirks of the sample) rather than
      capturing stable structure. Regularization makes such memorization
      expensive and rewards explanations that survive on held-out data.

    • L2 (ridge) shrinks weights smoothly, is rotationally invariant, and
      works well when features are dense and correlated.

    • L1 (lasso) promotes sparsity, effectively performing feature selection
      when many coeﬀicients should be zero.

    • Why the names? “Ridge” refers to the ridge-like valleys that
      appear in least-squares objectives under multicollinearity; the L2
      penalty lifts the valley floor and stabilizes the solution. “LASSO” is
      an acronym for Least Absolute Shrinkage and Selection Operator.

    • Why L1 vs. L2 feels different: the L2 penalty discourages large
      coeﬀicients but rarely drives them exactly to zero, while the L1
      penalty creates corners in the geometry that tend to set some
      coeﬀicients to exactly zero.

    • Standardization (zero mean, unit variance) is essential before
      applying L1/L2/elastic-net so the penalty treats all dimensions
      comparably.

    • With an intercept term, centering y makes the algebra cleaner; ridge
      and lasso still apply directly once features are scaled.

    Figure 4 summarizes the geometric reason L1 and L2 penalties behave dif-
ferently.
    Figure 5 provides the coeﬀicient-path view used when tuning sparsity
strength.




                                      73
Modern Intelligent Systems                                                                                                    3



                                 θ2                                                                θ2

                                                                                                        solution
                                            solution


                                                      θ1                                                                 θ1




                        L2 (ridge):                                                           L1 (lasso):
                     round constraint                                                   corners encourage zeros


                  Figure 4: Why L1 promotes sparsity. Minimizing loss subject to an L2
                  constraint tends to hit a smooth boundary; an L1 constraint has corners
               aligned with coordinate axes, so tangency often occurs at a point where some
                   coordinates are exactly zero. Use it when choosing between L1 and L2
                                        penalties for feature selection.

                        1
  Coeﬀicient value




                       0.5

                        0
                                                                                                         β1 (shrinks)
                     −0.5                                                                               β2 (hits zero)
                                                                                                        β3 (hits zero)
                       −1
                             0        0.5         1        1.5       2        2.5   3        3.5    4         4.5        5
                                                                 Regularization strength λ

                      Figure 5: A typical lasso path as the regularization strength increases.
                     Coeﬀicients shrink, and some become exactly zero, yielding sparse models.
                     Use it when interpreting how penalty strength trades accuracy for sparsity.


3.4                  Elastic-net paths and cross-validation
Pure L1 or L2 penalties rarely dominate modern workflows; the elastic net mixes
them to balance sparsity and stability:
                                                       
        θ̂α,λ = arg min R̂N (hθ ) + λ αkθk1 + 1−α
                                               2  kθk 2
                                                      2   , α ∈ [0, 1].    (3.5)
                                              θ




                                                                         74
Modern Intelligent Systems                                                        3


Setting α = 1 recovers the lasso, α = 0 yields ridge, and intermediate values
trace a solution path that tends to group correlated features while still pruning
irrelevant ones. In practice we standardize the features once, draw a logarithmic
grid of λ values, and run K-fold cross-validation for each pair (α, λ). The “one-
standard-error” rule selects the largest λ whose validation error is within one
standard error of the minimum. It gives a stable operating point and avoids
over-interpreting tiny validation differences.

3.5   Common Loss Functions
Loss functions make the teacher signal quantitative: they decide what counts as
a small mistake, what counts as a large one, and which kinds of errors matter
most. For binary classification with labels y ∈ {−1, +1} and margin z = y f (x),
two standard losses are
                                                                         
      ℓhinge (y, z) = max 0, 1 − z ,        ℓlogistic (y, z) = log 1 + e−z .   (3.6)

Here y ∈ {−1, +1}; when labels are instead coded as y ∈ {0, 1} (common in
probability-of-class formulations), the margin expression uses y±1 = 2y − 1 to
map between codings. Figure 6 visualizes these curves together with the squared
hinge so you can match the algebra to the margin geometry. For regression with
residual e = y − ŷ, we frequently use

                  ℓsq (e) = 21 e2 ,                  ℓabs (e) = |e|.           (3.7)

The Huber loss interpolates between these: it is quadratic when |e| ≤ δ and
linear beyond that threshold (here the plot uses δ = 1), reducing sensitivity to
outliers while remaining smooth around the origin.
    Figure 7 compares common regression losses used in this section.




                                       75
Modern Intelligent Systems                                                             3




Table 2: Common losses and typical use (reference for Chapters 3 to 5). Use it when
   matching a loss to a modeling assumption and a downstream decision metric.

  Loss                   Convex?                  Typical use
  Squared error          Yes                      Regression when Gaussian
  1 2
  2e                                              noise is plausible; differentiable
                                                  everywhere.
  Absolute error |e|     Yes                      Robust regression with
                                                  Laplacian noise assumptions;
                                                  non-differentiable at 0.
  Huber (quadratic       Yes                      Regression when moderate
  → linear)                                       outliers are present; smooth
                                                  near zero.
  Logistic (binary       Yes                      Probabilistic classification;
  cross-entropy)                                  pairs naturally with sigmoid.
  Hinge / squared        Yes                      Margin-based classifiers (SVMs,
  hinge                                           large-margin perceptrons).




                             Hinge
                   2        Logistic
                         Squared hinge
            Loss




                   1



                   0
                    −3    −2       −1         0        1        2       3
                                         Margin z

     Figure 6: Classification losses as functions of the signed margin z. Use it
        when comparing how different losses treat confident mistakes and
                               near-boundary points.




                                         76
Modern Intelligent Systems                                                             3



                          Squared
                    4     Absolute
                           Huber
             Loss

                    2



                    0
                     −3    −2        −1         0       1        2         3
                                           Error e

         Figure 7: Regression losses versus prediction error. The Huber loss
      transitions from quadratic to linear to reduce sensitivity to outliers. Use it
               when choosing a loss that is robust to heavy-tailed noise.


3.6   Model Selection, Splits, and Learning Curves
Up to this point, we have defined what it means to fit: choose a model family,
pick an objective (loss plus any regularizer), and tune parameters to reduce that
objective on observed examples. The next question is how to choose among
competing model families, hyperparameters, and training procedures without
fooling ourselves. Model selection is the discipline of making those choices using
validation data, while keeping one final dataset split untouched so that the
reported performance remains honest.
    In other words, this is where the chapter’s “audit” step becomes operational:
we decide what to trust by checking performance on data the model has not
been allowed to fit.
    Practical workflows allocate data into training, validation, and test portions.
Training data are used to fit parameters; validation data guide choices such as
hyperparameters and model families; and the test set provides an unbiased audit
once those choices are fixed. The key habit is the separation of roles: training
is where you allow the model to “learn” (and potentially overfit), validation is
where you decide what kind of learning you trust, and the test set is the final
audit.




                                           77
Modern Intelligent Systems                                                           3


 Risk & audit
    • Leakage: avoid split mistakes (duplicates, near-duplicates, time
      leakage) that inflate validation accuracy.
```

### Findings
- The phrase "Worked example: Beta template vs. numeric fallback Consider the Beta integral" is missing a period or colon after "fallback" to separate the title from the text.
- In the integral expressions, the integral sign and limits are not consistently formatted; consider using proper integral notation with limits clearly aligned.
- The phrase "Safe transformations (factor constants, recognize the Beta template) immedi- ately identify" is split awkwardly across lines; hyphenation should be fixed for readability.
- The sentence "The solver therefore (i) records the unmet template, (ii) pushes a heuristic branch such as differentiation under" ends abruptly and seems incomplete; the continuation is missing or misplaced.
- The table caption "Table 1: Table: Transformation toolkit (safe vs. heuristic)." redundantly uses "Table" twice.
- The table content has inconsistent spacing and alignment, making it harder to read; consider improving formatting for clarity.
- The phrase "fails the template check after all safe moves" could be clearer if rephrased as "fails the template check even after all safe moves."
- The sentence "The solver then hands the integrand to an adaptive Gauss–Kronrod routine, which returns Inumeric ≈ 0.0915453885 with an internal error certificate < 3 × 10−7 ; this is a certified quadrature value rather than a closed form." has a spacing issue before the semicolon; replace with a comma or period.
- The phrase "Setting a = 32 , b = 2" has an extra space before the comma.
- The phrase "Safe moves reduce the plain Beta integral to B(3/2, 2) = 4/15" is slightly confusing because a=32 is set but then B(3/2,2) is used; clarify the connection or correct the parameter.
- The phrase "Failure path with certified numeric residual." is a fragment; consider rephrasing as a full sentence.
- The transition from the worked example to the "Discussion" section is abrupt; consider adding a sentence to guide the reader.
- The phrase "Under the operational framing in Chapter 1, the integrator exhibits several in- gredients" is hyphenated awkwardly; fix hyphenation.
- The sentence "Not every heuristic is helpful. For instance, applying x = tan y to (1 + x2 )3/2 dx looks attractive because 1 + tan2 y = sec2 y, yet it transforms the prob- lem into sec5 y dy" has awkward spacing and line breaks; fix for clarity.
- The phrase "This contrast helps position the data-driven chapters that follow, where the system’s “actions” are parameter updates guided by loss functions and validation checks." could be better connected to the previous paragraph.
- The "Connection to statistical learning." paragraph is somewhat dense; consider breaking into smaller sentences for clarity.
- The bullet points under "Connection: transformation search vs. empirical risk minimization" lack parallel punctuation; some end with periods, others do not.
- The "Key takeaways" section mixes bullet points with inconsistent capitalization and punctuation; standardize formatting.
- The "Common pitfalls" section uses colons inconsistently; some points start with verbs, others with nouns; unify style.
- The "Exercises and lab ideas" section uses incomplete sentences; consider rephrasing to full sentences or consistent fragments.
- The phrase "If you are skipping ahead. Keep the pattern vocabulary: safe vs. heuristic moves, explicit budgets, and residual/verification checks." is a fragment; rephrase as a full sentence.
- The transition "Where we head next." is a fragment; consider "Where we head next:" or a full sentence.
- The start of Chapter 3 is well oriented but could benefit from a clearer transition sentence linking it to the previous chapter.
- The phrase "When a mapping is known, we use the formula: Celsius and Fahrenheit are linked by a simple rule, and many physical laws give direct input–output rela- tionships." is awkward; consider rephrasing for clarity and flow.
- The paragraph starting "In this lens, supervised learning is prediction and inference: given evidence x, estimate an output y that you can act on or audit." is dense; consider breaking into two sentences.
- The phrase "The word fitting is meant literally." is abrupt; consider integrating it more smoothly.
- The paragraph about sensor calibration is somewhat long and could be split for readability.
- The "Learning Outcomes" section uses inconsistent capitalization and punctuation in bullet points; standardize.
- The "Design motif" section is a fragment; consider rephrasing as a full sentence.
- The notation list uses inconsistent punctuation and spacing; for example, "x⊤   i ; targets yi ∈ R" has extra spaces.
- The phrase "The aﬀine map y±1 = 2y −1 switches to {−1, +1} when margin-based expressions are convenient." is unclear; clarify or rephrase.
- The phrase "Noise uses ε; residuals use e = y − ŷ." is terse; consider expanding for clarity.
- The paragraph in 3.1 is dense; consider breaking into smaller sentences.
- The equations (3.1) and (3.2) have inconsistent spacing and parentheses; ensure consistent formatting.
- The phrase "Because P is unknown, learning algorithms minimize empirical proxies of R(hθ )." could be clearer if rephrased.
- The paragraph in 3.2 explaining fitting is somewhat repetitive; consider tightening prose.
- The figure caption for Figure 3 is long and could be broken into shorter sentences.
- The phrase "Use it when deciding whether to add capacity, add data, or add regularization." is informal; consider rephrasing.
- The section 3.3 has some redundancy in explaining ERM; consider condensing.
- The phrase "Regularization is not an arbitrary penalty. It is the mathematical version of a teaching move:" is somewhat informal; consider rephrasing.
- The bullet points under "Ridge and lasso." are inconsistent in punctuation; standardize.
- The phrase "The difference is easiest to remember geometrically: L2 has round level sets, while L1 has corners, and corners create exact zeros." is slightly awkward; consider rephrasing.
- The "Regularization: L1/L2 and scaling" section uses bullet points with inconsistent capitalization and punctuation; standardize.
- The phrase "Figure 4 summarizes the geometric reason L1 and L2 penalties behave dif- ferently." is split awkwardly; fix hyphenation.
- The figure captions for Figures 4 and 5 are long and could be more concise.
- The section 3.4 "Elastic-net paths and cross-validation" is clear but could benefit from a concluding sentence.
- The equations in 3.5 have inconsistent spacing around operators; ensure uniform formatting.
- The phrase "The “one-standard-error” rule selects the largest λ whose validation error is within one standard error of the minimum." could be clearer if rephrased.
- The section 3.5 "Common Loss Functions" is well structured but could use more consistent punctuation in equations.
- The phrase "Here y ∈ {−1, +1}; when labels are instead coded as y ∈ {0, 1} (common in probability-of-class formulations), the margin expression uses y±1 = 2y − 1 to map between codings." is dense; consider breaking into two sentences.
- The figure captions for Figures 6 and 7 are somewhat informal; consider more formal phrasing.
- The table 2 caption "Common losses and typical use (reference for Chapters 3 to 5). Use it when matching a loss to a modeling assumption and a downstream decision metric." is informal; consider rephrasing.
- The section 3.6 "Model Selection, Splits, and Learning Curves" is clear but could benefit from a more explicit transition sentence.
- The phrase "Risk & audit" is a fragment; consider rephrasing as a full sentence.
- The bullet point "Leakage: avoid split mistakes (duplicates, near-duplicates, time leakage) that inflate validation accuracy." is incomplete; consider expanding.

Overall, the chunk is rich in content and mostly clear but would benefit from improved transitions, consistent formatting, and polishing of punctuation and phrasing for a smoother graduate-level technical narrative.

## Chunk 7/31
- Character range: 162704–193587

```text
• Metric mismatch: align the loss you optimize with the metric you
      report (and the decision you must make).

    • Overfitting signals: track training vs. validation curves and use
      learning curves to diagnose data hunger vs. excess capacity.

    • Distribution shift: audit performance by slice (population, device,
      lighting, region) rather than relying on one aggregate score.

    • Calibration: check reliability when probabilities drive actions
      (thresholds, alerts, resource allocation).

    • Reporting discipline: log data split policy, seeds, and selection
      criteria; Appendix E defines the book-wide template.

 Proper scoring rules and calibration
    • Log loss (cross-entropy) and the Brier score are proper scoring rules:
      in expectation, they are minimized by predicting the true class probability.
    • Brier is squared error in probability space; it penalizes confident mistakes
      less harshly than log loss and is often paired with reliability diagrams.
    • Log loss heavily punishes overconfident errors (loss → ∞ as predicted
      probability → 0 on the true class), so it is a natural objective when
      probabilities will be thresholded downstream.
    • Practical tip: train with log loss, but monitor both log loss and Brier
      score on validation data to catch calibration issues early.

   Figure 8 lays out the split protocol for the train/validation/test workflow.
 A concrete toy task
 As a reference point, keep in mind one small binary classification problem:
 a two-moons toy with a standard train/validation/test split. It is
 deliberately simple, but it is rich enough to reveal the recurring failure
 modes (memorization, metric mismatch, split leakage) and the recurring
 remedies (regularization, validation, and diagnostics).


                                        78
Modern Intelligent Systems                                                                               3



                                    Train                               Validation         Test
                                    70%                                    15%             15%

                                Shuffle, then split once or use K-fold CV


     Figure 8: Dataset partitioning into training, validation, and test segments.
    Any resampling scheme should preserve disjoint evaluation data; when classes
      are imbalanced, shuffle within strata so each split reflects the overall class
     mix. Use it when designing splits that support trustworthy model selection
                                    and reporting.


   To make the workflow concrete, Figure 9 summarizes the standard ERM
pipeline from dataset to model selection.

                 Stratified                                                            Frozen model
   Dataset                              Train model            Validate / tune
               train/val/test                                                           tested once
     D                               (ERM + regularizer)      hyperparameters
                                                                                     (best model only)
                    split


                                                hyperparameter update


     Figure 9: Mini ERM pipeline (split once, iterate train/validate, then test
      only the best model on the held-out set). Use it when enforcing a clean
                  separation between tuning and final reporting.

    Figure 11 anchors the calibration and capacity diagnostics in this aside.
    Learning curves plot training and validation error against the number of
training examples, revealing underfitting or overfitting regimes.
 Data-leakage checklist
    • Split data before any preprocessing or feature selection.

    • Fit scalers/imputers/dimensionality-reduction transforms on the
      training fold only; reuse fitted parameters on validation/test (or
      within each CV fold via pipelines).

    • Respect temporal order for time-series; avoid target/future-derived
      features.

    • Wrap preprocessing + model in a pipeline for cross-validation so
      transformers refit inside each fold.



                                                  79
Modern Intelligent Systems                                                              3



                                           Training error      Validation error
                                                      patience window

                            0.4
            Loss / metric




                            0.2



                             0
                                  0   20           40          60          80     100
                                               Training examples

      Figure 10: Learning curves reveal under/overfitting: the validation curve
        flattens while additional data continue to decrease training error only
    marginally. A shaded patience window marks when early stopping would halt
    if no validation improvement occurs. Use it when deciding whether you need
                 more data, more capacity, or different regularization.


 Bias–variance at a glance
    • High bias (underfit): train and validation errors both plateau high
      and together; add capacity/features or reduce regularization.

    • High variance (overfit): train error low, validation error
      high/diverging; add data, strengthen regularization, or use early
      stopping.

    • Well fit: train/validation track closely and decrease or level off at
      low error; further gains require better data or priors.

Learning curves explain why the train/validation split is useful: they show
whether more data, more capacity, or more regularization is the lever that actu-
ally moves the validation error. Once you can read these curves, a natural next
question is what happens as we scale up data and model size. The aside below
summarizes two modern empirical patterns that are best treated as guidance,
not as a recipe.




                                                     80
Modern Intelligent Systems                                                                                                         3


                                                Reliability                                       Double descent / scaling
                             1.0                                                          1.0
                                      ECE     0.02
        Empirical accuracy
                             0.8
                                                                                          0.8




                                                                        Validation loss
                             0.6
                                                                                          0.6
                             0.4

                             0.2                                                          0.4

                             0.0                                                          0.2 2
                                0.0     0.2      0.4   0.6      0.8   1.0                    10      103     104     105     106
                                              Predicted prob.                                       Model size (log scale)
     Figure 11: Calibration and capacity diagnostics. Left: reliability diagram
         with binned predicted probabilities vs. empirical accuracy; Expected
        Calibration Error (ECE) measures deviation from the diagonal. Right:
     illustrative double-descent risk vs. model size (log-scale on the x-axis); the
    dashed line sketches a scaling-law trend for choosing capacity/regularization.
       Use it when deciding whether to prioritize calibration, more data, more
                         capacity, or stronger regularization.


 Aside: scaling laws and double descent
 The simplest story is the classical bias–variance picture: as model capacity
 grows, training error falls, and validation error often has a U-shape. In
 modern overparameterized models, that picture can be incomplete. You
 may see double descent: after the classical U-shape, error can decrease
 again once model size exceeds the interpolation threshold (Belkin et al.,
 2019). You may also hear scaling laws: in some regimes, validation loss
 decreases roughly as a power law of compute, data, and model size (Kaplan
 et al., 2020; Hoffmann et al., 2022).
 Treat both as diagnostics rather than guarantees. Use them to decide
 whether to collect more data, shrink or expand a model, or regularize more
 aggressively, but still make final choices by comparing validation curves.
 Do not chase the interpolation peak as a goal.

   Regularization trades model complexity for generalization; Figure 12 depicts
the effect of ridge penalties on the weight norm.




                                                                       81
Modern Intelligent Systems                                                       3



             kθk2    1



                    0.5



                     0
                          0   1        2         3         4         5
                                             λ

      Figure 12: Ridge regularization shrinks parameter norms as the penalty
       strength increases. Use it when tuning weight decay to control variance
                               without forcing sparsity.


3.7   Linear regression: a first full case study
Up to this point, the supervised-learning pipeline has been described in abstract
terms: a dataset, a hypothesis class, an objective, and an audit. Linear regres-
sion is where those pieces become concrete enough that you can see every moving
part at once.
A useful habit, before you commit to any model family, is to ask whether there
is any signal to model in the first place. If the relationship were deterministic
(like Celsius ↔ Fahrenheit), there would be nothing to learn. In supervised
learning we assume the relationship is statistical: the same input can map to
different outputs because of noise, missing variables, or genuine uncertainty. For
simple problems, a scatter plot and a correlation coeﬀicient can reveal whether
a linear trend is even plausible. For high-dimensional data, analogous sanity
checks (feature scaling, collinearity) help you decide whether linear regression is
a sensible starting point or merely a baseline.
In this section, the coeﬀicients β are the knobs we turn. “Learning” means using
training pairs (X, y) to estimate β so predictions match observed targets as
well as they can under the chosen objective. Because least squares is a convex,
closed-form problem, repeating the fit with the same data returns the same
solution (up to numerical tolerance). That transparency is exactly why linear
regression is worth treating carefully: it makes the ideas of losses, optimization,
regularization, and validation feel concrete before we move on to models where
the same pipeline is less visible.


                                        82
Modern Intelligent Systems                                                          3


Model. Given inputs xi ∈ Rd and continuous targets yi ∈ R, the linear model
predicts
                       ŷ = Xβ,     X ∈ RN ×d .                        (3.8)

Equivalently, ŷi = x⊤
                     i β for each data point. The vector β is the set of adjustable
parameters: fitting the model means choosing β so that predictions align with
observed outputs. The residual e = y − ŷ captures what the model fails to
explain on the data at hand.

A noise model (why squared error shows up).                    A common way to formal-
ize “measurement scatter” is to write

                       yi = x ⊤
                              i β + εi ,         εi ∼ N (0, σ 2 ),               (3.9)

where εi is observation noise (sensor noise, unmodeled effects, annotation noise,
etc.). Under this assumption,

                             p(yi | xi , β) = N (x⊤     2
                                                  i β, σ ),                     (3.10)

and (assuming i.i.d. observations) the likelihood factorizes:

                                           Y
                                           N
                          p(y | X, β) =          p(yi | xi , β).                (3.11)
                                           i=1

Maximizing the (log) likelihood is equivalent to minimizing the negative log-
likelihood, and for Gaussian noise that becomes (up to constants and a scale
factor 1/(2σ 2 )) the familiar sum of squared errors:

                                        1 X
                                            N
                − log p(y | X, β) =         (yi − x⊤   2
                                                   i β) + const.                (3.12)
                                       2σ 2
                                            i=1

This is the simplest example of a recurring theme: if you propose an “educated
guess” model for how data are generated, training often becomes “minimize a
loss”.




                                           83
Modern Intelligent Systems                                                      3


Objective. To fit β, we need a grading rubric. Squared error is the standard
starting point because it is smooth and strongly penalizes large mistakes:

                              L(β) = 21 ky − Xβk22 .                        (3.13)

The gradient is simple,

                             ∇β L(β) = X ⊤ (Xβ − y),                        (3.14)

so gradient descent is explicit: β ← β−ηX ⊤ (Xβ−y). This same loop reappears
later when the model is no longer linear and the loss is no longer quadratic.

Closed form and geometry. Least squares is convex and satisfies the normal
equations:
                         X ⊤ X β̂ = X ⊤ y.                           (3.15)

When X ⊤ X is invertible, the solution can be written explicitly as

                               β̂ = (X ⊤ X)−1 X ⊤ y.                        (3.16)

Geometrically, the prediction ŷ is the orthogonal projection of y onto the column
space of X. In code, solve the linear system (QR/SVD) rather than forming
(X ⊤ X)−1 explicitly; collinearity can make X ⊤ X poorly conditioned even when
the mathematics is correct.

Where overfitting enters. With raw features, a linear model may under-
fit; with aggressive feature expansions (polynomials, splines, kernels, learned
features), the same least-squares machinery can overfit. This is where the ear-
lier tools matter. Regularization (ridge, lasso, elastic net) makes memorization
harder; validation selects hyperparameters; learning curves diagnose whether
error is limited by bias, variance, or data.

Ridge and lasso in one line. Ridge adds λkβk22 to the objective, shrinking
coeﬀicients and stabilizing solutions when features are correlated; lasso uses
kβk1 and tends to drive some coeﬀicients to exactly zero. The ridge shrinkage
behavior is visualized in Figure 12.


                                        84
Modern Intelligent Systems                                                        3


The discipline of supervised learning is reusable across models: define a dataset
and a hypothesis class, choose an objective (loss plus regularizer), optimize it,
and then audit generalization with clean train/validation/test separation. In
Chapter 4, we apply this toolkit to classification, where the loss becomes a
Bernoulli negative log-likelihood (cross-entropy) and the evaluation tools expand
(confusion matrices, ROC/PR curves, and calibration).
  Key takeaways
  Minimum viable mastery
     • Supervised learning chooses a hypothesis class and fits parameters by
       minimizing empirical risk, then audits generalization on held-out
       data.

     • Overfitting is a training success but a deployment failure;
       regularization and validation protocols are the practical defenses.

     • Learning curves and bias–variance reasoning are diagnostics: they
       help decide whether to add data, change capacity, or adjust
       regularization.

  Common pitfalls
     • Tuning on the test set (or peeking repeatedly) turns the test set into
       training data.

     • Leakage through preprocessing: fit scalers/encoders/imputers on the
       training split only, then apply to val/test.

     • Over-interpreting a single metric: use learning curves and slice audits,
       not only one headline number.




                                       85
Modern Intelligent Systems                                                        4


 Exercises and lab ideas
    • Implement linear regression with ridge regularization using both (i) a
      closed-form solve (QR/SVD) and (ii) gradient descent; compare
      validation curves as λ varies.

    • Create a controlled overfitting experiment: increase polynomial
      feature degree or add noisy features, then use learning curves
      (Figure 10) to diagnose bias vs. variance and decide how much
      regularization is needed.

    • Demonstrate a leakage failure mode by fitting preprocessing on the
      full dataset (incorrect) versus on the training split only (correct);
      report the difference in test error.

 If you are skipping ahead. Keep the ERM loop and split hygiene close:
 model class, loss/regularizer, optimizer, and a clean train/val/test protocol.
 Those ideas are assumed immediately in Chapter 4 and reused throughout
 the neural chapters.



Where we head next. Chapter 4 extends this ERM setup from continuous
targets to discrete labels: outputs become class probabilities, the loss becomes
cross-entropy, and evaluation adds confusion matrices, ROC/PR curves, and
threshold selection.


4 Classification and Logistic Regression
Chapter 2 illustrated intelligence as transformation search with explicit goal
tests. Chapter 3 introduced the data-driven view: represent a task with data,
choose a hypothesis class, minimize empirical risk under regularization, and
audit performance on held-out data. This chapter extends that toolkit from
regression to classification, and Figure 1 places it on the core supervised path.




                                       86
Modern Intelligent Systems                                                       4


  Learning Outcomes
 After this chapter, you should be able to:
      • Derive the logistic log-likelihood and its gradient.

      • Explain the NLL (cross-entropy) connection and convexity.

      • Extend to softmax regression for multiclass problems.

  Design motif
  Keep the workflow, swap the likelihood: logistic regression keeps the linear
  score but changes the probabilistic model (Bernoulli likelihood) and the
  loss (negative log-likelihood, i.e., cross-entropy).


4.1    From regression to classification
Linear regression models a continuous target y and, under a Gaussian noise
model, yields a closed-form solution via the normal equations (Chapter 3, Sec-
tion 3.7). Classification changes the output space: y is a discrete label, and the
model predicts class probabilities rather than raw responses. The ERM pipeline
remains the same, but the loss becomes the negative log-likelihood (binary cross-
entropy) and optimization is typically iterative.
    Throughout this chapter we use y ∈ {0, 1} by default, switching to y±1 =
2y − 1 only when margin-based expressions are convenient. Predictions carry
hats (e.g., ŷ), ε denotes noise, and e = y − ŷ denotes residuals. For a refresher
on data splits, learning curves, and the bias–variance vocabulary, see Chapter 3;
here we focus on the logistic-specific modeling and diagnostics.
  Worked example: a toy decision boundary
 On a two-moons binary classification toy, the ideas in this chapter have a
 visible effect:
      • Logistic regression gives a calibrated probabilistic baseline (linear
        score + sigmoid) that is easy to diagnose.

      • The nonlinearity we will need later is not in the optimizer but in the
        representation: Chapter 6 introduces multilayer features and
        Chapter 7 supplies the training engine that lets those features
        improve the decision boundary.


                                         87
Modern Intelligent Systems                                                        4


4.2    Classification problem statement
This chapter shifts from regression to classification. Unlike regression, where y
is continuous, classification predicts a discrete label. We start with the binary
case y ∈ {0, 1}, where the goal is to estimate a probability

                               π(x) = P (y = 1 | x),

and then produce a decision by thresholding π(x) (or by comparing class proba-
bilities when there are more than two classes). For multiclass problems the label
belongs to one of K classes,

                                y ∈ {c1 , c2 , . . . , cK },

and the goal is to estimate P (y = ck | x) for each k; we return to the softmax
extension later in the chapter.

4.3    Bayes Optimal Classifier
A fundamental result in statistical pattern recognition is that the Bayes classifier
is the optimal classifier in terms of minimizing the expected classification error.
The Bayes classifier assigns x to the class:

                        ŷ = arg        max            P (y = ck | x).
                                   ck ∈{c1 ,...,cK }


   Using Bayes’ theorem, the posterior probability can be expressed as

                                          P (x | y = ck )P (y = ck )
                    P (y = ck | x) =                                 .        (4.1)
                                                    P (x)

Here
   • P (x | y = ck ) is the class-conditional likelihood,

   • P (y = ck ) is the prior probability of class ck ,
              P
   • P (x) = K    j=1 P (x | y = cj )P (y = cj ) is the marginal likelihood of the
     input.
    Equation (4.1) provides a principled way to compute the posterior probabil-
ities, and thus the optimal classification rule.


                                              88
Modern Intelligent Systems                                                        4


Challenges in Practice Despite its theoretical appeal, the Bayes classifier is
rarely used directly in practice because:
  • The class-conditional densities P (x | y = ck ) are typically unknown.

  • The prior probabilities P (y = ck ) may also be unknown or diﬀicult to
    estimate accurately.

  • Estimating these distributions nonparametrically or parametrically can be
    challenging, especially in high-dimensional spaces.
    Consequently, practical classification methods often rely on approximations
or alternative formulations.

Running example: a two-cluster dataset To keep the discussion concrete,
we reuse a small toy dataset in Figure 13 consisting of two Gaussian clusters.
Under a simple generative assumption (equal covariances and similar priors),
Figure 14 visualizes the Bayes-optimal decision boundary: it is linear in this LDA
setting, while unequal covariances yield a quadratic boundary. This running
example will anchor the geometric intuition (what a decision boundary looks
like) before we turn to discriminative models that learn π(x) directly.
    As shown in Figure 15, logits, BCE curvature, and regularization strength
appear in one compact diagnostic view.
    Figure 18 provides the low-data MAP-versus-MLE comparison used in this
discussion.

Naive Bayes Approximation One classical workaround is the Naive Bayes
classifier, which assumes that the components of x are conditionally independent
given the class label. Under this assumption,

                                           Y
                                           p
                       P (x | y = ck ) =         P (xj | y = ck ),
                                           j=1


making the computation and estimation of the likelihood tractable. It is impor-
tant to remember that this factorization is justified only under the conditional in-
dependence assumption; when the features are strongly correlated, Naive Bayes
can suffer because the assumption is violated.



                                           89
Modern Intelligent Systems                                                                4



                         2


                         1
                  x2



                         0


                       −1              Class C0 density contour
                                       Class C1 density contour
                                       Samples from C0
                       −2              Samples from C1

                             −3        −2      −1         0       1       2       3
                                                         x1

      Figure 13: Synthetic binary dataset built from two anisotropic Gaussian
      clusters; shaded ellipses hint at the underlying density while the scattered
     samples are reused throughout the running examples. Use it when building
     intuition for how decision boundaries relate to class geometry before fitting
                                 discriminative models.

                   2          C0 samples
                              C1 samples
                              decision boundary
                   1
             x2




                   0



                  −1



                  −2
                    −3            −2         −1          0            1       2       3
                                                         x1

        Figure 14: Bayes-optimal boundary for two Gaussian classes. Equal
    covariances and similar priors (LDA setting) yield a linear separator; unequal
          covariances yield a quadratic boundary. The boundary is near the
    equal-posterior line (vertical, pink); left/right regions map to predicted classes
      R0 and R1. Use it when contrasting linear vs. quadratic boundaries under
                            different generative assumptions.


                                                    90
Modern Intelligent Systems                                                        4


4.4   Logistic Regression: A Probabilistic Discriminative Model
One widely used approach to classification, especially for binary problems, is
logistic regression. Logistic regression models the posterior probability P (y = 1 |
x) directly as a function of x, without explicitly modeling the class-conditional
densities.
  Logistic regression at a glance
  Objective: Minimize binary cross-entropy (negative log-likelihood)
  between true labels y ∈ {0, 1} and predicted probabilities p̂ = σ(β ⊤ x̃).
  Key hyperparameters: Regularization type/strength (L2 or L1, penalty
  λ; many libraries use C = 1/λ), feature scaling, optimization settings (step
  size, iterations).
  Defaults: Standardize features; use L2 regularization with moderate
  strength; start with a 0.5 decision threshold and adjust only if class costs
  are asymmetric.
  Common pitfalls: Strong collinearity between features, severe class
  imbalance, and uncalibrated probability outputs if the model is
  over-regularized or trained on a biased sample.


Binary Classification Setup Consider the binary classification problem
where y ∈ {0, 1}. The goal is to model the probability that the output is class 1
given the input x: P (y = 1 | x) = π(x).

Linear Model for the Log-Odds Logistic regression assumes that the log-
odds (also called the logit) of the positive class is a linear function of the input
features. Introducing the augmented feature vector x̃ = [1, x1 , . . . , xp ]⊤ and
parameter vector β = [β0 , β1 , . . . , βp ]⊤ , we write

                                       π(x)
                               log            = β ⊤ x̃.                        (4.2)
                                     1 − π(x)

    This implies that the posterior probability π(x) can be written as the logistic
sigmoid function applied to the linear predictor:

                                               1
                             π(x) =                       .                   (4.3)
                                       1 + exp −β ⊤ x̃


                                          91
Modern Intelligent Systems                                                                  4


  Author’s note: why “logistic” and why “regression”?
  The name logistic comes from the logistic (sigmoid) link in Equation (4.3),
  which maps a real-valued score to a probability in [0, 1]. The word
  regression reflects what we model linearly: the log-odds (logit) in
  Equation (4.2) is a linear function of the features. The model itself outputs
  a continuous probability; we turn that probability into a class label by
  thresholding (or comparing class probabilities in the multiclass extension).


4.4.1    Likelihood, loss, and gradient
                                                                   ⊤
For data {(xi , yi )}N
                     i=1 with yi ∈ {0, 1}, define pi = π(xi ) = σ(β x̃i ). Under a
Bernoulli model, the likelihood factorizes as

                                         Y
                                         N
                           p(y | X, β) =   pyi i (1 − pi )1−yi ,                        (4.4)
                                            i=1

so the log-likelihood is

                                   N 
                                   X                                        
               log p(y | X, β) =          yi log pi + (1 − yi ) log(1 − pi ) .          (4.5)
                                    i=1

Maximizing Equation (4.5) is equivalent to minimizing the negative log-likeli-
hood (binary cross-entropy). With the design matrix X = [x̃⊤                          ⊤
                                                                        1 ; . . . ; x̃N ] and
                             ⊤
vector p = (p1 , . . . , pN ) , the gradient of the negative log-likelihood is
                                                
                          ∇β − log p(y | X, β) = X ⊤ (p − y).                            (4.6)

The Hessian has the form X ⊤ W X where W = diag(pi (1 − pi ))  0, which
makes the objective convex and explains why second-order methods work well
for moderate feature dimensions.

Optimization geometry (why iterative solvers) Unlike linear regression,
logistic regression does not have a closed-form solution for β, even though the
objective is convex. In practice we therefore rely on iterative solvers (gradi-
ent methods, quasi-Newton methods, or Newton/IRLS in moderate dimensions).
Figure 16 is a convex quadratic toy that reminds us what an optimization trajec-


                                             92
Modern Intelligent Systems                                                                                 4
```

### Findings
Issues flagged:

1. Narrative flow and transitions:
   - The chunk covers many topics, from practical tips on metrics and overfitting, through linear regression, to classification and logistic regression. The transitions between these topics are abrupt and could be smoother. For example, the jump from Figure 12 (ridge regularization) directly into "3.7 Linear regression" is somewhat jarring. A brief transition sentence summarizing the previous section and introducing the case study would improve flow.
   - Similarly, the transition from the linear regression case study to the classification chapter (Chapter 4) is abrupt. A concluding paragraph summarizing the key points of linear regression before moving on would help orient the reader.

2. Reader orientation:
   - The section "Aside: scaling laws and double descent" is introduced without a clear lead-in or explanation of its relevance to the preceding content. A brief introduction explaining why these empirical patterns are important diagnostics would improve clarity.
   - The "Author’s note" in the logistic regression section is helpful but could be better integrated into the main text or clearly set apart typographically to avoid disrupting the flow.

3. Repetitive templating:
   - The bullet points at the start (e.g., metric mismatch, overfitting signals, distribution shift) are presented in a list format but lack parallel structure in phrasing. For example, some start with verbs ("align," "track," "audit"), others with nouns ("Calibration," "Reporting discipline"). Consistent phrasing would improve readability.

4. Punctuation and spacing:
   - In the bullet point "Reporting discipline: log data split policy, seeds, and selection criteria; Appendix E defines the book-wide template." the semicolon is used correctly but the sentence could be clearer if split or rephrased for better flow.
   - In the equation references, spacing around parentheses and commas is inconsistent, e.g., "p(yi | xi , β)" sometimes has spaces before commas, sometimes not.
   - In the sentence "The gradient is simple, ∇β L(β) = X ⊤ (Xβ − y), so gradient descent is explicit: β ← β−ηX ⊤ (Xβ−y)." there should be spaces around operators for clarity: "β ← β − η X⊤(Xβ − y)."
   - In the phrase "the same input can map to different outputs because of noise, missing variables, or genuine uncertainty." the serial comma is used correctly, but elsewhere serial commas are inconsistent.

5. Clarity of prose:
   - The phrase "A noise model (why squared error shows up)." as a section heading is informal and could be more descriptive, e.g., "Noise model and the origin of squared error."
   - The sentence "This is the simplest example of a recurring theme: if you propose an “educated guess” model for how data are generated, training often becomes “minimize a loss”." uses quotation marks around "educated guess" and "minimize a loss" which may be unnecessary or could be replaced with italics for emphasis.
   - The sentence "The discipline of supervised learning is reusable across models: define a dataset and a hypothesis class, choose an objective (loss plus regularizer), optimize it, and then audit generalization with clean train/validation/test separation." is somewhat long and could be broken up for clarity.
   - The "Key takeaways" section is clear but could benefit from parallel structure in bullet points.
   - The "Common pitfalls" bullet "Over-interpreting a single metric: use learning curves and slice audits, not only one headline number." could be clearer if rephrased, e.g., "Avoid over-interpreting a single metric; instead, use learning curves and slice audits rather than relying on a single headline number."

6. Minor typographical issues:
   - In the phrase "the same least-squares machinery can overfit. This is where the ear- lier tools matter." the word "earlier" is split across lines awkwardly ("ear- lier").
   - In the phrase "the same input can map to different outputs because of noise, missing variables, or genuine uncertainty." the phrase "missing variables" might be clearer as "missing variables in the data" or "missing explanatory variables."
   - The phrase "the same pipeline is less visible." could be more precise, e.g., "the same pipeline is less transparent."

No other concrete issues were found.

## Chunk 8/31
- Character range: 193593–225409

```text
Sigmoid                       BCE loss                          L2 shrinkage

               1                               6                                  1
                                                                 y=1
                                               4                 y=0




                                           L
          p



              0.5                                                               0.5
                                               2                                                 shrinks
                                                                                                 weights
               0                               0                                  0
                    −5         0      5            −5        0         5              0      2       4
                           logit z                       logit z                                 λ


      Figure 15: The sigmoid maps logits to probabilities (left). The binary
    cross-entropy (negative log-likelihood) penalizes confident wrong predictions
     sharply (middle). Regularization typically shrinks parameter norms as the
         penalty strength increases (right). Use it when choosing a baseline
                probabilistic classifier and diagnosing overconfidence.


tory looks like when we minimize a smooth objective: step size and conditioning
shape how quickly iterates contract toward the minimizer.

                          1


                         0.5


                          0                                          minimum
                                                                 t→∞
                                                                 t = 10
                     −0.5
              w2




                                                   t=5
                         −1


                     −1.5
                                     t=0

                         −2                                                    GD trajectory

                                     −2                 −1                 0                 1
                                                             w1

    Figure 16: Gradient-descent iterates contracting toward the minimizer of a
      convex quadratic cost. Ellipses are level sets; arrows show the “steepest
    descent along contours” direction. Use it when visualizing why conditioning
                              slows gradient descent.




                                                        93
Modern Intelligent Systems                                                           4


Geometry of the logistic surface. The decision rule is linear in feature
space even though the posterior itself is smoothly varying. Figure 17 depicts
this duality: the white hyperplane slices the space into two half-spaces while the
probability “ramp” shows how margins translate into calibrated confidences.

                                                 0        1
                  2       (x) contours

                  1
                                  0.2
                  0
           x2




                  1       0.4
                                0.6
                  2                       0.8
                      2               1              0        1         2
                                                     x1
      Figure 17: Illustrative logistic-regression boundary. The dashed line marks
       the linear decision boundary at probability 0.5; labeled contours show how
      the posterior varies smoothly with margin, enabling calibrated decisions and
       adjustable thresholds. Use it when explaining why logistic outputs support
                                    threshold tuning.


4.5    Probabilistic Interpretation: MLE and MAP
The ERM view in Chapter 3 treats learning as minimizing an average loss plus
(optionally) a regularizer. The probabilistic view arrives at the same objective
from a different direction:
   • MLE maximizes the data likelihood under a chosen observation model
     (for logistic regression: Bernoulli with pi = σ(β ⊤ x̃i )).

   • MAP maximizes the posterior, which multiplies the likelihood by a prior
     p(β). In optimization form, MAP adds a penalty − log p(β), which is
     exactly regularization.
Two common priors explain the two penalties that appear most often in practice:

                                                94
Modern Intelligent Systems                                                      4


a zero-mean Gaussian prior yields an L2 (ridge) penalty, while a Laplace prior
yields an L1 (lasso) penalty. The schematic below illustrates the MLE→MAP
idea on a simple mean-estimation problem: with little data, the prior matters;
with enough data, MAP approaches MLE.

                            1
                                     MAP (prior µ0 = 0.5)
                           0.8              MLE
                                        true mean 0.7
                Estimate




                           0.6

                           0.4

                           0.2
                                 0     10        20         30   40   50
                                               Sample size n

       Figure 18: MAP estimates interpolate between the prior mean and the
      data-driven MLE. As the sample size grows, the MAP curve approaches the
        true mean. Use it when explaining how priors matter most in low-data
                                      regimes.


4.6    Confusion Matrices and Derived Metrics
 Risk & audit
      • Threshold choice: a high AUC can still yield a poor operating
        point; pick thresholds using a validation objective that matches the
        cost.

      • Class imbalance: report PR curves (or per-class metrics) when
        positives are rare; audit confusion matrices, not just accuracy.

      • Probability quality: logits can be miscalibrated; use reliability
        diagrams/ECE when probabilities are consumed downstream.

      • Feature shortcuts: strong apparent accuracy can come from
        spurious correlates; sanity-check with slices and perturbations.

      • Regularization: tune λ with held-out data; do not report the best
        test result after repeated tuning.



                                                  95
Modern Intelligent Systems                                                                                      4


    Once we have a probabilistic classifier, we need diagnostics that quantify
performance on held-out data. For multi-class prediction, the confusion matrix
Cij records the number of examples with true class i predicted as j. From C
we compute accuracy, per-class precision/recall, and aggregate metrics. Macro-
averaged precision/recall first evaluate the metric per class and then average
them uniformly, whereas micro-averaged precision/recall pool all true/false pos-
itives across classes before computing the ratio (equivalent to weighting each
example equally). Visual inspection (Figure 20) helps diagnose systematic er-
rors across classes.
    On highly imbalanced problems accuracy and AUROC can be misleading;
prefer class-balanced metrics (macro-F1) and AUPRC. Figure 19 collects ROC
and PR curves on one page so you can choose operating points explicitly.

                               ROC                                                      PR
              1.0                                                  1.0

              0.8                                                  0.8
                                                                                        op. point
                                   op. point
                                                       Precision




              0.6                                                  0.6
        TPR




              0.4                                                  0.4

              0.2                                                  0.2

              0.0                                                  0.0
                 0.0   0.2   0.4      0.6      0.8   1.0              0.0   0.2   0.4        0.6    0.8   1.0
                               FPR                                                 Recall
    Figure 19: ROC and PR curves with an explicit operating point. Left: ROC
    curve with iso-cost lines; right: PR curve with a class-prevalence baseline and
     iso-F1 contours. Together they visualize threshold trade-offs and calibration
     quality. Use it when selecting an operating point under class imbalance and
                                    asymmetric costs.


  Imbalance and thresholds
  Use class or sample weights (e.g., inverse prevalence) inside the loss, and
  pick thresholds via ROC/PR curves or explicit cost ratios rather than
  defaulting to 0.5. With symmetric priors but asymmetric costs, predict
  class 1 when the logit exceeds log(c10 /c01 ); for rare positives, report
  PR-AUC alongside AUROC.




                                                      96
Modern Intelligent Systems                                                          4



                                                                      40
                   True C     0           6             32
                                                                      30
            True

                   True B     4           37            5             20


                                                                      10
                   True A     42          3             1

                                                                      0
                            Pred A      Pred B        Pred C
                                      Predicted

    Figure 20: Confusion matrix for a three-class classifier; diagonals dominate,
     indicating strong accuracy with modest confusion between classes B and C.
      Use it when diagnosing which error types dominate in multiclass settings.


 Key takeaways
 Minimum viable mastery
    • Logistic regression models class probability with a sigmoid link and
      maximizes a concave log-likelihood (equivalently minimizes a convex
      negative log-likelihood); there is no closed-form solution.

    • ROC and PR curves provide threshold-independent evaluation; AUC
      summarizes performance.

    • Proper feature scaling and regularization improve convergence and
      generalization.

 Common pitfalls
    • Confusing scores with decisions: choose thresholds using costs and
      PR/ROC trade-offs, not a default 0.5.

    • Reporting only AUC: check calibration when probabilities are used
      downstream (reliability/ECE).

    • Letting imbalance hide failure: stratify splits and audit per-class
      performance, not only overall accuracy.




                                         97
Modern Intelligent Systems                                                           4


  Probability calibration
  Discrimination metrics (ROC/PR, AUC) say how well a classifier ranks
  examples but not how reliable its probabilities are. Calibration methods
  such as Platt scaling and temperature scaling adjust the logits so that
  predicted probabilities match empirical frequencies (e.g., 0.8 scores
  correspond to ≈ 80% positives), often measured via Expected Calibration
  Error (ECE) and inspected with reliability diagrams (Platt, 1999; Guo
  et al., 2017).

Table 3: Handling class imbalance for logistic models (Chapter 4 reference table). Use
it when choosing resampling, weighting, and thresholding strategies for rare positives.

Tactic                         When/why
Stratified splits (and         Preserve class ratios in train/validation/test to
K-fold)                        avoid optimistic validation scores.
Class weighting /              Multiply the cross-entropy (or hinge loss) by
cost-sensitive loss            per-class weights so minority errors matter more.
                               Useful when collecting more data is diﬀicult.
Resampling                     Balance the dataset prior to training. Helps tree
(over/undersampling,           ensembles and linear models; pair with
SMOTE)                         cross-validation to avoid overfitting. Use simple
                               baselines (logistic/SVM) as a tie-break to detect
                               overfitting.
Threshold tuning               Choose a decision threshold based on PR curves
                               or cost ratios rather than default 0.5; report
                               PR-AUC when positives are rare.




                                          98
Modern Intelligent Systems                                                   4


 Exercises and lab ideas
    • Implement a minimal example from this chapter and visualize
      intermediate quantities (plots or diagnostics) to match the
      pseudocode.

    • Stress-test a key hyperparameter or design choice discussed here and
      report the effect on validation performance or stability.

    • Re-derive one core equation or update rule by hand and check it
      numerically against your implementation.

 If you are skipping ahead. Keep three ideas: (i) Bayes-optimal
 boundaries are a conceptual anchor, (ii) logistic regression is the first
 practical probabilistic baseline, and (iii) evaluation depends on costs,
 thresholds, and calibration. Those recur throughout the neural and
 deployment chapters.



Where we head next. Logistic regression is still linear at the boundary.
Chapter 5 introduces trainable neuron models, and stacking nonlinear units
then removes that linear ceiling and sets up multilayer networks plus backprop-
agation.
 Part I takeaways
    • Intelligence as engineered self-correction: represent state, choose
      actions, verify outcomes.

    • Two recurring toolkits: safe vs. heuristic moves (search) and ERM
      (model–loss–optimize–audit).

    • Classification as a probabilistic decision problem: Bayes optimality
      and calibrated scores precede thresholds.

    • Reading paths are a dependency graph: later chapters reuse
      diagnostics, notations, and audit habits introduced here.




                                       99
Modern Intelligent Systems                                                      5



Part II: Neural networks, sequence
modeling, and NLP
5 Introduction to Neural Networks
Chapter 4 established linear and logistic models as strong baselines, but their
decision boundaries stay linear in the original feature space. We now shift from
a statistical lens to a biological abstraction: simple neurons whose composi-
tion yields nonlinear decision surfaces. This chapter introduces neuron models,
perceptrons, activation functions, and the first learning rules (perceptron and
Adaline); Figure 1 marks this as the start of the neural strand.
 Learning Outcomes
 After this chapter, you should be able to:
      • Describe the core ingredients of neural networks (architecture,
        activations, learning).

      • Explain how multilayer perceptrons learn via gradient-based training.

      • Identify common pitfalls (saturation, poor initialization) and basic
        remedies.

 Design motif
 Biology as engineering abstraction: start with simple units, make the
 update rule explicit, and use geometry to build intuition before the algebra
 gets deep.


5.1    Biological Inspiration
Neural networks borrow a simple but powerful idea from biology: complex be-
havior can emerge from many simple units interacting through many simple
connections. The goal is not to model the brain in detail, but to steal an engi-
neering abstraction we can write down and implement: signals flow through a
network of units, and learning adjusts connection strengths so the overall system
changes its behavior.



                                       100
Modern Intelligent Systems                                                      5


Neurons and Neural Activity A biological neuron can be viewed as a pro-
cessing unit that receives multiple inputs, integrates them, and produces an
output if certain conditions are met. In the simplified picture we use here, the
key parts are:
  • Dendrites: Receive incoming signals from other neurons.

  • Cell body (soma): Integrates incoming signals.

  • Axon: Transmits the output signal to other neurons.

  • Synapses: Junctions where signals are transmitted between neurons.
    Incoming signals can excite or inhibit the neuron. When the combined in-
fluence crosses a threshold, the neuron “fires” and sends an impulse down the
axon to connected neurons. Real neurons are richer than this sketch (timing,
frequency, and graded effects matter), but the abstraction is enough to moti-
vate an artificial unit that combines inputs, applies a nonlinearity, and emits an
output.

Complexities and Unknowns Despite extensive research, many aspects of
neural function remain poorly understood. For our purposes, what matters is
that even simple descriptions raise practical questions:
  • How signals arriving at different dendrites simultaneously interact.

  • The effect of signal timing and frequency on neuron firing.

  • The mechanisms of cooperation and competition among neurons.

  • How neural activity culminates in complex behaviors.
    These uncertainties highlight why we do not try to copy biology literally.
Instead, we build simplified artificial models that preserve the compositional
story (many units, many connections) while making the update rule explicit
and learnable.

5.2   From Biological to Artificial Neural Networks
Artificial neural networks (ANNs) are computational models inspired by the
structure and function of biological neural systems. The goal is to create systems



                                       101
Modern Intelligent Systems                                                       5


that can process information, learn from data, and perform tasks that require
intelligence.

Key Features of Artificial Neural Networks To design an ANN that
captures essential aspects of biological neural processing, several features must
be considered:
  1. Architecture: The arrangement and connectivity of neurons within the
     network. This includes the number of layers, the pattern of connections
     (e.g., feedforward, recurrent), and the flow of information.

  2. Signal Propagation: How input signals are transmitted through the
     network, transformed by neurons, and produce outputs.

  3. Learning Mechanism: The method by which the network adjusts its
     parameters (e.g., weights) based on data to improve performance. This
     involves capturing and retaining knowledge from experience.

  4. Activation Dynamics: The rules governing neuron activation, including
     how neurons decide to fire based on inputs, the degree of activation, and
     inhibition mechanisms.

Historical Context The concept of artificial neural networks dates back to
the early 1940s, with pioneering work that attempted to mathematically model
neuron behavior. Over the past eight decades, ANNs have evolved significantly,
leading to a variety of architectures and learning algorithms. This evolution re-
flects ongoing efforts to better approximate biological intelligence and to address
practical challenges in computation and learning.

5.3   Outline of Neural Network Study
This chapter introduces perceptrons and common activation functions. Chap-
ter 6 then develops multilayer perceptrons and the backpropagation machinery
needed to train them; Chapter 12 returns to sequence models with recurrent
connections.
    Formal definitions of the perceptron neuron model (activation functions,
weighted sums, and thresholds) follow in Section 5.10. Refer back to the bi-
ological narrative above when interpreting the abstractions.


                                       102
Modern Intelligent Systems                                                       5


5.4   Neural Network Architectures
Neural networks can be broadly categorized based on the flow of information
through their structure. Understanding these architectures is crucial for design-
ing and analyzing neural models that mimic biological neural systems.

Feedforward Neural Networks Feedforward neural networks (FNNs) are
characterized by a unidirectional flow of information from input to output lay-
ers without any cycles or loops. The information propagates forward through
successive layers of neurons, each layer transforming the input received from the
previous layer.
    Conceptually, this can be thought of as a cascade of neuron activations where
each neuron receives input signals, processes them, and passes the output to the
next layer. This architecture aligns with the idea that sensory information in
biological systems is processed in a hierarchical manner.
    Mathematically, if we denote the input vector as x, the output of layer l
as a(l) , and the weight matrix connecting layer l − 1 to layer l as W(l) , the
feedforward operation is given by:

                             z(l) = a(l−1) W(l) + b(l)                       (5.1)
                                 (l)        (l)
                             a         = f (z ).                             (5.2)

where b(l) is the bias vector and f (·) is the activation function applied element-
wise.

Shapes and convention. We use the row-major (deep-learning) convention.
A single example is a row vector a(l) ∈ R1×nl , a mini-batch stacks examples by
rows A(l) ∈ RB×nl , and weights map features by right multiplication W (l) ∈
Rnl−1 ×nl . Biases b(l) ∈ Rnl broadcast across the batch: Z (l) = A(l−1) W (l) +
1(b(l) )⊤ . We reserve ϕ(·) for kernel feature maps (Appendix B).

Recurrent Neural Networks In contrast, recurrent neural networks (RNNs)
allow information to flow in cycles, enabling feedback connections. This means
that the network’s state at a given time depends not only on the current input
but also on previous states, effectively creating a form of memory.



                                            103
Modern Intelligent Systems                                                        5


   The recurrent architecture is more flexible and biologically plausible since
neurons can influence each other bidirectionally and inputs/outputs can be in-
troduced or sampled at various points in the network. This allows modeling of
temporal sequences and dynamic behaviors. A simple recurrent update is

            ht = f (xt Wxh + ht−1 Whh + bh ),       yt = ht Why + by ,

with the full treatment deferred to Chapter 12.

5.5   Activation Functions
Activation functions determine how the input to a neuron is transformed into
an output signal, effectively controlling the neuron’s excitation level. They play
a critical role in enabling neural networks to model complex, nonlinear relation-
ships.

Biological Motivation In biological neurons, excitation occurs when the com-
bined chemical signals exceed a certain threshold, triggering an action potential
(a ”fire”). Similarly, artificial neurons use activation functions to decide whether
to activate (fire) based on their input.

Common Activation Functions Activation functions map the aggregated
input z to a neuron’s output y = f (z); they inject nonlinearity and control
gradient flow during learning. Different choices trade off biological plausibility,
numerical stability, and ease of optimization.
   • Step Function (Heaviside):
                                             
                                             1   x>0
                                   f (x) =
                                             0   x≤0

      Models a binary firing behavior but is not differentiable, limiting its use
      in gradient-based learning.




                                        104
Modern Intelligent Systems                                                        5


  • Sign Function:                         
                                           
                                           
                                           1       x>0
                                 f (x) =       0    x=0
                                           
                                           
                                           
                                               −1   x<0

     Allows for inhibitory (negative) outputs, mimicking excitatory and in-
     hibitory neuron behavior. We adopt the convention f (0) = 0; some au-
     thors either leave sign(0) undefined or set it to +1, so it is helpful to state
     the choice explicitly.

  • Linear Function:
                                       f (x) = x

     Useful in some contexts but cannot model nonlinearities alone.

  • Sigmoid Function:
                                                  1
                                    f (x) =
                                               1 + e−x
     Smoothly maps inputs to (0, 1), differentiable, and historically popular.
     Because sigmoid outputs saturate near 0 and 1, gradients can become
     small in deep stacks; later chapters discuss practical workarounds and
     alternatives.

  • Hyperbolic Tangent (tanh):

                                                    ex − e−x
                             f (x) = tanh(x) =
                                                    ex + e−x

     Maps inputs to (−1, 1), zero-centered, often preferred over sigmoid.

  • ReLU (Rectified Linear Unit):

                                   f (x) = max(0, x)

     Computationally eﬀicient and helps mitigate vanishing gradient problems.




                                       105
Modern Intelligent Systems                                                      5


 Notation note: activations and thresholds
 In this chapter we use f (·) as a generic placeholder for an activation
 function; when we need the logistic sigmoid specifically we write σ(·).
 Elsewhere in the book, ϕ(·) denotes a kernel feature map. For thresholded
 functions we adopt H(0) = 1 (Heaviside) and sgn(0) = 0 by convention.
 These choices do not affect continuous models but keep examples
 consistent.


5.6   Learning Paradigms in Neural Networks
When building a neural network, whether feedforward or recurrent, the funda-
mental process involves producing an output, comparing it with a target, and
then adjusting the network parameters based on the error. This iterative process
is the essence of learning. We distinguish several learning paradigms depending
on the availability and nature of the target information:

Supervised Learning In supervised learning, the network is provided with
input-output pairs. The network produces an output for a given input, compares
it to the known target output, computes an error, and updates its parameters to
reduce this error. This requires labeled data and is the most common learning
paradigm in practice.

Unsupervised Learning In unsupervised learning, there is no explicit target
output. The network must discover patterns or structure in the input data by
itself. This often involves competition among different patterns, where some pat-
terns become dominant and reinforce themselves, while others are suppressed.
The network evolves until it reaches an equilibrium state where the learned rep-
resentations stabilize. Beyond competitive learning, unsupervised methods en-
compass clustering, density estimation, dimensionality reduction, autoencoders,
and modern self-supervised objectives—any setting where structure is inferred
directly from the inputs.

Reinforcement Learning Reinforcement learning (RL) models learning from
interaction with feedback. An agent with policy π(a | s) selects actions, collects
rewards, and updates π to improve expected return. Full RL treatments appear


                                       106
Modern Intelligent Systems                                                       5


later; here the point is that not all learning is supervised, and neural-network
controllers are common in modern RL.

5.7   Fundamentals of Artificial Neural Networks
The foundational model of artificial neural networks dates back to McCulloch
and Pitts (1943), who proposed a simple neuron model capturing essential fea-
tures of biological neurons.

McCulloch-Pitts Neuron Model Consider a single neuron with multiple
binary inputs xi ∈ {0, 1}, i = 1, . . . , n. Each input is associated with a weight
wi , which can be positive (excitatory) or negative (inhibitory). The neuron
computes a weighted sum of its inputs:


                                         X
                                         n
                                   S=          w i xi .                       (5.3)
                                         i=1

   The output y of the neuron is determined by comparing S to a threshold θ:

                                   
                                   1,    if S ≥ θ,
                              y=                                              (5.4)
                                   0,    otherwise.

   Key characteristics of this model include:
  • Binary inputs: Inputs are either active (1) or inactive (0).

  • Excitatory and inhibitory weights: Weights wi > 0 excite the neuron,
    while wi < 0 inhibit it.

  • Thresholding: The neuron fires (outputs 1) only if the weighted sum
    exceeds the threshold.

Interpretation This simple neuron can be viewed as a linear classifier that
partitions the input space into two regions separated by the hyperplane defined
by the equation




                                         107
Modern Intelligent Systems                                                     5




                                 X
                                 n
                                        wi xi = θ.                          (5.5)
                                  i=1

   The learning task reduces to finding appropriate weights wi and threshold θ
that correctly classify inputs.

Excitation and Inhibition The neuron can be excited or inhibited depending
on the sign and magnitude of the weights. For example:
  • If all wi > 0, the neuron is purely excitatory.

  • If some wi < 0, those inputs inhibit the neuron.

  • The balance of excitation and inhibition determines the neuron’s response.
In biological circuits inhibition is carried by specialized interneurons, whereas
here a negative weight is an abstract shortcut; the sign simply indicates whether
an input pushes the weighted sum above or below the threshold. Artificial
neurons are function approximators; similarity to biology is inspirational, not
mechanistic.

Learning Objective In this model, learning can be interpreted as adjusting
the weights wi and threshold θ to achieve desired input-output mappings. The
challenge is to find these parameters such that the neuron outputs 1 for inputs
belonging to a certain class and 0 otherwise.

5.8   Mathematical Formulation of the Neuron Output
To summarize, the neuron output is given by

                                                      !
                                    X
                                    n
                             y=f              w i xi − θ ,                  (5.6)
                                        i=1

   where f (·) is the activation function, which in the McCulloch-Pitts model is
a Heaviside step function:




                                         108
Modern Intelligent Systems                                                      5




                                      
                                      1, z ≥ 0,
                              f (z) =                                        (5.7)
                                      0, z < 0.
```

### Findings
Issues flagged:

1. Narrative flow and transition:
   - The chunk begins abruptly with Figure 15 and its description, but the preceding sentence fragment "tory looks like when we minimize a smooth objective: step size and conditioning shape how quickly iterates contract toward the minimizer." appears incomplete and disconnected. It seems like a fragment of a sentence or a transition that is missing context or the beginning of the sentence.
   - The transition from Figure 15 to Figure 16 is not smooth; the text jumps from discussing sigmoid, BCE loss, and L2 shrinkage to gradient descent iterates without a clear linking sentence.
   - Similarly, the jump from Figure 16 to the "Geometry of the logistic surface" section (Figure 17) could benefit from a clearer transition sentence to orient the reader.

2. Reader orientation:
   - The fragment "tory looks like when we minimize a smooth objective..." is confusing and likely a typographical error or incomplete sentence, which disrupts reader orientation.
   - The section "Risk & audit" is presented as bullet points without a clear introductory sentence or paragraph, which may confuse readers about its context or purpose.
   - The "Key takeaways" and "Common pitfalls" sections are well structured but could benefit from brief introductory sentences to frame their purpose.

3. Repetitive templating:
   - The repeated use of "Use it when..." in figure captions is consistent but may feel formulaic. While this is a stylistic choice, consider varying phrasing slightly to improve engagement.

4. Punctuation and spacing:
   - In Figure 15's caption, "Use it when choosing a baseline probabilistic classifier and diagnosing overconfidence." could be clearer with a comma: "...classifier, and diagnosing overconfidence."
   - In the "Risk & audit" bullet points, inconsistent capitalization is present (e.g., "Threshold choice" vs. "Class imbalance" vs. "Probability quality"). Consider standardizing capitalization for bullet points.
   - In the "Imbalance and thresholds" paragraph, the formula "predict class 1 when the logit exceeds log(c10 /c01 );" has inconsistent spacing around the slash and semicolon; it should be "log(c10 / c01);"
   - In the "Confusion matrix" figure caption, "Use it when diagnosing which error types dominate in multiclass settings." could be improved by adding a comma after "settings."
   - In the "Notation note" section, "Elsewhere in the book, ϕ(·) denotes a kernel feature map." The phi symbol is not rendered consistently (sometimes ϕ, sometimes phi). Ensure consistent symbol usage.
   - In the "Sign Function" description, the phrase "We adopt the convention f (0) = 0; some au- thors either leave sign(0) undefined or set it to +1, so it is helpful to state the choice explicitly." has a hyphenated word "au- thors" that should be corrected to "authors."

5. Clarity of prose:
   - The sentence fragment "tory looks like when we minimize a smooth objective: step size and conditioning shape how quickly iterates contract toward the minimizer." is unclear and likely a typographical error.
   - The phrase "The ERM view in Chapter 3 treats learning as minimizing an average loss plus (optionally) a regularizer." could be clearer if "plus (optionally) a regularizer" is rephrased to "plus an optional regularizer."
   - The sentence "The probabilistic view arrives at the same objective from a different direction:" is followed by bullet points but lacks a concluding sentence to tie the points back to the main argument.
   - The paragraph starting with "Once we have a probabilistic classifier..." is dense and could be broken into smaller paragraphs for readability.
   - The "Imbalance and thresholds" section is presented as a paragraph but contains multiple ideas; consider bullet points or clearer separation.
   - The "Learning Paradigms in Neural Networks" section introduces supervised, unsupervised, and reinforcement learning but the last sentence "Full RL treatments appear later; here the point is that not all learning is supervised, and neural-network controllers are common in modern RL." could be clearer if rephrased for flow.

Summary: The main concrete issues are the incomplete sentence fragment at the start, abrupt transitions between figures and sections, inconsistent punctuation and spacing, a hyphenation error, and some dense paragraphs that could be better structured for clarity.

## Chunk 9/31
- Character range: 225439–253800

```text
We explicitly set f (0) = 1; other texts sometimes use f (0) = 21 , so documenting
the convention avoids confusion when comparing derivations. It is also common
to absorb the threshold into an augmented weight vector by defining x0 = 1 and
w0 = −θ, yielding a pure inner product w⊤ x that we will reuse in the perceptron
section.
    This model laid the groundwork for later developments in neural networks,
including the introduction of differentiable nonlinearities that enable gradient-
based learning.

5.9   McCulloch-Pitts neuron: examples and limits
Recall that the McCulloch-Pitts (MP) neuron model is defined by a weighted
sum of binary inputs compared against a threshold to produce a binary output.
Formally, for inputs xi ∈ {0, 1} and weights wi , the neuron output y is given by
                               
                               1 if Pn w x ≥ θ,
                                         i=1 i i
                           y=                                                (5.8)
                               0 otherwise,

where θ is the threshold.

Example: AND and OR gates - For an AND gate with inputs x1 , x2 , set
weights w1 = w2 = 1 and threshold θ = 2. The output is 1 only if both inputs
are 1, matching the AND truth table.
    - For an OR gate, keep weights w1 = w2 = 1 but set θ = 1. The output is 1
if at least one input is 1, matching the OR truth table.
    This demonstrates how the MP neuron can implement simple logical func-
tions by appropriate choice of weights and threshold.

Limitations of the MP model           Despite its conceptual simplicity, the MP
neuron has significant limitations:



                                       109
Modern Intelligent Systems                                                      5


  • No learning mechanism: The weights and threshold must be manually
    assigned or guessed. There is no algorithmic way to adjust parameters
    based on data.

  • Limited computational power: The MP neuron can only represent lin-
    early separable functions. Complex patterns requiring nonlinear decision
    boundaries cannot be modeled.

  • Binary inputs and outputs: The model is restricted to binary signals,
    limiting its applicability to real-valued data.
  These limitations motivated the development of more sophisticated neuron
models and learning algorithms.

5.10   From MP Neuron to Perceptron and Beyond
The MP neuron laid the groundwork for subsequent models that introduced
learning capabilities and continuous-valued inputs and outputs.

Perceptron model The perceptron, introduced by Rosenblatt in 1958, ex-
tends the MP neuron by incorporating a learning algorithm to adjust weights
based on training data. The perceptron output is
                              
                              1 if w⊤ x + b ≥ 0,
                          y=                                           (5.9)
                              0 otherwise,

where x is the input vector, w the weight vector, and b the bias (threshold).
 Targets and encodings
 We switch between labels in {0,1} (probability view) and labels in {-1,+1}
 (margin view). Convert with y_pm = 2*y01 - 1 and y01 = (y_pm + 1)/2.
 Perceptron updates below use the {-1,+1} encoding.

    The perceptron learning rule iteratively updates weights to reduce classifi-
cation errors, enabling the model to learn from data rather than relying on
manual parameter selection. With labels yi ∈ {−1, +1}, a mistake triggers
w ← w + ηyi xi and b ← b + ηyi . The induced separating hyperplane and signed
distance are illustrated in Figure 21.


                                      110
Modern Intelligent Systems                                                    5


Perceptron update from the signed margin. Let di = yi (w⊤ xi + b) be
the signed margin. If di ≥ 0 the example is correctly classified; if di < 0 the
example is misclassified. A common perceptron criterion is
                                 X              X
                   J(w, b) = −         di = −         yi (w⊤ xi + b),
                                 i∈M            i∈M

where M is the set of misclassified examples. Taking a gradient step on J yields

                       w ← w + ηyi xi ,          b ← b + ηyi ,

which is exactly the perceptron update. In augmented form, set x0 = 1 and
w0 = b, and the update becomes w ← w + ηyi xi . Geometrically, each mistake
nudges the hyperplane so the signed distance di increases.

Perceptron convergence theorem. If a training set is linearly separable
with margin γ > 0, the perceptron learning algorithm is guaranteed to find a
separating hyperplane after at most (R/γ)2 updates, where R bounds the input
norms. Rescaling features changes R and γ, so standardizing inputs tightens
the bound. When the data are not separable the algorithm can cycle forever;
Section 6.1 (and Chapter 6) therefore emphasize feature scaling, bias terms, and
the move to differentiable multilayer models to handle nonlinear problems.




                                         111
Modern Intelligent Systems                                                    5


 Perceptron convergence theorem (proof sketch)
 Assume there exists a unit vector w⋆ such that yi w⋆ ·xi ≥ γ for all i and
 that kxi k ≤ R. Let w(t) denote the perceptron weights after t mistakes.
 Each mistake updates:
                            w(t+1) = w(t) + yi xi .

    1. Progress along the separator. The inner product with w* grows
       by at least gamma each mistake:

                             w(t+1) · w⋆ = w(t) · w⋆ + yi xi · w⋆
                                         ≥ w(t) · w⋆ + γ.

       Thus after T mistakes, the dot product with w* is at least T*gamma.

    2. Bounding the norm. The squared norm grows slowly:

                      kw(t+1) k2 = kw(t) k2 + kxi k2 + 2yi xi · w(t)
                                   ≤ kw(t) k2 + R2 ,

       because the mistake condition implies yi xi · w(t) ≤ 0. Inductively,
       kw(T ) k2 ≤ T R2 .

    3. Combine via Cauchy–Schwarz.

                                T γ ≤ w(T ) · w⋆
                                                        √
                                    ≤ kw(T ) kkw⋆ k ≤       T R,

       which implies T ≤ (R/γ)2 .
 Therefore the perceptron halts after finitely many mistakes on separable
 data. If the data are not separable, some γ > 0 cannot be found, and the
 above argument no longer applies; hence the need for multilayer networks.




                                          112
Modern Intelligent Systems                                                          5



                        Class +1
                        Class −1      2




                                            d(x, H)

                         −2                           2




                                                          w
                                                          ⊤x
                                    −2                    C=1




                                                              +
                                                               b
                                                                  =
                                                                   0
    Figure 21: Perceptron geometry. Points on opposite sides of the separating
       hyperplane receive different labels, and signed distance to the boundary
     controls both prediction and update magnitude. Compare with Figure 17 in
    Chapter 4: both are linear separators, but logistic smooths the boundary into
    calibrated probabilities. Use it when relating margin geometry to update size
                                    and convergence.


 Common perceptron pitfalls
    • Feature scaling: Large-magnitude features dominate updates;
      standardize inputs first.

    • Random seed sensitivity: Different initial weights can lead to
      drastically different separating hyperplanes.

    • Non-separable data: Without slack variables or kernels the
      perceptron will not converge; diagnose this before training
      indefinitely. XOR is the canonical counterexample.


Adaline model The Adaptive Linear Neuron (Adaline), developed in the
1960s, further improves on the perceptron by using a linear activation function
and minimizing a continuous error function (mean squared error). This allows
the use of gradient descent for training, leading to more stable convergence.




                                          113
Modern Intelligent Systems                                                          5


Adaline weight update (derivation) Adaline uses a linear output y =
w⊤ x + b and the squared error

                                  E = 12 (t − y)2 .

The gradient is ∂E/∂w = −(t − y)x and ∂E/∂b = −(t − y), so the update is

                   w ← w + η(t − y)x,          b ← b + η(t − y).

Unlike the perceptron, Adaline updates on every example and scales the step by
the residual t − y; this is the first explicit appearance of gradient-based weight
optimization in the neural narrative.
    The perceptron and Adaline models are limited to linearly separable prob-
lems. To overcome this, multilayer perceptrons (MLPs) with hidden layers were
introduced; Chapter 6 and Chapter 7 develop the mechanics in full.
 Perceptron vs. logistic regression
 Linear score s(x) = w⊤ x + b. The perceptron predicts ⊮[s ≥ 0] and
 updates w ← w + ηyi xi (and b ← b + ηyi ) only on mistakes, with
 yi ∈ {−1, +1}. Logistic regression predicts σ(s), minimizes cross-entropy
    P                                                       P
 − i yi log σ(si ) + (1 − yi ) log(1 − σ(si )), and steps by i (σ(si ) − yi )xi .
 Prefer logistic when calibrated probabilities and smooth optimization are
 needed (Chapter 4).

 Author’s note: what a single perceptron cannot express
 A single perceptron makes one global, all-or-none decision: one hyperplane,
 one threshold, one set of weights shared across every example. That
 simplicity is the point of the model, but it also explains its limitations.
 Many real problems require communities of units that specialize: different
 hidden units respond to different regions, features, or patterns, and their
 combined vote produces a flexible decision surface. Multi-layer networks do
 not just add parameters; they add internal structure that lets different
 parts of the model “care about” different parts of the data.




                                        114
Modern Intelligent Systems                                                        5


 Key takeaways
 Minimum viable mastery
    • The perceptron and Adaline turn threshold units into trainable
      classifiers by updating weights from data.

    • Geometry (hyperplanes and signed distance) explains predictions and
      update magnitude.

    • Logistic regression keeps the same linear score but learns calibrated
      probabilities via a smooth loss (Chapter 4).

    • Nonlinear tasks (e.g., XOR) require multilayer networks and
      backpropagation (Chapters 6 to 7).

 Common pitfalls
    • Expecting a single hyperplane to solve nonconvex structure: without
      hidden units you cannot express XOR-like logic.

    • Mixing label codings ({−1, +1} vs. {0, 1}) without adjusting the
      loss/update formulas.

    • Treating linear scores as probabilities: calibrated probabilities require
      a probabilistic model/loss (e.g., logistic).

 Exercises and lab ideas
    • Implement a minimal example from this chapter and visualize
      intermediate quantities (plots or diagnostics) to match the
      pseudocode.

    • Stress-test a key hyperparameter or design choice discussed here and
      report the effect on validation performance or stability.

    • Re-derive one core equation or update rule by hand and check it
      numerically against your implementation.

 If you are skipping ahead. Remember the two bottlenecks that force
 multilayer networks: expressivity (nonlinear boundaries) and trainability
 (smooth gradients). Chapter 6 and Chapter 7 assume these motivations.



                                      115
Modern Intelligent Systems                                                    6


Where we head next. Perceptrons are intentionally simple: hard thresholds
and uniform updates. Their strengths (linear separation) and limits (for example
XOR) motivate multilayer models. Chapter 6 continues this thread by chaining
units, defining a loss, and asking the key training question: how should weights
change to improve performance? That question leads directly to the chain rule
and smooth activations. Chapter 7 then scales the same bookkeeping to arbitrary
depth and eﬀicient implementation.


6 Multi-Layer Perceptrons: Challenges and Founda-
  tions
Chapter 5 introduced the perceptron and Adaline: single units that learn by
updating weights from data, with Adaline giving our first explicit glimpse of
gradient descent on a smooth performance function.
    In this chapter we keep the story linear and concrete. We build the smallest
possible network (two neurons in series), define a performance function, and
ask the core question: how should the weights change to improve performance?
Answering that question forces us to use derivatives (the chain rule) and leads
naturally to gradient descent. Along the way we encounter a practical obstacle:
hard thresholds are not differentiable, so they do not support gradient-based
learning. We replace them with smooth activations and immediately gain a
clean update story. This is the conceptual bridge to full backpropagation in
Chapter 7. Figure 1 shows this as the hinge between single-unit models and
multilayer training.




                                      116
Modern Intelligent Systems                                                     6


 Learning Outcomes
 After this chapter, you should be able to:
      • Build the smallest multi-layer network and write its forward
        equations.

      • Define a simple performance (loss) function for the network output.

      • Explain why gradient descent is the right tool for weight updates.

      • Show why hard thresholds block gradients and motivate smooth
        activations.

      • Derive the weight updates for the two-neuron network using the
        chain rule.

 Design motif
 Build the smallest trainable network you can, keep every intermediate
 quantity visible, and let the chain rule explain how learning signals flow.


6.1    From a single unit to the smallest network
A short map: building a trainable network. The chapter follows one
tight loop:
  • Build: write the forward computation (a two-neuron chain).

  • Judge: define a performance function P (we use squared error).

  • Move: use derivatives to update parameters via gradient descent.

  • Fix: choose a differentiable activation so those derivatives exist and carry
    signal.
Once you can execute this loop for two neurons, scaling to many neurons is
mostly bookkeeping (Chapter 7).

How this chapter fits the workflow. The same objective→audit workflow
from the supervised toolkit still applies; what changes is the representation.
  • From Chapter 3: diagnostics (learning curves, bias–variance) tell you what
    is going wrong.


                                      117
Modern Intelligent Systems                                                       6


   • From Chapter 4: a linear probabilistic baseline tells you how far you can
     go without nonlinear features.

   • Here: we build the smallest nonlinear network and derive its gradient
     updates, setting up the general backprop machinery in Chapter 7.

Function estimation as the unifying view. Learning is function estima-
tion: approximate some unknown mapping f : X → Y from examples. A neural
network is a structured way to represent a nonlinear f by composing simple
units. In this chapter we keep the bookkeeping minimal and use one tiny net-
work plus a simple squared error objective so we can focus on the mechanics of
learning.

From one unit to a chain of units. A perceptron computes a weighted sum
and then applies an activation (often a threshold in the classical presentation):

                             y = f (p),    p = w⊤ x + b,                     (6.1)

where x ∈ Rn , w ∈ Rn , and b is a bias (threshold). Because the boundary
w⊤ x + b = 0 is a hyperplane, a single unit can only represent linear separations.
This explains the classic XOR failure and motivates building a network of units.
   The smallest network that is more than a single unit is a two-neuron chain:
one neuron feeds another. Write

                  p1 = w1⊤ x + b1 ,                  y1 = f (p1 ),           (6.2)
                  p2 = w 2 y 1 + b 2 ,               y2 = f (p2 ).           (6.3)

Even this tiny network introduces the central idea of neural networks: intermedi-
ate computations (here y1 ) are reused and influence the final output y2 . A single
neuron is a linear classifier; chaining neurons gives a nonlinear representation.
With multiple hidden units, that added structure is enough to solve XOR. We
will reuse Figure 22 as the bookkeeping diagram when we apply the chain rule.

Author’s note: why a network changes the story. With one percep-
tron, every training example pushes on the same single separator. A network
introduces intermediate representations: different hidden units can respond to


                                          118
Modern Intelligent Systems                                                                    6


               p1 = w1⊤ x + b1                            p 2 = w 2 y1 + b 2
       x                         f                   f                             y2
                                      y1 = f (p1 )
                                                                               y2 = f (p2 )

      Figure 22: The minimal neural network used in this chapter is a two-neuron
       chain. The first unit produces an intermediate signal, and the second unit
        maps that signal to the final output. Use it when tracking variables and
              gradients in a toy network before scaling to deeper models.


different patterns, and the output unit can combine those responses. That added
structure is what lets neural networks model nonlinearity while still using simple
building blocks.

A checklist of what we must settle (and why). To turn “a diagram of
neurons” into something trainable, we need:
  • A parameterization: weights and biases that control the mapping from
    inputs to outputs.

  • A performance function: a scalar P that is lower when the output is
    better.

  • An update rule: a systematic way to change parameters to reduce P .

  • Differentiability: if we want to use gradient descent, every link from
    parameters to P must be differentiable so the chain rule can propagate
    credit (and blame).
The chapter keeps everything small so you can see all four ingredients in one
place.

Bias as a learned threshold. A hard threshold θ can be absorbed into a bias
term by writing p = w⊤ x − θ and setting b = −θ. In practice we append x0 = 1
and treat b as another weight w0 ; the algebra is identical. The bias handles
where the unit switches, while the weights handle which direction it prefers.

6.2     Performance: what are we trying to improve?
Once we have a forward computation, we need a performance function that tells
us whether the output is good. For one training example with target t, a simple


                                          119
Modern Intelligent Systems                                                      6


choice is the squared error
                                   1
                                P = (y2 − t)2 .                              (6.4)
                                   2
The factor 21 makes derivatives cleaner. If you prefer to maximize a score rather
than minimize an error, you could take − 21 (y2 − t)2 instead. The math below is
identical up to a sign. We will minimize P .

Why a square? The signed error e = y2 − t can be positive or negative.
Squaring removes the sign and penalizes large deviations more heavily, while
keeping P smooth so a small change in a weight produces a small change in
performance. That smoothness is exactly what makes derivative-based updates
meaningful.
 Author’s note: one objective is enough for the first derivation
 We only need a performance function that (1) is easy to differentiate and
 (2) rewards outputs that move toward the target. The squared error does
 both, so it is a good stand-in while we learn the mechanics. Once the chain
 rule story is clear, swapping in other objectives is mostly a matter of
 changing a few local derivatives at the output layer.


A geometric intuition. For a fixed input, the performance becomes a surface
over the weights. If the surface looks like a “bowl,” then the bottom is the
optimum. The goal is to move weights along this surface in the direction that
improves performance. Figure 23 visualizes this geometry and contrasts vector
updates with coordinate-wise zig-zag steps.

6.3   Gradient descent: how do weights move?
We now ask: how should w1 , w2 , b1 , b2 change to reduce P ? The standard answer
is gradient descent:
                                 θ ← θ − η∇θ P,                              (6.5)

where θ stands for any parameter and η > 0 is the step size. Geometrically, you
can picture the performance surface as a landscape: the gradient points uphill,
so we step in the opposite direction to descend toward a minimum. The step
size controls how far we move; too large can overshoot, too small can crawl.


                                       120
Modern Intelligent Systems                                                            6



                                          2   w2
                                       one weight
                                        at a time
                                           1
                             −∇P
                                                                    w1

                      −2        −1                    1         2

                                        −1


                                        −2


        Figure 23: Think of performance as a surface over the weights. Gradient
      descent moves in one vector step (blue), whereas coordinate-wise updates can
       zig-zag (orange). Use it when building intuition for why gradient directions
                   reduce loss more eﬀiciently than axis-aligned steps.


   For a weight vector, the update is a vector step:

                                     ∆w = −η∇w P.                                 (6.6)

This is the “move the weights in the right direction” story made precise: we
do not guess the direction; we compute it from the derivative of performance.
Importantly, we update all weights at once (a vector step), not one coordinate
at a time.

Step size is a design choice. The gradient gives a direction; the step size η
sets the distance. In practice you pick η small enough to avoid oscillation and
large enough to make progress. Chapter 7 returns to this choice (learning-rate
schedules, momentum, and other practical stabilizers) once the core derivative
story is solid.

6.4     Why hard thresholds block learning
At this point the story is simple: define P , compute ∇P , and update weights.
The catch is that computing ∇P requires derivatives through the activation.
When we apply the chain rule to Equation (6.3), factors like f ′ (p1 ) and f ′ (p2 )
appear immediately. Figure 24 makes this derivative contrast concrete.
   If f is a hard threshold (a step function), it is discontinuous and non-differ-


                                           121
Modern Intelligent Systems                                                                       6



                 Hard threshold (step)                      Smooth activation (sigmoid)

                        1                                             1


                                                                     0.5

                                         p                                            p

           −4     −2              2          4         −4       −2              2         4


        Figure 24: Hard thresholds block gradient-based learning because the
      derivative is zero almost everywhere. A smooth activation like the sigmoid
      provides informative derivatives across a wide range of inputs. Use it when
         motivating why smooth nonlinearities enable gradient-based training.


entiable at the threshold. That breaks the gradient story: f ′ (p) either does not
exist or is zero almost everywhere, so derivatives cannot guide learning. This is
the core reason we replace thresholds with smooth, differentiable activations.

Absorbing the threshold. The threshold itself can be folded into a bias
term, but the discontinuity remains. We remove the discontinuity by choosing
a smooth f .

6.5   Differentiable activations and the sigmoid trick
A classic choice is the logistic (sigmoid) function

                                                     1
                                      σ(p) =              .                                   (6.7)
                                                  1 + e−p

It maps real inputs to (0, 1) and is differentiable everywhere. The key identity
is
                             σ ′ (p) = σ(p) [1 − σ(p)].                    (6.8)

This is a useful trick: the derivative is a function of the output itself. If y = σ(p)
is already computed in the forward pass, then σ ′ (p) = y(1 − y) is immediately
available in the backward pass. No extra exponentials are needed.




                                                 122
Modern Intelligent Systems                                                              6


 Author’s note: the derivative is already in the forward pass
 In practice you rarely want to recompute expensive expressions during
 learning. For the sigmoid, once you have computed the output y =
 sigmoid(p), you also have its slope for free: sigmoid_prime = y*(1-y).
 This is a small example of a bigger pattern: backpropagation works
 because we cache intermediate results on the forward pass and reuse them
 on the backward pass.


Derivation sketch. Let β = σ(α) = (1 + e−α )−1 . Differentiate:
                                                                
           dβ      e−α                    1                 1
              =             =                         1−               = β(1 − β).
           dα   (1 + e−α )2            1 + e−α           1 + e−α

This is the exact algebraic shortcut used in neural networks.

6.6   Deriving weight updates for the two- neuron network
The diagram in Figure 22 is also a derivative map: to update a weight, follow
how a small change in that weight would flow forward to the output and then
back to the performance. The chain rule turns that story into algebra.
   We now compute the gradients in Equation (6.3) using the chain rule. First
note the easy derivatives:
      ∂P
  •       = y2 − t.
      ∂y2
      ∂yi
  •       = f ′ (pi ).
      ∂pi
      ∂p2          ∂p2
  •       = y1 and     = w2 .
      ∂w2          ∂y1
      ∂p1
  •       = x.
      ∂w1

Second layer.

                         ∂P    ∂P ∂y2 ∂p2
                             =             = (y2 − t) f ′ (p2 ) y1 ,                 (6.9)
                         ∂w2   ∂y2 ∂p2 ∂w2




                                            123
Modern Intelligent Systems                                                 6


and similarly
                                  ∂P
                                      = (y2 − t)f ′ (p2 ).             (6.10)
                                  ∂b2

First layer. The first layer feels the effect of the second layer through the
chain rule:
                        ∂P    ∂P ∂y2 ∂p2 ∂y1 ∂p1
                            =                                          (6.11)
                        ∂w1   ∂y2 ∂p2 ∂y1 ∂p1 ∂w1
                                = (y2 − t) f ′ (p2 ) w2 f ′ (p1 ) x,   (6.12)

with bias derivative
                             ∂P
                                 = (y2 − t)f ′ (p2 )w2 f ′ (p1 ).      (6.13)
                             ∂b1

Error terms (backprop view). Define
```

### Findings
Issues flagged:

1. Inconsistent spacing around parentheses and variables:
   - "f (0) = 1; other texts sometimes use f (0) = 21 ," — the "21" likely should be "1/2" or "½" (typo or formatting error).
   - Spaces between function names and parentheses (e.g., "f (0)" instead of "f(0)") are inconsistent with standard mathematical notation and may confuse readers.

2. Equation formatting and punctuation:
   - Equation (5.8) is presented with a broken line and inconsistent alignment; the summation index and terms are split awkwardly, which may disrupt readability.
   - The phrase "Pn w x ≥ θ," is broken with subscripts and summation symbols in a way that is hard to parse.
   - The use of commas and periods around equations and inline math is inconsistent; for example, "weights w1 = w2 = 1 and threshold θ = 2." ends with a period, but the next sentence starts with a dash ("- For an OR gate...") which is stylistically inconsistent.

3. Section transitions and narrative flow:
   - The transition from the MP neuron limitations to the perceptron model is abrupt; a brief linking sentence summarizing the motivation for perceptron introduction would improve flow.
   - The "Targets and encodings" subsection is embedded inline without a clear heading or separation, making it harder to locate and disrupting reader orientation.
   - The "Author’s note" sections are helpful but sometimes interrupt the flow; consider setting them apart more clearly or placing them as sidebars or footnotes.

4. Repetitive templating and phrasing:
   - The phrase "Use it when..." in figure captions is repeated multiple times and may feel formulaic.
   - The "Key takeaways," "Common pitfalls," and "Exercises and lab ideas" sections are well structured but could benefit from more varied phrasing to avoid templating.

5. Minor punctuation and spacing issues:
   - Missing spaces after commas in some places (e.g., "w ← w + ηyi xi and b ← b + ηyi . The induced separating hyperplane..." should have consistent spacing).
   - Inconsistent use of en-dashes and hyphens in ranges and lists (e.g., "Chapters 6 to 7" vs. "Chapter 6 and Chapter 7").
   - The phrase "the factor 21 makes derivatives cleaner" likely intends "the factor 1/2" or "the factor ½"; this is a critical typo.

6. Clarity of prose:
   - Some sentences are dense and could be simplified for clarity, e.g., "The perceptron learning rule iteratively updates weights to reduce classification errors, enabling the model to learn from data rather than relying on manual parameter selection." could be split for easier reading.
   - The explanation of the perceptron convergence theorem proof is mathematically correct but might benefit from more explicit signposting or breaking into smaller steps for graduate readers less familiar with the proof.

7. Figure references:
   - Figure 21 is referenced before its caption appears, which is acceptable, but the caption itself is quite long and includes instructions ("Use it when...") that might be better placed in the main text or as a note.
   - Figure 22 and Figure 23 captions also include "Use it when..." phrasing, which may be better integrated into the text or rephrased.

Overall, the content is technically sound and well organized, but improvements in formatting, transitions, and minor typographical errors would enhance readability and professional polish.

## Chunk 10/31
- Character range: 253803–284232

```text
∂P
                              δ2 :=       = (y2 − t)f ′ (p2 ).         (6.14)
                                      ∂p2

Then ∂P/∂w2 = δ2 y1 and ∂P/∂b2 = δ2 . The first layer receives a backpropa-
gated error
                              ∂P
                        δ1 :=     = δ2 w2 f ′ (p1 ),                 (6.15)
                              ∂p1
so ∂P/∂w1 = δ1 x and ∂P/∂b1 = δ1 .
    This is the central lesson: once we compute a local error term, it can be
reused across many gradients. That reuse is exactly what makes backpropaga-
tion eﬀicient and is why deeper networks remain tractable.




                                            124
Modern Intelligent Systems                                                      6


 Worked example: one numerical gradient step (sanity check)
 Take a single input x = [1, −1]⊤ , target t = 1, sigmoid activation f = σ,
 and parameters w1 = [0.8, 0.2]⊤ , b1 = 0, w2 = 1, b2 = 0.
 Forward: p1 = 0.6, y1 = σ(p1 ) ≈ 0.646; p2 = y1 , y2 = σ(p2 ) ≈ 0.656;
 P = 12 (y2 − t)2 ≈ 0.059.
 Backward: σ ′ (p) = y(1 − y), so δ2 = (y2 − t)σ ′ (p2 ) ≈ −0.078 and
 δ1 = δ2 w2 σ ′ (p1 ) ≈ −0.018. Thus ∇w1 P = δ1 x ≈ [−0.018, +0.018]⊤ and
 ∇w2 P = δ2 y1 ≈ −0.050.
 Update: with η = 0.5, gradient descent increases w2 slightly (since the
 gradient is negative) and nudges w1 in a direction that increases y2 toward
 the target.


6.7   From two neurons to multi- layer networks
Nothing essential changes for deeper networks; we simply apply the same chain
rule repeatedly. For a layer l with pre-activations p(l) and weights W (l+1) , the
error signal satisfies
                                                  
                       δ (l) = δ (l+1) (W (l+1) )⊤ ◦ f ′ (p(l) ),           (6.16)

where ◦ denotes element-wise multiplication. This recursion is the heart of
backpropagation, which we derive and operationalize in Chapter 7.
 Author’s note: what backprop adds
 Conceptually, nothing new happens when you go from two neurons to
 many layers: it is still the chain rule and the same local derivatives. What
 changes is the organization: we run a forward pass that caches
 intermediate values, then a backward pass that reuses those caches to
 compute all gradients eﬀiciently (and stably) for an entire batch.
 Chapter 7 turns the recursion into an implementable algorithm and shows
 the standard bookkeeping.




                                         125
Modern Intelligent Systems                                                           6


6.8    Summary
  • A two-neuron chain is the smallest network that goes beyond a single
    perceptron.

  • Learning starts by defining a performance function and asking how weights
    change it.

  • Gradient descent uses derivatives to choose the correct update direction.

  • Hard thresholds obstruct gradients; smooth activations fix the problem.

  • The sigmoid derivative σ ′ (p) = σ(p)(1 − σ(p)) is a convenient identity
    because it reuses the output.

  • The two-neuron derivation already contains the backpropagation pattern
    used in deep networks.

 Derivation closure: implement, cache, fail-fast
      • Implement: treat the chapter equations as a forward function plus a
        scalar loss; write them once in vector form before batching.

      • Cache: keep (x, p1 , y1 , p2 , y2 ) from the forward pass so each gradient
        term is a local reuse, not a re-derivation.

      • Fail-fast checks: run finite-difference gradient checks on a tiny
        example, then track train/validation divergence to catch update-sign
        or step-size mistakes early.

      • Handoff: the same cache-then-backward discipline scales directly in
        Chapter 7; only bookkeeping grows.




                                        126
Modern Intelligent Systems                                                      6


 Key takeaways
 Minimum viable mastery
    • Training is a loop: define a forward computation, define a scalar
      performance, then use derivatives to update parameters.

    • Hard thresholds break the gradient story; smooth activations (e.g.,
      sigmoid) restore informative derivatives.

    • The two-neuron derivation already contains the reusable “local error”
      pattern that scales to deep networks.

 Common pitfalls
    • Trying to differentiate through discontinuities (step functions) and
      then “patching” gradients by hand.

    • Losing the chain rule in bookkeeping: cache intermediate values and
      reuse them consistently.

    • Confusing notation: distinguish pre-activation vs. activation, and
      keep shapes explicit when batching.

 Exercises and lab ideas
 Setup. These reinforce the two-neuron derivation and prepare you for the
 multi-layer bookkeeping in Chapter 7.
    • Numerical gradient check: Implement finite differences for the
      two-neuron chain and compare to your analytic gradients; report
      relative error.

    • Step vs. sigmoid: Replace the smooth activation with a hard
      threshold and observe what breaks when you try to compute updates
      via derivatives.

    • XOR with two hidden units: Train a tiny MLP on XOR and plot
      its decision regions; note sensitivity to initialization and step size.

 If you are skipping ahead. Be able to read a forward graph and a
 backward recursion: local derivatives, cached activations, and a scalar loss
 driving parameter updates. That is exactly what Chapter 7 scales up.


                                     127
Modern Intelligent Systems                                                      7


Where we head next. Chapter 7 lifts this two-neuron derivation to deep
networks and shows how to implement the same backward logic eﬀiciently in
batch training.


7 Backpropagation Learning in Multi-Layer Percep-
  trons
Building on the two-neuron derivation in Chapter 6, we derive backpropagation
for an L-layer network as a systematic application of the chain rule. The idea is
unchanged: compute local error terms (the δ’s), then reuse them to obtain all
weight gradients eﬀiciently. Figure 1 marks this chapter as the training engine
for deep models.
  Learning Outcomes
      • Derive the layerwise backpropagation recursions for arbitrary-depth
        MLPs.

      • Connect theoretical gradients to implementation details
        (vectorization, caching, numerical stability).

      • Translate training diagnostics (learning curves, early stopping) into
        concrete optimization policies.

  Design motif
  Compute local error signals once, then reuse them to update every
  parameter eﬀiciently. The organization (cache forward values, then sweep
  backward) is the algorithm.


7.1    Context and Motivation
Multi-layer networks raise a specific question: How do we update the weights
across multiple layers when the only explicit error signal is at the output? In a
single-layer perceptron, the output error touches the weights directly; in a deep
network, a change in one layer propagates through subsequent layers and alters
the output in a nonlinear, intertwined way.
    Shallow networks (one hidden layer) already move beyond linear separability,
but more complex tasks demand deeper hierarchies of features. The multi-layer


                                       128
Modern Intelligent Systems                                                        7


perceptron stacks these layers to learn richer decision boundaries, and backprop-
agation is the mechanism that makes that depth trainable.

Implementation lens. A practical MLP rarely updates one coordinate at
a time; gradients are treated as full vectors so every weight moves coherently.
Backpropagation is what turns a multilayer diagram into a trainable model: it
reuses local error signals so you can compute all gradients eﬀiciently, making it
practical to learn hidden representations (not just tune a final linear layer) while
keeping the same validation→audit discipline (learning curves, early stopping,
and slice checks).

7.2   Problem Setup
Consider a multi-layer perceptron with layers indexed by l = 1, 2, . . . , L, where
L is the output layer. Each layer l contains neurons indexed by i, and the
                                             (l)
output of neuron i in layer l is denoted by ai . The input to this neuron before
                           (l)
activation is denoted by zi . The weights connecting neuron i in layer l − 1 to
                                      (l)
neuron j in layer l are denoted by wij .
    The forward pass through the network is given by:

                              (l)
                                    X (l−1) (l)   (l)
                             zj =    ai    wij + bj ,                         (7.1)
                                     i
                              (l)            (l) 
                             a j = f zj              ,                        (7.2)

        (l)
where bj is the bias term for neuron j in layer l, and f (·) is the activation
function, typically nonlinear (e.g., sigmoid, ReLU). Equation (7.1) makes it
explicit that we sum over every incoming neuron i in layer l − 1 to form the
                      (l)
aﬀine pre-activation zj .

7.3   Loss and Objective
To keep the story linear (and aligned with Chapter 6), we will use a simple
squared-error objective. Let the network output be a(L) and let t be the target
(one-hot targets for classification are fine; we do not need a separate regression/-
classification split yet). A standard loss is

                                    1 X           
                                                (L) 2
                             L=          tk − a k     .                       (7.3)
                                    2
                                         k


                                              129
Modern Intelligent Systems                                                              7


                                                     (l)
The goal of learning is to adjust the weights {wij } to minimize L. Later in this
chapter, we briefly note how common alternatives (notably cross-entropy with
sigmoid/softmax outputs) simplify the output-layer error term; the backprop
recursion itself does not change.

7.4   Challenges in Weight Updates
In a shallow network, weight updates can be computed directly from the output
error. However, in a deep network, the output error depends on all weights in a
complex way. A change in a weight in an earlier layer affects the activations of
subsequent layers, ultimately influencing the output.
                                       (l)
    For example, consider a weight wij connecting neuron i in layer l − 1 to
                                                           (l)                 (l)
neuron j in layer l. Changing this weight affects zj , which affects aj , which
in turn affects all neurons in layers l + 1, l + 2, . . . , L. Therefore, the total effect
               (l)
of changing wij on the loss is a composition of many intermediate effects.

7.5   Notation for Layers and Neurons
To formalize this, we introduce the following notation:
   • l: layer index, with l = 0 representing the input layer, and l = L the
     output layer.

   • i: neuron index in layer l − 1.

   • j: neuron index in layer l.

   • k: neuron index in layer L (output layer).
       (l)
   • ai : activation of neuron i in layer l.
       (l)
   • zj : weighted input to neuron j in layer l.
        (l)
   • wij : weight from neuron i in layer l − 1 to neuron j in layer l.
       (l)
   • bj : bias of neuron j in layer l.

   • f (·): activation function.
These definitions carry directly into the forward-pass recap below, where we
chain the aﬀine map and nonlinearity across layers.




                                          130
Modern Intelligent Systems                                                   7


Notation handoff. Across this chapter, a denotes activations and z denotes
pre-activations; this pairing is reused in later deep-learning chapters. If you
jump into chapters out of order, keep Appendix D nearby for symbol overloads.

7.6   Forward Pass Recap
The forward pass computes activations layer by layer:

                             (l)
                                    X (l−1) (l)   (l)
                             zj =    ai    wij + bj ,                     (7.4)
                                      i
                              (l)          (l) 
                             aj = f       zj       .                      (7.5)

                                    (L)
   The output layer activations ak             are compared to the




                                               131
Modern Intelligent Systems                                                 7


 Mini example: two-layer backprop in practice
 # Shapes: X in R^{B x d}, W1 in R^{d x h}, W2 in R^{h x c}
 def step(X, Y, params, eta, wd=1e-4, p_drop=0.1):
     W1, b1, W2, b2 = params
     B = X.shape[0]
     # Forward pass
     Z1 = X @ W1 + b1
     H1 = relu(Z1)
     mask1 = (np.random.rand(*H1.shape) > p_drop).astype(
         H1.dtype
     )
     # inverted dropout
     H1 = H1 * mask1 / (1 - p_drop)
     Z2 = H1 @ W2 + b2
     Yhat = softmax(Z2)
     # Backward pass
     delta2 = (Yhat - Y) / B            # CE output error
     grad_W2 = H1.T @ delta2
     grad_W2 += wd * W2              # L2 decay
     grad_b2 = delta2.sum(axis=0)
     delta1 = (delta2 @ W2.T) * relu_deriv(Z1)
     # dropout backprop
     delta1 = delta1 * mask1 / (1 - p_drop)
     grad_W1 = X.T @ delta1
     grad_W1 += wd * W1
     grad_b1 = delta1.sum(axis=0)
     # SGD step
     return (W1 - eta * grad_W1, b1 - eta * grad_b1,
             W2 - eta * grad_W2, b2 - eta * grad_b2)


 The elementwise product * mirrors the Hadamard notation from
 Equations (7.1) to (7.2). This miniature example bridges the algebra to
 vectorized code before we scale to L-layer MLPs later in the chapter.




                                     132
Modern Intelligent Systems                                                        7


  Shape ledger for an L-layer MLP (batch size B)
      • A(l−1) ∈ RB×nl−1 , Z (l) , δ (l) ∈ RB×nl

      • W (l) ∈ Rnl−1 ×nl , b(l) ∈ Rnl

      • ∂L/∂W (l) = (A(l−1) )⊤ δ (l) /B ∈ Rnl−1 ×nl

      • ∂L/∂b(l) = batch_mean(δ (l) ) ∈ Rnl
  Layers share this structure; convolutional/sequence models reuse the same
  calculus with different bookkeeping.


7.7    Backpropagation: Recursive Computation of Error Terms
Recall that our goal is to compute the gradient of the loss with respect to the
weights in the network, specifically for weights connecting layer l to layer l + 1.
We denote the weight connecting neuron i in layer l to neuron j in layer l + 1 as
 (l)
wij .
    We will continue with the squared-error loss from Chapter 6:

                                       1X        (L)
                                L=        (tk − ak )2 .                        (7.6)
                                       2
                                           k

                                       (L)
where tk is the target output and ak is the activation of output neuron k. Other
losses change only a few local derivatives (most notably at the output layer), but
the backprop recursion and bookkeeping are the same.
    To update the weights using gradient descent, we need to compute

                                               ∂L
                                                 (l)
                                                       .
                                             ∂wij

Chain rule decomposition             By the chain rule, we have
                                                                 (l+1)
                               ∂L              ∂L              ∂zj
                                 (l)
                                       =       (l+1)
                                                           ·         (l)
                                                                           .   (7.7)
                              ∂wij         ∂zj                 ∂wij




                                               133
Modern Intelligent Systems                                                                                   7


         (l+1)
where zj         is the weighted input to neuron j in layer l + 1:

                                     (l+1)
                                                  X (l) (l)  (l+1)
                                    zj       =     ai wij + bj     .
                                                    i

        (l)                                                                      (l+1)
Here ai is the activation of neuron i in layer l, and bj                                 the bias term.
          (l+1)               (l)
   Since zj     is linear in wij , we have

                                                    (l+1)
                                              ∂zj                  (l)
                                                    (l)
                                                             = ai .
                                                  ∂wij

   Thus,
                                              ∂L             (l+1) (l)
                                             (l)
                                                        = δj      ai ,                                    (7.8)
                                           ∂wij
where we define the error term

                                              (l+1)            ∂L
                                             δj         :=     (l+1)
                                                                             .
                                                             ∂zj

                    (l+1)
Collecting the δj    for all neurons in layer l + 1 forms a vector δ (l+1) with the
                                                   ∂L
same dimension as z (l+1) , ensuring the gradient ∂W  (l) has the same shape as the

weight matrix.

                            (l+1)                         (l+1)
Interpretation of δj                     The term δj               measures how sensitive the error is
                             (l+1)
to changes in the net input aj     . Our task reduces to computing these δ terms
for all neurons in the network.

7.7.1    Output layer error terms
For the output layer L, the activation of neuron k is

                                                  (L)          (L) 
                                              ak        = f zk           ,

where f (·) is the activation function.




                                                         134
Modern Intelligent Systems                                                                              7


   The error term for output neuron k is

                                       (L)            ∂L
                                   δk          =          (L)
                                                                                                     (7.9)
                                                   ∂zk
                                                                    (L)
                                                      ∂L ∂ak
                                               =          (L)       (L)
                                                                                                    (7.10)
                                                   ∂ak          ∂zk
                                                               (L) 
                                               = a k − t k ϕ ′ zk ,
                                                   (L)
                                                                                                    (7.11)

where ϕ′ denotes the derivative of the activation function evaluated element-wise.
For cross-entropy with sigmoid/softmax output, ϕ′ cancels and δk = ak − tk ;
                                                                   (L)    (L)

for MSE retain the factor above.

7.7.2         Hidden layer error terms
                                                                                     (l)
For a hidden neuron j in layer l, the error term δj depends on the error terms
of the neurons in the next layer l + 1 to which it connects. Using the chain rule,

                                         (l)          ∂L
                                       δj =               (l)
                                                                                                    (7.12)
                                                   ∂zj
                                                   X              ∂L
                                                                                (l+1)
                                                                              ∂zk
                                               =                  (l+1)             (l)
                                                                                                    (7.13)
                                                      k    ∂zk                 ∂zj
                                                   X (l+1) ∂z (l+1)
                                                             k
                                               =     δk         (l)
                                                                    .                               (7.14)
                                                   k        ∂z  j

   Since                                           X
                                   (l+1)                                (l)          (l+1)
                                  zk           =           a(l)
                                                            m wmk + bk                          ,
                                                      m
        (l)        (l) 
and aj = ϕ zj              , we have

                                                                                (l) 
                                               (l+1)
                                         ∂zk
                                                          = wjk ϕ′ zj
                                                                  (l)
                                                (l)
                                                                                        .
                                             ∂zj

   Substituting into (7.14) yields

                                                          (l) 
                                                                  X
                                   δ j = ϕ ′ zj
                                       (l)                                    (l) (l+1)
                                                                         wjk δk             .       (7.15)
                                                                   k



                                                            135
Modern Intelligent Systems                                                           7


   For sigmoid activations ϕ, the derivative simplifies to ϕ′ (zj ) = aj (1 − aj );
                                                               (l)     (l)     (l)

other activations require substituting their respective derivatives in (7.15).

Summary: Backpropagation recursion Backpropagation is reverse-mode
automatic differentiation on the network graph. A forward pass caches inter-
mediates; a reverse pass reuses caches to get all gradients in O(P ) time (versus
O(P 2 ) for finite differences) for P parameters. Frameworks (PyTorch/JAX/TF)
automate this; the algebra below is its manual derivation.

7.8   Backpropagation Algorithm: Detailed Derivation
Recall that the goal of backpropagation is to compute the gradient of the loss
with respect to each weight in the network, enabling gradient descent updates.
Consider a single neuron k in the output layer with output ok and activation ak .
The target output is tk .

Error function and its derivatives We use the squared-error loss for a
single output neuron:
                        LSE = 0.5 (tk − ok )2 .                 (7.16)

   Our objective is to compute ∂L
                                ∂wjk , where wjk is the weight from neuron j in
                                  SE


the previous layer to neuron k.
   By the chain rule,

                             ∂LSE   ∂LSE ∂ok ∂ak
                                  =      ·  ·     .                          (7.17)
                             ∂wjk    ∂ok ∂ak ∂wjk

Step 1: Derivative of error with respect to output             From the squared-
error definition above,
                           ∂LSE
                                = o k − tk .                                 (7.18)
                            ∂ok

Step 2: Derivative of output with respect to activation Assuming the
activation function f is the sigmoid,

                                                  1
                              ok = f (ak ) =            ,
                                               1 + e−ak




                                        136
Modern Intelligent Systems                                                           7


its derivative is
                             ∂ok
                                 = f ′ (ak ) = ok (1 − ok ).                 (7.19)
                             ∂ak

Step 3: Derivative of activation with respect to weight The activation
ak is the weighted sum of inputs:
                                          X
                                   ak =        wjk xj .
                                           j


Here xj is the output from neuron j in the previous layer. Thus,

                                      ∂ak
                                           = xj .                            (7.20)
                                      ∂wjk

Putting it all together       Substituting (7.18), (7.19), and (7.20) into (7.17):

                         ∂LSE
                              = (ok − tk ) ok (1 − ok ) xj .                 (7.21)
                         ∂wjk

   Define the error signal for neuron k as

                             δk = (ok − tk ) ok (1 − ok ).                   (7.22)

   Then,
                                    ∂LSE
                                         = δk xj .                           (7.23)
                                    ∂wjk
   The gradient descent update therefore becomes

                                  ∆wjk = −η δk xj ,                          (7.24)

where η is the learning rate.

7.9   Backpropagation for Hidden Layers
For neurons in hidden layers, the error signal δj is computed by propagating
the error backward from the next layer. Consider a hidden neuron j with pre-
activation zj and activation oj = f (zj ). Its error signal is
                                                 X
                             δj = oj (1 − oj )        wjk δk ,               (7.25)
                                                  k


                                          137
Modern Intelligent Systems                                                      7


where the sum is over all neurons k in the next layer to which neuron j connects.
   The weight update for weights wij feeding into neuron j is then

                                ∆wij = −η δj xi ,                           (7.26)

where xi is the output from the previous layer neuron i.

7.10   Batch and Stochastic Gradient Descent
Given a training set of N examples {(x(n) , t(n) )}N
                                                   n=1 , the weight updates can be
computed in different ways:
  • Batch gradient descent: Compute the gradient over the entire dataset
    and update weights once per epoch:

                                      η X (n) (n)
                                             N
                               ∆w = −    δ x .
                                      N
                                             n=1


  • Stochastic gradient descent (SGD): Update weights after each train-
    ing example using the instantaneous gradient −η δ (n) x(n) . Although the
    updates are noisy, SGD often converges faster in practice and can escape
    shallow local minima.
 Optimizer and stability notes
 SGD remains the backbone; momentum and Adam/AdamW from
 Chapter 11 accelerate convergence. Add L2 weight decay to the gradient or
 decouple it (AdamW) to avoid biasing adaptive steps. For deep or
 ill-conditioned nets, gradient clipping can prevent explosions; for
 classification, pair these with cross-entropy and the log-sum-exp stability
 tricks introduced alongside CNNs in Chapter 11. Reverse-mode AD
 underlies all of these updates.




                                       138
Modern Intelligent Systems                                                                          7



                    Forward
                    Backprop (δ)
                    Grads (∇)




                 W (1) , b(1)                        W (L) , b(L)                               t


                             ∇ (1)                              ∇ (L)
                              W                                  W
                             ∇ (1)                              ∇ (L)
                                 b                               b




  x                                    A(1)    ···                            A(L)              L
                     Z (1)             f (·)
                                                        Z (L)                 σ(·)



                         δ (1)                                               Forward cache

            chain rule via W ⊤ , f ′                                 δ (L)               ∂L
                                                                                        ∂A(L)



             Figure 25: Computational graph for a feedforward network.
      Backpropagation is reverse-mode AD: the forward sweep caches intermediate
          values, and the reverse sweep propagates deltas while accumulating
        weight/bias gradients from those cached values. Use it when debugging
              backprop implementations and tracing each gradient term.


 Debugging and gradient-check checklist
      • Overfit a tiny batch: Ensure the loss can be driven near zero on a
        handful of samples.
```

### Findings
1. Equation formatting and punctuation:
   - In the first equation, the partial derivative symbol ∂P/∂p2 is split awkwardly across lines, making it harder to read. Consider keeping the derivative expression on one line or formatting it more clearly.
   - In the sentence "Then ∂P/∂w2 = δ2 y1 and ∂P/∂b2 = δ2 .", there is an extra space before the period after δ2.
   - In the sentence "The first layer receives a backpropa- gated error", the word "backpropagated" is split across lines with a hyphen. This is acceptable in print but should be checked for consistency.
   - In the expression "δ1 := ∂P/∂p1 = δ2 w2 f ′ (p1 ), (6.15)", the spacing around the equal signs and function arguments is inconsistent; consider removing extra spaces inside parentheses for clarity.
   - In the worked example, the expression "P = 12 (y2 − t)2 ≈ 0.059." likely intends "P = 1/2 (y2 − t)^2 ≈ 0.059." or "P = 1/2 (y2 − t)^2 ≈ 0.059." The "12" is ambiguous and should be clarified.
   - In the same example, the notation "σ ′ (p)" has an extra space between σ and the prime symbol; it should be "σ′(p)".
   - In the phrase "gradient descent increases w2 slightly (since the gradient is negative) and nudges w1 in a direction that increases y2 toward the target.", the phrase "increases w2 slightly" is ambiguous because the gradient is negative but the weight is increased; clarify the direction or rephrase for precision.

2. Narrative flow and transitions:
   - The transition from the worked example to section 6.7 ("From two neurons to multi-layer networks") is abrupt. Consider adding a brief sentence summarizing the takeaway from the example before moving on.
   - The "Author’s note: what backprop adds" is helpful but could be better integrated with the preceding paragraph for smoother flow.
   - The summary section (6.8) is well structured but the bullet "The sigmoid derivative σ ′ (p) = σ(p)(1 − σ(p)) is a convenient identity because it reuses the output." could be expanded slightly to explain why reusing the output is convenient.
   - The "Derivation closure" subsection uses bullet points with inconsistent punctuation (some end with periods, others do not). Standardize punctuation for consistency.
   - The "Key takeaways" section uses bullet points with inconsistent capitalization (e.g., "Training is a loop" vs. "Hard thresholds break the gradient story"). Standardize capitalization.
   - The "Common pitfalls" section lists items with inconsistent punctuation and capitalization; for example, "Trying to differentiate through discontinuities (step functions) and then “patching” gradients by hand." ends with a period, but the next item does not.
   - The "Exercises and lab ideas" section is clear but the bullet "Numerical gradient check: Implement finite differences for the two-neuron chain and compare to your analytic gradients; report relative error." is a long sentence and could be split for clarity.
   - The phrase "If you are skipping ahead." is a sentence fragment; consider rephrasing to "If you are skipping ahead, be able to read a forward graph and a backward recursion..."

3. Reader orientation and clarity:
   - The notation section (7.5) is clear but the use of superscripts and subscripts (e.g., (l), (l+1)) is dense; consider adding a small table or diagram summarizing notation for quick reference.
   - The explanation of the error term δj in section 7.7.2 is mathematically correct but could benefit from a brief intuitive explanation of what the sum over k represents.
   - The mini example code snippet is helpful but lacks comments explaining the purpose of some steps (e.g., inverted dropout scaling). Adding brief comments would improve clarity.
   - The "Shape ledger" section uses notation like "A(l−1) ∈ RB×nl−1" without spaces around the set membership symbol ∈; consider adding spaces for readability.
   - The explanation of the backpropagation recursion (7.15) uses the symbol ϕ′ for the derivative of the activation function but earlier sections use f′; standardize notation for activation function derivatives.
   - The "Summary: Backpropagation recursion" paragraph mentions "O(P ) time (versus O(P 2 ) for finite differences)" but does not define P explicitly; clarify that P is the number of parameters.
   - The detailed derivation in section 7.8 uses both ok and ak for activations inconsistently; ensure consistent notation throughout.
   - In equation (7.19), the derivative of the sigmoid is given as ∂ok/∂ak = ok(1 - ok), but earlier the activation was defined as ak = f(zj); clarify the variable naming to avoid confusion.
   - The phrase "Putting it all together" is informal; consider rephrasing to "Combining these results" or similar.
   - The "Optimizer and stability notes" section is dense and could be broken into smaller paragraphs or bullet points for readability.

4. Repetitive templating:
   - The repeated use of phrases like "Consider a neuron...", "The error term is...", and "By the chain rule..." is necessary for clarity but could be varied slightly to improve narrative flow.
   - The phrase "Backpropagation is reverse-mode automatic differentiation" appears multiple times; consider consolidating or cross-referencing to avoid redundancy.

5. Minor typographical issues:
   - In the phrase "Backpropagation is reverse-mode AD: the forward sweep caches intermediate values, and the reverse sweep propagates deltas while accumulating weight/bias gradients from those cached values.", consider adding a comma after "values" for clarity.
   - The figure caption "Figure 25: Computational graph for a feedforward network." is followed by a paragraph that is not clearly separated; consider formatting the caption and description distinctly.
   - The last bullet "Overfit a tiny batch: Ensure the loss can be driven near zero on a handful of samples." ends abruptly; consider expanding or connecting it to subsequent text.

Summary: The chunk is generally well-written and technically accurate but would benefit from improved equation formatting, consistent notation, smoother transitions, standardized punctuation and capitalization in lists, and enhanced reader orientation through clarifications and added comments.

## Chunk 11/31
- Character range: 284272–313258

```text
• Gradient norms: Track k∇W (l) k per layer; look for dead layers (all
        zeros) or explosions.

      • Finite-difference check: Compare analytic gradients to numerical
        finite differences on a tiny network with fixed seeds; relative error
        should be < 10−6 .

      • Shape assertions: Verify that Z (l) , A(l) , δ (l) have the expected
        batch shapes and that bias broadcasts correctly.

      • Layerwise sanity: For a one-layer linear model, backprop gradients
        should match the closed-form linear-regression gradients.




                                               139
Modern Intelligent Systems                                                             7


7.11   Backpropagation Algorithm: Brief Numerical Check
For a quick sanity check, take a tiny 2–2–1 network with sigmoid output and
cross-entropy loss. Using
                            "          #
                              0.5  −0.3
                    W (1) =              , b(1) = [0.1, −0.2],
                              0.8 0.2
                            "      #
                               0.7
                    W (2) =          , b(2) = 0.05,
                              −0.4
                          x = [0.6, −1.2],     t = 1,

the forward pass yields

z (1) = [−0.56, −0.62],    a(1) = [0.3635, 0.3498],     z (2) = 0.1646,   a(2) = 0.5411,

with loss L ≈ 0.6142. The cross-entropy output error is δ (2) = a(2) −t = −0.4590.
Backpropagating gives

 δ (1) = [−0.0743, 0.0418],     ∇W (2) = [−0.1669, −0.1605]⊤ ,      ∇b(2) = −0.4590,

and                 "              #
                   −0.0446 0.0251
          ∇W (1) =                   ,             ∇b(1) = [−0.0743, 0.0418].
                    0.0892 −0.0501
Finite-difference checks on the same network match to numerical precision, val-
idating the implementation.

Aside: squared-error loss (alternative) The remainder of this subsection
sketches the classic squared-error backprop derivation as a separate reminder; it
is not a continuation of the cross-entropy numerical check above.
    The error at the output neuron is:

                                       e = y − t,                                 (7.27)

and the squared error is:
                                           1
                                      LSE = e2 .                                  (7.28)
                                           2


                                             140
Modern Intelligent Systems                                                   7


Backward Propagation of Error Define the error term δj for each neuron
j as:
                         δj = ej σ ′ (netj ),                    (7.29)

where ej is the error at neuron j, and

                              σ ′ (z) = σ(z)(1 − σ(z)).

is the derivative of the sigmoid function.
    For the output neuron:

                         δout = (yout − t) yout (1 − yout ).

   For hidden neurons, the error term is computed by backpropagating the
weighted sum of the downstream error terms:
                                                 X
                             δj = yj (1 − yj )       wkj δk ,            (7.30)
                                                 k

where the sum is over neurons k in the next layer and wkj denotes the weight
from neuron j to neuron k.

Weight Update Rule Weights are updated using gradient descent with mo-
mentum:
                ∆wij (n) = −η δj xi + γ∆wij (n − 1),             (7.31)

where
  • η is the learning rate,

  • γ is the momentum coeﬀicient (typically 0 ≤ γ < 1),

  • ∆wij (n − 1) is the previous weight change,

  • n indexes the update step (e.g., the current training example in stochastic
    gradient descent).
The leading negative sign ensures that the update follows the negative gradient
direction because each δj equals ∂LSE /∂zj .




                                         141
Modern Intelligent Systems                                                     7


   The new weight is then:

                        wij (n) = wij (n − 1) + ∆wij (n).

Interpretation of Learning Rate and Momentum
  • The learning rate η controls the step size in the weight update. A small
    η leads to slow convergence, while a large η can cause oscillations or diver-
    gence.

  • The momentum term γ helps smooth the updates by incorporating a
    fraction of the previous weight change, reducing oscillations and potentially
    accelerating convergence.

Step-by-Step Example
  1. Initialization: Draw weights wij ∼ N (0, σ 2 ) with σ set by He/Xavier
     rules; set biases to zero and ∆wij (0) = 0.

  2. Feedforward: Compute netj and yj for all neurons.

  3. Compute output error: Calculate δout .

  4. Backpropagate error: Compute δj for hidden neurons.

  5. Update weights: Use equation (7.31) to update all weights.

  6. Repeat: Iterate over all training patterns until error E is below threshold
     or maximum epochs reached.




                                      142
Modern Intelligent Systems                                                      7


 Mini-batch backprop with explicit regularization
 Inputs: mini-batch {xb , tb }B
                              b=1 , learning rate η, L2 coeﬀicient λ, dropout
 keep probability q = 1 − p.
 1. Forward pass: propagate activations layer by layer; for each hidden
    layer draw a dropout mask m ∼ Bernoulli(q), apply ã = m a/q, and
    cache m for the backward step.

 2. Backward pass: compute ∇W (ℓ) L using the cached activations/masks
    so that dropped units contribute zero gradient.

 3. Update block (per layer):

                       1
                gℓ =     ∇ (ℓ) L + λW (ℓ) ,   W (ℓ) ← W (ℓ) − η gℓ .
                       B W
    Biases skip the weight-decay term. With Adam/SGD+momentum, gℓ
    replaces the raw gradient inside the optimizer step so L2 regularization
    and dropout are always enforced explicitly.


Remarks
  • Monitor the training error over epochs; a plateau may indicate the need
    to adjust learning rate or introduce regularization.

  • Shuffle training patterns between epochs when using SGD to avoid cyclic
    behaviors.

  • Always track validation error to detect overfitting and decide when to stop
    training.

7.12   Training Procedure and Epochs in Multi-Layer Percep-
       trons
Recall that during training of a multi-layer perceptron (MLP), we iteratively
update the weights based on each training pattern. The process for one epoch
can be summarized as follows:
  1. Present the first input pattern to the network.

  2. Perform a forward pass to compute the output.


                                       143
Modern Intelligent Systems                                                       7


  3. Calculate the error between the actual output and the desired output.

  4. Use backpropagation to compute the gradients and update the weights
     accordingly.

  5. Repeat steps 1–4 for all training patterns.
   After completing one epoch (i.e., one full pass through all training patterns),
we evaluate the overall error. If the error is greater than a predefined tolerance,
we continue training for additional epochs until the error converges below the
threshold or a maximum number of epochs is reached.

Remarks:
  • The weight updates after each pattern are typically small adjustments
    aimed at reducing the error.

  • The initial weights strongly influence the convergence behavior and final
    solution.

  • This iterative process is computationally intensive but essential for learning
    complex mappings.

7.13   Role and Design of Hidden Layers
In an MLP, the architecture consists of an input layer, one or more hidden
layers, and an output layer. The hidden layers are crucial because they enable
the network to learn nonlinear mappings.

Key Questions Regarding Hidden Layers:
  • How many hidden layers should be used? There is no fixed rule; it
    depends on the complexity of the problem.

  • How many neurons per hidden layer? This choice affects the net-
    work’s capacity and generalization ability.

  • What activation functions to use in each layer? Different layers can
    use different activation functions, such as sigmoid, ReLU, or tanh.




                                       144
Modern Intelligent Systems                                                         7


Design Considerations:
  • Number of neurons: More neurons increase the capacity to learn com-
    plex functions but also increase the risk of overfitting and computational
    cost.

  • Number of layers: Deeper networks can represent more complex func-
    tions but are harder to train.

  • Activation functions: Choice affects gradient flow and convergence.
   Ultimately, these design choices are made by the practitioner based on ex-
perimentation, domain knowledge, and validation performance.

Trade-offs:
  • Too many neurons/layers: Requires more training data to avoid over-
    fitting; increases computational burden.

  • Too few neurons/layers: Limits the network’s ability to approximate
    complex functions.

7.14     Case Study: Learning the Function y = x sin x
Consider the problem of training an MLP to approximate the function

                                   y = x sin x.

Setup:
  • Generate a dataset of input-output pairs {(xi , yi )} where yi = xi sin xi .

  • Use this dataset to train an MLP regressor.

  • Evaluate the network’s ability to generalize by testing on inputs not seen
    during training.

Questions to Explore:
  • How many hidden layers and neurons per layer are needed to approximate
    this nonlinear function well?

  • What activation functions yield better performance?


                                       145
Modern Intelligent Systems                                                    7


  • How does the size of the training set affect generalization?

Remarks:
  • This is a regression problem, not a classification problem.

  • The function is nonlinear and periodic, which challenges the network’s
    approximation capabilities.

  • Experimentation with different architectures and hyperparameters is es-
    sential.
    As a representative example (illustrative; depends on initialization and the
training recipe), a two-hidden-layer MLP with widths [64, 32], ReLU activations,
Adam optimization, and early stopping on a validation split can achieve mean
absolute error on the order of 10−3 on held-out samples when trained on 2,000
uniformly spaced points in [−3π, 3π].

7.15   Applications of Multi-Layer Perceptrons
Multi-layer perceptrons have found widespread applications across various do-
mains due to their ability to approximate complex nonlinear functions. Some
notable applications include:
  • Signal processing: Noise reduction, filtering, and feature extraction.

  • Weather forecasting: Modeling complex atmospheric patterns.

  • Data compression: Dimensionality reduction and encoding.

  • Pattern recognition: Handwriting recognition, face detection.

  • Financial market prediction: Time series forecasting and anomaly de-
    tection.

  • Image recognition: Object detection and classification.

  • Voice recognition: Speech-to-text and speaker identification.

Summary: MLPs are versatile and powerful tools that serve as foundational
building blocks in many machine learning systems.




                                      146
Modern Intelligent Systems                                                       7


7.16   Limitations of Multi-Layer Perceptrons
Despite their versatility, MLPs have several limitations that practitioners must
be aware of:
  • Convergence to local minima: Due to the non-convex nature of the
    loss surface, training may converge to different local minima depending on
    the initial weights.

  • Sensitivity to initialization: Different random initializations can lead
    to significantly different outcomes.

  • Hyperparameter tuning: Learning rates, momentum, and regulariza-
    tion require careful tuning for stable convergence.

7.17   Conclusion of Multi-Layer Perceptron Derivations
In this final segment of the chapter, we complete the derivations and discus-
sions related to the multi-layer perceptron (MLP) and its learning algorithm,
backpropagation.
    Recall that the MLP consists of multiple layers of neurons, each performing
an aﬀine transformation followed by a nonlinear activation. The key to training
the MLP is to minimize a loss L defined over outputs and targets.

Backpropagation Algorithm Recap The backpropagation algorithm eﬀi-
ciently computes the gradient of the loss function with respect to all network
parameters by applying the chain rule of calculus through the network layers.
For a network with L layers, denote by:

                Z (l) = A(l−1) W (l) + 1(b(l) )⊤ ,       A(l) = ϕ(l) (Z (l) ),

where W (l) and b(l) are the weights and biases of layer l, A(l−1) is the previous
layer activation (rows are samples), and ϕ(l) is the activation function.
    The error term at layer l is defined as:

                                               ∂L
                                    δ (l) =          .
                                              ∂Z (l)




                                          147
Modern Intelligent Systems                                                            7


   Using the chain rule, the error terms propagate backward as:

               δ (L) = ∇A(L) L ϕ(L)′ (Z (L) ),                                    (7.32)
                                     
            δ (l−1) = δ (l) (W (l) )⊤   ϕ(l−1)′ (Z (l−1) ),   l = L, . . . , 2,   (7.33)

where     denotes element-wise multiplication and ϕ(l)′ is the derivative of the
activation function at layer l.
    The gradients of the loss with respect to the parameters are then:

                                ∂L
                                      = (A(l−1) )⊤ δ (l) ,                        (7.34)
                               ∂W (l)
                                 ∂L
                                      = 1⊤ δ (l) .                                (7.35)
                                ∂b(l)
    These gradients are used in gradient-based optimization methods (e.g.,
stochastic gradient descent) to update the parameters and minimize the loss.
Figure 26 complements the algebra by showing how cached activations (blue)
line up with the backward error signals (orange) in a simple two-layer network.

                                                                    δ (2)
                   forward
                   backward    (1)                     (2)
                              w11                     w1
                   x1                     (1)
                                         a1                    a(2)
                               w (1)
                                21
                                     )          (1)
                                 (1           δ1       (2)
                                w 12                  w2
                   x2                     (1)
                               (1)
                                         a2
                              w22

                                                (1)
                                              δ2


    Figure 26: Forward (blue) and backward (orange) flows for a two-layer MLP.
     Cached activations and layerwise deltas travel along these arrows; backward
        signals use next-layer weights and activation derivatives. Use it when
     implementing backprop to confirm what to cache and where gradients flow.



Example Execution An example was provided illustrating the forward pass
computation of activations and the backward pass calculation of gradients for a
simple MLP with one hidden layer. This example concretely demonstrated how

                                          148
Modern Intelligent Systems                                                         7


the chain rule is applied layer-by-layer and how the error signals are propagated
backward.

Remarks on Convergence and Practical Considerations While the
backpropagation algorithm provides the exact gradients for the MLP, practical
training involves additional considerations such as:
  • Initialization of weights to avoid vanishing or exploding gradients.

  • Choice of activation functions (e.g., ReLU, sigmoid, tanh) affecting gradi-
    ent flow.

  • Regularization techniques (dropout, weight decay) to prevent overfitting.

  • Optimization algorithms (momentum, Adam) to accelerate convergence.
   These topics will be explored in subsequent chapters; for now, we compare
the canonical activation choices in one place.

Comparing canonical nonlinearities With the full MLP and backpropaga-
tion machinery in place, it is useful to compare the most common nonlinearities
side-by-side. Figure 27 overlays the step, sigmoid, tanh, and ReLU curves so
the saturation regions and derivative behavior are visually apparent before we
move on to deeper architectures.
                                         
    For reference, σ ′ (z) = σ(z) 1−σ(z) , tanh′ (z) = 1−tanh2 (z), and the ReLU
derivative is 0 for negative inputs and 1 for positive inputs (take 0 at the origin).

Trade-offs While some activation functions are inspired by biological neurons,
others are chosen for mathematical convenience and training eﬀiciency. Sigmoid
and tanh saturate at large magnitude inputs, which slows gradients in deep net-
works. ReLU avoids saturation on the positive side but can produce “dying Re-
LUs” when biases push units negative and the gradients become zero; if many
units stall, use He initialization, reduce the learning rate, or swap to a leaky
ReLU with a small negative slope (e.g., 0.01). This closes the core backpropaga-
tion story for MLPs. Next we summarize practical stability considerations and
the key takeaways that guide real training.




                                        149
Modern Intelligent Systems                                                          7




                      Step                               Sigmoid

                      1                                   1


                                                         0.5



              −2                 2            −4    −2             2       4
                      tanh                                ReLU
                      1                                   2


                                                          1
              −2                 2

                    −1
                                                   −2                  2


     Figure 27: Canonical activation functions on a common axis. Solid curves
    show the activation; dashed curves show its derivative. Use it when choosing
      an activation and checking whether its derivative will saturate or die out.




                                        150
Modern Intelligent Systems                                                     7


 Key takeaways
 Minimum viable mastery
    • MLP training relies on stable optimization: proper initialization,
      learning-rate schedules, and normalization help.

    • Regularization (weight decay, dropout) reduces overfitting; validation
      curves guide early stopping.

    • Despite power, MLPs remain sensitive to hyperparameters, so
      debugging and audits matter.

 Common pitfalls
    • Silent shape mistakes: mismatched dimensions can yield plausible but
      wrong gradients.

    • Learning-rate pathologies: too large diverges, too small stalls;
      diagnose with train/val curves.

    • Overfitting by optimization: improving training loss without
      validation gains is a signal to stop or regularize.

 Practical early stopping and checkpointing
    • Maintain a validation split distinct from the training mini-batches.
                                                     (e)
      After each epoch, record the validation loss Lval .

    • Stop training when Lval has not improved for k consecutive epochs
      (typical patience k ∈ [5, 10]). Optionally require a minimum relative
      improvement (e.g., 0.1%) to smooth noise.

    • Always checkpoint the parameters that achieved the best validation
      score and restore them before testing; averaging the last m
      checkpoints (“Polyak averaging”) can further stabilize performance.




                                     151
Modern Intelligent Systems                                                          8


 Derivation closure: implement, cache, fail-fast
    • Implement: encode one canonical forward signature
      (A(l−1) , W (l) , b(l) ) 7→ (Z (l) , A(l) ), then reuse it for every layer.

    • Cache: store (A(l−1) , Z (l) ) per layer so backward passes only apply
      local Jacobians and matrix multiplications.

    • Fail-fast checks: do a numerical gradient check on one mini-batch,
      then verify gradient norms and validation curves before long runs.

    • Reproducibility: log seed, optimizer, schedule, and stopping rule
      with each run; the reporting template in Appendix E keeps
      comparisons fair.

 Exercises and lab ideas
    • Implement a minimal example from this chapter and visualize
      intermediate quantities (plots or diagnostics) to match the
      pseudocode.

    • Stress-test a key hyperparameter or design choice discussed here and
      report the effect on validation performance or stability.

    • Re-derive one core equation or update rule by hand and check it
      numerically against your implementation.

If you are skipping ahead. Keep one practical habit: do a gradient check on a
tiny case before scaling up. That discipline mirrors residual checks in Chapter 2
and prevents most wasted training runs in later deep chapters.


Where we head next. Chapter 8 introduces radial basis function networks,
an alternative nonlinear route where hidden features are mostly fixed and only
the output layer is solved linearly. This provides a clean contrast to end-to-end
backpropagation.


8 Radial Basis Function Networks (RBFNs)
Building on the multilayer perceptron (MLP) architecture (Chapter 6) and its
training machinery (Chapter 7), we now introduce radial basis function networks

                                            152
Modern Intelligent Systems                                                     8


(RBFNs): three-layer models with fixed nonlinear bases and a linear readout.
Figure 1 places this as the kernel/prototype branch alongside the MLP path.
  Learning Outcomes
      • Explain the architecture and training stages of RBF networks (center
        selection, width tuning, linear solve).

      • Relate RBF solutions to linear estimators (normal equations,
        pseudoinverse, Wiener filtering) and know when ridge regularization
        is needed.

      • Compare RBFNs to kernelized methods and other nonlinear
        classifiers to choose appropriate models in practice.

  Design motif
  Make the nonlinearity explicit: use a fixed (or lightly tuned) basis
  expansion in the hidden layer, then learn the output weights with
  linear-algebra tools.


8.1    Overview and Motivation
How to read this chapter.
  • Core thread (RBFNs): architecture → basis functions and widths →
    linear solve (least squares / ridge) → kernel view and practical tuning.

  • Optional bridge: a short Wiener-filter refresher connects the RBFN
    linear solve to classical linear estimation; it is provided for context and
    can be skimmed without loss of continuity.
   Unlike MLPs, which learn weights in every layer, an RBFN fixes the hidden
nonlinearity and learns only the output weights. Concretely:
  • It has exactly three layers: an input layer, a single hidden layer, and an
    output layer.

  • The input layer simply forwards the raw feature vector to every hidden unit;
    there are no trainable weights on these connections because the hidden
    units encode their own parameters (centers and widths).



                                      153
Modern Intelligent Systems                                                        8


   • The hidden layer applies a nonlinear transformation to the input vector
     via a set of radial basis functions.

   • The output layer is a linear combination of the hidden layer outputs, with
     trainable weights.
    The RBFN was originally developed as a method to model nonlinear static
processes by mapping data from a lower-dimensional input space to a higher-
dimensional feature space. The key idea is that data which are not linearly
separable in the original input space can become linearly separable after a suitable
nonlinear transformation into a higher-dimensional space. This concept is closely
related to the kernel trick used in support vector machines (SVMs); Appendix B
collects the classical kernel/SVM viewpoint in one place.
    Chapter 3 frames this as a bias–variance tuning problem (choose capacity,
regularization, and diagnostics via learning curves). Kernel methods such as
kernel ridge regression and SVMs interpret the same trade-off through an RBF
kernel matrix; here we keep the bases explicit, then connect to the dual/kernel
view later in the chapter.

Author’s note: centers come from clustering. The hidden layer of an
RBF network is easiest to understand when its centers are viewed as K-means
prototypes: pick a coverage of the input space that reflects the data distribution,
assign widths accordingly, and let the output layer learn the linear weights on top
of those prototypes. Unsupervised clustering up front makes the later supervised
solve far more stable.

8.2   Architecture of RBFNs
The RBFN consists of three layers:
  Notation and shapes
 We denote each basis response by φi (x); stacking them yields G(x) ∈ RM
 with entries Gi (x) = φi (x). For a dataset of N samples, the corresponding
 design matrix Φ ∈ RN ×M stacks one transformed sample per row, with
 entries Φji = φi (xj ) = Gi (xj ). This matches the design-matrix convention
 used in Chapter 3.




                                       154
Modern Intelligent Systems                                                              8


                       Centers/widths
                       (µi , σi ) set by
                       k-means or heuristics


           x1                     φ1
                                                w1


                                               w2             Linear weights wi
           x2                     φ2                   ŷ     learned from data



            ..               ..
             .                .                 wM   bias b


           xd                     φM

    Figure 28: RBFN architecture. Inputs feed fixed radial units parameterized
     by centers and widths; a linear readout with weights and bias is trained by a
    regression or classification loss. Only the output weights are typically learned,
      while centers/widths come from k-means or spacing heuristics. Use it when
      separating representation design (centers/widths) from supervised readout
                                         training.


    Figure 28 highlights the split between fixed radial features and a trained
linear readout.

A picture to keep in mind Once you have the architecture in mind, it helps
to visualize what the hidden layer does. In one dimension, you can literally draw
the bases as overlapping Gaussian bumps; the model output is a weighted sum
of those bumps. Figure 29 is the mental model we will reuse as we introduce
centers, widths, and the final linear solve.
    Figure 30 compares center-placement strategies used during initialization.
    Figure 32 clarifies primal-versus-dual trade-offs as basis count grows and
Nyström approximations become attractive.
  1. Input layer: Receives the input vector x ∈ Rn .

  2. Hidden layer: Applies a set of M nonlinear radial basis functions
     {Gi (x)}M
             i=1 to the input. These functions serve as feature mappings.

  3. Output layer: Computes a weighted sum of the hidden layer outputs to

                                               155
Modern Intelligent Systems                                                          8


                                         ϕ1
                Activation    1          ϕ2
                                         ϕ3
                                     ∑
                             0.5       j j ϕj (x)
                                        w


                              0

                               −4   −3    −2        −1     0   1   2   3   4
                                                           x

    Figure 29: Localized Gaussian basis functions (dashed) and their weighted
    sum (solid). Overlapping bumps allow RBF networks to interpolate complex
      signals smoothly. Use it when building intuition for locality and smooth
                       interpolation in basis-function models.
```

### Findings
Issues found:

1. In the bullet list at the very beginning, the notation "k∇W (l) k" is unclear and inconsistent with standard norm notation. It should be clarified or corrected to something like "∥∇W^(l)∥" or "||∇W^(l)||" for gradient norms.

2. In the finite-difference check bullet, the relative error threshold is written as "< 10−6" with a minus sign that may be a Unicode minus rather than a hyphen-minus. Consistency in notation for exponents should be ensured.

3. The notation in the line "δ (2) = a(2) −t = −0.4590" is missing a space after the minus sign in "−t". It should be "− t" for clarity.

4. In the weight update rule equation (7.31), the notation "∆wij (n) = −η δj xi + γ∆wij (n − 1)" lacks parentheses around the terms after the learning rate and momentum coefficients, which could cause ambiguity. It would be clearer as "∆w_ij(n) = −η δ_j x_i + γ ∆w_ij(n−1)" or with parentheses to clarify order of operations.

5. In the "Mini-batch backprop with explicit regularization" section, the notation "gℓ = 1/B ∇ (ℓ) L + λW (ℓ)" is ambiguous. It should be "g_ℓ = (1/B) ∇_{W^(ℓ)} L + λ W^(ℓ)" or similar to clarify the gradient is with respect to W^(ℓ).

6. The phrase "Biases skip the weight-decay term" is a bit informal; consider rephrasing to "Bias terms are exempt from weight decay."

7. In section 7.12, the phrase "Recall that during training of a multi-layer perceptron (MLP), we iteratively update the weights based on each training pattern." could be improved by specifying that this is stochastic or mini-batch gradient descent to orient the reader.

8. In section 7.13, the bullet "How many neurons per hidden layer? This choice affects the net- work’s capacity and generalization ability." has a hyphenated line break in "net- work’s" which should be fixed.

9. In section 7.14, the bullet "Experimentation with different architectures and hyperparameters is es- sential." has a hyphenated line break in "es- sential" which should be fixed.

10. In section 7.17, the notation "δ (l) = ∂L / ∂Z (l)" is presented without clear formatting; it would be clearer as "δ^(l) = ∂L / ∂Z^(l)" or with proper sub/superscripts.

11. In the equations (7.32) and (7.33), the notation "δ (L) = ∇A(L) L ϕ(L)′ (Z (L) )" is ambiguous and missing multiplication symbols; it should be "δ^(L) = ∇_{A^(L)} L × ϕ'^(L)(Z^(L))" or similar.

12. The phrase "where     denotes element-wise multiplication" is missing the symbol that denotes element-wise multiplication (usually "⊙" or "∘"). This should be included for clarity.

13. In the figure captions and references (e.g., Figure 26, Figure 27), the text includes some formatting artifacts like "              " and inconsistent spacing that should be cleaned.

14. The phrase "Use it when choosing an activation and checking whether its derivative will saturate or die out." in Figure 27 caption is informal; consider rephrasing to "Refer to this figure when selecting activation functions and assessing their derivative behavior, particularly saturation and dying units."

15. In the "Key takeaways" section, the bullet "Silent shape mistakes: mismatched dimensions can yield plausible but wrong gradients." could be clearer by specifying "Silent shape mistakes: mismatched tensor dimensions can produce plausible but incorrect gradients."

16. The phrase "Maintain a validation split distinct from the training mini-batches." could be clearer as "Maintain a validation set distinct from the training mini-batches."

17. The phrase "After each epoch, record the validation loss Lval ." has an extra space before the period.

18. The phrase "Stop training when Lval has not improved for k consecutive epochs (typical patience k ∈ [5, 10]). Optionally require a minimum relative improvement (e.g., 0.1%) to smooth noise." could be split into two sentences for clarity.

19. The phrase "Always checkpoint the parameters that achieved the best validation score and restore them before testing; averaging the last m checkpoints (“Polyak averaging”) can further stabilize performance." is a long sentence; consider splitting for readability.

20. In the "Derivation closure" section, the phrase "encode one canonical forward signature (A(l−1) , W (l) , b(l) ) 7→ (Z (l) , A(l) ), then reuse it for every layer." uses "7→" which may be unfamiliar; consider replacing with "→" or "maps to" for clarity.

21. The phrase "Reproducibility: log seed, optimizer, schedule, and stopping rule with each run; the reporting template in Appendix E keeps comparisons fair." is a run-on sentence; consider splitting.

22. The phrase "If you are skipping ahead. Keep one practical habit: do a gradient check on a tiny case before scaling up." is a sentence fragment; consider combining into one sentence.

23. In the start of Chapter 8, the phrase "Building on the multilayer perceptron (MLP) architecture (Chapter 6) and its training machinery (Chapter 7), we now introduce radial basis function networks (RBFNs): three-layer models with fixed nonlinear bases and a linear readout." is a long sentence; consider splitting for readability.

24. The phrase "Figure 1 places this as the kernel/prototype branch alongside the MLP path." references Figure 1, but this is Chapter 8; ensure figure numbering is consistent or clarify.

25. The phrase "Learning Outcomes" is capitalized inconsistently compared to other section headings.

26. The phrase "Make the nonlinearity explicit: use a fixed (or lightly tuned) basis expansion in the hidden layer, then learn the output weights with linear-algebra tools." is a fragment; consider rephrasing as a complete sentence.

27. The phrase "Unlike MLPs, which learn weights in every layer, an RBFN fixes the hidden nonlinearity and learns only the output weights." is clear but could be improved by adding a brief explanation of the benefit.

28. The phrase "The hidden layer applies a nonlinear transformation to the input vector via a set of radial basis functions." could specify the typical choice of radial basis functions (e.g., Gaussian).

29. The phrase "The RBFN was originally developed as a method to model nonlinear static processes by mapping data from a lower-dimensional input space to a higher-dimensional feature space." is a long sentence; consider splitting.

30. The phrase "Author’s note: centers come from clustering." is informal; consider rephrasing as "Note: centers are typically obtained via clustering methods such as K-means."

31. In the description of notation, "We denote each basis response by φi (x); stacking them yields G(x) ∈ RM with entries Gi (x) = φi (x)." the use of G and φ is potentially confusing; clarify the relationship or choose consistent notation.

32. In Figure 28 caption, the phrase "Use it when separating representation design (centers/widths) from supervised readout training." is informal; consider rephrasing to "Refer to this figure to understand the separation between representation design (centers and widths) and supervised readout training."

33. In Figure 29 caption, the phrase "Use it when building intuition for locality and smooth interpolation in basis-function models." is informal; consider rephrasing to "This figure aids intuition for locality and smooth interpolation in basis-function models."

34. Throughout, there are inconsistent uses of spaces before and after parentheses and commas, e.g., "W (l)" vs "W^(l)"; standardize notation spacing.

No other issues spotted.

## Chunk 12/31
- Character range: 313266–340507

```text
produce the final output vector y ∈ RK .
    The key distinction is that the input-to-hidden layer connections do not have
trainable weights; instead, the hidden layer units themselves perform nonlinear
transformations of the input.

8.2.1    Mathematical Formulation
Let the input vector be x ∈ Rn . The hidden layer computes the vector
                                                     
                                               G1 (x)
                                                     
                                              G2 (x) 
                                             
                                      G(x) =  .     ∈R .
                                                         M
                                              .. 
                                               GM (x)

where each Gi (x) is a radial basis function centered at some point ci ∈ Rn ; stack-
ing all M responses into G(x) makes it clear that M controls the dimensionality
of the transformed feature space.
    The output layer then computes

                                         y(x) = W⊤ G(x) + b,                     (8.1)

where W ∈ RM ×K is the weight matrix connecting the hidden layer to the
output layer, and b ∈ RK is a bias vector.




                                                     156
Modern Intelligent Systems                                                            8



                       (a) K-means centers




                       (b) Random centers




      Figure 30: Center placement and overlap. Top: K-means prototypes roughly
      tile the data manifold, giving even overlap; bottom: random centers can leave
             gaps or excessive overlap, influencing the width (sigma) choice and
        conditioning. Use it when choosing how to place centers before tuning the
                                      width parameter.


Interpretation: The hidden layer maps the input x into a new feature space
via nonlinear functions Gi , and the output layer performs a linear combination
of these features to produce the final output.

8.3     Radial Basis Functions
The functions Gi (x) are typically chosen to be radially symmetric functions
centered at ci , such as Gaussian functions:
                                                             
                                                   kx − ci k2
                    Gi (x) = φ (kx − ci k) = exp −              ,                 (8.2)
                                                      2σi2

where σi is the width (spread) parameter controlling the receptive field of the
i-th basis function.
    Other choices of radial basis functions are possible, but the Gaussian is the
most common due to its smoothness and locality properties.




                                             157
Modern Intelligent Systems                                                    8


Normalized RBFs. Some texts normalize the hidden responses as G̃i (x) =
       P
Gi (x)/ j Gj (x) to smooth predictions when center density is uneven; the linear
readout then uses G̃(x) in place of G(x).

8.4   Key Properties and Advantages
  • Nonlinear transformation without weights: The input-to-hidden
    layer mapping is fixed by the choice of centers {ci } and widths {σi }, not
    by trainable weights.

  • Linear output layer: Training reduces to finding the optimal weights
    W in a linear model, which can be done eﬀiciently using linear regression
    techniques.

  • Universal approximation: With suﬀiciently many radial basis functions
    placed densely over a compact domain (and with nondegenerate widths),
    RBFNs can approximate any continuous function to arbitrary accuracy
    (Park and Sandberg, 1991; Micchelli, 1986).

  • Interpretability: Each hidden unit corresponds to a localized region in
    input space, making it easier to understand which prototypes influence a
    given prediction.

Curse of dimensionality. In high dimensions Euclidean distances concen-
trate, so widths and center counts must scale with dimension; kernel ridge re-
gression or learned features (e.g., CNNs) often dominate for images/audio.

8.5   Transforming Nonlinearly Separable Data into Linearly Sep-
      arable Space
Recall from the previous discussion that certain datasets are not linearly sep-
arable in their original input space. However, by applying nonlinear transfor-
mations, we can map the data into a new feature space where linear separation
becomes possible.
   Consider a nonlinear transformation function g(·) applied to the input vector
x ∈ Rn , producing a transformed vector g(x) ∈ Rm . The goal is to find a weight
vector w ∈ Rm such that the linear combination w⊤ g(x) separates the classes.




                                      158
Modern Intelligent Systems                                                        8


Example Setup: - Input vectors: x ∈ {0, 1}2 (e.g., (0, 0), (0, 1), (1, 0), (1, 1)) -
Two neurons in the hidden layer, each associated with weight vectors v1 and v2 .
- Activation functions g1 (x) and g2 (x) correspond to these neurons. - Output is
a linear combination of these activations:

                       y = w⊤ g(x) = w1 g1 (x) + w2 g2 (x).

Assumptions: - For simplicity, set σ 2 = 1 (so 2σ 2 = 2) in the Gaussian kernel
activation function. - Assume v1 = (0, 0)⊤ and v2 = (1, 1)⊤ . - The activation
function is Gaussian radial basis function (RBF):
                                                        
                                            kx − vi k2
                             gi (x) = exp −                  .
                                               2σ 2

Transformation Results: Applying the transformation to the inputs yields
new points in the g1 -g2 space. For example, the input x = (0, 0) maps to
(g1 , g2 ) = (1, e−1 ), and x = (1, 1) maps to (e−1 , 1). This transformation often
results in the classes becoming linearly separable in the g1 –g2 plane; plotting
the four transformed points reveals that samples from different classes occupy
opposite corners of the square, allowing a single linear decision boundary to
separate them.

8.6   Finding the Optimal Weight Vector w
Given the transformed data g(x) and desired outputs d, we want to find w that
minimizes the squared error between the predicted output and the target. Let
Φ ∈ RN ×M be the design matrix with entries Φji = φi (xj ) = Gi (xj ). The model
predicts d̂ = Φw, and the least-squares objective is

                                 J(w) = kd − Φwk2 .                           (8.3)

Normal Equations for the Weights: Differentiating (8.3) with respect to
w and setting the gradient to zero yields

                                   Φ⊤ Φ w = Φ⊤ d.                             (8.4)




                                         159
Modern Intelligent Systems                                                      8


When Φ⊤ Φ is well conditioned, the closed-form solution is w⋆ = (Φ⊤ Φ)−1 Φ⊤ d;
in practice we almost always add ridge regularization as described in the training
section below.

Conditioning and capacity. When M is large and Gaussians overlap heavily,
Φ⊤ Φ can become ill-conditioned. Ridge regularization (adding λI) stabilizes the
solve and controls variance, mirroring the bias–variance trade-off from Chapter 3.
Choosing M , σ, and λ together is essential for good generalization; Chapter 3’s
learning-curve diagnostics apply directly, and kernel methods (e.g., kernel ridge
regression or SVMs) interpret the same trade-off via RBF kernels.

8.7   The Role of the Transformation Function g(·)
The design matrix Φ is constructed by applying a nonlinear transformation g(·)
to the input data points relative to a set of centroids {vi }. Each element of Φ
is typically defined as:

                             Φji = gi (xj ) = g (kxj − vi k) .

where k · k denotes a norm (usually Euclidean distance), and g(·) is a nonlinear
kernel or activation function.
   Two parameters characterize g(·):
  • vi : the centroid or center of the i-th basis function.

  • σi : the width or spread parameter controlling the receptive field of the
    basis function.

Choosing g(·): The choice of g(·) is crucial. It defines how the input space is
mapped into the feature space where linear separation is possible. A common
rule-of-thumb for Gaussian widths is to set σ so that neighboring centers at
                                                        
average spacing r̄ overlap with height exp −r̄2 /(2σ 2 ) ≈ 0.5–0.7; too small σ
fragments the boundary, too large washes out locality.

8.8   Examples of Kernel Functions
1. Inverse Distance Function:
                                           1
                                 g(r) =       ,    ϵ > 0,
                                          r+ϵ

                                           160
Modern Intelligent Systems                                                      8


where r = kx − vk. This function decreases as the distance increases but can
become unbounded near zero, potentially causing numerical instability.

2. Gaussian Radial Basis Function:
                                       
                                     r2
                        g(r) = exp − 2 .
                                    2σ

This function is smooth, bounded, and has a clear interpretation as a localized
receptive field centered at v with width σ. It is the most commonly used kernel
in RBF networks.
  Author’s note: why “radial” and why a Gaussian?
 An RBF unit is called radial because its response depends primarily on
 distance from a center: points at the same radius (in the chosen metric)
 produce the same activation. The Gaussian basis is popular because it is
 smooth, has a clear center, and its width parameter σ directly controls
 locality: large σ makes each unit “see” broadly (risking underfit), while
 small σ makes units highly local (risking overfit and poor conditioning).
 The practical art is to pick centers that cover the data and then tune σ
 (and ridge λ) by validation, as in Figure 31.


8.9   Interpretation of the Width Parameter σ
The parameter σ controls the spread of the basis function. Conceptually, in-
creasing σ broadens the Gaussian bell, while decreasing σ produces a narrow
spike around the centroid.
  • σ = 1: The function is broad, covering a large region of the input space.

  • σ = 0.3: The function is narrow and sharply peaked around the centroid.
   Choosing σ appropriately is critical for the network’s performance:
  • If σ is too large, the basis functions overlap excessively, leading to smooth
    but potentially underfitting models.

  • If σ is too small, the basis functions become too localized, which may cause
    overfitting and poor generalization.



                                      161
Modern Intelligent Systems                                                         8


                                σ sweep (two-moons)



           underfit (large σ)         just right          overfit (small σ)




    Figure 31: How the width parameter (sigma) influences decision boundaries
    on a 2D toy dataset. Too-large sigma underfits, intermediate sigma captures
     the boundary, too-small sigma overfits with fragmented regions. Validation
     curves in Chapter 3 guide model size and regularization; they also motivate
            tuning sigma to balance smoothness against boundary fidelity.


8.10   Effect of σ on Classification Boundaries
Consider a one-dimensional dataset with two classes (e.g., red and blue points).
Projecting a sample x through the Gaussian basis functions produces feature
activations                                       
                                        (x − vi )2
                        φi (x) = exp −               ,
                                           2σ 2
which serve as localized similarity measures to each centroid vi . When σ is
large, many points activate the same basis functions with comparable strength,
leading to smooth decision boundaries after the linear output layer. When σ
is small, only points very close to a centroid elicit large activations, yielding
sharply varying boundaries that can overfit noise. Visualizing φi (x) for several
centroids illustrates how tuning σ controls the flexibility of the classifier.
    Figure 33 shows how the RBF model bends the boundary on the XOR-style
toy example.

Notation note. In this chapter we write radial basis functions as φi (·) and use
Φ for the associated design matrix. When we need a generic kernel feature map,
we use ϕ(·) (consistent with Appendix B); when probability density functions
are needed, we write them as p(·). This avoids overloading a single symbol.




                                        162
Modern Intelligent Systems                                                      8


8.11   Radial Basis Function Networks: Parameter Estimation
       and Training
Recall that in Radial Basis Function (RBF) networks, the hidden layer neurons
compute outputs based on radial basis functions centered at certain points vi
with spread parameters σi . The output is a linear combination of these nonlinear
transformations. The key challenge is to determine the parameters:

                                 {vi , σi , wi }M
                                                i=1 ,


where M is the number of hidden neurons.

Finding the Centers vi : A natural approach to find the centers is to use
clustering algorithms on the input data. For example, if we decide to have
M hidden neurons, we run a clustering algorithm (e.g., K-means) to find M
centroids:
                               v1 , v2 , . . . , vM .

These centroids represent typical data points around which the radial basis func-
tions are centered. This approach ensures that the radial basis functions cover
the input space effectively.

Determining the Spread Parameters σi : The spread parameters control
the width of each radial basis function. One can initialize all σi to a common
value or assign different values based on the data distribution. A practical rule-
of-thumb is
                                        dmax
                                    σ≈√       ,
                                          2M
where dmax is the maximum pairwise distance between centers and M the num-
ber of RBF units; this ensures neighboring receptive fields overlap without col-
lapsing to a constant function. After setting this global width, refine to per-
center widths by setting each σi proportional to the average distance between
the centroid vi and its nearest neighboring centroids. Anisotropic variants scale
each dimension separately but follow the same principle of matching the local
density of prototypes.




                                        163
Modern Intelligent Systems                                                      8


Training the Output Weights wi : Given fixed centers and spreads, the
output weights wi can be found by minimizing the squared error between the
network output and the target values. The network output for an input x is:

                                           X
                                           M
                                 ŷ(x) =         wi φi (x).
                                           i=1

where                                                        
                                            kx − vi k2
                             φi (x) = exp −                       .
                                               2σi2
   The training problem reduces to solving the linear system:

                                   min ky − Φwk2 ,                           (8.5)
                                    w

where y is the vector of target outputs and Φ is the design matrix with entries
Φji = φi (xj ). When Φ⊤ Φ is well-conditioned, the ordinary least-squares solution
is
                              w⋆ = (Φ⊤ Φ)−1 Φ⊤ y.




                                           164
Modern Intelligent Systems                                                      8


 Dual viewpoint: RBFN vs. kernel ridge regression
 Fixing the RBF centers and widths makes the hidden layer a finite basis
 expansion. Training restricts itself to the M coeﬀicients w and resembles
 kernel ridge regression with a truncated basis. In the dual view, kernel
 ridge regression solves

                             min ky − Kαk2 + λα⊤ Kα,
                              α

 where Kij = k(xi , xj ) uses the same Gaussian kernel. Setting M = N and
 letting the RBF centers coincide with the training points recovers this dual
 form exactly. Finite M acts like Nyström approximation: Φw projects onto
 a subset of kernel features.
 Numerically, Φ⊤ Φ can be ill-conditioned if the bases overlap excessively or
 if centers cluster tightly; kernel ridge has the same issue via K.
 Regularization is therefore essential: add λI before inversion,

                             w⋆ = (Φ⊤ Φ + λI)−1 Φ⊤ y,

 mirroring the λα⊤ Kα term in the dual problem. Larger λ damps
 coeﬀicients when σ is large (heavy overlap) or when data are noisy, while
 smaller λ preserves sharper fits at the cost of conditioning. Choosing λ via
 cross-validation keeps both primal (RBFN) and dual (kernel ridge) systems
 stable.

    To improve numerical stability or control model complexity, a Tikhonov
(ridge) regulariser can be added,

                      wλ⋆ = (Φ⊤ Φ + λI)−1 Φ⊤ y,       λ > 0,

or more generally one can use the Moore–Penrose pseudoinverse Φ+ when Φ⊤ Φ
is singular, yielding w⋆ = Φ+ y. A quick dimensional sanity check is that Φ ∈
RN ×M , w ∈ RM , and y ∈ RN ; all matrix products above respect these shapes.

Iterative Optimization of σi and wi : Since both σi and wi affect the net-
work output, an alternating optimization procedure can be employed:
  1. Initialize σi (e.g., all equal or based on data heuristics).


                                       165
Modern Intelligent Systems                                                            8


                        Primal

                                                   solve
                      Φ ∈ RN ×M             (Φ⊤ Φ + λI)w = Φ⊤ y     w ∈ RM
                     build features      Nys
                Dual (kernel ridge/SVM)
                                              tröm
                                                      M
                                                          <
                                                    solve N
                      K ∈ RN ×N                 (K + λI)α = y       α ∈ RN
                     kernel matrix

    Figure 32: Primal (finite basis) vs. dual (kernel ridge) viewpoints. Using as
       many centers as data points recovers the dual form; using fewer centers
      corresponds to a Nyström approximation. The same trade-off appears in
     kernel methods through the choice of kernel and effective rank. Use it when
    deciding whether to train a finite basis model or switch to a kernel viewpoint.


  2. Fix σi and find wi by solving the linear least squares problem (8.5).

  3. Fix wi and update σi to minimize the error, possibly using gradient-based
     methods or heuristics.

  4. Repeat steps 2 and 3 until convergence or error criteria are met.
    Note that the spreads σi can be scalar or vector-valued (anisotropic), allowing
different widths in each input dimension:

                                 σi = [σi1 , σi2 , . . . , σid ],

where d is the input dimension.

Summary of the Training Algorithm:
  1. Use clustering (e.g., K-means) to find centers vi (or sample centers uni-
     formly at random).

  2. Set widths σi via a rule-of-thumb (global σ from average center spacing or
     per-cluster covariance).

  3. Build Φ with entries Φji = φi (xj ); choose a small grid of λ values and
     solve (Φ⊤ Φ + λI)w = Φ⊤ y.

  4. Evaluate on a validation set and pick (σ, λ, M ) that minimizes validation
     loss; for classification, CE/hinge losses are also feasible with the same

                                              166
Modern Intelligent Systems                                                       8


       design matrix Φ.
 Practical RBFN training (pseudocode)
 Input: X, y, M, center_method=kmeans, sigma_rule, lambda_grid
 Centers = center_method(X, M)
 sigma = sigma_rule(Centers)
 Phi = build_design_matrix(X, Centers, sigma)   # NxM
 for lambda in lambda_grid:
     w_lambda = solve((Phi^T Phi + lambda I) w = Phi^T y)
     val_err[lambda] = validation_loss(Phi_val, y_val, w_lambda)
 lambda_star = argmin val_err
 Predict: yhat(x) = phi(x, Centers, sigma)^T w_lambda_star


Worked toy (classification, XOR-like). Consider four points and XOR
labels

       x1 = (0, 0), x2 = (0, 1), x3 = (1, 0), x4 = (1, 1),   t = [0, 1, 1, 0].

Choose M = 4 centers at the data and set a global σ from the mean inter-center
                                                                               
distance (here σ ≈ 0.8). Build Φ with entries Φji = exp − kxj − ci k2 /(2σ 2 )
and solve (Φ⊤ Φ + λI)w = Φ⊤ t over a small grid λ ∈ {10−4 , 10−3 , 10−2 }. The
best λ yields a linear separator in the lifted Φ-space that perfectly classifies
XOR; widening σ underfits, while shrinking σ without ridge overfits via an ill-
conditioned Φ⊤ Φ.

8.12    Remarks on Radial Basis Function Networks
Advantages:
  • Training speed: Once centers and spreads are fixed, training reduces
    to a linear least squares problem with a closed-form solution, which is
    computationally eﬀicient.

  • Universal approximation: RBF networks can approximate any contin-
    uous function on a compact domain to arbitrary accuracy given suﬀicient
    neurons, provided the centers cover the domain and the widths are chosen
    to avoid degeneracy (Micchelli, 1986; Park and Sandberg, 1991).


                                        167
Modern Intelligent Systems                                                               8


                 1.2



                   1



                 0.8



                 0.6
           x2




                 0.4



                 0.2



                   0



                −0.2
                   −0.2      0     0.2     0.4        0.6   0.8    1      1.2
                                                 x1

     Figure 33: RBFN decision boundary on XOR with 4 centers, sigma = 0.8,
     and ridge lambda = 1e-3. Shading indicates the predicted class under a 0.5
      threshold; the black contour marks the 0.5 boundary. Training points are
    overlaid (class 0: open circles; class 1: filled squares). See Figure 31 for sigma
     effects. Use it when checking whether center count and width are suﬀicient
                               for a non-linear boundary.


  • Interpretability: Centers correspond to representative data points, mak-
    ing the network structure more interpretable.

  • Applications: RBF networks have been successfully applied in control
    systems, communication systems, chaotic time series prediction (e.g.,
    weather and power load forecasting), and decision-making tasks.

  • Flexible losses: Squared loss is standard for regression; logistic or hinge
    losses pair naturally with the fixed design matrix for classification.

Disadvantages:
  • Parameter selection: Choosing the number of neurons M , centers vi ,


                                          168
Modern Intelligent Systems                                                         8


      and spreads σi is nontrivial and often requires heuristics or cross-validation.

   • Scalability: The number of radial units required can grow quickly with
     input dimensionality, increasing computation and storage costs.

   • Center determination: Identifying good centers (via clustering or other
     heuristics) can be computationally expensive and sensitive to noisy data.

Optional sidebar: Wiener filter refresher
Sidebar: why include Wiener filtering here? RBF networks inherit many
ideas from linear estimation (projection onto bases, Gaussian kernels). The short
Wiener-filter recap below is optional; feel free to skim or treat it as context that
connects kernelized least-squares estimators to the localized nonlinear networks
that opened this chapter.
    Recall from the previous discussion that the Wiener filter aims to minimize
the mean squared error (MSE) between the desired signal d(t) and the filter
output y(t), where
                                 y(t) = wT x(t),

with w the filter coeﬀicient vector and x(t) the input vector.
   The MSE cost function is
                                                   
                          J(w) = E |d(t) − wT x(t)|2 .                         (8.6)

    To find the optimal w⋆ , we set the gradient of J(w) with respect to w to
zero:
                        ∇w J(w) = −2p + 2Rw = 0,

where
                      R = E[x(t)xT (t)],      p = E[d(t)x(t)].

   Solving for w, we obtain the Wiener-Hopf equation:

                                    Rw⋆ = p.                                   (8.7)

   Assuming R is invertible, the optimal filter coeﬀicients are

                                   w⋆ = R−1 p.                                 (8.8)


                                        169
Modern Intelligent Systems                                                     8


   This completes the derivation of the Wiener filter solution.

Optional: interpretation and properties

Interpretation: The Wiener filter can be viewed as the linear estimator that
projects the desired signal d(t) onto the subspace spanned by the input vector
x(t) in the least-squares sense.

Properties:
  • Optimality: Minimizes the MSE among all linear filters.

  • Stationarity: Requires knowledge of the second-order statistics R and p,
    which are assumed stationary.

  • Causality: The Wiener filter as derived is non-causal; causal versions
    require additional constraints.

Optional: frequency-domain form For stationary processes, the Wiener
filter can be equivalently expressed in the frequency domain. Let Sxx (ω) and
Sdx (ω) denote the power spectral density (PSD) of the input and the cross-PSD
between desired and input signals, respectively. Then the frequency response of
the Wiener filter is
                                         Sdx (ω)
                                H(ω) =           .                         (8.9)
                                         Sxx (ω)
    This expression provides insight into the filter’s behavior as a frequency-
selective operator that emphasizes frequencies where the desired signal and input
are strongly correlated.

Optional: why adaptive filtering comes next While the Wiener filter
provides a closed-form solution, in practice the statistics R and p are often
unknown or time-varying. This motivates adaptive filtering algorithms such as
LMS and RLS, which iteratively approximate w⋆ using observed data.

8.13   Preview: Unsupervised and Localized Learning
In Chapter 9, we move from supervised RBF models to unsupervised, self-
organizing methods. Self-organizing maps (SOMs) and Hopfield-style associative


                                      170
Modern Intelligent Systems                                                       8
```

### Findings
Issues flagged in Chunk 12/31:

1. Narrative flow and transitions:
   - The transition from section 8.2.1 Mathematical Formulation to the figure (Figure 30) is abrupt. The figure is introduced without a clear lead-in sentence or explanation connecting it to the previous content. A brief sentence explaining the relevance of center placement before the figure would improve flow.
   - The "Author’s note" in section 8.8 interrupts the formal tone and flow. It might be better placed as a sidebar or clearly marked note to avoid breaking the narrative.
   - The "Optional sidebar: Wiener filter refresher" section is quite long and detailed for an optional sidebar. It might benefit from clearer separation or formatting to signal optional content, and a brief introductory sentence explaining its relevance before diving into equations.

2. Reader orientation:
   - In section 8.5, the example setup uses notation v1 and v2 for weight vectors associated with neurons, but earlier sections use ci or vi for centers. This inconsistency in notation could confuse readers. Consistent notation for centers/weights should be maintained or explicitly clarified.
   - The notation for the Gaussian RBF in section 8.3 and later sections sometimes uses σi and sometimes σ without subscript. Clarify when widths are shared or individual per basis function to avoid ambiguity.
   - The explanation of the design matrix Φ and its dimensions appears multiple times with slight variations. A consolidated, clear definition early on would help.

3. Repetitive templating:
   - The explanation of the Gaussian RBF function and its properties is repeated in multiple sections (8.3, 8.8, 8.9, 8.10). While some repetition is useful for emphasis, the content could be consolidated or cross-referenced to avoid redundancy.
   - The solution for weights w via normal equations and ridge regularization is presented multiple times (sections 8.6, 8.11, and the dual viewpoint). Consider consolidating these explanations or referencing earlier sections to reduce repetition.

4. Punctuation and spacing:
   - In section 8.2.1, the matrix G(x) is displayed with inconsistent spacing and alignment in the bracketed vector. The formatting of the vector could be improved for clarity.
   - In the formula for the Gaussian RBF (8.2), the spacing around the exponent and denominator is inconsistent; ensure consistent use of spacing and parentheses.
   - In the bullet points under 8.4 Key Properties and Advantages, the use of colons and semicolons is inconsistent. For example, some bullets end with periods, others do not.
   - In the "Author’s note" section, the quotation marks around “radial” and “see” are curly quotes, but elsewhere straight quotes are used. Consistency in quotation marks is recommended.
   - In the pseudocode snippet, the comment lines lack consistent capitalization and punctuation.

5. Clarity of prose:
   - The sentence "Use it when choosing how to place centers before tuning the width parameter." under Figure 30 is somewhat informal and vague. It could be rephrased for clarity, e.g., "Refer to this figure when deciding on center placement strategies prior to tuning the width parameter."
   - The phrase "The practical art is to pick centers that cover the data and then tune σ (and ridge λ) by validation, as in Figure 31." is informal. Consider rephrasing to maintain academic tone.
   - The explanation of the curse of dimensionality in section 8.4 is brief and could be expanded or linked to more detailed discussion elsewhere.
   - The explanation of the iterative optimization procedure in section 8.11 is terse; adding a brief rationale for alternating optimization would help reader understanding.
   - The "Worked toy (classification, XOR-like)" example is dense and could benefit from stepwise explanation or a small table summarizing inputs, transformations, and outputs.

No other concrete issues were found.
