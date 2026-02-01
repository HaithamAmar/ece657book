# Scientific QA Report

- Source PDF: `notes_output/ece657_notes.pdf`
- Total chunks: 5

## Chunk 60/95
- Character range: 390916–398708

```text
11.29    Nonlinear Activation Functions in Convolutional Neural Networks
Recall from previous lectures that neural networks apply nonlinear activation functions after linear
transformations to introduce nonlinearity, enabling the network to approximate complex functions.
In convolutional neural networks (CNNs), this principle remains the same.
    Given an input feature map x, a convolutional layer computes a linear combination of inputs
with learned filters W and biases b:
                                          z = W ∗ x + b,                                       (199)
where ∗ denotes the convolution operation.




                                                  148
Figure 34: Illustration of pooling: each 2 × 2 neighborhood is summarized either by its maximum
or average, shrinking the resolution while preserving salient activations.


    The output of this convolution is then passed through a nonlinear activation function σ(·), such
as the sigmoid, hyperbolic tangent, or ReLU (Rectified Linear Unit):

                                                y = σ(z).                                           (200)

     For example, if zij is the pre-activation value at spatial location (i, j), then the activated output
is
                                               yij = σ(zij ).                                       (201)
   This nonlinear step is crucial because it allows the network to learn complex hierarchical features
beyond linear combinations.

11.30     Pooling Layers: Motivation and Operation
After convolution and nonlinear activation, CNNs often include pooling layers to reduce spatial
dimensions and aggregate information. Pooling layers perform a form of downsampling by summa-
rizing local neighborhoods in the feature maps.

Pooling operation: Given an input feature map y of size H × W , a pooling layer applies a
sliding window (filter) of size k × k with stride s over the spatial dimensions. For each window, an
aggregation function A is applied to the values inside the window:
                                                                                 
                    pm,n = A {yi,j | i ∈ [ms, ms + k − 1], j ∈ [ns, ns + k − 1]} ,             (202)

where pm,n is the pooled output at location (m, n).
   Common aggregation functions include:

     • Max pooling: A = max

     • Average pooling: A = mean

     • Min pooling: A = min




                                                    149
Output dimensions The pooled feature map sizes are
                                                       
                           H −k                      W −k
                  Hout =           + 1,     Wout =          + 1,                               (203)
                             s                         s

where b·c denotes the floor operation. These expressions account for stride and the fact that the
pooling window must lie entirely within the input feature map.

Example: Consider a 4 × 4 feature map and a 3 × 3 max pooling filter with stride 1. The output
size is computed as                       
                                      4−3
                                             + 1 = 2,                                    (204)
                                       1
so the pooled feature map is 2 × 2. Each pooled value corresponds to the maximum value in the
3 × 3 window sliding over the input.

11.31    Pooling Layers: Biological and Theoretical Considerations
Pooling layers are often described as non-learnable layers because they do not contain parameters
updated during training. Unlike convolutional filters, pooling operations are fixed functions chosen
a priori.

Why is pooling not a ”layer” in the strict neural network sense? A typical neural
network layer involves learnable parameters that adapt to minimize a loss function. Pooling layers
perform deterministic aggregation without parameter updates. Thus, they do not contribute to the
network’s capacity to learn representations in the classical sense.

Biological analogy: Artificial neural networks are loosely inspired by biological neurons, which
integrate inputs and fire based on excitation thresholds. Pooling does not correspond directly to
any known biological neuron operation because it does not involve excitatory or inhibitory firing
or synaptic weight adaptation. Instead, pooling acts as a form of dimensionality reduction or
subsampling.

Empirical effectiveness: Despite the lack of a clear biological or theoretical justification, pooling
layers significantly improve CNN performance in practice. Max pooling, in particular, tends to
preserve the strongest activation signals, which may correspond to the most salient features in the
input.

Why does max pooling work better than average pooling? One hypothesis is that max
pooling retains the most prominent features by selecting the maximum activation within a local
neighborhood, effectively filtering out noise and weaker signals. Average pooling, by contrast,
smooths activations and may dilute important features.

Pooling vs. other dimensionality reduction methods: Replacing pooling with other di-
mensionality reduction techniques such as Principal Component Analysis (PCA) or learned down-
sampling often results in worse performance. This suggests that pooling captures some inductive
bias beneficial for hierarchical feature learning in CNNs, though the precise reasons remain an open
research question.


                                                150
Figure 35: Effective receptive field growth as convolutional and pooling layers stack. Each stage
covers a larger portion of the input despite using only 3 × 3 kernels.


11.32    Summary of the Convolution-Pooling Pipeline
A typical CNN block consists of the following sequence:

  1. Convolution: Apply learned filters to extract local features.

  2. Nonlinear activation: Apply a nonlinear function (e.g., ReLU) to introduce nonlinearity.

  3. Pooling: Downsample the feature maps by aggregating local neighborhoods.

    This pipeline is repeated multiple times, gradually transforming the input image into increas-
ingly abstract and spatially compressed feature representations. After several convolution-pooling
blocks, the network has accumulated a rich set of high-level descriptors that can feed downstream
classification heads.

11.33    Flattening and Classification in CNNs
After the convolutional and pooling layers extract features from the input image, the resulting multi-
dimensional tensor must be transformed into a format suitable for classification. This process is
called flattening, where the tensor is reshaped into a one-dimensional vector.
    For example, consider a feature map of size 4 × 4 × 40. Flattening this tensor yields a vector of
length:
                                          4 × 4 × 40 = 640.
This vector can then be fed into a fully connected (shallow) neural network or other classifiers
such as support vector machines (SVMs) or logistic regression models. The goal is to leverage the
extracted features for accurate classification.




                                                 151
Backpropagation through CNNs Backpropagation in CNNs updates the weights of convolu-
tional filters and fully connected layers by propagating the error gradients backward through the
network. Although the network may appear complex due to three-dimensional feature maps and
multiple layers, the underlying principle remains the same as in standard neural networks: compute
gradients with respect to weights and update them using gradient descent or its variants.
    The flattening operation is a logical reshaping and does not affect the gradient flow; gradients
are simply propagated through the reshaped vector back to the convolutional layers.
```

### Findings
- Equation (203) for output dimensions of pooling layers uses notation "b·c" to denote the floor operation, but the formula as written:
  
  \[
  H_{out} = \left\lfloor \frac{H - k}{s} \right\rfloor + 1, \quad W_{out} = \left\lfloor \frac{W - k}{s} \right\rfloor + 1
  \]
  
  is correct, but the text says "b·c denotes the floor operation" without explicitly showing the floor symbols in the formula. It would be clearer to explicitly include floor brackets in the formula to avoid ambiguity.

- In the example following equation (204), the calculation is:

  \[
  \frac{4 - 3}{1} + 1 = 2
  \]

  which is correct. However, the text should clarify that this assumes no padding and that the pooling window fits entirely inside the input.

- The statement "Pooling layers are often described as non-learnable layers because they do not contain parameters updated during training" is accurate, but it might be worth noting that some modern variants (e.g., learned pooling or strided convolutions) do introduce learnable downsampling.

- The claim "Pooling does not correspond directly to any known biological neuron operation" is broadly true but could be nuanced: biological neurons do perform forms of spatial integration and nonlinearities that can be loosely analogous to pooling.

- The explanation of why max pooling works better than average pooling is presented as a hypothesis, which is appropriate. However, it might be helpful to mention that this is still an active area of research and that the effectiveness can depend on the task and architecture.

- The comparison of pooling to PCA or learned downsampling methods is stated as "often results in worse performance," which is generally true but could be qualified. Some learned downsampling methods (e.g., strided convolutions or attention-based pooling) can outperform traditional pooling in certain contexts.

- The description of flattening and feeding into fully connected layers or other classifiers is correct. It might be useful to mention that flattening can lead to a large number of parameters, motivating the use of global average pooling or other dimensionality reduction techniques in modern architectures.

- The note that flattening does not affect gradient flow is correct and important.

- Minor typographical issue: In equation (199), the convolution operation is denoted by "∗" which is standard, but it might be helpful to clarify whether this is cross-correlation or convolution, as in many deep learning frameworks the operation called "convolution" is actually cross-correlation.

- The notation in equation (202) uses set notation with indices i ∈ [ms, ms + k − 1], j ∈ [ns, ns + k − 1]. It would be clearer to specify that these are integer indices and that the intervals are inclusive.

- The text uses both "feature map" and "tensor" somewhat interchangeably; it might be helpful to clarify that feature maps are multi-dimensional tensors with spatial and channel dimensions.

- The term "shallow neural network" in section 11.33 might be ambiguous; it would be clearer to say "fully connected layers" or "dense layers," as "shallow" could be interpreted differently.

- The explanation of backpropagation through CNNs is concise and accurate, but it could mention that the convolution operation's weight sharing and local connectivity are key differences from fully connected layers.

No major scientific or mathematical errors were found.

## Chunk 61/95
- Character range: 398710–405665

```text
11.34    Historical Perspective on CNNs
The development of convolutional neural networks has a rich history:

  • 1950s–1960s: Early inspirations for neural networks and pattern recognition.

  • 1980: Fukushima introduced the Neocognitron, a precursor to modern CNNs.

  • 1998: LeCun et al. developed LeNet, applying CNNs to digit recognition with moderate
    success.

  • 2012: Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton published a landmark paper
    demonstrating an 8-layer CNN (AlexNet) that significantly outperformed previous methods
    on the ImageNet classification challenge.

  • Post-2012: Deeper networks with hundreds or thousands of layers (e.g., VGG, ResNet) have
    been developed, pushing the state-of-the-art in image recognition and other domains.

    AlexNet introduced several key innovations, such as using ReLU activations, dropout for regu-
larization, and GPU acceleration, which contributed to its success.

11.35    Key Hyperparameters in CNN Design
Designing an effective CNN requires careful selection of several hyperparameters:

  • Filter size: The spatial dimensions of convolutional kernels (e.g., 3 × 3, 5 × 5).

  • Stride: The step size with which the filter moves across the input.

  • Padding: Whether to add zeros around the input to control the spatial size of the output.

  • Pooling type and size: Max pooling, average pooling, and their window sizes and strides.

  • Number of filters: The depth of the output feature maps.

   These parameters are typically chosen based on empirical results, domain knowledge, and com-
putational constraints. For example, AlexNet used a stride of 4 in its first convolutional layer,
which was a design choice balancing computational eﬀiciency and feature extraction quality.

11.36    Regularization and Optimization Heuristics
Modern CNNs lean heavily on regularization layers and adaptive optimizers to reach peak accuracy.




                                                152
Figure 36: Dropout randomly zeroes activations (left) and yields flatter validation curves compared
with the no-dropout baseline (right).




Figure 37: Batch normalization rescales activations so that each channel maintains zero mean and
unit variance before the learned aﬀine re-scaling.


Dropout. In convolutional stacks, dropout is typically applied after fully connected layers or
between residual blocks to decorrelate activations. Figure 36 visualizes the binary mask applied
during training and the characteristic training/validation curves: without dropout, the validation
error quickly diverges even though the training error keeps decreasing.

Batch normalization. BN accelerates convergence by normalizing mini-batch statistics and
learning scale/shift parameters. Figure 37 contrasts the pre- and post-normalization activation dis-
tributions; whitening the distribution keeps gradients in a well-behaved range and reduces covariate
shift.

Adaptive optimizers. While vanilla SGD remains a workhorse, Adam and related methods
adapt learning rates per-parameter. Figure 38 summarizes the typical loss trajectories; Adam
converges faster initially, whereas SGD+momentum often attains a slightly lower asymptote after
fine-tuning.

Summary
In this lecture, we concluded our discussion on convolutional neural networks by:


                                                153
Figure 38: Representative training curves for SGD with momentum versus Adam on the same
CNN.

  • Explaining the flattening operation that converts multi-dimensional feature maps into vectors
    for classification.

  • Reviewing backpropagation through CNNs and clarifying that the three-dimensional structure
    is a logical representation of connections.

  • Providing a historical overview of CNN development from early models to modern deep
    architectures.

  • Highlighting the importance of hyperparameter selection in CNN design and training.

    CNNs remain the state-of-the-art approach for image recognition and have been successfully
extended to speech, text, and other domains. In the next lecture, we will explore other neural
network architectures including autoencoders and recurrent neural networks, and their applications
in natural language processing.

References
  • LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998). Gradient-based learning applied to
    document recognition. Proceedings of the IEEE, 86(11), 2278-2324.

  • Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep
    convolutional neural networks. Advances in Neural Information Processing Systems, 25, 1097-
    1105.

  • Fukushima, K. (1980). Neocognitron: A self-organizing neural network model for a mech-
    anism of pattern recognition unaffected by shift in position. Biological Cybernetics, 36(4),
    193-202.

  • Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press. http:
    //www.deeplearningbook.org

                                               154
12 Introduction to Recurrent Neural Networks
In previous lectures, we have extensively studied feedforward neural networks (FNNs), including
multilayer perceptrons (MLPs), radial basis function (RBF) networks, and convolutional neural
networks (CNNs). These architectures have proven effective for a wide range of tasks such as
classification, regression, and feature extraction. However, they share a common characteristic: the
flow of information is strictly unidirectional, from input to output, without any form of internal
memory or feedback.
    Today, we begin our exploration of recurrent neural networks (RNNs), a fundamentally different
class of neural networks designed to handle sequential data and temporal dependencies. Unlike
feedforward networks, RNNs incorporate cycles in their computational graph, enabling them to
maintain a state that evolves over time and captures information about previous inputs.

12.1    Motivation for Recurrent Neural Networks
Before delving into the architecture and mathematics of RNNs, it is important to understand why
feedforward networks are insuﬀicient for certain applications. Consider the following scenario:
       You want to predict an output at time t based not only on the input at time t, but also
       on inputs from previous time steps t − 1, t − 2, . . . , t − k.
   This is a common situation in many real-world problems, such as:
  • Time series forecasting (e.g., stock prices, weather data)
  • Natural language processing (e.g., predicting the next word in a sentence)
  • Speech recognition and synthesis
  • Control systems with memory of past states
    Feedforward networks treat each input independently and do not have an inherent mechanism
to remember or utilize past inputs. To incorporate past information, one might consider explicitly
including previous inputs as part of the current input vector, but this approach quickly becomes
impractical as the history length grows.
```

### Findings
- The historical timeline and key milestones in CNN development are accurately presented, including the Neocognitron (1980), LeNet (1998), and AlexNet (2012). The mention of post-2012 deeper networks like VGG and ResNet is appropriate.

- The description of AlexNet’s innovations (ReLU, dropout, GPU acceleration) is correct and well-justified.

- The key hyperparameters listed for CNN design (filter size, stride, padding, pooling, number of filters) are standard and clearly explained. The example of AlexNet’s stride of 4 in the first layer is accurate.

- The explanation of dropout application in CNNs is reasonable, noting its typical use after fully connected layers or between residual blocks. The description of dropout’s effect on validation curves is consistent with known behavior.

- The batch normalization description correctly states that it normalizes activations to zero mean and unit variance per channel, with learned affine parameters. The claim that it reduces covariate shift and stabilizes gradients is standard, though the term “whitening” is somewhat loosely used here since BN normalizes but does not perform full whitening (decorrelation).

- The discussion of adaptive optimizers (Adam vs. SGD+momentum) is accurate and reflects common empirical observations.

- The summary points are consistent with the lecture content and correctly highlight the covered topics.

- The transition to RNNs is well-motivated, emphasizing the need for memory and temporal dependencies that feedforward networks lack.

- The examples given for sequential data tasks are appropriate and relevant.

- Minor points for improvement or clarification:
  - The term “whitening” in the batch normalization section could be clarified or replaced with “normalization” since BN normalizes mean and variance but does not decorrelate features.
  - The statement “dropout is typically applied after fully connected layers or between residual blocks” could mention that dropout is less commonly applied within convolutional layers themselves, which is a subtlety worth noting.
  - The phrase “validation error quickly diverges” without dropout might be better phrased as “validation error increases or overfits” since “diverges” can be ambiguous.
  - The explanation that the three-dimensional structure in CNNs is a “logical representation of connections” could be expanded or clarified for readers unfamiliar with tensor dimensions in CNNs.

No major scientific or mathematical errors detected. Overall, the content is accurate, well-structured, and appropriately referenced.

## Chunk 62/95
- Character range: 405667–413185

```text
12.2    Key Idea: State and Memory in RNNs
Recurrent neural networks address this limitation by introducing a state vector ht that summarizes
information from all previous inputs up to time t. The state is updated recursively as new inputs
arrive, allowing the network to maintain a form of memory.
    Formally, at each time step t, the RNN receives an input vector xt and updates its hidden state
ht according to a function f parameterized by weights θ:


                                         ht = f (ht−1 , xt ; θ)                                  (205)
   The output yt at time t is then computed as a function of the current state:


                                            yt = g(ht ; θ′ )                                     (206)
    Here, f and g are typically nonlinear functions implemented by neural network layers, and θ, θ′
are learned parameters.

                                                 155
Interpretation: The hidden state ht acts as a summary or encoding of the entire input history
{x1 , x2 , . . . , xt }. This allows the network to make predictions that depend on the temporal context,
not just the current input.

12.3    Comparison with Feedforward Networks
To contrast, a feedforward network computes the output at time t as:


                                             yt = ϕ(xt ; θ)                                        (207)

    where ϕ is a nonlinear function without any dependence on past inputs. This limits the ability of
feedforward networks to model temporal dependencies unless the input vector xt explicitly contains
past information.

Summary: RNNs extend feedforward networks by incorporating a recurrent connection that
allows information to persist across time steps, enabling modeling of sequences and temporal dy-
namics.

12.4    Outline of Lecture 7
In this lecture, we will:

   • Formally define the architecture of recurrent neural networks.

   • Derive the forward and backward passes for training RNNs.

   • Discuss challenges such as vanishing and exploding gradients.

   • Introduce variants of RNNs designed to mitigate these challenges.

   • Explore applications where RNNs provide significant advantages over feedforward networks.

    Before proceeding, we will briefly revisit some concepts from last lecture that are relevant to
today’s material, including padding in convolutional networks and autoencoders, to ensure a solid
foundation.
    Detailed algebraic derivations (forward/backward passes and gradient expressions) appear in
Sections 215–216; readers are encouraged to work through the accompanying examples to solidify
intuition.

12.5    Recap: Feedforward Building Blocks
RNNs reuse the same ingredients as multilayer perceptrons—activations, nonlinear decision bound-
aries, loss functions, and training heuristics—but wrap them around a temporal axis. Figure 39
highlights the canonical MLP dataflow along with common activation choices and derivatives that
govern gradient flow.
    Two-dimensional toy datasets remain useful for reasoning about inductive biases. Figure 40
contrasts logistic regression and a shallow MLP on the moons dataset, illustrating how additional
hidden units carve nonlinear boundaries that RNN readouts later rely on when decoding the final
state.


                                                  156
Figure 39: Feedforward recap: (left) a two-hidden-layer MLP; (right) popular activation functions
and their derivatives, which determine how gradients propagate through deep or recurrent stacks.

   Finally, Figure 41 summarises two practical diagnostics from prior lectures—binary cross-
entropy geometry and the impact of learning-rate schedules or early stopping. We will reference
these again when tuning sequence models, where overfitting manifests as divergence between per-
token training and validation likelihood.

12.6   Limitations of Feedforward Neural Networks for Sequential Data
Feedforward neural networks (FNNs) process inputs in a fixed, non-temporal manner. Given an
input vector x, the network produces an output y without any explicit notion of order or memory
of past inputs. This characteristic makes FNNs ill-suited for tasks where the order of data points
is crucial, such as language modeling or time series prediction.

Example: Language Modeling           Consider the phrase:

                                 “The ball came out of the blue.”

Here, the meaning of the word “blue” depends heavily on its context and position in the sequence.
The phrase “out of the blue” is an idiomatic expression meaning something sudden or unexpected,
whereas “the ball was blue” refers to the color of the ball. A feedforward network that treats each
word independently or as a fixed-size input vector without temporal context cannot distinguish
these meanings effectively.

Example: Predictive Text and Autocomplete When typing a query such as “I want to
buy ...”, a model that understands the sequence can predict “teddy bear” as the next phrase.

                                               157
Figure 40: Decision boundaries for logistic regression (left) versus a shallow MLP (right). The latter
captures curved manifolds, a capability we reuse when mapping RNN hidden states to outputs.

Changing the context to “Write a book about Teddy...” leads to a different prediction, such as
“Teddy Roosevelt.” This demonstrates the importance of capturing the order and dependencies in
the input sequence.

Example: Stock Price Prediction Stock prices are inherently sequential and often exhibit
patterns such as trends and seasonality. Predicting tomorrow’s price requires understanding the
temporal order of past prices:
                                  xt−3 , xt−2 , xt−1 , xt → x̂t+1
Ignoring the order or treating these as independent inputs loses critical information about growth
trends and seasonal cycles.

Challenges with Variable-Length Inputs Many real-world sequences vary in length. For
example, product reviews may range from a few words to hundreds of words, but the output (e.g.,
a star rating) is fixed-length. Feedforward networks require fixed-size inputs, so variable-length
sequences must be truncated or padded, which can degrade performance.

12.7    Recurrent Neural Networks (RNNs)
Recurrent Neural Networks are designed to address these limitations by incorporating memory of
past inputs into their architecture. Unlike feedforward networks, RNNs process sequences element-
by-element, maintaining a hidden state that summarizes information from previous time steps.

Key Idea At each time step t, the RNN receives an input xt and updates its hidden state ht
based on the current input and the previous hidden state ht−1 :

                                  ht = f (Wxh xt + Whh ht−1 + bh )                              (208)
                                   yt = g(Why ht + by )                                         (209)

where
  • Wxh , Whh , and Why are weight matrices,

  • bh and by are bias vectors,

  • f (·) is a nonlinear activation function (e.g., tanh or ReLU),

                                                 158
Figure 41: (Top) Binary cross-entropy curvature with respect to the logit; (bottom) effect of
aggressive versus conservative learning-rate schedules and the telltale validation plateau used for
early stopping.

  • g(·) is an output activation function (e.g., softmax for classification).
     The hidden state ht acts as a memory that captures information about all previous inputs
x1 , x 2 , . . . , x t .
```

### Findings
- **Equation (205) and (208) consistency:**  
  - Equation (205) states a general form: \( h_t = f(h_{t-1}, x_t; \theta) \).  
  - Equation (208) specifies a particular instantiation: \( h_t = f(W_{xh} x_t + W_{hh} h_{t-1} + b_h) \).  
  - It would be helpful to explicitly state that (208) is a common parametric form of the general function \( f \) in (205), to avoid confusion.

- **Notation clarity:**  
  - The parameters \(\theta\) and \(\theta'\) in (205) and (206) are introduced as general learned parameters, but later in (208) and (209) the parameters are explicitly named \(W_{xh}, W_{hh}, W_{hy}, b_h, b_y\). It would improve clarity to explicitly link \(\theta = \{W_{xh}, W_{hh}, b_h\}\) and \(\theta' = \{W_{hy}, b_y\}\) or mention that \(\theta, \theta'\) represent these sets of parameters.

- **Definition of functions \(f\) and \(g\):**  
  - The text states \(f\) and \(g\) are "typically nonlinear functions implemented by neural network layers," but does not specify that \(f\) usually includes an element-wise nonlinearity (e.g., tanh or ReLU) applied after the affine transformation. This is only clarified later in (208). It would be better to define this explicitly when first introducing \(f\) and \(g\).

- **Ambiguity in output function \(g\):**  
  - The function \(g\) is described as a function of \(h_t\) with parameters \(\theta'\), but the nature of \(g\) (e.g., linear layer followed by softmax or other activation) is not specified until (209). Early clarification would help.

- **Missing definition of input and output dimensions:**  
  - The dimensions of \(x_t\), \(h_t\), and \(y_t\) are not specified. While this may be covered elsewhere, a brief mention would help readers understand the shapes involved.

- **"Summary or encoding of entire input history":**  
  - The claim that \(h_t\) summarizes the entire input history \(\{x_1, ..., x_t\}\) is standard but should be qualified: in practice, due to vanishing gradients and limited capacity, \(h_t\) may not perfectly encode all past inputs, especially for long sequences.

- **Section 12.3: Feedforward network output \(y_t = \phi(x_t; \theta)\):**  
  - The notation \(\phi\) is introduced without prior definition. It would be better to explicitly state that \(\phi\) is a nonlinear function (e.g., an MLP) mapping input to output.

- **Section 12.6: Examples and claims:**  
  - The examples illustrating limitations of feedforward networks are well-chosen. However, the claim that feedforward networks "treat each word independently or as a fixed-size input vector without temporal context" could be nuanced by mentioning that feedforward networks can process fixed-size windows or concatenations of past inputs, but this is limited and inefficient compared to RNNs.

- **Section 12.6: Variable-length inputs:**  
  - The note that feedforward networks require fixed-size inputs is correct, but it would be helpful to mention common strategies like padding, truncation, or using sequence models (RNNs, Transformers) to handle variable-length sequences.

- **Section 12.7: RNN equations (208) and (209):**  
  - The notation \(W_{hy}\) in (209) is inconsistent with the earlier \(W_{yh}\) in (206). It should be consistent; typically, the weight matrix from hidden to output is denoted \(W_{hy}\) or \(W_{yh}\), but the same notation should be used throughout.

- **Activation functions:**  
  - The text mentions \(f(\cdot)\) as nonlinear activation (e.g., tanh or ReLU) and \(g(\cdot)\) as output activation (e.g., softmax). It would be helpful to clarify that \(g\) may be linear or nonlinear depending on the task (e.g., regression vs classification).

- **Figure references:**  
  - Figures 39, 40, and 41 are referenced but not included here. Ensure that these figures clearly illustrate the points made, especially the activation functions and decision boundaries.

- **Summary and flow:**  
  - The progression from general RNN definition to specific equations and examples is logical and well-structured.

**Overall, the content is accurate and well-presented but would benefit from:**

- Explicit linking of general and specific parameter notations.  
- Clear definitions of functions \(f, g, \phi\) when first introduced.  
- Consistent notation for weight matrices.  
- Brief mention of dimensionalities and practical limitations of hidden state summarization.  
- More precise language regarding feedforward networks' handling of temporal data.

## Chunk 63/95
- Character range: 413187–420341

```text
Comparison to Feedforward Networks
  • Memory: RNNs explicitly maintain a state that evolves over time, enabling them to remem-
    ber past inputs.

  • Variable-length inputs: RNNs naturally handle sequences of varying length by iterating
    over the input sequence.

  • Parameter sharing: The same weights Wxh , Whh , and Why are used at every time step,
    reducing the number of parameters and enabling generalization across time.

Historical Note: Hopfield Networks The first successful recurrent network was the Hopfield
network, which is a form of associative memory. Unlike modern RNNs, Hopfield networks have

                                                159
symmetric weights and are designed to converge to stable states representing stored patterns.
While Hopfield networks are not directly used for sequence modeling, they laid the groundwork for
understanding recurrent architectures.

12.8    Mathematical Formulation of RNNs
Consider an input sequence {x1 , x2 , . . . , xT }, where each xt ∈ Rd . The RNN computes hidden
states {h1 , h2 , . . . , hT } and outputs {y1 , y2 , . . . , yT } as follows:

                          h0 = 0 (initial hidden state)                                       (210)
                          ht = f (Wxh xt + Whh ht−1 + bh ),           t = 1, . . . , T        (211)
                          yt = g(Why ht + by ),    t = 1, . . . , T                           (212)

12.9    Recurrent Neural Networks: Historical Context and Motivation
Recall from our earlier discussion on Hopfield networks that the configuration of the network states
significantly impacts the overall energy landscape. The sequence of states, or more precisely, their
spatial arrangement within the network, determines the energy and thus the network’s behavior.
This property endowed Hopfield networks with associative memory capabilities, as the weights were
constructed to ”remember” specific patterns.
    However, Hopfield networks were primarily designed for storage and retrieval of static patterns
rather than for dynamic prediction or forecasting tasks. Despite their introduction in 1982, their
practical utility beyond research was limited.

12.10    The 1986 Breakthrough: David Rumelhart et al.’s Recurrent Neural Net-
         work
In 1986, a seminal paper by David Rumelhart and collaborators introduced a novel recurrent neural
network (RNN) architecture inspired by—but distinct from—the Hopfield network. This work laid
the foundation for modern RNNs by explicitly modeling temporal dependencies and contextual
relationships in sequential data.
    The key insight was to capture the notion that elements appearing adjacently or in close proxim-
ity within a sequence have meaningful relationships. For example, in natural language processing,
if word A frequently co-occurs with word B, then the connection between their corresponding
network units should be strong and positive. Conversely, if A appears without B, this implies a
negative or weak connection.

Example: Word Associations - The words ”apple” and ”juice” often appear together, so the
connection between their representations is strong and positive. - The words ”apple” and ”car”
rarely co-occur, indicating a weak or negative connection. - Such associations reflect statistical
regularities in language and can be encoded in the network weights.

Implications This approach allowed the network to learn and represent contextual dependencies,
which are crucial for tasks like language modeling and sequence prediction. The 1986 paper explic-
itly referenced Hopfield networks as an inspiration but extended the concept to handle temporal
sequences and state transitions.




                                                  160
12.11    State Dynamics in Recurrent Neural Networks
The 1986 RNN formulation introduced the concept of a state that evolves over time as a function
of the previous state and the current input. Formally, the state update can be expressed as:

                                         ht = f (ht−1 , xt ; θ),                             (213)

where

  • ht is the hidden state at time t,

  • xt is the input at time t,

  • f is a nonlinear function parameterized by θ (e.g., weights and biases),

  • ht−1 is the hidden state at the previous time step.

   The output at time t, denoted yt , is typically computed as a function of the hidden state:

                                            yt = g(ht ; ϕ),                                  (214)

where g is another nonlinear function parameterized by ϕ.

Interpretation - The hidden state ht acts as a memory that summarizes information from all
previous inputs up to time t. - The recurrence allows the network to maintain context and model
temporal dependencies.

12.12    Unfolding the Recurrent Neural Network
To better understand and implement RNNs, it is common to unfold the network through time.
Unfolding transforms the recurrent structure into a feedforward network with shared weights across
time steps.

Process - Start with an initial hidden state h0 , which may be initialized to zero or learned. - At
each time step t, compute ht using Equation (213). - Compute output yt using Equation (218). -
The parameters θ and ϕ are shared across all time steps, enabling the network to generalize across
sequences of varying lengths.

Significance - Unfolding clarifies the flow of information and dependencies across time. - It
facilitates the application of backpropagation through time (BPTT) for training.

12.13    Mathematical Formulation of a Simple RNN Cell
Consider a simple RNN cell with the following update equations:

                                 ht = σh (Whh ht−1 + Wxh xt + bh ) ,                         (215)
                                 yt = σy (Why ht + by ) .                                    (216)




                                                  161
Figure 42: Unrolling an RNN shows that the same parameters repeat across time steps; gradients
must therefore propagate through every copy during BPTT.


12.14    Recurrent Neural Network (RNN) Unfolding and Parameter Sharing
Recall that a recurrent neural network (RNN) processes sequential data by maintaining a hidden
state that evolves over time. At each time step t, the network receives an input xt and updates its
hidden state at , which in turn produces an output yt .

Unfolding the RNN Unfolding the RNN across time steps transforms the recurrent structure
into a deep feedforward network with shared weights across layers (time steps). This unrolled
network looks like a chain where each hidden state depends on the previous hidden state and the
current input:

                               at = f (at−1 , xt ; Θ),   yt = g(at ; Θy )
   where f and g are nonlinear functions parameterized by weights Θ and Θy , respectively.

Parameter Sharing      A key property of RNNs is parameter sharing across time steps. Specifically:

  • The weights connecting the previous hidden state at−1 to the current hidden state at are the
    same for all t.

  • The weights connecting the input xt to the hidden state at are also shared across all time
    steps.
```

### Findings
- **Ambiguous notation for hidden state:**  
  - The notes use both \( h_t \) and \( a_t \) to denote the hidden state in different sections (e.g., Eq. (213) uses \( h_t \), while the unfolding section uses \( a_t \)). This inconsistency can confuse readers. It is better to consistently use one symbol for the hidden state throughout.

- **Missing explicit definitions of functions \( f \) and \( g \):**  
  - While \( f \) and \( g \) are described as nonlinear functions parameterized by weights and biases, the notes do not explicitly state typical choices (e.g., \( f \) often involves a tanh or ReLU activation, \( g \) might be softmax or linear depending on the task). Adding this would clarify the model.

- **Equation (218) referenced but missing:**  
  - In section 12.12, the notes mention computing output \( y_t \) using Equation (218), but this equation is not present in the provided chunk. This is a gap that should be addressed.

- **Initial hidden state \( h_0 \) treatment:**  
  - The notes state \( h_0 = 0 \) in Eq. (210) but later mention it can be learned or initialized to zero. This should be clarified upfront to avoid confusion.

- **Historical claim about 1986 RNN paper:**  
  - The notes credit David Rumelhart et al. (1986) with introducing a novel RNN architecture inspired by Hopfield networks. While Rumelhart et al. contributed to backpropagation and neural networks, the first formal RNN training via backpropagation through time is often attributed to Werbos (1990) or earlier works by Elman (1990). The historical context could be nuanced or referenced more precisely.

- **Hopfield network description:**  
  - The notes correctly state Hopfield networks have symmetric weights and converge to stable states. However, it might be helpful to explicitly mention that Hopfield networks are energy-based models and do not have explicit temporal dynamics like RNNs.

- **Parameter sharing explanation:**  
  - The notes mention weights \( W_{xh}, W_{hh}, W_{hy} \) are shared across time steps, which is correct. However, the notation \( \Theta \) and \( \Theta_y \) introduced later for parameter sets is not explicitly connected to these matrices, which could confuse readers.

- **Use of "negative or weak connection":**  
  - The claim that if word A appears without word B, this implies a negative or weak connection is an oversimplification. Co-occurrence statistics do not necessarily imply negative weights; absence of co-occurrence often leads to near-zero or weak weights, but negative weights are not guaranteed or always meaningful.

- **Lack of mention of vanishing/exploding gradients:**  
  - While not strictly necessary here, a brief mention of challenges in training RNNs (e.g., vanishing/exploding gradients) would provide a more complete picture.

- **No explicit mention of output types:**  
  - The notes do not specify that outputs \( y_t \) can be used for different tasks (e.g., sequence labeling, sequence generation), which would help contextualize the equations.

- **Figure 42 reference without figure:**  
  - The text references Figure 42 about unrolling RNNs, but the figure is not included. This reduces clarity.

Overall, the chunk is mostly accurate but would benefit from consistent notation, clearer definitions, and minor historical clarifications.

## Chunk 64/95
- Character range: 420343–427969

```text
• The weights mapping the hidden state at to the output yt are shared as well.

   This parameter sharing reduces the number of parameters to learn and enables the network to
generalize across different positions in the sequence.


                                                  162
12.15   Mathematical Formulation of the RNN
We formalize the RNN update equations as follows. Let the hidden state at time t be at ∈ Rh , the
input at time t be xt ∈ Rd , and the output at time t be yt ∈ Ro .


                                 at = σ (Wa at−1 + Wx xt + ba ) ,                          (217)
                                 yt = ϕ (Wy at + by ) ,                                    (218)

   where:

  • Wa ∈ Rh×h is the recurrent weight matrix (hidden-to-hidden).

  • Wx ∈ Rh×d is the input-to-hidden weight matrix.

  • Wy ∈ Ro×h is the hidden-to-output weight matrix.

  • ba ∈ Rh and by ∈ Ro are bias vectors.

  • σ(·) is the activation function for the hidden state (commonly tanh or ReLU).

  • ϕ(·) is the output activation function (e.g., softmax for classification).

Interpretation Equation (229) shows that the current hidden state at is a nonlinear transforma-
tion of the previous hidden state at−1 and the current input xt . Equation (218) maps the hidden
state to the output at time t.

Reusability of the Hidden State The hidden state at serves as a summary of all previous inputs
up to time t. This recursive formulation allows the network to capture temporal dependencies of
arbitrary length.

12.16   Generalized Notation
To simplify notation, define the concatenated input vector at time t:
                                                 
                                              a
                                       zt = t−1 ∈ Rh+d .
                                               xt
   Correspondingly, define the combined weight matrix:
                                          
                                  W = Wa Wx ∈ Rh×(h+d) .
   Then the hidden state update can be written compactly as:

                                        at = σ (Wzt + ba ) .                               (219)




                                                163
Figure 43: Backpropagation Through Time unfolds the recurrent graph into a deep feedforward
stack, accumulating gradients from every time step before updating the shared parameters.


12.17    Recurrent Neural Network (RNN) Architectures and Loss Computation
Recall from previous discussions that the loss function for classification tasks often involves cross-
entropy terms of the form:                     X
                                        L=−        yi log ŷi ,                                 (220)
                                                  i

where yi is the true label (often one-hot encoded) and ŷi is the predicted probability for class i.
When ŷ = y, the loss is zero, indicating perfect prediction.
    In the context of RNNs, the total loss over a sequence is typically the sum of losses at each time
step:
                                                    XT
                                           Ltotal =     Lt ,                                     (221)
                                                      t=1

where T is the sequence length.

Forward and Backward Passes in RNNs The forward pass involves propagating inputs
through the network over time steps t = 1, . . . , T , producing outputs ŷt at each step. After comput-
ing the loss, the backward pass computes gradients with respect to parameters by backpropagating
errors through time, a process known as Backpropagation Through Time (BPTT).
    BPTT unfolds the RNN across time steps and applies standard backpropagation through this
unrolled network. The key insight is that parameters are shared across time steps, so gradients
accumulate contributions from all time steps.

Vanishing and Exploding Gradients Because each gradient term contains products of Ja-
cobians such as ∂ht /∂ht−1 = Whh  ⊤ diag(σ ′ ), long sequences amplify eigenvalues of W . If the
                                           h                                             hh
spectral radius is below one the gradients decay exponentially (vanishing); if it is above one they



                                                  164
Figure 44: Illustration of vanishing (blue) versus exploding (orange) gradient norms over many
recurrent steps. Stable training aims to keep gradients within the grey band.

grow uncontrollably (exploding). Figure 44 illustrates both behaviours across time. Practical reme-
dies include gradient clipping, orthogonal or unitary recurrent matrices, layer normalization, and
gated architectures (LSTM/GRU) that introduce additive memory paths.

Parameter Updates At each time step, the gradient of the loss with respect to parameters (e.g.,
weights W ) depends on the chain of partial derivatives through the network states:

                                         ∂L   X ∂Lt
                                                 T
                                            =       .                                        (222)
                                         ∂W     ∂W
                                                 t=1

Because of parameter sharing, the same W influences multiple time steps, and the total gradient
is the sum over these contributions.

12.18    Stabilizing Recurrent Training
Gradient clipping. A practical safeguard is to clip the global norm of the gradient when it
exceeds a threshold. Figure 45 shows how clipping prevents the exploding case from destabilizing
optimisation while leaving the vanishing regime untouched.

Teacher forcing and scheduled sampling. Sequence-to-sequence models frequently feed the
ground-truth token back into the decoder during training (teacher forcing) to accelerate conver-
gence. Figure 46 depicts this contrasted with free-running inference, underscoring why scheduled
sampling is often introduced to narrow the gap between the two regimes.

Gated cells. LSTMs and GRUs alleviate vanishing gradients by introducing additive memory
paths guarded by gates. Figures 47 and 48 present the canonical cell diagrams used later in the
lecture when deriving the update equations.

                                               165
Figure 45: Gradient norms with (green) and without (red) clipping, and the corresponding training
curves illustrating improved stability.


Attention mechanisms. Even with gating, long sequences can challenge fixed-size hidden states.
Attention augments the decoder with a content-based lookup into the encoder states, as visualised
in Figure 49. Bright entries correspond to encoder positions that most influence each generated
token.

12.19    RNN Input-Output Configurations
RNNs can be configured in several ways depending on the task:

  • Many-to-Many (Equal Length): Input and output sequences have the same length T .
    For example, sequence labeling tasks.

  • Many-to-One: Input is a sequence of length T , output is a single prediction. Example:
    sentiment analysis where a sentence maps to a sentiment score.

  • Many-to-Many (Unequal Length): Input and output sequences have different lengths.
    Example: machine translation where input and output sentences differ in length.

  • One-to-Many: Single input produces a sequence output. Less common, but applicable in
    tasks like image captioning where one image input generates a sequence of words.

   The main difference lies in how the loss is computed and how outputs are generated, but the
underlying backpropagation principles remain consistent.
```

### Findings
- **Ambiguous notation in concatenated vector definition (Section 12.16):**  
  The concatenated input vector \( z_t \) is defined as  
  \[
  z_t = \begin{bmatrix} a_{t-1} \\ x_t \end{bmatrix} \in \mathbb{R}^{h+d}
  \]  
  but the text shows a confusing symbol "     " and "t−1 ∈ Rh+d" which appears to be a formatting or typographical error. This should be corrected for clarity.

- **Equation numbering inconsistency:**  
  The text refers to "Equation (229)" when interpreting the hidden state update, but the equation for the hidden state update is numbered (217). This is likely a typo and should be corrected to avoid confusion.

- **Missing explicit definition of symbols in loss function (Equation 220):**  
  The loss function is given as  
  \[
  L = - \sum_i y_i \log \hat{y}_i
  \]  
  but it is not explicitly stated that \( y_i \) and \( \hat{y}_i \) correspond to the true and predicted probabilities for a single time step or a single sample. Clarifying this would improve precision.

- **Clarification needed on notation in total loss over sequence (Equation 221):**  
  The total loss is given as  
  \[
  L_{\text{total}} = \sum_{t=1}^T L_t
  \]  
  but it is not explicitly stated that \( L_t \) is the loss at time step \( t \), which is presumably computed as in (220). This should be explicitly mentioned.

- **Inconsistent notation for hidden state:**  
  The hidden state is denoted as \( a_t \) throughout, which is somewhat unusual since \( h_t \) is more standard in literature. While not incorrect, a note on this choice or consistency check would be helpful.

- **Lack of explicit mention of dimensions in concatenated weight matrix \( W \):**  
  The combined weight matrix \( W = [W_a \quad W_x] \) is defined as \( W \in \mathbb{R}^{h \times (h+d)} \), which is correct, but the notation \( W = W_a W_x \) in the text is ambiguous and could be misread as matrix multiplication rather than concatenation. It should be clarified that \( W \) is formed by horizontal concatenation of \( W_a \) and \( W_x \).

- **Vanishing and exploding gradients explanation could be more precise:**  
  The text states "Because each gradient term contains products of Jacobians such as \(\partial h_t / \partial h_{t-1} = W_{hh}^\top \operatorname{diag}(\sigma')\), long sequences amplify eigenvalues of \( W \)."  
  - The transpose on \( W_{hh} \) is unusual; typically the Jacobian is \( W_{hh} \) multiplied by the diagonal matrix of derivatives.  
  - The explanation that eigenvalues of \( W \) are amplified is somewhat imprecise; it is the product of Jacobians whose spectral radius determines gradient behavior.  
  - The term "spectral radius is below one" should specify that it refers to the spectral radius of the Jacobian matrix or recurrent weight matrix.

- **Equation (222) notation ambiguity:**  
  The gradient of the loss with respect to parameters is given as  
  \[
  \frac{\partial L}{\partial W} = \sum_{t=1}^T \frac{\partial L_t}{\partial W}
  \]  
  but the notation \(\partial L_t / \partial W\) is somewhat informal since \( L_t \) depends on \( W \) through the entire unrolled network up to time \( t \). A more precise statement would clarify that gradients accumulate over time steps due to parameter sharing.

- **Teacher forcing and scheduled sampling explanation could be expanded:**  
  The text mentions these techniques but does not define scheduled sampling explicitly. A brief definition or reference would improve completeness.

- **No explicit mention of initial hidden state \( a_0 \):**  
  The initial hidden state \( a_0 \) is not defined or discussed, which is important for understanding the recursion.

- **Inconsistent use of activation functions:**  
  The hidden state activation \( \sigma(\cdot) \) is said to be commonly tanh or ReLU, but ReLU is less common in vanilla RNNs due to exploding activations. A note on typical choices or implications would be helpful.

- **Minor typographical issues:**  
  - The phrase "the weights mapping the hidden state at to the output yt are shared as well" is missing subscripts formatting (should be \( a_t \), \( y_t \)).  
  - The phrase "the same W influences multiple time steps" could specify which \( W \) (e.g., \( W_a, W_x, W_y \)) for clarity.

Overall, the content is mostly correct but would benefit from clarifications, corrections of minor typographical and notation issues, and more precise explanations in some places.
