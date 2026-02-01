# Scientific QA Report

- Source PDF: `notes_output/ece657_notes.pdf`
- Total chunks: 5

## Chunk 1/110
- Character range: 0–4353

```text
Intelligent Systems and Soft Computing: A Graduate Companion
             From Neural Networks to Fuzzy Logic and Evolutionary Computing

                           Dr. Haitham Amar, University of Waterloo

                                         November 13, 2025



About This Book
These notes have evolved into a concise graduate companion that blends the original chapter voice
of ECE 657 with laboratory-style checklists and reflective prompts. The chapters move from su-
pervised learning foundations to fuzzy logic and evolutionary computing, mirroring the trajectory
of the course while adding connective tissue so that a reader can revisit the material years later
without hunting for missing context.
    Each chapter (originally a lecture) has been edited with four recurring questions in mind:
  • What is the core scientific idea and how does it relate to earlier material?

  • Which methodological cautions should a practitioner keep close at hand?

  • How do the accompanying figures or derivations anchor those ideas visually?

  • Where does the topic sit within the broader landscape of intelligent systems?
The result is a self-contained reference for researchers and engineers who want a rigorous but
narrative-friendly treatment of neural networks, soft computing, and hybrid reasoning systems.


Contents

About This Book                                                                                        1

Notation and Glossary                                                                                  16

1 About This Companion                                                                                 17
  1.1 How to Use These Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       17
  1.2 Logistics and Policies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   17
  1.3 Roadmap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      17
  1.4 Learning Outcomes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      17
  1.5 Introduction to Course Content . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       18
  1.6 Course Scope and Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       19
  1.7 Prerequisites and Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       19
  1.8 Relation to Other AI and Machine Learning Courses . . . . . . . . . . . . . . . . . .            19

                                                   1
Intelligent Systems Companion                                                                  Contents


   1.9 Recommended Textbooks and Resources . . . . . . . . . . . . . . . . . . . . . . . . .           20
   1.10 Course Tools and Software . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    20
   1.11 Defining Artificial Intelligence and Intelligent Systems . . . . . . . . . . . . . . . . .     21
   1.12 Problem Definition and Representation in AI . . . . . . . . . . . . . . . . . . . . . .        22
   1.13 Components of AI Systems: Thinking, Perception, and Action . . . . . . . . . . . . .           23
   1.14 Case Study: AI-Enabled Camera as an Intelligent System . . . . . . . . . . . . . . .           23
   1.15 Historical Foundations of Intelligent Systems (Continued) . . . . . . . . . . . . . . .        24
   1.16 Defining Intelligent Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   25
   1.17 Levels of Intelligence in Machines . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   28
   1.18 Defining Intelligent Machines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    29
   1.19 Examples of Intelligent Machines . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     30
   1.20 Intelligent Systems vs. Intelligent Machines . . . . . . . . . . . . . . . . . . . . . . .     30
   1.21 Levels of Intelligence and Defining AI . . . . . . . . . . . . . . . . . . . . . . . . . .     31
   1.22 Role of Emotions in Intelligent Systems . . . . . . . . . . . . . . . . . . . . . . . . .      31
   1.23 Are Business Intelligence Tools Intelligent? . . . . . . . . . . . . . . . . . . . . . . .     32
   1.24 What Constitutes an Intelligent System? . . . . . . . . . . . . . . . . . . . . . . . . .      32
```

### Findings
- No issues spotted.

## Chunk 2/110
- Character range: 4356–7061

```text
2 Supervised Learning Foundations                                                                      36
  2.1 Problem Setup and Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         36
  2.2 Empirical Risk Minimization and Regularization . . . . . . . . . . . . . . . . . . . .           36
  2.3 Common Loss Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        36
  2.4 Model Selection, Splits, and Learning Curves . . . . . . . . . . . . . . . . . . . . . .         36
  2.5 Probabilistic Interpretation: Bayes, MLE, and MAP . . . . . . . . . . . . . . . . . .            37
  2.6 Confusion Matrices and Derived Metrics . . . . . . . . . . . . . . . . . . . . . . . . .         38
  2.7 Synthetic Data and Optimization Geometry . . . . . . . . . . . . . . . . . . . . . . .           38
  2.8 Intelligent Machines and Automation . . . . . . . . . . . . . . . . . . . . . . . . . . .        40
  2.9 Problem Solving and Intelligence . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       42
  2.10 Utility Functions and Objectives . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      43
  2.11 Summary of Intelligent System Characteristics . . . . . . . . . . . . . . . . . . . . .         44
  2.12 Intelligence and Problem Solving in Machines . . . . . . . . . . . . . . . . . . . . . .        44
  2.13 Closure of Derivations from Chapter 1 . . . . . . . . . . . . . . . . . . . . . . . . . .       46

3 Chapter 2 Part I: Problem Solving Strategies in Symbolic Integration                                 48
  3.1 Context and Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       49
  3.2 Problem Decomposition and Transformation . . . . . . . . . . . . . . . . . . . . . . .           49
  3.3 Limitations of Safe Transformations . . . . . . . . . . . . . . . . . . . . . . . . . . .        50
  3.4 Heuristic Transformations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      50
  3.5 Summary of the Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        51
  3.6 Heuristic Transformations: Revisiting the Integral with 1 − x2 . . . . . . . . . . . . .         51
  3.7 Example: Solving an Integral via Transformation Trees . . . . . . . . . . . . . . . . .          54
  3.8 Transformation Trees and Search Strategies . . . . . . . . . . . . . . . . . . . . . . .         54
  3.9 Algorithmic Outline for Symbolic Problem Solving . . . . . . . . . . . . . . . . . . .           55


                                                   2
Intelligent Systems Companion                                                                    Contents
```

### Findings
- This chunk appears to be a table of contents for sections 2 and 3 of the lecture notes.
- As such, it does not contain scientific or mathematical statements, definitions, or derivations to analyze for correctness or rigor.
- No ambiguous claims, inconsistent notation, or logical gaps are present in this outline format.
- No missing definitions or places needing more justification can be identified from a table of contents alone.

**No issues spotted.**

## Chunk 3/110
- Character range: 7063–10516

```text
3.10 Discussion: Is Such a System Intelligent? . . . . . . . . . . . . . . . . . . . . . . . .        55
   3.11 Artificial Intelligence, Machine Learning, and Deep Learning . . . . . . . . . . . . . .         56
   3.12 Predictive Modeling: Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        56
   3.13 Regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   57
   3.14 Classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   57
   3.15 Data Modeling and Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         58
   3.16 Regression and Classification: A Recap . . . . . . . . . . . . . . . . . . . . . . . . . .       59
   3.17 Linear Regression: The Canonical Regression Model . . . . . . . . . . . . . . . . . .            59
   3.18 Deterministic vs. Statistical Relationships . . . . . . . . . . . . . . . . . . . . . . . .      60
   3.19 Assessing the Existence of a Relationship: Covariance and Correlation . . . . . . . .            61
   3.20 Examples of Correlation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      61
   3.21 Limitations of Correlation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     61
   3.22 Linear Regression Model and Error Minimization . . . . . . . . . . . . . . . . . . . .           62
   3.23 Learning Curves and Bias–Variance Intuition . . . . . . . . . . . . . . . . . . . . . .          62
   3.24 Maximum Likelihood Estimation (MLE) Interpretation . . . . . . . . . . . . . . . .               63
   3.25 Justification for Gaussian Assumption in Regression . . . . . . . . . . . . . . . . . .          64
   3.26 Maximum Likelihood Estimation (MLE) . . . . . . . . . . . . . . . . . . . . . . . . .            64
   3.27 MLE for Linear Regression with Gaussian Noise . . . . . . . . . . . . . . . . . . . .            65
   3.28 Closed-Form Solution for Simple Linear Regression . . . . . . . . . . . . . . . . . . .          65
   3.29 Closure of Parameter Estimation Derivations . . . . . . . . . . . . . . . . . . . . . .          66
   3.30 Transition to Classification Models . . . . . . . . . . . . . . . . . . . . . . . . . . . .      67

4 Classification and Logistic Regression                                                                 68
  4.1 From Regression to Classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        68
  4.2 Bayes Optimal Classifier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       69
  4.3 Logistic Regression: A Probabilistic Discriminative Model . . . . . . . . . . . . . . .            69
  4.4 Decision Rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      71
  4.5 Modeling the Conditional Probability . . . . . . . . . . . . . . . . . . . . . . . . . .           71
  4.6 Maximum Likelihood Estimation (MLE) for Logistic Regression . . . . . . . . . . . .                71
  4.7 Softmax (Multiclass) Logistic Regression . . . . . . . . . . . . . . . . . . . . . . . . .         72
  4.8 Interpretation of the Likelihood . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       72
  4.9 Completion of the Maximum Likelihood Estimation for Logistic Regression . . . . .                  72
  4.10 Evaluation Metrics: ROC and Precision–Recall Curves . . . . . . . . . . . . . . . . .             73
```

### Findings
- This chunk appears to be a table of contents for sections 3 and 4 of the lecture notes, listing topics and page numbers.
- No scientific or mathematical statements are present in this chunk, so there are no claims, definitions, or notations to evaluate.
- No issues spotted.

## Chunk 4/110
- Character range: 10522–13081

```text
5 Introduction to Neural Networks                                                                        75
  5.1 Biological Inspiration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     75
  5.2 From Biological to Artificial Neural Networks . . . . . . . . . . . . . . . . . . . . . .          76
  5.3 Outline of Neural Network Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          76
  5.4 Neural Network Architectures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         77
  5.5 Activation Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       78
  5.6 Learning Paradigms in Neural Networks . . . . . . . . . . . . . . . . . . . . . . . . .            79
  5.7 Fundamentals of Artificial Neural Networks . . . . . . . . . . . . . . . . . . . . . . .           80


                                                    3
Intelligent Systems Companion                                                                 Contents


   5.8 Mathematical Formulation of the Neuron Output . . . . . . . . . . . . . . . . . . . . 82
   5.9 Wrapping up the McCulloch-Pitts Neuron Model . . . . . . . . . . . . . . . . . . . . 82
   5.10 From MP Neuron to Perceptron and Beyond . . . . . . . . . . . . . . . . . . . . . . 83

6 Multi-Layer Perceptrons: Challenges and Foundations                                                85
  6.1 Limitations of the Single-Layer Perceptron . . . . . . . . . . . . . . . . . . . . . . . .     85
  6.2 Biological Inspiration and the Need for Multiple Neurons . . . . . . . . . . . . . . .         85
  6.3 Challenges in Extending Perceptrons to Multi-Layer Architectures . . . . . . . . . .           86
  6.4 From Perceptron to Differentiable Activation Functions . . . . . . . . . . . . . . . .         87
  6.5 Performance Measure and Loss Function . . . . . . . . . . . . . . . . . . . . . . . . .        88
  6.6 Extending to Multi-Layer Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . .      88
  6.7 Gradient Descent and Backpropagation . . . . . . . . . . . . . . . . . . . . . . . . .         89
  6.8 Completing the Derivative Calculations . . . . . . . . . . . . . . . . . . . . . . . . .       90
  6.9 Single-Neuron Gradient Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       91
  6.10 Extension to Multi-Layer Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . .     92
  6.11 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   92
```

### Findings
- This chunk appears to be a table of contents for sections 5 and 6 of the lecture notes, rather than substantive content.
- No scientific or mathematical statements are present to analyze for correctness.
- No definitions, claims, or notation are present to check for ambiguity or inconsistency.

No issues spotted.

## Chunk 5/110
- Character range: 13083–17023

```text
7 Backpropagation Learning in Multi-Layer Perceptrons                                              93
  7.1 Context and Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
  7.2 Problem Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
  7.3 Error and Objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
  7.4 Challenges in Weight Updates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
  7.5 Notation for Layers and Neurons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
  7.6 Forward Pass Recap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
  7.7 Backpropagation: Recursive Computation of Error Terms . . . . . . . . . . . . . . . 95
  7.8 Backpropagation Algorithm: Detailed Derivation . . . . . . . . . . . . . . . . . . . . 97
  7.9 Backpropagation for Hidden Layers . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
  7.10 Batch and Stochastic Gradient Descent . . . . . . . . . . . . . . . . . . . . . . . . . 98
  7.11 Backpropagation Algorithm: Detailed Numerical Example . . . . . . . . . . . . . . . 99
  7.12 Training Procedure and Epochs in Multi-Layer Perceptrons . . . . . . . . . . . . . . 101
  7.13 Role and Design of Hidden Layers . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
  7.14 Case Study: Learning the Function y = x sin x . . . . . . . . . . . . . . . . . . . . . 102
  7.15 Applications of Multi-Layer Perceptrons . . . . . . . . . . . . . . . . . . . . . . . . . 103
  7.16 Limitations of Multi-Layer Perceptrons . . . . . . . . . . . . . . . . . . . . . . . . . . 103
  7.17 Conclusion of Multi-Layer Perceptron Derivations . . . . . . . . . . . . . . . . . . . . 104
  7.18 Preview: Radial Basis Function Networks . . . . . . . . . . . . . . . . . . . . . . . . 105

8 Radial Basis Function Networks (RBFNs)                                                          106
  8.1 Overview and Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
  8.2 Architecture of RBFNs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
  8.3 Radial Basis Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
  8.4 Key Properties and Advantages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108


                                                  4
Intelligent Systems Companion                                                                Contents


   8.5 Transforming Nonlinearly Separable Data into Linearly Separable Space . . . . . . . 108
   8.6 Finding the Optimal Weight Vector w . . . . . . . . . . . . . . . . . . . . . . . . . . 108
   8.7 Closed-Form Solution for the Weight Vector w . . . . . . . . . . . . . . . . . . . . . 109
   8.8 The Role of the Transformation Function g(·) . . . . . . . . . . . . . . . . . . . . . . 110
   8.9 Examples of Kernel Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
   8.10 Interpretation of the Width Parameter σ . . . . . . . . . . . . . . . . . . . . . . . . . 110
   8.11 Effect of σ on Classification Boundaries . . . . . . . . . . . . . . . . . . . . . . . . . 111
   8.12 Radial Basis Function Networks: Parameter Estimation and Training . . . . . . . . . 111
   8.13 Remarks on Radial Basis Function Networks . . . . . . . . . . . . . . . . . . . . . . 113
   8.14 Wrapping up the Derivation of the Wiener Filter . . . . . . . . . . . . . . . . . . . . 113
   8.15 Interpretation and Properties of the Wiener Filter . . . . . . . . . . . . . . . . . . . 114
   8.16 Extension: Frequency-Domain Wiener Filter . . . . . . . . . . . . . . . . . . . . . . . 114
   8.17 Closing Remarks on Adaptive Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . 114
   8.18 Preview: Unsupervised and Localized Learning . . . . . . . . . . . . . . . . . . . . . 114
```

### Findings
- This chunk is a table of contents for sections 7 and 8, not actual lecture content. As such, it does not contain scientific or mathematical statements to analyze for correctness.
- No definitions, claims, or notation are present to check for ambiguity, inconsistency, or logical gaps.
- No issues spotted.
