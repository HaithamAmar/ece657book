# Scientific QA Report

- Source PDF: `notes_output/ece657_notes.pdf`
- Total chunks: 31

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
No issues spotted.

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
No issues spotted.

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
No issues spotted.

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
No issues spotted.

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
No issues spotted.

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
No issues spotted.

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
No issues spotted.

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
No issues spotted.

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
No issues spotted.

## Chunk 13/31
- Character range: 340518–368956

```text
memory discover structure in data (clusters, manifolds) without labeled targets,
complementing the supervised architectures covered so far.
 Key takeaways
 Minimum viable mastery
    • Localized Gaussian bases + linear readout give an interpretable
      nonlinear model; center/width/regularization choices control
      bias–variance.

    • Primal RBFNs and kernel ridge regression are two views of the same
      estimator (full vs. truncated basis); regularization cures conditioning.

    • RBFNs bridge learned-feature models (MLPs) and kernel methods
      (SVMs/GPs); they form a strong baseline for localized decision
      boundaries.

 Common pitfalls
    • Width selection: too small memorizes, too large collapses to a linear
      model; validate σ and λ.

    • Poor conditioning: without regularization, solves can be numerically
      unstable even when the math is correct.

    • Confusing kernels with bases: a full kernel method scales differently
      than a truncated (primal) basis expansion.




                                      171
Modern Intelligent Systems                                                     9


  Exercises and lab ideas
    • Train an RBFN on the two-moons dataset; sweep M and σ, add a
      small λ grid, plot validation curves and decision boundaries; report
      the (M, σ, λ) that minimizes validation error and discuss
      over/underfitting.

    • Compare primal RBFN and kernel ridge regression with an RBF
      kernel on datasets of size N ∈ {200, 2000, 20 000}; measure accuracy
      and runtime; note when each approach is preferable.

    • Show that setting centers at all data points with λ > 0 yields the
      same predictions as kernel ridge regression; derive the relationship
      between w and α.

    • Plot how validation error moves with (M, σ, λ) and link the curves
      back to the bias–variance discussion in Chapter 3.

 If you are skipping ahead. Keep the idea that “nonlinear” can still be
 linear-in-parameters once a basis is fixed. That perspective is reused in
 kernel methods and shows up again when we discuss architectural bias
 (CNNs) and representation choices.



Where we head next. Chapter 9 moves from supervised objectives to unla-
beled competitive learning and prototype organization. Chapter 10 then revisits
recurrence through an energy-based lens, setting up later sequence-model chap-
ters.


9 Introduction to Self-Organizing Networks and Un-
  supervised Learning
Chapter 8 offered a nonlinearity that stays close to linear algebra (basis expan-
sion + linear solve). Here we switch to unsupervised learning: self-organizing
maps discover prototypes and organize them on a lattice without labels. Figure 1
highlights this as the competitive/unsupervised branch.
    This chapter opens the unsupervised neural thread with Self-Organizing
Maps (SOMs), also known as Kohonen maps. Chapter 10 then studies Hopfield

                                      172
Modern Intelligent Systems                                                    9


networks as an energy-based associative memory model. Both operate without
explicit targets, in contrast to the supervised ERM pipeline in Chapter 3.
  Learning Outcomes
      • Describe how competitive learning, cooperation, and annealing
        interact in SOM training.

      • Monitor SOM quality via quantization/topographic errors and
        interpret U-Matrices.

      • Connect SOMs to broader unsupervised techniques (clustering,
        dimensionality reduction) and know when to use each.

  Design motif
  Competition plus cooperation: pick a winner, then let its neighbors learn
  too, so the map becomes both a clustering device and a visualization.


9.1    Overview of Self-Organizing Networks
Self-organizing networks are a class of neural networks designed to discover in-
herent structures in input data by organizing neurons in a way that reflects
the statistical properties of the data. The most prominent example is the Self-
Organizing Map (SOM), introduced by Teuvo Kohonen. SOMs are widely used
for tasks such as clustering, visualization, and dimensionality reduction.
    The key characteristics of SOMs include:
   • Unsupervised learning: No labeled outputs are required; the network
     self-organizes based on input similarity.

   • Competitive learning: Neurons compete to become the ”winner” for a
     given input, and only the winner and its neighbors update their weights.

   • Topology preservation: The network maps high-dimensional input data
     onto a usually two-dimensional grid of neurons, preserving the topological
     relationships of the input space.




                                      173
Modern Intelligent Systems                                                        9


 Historical intuition: two sheets and topographic neighborhoods
 A useful way to picture SOMs is as two coupled “sheets”: an input space
 and a fixed lattice of units. Each input is connected (in principle) to the
 whole lattice, but learning makes some regions of the lattice respond
 strongly (excitation) while others respond weakly (inhibition). The payoff
 is a topographic map: inputs that are far apart in the original space can
 end up near one another on the lattice if they are statistically similar under
 the features the SOM has learned.

 Author’s note: tie SOMs back to clustering and dimensionality
 reduction
 SOMs live in the same ecosystem as clustering and dimensionality
 reduction: they learn prototypes without labels and simultaneously
 organize those prototypes on a low-dimensional lattice. Treat the update
 rules as a carefully annealed clustering algorithm whose output just
 happens to be arranged on a grid for interpretability.

    The neighborhood influence is usually controlled by a kernel (often Gaussian)
whose amplitude decays with lattice distance and shrinks as training progresses,
so early updates promote global organization while later updates refine only the
closest units. Figure 34 juxtaposes these two time scales: the left panel shows
why coarse early steps help traverse the energy landscape quickly, while the
right panel compares two decaying learning-rate schedules commonly used when
training SOMs.
    Figure 43 pairs feature-plane views with U-Matrix diagnostics for SOM au-
dits.
    Before delving into the mathematical formulation and algorithmic details of
SOMs, it is important to review two foundational concepts that underpin their
operation: clustering and dimensionality reduction.

9.2   Clustering: Identifying Similarities and Dissimilarities
Clustering is the process of grouping a set of objects such that objects within
the same group (cluster) are more similar to each other than to those in other
groups. Formally, given a dataset X = {x1 , x2 , . . . , xN } where each xi ∈ Rd is
represented by a feature vector, the goal is to partition the data into K clusters


                                       174
Modern Intelligent Systems                                                            9


           Coarse → fine steps on f (x, y)                   Decay of α(t)
                           2   y
                                                   0.3
                           1
                  large steps         x            0.2
                          small steps




                                             α
             −2      −1              1   2
                          −1                       0.1

                          −2
                                                    0
                                                         0      20            40

                                                              α(t) =t 0.3 e−t/15
                                                              α(t) = 0.25 · 0.85t


     Figure 34: Learning-rate scheduling intuition. On a smooth objective (left),
     large initial steps quickly cover ground and roughly align prototypes, while a
        decaying step-size refines the solution near convergence. Right: common
       exponential and multiplicative decays used in SOM training. Use it when
             choosing a schedule that converges without freezing too early.


{C1 , C2 , . . . , CK } such that:
   • Intra-cluster similarity is maximized: points within the same cluster
     are close to each other.

   • Inter-cluster dissimilarity is maximized: points in different clusters are
     far apart.
In the classical formulation used here (e.g., for K-means), the clusters form a
partition of X : they are disjoint and their union equals the entire dataset.

Example: Consider three types of geometric shapes (triangles, circles, and
squares) represented only by their feature vectors without labels. Clustering
aims to group these shapes into clusters corresponding to their types based on
similarity in features, even though the network does not know the labels.

K-means Clustering: A classical and widely used clustering algorithm is
K-means, which operates as follows:
   1. Initialize K cluster centroids {v1 , v2 , . . . , vK } randomly.




                                             175
Modern Intelligent Systems                                                      9


  2. For each data point xi , assign it to the cluster with the nearest centroid:

                                ci = arg min kxi − vk k2 ,                   (9.1)
                                          k

      where k · k2 denotes the Euclidean norm.

  3. Update each centroid as the mean of all points assigned to it:

                                          1 X
                                  vk =         xi ,                          (9.2)
                                         |Ck |
                                              xi ∈Ck


      where |Ck | is the number of points in cluster Ck .

  4. Repeat steps 2 and 3 until convergence (i.e., cluster assignments no longer
     change significantly).
   K-means is an unsupervised learning method because it does not require
labeled data; it discovers clusters purely based on feature similarity.

9.3   Dimensionality Reduction: Simplifying High-Dimensional
      Data
Dimensionality reduction refers to techniques that transform high-dimensional
data into a lower-dimensional representation while preserving important struc-
tural properties, such as pairwise distances, variance, or neighborhood relation-
ships. This is crucial for:
  • Visualization: Humans can easily interpret data in two or three dimen-
    sions.

  • Computational eﬀiciency: Reducing dimensions can simplify subse-
    quent processing.

  • Noise reduction: Eliminating irrelevant or redundant features.

Example: Consider a three-dimensional cube. Depending on its orientation,
a linear projection (matrix multiplication by P : R3 → R2 with matrix repre-
sentation in R2×3 ) onto a two-dimensional plane can look like different shapes:
a square arises from an orthogonal projection onto a face, whereas a hexagon
appears under an oblique projection along a body-diagonal. This highlights that
while the combinatorial adjacency (which vertices are connected) is preserved

                                       176
Modern Intelligent Systems                                                          9


                 Orthogonal projection                  Oblique projection




            −1                           1         −1                        1




                       −1                                   −1

    Figure 35: Classical MDS intuition. Projecting a cube onto a plane via an
    orthogonal map yields a square (left), whereas an oblique projection along a
    body diagonal produces a hexagon (right). The local adjacency of vertices is
    preserved even though metric structure is distorted. Use it when interpreting
      low-dimensional embeddings as geometry-preserving only in limited ways.


under such a projection, Euclidean lengths and angles are inevitably distorted.
Figure 35 illustrates these two views.

Challenges: Reducing dimensions inevitably leads to some loss of information.
The goal is to minimize this loss while achieving a more tractable representation.

Common Techniques: Principal Component Analysis (PCA) is a linear
method that preserves orthogonal directions of maximum variance (the eigen-
vectors of the covariance matrix), while classical Multidimensional Scaling
(MDS) reconstructs an embedding by double-centering a squared-distance
matrix (B = − 21 JD(2) J, where Dij = kxi − xj k22 and J = I − n1 11⊤ is the cen-
                                  (2)

tering matrix) and performing eigen-decomposition so that Euclidean pairwise
distances are approximated as closely as possible. Methods such as t-SNE or
UMAP provide nonlinear embeddings that emphasize local neighborhoods but
typically do not preserve global distances. Self-Organizing Maps also serve as
a nonlinear dimensionality reduction technique by mapping high-dimensional
inputs onto a low-dimensional lattice while preserving neighborhood relation-
ships among data points, albeit on a discrete grid rather than a continuous
embedding.




                                             177
Modern Intelligent Systems                                                      9


9.4   Dimensionality Reduction and Feature Mapping
Recall from the previous discussion that dimensionality reduction aims to map
a high-dimensional feature space into a lower-dimensional representation while
preserving as much information as possible. This is crucial in many applications
such as image processing, speech recognition, and pattern analysis, where the
original data may have many correlated or redundant features yet the geomet-
ric relationships (distances, variance directions, neighborhoods) must remain
meaningful.
    For example, consider a face represented by multiple features: eyes, nose,
mouth, ears, shape of the face, etc. If we want to reduce this to three dimen-
sions, we must carefully choose which features to combine or discard so that the
essential characteristics of the face remain recognizable. A naive reduction that
drops important features arbitrarily will result in poor representation.
    Depending on the application, the map may be linear (a projection as in
PCA) or nonlinear (a learned embedding as in t-SNE or SOM; note that SOMs
produce a discrete lattice embedding rather than a continuous Euclidean em-
bedding). The goal is to find a mapping

                             f : Rn → Rm ,   m < n,

such that the new feature vector y = f (x) retains the salient structure of x, for
example by approximately preserving pairwise distances, nearest neighbors, or
dominant variance directions. Modern algorithms discover these combinations
automatically from data, often in an unsupervised manner (PCA, t-SNE, SOM).
Supervised (e.g., Linear Discriminant Analysis) and semi-supervised variants
also exist, where label information guides f , rather than relying on manual fea-
ture selection. For instance, PCA derives f analytically via eigen-decomposition
of the covariance matrix, whereas t-SNE and SOM learn f iteratively from data.

9.5   Self-Organizing Maps (SOMs): Introduction
Self-Organizing Maps (SOMs), also known as Kohonen maps, provide a powerful
approach to unsupervised learning that combines clustering and dimensionality
reduction. Unlike supervised neural networks, SOMs learn without explicit tar-
get outputs or labels. Instead, they discover the underlying structure of the
input data by organizing neurons in a topological map.


                                      178
Modern Intelligent Systems                                                   9


 SOM at a glance
 Objective: Learn prototype vectors wi arranged on a low-dimensional
 lattice such that nearby neurons represent nearby regions of the input
 space (topographic mapping).
 Key hyperparameters: Map size and topology, initial learning rate α(0),
 neighborhood width σ(0) and their decay schedules, distance metric
 (typically squared Euclidean).
 Defaults: Start with a 2D rectangular grid, squared Euclidean distance,
 exponentially decaying α(t) and σ(t), and a number of neurons comparable
 to or slightly larger than the expected number of clusters.
 Common pitfalls: Too small a map (forcing unrelated inputs to share
 neurons), overly fast decay of α(t) or σ(t) (freezing the map early), and
 interpreting the lattice as metric when it is only approximately
 topology-preserving.


Historical Context The concept of SOMs traces back to early models of self-
organizing topographic maps, such as the two-sheet formulation of Willshaw and
von der Malsburg (1976). Teuvo Kohonen later formalized and popularized the
algorithmic framework in Kohonen (1982) (see also Kohonen, 2001).

Basic Architecture Conceptually, the SOM consists of two stages:
  • Input layer: A vector x ∈ Rn representing the input features.

  • Output layer (map): A usually two-dimensional grid of units (neurons).
    Each neuron i is assigned a fixed coordinate vector ri = [ui , vi ]⊤ with
    ui , vi ∈ Z together with a weight vector wi ∈ Rn . The coordinates ri
    determine geometric proximity on the lattice and are used by the neigh-
    borhood function (Section 9.16).
    Each output neuron therefore possesses a weight vector of the same dimen-
sionality as the input, so evaluating the match between an input and the map
amounts to comparing the input against every stored prototype. The neurons
then compete; the closest (best matching) unit ”wins” and its neighbors are
allowed to adapt by nudging their weight vectors toward the input, while dis-
tant units remain unchanged during that update. The resulting organization

                                     179
Modern Intelligent Systems                                                         9


produces a discrete map that preserves qualitative ordering; it approximates the
topology of the input space without providing a continuous Euclidean embed-
ding.

Key Concept: Topographic Mapping The fundamental idea is that inputs
that are similar in the original space will activate output units that are close to
each other on the map. This preserves the topological relationships of the input
data in the reduced-dimensional output space.
    Formally, if Nϵ (x) = {z | kz − xk2 < ϵ} denotes an Euclidean ϵ-neighborhood
of an input vector, the SOM training procedure aims to ensure that the image of
this neighborhood under the map lies within a small neighborhood of the BMU
on the lattice. In practice the preservation is approximate (see, e.g., Kohonen,
2001 for discussion), but it is suﬀicient to maintain qualitative ordering of regions
in the input manifold.
    For example, two inputs x1 and x2 that are close in Rn will select best match-
ing units whose lattice locations ri and rj are neighbors on the output grid. This
spatial organization is what makes SOMs particularly useful for visualization and
clustering.

9.6   Conceptual Description of SOM Operation
  1. Initialization: The weight vectors wi are initialized, often randomly or
     by sampling from the input space.

  2. Competition: For a given input x, find the best matching unit (BMU)
     or winning neuron:
                           c = argmin kx − wi k22 ,                  (9.3)
                                         i

      that is, the BMU index c minimizes the squared Euclidean distance be-
      tween x and the candidate prototype wi . Minimizing the squared distance
      yields the same winner as minimizing the unsquared norm but stream-
      lines gradient derivations, so we retain the squared form for consistency
      with later update rules. Here k · k2 denotes the Euclidean norm unless
      explicitly stated otherwise. Euclidean distance is the default choice be-
      cause it yields particularly simple gradient expressions for the update rule
      (9.4), but alternatives such as Mahalanobis distance (for anisotropic co-
      variance structures) or cosine-based measures (e.g., the cosine distance

                                        180
Modern Intelligent Systems                                                           9


                             ⊤
      dcos (x, wi ) = 1 − ∥x∥x2 ∥w
                                 wi
                                   i ∥2
                                        ) can be used; the metric must be chosen to re-
      flect the notion of similarity relevant to the application. Throughout this
      section we denote the best matching unit (BMU) by the index c; alterna-
      tive notations such as j ⋆ or i⋆ in the literature refer to the same winning
      neuron.

  3. Cooperation: Define a neighborhood function hci (t) that determines the
     degree of influence the BMU has on its neighbors in the output grid. This
     function decreases with the distance between neurons c and i on the map
     and with time t.

  4. Adaptation: Update the weight vectors of the BMU and its neighbors to
     move closer to the input vector:
                                                                   
                       wi (t + 1) = wi (t) + α(t)hci (t) x − wi (t) ,            (9.4)

      where α(t) is the learning rate, which decreases over time, and the effective
      width of hci (t) likewise shrinks so that large-scale ordering occurs early and
      fine-tuning occurs later (see Section 9.16).

 Tiny numeric step (online update)
 Input x = [0.2, 0.8], two map units with weights w1 = [0.1, 0.9],
 w2 = [0.7, 0.3], coordinates r1 = [0, 0], r2 = [1, 0], α = 0.5, σ = 1. BMU
 c = 1 (closest to x). Neighborhoods: h11 = 1, h21 = exp(−1/2) ≈ 0.607.
 Updates:
                    w1 ← [0.15, 0.85], w2 ← [0.548, 0.452].

 Even the neighbor moves toward x, illustrating cooperation.

    This iterative process causes the map to self-organize, with neurons special-
izing to represent clusters or features of the input space.

9.7   Mathematical Formulation of SOM
Let the input space be X ⊆ Rn , and the output map be a lattice of neurons
indexed by i, each with weight vector wi ∈ Rn .




                                         181
Modern Intelligent Systems                                                             9


                            1
                                     Early σ(t) (broad)
                 hci (t)             Late σ(t) (narrow)


                           0.5




                            0
                                 0        1               2       3     4
                                        Lattice distance krc − ri k2

           Figure 36: Gaussian neighborhood weights in SOM training. Early
      iterations use a broad kernel so many neighbors adapt; later iterations shrink
      the neighborhood width sigma(t) so only units near the BMU update. Use it
            when tuning sigma(t) to trade global ordering for local refinement.


Best Matching Unit (BMU)                      Given an input x, the BMU is found by min-
imizing the squared distance:

                                      c = arg min kx − wi k22 .
                                                 i


Neighborhood Function A common choice for the neighborhood kernel is
the Gaussian function
                                                 
                                      krc − ri k2
                      hci (t) = exp −               ,          (9.5)
                                        2σ 2 (t)

where ri denotes the lattice coordinates of neuron i and σ(t) is the neighbor-
hood radius that decreases monotonically with t. Early in training σ(t) is large,
encouraging broad cooperation; as σ(t) shrinks, only neurons near the BMU
continue to adapt (Figure 36).

9.8     Kohonen Self-Organizing Maps (SOMs): Network Architec-
        ture and Operation
Building on the inspiration from perceptrons, Kohonen Self-Organizing Maps
(SOMs) introduce a distinctive neural network architecture designed for unsu-
pervised learning and feature mapping. Unlike classical supervised networks,
SOMs aim to discover the underlying structure of the input data by organizing
neurons in a fixed, usually low-dimensional, lattice.

                                                 182
Modern Intelligent Systems                                                       9


Network Structure
  • Input layer: The input vector x ∈ Rn represents the feature space, where
    n is the input dimension.

  • Output layer (map): A fixed lattice of neurons arranged in a low-
    dimensional grid, e.g., a 6 × 4 or 3 × 3 grid, independent of the input
    dimension.

  • Connectivity: Each neuron in the output layer is fully connected to all
    input components via a weight vector wi ∈ Rn , where i indexes the neuron.

Mapping and Competition The SOM maps the high-dimensional input x
to a single neuron in the output lattice that best represents the input. This
is achieved by measuring the similarity between x and each neuron’s weight
vector wi . The neuron with the highest similarity (or equivalently, the smallest
distance) is declared the winner.
    Formally, the winning neuron c for input x is given by

                             c = arg min kx − wi k22 ,                       (9.6)
                                       i

where k·k2 denotes the Euclidean norm. Squaring the norm leaves the minimizer
unchanged (arg mini kx − wi k2 = arg mini kx − wi k22 ), but simplifies derivatives
in the subsequent learning rule. Alternative similarity metrics (e.g., cosine dis-
tance) can replace kx − wi k2 when appropriate.

Weight Update Rule Only the winning neuron and its neighbors in the
lattice update their weights to better represent the input. This competitive
learning rule can be expressed as
                                                                 
                 wi (t + 1) = wi (t) + α(t) hci (t) x(t) − wi (t) ,          (9.7)

where the learning rate symbol matches the one used in the conceptual outline,
  • α(t) is the learning rate at iteration t,

  • hci (t) is the neighborhood function centered on the winning neuron c, typ-
    ically a Gaussian kernel that decreases with the lattice distance between
    neurons c and i (see Equation (9.5)).

                                        183
Modern Intelligent Systems                                                           9


    This update rule ensures that the winning neuron and its neighbors move
closer to the input vector, preserving topological relationships in the input space.
Intuitively, simultaneous adaptation of the BMU and its nearby units keeps
neighboring weight vectors in similar regions of the input space, so the lattice
retains the ordering of the data manifold.

9.9   Example: SOM with a 3 × 3 Output Map and 4-Dimensional
      Input
Consider a SOM with the following specifications:
  • Input dimension: n = 4, so each input vector is x = [x1 , x2 , x3 , x4 ]T .

  • Output lattice: 3 × 3 grid, totaling 9 neurons indexed i = 1, . . . , 9.

  • Each neuron i has a weight vector wi ∈ R4 .

Feedforward Computation For a given input x, each neuron computes a
similarity score. Two common choices are:

            yi = wi⊤ x                  (dot-product similarity),                 (9.8)
            di = kx − wi k22            (squared Euclidean distance).             (9.9)

In both expressions wi and x are column vectors, so wi⊤ x is a scalar similarity
score while di computes the squared Euclidean distance.
    When using dot products we select the neuron with the maximum yi ; when
using distances we equivalently select the neuron with the minimum di (or the
maximum of −di ):
                
                arg max y , if similarities are measured via (9.8),
                         i i
           c=
                arg mini di , if distances are used as in (9.9).


Weight Initialization and Update Weights wi are typically initialized ran-
domly or sampled from the input distribution. During training, for each input x,
the winning neuron c and its neighbors update their weights according to (9.7).

Illustration
  • Suppose the input x is presented.

                                       184
Modern Intelligent Systems                                                    9


  • Compute yi = wiT x for all neurons i.

  • Identify the winning neuron c with the highest yi .
```

### Findings
No issues spotted.

## Chunk 14/31
- Character range: 368959–398246

```text
• Update wc and neighboring weights wi using (9.7).
    This process repeats over many inputs, gradually organizing the map such
that neighboring neurons respond to similar inputs, effectively performing a
topology-preserving dimensionality reduction.
    The lattice coordinates ri ∈ Z2 introduced for the neighborhood kernel serve
as the geometry of the output grid; distances such as kri − rc k2 determine how
strongly each neuron responds when c wins. Broad kernels (large σ(t)) encourage
global ordering early in training, whereas shrinking σ(t) confines adaptation to
local neighborhoods so that fine-grained structure emerges. Alternative kernel
shapes (e.g., Epanechnikov, bubble) can be used, though Gaussians provide
smooth decay and convenient derivatives.
    SOM training is typically stochastic: each input triggers an update, so the
map continuously refines prototypes as data arrive. Batch variants exist, but
online updates capture streaming data and mirror Kohonen’s original algorithm.
Initialization also affects convergence; besides random sampling, practical sys-
tems often initialize weights along leading principal components to align the
lattice orientation with the data manifold.

9.10   Key Properties of Kohonen SOMs
  • Fixed output dimension: The lattice size is a design choice specified a
    priori and does not automatically scale with the input dimension.

  • Winner-takes-all competition: Only the best matching unit and its
    neighbors adapt their weights, encouraging topological ordering.

  • Neighborhood cooperation: Updating neighboring neurons enforces
    smooth transitions across the map.

9.11   Winner-Takes-All Learning and Weight Update Rules
Recall that in competitive learning networks, the neuron with the highest dis-
criminant value for a given input x is declared the winner. This subsection
analyzes the classical winner-takes-all (WTA) principle in which only the win-
ning neuron updates its weights, while all others remain unchanged. In the SOM

                                     185
Modern Intelligent Systems                                                      9


setting discussed earlier, a softened variant is used in which the winner and its
lattice neighbors update together.

Discriminant Function and Similarity Measures The discriminant value
for neuron j is typically computed from a similarity or distance measure between
the input x and the neuron’s weight vector wj . Two common formulations are:
   • Maximizing similarity:

                                       gj (x) = wj⊤ x.

         where a higher inner product indicates greater similarity.

   • Minimizing distance:

                                    dj (x) = kx − wj k22 .

         where a smaller Euclidean distance indicates greater similarity.
    While both are valid, minimizing the Euclidean distance is often preferred
for weight updates because it leads to more tractable learning rules.

Weight Update Rule Once the winning neuron c is identified, its weight
vector wc is updated to better represent the input x. The general update rule
is:

                             wc (t + 1) = wc (t) + ∆wc (t).                 (9.10)

   where t indexes the iteration or training cycle and ∆wc (t) = wc (t+1)−wc (t).
   The increment ∆wc (t) is chosen to reduce the distance between wc and x,
but not to make them identical immediately. This is because:
   • Multiple inputs x may be represented by the same neuron.

   • Immediate convergence to a single input would prevent generalization.
       Hence, the update is typically proportional to the difference between x and
wc :

                             ∆wc (t) = α(t) (x − wc (t)) .                  (9.11)

                                          186
Modern Intelligent Systems                                                       9


    where α(t) ∈ [0, 1) is the learning rate at iteration t. The learning rate
controls the step size so that wc moves toward x gradually rather than collapsing
to it in a single update.

Learning Rate Schedule The learning rate α(t) controls the magnitude of
weight updates. It typically decreases over time to ensure convergence and
stability:

                         α(t + 1) ≤ α(t),     lim α(t) = 0.
                                              t→∞

    This schedule allows large adjustments early in training (rapid learning) and
fine-tuning later (stabilization). Practitioners often start with α(0) in the range
0.05–0.5 and decay it toward 10−3 or smaller so that updates remain responsive
initially but become conservative as the map stabilizes.

Summary of the Competitive Learning Algorithm
  1. Initialize weights wj (0) randomly or heuristically.

  2. For each input x:

       (a) Compute discriminant functions gj (x) or distances dj (x).
       (b) Select winning neuron:

                         c = arg max gj (x)       or c = arg min dj (x)
                                    j                          j


       (c) Update the winning neuron’s weights using (9.10) and (9.11).

  3. Decrease learning rate α(t) according to schedule.

  4. Repeat until convergence or maximum iterations reached.

9.12   Numerical Example of Competitive Learning
Consider a simple example with:
  • Four input vectors x1 , x2 , x3 , x4 ∈ R4 .

  • A competitive layer with three neurons (clusters).



                                        187
Modern Intelligent Systems                                                         9


  • Initial learning rate α(0) = 0.3 with multiplicative decay α(t) = 0.3 × 0.5t
    (ensuring α(t) > 0).

  • No neighborhood function (i.e., only the winner updates).

Initial Weights The initial weights wj (0) for neurons j = 1, 2, 3 are:
                                                 
                                  0.2 0.3 0.5 0.1
                                                 
                         W(0) = 0.2 0.3 0.1 0.4
                                  0.3 0.5 0.2 0.3
   where row j contains the initial weight vector wj (0) for neuron j = 1, 2, 3.

9.13   Winner-Takes-All Learning Recap
Recall from the previous discussion that in the Winner-Takes-All (WTA) learn-
ing scheme, for each input vector x, we compute the similarity (or distance)
between x and each neuron’s weight vector wj . The neuron c with the mini-
mum distance (or maximum similarity) is declared the winner:

                             c = arg min kx − wj k22 .                     (9.12)
                                       j


   Only the weights of the winning neuron are updated according to:

                     wc (t + 1) = wc (t) + α(t) (x − wc (t)) ,             (9.13)

where α(t) is the learning rate (constant or decaying). In the full SOM update
of (9.7), this increment is additionally scaled by the neighborhood kernel hci (t)
so that only units with lattice coordinates ri near the BMU location rc receive
appreciable adjustments.
    This process is repeated for each input in the training set, and multiple
epochs are run with a gradually decreasing α until convergence.

Practical considerations In both SOMs and WTA networks, input vec-
tors are commonly normalized (e.g., zero mean and unit variance) so that dis-
tance comparisons are meaningful. Training is typically terminated when weight
changes fall below a small threshold or after a prescribed number of epochs.



                                       188
Modern Intelligent Systems                                                                    9


                                      Bias         Variance         Total error

                0.8

                0.6
        Error




                0.4
                                                     validation floor
                0.2

                 0
                      0   0.1   0.2   0.3    0.4      0.5     0.6       0.7   0.8   0.9   1
                                             Model capacity

    Figure 37: Bias–variance trade-off when sweeping SOM capacity (number of
     units or kernel width). The optimum appears near the knee where bias and
      variance intersect. Use it when selecting map size/capacity via validation
                             curves rather than aesthetics.


9.14   Regularization and Monitoring During SOM Training
Even though SOMs are inherently unsupervised, their training dynamics still
benefit from the same regularization heuristics used in supervised settings. Two
complementary diagnostics are especially useful in practice.

Bias–variance view. Increasing the lattice resolution or keeping the kernel
width large for too long can overfit local noise. Figure 37 visualizes the famil-
iar U -shaped trade-off: the left regime underfits (high bias), whereas the right
regime yields jagged maps (high variance).

Loss-landscape smoothing. Adding small cooperative penalties (e.g., weight
decay between neighbors) produces smoother loss contours and accelerates con-
vergence, as sketched in Figure 38. The penalty discourages neighboring proto-
types from diverging and keeps the map topologically ordered.

Quantization vs. information preservation. Classical SOM optimizes
a topology-preserving vector quantization objective; it does not include cross-
entropy terms. Modern variants sometimes introduce auxiliary regularizers
to encourage codebook utilization (e.g., entropy penalties on assignment his-
tograms) or draw analogies to VQ-VAE. Monitoring both quantization error


                                               189
Modern Intelligent Systems                                                           9


                 Unregularized                          Neighbor-coupled



        w2                                       w2




                       w1                                       w1

     Figure 38: Regularization smooths the loss surface. Coupling neighboring
     prototypes (right) yields wider, flatter basins than the jagged unregularized
      landscape (left). Use it when explaining why regularization can improve
                              stability and generalization.


and an entropy-style regularizer, as in Figure 39, helps reveal when the map is
collapsing to a few units or when density variations are no longer represented
faithfully.

Quantization vs. topographic error. Given data points {xi } and best-
matching units bi = BMU(xi ), the quantization error is

                                  1 X
                                        N
                             QE =     x i − w bi 2 ,
                                  N
                                        i=1

which measures reconstruction fidelity. The topographic error is the fraction of
inputs whose first- and second-best BMUs are not adjacent on the lattice (de-
fault: 4-neighbor connectivity), capturing topology preservation. Both metrics
reappear in later figures; we monitor QE for representation quality and TE for
magnification distortions.
 Batch SOM in practice
 Online SOM updates one sample at a time: pick a best-matching unit
 (BMU), nudge it and its neighbors, move on. Batch SOM instead
 aggregates responsibilities across a dataset (or mini-batch) before shifting




                                         190
Modern Intelligent Systems                                                                    9




          Objective
                      0.5



                       0
                                                                                          1
                       0                                                            0.8
                               0.2                                            0.6
                                     0.4                                0.4
                                           0.6                  0.2
                                                 0.8    1 0
                            Quantization error                          Entropy penalty

     Figure 39: Quantization error combined with an entropy-style regularizer
       (modern SOM variant; for example, a negative sum of p log p over unit
    usage). Valleys arise when prototypes cover the space evenly; ridges highlight
     collapse or poor topological preservation. Use it when diagnosing prototype
                           collapse versus healthy coverage.


 prototypes:
                                                                   
                                     hj,i (t) = κ dist(j, b(i)); σt ,
                                                P
                                      (t+1)       i hj,i (t) xi
                                     wj       = P               .
                                                    i hj,i (t)

 Key differences:
    • Deterministic passes. Batch updates remove stochastic noise and
      converge in fewer epochs on static datasets, making results
      reproducible (useful for dashboards/visual analytics).

    • Parallelism. Computations collapse to matrix ops (compute BMUs,
      accumulate weighted sums), so GPUs/CPUs can process large
      mini-batches eﬀiciently.

    • Streaming trade-off. Online updates remain preferable when data
      arrive continuously or when you need the map to adapt mid-stream;
      batch SOM suits offline datasets.
 Most modern SOM libraries expose both modes, so choose the update rule
 that matches your data pipeline and stability requirements.




                                                  191
Modern Intelligent Systems                                                           9


                               Quantization error     Topographic error
                 1

                0.8

                0.6
        Error




                0.4
                                                         stop window
                0.2

                 0
                      0   10        20           30       40           50   60
                                             Epoch

    Figure 40: Validation curves used to identify an early-stopping knee. When
       both quantization and topographic errors flatten (shaded band), further
    training risks map drift. Use it when deciding where to stop training based on
                              stability, not only final error.


Stopping criteria. Because stochastic updates can eventually increase topo-
graphic error, it is standard to stop training once a moving-average validation
curve plateaus. Figure 40 shows the canonical trend: fast initial improvement
followed by saturation.

9.15   Limitations of Winner-Takes-All and Motivation for Coop-
       eration
While WTA is simple and effective for clustering, it has some limitations:
  • Only one neuron updates per input, which can lead to slow convergence.

  • The hard competition ignores relationships among neighboring neurons.

  • The resulting clusters correspond to hard assignments, so boundaries be-
    tween codebook vectors are sharp with little smoothing across neighboring
    neurons.
The geometric effect of these limitations is easiest to see in Figure 41: the left
panel shows the brittle Voronoi partitions created by a strict winner-takes-all
rule, whereas the right panel demonstrates how shrinking the neighborhood
kernel produces softer responsibilities and smoother maps.
    To address these issues, the concept of cooperation among neurons is intro-
duced. Instead of a single winner neuron updating its weights, a neighborhood


                                           192
Modern Intelligent Systems                                                           9


                  Hard BMU regions                         Soft assignments

             x2             r3        r4




                                                      x2
                       r1                  r2

                                                                      σ(t) small

                                 x1                              x1

      Figure 41: Voronoi-like regions induced by SOM prototypes (left) and the
       corresponding softmax confidence after shrinking the neighborhood kernel
    (right). Softer updates blur the decision frontiers and reduce jagged mappings
       between adjacent neurons. Use it when interpreting a prototype map as a
                      piecewise-constant partition of feature space.


of neurons around the winner also update their weights, albeit to a lesser extent.
This idea leads to smoother mappings and better topological ordering.

9.16    Cooperation in Competitive Learning
Neighborhood Concept Consider the output layer arranged in a 2D grid
(or lattice) of neurons. For each input x, after determining the winning neuron
c, we define a neighborhood N (c) consisting of neurons close to c in the output
space. In practice the neighborhood weight is supplied by the kernel hjc (t) of
(9.5), which is positive for units inside the neighborhood (and decays with the
lattice distance krj − rc k) and zero for units far away.
    The neighborhood size typically shrinks over time during training, starting
large to encourage global ordering and gradually reducing to fine-tune local
details.

Weight Update with Neighborhood Cooperation The lattice structure
and how the best matching unit (BMU) influences nearby neurons are visualized
in Figure 42. The U-Matrix on the right provides a quick diagnostic for cluster
boundaries during training.




                                                193
Modern Intelligent Systems                                                                           9


                                                         U-Matrix (neighbor distances)
                                                                                     avg. distance
                                                                                              0.9



                    ∥rj − rc ∥ = 1
                                                                                              0.6




                                                                                              0.3
                      rc
  SOM lattice and BMU neighborhood

     Figure 42: Left: a 5-by-5 SOM lattice with best matching unit (blue) and
     neighbors inside the Gaussian-kernel radius (green). Right: a toy U-Matrix
      (grayscale-safe colormap) showing average distances between neighboring
     codebook vectors; larger distances indicate likely cluster boundaries. Use it
         when reading U-Matrices as boundary hints, not absolute distances.


   The weight update rule generalizes to:

                   wj (t + 1) = wj (t) + α(t) hjc (t) (x − wj (t)) ,                         (9.14)

where
  • hjc (t) is the neighborhood function that quantifies the degree of cooperation
    between neuron j and the winner c.

  • α(t) is the learning rate at time t.
   The neighborhood function satisfies:
                                     
                                     
                                     
                                     1,            j=c
                       hjc (t) =         ∈ (0, 1), j ∈ N (c), j 6= c
                                     
                                     
                                     
                                         0,         otherwise

Gaussian Neighborhood Function A common choice for hjc (t) is a Gaus-
sian function based on the distance between neurons j and c on the output




                                              194
Modern Intelligent Systems                                                                         9


             Plane: pixel 1          Plane: pixel 2         Plane: pixel 3
                                                                                      0.70.7
             0 0.1 0.1 0.2 0.3        0.3 0.1 0   0    0    0.1 0.2 0.3 0.4 0.5
             0 0.1 0.2 0.3 0.4        0.4 0.2 0.1 0    0    0.1 0.2 0.3 0.4 0.5
             0 0.1 0.2 0.4 0.5        0.5 0.3 0.2 0.1 0     0.1 0.2 0.3 0.4 0.5         0.35
             0.1 0.2 0.3 0.5 0.6      0.6 0.4 0.3 0.2 0.1   0.1 0.2 0.3 0.4 0.5
             0.2 0.3 0.4 0.6 0.7      0.7 0.5 0.4 0.3 0.2   0.1 0.2 0.3 0.4 0.5
                                                                                  0     0

       Figure 43: Component planes for three features on a trained SOM (toy
        data). Each plane maps one feature across the grid; aligned bright/dark
     regions reveal correlated features and complement the U-Matrix in Figure 42.
     Interpret brightness comparatively within a plane rather than as an absolute
      scale. Use it when diagnosing which input features drive map organization.


lattice:
                                                                   
                                                   krj − rc k2
                                   hjc (t) = exp −                      ,                      (9.15)
                                                     2σ 2 (t)

where
   • rj and rc are the coordinates of neurons j and c on the output grid.

   • σ(t) is the neighborhood radius (width) at time t, which decreases over
     training.
   This function ensures that neurons closer to the winner receive larger updates,
while distant neurons are updated less or not at all.

Interpretation The cooperative update encourages neighboring neurons to
become sensitive to similar inputs, thereby preserving topological relationships
in the input space. This is the key principle behind Self-Organizing Maps
(SOMs).

9.17       Example: Neighborhood Update Illustration
Suppose the output neurons are arranged in a 2D lattice as shown schematically
in Figure 44, where each neuron is indexed by its grid coordinates. For an input
x, neuron c wins. The neighborhood N (c) might include neurons within a radius
σ around c.



                                                   195
Modern Intelligent Systems                                                        9




                                      BMU c
                                              radius σ(t)




    Figure 44: SOM lattice with the best-matching unit (BMU) highlighted in
     blue and a dashed neighborhood radius indicating which prototype vectors
    receive cooperative updates. Use it when visualizing the cooperative update
                          neighborhood around the BMU.


   Each neuron j in N (c) updates its weight vector according to (9.14), with
the magnitude of update modulated by hjc (t).

9.18     Summary of Cooperative Competitive Learning Algorithm
  1. Present an input vector and identify the winning neuron using the discrim-
     inant function.

  2. Update the winning neuron’s weights and those of its neighbors according
     to the cooperative rule.

  3. Decrease the learning rate and neighborhood radius according to the an-
     nealing schedule.

  4. Repeat for all inputs until the map stabilizes or a maximum number of
     epochs is reached.

9.19     Wrapping Up the Kohonen Self-Organizing Map (SOM)
         Derivations
We conclude our derivation and discussion of the Kohonen Self-Organizing Map
(SOM) learning algorithm by summarizing the key components and their evolu-
tion during training.
    Recall the weight update rule for neuron j at time step t:

                      ∆wj (t) = α(t) hj,c (t) [x(t) − wj (t)] .               (9.16)

where:


                                        196
Modern Intelligent Systems                                                       9


  • x(t) is the input vector at time t.

  • wj (t) is the weight vector of neuron j at time t.

  • c is the index of the winning neuron (best matching unit) for input x(t).

  • α(t) is the learning rate, a monotonically decreasing function of time.

  • hj,c (t) is the neighborhood function centered on the winning neuron c, also
    decreasing over time.

Neighborhood Function and Its Role               The neighborhood function hj,c (t)
typically takes a Gaussian form:
                                                       
                                          krj − rc k2
                         hj,c (t) = exp −                   .                (9.17)
                                            2σ 2 (t)

where:
  • rj and rc are the positions of neurons j and c on the SOM lattice.

  • σ(t) is the neighborhood radius, which decreases over time.
    This function ensures that neurons closer to the winning neuron receive larger
updates, while those farther away receive smaller or zero updates. Initially, σ(t)
is large, allowing broad neighborhood cooperation, but it shrinks as training
progresses, focusing updates increasingly on the winning neuron itself.

Time-Dependent Parameters Both the learning rate α(t) and neighbor-
hood radius σ(t) decrease over time, typically following exponential decay laws:
                                               
                                              t
                             α(t) = α0 exp −      ,                          (9.18)
                                             τα
                                               
                                              t
                             σ(t) = σ0 exp −      ,                          (9.19)
                                             τσ

where α0 and σ0 are initial values, and τα , τσ are time constants controlling the
decay rates.

Summary of the Six Learning Steps            SOM training iteratively repeats the
following six steps:


                                       197
Modern Intelligent Systems                                                    9


  Self-Organizing Map (SOM) training pseudocode

    1. Initialize weight vectors wj (0) randomly or from samples.

    2. For iteration t = 0, . . . , T :

        (a) Sample an input x(t).
        (b) Find the best matching unit (BMU)
            c = arg minj kx(t) − wj (t)k22 .
        (c) Compute neighborhood coeﬀicients hj,c (t).
        (d) Update every neuron:
                                                                        
                        wj (t + 1) = wj (t) + α(t) hj,c (t) x(t) − wj (t) .

        (e) Decay learning-rate α(t) and neighborhood radius σ(t) (e.g.,
            exponentially).

  Batch SOM (deterministic pass)

    1. Fix centers rj on the lattice; initialize wj (random data or along
       PCA directions).

    2. Repeat until convergence or max epochs:

        (a) Assign each xn to its BMU cn .
        (b) For each neuron j, update
                                              P
                                                n hj,cn (t) xn
                                          wj ← P               .
                                                  n hj,cn (t)

        (c) Decay α(t), σ(t).

  Batch SOM (one pass per epoch) is deterministic given the assignments; it
  often stabilises faster than purely online updates.

These procedural steps implement three conceptual stages: (1) Initialization
(seed the weight lattice), (2) Competition (select the best-matching unit for
each input), and (3) Cooperation (neighborhood-weighted updates plus the
associated parameter decay). Calling out these stages separately helps when

                                             198
Modern Intelligent Systems                                                    9


comparing SOMs to other competitive-learning algorithms later in the chapter.
   These steps are repeated until convergence criteria are met, such as a maxi-
mum number of iterations or a threshold on weight changes.

Stages vs. Steps It is important to distinguish between the three stages of
SOM learning and the six steps described above:
   • Stages:

        1. Initialization: setting up the network.
        2. Competition: neurons compete to respond to input.
        3. Cooperation: neighboring neurons cooperate to update weights.

   • Steps: The six procedural steps in Section 9.19 that operationalize these
     stages during training.

9.20   Applications of Kohonen Self-Organizing Maps
Kohonen SOMs are widely used for:
   • Clustering: Grouping similar data points without supervision.

   • Dimensionality Reduction: Mapping high-dimensional data onto a low-
     dimensional space (often arranged as a discrete lattice in SOM implemen-
     tations) for visualization and exploratory analysis.

   • Data Visualization: Providing intuitive heatmaps or component planes
     that reveal correlations and patterns across features.

Relation to k-means and modern variants When the SOM lattice is col-
lapsed to a single point, the algorithm reduces to a k-means-style prototype up-
date without any notion of neighborhood (MacQueen, 1967); SOMs therefore sit
between pure clustering (k-means) and manifold learning, adding a topographic
prior that encourages neighboring units to represent similar inputs. Recent
“neural-SOM” hybrids embed SOM-like updates inside deep networks, but still
rely on the same BMU search and neighborhood-weighted updates described
above.




                                      199
Modern Intelligent Systems                                                       9
```

### Findings
No issues spotted.

## Chunk 15/31
- Character range: 398250–426919

```text
Theory notes and recipes
 Convergence/magnification: With decays α(t) → 0, σ(t) → 0 and
 P              P 2
    t α(t) = ∞,    t α (t) < ∞, SOM updates converge under mild
 assumptions (Erwin et al., 1992; Cottrell and Fort, 1986). Lattice density
 follows data density (magnification) so dense regions attract more neurons.
                                        √     √
 Map-size/schedule recipe: Use 5 N –10 N neurons when unsure; hex
 grids reduce anisotropy; toroidal lattices mitigate edges. Initialize wj from
 data or first two PCs; α0 ∈ [0.1, 0.5] → αmin ≈ 10−3 ; σ0 equal to the map
 radius, decaying to 1–1.5 cells.

 Related and growing variants
 Neural Gas / Growing Neural Gas (Martinetz et al., 1993; Fritzke,
 1994) drop the fixed lattice and learn topology or add units dynamically.
 GTM (Bishop et al.) provides a probabilistic, topographic embedding
 with likelihoods/uncertainty. SOMs sit between k-means (no topology) and
 these adaptive-topology models.


Complexity and out-of-sample mapping. A full online epoch costs
O(N M ) (N data, M units); batch passes cost similar but fewer epochs. For
large M, use approximate nearest-neighbor BMU search (k-d trees, FAISS). New
points map via their BMU; optional soft responsibilities use hci for smoothing.

Theory link to other chapters. SOMs learn prototypes like the centers in
Chapter 8 but add a topographic prior; quality diagnostics (QE/TE) can be
tracked with the validation-curve diagnostics in Chapter 3. For task-driven em-
beddings, see Chapters 11 and 13; Hopfield (Chapter 10) contrasts with energy-
based associative recall.

Quality measures and magnification.         Two diagnostics are standard when
reporting SOM quality:
  • Quantization error (QE): average Euclidean distance between each in-
    put and its BMU. Lower QE indicates prototypes that better represent
    the data manifold.



                                     200
Modern Intelligent Systems                                                   9


  • Topographic error (TE): fraction of inputs whose first- and second-best
    BMUs are not adjacent, quantifying topology preservation (magnification
    factor).
Tracking both metrics reveals whether the neighborhood decay is too slow (over-
smoothing) or too aggressive (tearing the topology). Chapter 3’s learning-curve
plots suggest early-stopping heuristics: stop when QE/TE on a validation split
flatten.




                                     201
Modern Intelligent Systems                                                 9


 Key takeaways
    • SOMs perform topology-preserving vector quantization on a discrete
      lattice.

    • A shrinking neighborhood and decaying learning rate drive
      coarse-to-fine organization.

    • U-Matrices and quantization/topographic errors are practical
      diagnostics for convergence.

 Minimum viable mastery.
    • Given x, compute the BMU, write the weight update
      wi ← wi + α(t)hci (t)(x − wi ), and explain how hci enforces
      cooperation.

    • Interpret a U-Matrix and component planes as diagnostics for
      neighborhood structure and convergence.

    • Choose sensible α(t) and σ(t) schedules and justify them using
      QE/TE validation curves.
 Common pitfalls.
    • Using a map that is too small or a neighborhood decay that is too
      aggressive (tearing the topology).

    • Skipping input normalization, causing prototypes to track scale
      rather than structure.

    • Treating lattice distance as a true metric in data space (SOM
      topology is approximate, not exact geometry).

    • Over-interpreting a single run without checking QE/TE plateaus and
      sensitivity to initialization.




                                     202
Modern Intelligent Systems                                                    10


  Exercises and lab ideas
     • Train a 10 × 10 SOM on handwritten digits (MNIST) and plot
       component planes; report quantization/topographic errors as training
       progresses.

     • Implement the six-step SOM procedure with both Gaussian and
       rectangular neighborhood functions and compare convergence speed.

     • Visualize the effect of annealing schedules by freezing the learning
       rate and neighborhood radius at different epochs and observing the
       resulting U-Matrix.

     • Compare SOM prototypes to K-means centers on the same dataset;
       sweep (σ(t)) schedules and map sizes; report QE/TE and a
       trustworthiness@k measure.

  If you are skipping ahead. Keep the notion of an “energy landscape”
  from this chapter in mind: Chapter 10 makes that idea explicit with a
  Lyapunov energy, and later attention models (Chapter 14) can be read as
  learned, content-based neighborhood selection.



Where we head next. Chapter 10 extends the unsupervised thread with
energy-based associative memory, complementing SOM topology learning with
retrieval dynamics that foreshadow later attention-style mechanisms.


10    Hopfield Networks: Introduction and Context
Chapter 9 focused on self-organizing maps and unsupervised feature maps; we
now transition to another unsupervised/energy-based model: the Hopfield net-
work, a recurrent system that stores patterns as attractors. Figure 1 marks this
as the energy-based branch.




                                      203
Modern Intelligent Systems                                                    10


 Learning Outcomes
    • Interpret Hopfield networks as energy-minimizing recurrent systems
      and derive their asynchronous update rule.

    • Quantify capacity, recall dynamics, and pitfalls (spurious memories,
      bias encodings) using simple analytical bounds.

    • Relate Hopfield updates to modern energy-based models and
      attention mechanisms to build intuition for later chapters.

 Design motif
 Constrain recurrence so the dynamics become a descent process: symmetric
 weights and an energy function turn “feedback” into “stable memory.”


10.1   From Feedforward to Recurrent Neural Networks
Feedforward neural networks are characterized by a unidirectional flow of infor-
mation: inputs propagate through successive layers until reaching the output
layer, and backpropagation updates weights via error gradients. They work
well for static input→output mappings, but they do not capture the recurrent,
feedback-driven dynamics observed in biological neural systems.
    Recurrent neural networks introduce cycles in the connectivity graph, so a
neuron’s state can influence itself and upstream neurons through feedback loops.
These cycles enable internal state and temporal dynamics, which are essential for
sequences and memory—but they also create instability and training diﬀiculty.

Challenges with General Recurrent Networks However, the general
topology of recurrent networks introduces significant challenges:
  • Unstable dynamics: Without careful design, recurrent networks may
    fail to settle into stable states, instead exhibiting chaotic or oscillatory
    behavior.

  • Dependence on initial conditions: The final state of the network can
    be highly sensitive to the initial state, making the network’s behavior un-
    predictable.




                                      204
Modern Intelligent Systems                                                       10


  • Training diﬀiculties: Backpropagation through time and other train-
    ing methods can be computationally expensive and prone to vanishing or
    exploding gradients.
    These issues historically limited the practical use of recurrent networks, lead-
ing to a preference for feedforward architectures in many applications.
 Then vs. now: energy-based memory in context
    • Then (classical Hopfield): binary states, symmetric weights, and
      an explicit Lyapunov energy guarantee convergence to a fixed point.

    • What persists: stable attractors, pattern completion, and the idea
      that “memory” is a geometry (an energy landscape), not a stored list.

    • What changes in modern systems: memory is often
      content-addressable and learned from data at scale (retrieval,
      associative recall), with softer states and differentiable training
      objectives.

    • How to read the bridge: keep the energy/attractor intuition, but
      do not assume every modern memory mechanism inherits Hopfield’s
      symmetry or convergence guarantees.

 Author’s note: stabilizing recurrence
 General recurrent networks can behave unpredictably because feedback can
 create cycles that oscillate or amplify small differences. Hopfield’s key move
 was to restrict the architecture so the dynamics become a descent process:
 symmetric weights and no self-loops allow the network to be assigned an
 energy function that decreases under asynchronous updates. That single
 design choice turns “recurrent” from “chaotic” into “stable memory.”


10.2   Hopfield’s breakthrough
In 1982, John Hopfield introduced a special class of recurrent networks that over-
came many of these challenges by imposing specific constraints on the network
architecture and weights (Hopfield, 1982). The key insights were:
  • Symmetric weights: The connection weights between neurons are bidi-



                                       205
Modern Intelligent Systems                                                      10


       rectional and symmetric, i.e.,

                                    wij = wji         ∀i, j,                 (10.1)

       where wij is the weight from neuron j to neuron i.

   • No self-connections: Neurons do not have self-feedback loops, so

                                        wii = 0       ∀i.                    (10.2)

   • Binary neuron states: Each neuron i has a state si ∈ {+1, −1}, repre-
     senting on or off states, rather than continuous activations.

   • Energy-based formulation: The network dynamics can be described
     by an energy function E(s) that decreases monotonically as the network
     updates its states, guaranteeing convergence to a stable fixed point.
    These constraints ensure that the network evolves toward local minima of
the energy function, providing a natural mechanism for associative memory and
pattern completion.

10.3     Network Architecture and Dynamics
Consider a Hopfield network with N neurons. The state vector is s =
(s1 , s2 , . . . , sN )T , where each si ∈ {+1, −1}. The symmetric weight matrix
W = [wij ] satisfies wij = wji and wii = 0. Throughout this discussion wij
denotes the weight applied to state sj when computing the input to neuron i,
so column indices correspond to presynaptic neurons.
      The local field or input energy to neuron i is defined as

                                          X
                                          N
                               hi (t) =         wij sj (t).                  (10.3)
                                          j=1


The scalar hi (t) therefore represents the total input (or local field) accumulated
at neuron i before thresholding during iteration t.
    The neuron updates its state according to the sign of hi (t) relative to a




                                          206
Modern Intelligent Systems                                                                  10


threshold θi :                            
                                          +1,     hi (t) ≥ θi ,
                         si (t + 1) =                                                (10.4)
                                          −1,     hi (t) < θi ,

   Typically, thresholds θi are set to zero or learned as part of the model.

Interpretation: The neuron ”fires” (state +1) if the weighted sum of inputs
exceeds the threshold; otherwise, it remains ”off” (state −1). This binary up-
date rule contrasts with the continuous activation functions used in feedforward
networks.

10.4    Encoding conventions
Two binary encodings are common. We primarily use si ∈ {−1, +1} because it
simplifies the energy function, but many software libraries work with xi ∈ {0, 1}.
Define s = 2x − 1 and x = (s + 1)/2; then

                                         1X             X
                       E±1 (s) = −          wij si sj +   θi s i
                                         2
                                           i̸=j            i


and
                                 1X ′          X
                   E01 (x) = −     wij xi xj +   θi′ xi + const,
                                 2
                                  i̸=j                i
      ′ = 4w and θ ′ = 2θ + 2
                                         P
with wij      ij      i     i        j̸=i wij under the sign convention in E±1 .
The additive constant does not affect which states minimize the energy or the
update dynamics. This table summarizes the correspondence:

                                 {−1, +1} encoding                 {0, 1} encoding
  State variable                 si ∈ {−1, +1}                     xi = (si + 1)/2
  Energy                         E±1 (s)                           E01 (x) = E±1 (2x − 1)
  Update rule                    si ← sign(hi − θi )               xi ← 1[h′i − θi′ > 0]

    Whenever an equation later in the chapter uses si you can translate it to xi
via this aﬀine mapping; we call out both forms only when the distinction matters.
As a concrete example, the pattern x = [1, 0, 1, 0] in the {0, 1} encoding maps
to s = 2x − 1 = [+1, −1, +1, −1]; conversely s = [−1, +1, +1] corresponds to
x = [0, 1, 1].

                                             207
Modern Intelligent Systems                                                          10


10.5    Energy Function and Stability
Hopfield defined an energy function E : {−1, +1}N → R associated with the
network state s:
                              1 XX                X
                                N N               N
                     E(s) = −         wij si sj +   θi s i .        (10.5)
                              2
                                    i=1 j=1           i=1

Because the weights are symmetric and satisfy wii = 0, the double sum may
                           P
equivalently be written as i<j wij si sj ; the 21 factor explicitly prevents count-
ing each unordered pair twice, so removing it would scale the energy by two.
                                                                            P
Thresholds θi act like biases; many texts write the second term as − i bi si
with bi = θi .

10.6    Hopfield Network States and Energy Function
Recall that in Hopfield networks, the state of each neuron is typically binary, ei-
ther ±1 or 0/1. The network is characterized by symmetric weights wij between
neurons and possibly thresholds θi . The energy function E of the network is
defined to capture the ”stability” of a given state vector s = (s1 , s2 , . . . , sN ).

Energy function for ±1 states: When states are bipolar, si ∈ {−1, +1},
and thresholds are zero, the energy is given by

                                  1 XX
                                        N     N
                              E=−      wij si sj .                              (10.6)
                                  2
                                        i=1 j=1


If thresholds θi are nonzero, the energy generalizes to

                                1 XX             X
                                   N   N              N
                        E=−          wij si sj +   θi s i .                     (10.7)
                                2
                                  i=1 j=1            i=1


Energy function for {0, 1} states: When neuron states take values in {0, 1},
we denote them by xi to avoid overloading si . Recenter via si = 2xi − 1, so that
si ∈ {−1, +1}. Substituting this into (10.7) yields an equivalent expression




                                           208
Modern Intelligent Systems                                                     10


written directly in terms of the {0, 1} variables:

                    1 XX                          X
                      N      N                        N
            E=−          wij (2xi − 1)(2xj − 1) +   θi (2xi − 1).          (10.8)
                    2
                      i=1 j=1                         i=1


Some references drop the 21 factor when working with {0, 1} states, but doing
so merely rescales the energy because symmetry still causes every pair (i, j) to
appear twice; we retain the factor to avoid double counting. The recentering
view also clarifies that the dynamical behavior is the same under either encoding.
One simply interprets 0 and 1 as the inactive/active states instead of −1 and
+1.

10.7    Energy Minimization and Stable States
The fundamental goal in Hopfield networks is to find a state s that minimizes
the energy E. Such states correspond to stable equilibria or attractors of the
network dynamics.

State update dynamics: The network updates neuron states according to
                                                      
                                     X
                                     N
                 si (t + 1) = sign    wij sj (t) − θi  ,       (10.9)
                                         j=1


where sign(·) returns +1 for positive inputs and −1 otherwise (or applies the
corresponding threshold for {0, 1} encodings).




                                       209
Modern Intelligent Systems                                                      10


 Asynchronous Hopfield update (pseudo-code)

    1. Initialize s (e.g., noisy probe), set max sweeps T .

    2. For t = 1, . . . , T :

        (a) Pick a neuron index i (random order or cyclic sweep).
                           P
        (b) Compute hi = j wij sj − θi .
         (c) Update si ← sign(hi ).

    3. Stop early if a full sweep causes no flips; else continue.
 Each single-neuron update satisfies ∆E ≤ 0 by (10.15), so the loop
 converges to a local minimum of (10.11).

    When neurons are updated asynchronously (one at a time) in any order,
each step is guaranteed not to increase the energy E, ensuring convergence to a
local minimum. Random or cyclic update orders satisfy the classic convergence
conditions (any single flip obeys ∆E ≤ 0 by Equation (10.15)). Synchronous
updates of all neurons, by contrast, can oscillate and are discussed in more detail
in Section 10.10.

10.8   Example: Energy Calculation and State Updates
Consider a Hopfield network with three neurons, bipolar states si ∈ {−1, +1},
zero thresholds, and the symmetric weight matrix
                                            
                                       0 3 −4
                                            
                                W =  3 0 2 .
                                      −4 2 0

   Let the initial state be s = (1, 1, −1). Using the energy definition with the
1
2 factor to avoid double counting, we obtain


            1 XX
                  3   3
   E(s) = −           wij si sj
            2
              i=1 j=1
            1h                                                   i
        = − 2 · 3 · (1)(1) + 2 · (−4) · (1)(−1) + 2 · 2 · (1)(−1) = −5.    (10.10)
            2



                                          210
Modern Intelligent Systems                                                              10


State update attempts:          Flip each neuron in turn and recompute the energy:
   • Flip s1 to −1: E(−1, 1, −1) = 9 (energy increases).

   • Flip s2 to −1: E(1, −1, −1) = −3 (energy increases toward zero).

   • Flip s3 to +1: E(1, 1, 1) = −1 (energy increases).
   For clarity, Table 4 reports the energy change for each single flip relative to
the current state.

                      Flip          New state      ∆E      Accept?
                      s1 ← −1      (−1, 1, −1)     +14         No
                      s2 ← −1      (1, −1, −1)     +2          No
                      s3 ← +1        (1, 1, 1)     +4          No

Table 4: Single-neuron flips from (1, 1, -1); all raise the energy, so the state is a local
    minimum. Use it when checking stability of a stored pattern under single-bit
                                   perturbations.


    Because every single-neuron flip raises the energy, the state (1, 1, −1) is a
stable local minimum for this network. If the network is perturbed slightly (for
instance, by flipping s3 to +1 to create the noisy pattern (1, 1, 1)), asynchronous
updates follow the gradient of decreasing energy and drive the system back to
the stored memory (1, 1, −1). This illustrates how Hopfield networks perform
content-addressable recall; the staircase energy trajectory in Figure 45 makes
the monotone descent concrete.

10.9    Energy Function and Convergence of Hopfield Networks
Recall that the Hopfield network is characterized by the energy in (10.5), re-
peated here for convenience:

                                 1 XX             X
                                      N    N              N
                        E(s) = −      wij si sj +   θi s i ,                       (10.11)
                                 2
                                      i=1 j=1            i=1


where wij are the symmetric weights (wij = wji ) and θi are the thresholds for
each neuron.




                                           211
Modern Intelligent Systems                                                                   10


                     0      noisy start s(0)

                    −2                                asynchronous single-neuron flips
             E(s)


                    −4

                    −6

                         s(0)                         s(1)                       s(2)
                                                Update step

     Figure 45: Hopfield energy decreases monotonically under asynchronous
    updates. Starting from a noisy probe state s(0), successive single-neuron flips
       move downhill until the stored memory s(2) is recovered. Use it when
     explaining why asynchronous updates converge under Hopfield’s symmetry
                                    constraints.


Goal: Show that asynchronous updates of neuron states always decrease (or
leave unchanged) the energy E, guaranteeing convergence to a local minimum.

10.9.1   Energy Change Upon Updating a Single Neuron
Consider updating neuron i from old state sold i  to new state snew
                                                                  i . All other
neuron states sj for j 6= i remain fixed. The change in energy is

                                    ∆E = Enew − Eold .                                   (10.12)

   Using (10.11), write out the energies explicitly:

                                1 XX              X
                                    N   N                       N
                     Eold = −        wkl sold old
                                          k sl +    θk sold
                                                        k ,                              (10.13)
                                2
                                    k=1 l=1                    k=1

                                1 XX                            X
                                  N N                            N
                     Enew = −                  wkl snew
                                                    k sl
                                                        new
                                                            +          θk snew
                                                                           k .           (10.14)
                                2
                                    k=1 l=1                      k=1

   Since only si changes, and weights are symmetric with zero diagonal wii = 0,




                                                212
Modern Intelligent Systems                                                          10


the difference simplifies to

               ∆E = Enew − Eold
                          1X
                               N
                    =−       (wij snew
                                   i   sj + wji sj snew
                                                    i   ) + θi snew
                                                                i
                          2
                              j=1

                          1 X                            
                               N
                      +        wij sold
                                    i   s j + w   s s
                                                ji j i
                                                      old
                                                            − θi sold
                                                                  i
                          2
                              j=1

                          X
                          N                                              
                    =−          wij sj snew
                                        i   − s old
                                                i     + θ i   s new
                                                                i   − s old
                                                                        i
                          j=1
                                                                    
                                                  X
                                                    N
                    = − snew
                         i   − sold
                                i
                                                         wij sj − θi  .       (10.15)
                                                    j=1


   Define the local field hi at neuron i as

                                            X
                                            N
                                     hi =         wij sj − θi .                 (10.16)
                                            j=1

   Then,
                                   ∆E = −(snew
                                           i   − sold
                                                  i )hi .


Numeric check (single flip). With two neurons, weights w12 = w21 = 1,
thresholds θi = 0, and current state (s1 , s2 ) = (1, −1), the local field at neuron
1 is h1 = 1 · (−1) = −1. The update rule sets snew      1    = sign(h1 ) = −1, so
 new    old
s1 − s1 = −2 and ∆E = −(−2)(−1) = −2 < 0, confirming the energy drop
predicted by (10.15).




                                                213
Modern Intelligent Systems                                                    10


  Modern Hopfield views and attention
  Recent work (Krotov and Hopfield, 2016, 2020; Ramsauer et al., 2021)
  revisits Hopfield networks as dense associative memories with continuous
  states and softmax interactions that are closely related to Transformer
  attention. In this view the stored patterns play the role of keys and values,
  the current state or query probes the landscape, and the update rule
  resembles a softmax-weighted average over memories, minimizing an energy
                  P               
  of the form log µ exp βs⊤ mµ with inverse temperature β. While this
  book does not develop the full modern Hopfield formalism, it is helpful to
  remember that the energy function in (10.11) already anticipates ideas that
  reappear in the attention mechanisms of Chapter 14.


Continuous Hopfield / dense associative memory. Modern extensions
replace the binary sign activation with a smooth, often softmax-like update
that keeps neuron states continuous. Storing P real-valued patterns {mµ }, the
update becomes                                   
                        s(t+1) = softmax βM ⊤ s(t) M,

where M stacks the memory vectors and β controls sharpness. This view uni-
fies classical Hopfield dynamics, associative memories used in few-shot meta-
learning, and attention heads in Transformers: all minimize a convex energy
    P               
log µ exp βs⊤ mµ and pull the state toward a convex combination of stored
patterns. Continuous updates are differentiable (enabling end-to-end training),
offer higher storage capacity via richer nonlinearities, and connect directly to
“dense associative memory” results in the modern literature.

10.9.2   Update Rule and Energy Decrease
The neuron update rule is
                                             
                                             +1   hi > 0,
                        snew = sign(hi ) =                               (10.17)
                         i
                                             −1   hi < 0.
```

### Findings
Issues found in Chunk 15/31:

1. **Notation inconsistency in SOM convergence conditions:**
   - The conditions for SOM convergence are stated as:
     \[
     \sum_t \alpha(t) = \infty, \quad \sum_t \alpha^2(t) < \infty,
     \]
     but the text writes:
     \[
     t \alpha(t) = \infty, \quad t \alpha^2(t) < \infty,
     \]
     which is ambiguous and nonstandard. The standard Robbins-Monro conditions require the sums over \(t\), not products. This should be clarified to:
     \[
     \sum_{t=1}^\infty \alpha(t) = \infty, \quad \sum_{t=1}^\infty \alpha^2(t) < \infty.
     \]

2. **Ambiguous phrase "magnification factor" in TE definition:**
   - The text states:
     > Topographic error (TE): fraction of inputs whose first- and second-best BMUs are not adjacent, quantifying topology preservation (magnification factor).
   
   - The "magnification factor" is a distinct concept in SOM literature related to neuron density vs data density, not directly the same as TE. This conflation may confuse readers. It would be better to separate these concepts or clarify that TE measures topology preservation, while magnification factor relates to neuron density distribution.

3. **Inconsistent or unclear notation in energy function definitions:**
   - Equation (10.5) and subsequent energy definitions use sums over all \(i,j\) with a factor \(\frac{1}{2}\) to avoid double counting. However, the text sometimes writes the double sum over all pairs and sometimes over \(i<j\), which can confuse readers.
   - For clarity, it is better to consistently write:
     \[
     E(s) = -\sum_{i<j} w_{ij} s_i s_j - \sum_i \theta_i s_i,
     \]
     or explicitly state the factor \(\frac{1}{2}\) when summing over all pairs.

4. **Typo or formatting error in weight matrix example:**
   - The weight matrix \(W\) is given as:
     \[
     W = \begin{bmatrix}
     0 & 3 & -4 \\
     3 & 0 & 2 \\
     -4 & 2 & 0
     \end{bmatrix}
     \]
     but the matrix is shown with the last row starting with \(-4\) and the last element 0, which is correct, but the formatting in the text is confusing (the matrix is split across lines with inconsistent indentation). This should be typeset clearly.

5. **Energy calculation in example (10.10) is confusing:**
   - The calculation:
     \[
     E(s) = -\frac{1}{2} \sum_{i,j} w_{ij} s_i s_j = -\frac{1}{2} [2 \cdot 3 \cdot (1)(1) + 2 \cdot (-4) \cdot (1)(-1) + 2 \cdot 2 \cdot (1)(-1)] = -5,
     \]
     is not clearly explained. The factor 2 appears without explanation (it comes from symmetry, counting pairs twice). This should be explicitly stated to avoid confusion.

6. **In the numeric check for energy change (10.15), the sign of \(\Delta E\) is negative but the text says "energy drop predicted by (10.15)".**
   - The numeric example computes \(\Delta E = -2 < 0\), which is correct, but the explanation could be clearer by explicitly stating that negative \(\Delta E\) means energy decreases, confirming convergence.

7. **In the "Modern Hopfield views and attention" paragraph, the notation is garbled:**
   - The expression:
     \[
     \log \sum_\mu \exp \beta s^\top m_\mu
     \]
     is written with strange symbols:
     \[
     \log \mu \exp \beta s^\top m_\mu
     \]
     and
     \[
     P \quad \text{and} \quad \sum_\mu
     \]
     are mixed with strange characters like \(P\), \(\), and \(\).
   - This appears to be a formatting or OCR error and should be corrected for clarity.

8. **In the continuous Hopfield update formula:**
   \[
   s(t+1) = \text{softmax}(\beta M^\top s(t)) M,
   \]
   the dimensions and operations are not fully explained. Since \(M\) stacks memory vectors, the multiplication order and shapes should be clarified to avoid confusion.

9. **In the update rule (10.17), the case \(h_i = 0\) is not specified:**
   - The sign function is defined for \(h_i > 0\) and \(h_i < 0\), but the behavior at \(h_i = 0\) is not stated. This is a minor but important detail for reproducibility.

---

No other concrete mathematical or internal consistency issues were found. The explanations are generally correct and consistent with standard Hopfield network theory and SOM convergence theory.

---

**Summary:**

- Fix notation for SOM convergence conditions.
- Clarify distinction between topographic error and magnification factor.
- Consistently define energy sums and avoid ambiguous double counting.
- Correct formatting and explanation in example calculations.
- Fix garbled notation in modern Hopfield/attention paragraph.
- Clarify continuous Hopfield update formula.
- Specify sign function behavior at zero input.

---

If these are addressed, the chunk is mathematically sound and internally consistent.

## Chunk 16/31
- Character range: 426923–455580

```text
Note that snew
              i   ∈ {−1, +1}, and sold
                                   i ∈ {−1, +1}.
   Consider two cases:



                                      214
Modern Intelligent Systems                                                   10


  • Case 1: snew
             i   = sold
                    i . Then ∆E = 0, so the network state is unchanged.

  • Case 2: snew
             i   6= sold
                     i . Substituting into (10.17) gives
                                                   
                                    X
                                    N
                      ∆E = −2            wij sj − θi  (snew
                                                          i   − sold
                                                                 i ).
                                    j=1


     Because the update chooses the sign of snew
                                             i   to agree with the bracketed
     term, ∆E ≤ 0, ensuring the energy never increases.

10.10 Asynchronous vs. Synchronous Updates in Hopfield Net-
      works
Recall from the previous discussion that the Hopfield network energy function
decreases monotonically with each asynchronous update of a single neuron state.
This guarantees convergence to a local minimum of the energy landscape. In
contrast, fully synchronous updates (flipping all neurons at once) can lead to
oscillations or short cycles rather than convergence, which is why the classical
convergence proofs assume asynchronous updates.

Why asynchronous updates? Suppose we attempt to update multiple neu-
ron states simultaneously (synchronously). Consider a simple example with two
neurons having states s1 , s2 ∈ {+1, −1} and weights w12 = w21 = 10. The
energy function is:
                                    1X
                              E=−        wij si sj .
                                    2
                                           i,j

   If both neurons are updated simultaneously, the energy can oscillate rather
than decrease monotonically. For instance:
  • Current state: s1 = +1, s2 = +1, energy E = −20.

  • Flip both states simultaneously to s1 = −1, s2 = −1, energy E = −20.

  • Flip back to s1 = +1, s2 = +1, energy E = −20.
This leads to oscillations without convergence.

Conclusion: To ensure convergence, updates must be asynchronous and se-
quential, updating one neuron at a time and respecting an update order. Revis-


                                          215
Modern Intelligent Systems                                                    10


iting states before all others have been updated can cause instability.

10.11 Storage Capacity of Hopfield Networks
A key question is: How many memories can a Hopfield network reliably store
and recall?

Classical result: For a network of n neurons, the number of random patterns
p that can be stored with low error is approximately

                                  p ≈ 0.138 n,

which is a small fraction of the total number of neurons (McEliece et al., 1987).
This means the storage capacity scales linearly but with a small proportionality
constant; both ξ µ and its complement −ξ µ are fixed points, and odd mixtures
of stored patterns become spurious states as p/n grows.

Ineﬀiciency: This low capacity is why Hopfield networks are not used as prac-
tical storage devices despite their associative memory properties.

Stochastic updates (bridge to Boltzmann machines). A stochastic vari-
ant replaces the hard sign in (10.17) with probabilistic flips (e.g., Gibbs sam-
pling). With symmetric weights this defines a Boltzmann distribution whose
energy matches (10.11), linking Hopfield recall to the Boltzmann/energy-based
models that underlie modern probabilistic neural networks.

10.12 Improving Storage Capacity via Weight Updates
Is it possible to improve the storage capacity by modifying the weight update
rule?

Idea: Instead of fixing weights and updating states, can we update weights
based on stored patterns to better encode memories?




                                      216
Modern Intelligent Systems                                                    10


Hebbian learning rule: Given p stored patterns {b1 , b2 , . . . , bp }, each bµ =
(bµ1 , bµ2 , . . . , bµn ) with bµi ∈ {+1, −1}, the weights are set by:

                                   1X µ µ
                                     p
                             wij =   bi bj ,    wii = 0.                  (10.18)
                                   n
                                    µ=1


   This is the classical Hebbian learning rule for Hopfield networks.

Properties:
   • The diagonal terms wii are set to zero to avoid self-feedback.

   • The factor n1 normalizes the weights.

   • The weights encode correlations between neuron activations across stored
     patterns.

Effect on capacity: Using this weight update rule, the network can store
on the order of 0.138n random patterns reliably, which is an improvement over
naive storage but still limited.

10.13 Example: Weight Calculation for a Single Pattern
Consider a fundamental memory pattern:

                                 b = (1, 1, 1, −1),

with no thresholds (θi = 0).

Step 1: Compute outer product Form the matrix B = bb⊤ . Each entry
Bij = bi bj captures the pairwise correlation between neurons i and j.

Step 2: Remove diagonal terms Zero the diagonal entries to obtain the
weight matrix W with wii = 0. The off-diagonal values remain the same as in
B, encoding the pairwise interactions required to store the memory pattern.




                                          217
Modern Intelligent Systems                                                     10


10.14 Finalizing the Hopfield Network Derivation and Discus-
      sion
Recall from previous parts that the Hopfield network is a fully connected re-
current neural network designed to store and retrieve binary memory patterns
ξ µ ∈ {−1, +1}N , µ = 1, . . . , P , where N is the number of neurons and P the
number of stored patterns.
    The weight matrix W = [wij ] is typically constructed using the Hebbian
learning rule:

                                   1 X µ µ
                                      P
                             wij =    ξi ξj ,          wii = 0,           (10.19)
                                   N
                                     µ=1


where the diagonal weights are set to zero to avoid self-feedback.

Energy Function and Convergence The network dynamics evolve asyn-
chronously or synchronously according to the update rule:
                                                     
                                          X
                                          N
                      si (t + 1) = sign    wij sj (t) , (10.20)
                                                 j=1


where si (t) ∈ {−1, +1} is the state of neuron i at time t.
   The Hopfield network is equipped with an energy function:

                                        1 X
                                             N
                               E(s) = −     wij si sj ,                   (10.21)
                                        2
                                            i,j=1


which monotonically decreases (or remains constant) with each asynchronous
update, guaranteeing convergence to a local minimum of E.

Memory Retrieval and Basins of Attraction The stored patterns {ξ µ }
correspond to local minima of the energy landscape. Starting from an initial
state s(0) that is a noisy or partial version of a stored pattern, the network
dynamics converge to the closest attractor, ideally retrieving the original memory
or its complement −ξ µ .
    For example, if the initial state is corrupted, the network will iteratively


                                           218
Modern Intelligent Systems                                                  10


update states to reduce energy until it reaches a stable point:

                               s(∞) ∈ {ξ µ , −ξ µ }.

Limitations: Capacity and Classification Despite its elegant memory re-
trieval properties, the Hopfield network has significant limitations:
  • Storage Capacity: The maximum number of patterns Pmax that can be
    reliably stored and retrieved scales approximately as 0.138N for large N .
    Beyond this, spurious minima and retrieval errors increase dramatically.

  • Spurious States: The network may converge to spurious attractors that
    are not stored memories, especially when the number of stored patterns is
    large or when the input is heavily corrupted.

  • Classification Diﬀiculty: Using Hopfield networks for classification (e.g.,
    digit recognition) is problematic. Since the network converges to the near-
    est energy minimum, a corrupted input pattern may converge to a wrong
    stored pattern or its complement. There is no guarantee that the minimum
    energy state corresponds to the correct class.

  • When not to use: Large patterns and heavy loading (P/N ) create a
    glassy energy landscape, scaling is quadratic in the number of units, and
    low capacity makes Hopfield networks ill-suited for high-dimensional dis-
    criminative tasks compared with the ERM models from Chapter 4 or deep
    models in Chapter 14.

Example: Memory Recovery Consider a Hopfield network with N = 4
neurons and a single stored pattern ξ = [−1, −1, 1, −1]T . The weight matrix
constructed via (10.18) is

                                1
                             W = ξξ ⊤ ,       wii = 0,
                                4




                                       219
Modern Intelligent Systems                                                         10


which numerically becomes a single symmetric matrix
                                        
                                0 1 −1 1
                            11  0 −1 1 
                                         
                          W=            .
                            4 −1 −1 0 −1
                               1  1 −1 0

The off-diagonal entries are therefore the scaled products of pattern components
(e.g., w12 = w21 = 0.25 and w13 = w31 = −0.25). Thus every off-diagonal
weight is simply the scaled product of the corresponding pattern entries, e.g.,
w12 = w21 = 0.25, w13 = w31 = −0.25, and so on.
    Starting from an initial state s(0) = [−1, −1, 1, 1]T (with zero thresholds
θi = 0), we apply the familiar asynchronous sign update

                                         X
                                          N                  
                             si ← sign         wij sj − θi
                                         j=1

one neuron at a time, i.e., neuron i is set to +1 whenever the weighted sum
exceeds its threshold and to −1 otherwise. Because each update reduces the
                             P PN                    PN
Lyapunov energy E = − 21 N      i=1  j=1 wij si sj +  i=1 θi si from (10.11), the tra-
jectory converges to ξ or its complement −ξ, demonstrating successful memory
retrieval despite the initial corruption. The appearance of −ξ as a fixed point is
expected: the energy only depends on products si sj , so negating all bits leaves
every term unchanged.

Spurious attractors Beyond the intended memories {±ξ µ }, Hopfield net-
works can converge to spurious attractors: stable states formed by mixtures of
stored patterns. These unintended minima become increasingly common as the
loading factor P/N grows (here P denotes the number of stored patterns); for
random patterns the practical capacity is roughly 0.138 N . The possibility of
converging to a spurious state, or to the complemented memory rather than
the original, explains why Hopfield networks are better viewed as associative
memories than as discriminative classifiers.

Historical and Practical Significance The Hopfield network was revolu-
tionary in demonstrating that artificial neural networks can model associative

                                         220
Modern Intelligent Systems                                                    10


memory and converge to stable states corresponding to stored memories. It laid
foundational concepts for energy-based models and inspired subsequent develop-
ments in neural computation.
    However, its practical use is limited by low storage capacity and sensitivity
to noise. Modern networks and learning algorithms have since extended these
ideas to more scalable and robust architectures.

Connections to other chapters. Hopfield networks sit between prototype-
based maps and energy-based attention mechanisms. Chapter 9 and Chap-
ter 14 provide those contexts. Their Lyapunov-style energy descent mirrors
the validation-driven convergence checks from Chapter 3. Their symmetric re-
current structure also offers a counterpoint to the feedforward ERM models in
Chapters 4 to 7.




                                      221
Modern Intelligent Systems                                                     10


 Key takeaways
    • Hopfield networks store binary patterns as attractors in an energy
      landscape defined by symmetric weights.

    • Asynchronous updates monotonically reduce the Lyapunov energy,
      ensuring convergence to a fixed point.

    • Capacity is limited and spurious attractors appear as the load P/N
      grows; treat Hopfield nets primarily as associative memories.

 Minimum viable mastery.
    • Write the energy E(s), state the symmetry condition W = W ⊤ with
      zero diagonal, and explain why asynchronous updates decrease E.

    • Distinguish true memories from spurious attractors, and connect
      failure modes to loading P/N and correlation among stored patterns.

    • Use overlap and energy traces as diagnostics when demonstrating
      recall under corruption.
 Common pitfalls.
    • Using asymmetric weights or nonzero self-connections (breaks the
      standard energy argument).

    • Overloading the network and expecting clean recall (spurious minima
      dominate).

    • Reporting a single cherry-picked recall trajectory instead of multiple
      corruption levels and multiple stored sets.




                                     222
Modern Intelligent Systems                                                    11


 Exercises and lab ideas
     • Implement a minimal example from this chapter and visualize
       intermediate quantities (plots or diagnostics) to match the
       pseudocode.

     • Stress-test a key hyperparameter or design choice discussed here and
       report the effect on validation performance or stability.

     • Re-derive one core equation or update rule by hand and check it
       numerically against your implementation.

 If you are skipping ahead. The key transferable idea is the combination
 of a state update rule with a scalar quantity that tracks progress (energy,
 loss, or validation curves). That mindset carries into deep training in
 Chapters 6 to 11.



Where we head next. Chapter 11 turns from associative memory to deep
feedforward perception, where convolution and pooling form hierarchical fea-
tures. The optimization workflow is unchanged: the ERM toolkit from Chapter 3
and the training mechanics from Chapters 6 to 7 remain central. Recurrence
and attention return in Chapter 12 and Chapter 14.


11    Convolutional Neural Networks and Deep Train-
      ing Tools
Chapter 10 used energy to make recurrence stable: dynamics settle, memories
persist, and failure has a concrete signature. Vision problems have a different
flavor. The system must form a representation that is rich enough to support
decisions, yet structured enough to learn from finite data.
    Convolutional networks are the simplest version of that bargain. They keep
the ERM workflow from Chapters 3 to 4 and the gradient-training machinery
from Chapter 6, but move a large fraction of the “modeling bias” into architec-
ture. Local connectivity and weight sharing make images tractable: the model
spends capacity on patterns that actually recur across a grid.
    The second thread in this chapter is pragmatic. Deep models are only useful


                                     223
Modern Intelligent Systems                                                        11


when they train. After the CNN mechanics, we transition into the deep-training
toolkit (initialization, activations, normalization, regularization, and optimizers)
that will reappear in Chapters 12 to 14.
  Learning Outcomes
 After this chapter, you should be able to:
     • Derive convolution/cross-correlation with stride and padding in
       1D/2D.

     • Explain receptive-field growth across layers and pooling effects.

     • Compare loss choices for classification vs. regression and evaluation
       metrics.

     • Connect the hinge-loss/soft-margin ideas from Chapter 3 to kernels
       and CNN features.

     • Describe practical optimizers and regularizers (BN, dropout, weight
       decay).

  Design motif
  Keep the same statistical learning loop from Chapters 3 to 4, but move a
  large fraction of the “bias” into architecture via weight sharing and locality.


11.1    Motivation and map
The core backprop loop from earlier chapters scales to high-dimensional percep-
tion tasks, but naively applying dense multilayer perceptrons (MLPs) to images
runs into two practical walls: parameter count and inductive bias. Images have
strong local structure (edges, corners, textures), yet a fully connected layer treats
every pixel as unrelated to its neighbors and spends parameters learning spatial
patterns from scratch.
    In practice, this is also where “deep learning” stopped being a promise and
became a reliable workflow: large datasets and modern accelerators made the
iterative training loop feasible, while architectural priors such as locality and
weight sharing made that loop data-eﬀicient on image grids.
    CNNs emerged as a pragmatic answer: keep end-to-end gradient training,
but bake in locality and translation structure through sparse connectivity and

                                        224
Modern Intelligent Systems                                                       11


shared weights. The result is a model class that is both more sample-eﬀicient
and more computationally viable on large grids.

How to read this chapter.
   • Core thread (CNNs): why locality + weight sharing → convolu-
     tion/pooling mechanics → channels/feature maps → end-to-end classifiers.

   • Going deeper: why depth works (receptive-field growth) and how CNNs
     displaced classical pipelines at scale.

   • Training toolkit: gradient-based optimization and the stabilizers you
     will reuse later (initialization, activations, batch norm, dropout, AdamW).

11.2   Why fully connected layers break on images
Requirement for large datasets Dense feedforward networks can be com-
petitive on small tabular problems, but on images they become data-hungry fast:
you are trying to learn spatial structure from scratch while fitting millions of pa-
rameters. The issue is not that the model class is “wrong”; it is that the sample
complexity and compute burden are badly mismatched to the grid structure of
vision data.

High-dimensional inputs and flattening Consider image data, which is
naturally represented as a 2D matrix (or 3D tensor for color images). For exam-
ple, a single-channel (grayscale) image of size 256×276 pixels can be represented
as a matrix:
                                   X ∈ R256×276 .

    To input this into a traditional feedforward network, the image must be
flattened into a vector:
                            x = vec(X) ∈ R70,656 ,

where 70, 656 = 256 × 276 is the total number of pixels.
   This flattening process has two major drawbacks:
   • Loss of spatial structure: The 2D spatial relationships between pixels
     are ignored, which is critical for tasks like image recognition.




                                       225
Modern Intelligent Systems                                                   11


  • High dimensionality: The input vector becomes very large, increasing
    the number of parameters and computational cost, and requiring more
    data to train effectively.

Implications The punchline is not that dense networks “cannot” learn images;
it is that the price is too high. Without any architectural prior, you pay in
parameters, data, and compute. Convolutions and pooling supply that prior:
they make the model spend capacity on local patterns and reuse those patterns
across the grid.

Parameter Explosion          The number of weights between the input and hidden
layer is:
                             70, 656 × 100 = 7, 065, 600,                 (11.1)

and between the hidden and output layer (assuming 4 output classes) is:

                                   100 × 4 = 400.                         (11.2)

   Thus, the first layer alone requires learning just over 7 million parameters
before we even consider deeper architectures. Coupled with the additional 400
output weights (plus biases), the optimization problem quickly becomes data-
hungry and computationally expensive.

Data Requirements To reliably learn these parameters, the amount of train-
ing data must be suﬀiciently large. A common heuristic is that the number of
training samples should be at least 10 times the number of parameters:

                             Nsamples ≥ 10 × Nparameters .                (11.3)

    This rule-of-thumb is intentionally conservative and should be read as guid-
ance rather than a hard requirement; in practice, regularization, data augmenta-
tion, and strong inductive biases often permit useful models with fewer samples.
    For the first layer, this implies roughly:

                   Nsamples ≳ 10 × 7, 000, 000 ≈ 70, 000, 000,            (11.4)




                                         226
Modern Intelligent Systems                                                     11


meaning on the order of seventy million labeled images. This is an impractical
requirement for most projects.

Computational and Storage Constraints Storing and processing such a
large dataset requires enormous storage and computational resources. Training
on hundreds of millions of images is typically infeasible for most research groups
or applications without specialized infrastructure.

Overfitting Risk With millions of parameters, the model has high capacity
and can easily memorize the training data, leading to overfitting. This means
the network may not generalize well to unseen data, as it learns to fit noise or
irrelevant details rather than meaningful features.

11.3   Sparse connectivity and parameter sharing
CNNs replace dense connections with local receptive fields. Each output unit
connects to a small neighborhood of pixels, not the entire image. If a k × k
filter scans a H × W input, the number of learned weights is k 2 (per channel),
not HW . The same filter is reused at every spatial location, so a single set of
parameters detects a pattern anywhere in the image. This parameter sharing
is the key to scalability: it cuts the parameter count and preserves translation
equivariance.
     Historically, dense MLPs on image benchmarks struggled to compete with
classical pipelines because the parameter count and data requirements were pro-
hibitive. CNNs reversed that trend by tying weights and focusing on local pat-
terns while keeping the same gradient-based training loop, so capacity grows
with depth and channel count rather than with the raw pixel grid.
 Shape reminder
 Throughout this chapter we use the row-major (deep-learning) convention
 for batches: inputs X ∈ RB×din , weights W ∈ Rdin ×dout , and biases
 b ∈ Rdout , with forward map Z = XW + 1b⊤ . When we write
 single-example equations, you can read them as the same convention with
 B = 1. For convolution/cross-correlation we follow the standard
 deep-learning tensor convention (channels and spatial axes); the same
 shape logic applies once the tensors are flattened into matrix form.


                                       227
Modern Intelligent Systems                                                      11


Notation handoff. Here σ(·) is used only as an activation nonlinearity, while
earlier statistical chapters use σ 2 for variance. Keep Appendix D nearby when
moving between probability and deep-learning sections.

11.4   Convolution and pooling mechanics
For an input feature map X and filter K, the (cross-correlation) output at spatial
location (i, j) is
                                    X
                                    k−1 X
                                        k−1
                      (X ∗ K)ij =           Kuv Xi+u, j+v .
                                    u=0 v=0

 Author’s note: “convolution” vs. cross-correlation
 In most deep-learning libraries, the operation called “convolution” is
 technically cross-correlation: the kernel is not flipped before sliding. The
 name stuck because the two operations differ only by a reversal of the
 kernel, and the kernel is learned anyway. What matters in practice is that
 the “filter” is a small learned weight matrix that is applied repeatedly
 across space (weight sharing). Learn the shapes, the stride/padding
 bookkeeping, and the inductive bias; the terminology is imperfect but the
 idea is powerful.

   With stride s and padding p, the output size along one axis is
                                        
                              n + 2p − k
                                           + 1,
                                   s

so padding controls resolution while stride controls downsampling. Pooling then
aggregates local neighborhoods (typically max or average) to build invariance
and further reduce spatial size.
    Convolution itself is a linear map; the nonlinearity enters when we apply
an activation after each convolutional block. Stacking these linear–nonlinear
stages yields hierarchical feature detectors (edges → textures → parts → objects)
without abandoning the backprop training machinery.
    Without padding (often called valid convolution), boundary pixels partic-
ipate in fewer receptive fields and the spatial grid shrinks each layer. Same
padding chooses p = (k − 1)/2 for odd k to preserve spatial size when s = 1 and
give edge pixels comparable influence. Larger strides reduce resolution and com-


                                       228
Modern Intelligent Systems                                                      11


pute but can skip fine detail, so the padding/stride combination is a deliberate
trade-off rather than a fixed rule.

11.4.1    Worked stride and padding example
Suppose an input is 6 × 6 and the filter is 3 × 3.
  • Stride s = 1, valid padding (p = 0). Output size is (6 − 3)/1 + 1 = 4,
    so you get a 4 × 4 feature map.

  • Stride s = 2, valid padding. Output size is b(6 − 3)/2c + 1 = 2, so you
    get a 2 × 2 feature map.

  • Stride s = 1, same padding. With k = 3, choose p = 1 so the output
    stays 6 × 6.
The floor in the formula is important: if (n + 2p − k) is not divisible by s, the
last partial window is dropped.

Convolutional hyperparameters (what you choose up front).
  • Filter size (k × k) and number of filters (Cout ).

  • Stride s and padding p (valid vs. same).

  • Activation function after each convolution.

  • Pooling type (max/average), window size, and stride (if pooling is used).

11.5     Pooling as nonparametric downsampling
Pooling reduces spatial size without learning new parameters: a max-pooling
window keeps the strongest activation; average pooling keeps the mean. This is
a nonparametric operation, so it can feel like “cheating” compared to learned
filters, yet it often improves robustness by discarding small shifts and noise. Max
pooling is the most common because it preserves the strongest feature response,
but average and even median pooling appear in specialized settings. In modern
CNNs, aggressive pooling is used sparingly; strided convolutions are a common
alternative when you want learned downsampling instead of a fixed aggregation.




                                       229
Modern Intelligent Systems                                                        11


 Author’s note: pooling is a design choice
 Pooling is not “more correct” than strided convolutions; it is a trade-off. If
 you want downsampling with learned weights, use stride. If you want a
 fixed local summary (often more stable early in training), max pooling is a
 reasonable default. Avoid padding in pooling unless you need spatial
 alignment with a parallel branch.
```

### Findings
No issues spotted.

## Chunk 17/31
- Character range: 455585–485305

```text
11.6    Channels and feature maps
Real inputs are multi-channel. An RGB image has three channels, so a k×k filter
is really k × k × Cin and produces one output map. A convolutional layer applies
Cout such filters, yielding a volume of feature maps with shape H × W × Cout .
This is why “same” padding refers to spatial dimensions only: channel depth is
set by the number of filters, not by padding.
  Dimensionality bookkeeping example
 Start with an input tensor of size 50 × 50 × 30. Apply 10 filters of size 3 × 3
 with stride 1 and valid padding. The spatial size becomes 50 − 3 + 1 = 48,
 so the output is 48 × 48 × 10. Apply 2 × 2 max pooling with stride 2: the
 spatial size becomes b(48 − 2)/2c + 1 = 24, so the pooled output is
 24 × 24 × 10. Flattening that volume yields 24 · 24 · 10 = 5760 features for a
 dense classifier.


From feature maps to classifiers. Stacks of convolutional and pooling lay-
ers produce a hierarchy of feature maps. A common design is to flatten the
final maps into a vector and pass them to a small dense classifier (often a soft-
max layer) that predicts the class label. Backpropagation updates both the
dense weights and the shared convolutional filters, so the feature extractor and
classifier are learned jointly.

Multi-branch convolution blocks (Inception idea). One practical variant
is to run multiple filter sizes in parallel (for example 1 × 1, 3 × 3, and 5 × 5) and
concatenate the resulting feature maps along the channel axis. This allows the
network to capture multi-scale patterns without committing to a single kernel
size. When branches must line up spatially, same padding is used to keep all


                                        230
Modern Intelligent Systems                                                           11



                                                after 1 layer

                                                after 2 layers

                                                after 3 layers




       Figure 46: Receptive field growth across depth. Even with small 3 × 3
    kernels, stacking layers expands the spatial context seen by deeper units. Use
             it when explaining why depth can replace very large kernels.


outputs the same height and width; pooling branches often pad for this alignment
even though pooling by itself is usually unpadded.
    At scale, this architectural prior became decisive once large labeled datasets
and GPU training matured: the sample-eﬀiciency and compute-eﬀiciency gap
versus classical kernel pipelines narrowed and then flipped in favor of deep con-
volutional stacks.

Stack depth versus receptive field. Stacking identical 3 × 3 filters still
grows the effective receptive field: each stage wraps a thicker box around the
original pixels, which explains why deep-but-narrow CNNs can capture wide
spatial context without enormous kernels even when individual kernels remain
small.
    Figure 46 provides the receptive-field intuition used in the depth discussion.
    With the architectural motivation in place, we now focus on how these models
are trained and why deep optimization remains delicate.

11.7    Training Neural Networks: Gradient-Based Optimization
Training neural networks involves minimizing a loss function L that measures
the discrepancy between the network output and the target. The parameters
(weights and biases) are updated iteratively using gradient descent or its variants.
    For a weight w, the update rule is

                                               ∂L
                                  w ←w−η          .                             (11.5)
                                               ∂w
where η is the learning rate.


                                         231
Modern Intelligent Systems                                                       11


                                                                   ∂L
Backpropagation and Gradient Computation The gradient ∂w              is com-
puted eﬀiciently using the backpropagation algorithm, which applies the chain
rule to propagate errors backward through the network layers.

Preview: why deep optimization needs extra care As depth grows, gra-
dient flow becomes fragile (vanishing/exploding gradients). The next sections
make that failure mode explicit and summarize the mitigation toolkit used in
modern CNN stacks.

Deep optimization challenges. Deep networks are diﬀicult to optimize be-
cause the objective is highly nonconvex and the gradient signal can be distorted
as it flows through many layers. We begin with the most basic pathology—
vanishing and exploding gradients—and then summarize practical mitigations.

11.8    Vanishing and Exploding Gradients in Deep Networks
Recall from the previous discussion that when training deep neural networks, the
backpropagation algorithm involves repeated multiplication of gradients through
many layers. This repeated multiplication can cause gradients to either vanish
(approach zero) or explode (grow exponentially large), leading to significant
training diﬀiculties.

Mathematical intuition Consider a deep network with L layers. Let
δW(ℓ) = ∇W(ℓ) L denote the gradient of the loss with respect to the weights at
layer ℓ. If we assume the weights are initialized identically and the derivative of
the activation function is approximately constant, then the gradient at the first
layer can be expressed schematically as:
                                                         
             δW(1) ≈ W (2) D(2) W (3) D(3) · · · W (L) D(L) δW(L) .          (11.6)

where W represents the weight matrix and f ′ is the derivative of the activation
function.
   Here W (ℓ) denotes the weight matrix connecting layers ℓ − 1 and ℓ, while
                        
D(ℓ) = diag f ′ (z (ℓ) ) collects the activation derivatives at layer ℓ. The product
therefore chains together Jacobians from layers 2 through L. If the spectral
norm (largest singular value) of each factor W (ℓ) D(ℓ) exceeds one, then kδW(1) k


                                        232
Modern Intelligent Systems                                                         11


grows exponentially with L, causing exploding gradients. Conversely, norms
less than one cause kδW(1) k to shrink exponentially, leading to vanishing gra-
dients.

Consequences
   • Exploding gradients: The gradient values become extremely large, caus-
     ing numerical instability and making the network parameters diverge dur-
     ing training.

   • Vanishing gradients: The gradient values approach zero, especially in
     early layers, preventing those weights from updating effectively. This stalls
     learning in the initial layers, limiting the network’s ability to learn hierar-
     chical features.

Example: Activation function derivatives Consider the sigmoid activa-
tion function σ(x) = 1+e1−x . Its derivative is:

                              σ ′ (x) = σ(x)(1 − σ(x)).

Note that σ ′ (x) approaches zero when σ(x) is near 0 or 1, i.e., when the neuron
output saturates. This saturation leads to very small gradients, exacerbating the
vanishing gradient problem. The derivative is maximized at σ(x) = 0.5, where
σ ′ (x) = 0.25, so repeatedly multiplying sigmoid derivatives can shrink gradients
roughly like 0.25L across L layers.

Notation note. In this chapter σ(·) always denotes the logistic sigmoid non-
linearity, whereas symbols such as σ 2 are reserved for variances in earlier statisti-
cal chapters; context (function of an argument vs. squared scalar) distinguishes
them.




                                        233
Modern Intelligent Systems                                                      11


 Training failure signatures (symptom → likely fixes)
    • Loss becomes NaN / diverges quickly: lower learning rate;
      check data normalization; add gradient clipping; verify BN statistics
      (or switch norm).

    • Training loss decreases but validation stalls: audit split
      hygiene (Chapter 3); add regularization (weight decay, dropout);
      strengthen augmentation; check shortcut features via slice tests.

    • Both training and validation improve slowly: revisit
      initialization and normalization; try momentum/AdamW; confirm the
      objective matches the metric you care about.

    • High accuracy but poor probability decisions: audit
      calibration (reliability/ECE) and re-threshold on held-out data rather
      than trusting raw scores (Chapter 4).


11.9    Strategies to Mitigate Vanishing and Exploding Gradients
Weight initialization Initializing weights carefully can help maintain gradi-
ent magnitudes within a reasonable range. Set var ≈ 1/n (fan-in n).
This stabilizes signals across layers. It underlies Xavier and He.

Choice of activation function Selecting activation functions whose deriva-
tives do not vanish easily is crucial. For example:
  • ReLU (Rectified Linear Unit): Defined as

                                 ReLU(x) = max(0, x),

       its derivative is 1 for positive inputs and 0 otherwise. This avoids satura-
       tion in the positive regime and helps maintain gradient flow.

  • Leaky ReLU and variants: These allow a small, non-zero gradient
    when the input is negative, further mitigating dead neurons and keeping
    derivatives away from exact zero.




                                        234
Modern Intelligent Systems                                                     11


Batch normalization Batch normalization normalizes layer inputs during
training, reducing the effective internal covariate shift and helping gradients
maintain stable magnitudes.

Gradient clipping For exploding gradients, gradient clipping limits the max-
imum gradient norm during backpropagation, preventing excessively large up-
dates.
   Taken together, these tools stabilize optimization; the figures below highlight
dropout, normalization, and optimizer behavior in practice.
 Risk & audit
    • Train/val mismatch: augmentation, preprocessing, and
      normalization must match at evaluation time (except stochastic
      augmentation).

    • Resolution trade-offs: downsampling can erase small objects;
      audit performance by scale and by class, not only overall accuracy.

    • BatchNorm regimes: very small batch sizes can destabilize BN
      statistics; consider alternatives (layer/group norm) and audit
      sensitivity.

    • Shortcut learning: CNNs can latch onto background cues; use
      perturbations, counterfactual crops, and slice audits.

    • Robustness: report performance under shifts (lighting, camera,
      compression) and track calibration when scores are used as
      probabilities.

    • Run-to-run variance: report seeds, spread, and stopping policy;
      use Appendix E as the default reporting format.

   Figure 47 provides the validation-curve diagnostic view used for dropout
decisions.

Batch normalization. BN accelerates convergence by normalizing mini-
batch statistics and learning scale/shift parameters. Figure 48 contrasts the
pre- and post-normalization activation distributions; whitening the distribution
keeps gradients in a well-behaved range and reduces covariate shift. In deep

                                       235
Modern Intelligent Systems                                                      11



                    1.0                          train (dropout)
                                                 val (dropout)
                    0.8                          val (no dropout)
                    0.6
             loss


                    0.4
                    0.2
                    0.0
                          0   10       20       30       40         50
                                         epoch
        Figure 47: Illustrative dropout effect on training/validation curves.
         Compared to a no-dropout baseline, validation curves flatten and
       generalization improves. Use it when diagnosing variance and deciding
          whether dropout is likely to help versus simpler regularization.


Transformer stacks, a closely related design choice is pre-LN versus post-LN :
modern architectures typically place layer normalization before the residual
block (pre-LN) to improve training stability on very deep networks.

Adaptive optimizers. While vanilla SGD remains a workhorse, Adam and
related methods adapt learning rates per-parameter (Kingma and Ba, 2015).
Figure 49 summarizes the typical loss trajectories; Adam converges faster ini-
tially, whereas SGD+momentum often attains a slightly lower asymptote after
fine-tuning.




                                        236
Modern Intelligent Systems                                                              11



                          Pre-BN activations                    Post-BN (per-channel)

                   0.4                                    0.4
         density




                                                density
                   0.2                                    0.2



                    0                                      0
                         −5       0        5                    −5        0         5
                                  x                                      x
                                                                        channel 1
                                                                        channel 2


    Figure 48: Batch normalization transforms per-channel activations toward
    zero mean and unit variance prior to the learned aﬀine re-scaling, stabilizing
     training. Use it when diagnosing unstable training from drifting activation
                                       scales.


 Practical optimizer notes
 Mixed precision. Modern CNN stacks often run activations/gradients in
 FP16 or BF16 while keeping master weights in FP32. Frameworks such as
 PyTorch AMP/TF mixed precision insert dynamic loss scaling so gradients
 do not underflow; the reward is higher throughput and lower memory
 pressure on recent GPUs/TPUs.
 AdamW vs. Adam. Decoupled weight decay (AdamW) subtracts ηλW
 outside the adaptive-moment step, avoiding the “L2-as-gradient-scaling”
 behavior of classical Adam and producing more predictable regularization
 (Loshchilov and Hutter, 2019). In code:

 m = beta1 * m + (1-beta1) * grad
 v = beta2 * v + (1-beta2) * grad**2
 W -= eta * (m_hat / (sqrt(v_hat) + eps) + lambda * W)

 Use AdamW (or SGD+momentum) when you want clean weight-decay
 semantics; reserve plain Adam for rapid prototyping or when adaptive
 steps dominate regularization.




                                               237
Modern Intelligent Systems                                                   11


                                       SGD+momentum
                                           Adam

                    1
            loss




                   0.5




                    0
                         0   10   20         30   40    50      60
                                         epoch

    Figure 49: Representative training curves for SGD with momentum versus
    Adam on the same CNN. Use it when comparing optimizer behavior under
                           the same model and data.


 MLP/CNN block pseudocode (schematic)
 function ForwardBackward(params, x, y):
   # forward
   caches = []
   a = x
   for (W, b, f) in params.layers:
     z = W @ a + b
     caches.append((a, z))
     a = f(z)
   loss, delta = params.loss(a, y)

   # backward
   grads = []
   for (W, b, f), (a_prev, z_prev) in
       reversed(list(zip(params.layers, caches))):
     grads.append((delta @ a_prev.T, delta))
     delta = (W.T @ delta) * f'(z_prev)

   params.update(grads[::-1])
   return loss


 This omits batching, convolution strides, and optimizer detail but
 highlights the cache-then-backprop pattern reused throughout the
 deep-learning chapters.


                                       238
Modern Intelligent Systems                                                  11


 Derivation closure: implement, cache, fail-fast
    • Implement: treat each block as a typed transform
      (conv/BN/activation/pool) with explicit input-output shapes.

    • Cache: retain pre-activations, normalization statistics, and masks
      needed for backward passes; do not recompute them implicitly.

    • Fail-fast checks: validate shape arithmetic, then run one-batch
      overfit tests before full training to catch broken gradients early.

    • Report: publish seed, augmentation recipe, and calibration metrics
      with every benchmark, following Appendix E.




                                     239
Modern Intelligent Systems                                                   11


 Key takeaways
    • Convolutions introduce sparse connectivity and parameter sharing,
      dramatically reducing parameters vs. fully connected layers.

    • Padding and stride control spatial resolution; pooling aggregates
      features to build invariances.

    • Batch normalization, dropout, and optimizer choice strongly
      influence training stability and generalization.

    • Stacking small kernels expands the effective receptive field across
      depth.

 Minimum viable mastery.
    • Given (n, f, s, p), compute output shapes and parameter counts for a
      convolutional block.

    • Explain equivariance vs. invariance and how stride/pooling/padding
      affect each.

    • Describe what batch normalization and dropout do during training
      and how they change behavior at evaluation time.
 Common pitfalls.
    • Letting shape bookkeeping drift (mismatched padding/stride) until
      the first dense layer fails.

    • Forgetting train/eval mode for batchnorm/dropout, producing
      misleading validation curves.

    • Treating pooling as mandatory or always beneficial; in some tasks,
      stride-2 convolutions or anti-aliasing are better choices.




                                     240
Modern Intelligent Systems                                                    12


 Exercises and lab ideas
     • Hand-compute a 1D cross-correlation with several (n, f, s, p) tuples
       and verify the shapes and values against a small script.

     • Compare max-pool + stride 1 vs. stride-2 convolutions on a toy
       dataset; report accuracy and FLOPs.

     • Equivariance sanity check: translate an image and confirm
       intermediate feature maps translate accordingly.

     • Train two depth-10 CNNs on a tiny dataset: one plain, one with
       identity skips; compare convergence and accuracy.

 If you are skipping ahead. The optimization and regularization knobs
 here carry almost unchanged into Chapters 12 to 14; what changes there is
 how context is represented and propagated, not the core loss-minimization
 discipline.



Where we head next. Chapter 12 keeps the same training and audit disci-
pline but shifts the modeling axis from spatial locality to temporal state and
sequence dependence.


12    Introduction to Recurrent Neural Networks
Chapter 11 showed how architectural bias (convolution/pooling) improves sam-
ple eﬀiciency while preserving the same optimization loop. This chapter keeps
that loop but changes the axis from space to time: sequence models need mem-
ory so present predictions can depend on prior tokens. Figure 1 flags this as the
sequential branch of the neural strand.




                                      241
Modern Intelligent Systems                                                          12


 Learning Outcomes
    • Explain why recurrent structures are needed for sequence modeling
      and contrast them with feedforward nets.

    • Derive the forward dynamics and backpropagation-through-time
      (BPTT) updates for vanilla RNN cells.

    • Recognize practical stabilization techniques (gradient clipping, gating,
      normalization) that motivate later LSTM/Transformer chapters.

 Design motif
 Add recurrence, then train it by unrolling time and reusing the backprop
 machinery from Chapter 7.

    The statistical learning chapters (Chapters 3 to 4) established the basic train-
ing loop: choose a model class, define a loss, optimize it, and then audit gener-
alization and calibration. The feedforward neural chapters then expanded the
model class from linear predictors to multilayer networks (MLPs, RBF networks,
and CNNs).
    Those architectures are effective for classification, regression, and feature
extraction, but they share a structural limitation: information flows strictly
from input to output, without an internal state that can store context over
time.

12.1     Motivation for Recurrent Neural Networks
Before delving into the architecture and mathematics of RNNs, it is important
to understand why feedforward networks are insuﬀicient for certain applications.
Consider the following scenario:

       You want to predict an output at time t based not only on the input at
       time t, but also on inputs from previous time steps t−1, t−2, . . . , t−k.

   This is a common situation in many real-world problems, such as:
  • Time series forecasting (e.g., stock prices, weather data)

  • Natural language processing (e.g., predicting the next word in a sentence)

  • Speech recognition and synthesis

                                          242
Modern Intelligent Systems                                                     12


  • Control systems with memory of past states

Chapter flow. We proceed in one pass: motivate temporal memory, formalize
state updates and parameter sharing, derive unrolling/BPTT, then cover stabi-
lization (clipping and gating) before closing with attention as the transition
beyond recurrent bottlenecks. Optional reminders are kept near the chapter
close so they do not interrupt the derivation arc.
    Order carries meaning even in simple settings: if it is Saturday, the next day
is Sunday. In language, “out of the blue” means something sudden, whereas “the
ball was blue” refers to color; the sequence makes the difference. In predictive
text, “I want to buy...” favors a different continuation than “Write a book about
Teddy...” These examples also highlight variable-length inputs: a review can
be three words or three hundred. You can always build a fixed window of past
inputs and feed it to a standard MLP, but that approach scales poorly as the
history grows and does not share parameters across time.
    Feedforward networks treat each input independently and do not have an
inherent mechanism to remember or utilize past inputs. To incorporate past
information, one might consider explicitly including previous inputs as part of
the current input vector, but this approach quickly becomes impractical as the
history length grows.

12.2   Key Idea: State and Memory in RNNs
Recurrent neural networks address this limitation by introducing a state vector
ht that summarizes information from all previous inputs up to time t. The state
is updated recursively as new inputs arrive, allowing the network to maintain a
form of memory.
    Formally, at each time step t, the RNN receives an input vector xt and
updates its hidden state ht according to a function f parameterized by weights
θ:



                               ht = f (ht−1 , xt ; θ)                      (12.1)

   The output yt at time t is then computed as a function of the current state:



                                       243
Modern Intelligent Systems                                                            12




                                     yt = g(ht ; θ′ )                             (12.2)

   Here, f and g are typically nonlinear functions implemented by neural net-
work layers, and θ, θ′ are learned parameters.

Interpretation: The hidden state ht acts as a summary or encoding of the
entire input history {x1 , x2 , . . . , xt }. This allows the network to make predictions
that depend on the temporal context, not just the current input.

Parameter sharing across time. The same weights are reused at each time
step. In the simplest formulation there are three learned matrices: Wxh (input
to state), Whh (state to state), and Why (state to output). When you unroll
the recurrence, these matrices appear at every step, so the model learns a single
transition rule rather than a separate set of parameters for each position in the
sequence.
    Unrolling makes the training graph T steps deep. Gradients from each time
step accumulate onto the shared weights, and the repeated Jacobian products
are precisely why long sequences revive the vanishing/exploding gradient issues
from deep feedforward networks. Training this unrolled graph with standard
backpropagation is known as backpropagation through time (BPTT).
    Recurrent neural networks (RNNs) were among the first practical sequence
models (Elman, 1990; Bengio et al., 1994). CNNs from Chapter 11 trade recur-
rence for parallel, spatially shared filters. Chapter 13 then supplies the token
representations and evaluation lens commonly paired with RNNs, and Chap-
ter 14 revisits sequence modeling without recurrence.

12.3    Comparison with Feedforward Networks
To contrast, a feedforward network computes the output at time t as:



                                     yt = ψ(xt ; θ)                               (12.3)

    where ψ is a nonlinear function without any dependence on past inputs. This
limits the ability of feedforward networks to model temporal dependencies unless

                                          244
Modern Intelligent Systems                                                     12


the input vector xt explicitly contains past information.

Summary: RNNs extend feedforward networks by incorporating a recurrent
connection that allows information to persist across time steps, enabling model-
ing of sequences and temporal dynamics.
 Shape reminder
 We keep the row-major (deep-learning) convention: xt ∈ Rdx , ht ∈ Rdh ,
 pre-activation at = xt Wxh + ht−1 Whh + bh , output yt = ht Why + by .
 Column-vector formulations simply transpose the order of factors; all
 stability conclusions (spectral norms of Jacobian factors) carry over.


Roadmap. The sequence is: architecture and state updates, unrolling/BPTT,
instability sources, stabilization strategies, gated variants, and attention-era
transition.

12.4   Recap: Feedforward Building Blocks
Simple RNN at a glance.
  • Objective: Minimize cross-entropy (or another sequence loss) between
    targets and pθ (yt | ht ), with ht = f (xt Wxh + ht−1 Whh + bh ).

  • Key hyperparameters: hidden state size, BPTT truncation window, op-
    timizer/learning rate, regularization (dropout, weight decay), and clipping
    threshold.

  • Defaults: tanh or ReLU activations, hidden size 128–512, Adam or
    SGD+momentum with clipping, and layer norm or gating (LSTM/GRU)
    for long sequences.

  • Common pitfalls: vanishing/exploding gradients on long sequences, too-
    small hidden states, and train/test mismatch when teacher forcing is not
    reflected at inference.
    RNNs reuse the same ingredients as multilayer perceptrons (activations, non-
linear decision boundaries, loss functions, and training heuristics) but wrap them
around a temporal axis. Figure 25 from Chapter 7 highlights the canonical MLP



                                       245
Modern Intelligent Systems                                                               12


                       Logistic regression                  Shallow MLP


              1                                    1                      Nonlinear separator
                                       w⊤ x + b = 0
         x2




                                              x2
              0                                    0


                   Class 1 Class 2

                  −1          0        1               −1      0        1
                                  x1                               x1

    Figure 50: Decision boundaries for logistic regression (left) versus a shallow
    MLP (right). Linear models carve a single hyperplane, whereas hidden units
     can warp the boundary to follow non-convex manifolds such as the moons
       dataset. Use it when diagnosing whether representation capacity (not
                          optimization) limits a classifier.


dataflow along with common activation choices and derivatives that govern gra-
dient flow.
     Two-dimensional toy datasets remain useful for reasoning about inductive
biases. Figure 50 contrasts logistic regression and a shallow MLP on the moons
dataset, illustrating how additional hidden units carve nonlinear boundaries that
RNN readouts later rely on when decoding the final state.
     Figure 52 is the canonical unrolling view used to interpret shared-parameter
BPTT updates.
     Finally, Figure 51 summarizes two diagnostics: BCE geometry and the ef-
fect of learning-rate schedules/early stopping. Here BCE (binary cross-entropy)
for a binary target y ∈ {0, 1} and logit z is L(z, y) = log(1 + e−z ) for y=1
and log(1 + ez ) for y=0; the logit z is the pre-sigmoid score so that σ(z) yields
the predicted probability. The middle panel contrasts a conservative schedule
(smooth decay) with a more aggressive one (faster initial drop but risk of os-
cillation), and the right panel shows early stopping triggered when validation
loss ceases to improve while training loss continues decreasing. We will reuse
these when tuning sequence models, where overfitting appears as a divergence
between per-token training and validation likelihood.




                                             246
Modern Intelligent Systems                                                                              12
```

### Findings
1. Mathematical correctness and notation:

- The update rule for weight w in equation (11.5) is correctly stated as \( w \leftarrow w - \eta \frac{\partial L}{\partial w} \).

- The expression for the gradient at the first layer in equation (11.6) is given as:
  \[
  \delta W^{(1)} \approx W^{(2)} D^{(2)} W^{(3)} D^{(3)} \cdots W^{(L)} D^{(L)} \delta W^{(L)}
  \]
  This is a standard schematic representation of the chain of Jacobians in backpropagation through layers. The notation is consistent and the explanation of spectral norms causing vanishing/exploding gradients is correct.

- The sigmoid function derivative is correctly given as:
  \[
  \sigma'(x) = \sigma(x)(1 - \sigma(x))
  \]
  and the explanation about saturation and maximum derivative at 0.25 is accurate.

- The RNN state update equations (12.1) and (12.2) are standard and correctly presented:
  \[
  h_t = f(h_{t-1}, x_t; \theta), \quad y_t = g(h_t; \theta')
  \]

- The feedforward network output at time t is correctly given as:
  \[
  y_t = \psi(x_t; \theta)
  \]

- The shape reminder for RNNs is consistent with common deep learning practice (row-major, inputs and states as row vectors).

- The pseudocode for the MLP/CNN block forward-backward pass is schematic but consistent with standard backpropagation logic.

2. Internal consistency:

- The chapter flows logically from convolutional layers and their dimensionality, through training challenges (vanishing/exploding gradients), to mitigation strategies, and then transitions to sequence models and RNNs.

- The explanations of vanishing/exploding gradients and their causes are consistent with the mathematical intuition provided.

- The discussion of batch normalization, dropout, and optimizer choices aligns with standard practice.

- The transition to RNNs and the motivation for recurrence is coherent and consistent with the prior discussion on deep networks.

3. Reproducibility risks:

- The pseudocode omits batching, convolution strides, and optimizer details, which is explicitly noted. This is acceptable for schematic illustration but could cause confusion if readers attempt direct implementation without these details.

- The explanation of AdamW update includes code-like notation but does not define all variables explicitly (e.g., \(m_{\text{hat}}\), \(v_{\text{hat}}\), \(\lambda\), \(\eta\), \(\epsilon\)). While these are standard, a brief definition would improve clarity.

- The description of batch normalization and dropout effects references figures (47, 48, 49) which are not included here; readers need access to these figures for full understanding.

4. Notation issues:

- The notation \( \delta W^{(\ell)} = \nabla_{W^{(\ell)}} L \) is clear, but the use of parentheses in superscripts for layer indices is somewhat unusual; however, it is common in deep learning literature.

- The notation \( D^{(\ell)} = \text{diag} f'(z^{(\ell)}) \) is clear, but the text says "where \(f'\) is the derivative of the activation function" without explicitly defining \(z^{(\ell)}\) as the pre-activation at layer \(\ell\). This could be clarified.

- The sigmoid function is written as \(\sigma(x) = 1 + e^{1 - x}\) in the text, which is incorrect. The correct sigmoid function is:
  \[
  \sigma(x) = \frac{1}{1 + e^{-x}}
  \]
  The text currently says:
  > "Consider the sigmoid activation function \(\sigma(x) = 1 + e^{1 - x}\)."
  
  This is a concrete error and must be corrected.

- The notation for BCE loss is given as:
  \[
  L(z, y) = \log(1 + e^{-z}) \text{ for } y=1, \quad \log(1 + e^{z}) \text{ for } y=0
  \]
  This is correct, but the text could clarify that \(z\) is the logit (pre-sigmoid score).

5. Unverifiable claims:

- The claim that "At scale, this architectural prior became decisive once large labeled datasets and GPU training matured: the sample-efficiency and compute-efficiency gap versus classical kernel pipelines narrowed and then flipped in favor of deep convolutional stacks" is a well-known historical fact but is stated without citation. While not incorrect, a reference would strengthen the claim.

- The statement "Batch normalization normalizes layer inputs during training, reducing the effective internal covariate shift" is a common explanation but the notion of "internal covariate shift" has been debated in literature. This is a minor point but could be noted.

Summary of concrete issues to fix:

- Correct the definition of the sigmoid function from \(\sigma(x) = 1 + e^{1 - x}\) to \(\sigma(x) = \frac{1}{1 + e^{-x}}\).

- Clarify the definition of \(z^{(\ell)}\) as the pre-activation at layer \(\ell\) when introducing \(D^{(\ell)}\).

- Define variables used in the AdamW update pseudocode explicitly (e.g., \(m_{\text{hat}}\), \(v_{\text{hat}}\), \(\lambda\), \(\eta\), \(\epsilon\)) or refer to their standard definitions.

- Consider adding citations for historical claims about convolutional architectures overtaking classical kernel pipelines.

No other mathematical or conceptual errors were found.

---

**Final verdict:**  
The chunk is mostly mathematically correct and internally consistent, with clear explanations and standard notation. The main concrete issue is the incorrect formula for the sigmoid function, which must be corrected. Minor clarifications on notation and variable definitions would improve clarity and reproducibility.

## Chunk 18/31
- Character range: 485308–515024

```text
BCE vs logit z             Learning rate effect                      Early stopping
          6
                        y=1                        conservative                                 train
                                         1                                1
                        y=0                         aggressive                                   val
          4




                                 loss




                                                                  loss
      L




                                        0.5                              0.5
          2

                                                                                         stop
          0                              0                                0
              −5    0        5                0    20      40                  0       20        40
                    z                              epoch                               epoch

       Figure 51: Binary cross-entropy geometry (left), effect of learning-rate
    schedules on loss (middle), and the typical training/validation divergence that
        motivates early stopping (right). Use it when choosing a learning-rate
                   schedule and interpreting early-stopping signals.


 Author’s note: treat early stopping as the default brake
 Unless there is a compelling reason to run to numerical convergence, stop
 as soon as the validation curve flattens while the training curve keeps
 dropping. Checkpoint the best weights and resume only if new data or
 regularization changes warrant it. That simple rule prevents most runaway
 experiments without elaborate hyperparameter sweeps.

 LayerNorm and residual RNN tips
 Layer Normalization (Ba et al., 2016) stabilizes recurrent dynamics by
 normalizing each hidden vector ht across features before applying the
 nonlinearity; unlike BatchNorm it works with batch size 1 and handles
 variable-length sequences gracefully. Residual RNN stacks (adding the
 input of a layer back to its output) keep gradients flowing even when depth
 increases, mirroring the skip-connections that make deep CNNs trainable.
 Together, LayerNorm + residual links curb exploding/vanishing gradients
 and are the default when building multi-layer RNN/LSTM stacks.


Historical Note: Hopfield Networks An early influential recurrent net-
work is the Hopfield network (Hopfield, 1982), which is a form of associative
memory. Unlike modern RNNs, Hopfield networks have symmetric weights and

                                                  247
Modern Intelligent Systems                                                                 12


are designed to converge to stable states representing stored patterns. While
Hopfield networks are not directly used for sequence modeling, they helped estab-
lish the energy-based viewpoint that reappears in later recurrent and attention-
based models.
    Bidirectional extensions run two RNNs in opposite directions and concate-
nate their states; they are widely used in encoders for labeling tasks when the
full context is available.

12.5    Input–output configurations and mathematical formula-
        tion
RNNs can map sequences to sequences in several ways:
   • Many-to-one (e.g., sentiment classification): consume x1:T , emit one label
     after the final state.

   • One-to-many (e.g., conditional generation): condition on a context vector,
     then autoregressively emit a sequence.

   • Many-to-many (e.g., tagging, ASR): emit yt at every step; encoder–decoder
     variants compress x1:T then decode.

   • Bidirectional encoders: run a forward and backward RNN and concatenate
     the states for sequence labeling or as encoder context.
   Consider an input sequence {x1 , x2 , . . . , xT }, where each xt ∈ Rd . The RNN
computes hidden states {h1 , h2 , . . . , hT } and outputs {y1 , y2 , . . . , yT } as follows:

                   h0 = 0 (initial hidden state)                                       (12.4)
                   ht = f (xt Wxh + ht−1 Whh + bh ),             t = 1, . . . , T      (12.5)
                    yt = g(ht Why + by ),     t = 1, . . . , T                         (12.6)

  Shapes and masks (batch B, time T )
  Inputs X ∈ RB×T ×dx ; hidden states H ∈ RB×T ×dh ; logits Y ∈ RB×T ×do .
  Parameters (row-major): Wxh ∈ Rdx ×dh , Whh ∈ Rdh ×dh , Why ∈ Rdh ×do ,
  biases bh ∈ Rdh , by ∈ Rdo .
                                         P                         P
  Padding mask M ∈ {0, 1}B×T : loss L = b,t Mb,t CE(ŷb,t , yb,t )/ b,t Mb,t .
  Masks preview the padding/causal masks detailed in Chapter 14.


                                            248
Modern Intelligent Systems                                                          12


            yt−1                           yt                          yt+1
                Why                             Why                       Why
                          Whh
            ht−1                           ht                          ht+1
                Wxh                             Wxh                       Wxh
            xt−1                           xt                          xt+1


                      shared parameters across the unrolled sequence

      Figure 52: Unrolling an RNN reveals repeated application of the same
    parameters across time steps. This view motivates backpropagation through
       time (BPTT), which accumulates gradients through every copy before
    updating the shared weights. Use it when translating a recurrent cell into an
                      explicit computation graph for training.


Unrolling and shared weights. The cleanest way to understand recurrence
is to unroll time: the same cell is applied repeatedly, reusing the same parameters
at each step. Training then becomes ordinary backpropagation on the unrolled
computation graph, with gradients accumulated across every copy of the shared
weights (backpropagation through time, BPTT).

12.6   Mathematical Formulation of a Simple RNN Cell
Consider a simple RNN cell with the following update equations:

                       ht = σh (xt Wxh + ht−1 Whh + bh ) ,                      (12.7)
                       yt = σy (ht Why + by ) .                                 (12.8)



12.7   Recurrent Neural Network (RNN) Architectures and Loss
       Computation
Recall from previous discussions that the loss function for classification tasks
often involves cross-entropy terms of the form:
                                          X
                                 L=−            yi log ŷi ,                    (12.9)
                                            i




                                           249
Modern Intelligent Systems                                                        12


where yi is the true label (often one-hot encoded) and ŷi is the predicted proba-
bility for class i. When ŷ = y, the loss is zero, indicating perfect prediction.
    In the context of RNNs, the total loss over a sequence is typically the sum
of losses at each time step:
                                            XT
                                  Ltotal =      Lt ,                          (12.10)
                                           t=1

where T is the sequence length.

Forward and Backward Passes in RNNs The forward pass involves prop-
agating inputs through the network over time steps t = 1, . . . , T , producing
outputs ŷt at each step. After computing the loss, the backward pass computes
gradients with respect to parameters by backpropagating errors through time, a
process known as Backpropagation Through Time (BPTT).
    BPTT unfolds the RNN across time steps and applies standard backpropa-
gation through this unrolled network. The key insight is that parameters are
shared across time steps, so gradients accumulate contributions from all time
steps; Figure 53 highlights the simultaneous forward flow (black) and backward
gradients (pink) that piggyback across every copy.
 Truncated BPTT in practice
  Unroll K steps, accumulate loss, backprop through those K steps, then
  detach the hidden state to stop graph growth:

  h = h0
  for t in range(T):
      h, yhat = rnn(x[t], h)
      loss += mask[t] * CE(yhat, y[t])
      if (t+1) % K == 0:
          loss.backward()
          clip_grad_norm_(model.parameters(), tau)
          opt.step(); opt.zero_grad()
          h = h.detach() # carry state, drop graph

  Choose K to balance memory and credit assignment (common range:
  20–100 steps).



                                        250
Modern Intelligent Systems                                                    12


  Vanilla RNN cell (forward + BPTT)
  # Forward for a sequence {x_t, y_t}
  h_0 = 0
  for t = 1..T:
      pre_h = h_{t-1} W_hh + x_t W_xh + b_h
      h_t = tanh(pre_h)
      yhat_t = h_t W_hy + b_y

  # Backward (BPTT with optional truncation K)
  delta_pre_next = 0
  for t = T..1:
      delta_y = grad_loss(yhat_t, y_t)
      grad_W_hy += h_t^T delta_y
      grad_b_y += delta_y
      delta_h = delta_y W_hy^T + delta_pre_next W_hh^T
      delta_pre = delta_h .* (1 - h_t^2)
      grad_W_hh += h_{t-1}^T delta_pre
      grad_W_xh += x_t^T delta_pre
      grad_b_h += delta_pre
      delta_pre_next = delta_pre
      if t < T-K: break # truncated BPTT

  Use gradient clipping (e.g., clip the global norm of parameter gradients)
  and layer/batch normalization when sequences are long to avoid
  exploding/vanishing gradients.

    The element-wise product in the backward step corresponds to the Hadamard
factors described in the derivation in Chapter 6; we write it as .* to align with
NumPy/Matlab notation.

Code–math dictionary. In code blocks we use ASCII identifiers such as h_-
t, W_hh, and b_h; in equations the same objects appear as ht , Whh , and bh
(boldface for vectors/matrices, subscripts for time and role). Detailed algebraic
derivations (forward/backward passes and gradient expressions) appear in Equa-
tions (12.7) to (12.8).


                                      251
Modern Intelligent Systems                                                                       12


                     ∂L/∂ht+1          ∂L/∂ht+2          ∂L/∂ht+3          ∂L/∂ht+4



              ht+0              ht+1              ht+2              ht+3              ht+4

              xt+0              xt+1              xt+2              xt+3              xt+4

                            shared (Whh , Wxh , Why ) across time


    Figure 53: Backpropagation through time (BPTT): unrolled forward pass
    (black) and backward gradients (pink) through time. Use it when reasoning
       about truncation windows and why long histories strain gradient flow.


Vanishing and Exploding Gradients Because each gradient term contains
products of Jacobians such as

                                 ∂ht                   ⊤
                                      = diag f ′ (at ) Whh ,
                                ∂ht−1

with pre-activation at = xt Wxh + ht−1 Whh + bh and elementwise nonlinear-
ity f , long sequences multiply many such factors. Here Whh ∈ Rdh ×dh and
              
diag f ′ (at ) ∈ Rdh ×dh , so the Jacobian ∂ht /∂ht−1 is a dh × dh matrix. If the
spectral norm of each factor is below one the product decays exponentially (van-
ishing); norms above one cause growth (exploding). Figure 54 illustrates both
behaviors across time. Practical remedies include gradient clipping, orthogonal
or unitary recurrent matrices, layer normalization, and gated architectures (LST-
M/GRU) that introduce additive memory paths. Empirically, vanilla RNNs of-
ten fail to preserve dependencies beyond roughly 5–10 steps in language tasks,
which is why gated cells became the default for longer sequences.

Parameter Updates At each time step, the gradient of the loss with respect
to parameters (e.g., weights W ) depends on the chain of partial derivatives
through the network states:

                                         ∂L   X ∂Lt T
                                            =       .                                        (12.11)
                                         ∂W     ∂W
                                                   t=1




                                                  252
Modern Intelligent Systems                                                            12



                  100

                 10 1 safe band
          / ht


                 10 2
                                                           Vanishing
                                                           Exploding
                 10 3
                        0    5    10    15     20   25     30    35    40
                                         Time steps
      Figure 54: Vanishing (blue) versus exploding (orange) gradients on a log
     scale. The gray strip highlights the stability band; the inset reminds readers
    that repeated Jacobian products either shrink gradients (thin blue arrows) or
     amplify them (thick orange arrows). Use it when diagnosing why long-range
                               dependencies fail to train.


Because of parameter sharing, the same W influences multiple time steps, and
the total gradient is the sum over these contributions.

12.8   Stabilizing Recurrent Training
Gradient clipping. A practical safeguard is to clip the global norm of the
gradient when it exceeds a threshold. Figure 55 shows how clipping prevents
the exploding case from destabilizing optimization while leaving the vanishing
regime untouched. Orthogonal or unitary initializations for the recurrent weight
matrix Whh are another common trick: because orthogonal matrices preserve
Euclidean norms, gradients neither explode nor vanish in the very early stages
of training (before nonlinearities and data-dependent effects accumulate).




                                         253
Modern Intelligent Systems                                                                                 12


           20                                                         1.2
                     Unclipped
                                                                       1




                                                      Training loss
           15       Clipped at τ
                                                                      0.8
     kgk




           10
                                   threshold τ                        0.6
            5
                                                                      0.4

            0                                                         0.2
                0   20      40        60         80                         0   20      40       60   80
                         Iteration                                                   Iteration

      Figure 55: Gradient norms (left) explode without clipping (orange) but
    remain bounded when the global norm is clipped at tau (green). Training loss
       (right) stabilizes as a result. Use it when setting clipping thresholds to
                       stabilize training without freezing learning.


  Stability defaults in practice
  Spectral norm kWhh k2 ≈ 1 keeps gradients roughly stable over tens of
  steps; clipping thresholds τ ∈ [0.5, 5] are sensible defaults when sequences
  are long. BatchNorm inside the recurrent loop is rarely helpful; prefer
  LayerNorm or gating to stabilize dynamics.
  Author’s note: do not fight vanilla RNNs. If your task needs
  dependencies longer than a handful of steps, do not over-tune a plain RNN.
  Start with clipping and a sensible truncation window, but move to
  GRU/LSTM once long-range information vanishes.


Dropout in RNNs. Variational/recurrent dropout applies the same dropout
mask at every time step to avoid injecting temporal noise (Gal and Ghahramani,
2016; Semeniuta et al., 2016); zoneout preserves hidden units stochastically in-
stead of zeroing them (Krueger et al., 2017). Standard per-time-step dropout
often harms sequence retention.

Teacher forcing and scheduled sampling. Sequence-to-sequence models
frequently feed the ground-truth token back into the decoder during training
(teacher forcing) to accelerate convergence. Figure 56 contrasts this regime with
free-running inference: teacher forcing injects gold tokens at every step, whereas
inference conditions the decoder on its own predictions. This mismatch is pre-


                                                  254
Modern Intelligent Systems                                                                12


   (a) Teacher forcing
          ht−1                   distribution           distribution
                          fθ                    fθ                      fθ     fθ   ···


      (b) Inference
          ht−1           yt−1   sampled token   yt     sampled token   yt+1
                          fθ                    fθ                      fθ     fθ   ···



                      hSTARTi                   ŷt                    ŷt+1


    Figure 56: Teacher forcing vs. inference in a sequence-to-sequence decoder.
    Gold arrows show supervised targets; orange arrows highlight autoregressive
       feedback that motivates scheduled sampling. Use it when diagnosing
                    train/test mismatch from teacher forcing.


cisely what scheduled-sampling curricula aim to mitigate (Bengio et al., 2015).

Gated cells. LSTMs (Hochreiter and Schmidhuber, 1997; Gers et al., 2000)
and GRUs (Cho et al., 2014) alleviate vanishing gradients by introducing addi-
tive memory paths guarded by gates. Figures 57 and 58 present the canonical
cell diagrams used later in the chapter when deriving the update equations.
Intuitively, LSTM forget/input/output gates control retention, writing, and ex-
posure of the memory ct ; GRU update/reset gates interpolate between ht−1 and
a candidate h̃t and decide how much past context influences the candidate. In
an LSTM, the state updates as ct = ft ct−1 + it c̃t and ht = ot tanh(ct ).
In a GRU, the hidden state updates as ht = (1 − zt ) ht−1 + zt h̃t , with the
reset gate rt shaping the candidate computation. In both figures, xt denotes the
input at time t, and ht−1 / ct−1 denote the carried state(s).




                                                      255
Modern Intelligent Systems                                                               12




       ct−1                                                  +                     ct




                                      ft
                                      σ

       ht−1                                                             tanh

                                      it
                                      σ

                    Aﬀine


                                      c̃t
                                     tanh

        xt

                                      ot
                                                                                   ht
                                      σ



        Figure 57: Long Short-Term Memory (LSTM) cell (Hochreiter and
     Schmidhuber, 1997; Gers et al., 2000). Use it when mapping gates and the
                       cell state to the gradient-flow path.




                                            1 − zt


      ht−1
                                zt
                                σ
                                                                               +   ht
                     aﬀine


                                rt                               h̃t
                                                     aﬀine
                                σ                                tanh               yt
       xt



    Figure 58: Gated Recurrent Unit (GRU) cell (Cho et al., 2014). Use it when
        comparing gating to vanilla recurrence and to LSTM-style memory.




                                            256
Modern Intelligent Systems                                                    12


 Vanilla RNN vs. GRU vs. LSTM
 Vanilla RNN: Single hidden state ht updated via
 ht = f (xt Wxh + ht−1 Whh + bh ); simplest and parameter-eﬀicient but most
 prone to vanishing/exploding gradients on long sequences.
 GRU: Uses update and reset gates to interpolate between ht−1 and a
 candidate state; fewer parameters than LSTM, often a good default when
 sequences are moderately long.
 LSTM: Maintains a separate cell state ct and uses input/forget/output
 gates; highest parameter count but most robust on very long-range
 dependencies and widely used in legacy sequence models.

 Implementation checklist: masks, clipping, pitfalls
 Minimal training loop with masks and clipping

 h = torch.zeros(B, d_h)
 for x, y, mask in loader:         # [B, T, dx], [B, T], [B, T]
     h = h.detach()                # carry state, drop graph
     logits, h = rnn(x, h)
     loss = (mask * CE(logits, y)).sum() / mask.sum()
     loss.backward()
     torch.nn.utils.clip_grad_norm_(model.parameters(), tau)
     opt.step(); opt.zero_grad()

 Variable-length sequences are padded; the mask zeros out pads in the loss.
 Reset h between sequences that should not share state.
 Pitfalls checklist Mis-handled pads (loss on padded tokens); forgetting to
 detach hidden state across mini-batches; no clipping on long sequences;
 BatchNorm inside recurrence (prefer LayerNorm); teacher-forcing
 train/test mismatch without scheduled sampling; no masking leads to
 biased gradients; dropout applied independently each time step instead of
 variational/recurrent dropout.


12.9   From recurrent state to attention
Attention mechanisms. Even with gating, long sequences can challenge
fixed-size hidden states. Attention augments the decoder with a content-based

                                     257
Modern Intelligent Systems                                                                                   12


                                                                                                αt,s
                                                                                                       1
      Target tokens (decoder steps)



                                         I   0.75
                                               1        0.1        0.05      0.05       0.05
                                                                                                       0.8

                                                                                                       0.6
                                      want   0.1        0.7
                                                         2         0.1       0.05       0.05
                                                                                                       0.4

                                        to   0.1        0.15       0.55
                                                                     3        0.1        0.1           0.2

                                                                                                       0
                                      buy    0.05       0.1        0.7
                                                                    4         0.1       0.05



                                         .   0.05       0.05       0.1        0.2        0.6
                                                                                          5


                                              je       veux      acheter      un        livre

                                                    Source tokens (encoder positions)

      Figure 59: Attention heatmap for a translation model. Rows are target
      tokens (decoder steps) and columns are source tokens (encoder positions).
        Each cell is an attention weight; the dot in each row marks the source
    position receiving the most attention. Use it when checking whether attention
                         aligns to the intended source context.


lookup into the encoder states, as visualized in Figure 59. Bright entries corre-
spond to encoder positions that most influence each generated token.
 Historical note: from gating to attention
 Gating (LSTM/GRU) made long-range gradient flow workable by creating
 additive memory paths. Attention takes a different route: rather than
 forcing all context into a single state, it learns a soft retrieval rule over past
 representations. This shift explains why modern sequence models often
 prefer attention when long context and parallel training matter most, while
 gated RNNs remain competitive for streaming and low-latency settings.


12.10 Wrapping Up the Derivations
This chapter develops the core ideas behind recurrent neural networks (RNNs)
for sequence modeling. A canonical task is language modeling: predicting the
next token from preceding context.
    Recall that the goal is to estimate the conditional probability of a word wt



                                                                  258
Modern Intelligent Systems                                                             12


given the sequence of previous words w1 , w2 , . . . , wt−1 :

                               P (wt | w1 , w2 , . . . , wt−1 ).                  (12.12)

    This probability can be modeled using an RNN, which maintains a hidden
state ht that summarizes the history up to time t. A common indexing choice is:
consume the current token wt (as an embedding xt ) and predict the next token
wt+1 . This is equivalent to modeling P (wt | w1:t−1 ) after a one-step shift.

                                                 ht = f (ht−1 , xt ; θ),          (12.13)
                        P (wt+1 | w1 , . . . , wt ) = g(ht ; θ),                  (12.14)

where xt is the input representation (e.g., word embedding) of the word wt , f is
the recurrent update function parameterized by θ, and g maps the hidden state
to a probability distribution over the vocabulary. Because the hidden state is
computed recursively, ht already aggregates information about the entire prefix
(w1 , . . . , wt ); predicting wt+1 from ht therefore reflects the Markovian summary
that RNNs maintain. Explicitly, repeatedly substituting Equation (12.5) reveals
that ht = f (f (· · · f (h0 , x1 ), . . .), xt ), so no information is lost other than the
compression inherent to the finite-dimensional state vector.

Training Objective The network is trained to maximize the likelihood of
the observed sequences in a large corpus of text. Given a training sequence
(w1 , w2 , . . . , wT ), the log-likelihood is:

                                 X
                                 T −1
                       L(θ) =           log P (wt+1 | w1 , . . . , wt ; θ).       (12.15)
                                 t=1

   This objective encourages the model to assign high probability to the actual
next word in the sequence, effectively learning the statistical structure of the
language without explicit labeling of word relationships.

Self-supervised nature of language modeling A key insight is that no
explicit labeling is required to train such models. The natural co-occurrence
statistics of words in large corpora serve as implicit supervision. For example,
the model learns that the word ”juice” often follows ”apple” because this pattern

                                               259
Modern Intelligent Systems                                                           12


frequently appears in the training data. This is the essence of self-supervised
learning in NLP, where the prediction targets are created directly from the input
sequence.

Input representations. The input xt is a numeric vector. In language mod-
eling and other discrete-token problems, it is typically a token embedding pro-
duced by a learned lookup table. Chapter 13 covers where those vectors come
from (training objectives, evaluation, and audit considerations).

12.10.1    Worked example: sentiment as a many-to-one decision
To make the sequence viewpoint concrete, consider a short review such as: “This
place is great.” In a sentiment classifier, we map the token sequence (w1 , . . . , wT )
to a single label y ∈ {0, 1} (negative/positive). The recurrence consumes nu-
meric inputs xt (one per token) and produces a final state hT that summarizes
the sentence:
                     ht = f (ht−1 , xt ; θ),  ŷ = σ(w⊤ hT + b),              (12.16)

where σ(·) is the logistic sigmoid and ŷ is the predicted probability of the positive
class.
    This setup highlights a subtle but important dependency between represen-
tation and generalization. If tokens are treated as unrelated IDs (e.g., purely
one-hot indicators), then “great” and “awesome” are orthogonal inputs: the
model has no built-in reason to transfer evidence across similar words unless the
training objective supplies a geometry that makes them nearby. In Chapter 13,
we return to this same kind of task and show how learning word vectors from
context gives the model a meaningful input space before any sequence model is
applied.

Summary of the Modeling Pipeline
   1. Collect a large corpus of text data.

   2. Tokenize the text into sequences of words.

   3. Represent words as embeddings (initialized from a lookup table that is
      learned jointly with the network parameters).

   4. Use an RNN to process sequences and produce hidden states.


                                         260
Modern Intelligent Systems                                                               12


  5. Predict the next word probability distribution from the hidden state.

  6. Train the model by maximizing the likelihood of the observed sequences.
 LSTM and GRU equations (compact)
 LSTM (single layer):
```

### Findings
No issues spotted.

## Chunk 19/31
- Character range: 515041–543230

```text
it = σ(xt Wi + ht−1 Ui + bi ),         ft = σ(xt Wf + ht−1 Uf + bf ),
      c̃t = tanh(xt Wc + ht−1 Uc + bc ), ot = σ(xt Wo + ht−1 Uo + bo ),
      ct = f t   ct−1 + it   c̃t ,            ht = ot   tanh(ct ).

 GRU:

   zt = σ(xt Wz + ht−1 Uz + bz ),                 rt = σ(xt Wr + ht−1 Ur + br ),
   h̃t = tanh(xt Wh + (rt     ht−1 )Uh + bh ), ht = (1 − zt )        ht−1 + zt   h̃t .

 All gates are elementwise; σ denotes the logistic sigmoid and           the
 Hadamard product.

 Notation note. In the sequence-model chapters, σ(·) always denotes the
 logistic sigmoid gate nonlinearity; when σ is used without an argument
 (e.g., in earlier chapters for noise scales σ 2 ) it refers to a standard deviation.
 Context distinguishes these roles; see Appendix D for the cross-chapter
 symbol index.


Optional refresher (padding and autoencoders). For a 1D/2D convolu-
tion with input size n, kernel size k, stride s, and padding p, the output size
is                                         
                                 n + 2p − k
                                              + 1.
                                     s
When s = 1 and you want to preserve size, choose p = (k − 1)/2 for odd k. For
encoder intuition, recall that autoencoders map x 7→ z 7→ x̂ with a reconstruc-
tion loss; the same compression intuition reappears in sequence encoders and
attention models.




                                        261
Modern Intelligent Systems                                                    12


 Key takeaways
    • Language modeling is trained with self-supervision by maximizing
      next-token likelihood.

    • Token vectors provide the numeric inputs; RNN hidden states encode
      context over time.

    • Stability tools (clipping, gating, attention) enable long-range
      dependency modeling.

 Minimum viable mastery.
    • Define the next-token objective and relate cross-entropy, perplexity,
      and log-likelihood.

    • Explain BPTT, truncation, and masking for variable-length
      sequences.

    • Describe why gates help (information and gradient flow) and when
      attention is a practical alternative.
 Common pitfalls.
    • Train/inference mismatch (teacher forcing without a decoding
      strategy that reflects it).

    • Unstable gradients on long sequences (no clipping, poor initialization,
      or overly large learning rates).

    • Incorrect padding masks that leak future tokens or contaminate the
      loss.




                                     262
Modern Intelligent Systems                                                    13


 Exercises and lab ideas
     • Train a many-to-one sentiment classifier; plot gradient norms with
       and without clipping.

     • Train a small LSTM language model; compare perplexity
       with/without weight tying and scheduled sampling.

     • Empirically sweep kWhh k (spectral scaling) and reproduce
       vanishing/exploding behavior.

     • Implement the masked, truncated-BPTT loop above and verify that
       pads do not affect the loss.

 If you are skipping ahead. Keep the loss/perplexity diagnostics and
 masking discipline from this chapter. Chapter 14 changes the architecture,
 but the same evaluation traps and data-leakage risks remain.



Where we head next. Chapter 13 translates this sequence viewpoint into
representation tooling: embedding objectives, neighborhood/analogy diagnos-
tics, and deployment audits. Keep the sentiment example (Section 12.10.1) in
mind: with learned token geometry, the same many-to-one task generalizes bet-
ter than with raw IDs. Chapter 14 then changes architecture again, replacing
recurrence with attention while preserving the same evaluation and masking
discipline.


13    Neural Network Applications in Natural Lan-
      guage Processing
Chapter 12 framed language as prediction under context: the model must assign
probability to the next token from a compressed state. That framing makes
the bottleneck obvious. Tokens are discrete identifiers, while the model is a
continuous function; if the input geometry is unhelpful, the network cannot
generalize systematically from one string to another.
   This chapter supplies that geometry. We build word embeddings and the
objectives that train them, then show how to sanity-check the resulting space


                                     263
Modern Intelligent Systems                                                   13


(neighbors, analogies, and simple audits). Those same representation primitives
become inputs to both recurrent and attention-based models; Chapter 14 reuses
them when recurrence is replaced by attention.
  Learning Outcomes
    • Describe distributional semantics and the motivation for dense word
      embeddings.

    • Derive and implement common embedding objectives
      (CBOW/skip-gram, negative sampling) and evaluate them via
      analogy tasks.

    • Connect embedding quality to downstream architectures (RNNs,
      Transformers) and fairness considerations.

  Design motif
  Representation learning as a contract between data and objective—when
  you train on co-occurrence, you get both useful structure (analogies,
  clusters) and the biases present in the corpus.


13.1   Context and Motivation
In this chapter, we focus on neural methods for natural language processing
(NLP) through the lens of representation learning. The recurring question from
Chapter 12 is practical: what input space makes sequence prediction stable
and data eﬀicient? The answer is to learn vectors whose geometry captures
contextual similarity.
   A classic example illustrating the power of such representations is the anal-
ogy:
                        king − man + woman ≈ queen.

This demonstrates that vector arithmetic on word embeddings can capture mean-
ingful relationships between words. The goal is to find a vector space embedding
where semantic similarity corresponds to geometric closeness.

How this chapter is organized.
   • Core path: distributional hypothesis → Word2Vec (CBOW/skip-gram)


                                      264
Modern Intelligent Systems                                                    13


       objectives → negative sampling → how to evaluate embeddings (analo-
       gy/neighbors) → how embeddings plug into RNNs/attention models.

   • Optional detours: deeper objective derivations, historical notes, and the
     deployment/fairness discussion (important when embeddings are used in
     decisions rather than as a pure feature extractor).

Notation. We use V for vocabulary size, d for embedding dimension, xt for
one-hot token indicators, and et for learned embedding vectors. When symbols
collide with earlier chapters (e.g., d as data dimension vs. embedding size), the
local meaning is authoritative; Appendix D gives the global index.

Problem statement. Given a vocabulary (corpus) of approximately 10,000
words, we want to learn a mapping from each word to a dense vector repre-
sentation in a feature space of dimension d, where d is typically between 200
and 500. Formally, if the vocabulary size is V , each word wi begins as an in-
dex (equivalently, a one-hot indicator). Our objective is to learn an embedding
function
                              f : {1, . . . , V } → Rd ,

such that semantic and syntactic properties of words are preserved in the em-
bedding space.

13.2    Warm-up: from symbols to vectors
One-hot vectors make discrete tokens compatible with linear algebra, but they
do not express similarity: synonyms are orthogonal, and a model that treats
each basis element independently has no reason to generalize from “great” to
“awesome” without seeing both during training.

One-hot encoding (baseline). Fix a dictionary of size V . A token at posi-
tion t can be represented as a one-hot row indicator xt ∈ {0, 1}1×V with a single
1. This guarantees uniqueness, but it makes every pair of distinct words equally
far apart.

Why one-hot is not enough (two quick failures). Synonyms. A sen-
timent model trained to treat “great” as positive has no immediate reason to


                                      265
Modern Intelligent Systems                                                            13


Table 5: Feature-based word vectorization example. Each word is mapped to a vector
 of graded semantic features; fractional entries (e.g., 0.5) indicate mixed usage across
contexts. Use it when building intuition for how discrete symbols become vectors that
                          downstream models can consume.

   Word       Gender    Royalty    Age    Person   Fruit   Title   Abstract   Sweet
   man          1         0         1       1        0      0         0         0
   woman        0         0         1       1        0      0         0         0
   king         1         1         1       1        0      1         0         0
   queen        0         1         1       1        0      1         0         0
   orange       0         0         0       0        1      0         0         1
   apple        0         0         0       0        1      0         0         1
   monarch     0.5        1        0.5      1        0      1         0         0
   royal        0         1        0.5      0        0      1         1         0


treat “awesome” as positive if the two words are orthogonal basis vectors.
    Document similarity. “I enjoyed talking to the monarchs” and “I loved
conversing with the royals” express the same meaning, but a bag-of-words sim-
ilarity score stays low if it cannot recognize that monarchs and royals occupy
similar roles.
This is the same friction point you saw in Section 12.10.1: the sequence model
can only be as systematic as its input geometry.

Embedding lookup as learned features. Instead of using the identity basis,
we learn a table E ∈ RV ×d whose rows are trainable parameters. A one-hot
indicator becomes a row lookup:

                                  et = xt E ∈ R1×d .

This is the same linear algebra as one-hot, but now the coordinates are learned
so that similar words end up nearby when that helps prediction.
    A useful mental model is to imagine that each word is a graded bundle of
attributes. If we could write those attributes down explicitly, each word would
already be a vector:
    Table 5 gives a concrete intuition for mapping symbolic tokens into graded
feature vectors.
    Of course, hand-crafting features does not scale to large vocabularies, and
it bakes in subjective choices. The central move of modern embeddings is to

                                          266
Modern Intelligent Systems                                                     13


let the training objective discover whatever coordinates best support prediction
from context.

Subword tokenization and OOV handling. Practical systems rarely op-
erate on raw word types alone. To reduce vocabulary size and handle out-of-
vocabulary (OOV) forms, they tokenize text into subword units. Byte Pair
Encoding (BPE) and WordPiece learn a compact inventory of frequent charac-
ter sequences; words are segmented into a small number of subwords that can
be re-composed by the model. FastText instead augments word vectors with
character n-gram embeddings, so the representation of an unseen word is the
sum of its subword vectors.

13.3    Key Insight: Distributional Hypothesis
The foundational linguistic principle underlying word embeddings is the distri-
butional hypothesis, often summarized by the phrase:

       You shall know a word by the company it keeps.

This idea, attributed to the linguist John Robert Firth, states that the meaning
of a word can be inferred from the contexts in which it appears.

Example:      The word pretty can have different meanings depending on context:
  • In the collocation “pretty good,” pretty functions as an adverb meaning
    “very” and modifies an adjective.

  • In phrases such as “pretty image” or “pretty optics,” pretty is an adjective
    meaning “attractive.”
By explicitly examining the surrounding words (context windows of a few tokens
to the left and right), we can infer the intended meaning: instances co-occurring
with evaluative adjectives like “good” teach the “intensifier” sense, whereas con-
texts rich in nouns like “image” teach the “aesthetic” sense.

13.4    Contextual Meaning and Feature Extraction
The practical takeaway is that repeated context patterns reveal latent word prop-
erties. In the pretty example, co-occurrence with evaluative adjectives points to



                                       267
Modern Intelligent Systems                                                         13


an intensifier sense, while co-occurrence with visual nouns points to an aesthetic
sense.
    This is why modern embedding models treat corpus co-occurrence as super-
vision.
  Author’s note: who chooses the features?
  A natural student question is: if embeddings represent “features,” who
  decides what the features are? In modern embedding learning, the answer
  is: nobody writes them down explicitly. The features emerge from the
  training objective. By training a model to predict nearby words (or to
  distinguish real context pairs from random ones), the optimization process
  forces the hidden representation to encode whatever properties are useful
  for prediction. This is best viewed as self-supervised learning: targets come
  from the text itself via context windows, rather than from human labels.


13.5     Word2Vec at a glance
The Word2Vec framework, introduced by Mikolov et al. (2013), operationalizes
the distributional hypothesis through two main architectures:
   1. Continuous Bag of Words (CBOW): Predicts the target word given
      its surrounding context words.

   2. skip-gram: Predicts the surrounding context words given the target word.
   Both architectures learn vectors by solving local prediction tasks rather than
from hand-labeled semantic features.

13.5.1    Continuous Bag of Words (CBOW)
In CBOW, the model takes as input the context words surrounding a target
word and tries to predict the target word itself. Formally, given a sequence of
words {w1 , w2 , . . . , wT }, and a context window size n, the context for word wt is

                      Ct = {wt−n , . . . , wt−1 , wt+1 , . . . , wt+n }.

   The CBOW model maximizes the probability

                                        p(wt | Ct ),



                                            268
Modern Intelligent Systems                                                     13


where the context words Ct are represented as one-hot vectors and combined
(e.g., averaged) to form the input.

Example:     Consider the sentence

                             “to buy an automatic car”.

If we want to learn the embedding for the word automatic, the context might
be {to, buy, an, car}. The CBOW model uses these context words to predict
automatic.

13.5.2    skip-gram
Conversely, the skip-gram model takes the target word as input and tries to
predict each of the context words. It maximizes
                                   Y
                                           p(wc | wt ).
                                  wc ∈Ct

The product makes the modeling assumption explicit: every context word within
the window contributes a likelihood factor. In practice we maximize the sum
                      P
of log-probabilities    wc ∈Ct log p(wc | wt ) so that each neighboring prediction
provides an additive gradient signal.
    This approach tends to perform better on infrequent words and captures
more detailed semantic relationships.
    This first pass is conceptual. The next sections pin down the exact parame-
terization and training objectives used in practice.

13.6     From lookup to objective: compact derivation path
With the conceptual picture fixed, we now run one continuous derivation path
from lookup mechanics to CBOW/skip-gram training objectives. Let vocabulary
size be V and embedding dimension be d. Define the embedding matrix W ∈
RV ×d , where the i-th row vi is the embedding vector for word wi . Convention:
we treat embeddings as rows; one-hot words index rows via xW (row lookup).

Neural network architecture for word embeddings. For a concrete setup,
take a corpus with vocabulary size V = 10,000 and embedding dimension d =


                                           269
Modern Intelligent Systems                                                   13


300. The goal is to learn one dense vector per vocabulary item.

Input Representation Each input word is represented as a one-hot row vec-
tor x ∈ R1×V , where only one element is 1 (corresponding to the word index)
and the rest are 0. For example, if the word ”want” is the i-th word in the
vocabulary, then xi = 1 and xj = 0 for j 6= i.

Network Structure We consider a simple feedforward neural network with:
  • An input layer of size V (one-hot encoded words).

  • A hidden layer of size d = 300, which will serve as the embedding layer.

  • An output layer of size V , which predicts the target word.
   The weight matrix between the input and hidden layer is denoted as

                                  W ∈ RV ×d .

Each row Wi,: corresponds to the embedding vector of the i-th word.

Forward Pass Given an input word represented by x, the hidden layer output
h ∈ Rd is computed as:

                                   h = xW,                                (13.1)

where x is a 1 × V vector and W is V × d, resulting in h of size 1 × d.
    Because x is one-hot, this operation simply selects the row of W correspond-
ing to the input word, i.e., the embedding vector for that word.

Output Layer The hidden layer output h is then multiplied by an output
matrix Wout ∈ Rd×V to produce the output logits z ∈ RV :

                                  z = hWout .                             (13.2)

   These logits are then passed through a softmax function to produce a prob-




                                      270
Modern Intelligent Systems                                                     13


ability distribution over the vocabulary:

                              exp(zj )
                      ŷj = PV            ,       j = 1, . . . , V.        (13.3)
                             k=1 exp(zk )

Training Objective The target output y is also a one-hot vector correspond-
ing to the word we want to predict (e.g., the word ”automatic”). The training
objective is to minimize the cross-entropy loss between the predicted distribution
ŷ and the target y:

                                      X
                                      V
                               L=−          yj log ŷj .                   (13.4)
                                      j=1


Backpropagation and Weight Updates During training, the weights W
and Wout are updated via backpropagation to minimize L. This process adjusts
the embeddings in W so that words appearing in similar contexts have similar
vector representations.

Context window and sequential input. Reusing the same toy phrase, let
the context window size be 4 around the target token. To predict “automatic”
in “to buy an automatic car,” the context words are

                             to,   buy,     an,     car.

   Each context word is represented as a one-hot vector and fed into the network.
Each one-hot vector shares the same embedding matrix W; multiplying xW is
an eﬀicient row lookup because x is one-hot.

Input Sequence Processing The same embedding lookup is applied to each
context token. If xt+j is the one-hot vector for the word at position t + j, then
its embedding is
                                 ht+j = xt+j W.

    The hidden representations h(i) for each context word can be combined (e.g.,
concatenated or averaged) before passing to the output layer to predict the
target word.


                                       271
Modern Intelligent Systems                                                      13


Dimensionality and Sparsity Note that the input vectors xt+j are ex-
tremely sparse (one-hot), and the embedding matrix W is large (10,000 × 300,
for example). However, the multiplication xt+j W is eﬀicient because it selects
a single row of W per input word.

Interpretation of the weight matrix W . The matrix W can be interpreted
as a lookup table: the i-th row is the embedding for word wi , and xW (with
one-hot x) selects that row directly.

13.7     Word2Vec objectives in detail
With notation fixed, we now write the two Word2Vec objectives in full form:
Continuous Bag of Words (CBOW) and skip-gram.

13.7.1    CBOW objective (detailed form)
In the detailed CBOW form, the model predicts center token wt from its window
context. For a sequence w1 , w2 , . . . , wT and half-window size c, the context is
{wt−c , . . . , wt−1 , wt+1 , . . . , wt+c }.
    Each context token is encoded as a one-hot row in R1×V , then mapped
through W ∈ RV ×d to its dense embedding.
    The CBOW model computes the average of the embeddings of the context
words using an input embedding matrix W and predicts with a separate output
embedding matrix Wout :


                                   1 X
                              h=       xt+j W                                (13.5)
                                   2c
                                      −c≤j≤c
                                       j̸=0


    where xt+j is the one-hot vector for the context word at position t + j, and
c denotes the half-window size (there are 2c context words around wt when the
document is long enough).
    This hidden representation h is then used to predict the target word wt via
a softmax layer:


                                           exp(h uwt )
                       P (wt | context) = PV                                 (13.6)
                                           w=1 exp(h uw )


                                       272
Modern Intelligent Systems                                                 13


    where uw is the output vector corresponding to word w. It is useful to
think of the set of output vectors as the columns of a second matrix Wout ∈
Rd×V ; although Wout often starts as a copy of W⊤ , the two sets of embeddings
are optimized independently during training. Many modern implementations
optionally tie these matrices so that Wout = W⊤ , reducing parameters and
encouraging symmetry between input and output spaces.
    Training maximizes corpus log-likelihood, updating both W and output vec-
tors uw . The rows of W are then used as the learned embeddings.

Key Insight: Multiplying one-hot input xt+j by W performs a row lookup.
The embedding matrix therefore behaves as a trainable feature table.

13.7.2   skip-gram objective (detailed form)
The detailed skip-gram form reverses CBOW: use center word wt to predict each
context token wt+j in window c:


                                Y
                                       P (wt+j | wt )                   (13.7)
                              −c≤j≤c
                               j̸=0

   The input is the one-hot vector xt representing the center word, which is
projected into the embedding space via the same input embedding matrix W ∈
RV ×d :



                                    h = xt W                            (13.8)

   Each context word wt+j is predicted by applying a softmax over the output
vectors (again using the output-embedding matrix Wout ):

                                                      
                                          exp h uwt+j
                        P (wt+j | wt ) = PV                             (13.9)
                                           w=1 exp(h uw )

   where uw are the output vectors as before.




                                        273
Modern Intelligent Systems                                                       13


Training Objective: Maximize the log-likelihood of the context words given
the center word over the entire corpus. Compare to the RNN language-model
objective in Chapter 12: both predict nearby tokens, but here the context is a
fixed sliding window rather than a learned recurrent state.

Interpretation: Skip-gram pushes words with similar neighborhoods toward
similar embeddings.

13.7.3   Computational Challenges: Softmax Normalization
Both CBOW and skip-gram models require computing the softmax normaliza-
tion over the entire vocabulary V , which can be very large (e.g., V = 10, 000
or more). The denominator in equations (13.6) and (13.9) involves summing
exponentials over all vocabulary words:


                                   X
                                   V
                              Z=         exp(h uw )                      (13.10)
                                   w=1


 Recipe: skip-gram with negative sampling
 Preprocess: tokenize (BPE/WordPiece or whitespace), lowercase if
 appropriate, drop rare words below a cutoff, subsample frequent words
 with t ≈ 10−5 .
 Hyperparameters: window c = 2–5 (often dynamic/symmetric), embedding
 dim d = 100–300, negatives k = 5–20, unigram noise Pn (w) ∝ f (w)0.75 , LR
 on the order of 10−3 –10−2 .
 Per-positive loss (one context word):
                    P
 − log σ(h upos ) − ki=1 log σ(−h uneg,i ); complexity O(k) vs. O(V ) for full
 softmax.

   This is computationally expensive, especially when training on large corpora.

Approximate Solutions:       To address this, several approximation techniques
have been proposed:
  • Hierarchical softmax: factor the softmax into a tree so each update
    touches only a log V path.


                                     274
Modern Intelligent Systems                                                     13


  • Negative sampling: replace the full softmax with k binary logistic losses
    against sampled “noise” words.

13.8   Eﬀicient Training of Word Embeddings: Hierarchical Soft-
       max and Negative Sampling
Recall from the previous discussion that computing the full softmax over a large
vocabulary is computationally expensive. Specifically, given an input word, cal-
culating the probability distribution over all possible output words in the vo-
cabulary requires a normalization over potentially millions of terms, which is
prohibitive in practice.
    There are two primary strategies to address this computational bottleneck:

1. Hierarchical Softmax Hierarchical softmax replaces the flat softmax layer
with a binary tree representation of the vocabulary. Each word corresponds to a
leaf node, and the probability of a word is decomposed into the probabilities of
traversing the path from the root to that leaf. This reduces the computational
complexity from O(V ) to O(log V ), where V is the vocabulary size.
    The key idea is to organize words so that frequent words have shorter paths,
thus further improving eﬀiciency. During training, only the nodes along the
path to the target word are updated, avoiding the need to compute scores for
all words.

2. Negative Sampling Negative sampling is an alternative approximation
that simplifies the objective by transforming the multi-class classification prob-
lem into multiple binary classification problems.
  • For each observed word-context pair (w, c), the model aims to distinguish
    the true pair from randomly sampled negative pairs (w, c′ ), where c′ is
    drawn from a noise distribution.

  • Instead of computing probabilities over the entire vocabulary, the model
    only updates parameters for the positive pair and a small number of neg-
    ative samples.




                                       275
Modern Intelligent Systems                                                         13


Example:     Consider the sentence:

                 “I want to buy a big brick house in the city.”

Suppose the context word is brick. The true target word is house. Negative
samples might be lion, bake, or big (although big appears in the sentence, it
can still be sampled as a negative example depending on the sampling strategy).
Negative draws occasionally colliding with real context words is harmless. The
associated losses simply push the model to separate the sampled pair unless the
data provide strong evidence to the contrary.
```

### Findings
No issues spotted.

## Chunk 20/31
- Character range: 543239–573267

```text
Training Objective with Negative Sampling Define the logistic regression
classifier that, given an input word vector vw and an output word vector vc′ ,
predicts whether the pair (w, c) is observed (label 1) or a negative sample (label
0).
    The probability that the pair is observed is modeled as:

                             p(D = 1 | w, c) = σ(vw vc′ )                      (13.11)

where σ(x) = 1+e1−x is the sigmoid function.
     The training objective for one positive pair (w, c) and k negative samples
{c1 , . . . , c′k } is:
  ′

                                         X
                                         k
                                                            
                        log σ(vw vc′ ) +   log σ − vw vc′ ′              (13.12)
                                                            i
                                        i=1

where each c′i is drawn independently from the noise distribution Pn (c). A
widely used practical choice is Pn (w) ∝ f (w)0.75 , where f (w) is the empirical
unigram frequency; this slightly downweights extremely frequent words while
still sampling them often enough to learn robust embeddings.

Tiny worked example (skip-gram with k = 2). Suppose the center word is
                                                          ′
brick with embedding vbrick , the true context is house (vhouse ), and we sample
two negatives lion, bake. We compute:

                        ′                        ′                       ′
      L = log σ(vbrick vhouse ) + log σ(−vbrick vlion ) + log σ(−vbrick vbake ).



                                         276
Modern Intelligent Systems                                                      13


                                   ′
Gradients push vbrick closer to vhouse   (if the dot product is too small) and
                                       ′
simultaneously push it away from vlion and vbake ′  . Only these three context
vectors update this step, so the cost stays O(k) regardless of vocabulary size.

Interpretation: The model learns to assign high similarity scores to true
word-context pairs and low similarity scores to randomly sampled pairs, effec-
tively learning meaningful embeddings without computing the full softmax. The
expectation over the noise distribution is estimated by the empirical average
across the k sampled negatives in (13.12). Unlike noise-contrastive estimation
(NCE), negative sampling is not a consistent estimator of the normalized soft-
max probabilities; it is best viewed as a task-specific approximation that yields
high-quality embeddings rather than calibrated class posteriors.

Backpropagation: The gradients are computed only for the positive pair and
the sampled negative pairs, drastically reducing computation.

Connection to PMI (Levy & Goldberg). A useful theoretical lens re-
lates skip-gram with negative sampling (SGNS) to pointwise mutual information
(PMI). Under common choices of windowing and negative sampling distribution,
SGNS implicitly factorizes a shifted PMI matrix such that inner products ap-
proximate:

                                                                  P (i, k)
        vi uk ≈ PMI(i, k) − log k,    where    PMI(i, k) = log              .
                                                                 P (i)P (k)

This connection helps explain why SGNS and GloVe often yield similar geometric
regularities despite different training objectives: both methods recover statistics
of co-occurrence up to monotone transformations and weighting.

13.9   Local Context vs. Global Matrix Factorization Approaches
Word embedding methods can be broadly categorized into two classes based on
how they utilize context information:

1. Local Context Window Methods These methods focus on the immedi-
ate context of a word within a fixed-size window. Examples include:
   • Continuous Bag-of-Words (CBOW)

                                       277
Modern Intelligent Systems                                                      13


  • skip-gram
    They learn embeddings by predicting a word given its neighbors (CBOW)
or predicting neighbors given a word (skip-gram). These methods are compu-
tationally eﬀicient and capture syntactic and semantic relationships based on
local co-occurrence patterns.

2. Global Matrix Factorization Methods These methods consider the
entire corpus to build a global co-occurrence matrix X, where each entry Xij
counts how often word i co-occurs with word j across the corpus.
  • Latent Semantic Analysis (LSA) is an early example, which applies singu-
    lar value decomposition (SVD) to the co-occurrence matrix.

  • More recent methods include GloVe (Global Vectors), which factorizes a
    weighted log-count matrix (Pennington et al., 2014).

Example: Co-occurrence Matrix Suppose the vocabulary size is V . The
co-occurrence matrix X ∈ RV ×V is defined as:

        Xij = number of times word i appears in the context of word j

    This matrix is sparse and large (especially when V runs into the hundreds
of thousands), so storing it explicitly or factorizing it naively can be computa-
tionally expensive.

13.10 Global Word Vector Representations via Co-occurrence
      Statistics
Recall that our goal is to obtain a global vector representation for words, captur-
ing semantic relationships beyond simple one-hot encodings. Instead of encoding
words individually, we leverage co-occurrence statistics of word pairs within a
corpus to build richer embeddings.

Setup: Consider two words wi and wj appearing in some context window
within a text corpus. We are interested in modeling the co-occurrence of these
words, possibly mediated by a third context word wk . For example, in the phrase



                                       278
Modern Intelligent Systems                                                      13


“big historic castle,” the words “big” and “historic” are targets, and “castle” can
be a context word connecting them.

Notation:
   • Plain symbols wi , wj , wk denote lexical items drawn from the vocabulary.

   • Bold symbols denote vectors: vi is the embedding of target word wi and
     uk the embedding of context word wk .

   • Xik counts how often wi and wk co-occur within the chosen context window,
               P
     and Xi = k Xik is the total number of context observations for wi .

Goal: Define a function f that relates the co-occurrence statistics of the word
pairs and context words to a scalar quantity representing their semantic associ-
ation.

Visualization. Projecting the learned vectors onto two principal components
typically reveals well-separated semantic clusters. Figure 60 highlights how gen-
dered titles, fruits, and locations occupy distinct regions, reinforcing that co-
occurrence-driven training captures rich lexical structure.

13.10.1    Modeling Co-occurrence Probabilities
We start by considering the conditional probability of observing a context word
wk given a target word wi :
                                          Xik
                                P (k|i) =     .                          (13.13)
                                          Xi
    This probability captures how likely the context word wk appears near the
target word wi .

Relating to word vectors: Suppose each word wi is represented by a vec-
tor vi ∈ Rd . We want to model the relationship between vi , uk , and the co-
occurrence probability P (k|i).
    A natural assumption is that the co-occurrence probability can be modeled as
an exponential function of the inner product of the corresponding word vectors:

                              P (k|i) ∝ exp (vi uk ) .                     (13.14)


                                        279
Modern Intelligent Systems                                                         13



                  king                    analogy plane
                                                          queen



                                      man                            woman
      PC2




                           doctor                            nurse



                                                PC1
      Figure 60: Analogy geometry in embedding space. The offset “v(king) -
       v(man) + v(woman) approx v(queen)” forms a parallelogram; a similar
      gender direction shifts “doctor” toward “nurse.” Solid and dashed vectors
    highlight the shared relational direction. Points are shown after 2D PCA, so
    directions are approximate. Use it when checking whether embedding offsets
                encode consistent relations and reveal bias directions.


More explicitly, we can write a normalized model

                                         1                     
                          P (k|i) ≈         exp vi uk + bi + bk ,
                                         Zi

with partition function
                                    X                         
                           Zi =          exp vi uk′ + bi + bk′ .
                                    k′

    Taking logarithms on both sides and absorbing the (word-specific) normalizer
into the biases gives the approximate relation

                             log P (k|i) ≈ vi uk + bi + bk ,                 (13.15)

where bi and bk are bias terms associated with words wi and wk , respectively.
These biases account for the overall frequency or importance of each word while
implicitly capturing the effect of Zi .




                                               280
Modern Intelligent Systems                                                       13


Derivation: Starting from the co-occurrence counts,

                                                    Xik
                     log Xik − log Xi = log             = log P (k|i)       (13.16)
                                                    Xi
                                         ≈ v i u k + bi + bk .              (13.17)

   This equation suggests that the log co-occurrence counts can be approxi-
mated by a bilinear form plus biases.

13.10.2   Optimization Objective
Given the corpus co-occurrence matrix X = [Xik ], our goal is to find word
vectors vi , uk and biases bi , bk that minimize the reconstruction error:
                        X
                   J=         f (Xik ) (vi uk + bi + bk − log Xik )2 ,      (13.18)
                        i,k


where f is a weighting function that controls the influence of each co-occurrence
pair.

Why weighting? Many entries Xik are zero or very small, which can cause
numerical instability or dominate the objective. The function f is designed to:
  • Downweight rare co-occurrences (small Xik ) to avoid overfitting noise.

  • Possibly cap the influence of very frequent co-occurrences to prevent them
    from dominating.
   A typical choice for f is:
                                             α
                                        x
                                                     if x < xmax ,
                                        xmax
                        f (x) =                                             (13.19)
                                   1                otherwise,

where α ∈ (0, 1) and xmax is a cutoff parameter.

13.11 Finalizing the Word Embedding Derivations
In the previous sections, we explored the formulation of word embeddings
through co-occurrence statistics and matrix factorization approaches. This sec-
tion closes the derivation arc and clarifies the role of bias terms and optimization
strategies.

                                             281
Modern Intelligent Systems                                                        13


    Recall the key equation relating the word vectors vi and context vectors uk
to the co-occurrence counts xik :

                             vi uk + bi + bk = log xik ,                     (13.20)

where bi and bk are bias terms associated with the word and context, respectively.

Symmetry and Bias Terms Initially, two separate bias terms bi and bk were
introduced to account for asymmetries in the data. However, it is often possible
to simplify the model by combining or eliminating one of the biases without
loss of generality. This is because the biases can absorb constant shifts in the
embeddings, and the key information lies in the relative positions of the vectors.
In practice we keep both biases so that very frequent terms (e.g., stop words)
can learn large offsets while rarer words keep their dot products numerically
stable.
    Hence, the equation can be rewritten as

                             vi uk = log xik − bi − bk .                     (13.21)

   In practice, the biases bi and bk are learned jointly with the embeddings to
best fit the observed co-occurrence statistics.

Objective Function and Optimization Let the target embeddings be rows
vi ∈ R1×d , the context embeddings be columns uk ∈ Rd×1 , and the biases scalars
bi , bk ∈ R. The scalar score vi uk therefore measures the alignment between the
target and context embeddings. The goal is to find {vi , uk , bi , bk } that minimize
the reconstruction error of the log co-occurrence matrix. Because raw counts
span several orders of magnitude, the loss must behave like plain least squares
for large xik yet dampen the influence of very small counts. Enforcing the limits
f (x) → 0 as x → 0 and f (x) → 1 for x ≥ xmax yields the weighting scheme used
by GloVe. The final weighted least-squares loss is

                       X
                       V X
                         V
                  J=             f (xik ) (vi uk + bi + bk − log xik )2 ,    (13.22)
                       i=1 k=1




                                           282
Modern Intelligent Systems                                                       13


where f (x) is the weighting function that downweights rare (or extremely com-
mon) co-occurrences to improve robustness. GloVe, for instance, uses the piece-
wise definition
                               α
                          x         if x < xmax ,
                            xmax
                 f (x) =                            0 < α ≤ 1,          (13.23)
                         1          otherwise,

so that very small counts contribute little to the loss while still allowing moder-
ately frequent pairs to influence the fit. In the original paper, practical defaults
such as α ≈ 0.75 and xmax ≈ 100 were found to work well across a range of
corpora (Pennington et al., 2014); keeping those guardrails explicit also explains
why the same weighting recipe keeps reappearing in derived models.

Singular Value Decomposition (SVD) Connection One approach to solv-
ing this problem is to perform a low-rank approximation of the matrix log X,
where X = [xik ] is the co-occurrence matrix and the logarithm is applied ele-
mentwise (with small smoothing constants, e.g., ϵ = 10−8 , added to avoid log 0).
The singular value decomposition (SVD) provides a principled method to find
such a factorization:
                              log X ≈ Ur Σr Vr⊤ ,                        (13.24)

where Ur ∈ RV ×r and Vr ∈ RV ×r contain the top-r singular vectors (for the
desired embedding dimension d = r), and Σr ∈ Rr×r is a diagonal matrix of the
corresponding singular values. The truncation rank r, often between 100 and
300 in practice, acts exactly like the embedding dimensionality knob in neural
models.
    By setting
                       vi = (Ur )i Σr1/2 , uk = (Vr )k Σr1/2 ,

we obtain embeddings that approximate the log co-occurrence matrix in a least-
squares sense.

Interpretation and Limitations While SVD provides a closed-form solu-
tion, it does not explicitly model the bias terms bi , bk or the weighting function
f (x). Those additional degrees of freedom allow gradient-based methods such as
GloVe to better match empirical co-occurrence ratios. Biases soak up unigram


                                        283
Modern Intelligent Systems                                                       13


frequency effects while the weighting function prevents very noisy counts from
dominating the fit.
    Before moving from geometry to governance, keep the boundary clear: the
sections above establish how embeddings are learned and why their vector arith-
metic works. The next sections address whether that learned geometry is reliable
and safe under real deployment constraints.
  Risk & audit
     • Evaluation leakage: similarity/analogy benchmarks can overlap
       training sources; keep a truly held-out evaluation set and treat
       “standard” datasets as potentially contaminated.

     • Tokenization debt: preprocessing and vocabulary choices (case,
       subwords, cutoffs) change what the model can represent; version
       tokenizers and report them with results.

     • Frequency bias: rare words get unstable vectors; audit
       neighborhoods by frequency and use subsampling/regularization so
       geometry is not just Zipf effects.

     • Social bias: co-occurrence reflects social structure and stereotypes;
       probe for bias before using embeddings in decisions and document
       mitigations.

     • Privacy/memorization: large corpora can contain sensitive strings;
       treat training data as a security boundary and audit downstream
       systems for memorization.


13.12 Bias in Natural Language Processing
An important consideration in word embedding models is the presence of bias
inherited from the training corpora. Since embeddings are learned from co-
occurrence patterns in text, they reflect the statistical properties of the language
data, including cultural and societal biases.

Sources of Bias - Cultural Bias: Text corpora often contain stereotypes
or skewed representations of gender, ethnicity, and other social categories (e.g.,
news archives that associate “nurse” more frequently with women than men). -


                                        284
Modern Intelligent Systems                                                     13


Historical Bias: Older texts may reflect outdated or prejudiced views. Dig-
itized literature from the 19th century, for instance, over-represents colonial
perspectives. - Language-Specific Bias: Different languages and dialects en-
code different cultural norms and connotations, such as grammatical gender or
honorifics that privilege particular groups.

Impact on Embeddings For example, the well-known analogy

                         king − man + woman ≈ queen

illustrates that many embeddings support approximately linear semantic rela-
tionships. However, these same linear structures can also reveal problematic
biases, such as associating certain professions or attributes disproportionately
with one gender or group.

Debiasing Techniques Addressing bias in embeddings is an active area of
research. Techniques include: - Post-processing embeddings to remove bias di-
rections (e.g., Hard Debiasing by Bolukbasi et al. (2016)). - Data augmentation
to balance training corpora or swap gendered terms. - Regularization during
training to penalize biased associations or enforce equality constraints.

Cross-Lingual Challenges When extending embeddings to multiple lan-
guages, biases can manifest differently due to linguistic and cultural variations.
For example, gender is grammatically encoded in Romance languages, so direct
projection of English debiasing techniques may still leave gendered artifacts
in Spanish or French embeddings. Careful consideration is required to ensure
fairness and robustness across languages.




                                      285
Modern Intelligent Systems                                                    13


 Practical bias checks
    • Dataset audit: Inspect class balance, label sources, and sensitive
      attributes; check for under-represented groups and spurious
      correlations (e.g., profession ↔ gender cues).

    • Calibration and reliability: Evaluate calibration (ECE, reliability
      diagrams) overall and for key subgroups; severely miscalibrated
      models magnify harm when used for decision support.

    • Disaggregated evaluation: Report accuracy, ROC/PR, and
      calibration metrics by subgroup rather than only aggregate scores;
      look for systematic performance gaps.

    • Mitigation loop: Combine data interventions (rebalancing,
      augmentation) with model-side debiasing and re-evaluation; treat
      mitigation as an iterative, experiment-driven process.

 Author’s note: embeddings mix geometry and bias
 Embedding spaces faithfully capture geometry (analogies, clusters)
 precisely because they also capture the biases present in the data. Treat
 every downstream use as a combination of those two facets: audit the
 geometry you need, but also audit the offset directions you would rather
 suppress. Vector arithmetic makes biases quantifiable, so put that ability
 to work before shipping a model.


13.13 Responsible deployment checklist
  1. Purpose & consent. Document the use-case, decision stakes, and where
     humans remain in the loop; distinguish exploratory prototypes from pro-
     duction decision aids.

  2. Data lineage & licensing. Track licenses for each corpus (newswire,
     Common Crawl, proprietary logs) and state whether downstream users
     may redistribute the embeddings or derived models.

  3. Privacy & security. Scan corpora for PII, redact when necessary, and
     restrict raw-data access. When embeddings leave the lab, accompany them
     with an acceptable-use policy and redaction guarantees.

                                     286
Modern Intelligent Systems                                                    13


  4. Monitoring. Deploy subgroup-aware metrics, calibration checks, and
     toxicity filters in production; log drifts and institute retraining/rollback
     thresholds.

  5. Documentation. Ship a short “model card” summarizing intended uses,
     failure modes, and evaluation data so downstream teams can reason about
     fit-for-purpose decisions.

Contextual embeddings and transformers. Static embeddings assign a
single vector per word type, so polysemous words such as “bank” cannot adapt
to their context. Transformer-based language models (e.g., BERT; Devlin et al.,
2019) compute token representations conditioned on the entire sentence via
multi-head self-attention, allowing each occurrence to carry a context-specific
vector. The techniques developed in this chapter remain useful for lightweight
models and as initialization, but modern NLP pipelines increasingly fine-tune
contextual models to capture sentence-level nuance.

Wrap-up
This chapter has developed word-embedding models from co-occurrence statis-
tics, including the role of bias terms and optimization tools such as singular
value decomposition. It also emphasized a practical constraint: embeddings in-
herit social and cultural structure from training corpora, so bias diagnosis and
mitigation are part of model quality, not an optional add-on.




                                      287
Modern Intelligent Systems                                                    13


 Key takeaways
    • Word embeddings are dense vectors learned from co-occurrence
      statistics (local windows or global matrices).

    • Analogies and clustering arise from linear geometry in the embedding
      space.

    • Bias in corpora propagates to embeddings; debiasing and careful
      datasets are important.

 Minimum viable mastery.
    • Explain how co-occurrence statistics induce geometry (dot products,
      cosine similarity, and linear offsets).

    • Distinguish local-window objectives from global matrix factorization
      views and state when each is a good approximation.

    • Identify at least one concrete bias test and one mitigation strategy,
      and articulate their limitations.
 Common pitfalls.
    • Treating nearest neighbors as meaning rather than distributional
      evidence (polysemy and domain shift).

    • Over-interpreting analogy accuracy without controlling for frequency
      and evaluation set construction.

    • Applying debiasing as a post-hoc patch while ignoring corpus
      composition and labeling practices.




                                     288
Modern Intelligent Systems                                                    14


 Exercises and lab ideas
     • Implement a minimal example from this chapter and visualize
       intermediate quantities (plots or diagnostics) to match the
       pseudocode.

     • Stress-test a key hyperparameter or design choice discussed here and
       report the effect on validation performance or stability.

     • Re-derive one core equation or update rule by hand and check it
       numerically against your implementation.

 If you are skipping ahead. You can treat embeddings as feature vectors
 for any downstream model, but the audit mindset matters: log your corpus
 choices and evaluation splits so that later “fairness” or calibration
 conclusions have context.



Where we head next. Chapter 14 keeps the same token geometry but
changes context formation: attention replaces recurrent state, so dependencies
are queried directly. The same many-to-one decisions from Section 12.10.1
remain, but computational path and scaling behavior change. Keep the same
audit lens as you read: tokenization choices, masking correctness, and evalua-
tion protocol matter as much as architecture. After that, Chapter 15 pivots to
soft computing (fuzzy logic and evolutionary ideas) as an alternative paradigm
for reasoning under uncertainty.


14    Transformers: Attention-Based Sequence Model-
      ing
Chapter 12 made the sequence problem explicit: stateful computation plus gra-
dients that must flow across time. Chapter 13 then supplied the representation
layer that makes those sequence objectives practical. This chapter keeps those
representations but removes recurrence, replacing it with attention so informa-
tion can move globally within a layer.




                                     289
Modern Intelligent Systems                                                        14


  Learning Outcomes
  After this chapter, you should be able to:
     • Write the scaled dot-product attention and multi-head attention
       formulas.

     • Explain positional encodings and masking (causal/padding) in
       training/inference.

     • Describe encoder/decoder stacks, residuals, layer norm, and training
       stabilizers.

     • Compare RNNs vs. Transformers and know when each is preferable.

     • Outline common pretraining and fine-tuning strategies (MLM/CLM,
       LoRA/IA3) and decoding.

  Design motif
  Control information flow with structure (masks, normalization, residual
  paths) so optimization remains stable while context windows grow.


14.1    Why transformers after RNNs?
The RNN chapter (Chapter 12) closed with recurrent models that process to-
kens sequentially: information must travel through time steps, training cannot
fully parallelize across positions, and gradients can still struggle on long contexts
even with gating. The embeddings chapter (Chapter 13) addressed a different
bottleneck—how tokens become vectors so many-to-one decisions (e.g., senti-
ment classification) can generalize across similar words. Transformers replace
recurrence with attention so every position can condition on any other in a sin-
gle layer, enabling parallel hardware use and more direct long-range interactions
(Vaswani et al., 2017).




                                        290
Modern Intelligent Systems                                                     14


 Risk & audit
    • Masking errors: audit causal and padding masks; subtle bugs can
      leak future tokens or corrupt attention weights.

    • Evaluation leakage: benchmark contamination (train/test overlap)
      can inflate results; prefer held-out slices and time-based splits when
      possible.

    • Long-context failure: measure how quality degrades with sequence
      length; do not assume attention implies usable memory.

    • Calibration and confidence: likelihood and token probabilities
      need not align with factual correctness; audit reliability for
      downstream decisions.

    • Reproducibility: log tokenizer, data filters, and decoding settings;
      minor changes can swing outcomes more than architectural tweaks.


14.2   Scaled Dot-Product Attention
 Author’s note: attention allocates focus per token
 It is helpful to view attention as each token asking “who else helps me
 understand my role,” with masks and layer norms enforcing the rules of
 that dialogue. The scaled dot-product equations that follow quantify that
 per-token focus allocation.

   Given query, key, value matrices Q ∈ Rnq ×dk , K ∈ Rnk ×dk , and V ∈ Rnk ×dv ,
the basic attention operation is
                                                     
                                             QK⊤
                     Attn(Q, K, V) = softmax √            V.              (14.1)
                                               dk

Here nq is the sequence length of the queries and nk the sequence length of
keys/values. We keep the same sequence-first convention used in Chapters 12
and 13: rows index time positions (a “token dimension”) and columns index
                                                                  √
features, while batch elements are processed independently. The 1/ dk factor
stabilizes gradients by keeping logits in a reasonable range.



                                      291
Modern Intelligent Systems                                                      14


  Shape ledger
 We treat mini-batches as X ∈ RB×n×dmodel (batch, sequence, features).
 After the linear projections each head carries Q, K ∈ RB×h×n×dk ,
 V ∈ RB×h×n×dv , and the attention weights live in RB×h×n×n . Reading
 dimensions in this order avoids confusion when mixing frameworks;
 h · dk = dmodel (often dv = dk ). FFN inner widths typically 2–4×dmodel .
```

### Findings
Issues found in Chunk 20/31:

1. **Sigmoid function definition (Equation 13.11):**  
   The sigmoid function is incorrectly defined as  
   \[
   \sigma(x) = 1 + e^{1 - x}
   \]  
   This is mathematically incorrect. The standard sigmoid function is  
   \[
   \sigma(x) = \frac{1}{1 + e^{-x}}
   \]  
   This is a critical error as it affects the entire negative sampling objective.

2. **Notation inconsistency in negative sampling objective (Equation 13.12):**  
   The equation uses \( v_w v_{c'} \) and \( v_w v_{c'_i} \) but the primes and subscripts are not clearly distinguished or consistently formatted. For clarity, the output/context word vector should be consistently denoted, e.g., \( v_{c} \) for positive context and \( v_{c_i'} \) for negative samples. The notation \( c' \) and \( c'_i \) is confusing and should be clarified.

3. **Typographical errors in the negative sampling objective (Equation 13.12):**  
   The equation is presented as:  
   \[
   \log \sigma(v_w v_{c'}) + \sum_{i=1}^k \log \sigma(-v_w v_{c'_i})
   \]  
   but the text shows some stray symbols (e.g., "") and formatting issues that could confuse readers.

4. **Ambiguity in the noise distribution \( P_n(w) \propto f(w)^{0.75} \):**  
   The text states "A widely used practical choice is \( P_n(w) \propto f(w)^{0.75} \)". While this is standard, it should be explicitly noted that \( f(w) \) is the unigram frequency normalized over the vocabulary, and that the distribution is renormalized after exponentiation. This is important for reproducibility.

5. **Equation 13.14 (Modeling co-occurrence probabilities):**  
   The proportionality  
   \[
   P(k|i) \propto \exp(v_i^\top u_k)
   \]  
   is stated without mention of normalization, which is later introduced. It would be clearer to immediately state that this is an unnormalized model and that normalization is required for a proper probability distribution.

6. **Equation 13.15 (Log probability approximation):**  
   The equation  
   \[
   \log P(k|i) \approx v_i^\top u_k + b_i + b_k
   \]  
   is presented as an approximation after absorbing the partition function into biases. This is standard but should be explicitly stated as an approximation, not an equality, since the partition function depends on all \( u_k \) and biases.

7. **Equation 13.16 and 13.17 (Derivation from counts to embeddings):**  
   The step from  
   \[
   \log X_{ik} - \log X_i = \log P(k|i) \approx v_i^\top u_k + b_i + b_k
   \]  
   is correct but the notation \( X_i = \sum_k X_{ik} \) should be explicitly stated here for clarity.

8. **Equation 13.18 (Objective function):**  
   The objective is  
   \[
   J = \sum_{i,k} f(X_{ik}) (v_i^\top u_k + b_i + b_k - \log X_{ik})^2
   \]  
   but the text should clarify that \( X_{ik} > 0 \) to avoid \(\log 0\) issues, or mention smoothing strategies.

9. **Equation 13.19 and 13.23 (Weighting function \( f(x) \)):**  
   The piecewise function is given twice with slightly different notation and formatting. The function should be consistently defined once, with clear parameter ranges and explanation.

10. **Equation 13.22 (Objective function repeated):**  
    The equation is repeated with inconsistent summation indices:  
    \[
    J = \sum_{i=1}^V \sum_{k=1}^V f(x_{ik}) (v_i^\top u_k + b_i + b_k - \log x_{ik})^2
    \]  
    The notation switches between uppercase \( X_{ik} \) and lowercase \( x_{ik} \) without explanation. Consistency is needed.

11. **Equation 13.24 (SVD approximation):**  
    The equation  
    \[
    \log X \approx U_r \Sigma_r V_r^\top
    \]  
    is correct, but the text should clarify that the logarithm is elementwise and that smoothing (e.g., adding \(\epsilon\)) is necessary to avoid \(\log 0\).

12. **Equation for embeddings from SVD:**  
    The embeddings are defined as  
    \[
    v_i = (U_r)_i \Sigma_r^{1/2}, \quad u_k = (V_r)_k \Sigma_r^{1/2}
    \]  
    but the notation \((U_r)_i\) and \((V_r)_k\) is ambiguous. It should be clarified that these are the \(i\)-th and \(k\)-th rows of \(U_r\) and \(V_r\), respectively.

13. **Typographical and formatting issues:**  
    Throughout the chunk, there are stray symbols (e.g., "") and inconsistent use of primes and subscripts that may confuse readers.

14. **Claims about negative sampling vs. NCE:**  
    The text states that negative sampling is not a consistent estimator of normalized softmax probabilities and is best viewed as a task-specific approximation. This is accurate but could be strengthened by citing relevant literature or clarifying under what assumptions this holds.

15. **Claims about bias and debiasing:**  
    The discussion on bias and debiasing techniques is generally accurate but lacks citations for some claims (e.g., data augmentation, regularization). Adding references would improve verifiability.

16. **"Risk & audit" and "Practical bias checks" sections:**  
    These are useful but contain some vague terms like "tokenization debt" and "calibration (ECE, reliability diagrams)" without definitions or references, which may hinder reproducibility or understanding.

---

Summary: The main concrete issues are the incorrect sigmoid definition, inconsistent notation and formatting in equations, missing clarifications on normalization and smoothing, and some ambiguous notation in SVD embeddings. These should be corrected for mathematical correctness and clarity. Other points are suggestions for improved clarity and reproducibility.

## Chunk 21/31
- Character range: 573269–602919

```text
Complexity and memory
 Naive attention is O(n2 dmodel ) compute and O(n2 ) memory per head/layer
 for the attention map; this dominates long sequences. FlashAttention
 reduces activation I/O but keeps the quadratic arithmetic; sparse/linear
 variants reduce the n2 factor by trading exactness for structure (see
 Longformer/BigBird/Reformer/Performer/Linformer). Causal/padding
 masks do not change complexity, only which entries participate.


14.3   Multi-Head Attention (MHA)
Multiple heads attend in parallel after learned linear projections:

                             headi = Attn(QWiQ , KWiK , VWiV ),              (14.2)
                MHA(Q, K, V) = [head1 ; . . . ; headh ] WO ,                 (14.3)

with WiQ ∈ Rdmodel ×dk , WiK ∈ Rdmodel ×dk , WiV ∈ Rdmodel ×dv , and output projec-
tion WO . Figure 61 bundles scaled dot-product attention, multi-head concate-
nation, and the residual pre-LN block so the entire signal path is visible at a
glance.
    Figure 62 is the compact visual bridge for positional encoding, KV cache
reuse, and LoRA adapters.
    Figure 63 shows how padding and causal masks constrain attention patterns.

Micro
"     # attention example (2 tokens, causal mask). Let Q = K = V =
  1 0
        and dk = 2. Use a causal mask that sets all logits above the diagonal
  0 1
to −∞, so those entries vanish after the softmax. The unscaled score matrix is



                                       292
Modern Intelligent Systems                                                                                14


(a) Scaled Dot-Product                  (b) Multi-Head                        (c) Pre-LN Block

      Q       K         V                     Projections
                                             WiQ , WiK , WiV               residual
                                                                                        LayerNorm

                               ⊤
           MatMul           √
                            QK
                                                                                      Multi-Head Attn
                              dk
                                               Attention       ×h
                                                Head i
                                                                                            +
          Mask (opt.)
                                                 Concat                    residual
                                                                                        LayerNorm
           Softmax
                                                                                       FFN (GELU)
                                              Output W O
                        Weighted
           MatMul       Sum                                                                 +       Post-LN:
                                                                                                    Norm here




         Figure 61: Schematic: Reference schematic for the Transformer. Left:
        scaled dot-product attention. Center: multi-head concatenation with an
       output projection. Right: pre-LN encoder block combining attention, FFN,
       and residual connections; a post-LN variant simply moves each LayerNorm
                 after its residual add (dotted alternative, not shown).

"       #
    1 0                                  √
          ; after masking and dividing by 2, the first row softmaxes to [1, 0] and
    0 1
                                        √
                        0          1/    2
the second to [ 0 e 1/√2 , 0e 1/√2 ]. These are exactly the attention weights, and
               e +e       e +e
because V is the identity the attention output equals the weight matrix:
                                                   "                          #
                                                          1           0√
                             Attn(Q, K, V ) =             1 √        e1/ √
                                                                         2        ,
                                                       1+e1/ 2      1+e1/ 2

which grounds the shapes and masking rules before we move on to larger exam-
ples. This toy case instantiates the left panel of Figure 61 with Q = K = V = I2
and a 2 × 2 causal mask.

14.4      Positional Information
Transformers lack recurrence, so order is encoded explicitly.                              Two common
choices:
     • Sinusoidal encodings: add P with fixed sine/cosine frequencies to token
       embeddings.



                                                  293
Modern Intelligent Systems                                                                       14



 (a)                                     (b)                           (c)        W
                                                                                 rank r
                                               Decoder block
                                 token
                                                                        B                    A
                                                               reuse
                                                K/V cache
       Positional encodings

       sinusoidal / RoPE
                                                                             LoRA adapters

        Figure 62: Schematic: Transformer micro-views. Left: positional encodings
         (sinusoidal/rotary) add order information. Center: KV cache stores past
          keys/values so decoding a new token reuses prior context. Right: LoRA
          inserts low-rank adapters (B A) on top of a frozen weight matrix W for
                                parameter-eﬀicient tuning.


   • Learned encodings: learn a position embedding table and add to token
     embeddings.
Relative position encodings generalize better to long contexts and variable win-
dows.

14.5        Masks and Training Objectives
   • Causal masks zero out attention to future positions for autoregressive
     language models.

   • Padding masks prevent attending to padding tokens in batches.

   • Pretraining: masked language modeling (MLM; encoder) and causal LM
     (CLM; decoder-only). Sequence-to-sequence uses teacher forcing with en-
     coder →decoder cross-attention.

14.6        Encoder/Decoder Stacks and Stabilizers
Each block uses residual connections and layer normalization:

                               H′ = LayerNorm(H + MHA(H, H, H)),                             (14.4)
                              Hout = LayerNorm(H′ + FFN(H′ )).                               (14.5)

The feed-forward sublayer (FFN) is position-wise, typically two linear layers
with a nonlinearity (e.g., GELU). Dropout and label smoothing are common.



                                                    294
Modern Intelligent Systems                                                    14


 Transformer block (pre-LN) pseudocode
 function Block(H):
     # Pre-normalize inputs (pre-LN stabilizes deep stacks)
     H_norm = LayerNorm(H)
     attn = MHA(H_norm, H_norm, H_norm)
     H = H + Dropout(attn)
     H_norm = LayerNorm(H)
     ff = FFN(H_norm)
     return H + Dropout(ff)

 Decoder blocks add causal masks and cross-attention with encoder states.
 Pre-LN (shown here) is now common because it keeps gradients well
 behaved for very deep stacks; post-LN (original Transformer) is still used
 in smaller models.

 Training defaults (decoder-only, 2024)
 AdamW with cosine decay and 1–3% warmup; LR ∼ 10−3 for small models,
 1−2 × 10−4 for mid-size. Weight decay ≈ 0.01 (exclude biases/LayerNorm
 gains). Attention/MLP dropout ≈ 0.1; clip global norm to 1.0. Mixed
 precision (FP16/BF16) plus gradient checkpointing for long contexts; tie
 input embeddings to the LM head; use causal masks for CLM, padding
 masks for packed batches.




                                     295
Modern Intelligent Systems                                                14


 One training step (decoder-only, causal mask)
 x = tokenizer(batch_text)                # [B, T]
 mask = causal_mask(x)                    # [B, 1, T, T]
 h = embed(x) + pos(x)                    # [B, T, d_model]
 for block in blocks:
     h = block(h, mask)                   # pre-LN MHA + FFN
 logits = lm_head(h)                      # [B, T, vocab]
 loss = CE(logits[:, :-1], x[:, 1:])      # next-token
 loss.backward()
 clip_grad_norm_(model.parameters(), 1.0)
 opt.step(); opt.zero_grad()

 At inference, reuse cached K/V states per layer instead of recomputing
 attention over the full prefix.


Code–math dictionary. In code blocks, x is the token-index tensor (input
IDs), h is the hidden-state array H, mask is the attention mask, and embed(x)
denotes an embedding lookup into the learned matrix E (written algebraically
as a row-selection or E[wt ] in Chapter 13).

14.7   Long Contexts and Eﬀicient Attention
Memory and compute scale quadratically with sequence length. Practical sys-
tems therefore mix several tricks:
  • Sparse or local attention (e.g., Longformer, BigBird) to limit each
    query to a sliding or block-sparse neighborhood.

  • Low-rank/kernelized approximations and recurrent chunking (Per-
    former, Transformer-XL) so that computation/storage grows roughly lin-
    early in context length.

  • Relative/rotary positions and cache reuse to extrapolate beyond
    training lengths and avoid recomputing past keys/values during autore-
    gressive decoding.

  • I/O-aware kernels such as FlashAttention that stream tiles through


                                    296
Modern Intelligent Systems                                                              14


                    Padding mask                        Causal mask
                                             11                                  11
        t4   keep
              1      1    1    0    0        t4   1     1    future1masked
                                                             1          1
                                              0.8                                 0.8
        t3   1       1    1    0    0        t3   1     1    1    1     0
                                              0.6                                 0.6
        t2   1       1    1    0    0        t2   1     1    1    0     0
                                              0.4                                 0.4
        t1   1       1    1   0     0        t1   1     1    0    0     0
                                              0.2                                 0.2
                            mask
        t0   1       1    1   0     0    0   t00   1    0    0    0     0    0    0
             t0      t1   t2   t3   t4             t0   t1   t2   t3   t4

    Figure 63: Schematic: Attention masks visualized as heatmaps (queries on
     rows, keys on columns). Left: padding mask zeroes attention into padded
       positions of a shorter sequence in a packed batch. Right: causal mask
        enforces autoregressive flow by blocking attention to future tokens.


       SRAM so the quadratic pattern remains exact without exhausting mem-
       ory.

14.8    Fine-Tuning and Parameter-Eﬀicient Adaptation
Full fine-tuning updates all weights. Parameter-eﬀicient methods (LoRA, IA3,
adapters, prefix/prompt tuning) inject small trainable modules while freezing
most of the base model, enabling rapid adaptation. Beyond RLHF, preference-
based objectives such as DPO, KTO, or ORPO optimize alignment directly from
ranked pairs without a full reinforcement-learning loop.

14.9    Decoding and Evaluation
Autoregressive generation uses greedy, beam search, top-p (nucleus), or top-k
sampling. For safety and quality, monitor repetition, degeneration, and calibra-
tion. For classification tasks, prefer metrics aligned with class balance (AUPRC
on imbalanced sets).

When to use which. Beam search suits short factual tasks; top-p/top-k sam-
pling suits open-ended generation; temperature controls diversity/style. Track
perplexity for language modeling (see Chapter 13) and win-rates or task metrics
for downstream tasks.




                                             297
Modern Intelligent Systems                                                   14


14.10 Alignment (Brief)
Post-training alignment shapes model behavior to human preferences. RLHF op-
timizes a policy against a learned reward model; DPO offers a simpler objective
based on preference pairs.

14.11 Advanced attention and eﬀiciency notes (2024 snapshot)
  • Relative/rotary positions. RoPE (Su et al., 2021) and ALiBi (Press
    et al., 2022) replace absolute sinusoidal embeddings with rotation/bias
    terms so extrapolating to longer sequences no longer requires re-fitting
    positional lookups; the trade-off is that absolute tables keep fixed anchors
    for classification tokens while rotary/relative schemes favour extrapolation
    and smoothly sliding windows.

  • KV-cache management. Decoder-only inference stores per-layer key/-
    value tensors; chunked caching, paged attention, and sliding windows keep
    memory linear in context length. Speculative decoding and assisted decod-
    ing reuse a lightweight draft model to propose tokens that the full model
    verifies before committing.

  • Eﬀicient kernels. FlashAttention (Dao et al., 2022) computes attention
    blocks in streaming tiles to keep activations in SRAM. Long-context vari-
    ants mix windowed attention, recurrent memory, or low-rank adapters;
    state-space models such as Mamba (Gu et al., 2023) provide linear-time
    alternatives that back-propagate through implicitly defined kernels.

  • Mixture-of-experts and routing. Sparse MoE layers (Shazeer et al.,
    2017) add conditional capacity; router z-losses, capacity factors, and load-
    balancing losses are essential to avoid expert collapse.

  • Parameter-eﬀicient tuning. LoRA/QLoRA (Hu et al., 2022; Dettmers
    et al., 2023) insert low-rank adapters; DoRA/LoRA-FA refine the decompo-
    sition by separating direction and magnitude to better preserve pretrained
    weights. Adapter stacks and prefix tuning remain competitive for small
    target datasets.

  • Test-time scaling. Curriculum-based sampling (nucleus, temperature
    annealing), classifier-free guidance, and beam-search variants all tune the


                                     298
Modern Intelligent Systems                                                       14


     accuracy/latency frontier; plan to log decoding hyperparameters alongside
     checkpoints so experiments are reproducible.

14.12 RNNs vs. Transformers: When and Why

                      RNN/LSTM/GRU                   Transformer
Parallelism           Limited (sequential)           High (tokens in parallel)
Long context          Challenging (vanishing)        Natural; quadratic cost
Inductive bias        Order, recurrence              Content-based attention
Best for              Small data, streaming          Large data, global deps
Equivariance          N/A                            Permutation-equivariant
                                                     until positions (cf. conv
                                                     translation equivariance in
                                                     Chapter 11)


 Practitioner box: pitfalls and checks
 Pitfalls: training instability (lr too high), attention collapse, over-length
 inputs.
 Checks: monitor loss/entropy, validation perplexity, and attention
 patterns on probes.
 Hyperparams: heads (4–16), depth (6–24), dmodel (256–2048), FFN
 multiplier (×2–×4).


Notes
Terminology: masked-LM and next-token LM are self-supervised (targets de-
rived from input), not unsupervised. For embeddings downstream, we adopt
row-embedding convention consistent with Chapters 7 to 8.




                                      299
Modern Intelligent Systems                                                    14


 Key takeaways
    • Attention replaces recurrence with content-based mixing, enabling
      highly parallel training but introducing quadratic cost in sequence
      length.

    • Practical stability depends on details (pre-LN vs. post-LN, optimizer
      choices, masking, and careful decoding/evaluation).

    • Architecture choices (encoder/decoder, positions, caching) are not
      cosmetic: they determine what the model can reuse at inference time.

 Minimum viable mastery.
    • Compute masked attention for a short sequence and explain why the
      mask enforces causality.

    • Explain pre-LN vs. post-LN and why residual paths influence
      optimization stability.

    • Describe KV caching and how it changes inference-time cost
      compared to training-time cost.
 Common pitfalls.
    • Incorrect masking (future leakage) or inconsistent tokenization
      between train and evaluation.

    • Reporting speed or memory without stating context length, batch
      size, and caching assumptions.

    • Treating decoding strategy as an afterthought; greedy, beam, and
      sampling regimes change observed quality.




                                     300
Modern Intelligent Systems                                                 14


 Exercises and lab ideas
    • Hand-compute a 2-token attention step with masking; verify against
      a short script.

    • Implement a single-block decoder-only transformer (embed + pos +
      pre-LN MHA + FFN) and train on a tiny character corpus; report
      perplexity.

    • Compare naive attention vs. FlashAttention on n ∈ {256, 1024, 4096};
      log peak memory and tokens/sec.

    • Fine-tune a base model with RoPE vs. ALiBi and evaluate
      extrapolation to 2× the training context.

    • Implement DPO on a small preference dataset; report win-rates
      versus the SFT baseline.

 If you are skipping ahead. After this chapter, the book pivots away
 from neural sequence models, so treat this chapter as the last stop for
 masking discipline and evaluation hygiene. If you need the embedding
 objectives and bias/deployment checklist, see Chapter 13.



Where we head next. Chapter 15 steps away from neural sequence models
and re-enters the broader soft-computing toolkit (fuzzy logic and evolutionary
ideas) previewed in Chapter 1. Read this chapter as the endpoint of the neural
sequence thread: representation objectives from Chapter 13 plus masking/cali-
bration discipline from Chapters 12 to 14.




                                     301
Modern Intelligent Systems                                                      15


  Part II takeaways
     • Representation and training are coupled: expressivity is only useful if
       gradients can reach the parameters.

     • Depth and inductive bias trade parameters for structure (MLPs vs.
       CNNs vs. recurrence vs. attention).

     • Stability tools recur across architectures: initialization, normalization,
       regularization, and validation-driven stopping.

     • Sequence models turn memory into computation: unrolling, masking,
       and caching define what information can flow.




Part III: Soft computing and fuzzy
reasoning
15    Introduction to Soft Computing
Parts I–II emphasized two complementary toolkits: probabilistic modeling
and ERM (model–loss–optimize–audit), and biologically inspired learning (dis-
tributed representations trained by gradient descent). They shine when you
can write down a smooth objective and collect enough data. Many engineered
systems, however, are constrained less by data or compute than by specification:
the relevant concepts are linguistic (“too warm,” “slightly fast,” “acceptable
risk”), the boundaries are negotiable, and the decision logic must remain
auditable.
    Soft computing makes that vagueness explicit. Instead of insisting on exact
equations everywhere, we represent human concepts with graded membership
functions, combine them with transparent rules, and then tune those choices
(and their trade-offs) with optimization rather than brittle hand tweaks. The
shift is not away from rigor; it is toward placing approximations where they
belong—at the interface between messy human predicates and systems that still
have to act.



                                       302
Modern Intelligent Systems                                                      15


 Learning Outcomes
    • Articulate why soft computing (fuzzy logic, evolutionary search,
      neural hybrids) complements the statistical strand from earlier
      chapters.

    • Define fuzzy sets, linguistic variables, and rule bases at a conceptual
      level before Chapters 16 to 18 formalize them.

    • Work through a compact thermostat/autofocus controller example
      that grounds the design choices introduced throughout the fuzzy
      trilogy.

 Design motif
 When precision is costly or ill-defined, make the vagueness explicit and
 keep the system auditable: represent linguistic concepts with membership
 functions, reason with operator choices you can explain, and tune those
 choices with optimization rather than brittle rules.


Running example (thermostat). We revisit a smart thermostat that regu-
lates a room using two linguistic inputs (temperature error and rate of change)
and one output (heater power). This compact scenario returns throughout the
fuzzy trilogy: first to parameterize membership functions (Chapter 16), then to
transport labels across related universes (Chapter 17), and finally to assemble
complete inference systems (Chapter 18).

15.1   Hard Computing: The Classical Paradigm
Hard computing refers to the classical approach to computation where the goal
is to produce precise, unambiguous, and mathematically exact outputs. This
paradigm assumes that the relationships between inputs and outputs can be
modeled accurately using well-defined mathematical equations. For example,
Einstein’s mass-energy equivalence formula,

                                  E = mc2 ,                               (15.1)

is a precise, unambiguous, and exact mathematical expression.
    In hard computing, the process typically involves:

                                     303
Modern Intelligent Systems                                                     15


  • Precise inputs,

  • Deterministic models,

  • Exact outputs.
   However, this approach is often inadequate for many real-world problems
because:
  1. The real world is pervasively imprecise and uncertain.

  2. Achieving precision and certainty is often costly and diﬀicult.
   These limitations motivate the need for alternative computational frame-
works that can tolerate and exploit imprecision and uncertainty.

15.2   Soft Computing: Motivation and Definition
Soft computing, introduced by Zadeh (1994, 1997) after his 1965 fuzzy sets paper,
is a computational paradigm designed to handle problems where precision and
certainty are either impossible or prohibitively expensive to obtain. Unlike hard
computing, soft computing tolerates imprecision, uncertainty, and approximate
reasoning to achieve solutions that are:
  • Tractable: Computationally feasible to obtain,

  • Robust: Insensitive to noise and variations,

  • Low-cost: Economical in terms of computational resources.
   Formally, soft computing is not a single homogeneous methodology but
rather a partnership of distinct methods that conform to these guiding principles.
In Zadeh’s broad usage, the principal constituents include:
  • Fuzzy Logic: Handling imprecision and approximate reasoning,

  • Neurocomputing (and neuro-fuzzy hybrids): Learning from data
    through neural networks, sometimes combined with fuzzy rule bases (e.g.,
    ANFIS),

  • Genetic Algorithms: Evolutionary optimization inspired by natural se-
    lection.
   These components often overlap and complement each other in practical
applications. In this book, probabilistic modeling is treated in the statistical


                                      304
Modern Intelligent Systems                                                        15


strand (Chapters 3 to 4); the soft-computing block focuses on fuzzy systems and
evolutionary search, with neuro-fuzzy hybrids serving as the bridge back to the
neural chapters.

15.3   Why Soft Computing?
The key insight behind soft computing is to exploit the tolerance for imprecision
and uncertainty inherent in many real-world problems. Consider the example of
handwritten digit recognition using a convolutional neural network (CNN):
   • The input is a handwritten digit, say the digit ”4”.

   • The network extracts features and produces a probability distribution over
     possible digits.

   • The output might be:

          P (digit = 4) = 0.60,   P (digit = 7) = 0.20,   P (digit = 1) = 0.20.

   This output is not precise in the classical sense; it expresses uncertainty and
partial belief. The system tolerates this imprecision and still makes a decision
based on the highest probability, demonstrating robustness and flexibility.

15.4   Relationship Between Hard and Soft Computing
We can conceptualize the landscape of computing as follows:
   • Hard Computing: Precise, deterministic, mathematically exact.

   • Soft Computing: Approximate, tolerant of imprecision and uncertainty,
     heuristic.
   There is some overlap, especially in optimization problems, which can be
approached via either paradigm depending on the context and requirements.

15.5   Overview of Soft Computing Constituents
Fuzzy Logic: Deals with fuzziness or vagueness, allowing partial membership
    in sets and approximate reasoning. It is particularly useful when informa-
    tion is incomplete or linguistic in nature.

Neurocomputing: Encompasses various neural network architectures (multi-
    layer perceptrons, convolutional networks, recurrent models, Hopfield net-

                                       305
Modern Intelligent Systems                                                    15


       works, and Radial Basis Function (RBF) networks) as well as neuromor-
       phic hardware that learn from data and approximate complex nonlinear
       mappings.

Probabilistic Reasoning: Manages uncertainty using probability theory, be-
    lief networks, and Bayesian inference. It assumes known or estimable
    probability distributions.

Genetic Algorithms: Inspired by biological evolution, these algorithms per-
    form heuristic search and optimization by mimicking natural selection and
    genetic variation.

15.6    Distinguishing Imprecision, Uncertainty, and Fuzziness
It is important to clarify the subtle differences among these concepts:
   • Uncertainty refers to situations where the outcome is unknown but can
     be described probabilistically. For example, a classifier might assign a 60%
     probability to a particular class.

   • Imprecision refers to limited resolution or vagueness in the available
     descriptions or measurements. Saying that the outside temperature is
     “warm” rather than specifying 24.5◦ C is imprecise because we are unsure
     about the precise boundary that should separate “warm” from “hot.”

   • Fuzziness captures graded membership in a linguistic category; for in-
     stance, the extent to which a day is “warm.” Membership values range
     continuously between 0 and 1 instead of forcing a binary decision.
In short, imprecision concerns our knowledge about a precise boundary, whereas
fuzziness is a property of the concept itself: even with perfect measurements,
“warm” transitions smoothly into “hot.” For example, reading 24.5◦ C from a
thermometer with ±1◦ C resolution is an imprecise observation, whereas decid-
ing whether 24.5◦ C should be labelled “warm” or “hot” is a fuzzy membership
question that remains even if the thermometer were infinitely precise.




                                      306
Modern Intelligent Systems                                                    15


   Imprecision vs. Fuzziness
  Imprecision concerns uncertainty about the exact value or boundary
  (e.g., measurement error or coarse resolution). Fuzziness concerns graded
  membership in a concept (e.g., the degree to which a day is “warm”) even
  when measurements are exact. Probability quantifies uncertainty about
  events; fuzziness quantifies degree of truth of linguistic predicates.


15.7   Soft Computing: Motivation and Overview
Soft computing is not a monolithic framework but rather a coalition of distinct
methods unified by a common goal: to exploit tolerance for imprecision, uncer-
tainty, and partial truth to achieve tractability, robustness, and low solution
cost. Unlike traditional hard computing, which demands exact inputs and pro-
duces precise outputs, soft computing embraces the inherent vagueness of many
real-world problems, particularly those involving human reasoning and percep-
tion. The constituents mirror the probabilistic and connectionist tools from
Chapters 3 to 14 but favour interpretability and rule-based reasoning:
  • Fuzzy Logic: Captures human knowledge and reasoning expressed in
    linguistic terms, allowing approximate reasoning with imprecise concepts.

  • Neurocomputing (Neural Networks): Learning from data and pat-
    tern recognition; hybrids such as ANFIS (Jang, 1993) blend fuzzy rules
    with trainable neural layers.

  • Probabilistic modeling (already covered): Bayesian/MAP views
    from Chapters 3 to 4 remain complementary to fuzzy possibility views
    (Dubois and Prade, 1988), but the emphasis in this block is on rule-based
    reasoning rather than probabilistic inference.
```

### Findings
No issues spotted.

## Chunk 22/31
- Character range: 602923–631647

```text
• Genetic/Evolutionary Computation: Chapter 19 shows how evolu-
    tionary search tunes rule bases and membership parameters (Herrera and
    Lozano, 2008; Ishibuchi and Nakashima, 2007).
    Table 7 provides a quick translation from crisp logic operators to fuzzy op-
erators.




                                      307
Modern Intelligent Systems                                                              15


Table 6: Fuzzy vs. probabilistic reasoning at a glance. Use it when deciding whether
   your uncertainty is about randomness (probability) or about graded concepts
                                     (fuzziness).

                       Fuzzy logic                       Probabilistic logic
 Semantics             Degree of membership              Degree of
                       (vagueness); e.g.,                belief/uncertainty—
                       “temperature is high to           probability that an event
                       degree 0.7.”                      occurs.
 Operators             t-norms / s-norms (min,           Sum / product rules, Bayes’
                       product, max) model               theorem govern
                       AND/OR; implication via           AND/OR/conditionals.
                       fuzzy rules.
 Outputs               Fuzzy sets defuzzified to crisp   Numeric probabilities used
                       actions (e.g., heater power).     for expectation, decision
                                                         thresholds.
 Typical use           Rule bases, approximate           Stochastic modeling,
                       control, linguistic policies.     hypothesis testing, Bayesian
                                                         inference.

 Table 7: Boolean operators vs. fuzzy operators at a glance. Use it when translating
            crisp logic rules into graded operators for fuzzy inference.

                       Boolean logic                     Fuzzy logic
 AND                   min(a, b)                         t-norm (e.g., min, product)
 OR                    max(a, b)                         s-norm (e.g., max, prob.
                                                         sum)
 NOT                   1−a                               complement 1 − a


15.8    Fuzzy Logic: Capturing Human Knowledge Linguistically
One of the most compelling aspects of fuzzy logic is its ability to represent
human knowledge and experience in a linguistic form that machines can process.
Consider the everyday reasoning:

       If you wake up late and the traﬀic is congested, then you will be late.

    This statement involves vague concepts such as “late,” “congested,” and
“will be late,” which are not crisply defined but are intuitively understood by
humans. Fuzzy logic allows us to formalize such rules without requiring precise
probabilistic models or extensive training data.

                                          308
Modern Intelligent Systems                                                        15


Fuzzy Rules and Approximate Reasoning A fuzzy rule typically has the
form:
                      IF A AND B THEN C,                      (15.2)

where A, B, and C are fuzzy propositions characterized by membership functions
rather than crisp sets.
   For example:
   • A: “Wake up late” could be represented by a membership function µlate (t)
     over the waking time t.

   • B: “Traﬀic is congested” could be represented by a membership function
     µcongested (x) over traﬀic density x.

   • C: “You will be late” is the fuzzy output.
     Each membership function maps from the relevant universe of discourse to
[0, 1], i.e., µlate : R → [0, 1], so that linguistic labels become numeric degrees of
support. The fuzzy inference system combines these membership values using
t-norm operators (e.g., min, product) to model logical conjunction and s-norms
(e.g., max) to model disjunction, thereby inferring the degree to which the con-
clusion C holds. In practical systems the resulting fuzzy set is often defuzzified
(e.g., via centroid or maximum-membership methods) to obtain a single crisp
recommendation.

Advantages over Traditional Systems Traditional rule-based systems or
statistical models require precise numerical inputs or probability distributions.
In contrast, fuzzy logic:
   • Does not require exact numerical data or probability distributions.

   • Allows direct encoding of expert knowledge in natural language.

   • Handles imprecision and vagueness inherent in human concepts.

   • Provides interpretable models that align with human reasoning.

15.9    Comparison with Other Soft Computing Paradigms
Neural Networks Neural networks model complex nonlinear relationships
by learning from data. They transform input features x ∈ Rn into new feature


                                        309
Modern Intelligent Systems                                                      15


spaces through weighted sums and nonlinear activations:

                                h = σ(W⊤ x + b),                             (15.3)

where W ∈ Rn×m maps the n-dimensional input into an m-dimensional hidden
space, b ∈ Rm is the bias vector, and σ(·) is a nonlinear activation function
applied elementwise.
    Unlike fuzzy logic, neural networks require training on large datasets and do
not inherently provide interpretable linguistic rules; there is, however, an active
line of research on rule extraction and network distillation aimed at recovering
approximate linguistic descriptions from trained models.

Genetic Algorithms Genetic algorithms simulate evolutionary processes to
optimize solutions by iteratively selecting, recombining, and mutating candidate
solutions. They are useful for derivative-free optimization and problems with
complex search spaces.

Probabilistic Reasoning Probabilistic methods model uncertainty explicitly
using probability distributions and Bayesian inference. They require knowledge
or estimation of underlying distributions, which may be diﬀicult in many prac-
tical scenarios, but approximate inference schemes (e.g., Monte Carlo sampling,
variational methods) can mitigate this requirement when exact distributions are
unavailable.

15.10 Zadeh’s Insight and the Birth of Fuzzy Logic
Lotfi Zadeh, in the late 1960s, observed that classical statistics and probability
theory demand precise knowledge of distributions and exact calculations, which
is often unrealistic for human decision-making. Humans rely on approximate,
linguistic knowledge rather than exact numerical data.
    Zadeh’s key insight was to develop a mathematical framework that could:
   • Represent imprecise concepts using fuzzy sets.

   • Allow approximate reasoning with these fuzzy sets.

   • Enable machines to operate based on human-like linguistic rules.



                                       310
Modern Intelligent Systems                                                     15


    This approach revolutionized how we model uncertainty and reasoning in
artificial intelligence and control systems.

15.11 Challenges in Fuzzy Logic Systems
Despite its advantages, fuzzy logic faces several challenges:
   • Lack of a systematic methodology: Initially, there was no formal
     mechanism to construct fuzzy inference systems from human knowledge.

   • Handling imprecision in linguistic terms: Choosing membership
     functions and linguistic labels still relies on expert elicitation or data-
     driven tuning; poor choices can degrade system performance.

15.12 Mathematical Languages as Foundations for Fuzzy Logic
Recall that the motivation behind fuzzy logic was to develop a mathematical
and linguistic framework capable of handling imprecision and uncertainty in a
principled way. To achieve this, Lotfi Zadeh drew inspiration from several well-
established mathematical languages, each with its own syntax, semantics, and
rules of inference. Understanding these languages helps us appreciate how fuzzy
logic extends and generalizes classical logic to accommodate vagueness.

15.12.1   Relational Algebra
Relational algebra is a formal language used primarily in database theory to ma-
nipulate sets and relations. It provides operators such as union (∪), intersection
(∩), and set difference (\) that operate on sets:



                        A ∪ B = {x | x ∈ A or x ∈ B},                      (15.4)
                        A ∩ B = {x | x ∈ A and x ∈ B}.                     (15.5)

   The third canonical operator is the set difference

                        A \ B = {x | x ∈ A and x ∈
                                                 / B},

which removes from A any elements that also belong to B. For instance, if A is
the set of all graduate students and B the set of teaching assistants, then A \ B
contains graduate students who are not currently TAs.


                                       311
Modern Intelligent Systems                                                       15


    These operators have well-defined meanings and predictable outputs, making
relational algebra a precise language for reasoning about collections of elements.
The vocabulary is limited but suﬀicient for set-theoretic operations.

15.12.2    Boolean Algebra
Boolean algebra is the algebraic structure underlying classical logic and digital
circuits. It operates on binary variables taking values in {0, 1}, with logical
operators such as AND (∧), OR (∨), and XOR (⊕):



                         A∨B =1       if A = 1 or B = 1,                      (15.6)
                         A∧B =1       if A = 1 and B = 1,                     (15.7)
                        A⊕B =1        if A 6= B.                              (15.8)

Conversely, A ∨ B = 0 only when both inputs are 0, and A ∧ B = 0 unless both
inputs equal 1; the XOR operator returns 0 exactly when both operands share
the same truth value.
    Boolean algebra provides a crisp, binary framework where propositions are
either true or false, with no intermediate values. This crispness is a limitation
when modeling real-world phenomena involving gradations of truth.

15.12.3    Predicate Algebra
Predicate algebra extends Boolean algebra by incorporating quantifiers and vari-
ables, allowing statements about properties of elements in a domain. For exam-
ple, a predicate statement might be:

                                 ∀x ∈ R,   x2 ≥ 0,

    which reads: ”For all real numbers x, x2 is greater than or equal to zero.” This
language combines logical connectives with quantifiers such as ∀ (for all) and ∃
(there exists), enabling more expressive statements about sets and relations.
    An example involving two domains could be:

                 ∀x ∈ Rabbits,     ∀y ∈ Tortoises,   Faster(x, y),

    meaning ”For any rabbit x and any tortoise y, x is faster than y.”


                                        312
Modern Intelligent Systems                                                     15


   Predicate algebra thus provides a linguistic and symbolic framework to ex-
press complex relationships and properties.

15.12.4   Propositional Calculus
Propositional calculus (or propositional logic) deals with propositions and their
logical connectives. It focuses on the relationships between propositions without
internal structure. The basic form involves premises and conclusions, such as:



                             P =⇒ Q,     P    ⇒    Q,                       (15.9)

   where P and Q are propositions, and =⇒ denotes implication.

Modus Ponens One fundamental rule of inference in propositional calculus
is modus ponens:

     If P =⇒ Q and P is true, then Q must be true.

   Symbolically,



                             P =⇒ Q,     P    `    Q.                      (15.10)

   This rule aﬀirms the consequent by aﬀirming the antecedent.

Modus Tollens Another inference rule is modus tollens:

     If P =⇒ Q and Q is false, then P must be false.

   Symbolically,



                             P =⇒ Q,    ¬Q    `    ¬P.                     (15.11)

    This rule denies the antecedent by denying the consequent. However, as
noted, this inference can sometimes be risky or invalid in practical scenarios due
to exceptions or additional factors.


                                       313
Modern Intelligent Systems                                                       15


Hypothetical Syllogism        A further inference pattern is the hypothetical syl-
logism:

      If P =⇒ Q and Q =⇒ R, then P =⇒ R.

   Symbolically,



                    P =⇒ Q,       Q =⇒ R       `    P =⇒ R.                 (15.12)

   This transitive property of implication allows chaining of logical statements.

15.13 Fuzzy Logic as a New Mathematical Language
Zadeh’s insight was to synthesize these classical mathematical languages into a
new framework that could handle degrees of truth rather than binary true/false
values. Fuzzy logic generalizes Boolean algebra by allowing truth values to range
continuously over the interval [0, 1], representing partial truth

15.14 Fuzzy Logic: Motivation and Intuition
Recall that classical (crisp) logic deals with binary truth values: a proposition is
either true (1) or false (0). For example, the question “Was the exam easy?” can
be answered crisply as “Yes” or “No.” However, many real-world situations are
not so black-and-white. Often, we want to express uncertainty or partial truth,
such as “The exam was somewhat easy,” or “The exam was easy to a certain
degree.”

Fuzzy truth values allow us to express such intermediate degrees of truth.
Instead of restricting truth values to {0, 1}, fuzzy logic permits any value in the
continuous interval [0, 1]. For instance, if the exam was moderately easy, we
might assign a truth value of 0.6 or 0.7, indicating partial truth.
    This flexibility captures the inherent vagueness in many human concepts and
perceptions. For example, when asked “Did you enjoy your lunch?” one might
respond “sort of,” reflecting a fuzzy assessment rather than a crisp yes/no.

Why fuzzy logic?



                                       314
Modern Intelligent Systems                                                        15


   • Tolerance for imprecision: Observations and measurements are often
     noisy or uncertain.

   • Expressiveness: Allows linguistic hedging such as “somewhat,” “maybe,”
     or “approximately.”

   • Robustness: Systems can handle ambiguous or incomplete information
     gracefully.

15.15 From Crisp Sets to Fuzzy Sets
Crisp sets are classical sets where an element either belongs or does not belong
to the set. Formally, for a universe X, a crisp set A ⊆ X is characterized by its
characteristic function:              
                                      1 if x ∈ A,
                             χA (x) =
                                      0 if x ∈ / A.

Example:     Consider two classes:

        Class 1 = {Li, Rajnish},     Class 2 = {Hamid, John, Julia, Yet}.

These are crisp sets since no student belongs to both classes simultaneously.

Fuzzy sets generalize this notion by allowing partial membership. A fuzzy
set Ã on X is characterized by a membership function:

                                 µÃ : X → [0, 1],

where µÃ (x) quantifies the degree to which x belongs to Ã.

Example: Sizes as fuzzy sets
Consider the linguistic labels Small, Medium, and Large for weights (in kilo-
grams). A crisp partition such as [0, 10], [11, 20], [21, 30] is disjoint; fuzzy sets
allow these labels to overlap smoothly so a weight can belong to both Medium
and Large to different degrees. See Chapter 16 (especially Section 16.8) for the
explicit membership formulas and plots; here keep the intuition that fuzzy labels
overlap and map a universe of discourse into [0, 1].



                                        315
Modern Intelligent Systems                                                     15


Thermostat at a glance. Throughout Chapters 16 to 18 we reuse a fuzzy
thermostat: inputs are temperature error and rate (linguistic labels such as
Cold, Warm, Hot; Cooling, Stable, Heating); rules map these to heater power;
defuzzification turns the fuzzy action into a crisp control signal. Keep this loop
in mind as membership functions and operators are introduced.
 Lab prep: fuzzy thermostat starter
    • Install scikit-fuzzy and matplotlib.

    • Define triangular membership functions for Cold/Warm/Hot over a
      temperature universe; plot the overlap.

    • Write one rule: IF error is Cold AND rate is Heating THEN power is
      Low; preview centroid defuzzification.

 Exercises (Chapter 15)
    • Classify three scenarios as imprecision vs. uncertainty vs. fuzziness;
      justify each.

    • Write two fuzzy thermostat rules and reason qualitatively about the
      output for a borderline input.

    • Compare min vs. product t-norm on the same antecedent degrees
      (e.g., 0.4 and 0.7); explain the impact.

    • Sketch (or code) a triangular membership and a simple IF–THEN
      rule; describe how defuzzification would proceed.

    • Identify where probability (Chapter 3) and fuzzy possibility (this
      chapter) would lead to different interpretations.

Forward pointer. Chapter 16 builds the membership functions and universes
for the thermostat inputs/outputs; Chapters 17 to 18 assemble full inference
and defuzzification, and Chapter 19 shows how evolutionary search can tune
rule bases and memberships.

15.16 Wrapping Up Fuzzy Sets and Fuzzy Logic
In this final part of the chapter, we conclude our introduction to fuzzy sets and
fuzzy logic by summarizing key concepts and clarifying the open points from the


                                       316
Modern Intelligent Systems                                                     15


previous discussion.

Fuzzy Sets Recap Recall that a fuzzy set A defined on a universe of discourse
X is characterized by a membership function

                                µA : X → [0, 1],

which assigns to each element x ∈ X a degree of membership µA (x) indicating
the extent to which x belongs to the set A. Unlike classical (crisp) sets where
membership is binary (0 or 1), fuzzy sets allow partial membership, capturing
the inherent vagueness of many real-world concepts.

Universe of Discourse The universe of discourse X is the domain over which
fuzzy sets are defined. For example, if X represents the set of all students,
fuzzy subsets could be “tall students,” “medium height students,” and “short
students,” each with overlapping membership functions reflecting the subjective
nature of these categories.

Fuzziness and Degrees of Truth Fuzzy logic extends classical Boolean logic
by allowing truth values to range continuously between 0 and 1. This enables
reasoning with imprecise or approximate information, such as the statement “the
water is warm,” which is neither absolutely true nor false but has a degree of
truthfulness.

Example: Height Classification Consider the linguistic variables “short,”
“medium,” and “tall.” In classical logic, a person is either short or not, tall
or not, with crisp boundaries. In fuzzy logic, these categories overlap, and a
person’s height can partially belong to multiple categories simultaneously. This
reflects human intuition and natural language better than crisp sets.

Fuzzy Actions and Control In intelligent control systems, such as auto-
motive braking, fuzzy logic allows the control actions to be fuzzy themselves.
Instead of a binary decision to “hit the brakes” or “not hit the brakes,” the sys-
tem can decide to apply the brakes “somewhat,” “moderately,” or “strongly,”



                                      317
Modern Intelligent Systems                                                15


based on fuzzy inputs like distance and speed. This leads to smoother, more
adaptive control.

Next Steps: Membership Functions and Fuzzy Inference Systems
Chapters 16 to 18 pick up the thermostat running example and formalize each
stage: Chapter 16 constructs the membership functions for error/rate labels,
Chapter 17 shows how relations and projections move information between uni-
verses, and Chapter 18 assembles the full Mamdani/Sugeno inference pipeline.
Keep this soft-computing overview handy as a conceptual map while those chap-
ters work through the algebra.




                                    318
Modern Intelligent Systems                                                     15


 Key takeaways
    • Soft computing embraces imprecision via fuzzy logic, evolutionary
      search, and neural networks.

    • Fuzzy operators (t-norms, implications) enable approximate
      reasoning under uncertainty.

    • Choosing operators and membership functions matches problem
      semantics to inference behavior.

 Minimum viable mastery.
    • Define what is being approximated (truth values, search steps, or
      function classes) in each soft-computing pillar.

    • Explain why operator choices matter (they encode semantics and
      shape the resulting decision surfaces).

    • Connect fuzzy-set primitives to the later inference pipeline (fuzzify,
      combine, imply, aggregate, defuzzify).
 Common pitfalls.
    • Mixing operator families inconsistently across a pipeline and then
      debugging symptoms at the end.

    • Treating “soft” as a license to skip validation: soft methods still
      require measurable objectives and checks.

    • Ignoring scaling and units when defining universes and membership
      functions.




                                      319
Modern Intelligent Systems                                                     16


 Exercises and lab ideas
     • Implement a minimal example from this chapter and visualize
       intermediate quantities (plots or diagnostics) to match the
       pseudocode.

     • Stress-test a key hyperparameter or design choice discussed here and
       report the effect on validation performance or stability.

     • Re-derive one core equation or update rule by hand and check it
       numerically against your implementation.

 If you are skipping ahead. When you reach Chapters 16 to 18, keep the
 operator choices explicit and consistent. Many formatting and
 interpretation problems later come from hidden operator defaults.


Where we head next. Chapters 16 to 18 carry the thermostat running exam-
ple end-to-end: Chapter 16 builds membership functions, Chapter 17 transports
information across universes through relations, and Chapter 18 assembles full
inference plus defuzzification.


16    Fuzzy Sets and Membership Functions: Founda-
      tions and Representations
Building on Chapter 15, we formalize the foundations of fuzzy logic: universes of
discourse, fuzzy sets, membership functions, and the operators used throughout
the fuzzy trilogy. These tools define the thermostat labels used later and prepare
the transfer/inference steps developed in Chapters 17 to 18.




                                       320
Modern Intelligent Systems                                                      16


  Learning Outcomes
  After this chapter, you should be able to:
     • Distinguish imprecision (uncertain value/boundary) from fuzziness
       (graded membership).

     • Define and interpret membership functions in discrete and continuous
       domains.

     • Apply fuzzy set operations and De Morgan’s laws using max/min
       forms.

     • Execute an end-to-end Mamdani inference and compute the centroid
       defuzzification.

  Design motif
  Treat vagueness as a first-class modeling choice: write the membership
  functions down, pick operators explicitly, and then audit how those choices
  shape the behavior of a rule base.


Running example checkpoint. For the thermostat scenario introduced in
Chapter 15, the universe of discourse for the inputs is [−5, 5]◦ C temperature
error and [−2, 2]◦ C/min rate-of-change. As you study triangular, trapezoidal,
and Gaussian membership functions, imagine parameterizing the linguistic labels
Cold, Comfy, and Hot for these inputs. We reuse those shapes when composing
rules in Chapters 17 to 18.

16.1   Motivating example:           designing a membership function
       from measurements
Consider the thermostat’s temperature error e = Troom − Tset in degrees Celsius
(so e < 0 means “too cold”). We want a linguistic label Cold that is clearly true
when the room is far below setpoint, clearly false when the room is at/above
setpoint, and graded in between. A simple, auditable choice is a piecewise-linear




                                      321
Modern Intelligent Systems                                                          16


“shoulder” membership:
                                        
                                        
                                                   e ≤ −4,
                                        1,
                          µCold (e) =     0−e
                                                ,   −4 < e < 0,                 (16.1)
                                        
                                        
                                           4
                                        
                                          0,        e ≥ 0.

With this design, e = −2 yields µCold (−2) = 0.5: “cold” is half true. Later chap-
ters reuse this shoulder shape but may shift its breakpoints to reflect different
sensors, comfort bands, or operating assumptions. This number is not a proba-
bility; it is a degree of truth for a linguistic predicate. The rest of this chapter is
about making these mappings explicit (shapes, overlaps, and operators) so they
can be inspected and tuned rather than assumed.

16.2    Fuzzy sets and the universe of discourse
A fuzzy set A in a universe of discourse X is characterized by a membership
function µA : X → [0, 1]. This membership function assigns to each element
x ∈ X a degree of membership µA (x), which quantifies the extent to which x
belongs to the fuzzy set A.
   • If µA (x) = 1, then x fully belongs to A.

   • If µA (x) = 0, then x does not belong to A at all.

   • If 0 < µA (x) < 1, then x partially belongs to A to the degree µA (x).
    This contrasts with classical (crisp) sets, where membership is binary (either
0 or 1).

16.3    Membership Functions: Definition and Interpretation
A membership function µA (x) maps each element x in the universe X to a
membership grade in the interval [0, 1]. The shape and parameters of µA encode
the fuzziness or uncertainty associated with the concept represented by A.

Example: Consider the fuzzy set Slow Speed defined over the universe of
speeds X ⊆ R. The membership function µSlow (x) might assign high member-
ship values to speeds near 20 km/h and gradually decrease as speed increases,
reflecting the gradual transition from ”slow” to ”not slow.”


                                          322
Modern Intelligent Systems                                                                  16


Mathematical Representation: For each x ∈ X,

                                       µA (x) ∈ [0, 1].                                 (16.2)

    The fuzzy set A can be represented as the collection of ordered pairs:

                               A = {(x, µA (x)) | x ∈ X}.                               (16.3)

16.4     Discrete vs. Continuous Universes of Discourse
The universe X can be either discrete or continuous, which affects how fuzzy
sets and membership functions are represented.

16.4.1    Discrete Universe
When X = {x1 , x2 , . . . , xn } is finite or countable, the fuzzy set A is represented
as a finite collection of ordered pairs:

                A = {(x1 , µA (x1 )), (x2 , µA (x2 )), . . . , (xn , µA (xn ))}.        (16.4)

   Typically, membership values equal to zero are omitted for brevity, since
they indicate no membership.

Example:       Suppose X = {1, 2, 3, 4, 5} and the membership function values are:

       µA (1) = 0,   µA (2) = 0.1,      µA (3) = 0.3,      µA (4) = 0.7,      µA (5) = 0.

Then,
                             A = {(2, 0.1), (3, 0.3), (4, 0.7)}.

16.4.2    Continuous Universe
When X ⊆ R is continuous (e.g., an interval), the fuzzy set A is described
by a membership function µA (x) defined for all x ∈ X. The representation is
functional rather than enumerative:
                                  Z
                             A=       µA (x)/x,                       (16.5)
                                           x∈X
                         R
where the notation           µA (x)/x denotes the continuous collection of pairs
(x, µA (x)).

                                             323
Modern Intelligent Systems                                                    16
```

### Findings
No issues spotted.

## Chunk 23/31
- Character range: 631651–659424

```text
Interpretation: The integral sign here is symbolic, indicating a continuous
aggregation over X, not a numerical integral in the calculus sense.

Example:     Consider a triangular membership function centered at c with base
width w:                                              
                                             |x − c|
                         µA (x) = max 0, 1 −               .              (16.6)
                                                w
This function assigns membership 1 at x = c, decreasing linearly to zero at
x = c ± w.

16.5   Crisp Sets versus Fuzzy Sets
Crisp (classical) sets assign membership values in the binary set {0, 1}, so each
element either belongs to the set or it does not. In contrast, fuzzy sets allow
intermediate membership values, enabling gradual transitions between full inclu-
sion and full exclusion. Understanding this contrast highlights why membership
functions are central to fuzzy logic.
   Imprecision vs. Fuzziness (recap)

   As discussed in Section 15.6, imprecision concerns uncertainty about the
   exact value or boundary (e.g., measurement noise or coarse resolution),
   whereas fuzziness concerns graded membership in a concept (e.g., the
   degree to which a speed is “slow”) even when measurements are exact.
   Probability models uncertainty about events; fuzzy logic models degrees
   of truth of linguistic predicates.


16.6   Membership Functions in Fuzzy Sets
With the universe X fixed and the concept A named, the membership function
µA : X → [0, 1] assigns to each element x ∈ X a degree of membership µA (x)
indicating the extent to which x belongs to A.

Triangular Membership Function One of the simplest and most intuitive
membership functions is the triangular membership function. It is defined by




                                       324
Modern Intelligent Systems                                                   16


three parameters a < b < c and given by
                                     
                                     
                                      0,    x≤a
                                     
                                     
                                     
                                      x−a , a < x ≤ b
                             µA (x) = b−a                                 (16.7)
                                     
                                      c−x
                                     
                                      c−b , b < x < c
                                     
                                     
                                       0,    x≥c

This function attains its maximum value 1 at x = b, representing the point of
highest confidence that x belongs to the fuzzy set A. The membership decreases
linearly on either side of b, reaching zero at a and c. This shape expresses a
strong belief in membership near b and uncertainty elsewhere.

Trapezoidal Membership Function The trapezoidal membership function
generalizes the triangular shape by allowing a flat top, representing a range of
values with full membership. It is defined by four parameters a < b ≤ c < d:
                                     
                                     
                                      0,      x≤a
                                     
                                     
                                     
                                     
                                     
                                     
                                       x−a
                                               a<x≤b
                                      b−a ,
                             µA (x) = 1,       b<x≤c                      (16.8)
                                     
                                     
                                     
                                     
                                     
                                     
                                       d−x
                                       d−c ,   c<x<d
                                     
                                     
                                     0,       x≥d

This function models situations where there is full confidence that all values
between b and c belong to the fuzzy set, with gradual transitions on the edges.

Gaussian Membership Function The Gaussian membership function is
widely used due to its smoothness and differentiability, which are advantageous
in optimization and learning algorithms. It is defined by parameters c (center)
and σ > 0 (width):                                
                                          (x − c)2
                          µA (x) = exp −             .                    (16.9)
                                            2σ 2
This bell-shaped curve smoothly assigns membership values, with the highest
membership at x = c and decreasing membership as x moves away from c. The
parameter σ controls the spread or fuzziness of the set.


                                        325
Modern Intelligent Systems                                                             16


Generalized Bell Membership Function Another flexible membership
function is the generalized bell function, defined by parameters a, b, c:

                                                  1
                                 µA (x) =             2b
                                                           .                       (16.10)
                                            1 + x−c
                                                 a

This function allows control over the width and slope of the membership curve,
interpolating between shapes similar to triangular and Gaussian functions.

16.7    Comparison of Membership Functions
  • Triangular and Trapezoidal: These are piecewise linear, computation-
    ally inexpensive, and easy to interpret. However, they are not differen-
    tiable at the vertices, which can be a limitation in gradient-based learning.

  • Gaussian and Bell: These are smooth and differentiable, making them
    suitable for optimization and adaptive systems. They provide more mod-
    eling flexibility but are computationally more expensive.

Example: Grading System as Fuzzy Sets Consider a typical university
grading scale as an example of fuzzy sets. Traditional crisp sets assign grades
as follows:

       F : [0, 59],   D : [60, 69],   C : [70, 79],   B : [80, 89],   A : [90, 100].

In a crisp set, membership is binary: a score of 75 is fully in C and not in B.
    However, students and instructors may perceive these boundaries differently.
For example, some may consider 75 to be a borderline B, or 68 to be a borderline
C. This uncertainty can be modeled by fuzzy sets with overlapping membership
functions.




                                            326
Modern Intelligent Systems                                                       16


   For instance, the membership function for grade C could be trapezoidal:
                                         
                                         
                                          0,            x ≤ 65,
                                         
                                         
                                         
                                          x − 65
                                         
                                                 ,      65 < x ≤ 70,
                                         
                                          5
                                 µC (x) = 1,             70 < x ≤ 75,
                                         
                                         
                                         
                                          80 − x
                                         
                                                 ,      75 < x ≤ 80,
                                         
                                             5
                                         
                                         0,             x > 80.

Similarly, the membership for grade B could be written as
                                         
                                         
                                          0,            x ≤ 75,
                                         
                                         
                                         
                                          x − 75
                                         
                                                 ,      75 < x ≤ 80,
                                         
                                          5
                                 µB (x) = 1,             80 < x ≤ 85,
                                         
                                         
                                         
                                          90 − x
                                         
                                                 ,      85 < x ≤ 90,
                                         
                                             5
                                         
                                         0,             x > 90,

with analogous expressions for the A and D categories. These overlapping trape-
zoids capture the intuition that a borderline score (e.g., 79) can simultaneously
belong to both C and B to different degrees, as sketched in Figure 64.

                           1
                                   Grade C
             Membership




                                   Grade B

                                                   overlap
                          0.5




                           0
                            60     65        70   75           80   85   90
                                                       Score

    Figure 64: Trapezoidal membership functions for grades C and B with the
     overlapping region shaded. Scores near 78–82 partially satisfy both grade
      definitions. Use it when designing overlapping grade/linguistic bins so
                          boundary cases behave smoothly.

   Figure 65 is the overlap diagnostic used when tuning membership coverage.


                                                  327
Modern Intelligent Systems                                                        16


16.8    Example: Overlapping weight labels
Fuzzy labels often overlap so that borderline values belong to multiple sets. For
weights measured in kilograms, one crisp partition is [0, 10], [11, 20], [21, 30] for
Small, Medium, Large. A fuzzy partition smooths these transitions:
                                
                                
                                 1,            x ≤ 10,
                                
                                
                                      x − 10
                    µSmall (x) = 1 −         , 10 < x < 15,
                                
                                       5
                                
                                0,             x ≥ 15,
                                  
                                  
                                   0,           x ≤ 10,
                                  
                                  
                                  
                                   x − 10
                                  
                                          ,     10 < x < 15,
                                  
                                   5
                     µMedium (x) = 1,            15 ≤ x ≤ 20,
                                  
                                  
                                  
                                   25 − x
                                  
                                          ,     20 < x < 25,
                                  
                                      5
                                  
                                  0,            x ≥ 25,
and                                
                                   
                                    0,         x ≤ 20,
                                   
                                   
                                     x − 20
                      µLarge (x) =          ,   20 < x < 25,
                                   
                                       5
                                   
                                   1,          x ≥ 25.
The overlap reflects the vagueness of the labels: a weight near 22 kg partially
satisfies both Medium and Large.
    Figure 66 compares operator shapes when choosing conjunction behavior in
rule aggregation.

Quick plotting snippet. With scikit-fuzzy or plain matplotlib you can
visualize overlaps to debug label choices:

import numpy as np, matplotlib.pyplot as plt
x = np.linspace(0, 30, 400)
mu_small = np.clip(1 - (x-10)/5, 0, 1) * (x <= 15)
mu_med    = np.clip((x-10)/5, 0, 1) * (x < 15)
mu_med   += ((x>=15) & (x<=20))
mu_med   += np.clip((25-x)/5, 0, 1) * (x > 20)

                                        328
Modern Intelligent Systems                                                                  16


                                               Small       Medium     Large

                              1
         Membership degree



                             0.5




                              0
                                   0    5       10           15      20       25   30
                                                       Weight (kg)

     Figure 65: Overlapping membership functions for the “Small”, “Medium”,
     and “Large” weight labels. The shaded overlaps capture gradual transitions.
      Use it when tuning membership overlaps so small numeric changes do not
                             cause abrupt rule changes.


mu_large = np.clip((x-20)/5, 0, 1)
plt.plot(x, mu_small, label="Small")
plt.plot(x, mu_med, label="Medium")
plt.plot(x, mu_large, label="Large")
plt.legend(); plt.show()

16.9   Fuzzy Sets: Core Concepts and Terminology
Recall that a fuzzy set A on a universe X is characterized by a membership
function µA : X → [0, 1], where µA (x) quantifies the degree to which element x
belongs to A. Unlike crisp sets, where membership is binary (0 or 1), fuzzy sets
allow partial membership.

Support Set The support of a fuzzy set A is the set of all elements with
nonzero membership:

                                       supp(A) = {x ∈ X | µA (x) > 0}.                  (16.11)

This set captures all elements that belong to A to some degree.




                                                       329
Modern Intelligent Systems                                                      16


Core Set     The core of A is the set of elements fully belonging to A:

                        core(A) = {x ∈ X | µA (x) = 1}.                    (16.12)

The core set generalizes the notion of crisp membership to fuzzy sets.

Normality A fuzzy set A is said to be normal if there exists at least one
element x ∈ X such that µA (x) = 1. Otherwise, A is subnormal. Normality
ensures the fuzzy set has at least one element fully included.

Crossover Points For many membership functions, especially triangular or
trapezoidal shapes, the crossover points c−      +
                                          A and cA are defined as the points
where the membership function crosses the value 0.5:

                             µA (c−          +
                                  A ) = µA (cA ) = 0.5.                    (16.13)

These points are useful for interpreting the ”core region” and the ”fuzzy bound-
ary” of the set.

Open and Closed Fuzzy Sets - A left-shoulder set reaches membership 1
for suﬀiciently small x and then decreases smoothly (useful for labels such as
“Very Cold”). - A right-shoulder set mirrors this behavior for large x (e.g., “Very
Hot”). - A closed fuzzy set has a membership function that attains 1 only on a
bounded interval, typically forming a trapezoidal or triangular shape.
    These distinctions help in modeling asymmetric uncertainties or preferences.

16.10 Probability vs. Possibility
It is crucial to distinguish between probability and possibility when interpreting
membership functions:
   • Probability measures the likelihood of an event occurring based on fre-
     quency or relative occurrence in repeated trials. Probabilities of mutually
     exclusive and exhaustive events sum to 1:
                                     X
                                          P (Ei ) = 1.
                                      i




                                          330
Modern Intelligent Systems                                                     16


     For example, the probability that a ball drawn from a bag is red, blue, or
     black sums to 1.

  • Possibility, on the other hand, measures the degree of plausibility or
    evidence supporting an event, without requiring additivity or summation
    to 1. Possibility values reflect uncertainty or vagueness rather than fre-
    quency. For example, a doctor’s confidence in a surgery’s success might
    be expressed as a possibility of 0.75, indicating a degree of belief rather
    than a statistical frequency.
    Thus, membership functions in fuzzy sets represent possibility rather than
probability. This distinction is fundamental in fuzzy logic and inference (cf. Ta-
ble 6 in Chapter 15). When treating a membership as a possibility distribution
π(x), we usually normalize so that supx π(x) = 1, yielding Π(A) = supx∈A π(x)
and N (A) = 1 − Π(Ac ).
 Alpha-cuts, convexity, and fuzzy numbers
    • Alpha-cut: Aα = {x ∈ X | µA (x) ≥ α} for α ∈ (0, 1]; A0 is the
      support. Alpha-cuts turn fuzzy sets into nested crisp sets.

    • Convex fuzzy set: A is convex if every alpha-cut Aα is convex.
      Normal + convex fuzzy sets with bounded support are called fuzzy
      numbers.

    • Why it matters: Alpha-cuts commute with many
      continuous/monotone maps, making them a practical tool for the
      extension principle (Chapter 17) and for defuzzification (centroid in
      Chapter 18).




                                       331
Modern Intelligent Systems                                                        16


16.11 Fuzzy Set Operations
 Operator defaults used in Chapters 16 to 18
 Unless stated otherwise, the fuzzy trilogy uses the standard operators:
    • Complement (negation): C(µ) = 1 − µ (so C(C(µ)) = µ).

    • Intersection and union: Tmin (a, b) = min(a, b), Smax (a, b) = max(a, b).

    • De Morgan’s laws are interpreted with this standard complement.
 Alternative t-/s-norms or complements are called out explicitly when they
 appear.

 Notation handoff
 In the fuzzy trilogy, µA (x) always denotes membership grade, T denotes a
 t-norm when generalized conjunction is needed, and S denotes an s-norm
 for generalized union. If these symbols clash with other parts, use the local
 chapter meaning and consult Appendix D.

   Fuzzy logic introduces operations on fuzzy sets that generalize classical set
operations but operate on membership functions. Let A and B be fuzzy sets on
X with membership functions µA and µB .

Union The union A ∪ B is defined by the membership function:
                                                     
                        µA∪B (x) = max µA (x), µB (x) .                    (16.14)

This generalizes the classical union by taking the maximum membership degree
at each element.

Intersection The intersection A ∩ B is defined by:
                                                     
                        µA∩B (x) = min µA (x), µB (x) .                    (16.15)

This corresponds to the minimum membership degree, reflecting the degree to
which x belongs to both sets.




                                      332
Modern Intelligent Systems                                                     16


Complement The complement Ac is given by:

                               µAc (x) = 1 − µA (x).                      (16.16)

This generalizes the classical complement by inverting the membership degree.
Parameterized complements Cλ (e.g., Yager, Sugeno classes) are sometimes
used to alter the “steepness” of the negation; they rarely satisfy involution
(C(C(x)) = x). A common Sugeno form is

                                         1−µ
                             Cp (µ) =          ,   p ≥ 0,
                                        1 + pµ

which preserves Cp (0) = 1 and Cp (1) = 0 but is involutive only when p = 0.
Whenever strict involution is required (as in many De Morgan identities), we
default to the standard complement C(µ) = 1 − µ.

Remarks These operations satisfy properties analogous to classical set theory
but adapted to fuzzy membership values. For completeness, De Morgan’s laws
in fuzzy logic can be written either as equivalences between sets or explicitly in
max/min form:
                                                                
         µ(A∩B)c (x) = µAc ∪B c (x) = max 1 − µA (x), 1 − µB (x) ,        (16.17)
                                                                
         µ(A∪B)c (x) = µAc ∩B c (x) = min 1 − µA (x), 1 − µB (x) .        (16.18)

Throughout the book we adopt ∧ = min and ∨ = max as the default t-/s-norm
pair with the standard complement 1 − µ (the De Morgan triple used again in
Chapter 18 unless noted otherwise); alternative norms appear later in operator
tables.

Reminder on basic operators Equations (16.14) to (16.16) already define
the max/min/standard-complement pair that we use by default. Rather than
restate them, we emphasise their practical role: unions aggregate rule conse-
quents, intersections combine antecedents, and complements capture linguistic
negations. The thermostat example later in the chapter uses these defaults
unless stated otherwise.




                                         333
Modern Intelligent Systems                                                     16


16.12 Graphical Interpretation
For continuous universes, the union and intersection membership functions can
be visualized as the pointwise maximum and minimum of the two membership
curves, respectively. The complement is obtained by reflecting the membership
function about the horizontal line µ = 0.5: every membership degree m is
mapped to 1 − m.

16.13 Additional Fuzzy Set Operations
Beyond the basic operations, several other algebraic operations are defined on
fuzzy sets:

Algebraic Product The algebraic product of fuzzy sets A and B is defined
by the product of their membership values:

                      µA·B (x) = µA (x) · µB (x),   ∀x ∈ X.             (16.19)

Scalar Multiplication Given a scalar α ∈ [0, 1], scalar multiplication of a
fuzzy set A is:
                     µαA (x) = α · µA (x), ∀x ∈ X.                   (16.20)

Algebraic Sum The algebraic sum of fuzzy sets A and B is given by:

         µA+B (x) = µA (x) + µB (x) − µA (x) · µB (x),   ∀x ∈ X.        (16.21)

This operation ensures the resulting membership values remain within [0, 1].

Difference The difference between fuzzy sets A and B, denoted A − B, can
be defined as:
                                                             
       µA−B (x) = µA (x) ∧ 1 − µB (x) = min µA (x), 1 − µB (x) ,        (16.22)

where ∧ denotes the minimum operator.

Bounded Difference An alternative definition of difference is the bounded
difference:
                                                  
                 µA⊖B (x) = max 0, µA (x) − µB (x) .               (16.23)

                                       334
Modern Intelligent Systems                                                                  16


Remarks:
  • The difference operation in (16.22) corresponds to the intersection of A
    with the complement of B.

  • The bounded difference in (16.23) ensures membership values remain non-
    negative.

  • These operations extend classical set difference to fuzzy sets, but their
    interpretations can vary depending on the application.

16.14 Example: Union and Intersection of Fuzzy Sets
Consider two fuzzy sets

16.15 Cartesian Product of Fuzzy Sets
Recall that fuzzy sets are characterized by membership functions assigning to
each element a membership grade in [0, 1]. When dealing with two fuzzy sets A
and B defined on universes X and Y respectively, the Cartesian product A × B
is a fuzzy relation on the product space X × Y .

Definition:    The membership function of the Cartesian product A × B is de-
fined as
                                               
               µA×B (x, y) = min µA (x), µB (y) ,          ∀x ∈ X, y ∈ Y.             (16.24)

    This operation generalizes the classical Cartesian product of crisp sets to
fuzzy sets by taking the minimum membership grade of the paired elements.

Example:      Suppose

    A = {(x1 , 1.0), (x2 , 0.8), (x3 , 0.4)},   B = {(y1 , 0.6), (y2 , 0.8), (y3 , 1.0)}.

Then the Cartesian product A × B is represented by the matrix of membership
values:

   µA×B (x, y)         y1                  y2                  y3
      x1       min(1.0, 0.6) = 0.6 min(1.0, 0.8) = 0.8 min(1.0, 1.0) = 1.0
      x2       min(0.8, 0.6) = 0.6 min(0.8, 0.8) = 0.8 min(0.8, 1.0) = 0.8
      x3       min(0.4, 0.6) = 0.4 min(0.4, 0.8) = 0.4 min(0.4, 1.0) = 0.4


                                            335
Modern Intelligent Systems                                                    16


  Note that the Cartesian product lifts the fuzzy sets from one-dimensional
membership functions to a two-dimensional fuzzy relation.

16.16 Properties of Fuzzy Set Operations
The fuzzy set operations (union, intersection, complement) satisfy several impor-
tant algebraic properties analogous to classical set theory, but defined in terms
of membership functions.

Commutativity:

                                µA∩B (x) = µB∩A (x),                     (16.25)
                                µA∪B (x) = µB∪A (x).                     (16.26)

Associativity:

                             µ(A∩B)∩C (x) = µA∩(B∩C) (x),                (16.27)
                             µ(A∪B)∪C (x) = µA∪(B∪C) (x).                (16.28)

Distributivity:

                        µA∪(B∩C) (x) = µ(A∪B)∩(A∪C) (x),                 (16.29)
                        µA∩(B∪C) (x) = µ(A∩B)∪(A∩C) (x).                 (16.30)

Identity Elements:

                                  µA∪∅ (x) = µA (x),                     (16.31)
                                  µA∩X (x) = µA (x),                     (16.32)

where ∅ is the empty fuzzy set with membership zero everywhere, and X is the
universal fuzzy set with membership one everywhere.

Involution:
                                 µ(Ac )c (x) = µA (x),                   (16.33)

In operator notation this reads C(C(µA (x))) = µA (x): applying the comple-
ment twice recovers the original membership degree. For the standard fuzzy

                                         336
Modern Intelligent Systems                                                    16


complement C(µA (x)) = 1 − µA (x), involution is just the identity
                                           
                             1 − 1 − µA (x) = µA (x),

so the membership “returns” to its original value after two applications.

De Morgan’s Laws: With the standard complement Ac and the max/min
operators in Equations (16.14) to (16.16), the classical De Morgan identities
hold: (A ∩ B)c = Ac ∪ B c and (A ∪ B)c = Ac ∩ B c .
    These properties ensure that fuzzy set operations behave in a consistent and
algebraically sound manner, enabling the extension of classical set theory to
fuzzy logic.
```

### Findings
1. Equation (16.10) Generalized Bell Membership Function:

- The formula is given as:

  \[
  \mu_A(x) = \frac{1}{1 + \left|\frac{x - c}{a}\right|^{2b}}
  \]

- However, the text shows:

  \[
  \mu_A(x) = \frac{1}{1 + x - c \over a^{2b}}
  \]

  which is incorrect or at least incomplete/misformatted.

- The standard generalized bell function is:

  \[
  \mu_A(x) = \frac{1}{1 + \left|\frac{x - c}{a}\right|^{2b}}
  \]

- The current notation is ambiguous and mathematically incorrect as written.

**Recommendation:** Correct the formula to the standard form with absolute value and exponentiation.

---

2. Membership function definitions for trapezoidal and triangular functions (Equations 16.7 and 16.8):

- The piecewise definitions are given with some formatting issues (e.g., missing braces or unclear line breaks), but the mathematical content is correct.

- However, in the triangular membership function (16.7), the function is defined as:

  \[
  \mu_A(x) = \begin{cases}
  0, & x \leq a \\
  \frac{x - a}{b - a}, & a < x \leq b \\
  \frac{c - x}{c - b}, & b < x < c \\
  0, & x \geq c
  \end{cases}
  \]

- The text has some formatting issues but the formula is correct.

---

3. In the trapezoidal membership function (16.8), the piecewise function is:

  \[
  \mu_A(x) = \begin{cases}
  0, & x \leq a \\
  \frac{x - a}{b - a}, & a < x \leq b \\
  1, & b < x \leq c \\
  \frac{d - x}{d - c}, & c < x < d \\
  0, & x \geq d
  \end{cases}
  \]

- The text formatting is somewhat confusing but the formula is mathematically correct.

---

4. In the grading system example, the trapezoidal membership functions for grades C and B are given with piecewise definitions.

- The formulas for µ_C(x) and µ_B(x) have formatting issues (e.g., misplaced braces, line breaks), but the mathematical expressions are correct.

- For example, for µ_C(x):

  \[
  \mu_C(x) = \begin{cases}
  0, & x \leq 65 \\
  \frac{x - 65}{5}, & 65 < x \leq 70 \\
  1, & 70 < x \leq 75 \\
  \frac{80 - x}{5}, & 75 < x \leq 80 \\
  0, & x > 80
  \end{cases}
  \]

- Similarly for µ_B(x).

---

5. In the fuzzy weight labels example, the membership functions for Small, Medium, and Large are given.

- The function µ_Small(x) is:

  \[
  \mu_{\text{Small}}(x) = \begin{cases}
  1, & x \leq 10 \\
  1 - \frac{x - 10}{5}, & 10 < x < 15 \\
  0, & x \geq 15
  \end{cases}
  \]

- µ_Medium(x) and µ_Large(x) are similarly defined.

- The text has some formatting issues (e.g., repeated braces, misplaced line breaks), but the formulas are mathematically correct.

---

6. Python snippet for plotting membership functions:

- The code uses np.clip and logical indexing to define membership functions.

- The line:

  ```python
  mu_med    = np.clip((x-10)/5, 0, 1) * (x < 15)
  mu_med   += ((x>=15) & (x<=20))
  mu_med   += np.clip((25-x)/5, 0, 1) * (x > 20)
  ```

- The second line adds a boolean array ((x>=15) & (x<=20)) which is True/False, implicitly cast to 1/0 in addition.

- This is acceptable in numpy but could be clearer if explicitly cast to float.

- No major reproducibility risk here.

---

7. Equation (16.13) Crossover points:

- The notation:

  \[
  \mu_A(c_A^-) = \mu_A(c_A^+) = 0.5
  \]

- The text writes:

  \[
  \mu_A(c_A^- +) = \mu_A(c_A) = 0.5
  \]

- The notation is unclear and inconsistent.

- Standard notation is to denote two crossover points \( c_A^- \) and \( c_A^+ \) where membership equals 0.5.

- The text should clarify this notation.

---

8. Equation (16.17) and (16.18) De Morgan's laws:

- The equations are:

  \[
  \mu_{(A \cap B)^c}(x) = \mu_{A^c \cup B^c}(x) = \max(1 - \mu_A(x), 1 - \mu_B(x))
  \]

  \[
  \mu_{(A \cup B)^c}(x) = \mu_{A^c \cap B^c}(x) = \min(1 - \mu_A(x), 1 - \mu_B(x))
  \]

- The text uses the notation \( \max 1 - \mu_A(x), 1 - \mu_B(x) \) without parentheses, which can be confusing.

- Parentheses should be added for clarity.

---

9. Equation (16.10) again:

- The formula is missing absolute value and exponentiation, which is critical.

- This is a concrete mathematical error.

---

10. Minor: In the explanation of the complement operator Cp(µ), the text says "they rarely satisfy involution (C(C(x)) = x)".

- The notation C(C(x)) = x is ambiguous because C is defined on membership values µ, not on elements x.

- It should be written as \( C(C(\mu)) = \mu \).

---

**Summary of concrete issues:**

- **(1)** Equation (16.10) Generalized Bell Membership Function is incorrect/misformatted; missing absolute value and exponentiation.

- **(2)** Notation for crossover points in (16.13) is unclear and inconsistent; should clarify \( c_A^- \) and \( c_A^+ \).

- **(3)** Parentheses missing in De Morgan's laws (16.17) and (16.18) around max and min arguments.

- **(4)** Minor notation inconsistency in complement operator Cp(µ) explanation.

- **(5)** Formatting issues in piecewise function definitions (triangular, trapezoidal, grading functions) but mathematically correct.

No other mathematical or reproducibility issues spotted.

## Chunk 24/31
- Character range: 659427–685219

```text
16.17 Fuzzy Set Operators
While operations such as union, intersection, and complement define how to com-
bine or modify fuzzy sets, operators formalize the logic or rules by which these
combinations occur. Operators are mappings that take one or more fuzzy sets
and produce another fuzzy set, often encapsulating specific logical or algebraic
behavior.

Examples of Operators:
  • Equality operator: Checks if two fuzzy sets are equal by comparing
    membership functions.

16.18 Complement Operators in Fuzzy Logic
In classical logic, the complement of a proposition A is simply 1 − µA (x), where
µA (x) is the membership function of A. However, in fuzzy logic, this complement
operation can be generalized to allow more flexible modeling of uncertainty and
partial membership.

Standard Complement The standard complement operator is defined as:
the standard fuzzy negation C(µ) = 1 − µ, so µAc (x) = 1 − µA (x) as in Equa-
tion (16.16). This operator is linear and intuitive but may not capture all nu-
ances of uncertainty.



                                       337
Modern Intelligent Systems                                                       16


Parameterized Complement Operators To generalize the complement,
choose a negation operator Cp : [0, 1] → [0, 1] and apply it pointwise:
µCp (A) (x) = Cp (µA (x)). One common (Sugeno-type) family is

                                         1−µ
                             Cp (µ) =          ,     p ≥ 0,                  (16.34)
                                        1 + pµ

which reduces to the standard complement when p = 0.
   Another simple family is a power-law negation:

                             Cp (µ) = (1 − µ)p ,     p > 0,                  (16.35)

which recovers the standard complement when p = 1 and adjusts the steepness
for other p.
    These operators allow for a nonlinear mapping of the complement, reflecting
different degrees of confidence or hesitation in the membership values. Unlike the
standard complement, most parameterized families do not preserve involution
C(C(µ)) = µ for arbitrary p; they are typically designed to satisfy boundary
conditions and monotonicity instead. When strict involution is required, it is
safest to use the standard complement.

Properties of Complement Operators                 A commonly desired set of proper-
ties for a complement operator C is:
  • Boundary conditions: C(0) = 1 and C(1) = 0.

  • Monotonicity: µA (x) ≤ µB (x) =⇒ C(µA (x)) ≥ C(µB (x)).

  • Involution (optional): C(C(µA (x))) = µA (x).
   The standard complement satisfies all three. Parameterized complements
typically satisfy the first two, while involution may be relaxed to gain extra
modeling flexibility; one should check involution explicitly if it is required by a
particular application.

16.19 Triangular norms (t- norms)
Motivation In fuzzy logic, the logical AND operation is generalized by trian-
gular norms (t-norms). These are binary operators that combine membership



                                           338
Modern Intelligent Systems                                                                                       16


                         Tmin(a, b)                                          T (a, b) = ab
       1.0                                                 1.0




                                                                                                0.8
                                                                               0.4
                                                                       0.2
             0.0

                   0.2

                         0.4

                                   0.6

                                           0.8




                                                                 0.0
       0.8                                                 0.8
                                                                                                     0.6
       0.6                                                 0.6
   b




                                                      b
       0.4                                                 0.4

       0.2                                                 0.2

       0.0                                                 0.0
          0.0      0.2   0.4       0.6     0.8      1.0       0.0      0.2     0.4       0.6   0.8         1.0
                               a                                                     a
        Figure 66: Fuzzy AND surfaces comparing minimum versus product
        t-norms; analogous OR surfaces show similar differences. Choices here
       influence rule aggregation in Chapter 18. Use it when deciding whether
     conjunction should behave like a conservative minimum or a multiplicative
                                     attenuation.


values while preserving certain desirable properties analogous to intersection in
classical set theory.

Definition A t-norm is a binary operator T : [0, 1]2 → [0, 1] satisfying the
following properties for all x, y, z ∈ [0, 1]:
  1. Commutativity:
                                                 T (x, y) = T (y, x).

  2. Associativity:
                                     T (x, T (y, z)) = T (T (x, y), z).

  3. Monotonicity:

                           x ≤ x′ ,        y ≤ y ′ =⇒ T (x, y) ≤ T (x′ , y ′ ).

  4. Boundary condition (Identity):

                                         T (x, 1) = x,      T (x, 0) = 0.


                                                     339
Modern Intelligent Systems                                                   16


   These properties ensure that T behaves like a generalized intersection oper-
ator.

Examples of t-norms
  • Minimum t-norm:
                                 Tmin (x, y) = min(x, y).

     This corresponds to the classical intersection in fuzzy sets.

  • Algebraic product t-norm:

                                   Tprod (x, y) = x · y.

     This is a smooth, multiplicative generalization of intersection.

  • Łukasiewicz t-norm:

                             TLuk (x, y) = max(0, x + y − 1).

   Each t-norm captures different semantics of conjunction in fuzzy logic.

Interpretation The t-norm generalizes the classical intersection operator to
fuzzy sets by ensuring the output membership value remains within [0, 1] and
respects the ordering and boundary conditions expected of an intersection.

16.20 Triangular conorms (t- conorms / s-norms)
Definition The dual concept to t-norms is the triangular conorm (t-
conorm), also called an s-norm, which generalizes the logical OR operation. A
t-conorm S : [0, 1]2 → [0, 1] satisfies:
  1. Commutativity:
                                    S(x, y) = S(y, x).

  2. Associativity:
                              S(x, S(y, z)) = S(S(x, y), z).




                                        340
Modern Intelligent Systems                                                     16


  3. Monotonicity: If x ≤ x′ and y ≤ y ′ , then

                                  S(x, y) ≤ S(x′ , y ′ ).

  4. Boundary conditions:

                             S(x, 0) = x,       S(x, 1) = 1.

    These axioms mirror those of t-norms but with 1 as the neutral element
instead of 0. Standard examples include the maximum s-norm Smax (x, y) =
max(x, y), the algebraic sum Ssum (x, y) = x + y − xy, and the bounded sum
Sbs (x, y) = min(1, x + y); explicit formulas and their dual t-norms appear in the
next subsection. Note that the algebraic sum explicitly enforces Ssum (x, y) =
x + y − xy ≤ 1 for all x, y ∈ [0, 1].

16.21 T-Norms and S-Norms: Complementarity and Properties
Recall that a t-norm is a binary operator T : [0, 1]2 → [0, 1] modeling the
fuzzy intersection, and an s-norm (or t-conorm) S : [0, 1]2 → [0, 1] models the
fuzzy union. These operators satisfy certain axioms such as commutativity,
associativity, monotonicity, and boundary conditions:
                          
                          T (x, 1) = x, T (x, 0) = 0,
                          S(x, 0) = x, S(x, 1) = 1,

for all x ∈ [0, 1].
    An important relationship between t-norms and s-norms is their complemen-
tarity via a negation operator. Throughout this section we use the standard
fuzzy negation N (x) = 1 − x, so that the complement of µA is

                              µAc (x) = 1 − µA (x).

   With this explicit choice of negation, the complementarity between T and S
reads:
               T (µA (x), µB (x)) = 1 − S(1 − µA (x), 1 − µB (x)),     (16.36)




                                       341
Modern Intelligent Systems                                                        16


and equivalently,

                S(µA (x), µB (x)) = 1 − T (1 − µA (x), 1 − µB (x)).

    This duality ensures that the fuzzy intersection and union are consistent with
respect to complementation, generalizing classical De Morgan’s laws.

16.22 Examples of common t- norm/s-norm pairs
Several standard t-norms and their corresponding s-norms are widely used:
   • Minimum t-norm and maximum s-norm:

                    Tmin (x, y) = min(x, y),     Smax (x, y) = max(x, y).

   • Algebraic product t-norm and algebraic sum s-norm:

                     Tprod (x, y) = x · y,     Ssum (x, y) = x + y − xy.

   • Bounded difference t-norm and bounded sum s-norm:

              Tbd (x, y) = max(0, x + y − 1),       Sbs (x, y) = min(1, x + y).

   Each of these pairs satisfies the complementarity relation (16.36).

16.23 Fuzzy Set Inclusion and Subset Relations
In classical set theory, A ⊆ B means every element of A is also in B. For fuzzy
sets, the notion of subset is generalized via membership functions.

Definition (Fuzzy Subset). A fuzzy set A is a subset of fuzzy set B, denoted
A ⊆ B, if and only if
                       µA (x) ≤ µB (x), ∀x ∈ X,

where X is the universe of discourse.
   If the inequality is strict for at least one x, i.e., µA (x) < µB (x) for some x,
then A is a proper fuzzy subset of B.




                                         342
Modern Intelligent Systems                                                       16


Interpretation: Since membership functions represent degrees of belonging,
the subset relation is graded rather than binary. This leads naturally to the
concept of degree of inclusion.

16.24 Degree of Inclusion
Because fuzzy membership values lie in [0, 1], the subset relation can be quanti-
fied by a scalar measure indicating how much A is included in B.
    For practical work we often use an aggregate measure:
                                  P
                                        min(µA (x), µB (x))
                     incl(A, B) = x∈X P
                                          x∈X µA (x)

for discrete universes (integrals for continuous, assuming finite mass). It summa-
rizes how much of the mass of A lies inside B’s support. A pointwise alternative
relies on an implicator I and defines Inc(A, B) = inf x I(µA (x), µB (x)) (see be-
low); implicator-based grades avoid division by small µB and behave well when
B has zeros. Both constructions satisfy 0 ≤ incl(A, B) ≤ 1, where 1 means A is
fully included in B.

16.25 Set Operations and Inclusion Properties
Given fuzzy sets A, B, and C, the following properties hold for the standard
t-norm and s-norm operations:
  • If A ⊆ B, then A ∩ C ⊆ B ∩ C and A ∪ C ⊆ B ∪ C. Explicitly,

          µA∩C (x) = min(µA (x), µC (x)) ≤ min(µB (x), µC (x)) = µB∩C (x),

     and analogously for the union/max operator.

  • If A ⊆ B, applying any t-norm T and its dual s-norm S preserves inclusion:
    T (A, C) ⊆ T (B, C) and S(A, C) ⊆ S(B, C). In terms of memberships,

            µT (A,C) (x) ≤ µT (B,C) (x)   and   µS(A,C) (x) ≤ µS(B,C) (x), ∀x.

  • Complements reverse inclusion: A ⊆ B ⇒ B c ⊆ Ac because complements
    flip the ordering of memberships. µB c (x) = 1 − µB (x) ≤ 1 − µA (x) =
    µAc (x).


                                          343
Modern Intelligent Systems                                                         16


16.26 Grades of Inclusion and Equality in Fuzzy Sets
Recall that in classical set theory, the notion of subset and equality is crisp: a set
A is a subset of B if every element of A is also in B, and A = B if they contain
exactly the same elements. In fuzzy set theory, these notions are generalized via
grades of inclusion and equality, which quantify the degree to which one fuzzy
set is included in or equal to another.

Grade of Inclusion Given two fuzzy sets A and B defined on the universe X,
with membership functions µA (x) and µB (x), respectively, the grade of inclusion
of A in B, denoted Inc(A, B), measures how much A is a subset of B.
    One way to define this grade is:
                                                        
                        Inc(A, B) = inf I µA (x), µB (x) ,                    (16.37)
                                      x∈X

where I is an implicator function, often derived from a chosen t-norm T . A
common choice is the Gödel implicator:
                                    
                                    1, if a ≤ b,
                          I(a, b) =
                                    b, otherwise.

    Alternatively, if T is part of a residuated pair (T, I), one sometimes writes
                                                        
                        Inc(A, B) = inf T µA (x), µB (x) ,
                                      x∈X

which should be interpreted as computing the tightest lower bound obtainable
from the chosen T ; this coincides with the implicator-based definition when I is
the residuum of T .

Example Suppose A and B are fuzzy sets with membership functions such
that for some x we have µA (x) ≤ µB (x), and for others µA (x) > µB (x). Using
the Gödel implicator,
                                      
                                      1,      µA (x) ≤ µB (x),
                IG (µA (x), µB (x)) =
                                      µB (x), µA (x) > µB (x),



                                         344
Modern Intelligent Systems                                                          16


so the overall grade of inclusion is inf x∈X IG (µA (x), µB (x)). This explicitly shows
how the implicator returns the smaller membership where A exceeds B.

Grade of Equality Similarly, the grade of equality between fuzzy sets A and
B, denoted Eq(A, B), measures how close the two sets are to being equal. It can
be defined as:
                                                     
                     Eq(A, B) = inf J µA (x), µB (x) ,                  (16.38)
                                      x∈X

where J is an equality function. One convenient choice is
                                  
                                  1,        if a = b,
                        J(a, b) =
                                  T (a, b), otherwise,

with T a t-norm, so that exact agreement receives unit credit while disagreements
are down-weighted via T . Other smooth symmetry measures (e.g., J(a, b) =
1 − |a − b|) can also be used; the key requirement is that J be symmetric,
bounded in [0, 1], and reach 1 only when a = b.
   This definition allows for a graded notion of equality, reflecting the fuzzy
nature of the sets.

16.27 Dilation and Contraction of Fuzzy Sets
Motivation Constructing fuzzy sets with appropriate membership functions
is a challenging task. Often, one starts with an initial fuzzy set A and wishes to
generate related fuzzy sets that represent concepts such as ”more or less A” or
”somewhat A”. This leads to the operations of dilation and contraction of fuzzy
sets, which modify the membership function to reflect these linguistic hedges.

Definitions Given a fuzzy set A with membership function µA (x), we intro-
duce two non-negative shape parameters constrained to α ≥ 1 (dilation gain)
and β ≥ 1 (contraction gain) so that the resulting hedges behave monotonically:
                                                 1/α
                    Dilation: µA(d) (x) = µA (x)      , α ≥ 1,                 (16.39)
                                                β
                 Contraction: µA(c) (x) = µA (x) , β ≥ 1.                      (16.40)




                                         345
Modern Intelligent Systems                                                   16


Using separate symbols α and β avoids the notational clash that occurs when
a single parameter k is forced to satisfy both 0 < k ≤ 1 (for dilation) and
k ≥ 1 (for contraction). In some references these two operations are also called
expansion and narrowing; we treat the terms as synonyms.
    Note that:
   • For dilation, 0 < µA (x) < 1 implies µA (x)1/α ≥ µA (x) when α ≥ 1, so
     every membership value moves closer to 1, making the fuzzy set ”larger”
     or more inclusive. Setting α = 1 leaves the set unchanged.

   • For contraction, 0 < µA (x) < 1 implies µA (x)β ≤ µA (x) when β ≥ 1, so
     the membership values move toward 0, making the fuzzy set ”smaller” or
     more restrictive. Again, β = 1 recovers the original set.

Properties
   • The core of the fuzzy set, i.e., the elements with membership 1, remains
     unchanged under dilation or contraction because 11/α = 1β = 1 for all
     positive α, β:

                   µA (x) = 1 =⇒ µA(d) (x) = 1 and µA(c) (x) = 1.


16.28 Closure of Membership Function Derivations
This chapter completes the toolkit for generating new membership functions
from existing ones via fuzzy-set operations. Membership functions encode
graded belonging over a universe of discourse, and algebraic manipulation of
those functions is central to fuzzy logic and fuzzy inference.

16.28.1   Generating New Membership Functions via Set Operations
Given two membership functions, for example, µyoung (x) and µold (x), defined
over the same universe X, we can construct new membership functions by ap-
plying the following operations:

Dilation (Expansion) Dilation increases the support of a fuzzy set, effec-
tively ”loosening” the membership criteria. For instance, dilating the old mem-




                                      346
Modern Intelligent Systems                                                        16


bership function yields a new fuzzy set more or less old:

                       µmore or less old (x) = dilate(µold (x))

This operation broadens the range of x values considered ”old” to some degree,
reflecting linguistic vagueness.

Contraction (Narrowing) Contraction tightens the membership function,
focusing on a core subset. For example, contracting µold (x) produces µtoo old (x):

                         µtoo old (x) = contract(µold (x))

This captures a stricter notion of ”old.”

Complement The complement of a fuzzy set reverses membership degrees:

                              µnot A (x) = 1 − µA (x)

For example, µnot young (x) = 1 − µyoung (x).

Intersection The intersection of two fuzzy sets corresponds to the minimum
of their membership functions:

                         µA∩B (x) = min{µA (x), µB (x)}

This operation models the logical AND.

Union The union corresponds to the maximum:

                         µA∪B (x) = max{µA (x), µB (x)}

16.28.2   Examples of Constructed Membership Functions
Using these operations, we can create nuanced fuzzy sets:
  • Not young and not old:
                                                                              
              µnot young and not old (x) = min 1 − µyoung (x), 1 − µold (x)


                                        347
Modern Intelligent Systems                                                         16


      This set captures individuals who are neither young nor old, representing
      a middle-aged group.

   • Young but not too old: First, contract µold (x) to get µtoo old (x), then
     take its complement, and intersect with µyoung (x):
                                                                               
               µyoung but not too old (x) = min µyoung (x), 1 − µtoo old (x)

      This set isolates those who are young but excludes those considered ”too
      old,” refining the concept of youthfulness.

   • More or less old: Applying dilation to µold (x) expands the fuzzy set:

                             µmore or less old (x) = dilate(µold (x))

Remark on Normality Note that some constructed membership functions
may not be normal, i.e., their maximum membership degree may be less than 1.
This reflects the inherent fuzziness and partial membership in linguistic concepts.

16.29 Implications for Fuzzy Inference Systems
The ability to generate new membership functions from a small set of base
functions (e.g., µyoung and µold ) is powerful. It allows us to encode complex
human knowledge and linguistic nuances into fuzzy sets, which can then be used
in fuzzy inference systems.
    For example, consider an inference system with inputs:

                         Age      (x),   Exercise Level (e)

and output:
                                  Health Status (h)

    We can define membership functions for age (e.g., young, old) and exercise
level (e.g., low, high), then use fuzzy operators (intersection, union, complement)
to combine these inputs according to rules such as:

                       IF Age is old AND Exercise is high
                                         THEN Health is good


                                           348
Modern Intelligent Systems                                                          16


  Table 8: Typical operator choices in fuzzy inference and their qualitative effects.
 Here the t-norm implements fuzzy AND, the s-norm implements fuzzy OR, and the
    implication shapes consequents. Use it when choosing default operators for a
             Mamdani-style pipeline and predicting qualitative behavior.

t-norm T (a, b)      s-norm S(a, b)         Implication ⇒         Qualitative
                                                                  behavior
min(a, b)            max(a, b)              Mamdani               Sharp,
                                            (clipping:            piecewise-linear
                                            min(α, µB ))          surfaces;
                                                                  conservative.
a·b                  a + b − ab             Larsen (scaling:      Smoother
                                            α µB )                transitions;
                                                                  products damp
                                                                  small activations.
max(0, a + b − 1)    min(1, a + b)          Bounded (e.g.,        Bounded sums;
                                            Łukasiewicz)          useful when
                                                                  saturation is
                                                                  desired.


In a Mamdani-style controller the conjunction “AND” is typically modeled by
the minimum operator and the implication uses the same t-norm (i.e., the conse-
quent is clipped at the firing strength). Other choices include using the product
t-norm for conjunction, Larsen-style scaling for implication, and max for rule
aggregation. Any alternative should be stated explicitly.
    The next step is to formalize the implication and aggregation operators that
map these fuzzy inputs to fuzzy outputs, and then perform defuzzification to
obtain crisp outputs.
    Table 8 serves as the operator-choice checklist in the Mamdani design dis-
cussion.

16.30 Worked Example:                Mamdani Fuzzy Inference (End-to-
      End)
We illustrate a complete Mamdani pipeline with one antecedent (temperature)
and one consequent (fan speed).

Universes and membership functions

                                         349
Modern Intelligent Systems                                                    16


  • Temperature T ∈ [0, 40] ◦ C with fuzzy sets
                                            
              µCold (t) = max 0, 1 − 15−0t−0
                                                           (0, 0, 15),
                                             
             µWarm (t) = max 0, 1 − |t−20|10               (10, 20, 30),
                                         
                                    t−25
               µHot (t) = max 0, 40−25                     (25, 40, 40).

  • Fan speed S ∈ [0, 1] with fuzzy sets
                                              
              µLow (s) = max 0, 1 − 0.5−0s−0
                                                         (0, 0, 0.5),
                                               
           µMedium (s) = max 0, 1 − |s−0.5|
                                          0.25           (0.25, 0.5, 0.75),
                                        
                                   s−0.5
              µHigh (s) = max 0, 1−0.5                   (0.5, 1, 1).

Rule base
  1. IF T is Cold THEN S is Low.

  2. IF T is Warm THEN S is Medium.

  3. IF T is Hot THEN S is High.

Fuzzify input and compute firing strengths For an input temperature
T = 27 ◦C,
                   µCold (27) = 0,
                                30 − 27
                  µWarm (27) =          = 0.3,
                                   10
                                27 − 25    2
                    µHot (27) =         =     ≈ 0.133.
                                   15     15
Using min-implication (clipping), the consequents become
                            ′                      
                         µLow (s) = min 0, µLow (s) = 0,
                       ′                                 
                      µMedium (s) = min 0.3, µMedium (s) ,
                          ′                              
                         µHigh (s) = min 0.133, µHigh (s) .
```

### Findings
Issues found:

1. **Equation (16.34) notation and clarity:**
   - The formula for the Sugeno-type complement operator is given as:
     \[
     C_p(\mu) = \frac{1 - \mu}{1 + p \mu}, \quad p \geq 0,
     \]
     but the text writes it as:
     \[
     C_p(\mu) = \frac{1-\mu}{1 + p \mu}
     \]
     without explicitly stating the domain or range of \(p\) in the equation line. While the text mentions \(p \geq 0\), it would be clearer to include this explicitly in the equation or immediately after it for reproducibility.

2. **Equation (16.35) power-law negation:**
   - The power-law negation is given as:
     \[
     C_p(\mu) = (1 - \mu)^p, \quad p > 0,
     \]
     which is correct. However, the text states it "recovers the standard complement when \(p=1\) and adjusts the steepness for other \(p\)." This is mathematically correct, but it would be helpful to mention explicitly that for \(p < 1\), the function is concave and for \(p > 1\), it is convex, to clarify the effect on steepness.

3. **Involution property and parameterized complements:**
   - The text states: "Unlike the standard complement, most parameterized families do not preserve involution \(C(C(\mu)) = \mu\) for arbitrary \(p\); they are typically designed to satisfy boundary conditions and monotonicity instead."
   - This is correct, but it would be beneficial to explicitly mention that the Sugeno-type complement is involutive only when \(p=0\), and the power-law negation is involutive only when \(p=1\). This helps clarify the conditions under which involution holds.

4. **Figure 66 description:**
   - The figure compares minimum and product t-norms. The text says "analogous OR surfaces show similar differences," which is a vague claim without visual or mathematical support here. This is a minor unverifiable claim unless the figure or text elsewhere explicitly shows OR surfaces.

5. **Boundary condition for t-norms:**
   - The boundary condition is given as:
     \[
     T(x,1) = x, \quad T(x,0) = 0,
     \]
     which is standard. However, the text does not explicitly mention that \(T(1,x) = x\) also holds due to commutativity, which might be useful for completeness.

6. **Definition of s-norm boundary conditions:**
   - The text states:
     \[
     S(x,0) = x, \quad S(x,1) = 1,
     \]
     which is correct. However, the duality with t-norms implies \(S(1,x) = 1\) as well, which is not explicitly stated.

7. **Equation (16.36) complementarity relation:**
   - The complementarity relation is given as:
     \[
     T(\mu_A(x), \mu_B(x)) = 1 - S(1 - \mu_A(x), 1 - \mu_B(x)),
     \]
     and equivalently for \(S\).
   - This is correct for standard negation \(N(x) = 1 - x\), but it should be explicitly stated that this duality holds only under this standard negation and may not hold for other negations.

8. **Equation (16.37) grade of inclusion:**
   - The grade of inclusion is defined as:
     \[
     \mathrm{Inc}(A,B) = \inf_{x \in X} I(\mu_A(x), \mu_B(x)),
     \]
     where \(I\) is an implicator.
   - The text also mentions an alternative:
     \[
     \mathrm{Inc}(A,B) = \inf_{x \in X} T(\mu_A(x), \mu_B(x)),
     \]
     which is confusing because \(T\) is a t-norm, not an implicator. The text says "if \(T\) is part of a residuated pair \((T,I)\), one sometimes writes..." but this is not precise. The residuum \(I\) is the implicator derived from \(T\), not \(T\) itself. Using \(T\) directly as an implicator is incorrect. This could mislead readers and should be clarified.

9. **Gödel implicator definition:**
   - The Gödel implicator is given as:
     \[
     I_G(a,b) = \begin{cases}
     1, & a \leq b \\
     b, & a > b
     \end{cases}
     \]
   - This is correct, but the text should clarify that this is a standard example of an implicator derived from the minimum t-norm.

10. **Equation (16.38) grade of equality:**
    - The grade of equality is defined as:
      \[
      \mathrm{Eq}(A,B) = \inf_{x \in X} J(\mu_A(x), \mu_B(x)),
      \]
      where \(J\) is an equality function.
    - The example choice of \(J\) is:
      \[
      J(a,b) = \begin{cases}
      1, & a = b \\
      T(a,b), & \text{otherwise}
      \end{cases}
      \]
    - This is somewhat unusual because \(T(a,b)\) is generally less than or equal to \(\min(a,b)\), and it is not symmetric in general unless \(T\) is symmetric (which t-norms are). The text should clarify that \(T\) is a symmetric t-norm and that this choice is just one possible definition. Also, the discontinuity at \(a=b\) might cause issues in some applications; a smooth function like \(1 - |a-b|\) is often preferred.

11. **Equations (16.39) and (16.40) dilation and contraction:**
    - The definitions are:
      \[
      \mu_A^{(d)}(x) = \mu_A(x)^{1/\alpha}, \quad \alpha \geq 1,
      \]
      \[
      \mu_A^{(c)}(x) = \mu_A(x)^\beta, \quad \beta \geq 1.
      \]
    - The text states "Using separate symbols \(\alpha\) and \(\beta\) avoids the notational clash that occurs when a single parameter \(k\) is forced to satisfy both \(0 < k \leq 1\) (for dilation) and \(k \geq 1\) (for contraction)."
    - This is correct, but the text should clarify that the dilation exponent \(1/\alpha\) is in \((0,1]\) since \(\alpha \geq 1\), which makes the function concave and increases membership values (except at 0 and 1). Similarly, contraction with \(\beta \geq 1\) is convex and decreases membership values.
    - Also, the text should mention that these operations preserve the range \([0,1]\).

12. **Worked example membership functions:**
    - The membership functions for temperature and fan speed are given using max and linear functions with parameters in parentheses, e.g.:
      \[
      \mu_{\text{Cold}}(t) = \max\left(0, 1 - \frac{15 - t}{15 - 0}\right) \quad (0,0,15),
      \]
      but the notation "(0,0,15)" is unexplained here. Presumably, these are parameters for triangular membership functions, but this is not explicitly stated, which may confuse readers.
    - Also, the formula for \(\mu_{\text{Cold}}(t)\) is written as:
      \[
      \max\left(0, 1 - \frac{15 - 0 t - 0}{\cdots}\right),
      \]
      which appears to have a typo: "15 - 0 t - 0" is unclear and likely a formatting error. It should be something like:
      \[
      \max\left(0, 1 - \frac{15 - t}{15 - 0}\right).
      \]
    - Similar issues appear for \(\mu_{\text{Warm}}(t)\) and \(\mu_{\text{Hot}}(t)\) with unclear or inconsistent notation.

13. **Firing strength calculations:**
    - For \(T=27^\circ C\), the text computes:
      \[
      \mu_{\text{Warm}}(27) = \frac{30 - 27}{10} = 0.3,
      \]
      but the membership function for Warm was given as:
      \[
      \mu_{\text{Warm}}(t) = \max\left(0, 1 - \frac{|t - 20|}{10}\right),
      \]
      so at \(t=27\),
      \[
      \mu_{\text{Warm}}(27) = 1 - \frac{|27 - 20|}{10} = 1 - \frac{7}{10} = 0.3,
      \]
      which is correct.
    - For \(\mu_{\text{Hot}}(27)\), the text writes:
      \[
      \mu_{\text{Hot}}(27) = \frac{27 - 25}{15} = \frac{2}{15} \approx 0.133,
      \]
      but the membership function was given as:
      \[
      \mu_{\text{Hot}}(t) = \max\left(0, \frac{t - 25}{40 - 25}\right),
      \]
      so this is consistent.
    - However, the text writes the formula as:
      \[
      \mu_{\text{Hot}}(t) = \max\left(0, \frac{40 - 25}{t - 25}\right),
      \]
      which is incorrect and likely a formatting error. It should be:
      \[
      \mu_{\text{Hot}}(t) = \max\left(0, \frac{t - 25}{40 - 25}\right).
      \]

14. **Implication step:**
    - The text uses min-implication (clipping) for the consequents:
      \[
      \mu'_{\text{Low}}(s) = \min(0, \mu_{\text{Low}}(s)) = 0,
      \]
      which is trivial and correct since \(\mu_{\text{Cold}}(27) = 0\).
    - For the others, the notation is:
      \[
      \mu'_{\text{Medium}}(s) = \min(0.3, \mu_{\text{Medium}}(s)),
      \]
      \[
      \mu'_{\text{High}}(s) = \min(0.133, \mu_{\text{High}}(s)).
      \]
    - This is consistent with Mamdani inference.

**Summary:**

- Mostly mathematically correct and consistent.
- Some notation and formatting errors in membership function definitions and formulas.
- Some minor clarifications needed on properties of parameterized complements, implicator vs t-norm confusion, and explicit domain/range statements.
- Minor unverifiable claim about OR surfaces in Figure 66.
- The worked example has some formatting and clarity issues in membership function definitions.

---

**Recommendation:** Fix formatting and clarify the points above for better reproducibility and clarity.

## Chunk 25/31
- Character range: 685221–711578

```text
Aggregating by max yields the overall output fuzzy set
                                ′         ′            ′       
                µout (s) = max µLow (s), µMedium (s), µHigh (s) .

                                       350
Modern Intelligent Systems                                                                                                    16


                          (A) Sets and clipping                             (B) Aggregated µout and centroid
                              Low           Medium            High

                     1                                                                   1
       Membership




                                                                           Membership
                    0.5                                                                 0.5
                                                                                                         s⋆ ≈ 0.58
                              0.3                           0.3

                              0.133                   0.133
                     0                                                                   0
                          0         0.2   0.4   0.6   0.8         1                           0   0.2   0.4   0.6   0.8   1
                                      Fan speed s                                                   Fan speed s

         Figure 67: End-to-end fuzzy inference example. (A) Consequent
    membership functions with clipping levels from firing strengths at T = 27 deg
    C. (B) Aggregated output set (max of truncated consequents) and a centroid
         marker near s* approx 0.58. Use it when sanity-checking clipping,
               aggregation, and centroid defuzzification end to end.


Defuzzification (centroid) The crisp fan speed is the centroid
                                                                      R1
                                                        ⋆     s µout (s) ds
                                                      s = R0 1              .
                                                            0 µout (s) ds

For symmetric triangles, the centroid of a truncated Medium set remains at 0.5,
and the centroid of High is at ≈ 0.833. Approximating the centroid of the max-
aggregated set by a convex combination of these centroids weighted by their
peak heights,
                           0.3 · 0.5 + 0.133 · 0.833
                     s⋆ ≈                            ≈ 0.58.
                                  0.3 + 0.133
An exact centroid can be computed analytically or numerically by integrating
the clipped shapes; the approximation above matches a direct trapezoidal inte-
gration on a uniform grid (10k points), which yields s⋆ ≈ 0.580 to three decimals.
See Figure 67 for the membership functions and clipping levels used in this ex-
ample. Practical tip: libraries such as scikit-fuzzy provide a tested defuzz
(centroid) routine; when in doubt, compute the centroid numerically rather than
relying on heuristic convex combinations.




                                                                           351
Modern Intelligent Systems                                                  16


 Key takeaways
    • Fuzzy sets map elements to degrees in [0, 1]; membership shapes
      (triangular, trapezoidal, Gaussian) encode semantics.

    • Support/core and set operations (intersection/union/complement)
      generalize crisp logic.

    • Visualizing membership and operations clarifies design of fuzzy
      controllers.

 Minimum viable mastery.
    • Construct a universe of discourse, define overlapping memberships,
      and compute degrees for concrete inputs.

    • Apply basic operations (min/max, product, complements) and
      predict how the choice changes shape.

    • Translate a design intent (“smooth”, “conservative”, “aggressive”)
      into membership overlap and operator choices.
 Common pitfalls.
    • Setting memberships without checking units/scales, producing labels
      that never activate or always saturate.

    • Using too many overlapping labels without justification (hard to
      tune, hard to interpret).

    • Tuning by aesthetics alone instead of checking downstream sensitivity
      and stability.




                                    352
Modern Intelligent Systems                                                      17


 Exercises and lab ideas
     • Define fuzzy labels for a new universe (e.g., vehicle speed); sketch
       overlapping memberships and compute degrees for 3 sample points.

     • Using two different t-norm/s-norm pairs, compute the
       union/intersection of two fuzzy sets at specific points; comment on
       differences.

     • Write memberships for the thermostat error/rate variables (triangular
       or trapezoidal) and evaluate them at a few inputs.

     • Plot overlapping memberships using the provided snippet; adjust
       parameters to see how overlap changes.

 If you are skipping ahead. The rest of the fuzzy chapters build on these
 primitives. If you find later rule outputs unstable, the first place to revisit
 is the universe scaling and overlap choices here.


Where we head next. Chapter 17 moves from fuzzification/defuzzification
mechanics to system-level design and adaptive fuzzy controllers; relation oper-
ators and projections there connect these set-level tools to control and hybrid
schemes.


17    Fuzzy Set Transformations Between Related Uni-
      verses
Building on Chapter 16, we address a fundamental question: How do we transfer
fuzzy knowledge from one universe of discourse to another related universe? This
arises whenever the same linguistic label must be reused across units, sensors,
or derived variables (Celsius vs. Fahrenheit; position vs. velocity), each with its
own universe and membership functions. This chapter develops that transfer
layer so Chapter 18 can assemble full inference pipelines.




                                       353
Modern Intelligent Systems                                                      17


  Learning Outcomes
    • Apply the extension principle (single and multi-variable) to transport
      fuzzy knowledge across domains.

    • Select appropriate t-norms/s-norms and understand how those
      choices affect projection, dilation, and composition.

    • Tie these transformations to the running thermostat/autofocus
      example to anticipate how inference rules will behave in Chapter 18.

  Design motif
  Preserve meaning while changing representation: the extension principle is
  a disciplined way to push fuzzy concepts through transformations so
  downstream inference remains interpretable (see Chapter 18).


Running example checkpoint. We treat the thermostat’s heater power as
the target universe while the inputs remain error/rate. When mapping “Com-
fortable” from Celsius to Fahrenheit or translating error/rate pairs into control
actions, the extension principle tells us how those fuzzy labels transfer; keep
that single example in mind as you work through the upcoming dilation and
projection formulas.

17.1   Context and Motivation
Previously, we studied operations such as dilation and contraction on fuzzy sets
within a single universe of discourse. For example, given a fuzzy set representing
the concept young, we can generate related fuzzy sets like less young or too old
by applying these operations. By combining these fuzzy sets, we can express
nuanced concepts such as not too young or not too old within the same universe.
    However, what if we want to extend this reasoning to a different universe of
discourse that is related to the original one? For instance, consider the following
scenarios:
  • Mapping temperature from Celsius to Fahrenheit.

  • Transforming a variable x to y = x2 .

  • Relating speed and acceleration to derive new fuzzy sets.

                                       354
Modern Intelligent Systems                                                     17


    In such cases, the new universe is a function of the original universe, and we
want to preserve and transfer the fuzzy knowledge encoded in the original fuzzy
sets to the new universe.
  Operator defaults in this trilogy
  Unless stated otherwise in Chapters 16 to 18, we use the standard De
  Morgan triple: ∧ = min, ∨ = max, and complement C(µ) = 1 − µ.
  Parameterized complements (Yager/Sugeno) are noted when used, but they
  generally lose involution (C(C(µ)) 6= µ) unless the parameter is zero.


Notation. Throughout this chapter we use the trilogy defaults stated in the
box above: ∧ = min, ∨ = max, and complement 1 − µ. When we introduce
a general t-norm T , it appears explicitly (e.g., in Equation (17.2) and Equa-
tion (17.10)). For symbol overloads when reading across parts, see Appendix D.

17.2   Problem Statement
Let X and Y be two universes of discourse, with a known mapping function

                             y = f (x),   x ∈ X,   y ∈ Y.

Suppose we have a fuzzy set A ⊆ X with membership function µA : X → [0, 1].
We want to define a fuzzy set B ⊆ Y with membership function µB : Y → [0, 1]
that corresponds to A under the transformation f .
   The key questions are:
  • How do we compute µB (y) for each y ∈ Y ?

  • How do we handle the fact that multiple x ∈ X may map to the same
    y ∈Y?

  • How do we combine membership values µA (x) for all x such that f (x) = y?

17.3   Intuition and Challenges
It is tempting to define µB (y) = µA (x) where y = f (x), but this is generally
insuﬀicient because:
  • The mapping f may not be one-to-one; multiple x values can map to the
    same y.


                                          355
Modern Intelligent Systems                                                       17


   • Membership values represent degrees of truth or compatibility, not numer-
     ical values to be transformed arithmetically.

   • Simply applying f to membership values (e.g., squaring them) does not
     preserve the semantic meaning of membership.
   Therefore, we need a principled method to aggregate membership values
from all preimages of y under f .

17.4    Formal Definition of the Transformed Membership Func-
        tion
Given the fuzzy set A ⊆ X with membership function µA , and the mapping
y = f (x), the membership function µB of the fuzzy set B ⊆ Y is defined by

                             µB (y) =      sup        µA (x)                 (17.1)
                                        x∈X:f (x)=y


The strongest pre-image membership determines the membership of y. When
the mapping depends on multiple fuzzy variables (e.g., f (x1 , x2 )), the individual
memberships are combined with a chosen t-norm before taking the supremum,
as shown later in Equation (17.2).

Remarks:
   • The sup (supremum) operator generalizes the maximum operator, captur-
     ing the highest membership value among all x mapping to y; when X is
     finite the supremum collapses to an ordinary maximum.

   • If no x ∈ X maps to y, then µB (y) = 0.

   • For single-input transformations no additional t-norm is needed; the aggre-
     gation shows up only when several input memberships must be combined
     before mapping through f .

   • In continuous settings we assume f is measurable so that the pre-image
     sets {x | f (x) = y} are well-defined and the supremum exists.

17.5    Interpretation
Equation (17.1) states that the membership degree of y in B is the supremum
over all membership degrees of x in A such that f (x) = y. For single-input map-

                                          356
Modern Intelligent Systems                                                          17


pings no additional combination is necessary; when multiple fuzzy inputs are
involved we first combine their memberships with a chosen T-norm (cf. Equa-
tion (17.2)) and then take the supremum. Intuitively, this means:

       The degree to which y belongs to the transformed fuzzy set B is
       determined by the strongest membership degree among all x values
       that map to y, appropriately combined.

    This approach preserves the logical interpretation of membership values and
respects the structure of the mapping f .

17.6    Example Setup
Consider the universe X = R and the fuzzy set A

17.7    Transformation of Fuzzy Sets Between Universes
We continue our discussion on fuzzy set transformations, focusing on mapping
fuzzy sets from one universe to another via a function y = f (x).

Example: Mapping via y = x2 Consider a fuzzy set A defined on universe
X = {−1, 0, 1, 2} with membership values:

        µA (−1) = 0.340,     µA (0) = 0.141,      µA (1) = 0.242,   µA (2) = 0.4.

Note that A is not normal because no element achieves membership 1; a fuzzy
set is normal precisely when supx∈X µA (x) = 1.
    Define the transformation y = x2 . The image universe Y consists of:

                       Y = {02 , (−1)2 , 12 , 22 } = {0, 1, 4}.

    To find the membership function µB (y) of the transformed fuzzy set B on
Y , we use the extension principle:

                              µB (y) =      sup        µA (x).
                                         x∈X:f (x)=y




                                           357
Modern Intelligent Systems                                                       17


   Calculating explicitly:

          µB (0) = µA (0) = 0.141,
          µB (1) = max{µA (−1), µA (1)} = max{0.340, 0.242} = 0.340,
          µB (4) = µA (2) = 0.4.

   Thus, the transformed fuzzy set B on Y is:

                      B = {(0, 0.141), (1, 0.340), (4, 0.4)}.

   Even on this very small domain the mapping f (x) = x2 is many-to-one,
because x = −1 and x = 1 both map to y = 1; the example therefore highlights
how the supremum handles multiple pre-images.
 Worked example: monotone map (Celsius → Fahrenheit)
 Let A = ComfortableC be triangular on Celsius with breakpoints
 (21, 23, 25). For the aﬀine map f (x) = 1.8x + 32, the image B = f (A) is
 triangular with breakpoints f (21) = 69.8, f (23) = 73.4, f (25) = 77.0.
 Because f is strictly increasing, µB (y) = µA (f −1 (y)) and every α-cut maps
 directly: Bα = f (Aα ). This is the fastest way to reuse the same linguistic
 label across units without recomputing via (17.1).


Visual intuition. Figure 68 walks through a simple mapping y = x2 , showing
how memberships on X lift to memberships on Y via the supremum over all pre-
images that map to the same point.
   Figure 69 makes the non-monotone alpha-cut mapping explicit for piecewise
image transforms.

Extension to Multiple Fuzzy Sets Suppose now we have two fuzzy sets
A1 and A2 defined on the same universe X = {−1, 0, 1, 2}, with membership
functions listed in the order (−1, 0, 1, 2):

             µA1 = {0.4, 0.7, 0.5, 0.13},    µA2 = {0.5, 0.1, 0.4, 0.7}.




                                       358
Modern Intelligent Systems                                                                                         17



                    0.4                                                        0.4
       Membership




                                                                  Membership
                    µA (x)                                                     µB (y)



                    0.2                                                        0.2



                     0                                                          0
                          −1       0           1          2                          0   1                 4
                                    x in X                                               y = f (x) = x2

    Figure 68: Mapping a fuzzy set through the function “y = x-squared”. The
    membership at an output value y is the supremum over all pre-images x that
    map to y; shared images such as x = +/-1 map to y = 1 using the maximum
    membership. Use it when applying the extension principle to a non-invertible
                                     function.


Equivalently, for A1 we have µA1 (−1) = 0.4, µA1 (0) = 0.7, µA1 (1) = 0.5,
µA1 (2) = 0.13. For A2 we have µA2 (−1) = 0.5, µA2 (0) = 0.1, µA2 (1) = 0.4,
µA2 (2) = 0.7.
   Define a function y = f (x1 , x2 ) = x21 +x22 , where x1 , x2 ∈ X and their degrees
of membership are taken from A1 and A2 respectively.
   The universe Y is the set of all possible sums of squares:

                                         Y = {x21 + x22 | x1 , x2 ∈ X}.

   For example, some values in Y include:

         02 + 02 = 0,             (−1)2 + 02 = 1,                 12 + 12 = 2,            22 + 22 = 8,    ...

Computing Membership Values in Y The membership function µB (y) is
given by Zadeh’s extension principle for two variables:

                             µB (y) =              sup            min{µA1 (x1 ), µA2 (x2 )}.                    (17.2)
                                        (x1 ,x2 ):f (x1 ,x2 )=y


The minimum t-norm plays the role of the generic operator ⊗; any other t-
norm could be substituted so long as the same choice is applied throughout the
inference pipeline.
    Example: Compute µB (0).


                                                              359
Modern Intelligent Systems                                                           17


    The pairs (x1 , x2 ) such that x21 + x22 = 0 are only (0, 0). Then,

               µB (0) = min{µA1 (0), µA2 (0)} = min{0.7, 0.1} = 0.1.

    Example: Compute µB (1).
    The pairs (x1 , x2 ) such that x21 + x22 = 1 are:

                        (−1, 0),    (0, −1),     (1, 0),   (0, 1).

    Calculate the minimum membership values for each pair:

                   min{µA1 (−1), µA2 (0)} = min{0.4, 0.1} = 0.1,
                   min{µA1 (0), µA2 (−1)} = min{0.7, 0.5} = 0.5,
                     min{µA1 (1), µA2 (0)} = min{0.5, 0.1} = 0.1,
                     min{µA1 (0), µA2 (1)} = min{0.7, 0.4} = 0.4.

Taking the supremum over all contributing pairs gives

                       µB (1) = max{0.1, 0.5, 0.1, 0.4} = 0.5.

17.8    Extension Principle Recap and Projection Operations
Recall from the previous discussion that the extension principle allows us to
extend a fuzzy set defined on one universe to another universe via a known
function. For example, if we have a fuzzy set A ⊆ X and a function f : X → Y ,
then the image fuzzy set B = f (A) ⊆ Y is defined by

                             µB (y) =      sup        µA (x).                    (17.3)
                                        x∈X:f (x)=y


This corresponds to taking the maximum membership value among all preimages
of y under f . In discrete settings the supremum reduces to a maximum over the
(finite) preimage of y; for multi-input maps f (x1 , . . . , xn ) we first combine input
memberships with a chosen t-norm and then take the supremum over all tuples
mapping to y.
     In the continuous universe, this can become challenging because multiple x
values may map to the same y, requiring careful evaluation of the supremum.


                                          360
Modern Intelligent Systems                                                    17


The extension principle thus generalizes the image of fuzzy sets under arbitrary
mappings.
 Computation and discretisation tips
 For discrete universes the extension principle costs O(|X|) per y (or
 O(|X|n ) for n-ary maps) because we evaluate every preimage tuple. In
 discrete settings sup reduces to a max. Continuous universes require
 discretisation: sample each input axis on a uniform or adaptive grid
 (typical 200–500 points per dimension), apply the t-norm/aggregation on
 that mesh, and approximate the supremum via max. Sparse grids or Monte
 Carlo sampling reduce the curse of dimensionality; always report the
 resolution so readers understand numeric fidelity.

 Alpha-cuts as an alternative
    • Unary monotone f : Bα = f (Aα ) for every α ∈ (0, 1];
      computationally trivial for aﬀine/monotone maps.

    • Non-monotone f : split X into monotone pieces Dk ; compute
            S
      Bα = k f (Aα ∩ Dk ). This is the standard route for fuzzy arithmetic
      on fuzzy numbers.

    • When to use: alpha-cuts are numerically stable for continuous
      domains and avoid sampling artifacts when f is smooth; pointwise
      sup is more convenient on discrete grids.

   Figure 70 visualizes how relation entries project into the corresponding
marginals.

17.9   Projection of Fuzzy Relations
Now, consider the case where we have a fuzzy relation R ⊆ X × Y , where X
and Y are universes of discourse. The fuzzy relation R is characterized by a
membership function
                            µR : X × Y → [0, 1].

This relation can be viewed as a fuzzy set on the Cartesian product X × Y .

Cartesian Product of Fuzzy Sets Given fuzzy sets A ⊆ X and B ⊆ Y with
membership functions µA and µB , their Cartesian product R = A × B is defined

                                      361
Modern Intelligent Systems                                                                                    17


                1                                                          1
                          A on X                                                             B = f (A) on Y
                                                                                    Bα
     µA (x)




                                                                 µB (y)
                     α
               0.5                                                        0.5



                0                                                          0
                     −2            0           2                                0        1             2
                                x                                                        y=x     2


               Figure 69: Alpha-cuts under the non-monotone map “y = x-squared”. A
              symmetric triangular fuzzy set on X maps to a right-skewed fuzzy set on Y.
                Each alpha-cut on A splits into two intervals whose images union to the
                   output alpha-cut. Use it when propagating a fuzzy set through a
                                  non-monotone map via alpha-cuts.


by
                                          µR (x, y) = T (µA (x), µB (y)),                                  (17.4)

where T is a chosen t-norm, commonly the minimum operator:

                                              T (a, b) = min(a, b).

A t-norm is any binary operator T : [0, 1]2 → [0, 1] that is commutative, as-
sociative, monotone in each argument, and has 1 as identity, so it faithfully
generalizes set intersection to graded memberships. Popular choices include the
minimum, the product ab, and the Łukasiewicz t-norm max(0, a + b − 1).

Example               Suppose

                                       µA = {0.5, 0.9},   µB = {0.8, 0.9}.

Then the Cartesian product membership values are
                   "                             # "         #
                     min(0.5, 0.8) min(0.5, 0.9)     0.5 0.5
             µR =                                 =            .
                     min(0.9, 0.8) min(0.9, 0.9)     0.8 0.9

Here the first row corresponds to x1 , the second row to x2 , and the columns
correspond to y1 and y2 . Keeping that indexing explicit avoids ambiguity when
reading off the projected membership values.

                                                       362
Modern Intelligent Systems                                                                 17


  Table 9: Popular t-norms and their typical roles. Use it when choosing a default
         conjunction operator and understanding its qualitative behavior.

  T-norm                Dual t-conorm /                    When to use
                        identity
  Minimum               Dual: max(a, b);                   Linguistic rules mirroring
  Tmin (a, b) =         idempotent                         classical AND; preserves
  min(a, b)                                                interpretability.
  Product               Dual: probabilistic sum            Smooth gradients,
  TΠ (a, b) = ab        a + b − ab                         probabilistic semantics,
                                                           differentiable control.
  Łukasiewicz           Dual: bounded sum                  Allows partial satisfaction
  TLuk (a, b) =         min(1, a + b)                      to accumulate; useful in
  max(0, a + b − 1)                                        preference aggregation and
                                                           graded constraints;
                                                           tolerates partial violations.


Projection of Fuzzy Relations Often, we are interested in reducing the
dimensionality of a fuzzy relation by projecting it onto one of its component
universes. The projection operation extracts a fuzzy set on X or Y from the
fuzzy relation R.

Definition (Projection onto X). The projection of R onto X, denoted
πX (R), is defined by
                       µπX (R) (x) = sup µR (x, y).           (17.5)
                                               y∈Y


Definition (Projection onto Y ).             Similarly, the projection of R onto Y , de-
noted πY (R), is defined by

                              µπY (R) (y) = sup µR (x, y).                           (17.6)
                                               x∈X


Total Projection The total projection of R is the maximum membership value
over the entire relation:

                             µπtotal (R) =     sup     µR (x, y).                    (17.7)
                                             x∈X,y∈Y




                                             363
Modern Intelligent Systems                                                            17


Interpretation - The projection onto X collapses the Y -dimension by taking
the maximum membership value along each fixed x. - The projection onto
Y collapses the X-dimension similarly. - The total projection gives the single
highest membership value in the relation.

                           y1    y2      y3          πX (R)     πY (R)
                    x1     0.9   0.3     0.1          0.9        0.9
                    x2     0.4   0.8     0.2          0.8        0.8
                    x3     0.1   0.6     0.5          0.6        0.5
```

### Findings
No issues spotted.

## Chunk 26/31
- Character range: 711580–737474

```text
Figure 70: Illustrative fuzzy relation table (left) together with its
       projections onto the error universe (middle) and the rate-of-change universe
         (right). These are the exact quantities used in the running thermostat
      example before composing rules. Use it when building rule antecedents from a
              relation and checking which universes each projection lives on.



Example (continued) Using the previous example matrix for µR :
                                               "    #
                                            0.5 0.5
                                       µR =           ,
                                            0.8 0.9

we compute

                µπX (R) = {max(0.5, 0.5), max(0.8, 0.9)} = {0.5, 0.9},

                µπY (R) = {max(0.5, 0.8), max(0.5, 0.9)} = {0.8, 0.9},

and
                         µπtotal (R) = max{0.5, 0.8, 0.5, 0.9} = 0.9.

17.10 Dimensional Extension and Projection in Fuzzy Set Oper-
      ations
In practice, we frequently need to combine fuzzy sets and fuzzy relations that live
on different universes of discourse. For example, one object may be defined on
a one-dimensional universe X, while another lives on a product space X × Y (as
relations do). Before we can take unions/intersections or compose rules, we must
reconcile dimensions. Two operators do the heavy lifting: cylindrical extension
lifts a set into a higher-dimensional space without changing its meaning, and

                                               364
Modern Intelligent Systems                                                      17


projection collapses a relation back onto the universe we want to summarize.

Cylindrical Extension The cylindrical extension is a technique used to ex-
tend a fuzzy set defined on a lower-dimensional universe to a higher-dimensional
universe by replicating membership values along the new dimension(s).
     Suppose we have a fuzzy set A ⊆ X with membership function µA : X →
[0, 1]. To extend A to X × Y , define the cylindrical extension A∗ as:

                       µA∗ (x, y) = µA (x),      ∀x ∈ X, y ∈ Y.              (17.8)

This operation ”copies” the membership values of A uniformly along the Y -
dimension, resulting in a fuzzy set over X × Y .

Projection Conversely, the projection operation reduces the dimension of a
fuzzy set by aggregating membership values over one or more dimensions. For a
fuzzy set R ⊆ X × Y with membership function µR : X × Y → [0, 1], the projec-
tion onto X is again given by µπX (R) (x) = supy∈Y µR (x, y) as in Equation (17.5).
This operation captures the maximum membership value over all y ∈ Y for each
fixed x, effectively ”collapsing” the Y -dimension.

Example Consider a fuzzy set A on X = {x1 , x2 } with membership values
µA (x1 ) = 0.5, µA (x2 ) = 0.7. Extending A cylindrically to X × Y where Y =
{y1 , y2 , y3 } yields:

                  µA∗ (xi , yj ) = µA (xi ),   i = 1, 2;   j = 1, 2, 3.

Thus, the membership values are replicated along the Y -axis. In practice this
extension step is often paired with projections to reconcile relation dimensions
before composing rules and, later, to marginalize the inferred relation back onto
the universe of interest.

17.11 Fuzzy Inference via Composition of Relations
The ultimate goal of building fuzzy logic systems is to perform inference, i.e., to
compose fuzzy rules to generate predictions or decisions. This involves combining
fuzzy relations that represent knowledge or rules.



                                           365
Modern Intelligent Systems                                                      17


Setup Suppose we have three universes of discourse X, Y, Z, and two fuzzy
relations:
                    R1 ⊆ X × Y, R2 ⊆ Y × Z,

with membership functions µR1 (x, y) and µR2 (y, z), respectively.
    The question is: can we infer a fuzzy relation R ⊆ X × Z that relates X
directly to Z by composing R1 and R2 ? This is the essence of fuzzy inference.

Composition of Fuzzy Relations The composition R = R1 ◦ R2 is defined
by:
                                                          
                µR (x, z) = sup min µR1 (x, y), µR2 (y, z) .   (17.9)
                                 y∈Y

This is known as the sup–min composition (or max–min composition) of fuzzy
relations; replacing min with another t-norm T swaps in the chosen operator
from Table 9.

Interpretation - The min operator captures the degree to which x is related
to y and y is related to z simultaneously. - The sup (maximum) over all inter-
mediate y aggregates all possible ”paths” from x to z through y.

Dimensional Considerations Note that R1 is defined on X × Y , and R2 on
Y × Z. The composition yields R on X × Z. If the dimensions of the relations
differ or if the universes are not aligned, cylindrical extension or projection can
be applied to make the dimensions compatible before composition.

Example     Let X = {x1 , x2 }, Y = {y1 , y2 }, and Z = {z1 , z2 }. Consider
                             "    #                 "        #
                          0.2 0.9                    0.7 0.3
                   µ R1 =           ,         µ R2 =           .
                          0.5 0.1                    0.4 0.8




                                        366
Modern Intelligent Systems                                                      17


Using the max–min composition,

     µR (x1 , z1 ) = max{min(0.2, 0.7), min(0.9, 0.4)} = max{0.2, 0.4} = 0.4,
     µR (x1 , z2 ) = max{min(0.2, 0.3), min(0.9, 0.8)} = max{0.2, 0.8} = 0.8,
     µR (x2 , z1 ) = max{min(0.5, 0.7), min(0.1, 0.4)} = max{0.5, 0.1} = 0.5,
     µR (x2 , z2 ) = max{min(0.5, 0.3), min(0.1, 0.8)} = max{0.3, 0.1} = 0.3.

Therefore                               "     #
                                      0.4 0.8
                                 µR =           .
                                      0.5 0.3

 Max–min composition as “fuzzy matrix multiply”
 Given R1 ∈ [0, 1]|X|×|Y | and R2 ∈ [0, 1]|Y |×|Z| ,

 for i in range(|X|):
     for k in range(|Z|):
         acc = 0
         for j in range(|Y|):
             acc = max(acc, min(R1[i, j], R2[j, k]))
         R[i, k] = acc
 return R # the composition R1 o R2

 Swap min for another T (product, Łukasiewicz) and max for the
 corresponding s-norm to instantiate other composition families.


17.12 Recap and Motivation
Earlier in this chapter, we introduced fuzzy relations and their compositions,
focusing on max–min composition as a fundamental operation. We saw how
fuzzy relations can represent uncertain or imprecise mappings between sets, and
how compositions allow chaining these relations to infer new relationships.
    The goal of this final part is to wrap up the derivations related to fuzzy
relation composition, clarify the generalization of these operations, and highlight
key properties that enable their effective use in fuzzy inference systems.




                                         367
Modern Intelligent Systems                                                       17


17.13 Generalization of Fuzzy Relation Composition
Suppose we have two fuzzy relations:

                             R1 ⊆ X × Y,     R2 ⊆ Y × Z,

with membership functions µR1 (x, y) and µR2 (y, z), respectively.
   The composition R = R1 ◦ R2 is a fuzzy relation from X to Z defined by:
                                                             
                     µR (x, z) = sup T µR1 (x, y), µR2 (y, z) ,             (17.10)
                                  y∈Y


where T is a chosen t-norm (triangular norm) representing fuzzy conjunction
(e.g., minimum, product). Recall that a t-norm T : [0, 1]2 → [0, 1] is commuta-
tive, associative, monotone in each argument, and satisfies T (a, 1) = a; popular
choices include the minimum, product, and Łukasiewicz operators.

Max–min Composition:             The most common choice is the max–min compo-
sition where
                                 T (a, b) = min(a, b),

and the supremum is replaced by maximum:
                                                             
                   µR (x, z) = max min µR1 (x, y), µR2 (y, z) .
                                 y∈Y


    This operation generalizes the classical composition of crisp relations to fuzzy
sets.

17.14 Example Calculation of Composition
Consider discrete sets X = {x1 , x2 }, Y = {y1 , y2 }, and Z = {z1 , z2 }, with
membership values:
                             "      #               "      #
                            0.5 0.6                0.5 0.1
                     µ R1 =           ,     µ R2 =           ,
                            0.5 0.5                0.2 0.5
where rows correspond to X or Y elements and columns to Y or Z elements
respectively.




                                         368
Modern Intelligent Systems                                                       17


   To compute µR (x1 , z1 ), we evaluate:

     µR (x1 , z1 ) = max {min(0.5, 0.5), min(0.6, 0.2)} = max{0.5, 0.2} = 0.5.

   Similarly, for µR (x1 , z2 ):

     µR (x1 , z2 ) = max {min(0.5, 0.1), min(0.6, 0.5)} = max{0.1, 0.5} = 0.5.

   This process continues for all pairs (xi , zj ) to form the composed relation
matrix.

17.15 Properties of Fuzzy Relation Composition
The composition operation inherits several important algebraic properties, anal-
ogous to classical relations:
  • Associativity: For fuzzy relations R1 , R2 , R3 ,

                              (R1 ◦ R2 ) ◦ R3 = R1 ◦ (R2 ◦ R3 ).

     This allows chaining multiple relations without ambiguity.

  • Non-commutativity: Generally,

                                     R1 ◦ R2 6= R2 ◦ R1 ,

     reflecting the directional nature of relations.

  • Distributivity: Composition distributes over union:

                         R1 ◦ (R2 ∪ R3 ) = (R1 ◦ R2 ) ∪ (R1 ◦ R3 ).

  • De Morgan’s Laws and Inclusion: These extend naturally to fuzzy
    relations and their complements, intersections, and unions.

17.16 Alternative Composition Operators
While max–min is standard, other t-norms and t-conorms can be used to define
composition:



                                          369
Modern Intelligent Systems                                                       17


   • Max-Product Composition:

                        µR (x, z) = max (µR1 (x, y) · µR2 (y, z)) .
                                      y


   • Max-Average or Other Aggregations: Depending on application
     needs, different norms can be used to model conjunction and aggregation.

 Author’s note: choosing an operator family
 Start with max–min when safety and monotonicity matter; its outputs stay
 within the tightest support and preserve ordering. Swap to max–product or
 algebraic t-norms when you need smoother surfaces or when small
 disagreements should be penalized multiplicatively (e.g., sensor fusion). If
 the resulting surfaces are too flat, tighten the t-norm; if they are too brittle,
 loosen it. Operator choice is an engineering dial, not an article of faith.

   The choice of composition operator therefore follows a practical rule: begin
with max–min for its interpretability and stability, and reach for the alternatives
catalogued in Table 9 only when the application demands smoother or more
aggressive aggregation.




                                          370
Modern Intelligent Systems                                                    17


 Key takeaways
    • The extension principle transfers fuzzy sets across related universes
      via functions y = f (x).

    • Multiple preimages require aggregation (e.g., sup over inverse
      mappings with a chosen t-norm).

    • Clear notation and figures (domains, mappings) prevent ambiguity in
      fuzzy transformations.

 Minimum viable mastery.
    • Given y = f (x), compute µY (y) via inverse mappings and a chosen
      aggregation rule.

    • State when the mapping is one-to-one vs. many-to-one and how that
      changes the computation.

    • Track domain restrictions explicitly so transformed sets respect
      feasibility (e.g., square-root domains).
 Common pitfalls.
    • Dropping multi-preimage cases and silently producing overconfident
      outputs.

    • Hiding domain restrictions, leading to membership mass on invalid
      regions.

    • Mixing notations for T , sup, and complements across examples (hard
      to audit later).




                                     371
Modern Intelligent Systems                                       Fuzzy inference


 Exercises and lab ideas
     • Implement a minimal example from this chapter and visualize
       intermediate quantities (plots or diagnostics) to match the
       pseudocode.

     • Stress-test a key hyperparameter or design choice discussed here and
       report the effect on validation performance or stability.

     • Re-derive one core equation or update rule by hand and check it
       numerically against your implementation.

 If you are skipping ahead. The extension principle is the bookkeeping
 layer for the full inference pipeline. When you reach Chapter 18, every
 “rule output” is an instance of the same transfer-and-aggregate pattern.


Where we head next. Chapter 18 operationalizes these relation tools: each
rule induces a fuzzy relation on input-output space, then sup-T composition
and projection produce the implied output set before aggregation and defuzzifi-
cation. The same defaults (max–min with standard complement) carry over, as
summarized in Equations (18.2) to (18.6).


18    Fuzzy Inference Systems: Rule Composition and
      Output Calculation
Building on Chapter 17, where transfer operators (projection, composition, and
the extension principle) move fuzzy information between related universes, we
now assemble complete fuzzy inference systems (FIS): rule composition and out-
put calculation. This closes the fuzzy trilogy by turning set/relation machinery
into end-to-end decisions.




                                      372
Modern Intelligent Systems                                       Fuzzy inference


 Learning Outcomes
    • Execute full Mamdani/Larsen style inference: antecedent aggregation,
      implication, aggregation, and defuzzification.

    • Compare implication/aggregation choices (product vs. min, max vs.
      sum) and their impact on the running thermostat/autofocus example.

    • Contrast Mamdani systems with Sugeno/Takagi–Sugeno systems to
      know when weighted-average consequents are preferable.

 Design motif
 Local linguistic rules become a global behavior only after you commit to
 concrete operators (t-norm, implication, aggregation, defuzzifier) and then
 sanity-check the resulting surface.


Running example checkpoint. For the thermostat, each rule combines the
temperature error (Cold, Slightly Warm, …) and rate-of-change to set heater
power. As you work through antecedent aggregation, implication, and defuzzifi-
cation, keep one concrete rule base (e.g., “IF error is Cold AND rate is Falling
THEN heater power is High”) in mind; the formulas below map directly onto
that setup.

18.1    Context and Motivation
 Notation handoff
 Throughout this chapter we keep the trilogy defaults from Chapters 16
 to 17: ∧ = min, ∨ = max, and the standard complement 1 − µ.
 Aggregation over rule consequents defaults to the max s-norm unless stated
 otherwise; alternatives live in Table 9. If symbols conflict with earlier
 chapters, use local definitions and refer to Appendix D.

   Recall that a fuzzy inference system maps crisp inputs to fuzzy outputs by
applying a set of fuzzy rules. Each rule typically has the form:

       If x1 is A1 and x2 is A2 and · · · then y is B,




                                        373
Modern Intelligent Systems                                         Fuzzy inference


   where Ai and B are fuzzy sets defined on the respective universes of discourse.
The antecedent (premise) combines multiple fuzzy conditions on inputs, and the
consequent (conclusion) specifies the fuzzy output.
 Author’s note: rules as lived experience
 These rules are not immutable physical laws; they are codified experience.
 We record facts such as “if it is morning then the sun is in the east,” yet
 real observations may arrive at noon. Fuzzy inference exists to bridge that
 gap: observed memberships are composed with stored rules so that slight
 deviations in the antecedent produce softened consequents instead of
 brittle yes/no responses. When you carry out the algebra below, keep that
 picture of “experience vs. observation” in mind.

   The key challenge is to systematically combine the antecedent fuzzy sets
and then infer the output fuzzy set for each rule, before aggregating all rules to
produce a final output.

18.2   Rule Antecedent Composition
Given a rule with n antecedents, each associated with a fuzzy set Ai and an
input value xi , the degree to which the rule is activated (also called the firing
strength) is computed by combining the membership values of each antecedent
condition.

Membership values of antecedents: For each input xi , the membership
degree in fuzzy set Ai is

                                 µAi (xi ) ∈ [0, 1]                         (18.1)

Aggregation operator: The combined antecedent membership is obtained
by applying a fuzzy logical operator, typically the minimum (intersection) or
the product operator:




                                       374
Modern Intelligent Systems                                                        Fuzzy inference




                                              n
            µantecedent (x1 , . . . , xn ) = min µAi (xi ),      (min operator)            (18.2)
                                             i=1
                                             Yn
       or µantecedent (x1 , . . . , xn ) =         µAi (xi ).   (product operator)         (18.3)
                                             i=1

    This value quantifies the degree to which the entire antecedent condition is
satisfied by the input vector x = (x1 , . . . , xn ). More generally, any t-norm T
can be used in place of the min or product, provided it satisfies the standard
properties (commutativity, associativity, monotonicity, and T (a, 1) = a); the
chosen t-norm shapes how strictly the rule demands simultaneous satisfaction
of all antecedents.

18.3    Rule Consequent and Output Fuzzy Set
Once the antecedent firing strength α is computed, it is used to modify the
consequent fuzzy set B. The consequent fuzzy set is typically defined by its
membership function µB (y) over the output universe.

Implication operator: The implication step adjusts the consequent mem-
bership function based on the firing strength α. Commonly used implication
methods include:
  • Minimum implication: Truncate the consequent membership function
    at level α,
                                               
                       µB ′ (y) = min α, µB (y) .              (18.4)

  • Product implication: Scale the consequent membership function by α,

                                        µB ′ (y) = α · µB (y).                             (18.5)

   The resulting fuzzy set B ′ represents the output fuzzy set contributed by this
particular rule.




                                                  375
Modern Intelligent Systems                                        Fuzzy inference


 Implication choices
 Mamdani uses min-implication (clipping), Larsen uses product-implication
 (scaling). Other options include residuated and axiomatic implicators
 paired with their t-norms (e.g., Gödel, Product/Goguen, Łukasiewicz; see
 Klement et al., 2000; Dubois and Prade, 1988). Pick by desired
 smoothness: clipping preserves shape and interpretability; scaling yields
 smoother surfaces and is friendlier to gradient-based tuning.


18.4   Aggregation of Multiple Rules
When multiple rules are present, each produces an output fuzzy set Bj′ with
membership function µBj′ (y), where j indexes the rules. These are aggregated
to form a combined output fuzzy set:

                             µBagg (y) = max µBj′ (y).                     (18.6)
                                           j

   The max operator corresponds to the fuzzy union of the individual rule
outputs, capturing the overall inference result.

Other aggregations Algebraic sum or bounded sum (Table 9) are used when
max is too brittle; they can over-saturate when many rules fire, so start with
max unless smooth blending is required.

18.5   Summary of the Fuzzy Inference Process
To summarize, the fuzzy inference process for a given input vector x proceeds
as follows:
  1. For each rule j, compute the antecedent membership degree αj using (18.2)
     or (18.3).

  2. Modify the consequent fuzzy set Bj by applying the implication operator
     (18.4) or (18.5) to obtain Bj′ .

  3. Aggregate all Bj′ using (18.6) to obtain the overall output fuzzy set Bagg .




                                       376
Modern Intelligent Systems                                        Fuzzy inference


 Risk & audit
    • Rule explosion: too many overlapping rules can make behavior
      opaque; prune with coverage and conflict diagnostics.

    • Operator mismatch: min/product implication and max/sum
      aggregation produce different surfaces; choose once and document
      why.

    • Membership miscalibration: poorly scaled sets can overfire or
      underfire rules; audit control-surface smoothness and boundary
      behavior.

    • Defuzzification sensitivity: centroid vs. weighted average can shift
      outputs materially; test with edge-case inputs.

    • Deployment drift: sensor scaling changes break rule semantics;
      version normalization and monitor post-deployment residuals.

    In sup-T form this is the same compositional rule of inference used in Chap-
ter 17; here T defaults to min (or product) and sup reduces to a max on discrete
grids.
    The final step, defuzzification, converts Bagg into a crisp output value. One
widely used approach is the centroid (center-of-gravity) method, which computes
                                 R
                              ∗     y µBagg (y) dy
                             y = RY                .                       (18.7)
                                   Y µBagg (y) dy

   This expression balances all candidate output values y by weighting them
according to their membership grade in the aggregated fuzzy set. In discrete
implementations, the integral is replaced with a sum over sampled output points.

Other defuzzifiers Common alternatives are mean/center of maxima (robust
to multi-modal sets), smallest/largest of maxima (conservative tie-breaks), and
center of sums (less sensitive to overlap than max aggregation). Choose centroid
for smoothness, a max-based rule for fast or safety-critical switches, and always
handle the zero-mass case explicitly.




                                      377
Modern Intelligent Systems                                       Fuzzy inference


Zero-mass fallback If the denominator in (18.7) is zero (e.g., all consequents
clipped to zero), fall back to a max-membership or rule-based tie-breaker to
avoid NaNs; log the condition for debugging.

Computation note With uniform sampling over m output points, centroid
costs O(mR) per evaluation for R rules. Non-singleton inputs add a convolution
step but reuse the same aggregation/defuzz pipeline; refine the grid near peaks
to reduce bias.
  Centroid stability and tie-breaking
    • Multi-modal sets. When Bagg has multiple peaks, the centroid may
      fall between modes. Log numerator and denominator separately and
                 R
      check that µBagg (y) dy is non-zero; otherwise fall back to
      max-membership or a rule-based tie-break.

    • Discretisation. Sampling the universe with too few points biases
      the centroid. Use uniform grids for smooth consequents and adaptive
      refinement near peaks for multi-modal sets. Report the step size (e.g.,
      0.5◦ C) to show numeric fidelity.


18.6   Worked example: thermostat inference with numbers
We now run one complete inference pass for a compact thermostat rule base with
two inputs and one output. The goal is not to defend a particular membership
design, but to show how the algebra produces a concrete output that you can
compute, audit, and debug.

Universes and memberships. Let temperature error e ∈ [−5, 5] ◦ C and rate
r ∈ [−2, 2] ◦ C/min. Let the controller output u ∈ [0, 1] denote heater power as




                                      378
Modern Intelligent Systems                                                      Fuzzy inference


a fraction of maximum. We use simple piecewise-linear labels:
                    
                    
                             e ≤ −5,                                                
                    1,                                                    |e|
      µCold (e) = 0−e ,       −5 < e < 0,          µComfy (e) = max 0, 1 −                ,
                  5                                                      2.5
                    
                        0,    e ≥ 0,
                                                                   
                                                                   
                                                                            r ≤ 0,
                                                                   0,
     µStable (r) = max(0, 1 − |r|) ,               µRising (r) =     r
                                                                     2 , 0 < r < 2,
                                                                   
                                                                   
                                                                   
                                                                     1, r ≥ 2.
```

### Findings
Issues found:

1. **Notation inconsistency in Example (continued) for projections:**

   - The example computes projections µπX(R) and µπY(R) as sets of max values:
     ```
     µπX (R) = {max(0.5, 0.5), max(0.8, 0.9)} = {0.5, 0.9},
     µπY (R) = {max(0.5, 0.8), max(0.5, 0.9)} = {0.8, 0.9},
     ```
     However, the notation `{...}` suggests a set or vector, but the projection is a fuzzy set over X or Y, so the output should be a function or vector indexed by elements of X or Y, not a set literal. This could confuse readers.

   - Suggestion: Use vector notation or explicitly state the membership function values for each element, e.g.,
     ```
     µπX(R)(x1) = max(0.5, 0.5) = 0.5,
     µπX(R)(x2) = max(0.8, 0.9) = 0.9,
     ```
     similarly for µπY(R).

2. **Ambiguity in the definition of projection:**

   - The projection onto X is defined as:
     ```
     µπX (R)(x) = sup_{y ∈ Y} µR(x, y)
     ```
     but in the example, the projection onto Y is also computed as:
     ```
     µπY (R)(y) = sup_{x ∈ X} µR(x, y)
     ```
     This is not explicitly stated in the text. The text only defines projection onto X, but the example uses projection onto Y as well.

   - Suggestion: Explicitly define projection onto Y as:
     ```
     µπY (R)(y) = sup_{x ∈ X} µR(x, y)
     ```
     for completeness and clarity.

3. **Inconsistent use of notation for supremum and maximum:**

   - The text uses "sup" and "max" interchangeably in discrete examples, which is acceptable, but the notation sometimes uses "sup" and sometimes "max" without clarifying that for finite universes sup = max.

   - Suggestion: Add a note clarifying that for finite discrete universes, suprema reduce to maxima.

4. **In the max–min composition pseudocode:**

   - The pseudocode uses variables i, j, k for indices over X, Y, Z respectively, but the text uses x, y, z for elements of universes.

   - This is acceptable, but the pseudocode should clarify the correspondence to avoid confusion.

5. **In the "Author’s note: choosing an operator family":**

   - The phrase "If the resulting surfaces are too flat, tighten the t-norm; if they are too brittle, loosen it." is somewhat informal and may confuse readers unfamiliar with the terminology.

   - Suggestion: Clarify what "tighten" and "loosen" mean in terms of t-norm parameters or choice.

6. **In the "Zero-mass fallback" section:**

   - The fallback strategy is described as "fall back to a max-membership or rule-based tie-breaker to avoid NaNs," but no explicit formula or algorithm is given.

   - This is acceptable as a practical note, but readers may benefit from a more concrete description or reference.

7. **In the thermostat membership functions at the end:**

   - The piecewise definitions for µCold(e), µComfy(e), µStable(r), and µRising(r) are incomplete or inconsistent:

     - For µCold(e), the text shows:
       ```
       µCold (e) = 0−e ,       −5 < e < 0,
       ```
       but the formula is incomplete or misformatted. It likely intends:
       ```
       µCold(e) = (0 - e)/5,  for -5 < e < 0,
       ```
       or similar.

     - For µComfy(e), the formula is:
       ```
       µComfy (e) = max(0, 1 - |e|/2.5),
       ```
       but the text shows:
       ```
       µComfy (e) = max 0, 1 − |e| / 2.5,
       ```
       which is missing parentheses and proper formatting.

     - For µStable(r), the formula is:
       ```
       µStable (r) = max(0, 1 - |r|),
       ```
       but the domain is not specified clearly.

     - For µRising(r), the piecewise definition is incomplete and misformatted:
       ```
       µRising (r) = r/2, 0 < r < 2,
       ```
       but the other cases are not clearly stated.

   - Suggestion: Rewrite all membership functions with clear piecewise definitions, proper parentheses, and domain specifications.

8. **Minor typographical issues:**

   - In the text, sometimes the multiplication dot is missing or inconsistent, e.g., "α · µB(y)" vs. "α µB(y)".

   - The use of quotation marks around matrices (e.g., " # ... ") is nonstandard and may confuse readers.

---

No issues spotted regarding mathematical correctness of fuzzy relation composition, properties, or inference steps. The explanations and examples are consistent and reproducible given the corrections above.

## Chunk 27/31
- Character range: 737487–767926

```text
For u, use the standard three-label output family (Low/Medium/High) from
Chapter 16:
                                                  
                        µLow (u) = max 0, 1 − 0.5
                                                u
                                                     ,
                                                      
                     µMedium (u) = max 0, 1 − |u−0.5|
                                                 0.25    ,
                                               
                       µHigh (u) = max 0, u−0.5
                                            0.5   .

Rule base.
  1. IF e is Cold AND r is Stable THEN u is High.

  2. IF e is Cold AND r is Rising THEN u is Medium.

  3. IF e is Comfy THEN u is Low.

Fuzzify inputs and compute firing strengths.                       For inputs e = −2 and
r = 0.5,

µCold (−2) = 0.4,       µComfy (−2) = 0.2,    µStable (0.5) = 0.5,       µRising (0.5) = 0.25.

With T = min (Equation (18.2)), the rule firing strengths are

      α1 = min(0.4, 0.5) = 0.4,         α2 = min(0.4, 0.25) = 0.25,           α3 = 0.2.

Implication, aggregation, and defuzzification. Using Mamdani min-
implication (Equation (18.4)), each consequent is clipped at its firing strength



                                             379
Modern Intelligent Systems                                        Fuzzy inference


(e.g., µ′High (u) = min(α1 , µHigh (u))). Aggregating consequents by max (Equa-
tion (18.6)) yields µout (u). Finally, centroid defuzzification (Equation (18.7))
produces a crisp heater-power command. Using a uniform grid on u ∈ [0, 1]
(step 10−4 ) gives
                                      u⋆ ≈ 0.577.

This value is above the midpoint because the Cold rules (High/Medium conse-
quents) fire more strongly than the Comfy rule, while the positive rate term
(Rising) tempers full-High output. In implementations, compute the centroid
numerically (and log the grid/step size) rather than relying on heuristic convex
combinations when overlap patterns become complex.


  Pipeline at a glance (Mamdani/Larsen)
  for each rule j:
      alpha_j = T( mu_A1(x1), ..., mu_An(xn) )
          # firing strength
      mu_Bj_prime(y) = implication(alpha_j, mu_Bj(y))
          # clip or scale
  mu_Bagg(y) = S( mu_B1_prime(y), ..., mu_BR_prime(y) )
      # aggregate
  y_star = centroid(mu_Bagg(y))
      # or another defuzzifier

  Defaults: T = min or product; S = max; centroid defuzzification.
  Non-singleton fuzzification (convolving input uncertainty with µAi ) uses
  the same pipeline once the input blend is computed.




                                      380
Modern Intelligent Systems                                             Fuzzy inference


 Design checklist
    • Define universes/labels; ensure coverage and reasonable overlap.

    • Pick T /S/ ⇒ via Table 9 to get the smoothness/interpretability you
      need.

    • Verify rule-base coverage; avoid contradictions/holes.

    • Choose defuzzifier and sampling resolution; set a minimum-mass
      fallback.

    • Test monotonicity/saturation; refine membership widths or rule
      weights.

 Common pitfalls
    • Max aggregation can mask contributions from several moderate rules;
      algebraic sum can over-saturate.

    • Memberships that are too narrow yield sparse firing; too wide
      produce mushy outputs.

    • Coarse grids bias centroids; inconsistent units across labels break
      interpretability.

    • Neglecting non-singleton inputs: if sensor noise matters, blur inputs
      before fuzzifying.


18.7   Mamdani vs. Sugeno/Takagi–Sugeno systems
Mamdani-style inference (scaled fuzzy consequents, centroid defuzzification) ex-
cels when linguistic interpretability is a priority and when rule consequents must
remain human-readable.
Sugeno/Takagi–Sugeno (TSK) systems replace fuzzy consequents with crisp
functions such as aﬀine models,

               IF e is Ai AND ė is Bi THEN ui = pi e + qi ė + ri .




                                       381
Modern Intelligent Systems                                                 Fuzzy inference


Each rule still produces a firing strength λi via a t-norm, but the final output
becomes the weighted average
                                       P
                                   ∗       λi u i
                                  u = Pi          ,
                                           i λi

eliminating the defuzzification integral. The trade-offs are:
   • Mamdani: transparent consequents, straightforward incorporation of
     expert knowledge, but higher computational cost due to aggregation and
     centroid evaluation.

   • Sugeno/TSK: faster evaluation (weighted averages), amenable to
     gradient-based tuning of the consequent parameters, yet less interpretable
     because consequents are numerical functions rather than linguistic labels.
    For the thermostat example, Mamdani rules (“IF error is Cold AND rate
is Falling THEN heater power is High”) are ideal when operators must audit
decisions, whereas a Sugeno/TSK variant is preferable when embedding the
controller into a high-speed or automatically tuned loop. 2
   2
    Classic sources: Mamdani and Assilian (1975) for clipping implication; Takagi and Sugeno
(1985) for TSK; Jang (1993) for ANFIS; see also (Klement et al., 2000; Dubois and Prade,
1988) for operator/implicator theory.




                                           382
Modern Intelligent Systems                                      Fuzzy inference


 Key takeaways
    • Fuzzy inference composes rule antecedents (via a t-norm) and
      modifies consequents by implication.

    • Aggregation and defuzzification (e.g., centroid) produce crisp outputs
      from fuzzy rule bases.

    • Design choices (operators, shapes) trade interpretability and control
      smoothness.

 Minimum viable mastery.
    • For a rule base, compute firing strengths, apply implication,
      aggregate consequents, and compute a centroid output.

    • Explain the Mamdani vs. Sugeno/TSK tradeoff (interpretability vs.
      eﬀiciency/tunability).

    • Treat operator choice as part of the specification and keep it
      consistent across examples and implementations.
 Common pitfalls.
    • Defining memberships on incompatible scales (inputs never trigger, or
      everything triggers).

    • Writing many redundant rules and then tuning symptoms rather
      than consolidating the rule base.

    • Comparing controllers without stating operators, defuzzification, and
      evaluation protocol.




                                     383
Modern Intelligent Systems                                           Fuzzy inference


 Exercises and lab ideas
    • Implement a Mamdani thermostat with three error labels and two
      rate labels; experiment with min/product t-norms and report the
      resulting control surfaces.

    • Build a Sugeno/TSK variant of the same controller and compare
      outputs to the Mamdani version under identical test trajectories.

    • Evaluate different defuzzification methods (centroid, weighted
      average, max membership) on a toy rule base and quantify the
      steady-state error they induce.

 If you are skipping ahead. When you reach Chapter 19, keep this
 chapter’s audit instinct: log your design choices. Evolutionary and fuzzy
 systems both invite silent degrees of freedom that only become visible with
 disciplined reporting.


Where we head next. Chapter 19 shifts from fuzzy controllers to evolution-
ary computing, where population-based search and optimization heuristics form
the other major soft-computing pillar.
 Part III takeaways
    • Soft computing makes uncertainty explicit: degrees of membership
      and rule-based aggregation.

    • Interpretability is a design variable: rules, operators, and
      defuzzification encode assumptions.

    • Debugging is empirical: test edge cases, inspect rule firing, and
      validate monotonicity and scale.

    • The same audit mindset applies: define failure modes up front and
      track them as you tune operators and rules.




                                      384
Modern Intelligent Systems                                                     19



Part IV: Evolutionary optimization
19    Introduction to Evolutionary Computing
Parts I–IV built three complementary toolkits: optimize models against data
(ERM), learn representations with gradients, and encode auditable heuristics
with fuzzy rules. Each is powerful when you can write a smooth objective or
commit to a compact rule base. Many engineering choices, however, live outside
that comfort zone: the knobs are discrete or tightly constrained, evaluations are
noisy or expensive, and the landscape is rugged enough that local improvement
is unreliable.
    Evolutionary computing treats that situation as search. Instead of following
gradients or hand-tuning rules, we maintain a population of candidate designs,
score them with a fitness function, and use selection plus variation to explore
and refine solutions within a fixed budget. After the fuzzy trilogy (Chapters 15
to 18), this chapter develops the evolutionary strand introduced in Chapter 1
and focuses on population-based optimization under constraints, budgets, and
stochastic noise.
  Learning Outcomes
     • Explain the evolutionary-computation toolbox (GAs, GP, CMA-ES,
       DE) and when each is well-suited.

     • Implement population-based optimization loops with selection,
       crossover/mutation, and constraint handling.

     • Diagnose convergence, premature stagnation, and feasibility
       trade-offs on examples such as controller tuning.

  Design motif
  When gradients are unavailable or the landscape is rugged, treat design as
  search: maintain a diverse population, score candidates with a fitness
  function, and let selection plus variation drive improvement under
  constraints.




                                      385
Modern Intelligent Systems                                                     19


19.1   Context and Motivation
Evolutionary computing is the strand you reach for when the objective is a black
box (simulation, experiment, or expensive audit) or when the design space is a
mix of continuous and discrete choices. The modeling contract stays simple:
pick an encoding, define a fitness function, state the constraints, and commit to
an evaluation budget. The algorithm then trades exploration (diversity) against
exploitation (selecting what works) as it searches a rugged landscape.
    In the fuzzy trilogy, once you commit to membership shapes and a rule base,
a practical question remains: how do you tune those choices (and their trade-
offs) when hand tweaks do not scale? Evolutionary search provides a disciplined
answer: score candidate controllers, select the better ones, perturb/recombine
them, and keep iterating until the improvements flatten or the budget runs out.

19.2   Philosophical and Historical Background
Evolutionary computing traces its roots back to the 1950s and 1960s, contempo-
raneous with early developments in neural networks. It is important to recognize
that evolutionary algorithms are not direct scientific models of biological evolu-
tion; rather, they are inspired by a simplified, abstracted view of evolutionary
principles such as selection, mutation, and reproduction.

Key Insight: These algorithms are heuristics; they provide practical methods
to find good enough solutions to problems that are otherwise computationally
intractable, rather than guaranteed optimal solutions. Consequently, conver-
gence proofs typically ensure improvement in expectation or under restrictive
assumptions, but not attainment of the true global optimum.
 Author’s note: a pragmatic take on evolution
 Evolutionary algorithms borrow the language of biology to provide a
 disciplined way to search rugged landscapes, not to recreate population
 genetics. The design mandate is pragmatic: deliver a respectable solution
 within the computational budget, even if it is only approximately optimal.
 Keep that lens in mind when evaluating selection, mutation, or
 recombination operators; they are tuned because they help optimization,
 not because they are biologically faithful.



                                       386
Modern Intelligent Systems                                                     19


19.3   Problem Setting: Optimization
 Notation handoff
 Vectors of candidate solutions are written as x, objective values as f (x),
 and population members as individuals/chromosomes depending on
 encoding. If symbol reuse from earlier chapters becomes ambiguous,
 default to local definitions and consult Appendix D.

   Consider an optimization problem where the goal is to find an input vector
x ∈ Rn that minimizes (or maximizes) a given objective function f : Rn → R.
Formally, we want to solve



                              x∗ = arg min f (x),                          (19.1)
                                       x∈D

    where D ⊆ Rn is the feasible domain incorporating any bound, equality, or
inequality constraints required by the application.

Challenges:
  • The function f may be non-convex, exhibiting multiple local minima and
    maxima.

  • There may be no closed-form or deterministic method to find the global
    optimum.

  • The search space D can be large or complex, making exhaustive search
    (brute force) computationally prohibitive.

  • Real-time or practical constraints often require solutions within limited
    time frames.

19.4   Illustrative Example
Imagine a function f with multiple peaks and valleys (local maxima and minima).
The global minimum is the lowest valley, but many local minima exist that can
trap naive optimization methods.

Goal: Instead of guaranteeing the global optimum, evolutionary computing
aims to find a good enough solution—one that is suﬀiciently close to optimal

                                      387
Modern Intelligent Systems                                                   19


and found within a reasonable computational budget.

19.5   Why Not Brute Force?
While brute force search guarantees finding the global optimum by evaluating
all possible candidates, it is often infeasible due to:
   • Computational complexity: The number of candidate solutions can be
     astronomically large.

   • Time constraints: Real-world applications often require timely decisions,
     making exhaustive search impractical.
    For example, in control systems, one might want to tune parameters to
regulate temperature or pressure optimally. Waiting for a brute force search to
complete could be unacceptable, whereas a near-optimal solution found quickly
is valuable.

19.6   Summary
Evolutionary computing provides a framework to address complex optimization
problems by mimicking evolutionary processes. It embraces the notion of ap-
proximate solutions that are computationally feasible and practically useful.
    The sections that follow develop the core components of evolutionary al-
gorithms: representations, selection, crossover/mutation operators, constraint
handling, and representative applications.
    This “rugged landscape” picture is a useful mental model when you later
interpret convergence traces, premature stagnation, and diversity metrics in
population-based search.

19.7   Challenges in Continuous Optimization and Motivation for
       Evolutionary Computing
In many continuous optimization problems, the objective function may be unde-
fined or discontinuous in certain regions of the domain. For example, consider
a function with singularities or points where the function value is not defined
(akin to division by zero). Such characteristics pose significant challenges for
classical optimization methods such as gradient descent or hill climbing, which
rely on smoothness and continuity to navigate the search space effectively.



                                      388
Modern Intelligent Systems                                                   19


Issues with Traditional Methods
  • Undefined regions: The presence of undefined or discontinuous regions
    means that the gradient or directional derivatives may not exist, preventing
    the use of gradient-based methods.

  • Local optima and plateaus: Even when the function is defined, it
    may have multiple local optima or flat regions where the gradient is zero,
    causing algorithms to get stuck.

  • Complex constraints: Problems such as integer programming introduce
    combinatorial constraints that are not amenable to continuous optimiza-
    tion techniques.

  • Computational complexity: Many optimization problems are NP-
    hard, meaning no known deterministic polynomial-time algorithm can
    solve them exactly.
    Given these challenges, deterministic approaches may be infeasible or compu-
tationally expensive. Instead, we can tolerate approximate solutions and employ
heuristic or metaheuristic methods that explore the search space more flexibly.
This motivates the use of evolutionary computing methods.

19.8   Introduction to Evolutionary Computing
Evolutionary computing (EC) is a class of algorithms inspired by the process
of natural evolution. These algorithms are designed to iteratively improve can-
didate solutions to optimization problems by mimicking mechanisms such as
selection, reproduction, and mutation observed in biological evolution.

Key Idea The goal is to design an algorithm that can solve parameter esti-
mation or optimization problems by evolving a population of candidate solu-
tions over successive generations. Unlike deterministic methods, evolutionary
algorithms do not require gradient information or continuity and can handle
complex, multimodal, and constrained problems.

Genetic Algorithms (GAs) One of the most well-known evolutionary al-
gorithms is the Genetic Algorithm (GA). GAs attempt to naively mimic the



                                      389
Modern Intelligent Systems                                                    19


process of biological evolution, albeit with a simplified and abstracted model of
genetic mechanisms.

19.9   Biological Inspiration: Evolutionary Concepts
To understand GAs, we briefly review relevant biological concepts:

Chromosomes and Genes In biology, an organism’s genetic information is
encoded in chromosomes, which are long sequences of DNA. Each chromosome
contains many genes, which determine specific traits.

Cell Division: Mitosis vs. Meiosis
  • Mitosis: A process where a cell divides to produce two genetically identi-
    cal daughter cells, each containing the full chromosome set (e.g., 46 chro-
    mosomes, i.e., 23 pairs in humans). This process is responsible for growth
    and tissue repair.

  • Meiosis: A specialized form of cell division that produces gametes (sperm
    or egg cells) with half the number of chromosomes (haploid). When two
    gametes combine during fertilization, they form a new cell with a full set
    of chromosomes (diploid), mixing genetic material from both parents.

Genetic Recombination and Variation During meiosis, chromosomes un-
dergo crossover events. Segments of genetic material are exchanged between
paired chromosomes.
Recombination increases genetic diversity.

Inheritance and Heredity The offspring’s chromosomes are a mixture of the
parents’ genetic material, but not a simple half-and-half split. Instead, genes
from multiple previous generations contribute to the genetic makeup, introduc-
ing variability and enabling adaptation over time.

19.10 Implications for Genetic Algorithms
The biological processes suggest several principles that GAs incorporate:
  • Population-based search: Maintain a population of candidate solutions
    (analogous to organisms).


                                      390
Modern Intelligent Systems                                                  19


  • Selection: Preferentially choose better solutions to reproduce, mimicking
    survival of the fittest.

  • Crossover (Recombination): Combine parts of two or more parent so-
    lutions to create offspring solutions, promoting exploration of new regions
    in the search space.

  • Mutation: Introduce random changes to offspring to maintain diversity
    and avoid premature convergence.

  • Generational evolution: Repeat the process over multiple generations,
    gradually improving solution quality.
     The stochastic nature of these operations allows GAs to explore complex,
multimodal landscapes and handle problems where deterministic methods strug-
gle.

19.11 Summary of Biological Mechanisms Modeled in GAs

     Biological Process          GA Analog
     Chromosomes and genes       Encoding of candidate solutions
                                 (chromosomes)
     Meiosis and fertilization   Crossover of parent chromosomes to
                                 produce offspring
     Genetic recombination       Mixing of solution components
     Mutation                    Random perturbations in offspring
     Selection                   Fitness-based selection of parents and
                                 survivors
     Generations                 Iterative improvement over time

   The remainder of this section formalizes how candidate solutions are encoded
and how genetic operators manipulate those encodings during evolution.




                                      391
Modern Intelligent Systems                                                     19


 GA hyperparameters at a glance
 As a starting point for binary encodings of length L, choose population
 sizes between 5L and 10L, tournament selection with small tournaments
 (2–4 individuals), one-point or uniform crossover, and mutation probability
 near 1/L per bit. For real-coded GAs, replace bit-flips with Gaussian
 mutations on parameters and use simulated binary crossover (SBX) or
 blend-style crossover to mix parents smoothly (Deb and Agrawal, 1995);
 then tune population size and mutation scale empirically based on
 convergence speed and population diversity.

 Author’s note: population and mutation heuristics
 Budget dictates population size and diversity mechanisms. If evaluations
 are cheap, spend them on larger populations to cover the search space; if
 evaluations are expensive, keep populations modest but invest in
 diversity-preserving steps (mutation, niching, restarts) to avoid premature
 convergence. Use the defaults in the box above as a first pass, then tune
 based on convergence traces and diversity diagnostics.


19.12 Genetic Algorithms: Modeling Chromosomes
In the previous discussion, we introduced the concept of diversity in genetic al-
gorithms (GAs) and the probabilistic nature of evolutionary processes. We now
delve deeper into modeling chromosomes and the mechanisms of genetic inheri-
tance, crossover, and mutation, drawing parallels to optimization problems.




                                      392
Modern Intelligent Systems                                                   19


 Genetic algorithm at a glance
 Objective: Optimize an objective J(x) over a discrete or continuous
 search space by evolving a population of encoded candidate solutions
 according to selection, crossover, and mutation.
 Key hyperparameters: Population size, selection pressure (tournament
 size or selection temperature), crossover and mutation rates, encoding
 scheme, and stopping criteria (max generations, no-improvement window,
 target fitness).
 Common pitfalls: Premature convergence due to excessive selection
 pressure or low mutation, deceptive fitness landscapes, constraint violations
 when mutation or crossover produce infeasible solutions, and
 overinterpreting stochastic runs without multiple seeds.


Chromosomes as Information Carriers Recall that chromosomes in GAs
represent candidate solutions encoded as strings of data. For modeling purposes,
we consider each chromosome as a sequence of bits or symbols, each encoding a
piece of information relevant to the problem domain. Formally, let a chromosome
be represented as
                                c = (c1 , c2 , . . . , cL ),

where each gene ci encodes a particular trait or parameter, and L is the chro-
mosome length.

Inheritance and Crossover During reproduction, chromosomes from parent
individuals combine to form offspring. This process involves:
  • Passing genes as-is: Some genes may be inherited unchanged from a
    parent.

  • Crossover: Portions of chromosomes from two parents are recombined to
    produce new gene sequences in offspring.

  • Mutation: Occasionally, genes may undergo random changes, introducing
    new genetic material.
   These mechanisms can be visualized by considering crossover as splicing
two parent strings according to a binary mask and mutation as independently

                                      393
Modern Intelligent Systems                                                               19


                     Selection             Crossover          Constraints




               fit                  1011|001
                                 higher selection prob.        1011|111
                                                          candidate         repair            evaluate
        Figure 71: Evolutionary micro-operators. Left: fitter individuals     get
                                                                 or penalty/feasible-first
             mid often (roulette/tournament).
    sampled more              0100|111           Middle: 0100|001
                                                          crossover splices parents
      by a mask (one-point shown). Right: constraint handling routes offspring
    through repair/penalty/feasibility
              low                      before evaluation. Use it when mapping an
                   implementation to the canonical operator loop.


flipping bits with a small probability.
    Figure 71 summarizes selection, crossover, and constraint handling at the
operator level.

Modeling the Genetic Operations Let p1 and p2 be parent chromosomes.
The offspring chromosome o is formed by combining segments from p1 and p2
according to a crossover pattern x, and then applying mutation m:
                                                           
                          o = Mutate Crossover(p1 , p2 , x) .                        (19.2)

  The crossover operator selects which genes come from which parent, often
modeled by a binary mask x ∈ {0, 1}L , where
                              
                              (p ) , if x = 0,
                                   1 i       i
                         oi =
                              (p2 )i , if xi = 1.

   Mutation introduces random changes with a small probability µ, altering
gene oi to a different value.

Fitness and Selection Each gene or chromosome corresponds to a phenotype,
representing a candidate solution with an associated fitness value f (o). Fitness
quantifies the quality or suitability of the solution, guiding the selection process
for reproduction.
    Consider a set of objects (e.g., facial features such as nose, eyes, lips) encoded


                                               394
Modern Intelligent Systems                                                    19


by chromosomes. Each object variant has a fitness value reflecting its quality or
adaptation. For example, fitness values might be:

                             f = {80, 75, 60, 65, 40, 20}

   Over many generations, chromosomes with higher fitness values have a higher
probability of surviving and reproducing, while those with lower fitness tend to
be eliminated.

Probabilistic Survival and Evolution The survival probability Ps of a chro-
mosome depends on its fitness and the evolutionary dynamics:

                                             f (c)
                                Ps (c) ≈ P          ′
                                                       .
                                             c′ f (c )

   Over multiple generations, this leads to the propagation of fitter chromo-
somes and the gradual improvement of the population.

19.13 Mapping Genetic Algorithms to Optimization Problems
Genetic algorithms can be viewed as heuristic optimization methods. To formal-
ize this analogy, consider the components of an optimization problem:
  • Objective function: J(x), which we seek to maximize or minimize.

  • Constraints: Conditions restricting the feasible set of solutions.

  • Input parameters: Decision variables x.
   In GAs, the chromosome encodes the input parameters x, and the fitness
function corresponds to the objective function J(x).

Key GA Components in Optimization Terms
  • Encoding: The method of representing x as chromosomes.

  • Initial population: The starting set of candidate solutions.

  • Fitness evaluation: Computing f (c) = J(x) for each chromosome.

  • Selection: Choosing chromosomes for reproduction based on fitness.



                                         395
Modern Intelligent Systems                                                        19


  • Crossover and mutation: Generating new candidate solutions by re-
    combining and perturbing chromosomes.

  • Convergence criteria: Determining when the algorithm has suﬀiciently
    optimized the objective.
  Constraint handling in GAs
 Realistic optimization problems often involve constraints gj (x) ≤ 0 or
 hk (x) = 0. Common strategies include (i) repair, which projects infeasible
 offspring back into the feasible set; (ii) penalties, which modify the fitness
                     P
 as f˜(x) = f (x) − ρ j max(0, gj (x)) for some ρ > 0; and (iii) feasibility
 rules, which prefer feasible individuals over infeasible ones at equal
 objective value. Penalty methods are simple and mesh well with existing
 GA code, while repair and feasibility rules are preferable when constraints
 encode hard physical or safety limits.


Fitness as Objective Function Proxy The fitness function guides the
search towards optimal solutions. The closer a chromosome’s phenotype is to
the desired optimum, the higher its fitness:

                         f (c) ∝ closeness to optimum.

   This relationship allows GAs to explore the solution space stochastically,
balancing exploitation of high-fitness regions and exploration via mutation and
```

### Findings
No issues spotted.

## Chunk 28/31
- Character range: 767928–797648

```text
19.14 Encoding in Genetic Algorithms
Recall that encoding is the process of representing the parameters of an optimiza-
tion problem as a genotype, typically a string of symbols (often binary digits),
which can be manipulated by genetic operators such as crossover and mutation.

Genotype and Phenotype
  • Genotype: The encoded representation of a solution, e.g., a binary string.

  • Phenotype: The decoded solution in the problem domain, e.g., real-
    valued parameters.



                                       396
Modern Intelligent Systems                                                    19


    The goal is to design an encoding scheme that allows eﬀicient exploration
of the search space while respecting constraints and enabling effective genetic
operations.

19.14.1   Common Encoding Schemes
1. Binary Encoding Each parameter is represented as a binary string of
fixed length. For example, if a parameter xi is to be represented with precision
p, the length of the binary string is chosen accordingly.
  • Advantages: Simple, well-studied, easy to implement crossover and muta-
    tion.

  • Disadvantages: May suffer from Hamming cliffs (large phenotypic changes
    from small genotypic changes).

2. Floating-Point Encoding       Parameters are represented directly as floating-
point numbers.
  • Advantages: No decoding needed, natural representation for real-valued
    parameters.

  • Genetic operators can be adapted, e.g., crossover by averaging.

  • Disadvantages: More complex mutation and crossover operators; may re-
    quire specialized operators to maintain diversity.

3. Gray Coding A binary encoding where consecutive numbers differ by only
one bit, reducing the Hamming distance between adjacent values.
  • Useful to reduce large jumps in phenotype space due to small genotypic
    changes.

  • Decoding involves mapping Gray code to decimal values.

19.14.2   Example: Binary Encoding of Parameters
Suppose we want to encode four parameters x1 , x2 , x3 , x4 each represented by
a binary string of length li . The genotype is the concatenation of these binary
strings:




                                      397
Modern Intelligent Systems                                                                               19




       b1,1 b1,2 · · · b1,l1    b2,1 b2,2 · · · b2,l2    b3,1 b3,2 · · · b3,l3   b4,1 b4,2 · · · b4,l4
       |       {z          }    |       {z          }    |       {z          }   |       {z          }
                x1                       x2                       x3                      x4

   For example, a genotype might look like:

                                  011       00100       0101     011110

   Each substring is decoded to a decimal or real value according to the encoding
scheme.

19.14.3      Example Problem: Minimization with Constraints
Consider the problem:
                                                           x 125
                                      min      f (x) =       +
                                        x                  2   x
subject to
                                              0 < x ≤ 15

Encoding Strategy
  • Since x is bounded between 0 and 15, we can encode x as a binary string
    representing integers in [1, 15].

  • For example, 4 bits can represent integers from 0 to 15, so we can use 4
    bits and exclude zero.

  • Each genotype corresponds to a candidate solution x.

Decoding
                               x = decimal value of binary string

   If the decoded value is zero, it is invalid due to division by zero, so such
genotypes are discarded or penalized.

Fitness Evaluation The fitness function corresponds to the objective func-
tion f (x), possibly with penalties for constraint violations.




                                                    398
Modern Intelligent Systems                                                      19


19.15 Population Initialization and Size
Once encoding is decided, the initial population is generated by randomly sam-
pling genotypes within the feasible space.

Population Size
  • Larger populations provide better coverage of the search space but increase
    computational cost.

  • Smaller populations may converge prematurely.

  • Typical sizes range from 20 to several hundreds depending on problem
    complexity.

Example For the problem above, a population of 50 individuals with 4-bit
genotypes representing x ∈ [1, 15] can be initialized by randomly generating 50
binary strings of length 4.

19.16 Genetic Operators
After initialization, genetic operators are applied to evolve the population.

19.16.1   Selection
Selection chooses individuals for reproduction based on fitness.

Common Methods
  • Roulette Wheel Selection: Probability proportional to fitness.

  • Tournament Selection: Randomly select a group and choose the best.

  • Rank Selection: Rank individuals and assign selection probabilities ac-
    cordingly.

19.16.2   Crossover
Crossover combines parts of two parent genotypes to produce offspring.

Binary Crossover
  • Single-point: Choose a crossover point and swap the tail segments of two
    parents.

                                       399
Modern Intelligent Systems                                                        19


  • Two-point: Choose two crossover points and exchange the intermediate
    segment.

  • Uniform: Swap genes independently with a fixed probability.

19.17 Selection in Genetic Algorithms
After encoding candidate solutions as chromosomes (e.g., binary strings), the
next step in a genetic algorithm (GA) is selection, which determines which chro-
mosomes will be chosen to reproduce and form the next generation. The goal
is to favor chromosomes with higher fitness, thereby guiding the search toward
better solutions.

19.17.1    Fitness and Selection Probability
Given a population of N chromosomes, each chromosome i has an associated
fitness value fi . The fitness function quantifies the quality of the solution repre-
sented by the chromosome.
    A common approach to selection is to assign each chromosome a probability
of being chosen proportional to its fitness. This can be expressed as:

                                fi
                         pi = P N         ,   i = 1, 2, . . . , N,            (19.3)
                                 j=1 fj

where pi is the probability that chromosome i is selected.

Roulette Wheel Selection This proportional selection method is often
called roulette wheel selection. Imagine a wheel divided into N slices, each
slice corresponding to a chromosome and sized proportionally to pi . To select
a chromosome, a random number is generated to ”spin” the wheel, and the
chromosome corresponding to the slice where the wheel stops is chosen.
    Key properties:
  • Chromosomes with higher fitness have a larger slice and thus a higher
    chance of being selected.

  • The same chromosome can be selected multiple times, reflecting its relative
    superiority.




                                          400
Modern Intelligent Systems                                                       19


   • This stochastic process maintains diversity but can be sensitive to fitness
     scaling.

Example      Suppose we have 5 chromosomes with fitness values:

                               f = [10, 20, 5, 15, 50].

The total fitness is 100, so the selection probabilities are:

                          p = [0.10, 0.20, 0.05, 0.15, 0.50].

Chromosome 5 has a 50% chance of selection, making it likely to be chosen
multiple times.

19.17.2    Ranking Selection
When fitness values are close or vary widely, roulette wheel selection may not
perform well. For example, if fitness values are very close, selection probabilities
become nearly uniform, reducing selection pressure. Conversely, if one chromo-
some dominates, diversity may be lost prematurely.
   Ranking selection addresses this by assigning selection probabilities based on
the rank of chromosomes rather than raw fitness values.

Procedure
   1. Sort chromosomes by fitness in descending order.

   2. Assign ranks ri such that the best chromosome has rank 1, the second best
      rank 2, and so forth.

   3. Define a selection probability function p(ri ) decreasing with rank.
   A simple linear ranking scheme is:

                                    2 − s 2(ri − 1)(s − 1)
                         p(ri ) =        +                 ,                 (19.4)
                                      N      N (N − 1)

where s ∈ [1, 2] controls selection pressure. When s = 1, all chromosomes have
equal probability; when s = 2, the best chromosome has twice the average
probability.


                                          401
Modern Intelligent Systems                                                   19


Elitism Ranking selection can be combined with elitism, where the best chro-
mosome(s) are guaranteed to survive to the next generation. This ensures that
the highest-quality solutions are preserved.

Advantages
  • Controls selection pressure explicitly.

  • Prevents premature convergence by maintaining diversity.

  • Avoids issues with scaling fitness values.
 Selection pressure and exploration/exploitation
    • Knobs: Tournament size, rank-selection parameter s,
      crossover/mutation rates, and elitism all modulate pressure.

    • High pressure (large tournaments, strong elitism, low mutation)
      speeds exploitation but risks premature convergence.

    • Low pressure (small tournaments, higher mutation) preserves
      diversity but slows progress.

    • Practical default: start with tournament size 2–3, modest elitism
      (top 1–5%), pc ≈ 0.8–0.9, and mutation tuned so 1–5% of bits/genes
      change per generation.


19.18 Crossover Operator
After selection, the crossover operator generates new offspring chromosomes by
recombining parts of two parent chromosomes. This mimics biological reproduc-
tion and promotes exploration of the solution space.

19.18.1   One-Point Crossover
Consider two parent chromosomes represented as binary strings of length L:

                                            (1)   (1)      (1)
                       Parent 1: c(1) = (c1 , c2 , . . . , cL )

                                            (2)   (2)      (2)
                       Parent 2: c(2) = (c1 , c2 , . . . , cL )

   One-point crossover proceeds as follows:


                                        402
Modern Intelligent Systems                                                                        19


  1. Choose a crossover point k uniformly at random from {1, 2, . . . , L − 1}.

  2. Create two offspring by exchanging the tails of the parents at point k:

                                               (1)         (1)     (2)         (2)
                           Offspring 1 = (c1 , . . . , ck , ck+1 , . . . , cL ),
                                               (2)         (2)     (1)         (1)
                           Offspring 2 = (c1 , . . . , ck , ck+1 , . . . , cL ).

   This operator allows mixing of genetic

19.19 Crossover Operators in Genetic Algorithms
In genetic algorithms, crossover is a fundamental operator used to combine the
genetic information of two parent chromosomes to produce new offspring. The
intuition behind crossover is to exchange segments of parent chromosomes to
explore new regions of the solution space.

Single-point crossover is the simplest form of crossover. Given two parent
chromosomes, a crossover point is selected randomly along their length. The
offspring are created by taking the segment before the crossover point from the
first parent and the segment after the crossover point from the second parent,
and vice versa. Formally, if the parents are represented as sequences:

              (1)   (1)                                          (2)     (2)
     P1 = (p1 , p2 , . . . , p(1)          (1)
                              c , . . . , pn ),      P2 = (p1 , p2 , . . . , p(2)          (2)
                                                                              c , . . . , pn ),


where c is the crossover point, then the offspring are:

                                   (1)   (1)               (2)
                          O1 = (p1 , p2 , . . . , p(1)                 (2)
                                                   c , pc+1 , . . . , pn ),

                                   (2)   (2)               (1)
                          O2 = (p1 , p2 , . . . , p(2)                 (1)
                                                   c , pc+1 , . . . , pn ).


Multi-point crossover generalizes this idea by selecting multiple crossover
points. For example, in two-point crossover, two points c1 and c2 are chosen,
and segments between these points are swapped between parents. This can be
visualized as:
                        (1)           (1)              (1)
                 P1 = p1 . . . p(1) p     . . . p(1) p     . . . p(1) ,
                       | {z c1} | c1 +1{z c2} | c2 +1{z n }
                                segment 1      segment 2          segment 3




                                                403
Modern Intelligent Systems                                                      19


                             (2)         (2)          (2)
                   P2 = p1 . . . p(2) p  . . . p(2) p  . . . p(2) .
                        | {z c1} | c1 +1{z c2} | c2 +1{z n }
                             segment 1    segment 2    segment 3

Offspring can be generated by swapping segment 2 between parents, or by other
combinations, leading to multiple possible crossover outcomes.

Probabilistic nature of crossover requires assigning a crossover probability
pc , which governs how often crossover is applied during reproduction. Typically,
pc is set between 0.6 and 0.9, balancing exploration and exploitation.

19.20 Mutation Operator
Mutation introduces random alterations to individual chromosomes, mimicking
biological mutations. It serves to maintain genetic diversity within the popula-
tion and helps the algorithm escape local optima.

Biological motivation Mutation is a rare event in nature but crucial for
evolution. For example, the white coloration of polar bears is a mutation that
provided an adaptive advantage in snowy environments. Similarly, environmen-
tal pressures can select for mutations, such as female elephants in Africa evolving
to lack ivory tusks to avoid poaching.

Role in optimization Mutation allows the algorithm to explore new regions
of the search space that are not reachable by crossover alone. Consider a fitness
landscape with multiple local maxima and minima. Mutation can randomly
perturb a solution, potentially moving it from a local minimum to a region near
a global maximum.

Implementation of mutation In binary-encoded chromosomes, mutation
typically involves flipping a bit:

                                    0 → 1,     1→0

The mutation is applied with a small mutation probability pm , often on the order
of 10−3 to 10−1 .




                                           404
Modern Intelligent Systems                                                     19


Mutation operator formalization Given a chromosome x ∈ {0, 1}n , muta-
tion produces x′ by mutating each gene xi independently with probability pm :
                         
                         1 − x , with probability p ,
                                i                   m
                   x′i =
                          xi ,   with probability 1 − pm

19.21 Summary of Genetic Operators and Their Probabilities
The three main genetic operators in a genetic algorithm are:
  • Selection: Chooses chromosomes for reproduction based on fitness.

  • Crossover: Combines genetic material from two parents to produce off-
    spring.

  • Mutation: Introduces random changes to chromosomes to maintain di-
    versity.
   Each operator is governed by a probability parameter:

                             ps = probability of selection,
                             pc = probability of crossover,
                         pm = probability of mutation

    Tuning these probabilities is critical for balancing exploration and exploita-
tion and for avoiding premature convergence.




                                          405
Modern Intelligent Systems                                                        19


19.22 Known Issues in Genetic Algorithms
 Risk & audit
    • Premature convergence: aggressive selection or weak mutation
      collapses diversity before good regions are explored.

    • Budget mismatch: comparisons are invalid unless algorithms share
      evaluation budgets and stopping rules.

    • Constraint leakage: hidden infeasibility can inflate scores; use
      explicit feasibility checks in logs and plots.

    • Single-run overclaim: stochastic algorithms require multi-seed
      reporting with spread, not one best trajectory.

    • Objective gaming: fitness proxies can drift from deployment goals;
      audit secondary metrics and failure cases.

    While genetic algorithms (GAs) provide a powerful heuristic framework for
optimization, several well-known issues can affect their performance and relia-
bility:

Premature Convergence Because GAs rely on heuristic search without a
global optimality guarantee, they often converge prematurely to local minima
rather than the global minimum. This is especially common if the initial popula-
tion is not diverse or if the selection pressure is too high, causing loss of genetic
diversity early on.
 Diversity maintenance
    • Crowding/sharing: penalize overly similar individuals to keep
      multiple niches in multi-modal landscapes.

    • Restarts/islands: run multiple subpopulations (often in parallel)
      with occasional migration; robust against stagnation.

    • Adaptive mutation: increase mutation or inject random
      individuals when diversity drops.




                                        406
Modern Intelligent Systems                                                      19


Mutation Interference Mutation is intended to introduce diversity and help
escape local minima by randomly altering genes. However, excessive or poorly
controlled mutation can cause oscillations, where beneficial mutations are un-
done by subsequent mutations. This back-and-forth effect can prevent conver-
gence and degrade solution quality.

Deception Deception refers to situations where the encoding or representation
of solutions misleads the GA’s fitness evaluation. Low-order schemata with high
observed fitness may actually guide the search away from the global optimum,
so that combining “good” building blocks produces worse offspring. There is no
single formal definition, but a deceptive fitness landscape is one in which local
improvements inferred from schemata systematically lead the GA to suboptimal
basins of attraction.

Fitness Misinterpretation Since selection is driven by fitness values, any
inaccuracies or misleading fitness evaluations can cause the GA to make poor
decisions about which individuals to propagate. This can arise from noisy fitness
functions, poorly designed objective functions, or deceptive encodings.

19.23 Convergence Criteria
Determining when to stop the GA is a critical practical consideration. Common
convergence criteria include:
  • Fixed number of generations: Run the GA for a predetermined number
    of iterations.

  • Time limit: Stop after a fixed amount of computational time.

  • No improvement: Terminate if the best fitness value has not improved
    over a specified number of generations.

  • Manual inspection: Periodically inspect the population to decide if the
    solutions are satisfactory.
   In practice, a combination of these criteria is often used. For example, one
might stop if either (a) no improvement in the best fitness is observed for 10 con-
secutive generations, or (b) the run reaches 100 generations in total, whichever



                                       407
Modern Intelligent Systems                                                                                19


                                                        Best fitness        Mean fitness
                              1
        Normalized fitness




                                           Flat region ⇒ consider stopping
                             0.8



                             0.6



                             0.4
                                   0   5    10     15       20         25    30     35     40   45   50
                                                              Generation

        Figure 72: Illustrative GA run showing the best and mean normalized
    fitness over 50 generations. Flat regions motivate “no improvement” stopping
        rules, while steady separation between best and mean indicates ongoing
       selection pressure. Use it when diagnosing premature convergence versus
                                  ongoing exploration.


condition is met first. Figure 72 visualizes such a run, making it easy to spot
plateaus and the persistent gap between best and mean fitness.

19.24 Summary of Genetic Algorithm Workflow
To summarize the GA process:
  1. Initialization: Generate an initial population of chromosomes (candidate
     solutions).

  2. Fitness Evaluation: Compute the fitness value for each chromosome
     based on the objective function.

  3. Termination Check: If a satisfactory solution is found or a stopping
     criterion is met, terminate.

  4. Selection: Select parent chromosomes based on fitness (e.g., roulette
     wheel, tournament).

  5. Crossover: Apply crossover operators to parents to produce offspring.

  6. Mutation: Apply mutation operators to offspring to maintain diversity.



                                                                 408
Modern Intelligent Systems                                                                                 19


   7. Replacement: Form the new population from offspring (and possibly
      some parents).

   8. Repeat: Return to step 2.
    This iterative cycle continues until convergence or stopping criteria are met.
The flow diagram in Figure 73 summarizes the control structure on a single page
                                                yes / stop
for quick reference.

    Initialization
                           Fitness evaluation                     Termination?
 random population


                                                        no

                                                   inner loop

                               Selection                              Crossover                 Mutation
                                                next generation




                                                                    Replacement



       Figure 73: GA flowchart showing the iterative process: initialization leads
           to fitness evaluation and a termination check. If not terminated, the
       algorithm proceeds through selection, crossover, mutation, and replacement,
          which then feeds the next generation’s fitness evaluation. Use it when
         verifying that your implementation preserves the intended control flow.


Step                         Example bitstrings                                   Decoded x   Fitness f (x)
Initial (subset)             00012 , 00102 , 01012 ,                        0.0625, 0.125,      0.40, 0.13,
                             01112                                         0.3125, 0.4375      -0.52, -0.02
Select parents (example)     00102 , 01012                                  0.125, 0.3125       0.13, -0.52
Crossover (one-point)        Parents: 00|10, 01|01                         0.0625, 0.3750        0.40, 0.29
                             → offspring: 00|01,
                             01|10
Mutation (flip one bit)      01102 → 01112                                           0.4375            -0.02

  Table 10: Toy GA generation on a bounded interval. One crossover and mutation
 illustrate how the fitness function guides selection before the next generation. Use it
        when explaining how variation operators interact with selection pressure.

   Table 10 is the step-by-step toy generation trace used to ground the operator
sequence.



                                                     409
Modern Intelligent Systems                                                  19


 Defaults that work (DE/CMA-ES)
 Differential Evolution (DE): start with population 10−20 × D
 (dimension D), mutation scale F ∈ [0.5, 0.8], crossover Cr ∈ [0.7, 0.9].
 CMA-ES: population λ ≈ 4 + b3 ln Dc, initial step-size σ0 ≈ 0.3 of the
 variable range. These defaults are robust first tries before tuning.


19.25 Pseudocode Representation
The GA can be expressed in pseudocode as follows:

Initialize population P with N chromosomes
Evaluate fitness of each chromosome in P

while termination criteria not met do
    Select parents from P based on fitness
    Apply crossover to parents to create offspring
    Apply mutation to offspring
    Evaluate fitness of offspring
    Replace some or all of P with offspring
end while

Return best chromosome found

19.26 Example: GA for a Constrained Optimization Problem
Consider the problem of minimizing the function:
                                                          
                             f (x) = cos(5πx) · exp −x2

subject to the constraint:
                                    0 ≤ x ≤ 0.5

with a precision of three decimal places.

GA Parameters:
  • Population size: 10 chromosomes



                                        410
Modern Intelligent Systems                                                      19


  • Encoding: Real-valued x encoded with 3 decimal places (i.e., precision of
    0.001)

  • Crossover probability: 25%

  • Mutation probability: 10%

  • Selection: All chromosomes are selected for crossover or mutation (no
    explicit selection probability)

Initialization: Generate 10 random values of x uniformly distributed in
[0, 0.5], each rounded to three decimal places. When prior designs or surrogate
models exist, warm start a few chromosomes with those known-good solutions
before filling the rest randomly; seeding accelerates convergence without losing
diversity if you keep most of the population stochastic.

Fitness Evaluation: Calculate f (x) for each chromosome. Since this is a
minimization problem, fitness can be defined as the negative of the function
value or by using a suitable transformation to ensure higher fitness corresponds
to better solutions.

Evolutionary Cycle: Apply selection, crossover, and mutation to produce
new offspring, then evaluate their fitness. Repeat this process for multiple gen-
erations until convergence criteria are met.

Remarks: In practice, some initial chromosomes may fall outside the con-
straint bounds due to rounding or mutation; these should be clipped or repaired
to maintain feasibility.
    As an illustration, consider an initial population with fitness values computed
directly from f (x):

    {0.041, 0.178, 0.203, 0.247, 0.311, 0.328, 0.359, 0.402, 0.435, 0.496}.

Each chromosome uses a 9-bit fixed-point code (3 fractional digits), decoded by
interpreting the bits as an integer n and scaling via x = n/1000. Chromosomes
decoding to x = 0 are discarded or repaired.
    A single generation could proceed as follows:

                                       411
Modern Intelligent Systems                                                     19


  • Select the top five chromosomes by fitness.

  • Apply one-point crossover at the 5th bit to produce offspring (e.g., parents
    0.203 and 0.359 yield 0.209 and 0.353).

  • Mutate each bit with probability 0.1, ensuring all decoded values remain
    within [0, 0.5].

  • Re-evaluate fitness and retain the best ten individuals for the next gener-
    ation.
 Constraint handling playbook
    • Penalty methods soften constraints by augmenting the fitness with
                                               P
      a violation term, e.g., F (x) = f (x) + λ k max{0, gk (x)}2 ; increase λ
      when infeasible individuals survive too often.

    • Repair operators project infeasible chromosomes back into the
      feasible region (clip bound violations, renormalize equality
      constraints, or rerun a problem-specific solver) before evaluation.

    • Feasibility-first selection ranks feasible candidates ahead of
      infeasible ones, then compares raw fitness only within each group;
      among infeasible solutions, select those with the smallest violation.

    • Deb’s feasibility rules (Deb, 2001): (i) if one solution is feasible
      and the other is not, pick the feasible one; (ii) if both are feasible,
      pick the better objective; (iii) if both are infeasible, pick the one with
      smaller total constraint violation. Adaptive penalties can be layered
      on top when violations persist.

 Reproducibility and fair comparison Fix random seeds when
 debugging, run many seeds (e.g., 20+) for reporting, match evaluation
 budgets across algorithms, and report mean/median best-so-far with
 variability bands. Log all hyperparameters and share code/configs to make
 comparisons fair, following Appendix E as the default reporting template.
 Penalty terms are easy to implement, repair operators exploit domain
 knowledge, and feasibility-first policies are useful in safety-critical
 controllers where violating constraints is unacceptable even temporarily.



                                      412
Modern Intelligent Systems                                                      19
```

### Findings
1. **Section 19.18.1 One-Point Crossover (p. 402):**

   - The offspring definitions appear incorrect or incomplete. The text states:

     > Create two offspring by exchanging the tails of the parents at point k:
     >
     > Offspring 1 = (c1, ..., ck, ck+1, ..., cL)
     >
     > Offspring 2 = (c1, ..., ck, ck+1, ..., cL)

     Both offspring are written identically, which is not correct. The standard one-point crossover produces:

     - Offspring 1: first k genes from Parent 1, remaining from Parent 2
     - Offspring 2: first k genes from Parent 2, remaining from Parent 1

     This should be explicitly stated and the notation corrected.

2. **Section 19.19 Crossover Operators (p. 403):**

   - The notation for parents and offspring is inconsistent and confusing. For example:

     > P1 = (p1, p2, ..., p(1)c, ..., pn), P2 = (p1, p2, ..., p(2)c, ..., pn)

     The superscripts and subscripts are not clearly defined, and the use of parentheses is inconsistent.

   - The offspring definitions:

     > O1 = (p1, p2, ..., p(1)c, pc+1, ..., pn)
     >
     > O2 = (p1, p2, ..., p(2)c, pc+1, ..., pn)

     Here, "pc+1" is ambiguous—does it come from parent 1 or 2? The notation should clearly indicate which parent's genes are taken before and after the crossover point.

   - Suggest using consistent notation such as:

     - Parent 1: \( (p_1^{(1)}, p_2^{(1)}, \ldots, p_c^{(1)}, p_{c+1}^{(1)}, \ldots, p_n^{(1)}) \)
     - Parent 2: \( (p_1^{(2)}, p_2^{(2)}, \ldots, p_c^{(2)}, p_{c+1}^{(2)}, \ldots, p_n^{(2)}) \)
     - Offspring 1: \( (p_1^{(1)}, \ldots, p_c^{(1)}, p_{c+1}^{(2)}, \ldots, p_n^{(2)}) \)
     - Offspring 2: \( (p_1^{(2)}, \ldots, p_c^{(2)}, p_{c+1}^{(1)}, \ldots, p_n^{(1)}) \)

3. **Section 19.20 Mutation Operator Formalization (p. 404):**

   - The mutation operator is defined as:

     \[
     x_i' = \begin{cases}
     1 - x_i, & \text{with probability } p_m \\
     x_i, & \text{with probability } 1 - p_m
     \end{cases}
     \]

     However, the text uses:

     > \( x_i' = \{ 1 - x_i, \text{ with probability } p, \quad x_i, \text{ with probability } 1 - p_m \} \)

     The probability symbol \( p \) is used instead of \( p_m \) in the first case, which is inconsistent and likely a typo.

4. **Section 19.26 Example: GA for a Constrained Optimization Problem (p. 410-411):**

   - The problem states:

     \[
     f(x) = \cos(5\pi x) \cdot e^{-x^2}
     \]

     with \( 0 \leq x \leq 0.5 \).

     - The fitness values given:

       \[
       \{0.041, 0.178, 0.203, 0.247, 0.311, 0.328, 0.359, 0.402, 0.435, 0.496\}
       \]

       are positive and increasing, but since this is a minimization problem, the fitness should be inversely related to \( f(x) \) or transformed accordingly. The text mentions fitness can be negative of the function or transformed, but the example does not clarify how these fitness values relate to \( f(x) \).

     - The example of crossover producing offspring values 0.209 and 0.353 from parents 0.203 and 0.359 is plausible but lacks explanation of how the bit-level crossover leads to these decimal values. More detail or a step-by-step decoding would improve reproducibility.

5. **General Notation and Clarity:**

   - Throughout the chunk, notation for indices, superscripts, and subscripts is inconsistent or ambiguous, especially in sections describing crossover and encoding.

   - Some equations and expressions are split awkwardly or use inconsistent fonts (e.g., mixing math and text fonts), which may confuse readers.

6. **Claims and Reproducibility:**

   - The text correctly emphasizes the need for multiple seeds and reporting variability for stochastic algorithms, which is good.

   - The "Defaults that work" section (p. 409) mentions DE and CMA-ES parameters without references or justification. While these are common heuristics, citing sources or empirical studies would strengthen the claim.

**Summary:**

- The main concrete issues are the incorrect or unclear definitions of offspring in one-point crossover (19.18.1), inconsistent and confusing notation in crossover descriptions (19.19), a typo in mutation operator probabilities (19.20), and insufficient detail in the example problem's fitness and decoding steps (19.26).

- Notation inconsistencies and ambiguous expressions appear throughout and should be standardized for clarity.

- No unverifiable claims are made; the text generally aligns with standard GA knowledge.

**Recommendation:**

- Correct the offspring definitions in 19.18.1.

- Revise crossover notation in 19.19 for clarity and consistency.

- Fix the mutation probability typo.

- Expand the example in 19.26 to clarify decoding and fitness calculation.

- Standardize notation throughout the chapter.

## Chunk 29/31
- Character range: 797650–828628

```text
19.27 Genetic Algorithms: Iterative Process and Convergence
Recall that in genetic algorithms (GAs), we start with an initial population of
candidate solutions, each represented by a chromosome encoding a potential so-
lution vector. The fitness of each candidate is evaluated by plugging the encoded
values into the objective function. Based on these fitness values, selection prob-
abilities are assigned, favoring candidates with higher fitness (for maximization
problems) or lower fitness (for minimization problems).

Selection and Reproduction Selection is typically stochastic but biased to-
wards fitter individuals. For example, in a population of size N = 10, some
individuals may be selected multiple times, while others may not be selected at
all. This process ensures that better solutions have a higher chance of propagat-
ing their genetic material to the next generation.

Crossover and Mutation         After selection, genetic operators such as crossover
and mutation are applied:
  • Crossover: With a certain probability (e.g., 25%), pairs of selected chro-
    mosomes exchange segments of their genetic code to produce offspring.
    This recombination explores new regions of the solution space by mixing
    existing solutions.

  • Mutation: With a smaller probability (e.g., 10%), random changes are
    introduced to individual genes in the chromosomes. Mutation maintains
    genetic diversity and helps prevent premature convergence to local optima.

Evolution Over Generations By iterating the cycle of selection, crossover,
and mutation over multiple generations, the population gradually evolves to-
wards better solutions. Early generations may have widely dispersed candidate
solutions, but as evolution proceeds, solutions cluster around local maxima or
minima of the fitness landscape.
    In practice, after a suﬀicient number of generations (e.g., 16 in the example),
the algorithm often converges to a solution with the highest fitness value found
so far. While this is not guaranteed to be the global optimum, it often provides
a very good approximation.



                                       413
Modern Intelligent Systems                                                       19


19.28 Beyond canonical GAs: real-coded strategies
Bit-string encodings are ideal for combinatorial search, yet most engineering
problems have continuous decision variables. Two mature real-coded families
are now standard tools:
   • Covariance Matrix Adaptation Evolution Strategy (CMA-ES)
     (Hansen and Ostermeier, 2001) maintains a multivariate Gaussian search
     distribution. Successful steps update the mean, adapt the global step size,
     and rotate the covariance to align with the landscape’s principal directions.
     CMA-ES shines on smooth, ill-conditioned black-box functions where gra-
     dients are unavailable but the objective rewards second-order adaptation.

   • Differential Evolution (DE) (Storn and Price, 1997) perturbs a target
     vector with scaled differences of two other individuals, v = xr +F (xp −xq ),
     then mixes v with the original via binomial or exponential crossover. This
     simple mechanism balances exploration/exploitation with only three hy-
     perparameters (F, Cr , N ) and handles noisy, non-smooth objectives well.
   Both algorithms plug into the same evaluation loop shown earlier and can
reuse the constraint-handling policies in the preceding box. In practice many
teams prototype with DE (fast, few knobs) and switch to CMA-ES when the
problem demands higher precision or adaptive covariance modeling.

19.29 Genetic Programming (GP)
Genetic programming extends the principles of genetic algorithms to the evo-
lution of computer programs or symbolic expressions rather than fixed-length
parameter vectors.

Problem Setup Consider a problem where the relationship between input
variables x1 , x2 , . . . , xn and output y is unknown. Unlike traditional parameter
estimation, we do not assume a fixed functional form. Instead, we want to
discover the function f such that

                              y = f (x1 , x2 , . . . , xn ).

Representation of Programs In GP, candidate solutions are represented as
tree-like structures encoding mathematical expressions or programs composed

                                          414
Modern Intelligent Systems                                                         19


of:
      • Terminals: Input variables (x1 , x2 , . . .) and constants.

      • Functions: Arithmetic operations (addition, subtraction, multiplication,
        division), logical operations, or other domain-specific functions.
      For example, a candidate program might represent the expression

                                 (x1 × x3 ) + (x1 + x4 ).

Genetic Operators in GP
      • Crossover: Subtrees from two parent programs are exchanged to create
        offspring programs.

      • Mutation: Random modifications are made to nodes in the program tree,
        such as changing an operator or replacing a subtree.
   These operations allow the evolution of increasingly complex and effective
programs.

Fitness Evaluation A candidate program is evaluated by executing it on a
training set and comparing its outputs with the desired targets. Fitness func-
tions often measure mean squared error, classification accuracy, or accumulated
reward, and penalize programs that raise runtime exceptions or exceed resource
limits. Individuals with higher fitness are more likely to be selected for repro-
duction.

Example        Suppose we have the following initial program trees:

                         Parent 1:   f1 = (x1 × x3 ) + (x1 + x4 )
                         Parent 2:    f2 = (x2 − 5) × (x4 + 1)

   Suppose we exchange the right subtree of f1 (the addition node x1 +x4 ) with
the left subtree of f2 (the subtraction node x2 − 5). The resulting offspring are

               f1′ = (x1 × x3 ) + (x2 − 5),         f2′ = (x1 + x4 ) × (x4 + 1).




                                              415
Modern Intelligent Systems                                                    19


Mutation might then replace the terminal x4 in f1′ with a constant (e.g., 5) or
switch the addition operator to multiplication, thereby exploring nearby pro-
gram structures while keeping the tree depth bounded.

Recursive and Modular Programs GP can evolve recursive functions and
modular code blocks (subroutines), enabling the discovery of complex behaviors
and algorithms. In practice this is achieved by allowing trees to reference au-
tomatically defined functions (ADFs) or macros that are evolved alongside the
main program. The depth of the program trees and the number of reusable
modules are usually constrained to prevent uncontrolled growth and to keep
execution cost manageable.

Applications Genetic programming is particularly useful for:
  • Symbolic regression: discovering analytical expressions fitting data.

  • Automated program synthesis:        generating code for control, decision-
    making, or data processing.

  • Robotics: evolving control programs for navigation, obstacle avoidance, or
    manipulation.

Example: Robot Obstacle Avoidance Consider evolving a program that
controls a robot’s movement based on sensor inputs indicating obstacles. The
function set might include commands like move_forward, turn_left, turn_-
right, and conditional statements. The GP evolves sequences and combinations
of these commands to maximize the robot’s ability to navigate without collisions.

Summary      Genetic programming generalizes genetic

19.30 Wrapping Up Genetic Algorithms and Genetic Program-
      ming
In this final segment of the chapter, we conclude our discussion on genetic al-
gorithms (GAs) and genetic programming (GP), emphasizing their conceptual
foundations, practical implications, and the distinctions between them.




                                      416
Modern Intelligent Systems                                                    19


Recap of Genetic Algorithms Genetic algorithms are population-based
metaheuristic optimization methods inspired by natural selection and genetics.
They operate on a population of candidate solutions, iteratively applying genetic
operators such as selection, crossover, and mutation to evolve solutions toward
optimality. The key components include:
  • Representation: Encoding candidate solutions as chromosomes (bit
    strings, real vectors, etc.).

  • Fitness Function: Quantifies the quality of each candidate solution.

  • Genetic Operators:

        – Selection favors fitter individuals.
        – Crossover recombines genetic material from parents.
        – Mutation introduces random variations.

  • Evolutionary Cycle: Repeat selection and genetic operations until con-
    vergence or stopping criteria are met.

Genetic Programming: Structure over Parameters Genetic program-
ming extends the GA paradigm by evolving computer programs or symbolic
expressions rather than fixed-length parameter vectors. The fundamental differ-
ence is that GP searches over the space of program structures (trees of functions
and terminals) instead of numeric parameter values.
   Key points about GP include:
  • Representation: Programs are represented as hierarchical trees, where
    internal nodes are functions (e.g., arithmetic operators, logical functions)
    and leaves are terminals (input variables, constants).

  • Evolution of Programs: Genetic operators manipulate program trees:

        – Crossover exchanges subtrees between parent programs.
        – Mutation randomly modifies nodes or subtrees.

  • Fitness Evaluation: Programs are executed on input data, and their
    outputs are compared against desired outputs to compute fitness.



                                       417
Modern Intelligent Systems                                                   19


  • Emergent Solutions: GP can discover novel program structures that
    model complex phenomena without explicit programming, often yielding
    surprising and insightful results.

Applications and Insights Genetic programming is particularly powerful
for modeling complex systems where the underlying relationships are unknown
or diﬀicult to specify explicitly. For example, given inputs such as wind speed,
humidity, and temperature, GP can evolve models that predict environmental
phenomena without prior assumptions about the functional form.
    This capability highlights the strength of GP as a tool for automated model
discovery and symbolic regression.

Further Topics and Extensions While this chapter provided a concise
overview, the field of evolutionary computation encompasses many advanced
topics, including:
  • Multi-objective Genetic Algorithms: Handling optimization prob-
    lems with multiple conflicting objectives.

  • Constraint Handling: Incorporating problem-specific constraints into
    the evolutionary process.

  • Hybrid Methods: Combining GAs/GP with other optimization or ma-
    chine learning techniques.

  • Scalability and Parallelization: Eﬀiciently implementing evolutionary
    algorithms for large-scale problems.
    Readers are encouraged to explore these topics through further reading and
research; the short primer below highlights the most widely used multi-objective
GA.

19.31 Multi-objective search and NSGA-II
When two or more objectives conflict, we seek a set of Pareto-optimal solutions
rather than a single best point. The Non-dominated Sorting Genetic Algorithm
II (NSGA-II) sorts each generation into Pareto fronts: rank-1 individuals are
non-dominated, rank-2 are dominated only by rank-1, etc. Replacement pre-
serves all members of the best fronts and uses crowding distance to maintain

                                      418
Modern Intelligent Systems                                                               19



                                 1.0               Pareto front
                                                   Dominated solutions
                                 0.8
                 f2 (minimise)   0.6
                                 0.4
                                 0.2
                                 0.0
                                    0.0   0.2    0.4    0.6     0.8   1.0
                                                f1 (minimise)
       Figure 74: Sample Pareto front for two objectives. NSGA-II keeps all
      non-dominated points (blue) while pushing dominated solutions (orange)
    toward the front via selection, yielding a spread of trade-offs in one run. Use it
     when interpreting multi-objective results as trade-offs, not a single optimum.


diversity along the trade-off curve. NSGA-II’s combination of elitist survival
and O(N log N ) non-dominated sorting makes it the default baseline for multi-
objective evolutionary optimization (Deb et al., 2002).

Metrics and variants Hypervolume (area/volume dominated by the front
with respect to a reference point) is a common scalar indicator; report it along-
side the spread of solutions (Zitzler et al., 2002). MOEA/D decomposes objec-
tives into weighted subproblems; SPEA2/IBEA are popular alternatives. Always
plot the Pareto set and budget-matched hypervolume traces when comparing al-
gorithms.
    Figure 74 is the trade-off view used to interpret multi-objective runs.




                                                  419
Modern Intelligent Systems                                                     19


 Key takeaways
    • Evolutionary algorithms optimize without gradients by iterating
      selection, variation, and replacement under a fitness evaluation loop.

    • Constraint handling is part of the design: penalties, repair, and
      feasibility-first selection each encode a different notion of “acceptable”
      search.

    • Multi-objective search replaces a single optimum with a Pareto front;
      NSGA-II is a standard baseline for producing diverse trade-offs.

 Minimum viable mastery.
    • Specify genotype, variation operators, selection scheme, and
      termination criteria in a way that is reproducible.

    • Distinguish constraint handling strategies and justify the one used
      (penalty vs. repair vs. feasibility rules).

    • Report multi-objective results as trade-offs (Pareto fronts) rather
      than as a single scalar score.
 Common pitfalls.
    • Over-interpreting a single stochastic run (report multiple seeds and
      dispersion).

    • Using aggressive selection and low mutation, collapsing diversity and
      getting stuck in deceptive basins.

    • Comparing algorithms without matching evaluation budget (fitness
      calls), constraint handling, and stopping rules.




                                      420
Modern Intelligent Systems                                                       19


 Exercises and lab ideas
                                                               
    • Implement a simple GA for f (x) = cos(5πx) exp −x2 , experimenting
      with penalty vs. repair strategies for the [0, 0.5] constraint.

    • Prototype a CMA-ES or Differential Evolution solver on a noisy
      Rosenbrock function and compare convergence traces against the
      canonical GA.

    • Build a tiny GP to rediscover a closed-form expression (e.g.,
      y = x3 + x) from samples; report how often crossover/mutation
      produce valid programs.

 If you are skipping ahead. This chapter is largely self-contained. If you
 revisit earlier model chapters, keep the common thread in mind: every
 method still requires a clear objective, a diagnostic that detects failure, and
 a reporting protocol that survives replication.


Where we head next. This chapter closes the soft-computing thread. For
targeted refreshers, Appendix A summarizes linear-systems prerequisites and
Appendix B consolidates kernel-method context used earlier in the book.
 Part IV takeaways
    • Evolutionary search is an optimization tool when gradients are
      unavailable or unreliable.

    • Operators (selection, crossover, mutation) encode exploration vs.
      exploitation; tune them against variance across runs.

    • Constraints and multi-objectives are first-class: define feasibility and
      trade-offs before optimizing.

    • Report reproducibly: seeds, multiple runs, and distributions matter
      more than a single best trajectory.




                                      421
Modern Intelligent Systems         19



Back matter




                             422
Modern Intelligent Systems                                                     19



Key Takeaways
Chapter 1             About This Book explains how to read the book, points to
                      the notation/figure conventions, and motivates the
                      four-level taxonomy for systems thinking across chapters.

Chapter 2             Symbolic Integration and Problem-Solving Strategies
                      shows how safe substitutions, heuristic branches, and
                      numeric fallbacks cooperate in a transformation tree,
                      giving a procedural view of algebraic problem solving.

Chapter 3             Supervised Learning Foundations develops
                      ERM/MLE/MAP, contrasts loss families, and grounds
                      diagnostics such as learning curves, calibration, and
                      proper scoring rules.

Chapter 4             Classification and Logistic Regression reuses the
                      Chapter 3 toolkit to build probabilistic classifiers,
                      emphasize ROC/PR analysis, and reason about class
                      imbalance, calibration, and optimization choices (Newton
                      vs. first-order).

Chapter 5             Introduction to Neural Networks casts the perceptron as a
                      thresholded linear classifier (vs. logistic as the smooth
                      probabilistic counterpart), proves convergence guarantees,
                      and catalogues practical pitfalls such as poor feature
                      scaling or non-separable data.

Chapter 6             MLP Foundations formalizes forward/backward passes
                      with matrix-calculus identities, highlights
                      caching/normalization for numerical stability, and frames
                      bias–variance behavior for deep linear stacks.

Chapter 7            Backpropagation in Practice turns the derivatives into
                     SGD/mini-batch pseudocode, adds early-stopping
                     heuristics, and compares optimization tweaks
                     (momentum, adaptive schedules) against the diagnostics
                     from Chapter 3.


                                      423
Modern Intelligent Systems                                                    19


Chapter 8            Radial Basis Function Networks interprets RBFs as local
                     “bubbles,” covers center/width selection (including
                     practical σ rules), contrasts primal vs. dual training
                     formulations, and connects the finite-basis view to kernel
                     methods (e.g., kernel ridge regression and SVMs with
                     RBF kernels).

Chapter 9            Self-Organizing Maps explains neighborhood
                     competition/cooperation phases, quality measures
                     (quantization/topographic error), and visualization tricks
                     for prototype-based embedding.

Chapter 10            Hopfield and Energy-Based Memories derives
                      discrete/continuous dynamics, capacity bounds, and
                      asynchronous vs. synchronous update strategies for
                      associative recall.

Chapter 11            Convolutional Neural Networks and Deep Training Tools
                      details convolution/cross-correlation, pooling,
                      receptive-field growth, and the engineering defaults
                      behind modern CNN blocks and training loops.

Chapter 12            Recurrent Neural Networks develops BPTT, gating
                      strategies, and conditioning tricks (teacher forcing,
                      scheduled sampling) for sequential modeling while
                      connecting to the diagnostics from earlier chapters.

Chapter 13            NLP Pipelines and Responsible Deployment links
                      static/contextual embeddings to downstream tasks, adds
                      bias/calibration checklists, and closes with a
                      deployment-readiness assessment.

Chapter 14           Transformers and Attention consolidates scaled
                     dot-product attention, multi-head blocks,
                     encoder/decoder stacks, long-context strategies
                     (RoPE/ALiBi, FlashAttention, KV caches), and PEFT
                     techniques.

Chapter 15            Soft Computing Orientation positions fuzzy logic,

                                       424
Modern Intelligent Systems                                                       19


                      neurocomputing, probabilistic reasoning, and
                      evolutionary search as complementary tools and
                      introduces the running thermostat example used in
                      Chapters 16 to 18.

Chapter 16            Fuzzy Sets and Membership Functions defines linguistic
                      variables, membership design patterns, set operations,
                      and inclusion metrics that quantify vagueness and
                      overlap.

Chapter 17            Fuzzy Relations and the Extension Principle covers
                      Cartesian products, projections, and composition
                      operators (max–min, algebraic, Łukasiewicz) that
                      transfer fuzzy information across universes.

Chapter 18            Fuzzy Inference Systems assembles complete Mamdani
                      and Sugeno pipelines (aggregation, implication,
                      defuzzification) and studies practical operator choices,
                      scaling, and thermostat/autofocus examples.

Chapter 19            Evolutionary and Population-Based Search surveys
                      canonical GAs, GP, CMA-ES, and Differential Evolution,
                      emphasizing constraint handling, budget-aware
                      population sizing, and integration with the rest of the
                      toolkit.




                                      425
Modern Intelligent Systems                                                  19


 Four-level taxonomy in practice
 Level 1 (reactive systems): Feedback loops and associative memories
 that respond instantly, e.g., Hopfield dynamics in Chapter 10 or the
 thermostat-style fuzzy controllers introduced across Chapters 16 to 18.
 Level 2 (deliberative planners): Rule-based systems that reason over
 an internal linguistic state before acting; see the fuzzy relation and
 inference machinery of Chapters 16 to 18, where conditions aggregate
 before a crisp recommendation is issued.
 Level 3 (adaptive learners): Data-driven models that update
 parameters from data, spanning the ERM toolkit (Chapters 3 to 4),
 perceptrons/MLPs/RBFs/CNNs (Chapters 5 to 8 and Chapter 11),
 sequence models and Transformers (Chapters 12 to 14), SOMs (Chapter 9),
 and population heuristics (Chapter 19).
 Level 4 (meta-cognitive agents): Algorithms that reason about their
 own learning loops: calibration and uncertainty estimation (Chapters 3
 to 4), training diagnostics and early-stop policies (Chapter 7),
 alignment/PEFT tooling for Transformers (Chapter 14), and self-adaptive
 evolutionary strategies (Chapter 19). These illustrate early steps toward
 systems that refine their own policies.

    Figure 75 provides the visual map for this chapter-level taxonomy.
    Table 11 is the compact lookup for model-family placement across levels and
learning signals.




                                     426
Modern Intelligent Systems                                                                            19




                                Level 1         Level 2               Level 3           Level 4
                                                Linear /           Kernel SVMs /
              Prob./kernel
                                                logistic             RBF nets


                                                                      RNNs /         Transformers /
             Connectionist                  MLPs / CNNs
                                                                    seq. models           LMs



Unsupervised / competitive                                  SOMs



                                             Fuzzy             Fuzzy
          Fuzzy rule-based
                                           controllers       inference



     Evolutionary / search                                 GA / GP



                                                           Hopfield /
             Energy-based
                                                         energy models




                                Legend:          supervised;                self-/unsupervised;

                                                 rules / hybrid;            search / associative;




      Figure 75: Color-coded map of model families across agent level, model
     nature, and learning signal. Use this when deciding which family matches a
                     required capability and where to read next.




                                          427
Modern Intelligent Systems                                                             19




   Table 11: Big-picture view of model families across the taxonomy and learning
   paradigms. Each entry represents a family introduced in the book; supervision
    labels indicate the dominant training signal rather than strict exclusivity. Use
    this when you want to locate which model family matches a needed capability
                         and what learning signal it relies on.

Model family            Level              Nature                Learning signal
Linear / logistic        2–3            probabilistic            supervised
regression
Kernel SVMs and          2–3        probabilistic / kernel       supervised
RBF networks
MLPs / CNNs               3             connectionist            supervised
RNNs / sequence           3             connectionist            supervised /
models                                                           self-supervised
Transformers /           3–4            connectionist            self-supervised
attention LMs
Self-organizing          2–3    unsupervised / competitive       unsupervised
maps (SOMs)
Fuzzy controllers        1–2          fuzzy rule-based           supervised / expert
and inference                                                    rules
systems
Genetic algorithms       1–3            evolutionary             search /
and GP                                                           fitness-driven
Hopfield and             1–3            energy-based             associative /
modern Hopfield                                                  unsupervised
variants




                                         428
Modern Intelligent Systems                                          References



References
Daniel J. Amit, Hanoch Gutfreund, and Haim Sompolinsky. Storing infinite
 numbers of patterns in a spin-glass model of neural networks. Physical Review
 Letters, 55(14):1530–1533, 1985. doi: 10.1103/physrevlett.55.1530.

Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman,
 and Dan Mané. Concrete problems in AI safety. arXiv preprint, 2016.

Ronald C. Arkin. Behavior-Based Robotics. MIT Press, 1998.

Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E. Hinton. Layer normalization,
  2016.

Wyllis Bandler and Ladislav J. Kohout. Semantics of implication operators and
 fuzzy relational products. International Journal of Man-Machine Studies, 12
 (1):89–116, 1980. doi: 10.1016/s0020-7373(80)80055-1.

Mikhail Belkin, Daniel Hsu, Siyuan Ma, and Soumik Mandal. Reconciling mod-
 ern machine-learning practice and the classical bias–variance trade-off. Pro-
 ceedings of the National Academy of Sciences, 116(32):15849–15854, 2019. doi:
 10.1073/pnas.1903070116.

Samy Bengio, Oriol Vinyals, Navdeep Jaitly, and Noam Shazeer. Scheduled
  sampling for sequence prediction with recurrent neural networks. In Advances
  in Neural Information Processing Systems (NeurIPS), volume 28, 2015.

Yoshua Bengio, Patrice Simard, and Paolo Frasconi. Learning long-term de-
  pendencies with gradient descent is diﬀicult. IEEE Transactions on Neural
  Networks, 5(2):157–166, 1994. doi: 10.1109/72.279181.

Christopher M. Bishop. Neural Networks for Pattern Recognition. Oxford Uni-
 versity Press, 1995.

Tolga Bolukbasi, Kai-Wei Chang, James Zou, Venkatesh Saligrama, and Adam
  Kalai. Man is to computer programmer as woman is to homemaker? debiasing
  word embeddings. In Advances in Neural Information Processing Systems
 (NeurIPS), volume 29, pages 4349–4357, 2016.



                                     429
Modern Intelligent Systems                                          References


Manuel Bronstein. Symbolic Integration I: Transcendental Functions. Springer,
 2nd ed., 2005.

Rodney A. Brooks. A robust layered control system for a mobile robot. IEEE
 Journal on Robotics and Automation, 2(1):14–23, 1986. doi: 10.1109/jra.1986.
 1087032.

Chi-Tsong Chen. Linear System Theory and Design. Oxford University Press,
 3rd ed., 1999.

Kyunghyun Cho, Bart van Merriënboer, Dzmitry Bahdanau, and Yoshua Ben-
 gio. On the properties of neural machine translation: Encoder–decoder ap-
 proaches. In Conference on Empirical Methods in Natural Language Processing
 (EMNLP), pages 103–111, 2014. doi: 10.3115/v1/w14-4012.

Corinna Cortes and Vladimir Vapnik. Support-vector networks. Machine Learn-
 ing, 20(3):273–297, 1995. doi: 10.1023/a:1022627411411.

M. Cottrell and J. C. Fort. A stochastic model of retinotopy: A self orga-
 nizing process. Biological Cybernetics, 53(6):405–411, 1986. doi: 10.1007/
 bf00318206.

Michael T. Cox and A. Raja. Metareasoning: A manifesto. AI Magazine, 32(1):
 39–54, 2011. doi: 10.1609/aimag.v32i1.2304.

Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. Flashat-
  tention: Fast and memory-eﬀicient exact attention with IO-awareness. In
  Advances in Neural Information Processing Systems (NeurIPS), 2022.

Kalyanmoy Deb. Multi-Objective Optimization Using Evolutionary Algorithms.
 Wiley, 2001.

Kalyanmoy Deb and Ram Bhushan Agrawal. Simulated binary crossover for
 continuous search space. In Complex Systems, volume 9, pages 115–148, 1995.
 URL https://www.complex-systems.com/abstracts/v09_i02_a02/.
```

### Findings
No issues spotted.

## Chunk 30/31
- Character range: 828631–852100

```text
Kalyanmoy Deb, Amrit Pratap, Sameer Agarwal, and T. Meyarivan. A fast
 and elitist multiobjective genetic algorithm: NSGA-II. IEEE Transactions on
 Evolutionary Computation, 6(2):182–197, 2002. doi: 10.1109/4235.996017.


                                     430
Modern Intelligent Systems                                         References


Tim Dettmers, Younes Belkada, and Luke Zettlemoyer. QLoRA: Eﬀicient fine-
  tuning of quantized LLMs. In Advances in Neural Information Processing
  Systems (NeurIPS), 2023.

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert:
  Pre-training of deep bidirectional transformers for language understanding.
  In North American Chapter of the Association for Computational Linguistics:
  Human Language Technologies (NAACL-HLT), pages 4171–4186, 2019.

Didier Dubois and Henri Prade. Fuzzy Sets and Systems: Theory and Applica-
  tions. Academic Press, 1980.

Didier Dubois and Henri Prade. Possibility Theory: An Approach to Computer-
  ized Processing of Uncertainty. Plenum Press, 1988.

Richard O. Duda, Peter E. Hart, and David G. Stork. Pattern Classification.
  Wiley, 2nd ed., 2001.

Jeffrey L. Elman. Finding structure in time. Cognitive Science, 14:179–211,
  1990. doi: 10.1207/s15516709cog1402_1.

E. Erwin, K. Obermayer, and K. Schulten. Self-organizing maps: Ordering,
  convergence properties and energy functions. Biological Cybernetics, 67(1):
  47–55, 1992. doi: 10.1007/bf00201801.

Bernd Fritzke. A growing neural gas network learns topologies. In Ad-
  vances in Neural Information Processing Systems (NeurIPS), volume 7, pages
  625–632, 1994. URL https://proceedings.neurips.cc/paper/1994/hash/
  1ccefb98e3ce8f4d1536b8f2f6f7f15a-Abstract.html.

Yarin Gal and Zoubin Ghahramani. A theoretically grounded application of
  dropout in recurrent neural networks. In Advances in Neural Information
  Processing Systems (NeurIPS), volume 29, 2016.

Felix A. Gers, Jürgen Schmidhuber, and Fred Cummins. Learning to forget:
  Continual prediction with LSTM. Neural Computation, 12(10):2451–2471,
  2000. doi: 10.1162/089976600300015015.

David E. Goldberg. Genetic Algorithms in Search, Optimization, and Machine
 Learning. Addison-Wesley, 1989.

                                    431
Modern Intelligent Systems                                           References


Ian Goodfellow, Yoshua Bengio, and Aaron Courville. Deep Learning. MIT
  Press, 2016.

Albert Gu, Isys Johnson, and Tri Dao. Mamba: Linear-time sequence modeling
  with selective state spaces. arXiv preprint, 2023.

Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. On calibration of
  modern neural networks. In International Conference on Machine Learning
 (ICML), 2017.

Nikolaus Hansen and Andreas Ostermeier. Completely derandomized self-
  adaptation in evolution strategies. Evolutionary Computation, 9(2):159–195,
  2001. doi: 10.1162/106365601750190398.

Trevor Hastie, Robert Tibshirani, and Jerome Friedman. The Elements of Sta-
  tistical Learning. Springer, 2nd ed., 2009.

Simon Haykin. Neural Networks and Learning Machines. Pearson, 3rd ed., 2009.

Simon Haykin. Adaptive Filter Theory. Pearson, 5th ed., 2013.

Francisco Herrera and Manuel Lozano.        Fuzzy Evolutionary Computation.
  Springer, 2008.

Donald R. Hill. Studies in Medieval Islamic Technology. Routledge, 1998.

Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. Neural
  Computation, 9(8):1735–1780, 1997. doi: 10.1162/neco.1997.9.8.1735.

Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, et al. Training compute-
  optimal large language models. In arXiv preprint, 2022.

John H. Holland. Adaptation in Natural and Artificial Systems. University of
  Michigan Press, 1975.

John J. Hopfield. Neural networks and physical systems with emergent collective
  computational abilities. Proceedings of the National Academy of Sciences, 79
  (8):2554–2558, 1982. doi: 10.1073/pnas.79.8.2554.




                                     432
Modern Intelligent Systems                                          References


Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li,
  Shean Wang, Lu Wang, and Weizhu Chen. LoRA: Low-rank adaptation of
  large language models. In International Conference on Learning Representa-
 tions (ICLR), 2022.

IEEE Global Initiative on Ethics of Autonomous and Intelligent Systems. Ethi-
  cally aligned design. 1st ed. white paper, 2019. IEEE Standards Association.

Hisao Ishibuchi and Tomohiro Nakashima. Fuzzy Multiobjective Optimization:
  Evolutionary and Genetic Algorithms. Springer, 2007.

Jyh-Shing Roger Jang. ANFIS: Adaptive-network-based fuzzy inference system.
  IEEE Transactions on Systems, Man, and Cybernetics, 23(3):665–685, 1993.
  doi: 10.1109/21.256541.

Kenneth A. De Jong. Evolutionary Computation: A Unified Approach. MIT
  Press, 2006.

Daniel Jurafsky and James H. Martin. Speech and language processing, 2023.
 Draft (3rd ed.), chapters available online.

Thomas Kailath. Linear Systems. Prentice Hall, 1980.

Jared Kaplan, Sam McCandlish, Tom Henighan, et al. Scaling laws for neural
  language models. In arXiv preprint, 2020.

Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimiza-
  tion. International Conference on Learning Representations (ICLR), 2015.

Erich P. Klement, Radko Mesiar, and Endre Pap. Triangular Norms. Trends in
  Logic. Springer, 2000.

George J. Klir and Bo Yuan. Fuzzy Sets and Fuzzy Logic: Theory and Applica-
 tions. Prentice Hall, 1995.

Teuvo Kohonen. Self-organized formation of topologically correct feature maps.
  Biological Cybernetics, 43(1):59–69, 1982. doi: 10.1007/bf00337288.

Teuvo Kohonen. Self-Organizing Maps. Springer, 3rd ed., 2001.



                                     433
Modern Intelligent Systems                                            References


John R. Koza. Genetic Programming: On the Programming of Computers by
  Means of Natural Selection. MIT Press, 1992.

Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hinton. Imagenet classification
  with deep convolutional neural networks. Advances in Neural Information
  Processing Systems (NeurIPS), 25:1097–1105, 2012.

Dmitry Krotov and John J. Hopfield. Dense associative memory for pattern
 recognition. Advances in Neural Information Processing Systems (NeurIPS),
 29, 2016.

Dmitry Krotov and John J. Hopfield. Large associative memory problem in
 neurobiology and machine learning. Journal of Statistical Mechanics: Theory
 and Experiment, page 034003, 2020.

David Krueger, Tegan Maharaj, Jörg Tiedemann, et al. Zoneout: Regularizing
 rnns by randomly preserving hidden activations. In International Conference
 on Learning Representations (ICLR), 2017.

Omer Levy and Yoav Goldberg. Neural word embedding as implicit matrix fac-
 torization. In Advances in Neural Information Processing Systems (NeurIPS),
 2014.

Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In-
   ternational Conference on Learning Representations (ICLR), 2019.

J. B. MacQueen. Some methods for classification and analysis of multi-
  variate observations. In Proceedings of the Fifth Berkeley Symposium on
  Mathematical Statistics and Probability, pages 281–297, 1967. URL https:
  //projecteuclid.org/euclid.bsmsp/1200512992.

Ebrahim H. Mamdani and Sedrak Assilian. An experiment in linguistic synthesis
  with a fuzzy logic controller. International Journal of Man-Machine Studies,
  7(1):1–13, 1975. doi: 10.1016/s0020-7373(75)80002-2.

T. M. Martinetz, S. G. Berkovich, and K. J. Schulten. Neural-gas network
  for vector quantization and its application to time-series prediction. IEEE
 Transactions on Neural Networks, 4(4):558–569, 1993. doi: 10.1109/72.238311.


                                      434
Modern Intelligent Systems                                            References


Warren S. McCulloch and Walter Pitts. A logical calculus of the ideas immanent
 in nervous activity. The Bulletin of Mathematical Biophysics, 5(4):115–133,
 1943. doi: 10.1007/bf02478259.

Robert J. McEliece, Edward C. Posner, Eugene R. Rodemich, and Santosh S.
 Venkatesh. The capacity of the hopfield associative memory. IEEE Trans-
 actions on Information Theory, 33(4):461–482, 1987. doi: 10.1109/tit.1987.
 1057328.

Charles A. Micchelli. Interpolation of scattered data: Distance matrices and
  conditionally positive definite functions. Constructive Approximation, 2(1):
 11–22, 1986. doi: 10.1007/bf01893414.

Tomas Mikolov, Martin Karafiát, Lukas Burget, Jan Černocký, and Sanjeev
  Khudanpur. Recurrent neural network based language model. In Interspeech,
  2010. doi: 10.21437/interspeech.2010-343.

Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. Eﬀicient estima-
  tion of word representations in vector space. In International Conference on
  Learning Representations (ICLR), 2013.

Melanie Mitchell. An Introduction to Genetic Algorithms. MIT Press, 1998.

Katsuhiko Ogata. Modern Control Engineering. Prentice Hall, 5th ed., 2010.

Jihun Park and Irene W. Sandberg. Universal approximation using radial-basis-
  function networks. Neural Computation, 3(2):246–257, 1991. doi: 10.1162/
  neco.1991.3.2.246.

Jeffrey Pennington, Richard Socher, and Christopher D. Manning. Glove:
  Global vectors for word representation. In Conference on Empirical Meth-
  ods in Natural Language Processing (EMNLP), pages 1532–1543, 2014. doi:
  10.3115/v1/d14-1162.

John C. Platt. Probabilistic outputs for support vector machines and compar-
  isons to regularized likelihood methods. In Alexander J. Smola, Peter Bartlett,
  Bernhard Schölkopf, and Dale Schuurmans, editors, Advances in Large Margin
  Classifiers, pages 61–74. MIT Press, 1999.


                                      435
Modern Intelligent Systems                                            References


Tomaso Poggio and Federico Girosi. Networks for approximation and learning.
  Proceedings of the IEEE, 78(9):1481–1497, 1990. doi: 10.1109/5.58326.

David Poole and Alan Mackworth. Artificial Intelligence: Foundations of Com-
 putational Agents. Cambridge University Press, 2nd ed., 2017.

Ofir Press, Noah A. Smith, and Mike Lewis. Train short, test long: Attention
  with linear biases enables input length extrapolation. In Advances in Neural
  Information Processing Systems (NeurIPS), 2022.

Hubert Ramsauer, Bernhard Schäfl, Johannes Lehner, Philipp Seidl, Michael
 Widrich, Thomas Adler, Lukas Gruber, Markus Holzleitner, Milena Pavlovic,
 Michael Sandve, Viktor Deiseroth, and Sepp Hochreiter. Hopfield networks is
 all you need. International Conference on Learning Representations (ICLR),
 2021.

Robert H. Risch. The problem of integration in finite terms. Transactions of the
 American Mathematical Society, 139:167–189, 1969. doi: 10.2307/1995313.

Frank Rosenblatt. The perceptron: A probabilistic model for information storage
  and organization in the brain. Psychological Review, 65(6):386–408, 1958. doi:
  10.1037/h0042519.

David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams. Learning
 representations by back-propagating errors. Nature, 323(6088):533–536, 1986.
 doi: 10.1038/323533a0.

Stuart J. Russell and Peter Norvig. Artificial Intelligence: A Modern Approach.
  Pearson, 4th ed., 2021.

Peter J. Schreier and Louis L. Scharf. Statistical Signal Processing of Complex-
 Valued Data: The Theory of Improper and Noncircular Signals. Cambridge
  University Press, 2010.

Stanislau Semeniuta, Aliaksei Severyn, and Erhardt Barth. Recurrent dropout
  without memory loss. In International Conference on Computational Linguis-
  tics (COLING), pages 1757–1766, 2016.




                                      436
Modern Intelligent Systems                                           References


Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc V.
  Le, Geoffrey E. Hinton, and Jeff Dean. Outrageously large neural networks:
 The sparsely-gated mixture-of-experts layer. In International Conference on
 Learning Representations (ICLR), 2017.

Rainer Storn and Kenneth Price. Differential Evolution – a simple and eﬀicient
  heuristic for global optimization over continuous spaces. Journal of Global
 Optimization, 11(4):341–359, 1997. doi: 10.1023/a:1008202821328.

Jianlin Su, Yu Lu, Shengfeng Pan, Bo Wen, and Yunfeng Liu. Roformer: En-
  hanced transformer with rotary position embedding. In Annual Meeting of
  the Association for Computational Linguistics (ACL), 2021.

Tomohiro Takagi and Michio Sugeno. Fuzzy identification of systems and its
  applications to modeling and control. IEEE Transactions on Systems, Man,
  and Cybernetics, 15(1):116–132, 1985. doi: 10.1109/tsmc.1985.6313399.

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
  Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you
  need. In Advances in Neural Information Processing Systems (NeurIPS), vol-
  ume 30, 2017.

Bernard Widrow and Marcian E. Hoff. Adaptive switching circuits. In 1960 IRE
 WESCON Convention Record, volume 4, pages 96–104, 1960. doi: 10.21236/
  ad0241531.

Bernard Widrow and Samuel D. Stearns. Adaptive Signal Processing. Prentice
  Hall, 1985.

David Willshaw and C. von der Malsburg. How patterned neural connections can
 be set up by self-organization. Proceedings of the Royal Society of London.
 Series B. Biological Sciences, 194(1117):431–445, 1976. doi: 10.1098/rspb.
 1976.0087.

John Yen and Reza Langari. Fuzzy Logic: Intelligence, Control, and Information.
  Prentice Hall, 1999.

Lotfi A. Zadeh. Fuzzy sets. Information and Control, 8(3):338–353, 1965. doi:
  10.1016/S0019-9958(65)90241-X.

                                     437
Modern Intelligent Systems                                        References


Lotfi A. Zadeh. The concept of a linguistic variable and its application to
  approximate reasoning. Information Sciences, 8(3):199–249, 1975. doi:
  10.1016/0020-0255(75)90036-5.

Lotfi A. Zadeh. Fuzzy logic, neural networks, and soft computing. Communica-
  tions of the ACM, 37(3):77–84, 1994. doi: 10.1145/175247.175255.

Lotfi A. Zadeh. What is soft computing? Soft Computing, 1:1–2, 1997. No
  canonical DOI found in Crossref; keep journal metadata authoritative.

Eckart Zitzler, Marco Laumanns, and Lothar Thiele.      Spea2:   Im-
  proving the strength pareto evolutionary algorithm.  Technical Re-
  port 103, 2002. URL https://tik-old.ee.ethz.ch/db/public/tik/?db=
  publications&form=report_single_publication&publication_id=1287.




                                    438
Modern Intelligent Systems                                                       A



A Linear Systems Primer
This appendix collects basic material on signals, linear time-invariant (LTI)
systems, and state-space models. It serves as a reference for the dynamical
viewpoints used in later chapters (e.g., Hopfield networks, RNNs, and control-
oriented fuzzy systems).

Signals and Systems
A signal is a mapping from an index set (typically time or space) into a set of
values that encode a physical or abstract quantity. Formally, a continuous-time
scalar signal is a function x : R → R (or C), while a continuous-time vector
signal is x : R → Rn (or Cn ). Discrete-time signals are defined analogously on
Z. Signals may be deterministic, stochastic, scalar, or vector-valued depending
on the context.
    A system is an operator T that maps an input signal space X to an out-
put signal space Y, i.e., y = T {x}. Systems are characterized by properties
such as linearity, time-invariance, causality, and stability; determining which of
these properties hold tells us which analytical tools (Fourier analysis, state-space
models, etc.) are applicable.

Linear Time-Invariant Systems
LTI systems are a central class of models. They satisfy:
   • Linearity: For any inputs x1 (t), x2 (t) and scalars a1 , a2 ,

                    S[a1 x1 (t) + a2 x2 (t)] = a1 S[x1 (t)] + a2 S[x2 (t)].

   • Time-invariance: If the input is shifted in time by τ , the output is shifted
     by the same amount:

                                  S[x(t − τ )] = y(t − τ ),

      where y(t) = S[x(t)].




                                          439
Modern Intelligent Systems                                                     A


Impulse Response and Convolution
The behavior of an LTI system is completely characterized by its impulse re-
sponse h(t), defined as the output when the input is a Dirac delta function δ(t):

                                   h(t) = S[δ(t)].

   For any input x(t), the output y(t) is given by the convolution integral
                                             Z ∞
                    y(t) = (x ∗ h)(t) =            x(τ ) h(t − τ ) dτ.     (A.1)
                                              −∞

In discrete time the integral is replaced by a sum over integer indices.

Frequency-Domain Representation
The Fourier transform is a standard tool for analysing signals and LTI systems
in the frequency domain. For a signal x(t), the Fourier transform X(f ) is
                                       Z ∞
                             X(f ) =         x(t) e−j2πf t dt.
                                       −∞

Under suitable regularity conditions, convolution in time corresponds to multi-
plication in frequency:
                             Y (f ) = H(f )X(f ),

where H(f ) is the transform of h(t).

State-Space Models and Transfer Functions
Many dynamical systems in this book are expressed in continuous-time state-
space form:

                              dx(t)
                                    = Ax(t) + Bu(t),                       (A.2)
                               dt
                               y(t) = Cx(t) + Du(t),                       (A.3)

where x(t) ∈ Rn is the state, u(t) ∈ Rm the input, and y(t) ∈ Rp the output.




                                         440
Modern Intelligent Systems                                                        A


Homogeneous solution.          For the zero-input system, the state evolves as

                                     x(t) = eAt x(0),                          (A.4)

where eAt is the matrix exponential
                                                  ∞
                                                  X
                                         At         (At)k
                                     e        =               .                (A.5)
                                                         k!
                                                  k=0

                                     d At
Key properties include eA0 = I and dt e = AeAt = eAt A. If A is diagonaliz-
able, eAt can be computed eﬀiciently via eigen-decomposition.

Forced response. With input u(t), the solution is
                                                  Z t
                                At
                     x(t) = e        x(0) +             eA(t−τ ) Bu(τ ) dτ,    (A.6)
                                                   0

which mirrors the convolution expression for LTI systems: the kernel eA(t−τ )
plays the role of a matrix-valued impulse response.

Transfer function.       Taking the Laplace transform of (A.2) with zero initial
conditions yields

                             sX(s) = AX(s) + BU(s),                            (A.7)
                              Y(s) = CX(s) + DU(s).                            (A.8)

Solving for X(s) gives

                             X(s) = (sI − A)−1 BU(s),                          (A.9)

and substituting into the output equation produces the transfer function matrix

                             G(s) = C(sI − A)−1 B + D.                        (A.10)

This compactly describes the input–output behavior of the LTI system in the
Laplace domain.



                                                  441
Modern Intelligent Systems                                                      B


Further Reading
   • Kailath, T. (1980). Linear Systems. Prentice Hall.

   • Chen, C.-T. (1999). Linear System Theory and Design. Oxford University
     Press.

   • Ogata, K. (2010). Modern Control Engineering. Prentice Hall.


B Kernel Methods and Support Vector Machines
This appendix is a concise reference for the “kernel/SVM” thread that appears
throughout the book (hinge losses in Chapter 3, RBF feature maps in Chapter 8,
and the geometry of margins). The goal is not to be exhaustive, but to make the
notation and the relationship between explicit (finite) feature maps and implicit
(kernel) feature maps unambiguous.

Kernel trick and Gram matrices
Let ϕ : Rd → H be a (possibly high-dimensional) feature map into an inner-
product space H. A kernel is a symmetric, positive semidefinite function

                             k(x, z) ≜ hϕ(x), ϕ(z)iH .

Given training points {xi }N                              N ×N has entries K =
                              i=1 , the Gram matrix K ∈ R                   ij
k(xi , xj ); by construction, K is symmetric and positive semidefinite.

Kernel ridge regression (KRR)
Kernel ridge regression fits a function of the form

                                       X
                                       N
                             f (x) =         αi k(xi , x),
                                       i=1


where the coeﬀicient vector α ∈ RN solves

                                (K + λI)α = y.                              (B.1)

Here λ > 0 regularizes the solution and stabilizes the linear system when K
is ill-conditioned. This is the fully kernelized analogue of ridge regression in a


                                        442
Modern Intelligent Systems                                                       B


finite design matrix Φ. Chapter 8’s dual viewpoint shows that a primal RBF
network with centers at all data points (M = N ) recovers this same predictor
under an RBF kernel.

Soft-margin SVMs (primal and kernelized form)
For binary labels yi ∈ {−1, +1}, the (linear) soft-margin SVM solves (Cortes
and Vapnik, 1995)

                              1           X     N
                     min        kwk22 + C   ξi                               (B.2)
                     w,b,ξ    2
                                               i=1
                                   ⊤
                      s.t.    yi (w xi + b) ≥ 1 − ξi ,         ξi ≥ 0.       (B.3)

The parameter C > 0 trades margin size against slack violations. The decision
function is f (x) = w⊤ x + b, with classification by sign(f (x)). In the kernelized
form, w is never formed explicitly; instead,

                                       X
                                       N
                             f (x) =         αi yi k(xi , x) + b,            (B.4)
                                       i=1

where many coeﬀicients αi become zero (only support vectors remain).

How kernels relate to RBFNs (and when to use which)
   • RBFN (explicit features): choose M  N centers and widths, build
     Φ ∈ RN ×M , and solve a regularized linear system in M unknowns. This is
     eﬀicient when you can afford explicit features and want direct control over
     locality and model size.

   • Kernel method (implicit features): work directly with K ∈ RN ×N ,
     which corresponds to an implicit feature map of potentially very high di-
     mension. This is attractive for small-to-medium N when the kernel en-
     codes a useful inductive bias, but training and storage scale poorly with
     N unless approximations are used.
```

### Findings
No issues spotted.

## Chunk 31/31
- Character range: 852102–860784

```text
• Nyström / low-rank approximations: choose M landmark points and
     project into a rank-M space, recovering an explicit finite basis that con-
     nects the kernel view back to the RBFN picture in Chapter 8.


                                             443
Modern Intelligent Systems                                                        C



C     Course Logistics
This appendix consolidates administrative information that previously appeared
in scattered subsections of Chapter 1. It is intended to remain stable across offer-
ings and can be skimmed or skipped by readers focused purely on the technical
material.
If you are not taking ECE 657: you can skip this appendix entirely.

Materials
This book is self-contained. It does not rely on external companion resources
(such as code bundles, figure packs, or solution sets). When the book is used in
a course offering, offering-specific documents (syllabus, deadlines, problem sets)
are distributed through the local course channel and may change from term to
term.

Communication
Questions and feedback can be handled via email or a forum if one is announced.
Oﬀice hours, if any, will be communicated alongside the course materials.

Assessment Overview
Assignments (individual or groups up to three), examinations (if applicable), and
self-check exercises interleaved with chapters. Exact dates and policies depend
on the offering and will be communicated with the course materials.

Policies
Submission windows, late policies, and academic integrity guidelines are offering-
specific and should be consulted in the local course documentation.

C.1     Using this book in ECE 657
When this book is used in ECE 657 at the University of Waterloo, the following
apply:
    • Communication/support: Course announcements (including clarifica-
      tions and errata relevant to an offering) are distributed through the course
      channel; an oﬀicial forum or mailing list may be announced for Q&A. Of-
      fice hours (if any) are posted with the term schedule.

                                       444
Modern Intelligent Systems                                                      D


    • Assessment structure: Problem sets (solo or teams of up to three),
      quizzes, and two term exams are typical. Weighting and deadlines are
      confirmed in the term syllabus; use the most recent syllabus if numbers
      differ from prior offerings.

    • Pacing: Condensed offerings do not include a formal reading week; exam
      weeks typically suppress new material. Follow the posted weekly schedule
      in the syllabus.

    • Accessibility: Students requiring accommodations should contact Access-
      Ability Services and notify the instructor early so quiz/exam windows and
      deadlines can be adjusted. Captions and alternative formats are provided
      on request when videos accompany the course materials.

    • Integrity: Follow the University of Waterloo Academic Integrity policy.
      Credit collaborators appropriately and avoid sharing solutions outside ap-
      proved groups.


D     Notation collision index
This appendix lists the most common notation collisions in this book: symbols
that appear in multiple domains (probability, optimization, deep learning) with
different meanings. The goal is not to eliminate reuse—that is unrealistic—but
to make the disambiguation rule explicit so reading remains fast and consistent.
 Disambiguation rule (used throughout the book)
     • Function argument wins: σ(x) is the sigmoid; f (·) is an
       activation; p(·) is a density/pmf.

     • Plain scalars default to the local domain: σ without an
       argument is a width/scale unless the paragraph is explicitly about
       the sigmoid.

     • Typography is a hint, not a guarantee: bold symbols are
       vectors/matrices; subscripts usually indicate time, layer, or an index
       set.




                                      445
Modern Intelligent Systems                                                                      E


 Symbol      Common meanings                     Where to look / how to
                                                 disambiguate
 σ           Sigmoid nonlinearity;               σ(x) is always sigmoid; plain σ is a
             standard deviation / scale;         width/scale (e.g., RBFNs) unless the
             RBF width                           section is explicitly about activations.
 λ           Regularization strength;            Regularization uses λ alongside an
             eigenvalue; Lagrange                objective; spectral topics use λ with
             multiplier                          matrices/operators; constraints use λ
                                                 as a multiplier.
 p          Probability / density; padding p(y | x) is probability; convolution
            (CNNs); momentum/              padding is stated as p in the
            parameter name in code         output-size formula with n, k, s.
 L           Number of layers; sequence          Layer count uses L with indices
             length; loss                        l = 1, . . . , L; loss is L; sequence length
                                                 is usually T .
 t           Time index; target                  Time is t with sequences xt , ht ; targets
             vector/component                    use t (bold) or tk in loss definitions.
 h           Hypothesis function hθ ;       Hypotheses appear as hθ (·) in
             hidden state ht / hidden units supervised chapters; hidden state uses
             h                              a time index ht ; hidden width uses a
                                            dimension symbol (e.g., h or dh ) in
                                            network-shape context.

Reading note. When a symbol is reused with a different meaning, chapters
typically flag the local meaning near the first use. When reading out of order,
use this index to disambiguate quickly and keep the local convention consistent.


E    Reproducibility and Reporting Standards
This appendix defines the minimum reporting standard used throughout this
book when experiments include stochastic training, model selection, or con-
strained optimization. The objective is simple: results should be auditable and
repeatable by another reader with the same code and data access.




                                           446
Modern Intelligent Systems                                                  E


 Core reporting template (required fields)
    • Data protocol: split policy, leakage controls, and
      preprocessing/tokenization version.

    • Model protocol: architecture configuration, parameter count,
      initialization policy, and regularization settings.

    • Optimization protocol: optimizer, schedule, batch size, stopping
      rule, and checkpoint selection criterion.

    • Evaluation protocol: primary metric, calibration/slice checks, and
      whether thresholds were tuned on validation only.

    • Variance protocol: random seeds, number of runs, and summary
      statistics (median/mean plus spread).


Minimum acceptable evidence
  • Report at least 5 seeds for low-cost experiments and 10+ seeds when claims
    depend on small metric differences.

  • Show both central tendency and spread (e.g., median + interquartile range,
    or mean + standard deviation).

  • Match evaluation budgets when comparing methods (same number of
    epochs/fitness calls and same stopping policy).

  • Preserve a machine-readable experiment log (configuration + metrics +
    seed) for each run.

Common failure modes to avoid
  • Best-run reporting: publishing only the strongest seed and omitting
    dispersion.

  • Budget mismatch: giving one method more training/evaluation budget
    than another.

  • Selection leakage: tuning hyperparameters on test data (explicitly or
    implicitly).



                                    447
Modern Intelligent Systems                                                E


  • Unversioned preprocessing: changing tokenization or normalization
    without recording the revision.

Chapter-specific notes
  • Supervised/Logistic chapters: pair accuracy-like metrics with calibra-
    tion and slice checks.

  • Deep-learning chapters: track gradient health, early stopping criteria,
    and checkpoint restore policy.

  • Evolutionary chapter: report evaluation-budget-normalized perfor-
    mance and multi-seed front dispersion.

Practical rule. If a claim changes a design decision, it must include enough
protocol detail for a third party to reproduce the comparison.




                                    448
```

### Findings
No issues spotted.
