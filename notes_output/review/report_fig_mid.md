# Scientific QA Report

- Source PDF: `notes_output/ece657_notes.pdf`
- Total chunks: 5

## Chunk 40/108
- Character range: 233585–240812

```text
• Widrow, B., & Hoff, M. E. (1960). Adaptive switching circuits. 1960 IRE WESCON Con-
     vention Record, 4, 96–104.

   • Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by
     back-propagating errors. Nature, 323(6088), 533–536.

  Summary
  Key takeaways
      • The perceptron implements a linear separator and learns via mistake‑driven updates.

      • Geometry (hyperplane and signed distance) explains predictions and update magnitude.

      • Nonlinear problems require multilayer networks or feature mappings.



6 Multi-Layer Perceptrons: Challenges and Foundations
In the previous chapters, we introduced the perceptron as a fundamental building block for bi-
nary classification tasks. However, the perceptron model is inherently limited to solving linearly
separable problems. In this section, we revisit these limitations and set the stage for the introduc-
tion of multi-layer perceptrons (MLPs), which overcome these challenges by leveraging multiple
interconnected neurons.

6.1    Limitations of the Single-Layer Perceptron
Recall that a perceptron computes a weighted sum of its inputs and applies a threshold activation
function to produce a binary output. Formally, for input vector x = [x1 , x2 , . . . , xn ]T and weight
vector w = [w1 , w2 , . . . , wn ]T , the perceptron output y is given by
                                                 
                                                 1, wT x + b > 0,
                                             y=                                                   (6.1)
                                                 0, otherwise,

where b is the bias term representing the threshold. The bias is added to the weighted sum, shifting
the decision boundary without altering the linear form w⊤ x. Some authors instead encode the
perceptron output as {−1, +1}; both conventions are equivalent after a simple aﬀine rescaling.
Throughout this chapter we use the {0, 1} convention for clarity when relating the perceptron to
probability models and loss functions.
    The chief limitation of this model is its inability to solve problems where the classes are not
linearly separable. For example, consider a dataset with two classes arranged in a non-linear pattern
(e.g., two interleaved triangles). A single hyperplane cannot separate these classes, and thus the
perceptron fails to find a suitable decision boundary.

Example: Non-linearly Separable Data
   • Suppose the data points are arranged such that no straight line can separate the two classes
     (the classic XOR configuration—labeling (0, 0) and (1, 1) as class 0 and (1, 0) and (0, 1) as


                                                  83
Intelligent Systems Companion                      Multi-Layer Perceptrons: Challenges and Foundations


      class 1—is the canonical example).

  • The perceptron attempts to find a linear separator but fails, as it can only represent linear
    decision boundaries.
    This limitation motivates the need for more complex architectures that can model non-linear de-
cision boundaries. In fact, the Perceptron Convergence Theorem guarantees convergence only when
the data are linearly separable; on XOR-like datasets the learning algorithm oscillates indefinitely
instead of finding weights that solve the classification task.

6.2   Biological Inspiration and the Need for Multiple Neurons
The human brain operates through a network of interconnected neurons, not isolated units. Each
neuron receives inputs from many others, processes them, and passes the output forward. This
collective behavior enables the brain to perform complex pattern recognition and decision-making
tasks.
    Similarly, in artificial neural networks, we seek to emulate this by connecting multiple percep-
trons (neurons) in layers, allowing them to work together to represent complex functions.

Key Observations:
  • A single perceptron has an all-or-none response, limiting its expressiveness.

  • Combining multiple neurons allows the network to learn hierarchical and compositional fea-
    tures.

  • The output of one neuron can influence many others, creating tightly coupled pathways of
    computation across the network.

  • While artificial neurons are simplified abstractions, biological neurons exhibit richer temporal
    dynamics and signaling mechanisms; the layered analogy should therefore be interpreted as
    inspiration rather than literal equivalence.

6.3   Challenges in Extending Perceptrons to Multi-Layer Architectures
Before we delve into the architecture of multi-layer perceptrons, it is important to understand the
challenges that arise when moving beyond a single perceptron.

1. Weight Update Complexity Consider a perceptron with two weights w1 and w2 . To update
these weights during training, one typically uses gradient descent on a loss function. The update
involves computing partial derivatives with respect to each weight:

                                           ∂L                      ∂L
                                ∆w1 = −η       ,        ∆w2 = −η       ,                         (6.2)
                                           ∂w1                     ∂w2

where η is the learning rate and L is the loss.
   When the number of weights grows large (e.g., millions in deep networks), computing and
applying these updates individually becomes computationally expensive and ineﬀicient.



                                                   84
Intelligent Systems Companion                        Multi-Layer Perceptrons: Challenges and Foundations




                                                 1




                                −2                                     2



                                               −1




      Figure 20: Gradient descent viewed in weight space. Contours represent level sets of L(w);
       successive updates follow the negative gradient (blue path) until they reach the minimizer.


Solution: Vectorized Updates         Instead of updating weights one at a time, we update the entire
weight vector simultaneously:

                                           ∆w = −η∇w L,                                              (6.3)

where ∇w L is the gradient vector of the loss with respect to all weights.
    This approach scales eﬀiciently to high-dimensional parameter spaces and is foundational for
training deep networks.

2. Handling Thresholds and Bias Terms In the original perceptron model, the neuron fires if
the weighted sum exceeds a threshold. However, representing and learning this threshold explicitly
poses challenges:
  • How do we mathematically represent the threshold in a differentiable manner?

  • How can the threshold be learned from data rather than fixed a priori?

Incorporating Bias as a Learnable Parameter A common technique is to absorb the thresh-
old into the bias term b, which is treated as an additional weight with a constant input:
                                                            !
                                               Xn
                                       y=σ        w i xi + b ,                            (6.4)
                                                i=1
```

### Findings
- **Equation (6.1) notation and explanation:**
  - The perceptron output is defined as \( y = 1 \) if \( w^T x + b > 0 \), else 0. This is correct.
  - The note that some authors use \(\{-1, +1\}\) encoding and that these are equivalent after affine rescaling is accurate.
  - However, the term "threshold" is used somewhat ambiguously: the bias \(b\) is described as representing the threshold, but more precisely, the threshold is the value that the weighted sum must exceed, and the bias shifts the decision boundary. It might be clearer to say the bias shifts the decision boundary rather than "representing the threshold."

- **Example of non-linearly separable data:**
  - The XOR example is correctly identified as a canonical non-linearly separable problem.
  - The description "two interleaved triangles" is less standard; the XOR example is more commonly described as points in the plane with labels that cannot be separated by a single line. The "two interleaved triangles" example is a different non-linear pattern (e.g., the "two moons" dataset). Clarify or separate these examples to avoid confusion.

- **Perceptron Convergence Theorem:**
  - The statement that the theorem guarantees convergence only for linearly separable data is correct.
  - The claim that on XOR-like datasets the algorithm "oscillates indefinitely" is a simplification; more precisely, the perceptron algorithm fails to converge and may cycle through weight updates without settling.

- **Section 6.2 Biological Inspiration:**
  - The analogy between biological neurons and artificial neurons is well stated.
  - The note that biological neurons have richer temporal dynamics and signaling mechanisms is important and appropriately cautions against over-literal interpretation.

- **Section 6.3 Challenges:**
  - The gradient descent update formulas (6.2) are presented as partial derivatives with respect to weights \(w_1\) and \(w_2\), which is correct.
  - The explanation that updating weights individually is inefficient for large networks is valid.
  - The vectorized update (6.3) is correctly introduced and is standard practice.

- **Handling thresholds and bias terms:**
  - The question "How do we mathematically represent the threshold in a differentiable manner?" is posed but not answered in this chunk.
  - Equation (6.4) introduces the bias term \(b\) as an additional weight with constant input, but the equation is incomplete or incorrectly formatted:
    - The equation shows \( y = \sigma \left( \sum_{i=1}^n w_i x_i + b \right) \), but the summation symbol is not properly closed or formatted.
    - The activation function \(\sigma\) is introduced here without prior definition in this chunk; it should be defined (e.g., sigmoid, ReLU, or step function).
    - The notation "!" before the summation is unclear and likely a formatting error.
  - The explanation that the bias can be treated as a weight with constant input (usually 1) is standard and should be explicitly stated.

- **Additional notes:**
  - The figure caption for Figure 20 is clear and helpful.
  - The chunk ends abruptly after equation (6.4), suggesting incomplete content or missing continuation.

**Summary of issues:**

- Ambiguous use of "threshold" vs. "bias" terminology.
- Mixing examples of non-linear separability (XOR vs. interleaved triangles) without clear distinction.
- Minor formatting errors in equation (6.4) and missing definition of \(\sigma\).
- Missing explicit statement that bias is treated as a weight with constant input (usually 1).
- The question about differentiable threshold representation is posed but not addressed here.
- The chunk ends abruptly, indicating incomplete explanation.

No major scientific errors, but some clarifications, formatting fixes, and more precise definitions are needed.

## Chunk 41/108
- Character range: 240818–247100

```text
where σ(·) is the activation function (e.g., step function or sigmoid).
    The explicit summation index emphasizes that every input contributes linearly before the bias
                              P
shift is applied; the notation ni=1 wi xi + b is shorthand for (w1 x1 + · · · + wn xn ) + b.
    By including b as a parameter to be learned during training, the network can adapt the threshold
dynamically. Setting b = −θ recovers the classical thresholded expression in (6.1), so the bias is
best viewed as a learnable threshold.




                                                     85
Intelligent Systems Companion                     Multi-Layer Perceptrons: Challenges and Foundations


6.4   From Perceptron to Differentiable Activation Functions
Recall that the original perceptron model uses a hard threshold activation function:
                                              
                                              +1 z ≥ 0
                                      f (z) =
                                              −1 z < 0


where z = w⊤ x + b.
    This symmetric {−1, +1} encoding is algebraically convenient when we later discuss differen-
tiable approximations such as tanh. The two conventions are related by the aﬀine map

                                  ỹ = 2y − 1,     y = 0.5 (ỹ + 1),

so classifiers expressed in either coding are equivalent up to this simple rescaling. In words: double
a {0, 1} label and subtract one to obtain a {−1, +1} label; add one and halve to map back.
    This function is not differentiable at z = 0 and is discontinuous, which prevents the use
of gradient-based optimization methods. Introducing a bias term b simply shifts the threshold,
rewriting the activation as:
                                             z = w⊤ x + b.

    However, even with the bias shift the key challenge remains: the step function is not differ-
entiable. It is piecewise constant with a jump at zero. We therefore replace it with a smooth,
differentiable activation such as the sigmoid or hyperbolic tangent:

                                                  1
                                       σ(z) =            ,                                       (6.5)
                                             1 + exp(−z)
                                             exp(z) − exp(−z)
                                   tanh(z) =                  .                                  (6.6)
                                             exp(z) + exp(−z)

Explicitly, both expressions rely on exponentials: σ(z) divides 1 by 1 + exp(−z), while tanh(z)
takes the difference and sum of exp(z) and exp(−z).
   These functions are smooth and differentiable everywhere, enabling gradient-based learning.

6.5   Performance Measure and Loss Function
Instead of counting misclassifications, we define a performance measure based on the difference
between the target t and the network output y. A common choice is the mean squared error
(MSE):
                                          P = 0.5 (t − y)2 ,                               (6.7)

where the coeﬀicient 0.5 simplifies derivatives.
   This loss function is smooth and differentiable, making it suitable for gradient descent.




                                                 86
Intelligent Systems Companion                          Multi-Layer Perceptrons: Challenges and Foundations


6.6    Extending to Multi-Layer Networks
Consider a simple feedforward network with two layers of neurons. The input vector is x =
(x1 , x2 , . . . , xn ), and the first layer computes:

                                     p1 = w1⊤ x + b1 ,      y1 = f (p1 ),

where f (·) is the differentiable activation function.
   The second layer neuron receives y1 as input:

                                     p2 = w 2 y 1 + b 2 ,   y2 = f (p2 ).

   The output y2 is compared to the target t using the loss P in (6.7).

Notation. To stay consistent with the feedforward notation in Equation (5.2), we interpret each
pℓ as the pre-activation z (ℓ) and each yℓ as the activation a(ℓ) = f (z (ℓ) ). For scalar examples we
write y for a to emphasize the neuron output, but we maintain the mapping z ↔ p and a ↔ y
when comparing formulas across sections.

6.7    Gradient Descent and Backpropagation
Our goal is to update weights w1 , w2 to minimize P . Using gradient descent, the weight update
rule is:
                                                    ∂P
                                          ∆w = −η       ,
                                                    ∂w
where η is the learning rate.
    To compute ∂P ∂w , we apply the chain rule explicitly as a product of partial derivatives. For
example, for w2 :

                                          ∂P    ∂P ∂y2 ∂p2
                                              =             .                                        (6.8)
                                          ∂w2   ∂y2 ∂p2 ∂w2

   Similarly, for w1 :

                                      ∂P    ∂P ∂y2 ∂p2 ∂y1 ∂p1
                                          =                     .                                    (6.9)
                                      ∂w1   ∂y2 ∂p2 ∂y1 ∂p1 ∂w1

   Breaking down each term:
       ∂P     ∂ 1
   •       =       (t − y2 )2 = y2 − t.
       ∂y2   ∂y2 2
       ∂yi
   •       = f ′ (pi ), the derivative of the activation function evaluated at the neuron’s pre-activation.
       ∂pi
       ∂p2
   •       = y1 .
       ∂w2
       ∂p2
   •       = w2 .
       ∂y1


                                                      87
Intelligent Systems Companion                     Multi-Layer Perceptrons: Challenges and Foundations


      ∂p1
  •       = x, the input vector feeding the first neuron.
      ∂w1
    Equivalently, the three scalar sensitivities we need are ∂p2 /∂w2 = y1 , ∂p2 /∂y1 = w2 , and
∂p1 /∂w1 = x; the activation derivative is provided by f ′ (pi ).
    Thus, the gradients become:

                                 ∂P
                                     = (y2 − t)f ′ (p2 )y1 ,                                   (6.10)
                                 ∂w2
                                 ∂P
                                     = (y2 − t)f ′ (p2 )w2 f ′ (p1 )x.                         (6.11)
                                 ∂w1
```

### Findings
- **Notation inconsistency and ambiguity:**
  - The notation for the summation index in the first paragraph is confusing: "ni=1 wi xi + b" should be "∑_{i=1}^n w_i x_i + b" or explicitly written as "w_1 x_1 + ... + w_n x_n + b". The current form "ni=1 wi xi + b" is not standard and may confuse readers.
  - The text uses both \(p_\ell\) and \(z^{(\ell)}\) interchangeably for pre-activation, and \(y_\ell\) and \(a^{(\ell)}\) for activation. While this is explained, it may cause confusion. It would be clearer to pick one notation consistently or clearly state when switching.
  - In the gradient expressions, the partial derivatives are written with inconsistent spacing and formatting, e.g., \(\frac{\partial P}{\partial y_2}\) is sometimes written as \(\partial P / \partial y_2\) and sometimes as \(\frac{\partial P}{\partial y_2}\). Consistent notation would improve clarity.

- **Mathematical errors or unclear derivative expressions:**
  - In the bullet point under "Breaking down each term," the derivative of the loss with respect to \(y_2\) is written as:
    \[
    \frac{\partial P}{\partial y_2} = \frac{\partial}{\partial y_2} \frac{1}{2} (t - y_2)^2 = y_2 - t.
    \]
    This is correct, but the intermediate step is missing or not clearly shown. It would be clearer to explicitly write:
    \[
    \frac{\partial P}{\partial y_2} = \frac{\partial}{\partial y_2} \frac{1}{2} (t - y_2)^2 = (t - y_2)(-1) = y_2 - t.
    \]
  - The bullet point:
    \[
    \frac{\partial p_2}{\partial w_2} = y_1,
    \]
    is correct only if \(w_2\) and \(y_1\) are scalars. However, if \(w_2\) is a vector and \(y_1\) is a vector, this derivative should be a vector or matrix. The text should clarify the scalar vs vector case explicitly.
  - Similarly, the term:
    \[
    \frac{\partial p_2}{\partial y_1} = w_2,
    \]
    is only valid if \(p_2 = w_2^\top y_1 + b_2\) with vector inputs. The text should clarify the dimensions and whether these are scalar or vector quantities.
  - The term:
    \[
    \frac{\partial p_1}{\partial w_1} = x,
    \]
    again assumes scalar weights and inputs. For vector/matrix weights, this derivative is more complex and should be clarified.

- **Logical gaps or missing explanations:**
  - The transition from the perceptron step function to differentiable activations is well motivated, but the text could better explain why the sigmoid and tanh are chosen beyond differentiability (e.g., their smoothness, boundedness, and historical usage).
  - The loss function is introduced as mean squared error (MSE) for classification tasks, but MSE is not always the best choice for classification (cross-entropy is often preferred). This could be mentioned or justified.
  - The chain rule application in equations (6.8) and (6.9) is shown, but the full expansion and final gradient expressions are only partially given. A more complete derivation or reference to backpropagation would help.

- **Typographical and formatting issues:**
  - In equation (6.5), the sigmoid function is written as:
    \[
    \sigma(z) = \frac{1}{1 + \exp(-z)},
    \]
    which is correct, but the line break and spacing could be improved for readability.
  - Similarly, equation (6.6) for tanh is:
    \[
    \tanh(z) = \frac{\exp(z) - \exp(-z)}{\exp(z) + \exp(-z)},
    \]
    which is correct but could be formatted more cleanly.
  - The bullet point list under "Breaking down each term" has inconsistent indentation and spacing, making it harder to read.

- **Terminology and definitions:**
  - The term "performance measure" is used interchangeably with "loss function." It would be clearer to define these terms explicitly and distinguish between them if needed.
  - The term "activation function" is introduced as \(\sigma(\cdot)\) but later the notation \(f(\cdot)\) is used. Consistency or clarification would help.

- **Summary:**
  - Overall, the content is mostly correct and well-structured.
  - The main issues are inconsistent notation, lack of clarity on scalar vs vector cases, incomplete derivative explanations, and minor formatting problems.
  - Adding more explicit steps in derivative calculations and clarifying assumptions about dimensions would improve the rigor and clarity.

## Chunk 42/108
- Character range: 247102–254309

```text
Interpretation The gradients in Equations (6.10) and (6.11) reveal the essence of backpropaga-
tion: errors at the output layer are weighted by downstream sensitivities and propagated backward
through the network, modulated by activation derivatives and incoming activations. Each weight
update is proportional to the contribution of that weight to the overall prediction error.

6.8   Completing the Derivative Calculations
We now finalize the key derivative expressions involved in training a single-layer neural network
with a sigmoid activation function. Recall the notation:
  • p: pre-activation input to a neuron (scalar),

  • w: weight parameters (vector),

  • y: output of the neuron after activation (scalar),

  • α: input to the activation function,

  • β: output of the activation function,

  • t: target output.

Derivative of output with respect to input Assuming the sigmoid activation function:

                                                          1
                                      β = σ(α) =               ,
                                                       1 + e−α

where α is the neuron’s pre-activation (denoted p in the scalar example above). We compute the
           dβ
derivative dα as follows:
                                                               
                                       dβ    d           1
                                          =
                                       dα   dα        1 + e−α
                                                  e−α
                                           =
                                               (1 + e−α )2
                                           = β(1 − β).                                         (6.12)

   In other words, differentiating the reciprocal 1/(1 + exp(−α)) yields exp(−α)/(1 + exp(−α))2 ,
which collapses to β(1 − β) once we substitute back the original sigmoid output.

                                                  88
Intelligent Systems Companion                       Multi-Layer Perceptrons: Challenges and Foundations


   This key identity allows us to express the derivative of the output with respect to its input
purely in terms of the output itself, which simplifies backpropagation computations significantly.

Derivative of the loss with respect to weights For a neuron with output y = β, target t,
and weights w, the error term at the output layer is obtained by applying the chain rule explicitly.
We denote the pre-activation by p = w · x + b so that y = σ(p) is the sigmoid output of the neuron,
and we work with the squared-error loss E = 0.5 (y − t)2 .

                                     ∂E   ∂E ∂y
                                δ=      =       = (y − t) y(1 − y).
                                     ∂p   ∂y ∂p

The gradient with respect to the incoming weights is therefore

                                             ∂E
                                                = δ · x,
                                             ∂w
where x is the input to the neuron (and ∂E/∂b = δ when an explicit bias b is present). Writing
the derivative in this way makes it clear that δ already captures the sign of the deviation y − t, so
the gradient descent update w ← w − η ∂E ∂w automatically moves the weights in the error-reducing
direction.

Interdependence of weights When considering multiple layers or neurons, the weights influence
each other through the network’s connectivity. Specifically, the derivative of the output with respect
to a weight in a previous layer involves the weights and activations of subsequent layers. This
network-wide coupling means that updating one weight affects the gradient computations of others,
which is fundamental to the backpropagation algorithm.

6.9   Single-Neuron Gradient Example
To better understand the gradient flow, we denote:

                                       p = w · x,        y = σ(p),

where p is the weighted sum input, x the input vector, and w the weight vector.
   The derivative of p with respect to w is simply:

                                              ∂p
                                                 = x,
                                              ∂w
and the derivative of y with respect to p is given by (6.12).
   Thus, the gradient of the loss with respect to w is:

                                     ∂E   ∂E ∂y ∂p
                                        =   ·  ·
                                     ∂w   ∂y ∂p ∂w
                                         = (y − t) · y(1 − y) · x.                               (6.13)

   Here we have reused the squared-error loss E = 0.5 (y − t)2 from (6.7), so ∂E/∂y = y − t and


                                                    89
Intelligent Systems Companion                           Multi-Layer Perceptrons: Challenges and Foundations


∂E/∂w is a gradient vector whose i-th component equals ∂E/∂wi .

6.10    Extension to Multi-Layer Networks
For networks with more than one layer, the same principles apply recursively. The error term δ for
a neuron in layer l depends on the weighted sum of the δ terms in layer l + 1 and the derivative of
the activation function at layer l:
                                                  ⊤ (l+1)                    
                                δ (l) = W (l+1)     δ      ◦ y (l) ◦ 1 − y (l) ,

where the superscript indicates layer index, (·)⊤ denotes matrix transpose, and ◦ is element-wise
(Hadamard) multiplication. The final factor y (l) ◦ (1 − y (l) ) corresponds to f ′ (z (l) ) under a sigmoid
activation; for other activation functions it should be replaced with the appropriate derivative
vector.
    This recursive calculation allows the error to be propagated backward through the network,
enabling eﬀicient computation of gradients for all weights.

Reuse of intermediate computations A crucial insight is that intermediate terms, such as
δ (l) , are computed once per layer and reused when calculating gradients for all weights in that layer.
This reuse avoids redundant calculations and is a key eﬀiciency feature of backpropagation.

6.11    Summary
   • The derivative of the sigmoid activation function can be expressed simply as y(1 − y), where
     y is the output of the neuron.

   • The gradient of the loss with respect to weights in a single-layer network is given by the
     product of the error term, the sigmoid derivative, and the input.

   • In multi-layer networks, the error terms propagate backward through the layers, weighted by
     the connections and modulated by the activation derivatives.

   • Intermediate computations such as error terms are reused across gradient calculations, im-
     proving computational eﬀiciency.

   • These derivations set the stage for the backpropagation learning algorithm, which will be
     discussed in detail in the next chapter.

References
   • Bishop, C. M. (1995). Neural Networks for Pattern Recognition. Oxford University Press.

   • Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.




                                                       90
Intelligent Systems Companion                       Backpropagation Learning in Multi-Layer Perceptrons
```

### Findings
- **Notation ambiguity:** The text uses both \( p \) and \( \alpha \) to denote the pre-activation input to a neuron, but does not explicitly clarify that these are the same quantity. This could confuse readers. It would be clearer to consistently use one symbol or explicitly state \( \alpha = p \).

- **Derivative notation inconsistency:** In the derivative of the sigmoid function, the text writes "We compute the derivative \( d\beta \) as follows: \( d\beta/d\alpha = \beta(1-\beta) \)". The initial expression is somewhat informal and could be improved by explicitly writing \( \frac{d\beta}{d\alpha} = \beta(1-\beta) \) for clarity.

- **Missing explicit chain rule step:** When computing \( \delta = \frac{\partial E}{\partial p} = \frac{\partial E}{\partial y} \frac{\partial y}{\partial p} \), the text jumps directly to the final expression \( (y - t) y (1 - y) \) without explicitly showing the intermediate step \( \frac{\partial E}{\partial y} = y - t \). Although this is standard, including it would improve clarity.

- **Ambiguous statement about interdependence of weights:** The section on "Interdependence of weights" states that updating one weight affects the gradient computations of others due to network connectivity. While conceptually true, this could be misleading if interpreted as weights directly influencing each other's gradients during a single backward pass. It would be better to clarify that the gradients depend on activations and errors propagated through the network, which are functions of all weights, but the gradient of each weight is computed independently once these terms are known.

- **Inconsistent use of boldface and vector notation:** The text sometimes uses boldface (e.g., \( \mathbf{w} \), \( \mathbf{x} \)) and sometimes plain letters for vectors (e.g., \( w \), \( x \)). Consistent notation for vectors and scalars would improve readability.

- **Lack of explicit definition of the bias term \( b \):** The bias \( b \) is introduced in the pre-activation \( p = w \cdot x + b \), but its role and gradient are only briefly mentioned. A more explicit explanation of how \( b \) is treated in gradient calculations would be helpful.

- **Equation (6.12) formatting issue:** The derivative calculation for the sigmoid function is presented with some formatting artifacts (e.g., "             ") that may confuse readers. These should be cleaned up for clarity.

- **Clarification on the Hadamard product:** The notation \( \circ \) is introduced as element-wise (Hadamard) multiplication in the multi-layer error term formula. It would be helpful to explicitly state that this operation is element-wise multiplication of vectors, especially for readers unfamiliar with the notation.

- **Missing mention of activation function input notation:** In the multi-layer error term formula, the derivative is expressed as \( y^{(l)} \circ (1 - y^{(l)}) \), which corresponds to \( f'(z^{(l)}) \) for sigmoid. However, \( z^{(l)} \) is not defined in the text. Defining \( z^{(l)} \) as the pre-activation input at layer \( l \) would improve clarity.

- **No explicit mention of vector/matrix dimensions:** When discussing multi-layer networks and the recursive formula for \( \delta^{(l)} \), the dimensions of \( W^{(l+1)} \), \( \delta^{(l+1)} \), and \( y^{(l)} \) are not specified. Including this information would help readers understand the matrix operations involved.

- **Summary bullet points could be more precise:** For example, the first bullet states "The derivative of the sigmoid activation function can be expressed simply as \( y(1 - y) \), where \( y \) is the output of the neuron." It would be clearer to say "The derivative of the sigmoid activation function \( \sigma(\alpha) \) with respect to its input \( \alpha \) can be expressed as \( \sigma(\alpha)(1 - \sigma(\alpha)) \), which equals \( y(1 - y) \) when \( y = \sigma(\alpha) \)."

- **Minor typographical issues:** Some words are hyphenated oddly (e.g., "eﬀicient" instead of "efficient") due to font encoding issues. These should be corrected.

Overall, the content is mostly correct and well-explained but would benefit from improved clarity, consistent notation, and minor corrections as noted above.

## Chunk 43/108
- Character range: 254311–262550

```text
Summary
  Key takeaways
      • MLPs compose linear maps and nonlinearities to approximate complex functions.

      • Backpropagation computes gradients eﬀiciently via the chain rule across layers.

      • Depth/width, initialization, and activation choices shape optimization and expressivity.



7 Backpropagation Learning in Multi-Layer Perceptrons
In the previous chapters, we have developed a foundational understanding of intelligent system
design, focusing on linear regression, logistic regression, and perceptrons. Last time, we concluded
with the multi-layer perceptron (MLP) model, exploring its mathematical formulation and the
intuition behind its architecture. Today, we extend that understanding by generalizing the learning
process to networks with multiple layers and complex interconnections.

7.1    Context and Motivation
Recall that a simple perceptron or a shallow neural network consists of an input layer, a single
hidden layer, and an output layer. While this structure can solve linearly separable problems,
it is insuﬀicient for more complex tasks. The multi-layer perceptron introduces multiple layers
of neurons, each connected by weighted links, enabling the network to learn nonlinear decision
boundaries.
    However, this increased complexity raises the question: How do we update the weights across
multiple layers to minimize the error at the output? Unlike the single-layer perceptron, where weight
updates depend directly on the output error, in a deep network, changes in weights at one layer
propagate through subsequent layers, influencing the final output in a nonlinear and intertwined
manner.

7.2    Problem Setup
Consider a multi-layer perceptron with layers indexed by l = 1, 2, . . . , L, where L is the output
layer. Each layer l contains neurons indexed by i, and the output of neuron i in layer l is denoted
     (l)                                                              (l)
by ai . The input to this neuron before activation is denoted by zi . The weights connecting
                                                               (l)
neuron i in layer l − 1 to neuron j in layer l are denoted by wji .
    The forward pass through the network is given by:

                                      (l)
                                            X      (l) (l−1)      (l)
                                     zj =        wji ai        + bj ,                             (7.1)
                                             i
                                      (l)        (l) 
                                     a j = f zj          ,                                        (7.2)

         (l)
where bj is the bias term for neuron j in layer l, and f (·) is the activation function, typically
nonlinear (e.g., sigmoid, ReLU). Equation (7.1) makes it explicit that we sum over every incoming
                                                          (l)
neuron i in layer l − 1 to form the aﬀine pre-activation zj .


                                                   91
Intelligent Systems Companion                               Backpropagation Learning in Multi-Layer Perceptrons


7.3   Error and Objective
Suppose the network is tasked with a classification problem, such as distinguishing between cats
and dogs. For a given input, the network produces an output vector a(L) , where each component
corresponds to the predicted probability of a class. Let the target output vector be t. The error
function (loss) for a single training example is often defined as the squared error:

                                                1 X           
                                                            (L) 2
                                         E=          tk − a k     .                                       (7.3)
                                                2
                                                     k

                                                                     (l)
   The goal of learning is to adjust the weights {wji } to minimize E.

7.4   Challenges in Weight Updates
In a shallow network, weight updates can be computed directly from the output error. However, in
a deep network, the output error depends on all weights in a complex way. A change in a weight
in an earlier layer affects the activations of subsequent layers, ultimately influencing the output.
                                         (l)
    For example, consider a weight wji connecting neuron i in layer l − 1 to neuron j in layer
                                   (l)                                (l)
l. Changing this weight affects zj , which affects aj , which in turn affects all neurons in layers
                                                                                (l)
l + 1, l + 2, . . . , L. Therefore, the total effect of changing wji on the error E is a composition of
many intermediate effects.

7.5   Notation for Layers and Neurons
To formalize this, we introduce the following notation:
  • l: layer index, with l = 0 representing the input layer, and l = L the output layer.

  • i: neuron index in layer l − 1.

  • j: neuron index in layer l.

  • k: neuron index in layer L (output layer).
       (l)
  • ai : activation of neuron i in layer l.
       (l)
  • zj : weighted input to neuron j in layer l.
        (l)
  • wji : weight from neuron i in layer l − 1 to neuron j in layer l.
       (l)
  • bj : bias of neuron j in layer l.

  • f (·): activation function.

7.6   Forward Pass Recap
The forward pass computes activations layer by layer:

                                          (l)
                                                X          (l) (l−1)           (l)
                                         zj =            wji ai             + bj ,                        (7.4)
                                                 i
                                          (l)            (l) 
                                         a j = f zj              .                                        (7.5)


                                                           92
Intelligent Systems Companion                                     Backpropagation Learning in Multi-Layer Perceptrons


                                     (L)
   The output layer activations ak         are compared to the

7.7   Backpropagation: Recursive Computation of Error Terms
Recall that our goal is to compute the gradient of the error function with respect to the weights
in the network, specifically for weights connecting layer l to layer l + 1. We denote the weight
                                                              (l)
connecting neuron i in layer l to neuron j in layer l + 1 as wji .
    The error function E is typically defined as the sum of squared errors over the output neurons:

                                                     1X        (L)
                                             E=         (tk − ak )2 ,                                                (7.6)
                                                     2
                                                             k

                                       (L)
where tk is the target output and ak is the activation of output neuron k.
   To update the weights using gradient descent, we need to compute

                                                                 ∂E
                                                                  (l)
                                                                        .
                                                             ∂wji

Chain rule decomposition           By the chain rule, we have
                                                                                      (l+1)
                                           ∂E                    ∂E             ∂zj
                                             (l)
                                                     =           (l+1)
                                                                            ·             (l)
                                                                                                ,                    (7.7)
                                        ∂wji             ∂zj                      ∂wji
```

### Findings
- **Inconsistent indexing of weights in Section 7.7:**  
  - Earlier (Section 7.2), weights are defined as \( w_{ji}^{(l)} \) connecting neuron \( i \) in layer \( l-1 \) to neuron \( j \) in layer \( l \).  
  - In Section 7.7, it states "weights connecting layer \( l \) to layer \( l+1 \)" are denoted \( w_{ji}^{(l)} \), connecting neuron \( i \) in layer \( l \) to neuron \( j \) in layer \( l+1 \). This conflicts with the previous definition and can cause confusion.  
  - **Suggestion:** Maintain consistent notation throughout, e.g., \( w_{ji}^{(l)} \) always connects layer \( l-1 \) to layer \( l \), or clearly redefine if changing.

- **Ambiguity in summation indices in equations (7.1), (7.4):**  
  - The summation index \( i \) is used, but the range is not explicitly stated (e.g., \( i = 1, \ldots, n_{l-1} \)).  
  - **Suggestion:** Explicitly specify summation limits to avoid ambiguity.

- **Missing definition of activation function \( f(\cdot) \):**  
  - While examples (sigmoid, ReLU) are given, the properties required for backpropagation (e.g., differentiability) are not stated.  
  - **Suggestion:** Include a brief note on the required properties of \( f \) for gradient computation.

- **Squared error loss for classification (Section 7.3):**  
  - The squared error loss is used for classification, which is less common than cross-entropy loss for probabilistic outputs.  
  - While not incorrect, it would be helpful to mention this choice explicitly and possibly discuss its limitations or alternatives.

- **Equation (7.3) formatting:**  
  - The equation is written as  
    \[
    E = \frac{1}{2} \sum_k (t_k - a_k^{(L)})^2
    \]  
    but the notation in the text is somewhat cluttered with misplaced parentheses and superscripts.  
  - **Suggestion:** Clean up notation for clarity.

- **In Section 7.4, the explanation of how weight changes propagate is conceptually correct but could benefit from more precise language:**  
  - The phrase "a composition of many intermediate effects" is vague. It would be clearer to say that the gradient of the error with respect to a weight involves the chain rule applied through all subsequent layers.

- **In Section 7.7, the chain rule decomposition equation (7.7) is incomplete and ambiguous:**  
  - The equation is written as  
    \[
    \frac{\partial E}{\partial w_{ji}^{(l)}} = \frac{\partial E}{\partial z_j^{(l+1)}} \cdot \frac{\partial z_j^{(l+1)}}{\partial w_{ji}^{(l)}}
    \]  
    but the notation is inconsistent with previous definitions of layers and weights.  
  - Also, the partial derivative with respect to \( z_j \) is indexed as \( (l+1) \), but \( z_j \) is the pre-activation of neuron \( j \) in layer \( l \) according to earlier notation.  
  - **Suggestion:** Clarify the indexing and ensure consistency. For example, if \( w_{ji}^{(l)} \) connects layer \( l-1 \) to \( l \), then \( z_j^{(l)} \) depends on \( w_{ji}^{(l)} \), so the derivative should be with respect to \( z_j^{(l)} \), not \( z_j^{(l+1)} \).

- **No explicit mention of the error term \(\delta_j^{(l)}\) or the recursive formula for backpropagation:**  
  - The section introduces backpropagation but does not yet define the error terms or how the recursion proceeds. This is a logical gap that should be addressed in subsequent sections.

- **Typographical issues:**  
  - Some equations have misplaced or inconsistent parentheses and superscripts, which can confuse readers.  
  - For example, in equation (7.2), the activation is written as \( a_j^{(l)} = f z_j^{(l)} \), missing parentheses around the argument of \( f \). It should be \( a_j^{(l)} = f(z_j^{(l)}) \).

- **Summary section is concise but could benefit from more precise language:**  
  - For example, "Depth/width, initialization, and activation choices shape optimization and expressivity" is somewhat vague. It could specify how these factors influence learning dynamics and representational capacity.

**Overall, the chunk is mostly correct but would benefit from consistent notation, clearer definitions, and more precise mathematical statements.**

## Chunk 44/108
- Character range: 262555–272449

```text
(l+1)
where zj        is the weighted input to neuron j in layer l + 1:

                                        (l+1)
                                                     X            (l) (l)                 (l+1)
                                      zj        =                wji ai + bj                        ,
                                                         i

      (l)                                                                             (l+1)
with ai being the activation of neuron i in layer l, and bj                                         the bias term.
          (l+1)               (l)
   Since zj     is linear in wji , we have

                                                         (l+1)
                                                   ∂zj                          (l)
                                                       (l)
                                                                   = ai .
                                                     ∂wji

   Thus,
                                                ∂E                 (l+1) (l)
                                                (l)
                                                             = δj       ai ,                                         (7.8)
                                              ∂wji
where we define the error term
                                                   (l+1)                ∂E
                                                δj           :=             (l+1)
                                                                                      .
                                                                   ∂zj
                   (l+1)
Collecting the δj       for all neurons in layer l + 1 forms a vector δ (l+1) with the same dimension as
                                   ∂E
z (l+1) , ensuring the gradient ∂W   (l) has the same shape as the weight matrix.




                                                                 93
Intelligent Systems Companion                                    Backpropagation Learning in Multi-Layer Perceptrons


                     (l+1)                   (l+1)
Interpretation of δj         The term δj               measures how sensitive the error is to changes in the
           (l+1)
net input aj     . Our task reduces to computing these δ terms for all neurons in the network.

7.7.1   Output layer error terms
For the output layer L, the activation of neuron k is

                                                     (L)                  (L) 
                                                  ak       = ϕ zk                 ,

where ϕ(·) is the activation function.
   The error term for output neuron k is

                                          (L)          ∂E
                                     δk          =         (L)
                                                                                                               (7.9)
                                                     ∂zk
                                                                       (L)
                                                       ∂E ∂ak
                                                 =         (L)         (L)
                                                                                                              (7.10)
                                                     ∂ak         ∂zk
                                                                 (L) 
                                                 = a k − t k ϕ ′ zk ,
                                                     (L)
                                                                                                              (7.11)

where ϕ′ denotes the derivative of the activation function evaluated element-wise.

7.7.2   Hidden layer error terms
                                                                   (l)
For a hidden neuron j in layer l, the error term δj depends on the error terms of the neurons in
the next layer l + 1 to which it connects. Using the chain rule,

                                           (l)         ∂E
                                      δj =                 (l)
                                                                                                              (7.12)
                                                     ∂zj
                                                     X           ∂E          ∂zk
                                                                                      (l+1)
                                                 =                 (l+1)                (l)
                                                                                                              (7.13)
                                                       k    ∂zk               ∂zj
                                                     X (l+1) ∂z (l+1)
                                                               k
                                                 =     δk         (l)
                                                                      .                                       (7.14)
                                                     k        ∂z  j

   Since                                             X
                                      (l+1)                      (l)                    (l+1)
                                     zk          =           wkm a(l)
                                                                  m + bk                          ,
                                                       m
     (l)    (l) 
and aj = ϕ zj , we have
                                                                                      (l) 
                                                 (l+1)
                                           ∂zk
                                                           = wkj ϕ′ zj
                                                                   (l)
                                               (l)
                                                                                              .
                                             ∂zj
   Substituting into (7.14) yields

                                                           (l) 
                                                                   X
                                     δ j = ϕ ′ zj
                                      (l)                                    (l) (l+1)
                                                                           wkj δk                 .           (7.15)
                                                                      k




                                                                 94
Intelligent Systems Companion                     Backpropagation Learning in Multi-Layer Perceptrons


   For sigmoid activations ϕ, the derivative simplifies to ϕ′ (zj ) = aj (1 − aj ); other activations
                                                                 (l)    (l)    (l)

require substituting their respective derivatives in (7.15).

Summary: Backpropagation recursion

7.8   Backpropagation Algorithm: Detailed Derivation
Recall that the goal of backpropagation is to compute the gradient of the error function with respect
to each weight in the network, enabling gradient descent updates. Consider a single neuron k in
the output layer with output ok and activation ak . The target output is tk .

Error function and its derivatives We use the squared error function for a single output
neuron:
                                  E = 0.5 (tk − ok )2 .                            (7.16)
                                 ∂E
    Our objective is to compute ∂w jk
                                      , where wjk is the weight from neuron j in the previous layer
to neuron k.
    By the chain rule,
                                       ∂E     ∂E ∂ok ∂ak
                                           =      ·     ·     .                              (7.17)
                                     ∂wjk     ∂ok ∂ak ∂wjk

Step 1: Derivative of error with respect to output              From (7.3),

                                           ∂E
                                               = o k − tk .                                    (7.18)
                                           ∂ok

Step 2: Derivative of output with respect to activation Assuming the activation function
f is the sigmoid,
                                                  1
                                ok = f (ak ) =          ,
                                               1 + e−ak
its derivative is
                                    ∂ok
                                        = f ′ (ak ) = ok (1 − ok ).                            (7.19)
                                    ∂ak

Step 3: Derivative of activation with respect to weight The activation ak is the weighted
sum of inputs:                            X
                                     ak =   wjk xj ,
                                                  j

where xj is the output from neuron j in the previous layer. Thus,

                                             ∂ak
                                                  = xj .                                       (7.20)
                                             ∂wjk

Putting it all together     Substituting (7.18), (7.19), and (7.20) into (7.17):

                                   ∂E
                                       = (ok − tk ) ok (1 − ok ) xj .                          (7.21)
                                  ∂wjk


                                                  95
Intelligent Systems Companion                      Backpropagation Learning in Multi-Layer Perceptrons


   Define the error signal for neuron k as

                                      δk = (ok − tk ) ok (1 − ok ).                               (7.22)
```

### Findings
- **Notation inconsistency:**  
  - The notation for activations and weighted inputs is sometimes ambiguous or inconsistent. For example, the text uses both \(a_j^{(l)}\) and \(z_j^{(l)}\) but does not explicitly define \(a_j^{(l)} = \phi(z_j^{(l)})\) at the start of the section. Although it appears later, an explicit initial definition would improve clarity.  
  - The notation \(a_k\) and \(o_k\) seem to be used interchangeably for output neuron activations (e.g., equations (7.16) and (7.18) use \(o_k\), while earlier sections use \(a_k\)). This could confuse readers; consistent notation should be maintained or explicitly related.

- **Ambiguous or missing definitions:**  
  - The bias term \(b_j^{(l+1)}\) is introduced but not explicitly discussed in the gradient derivations. While it is standard to include bias gradients, the notes do not show the derivative of the error with respect to biases or how biases are updated.  
  - The activation function \(\phi(\cdot)\) is introduced but not explicitly defined before its derivative is used. Although sigmoid is mentioned later, a general definition or examples of activation functions would be helpful.

- **Mathematical clarity and justification:**  
  - Equation (7.11) states \(\delta_k^{(L)} = a_k^{(L)} - t_k \phi'(z_k^{(L)})\), which is incorrect. The correct formula for the output layer error term is:  
    \[
    \delta_k^{(L)} = \frac{\partial E}{\partial z_k^{(L)}} = \frac{\partial E}{\partial a_k^{(L)}} \cdot \phi'(z_k^{(L)}) = (a_k^{(L)} - t_k) \phi'(z_k^{(L)}).
    \]  
    The current expression incorrectly multiplies \(t_k\) by \(\phi'(z_k^{(L)})\) instead of the difference \(a_k^{(L)} - t_k\). This is a significant error and should be corrected.

- **Logical gaps:**  
  - The derivation of the hidden layer error term \(\delta_j^{(l)}\) in equation (7.15) uses the chain rule but does not explicitly show the step where the derivative \(\partial z_k^{(l+1)} / \partial a_j^{(l)} = w_{kj}^{(l+1)}\) is used. This step is crucial and should be explicitly stated for clarity.  
  - The transition from the general chain rule expression (7.13) to the summation form (7.14) could be better explained, especially clarifying the indices and the role of weights connecting layers \(l\) and \(l+1\).

- **Inconsistent or unclear variable usage:**  
  - In the section "Step 3: Derivative of activation with respect to weight," the activation \(a_k\) is defined as a weighted sum of inputs \(x_j\), but previously activations were denoted \(a_j^{(l)}\). The variable \(x_j\) is introduced without definition; it presumably corresponds to \(a_j^{(l)}\), but this should be explicitly stated to avoid confusion.  
  - The use of \(w_{jk}\) and \(w_{kj}\) is inconsistent. For example, in the hidden layer error term derivation, weights are denoted \(w_{kj}\), while in the output layer gradient derivation, weights are \(w_{jk}\). The order of indices should be consistent and clearly defined (e.g., \(w_{ij}\) is weight from neuron \(i\) in layer \(l\) to neuron \(j\) in layer \(l+1\)).

- **Typographical and formatting issues:**  
  - Some equations have misplaced or missing parentheses, e.g., in (7.11) and (7.21), which can lead to misinterpretation of terms.  
  - The notation \(\phi'(z_j^{(l)})\) is sometimes written as \(\phi' z_j^{(l)}\) without parentheses, which can be confusing.

- **Additional suggestions:**  
  - It would be helpful to explicitly state the dimensions of vectors and matrices involved in the gradient computations to reinforce understanding of shapes and ensure correctness.  
  - The summary section could benefit from a concise algorithmic pseudocode or stepwise outline of backpropagation to complement the mathematical derivations.

**Summary:**  
- Correct the error term formula for the output layer (equation 7.11).  
- Maintain consistent notation for activations, outputs, and weights throughout.  
- Explicitly define all variables when first introduced, including \(x_j\), biases, and activation functions.  
- Clarify and justify each step in the chain rule applications, especially for hidden layers.  
- Address minor typographical and formatting issues to improve readability.
