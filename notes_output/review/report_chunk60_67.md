# Scientific QA Report

- Source PDF: `notes_output/ece657_notes.pdf`
- Total chunks: 8

## Chunk 60/91
- Character range: 383290–390166

```text
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

Backpropagation through CNNs Backpropagation in CNNs updates the weights of convolu-
tional filters and fully connected layers by propagating the error gradients backward through the
network. Although the network may appear complex due to three-dimensional feature maps and
multiple layers, the underlying principle remains the same as in standard neural networks: compute
gradients with respect to weights and update them using gradient descent or its variants.
    The flattening operation is a logical reshaping and does not affect the gradient flow; gradients
are simply propagated through the reshaped vector back to the convolutional layers.




                                                 139
11.34   Historical Perspective on CNNs
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

11.35   Key Hyperparameters in CNN Design
Designing an effective CNN requires careful selection of several hyperparameters:

  • Filter size: The spatial dimensions of convolutional kernels (e.g., 3 × 3, 5 × 5).

  • Stride: The step size with which the filter moves across the input.

  • Padding: Whether to add zeros around the input to control the spatial size of the output.

  • Pooling type and size: Max pooling, average pooling, and their window sizes and strides.

  • Number of filters: The depth of the output feature maps.

   These parameters are typically chosen based on empirical results, domain knowledge, and com-
putational constraints. For example, AlexNet used a stride of 4 in its first convolutional layer,
which was a design choice balancing computational eﬀiciency and feature extraction quality.

Summary
In this lecture, we concluded our discussion on convolutional neural networks by:

  • Explaining the flattening operation that converts multi-dimensional feature maps into vectors
    for classification.

  • Reviewing backpropagation through CNNs and clarifying that the three-dimensional structure
    is a logical representation of connections.

  • Providing a historical overview of CNN development from early models to modern deep
    architectures.

  • Highlighting the importance of hyperparameter selection in CNN design and training.


                                               140
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
```

### Findings
- The explanation of flattening is clear and correct; the example of flattening a 4 × 4 × 40 tensor to a 640-length vector is accurate.

- The note that flattening is a logical reshaping that does not affect gradient flow is correct and important.

- The historical timeline of CNN development is accurate and well summarized, including key milestones and innovations introduced by AlexNet.

- The list of key hyperparameters in CNN design is appropriate and covers the main factors influencing CNN architecture.

- The mention of AlexNet’s use of stride 4 in the first convolutional layer is correct and well contextualized.

- The summary correctly recaps the main points of the lecture.

- The transition to RNNs and the motivation for their use is well stated, emphasizing the need for memory and temporal dependencies.

- The examples of applications requiring RNNs are appropriate and relevant.

No issues spotted.

## Chunk 61/91
- Character range: 390170–397406

```text
141
    Feedforward networks treat each input independently and do not have an inherent mechanism
to remember or utilize past inputs. To incorporate past information, one might consider explicitly
including previous inputs as part of the current input vector, but this approach quickly becomes
impractical as the history length grows.

12.2    Key Idea: State and Memory in RNNs
Recurrent neural networks address this limitation by introducing a state vector ht that summarizes
information from all previous inputs up to time t. The state is updated recursively as new inputs
arrive, allowing the network to maintain a form of memory.
    Formally, at each time step t, the RNN receives an input vector xt and updates its hidden state
ht according to a function f parameterized by weights θ:


                                          ht = f (ht−1 , xt ; θ)                                   (205)

   The output yt at time t is then computed as a function of the current state:


                                             yt = g(ht ; θ′ )                                      (206)

    Here, f and g are typically nonlinear functions implemented by neural network layers, and θ, θ′
are learned parameters.

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


                                                  142
  • Discuss challenges such as vanishing and exploding gradients.

  • Introduce variants of RNNs designed to mitigate these challenges.

  • Explore applications where RNNs provide significant advantages over feedforward networks.

    Before proceeding, we will briefly revisit some concepts from last lecture that are relevant to
today’s material, including padding in convolutional networks and autoencoders, to ensure a solid
foundation.
    Detailed algebraic derivations (forward/backward passes and gradient expressions) appear in
Sections 215–216; readers are encouraged to work through the accompanying examples to solidify
intuition.

12.5   Limitations of Feedforward Neural Networks for Sequential Data
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



                                               143
12.6    Recurrent Neural Networks (RNNs)
Recurrent Neural Networks are designed to address these limitations by incorporating memory of
past inputs into their architecture. Unlike feedforward networks, RNNs process sequences element-
by-element, maintaining a hidden state that summarizes information from previous time steps.

Key Idea At each time step t, the RNN receives an input xt and updates its hidden state ht
based on the current input and the previous hidden state ht−1 :

                                  ht = f (Wxh xt + Whh ht−1 + bh )                         (208)
                                  yt = g(Why ht + by )                                     (209)

where

  • Wxh , Whh , and Why are weight matrices,

  • bh and by are bias vectors,

  • f (·) is a nonlinear activation function (e.g., tanh or ReLU),

  • g(·) is an output activation function (e.g., softmax for classification).

     The hidden state ht acts as a memory that captures information about all previous inputs
x1 , x 2 , . . . , x t .

Comparison to Feedforward Networks

  • Memory: RNNs explicitly maintain a state that evolves over time, enabling them to remem-
    ber past inputs.

  • Variable-length inputs: RNNs naturally handle sequences of varying length by iterating
    over the input sequence.

  • Parameter sharing: The same weights Wxh , Whh , and Why are used at every time step,
    reducing the number of parameters and enabling generalization across time.

Historical Note: Hopfield Networks The first successful recurrent network was the Hopfield
network, which is a form of associative memory. Unlike modern RNNs, Hopfield networks have
symmetric weights and are designed to converge to stable states representing stored patterns.
While Hopfield networks are not directly used for sequence modeling, they laid the groundwork for
understanding recurrent architectures.

12.7    Mathematical Formulation of RNNs
Consider an input sequence {x1 , x2 , . . . , xT }, where each xt ∈ Rd . The RNN computes hidden
states {h1 , h2 , . . . , hT } and outputs {y1 , y2 , . . . , yT } as follows:
```

### Findings
- **Equation (205) and (208) consistency:**  
  Equation (205) states a general form: \( h_t = f(h_{t-1}, x_t; \theta) \), while equation (208) specifies a particular instantiation:  
  \[
  h_t = f(W_{xh} x_t + W_{hh} h_{t-1} + b_h)
  \]  
  It would be helpful to explicitly state that (208) is a common parameterization of the general function \( f \) in (205), to avoid confusion.

- **Notation clarity for parameters:**  
  The parameters \(\theta\) and \(\theta'\) in (205) and (206) are introduced as learned parameters, but their relationship to \(W_{xh}, W_{hh}, W_{hy}, b_h, b_y\) in (208) and (209) is not explicitly stated. Clarifying that \(\theta = \{W_{xh}, W_{hh}, b_h\}\) and \(\theta' = \{W_{hy}, b_y\}\) would improve clarity.

- **Definition of functions \(f\) and \(g\):**  
  The functions \(f\) and \(g\) are described as "typically nonlinear functions implemented by neural network layers," but no explicit mention is made that \(f\) usually includes an activation function (e.g., tanh or ReLU), and \(g\) often includes an output activation (e.g., softmax for classification). While this is mentioned later, it would be better to introduce these details earlier when \(f\) and \(g\) are first defined.

- **Ambiguity in "state vector \(h_t\) summarizes information from all previous inputs":**  
  The claim that \(h_t\) summarizes information from all previous inputs \(\{x_1, \ldots, x_t\}\) is conceptually correct but should be qualified: in practice, due to vanishing gradients and limited capacity, \(h_t\) may not perfectly encode all past information, especially for long sequences. A brief mention of this limitation would be beneficial.

- **Feedforward network input vector containing past information:**  
  The text states that including previous inputs explicitly in the input vector becomes impractical as history length grows. It would be helpful to mention the dimensionality explosion and computational inefficiency explicitly to justify this claim.

- **Example of language modeling:**  
  The example "The ball came out of the blue" vs. "the ball was blue" is good, but the explanation could be improved by clarifying that feedforward networks lack the mechanism to capture word order or context beyond the fixed input window, which is why they fail to distinguish idiomatic expressions.

- **Variable-length input handling in feedforward networks:**  
  The text mentions truncation or padding as solutions but does not discuss their drawbacks in detail. It would be useful to briefly mention that padding can introduce artificial tokens and truncation can lose important information.

- **Historical note on Hopfield networks:**  
  The note is accurate but could be expanded to clarify that Hopfield networks are recurrent but not sequence models, and their dynamics differ fundamentally from RNNs used in sequence processing.

- **Missing explicit definition of dimensions:**  
  When introducing \(x_t \in \mathbb{R}^d\), it would be helpful to also specify the dimensions of \(h_t\), \(W_{xh}\), \(W_{hh}\), \(W_{hy}\), \(b_h\), and \(b_y\) for completeness.

- **No mention of initial hidden state \(h_0\):**  
  The initial hidden state \(h_0\) is not defined or discussed. Since it is important for the recursion, a brief note on its typical initialization (e.g., zero vector or learned parameter) would be appropriate.

- **Equation numbering and referencing:**  
  The text references equations (205), (206), (207), (208), and (209) appropriately, but the transition between general and specific forms could be smoother by explicitly linking these equations.

- **Typographical consistency:**  
  The notation for the output weight matrix is given as \(W_{hy}\) in (209) but as \(W_{y h}\) in the text (e.g., "Why"). Consistent notation (preferably \(W_{hy}\)) should be used throughout.

- **Summary and outline sections:**  
  The outline of Lecture 7 is clear and well-structured. However, the mention of revisiting padding and autoencoders from the previous lecture seems slightly out of place here unless explicitly connected to RNNs.

- **Minor wording:**  
  The phrase "feedforward networks treat each input independently" could be misinterpreted; it might be better to say "treat each input vector independently without temporal context."

Overall, the content is accurate and well-presented but would benefit from the above clarifications and additional details to improve rigor and clarity.

## Chunk 62/91
- Character range: 397456–404381

```text
h0 = 0 (initial hidden state)                                    (210)
                          ht = f (Wxh xt + Whh ht−1 + bh ),           t = 1, . . . , T     (211)
                          yt = g(Why ht + by ),    t = 1, . . . , T                        (212)



                                                  144
12.8    Recurrent Neural Networks: Historical Context and Motivation
Recall from our earlier discussion on Hopfield networks that the configuration of the network states
significantly impacts the overall energy landscape. The sequence of states, or more precisely, their
spatial arrangement within the network, determines the energy and thus the network’s behavior.
This property endowed Hopfield networks with associative memory capabilities, as the weights were
constructed to ”remember” specific patterns.
    However, Hopfield networks were primarily designed for storage and retrieval of static patterns
rather than for dynamic prediction or forecasting tasks. Despite their introduction in 1982, their
practical utility beyond research was limited.

12.9    The 1986 Breakthrough: David Rumelhart et al.’s Recurrent Neural Net-
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

12.10    State Dynamics in Recurrent Neural Networks
The 1986 RNN formulation introduced the concept of a state that evolves over time as a function
of the previous state and the current input. Formally, the state update can be expressed as:

                                        ht = f (ht−1 , xt ; θ),                               (213)

where

  • ht is the hidden state at time t,

  • xt is the input at time t,

  • f is a nonlinear function parameterized by θ (e.g., weights and biases),

  • ht−1 is the hidden state at the previous time step.


                                                 145
   The output at time t, denoted yt , is typically computed as a function of the hidden state:

                                            yt = g(ht ; ϕ),                                  (214)

where g is another nonlinear function parameterized by ϕ.

Interpretation - The hidden state ht acts as a memory that summarizes information from all
previous inputs up to time t. - The recurrence allows the network to maintain context and model
temporal dependencies.

12.11    Unfolding the Recurrent Neural Network
To better understand and implement RNNs, it is common to unfold the network through time.
Unfolding transforms the recurrent structure into a feedforward network with shared weights across
time steps.

Process - Start with an initial hidden state h0 , which may be initialized to zero or learned. - At
each time step t, compute ht using Equation (213). - Compute output yt using Equation (218). -
The parameters θ and ϕ are shared across all time steps, enabling the network to generalize across
sequences of varying lengths.

Significance - Unfolding clarifies the flow of information and dependencies across time. - It
facilitates the application of backpropagation through time (BPTT) for training.

12.12    Mathematical Formulation of a Simple RNN Cell
Consider a simple RNN cell with the following update equations:

                               ht = σh (Whh ht−1 + Wxh xt + bh ) ,                           (215)
                               yt = σy (Why ht + by ) .                                      (216)

12.13    Recurrent Neural Network (RNN) Unfolding and Parameter Sharing
Recall that a recurrent neural network (RNN) processes sequential data by maintaining a hidden
state that evolves over time. At each time step t, the network receives an input xt and updates its
hidden state at , which in turn produces an output yt .

Unfolding the RNN Unfolding the RNN across time steps transforms the recurrent structure
into a deep feedforward network with shared weights across layers (time steps). This unrolled
network looks like a chain where each hidden state depends on the previous hidden state and the
current input:

                               at = f (at−1 , xt ; Θ),   yt = g(at ; Θy )
   where f and g are nonlinear functions parameterized by weights Θ and Θy , respectively.




                                                  146
Parameter Sharing      A key property of RNNs is parameter sharing across time steps. Specifically:

  • The weights connecting the previous hidden state at−1 to the current hidden state at are the
    same for all t.

  • The weights connecting the input xt to the hidden state at are also shared across all time
    steps.

  • The weights mapping the hidden state at to the output yt are shared as well.

   This parameter sharing reduces the number of parameters to learn and enables the network to
generalize across different positions in the sequence.

12.14   Mathematical Formulation of the RNN
We formalize the RNN update equations as follows. Let the hidden state at time t be at ∈ Rh , the
input at time t be xt ∈ Rd , and the output at time t be yt ∈ Ro .


                                 at = σ (Wa at−1 + Wx xt + ba ) ,                            (217)
                                 yt = ϕ (Wy at + by ) ,                                      (218)

   where:

  • Wa ∈ Rh×h is the recurrent weight matrix (hidden-to-hidden).

  • Wx ∈ Rh×d is the input-to-hidden weight matrix.

  • Wy ∈ Ro×h is the hidden-to-output weight matrix.

  • ba ∈ Rh and by ∈ Ro are bias vectors.

  • σ(·) is the activation function for the hidden state (commonly tanh or ReLU).

  • ϕ(·) is the output activation function (e.g., softmax for classification).
```

### Findings
- **Equation numbering inconsistency:**  
  - Equation (218) is referenced in section 12.11 ("Compute output yt using Equation (218)"), but the actual equation (218) appears only in section 12.14. This could confuse readers; it would be clearer to introduce or reference equations in order.

- **Ambiguous notation for hidden state:**  
  - The hidden state is denoted as both \( h_t \) (e.g., Eq. 211, 215) and \( a_t \) (e.g., Eq. 217). While this is common, the notes should explicitly state that \( h_t \) and \( a_t \) represent the same concept to avoid confusion.

- **Missing explicit definitions of activation functions:**  
  - The functions \( f \), \( g \), \( \sigma \), and \( \phi \) are described as nonlinear functions or activation functions, but their specific forms (e.g., sigmoid, tanh, ReLU) are not always clearly defined or exemplified when first introduced. For clarity, the notes should specify typical choices and their roles.

- **Inconsistent use of parameters:**  
  - In Eq. (213), the function \( f \) is parameterized by \( \theta \), and in Eq. (214), \( g \) is parameterized by \( \phi \). Later, in Eq. (217) and (218), parameters are explicitly matrices and biases \( W_a, W_x, W_y, b_a, b_y \). The notes should clarify the relationship between \( \theta, \phi \) and these matrices/vectors to avoid ambiguity.

- **Lack of explicit mention of dimensions in earlier equations:**  
  - Dimensions of vectors and matrices are only introduced in section 12.14. It would be helpful to mention or remind the reader of these dimensions earlier when the equations first appear.

- **Potential confusion in the example of word associations:**  
  - The example states that if word A frequently co-occurs with word B, the connection between their corresponding network units should be strong and positive, and if A appears without B, this implies a negative or weak connection. This is an oversimplification: co-occurrence statistics do not directly translate to positive or negative weights in RNNs, which learn complex representations. The notes should clarify that this is an intuitive analogy rather than a strict rule.

- **Terminology clarification:**  
  - The term "state" is used interchangeably with "hidden state" without explicit clarification. It would be beneficial to define "state" as the hidden representation maintained by the RNN at each time step.

- **Initial hidden state \( h_0 \) treatment:**  
  - The initial hidden state \( h_0 \) is set to zero in Eq. (210) and mentioned as possibly learned or zero in section 12.11. The notes should clarify the implications of these choices and their impact on training.

- **No mention of vanishing/exploding gradients or training challenges:**  
  - While the historical context is given, the notes do not mention common issues with simple RNNs such as vanishing or exploding gradients, which motivated later architectures like LSTM and GRU. Including this would provide a more complete picture.

- **Equation (213) is somewhat abstract:**  
  - The equation \( h_t = f(h_{t-1}, x_t; \theta) \) is abstract and does not specify the functional form. While this is acceptable, a brief explanation or example would help readers understand the transition to the more explicit equations (215) and (217).

- **Typographical issues:**  
  - In section 12.13, the notation "at" is sometimes written without subscripts or with inconsistent spacing (e.g., "at , which in turn produces an output yt ."). Consistent formatting would improve readability.

- **Clarify the difference between \( \sigma \) and \( \phi \):**  
  - The notes mention \( \sigma \) as the activation function for the hidden state and \( \phi \) for the output activation function, but do not clarify when each is used or why different functions are chosen. A brief explanation would be helpful.

- **No explicit mention of the loss function or training objective:**  
  - The notes describe the forward pass but do not mention how the network is trained (e.g., loss functions, backpropagation through time). Including this would complete the mathematical formulation.

Overall, the content is mostly accurate and well-structured but would benefit from clarifications, consistent notation, and additional explanations as noted above.

## Chunk 63/91
- Character range: 404409–411964

```text
Interpretation Equation (229) shows that the current hidden state at is a nonlinear transforma-
tion of the previous hidden state at−1 and the current input xt . Equation (218) maps the hidden
state to the output at time t.

Reusability of the Hidden State The hidden state at serves as a summary of all previous inputs
up to time t. This recursive formulation allows the network to capture temporal dependencies of
arbitrary length.

12.15   Generalized Notation
To simplify notation, define the concatenated input vector at time t:
                                                  
                                              at−1
                                       zt =          ∈ Rh+d .
                                               xt
   Correspondingly, define the combined weight matrix:


                                                147
                                            
                                    W = Wa Wx ∈ Rh×(h+d) .
   Then the hidden state update can be written compactly as:

                                         at = σ (Wzt + ba ) .                                     (219)

12.16    Recurrent Neural Network (RNN) Architectures and Loss Computation
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

Parameter Updates At each time step, the gradient of the loss with respect to parameters (e.g.,
weights W ) depends on the chain of partial derivatives through the network states:

                                           ∂L   X ∂Lt T
                                              =       .                                           (222)
                                           ∂W     ∂W
                                                      t=1

Because of parameter sharing, the same W influences multiple time steps, and the total gradient
is the sum over these contributions.

12.17    RNN Input-Output Configurations
RNNs can be configured in several ways depending on the task:

  • Many-to-Many (Equal Length): Input and output sequences have the same length T .
    For example, sequence labeling tasks.

  • Many-to-One: Input is a sequence of length T , output is a single prediction. Example:
    sentiment analysis where a sentence maps to a sentiment score.



                                                  148
  • Many-to-Many (Unequal Length): Input and output sequences have different lengths.
    Example: machine translation where input and output sentences differ in length.

  • One-to-Many: Single input produces a sequence output. Less common, but applicable in
    tasks like image captioning where one image input generates a sequence of words.

   The main difference lies in how the loss is computed and how outputs are generated, but the
underlying backpropagation principles remain consistent.

12.18    Representing Words for RNN Inputs
Natural language processing (NLP) requires converting words into numerical representations that
RNNs can process. Since machines operate on numbers, words must be encoded appropriately.

Vocabulary Size and Word Representation The English language, for example, has a large
but finite vocabulary. The Oxford English Dictionary lists approximately 273,000 headwords, with
around 171,000 currently in use. Including all inflections and variations, the total number of distinct
word forms can be on the order of one million.
   This finite vocabulary allows us to define a fixed-size dictionary V of words.

One-Hot Encoding A simple method to represent words is one-hot encoding:

  • Assign each word in the vocabulary a unique index i ∈ {1, . . . , |V |}.

  • Represent each word as a vector w ∈ R|V | where all entries are zero except the i-th entry,
    which is 1.

   For example, if |V | = 10, 000, the word ”house” might be represented as:

                                    whouse = [0, 0, . . . , 1, . . . , 0]T ,

with the 1 in the position corresponding to ”house”.
    This representation is sparse and high-dimensional. Conceptually the one-hot basis vectors
correspond to the rows of the identity matrix I|V | , but in practice modern models replace that fixed
basis with a learned embedding table whose rows are trainable parameters:

                                             Wembed = I|V | .

Limitations of One-Hot Encoding One-hot vectors do not capture semantic similarity between
words (e.g., ”king” and ”queen” are orthogonal). Indeed, the cosine similarity between any two
distinct one-hot vectors is exactly zero because their non-zero entries never overlap. They also lead
to very high-dimensional inputs, which can be computationally costly to store and process.
    To address these limitations we introduce distributed word representations (e.g., Word2Vec,
GloVe, fastText) that map words to dense vectors where geometric relationships encode semantic
similarity.




                                                     149
12.19    Example: Sentiment Analysis with RNNs
Consider the sentence:
                                       ”This place is great.”
    Each word is first converted into a numerical vector (e.g., one-hot encoded). The sequence of
vectors is fed into the RNN, which processes them sequentially.
    For a many-to-one RNN (e.g., sentiment classification), we are interested in the hidden state
after processing the entire sentence. This final hidden state summarizes the contextual information
and can be fed into a classifier to predict the sentiment label.

12.20    Limitations of One-Hot Encoding in Natural Language Processing
Recall that one-hot encoding represents each word in the vocabulary as a unique vector with a
single 1 and zeros elsewhere. While this approach guarantees uniqueness, it fails to capture any
semantic or syntactic relationships between words.

Example:     Consider the sentences:

  • “This place is great.”

  • “This place is awesome.”

  • “This place is good.”

Using one-hot encoding, the words great, awesome, and good are represented as orthogonal vectors.
Thus, a model trained to associate “great” with a five-star rating may not generalize to “awesome”
or “good,” despite their similar meanings.

Document similarity: Suppose we have two documents:
```

### Findings
- **Equation references and clarity:**
  - Equation (229) is mentioned at the start but not provided in this chunk. Without seeing it, the claim that the current hidden state is a nonlinear transformation of the previous hidden state and current input is standard but should be explicitly stated or referenced.
  - Equation (218) is referenced as mapping the hidden state to output at time t, but it is not shown here. For completeness, it would be helpful to restate or summarize it.

- **Notation and definitions:**
  - The concatenated input vector \( z_t = \begin{bmatrix} a_{t-1} \\ x_t \end{bmatrix} \in \mathbb{R}^{h+d} \) is well-defined, but the notation \( \begin{bmatrix} a_{t-1} \\ x_t \end{bmatrix} \) should be explicitly stated as vertical concatenation to avoid ambiguity.
  - The combined weight matrix \( W = [W_a \quad W_x] \in \mathbb{R}^{h \times (h+d)} \) is introduced, but the notation \( W = W_a W_x \) in the text is ambiguous or incorrect. It should be clarified that \( W \) is formed by concatenating \( W_a \) and \( W_x \) horizontally, not by matrix multiplication.
  - The bias term \( b_a \) appears in equation (219) but is not explicitly defined in this chunk; it should be introduced clearly.

- **Loss function:**
  - Equation (220) defines the cross-entropy loss as \( L = -\sum_i y_i \log \hat{y}_i \). It should be clarified that \( y_i \) and \( \hat{y}_i \) are components of the true and predicted probability distributions, respectively.
  - The statement "When \( \hat{y} = y \), the loss is zero" is only true if \( y \) is a one-hot vector and \( \hat{y} \) matches it exactly, which is a rare ideal case. This could be nuanced to avoid misunderstanding.

- **Gradient notation:**
  - Equation (222) writes \( \frac{\partial L}{\partial W} = \sum_{t=1}^T \frac{\partial L_t}{\partial W} \), which is correct. However, the notation \( \partial L_t / \partial W \) should be clarified as the gradient of the loss at time \( t \) with respect to parameters \( W \).
  - It would be helpful to mention that the chain rule is applied through time steps due to parameter sharing.

- **RNN input-output configurations:**
  - The four configurations are well described. However, the "One-to-Many" example (image captioning) is somewhat simplified; image captioning typically uses CNNs for image encoding followed by RNNs for sequence generation. This could be noted for completeness.

- **Word representation:**
  - The vocabulary size numbers are informative but could be cited or referenced.
  - The statement \( W_{\text{embed}} = I_{|V|} \) is misleading. While one-hot vectors correspond to rows of the identity matrix, the embedding matrix \( W_{\text{embed}} \) is typically a learned parameter matrix of size \( |V| \times d \), where \( d \) is the embedding dimension, not equal to the identity matrix.
  - The explanation that one-hot vectors are orthogonal and have zero cosine similarity is correct and well stated.
  - The transition to distributed word representations is appropriate but could briefly mention that these embeddings are dense and low-dimensional.

- **Example and limitations:**
  - The sentiment analysis example is clear.
  - The limitation example with "great," "awesome," and "good" is well chosen.
  - The last sentence "Document similarity: Suppose we have two documents:" is incomplete and should be finished or removed.

- **Minor points:**
  - Some formatting issues (e.g., misplaced line breaks, inconsistent spacing) could be cleaned up for readability.
  - The use of bold or italics for key terms (e.g., "One-Hot Encoding") could improve clarity.

**Summary:**  
The chunk is generally accurate and well-structured but would benefit from clarifications on notation (especially matrix concatenation vs multiplication), explicit definitions of variables (bias terms), more precise statements about loss behavior, and correction of the embedding matrix description. The incomplete sentence at the end should be addressed.

## Chunk 64/91
- Character range: 411966–419007

```text
D1 : “I enjoyed talking to the monarchs.”
                             D2 : “I loved conversing with the Royals.”

Semantically, these sentences convey the same meaning. However, one-hot encoding treats monar-
chs and Royals as distinct tokens, as well as talking and conversing. Consequently, simple word-
count based similarity metrics (e.g., cosine similarity on bag-of-words vectors) would yield a low
similarity score, failing to capture the semantic equivalence.

Summary:      One-hot encoding:

  • Ignores semantic similarity between words.

  • Treats synonyms and related words as completely unrelated.

  • Does not capture contextual or syntactic information.

    This motivates the need for richer feature representations of words that encode their mean-
ings and relationships.




                                                150
12.21    Feature-Based Word Representations
To encode the meaning of words, we can represent each word as a vector of features that capture
semantic properties. These features can be handcrafted or learned, and aim to reflect qualities such
as sentiment, category, or other linguistic attributes.

Example:     Consider the following words:

                     man, woman, king, queen, orange, apple, monarch, royal

We can define features such as:
  • Gender: male, female, neutral
  • Royalty status: commoner, royalty
  • Age: adult, child
  • Category: animal, fruit, person, abstract
  • Edibility: edible, inedible
  • Sweetness: sweet, not sweet
   Assigning numerical values to these features for each word yields a vector representation that
encodes semantic information. For example:

         Word        Gender    Royalty   Age    Person   Fruit   Title   Abstract   Sweet
         man           1         0        1       1        0      0         0         0
         woman         0         0        1       1        0      0         0         0
         king          1         1        1       1        0      1         0         0
         queen         0         1        1       1        0      1         0         0
         orange        0         0        0       0        1      0         0         1
         apple         0         0        0       0        1      0         0         1
         monarch      0.5        1       0.5      1        0      1         0         0
         royal         0         1       0.5      0        0      1         1         0

Notes:
  • The values can be binary or continuous, reflecting degrees or uncertainty (e.g., “monarch”
    receives a gender value of 0.5 to indicate that the term is used for multiple genders).
  • High-level categories are often represented with several binary indicators (person, fruit, title,
    abstract) rather than a single categorical feature.
  • Some features may be language- or culture-specific, and this approach requires domain knowl-
    edge and manual feature engineering.

Advantages:
  • Captures semantic similarity: words with similar features have similar representations.
  • Enables reasoning about relationships (e.g., gender, royalty).
  • Provides interpretable dimensions.

                                                151
Limitations:

  • Requires extensive manual effort to define and annotate features.

  • May not scale well to large vocabularies or complex semantics.

  • Diﬀicult to capture contextual nuances and polysemy.

12.22    Towards Distributed Word Representations
The feature-based approach motivates the idea of distributed representations, where each word
is represented as a dense vector in a continuous space. These vectors encode semantic and syntactic
properties implicitly, often learned from large corpora.

Key idea: Instead of one-hot vectors, represent each word w as a vector vw ∈ Rd , where d 
 |V |
(vocabulary size), such that:

                         similarity(vw , vw′ ) ≈ semantic similarity(w, w ′ )

Methods to obtain distributed representations Several approaches learn such embeddings
automatically from corpora, including neural language models (Word2Vec CBOW and Skip-gram),
matrix factorization methods (GloVe), and contextual models (ELMo, BERT). These methods
leverage co-occurrence statistics to place semantically similar words nearby in the embedding space.

12.23    Semantic Relationships in Word Embeddings
We continue our exploration of word embeddings by examining how semantic relationships between
words can be captured in vector space. The key insight, as demonstrated by Mikolov et al. [?],
is that certain linguistic regularities and patterns manifest as linear relationships between word
vectors.

Example: Gender and Royalty Analogies Consider the analogy involving gender and royalty:

                                  king − man + woman ≈ queen.
    This relationship suggests that the vector difference between king and man encodes the concept
of ”royal masculinity,” and adding the vector for woman shifts this to ”royal femininity,” yielding
a vector close to queen.
    More formally, if we denote the embedding of a word w as vw , then the analogy can be expressed
as:

                                 vking − vman + vwoman ≈ vqueen .                             (223)
   This vector arithmetic captures semantic relationships and can be used to find words that best
complete analogies by maximizing cosine similarity:
                                                                   
                             arg max cos vw , vking − vman + vwoman .
                                  w
                      a⊤ b
   Here cos(a, b) = ∥a∥ ∥b∥ denotes cosine similarity between vectors a and b.



                                                 152
Empirical Validation Mikolov et al. showed that these relationships hold not only for gender
and royalty but also for other semantic categories such as family relations (e.g., uncle to aunt),
geographical locations (e.g., Portugal to Lisbon), and cultural concepts. The distances between
word vectors reflect meaningful semantic distances, such as:

                               kvman − vwoman k2 ≈ kvking − vqueen k2 ,
   and similarly for other pairs.

Geographical and Cultural Clustering Word embeddings also often (empirically) capture
geographic and cultural proximity. For example, the embeddings for countries and their capitals
frequently cluster together:

                     vPortugal ≈ vLisbon ,   vSpain ≈ vMadrid ,   vFrance ≈ vParis ,
   and countries that are geographically close tend to have embeddings closer in vector space (e.g.,
China is closer to Russia and Japan than to Portugal), although the strength of this effect depends
on the corpus used for training.

12.24    Feature-Based Representation vs. One-Hot Encoding
The success of word embeddings lies in their ability to represent words as dense vectors encoding
multiple latent features, as opposed to sparse one-hot vectors.

One-Hot Encoding One-hot encoding represents each word as a vector with a single 1 and zeros
elsewhere. This representation is:
```

### Findings
- The initial claim that "semantically, these sentences convey the same meaning" is broadly correct, but it would be more precise to note that the sentences are paraphrases with similar meaning rather than strictly identical semantics, as subtle pragmatic or stylistic differences may exist.

- The explanation of one-hot encoding correctly states that it treats different words as distinct tokens and ignores semantic similarity. However, it would be helpful to explicitly define one-hot encoding before discussing its limitations for clarity.

- The feature-based word representation example is generally well-constructed, but some points need clarification or correction:
  - The "Age" feature is assigned 1 for "man," "woman," "king," and "queen," but 0 for "monarch" and "royal" (0.5). The rationale for these values is not fully explained. For example, "monarch" and "royal" are not age-specific terms, so assigning 0.5 is ambiguous and may confuse readers.
  - The "Person" feature is 1 for "monarch" but 0 for "royal," which is inconsistent because "royal" is an adjective describing people or things related to a monarchy. This inconsistency should be addressed or explained.
  - The "Title" feature is 1 for "king," "queen," "monarch," and "royal," but "royal" is an adjective, not a title. This could be misleading unless "Title" is redefined or renamed.
  - The "Abstract" feature is 1 only for "royal," which is unclear. The term "royal" is not typically considered an abstract noun; it is an adjective. The definition of "Abstract" as a feature should be clarified.
  - The "Sweet" feature is 1 for "orange" and "apple," which is reasonable, but "Sweetness" as a feature is somewhat subjective and may require justification or a more precise definition.

- The note that feature values can be continuous or binary is good, but the example uses mostly binary values with some 0.5 values without clear justification. More explanation on how to assign these values would improve understanding.

- The section on distributed word representations correctly introduces the concept and methods but contains a minor notation inconsistency:
  - The dimension d is said to be "d ≤ |V| (vocabulary size)," but typically d << |V| in practice. The symbol "≤" is used, but it would be clearer to state that d is much smaller than |V|, as embeddings are dense low-dimensional vectors.

- The formula for analogy vector arithmetic is correct, but the notation in the cosine similarity maximization is ambiguous:
  - The expression "arg max cos vw , vking − vman + vwoman" lacks parentheses and subscripts. It should be written as:
    \[
    \arg\max_w \cos\big(v_w, v_{king} - v_{man} + v_{woman}\big)
    \]
  - The definition of cosine similarity is given as "a⊤ b / (∥a∥ ∥b∥)" but the notation "a⊤ b" is not explained. It would be clearer to state that "a⊤ b" denotes the dot product between vectors a and b.

- The empirical validation section states:
  \[
  \|v_{man} - v_{woman}\|_2 \approx \|v_{king} - v_{queen}\|_2
  \]
  This is a useful observation but should be qualified as an empirical trend rather than a strict equality.

- The geographical and cultural clustering examples are appropriate but would benefit from a note that these relationships depend heavily on the training corpus and may not always hold.

- The last section ends abruptly with "One-Hot Encoding One-hot encoding represents each word as a vector with a single 1 and zeros elsewhere. This representation is:" without completing the sentence or listing the properties. This is an incomplete statement and should be finished or removed.

- Minor typographical issues:
  - The phrase "kvman − vwoman k2" uses "k" to denote norm, which is nonstandard; the standard notation is \(\| \cdot \|_2\).
  - The use of quotation marks is inconsistent (e.g., “monarch” vs. ”royal masculinity”).

Overall, the content is scientifically sound but would benefit from clarifications, consistent notation, and completion of unfinished statements.

## Chunk 65/91
- Character range: 419038–425674

```text
• Sparse: High-dimensional with mostly zeros (in the one-hot representation used here, the
    dimensionality equals the vocabulary size and only one entry is non-zero for each word).

  • Uninformative: No notion of similarity between words.

Feature-Based Embeddings In contrast, word embeddings are dense vectors in Rd (typically
d = 100 to 300) where each dimension can be interpreted as a latent feature capturing semantic or
syntactic properties. These features emerge from the training process rather than being explicitly
defined. Unlike the hand-crafted example below, the latent dimensions of distributed embeddings
are not usually interpretable in isolation—they capture statistical regularities uncovered automati-
cally during training. Interpretability can sometimes be probed post hoc (e.g., via probing classifiers
or dimension alignment), but there is no guarantee that any single axis corresponds cleanly to a
human-understandable attribute.

12.25    Open Questions: Feature Discovery and Representation
Two natural questions arise regarding the nature of these features:

  1. Who decides the features? Unlike manually engineered features, the features in word
     embeddings are discovered automatically during training. There is no explicit human selec-
     tion of features such as ”gender” or ”age.” Instead, the training algorithm uncovers latent
     dimensions that best capture word co-occurrence statistics.


                                                  153
  2. How are the feature values determined? The feature values (vector components) are
     learned by optimizing an objective function that encourages words appearing in similar con-
     texts to have similar embeddings. This is typically done via unsupervised or self-supervised
     learning on large corpora. In a self-supervised setting the model creates its own supervision
     signal—future tokens, masked tokens, or neighbouring sentences—so that no external labels
     are required.

Unsupervised Learning of Embeddings Although the learning is often called ”unsupervised,”
it is more accurately described as self-supervised learning because the training objective uses the
structure of the data itself (e.g., predicting context words) as supervision. In self-supervised setups
the model manufactures its own targets from the input (for example, masking a word and asking
the network to predict it), eliminating the need for manually annotated labels.

Summary Thus, the embedding process can be viewed as a function:

                                        f : Vocabulary → Rd ,
    where f is learned to encode semantic and syntactic properties implicitly, without explicit fea-
ture engineering. In matrix form we implement f by selecting the column of the learned embedding
matrix E corresponding to the word of interest.
    In practice we optimize objectives such as the continuous bag-of-words (CBOW) likelihood—
which predicts a center word from its surrounding context—and the skip-gram with negative sam-
pling (SGNS) loss—which predicts surrounding context words given a center word—using stochastic
gradient descent variants (SGD, Adam) on large corpora; these training regimes will be demon-
strated in the accompanying lab (see Section 238 for details).

12.26    Word Embedding via Recurrent Neural Networks
We now discuss the seminal work by Mikolov et al. on feature embedding, which introduced a
powerful approach to learning distributed representations of words from large corpora. The key
insight is to train a recurrent neural network (RNN) to predict the probability distribution of the
next word given the previous words, thereby learning meaningful vector representations of words
as a byproduct.

Input Representation: One-Hot Encoding The input to the RNN is a one-hot encoded
vector representing the current word. Suppose the vocabulary size is V , then each word w is
represented by a vector x ∈ {0, 1}V where exactly one entry is 1 (corresponding to the word’s
index) and the rest are 0. For example, if the word ”king” is the 5th word in the vocabulary, then
x = [0, 0, 0, 0, 1, 0, . . . , 0]T .

Building the Co-occurrence Matrix Before training, one can construct a co-occurrence matrix
C ∈ RV ×V from a large corpus of text. Each entry Cij counts how often word j appears in the
context of word i (in this section we treat the context as the next word after i). For example, if
the corpus consists of only two sentences:

                        ”I like the sky.” and    ”I like the chocolate water.”
   then the vocabulary might be {I, like, the, sky, chocolate, water}, and Clike,the = 2 because the
word “the” follows “like” in both sentences, whereas Csky,I = 0 because “I” never follows “sky.” This

                                                 154
toy illustration uses the immediate successor as the context; production systems usually aggregate
statistics over wider, possibly symmetric windows.
    The co-occurrence matrix can be normalized to obtain conditional probabilities (for the adja-
cency window illustrated here):

                                                          Cij
                                         P (wj | wi ) = P|V |        .                                 (224)
                                                           k=1 Cik
    This probability represents the empirical likelihood of seeing word wj immediately after word wi
                                                         P|V |
under the chosen windowing scheme. The denominator k=1 Cik aggregates the counts of all words
that may follow wi , guaranteeing that the conditional probabilities sum to one. Alternative window
definitions (e.g., symmetric ±n contexts) lead to the same normalization formula but change which
co-occurrences contribute to Cij ; in a symmetric window one typically adds counts for words that
appear within n positions to the left or right of wi , summing across both directions and all offsets
1 ≤ δ ≤ n. Larger windows tend to emphasise topical or semantic similarity, whereas smaller
windows focus more on syntactic relationships.

Training Objective The RNN is trained to predict the next word yt given the current input
xt and the previous hidden state. A simple recurrent language model performs the following
computations:

         et = Ext ,                                       E ∈ Rde ×|V | ,                              (225)
         ht = tanh(Whh ht−1 + Wxh et + bh ),              Whh ∈ Rdh ×dh , Wxh ∈ Rdh ×de ,              (226)
         ŷt = softmax(Who ht + bo ),                     Who ∈ R|V |×dh .                             (227)
```

### Findings
- **Sparse vector definition**: The description of one-hot vectors as "mostly zeros" with dimensionality equal to vocabulary size and exactly one non-zero entry is correct and clear.

- **Uninformative claim about one-hot vectors**: The statement that one-hot vectors have "no notion of similarity between words" is accurate, as one-hot vectors are orthogonal and do not encode semantic relationships.

- **Feature-based embeddings**: The explanation that embeddings are dense vectors in \(\mathbb{R}^d\) with latent features learned automatically is correct. The note that these latent dimensions are usually not interpretable individually is consistent with current understanding.

- **Interpretability caveat**: The mention that interpretability can be probed post hoc but is not guaranteed is a good nuance.

- **Open questions on feature discovery**: The two questions about who decides features and how feature values are determined are well posed and the answers given are accurate.

- **Unsupervised vs self-supervised learning**: The distinction made between unsupervised and self-supervised learning is important and correctly stated. The explanation that self-supervised learning uses the data structure itself as supervision (e.g., masked tokens) is accurate.

- **Summary function \(f: \text{Vocabulary} \to \mathbb{R}^d\)**: This is a clear and correct formalization of the embedding lookup process.

- **Training objectives (CBOW and SGNS)**: The description of CBOW and skip-gram with negative sampling as common objectives is accurate. Mentioning stochastic gradient descent variants (SGD, Adam) is appropriate.

- **RNN-based embedding learning**: The historical note on Mikolov et al.'s work using RNNs to predict next word distributions and learn embeddings as a byproduct is correct.

- **One-hot input representation to RNN**: The explanation of one-hot encoding for input words is precise and the example is clear.

- **Co-occurrence matrix \(C \in \mathbb{R}^{V \times V}\)**: The construction of \(C\) counting how often word \(j\) appears in the context of word \(i\) is standard. The toy example is illustrative.

- **Context window definition**: The note that the example uses immediate successor as context but production systems use wider or symmetric windows is accurate.

- **Normalization to conditional probabilities**: The formula for \(P(w_j | w_i) = \frac{C_{ij}}{\sum_{k=1}^{|V|} C_{ik}}\) is correct. However, the notation in the text is somewhat confusing:

  - The formula is written as:

    \[
    P(w_j | w_i) = \frac{C_{ij}}{\sum_{k=1}^{|V|} C_{ik}}.
    \]

  - But the text shows:

    \[
    P(w_j | w_i) = P|V| \frac{C_{ij}}{k=1 C_{ik}}.
    \]

    This appears to be a formatting or transcription error. The correct formula should be clearly stated as above.

- **Explanation of denominator**: The explanation that the denominator sums counts of all words following \(w_i\) to ensure probabilities sum to one is correct.

- **Window size effects**: The claim that larger windows emphasize topical/semantic similarity and smaller windows emphasize syntactic relationships is consistent with literature.

- **RNN training objective and equations**:

  - Equation (225): \(e_t = E x_t\), where \(E \in \mathbb{R}^{d_e \times |V|}\) is the embedding matrix, is correct.

  - Equation (226): \(h_t = \tanh(W_{hh} h_{t-1} + W_{xh} e_t + b_h)\) with dimensions specified is correct.

  - Equation (227): \(\hat{y}_t = \text{softmax}(W_{ho} h_t + b_o)\) with \(W_{ho} \in \mathbb{R}^{|V| \times d_h}\) is correct.

- **Notation consistency**: The notation is consistent throughout the chunk.

- **Minor issues**:

  - The phrase "feature embedding" in "the seminal work by Mikolov et al. on feature embedding" is somewhat vague; it would be clearer to say "distributed word embeddings" or "word vector representations."

  - The text mentions "Section 238" for lab details, which is presumably a reference within the larger document; no issue if cross-referencing is correct.

- **Summary**: Overall, the chunk is scientifically accurate and well-explained. The only notable issue is the formatting error in the conditional probability formula (Equation 224), which should be corrected for clarity.

---

**Summary of flagged points:**

- The conditional probability formula (Equation 224) is incorrectly formatted and should be clearly written as:

  \[
  P(w_j | w_i) = \frac{C_{ij}}{\sum_{k=1}^{|V|} C_{ik}}.
  \]

- Minor wording suggestion: replace "feature embedding" with "distributed word embeddings" for clarity.

- Otherwise, no scientific or mathematical errors detected.

## Chunk 66/91
- Character range: 425678–432490

```text
Here et is the learned embedding of the current word, ht is the hidden state summarising the
prefix w1 , . . . , wt , and ŷt ∈ R|V | is the predicted distribution over the vocabulary for the next word;
bh ∈ Rdh and bo ∈ R|V | are bias terms. For simplicity we often choose de = dh , but the formulation
above highlights that the embedding and hidden dimensions need not match.
     The training target is the actual next token in the sequence represented as a one-hot vector
yt . Cross-entropy loss between yt and ŷt therefore encourages the model to place high probability
on the observed next word (equivalently, the model maximises the log-likelihood of the observed
sequence). Empirical distributions derived from C (Equation (224)) are useful for analysis and
smoothing, but the baseline RNN language model is trained against the observed next-word labels.
This highlights the distinction between count-based embedding methods (which factorise statistics
such as C) and predictive models like RNN language models that learn embeddings by directly
optimizing next-word prediction.

Dimensionality and Embedding Size The one-hot input vector xt is of dimension V , which
can be very large (e.g., 10,000 or more). To reduce dimensionality and learn meaningful features, the
embedding matrix E ∈ Rde ×V projects the one-hot vector into a dense de -dimensional embedding
space, where de 
 V (e.g., de = 300).
   Since xt is one-hot, the multiplication Ext simply selects the column of E corresponding to
the input word. Thus, each column of E can be interpreted as the learned embedding vector for
a particular word (other texts sometimes store embeddings as rows—that is purely a notational
convention).




                                                    155
Example: Suppose the vocabulary size is V = 10, 000 and embedding dimension de = 300. Then
E is a 300 × 10, 000 matrix. For the word ”king” with one-hot vector xking , the embedding is

                                         eking = Exking ∈ Rde .
    During training, the parameters E, Whh , Wxh , and Who are updated to maximize the likelihood
of the observed sequences, effectively learning embeddings that capture semantic and syntactic
relationships.

Unsupervised Nature of Training This training procedure is unsupervised or self-supervised
because it does not require labeled data. Instead, the model learns from raw text corpora by
predicting the next word, leveraging the natural structure of language. The co-occurrence statistics
are derived directly from the corpus without manual annotation.

Summary - Input words are represented as one-hot vectors. - A co-occurrence matrix captures
empirical next-word probabilities. - The RNN learns to predict the next word distribution given
the current word. - The embedding matrix E maps sparse one-hot vectors to dense de -dimensional
feature vectors. - Training is self-supervised, relying solely on raw text data without manual labels.
    Next, a natural progression is to study the Word2Vec algorithms (Skip-gram and CBOW) that
operationalize these ideas with eﬀicient shallow architectures.

12.27    Wrapping Up the Derivations
In this lecture, we have explored the foundational concepts behind modeling sequences in natural
language processing (NLP) using recurrent neural networks (RNNs). We began by considering the
problem of predicting the probability of a word given its preceding context, which is central to
language modeling.
    Recall that the goal is to estimate the conditional probability of a word wt given the sequence
of previous words w1 , w2 , . . . , wt−1 :

                                       P (wt | w1 , w2 , . . . , wt−1 ).                          (228)

   This probability can be modeled using an RNN, which maintains a hidden state ht that sum-
marizes the history up to time t:

                                                        ht = f (ht−1 , xt ; θ),                   (229)
                                P (wt | w1 , . . . , wt−1 ) = g(ht−1 ; θ),                        (230)

where xt is the input representation (e.g., word embedding) of the word wt , f is the recurrent
update function parameterized by θ, and g maps the hidden state to a probability distribution
over the vocabulary. Because the hidden state is computed recursively, ht−1 already aggregates
information about the entire prefix (w1 , . . . , wt−1 ); predicting wt from ht−1 therefore reflects the
Markovian summary that RNNs maintain.

Training Objective The network is trained to maximize the likelihood of the observed sequences
in a large corpus of text. Given a training sequence (w1 , w2 , . . . , wT ), the log-likelihood is:

                                         X
                                         T
                                L(θ) =         log P (wt | w1 , . . . , wt−1 ; θ).                (231)
                                         t=1


                                                      156
   This objective encourages the model to assign high probability to the actual next word in the
sequence, effectively learning the statistical structure of the language without explicit labeling of
word relationships.

Unsupervised Nature of Language Modeling A key insight is that no explicit labeling is
required to train such models. The natural co-occurrence statistics of words in large corpora serve
as implicit supervision. For example, the model learns that the word ”juice” often follows ”apple”
because this pattern frequently appears in the training data. This is the essence of unsupervised
(more precisely, self-supervised) learning in NLP, where the prediction targets are created directly
from the input sequence.

Feature Representations The input to the RNN is typically a dense vector representation of
words, known as word embeddings. These embeddings capture semantic and syntactic properties of
words and are learned jointly with the model parameters. The embedding matrix E ∈ RV ×d , where
V is the vocabulary size and d is the embedding dimension, maps each word index to a vector:
We denote by ewt the one-hot indicator of word wt . The embedding lookup can then be written
compactly as
                                          x t = E ⊤ ew t ,                                (232)
so E[wt ] simply selects the row of E associated with wt .

Summary of the Modeling Pipeline

  1. Collect a large corpus of text data.

  2. Tokenize the text into sequences of words.

  3. Represent words as embeddings (initialized from a lookup table that is learned jointly with
     the network parameters).

  4. Use an RNN to process sequences and produce hidden states.

  5. Predict the next word probability distribution from the hidden state.

  6. Train the model by maximizing the likelihood of the observed sequences.
```

### Findings
- **Inconsistent notation for embedding matrix dimensions:**
  - Early in the text, the embedding matrix \( E \) is described as \( E \in \mathbb{R}^{d_e \times V} \) (embedding dimension by vocabulary size), with embeddings as columns.
  - Later, the embedding matrix is given as \( E \in \mathbb{R}^{V \times d} \) (vocabulary size by embedding dimension), with embeddings as rows.
  - This switch in notation is confusing and should be clarified or made consistent. The text notes that storing embeddings as rows or columns is a notational convention, but the change within the same chunk without explicit clarification can cause ambiguity.

- **Ambiguity in embedding lookup notation:**
  - The embedding lookup is described as \( e_t = E x_t \) when \( E \in \mathbb{R}^{d_e \times V} \) and \( x_t \) is one-hot \( \in \mathbb{R}^V \), which selects a column.
  - Later, the embedding lookup is written as \( x_t = E^\top e_{w_t} \), where \( e_{w_t} \) is one-hot and \( E \in \mathbb{R}^{V \times d} \), selecting a row.
  - The notation \( e_{w_t} \) is introduced without explicitly defining it as a one-hot vector, which could confuse readers.
  - The use of \( x_t \) for both the one-hot input vector and the embedding vector in different contexts is potentially ambiguous.

- **Minor typographical issues:**
  - The symbol "
" appears in "where \( d_e \ll V \) (e.g., \( d_e = 300 \))" but is rendered as a non-standard character; it should be the "much less than" symbol \( \ll \).
  - The phrase "eﬀicient" contains a ligature character that may not render properly in all contexts.

- **Lack of explicit definitions:**
  - The function \( f \) (recurrent update) and \( g \) (output mapping) are introduced but not explicitly defined or exemplified (e.g., \( f \) could be an LSTM or GRU cell, \( g \) a softmax layer).
  - The one-hot vector \( y_t \) is mentioned as the training target but not explicitly defined as a vector with a single 1 at the index of the true next word and zeros elsewhere.

- **Potential confusion in the description of co-occurrence matrix \( C \):**
  - The text references Equation (224) for the co-occurrence matrix \( C \) but does not restate or summarize it here.
  - It states that empirical distributions derived from \( C \) are useful for analysis and smoothing but that the RNN is trained against observed next-word labels.
  - This distinction is important but could be better emphasized or explained, especially for readers unfamiliar with count-based vs. predictive embedding methods.

- **Terminology precision:**
  - The term "unsupervised" is used but then qualified as "more precisely, self-supervised." This is good, but the text could clarify that language modeling is a form of self-supervised learning where supervision comes from the data itself.

- **Summary bullet points:**
  - The summary points are generally accurate but could be improved by explicitly stating that the RNN predicts the next word distribution conditioned on the entire prefix, not just the current word.

- **Equation (230) indexing inconsistency:**
  - Equation (230) writes \( P(w_t | w_1, \ldots, w_{t-1}) = g(h_{t-1}; \theta) \), which is correct.
  - However, the text sometimes refers to \( h_t \) as summarizing prefix \( w_1, \ldots, w_t \), which could confuse readers about whether the prediction uses \( h_t \) or \( h_{t-1} \).
  - It would be clearer to consistently state that \( h_{t-1} \) summarizes the prefix up to \( w_{t-1} \), and the prediction for \( w_t \) is made from \( h_{t-1} \).

- **Notation for the one-hot vector of the current word:**
  - The notation \( e_{w_t} \) is used for the one-hot vector of word \( w_t \) without explicit definition.
  - It would be clearer to define \( e_{w_t} \in \mathbb{R}^V \) as the one-hot vector with 1 at the index corresponding to \( w_t \).

- **Clarification on training parameters:**
  - The text mentions parameters \( E, W_{hh}, W_{xh}, W_{ho} \) but does not define \( W_{ho} \) explicitly (presumably the output weight matrix).
  - A brief description of each parameter's role would improve clarity.

Overall, the content is scientifically sound but would benefit from consistent notation, explicit definitions, and clearer explanations of key concepts.

## Chunk 67/91
- Character range: 432492–439543

```text
Summary
In this final lecture segment, we have completed the derivation and conceptual understanding of
language modeling using recurrent neural networks. We emphasized the unsupervised nature of
training, where the model learns to predict the next word based solely on the natural statistics of
language data, without explicit labels. The RNN hidden states serve as dynamic representations
of the preceding context, enabling the model to capture complex dependencies in sequences. This
framework underpins many modern NLP applications, from text generation to machine translation.

References
  • Jurafsky, D., & Martin, J. H. (2023). Speech and Language Processing (3rd ed.). Draft
    chapters available online.

  • Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.

                                                 157
  • Mikolov, T., Karafiát, M., Burget, L., Černocký, J., & Khudanpur, S. (2010). Recurrent
    neural network based language model. Interspeech.

   Suggested reading: Chapter 10 of Goodfellow, Bengio, and Courville (2016) for RNN funda-
mentals and Mikolov et al. (2013) for the original Word2Vec formulation.


13 Lecture 8 Part I: Neural Network Applications in Natural Lan-
   guage Processing
13.1    Context and Motivation
In this lecture, we conclude our discussion on neural networks by focusing on their applications in
natural language processing (NLP). Last week, we introduced the concept of representing words
as inputs to a neural network, typically encoded as one-hot vectors, and obtaining as output a
feature representation of these words. This feature representation captures semantic and syntactic
properties of words in a continuous vector space.
    A classic example illustrating the power of such representations is the analogy:

                                  king − man + woman ≈ queen.

This demonstrates that vector arithmetic on word embeddings can capture meaningful relationships
between words. The goal is to find a vector space embedding where semantic similarity corresponds
to geometric closeness.

13.2    Problem Statement
Given a vocabulary (corpus) of approximately 10,000 words, we want to learn a mapping from
each word to a dense vector representation in a feature space of dimension d, where d is typically
between 200 and 500. Formally, if the vocabulary size is V , each word wi is initially represented as
a one-hot vector xi ∈ RV , where            (
                                              1 if j = i,
                                      xij =
                                              0 otherwise.
Here the row index i selects the word and the column index j specifies the position within the
V -dimensional one-hot vector, so each word is associated with a unique canonical basis vector. Our
objective is to learn an embedding function

                                       f : {1, . . . , V } → Rd ,

such that semantic and syntactic properties of words are preserved in the embedding space.

13.3    Key Insight: Distributional Hypothesis
The foundational linguistic principle underlying word embeddings is the distributional hypothesis,
often summarized by the phrase:

       You shall know a word by the company it keeps.

This idea, attributed to the linguist John Robert Firth, states that the meaning of a word can be
inferred from the contexts in which it appears.


                                                 158
Example:      The word pretty can have different meanings depending on context:

   • In “pretty good,” pretty means “very” (an intensifier).

   • In “pretty optics,” pretty means “beautiful.”

By examining the surrounding words (context), we can infer the intended meaning.

13.4     Contextual Meaning and Feature Extraction
Words appear in many different contexts, and by aggregating information from these contexts, we
can infer intrinsic features of the word. For example, the contexts in which pretty appears with
good or image help us understand its different senses.
   This motivates the use of statistical models that learn word embeddings by analyzing large
corpora and capturing co-occurrence patterns.

13.5     Word2Vec: Two Architectures
The Word2Vec framework, introduced by Mikolov et al., operationalizes the distributional hypoth-
esis through two main architectures:

   1. Continuous Bag of Words (CBOW): Predicts the target word given its surrounding
      context words.

   2. Skip-Gram: Predicts the surrounding context words given the target word.

   Both architectures learn word embeddings as a byproduct of solving these prediction tasks.

13.5.1    Continuous Bag of Words (CBOW)
In CBOW, the model takes as input the context words surrounding a target word and tries to
predict the target word itself. Formally, given a sequence of words {w1 , w2 , . . . , wT }, and a context
window size n, the context for word wt is

                                Ct = {wt−n , . . . , wt−1 , wt+1 , . . . , wt+n }.

   The CBOW model maximizes the probability

                                                  p(wt | Ct ),

where the context words Ct are represented as one-hot vectors and combined (e.g., averaged) to
form the input.

Example:      Consider the sentence

                                       “to buy an automatic car”.

If we want to learn the embedding for the word automatic, the context might be {to, buy, an, car}.
The CBOW model uses these context words to predict automatic.




                                                      159
13.5.2    Skip-Gram
Conversely, the Skip-Gram model takes the target word as input and tries to predict each of the
context words. It maximizes            Y
                                            p(wc | wt ).
                                        wc ∈Ct

    This approach tends to perform better on infrequent words and captures more detailed semantic
relationships.

13.6     Mathematical Formulation of CBOW
Let the vocabulary size be V , and embedding dimension be d. Define the embedding matrix
W ∈ RV ×d , where the i-th row wi is the embedding vector for word wi .

13.7     Neural Network Architecture for Word Embeddings
Consider a corpus with vocabulary size V = 10, 000 words. Our goal is to learn a dense vector
representation (embedding) for each word in this vocabulary. We denote the dimensionality of the
embedding space as d = 300.

Input Representation Each input word is represented as a one-hot vector x ∈ RV , where only
one element is 1 (corresponding to the word index) and the rest are 0. For example, if the word
”want” is the i-th word in the vocabulary, then xi = 1 and xj = 0 for j 6= i.

Network Structure We consider a simple feedforward neural network with:

  • An input layer of size V (one-hot encoded words).

  • A hidden layer of size d = 300, which will serve as the embedding layer.

  • An output layer of size V , which predicts the target word.

   The weight matrix between the input and hidden layer is denoted as

                                          W ∈ RV ×d .
```

### Findings
- **Notation inconsistency in embedding matrix W**:  
  - In section 13.6, the embedding matrix \( W \in \mathbb{R}^{V \times d} \) is defined with the i-th row \( w_i \) as the embedding vector for word \( w_i \). This is consistent with the usual convention where each row corresponds to a word embedding.  
  - However, in the last paragraph, the weight matrix between input and hidden layer is again denoted as \( W \in \mathbb{R}^{V \times d} \), which is consistent, but the text does not explicitly clarify that the embedding vector for a word is obtained by selecting the corresponding row of \( W \). This could be made explicit for clarity.

- **Ambiguity in CBOW input representation**:  
  - The CBOW model input is described as the context words represented as one-hot vectors and combined (e.g., averaged) to form the input. It would be clearer to specify that the input to the network is the average (or sum) of the embeddings of the context words, not the average of the one-hot vectors themselves. Averaging one-hot vectors would produce a vector with fractional entries, which is not a valid one-hot vector. The embedding lookup and averaging happen after mapping one-hot vectors to embeddings.

- **Missing definition of the output layer weights**:  
  - The architecture mentions an output layer of size \( V \) predicting the target word, but does not specify the weight matrix from hidden to output layer (usually denoted \( W' \in \mathbb{R}^{d \times V} \)) or the use of softmax for prediction. Including this would complete the description.

- **Lack of explicit loss function**:  
  - The lecture notes mention maximizing probabilities \( p(w_t | C_t) \) for CBOW and \( \prod_{w_c \in C_t} p(w_c | w_t) \) for Skip-Gram, but do not explicitly state the loss function used (e.g., negative log-likelihood or cross-entropy loss). Adding this would improve mathematical rigor.

- **Inconsistent use of notation for word indices and vectors**:  
  - The notation \( w_i \) is used both for the i-th word and for the embedding vector of the i-th word, which could cause confusion. It would be better to distinguish between the word as a symbol and its embedding vector, e.g., \( w_i \) for the word and \( \mathbf{v}_i \) or \( \mathbf{w}_i \) for its embedding.

- **Unclear explanation of Skip-Gram probability product**:  
  - The Skip-Gram model maximizes \( \prod_{w_c \in C_t} p(w_c | w_t) \), but the text does not clarify whether this is done independently for each context word or jointly. It would be helpful to mention that the model assumes conditional independence of context words given the target word.

- **Missing mention of negative sampling or hierarchical softmax**:  
  - The Word2Vec models typically use approximations like negative sampling or hierarchical softmax to efficiently compute probabilities over large vocabularies. These are not mentioned, which might leave the reader wondering about computational feasibility.

- **Typographical issues**:  
  - In the formula for the one-hot vector \( x_{ij} \), the parentheses are not properly closed or aligned, which could confuse readers.  
  - The phrase "Y p(w_c | w_t)" in the Skip-Gram section appears to be a product symbol but is not clearly formatted.

- **Minor suggestion on example clarity**:  
  - The example "pretty optics" is somewhat unusual; "pretty" as an intensifier is common, but "pretty optics" is less standard. A more common example might improve clarity.

Overall, the content is mostly accurate but would benefit from clarifications and more precise mathematical definitions.
