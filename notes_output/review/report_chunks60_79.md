# Scientific QA Report

- Source PDF: `notes_output/ece657_notes.pdf`
- Total chunks: 20

## Chunk 60/104
- Character range: 384129–391455

```text
Example: Memory Recovery Consider a Hopfield network with N = 4 neurons and a single
stored pattern ξ = [−1, −1, 1, −1]T . The weight matrix constructed via (10.18) is

                                          1
                                       W = ξξ ⊤ ,           wii = 0,
                                          4

                                                  143
Intelligent Systems and Soft Computing                   Hopfield Networks: Introduction and Context


which numerically becomes a single symmetric matrix
                                                 
                                         0 1 −1 1
                                     11  0 −1 1 
                                                  
                                   W=            .
                                     4 −1 −1 0 −1
                                        1  1 −1 0

The off-diagonal entries are therefore the scaled products of pattern components (e.g., w12 = w21 =
0.25 and w13 = w31 = −0.25). Thus every off-diagonal weight is simply the scaled product of the
corresponding pattern entries, e.g., w12 = w21 = 0.25, w13 = w31 = −0.25, and so on.
    Starting from an initial state s(0) = [−1, −1, 1, 1]T (with zero thresholds θi = 0), we apply the
familiar asynchronous sign update

                                                 X
                                                  N                   
                                     si ← sign          wij sj − θi
                                                  j=1

one neuron at a time—i.e., neuron i is set to +1 whenever the weighted sum exceeds its threshold and
                                                                                 P PN
to −1 otherwise. Because each update reduces the Lyapunov energy E = − 12 N              j=1 wij si sj +
PN                                                                                 i=1
  i=1 θi si from (10.11), the trajectory converges to ξ or its complement −ξ, demonstrating successful
memory retrieval despite the initial corruption. The appearance of −ξ as a fixed point is expected:
the energy only depends on products si sj , so negating all bits leaves every term unchanged.

Spurious attractors Beyond the intended memories {±ξ µ }, Hopfield networks can converge to
spurious attractors: stable states formed by mixtures of stored patterns. These unintended minima
become increasingly common as the loading factor P/N grows (here P denotes the number of
stored patterns); for random patterns the practical capacity is roughly 0.138 N . The possibility of
converging to a spurious state, or to the complemented memory rather than the original, explains
why Hopfield networks are better viewed as associative memories than as discriminative classifiers.

Historical and Practical Significance The Hopfield network was revolutionary in demonstrat-
ing that artificial neural networks can model associative memory and converge to stable states cor-
responding to stored memories. It laid foundational concepts for energy-based models and inspired
subsequent developments in neural computation.
    However, its practical use is limited by low storage capacity and sensitivity to noise. Modern
networks and learning algorithms have since extended these ideas to more scalable and robust
architectures.

Summary
  • The Hopfield network stores binary patterns as attractors of a dynamical system defined by
    symmetric weights learned via Hebbian rule.

  • The network dynamics minimize an energy function, ensuring convergence to stable states
    corresponding to stored memories or their complements.


                                                 144
Intelligent Systems and Soft Computing       Introduction to Deep Learning and Neural Networks


  • Memory retrieval is robust to moderate noise, but the network suffers from limited capacity
    and spurious attractors.

  • Hopfield networks are not suitable for classification tasks due to ambiguous convergence be-
    havior on corrupted inputs.

  • Despite limitations, Hopfield networks were seminal in linking neural networks to associative
    memory and energy-based models.

References
  • J. J. Hopfield, “Neural networks and physical systems with emergent collective computational
    abilities,” Proceedings of the National Academy of Sciences, vol. 79, no. 8, pp. 2554–2558,
    1982.

  • D. Amit, H. Gutfreund, and H. Sompolinsky, “Storing infinite numbers of patterns in a spin-
    glass model of neural networks,” Physical Review Letters, vol. 55, no. 14, pp. 1530–1533,
    1985.


11     Introduction to Deep Learning and Neural Networks
In this chapter, we begin our exploration of deep learning, a subfield of machine learning that
has gained tremendous popularity and success in recent years. Deep learning models, particularly
deep neural networks, have revolutionized many areas such as computer vision, natural language
processing, and speech recognition.

11.1   Historical Context and Motivation
Artificial neural networks (ANNs) have a long history dating back to the 1940s, with the seminal
work of McCulloch and Pitts in 1943. Despite this early start, it took several decades before
deep learning models became widely successful and practical. Neural networks experienced waves
of interest, notably in the 1980s and 1990s, but it was only in the last 10-15 years that deep
architectures have become dominant.
    Understanding why deep learning took so long to mature is crucial. Several challenges hindered
progress for many years:
  • Optimization hurdles: Early neural networks were shallow (few layers) and suffered from
    problems such as vanishing or exploding gradients, making it hard to train deep models
    effectively.

  • Computational resources: Deep networks require significant computational power and
    memory, which were not readily available until recent advances in hardware (e.g., GPUs).

  • Data availability: Large labeled datasets, essential for training deep models, were scarce
    until the advent of big data.

  • Algorithmic improvements: Innovations such as better activation functions, initialization
    schemes, and optimization algorithms were necessary to enable deep learning.


                                               145
Intelligent Systems and Soft Computing          Introduction to Deep Learning and Neural Networks


   These factors combined to delay the widespread adoption of deep learning despite its theoretical
potential.

11.2     Overview of Neural Network Architectures
Before delving into deep learning, it is important to review the basic building blocks of neural
networks.

11.2.1    Feedforward Neural Networks (Multi-Layer Perceptrons)
A feedforward neural network consists of an input layer, one or more hidden layers, and an output
layer. Data flows in one direction from input to output without cycles.
    Consider a simple network with an input layer of dimension d and a single hidden layer with h
neurons. The input vector is denoted by

                                       x = [x1 , x2 , . . . , xd ]T ,

and the weight matrix connecting the input to the hidden layer is

                                             W ∈ Rh×d .

   The pre-activation input to the hidden layer neurons is
```

### Findings
- **Notation and formatting issues in the weight matrix W:**
  - The matrix W is defined as \( W = \frac{1}{N} \xi \xi^\top \) with \( w_{ii} = 0 \). This is correct for the Hebbian learning rule in Hopfield networks.
  - However, the matrix shown is not clearly formatted. The matrix should be explicitly written as:
    \[
    W = \frac{1}{4}
    \begin{pmatrix}
    0 & 1 & -1 & 1 \\
    1 & 0 & -1 & 1 \\
    -1 & -1 & 0 & -1 \\
    1 & 1 & -1 & 0
    \end{pmatrix}
    \]
    The current formatting is confusing and inconsistent (e.g., the placement of the scalar 1/4 and the matrix entries).
  - The text mentions \( w_{12} = w_{21} = 0.25 \) and \( w_{13} = w_{31} = -0.25 \), which is consistent with the formula, but the matrix entries shown are integers (1, -1) rather than the scaled values (0.25, -0.25). This inconsistency should be clarified.

- **Ambiguity in the update rule notation:**
  - The asynchronous update rule is given as:
    \[
    s_i \leftarrow \text{sign}\left(\sum_{j=1}^N w_{ij} s_j - \theta_i\right)
    \]
    but the formula is shown with some unusual symbols (e.g., "X", "") which appear to be formatting artifacts or errors.
  - The summation index and limits should be clearly stated, and the notation should be consistent and free of extraneous characters.

- **Energy function expression:**
  - The energy function is given as:
    \[
    E = -\frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N w_{ij} s_i s_j + \sum_{i=1}^N \theta_i s_i
    \]
    but in the text, the summations and indices are somewhat jumbled and hard to parse.
  - The factor of 1/2 is correctly included to avoid double counting, but the notation should be cleaned up for clarity.
  - It would be helpful to explicitly state that \( w_{ii} = 0 \) to avoid confusion about self-connections.

- **Complemented pattern as a fixed point:**
  - The text correctly states that the complement \(-\xi\) is also a fixed point because the energy depends on products \( s_i s_j \).
  - However, it would be beneficial to mention that this is a consequence of the symmetric weights and zero thresholds, and that the network dynamics are invariant under global sign flips.

- **Spurious attractors and capacity:**
  - The capacity estimate of approximately \(0.138 N\) for random patterns is correct and well-known.
  - The explanation that spurious attractors arise as mixtures of stored patterns is accurate.
  - It might be useful to briefly define what is meant by "loading factor" \( P/N \) for completeness.

- **Summary points:**
  - The summary is accurate and well-stated.
  - The claim that Hopfield networks are not suitable for classification tasks due to ambiguous convergence is valid.
  - The historical and practical significance section is concise and correct.

- **References:**
  - The references cited are appropriate and seminal works in the field.

- **Transition to next chapter:**
  - The transition to deep learning is smooth and the historical context is well summarized.
  - No issues in the introductory paragraphs on deep learning.

**Overall, the main issues are:**
- Formatting and clarity of the weight matrix and energy function expressions.
- Presence of formatting artifacts in the update rule.
- Minor missing definitions (e.g., loading factor).
- Slight inconsistency in showing scaled weights explicitly in the matrix.

No fundamental scientific errors are present, but improved clarity and notation consistency are needed.

## Chunk 61/104
- Character range: 391457–399075

```text
z = Wx + b,                                      (11.1)

where b ∈ Rh is the bias vector.
   Applying a nonlinear activation function σ(·) element-wise yields the hidden layer output

                                               h = σ(z).

    The output layer then produces the final output, often via another linear transformation and
activation.

Fully Connected Layers and Feature Transformation Each neuron in the hidden layer is
connected to every input feature, making the layer fully connected. The weights W serve two main
purposes:
  • Feature extraction: Each neuron computes a weighted combination of input features, ef-
    fectively extracting new features.

  • Attenuation of irrelevant inputs: Weights with small magnitude suppress the contri-
    bution of certain input features, although genuine feature selection usually requires explicit
    regularization (e.g., L1 penalties) or pruning.
    Thus, each layer transforms the input features into a new representation, which subsequent
layers can further process.




                                                   146
Intelligent Systems and Soft Computing         Introduction to Deep Learning and Neural Networks


11.3   Why Shallow Networks Are Insuﬀicient
In theory, shallow networks with a single hidden layer are universal function approximators (Cy-
benko, 1989). However, in practice, they have several limitations:
  • Large number of neurons required: To approximate complex functions, shallow networks
    often need exponentially many neurons.

  • Overfitting: Large networks with many parameters tend to overfit training data, especially
    with limited data.

  • Limited expressivity: Although universal approximators, shallow networks often require
    exponentially many neurons to capture rich structure, so depth provides a far more parameter-
    eﬀicient representation.
    Deep networks, with multiple hidden layers, can represent complex functions more compactly
by learning hierarchical feature representations. This hierarchical structure is key to the success of
deep learning.

11.4   Training Neural Networks: Gradient-Based Optimization
Training neural networks involves minimizing a loss function L that measures the discrepancy
between the network output and the target. The parameters (weights and biases) are updated
iteratively using gradient descent or its variants.
    For a weight w, the update rule is

                                                       ∂L
                                           w ←w−η         ,                                     (11.2)
                                                       ∂w
where η is the learning rate.

                                                                   ∂L
Backpropagation and Gradient Computation The gradient ∂w              is computed eﬀiciently using
the backpropagation algorithm, which applies the chain rule to propagate errors backward through
the network layers.

Challenges in Deep Networks In deep networks, gradients can vanish or explode as they
propagate through many layers, making training unstable or slow. This problem was a major
obstacle until solutions such as better activation functions (e.g., ReLU), normalization techniques,
and initialization methods were developed.

11.5   Deep Network Optimization Challenges
11.6   Vanishing and Exploding Gradients in Deep Networks
Recall from the previous discussion that when training deep neural networks, the backpropagation
algorithm involves repeated multiplication of gradients through many layers. This repeated multi-
plication can cause gradients to either vanish (approach zero) or explode (grow exponentially large),
leading to significant training diﬀiculties.



                                                 147
Intelligent Systems and Soft Computing          Introduction to Deep Learning and Neural Networks


Mathematical intuition Consider a deep network with L layers. Let δW(ℓ) = ∇W(ℓ) L denote
the gradient of the loss with respect to the weights at layer ℓ. If we assume the weights are
initialized identically and the derivative of the activation function is approximately constant, then
the gradient at the first layer can be expressed schematically as:
                                                                    
                       δW(1) ≈ W (2) D(2) W (3) D(3) · · · W (L) D(L) δW(L) ,                  (11.3)

where W represents the weight matrix and f ′ is the derivative of the activation function.
                                                                                                       
    Here W (ℓ) denotes the weight matrix connecting layers ℓ − 1 and ℓ, while D(ℓ) = diag f ′ (z (ℓ) )
collects the activation derivatives at layer ℓ. The product therefore chains together Jacobians from
layers 2 through L. If the spectral norm (largest singular value) of each factor W (ℓ) D(ℓ) exceeds
one, then kδW(1) k grows exponentially with L, causing exploding gradients. Conversely, norms
less than one cause kδW(1) k to shrink exponentially, leading to vanishing gradients.

Consequences
   • Exploding gradients: The gradient values become extremely large, causing numerical in-
     stability and making the network parameters diverge during training.

   • Vanishing gradients: The gradient values approach zero, especially in early layers, prevent-
     ing those weights from updating effectively. This stalls learning in the initial layers, limiting
     the network’s ability to learn hierarchical features.

Example: Activation function derivatives Consider the sigmoid activation function σ(x) =
  1
1+e−x
      . Its derivative is:
                               σ ′ (x) = σ(x)(1 − σ(x)).

Note that σ ′ (x) approaches zero when σ(x) is near 0 or 1, i.e., when the neuron output saturates.
This saturation leads to very small gradients, exacerbating the vanishing gradient problem.

11.7    Strategies to Mitigate Vanishing and Exploding Gradients
Weight initialization Initializing weights carefully can help maintain gradient magnitudes
within a reasonable range. Set var ≈ 1/n (fan‑in n).
This stabilizes signals across layers. It underlies Xavier and He.

Choice of activation function        Selecting activation functions whose derivatives do not vanish
easily is crucial. For example:
   • ReLU (Rectified Linear Unit): Defined as

                                           ReLU(x) = max(0, x),

       its derivative is 1 for positive inputs and 0 otherwise. This avoids saturation in the positive
       regime and helps maintain gradient flow.



                                                  148
Intelligent Systems and Soft Computing         Introduction to Deep Learning and Neural Networks


  • Leaky ReLU and variants: These allow a small, non-zero gradient when the input is
    negative, further mitigating dead neurons and keeping derivatives away from exact zero.

Batch normalization Batch normalization normalizes layer inputs during training, reducing the
effective internal covariate shift and helping gradients maintain stable magnitudes.

Gradient clipping For exploding gradients, gradient clipping limits the maximum gradient norm
during backpropagation, preventing excessively large updates.

11.8   Limitations of Traditional Feedforward Neural Networks
Requirement for large datasets Feedforward networks typically require large amounts of la-
beled data to generalize well. For small datasets (e.g., Titanic survival data, movie ratings), simpler
models like logistic regression or decision trees may outperform neural networks due to overfitting
risks.
```

### Findings
- **Equation (11.1) and notation:**
  - The equation \( z = Wx + b \) is standard for a fully connected layer. However, the dimension of \( b \) is given as \( b \in \mathbb{R}^h \), but \( h \) is not explicitly defined here. It would be clearer to state that \( h \) is the number of neurons in the hidden layer.
  - The notation \( \sigma(\cdot) \) is introduced as a nonlinear activation function applied element-wise, which is correct, but it would be helpful to explicitly state that \( \sigma \) acts element-wise on the vector \( z \).

- **Feature extraction and attenuation:**
  - The claim that weights with small magnitude "suppress the contribution of certain input features" is generally true, but it should be clarified that this is a soft form of feature selection and does not guarantee true feature elimination without explicit regularization or pruning.
  - The note about explicit regularization (e.g., L1 penalties) or pruning is appropriate and well-placed.

- **Section 11.3 on shallow networks:**
  - The statement that shallow networks "often need exponentially many neurons" to approximate complex functions is a common heuristic but could be more precise. The exponential growth depends on the function class and input dimension; this should be qualified.
  - The term "limited expressivity" is used but could be better defined or referenced, as shallow networks are universal approximators but may be inefficient in parameter usage.
  - The phrase "depth provides a far more parameter-efficient representation" is correct but would benefit from a citation or example illustrating this efficiency.

- **Equation (11.2) and gradient descent:**
  - The update rule \( w \leftarrow w - \eta \frac{\partial L}{\partial w} \) is standard and correctly presented.
  - It would be helpful to mention that \( \eta \) (learning rate) is a hyperparameter that controls the step size.

- **Backpropagation and gradient computation:**
  - The explanation is concise and accurate.
  - The term "chain rule" is used correctly but could be expanded slightly for clarity, e.g., "applying the chain rule of calculus to compute gradients layer by layer."

- **Vanishing and exploding gradients (Section 11.6):**
  - The schematic expression for \( \delta W^{(1)} \) in equation (11.3) is conceptually correct but somewhat informal. The notation \( W^{(\ell)} D^{(\ell)} \) should be clarified as the product of the weight matrix and a diagonal matrix of activation derivatives.
  - The assumption that weights are "initialized identically" is ambiguous. It likely means "initialized with identical distributions" or "independently and identically distributed (i.i.d.)" rather than literally identical values.
  - The explanation of spectral norm and its effect on gradient magnitude is correct and well-stated.
  - The notation \( k \delta W^{(1)} k \) presumably denotes a norm (likely Euclidean or spectral norm), but this should be explicitly stated.

- **Activation function derivative example:**
  - The sigmoid function and its derivative are correctly given.
  - The explanation of saturation and its effect on gradients is accurate.

- **Strategies to mitigate vanishing/exploding gradients:**
  - The variance initialization rule "Set var ≈ 1/n (fan-in n)" is correct but could be more precise by referencing Xavier (Glorot) or He initialization formulas explicitly.
  - The description of ReLU and its derivative is accurate.
  - The mention of Leaky ReLU and variants is appropriate; however, the term "dead neurons" could be briefly defined for clarity.
  - Batch normalization is described correctly but the phrase "reducing the effective internal covariate shift" is somewhat outdated; recent literature questions this explanation, so a more neutral phrasing like "stabilizing layer input distributions" might be better.
  - Gradient clipping is correctly described.

- **Limitations of traditional feedforward networks:**
  - The claim that feedforward networks require large labeled datasets is accurate.
  - The examples (Titanic survival data, movie ratings) are appropriate.
  - The suggestion that simpler models may outperform neural networks on small datasets due to overfitting risk is valid.

**Summary:**
- Mostly accurate and well-explained.
- Minor clarifications needed on notation, assumptions (e.g., weight initialization), and some terminology.
- Some statements could be more precise or supported with references.
- The explanation of batch normalization could be updated to reflect current understanding.

No major scientific errors detected.

## Chunk 62/104
- Character range: 399121–406235

```text
High-dimensional inputs and flattening Consider image data, which is naturally represented
as a 2D matrix (or 3D tensor for color images). For example, a single-channel (grayscale) image of
size 256 × 276 pixels can be represented as a matrix:

                                           X ∈ R256×276 .

   To input this into a traditional feedforward network, the image must be flattened into a vector:

                                        x = vec(X) ∈ R70,656 ,

where 70, 656 = 256 × 276 is the total number of pixels.
   This flattening process has two major drawbacks:
  • Loss of spatial structure: The 2D spatial relationships between pixels are ignored, which
    is critical for tasks like image recognition.

  • High dimensionality: The input vector becomes very large, increasing the number of
    parameters and computational cost, and requiring more data to train effectively.

Implications These limitations motivate the development of specialized architectures, such as
convolutional neural networks (CNNs), which exploit spatial locality and reduce parameter count
by sharing weights.
    Motivated by these limitations, we next motivate convolutional layers, which constrain connec-
tivity to local receptive fields, share weights across spatial locations, and dramatically reduce the
parameter count for image data.

11.9   Challenges in Training Large Fully Connected Networks
Consider a fully connected neural network where the input layer has 70,656 neurons (flattened
from a 256 × 276 grayscale image), connected to a hidden layer with 100 neurons, which in turn

                                                 149
Intelligent Systems and Soft Computing          Introduction to Deep Learning and Neural Networks


connects to an output layer for classification. Although this is a simplified example, it illustrates
key challenges in training large networks.

Parameter Explosion        The number of weights between the input and hidden layer is:

                                     70, 656 × 100 = 7, 065, 600,                              (11.4)

and between the hidden and output layer (assuming 4 output classes) is:

                                           100 × 4 = 400.                                      (11.5)

   Thus, the first layer alone requires learning just over 7 million parameters before we even
consider deeper architectures. Coupled with the additional 400 output weights (plus biases), the
optimization problem quickly becomes data-hungry and computationally expensive.

Data Requirements To reliably learn these parameters, the amount of training data must be
suﬀiciently large. A common heuristic is that the number of training samples should be at least 10
times the number of parameters:

                                     Nsamples ≥ 10 × Nparameters .                             (11.6)

   For the first layer, this implies roughly:

                             Nsamples ≳ 10 × 7, 000, 000 ≈ 70, 000, 000,                       (11.7)

meaning on the order of seventy million labeled images—an impractical requirement for most
projects.

Computational and Storage Constraints Storing and processing such a large dataset requires
enormous storage and computational resources. Training on hundreds of millions of images is
typically infeasible for most research groups or applications without specialized infrastructure.

Overfitting Risk With millions of parameters, the model has high capacity and can easily
memorize the training data, leading to overfitting. This means the network may not generalize well
to unseen data, as it learns to fit noise or irrelevant details rather than meaningful features.

11.10 Historical Context and the 2012 Breakthrough
Before 2012, neural networks were often dismissed in many academic circles due to their poor
performance on large-scale problems and the dominance of other methods such as Support Vector
Machines (SVMs). The sentiment was that neural networks were ”fancy” but not practical or
well-understood.




                                                 150
Intelligent Systems and Soft Computing            Introduction to Deep Learning and Neural Networks




      Figure 29: Soft-margin SVM intuition: maximize the margin while penalizing violations via
                                         slack variables ξi .


SVM geometry refresher. Figure 29 revisits the soft-margin formulation that dominated clas-
sification benchmarks prior to 2012. The slack variables ξi widen the feasible tube so that misla-
beled points incur linear penalties instead of rendering the optimization infeasible. The geometric
intuition—maximise the margin while tolerating limited violations—highlights why SVMs were
attractive when data were scarce.

Kernel trick intuition. SVMs also excelled thanks to kernels. The pair of plots in Figure 30
illustrate how a nonlinear map ϕ(x) turns a non-separable XOR pattern into a linearly sepa-
rable configuration in feature space. Rather than computing ϕ explicitly, the kernel function
k(xi , xj ) = ϕ(xi )⊤ ϕ(xj ) is evaluated to build the Gram matrix (Figure 31). This historical context
explains both the strengths and limitations that deep learning eventually overcame (e.g., the need
to predefine features).

11.10.1   Why discuss soft-margin SVMs here?
Before diving into modern deep architectures, it is instructive to recall why support vector machines
(SVMs) dominated pre-2012 benchmarks: they encode a clear inductive bias via the margin. The
soft-margin primal makes the trade-off explicit:

                        1
                                   nX                             
               min        kwk22 + C   ξi   s.t.   yi w⊤ ϕ(xi ) + b ≥ 1 − ξi , i = 1, . . . , n.   (11.8)
             w, b, ξ ≥0 2
                                  i=1

The parameter C balances margin maximization (regularization) against hinge-loss violations ξi .
Kernels k(x, x′ ) = ϕ(x)⊤ ϕ(x′ ) lift the data into feature spaces where large margins are attainable.
   Positioning SVMs here serves two purposes in our narrative:
   • It highlights the continuity of ideas: later, CNNs and deep nets will recover a similar bias–
     variance balance using weight decay, early stopping, and architectural priors (locality, param-

                                                   151
Intelligent Systems and Soft Computing         Introduction to Deep Learning and Neural Networks




        Figure 30: Kernel trick example: a polynomial feature map lifts the XOR dataset into a
                                   linearly separable configuration.


     eter sharing).

  • It provides a baseline mental model for decision boundaries and regularization that we will
    repeatedly contrast with learned representation approaches.

Convolutional Neural Networks (CNNs) Although CNNs had been proposed earlier, they
were not widely successful or adopted for large-scale image classification tasks until 2012. The
breakthrough came with the success of a deep CNN architecture trained on the ImageNet dataset,
which contains 1000 classes and millions of images.
```

### Findings
- **Notation and Dimensions:**
  - The image size is given as 256 × 276 pixels, but the text uses "276" instead of the more common "256 × 256" or "256 × 275". This is not an error but could be clarified as an example rather than a standard size.
  - The flattening operation is denoted as \( x = \text{vec}(X) \in \mathbb{R}^{70,656} \), which is correct given \( 256 \times 276 = 70,656 \).

- **Loss of Spatial Structure:**
  - The claim that flattening "ignores" spatial relationships is accurate. However, it might be helpful to explicitly mention that flattening destroys the 2D neighborhood information, which is crucial for convolutional architectures.

- **Parameter Explosion Calculation:**
  - The calculation of parameters between input and hidden layer is correct: \(70,656 \times 100 = 7,065,600\).
  - The number of parameters between hidden and output layer is also correct: \(100 \times 4 = 400\).
  - Bias terms are mentioned but not explicitly counted; it would be more precise to include biases in the parameter count or explicitly state they are excluded for simplicity.

- **Data Requirements Heuristic:**
  - The heuristic \( N_{\text{samples}} \geq 10 \times N_{\text{parameters}} \) is a common rule of thumb but not a strict rule. It should be clarified that this is an approximate guideline rather than a theoretical guarantee.
  - The implication that 70 million labeled images are needed is a rough estimate; in practice, regularization and other techniques can reduce data requirements.

- **Overfitting Risk:**
  - The explanation is sound, but it could be strengthened by mentioning regularization techniques (e.g., dropout, weight decay) that help mitigate overfitting.

- **SVM Section:**
  - The soft-margin SVM primal problem is correctly stated, but the notation in equation (11.8) is somewhat ambiguous:
    - The summation index \(i=1, \ldots, n\) is placed after the summation symbol but the formatting is slightly off.
    - The constraint \( y_i w^\top \phi(x_i) + b \geq 1 - \xi_i \) is correct.
    - The variables \(w, b, \xi \geq 0\) should clarify that only \(\xi_i \geq 0\), while \(w\) and \(b\) are unconstrained in sign.
  - The explanation of the kernel trick is accurate and well-illustrated by the XOR example.

- **Historical Context:**
  - The narrative correctly positions SVMs as a baseline before the deep learning breakthrough.
  - The mention of CNNs being proposed earlier but only widely adopted after 2012 is accurate.

- **Minor Typographical Issues:**
  - In the phrase "suﬀiciently large," the word "sufficiently" is misspelled.
  - The phrase "meaning on the order of seventy million labeled images" could be more formal as "requiring on the order of seventy million labeled images."

- **Logical Flow:**
  - The transition from the challenges of fully connected networks to the motivation for CNNs is clear and well-structured.
  - The connection between SVMs and deep learning is well motivated, emphasizing inductive bias and regularization.

**Summary:**
- Mostly accurate and well-explained.
- Minor clarifications needed on bias parameters, heuristic nature of data requirements, and constraints in SVM formulation.
- Typographical corrections recommended.
- No major scientific or mathematical errors detected.

## Chunk 63/104
- Character range: 406237–413191

```text
AlexNet (2012) The network introduced in 2012, often referred to as AlexNet, had approxi-
mately 60 million parameters and achieved:
  • Top-1 accuracy of approximately 62.5% (37.5% error) on the ImageNet classification task.

  • Top-5 accuracy of roughly 84.7% (15.3% error).
    These results, reported by Krizhevsky, Sutskever, and Hinton (2012), represented a dramatic
improvement over the prior state of the art and demonstrated the practical viability of deep learning
for large-scale image recognition.

Example Predictions        For instance, the network correctly classified images such as:
  • A mite, with the top guess being ”mite.”

  • A container ship, with the top guess being ”container ship.”

  • A motor scooter, correctly identified despite the complexity of the image.
   These successes marked a turning point in the adoption and development of deep learning
methods.


                                                 152
Intelligent Systems and Soft Computing           Introduction to Deep Learning and Neural Networks




     Figure 31: Kernel (Gram) matrix heatmap showing pairwise similarities after the feature map.
     High off-diagonal blocks indicate cluster structure captured without explicit feature engineering.


11.11 Summary of Key Challenges in Deep Networks
  • Parameter scale: Large networks require millions of parameters, increasing the complexity
    of training.

  • Data scale: Massive datasets are needed to avoid overfitting and to generalize well.

  • Computational resources: Training deep networks demands significant computational
    power and memory.

  • Overfitting: High-capacity models risk memorizing training data rather than learning gen-
    eralizable features.
    Practical mitigation strategies include weight regularization (L1/L2 penalties), dropout, exten-
sive data augmentation, batch normalization to stabilize activations, and architectural innovations
such as residual or densely connected networks that improve gradient flow.

11.12 Convolutional Neural Networks: Motivation and Parameter Sharing
Recall from the previous discussion that traditional fully connected neural networks suffer from an
explosion in the number of parameters when the input dimension is large. For example, consider
an input vector of size 8 and a hidden layer of size 6. A fully connected layer would require learning

                                                   153
Intelligent Systems and Soft Computing           Introduction to Deep Learning and Neural Networks




       Figure 32: Radial-basis SVM boundaries for increasing kernel sharpness. Moderately sharp
           kernels balance bias and variance, a lesson echoed later when tuning CNN capacity.




       Figure 33: RBF kernels enable SVMs to solve the XOR problem by lifting the data into a
      higher-dimensional feature space; CNN feature extractors would later learn such nonlinearities
                                             automatically.


8 × 6 = 48 parameters (weights).

Sparse Connectivity Convolutional Neural Networks (CNNs) address this challenge by intro-
ducing sparse connectivity. Instead of connecting every input neuron to every neuron in the next
layer, each neuron is connected only to a small local region of the input. For instance, each neuron
might be connected to only 4 inputs instead of all 8. This reduces the number of parameters from
48 to 8 × 4 = 32 in our example.

Parameter Sharing The next key innovation is parameter sharing. Instead of learning a unique
set of weights for each local connection, CNNs use the same set of weights (a filter or kernel) across
all spatial locations. This means that the same pattern detector is applied repeatedly across the
input.
    Formally, if the local receptive field size is k, then instead of learning 8 × k parameters, we learn
only k parameters, shared across all positions. This drastically reduces the number of parameters
and the amount of training data required.

Implications for Scalability This parameter sharing enables CNNs to scale to very large inputs.
For example, if the input has 70,000 features, a fully connected layer with 60,000 neurons would


                                                   154
Intelligent Systems and Soft Computing           Introduction to Deep Learning and Neural Networks




                  Interior position (no padding)Edge position with padding (p=1)

        Figure 34: Sliding a 3 × 3 kernel across an image. Left: interior positions reuse the same
      weights. Right: near edges, zero padding allows valid evaluations without shrinking the output
                                                   map.


require 70, 000 × 60, 000 = 4.2 × 109 parameters, which is infeasible. With sparse connectivity and
parameter sharing, the number of parameters depends only on the filter size (e.g., 4, 9, 25, or 49),
making it possible to train very large networks eﬀiciently.

11.13 Deep Learning: Depth vs. Width
Definition of Deep Learning Deep learning refers to neural networks with many layers between
the input and output, allowing the network to learn hierarchical feature representations. The term
deep emphasizes the number of layers (depth), not the number of neurons per layer (width).

Depth vs. Width A network with a single hidden layer containing many neurons is wide but
not deep. Conversely, a network with many layers but fewer neurons per layer is deep. Depth
allows the network to learn more complex, abstract features by composing simpler features learned
in earlier layers.

Why Depth Matters Depth enables the network to represent functions that would require
exponentially more neurons if implemented by a shallow (wide) network. This compositionality is
a key reason why deep learning has been so successful in tasks such as image recognition, natural
language processing, and speech recognition.

11.14 Mathematical Formulation of Convolution
Let us formalize the convolution operation used in CNNs.

Input and Filter Consider a one-dimensional input signal x = [x1 , x2 , . . . , xn ] and a filter (kernel)
w = [w1 , w2 , . . . , wk ] of size k ≤ n.




                                                   155
Intelligent Systems and Soft Computing                Introduction to Deep Learning and Neural Networks


Convolution Operation           The convolution output y = [y1 , y2 , . . . , yn−k+1 ] is given by

                                      X
                                      k
                               yi =         wj xi+j−1 ,    i = 1, 2, . . . , n − k + 1.                        (11.9)
                                      j=1


    This operation slides the filter w across the input x, computing a weighted sum of local input
regions.

Extension to Two Dimensions For images, the input is two-dimensional, X ∈ RH×W , and the
filter is a smaller 2D kernel W ∈ RkH ×kW . The convolution output Y ∈ R(H−kH +1)×(W −kW +1) is
given by
```

### Findings
- **AlexNet Accuracy Values**: The stated Top-1 accuracy of approximately 62.5% and Top-5 accuracy of roughly 84.7% for AlexNet on ImageNet are roughly correct but slightly outdated or rounded. The original AlexNet paper reported a Top-5 error rate of 15.3%, which corresponds to 84.7% accuracy, so this is consistent. However, the Top-1 accuracy was closer to 57% (43% error) rather than 62.5%. This discrepancy should be clarified or referenced precisely.

- **Example Predictions Section**: The examples given (mite, container ship, motor scooter) are illustrative but lack context such as the confidence scores or whether these were typical or cherry-picked examples. It would be better to clarify that these are representative examples rather than exhaustive or typical.

- **Figure 31 Caption**: The caption mentions a "Kernel (Gram) matrix heatmap showing pairwise similarities after the feature map" with "High off-diagonal blocks indicate cluster structure." This is scientifically plausible but would benefit from a brief explanation of what the feature map is, what data is being compared, and how the kernel matrix is constructed to avoid ambiguity.

- **Parameter Sharing Explanation**: The explanation of parameter sharing states: "if the local receptive field size is k, then instead of learning 8 × k parameters, we learn only k parameters." This is slightly ambiguous because the number 8 here refers to the input size, but the key point is that the same k parameters are shared across all spatial locations. It would be clearer to say: "For an input of length n and a filter of size k, a fully connected layer would learn n × k parameters, but with parameter sharing, only k parameters are learned and applied across all positions."

- **Example of Parameter Reduction**: The example reducing parameters from 48 to 32 by connecting each neuron to 4 inputs instead of 8 is correct, but the subsequent explanation of parameter sharing could be more explicit in distinguishing between sparse connectivity (reducing connections) and parameter sharing (reusing weights).

- **Notation in Convolution Formula (Equation 11.9)**: The convolution formula is given as:

  \[
  y_i = \sum_{j=1}^k w_j x_{i+j-1}, \quad i=1,2,\ldots,n-k+1.
  \]

  This is the standard cross-correlation operation rather than the strict mathematical convolution (which involves flipping the kernel). This is common in deep learning literature but should be explicitly stated to avoid confusion.

- **Extension to Two Dimensions**: The text ends abruptly after introducing the 2D convolution notation without providing the explicit formula for the 2D convolution output. This is a logical gap; the formula should be completed for clarity.

- **Inconsistent Notation for Filters**: The 1D filter is denoted as \( w = [w_1, w_2, \ldots, w_k] \), but the 2D filter is denoted as \( W \in \mathbb{R}^{k_H \times k_W} \). Using both lowercase and uppercase \( w \) and \( W \) for filters may cause confusion. Consistent notation should be used or explicitly clarified.

- **Missing Definitions**: Terms such as "padding" and "stride" are mentioned implicitly (e.g., Figure 34 caption mentions padding \( p=1 \)) but are not formally defined in the text. Including definitions would improve clarity.

- **Figure 32 and 33 Captions**: These figures discuss RBF kernels and SVMs in the context of CNNs. While interesting, the connection to CNNs is somewhat vague and could benefit from more explicit explanation of how these concepts relate to CNN feature extraction.

- **Summary of Key Challenges**: The list is accurate and well-justified. However, the mention of "batch normalization to stabilize activations" could be expanded to note its role in enabling higher learning rates and reducing internal covariate shift, for completeness.

- **Depth vs. Width Section**: The explanation is clear and accurate. However, the claim that depth allows representation of functions requiring exponentially more neurons in shallow networks is a strong theoretical statement that could be supported by references or a brief explanation.

Overall, the chunk is scientifically sound but would benefit from clarifications, completion of incomplete formulas, consistent notation, and more precise referencing of claims.

## Chunk 64/104
- Character range: 413193–420090

```text
kH X
            X  kW
   Yi,j =             Wm,n Xi+m−1,j+n−1 ,       i = 1, . . . , H − kH + 1,       j = 1, . . . , W − kW + 1.   (11.10)
            m=1 n=1


Parameter Sharing in Convolution Note that the same filter W is applied at every spatial
location (i, j), implementing parameter sharing.

11.15 Training Convolutional Neural Networks
Learning Shared Parameters Although the filter weights w are shared across all spatial loca-
tions, they are learned by backpropagation using gradient descent. The gradients from all locations
are accumulated to update the shared weights.

Effect on Training Data Requirements Parameter sharing reduces the number of parameters
to learn, which in turn reduces the amount of training data required to fit the model reliably before
overfitting.

11.16 Convolution Operation in Neural Networks
We continue our discussion on convolutional neural networks (CNNs) by formalizing the convolution
operation and illustrating its mechanics with concrete examples.

Definition of Convolution Consider two discrete signals (or functions) f and g. The convo-
lution (f ∗ g) is defined as the sum of the element-wise product of one signal with a reversed and
shifted version of the other. Mathematically, for discrete signals, this is expressed as:
                                                          ∞
                                                          X
                                      (f ∗ g)[n] =              f [m] g[n − m]                                (11.11)
                                                      m=−∞

where n indexes the output signal, and m indexes the summation variable.
   In the context of CNNs, f typically represents the input signal (e.g., an image or feature map),
and g represents the filter or kernel that is slid over f .




                                                          156
Intelligent Systems and Soft Computing         Introduction to Deep Learning and Neural Networks


Key Properties
  • The kernel g is flipped (reversed) before sliding over f .

  • At each position n, the overlapping elements of f and g are multiplied element-wise and
    summed to produce the output.

  • The output size depends on the input size, kernel size, stride, and padding.

Example: Convolution on a 2D Input Suppose we have a 6 × 6 input image F and a 3 × 3
kernel G. The convolution is performed by sliding G over F and computing the sum of element-wise
products at each position.
   For instance, at one position, the convolution output is:

                                          X
                                          3 X
                                            3
                                                    Fi,j · Gi,j
                                          i=1 j=1


   The kernel is moved one step at a time (stride = 1), and this process repeats until the kernel
has scanned the entire input.

Numerical Example        Given the input patch and kernel values:
                                                                
                                      1 0 3                  1 1 1
                                                                
                                F =  2 0 4 ,         G =  1 1 1
                                      4 0 6                  1 1 1
   The convolution at this position is:

            1 × 1 + 0 × 1 + 3 × 1 + 2 × 1 + 0 × 1 + 4 × 1 + 4 × 1 + 0 × 1 + 6 × 1 = 20

    Sliding the kernel one step to the right and repeating the calculation yields the next output
value, and so forth.

11.17 Convolution as Sparse Connectivity and Parameter Sharing
Sparse Connectivity Unlike fully connected layers where each neuron connects to every in-
put feature, convolutional layers use sparse connectivity. Each neuron in the convolutional layer
connects only to a small local region of the input, defined by the kernel size.
    For example, if the kernel size is 3 × 3, each neuron connects to only 9 input neurons, regardless
of the total input size.

Parameter Sharing The same kernel weights are used across all spatial locations of the input.
This means the filter G is shared across the input, drastically reducing the number of parameters
compared to fully connected layers.




                                                157
Intelligent Systems and Soft Computing          Introduction to Deep Learning and Neural Networks


Mathematical Representation Consider an input vector x = [x1 , x2 , . . . , x8 ] and a kernel with
weights w = [w1 , w2 , w3 , w4 ]. The output of the convolution at position k is:

                                                X
                                                4
                                         yk =         xk+i−1 wi                               (11.12)
                                                i=1

where k = 1, 2, . . . , 5 for an input of length 8 and kernel size 4.
    This operation corresponds to sliding the kernel over the input and computing a weighted sum
at each step.

Implications
   • The number of connections per neuron is limited to the kernel size, not the full input size.

   • The total number of parameters is equal to the kernel size, independent of the input size.

   • This leads to eﬀicient learning and better generalization, especially for spatially structured
     data like images.

11.18 Convolutional Layer Architecture
Input and Output Dimensions Suppose the input layer has N features arranged spatially
(e.g., a 6 × 6 image with N = 36 pixels). The convolutional layer applies M filters (kernels), each
of size k × k, producing M output feature maps.
    The output spatial dimensions depend on:
   • Input size S

   • Kernel size k

   • Stride s

   • Padding

11.19 Parameter Sharing and Scalability in Convolutional Layers
Recall that in convolutional neural networks (CNNs), the key idea of parameter sharing allows us
to use the same filter (or kernel) weights repeatedly across different spatial locations of the input.
This drastically reduces the number of parameters compared to fully connected layers.
    Consider an input matrix F of size n × n and a filter G of size f × f . The output size after
applying the convolution (or more precisely, cross-correlation) is given by:

                                         nout = n − f + 1.                                    (11.13)

   For example, if n = 6 and f = 3, then nout = 6 − 3 + 1 = 4, so the output is 4 × 4.

Effect of filter size on output dimension and parameters
   • Increasing the filter size f reduces the output spatial dimension nout .



                                                 158
Intelligent Systems and Soft Computing           Introduction to Deep Learning and Neural Networks


   • Larger filters have more parameters to learn (since the number of parameters per filter is f 2
     for a single input channel).
```

### Findings
- **Equation (11.10) notation**: The summation indices and limits are not clearly formatted; it would be clearer to write the double sum explicitly as \(\sum_{m=1}^{k_H} \sum_{n=1}^{k_W} W_{m,n} X_{i+m-1, j+n-1}\).

- **Definition of convolution (11.11)**: The definition given corresponds to the standard discrete convolution with kernel flipping. However, in CNNs, the operation implemented is typically *cross-correlation*, where the kernel is not flipped. This distinction should be explicitly stated to avoid confusion.

- **Kernel flipping in CNNs**: The notes say "The kernel \(g\) is flipped (reversed) before sliding over \(f\)". This is mathematically true for convolution but not for the operation used in CNNs, which is cross-correlation. This point should be clarified.

- **Numerical example kernel \(G\)**: The kernel \(G\) is given as a 3x3 matrix of all ones, but the input patch \(F\) is shown as a 3x3 matrix as well, which is inconsistent with the earlier example of a 6x6 input and 3x3 kernel. The example should clarify that this is a local patch extracted from the larger input.

- **Notation inconsistency**: The input patch \(F\) and kernel \(G\) are both shown as 3x3 matrices, but the notation \(F_{i,j}\) and \(G_{i,j}\) is not explicitly defined here. It would be helpful to define the indexing clearly.

- **Equation (11.12)**: The convolution output at position \(k\) is given as \(y_k = \sum_{i=1}^4 x_{k+i-1} w_i\). This is correct for 1D convolution without kernel flipping (cross-correlation). Again, the distinction between convolution and cross-correlation should be made explicit.

- **Output size formula (11.13)**: The formula \(n_{out} = n - f + 1\) assumes stride = 1 and no padding. This assumption should be explicitly stated.

- **Terminology "convolution (or more precisely, cross-correlation)"**: This is a good note, but it should be introduced earlier when defining the operation to avoid confusion.

- **Missing definitions**: Terms like stride and padding are mentioned but not formally defined or explained in this chunk.

- **Ambiguity in "Input and Output Dimensions"**: The input is said to have \(N\) features arranged spatially (e.g., a 6x6 image with \(N=36\) pixels). It would be clearer to say the input has spatial dimensions \(S \times S\) (e.g., \(6 \times 6\)) and total features \(N = S^2\).

- **Parameter sharing explanation**: The explanation is clear, but it would benefit from explicitly stating that parameter sharing leads to translation equivariance in CNNs.

- **Sparse connectivity**: The explanation is good, but it could mention that sparse connectivity reduces computational complexity as well as the number of parameters.

- **Effect of filter size on output dimension and parameters**: The notes correctly state that increasing filter size reduces output spatial dimension and increases parameters, but the effect of stride and padding on output size is not discussed here.

- **General clarity**: The chunk mixes 1D and 2D convolution examples without explicitly stating the dimensionality each time, which could confuse readers.

Overall, the main scientific issues are the lack of clarity about the difference between convolution and cross-correlation in CNNs, missing explicit definitions of stride and padding, and some notation and indexing ambiguities.

## Chunk 65/104
- Character range: 420104–427343

```text
• Smaller filters produce larger outputs but have fewer parameters.
   This trade-off is crucial for designing CNN architectures that balance model complexity and
computational eﬀiciency.

Example:
   • Input size: 6 × 6 (36 elements)

   • Filter size: 2 × 2

   • Output size: 6 − 2 + 1 = 5, so output is 5 × 5 = 25 elements (this assumes stride 1 and zero
     padding)
   Instead of learning 36×25 = 900 parameters as in a fully connected layer, we only learn 2×2 = 4
parameters for the filter, which are shared across all spatial locations.

11.20 Convolution vs. Cross-Correlation
Mathematical definition of convolution The convolution of two discrete signals f and g is
defined as:
                                         ∞
                                         X
                            (f ∗ g)[n] =   f [m] g[n − m].                        (11.14)
                                                 m=−∞

This operation involves flipping (mirroring) one of the signals before shifting and multiplying.

Cross-correlation Cross-correlation is defined as:
                                                 ∞
                                                 X
                                  (f ⋆ g)[n] =            f [m] g[n + m].                     (11.15)
                                                 m=−∞

Notice that there is no flipping of the signal g.

Practical implication in CNNs In practice, the operation implemented in CNNs is cross-
correlation, not convolution, because the filter is not flipped before sliding over the input. Despite
this, the term ”convolution” is widely used due to historical reasons and simplicity.
   • The filter weights are learned directly without flipping.

   • Cross-correlation is computationally simpler.

   • The difference does not affect the learning capability of CNNs.

Summary:
                          CNN operation ≈ cross-correlation 6= convolution.




                                                    159
Intelligent Systems and Soft Computing        Introduction to Deep Learning and Neural Networks


11.21 Design Considerations for Filters in CNNs
When designing convolutional layers, several practical considerations arise:

1. Filter size selection
  • Larger filters capture more complex spatial features but reduce output size and increase
    parameters.

  • Smaller filters preserve spatial resolution but may underfit if too simple.

  • Common choices include 3 × 3 or 5 × 5 filters.

2. Output dimension control Using Equation (11.13), the output size can be controlled by
choosing appropriate filter sizes. However, this may not always be desirable if the output shrinks
too much.

3. Padding and stride (to be discussed later) To address shrinking output sizes, techniques
such as zero-padding and strided convolutions are introduced, which allow control over output
dimensions without sacrificing filter size.

4. Parameter count and model complexity The number of parameters in a convolutional
layer is:
                         Parameters = f × f × Cin × Cout ,

where Cin and Cout are the number of input and output channels, respectively.

5. Feature representation Each output feature map corresponds to a learned filter that ex-
tracts a particular feature from the input. Because of parameter sharing, each spatial location in
the output represents the presence of that feature at that location in the input.

6. Balancing underfitting and overfitting
  • Too few parameters (small filters, few filters) may lead to underfitting.

  • Too many parameters (large filters, many filters)

11.22 Padding and Stride in Convolutional Layers
When performing convolution operations, it is crucial to understand how the input dimensions map
to the output dimensions. This mapping affects the preservation of spatial information and the
quality of feature extraction.

Motivation for Padding Consider an input image of size n × n and a filter (kernel) of size f × f .
Without padding, the output dimension after convolution with stride 1 is given by:

                                         nout = n − f + 1.                                 (11.16)


                                                160
Intelligent Systems and Soft Computing         Introduction to Deep Learning and Neural Networks


This means the output feature map is smaller than the input, which can lead to loss of important
edge information. For example, features near the borders of the input may be underrepresented or
lost entirely.
    To address this, padding is introduced. Padding adds extra pixels (usually zeros) around the
border of the input, effectively enlarging it. This allows the filter to be applied to border pixels as
well, preserving spatial dimensions or controlling the output size.

Padding Calculation          If we denote the padding size by p, the output size with padding and
stride 1 is:
                                        nout = n + 2p − f + 1.                                 (11.17)

   If the goal is to keep the output size equal to the input size, i.e., nout = n, then from (11.17):

                                           n = n + 2p − f + 1                                  (11.18)
                                        ⇒ 2p = f − 1                                           (11.19)
                                               f −1
                                         ⇒p=         .                                         (11.20)
                                                 2
   For example, if f = 3, then p = 1; if f = 5, then p = 2.

Practical Example       Suppose the input size is 6 × 6, filter size 3 × 3, and stride s = 1. Without
padding:
                                        nout = 6 − 3 + 1 = 4,

so the output is 4 × 4.
    With padding p = 1:
                                     nout = 6 + 2(1) − 3 + 1 = 6,

so the output size matches the input size.

Stride Stride s controls the step size of the filter as it moves across the input. Instead of moving
one pixel at a time, the filter can jump s pixels.
   The general formula for output size with padding and stride is:
                                                          
                                               n + 2p − f
                                      nout =                 + 1.                             (11.21)
                                                    s


Example with Stride Consider n = 6, f = 3, p = 0, and s = 2:
                                            
                             6+0−3            3
                    nout =             +1=        + 1 = 1 + 1 = 2.
                               2              2

Thus, the output is 2 × 2.




                                                 161
Intelligent Systems and Soft Computing          Introduction to Deep Learning and Neural Networks




                           Padding (p=1)                      Stride (s=2)

     Figure 35: Padding preserves border information (left) while stride down-samples by skipping
                                          positions (right).


Summary of Parameters
  • n: input dimension (height/width)

  • f : filter size

  • p: padding size

  • s: stride

  • nout : output dimension
```

### Findings
- The statement "Smaller filters produce larger outputs but have fewer parameters" is generally correct but could be clarified: smaller filters produce larger outputs only if padding and stride are fixed; changing stride or padding can alter output size independently of filter size.

- In the example calculating output size: "Output size: 6 − 2 + 1 = 5" assumes stride = 1 and zero padding, which is stated, so this is correct.

- The parameter count comparison between fully connected layer (36×25=900) and convolutional layer (2×2=4) is correct, but it should be noted that the convolutional layer typically has multiple filters (output channels), so total parameters would be 4 × number_of_filters.

- The convolution definition in equation (11.14) is correct, but the summation limits from -∞ to ∞ are idealized; in practice, signals are finite-length, and the summation limits should be adjusted accordingly or stated as over the domain where f and g are defined.

- The cross-correlation definition in equation (11.15) is correct and the explanation that CNNs implement cross-correlation rather than convolution is accurate.

- The claim "Cross-correlation is computationally simpler" is somewhat ambiguous; computational complexity is essentially the same, but cross-correlation avoids the flipping step, which is trivial in practice. This could be clarified.

- The statement "The difference does not affect the learning capability of CNNs" is generally accepted but could be justified or referenced.

- In section 11.21, point 2: "Using Equation (11.13), the output size can be controlled by choosing appropriate filter sizes" — Equation (11.13) is not provided here; the reader may need a reminder or the equation restated for clarity.

- In section 11.21, point 6 is incomplete: "Too many parameters (large filters, many filters)" — the sentence is unfinished and should be completed, presumably with "may lead to overfitting."

- In the padding calculation, equation (11.18) is written as "n = n + 2p − f + 1" which is correct for setting output size equal to input size, but the rearrangement to 2p = f − 1 (equation 11.19) should explicitly show the subtraction of n from both sides for clarity.

- The example with stride s=2 and no padding is correct, but the formatting of the calculation is somewhat confusing with extra brackets; it would be clearer to write:

  n_out = floor((6 + 0 − 3)/2) + 1 = floor(3/2) + 1 = 1 + 1 = 2.

- The notation in equation (11.21) uses unusual brackets " " around the numerator; standard notation would use floor or ceiling functions explicitly, since output size is typically an integer obtained by floor division.

- The summary of parameters is clear and consistent.

- Figure 35 is referenced but not shown here; ensure that the figure clearly illustrates the concepts of padding preserving border information and stride downsampling.

- Minor typo: "computational eﬀiciency" uses a non-standard character for 'f' (looks like a ligature or special character); ensure consistent font encoding.

- Overall, the chunk is well-written but would benefit from completing incomplete sentences, clarifying some ambiguous claims, and standardizing notation for output size calculations involving stride and padding.

## Chunk 66/104
- Character range: 427348–434222

```text
Implementation Notes In popular deep learning frameworks such as TensorFlow or Keras,
padding can be specified as:
  • valid: no padding (p = 0)

  • same: padding chosen to keep output size equal to input size
   The framework automatically calculates the required padding for same padding.

11.23 Feature Transformation in Deep Learning
One of the key strengths of deep learning is its ability to perform complex feature transformations.
Convolutional layers do not simply extract features; they transform the input representation into
new feature spaces that highlight different aspects of the data.
    For example, consider an image of a face. A convolutional filter may emphasize certain facial
features such as the nose, eyes, or mouth. However, if the filter size or stride is not chosen carefully,
some features may be lost or underrepresented in the output. Padding helps mitigate this by
ensuring border features are preserved.
    This transformation is crucial for hierarchical feature extraction, where deeper layers capture
more abstract and invariant representations.

11.24 Extending Convolution to Multi-Channel Inputs
So far, we have discussed convolution on single-channel (grayscale) images, which can be represented
as 2D arrays of size n × n.


                                                  162
Intelligent Systems and Soft Computing          Introduction to Deep Learning and Neural Networks


RGB Images Color images typically have three channels: Red, Green, and Blue (RGB). Such
images are represented as 3D tensors of size:

                                              n × n × c,

where c = 3 for RGB.

Convolution Across Channels When a filter is applied to a multi-channel input, each channel
has its own slice of filter weights. The convolution sums the elementwise products across both
spatial dimensions and channels, yielding a single scalar per spatial location. Thus a filter learns
to combine information from all channels simultaneously.

11.25 Multiple Filters and Feature Maps
Recall from the previous discussion that a single convolutional filter applied to an input image
produces one feature map (or output channel). However, the true power of convolutional neural
networks (CNNs) lies in the use of multiple filters at each convolutional layer. Each filter is designed
to extract a different type of feature from the input, such as edges, textures, or more complex
patterns.

Filter Dimensions and Output Channels Suppose the input to a convolutional layer is an
image or feature map of size H ×W ×D, where H and W are spatial dimensions and D is the number
of channels (e.g., 3 for RGB images). A convolutional filter in this layer has spatial dimensions
F × F and depth D, i.e., the filter size is F × F × D.
    Applying one such filter produces a single 2D feature map. If we use K such filters, the output
will be a tensor of size H ′ × W ′ × K, where H ′ and W ′ depend on the convolution parameters (filter
size, stride, padding).

Example: - Input size: 50 × 50 × 3 - Filter size: 3 × 3 - Number of filters: 10 - Stride: 1 - Padding:
0 (no padding)
    The output spatial size is computed as:

                                       H −F     50 − 3
                                H′ =        +1=        + 1 = 48,
                                         S        1

and similarly for W ′ . Thus, the output size is 48 × 48 × 10.
   Each of the 10 filters extracts a different feature representation, and stacking these feature maps
along the depth dimension forms the output tensor.

11.26 Stacking Convolutional Layers
CNNs typically consist of multiple convolutional layers stacked sequentially. Each layer extracts
increasingly abstract features from the input.




                                                  163
Intelligent Systems and Soft Computing             Introduction to Deep Learning and Neural Networks


Example Network Architecture: Consider the following sequence of convolutional layers ap-
plied to an input image of size 50 × 50 × 3:
  • Layer 1:

        – Filter size: 3 × 3
        – Number of filters: 10
        – Stride: 1
        – Padding: 0

     Output size:
                                                   48 × 48 × 10

  • Layer 2:

        – Filter size: 5 × 5
        – Number of filters: 20 (doubling previous)
        – Stride: 3
        – Padding: 0

     Output size:                           
                                      48 − 5
                                               + 1 = 15,      ⇒ 15 × 15 × 20
                                        3

  • Layer 3:

        – Filter size: 5 × 5
        – Number of filters: 40 (doubling previous)
        – Stride: 3
        – Padding: 0

     Output size:                               
                                          15 − 5
                                                   + 1 = 4,   ⇒ 4 × 4 × 40
                                            3

   This sequence reduces the spatial dimensions from 50 × 50 down to 4 × 4, while increasing the
depth from 3 to 40. This process extracts a rich set of features at multiple scales.

11.27 Parameter Count and Eﬀiciency
One of the key advantages of convolutional layers over fully connected layers is the dramatic reduc-
tion in the number of parameters.

Parameter calculation for convolutional layers: Each filter has F × F × D parameters, plus
one bias term. For K filters, the total number of parameters is:

                                           K × (F × F × D + 1).

                                                     164
Intelligent Systems and Soft Computing           Introduction to Deep Learning and Neural Networks


Example:       For the first layer above:

                        10 × (3 × 3 × 3 + 1) = 10 × (27 + 1) = 280 parameters.

   Compare this to a fully connected layer connecting a 50 × 50 × 3 = 7500 input vector to 100
neurons:
                              7500 × 100 = 750, 000 parameters.

   Clearly, convolutional layers are much more parameter-eﬀicient, enabling deeper networks with-
out overfitting.

11.28 Summary of Convolutional Layer Design Choices
When designing convolutional layers, the following parameters must be chosen carefully:
     • Filter size F : Typically small (e.g., 3 or 5), controls receptive field.

     • Number of filters K: Determines how many feature channels are learned at each stage and
       therefore the expressive capacity.

     • Stride s: Governs how aggressively the feature map is downsampled; large strides reduce
       resolution but increase invariance.

     • Padding p: Preserves border information and keeps feature map sizes stable across layers.

     • Nonlinearity: ReLU, GELU, or other activations control gradient flow and sparsity.

     • Pooling window/stride: Specifies how spatial aggregation is performed between convolu-
       tional stacks.
```

### Findings
- **Padding definitions (11.22 Implementation Notes):**  
  - The explanation of "valid" and "same" padding is correct and consistent with TensorFlow/Keras terminology. No issues here.

- **Feature transformation (11.23):**  
  - The description of convolutional layers as feature transformers rather than simple feature extractors is accurate and well-stated.  
  - The claim that padding helps preserve border features is correct and important.  
  - No missing definitions or ambiguous claims here.

- **Multi-channel convolution (11.24):**  
  - The explanation of RGB images as 3D tensors (n × n × c) with c=3 is standard and clear.  
  - The description of convolution summing elementwise products across spatial dimensions and channels to produce a scalar per spatial location is correct.  
  - No issues spotted.

- **Multiple filters and feature maps (11.25):**  
  - The notation for input size (H × W × D) and filter size (F × F × D) is consistent and standard.  
  - The formula for output spatial size:  
    \[
    H' = \frac{H - F}{S} + 1
    \]  
    is correctly applied in the example.  
  - The example calculation for output size (48 × 48 × 10) is correct given the parameters.  
  - No inconsistencies or missing justifications.

- **Stacking convolutional layers (11.26):**  
  - The example network architecture is clear and the output size calculations are mostly correct.  
  - However, the output size calculations for Layer 2 and Layer 3 are presented with some formatting issues (unusual symbols  and  around the formula), which may confuse readers. These should be cleaned up for clarity.  
  - The formula used for output size is consistent:  
    \[
    H' = \frac{H - F}{S} + 1
    \]  
  - The calculations:  
    - Layer 2: \((48 - 5)/3 + 1 = 15\) correct.  
    - Layer 3: \((15 - 5)/3 + 1 = 4\) correct.  
  - No logical gaps, but the formatting issue should be fixed.

- **Parameter count and efficiency (11.27):**  
  - The formula for parameter count per convolutional layer:  
    \[
    K \times (F \times F \times D + 1)
    \]  
    is correct (including bias term).  
  - The example calculation for the first layer (280 parameters) is accurate.  
  - The comparison to fully connected layers (750,000 parameters) is valid and well-illustrated.  
  - No issues here.

- **Summary of design choices (11.28):**  
  - The list of parameters to choose is comprehensive and well-explained.  
  - The explanations for each parameter are accurate and clear.  
  - No missing definitions or ambiguous claims.

**Additional minor points:**  
- The notation for stride is sometimes given as "S" and sometimes as "s" (e.g., in formulas and bullet points). Consistency in notation would improve clarity.  
- The term "nonlinearity" is introduced without explicitly defining what it means in this context (activation functions). While common knowledge in deep learning, a brief definition could help beginners.  
- The term "pooling window/stride" is mentioned in the summary but pooling has not been discussed in detail in this chunk; a cross-reference or brief explanation might be helpful.

**Summary:**  
- Mostly accurate and well-explained content.  
- Minor formatting issues in output size formulas for Layer 2 and Layer 3.  
- Minor inconsistency in stride notation (S vs s).  
- Slightly more explicit definition of "nonlinearity" and pooling could improve clarity.

Otherwise, no scientific or mathematical errors detected.

## Chunk 67/104
- Character range: 434224–441868

```text
11.29 Nonlinear Activation Functions in Convolutional Neural Networks
Recall from previous lectures that neural networks apply nonlinear activation functions after linear
transformations to introduce nonlinearity, enabling the network to approximate complex functions.
In convolutional neural networks (CNNs), this principle remains the same.
    Given an input feature map x, a convolutional layer computes a linear combination of inputs
with learned filters W and biases b:
                                          z = W ∗ x + b,                                    (11.22)

where ∗ denotes the convolution operation.
    The output of this convolution is then passed through a nonlinear activation function σ(·), such
as the sigmoid, hyperbolic tangent, or ReLU (Rectified Linear Unit):

                                                y = σ(z).                                         (11.23)

     For example, if zij is the pre-activation value at spatial location (i, j), then the activated output
is
                                               yij = σ(zij ).                                     (11.24)



                                                   165
Intelligent Systems and Soft Computing         Introduction to Deep Learning and Neural Networks




              Input feature map (4 × 4) Max pooling (2 × 2)Average pooling (2 × 2)

     Figure 36: Pooling summarizes local neighborhoods to shrink resolution: a 2 × 2 window with
             stride 2 reduces a 4 × 4 map to 2 × 2 via either max or average aggregation.


   This nonlinear step is crucial because it allows the network to learn complex hierarchical features
beyond linear combinations.

11.30 Pooling Layers: Motivation and Operation
After convolution and nonlinear activation, CNNs often include pooling layers to reduce spatial
dimensions and aggregate information. Pooling layers perform a form of downsampling by summa-
rizing local neighborhoods in the feature maps.

Pooling operation: Given an input feature map y of size H × W , a pooling layer applies a
sliding window (filter) of size k × k with stride s over the spatial dimensions. For each window, an
aggregation function A is applied to the values inside the window:
                                                                                
                    pm,n = A {yi,j | i ∈ [ms, ms + k − 1], j ∈ [ns, ns + k − 1]} ,             (11.25)

where pm,n is the pooled output at location (m, n).
   Common aggregation functions include:
  • Max pooling: A = max

  • Average pooling: A = mean

  • Min pooling: A = min


Output dimensions The pooled feature map sizes are
                                                       
                           H −k                      W −k
                  Hout =           + 1,     Wout =          + 1,                               (11.26)
                             s                         s

where b·c denotes the floor operation. These expressions account for stride and the fact that the
pooling window must lie entirely within the input feature map.

Example: Consider a 4 × 4 feature map and a 3 × 3 max pooling filter with stride 1. The output
size is computed as                       
                                      4−3
                                             + 1 = 2,                                   (11.27)
                                       1

                                                 166
Intelligent Systems and Soft Computing        Introduction to Deep Learning and Neural Networks


so the pooled feature map is 2 × 2. Each pooled value corresponds to the maximum value in the
3 × 3 window sliding over the input.

11.31 Pooling Layers: Biological and Theoretical Considerations
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

Pooling vs. other dimensionality reduction methods: Replacing pooling with other dimen-
sionality reduction techniques such as Principal Component Analysis (PCA) or learned downsam-
pling often results in worse performance. This suggests that pooling captures some inductive bias
beneficial for hierarchical feature learning in CNNs, though the precise reasons remain an open
research question.

11.32 Summary of the Convolution-Pooling Pipeline
A typical CNN block consists of the following sequence:
  1. Convolution: Apply learned filters to extract local features.

  2. Nonlinear activation: Apply a nonlinear function (e.g., ReLU) to introduce nonlinearity.

  3. Pooling: Downsample the feature maps by aggregating local neighborhoods.



                                                167
Intelligent Systems and Soft Computing          Introduction to Deep Learning and Neural Networks


         Effective receptive field growth across stacked conv/pool layers




           Stage 1 (RF = 3 × 3)          Stage 2 (RF = 5 × 5)           Stage 3 (RF = 7 × 7)

      Figure 37: Effective receptive field growth as convolutional/pooling layers stack. Even with
                       3 × 3 kernels, the spatial support expands at each stage.


    This pipeline is repeated multiple times, gradually transforming the input image into increas-
ingly abstract and spatially compressed feature representations. After several convolution-pooling
blocks, the network has accumulated a rich set of high-level descriptors that can feed downstream
classification heads.

11.33 Flattening and Classification in CNNs
After the convolutional and pooling layers extract features from the input image, the resulting multi-
dimensional tensor must be transformed into a format suitable for classification. This process is
called flattening, where the tensor is reshaped into a one-dimensional vector.
    For example, consider a feature map of size 4 × 4 × 40. Flattening this tensor yields a vector of
length:
                                          4 × 4 × 40 = 640.

This vector can then be fed into a fully connected (shallow) neural network or other classifiers
such as support vector machines (SVMs) or logistic regression models. The goal is to leverage the
extracted features for accurate classification.
```

### Findings
- **Equation (11.26) Output Dimensions:**
  - The notation for the floor operation is missing in the formula. The text states "b·c denotes the floor operation," but the formula uses parentheses without explicitly showing the floor brackets. It would be clearer to write:
    \[
    H_{out} = \left\lfloor \frac{H - k}{s} \right\rfloor + 1, \quad W_{out} = \left\lfloor \frac{W - k}{s} \right\rfloor + 1
    \]
  - This is important because without the floor operation, the output size could be non-integer or incorrectly interpreted.

- **Pooling Window Must Lie Entirely Within Input:**
  - The text states that the pooling window must lie entirely within the input feature map. This is true for "valid" pooling, but some frameworks allow "same" padding for pooling layers, which can produce output sizes equal to input sizes. This distinction could be mentioned for completeness.

- **Pooling as Non-Learnable Layer:**
  - The claim that pooling is "not a 'layer' in the strict neural network sense" because it lacks learnable parameters is somewhat ambiguous. In modern deep learning frameworks, pooling layers are considered layers despite having no parameters. The distinction should be clarified: pooling layers are non-parametric layers but still part of the network architecture.

- **Biological Analogy:**
  - The statement that pooling "does not correspond directly to any known biological neuron operation" is broadly correct but could be nuanced. Some biological processes involve forms of spatial integration or lateral inhibition that resemble pooling-like operations. A brief mention of this nuance would improve accuracy.

- **Pooling vs. Other Dimensionality Reduction Methods:**
  - The claim that replacing pooling with PCA or learned downsampling "often results in worse performance" is generally true but context-dependent. Some recent architectures use learned downsampling or strided convolutions effectively. This statement could be softened or supported with references.

- **Flattening and Classification:**
  - The explanation of flattening is clear, but it might be worth mentioning that flattening can lead to very high-dimensional vectors, which can increase the number of parameters in fully connected layers and risk overfitting. Alternatives like global average pooling could be briefly noted.

- **Notation Consistency:**
  - The notation for indices in equation (11.25) uses both i, j and m, n. While this is standard, it would help to explicitly state that (m, n) indexes the pooled output spatial locations, while (i, j) indexes the input feature map spatial locations.

- **Figure References:**
  - Figures 36 and 37 are referenced but not shown here. Ensure that the figures clearly illustrate the concepts described, especially the receptive field growth in Figure 37.

- **Minor Typographical Issues:**
  - In equation (11.27), the expression is split awkwardly across lines. It would be clearer to write the entire expression on one line or use proper equation formatting.

No major scientific or mathematical errors were found; the issues are mostly about clarity, completeness, and precision.

## Chunk 68/104
- Character range: 441870–449340

```text
Backpropagation through CNNs Backpropagation in CNNs updates the weights of convolu-
tional filters and fully connected layers by propagating the error gradients backward through the
network. Although the network may appear complex due to three-dimensional feature maps and
multiple layers, the underlying principle remains the same as in standard neural networks: compute
gradients with respect to weights and update them using gradient descent or its variants.
    The flattening operation is a logical reshaping and does not affect the gradient flow; gradients
are simply propagated through the reshaped vector back to the convolutional layers.

11.34 Historical Perspective on CNNs
The development of convolutional neural networks has a rich history:
  • 1950s–1960s: Early inspirations for neural networks and pattern recognition.

  • 1980: Fukushima introduced the Neocognitron, a precursor to modern CNNs.

                                                  168
Intelligent Systems and Soft Computing        Introduction to Deep Learning and Neural Networks


  • 1998: LeCun et al. developed LeNet, applying CNNs to digit recognition with moderate
    success.

  • 2012: Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton published a landmark paper
    demonstrating an 8-layer CNN (AlexNet) that significantly outperformed previous methods
    on the ImageNet classification challenge.

  • Post-2012: Deeper networks with hundreds or thousands of layers (e.g., VGG, ResNet) have
    been developed, pushing the state-of-the-art in image recognition and other domains.
    AlexNet introduced several key innovations, such as using ReLU activations, dropout for regu-
larization, and GPU acceleration, which contributed to its success.

11.35 Key Hyperparameters in CNN Design
Designing an effective CNN requires careful selection of several hyperparameters:
  • Filter size: The spatial dimensions of convolutional kernels (e.g., 3 × 3, 5 × 5).

  • Stride: The step size with which the filter moves across the input.

  • Padding: Whether to add zeros around the input to control the spatial size of the output.

  • Pooling type and size: Max pooling, average pooling, and their window sizes and strides.

  • Number of filters: The depth of the output feature maps.
   These parameters are typically chosen based on empirical results, domain knowledge, and com-
putational constraints. For example, AlexNet used a stride of 4 in its first convolutional layer,
which was a design choice balancing computational eﬀiciency and feature extraction quality.

11.36 Regularization and Optimization Heuristics
Modern CNNs lean heavily on regularization layers and adaptive optimizers to reach peak accuracy.

Dropout. In convolutional stacks, dropout is typically applied after fully connected layers or
between residual blocks to decorrelate activations. Figure 38 visualizes the binary mask applied
during training and the characteristic training/validation curves: without dropout, the validation
error quickly diverges even though the training error keeps decreasing.

Batch normalization. BN accelerates convergence by normalizing mini-batch statistics and
learning scale/shift parameters. Figure 39 contrasts the pre- and post-normalization activation dis-
tributions; whitening the distribution keeps gradients in a well-behaved range and reduces covariate
shift.

Adaptive optimizers. While vanilla SGD remains a workhorse, Adam and related methods
adapt learning rates per-parameter. Figure 40 summarizes the typical loss trajectories; Adam
converges faster initially, whereas SGD+momentum often attains a slightly lower asymptote after
fine-tuning.


                                                169
Intelligent Systems and Soft Computing        Introduction to Deep Learning and Neural Networks



                       1




               loss   0.5




                       0
                            0   5   10   15   20         25   30      35   40   45   50
                                                     epoch
                                                   train (dropout)
                                                    val (dropout)
                                                   val (no dropout)


     Figure 38: Dropout effect on training/validation curves. Compared to a no-dropout baseline,
                      validation curves flatten and generalization improves.


 Summary
 Key takeaways
    • Convolutions introduce sparse connectivity and parameter sharing, dramatically reducing
      parameters vs. fully connected layers.

    • Padding and stride control spatial resolution; pooling aggregates features to build invari-
      ances.

    • Batch normalization, dropout, and optimizer choice strongly influence training stability
      and generalization.

    • Stacking small kernels expands the effective receptive field across depth.


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




                                                   170
Intelligent Systems and Soft Computing                                         Introduction to Recurrent Neural Networks


                                       Pre-BN activations                           Post-BN (per-channel)


                    0.4                                                      0.4
          density




                                                                  density
                    0.2                                                      0.2




                     0                                                        0
                      −6       −4        −2    0    2        4    6            −6   −4   −2    0      2    4   6
                                               x                                               x
                                                                                              channel 1
                                                                                              channel 2


     Figure 39: Batch normalization transforms per-channel activations toward zero mean and unit
                  variance prior to the learned aﬀine re-scaling, stabilizing training.

                              1
                      loss




                             0.5




                              0
                                   0          10        20              30          40        50          60
                                                                      epoch
                                                                 SGD+momentum
                                                                            Adam


     Figure 40: Representative training curves for SGD with momentum versus Adam on the same
                                                CNN.
```

### Findings
- **Backpropagation through CNNs:**
  - The statement "The flattening operation is a logical reshaping and does not affect the gradient flow" is generally correct but could benefit from clarification. Flattening changes the tensor shape but does not alter the underlying data or gradients; however, it is important to note that the gradient must be reshaped back appropriately during backpropagation to match the convolutional layer's output shape. This reshaping step should be explicitly mentioned to avoid confusion.

- **Historical Perspective on CNNs:**
  - The timeline and key milestones are accurate and well summarized.
  - The claim that LeNet had "moderate success" might be better qualified by noting that LeNet was pioneering for its time but limited by computational resources and dataset size.
  - The description of AlexNet's innovations is accurate; however, it might be worth mentioning the use of local response normalization (LRN) as another notable feature in AlexNet.

- **Key Hyperparameters in CNN Design:**
  - The listed hyperparameters are appropriate and well explained.
  - The example of AlexNet using a stride of 4 in the first convolutional layer is correct.
  - It might be helpful to explicitly mention the impact of these hyperparameters on the receptive field and computational cost for completeness.

- **Regularization and Optimization Heuristics:**
  - The description of dropout is accurate, but the statement "dropout is typically applied after fully connected layers or between residual blocks" could be expanded. Dropout can also be applied after convolutional layers, though less commonly, and its placement depends on architecture and task.
  - The explanation of batch normalization (BN) is good; however, the phrase "whitening the distribution" is somewhat misleading. BN normalizes activations to zero mean and unit variance but does not perform full whitening (decorrelation). This distinction should be clarified.
  - The description of adaptive optimizers is accurate. The note that Adam converges faster initially but SGD+momentum may reach a better final performance is consistent with empirical findings.
  - Figures 38, 39, and 40 are referenced appropriately, but the text should ensure that the figures clearly illustrate the described effects (e.g., the dropout mask, activation distributions, and loss curves).

- **Summary:**
  - The key takeaways are well stated and cover important concepts.
  - The point "Stacking small kernels expands the effective receptive field across depth" is correct but could be elaborated to explain why small kernels (e.g., 3×3) stacked in multiple layers are preferred over larger kernels (e.g., 7×7) in terms of parameter efficiency and nonlinearity.

- **References:**
  - The references are appropriate and correctly cited.
  - The URL for the Goodfellow et al. book is split across lines; ensure it is presented as a single clickable link in the final version.

- **Notation and Terminology:**
  - The notation is consistent throughout.
  - Terms like "stride," "padding," "dropout," "batch normalization," and "adaptive optimizers" are used correctly.
  - Some terms (e.g., "covariate shift") are used without definition; a brief explanation or reference would improve clarity.

- **Minor Typographical/Formatting Issues:**
  - In the dropout description, "decorrelate activations" might be better phrased as "reduce co-adaptation of neurons."
  - The phrase "vanilla SGD remains a workhorse" is informal; consider rephrasing for a formal lecture note.
  - The figure captions could be more descriptive, e.g., specify the dataset or model used in the training curves.

**Overall, the content is scientifically sound with minor clarifications and elaborations recommended for precision and completeness.**

## Chunk 69/104
- Character range: 449342–457456

```text
12    Introduction to Recurrent Neural Networks
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


                                                                 171
Intelligent Systems and Soft Computing                     Introduction to Recurrent Neural Networks


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

12.2    Key Idea: State and Memory in RNNs
Recurrent neural networks address this limitation by introducing a state vector ht that summarizes
information from all previous inputs up to time t. The state is updated recursively as new inputs
arrive, allowing the network to maintain a form of memory.
    Formally, at each time step t, the RNN receives an input vector xt and updates its hidden state
ht according to a function f parameterized by weights θ:



                                          ht = f (ht−1 , xt ; θ)                                  (12.1)

   The output yt at time t is then computed as a function of the current state:



                                             yt = g(ht ; θ′ )                                     (12.2)

    Here, f and g are typically nonlinear functions implemented by neural network layers, and θ, θ′
are learned parameters.

Interpretation: The hidden state ht acts as a summary or encoding of the entire input history
{x1 , x2 , . . . , xt }. This allows the network to make predictions that depend on the temporal context,
not just the current input.




                                                  172
Intelligent Systems and Soft Computing                   Introduction to Recurrent Neural Networks


12.3   Comparison with Feedforward Networks
To contrast, a feedforward network computes the output at time t as:



                                            yt = ϕ(xt ; θ)                                     (12.3)

    where ϕ is a nonlinear function without any dependence on past inputs. This limits the ability of
feedforward networks to model temporal dependencies unless the input vector xt explicitly contains
past information.

Summary: RNNs extend feedforward networks by incorporating a recurrent connection that
allows information to persist across time steps, enabling modeling of sequences and temporal dy-
namics.

12.4   Outline of Lecture 7
In this chapter, we will:
  • Formally define the architecture of recurrent neural networks.

  • Derive the forward and backward passes for training RNNs.

  • Discuss challenges such as vanishing and exploding gradients.

  • Introduce variants of RNNs designed to mitigate these challenges.

  • Explore applications where RNNs provide significant advantages over feedforward networks.
    Before proceeding, we will briefly revisit some concepts from last lecture that are relevant to
today’s material, including padding in convolutional networks and autoencoders, to ensure a solid
foundation.
    Detailed algebraic derivations (forward/backward passes and gradient expressions) appear in
Sections 12.11–12.12; readers are encouraged to work through the accompanying examples to solid-
ify intuition.

12.5   Recap: Feedforward Building Blocks
RNNs reuse the same ingredients as multilayer perceptrons—activations, nonlinear decision bound-
aries, loss functions, and training heuristics—but wrap them around a temporal axis. Figure 41
highlights the canonical MLP dataflow along with common activation choices and derivatives that
govern gradient flow.
    Two-dimensional toy datasets remain useful for reasoning about inductive biases. Figure 42
contrasts logistic regression and a shallow MLP on the moons dataset, illustrating how additional
hidden units carve nonlinear boundaries that RNN readouts later rely on when decoding the final
state.
    Finally, Figure 43 summarises two diagnostics: BCE geometry and the effect of learning‑rate
schedules/early stopping. We will reuse these when tuning sequence models, where overfitting
appears as a divergence between per‑token training and validation likelihood.

                                                 173
Intelligent Systems and Soft Computing                      Introduction to Recurrent Neural Networks


                       Common activations                              Derivatives

                              1   y                                            y
                                                                          1



                                                x
                                                                         0.5
                  −2                        2


                                                                                              x
                            −1                                 −2                         2



                               tanh x                                     1 − tanh2 x
                                σ(x)                                     σ(x)(1 − σ(x))
                              ReLU(x)                                      ReLU′ (x)


     Figure 41: Feedforward recap: popular activation functions and their derivatives, which govern
                      how gradients propagate through deep or recurrent stacks.




       Figure 42: Decision boundaries for logistic regression (left) versus a shallow MLP (right). The
        latter captures curved manifolds, a capability we reuse when mapping RNN hidden states to
                                                  outputs.


12.6     Limitations of Feedforward Neural Networks for Sequential Data
Feedforward neural networks (FNNs) process inputs in a fixed, non-temporal manner. Given an
input vector x, the network produces an output y without any explicit notion of order or memory
of past inputs. This characteristic makes FNNs ill-suited for tasks where the order of data points
is crucial, such as language modeling or time series prediction.

Example: Language Modeling               Consider the phrase:

                                      “The ball came out of the blue.”

Here, the meaning of the word “blue” depends heavily on its context and position in the sequence.
The phrase “out of the blue” is an idiomatic expression meaning something sudden or unexpected,
whereas “the ball was blue” refers to the color of the ball. A feedforward network that treats each
```

### Findings
- **No explicit issues with definitions or notation:** The lecture notes clearly define the key concepts such as the hidden state \( h_t \), input \( x_t \), output \( y_t \), and the functions \( f \) and \( g \) with their parameters. The notation is consistent and standard.

- **Logical flow and motivation are sound:** The motivation for RNNs is well-explained, emphasizing the inability of feedforward networks to handle temporal dependencies without explicit input augmentation, which becomes impractical for long histories.

- **Equation (12.1) and (12.2) are standard and correctly presented:** The recursive update of the hidden state and the output computation are standard formulations in RNN literature.

- **Comparison with feedforward networks (Equation 12.3) is accurate:** It correctly highlights the lack of temporal dependency in feedforward networks.

- **Summary and outline sections are clear and appropriate:** They set expectations for the rest of the chapter and link back to previous material.

- **Figures 41 and 42 are well integrated:** The explanation of activation functions and decision boundaries is relevant and supports understanding of RNN readouts.

- **Minor suggestions for improvement:**
  - The function \( f \) and \( g \) are said to be "typically nonlinear functions implemented by neural network layers," but it might be helpful to explicitly mention common choices (e.g., \( f \) often involves tanh or ReLU activations, \( g \) might be a softmax or linear layer depending on the task).
  - The phrase "the state vector \( h_t \) summarizes information from all previous inputs" is conceptually correct but could be qualified by noting that in practice, RNNs have limited capacity to remember very long histories due to issues like vanishing gradients (which are mentioned later).
  - The note about explicitly including previous inputs as part of the current input vector could mention the term "windowing" or "context window" to connect with common terminology.
  - The last paragraph in section 12.6 is cut off mid-sentence; it would be better to complete the example to fully illustrate the limitation of feedforward networks in language modeling.

- **No mathematical errors or inconsistencies detected.**

- **No ambiguous claims:** All claims are well-supported or standard knowledge in the field.

**Summary:** The chunk is well-written, scientifically accurate, and logically coherent. Minor clarifications and completion of the last example would improve clarity.

## Chunk 70/104
- Character range: 457459–465318

```text
174
Intelligent Systems and Soft Computing                               Introduction to Recurrent Neural Networks


                    BCE vs logit z                    Learning rate effect                   Early stopping
               6

                                                 1                                  1

               4




                                         loss




                                                                            loss
           L



                                                0.5                                0.5
               2



               0                                 0                                  0
                   −5       0        5                0      20        40                0       20         40
                            zy=1                             epoch                               epoch
                                                             conservative                          train
                             y=0
                                                              aggressive                              val


         Figure 43: Binary cross-entropy geometry (left), effect of learning-rate schedules on loss
       (middle), and the typical training/validation divergence that motivates early stopping (right).


word independently or as a fixed-size input vector without temporal context cannot distinguish
these meanings effectively.

Example: Predictive Text and Autocomplete When typing a query such as “I want to buy
...”, a model that understands the sequence can predict “teddy bear” as the next phrase. Changing
the context to “Write a book about Teddy...” leads to a different prediction, such as “Teddy
Roosevelt.” This demonstrates the importance of capturing the order and dependencies in the
input sequence.

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




                                                           175
Intelligent Systems and Soft Computing                     Introduction to Recurrent Neural Networks


Key Idea At each time step t, the RNN receives an input xt and updates its hidden state ht
based on the current input and the previous hidden state ht−1 :

                                  ht = f (Wxh xt + Whh ht−1 + bh )                            (12.4)
                                  yt = g(Why ht + by )                                        (12.5)

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

Historical Note: Hopfield Networks The first successful recurrent network was the Hop-
field network, which is a form of associative memory. Unlike modern RNNs, Hopfield networks
have symmetric weights and are designed to converge to stable states representing stored patterns.
While Hopfield networks are not directly used for sequence modeling, they laid the groundwork for
understanding recurrent architectures.

12.8    Mathematical Formulation of RNNs
Consider an input sequence {x1 , x2 , . . . , xT }, where each xt ∈ Rd . The RNN computes hidden
states {h1 , h2 , . . . , hT } and outputs {y1 , y2 , . . . , yT } as follows:

                          h0 = 0 (initial hidden state)                                       (12.6)
                          ht = f (Wxh xt + Whh ht−1 + bh ),           t = 1, . . . , T        (12.7)
                          yt = g(Why ht + by ),    t = 1, . . . , T                           (12.8)

12.9    Recurrent Neural Networks: Historical Context and Motivation
Recall from our earlier discussion on Hopfield networks that the configuration of the network states
significantly impacts the overall energy landscape. The sequence of states, or more precisely, their

                                                  176
Intelligent Systems and Soft Computing                    Introduction to Recurrent Neural Networks


spatial arrangement within the network, determines the energy and thus the network’s behavior.
This property endowed Hopfield networks with associative memory capabilities, as the weights were
constructed to ”remember” specific patterns.
   However, Hopfield networks were primarily designed for storage and retrieval of static patterns
rather than for dynamic prediction or forecasting tasks. Despite their introduction in 1982, their
practical utility beyond research was limited.

12.10 The 1986 Breakthrough: David Rumelhart et al.’s Recurrent Neural Net-
      work
In 1986, a seminal paper by David Rumelhart and collaborators introduced a novel recurrent neural
network (RNN) architecture inspired by—but distinct from—the Hopfield network. This work laid
the foundation for modern RNNs by explicitly modeling temporal dependencies and contextual
relationships in sequential data.
    The key insight was to capture the notion that elements appearing adjacently or in close proxim-
ity within a sequence have meaningful relationships. For example, in natural language processing, if
word A frequently co-occurs with word B, then the connection between their corresponding network
units should be strong and positive. Conversely, if A appears without B, this implies a negative or
weak connection.

Example: Word Associations - The words ”apple” and ”juice” often appear together, so the
connection between their representations is strong and positive. - The words ”apple” and ”car”
rarely co-occur, indicating a weak or negative connection. - Such associations reflect statistical
regularities in language and can be encoded in the network weights.

Implications This approach allowed the network to learn and represent contextual dependencies,
which are crucial for tasks like language modeling and sequence prediction. The 1986 paper explic-
itly referenced Hopfield networks as an inspiration but extended the concept to handle temporal
sequences and state transitions.

12.11 State Dynamics in Recurrent Neural Networks
The 1986 RNN formulation introduced the concept of a state that evolves over time as a function
of the previous state and the current input. Formally, the state update can be expressed as:
```

### Findings
- The figure caption for Figure 43 references "BCE vs logit z" on the left plot, but the plot itself is not fully described in the text. It would be helpful to explicitly define BCE (Binary Cross-Entropy) and clarify what "logit z" refers to, as well as how the geometry is illustrated.

- The notation in the example for stock price prediction uses subscripts xt−3, xt−2, xt−1, xt → x̂t+1 without explicitly defining the notation for the predicted value x̂t+1. While common, it would be clearer to state that x̂t+1 is the predicted value at time t+1.

- The explanation of feedforward networks requiring fixed-size inputs and the need for truncation or padding is accurate but could benefit from a brief mention of alternative approaches (e.g., attention mechanisms or convolutional networks) that can also handle variable-length inputs.

- In the RNN equations (12.4) and (12.5), the activation functions f(·) and g(·) are introduced, but the choice of g(·) as "softmax for classification" is somewhat narrow. It would be better to note that g(·) depends on the task and can be other functions (e.g., sigmoid for binary classification, identity for regression).

- The statement "The hidden state ht acts as a memory that captures information about all previous inputs x1, x2, ..., xt" is conceptually correct but should be qualified: in practice, standard RNNs have difficulty capturing long-range dependencies due to vanishing gradients.

- The historical note on Hopfield networks is accurate but could clarify that Hopfield networks are recurrent but not sequence models; they are energy-based associative memories, which is distinct from the temporal processing in RNNs.

- In section 12.8, the initial hidden state h0 is set to zero. It would be useful to mention that h0 can also be learned or initialized differently depending on the application.

- The description of the 1986 breakthrough by Rumelhart et al. is somewhat simplified. The original paper introduced backpropagation through time (BPTT) for training RNNs, which is a critical detail missing here.

- The example of word associations ("apple" and "juice" vs. "apple" and "car") is intuitive but could be misleading if taken literally; the network weights do not directly encode co-occurrence counts but rather learned representations that capture statistical dependencies.

- The last sentence ends abruptly ("Formally, the state update can be expressed as:") without providing the formal expression. This is a logical gap that should be completed for clarity.

- Minor formatting: some equations and text are not fully aligned or spaced consistently, which can affect readability (e.g., equation numbering and indentation).

## Chunk 71/104
- Character range: 465373–472671

```text
ht = f (ht−1 , xt ; θ),                              (12.9)

where
  • ht is the hidden state at time t,

  • xt is the input at time t,

  • f is a nonlinear function parameterized by θ (e.g., weights and biases),

  • ht−1 is the hidden state at the previous time step.


                                                 177
Intelligent Systems and Soft Computing                      Introduction to Recurrent Neural Networks


                             yt−1                  yt                 yt+1
                                Why                  Why                 Why
                                       Whh                  Whh
                             ht−1                  ht                 ht+1
                                Wxh                  Wxh                 Wxh
                             xt−1                 x
                                    shared unrolled
                                           parameters   across time
                                                    tin time          xt+1

     Figure 44: Unrolling an RNN reveals repeated application of the same parameters across time
        steps. This view motivates Backpropagation Through Time (BPTT), which accumulates
                    gradients through every copy before updating the shared weights.


   The output at time t, denoted yt , is typically computed as a function of the hidden state:

                                             yt = g(ht ; ϕ),                                  (12.10)

where g is another nonlinear function parameterized by ϕ.

Interpretation - The hidden state ht acts as a memory that summarizes information from all
previous inputs up to time t. - The recurrence allows the network to maintain context and model
temporal dependencies.

12.12 Unfolding the Recurrent Neural Network
To better understand and implement RNNs, it is common to unfold the network through time.
Unfolding transforms the recurrent structure into a feedforward network with shared weights across
time steps.

Process - Start with an initial hidden state h0 , which may be initialized to zero or learned. - At
each time step t, compute ht using Equation (12.1). - Compute output yt using Equation (12.2). -
The parameters θ and ϕ are shared across all time steps, enabling the network to generalize across
sequences of varying lengths.

Significance - Unfolding clarifies the flow of information and dependencies across time. - It
facilitates the application of backpropagation through time (BPTT) for training.

12.13 Mathematical Formulation of a Simple RNN Cell
Consider a simple RNN cell with the following update equations:

                                ht = σh (Whh ht−1 + Wxh xt + bh ) ,                           (12.11)
                                yt = σy (Why ht + by ) .                                      (12.12)




                                                   178
Intelligent Systems and Soft Computing                    Introduction to Recurrent Neural Networks


12.14 Recurrent Neural Network (RNN) Unfolding and Parameter Sharing
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

  • The weights mapping the hidden state at to the output yt are shared as well.
   This parameter sharing reduces the number of parameters to learn and enables the network to
generalize across different positions in the sequence.

12.15 Mathematical Formulation of the RNN
We formalize the RNN update equations as follows. Let the hidden state at time t be at ∈ Rh , the
input at time t be xt ∈ Rd , and the output at time t be yt ∈ Ro .



                                 at = σ (Wa at−1 + Wx xt + ba ) ,                           (12.13)
                                 yt = ϕ (Wy at + by ) ,                                     (12.14)

   where:
  • Wa ∈ Rh×h is the recurrent weight matrix (hidden-to-hidden).

  • Wx ∈ Rh×d is the input-to-hidden weight matrix.

  • Wy ∈ Ro×h is the hidden-to-output weight matrix.

  • ba ∈ Rh and by ∈ Ro are bias vectors.

  • σ(·) is the activation function for the hidden state (commonly tanh or ReLU).

  • ϕ(·) is the output activation function (e.g., softmax for classification).


                                                  179
Intelligent Systems and Soft Computing                      Introduction to Recurrent Neural Networks


Interpretation Equation (12.7) shows that the current hidden state at is a nonlinear transforma-
tion of the previous hidden state at−1 and the current input xt . Equation (12.2) maps the hidden
state to the output at time t.

Reusability of the Hidden State The hidden state at serves as a summary of all previous inputs
up to time t. This recursive formulation allows the network to capture temporal dependencies of
arbitrary length.

12.16 Generalized Notation
To simplify notation, define the concatenated input vector at time t:
                                              "    #
                                              at−1
                                         zt =        ∈ Rh+d .
                                               xt
   Correspondingly, define the combined weight matrix:
                                      h     i
                                   W = Wa Wx ∈ Rh×(h+d) .

   Then the hidden state update can be written compactly as:

                                         at = σ (Wzt + ba ) .                                   (12.15)

12.17 Recurrent Neural Network (RNN) Architectures and Loss Computation
Recall from previous discussions that the loss function for classification tasks often involves cross-
entropy terms of the form:                     X
                                        L=−       yi log ŷi ,                                (12.16)
                                                  i

where yi is the true label (often one-hot encoded) and ŷi is the predicted probability for class i.
When ŷ = y, the loss is zero, indicating perfect prediction.
    In the context of RNNs, the total loss over a sequence is typically the sum of losses at each time
step:
                                                    XT
                                           Ltotal =     Lt ,                                    (12.17)
                                                      t=1

where T is the sequence length.
```

### Findings
- **Equation numbering inconsistency:**  
  - The text references equations (12.1) and (12.2) in section 12.12, but these are not included in the provided chunk. Instead, equations (12.9), (12.10), (12.11), (12.12), (12.13), (12.14), (12.15), (12.16), and (12.17) appear. This may confuse readers if the earlier equations are not nearby or clearly referenced.

- **Notation inconsistency:**  
  - The hidden state is denoted as both \( h_t \) and \( a_t \) in different sections (e.g., \( h_t \) in 12.9–12.13, and \( a_t \) in 12.14–12.16). While this is common in literature, it should be explicitly stated that \( h_t \) and \( a_t \) represent the same concept to avoid confusion.  
  - Similarly, parameters are denoted as \( \theta \), \( \phi \), \( \Theta \), and \( \Theta_y \) in different places. A consistent notation or a clear mapping between these symbols would improve clarity.

- **Ambiguous or missing definitions:**  
  - The activation functions \( \sigma_h \), \( \sigma_y \), \( \sigma \), and \( \phi \) are introduced but not explicitly defined. For example, it is stated that \( \sigma(\cdot) \) is commonly tanh or ReLU, and \( \phi(\cdot) \) could be softmax, but this could be made clearer by explicitly defining these functions or giving examples.  
  - The term "nonlinear function" \( f \) and \( g \) are used without specifying their forms or typical choices, which might leave readers unclear about their nature.

- **Equation (12.16) loss function notation:**  
  - The loss function \( L = -\sum_i y_i \log \hat{y}_i \) is presented without specifying the domain of \( i \) (e.g., classes). It would be clearer to state that \( i \) indexes over classes.  
  - The statement "When \( \hat{y} = y \), the loss is zero" is only true if \( y \) is a one-hot vector and \( \hat{y} \) matches it exactly, which is a rare ideal case. This could be clarified to avoid misunderstanding.

- **Logical gaps or missing justifications:**  
  - The explanation of unfolding the RNN and parameter sharing is good, but the text could benefit from a brief mention of how BPTT handles the gradient flow through time steps and the potential issues like vanishing/exploding gradients.  
  - The concatenation of \( a_{t-1} \) and \( x_t \) into \( z_t \) in section 12.16 is introduced without explicitly stating the order of concatenation (though implied). It would be clearer to write \( z_t = \begin{bmatrix} a_{t-1} \\ x_t \end{bmatrix} \) explicitly.

- **Typographical and formatting issues:**  
  - In the figure caption, "shared unrolled parameters across time" is somewhat awkwardly phrased; "shared parameters across unrolled time steps" might be clearer.  
  - The figure itself is not visible here, but the text mentions "Why" and "Wxh" labels that seem misaligned or unclear in the ASCII art. This might confuse readers.

- **Minor suggestions:**  
  - When introducing the initial hidden state \( h_0 \), it is said it "may be initialized to zero or learned." It would be helpful to mention common practices or implications of each choice.  
  - The term "Reusability of the Hidden State" is used but might be better phrased as "Role of the Hidden State" or "Interpretation of the Hidden State" since "reusability" is not a standard term in this context.

Overall, the chunk is mostly correct and well-structured but would benefit from improved notation consistency, clearer definitions, and minor clarifications.

## Chunk 72/104
- Character range: 472713–480486

```text
Forward and Backward Passes in RNNs The forward pass involves propagating inputs
through the network over time steps t = 1, . . . , T , producing outputs ŷt at each step. After comput-
ing the loss, the backward pass computes gradients with respect to parameters by backpropagating
errors through time, a process known as Backpropagation Through Time (BPTT).
    BPTT unfolds the RNN across time steps and applies standard backpropagation through this
unrolled network. The key insight is that parameters are shared across time steps, so gradients
accumulate contributions from all time steps.



                                                  180
Intelligent Systems and Soft Computing                      Introduction to Recurrent Neural Networks


                           ∂L/∂ht+1     ∂L/∂ht+2         ∂L/∂ht+3   ∂L/∂ht+4




                       ht+0         ht+1        ht+2            ht+3       ht+4

                       xt+0         xt+1        xt+2            xt+3       xt+4

                              shared (Whh , Wxh , Why ) across time

      Figure 45: Backpropagation Through Time (BPTT): forward computation (black) unrolls
     across time, while gradients (red) propagate backwards, accumulating contributions from each
                              step before updating the shared parameters.




    Figure 46: Illustration of vanishing (blue) versus exploding (orange) gradient norms over many
            recurrent steps. Stable training aims to keep gradients within the grey band.


Vanishing and Exploding Gradients Because each gradient term contains products of Ja-
cobians such as ∂ht /∂ht−1 = Whh   ⊤ diag(σ ′ ), long sequences amplify eigenvalues of W . If the
                                           h                                             hh
spectral radius is below one the gradients decay exponentially (vanishing); if it is above one they
grow uncontrollably (exploding). Figure 46 illustrates both behaviours across time. Practical reme-
dies include gradient clipping, orthogonal or unitary recurrent matrices, layer normalization, and
gated architectures (LSTM/GRU) that introduce additive memory paths.

Parameter Updates At each time step, the gradient of the loss with respect to parameters (e.g.,
weights W ) depends on the chain of partial derivatives through the network states:

                                           ∂L   X ∂Lt
                                                    T
                                              =       .                                         (12.18)
                                           ∂W     ∂W
                                                    t=1


                                                   181
Intelligent Systems and Soft Computing                 Introduction to Recurrent Neural Networks




      Figure 47: Gradient norms with (green) and without (red) clipping, and the corresponding
                           training curves illustrating improved stability.


Because of parameter sharing, the same W influences multiple time steps, and the total gradient
is the sum over these contributions.

12.18 Stabilizing Recurrent Training
Gradient clipping. A practical safeguard is to clip the global norm of the gradient when it
exceeds a threshold. Figure 47 shows how clipping prevents the exploding case from destabilizing
optimisation while leaving the vanishing regime untouched.

Teacher forcing and scheduled sampling. Sequence-to-sequence models frequently feed the
ground-truth token back into the decoder during training (teacher forcing) to accelerate convergence.
Figure 48 depicts this contrasted with free-running inference, underscoring why scheduled sampling
is often introduced to narrow the gap between the two regimes.

Gated cells. LSTMs and GRUs alleviate vanishing gradients by introducing additive memory
paths guarded by gates. Figures 49 and 50 present the canonical cell diagrams used later in the
lecture when deriving the update equations.

Attention mechanisms. Even with gating, long sequences can challenge fixed-size hidden states.
Attention augments the decoder with a content-based lookup into the encoder states, as visualised
in Figure 51. Bright entries correspond to encoder positions that most influence each generated
token.

12.19 RNN Input-Output Configurations
RNNs can be configured in several ways depending on the task:
  • Many-to-Many (Equal Length): Input and output sequences have the same length T .
    For example, sequence labeling tasks.

  • Many-to-One: Input is a sequence of length T , output is a single prediction. Example:
    sentiment analysis where a sentence maps to a sentiment score.



                                                182
Intelligent Systems and Soft Computing                   Introduction to Recurrent Neural Networks




      Figure 48: Teacher forcing during training versus autoregressive decoding at test time. The
       mismatch motivates curriculum strategies that gradually replace ground-truth inputs with
                                         model predictions.


   • Many-to-Many (Unequal Length): Input and output sequences have different lengths.
     Example: machine translation where input and output sentences differ in length.

   • One-to-Many: Single input produces a sequence output. Less common, but applicable in
     tasks like image captioning where one image input generates a sequence of words.
   The main difference lies in how the loss is computed and how outputs are generated, but the
underlying backpropagation principles remain consistent.

12.20 Representing Words for RNN Inputs
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

                                                 183
Intelligent Systems and Soft Computing                         Introduction to Recurrent Neural Networks


                                                        ct



                                            ft          it          ot
                       xt                        LSTM
                                                    c̃t Cell
                                                                                   ht


                    ht−1

                                                      ct−1

        Figure 49: Long Short-Term Memory (LSTM) cell with input, forget, and output gates
                               regulating an internal memory cell ct .



                                                 zt            rt
                       xt                         GRU Cell                         ht


                    ht−1

     Figure 50: Gated Recurrent Unit (GRU) merges input and forget gates into update and reset
                       gates, yielding a lighter-weight alternative to LSTMs.


   For example, if |V | = 10, 000, the word ”house” might be represented as:

                                    whouse = [0, 0, . . . , 1, . . . , 0]T ,
```

### Findings
- The explanation of Backpropagation Through Time (BPTT) is generally accurate, but the notation in the partial derivative expression ∂ht /∂ht−1 = Whh ⊤ diag(σ ′ ) could be clarified:
  - It is not explicitly defined what σ′ represents; presumably, it is the derivative of the activation function applied element-wise, but this should be stated.
  - The transpose symbol ⊤ on Whh is used, but it is not explained why the transpose appears here; typically, the Jacobian involves the weight matrix and the derivative of the activation function, so a brief derivation or reference would help.
- The statement "long sequences amplify eigenvalues of W" is somewhat ambiguous:
  - More precisely, the product of Jacobians over time involves repeated multiplication by Whh and the derivative matrix, so the spectral radius of Whh (or the product) determines gradient behavior.
  - It would be clearer to say "the repeated multiplication of Jacobians involves powers of Whh, so the spectral radius of Whh governs whether gradients vanish or explode."
- Equation (12.18) is given as ∂L/∂W = Σ_t ∂L_t/∂W, but the notation ∂L_t/∂W is not defined:
  - It would be better to clarify that L_t is the loss at time step t, or the contribution to the total loss from time t.
  - Also, the chain rule application through time steps could be briefly mentioned to justify the summation.
- The description of gradient clipping as "clipping the global norm of the gradient" is correct, but it would be helpful to specify that this is typically done by scaling the gradient vector if its norm exceeds a threshold.
- The explanation of teacher forcing and scheduled sampling is good, but the term "curriculum strategies" is introduced without definition:
  - It would be clearer to briefly define scheduled sampling as a curriculum learning technique that gradually replaces ground-truth inputs with model predictions during training.
- The description of gated cells (LSTM/GRU) as introducing additive memory paths "guarded by gates" is accurate, but the term "additive memory paths" might be unclear to some readers:
  - A brief explanation that additive paths help preserve gradients by avoiding repeated multiplication would be beneficial.
- The attention mechanism description is concise but could benefit from a more precise explanation:
  - For example, stating that attention computes a weighted sum of encoder hidden states where weights are computed via a compatibility function between decoder state and encoder states.
- The RNN input-output configurations are well summarized, but the "One-to-Many" example (image captioning) is somewhat simplified:
  - Image captioning typically uses a CNN encoder followed by an RNN decoder; this could be mentioned to clarify the input modality difference.
- The vocabulary size discussion is informative but mixing headwords and total word forms might confuse readers:
  - It would be clearer to separate the concepts of dictionary size (headwords) and total inflected forms, emphasizing that the vocabulary size |V| used in models is often a fixed subset chosen for practical reasons.
- The one-hot encoding explanation is correct but could mention the inefficiency of this representation for large vocabularies and motivate the use of embeddings.
- Figures 45-51 are referenced appropriately, but the text should ensure that all symbols used in figures (e.g., ct, ft, it, ot in LSTM) are defined in the text or figure captions for completeness.

## Chunk 73/104
- Character range: 480488–487479

```text
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




                                                      184
Intelligent Systems and Soft Computing                   Introduction to Recurrent Neural Networks




       Figure 51: Attention heatmap for a translation model: each row corresponds to a decoder
     timestep querying encoder states, enabling long-range dependencies without storing everything
                                                  in ht .


12.21 Example: Sentiment Analysis with RNNs
Consider the sentence:
                                        ”This place is great.”

    Each word is first converted into a numerical vector (e.g., one-hot encoded). The sequence of
vectors is fed into the RNN, which processes them sequentially.
    For a many-to-one RNN (e.g., sentiment classification), we are interested in the hidden state
after processing the entire sentence. This final hidden state summarizes the contextual information
and can be fed into a classifier to predict the sentiment label.

12.22 Limitations of One-Hot Encoding in Natural Language Processing
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

                                                 185
Intelligent Systems and Soft Computing                 Introduction to Recurrent Neural Networks


Document similarity: Suppose we have two documents:

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

12.23 Feature-Based Word Representations
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




                                                186
Intelligent Systems and Soft Computing                    Introduction to Recurrent Neural Networks


         Word        Gender    Royalty    Age    Person    Fruit   Title   Abstract   Sweet
         man           1         0         1       1         0      0         0         0
         woman         0         0         1       1         0      0         0         0
         king          1         1         1       1         0      1         0         0
         queen         0         1         1       1         0      1         0         0
         orange        0         0         0       0         1      0         0         1
         apple         0         0         0       0         1      0         0         1
         monarch      0.5        1        0.5      1         0      1         0         0
         royal         0         1        0.5      0         0      1         1         0

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

Limitations:
  • Requires extensive manual effort to define and annotate features.

  • May not scale well to large vocabularies or complex semantics.

  • Diﬀicult to capture contextual nuances and polysemy.

12.24 Towards Distributed Word Representations
The feature-based approach motivates the idea of distributed representations, where each word
is represented as a dense vector in a continuous space. These vectors encode semantic and syntactic
properties implicitly, often learned from large corpora.

Key idea: Instead of one-hot vectors, represent each word w as a vector vw ∈ Rd , where d 
 |V |
(vocabulary size), such that:

                         similarity(vw , vw′ ) ≈ semantic similarity(w, w ′ )




                                                 187
Intelligent Systems and Soft Computing                   Introduction to Recurrent Neural Networks
```

### Findings
- The equation "Wembed = I|V|" is ambiguous and potentially misleading:
  - The identity matrix \( I_{|V|} \) is a fixed matrix of size \(|V| \times |V|\), but the embedding matrix \( W_{embed} \) is typically a learned parameter matrix of size \(|V| \times d\), where \( d \ll |V| \).
  - The notation \( W_{embed} = I_{|V|} \) suggests equality, which is not correct; rather, the embedding matrix is initialized or conceptually related to the identity matrix in the one-hot basis but then learned.
  - This should be clarified, e.g., "Conceptually, one-hot vectors correspond to rows of the identity matrix \( I_{|V|} \), but in practice, the embedding matrix \( W_{embed} \in \mathbb{R}^{|V| \times d} \) is learned."

- The statement "cosine similarity between any two distinct one-hot vectors is exactly zero" is correct but could be more precise:
  - Since one-hot vectors are orthogonal, their dot product is zero, and their cosine similarity is zero.
  - However, cosine similarity is undefined if vectors are zero vectors; here, one-hot vectors are non-zero, so the statement holds.

- The example sentences and document similarity section correctly illustrate the limitations of one-hot encoding but could benefit from explicitly defining "bag-of-words vectors" and clarifying that cosine similarity is applied to these count vectors.

- In the feature-based word representations section:
  - The table includes a "Title" feature, but it is not defined in the preceding list of features; this should be clarified or corrected.
  - The "Abstract" feature is listed but not explained in the text; its meaning is ambiguous.
  - The "Sweet" feature is used in the table but not mentioned in the feature list; it should be added or explained.
  - The "Age" feature is assigned 0.5 for "monarch" and "royal," but the rationale for this is not fully explained; "monarch" and "royal" are not typically age-related terms, so this may confuse readers.
  - The "Person" and "Fruit" features are binary indicators, but the text mentions "category" as a feature; the relationship between these should be clarified.

- The note "High-level categories are often represented with several binary indicators (person, fruit, title, abstract) rather than a single categorical feature" is good but could mention that this is a form of one-hot or multi-hot encoding of categorical variables.

- The limitations mention "difficult to capture contextual nuances and polysemy," which is accurate; it would be helpful to briefly mention that distributed representations (e.g., contextual embeddings) address this.

- In the "Towards Distributed Word Representations" section:
  - The notation \( d \ll |V| \) is implied but not explicitly stated; it would be clearer to mention that the embedding dimension \( d \) is typically much smaller than vocabulary size.
  - The similarity approximation \( similarity(v_w, v_{w'}) \approx semantic similarity(w, w') \) is a key idea but should be qualified as an empirical goal rather than a strict equality.

- Minor formatting:
  - The use of quotation marks is inconsistent (e.g., ”house” vs. "house"); standardize to ASCII quotes for clarity.
  - The phrase "cosine similarity on bag-of-words vectors" could be expanded to clarify that these vectors are frequency counts or TF-IDF weighted.

Overall, the content is scientifically sound but would benefit from clarifications and more precise definitions in the above points.

## Chunk 74/104
- Character range: 487481–495236

```text
Methods to obtain distributed representations Several approaches learn such embeddings
automatically from corpora, including neural language models (Word2Vec CBOW and Skip-gram),
matrix factorization methods (GloVe), and contextual models (ELMo, BERT). These methods
leverage co-occurrence statistics to place semantically similar words nearby in the embedding space.

12.25 Semantic Relationships in Word Embeddings
We continue our exploration of word embeddings by examining how semantic relationships between
words can be captured in vector space. The key insight, as demonstrated by Mikolov et al. (2013),
is that certain linguistic regularities and patterns manifest as linear relationships between word
vectors.

Example: Gender and Royalty Analogies              Consider the analogy involving gender and royalty:

                                    king − man + woman ≈ queen.

    This relationship suggests that the vector difference between king and man encodes the concept
of ”royal masculinity,” and adding the vector for woman shifts this to ”royal femininity,” yielding
a vector close to queen.
    More formally, if we denote the embedding of a word w as vw , then the analogy can be expressed
as:

                                    vking − vman + vwoman ≈ vqueen .                         (12.19)

   This vector arithmetic captures semantic relationships and can be used to find words that best
complete analogies by maximizing cosine similarity:

                                                                   
                             arg max cos vw , vking − vman + vwoman .
                                    w
                       ⊤
                     a b
   Here cos(a, b) = ∥a∥ ∥b∥ denotes cosine similarity between vectors a and b.


Empirical Validation Mikolov et al. showed that these relationships hold not only for gender
and royalty but also for other semantic categories such as family relations (e.g., uncle to aunt),
geographical locations (e.g., Portugal to Lisbon), and cultural concepts. The distances between
word vectors reflect meaningful semantic distances, such as:

                              kvman − vwoman k2 ≈ kvking − vqueen k2 ,

   and similarly for other pairs.

Geographical and Cultural Clustering Word embeddings also often (empirically) capture
geographic and cultural proximity. For example, the embeddings for countries and their capitals
frequently cluster together:




                                                  188
Intelligent Systems and Soft Computing                      Introduction to Recurrent Neural Networks




     Figure 52: Toy 2D projection of word embeddings showing neighbouring clusters (countries vs.
     capitals vs. royalty). Such scatter plots help sanity-check that analogies like vPortugal ≈ vLisbon
                                         hold in the learned space.




                      vPortugal ≈ vLisbon ,   vSpain ≈ vMadrid ,    vFrance ≈ vParis ,

    and countries that are geographically close tend to have embeddings closer in vector space (e.g.,
China is closer to Russia and Japan than to Portugal), although the strength of this effect depends
on the corpus used for training. Throughout this lecture, statements such as vPortugal ≈ vLisbon
are shorthand for “the cosine similarity between the vectors exceeds a data-dependent threshold
(typically > 0.8)” or, equivalently, that the two vectors lie in each other’s k-nearest-neighbour list
under cosine distance. These relations are empirical regularities rather than hard equalities, and
the precise neighbourhood structure depends on the corpus, training objective, and dimensionality
of the embedding space.

12.26 Feature-Based Representation vs. One-Hot Encoding
The success of word embeddings lies in their ability to represent words as dense vectors encoding
multiple latent features, as opposed to sparse one-hot vectors.

One-Hot Encoding One-hot encoding represents each word as a vector with a single 1 and zeros
elsewhere. This representation is:
   • Sparse: High-dimensional with mostly zeros (in the one-hot representation used here, the
     dimensionality equals the vocabulary size and only one entry is non-zero for each word).


                                                    189
Intelligent Systems and Soft Computing                        Introduction to Recurrent Neural Networks


  • Uninformative: No notion of similarity between words.

Feature-Based Embeddings In contrast, word embeddings are dense vectors in Rd (typically
d = 100 to 300) where each dimension can be interpreted as a latent feature capturing semantic or
syntactic properties. These features emerge from the training process rather than being explicitly
defined. The term “feature-based embedding” is non-standard in the literature; we use it here
simply to stress that the coordinates behave like automatically discovered features. Most papers
instead refer to these objects as dense distributed representations, and we always mean that same
concept. Unlike the hand-crafted example below, the latent dimensions of distributed embeddings
are not usually interpretable in isolation—they capture statistical regularities uncovered automati-
cally during training. Interpretability can sometimes be probed post hoc (e.g., via probing classifiers
or dimension alignment), but there is no guarantee that any single axis corresponds cleanly to a
human-understandable attribute.

Context Window Convention When we refer to the “context” of a word wt we mean the mul-
tiset of tokens that fall within a symmetric sliding window of radius c around position t. Formally,

                              Ct = { wt−c , . . . , wt−1 , wt+1 , . . . , wt+c }.

Directional variants sometimes use only the preceding words. The co-occurrence matrix in the next
section corresponds to the special case c = 1, where we only count the following token. Making the
window definition explicit removes ambiguity about which neighbouring words contribute counts
to Cij .

12.27 Open Questions: Feature Discovery and Representation
Two natural questions arise regarding the nature of these features:
  1. Who decides the features? Unlike manually engineered features, the features in word em-
     beddings are discovered automatically during training. There is no explicit human selection of
     features such as ”gender” or ”age.” Instead, the training algorithm uncovers latent dimensions
     that best capture word co-occurrence statistics.

  2. How are the feature values determined? The feature values (vector components) are
     learned by optimizing an objective function that encourages words appearing in similar con-
     texts to have similar embeddings. This is typically done via unsupervised or self-supervised
     learning on large corpora. In a self-supervised setting the model creates its own supervision
     signal—future tokens, masked tokens, or neighbouring sentences—so that no external labels
     are required.

Unsupervised Learning of Embeddings Although the learning is often called ”unsupervised,”
it is more accurately described as self-supervised learning because the training objective uses the
structure of the data itself (e.g., predicting context words) as supervision. In self-supervised setups



                                                     190
Intelligent Systems and Soft Computing                  Introduction to Recurrent Neural Networks


the model manufactures its own targets from the input (for example, masking a word and asking
the network to predict it), eliminating the need for manually annotated labels.

Summary Thus, the embedding process can be viewed as a function:

                                       f : Vocabulary → Rd ,
```

### Findings
- **Notation inconsistency in cosine similarity formula:**  
  The formula for cosine similarity is given as  
  \[
  \cos(a, b) = \|a\| \|b\|
  \]  
  which is incorrect. The correct formula is  
  \[
  \cos(a, b) = \frac{a^\top b}{\|a\| \|b\|}
  \]  
  This should be corrected to avoid confusion.

- **Ambiguity in notation for analogy search:**  
  The expression  
  \[
  \arg\max_w \cos(v_w, v_{king} - v_{man} + v_{woman})
  \]  
  is correct, but the notation in the text is somewhat unclear due to the placement of transpose and subscripts. It would be clearer to write explicitly:  
  \[
  \arg\max_{w \in V} \frac{v_w^\top (v_{king} - v_{man} + v_{woman})}{\|v_w\| \|v_{king} - v_{man} + v_{woman}\|}
  \]  
  where \(V\) is the vocabulary.

- **Use of “≈” symbol:**  
  The text uses “≈” (approximately equal) for vector equality (e.g., \(v_{Portugal} \approx v_{Lisbon}\)) and for vector arithmetic (e.g., \(v_{king} - v_{man} + v_{woman} \approx v_{queen}\)). It should be clarified that these are approximate equalities in terms of cosine similarity or nearest neighbors, not exact vector equalities.

- **Lack of explicit definition of cosine similarity:**  
  Although cosine similarity is mentioned, the formula is incorrectly given and no explicit definition is provided. A precise definition should be included, e.g.:  
  \[
  \cos(a, b) = \frac{a^\top b}{\|a\| \|b\|}
  \]

- **Missing explanation of why vector arithmetic works:**  
  The text states that vector differences encode semantic relationships but does not provide intuition or theoretical justification for why linear relationships emerge in embedding spaces. A brief explanation or reference to the underlying distributional hypothesis or embedding training objectives would strengthen the section.

- **“Feature-based embedding” terminology is non-standard:**  
  The text acknowledges this, but it might be better to consistently use the standard term “dense distributed representations” or “word embeddings” to avoid confusion.

- **Context window definition could be clearer:**  
  The context window \(C_t\) is defined as a multiset of tokens within radius \(c\), excluding the center word \(w_t\). It would be helpful to explicitly state that \(w_t\) is excluded from \(C_t\) to avoid ambiguity.

- **Inconsistent use of norm notation:**  
  The text uses \(\| \cdot \|_2\) in some places and \(\| \cdot \|\) in others without explicitly stating that \(\|\cdot\|\) denotes the Euclidean norm. Consistency and explicitness would improve clarity.

- **“Self-supervised” vs. “unsupervised” learning distinction:**  
  The text correctly points out that embedding learning is better described as self-supervised. However, it would be helpful to briefly define these terms or provide examples to clarify the distinction for readers unfamiliar with the concepts.

- **No mention of limitations or failure cases:**  
  The section could benefit from a brief note on known limitations of word embeddings, such as inability to capture polysemy in static embeddings or biases encoded in embeddings.

- **Figure 52 reference lacks description:**  
  The figure is mentioned as a “toy 2D projection” but no details are given about the method used for projection (e.g., PCA, t-SNE). Including this would help interpret the figure.

- **Equation numbering inconsistency:**  
  Equation (12.19) is referenced, but no other equations are numbered. For consistency, either number all equations or none.

- **Typographical issues:**  
  - The phrase “cosine distance” is used when “cosine similarity” is intended; these are different metrics. The text should consistently use “cosine similarity” when referring to similarity measures.  
  - The phrase “k-nearest-neighbour list under cosine distance” should be “k-nearest-neighbour list under cosine similarity” or “using cosine similarity as the distance metric.”

Overall, the content is scientifically sound but would benefit from these clarifications and corrections.

## Chunk 75/104
- Character range: 495239–502152

```text
where f is learned to encode semantic and syntactic properties implicitly, without explicit fea-
ture engineering. In matrix form we implement f by selecting the column of the learned embedding
matrix E corresponding to the word of interest.
    In practice we optimize objectives such as the continuous bag-of-words (CBOW) likelihood—
which predicts a center word from its surrounding context—and the skip-gram with negative sam-
pling (SGNS) loss—which predicts surrounding context words given a center word—using stochastic
gradient descent variants (SGD, Adam) on large corpora; these training regimes will be demon-
strated in the accompanying lab (see Section 13.6 for details).

12.28 Word Embedding via Recurrent Neural Networks
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

                        ”I like the sky.” and   ”I like the chocolate water.”

    then the vocabulary might be {I, like, the, sky, chocolate, water}, and Clike,the = 2 because the
word “the” follows “like” in both sentences, whereas Csky,I = 0 because “I” never follows “sky.” This
toy illustration uses the immediate successor as the context; production systems usually aggregate
statistics over wider, possibly symmetric windows.
    The co-occurrence matrix can be normalized to obtain conditional probabilities (for the adja-
cency window illustrated here):



                                                191
Intelligent Systems and Soft Computing                      Introduction to Recurrent Neural Networks



                                                          Cij
                                         P (wj | wi ) = P|V |        .                               (12.20)
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

         et = Ext ,                                       E ∈ Rde ×|V | ,                            (12.21)
        ht = tanh(Whh ht−1 + Wxh et + bh ),               Whh ∈ Rdh ×dh , Wxh ∈ Rdh ×de ,            (12.22)
                                                                         |V |×dh
        ŷt = softmax(Who ht + bo ),                      Who ∈ R                  .                 (12.23)

Here et is the learned embedding of the current word, ht is the hidden state summarising the
prefix w1 , . . . , wt , and ŷt ∈ R|V | is the predicted distribution over the vocabulary for the next word;
bh ∈ Rdh and bo ∈ R|V | are bias terms. For simplicity we often choose de = dh , but the formulation
above highlights that the embedding and hidden dimensions need not match.
     The training target is the actual next token in the sequence represented as a one-hot vector
yt . Cross-entropy loss between yt and ŷt therefore encourages the model to place high probability
on the observed next word (equivalently, the model maximises the log-likelihood of the observed
sequence). Empirical distributions derived from C (Equation (12.20)) are useful for analysis and
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



                                                    192
Intelligent Systems and Soft Computing                        Introduction to Recurrent Neural Networks


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
```

### Findings
- **Equation (12.20) notation ambiguity:**  
  The equation for conditional probability  
  \[
  P(w_j | w_i) = \frac{C_{ij}}{\sum_{k=1}^{|V|} C_{ik}}
  \]  
  is written with a confusing notation:  
  \[
  P(w_j | w_i) = P|V| \frac{C_{ij}}{k=1 C_{ik}}
  \]  
  The "P|V|" and denominator "k=1 C_{ik}" are not standard notation and appear to be a typesetting or transcription error. It should clearly be:  
  \[
  P(w_j | w_i) = \frac{C_{ij}}{\sum_{k=1}^{|V|} C_{ik}}
  \]  
  This should be corrected for clarity.

- **Inconsistent or unclear notation in matrix dimensions (Equation 12.23):**  
  The dimension of \( W_{ho} \) is given as  
  \[
  W_{ho} \in \mathbb{R}^{|V| \times d_h}
  \]  
  but the text shows a vertical fraction-like notation:  
  \[
  W_{ho} \in \mathbb{R}^{|V| \times d_h}
  \]  
  The notation is somewhat confusing and should be presented clearly as a matrix of size \(|V| \times d_h\).

- **Clarification on embedding matrix indexing convention:**  
  The text states that the embedding matrix \( E \in \mathbb{R}^{d_e \times |V|} \) has columns corresponding to word embeddings, but notes that some texts store embeddings as rows. This is correct but could be confusing to readers. It would be helpful to explicitly state that the choice of storing embeddings as columns or rows is a matter of convention and that the multiplication \( E x_t \) selects the embedding vector corresponding to the one-hot input \( x_t \).

- **Missing explicit definition of variables in equations:**  
  While most variables are defined, the bias terms \( b_h \) and \( b_o \) are introduced without explicit dimension definitions. For completeness, it would be good to state:  
  \[
  b_h \in \mathbb{R}^{d_h}, \quad b_o \in \mathbb{R}^{|V|}
  \]

- **Ambiguity in the phrase "predict the probability distribution of the next word given the previous words":**  
  The text says the RNN predicts the next word given previous words, but the input at time \( t \) is the current word \( x_t \). It might be clearer to say the RNN predicts \( y_t \) (the next word) given \( x_t \) and the hidden state summarizing previous words \( h_{t-1} \).

- **Potential confusion in the description of co-occurrence matrix \( C \):**  
  The text says \( C_{ij} \) counts how often word \( j \) appears in the context of word \( i \), treating context as the next word after \( i \). This is a valid but narrow definition of context. It would be helpful to explicitly state that this is a simplified example and that in practice, context windows are often symmetric and larger.

- **Minor typographical issues:**  
  - The phrase "de 
 V" likely intends to say "de << V" (embedding dimension much smaller than vocabulary size).  
  - The phrase "xt is one-hot, the multiplication Ext simply selects the column of E" is correct but could be more precise by stating that \( x_t \) is a one-hot column vector, so \( E x_t \) selects the corresponding column of \( E \).

- **No explicit mention of the vanishing gradient problem or limitations of simple RNNs:**  
  Since this section introduces RNNs for word embeddings, a brief mention of known issues with simple RNNs (e.g., vanishing gradients) and motivation for more advanced architectures (LSTM, GRU) could be beneficial for completeness.

- **No issues with the overall scientific content:**  
  The explanations of CBOW, SGNS, one-hot encoding, co-occurrence matrices, and RNN language models are accurate and consistent with standard literature.

---

**Summary:**  
- Fix notation in Equation (12.20) for conditional probability.  
- Clarify matrix dimension notation in Equation (12.23).  
- Explicitly define bias vector dimensions.  
- Clarify embedding matrix indexing conventions.  
- Improve clarity on RNN input-output relationship.  
- Explicitly state context window assumptions for co-occurrence matrix.  
- Minor typographical corrections.  
- Consider adding remarks on RNN limitations for completeness.

## Chunk 76/104
- Character range: 502158–509031

```text
Summary - Input words are represented as one-hot vectors. - A co-occurrence matrix captures
empirical next-word probabilities. - The RNN learns to predict the next word distribution given
the current word. - The embedding matrix E maps sparse one-hot vectors to dense de -dimensional
feature vectors. - Training is self-supervised, relying solely on raw text data without manual labels.
    Next, a natural progression is to study the Word2Vec algorithms (Skip-gram and CBOW) that
operationalize these ideas with eﬀicient shallow architectures.

12.29 Wrapping Up the Derivations
In this chapter, we have explored the foundational concepts behind modeling sequences in natural
language processing (NLP) using recurrent neural networks (RNNs). We began by considering the
problem of predicting the probability of a word given its preceding context, which is central to
language modeling.
    Recall that the goal is to estimate the conditional probability of a word wt given the sequence
of previous words w1 , w2 , . . . , wt−1 :

                                      P (wt | w1 , w2 , . . . , wt−1 ).                         (12.24)

   This probability can be modeled using an RNN, which maintains a hidden state ht that sum-
marizes the history up to time t:

                                                     ht = f (ht−1 , xt ; θ),                    (12.25)
                               P (wt | w1 , . . . , wt−1 ) = g(ht−1 ; θ),                       (12.26)

where xt is the input representation (e.g., word embedding) of the word wt , f is the recurrent update
function parameterized by θ, and g maps the hidden state to a probability distribution over the
vocabulary. Because the hidden state is computed recursively, ht−1 already aggregates information
about the entire prefix (w1 , . . . , wt−1 ); predicting wt from ht−1 therefore reflects the Markovian
summary that RNNs maintain. Explicitly, repeatedly substituting Equation (12.7) reveals that



                                                    193
Intelligent Systems and Soft Computing                           Introduction to Recurrent Neural Networks


ht−1 = f (f (· · · f (h0 , x1 ), . . .), xt−1 ), so no information is lost other than the compression inherent
to the finite-dimensional state vector.

Training Objective The network is trained to maximize the likelihood of the observed sequences
in a large corpus of text. Given a training sequence (w1 , w2 , . . . , wT ), the log-likelihood is:

                                          X
                                          T
                                 L(θ) =         log P (wt | w1 , . . . , wt−1 ; θ).                   (12.27)
                                          t=1

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
                                          x t = E ⊤ ew t ,                               (12.28)

so E[wt ] simply selects the row of E associated with wt . The boldface E[ · ] notation is intentional:
it denotes array indexing into the learnable embedding matrix rather than an expectation operator
E[·]. Whenever expectations appear later in the notes we write them explicitly as E[·] to avoid
overload.

Summary of the Modeling Pipeline
   1. Collect a large corpus of text data.

   2. Tokenize the text into sequences of words.

   3. Represent words as embeddings (initialized from a lookup table that is learned jointly with
      the network parameters).

   4. Use an RNN to process sequences and produce hidden states.

   5. Predict the next word probability distribution from the hidden state.


                                                       194
Intelligent SystemsLecture
                    and Soft
                           8 Part
                             Computing
                                  I: Neural Network Applications in Natural Language Processing


  6. Train the model by maximizing the likelihood of the observed sequences.
 Summary
 Key takeaways
     • Language modeling is trained with self-supervision by maximizing next-token likelihood.

     • Embeddings provide dense, learned word features; RNN hidden states encode context.

     • Stability tools (clipping, gating, attention) enable long-range dependency modeling.


References
  • Jurafsky, D., & Martin, J. H. (2023). Speech and Language Processing (3rd ed.). Draft
    chapters available online.

  • Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.

  • Mikolov, T., Karafiát, M., Burget, L., Černocký, J., & Khudanpur, S. (2010). Recurrent
    neural network based language model. Interspeech.
   Suggested reading: Chapter 10 of Goodfellow, Bengio, and Courville (2016) for RNN funda-
mentals and Mikolov et al. (2013) for the original Word2Vec formulation.


13     Lecture 8 Part I: Neural Network Applications in Natural Lan-
       guage Processing
13.1   Context and Motivation
In this chapter, we conclude our discussion on neural networks by focusing on their applications in
natural language processing (NLP). Previously, we introduced the concept of representing words
as inputs to a neural network, typically encoded as one-hot vectors, and obtaining as output a
feature representation of these words. This feature representation captures semantic and syntactic
properties of words in a continuous vector space.
    A classic example illustrating the power of such representations is the analogy:

                                  king − man + woman ≈ queen.

This demonstrates that vector arithmetic on word embeddings can capture meaningful relationships
between words. The goal is to find a vector space embedding where semantic similarity corresponds
to geometric closeness.
```

### Findings
- **Notation and Definitions:**
  - The notation \( e_{w_t} \) is introduced as the one-hot indicator vector for word \( w_t \), which is good. However, it would be clearer to explicitly define the dimension of \( e_{w_t} \) as \( V \) (vocabulary size) to avoid ambiguity.
  - The embedding lookup is written as \( x_t = E^\top e_{w_t} \). This is correct but somewhat unconventional; typically, the embedding matrix \( E \in \mathbb{R}^{V \times d} \) is multiplied on the left by the one-hot vector \( e_{w_t}^\top \) to yield a \( d \)-dimensional vector: \( x_t = E^\top e_{w_t} \) or equivalently \( x_t = E[w_t] \). The text clarifies this, but a brief note on the shape of \( E \) and \( e_{w_t} \) would help.
  - The boldface notation \( E[\cdot] \) is used for indexing into the embedding matrix, which is a good clarification to avoid confusion with expectation \( \mathbb{E}[\cdot] \).

- **Equations (12.25) and (12.26):**
  - Equation (12.25) defines the hidden state update \( h_t = f(h_{t-1}, x_t; \theta) \), which is standard.
  - Equation (12.26) states \( P(w_t | w_1, \ldots, w_{t-1}) = g(h_{t-1}; \theta) \). This is slightly inconsistent because the hidden state at time \( t-1 \) is used to predict \( w_t \), but the input at time \( t \) is \( x_t \) (embedding of \( w_t \)). Usually, the prediction of \( w_t \) is made from \( h_t \), which incorporates \( x_t \). The text uses \( h_{t-1} \) for prediction, which is acceptable if the model predicts \( w_t \) before seeing \( x_t \), but this should be explicitly stated to avoid confusion.
  - More commonly, the RNN processes \( x_t \) to produce \( h_t \), and then \( h_t \) is used to predict \( w_{t+1} \). The text’s formulation is consistent with predicting \( w_t \) from \( h_{t-1} \), but this subtlety should be clarified.

- **Markovian Summary Claim:**
  - The text states that \( h_{t-1} \) aggregates information about the entire prefix \( (w_1, \ldots, w_{t-1}) \), which is true in theory.
  - However, it should be noted that this is an approximation due to the finite-dimensional hidden state and potential vanishing gradient issues in practice. The phrase "no information is lost other than the compression inherent to the finite-dimensional state vector" is accurate but could be emphasized more as an approximation.

- **Training Objective (Equation 12.27):**
  - The log-likelihood objective is correctly stated.
  - It might be helpful to mention that the model parameters \( \theta \) include both the RNN parameters and the embedding matrix \( E \), as embeddings are learned jointly.

- **Self-Supervised Learning Explanation:**
  - The explanation of self-supervised learning is clear and accurate.
  - The example "the model learns that the word 'juice' often follows 'apple'" is intuitive and well-chosen.

- **Summary of Modeling Pipeline:**
  - Step 3 mentions embeddings initialized from a lookup table learned jointly with the network parameters. It might be worth noting that embeddings can also be pre-trained and fine-tuned or fixed, depending on the application.
  - Step 5 states "Predict the next word probability distribution from the hidden state," which aligns with the earlier equations.

- **Summary Key Takeaways:**
  - The mention of "stability tools (clipping, gating, attention)" is appropriate but somewhat abrupt. Since attention mechanisms are not introduced in this chapter, a brief note or reference to later chapters would help contextualize this.

- **Word2Vec Mention:**
  - The text mentions Word2Vec (Skip-gram and CBOW) as a natural progression, which is appropriate.
  - However, it would be beneficial to briefly state how Word2Vec differs from RNN language models (e.g., shallow architectures, different training objectives) to prepare the reader.

- **Analogy Example:**
  - The analogy "king − man + woman ≈ queen" is a classic and well-chosen example.
  - It might be helpful to mention that this property emerges from the geometry of the embedding space learned by models like Word2Vec or GloVe, not necessarily from RNNs directly.

- **References and Suggested Reading:**
  - The references are appropriate and up-to-date.
  - The suggested reading aligns well with the content.

**Overall, the chunk is well-written and technically sound with minor clarifications needed on notation and the timing of predictions in the RNN.**

## Chunk 77/104
- Character range: 509033–516290

```text
13.2   Problem Statement
Given a vocabulary (corpus) of approximately 10,000 words, we want to learn a mapping from
each word to a dense vector representation in a feature space of dimension d, where d is typically
between 200 and 500. Formally, if the vocabulary size is V , each word wi is initially represented as



                                                195
Intelligent SystemsLecture
                    and Soft
                           8 Part
                             Computing
                                  I: Neural Network Applications in Natural Language Processing


a one-hot vector xi ∈ RV , where                
                                                1   if j = i,
                                        xij =
                                                0   otherwise.

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

Example:      The word pretty can have different meanings depending on context:
   • In the collocation “pretty good,” pretty functions as an adverb meaning “very” and modifies
     an adjective.

   • In phrases such as “pretty image” or “pretty optics,” pretty is an adjective meaning “attrac-
     tive.”
By explicitly examining the surrounding words (context windows of a few tokens to the left and
right), we can infer the intended meaning: instances co-occurring with evaluative adjectives like
“good” teach the “intensifier” sense, whereas contexts rich in nouns like “image” teach the “aesthetic”
sense.

13.4    Contextual Meaning and Feature Extraction
Words appear in many different contexts, and by aggregating information from these contexts, we
can infer intrinsic features of the word. For example, the contexts in which pretty appears with
good or image help us understand its different senses.
   This motivates the use of statistical models that learn word embeddings by analyzing large
corpora and capturing co-occurrence patterns.

13.5    Word2Vec: Two Architectures
The Word2Vec framework, introduced by Mikolov et al., operationalizes the distributional hypoth-
esis through two main architectures:
   1. Continuous Bag of Words (CBOW): Predicts the target word given its surrounding
      context words.

                                                  196
Intelligent SystemsLecture
                    and Soft
                           8 Part
                             Computing
                                  I: Neural Network Applications in Natural Language Processing


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

13.5.2    Skip-Gram
Conversely, the Skip-Gram model takes the target word as input and tries to predict each of the
context words. It maximizes            Y
                                            p(wc | wt ).
                                              wc ∈Ct

The product makes the modeling assumption explicit: every context word within the window con-
                                                                                  P
tributes a likelihood factor. In practice we maximize the sum of log-probabilities wc ∈Ct log p(wc |
wt ) so that each neighbouring prediction provides an additive gradient signal.
    This approach tends to perform better on infrequent words and captures more detailed semantic
relationships.

13.6     Mathematical Formulation of CBOW
Let the vocabulary size be V , and embedding dimension be d. Define the embedding matrix
W ∈ RV ×d , where the i-th row vi is the embedding vector for word wi .

13.7     Neural Network Architecture for Word Embeddings
Consider a corpus with vocabulary size V = 10, 000 words. Our goal is to learn a dense vector
representation (embedding) for each word in this vocabulary. We denote the dimensionality of the
embedding space as d = 300.


                                                       197
Intelligent SystemsLecture
                    and Soft
                           8 Part
                             Computing
                                  I: Neural Network Applications in Natural Language Processing


Input Representation Each input word is represented as a one-hot vector x ∈ RV , where only
one element is 1 (corresponding to the word index) and the rest are 0. For example, if the word
”want” is the i-th word in the vocabulary, then xi = 1 and xj = 0 for j 6= i.

Network Structure We consider a simple feedforward neural network with:
   • An input layer of size V (one-hot encoded words).

   • A hidden layer of size d = 300, which will serve as the embedding layer.

   • An output layer of size V , which predicts the target word.
   The weight matrix between the input and hidden layer is denoted as

                                            W ∈ RV ×d .

Each row Wi,: corresponds to the embedding vector of the i-th word.

Forward Pass Given an input word represented by x, the hidden layer output h ∈ Rd is computed
as:

                                             h = x⊤ W,                                         (13.1)

where x⊤ is a 1 × V vector and W is V × d, resulting in h of size 1 × d.
   Because x is one-hot, this operation simply selects the row of W corresponding to the input
word, i.e., the embedding vector for that word.

Output Layer The hidden layer output h is then multiplied by another weight matrix W ′ ∈ Rd×V
to produce the output logits z ∈ RV :

                                             z = hW ′ .                                        (13.2)

   These logits are then passed through a softmax function to produce a probability distribution
over the vocabulary:
```

### Findings
- **Notation inconsistency for embedding matrix W**:  
  - In section 13.6, the embedding matrix W is defined as \( W \in \mathbb{R}^{V \times d} \) with rows \( v_i \) as embeddings.  
  - In section 13.7, the same notation \( W \in \mathbb{R}^{V \times d} \) is used for the weight matrix between input and hidden layer, which is consistent. However, the text states "Each row \( W_{i,:} \) corresponds to the embedding vector of the i-th word," which is correct.  
  - Later, the output weight matrix is denoted as \( W' \in \mathbb{R}^{d \times V} \). This is standard but the prime notation \( W' \) is introduced without explicit definition or explanation. It would be clearer to explicitly define \( W' \) as the output weight matrix.

- **Ambiguity in the definition of the embedding function \( f \)**:  
  - The function \( f: \{1, \ldots, V\} \to \mathbb{R}^d \) is introduced as the embedding function mapping word indices to vectors. However, it is not explicitly stated that \( f(i) = W_{i,:} \), i.e., the i-th row of the embedding matrix. Adding this would clarify the connection between the embedding matrix and the embedding function.

- **Missing explicit definition of softmax function**:  
  - The softmax function is mentioned as applied to logits \( z \) to produce a probability distribution over the vocabulary, but the formula for softmax is not given. Including the formula  
    \[
    \text{softmax}(z)_j = \frac{e^{z_j}}{\sum_{k=1}^V e^{z_k}}
    \]
    would improve clarity.

- **Inconsistent use of indexing notation**:  
  - The one-hot vector \( x_i \in \mathbb{R}^V \) is defined with indices \( j \) for the vector components, but sometimes the text uses \( x_{ij} \) which could be misread as a matrix element. It would be clearer to denote the one-hot vector components as \( x_j \) or \( x^{(i)}_j \) to avoid confusion.

- **Lack of explicit mention of bias terms in the neural network**:  
  - The neural network architecture described (input → hidden → output) does not mention bias vectors at the hidden or output layers. While some Word2Vec implementations omit biases, it should be stated explicitly whether biases are included or not.

- **Clarification needed on CBOW input representation**:  
  - In section 13.5.1, it is stated that context words are represented as one-hot vectors and combined (e.g., averaged) to form the input. It would be helpful to specify that the combined vector is the average (or sum) of the one-hot vectors, resulting in a sparse vector with fractional values, which is then multiplied by the embedding matrix.

- **Mathematical expression in Skip-Gram section (13.5.2) could be clearer**:  
  - The product notation  
    \[
    \prod_{w_c \in C_t} p(w_c | w_t)
    \]
    is used but the text writes it as  
    \[
    Y p(w_c | w_t)
    \]
    which is ambiguous. It should be explicitly written as a product symbol \(\prod\) rather than \(Y\), which could be misread as a variable.

- **Minor typographical issues**:  
  - In the phrase "the product makes the modeling assumption explicit," "modeling" is spelled in British English; consistency with other spellings should be checked.  
  - The phrase "wc ∈Ct log p(wc | wt )" is missing summation notation; it should be  
    \[
    \sum_{w_c \in C_t} \log p(w_c | w_t)
    \]
    for clarity.

- **No explicit mention of negative sampling or hierarchical softmax**:  
  - While Word2Vec is introduced, the notes do not mention common optimization techniques like negative sampling or hierarchical softmax, which are important for practical training. A brief mention or a pointer to these methods would be beneficial.

- **No issues spotted regarding the distributional hypothesis and examples**:  
  - The explanation of the distributional hypothesis and the example with "pretty" is clear and accurate.

Overall, the chunk is mostly correct and well-explained but would benefit from clarifications and minor corrections as noted above.

## Chunk 78/104
- Character range: 516292–524235

```text
exp(zj )
                                ŷj = PV            ,     j = 1, . . . , V.                    (13.3)
                                       k=1 exp(zk )

Training Objective The target output y is also a one-hot vector corresponding to the word we
want to predict (e.g., the word ”automatic”). The training objective is to minimize the cross-entropy
loss between the predicted distribution ŷ and the target y:

                                               X
                                               V
                                        L=−          yj log ŷj .                              (13.4)
                                               j=1




                                                198
Intelligent SystemsLecture
                    and Soft
                           8 Part
                             Computing
                                  I: Neural Network Applications in Natural Language Processing


Backpropagation and Weight Updates During training, the weights W and W ′ are updated
via backpropagation to minimize L. This process adjusts the embeddings in W so that words
appearing in similar contexts have similar vector representations.

13.8   Context Window and Sequential Input
Suppose we use a context window of size 4 words surrounding the target word. For example, to
predict the word ”automatic”, the context words might be:

                                    want,    by,    and,   caught.

   Each context word is represented as a one-hot vector and fed sequentially into the network.
Each one-hot vector is fully connected to the hidden layer, sharing the same weight matrix W .

Input Sequence Processing The input sequence is processed as:

                      x(1) → h(1) = (x(1) )⊤ W,    x(2) → h(2) = (x(2) )⊤ W,   ...

   The hidden representations h(i) for each context word can be combined (e.g., concatenated or
averaged) before passing to the output layer to predict the target word.

Dimensionality and Sparsity Note that the input vectors x(i) are extremely sparse (one-hot),
and the weight matrix W is large (10, 000 × 300). However, the multiplication x⊤ W is eﬀicient
because only one row of W is selected per input word.

13.9   Interpretation of the Weight Matrix W
The matrix W can be interpreted as a lookup

13.10 Word Embeddings: Continuous Bag of Words (CBOW) and Skip-Gram
      Models
Recall from the previous discussion that word embeddings are dense vector representations of words
learned from large corpora, capturing semantic and syntactic properties. Two foundational models
for learning such embeddings are the Continuous Bag of Words (CBOW) and Skip-Gram models,
both introduced in the Word2Vec framework.

13.10.1   Continuous Bag of Words (CBOW)
In CBOW, the objective is to predict a target word given its surrounding context words. Formally,
given a sequence of words w1 , w2 , . . . , wT , and a context window of size c, the model predicts the
word wt based on the context words {wt−c , . . . , wt−1 , wt+1 , . . . , wt+c }.
    The input to the model is a one-hot encoded vector representing the context words. Since each
word is represented as a one-hot vector of dimension V (the vocabulary size), the input is a sparse
vector with a single 1 and zeros elsewhere. The embedding matrix W ∈ RV ×N maps each word to
an N -dimensional dense vector (embedding).
    The CBOW model computes the average of the embeddings of the context words:

                                                   199
Intelligent SystemsLecture
                    and Soft
                           8 Part
                             Computing
                                  I: Neural Network Applications in Natural Language Processing




                                           1 X
                                      h=       W⊤ xt+j                                        (13.5)
                                           2c
                                             −c≤j≤c
                                              j̸=0


    where xt+j is the one-hot vector for the context word at position t + j, and c denotes the
half-window size (there are 2c context words around wt when the document is long enough).
    This hidden representation h is then used to predict the target word wt via a softmax layer:

                                                                    
                                                        exp u⊤
                                                             wt h
                                P (wt | context) = PV                                         (13.6)
                                                                 ⊤
                                                        w=1 exp(uw h)

   where uw is the output vector corresponding to word w. It is useful to think of the set of output
vectors as the rows of a second matrix U ∈ RV ×N ; although U often starts as a copy of W, the
two sets of embeddings are optimized independently during training.
   Training proceeds by maximizing the log-likelihood over the corpus, adjusting the embedding
matrix W and output vectors uw to improve prediction accuracy. After suﬀicient training, the
rows of W serve as the learned word embeddings.

Key Insight: Because the input vectors are one-hot encoded, the multiplication W⊤ xt+j simply
selects the embedding vector corresponding to the context word wt+j . This makes the embedding
matrix W a lookup table of word features.

13.10.2   Skip-Gram Model
The Skip-Gram model reverses the CBOW objective: it uses the current word to predict its sur-
rounding context words. Given a center word wt , the model aims to maximize the probability of
each context word wt+j within a window c:


                                         Y
                                                 P (wt+j | wt )                               (13.7)
                                        −c≤j≤c
                                         j̸=0

   The input is the one-hot vector xt representing the center word, which is projected into the
embedding space via the matrix W ∈ RV ×N :



                                            h = W ⊤ xt                                        (13.8)

   Each context word wt+j is predicted by applying a softmax over the output vectors (again using
the output-embedding matrix U):




                                                  200
Intelligent SystemsLecture
                    and Soft
                           8 Part
                             Computing
                                  I: Neural Network Applications in Natural Language Processing



                                                               
                                                   exp u⊤wt+j h
                                 P (wt+j | wt ) = PV                                         (13.9)
                                                              ⊤
                                                    w=1 exp(uw h)

   where uw are the output vectors as before.

Training Objective: Maximize the log-likelihood of the context words given the center word
over the entire corpus.

Interpretation: The Skip-Gram model learns embeddings such that words appearing in similar
contexts have similar vector representations.

13.10.3   Computational Challenges: Softmax Normalization
Both CBOW and Skip-Gram models require computing the softmax normalization over the entire
vocabulary V , which can be very large (e.g., V = 10, 000 or more). The denominator in equations
(13.6) and (13.9) involves summing exponentials over all vocabulary words:


                                            X
                                            V             
                                       Z=         exp u⊤
                                                       w h                                 (13.10)
                                            w=1
```

### Findings
- **Equation (13.3) formatting and clarity**: The equation for \(\hat{y}_j\) is given as  
  \[
  \hat{y}_j = \frac{\exp(z_j)}{\sum_{k=1}^V \exp(z_k)}, \quad j=1,\ldots,V.
  \]  
  However, the notation "PV" in the denominator is ambiguous and likely a formatting error. It should be explicitly written as \(\sum_{k=1}^V \exp(z_k)\) for clarity.

- **Cross-entropy loss (13.4)**: The loss is defined as  
  \[
  L = -\sum_{j=1}^V y_j \log \hat{y}_j.
  \]  
  This is correct for a one-hot target vector \(y\). It would be helpful to explicitly state that \(y_j\) is a one-hot vector (i.e., \(y_j=1\) for the correct class and 0 otherwise) to avoid ambiguity.

- **Backpropagation and weight updates**: The text states that weights \(W\) and \(W'\) are updated via backpropagation to minimize \(L\), adjusting embeddings so that words in similar contexts have similar vectors. This is conceptually correct but could benefit from a brief mention that \(W\) and \(W'\) correspond to input and output embedding matrices, respectively, to avoid confusion.

- **Context window example**: The example context words for predicting "automatic" are given as "want, by, and, caught." It would be clearer to specify the order of these context words relative to the target word (e.g., two words before and two words after) to avoid ambiguity.

- **Input sequence processing notation**: The notation  
  \[
  x^{(1)} \to h^{(1)} = (x^{(1)})^\top W, \quad x^{(2)} \to h^{(2)} = (x^{(2)})^\top W, \ldots
  \]  
  is correct, but the use of superscripts for indexing time steps or positions should be explicitly defined to avoid confusion with exponentiation.

- **Dimensionality and sparsity**: The explanation that \(x^\top W\) is efficient because \(x\) is one-hot and selects a single row of \(W\) is accurate and well-stated.

- **Section 13.9 incomplete**: The sentence "The matrix \(W\) can be interpreted as a lookup" is incomplete and should be finished (e.g., "lookup table for word embeddings").

- **Equation (13.5) averaging in CBOW**: The formula  
  \[
  h = \frac{1}{2c} \sum_{\substack{-c \leq j \leq c \\ j \neq 0}} W^\top x_{t+j}
  \]  
  is correct, but the notation \(W^\top x_{t+j}\) implies \(W \in \mathbb{R}^{V \times N}\) and \(x_{t+j} \in \mathbb{R}^V\), so \(W^\top x_{t+j}\) yields an \(N\)-dimensional vector. This is consistent but should be explicitly stated to avoid confusion.

- **Equation (13.6) softmax for CBOW**:  
  \[
  P(w_t | \text{context}) = \frac{\exp(u_{w_t}^\top h)}{\sum_{w=1}^V \exp(u_w^\top h)}
  \]  
  is correct. However, the notation \(u_w\) as output vectors and \(U \in \mathbb{R}^{V \times N}\) should be clearly defined before use.

- **Clarification on \(W\) and \(U\)**: The note that \(U\) often starts as a copy of \(W\) but is optimized independently is good. It might be helpful to mention that \(W\) is the input embedding matrix and \(U\) is the output embedding matrix to avoid confusion.

- **Equation (13.7) Skip-Gram objective**:  
  \[
  \prod_{\substack{-c \leq j \leq c \\ j \neq 0}} P(w_{t+j} | w_t)
  \]  
  is correct as the product over context words. It would be clearer to write the log-likelihood explicitly since training maximizes the sum of log probabilities.

- **Equation (13.8) Skip-Gram embedding**:  
  \[
  h = W^\top x_t
  \]  
  is consistent with previous notation.

- **Equation (13.9) Skip-Gram softmax**:  
  \[
  P(w_{t+j} | w_t) = \frac{\exp(u_{w_{t+j}}^\top h)}{\sum_{w=1}^V \exp(u_w^\top h)}
  \]  
  is correct.

- **Equation (13.10) softmax normalization**: The denominator  
  \[
  Z = \sum_{w=1}^V \exp(u_w^\top h)
  \]  
  is correctly stated.

- **Minor formatting issues**: There are some formatting artifacts (e.g., "PV" instead of \(\sum_{k=1}^V\), misplaced parentheses, and line breaks) that should be cleaned up for clarity.

- **Missing definitions**:  
  - The vocabulary size \(V\) and embedding dimension \(N\) are used but not explicitly defined in this chunk.  
  - The notation for vectors and matrices (e.g., whether vectors are column or row vectors) should be clarified.

- **Logical flow**: The chunk flows logically from softmax output, loss, backpropagation, context window, CBOW, Skip-Gram, and computational challenges. However, the incomplete sentence in 13.9 interrupts the flow.

**Summary**: The scientific content is mostly correct and well-explained, but the chunk suffers from minor formatting errors, incomplete sentences, and some ambiguous notation that should be clarified for precision and readability.

## Chunk 79/104
- Character range: 524277–532179

```text
This is computationally expensive, especially when training on large corpora.

Approximate Solutions:       To address this, several approximation techniques have been proposed:
  •

13.11 Eﬀicient Training of Word Embeddings: Hierarchical Softmax and Nega-
      tive Sampling
Recall from the previous discussion that computing the full softmax over a large vocabulary is com-
putationally expensive. Specifically, given an input word, calculating the probability distribution
over all possible output words in the vocabulary requires a normalization over potentially millions
of terms, which is prohibitive in practice.
    There are two primary strategies to address this computational bottleneck:

1. Hierarchical Softmax Hierarchical softmax replaces the flat softmax layer with a binary
tree representation of the vocabulary. Each word corresponds to a leaf node, and the probability of
a word is decomposed into the probabilities of traversing the path from the root to that leaf. This
reduces the computational complexity from O(V ) to O(log V ), where V is the vocabulary size.
    The key idea is to organize words so that frequent words have shorter paths, thus further
improving eﬀiciency. During training, only the nodes along the path to the target word are updated,
avoiding the need to compute scores for all words.



                                                201
Intelligent SystemsLecture
                    and Soft
                           8 Part
                             Computing
                                  I: Neural Network Applications in Natural Language Processing


2. Negative Sampling Negative sampling is an alternative approximation that simplifies the
objective by transforming the multi-class classification problem into multiple binary classification
problems.
   • For each observed word-context pair (w, c), the model aims to distinguish the true pair from
     randomly sampled negative pairs (w, c′ ), where c′ is drawn from a noise distribution.

   • Instead of computing probabilities over the entire vocabulary, the model only updates param-
     eters for the positive pair and a small number of negative samples.

Example:      Consider the sentence:

                             “I want to buy a big brick house in the city.”

Suppose the context word is brick. The true target word is house. Negative samples might be
lion, bake, or big (although big appears in the sentence, it can still be sampled as a negative
example depending on the sampling strategy). Negative draws occasionally colliding with real
context words is harmless—the associated losses simply push the model to separate the sampled
pair unless the data provide strong evidence to the contrary.

Training Objective with Negative Sampling Define the logistic regression classifier that,
given an input word vector vw and an output word vector vc′ , predicts whether the pair (w, c) is
observed (label 1) or a negative sample (label 0).
    The probability that the pair is observed is modeled as:

                                       p(D = 1 | w, c) = σ(vc′ ⊤ vw )                                (13.11)

where σ(x) = 1+e1−x is the sigmoid function.
   The training objective for one positive pair (w, c) and k negative samples {c′1 , . . . , c′k } is:

                                                       X
                                                       k
                                                                                  
                                  log σ(vc′ ⊤ vw ) +         log σ − vc′ ′ ⊤ vw                      (13.12)
                                                                         i
                                                       i=1

where each c′i is drawn independently from the noise distribution Pn (c).

Interpretation: The model learns to assign high similarity scores to true word-context pairs
and low similarity scores to randomly sampled pairs, effectively learning meaningful embeddings
without computing the full softmax. The expectation over the noise distribution is estimated by
the empirical average across the k sampled negatives in (13.12).

Backpropagation: The gradients are computed only for the positive pair and the sampled neg-
ative pairs, drastically reducing computation.




                                                       202
Intelligent SystemsLecture
                    and Soft
                           8 Part
                             Computing
                                  I: Neural Network Applications in Natural Language Processing


13.12 Local Context vs. Global Matrix Factorization Approaches
Word embedding methods can be broadly categorized into two classes based on how they utilize
context information:

1. Local Context Window Methods These methods focus on the immediate context of a
word within a fixed-size window. Examples include:
   • Continuous Bag-of-Words (CBOW)

   • Skip-gram
   They learn embeddings by predicting a word given its neighbors (CBOW) or predicting neigh-
bors given a word (skip-gram). These methods are computationally eﬀicient and capture syntactic
and semantic relationships based on local co-occurrence patterns.

2. Global Matrix Factorization Methods These methods consider the entire corpus to build
a global co-occurrence matrix X, where each entry Xij counts how often word i co-occurs with
word j across the corpus.
   • Latent Semantic Analysis (LSA) is an early example, which applies singular value decompo-
     sition (SVD) to the co-occurrence matrix.

   • More recent methods include GloVe (Global Vectors), which factorizes a weighted log-count
     matrix.

Example: Co-occurrence Matrix            Suppose the vocabulary size is V . The co-occurrence matrix
X ∈ RV ×V is defined as:

                  Xij = number of times word i appears in the context of word j

    This matrix is sparse and large (especially when V runs into the hundreds of thousands), so
storing it explicitly or factorizing it naively can be computationally expensive.

13.13 Global Word Vector Representations via Co-occurrence Statistics
Recall that our goal is to obtain a global vector representation for words, capturing semantic
relationships beyond simple one-hot encodings. Instead of encoding words individually, we leverage
co-occurrence statistics of word pairs within a corpus to build richer embeddings.

Setup: Consider two words wi and wj appearing in some context window within a text corpus.
We are interested in modeling the co-occurrence of these words, possibly mediated by a third context
word wk . For example, in the phrase “big historic castle,” the words “big” and “historic” are targets,
and “castle” can be a context word connecting them.




                                                 203
Intelligent SystemsLecture
                    and Soft
                           8 Part
                             Computing
                                  I: Neural Network Applications in Natural Language Processing




      Figure 53: PCA projection of learned embeddings showing clusters for occupations, royalty,
     and fruit names. Analogies such as king − man + woman trace nearly straight lines within this
                                                space.


Notation:
  • Plain symbols wi , wj , wk denote lexical items drawn from the vocabulary.

  • Bold symbols denote vectors: vi is the embedding of target word wi and uk the embedding
    of context word wk .
                                                                                      P
  • Xik counts how often wi and wk co-occur within the chosen context window, and Xi = k Xik
    is the total number of context observations for wi .

Goal: Define a function f that relates the co-occurrence statistics of the word pairs and context
words to a scalar quantity representing their semantic association.
```

### Findings
- **Sigmoid function definition (Equation 13.11)**: The sigmoid function is incorrectly written as  
  \(\sigma(x) = 1 + e^{1-x}\).  
  The correct definition is  
  \[
  \sigma(x) = \frac{1}{1 + e^{-x}}.
  \]  
  This is a critical error since the sigmoid function is fundamental to negative sampling.

- **Training objective with negative sampling (Equation 13.12)**:  
  The formula is ambiguous and appears to have typographical errors:  
  \[
  \sum_{i=1}^k \log \sigma(-v_{c'_i}^\top v_w)
  \]  
  should be explicitly included alongside the positive term \(\log \sigma(v_c^\top v_w)\). The full objective for one positive pair \((w,c)\) and \(k\) negative samples \(\{c'_1, \ldots, c'_k\}\) is:  
  \[
  \log \sigma(v_c^\top v_w) + \sum_{i=1}^k \log \sigma(-v_{c'_i}^\top v_w).
  \]  
  The current notation is confusing and needs clarification.

- **Notation inconsistency in negative sampling**:  
  The text uses \(c\) for the true context word and \(c'\) for negative samples, but in the logistic regression classifier definition, the notation \(v_{c'}\) is used for the output vector, which may confuse readers since \(c'\) is a negative sample. It would be clearer to distinguish the positive context vector \(v_c\) and negative context vectors \(v_{c'_i}\).

- **Negative sampling example**:  
  The example states that "big" can be sampled as a negative example even though it appears in the sentence. This is correct but could benefit from a brief explanation that negative samples are drawn from a noise distribution independent of the current context, which may include words present in the sentence.

- **Definition of co-occurrence matrix \(X\)**:  
  The matrix \(X \in \mathbb{R}^{V \times V}\) is defined as \(X_{ij} =\) number of times word \(i\) appears in the context of word \(j\).  
  This is somewhat ambiguous because usually the co-occurrence matrix is defined as \(X_{ij} =\) number of times word \(j\) appears in the context of word \(i\), or vice versa, depending on convention. The directionality should be explicitly stated to avoid confusion.

- **Notation for total context counts \(X_i = \sum_k X_{ik}\)**:  
  This is introduced without specifying whether the sum is over all context words \(k\) or over all vocabulary words. It would be clearer to state explicitly:  
  \[
  X_i = \sum_{k=1}^V X_{ik}.
  \]

- **Missing definition of the function \(f\)**:  
  The text ends with the goal to define a function \(f\) relating co-occurrence statistics to semantic association but does not provide any further detail or examples. This leaves the reader hanging and should be followed by a formal definition or at least a description of candidate functions (e.g., PMI, log-counts, or GloVe's weighted least squares objective).

- **Figure 53 reference**:  
  The figure is mentioned but not shown in the chunk. It would be helpful to briefly describe what the PCA projection illustrates in terms of embedding quality and analogy properties, to connect the theory with empirical results.

- **Typographical and formatting issues**:  
  - The bullet point under "Approximate Solutions" is empty.  
  - The text contains some formatting artifacts (e.g., "" in equation 13.12) that should be cleaned up for clarity.

Overall, the chunk covers important concepts but requires corrections in mathematical definitions, clearer notation, and completion of some explanations.
