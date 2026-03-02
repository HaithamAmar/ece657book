# Chapter 14 Voice Blocks (Draft Scaffold)

Purpose: This file is a scratchpad for the voice-heavy blocks in Chapter 14
(`notes_output/lecture_transformers.tex`). Edit freely; I will integrate the
final wording into the chapter while keeping math/notation consistent.

## 1) Opening narrative (seq2seq -> attention; translation thread)

Draft:

Parts of the book so far treated sequences as something you process step by
step: an RNN reads inputs in order, updates a hidden state, and emits outputs.
That picture is natural for tasks like translation, where you read a source
sentence and then produce a target sentence.

The classical encoder--decoder idea is simple: an encoder reads the source and
produces a representation; a decoder reads that representation and generates
the output one token at a time. The bottleneck is also simple: if the entire
source must be squeezed into one fixed-size vector, the model is forced to
``remember everything at once,'' even when only one source word matters for the
next output word.

Attention is the engineering fix. Instead of compressing the source into a
single summary and hoping the decoder can carry it forever, the decoder is
allowed to look back at the encoder states and ask, at each step, ``which part
of the source should I use right now?'' That single design choice removes the
worst of the memory bottleneck, and it opens the door to the Transformer idea:
if ``looking around'' is the main operation, you can do it in parallel across
positions instead of marching through time.

## 2) Q/K/V intuition paragraph (weighted average; your voice)

Draft:

I like to read attention as a weighted average over a set of candidate pieces
of information. A query asks a question (what do I need?), keys advertise what
each candidate contains (what am I about?), and values carry the actual content
that gets mixed. The weights come from similarity: a query scores each key, a
softmax turns those scores into nonnegative weights that sum to one, and the
output is the weighted sum of the value vectors.

## 3) BERT vs GPT explanation (objectives + why it matters)

Draft:

Once you have attention blocks, most of the ``model family'' distinctions come
from two choices: (i) which directions a token is allowed to attend to, and
(ii) what prediction problem you train on.

Encoder-only models (BERT-style) see the whole input at once (no causal mask).
They are trained by hiding some input tokens and asking the network to predict
the missing pieces (masked language modeling). A special pooled vector (often a
prepended [CLS] token) can then serve as a sentence representation for
classification.

Decoder-only models (GPT-style) enforce a causal mask: each position can only
use the past. Training is next-token prediction, and inference is the same loop
run forward: sample or choose the next token, append it, and repeat. This
alignment between training and generation is one reason decoder-only models are
the default starting point for text generation.

Encoder--decoder models keep both roles: the encoder builds a representation of
the source, and the decoder generates the target while attending back to the
encoder states (cross-attention). That is the natural fit for translation and
other seq2seq problems.

