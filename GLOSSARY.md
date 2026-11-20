# Glossary

Every term the catalog introduces, in plain language, with a link to the lesson that first
teaches it. Entries are kept in alphabetical order.

When a lesson introduces a new term, its author adds an entry here in the same pull request
(see [CONTRIBUTING.md](CONTRIBUTING.md#terms-and-the-glossary)).

## Format

Each entry is a level-3 heading, a one- to three-sentence definition a newcomer can understand,
and the lesson that introduces it:

```markdown
### Embedding

A list of numbers that represents a piece of text (or an image, or a sound) so that similar
meanings end up close together. *Introduced in [L2-02](curriculum/level-2-deep-learning-and-generative-models/02-embeddings/README.md).*
```

## Terms

### AI winter

A period when funding, interest and progress in AI fall sharply, usually after early promises go unmet. The main ones were in the mid-1970s and from the late 1980s to the early 1990s. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Arithmetic coding

A compression method that uses a model's probabilities to encode a message in close to the model's cross-entropy in bits per symbol. A better predictor gives a shorter encoding. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Array

An ordered collection of numbers that can be processed all at once. NumPy's main data type. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Artificial general intelligence (AGI)

A hypothetical AI system that matches or exceeds people across essentially all cognitive tasks. There is no agreed definition or test, and whether or when it could exist is debated. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Artificial intelligence (AI)

The broad field of making machines do tasks we'd call intelligent, such as recognizing speech, planning, deciding or creating. There is no single agreed definition. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Artificial neuron

A simple calculating unit, loosely inspired by brain cells, that combines its inputs into one output. Neural networks are built from many of them. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Attention

A mechanism that lets a model decide how much each part of its input should influence each part of its output. It's the core of the transformer. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Automation bias

The tendency of people to over-trust the output of an automated system and check it less carefully than they should. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Autoregressive model

A model that generates a sequence one piece at a time, each piece drawn from a distribution conditioned on everything generated so far. Language models work this way. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Backpropagation

The method used to train neural networks: it works out how much each parameter contributed to an error, so each can be adjusted to reduce it. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Bayes' rule

A formula for reversing a conditional probability: P(A | B) = P(B | A) P(A) / P(B). It updates a belief about A after seeing B. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Bias

In AI, systematic unfairness or skew in a system's outputs, often inherited from its training data. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Bias (parameter)

A learned constant added to a weighted sum, such as b in wx + b. Unrelated to the unfairness meaning of bias. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Bigram

A pair of neighbouring items, such as two words in a row. A bigram model predicts each word from only the one before it. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Bit

The unit of information when logarithms are taken base 2. One bit is the surprisal of an event with probability 1/2. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Calibration

How well a model's confidence matches its accuracy. A well-calibrated model that is "90% sure" is right about 90% of the time. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Categorical distribution

A probability distribution over a fixed, finite set of outcomes, such as the possible next tokens. Each outcome has its own probability, and they sum to 1. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Central difference

A numerical derivative that compares the function a small step on each side: (f(x + h) - f(x - h)) / 2h. It's much more accurate than a one-sided difference. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Chain rule

The calculus rule that the derivative of a composed function is the product of the derivatives of its steps. Backpropagation applies it through a whole model. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Chain rule of probability

The rule that a joint probability equals a product of conditionals: P(a, b, c) = P(a) P(b | a) P(c | a, b). It's how a language model scores a whole sequence. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Chatbot

A program that converses with people in text or speech. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Computational graph

A diagram of a calculation as a series of simple steps, each taking earlier values as inputs. Gradients flow backward along it. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Conditional probability

The probability of one event given that another has happened, written P(A | B). It equals P(A, B) / P(B). *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Confabulation

Another word for hallucination, used in NIST's Generative AI Profile. Some researchers prefer it because "hallucination" wrongly suggests the system perceives things. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Conventional software

A program that follows step-by-step instructions written by people, rather than behaviour learned from data. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Cosine similarity

A measure of how closely two vectors point the same way: the dot product divided by both lengths. It runs from -1 (opposite) through 0 (unrelated) to 1 (same direction) and ignores length. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Cross-entropy

The average surprisal when outcomes come from one distribution but are scored with a model's probabilities. It's the loss language models are trained to lower. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Cumulative distribution

Running totals of probabilities in a fixed order. Sampling picks the first outcome whose running total passes a uniform random number. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Deep learning

Machine learning that uses neural networks with many layers. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Dependency pinning

Fixing the exact version of every package a project uses (for example numpy==2.4.6), so everyone gets the same behaviour. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Derivative

The rate at which a function's output changes as its input changes: the slope of its tangent line at a point. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Deterministic

Giving exactly the same output every time it runs with the same input. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Dimension

The number of entries in a vector. A vector with three numbers lives in three-dimensional space. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Discriminative model

A model that chooses between categories or predicts a value for an input, such as "spam or not spam". Contrast with a generative model. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Distributional hypothesis

The idea that words used in similar contexts tend to have similar meanings. It's why vectors learned from text put related words near each other. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Docstring

The descriptive text at the start of a Python file or function. In this catalog, every example's docstring ends with its expected output. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Dot product

Multiply two equal-length vectors entry by entry and add the results. It's large when the vectors point the same way and are long. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Empirical distribution

The distribution given by a dataset's own frequencies: each observed outcome gets probability equal to the fraction of times it appears. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Entropy

The average surprisal of a distribution: how unpredictable its outcomes are. It's zero for a certain outcome and largest for a uniform distribution. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Entropy rate

The average entropy of the next symbol given all previous ones, in the limit of long text. It measures how predictable a source such as English text is. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Euclidean distance

The straight-line distance between the tips of two vectors: the length of their difference. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Expected value

The probability-weighted average of a quantity: what you'd get on average over many draws. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Expert system

A program that captures a specialist's knowledge as many hand-written "if… then…" rules. Popular in the 1980s. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Exploding gradient

When gradients grow very large as they pass back through many steps, because many slopes larger than 1 multiply together. Training becomes unstable. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Finite difference

An estimate of a derivative from the change in a function's output over a small step in its input. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Forward KL

KL divergence measured from the data's distribution to the model's, D_KL(P || Q). Minimizing it is the same as maximum likelihood and tends to be mode-covering. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Forward pass

Running a calculation from inputs to output, keeping the intermediate values the backward pass will need. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Forward-mode differentiation

Computing derivatives by multiplying the chain rule's local derivatives from the input side. One pass gives the derivatives of every output with respect to one input. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Foundation model

A very large model trained on broad data that can be adapted to many different tasks. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Generative AI

AI whose main output is new content, such as text, images, audio, video or code. Today the term usually means deep learning models that create content. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Generative model

A model that learns the patterns of a kind of data well enough to produce new examples of it. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Gibbs' inequality

The result that cross-entropy is never smaller than entropy, with equality only when the model matches the true distribution. Equivalently, KL divergence is never negative. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Gradient

The vector of all partial derivatives of a function. It points in the direction of steepest increase. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Gradient checking

Testing a hand-written or automatic gradient by comparing it with a numerical estimate from finite differences. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Gradient descent

Training by repeatedly taking a small step in the direction opposite to the gradient of the loss. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Graphics processing unit (GPU)

A chip originally designed for graphics that performs many calculations in parallel, which makes it well suited to neural networks. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Grounding

Connecting a model's output to specific, checkable sources, so its claims can be verified. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Gumbel-max trick

A way to sample from a categorical distribution: add independent Gumbel-distributed noise to each log-probability and take the largest. The result is an exact sample. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Hallucination

When a generative model produces content that sounds plausible but is false or made up, such as an invented fact or citation. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Held-out data

Data kept out of training and used only to evaluate a model. Scores on it show how well the model generalizes. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Human in the loop

A design in which a person reviews, approves or corrects an AI system's output before it is used. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Jacobian

The matrix of partial derivatives of every output of a function with respect to every input. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Joint probability

The probability that several events all happen together, written P(A, B). *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### KL divergence

Kullback–Leibler divergence: cross-entropy minus entropy. It measures the extra surprisal from using a model's probabilities instead of the true ones, is never negative, and isn't symmetric. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Language model

A model trained to predict the next piece of text, given the text so far. Repeating that prediction produces new text. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Large language model (LLM)

A language model trained on an enormous amount of text, with billions of parameters. Chat assistants are built on them. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Law of large numbers

The result that the average of many independent draws gets close to the expected value as the number of draws grows. It's why frequencies from large samples approach the true probabilities. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Layer

One stage of a neural network, which transforms the output of the stage before it. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Learning path

A recommended route through the catalog's lessons for a particular role or goal. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Leitner system

A simple spaced-repetition method using boxes: remembered cards move up a box and are reviewed less often, forgotten cards go back to box 1. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Likelihood

The probability a model assigns to the data actually observed, viewed as a function of the model's parameters. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Local derivative

The derivative of one step of a computational graph with respect to its own inputs. The chain rule multiplies these together. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Log-probability

The logarithm of a probability. Sums of log-probabilities replace products of probabilities, which avoids underflow on long sequences. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Logits

The raw, unnormalized scores a model produces, one per possible outcome. Softmax turns them into probabilities. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Loss function

A number that measures how badly a model does on some data. Training adjusts parameters to make it smaller. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Machine learning (ML)

The part of AI in which systems learn their behaviour from data, instead of following rules written by people. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Marginal probability

The probability of one event on its own, found by adding up a joint probability over all values of the other events. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Markov assumption

The simplifying assumption that the next state depends only on the current state, not on the longer history. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Markov chain

A random process that moves between states using fixed transition probabilities that depend only on the current state. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Matrix

A rectangular grid of numbers arranged in rows and columns. A model's parameters are mostly stored in matrices. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Matrix–vector product

Multiplying a matrix by a vector: each entry of the result is the dot product of one row of the matrix with the vector. The matrix's column count must equal the vector's dimension. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Maximum likelihood

Choosing a model's parameters to give the training data the highest probability. It's the same as minimizing cross-entropy on that data. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Memorization

When a model reproduces parts of its training data word for word, instead of producing new combinations. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### MockLLM

The catalog's scripted stand-in for a language model. It gives fixed, predictable replies, so examples run offline and repeatably. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Mode-covering

The tendency of a model trained with forward KL to spread probability over every region where the data has probability, even if that puts probability between the peaks. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Mode-seeking

The tendency of a model trained with reverse KL to settle on one region of high probability and ignore others. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Model

The result of training: a set of learned numbers, plus the calculation that uses them to turn inputs into outputs. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### N-gram model

A model that predicts the next word or character from counts of the previous few (n minus 1) items. A bigram model is the simplest kind. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Narrow AI

AI built and validated for a particular range of tasks. Most researchers would describe every AI system in use today (as of November 2026) as narrow, though some argue the largest models show meaningful generality. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Nat

The unit of information when logarithms are natural (base e). One nat is about 1.443 bits. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Negative log-likelihood

Minus the log of the probability a model gives the data, often averaged per token. Lower is better, and averaged per token it's the same as cross-entropy on that data. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Neural network

A model built from many simple calculating units, connected in layers, whose connection strengths are learned from data. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Norm

The length of a vector: the square root of the sum of its squared entries (the Euclidean norm). *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### NumPy

A free Python package for fast arithmetic on arrays of numbers. Almost every AI project in Python uses it. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### One-hot vector

A vector of zeros with a single 1 marking one category, such as the correct next token. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Package

A bundle of ready-made code that you install and use in your own programs. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Parameter

One of the numbers inside a model that is adjusted during training. Large language models have billions of them. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Partial derivative

The derivative of a function of several inputs with respect to one of them, holding the others fixed. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Perplexity

Two raised to the cross-entropy in bits (or e raised to it in nats). It's the number of equally likely choices that would be as surprising as the model is on average. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Prerequisite

A lesson you should read before another one, because the later lesson builds on it. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Probability distribution

A description of how likely each possible outcome is. The probabilities of all outcomes add up to 1. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Prompt

The instruction, question or other input you give a generative model. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Prompt injection

An attack in which text the model reads, such as a web page or email, contains instructions that hijack the model's behaviour. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Proper scoring rule

A way of scoring probabilistic forecasts in which, on average, honestly reporting your true beliefs scores best. Log loss is one. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Python

A popular, free programming language, and the program that runs code written in it. Every example in this catalog uses it. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Random seed

The starting number for a random-number generator. The same seed always produces the same sequence of "random" choices. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Relative error

The size of the difference between two values divided by their combined size. Unlike absolute error, it means the same thing for large and small values. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Retrieval practice

Learning by recalling information from memory, for example by answering quiz questions. It strengthens memory more than re-reading. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Reverse KL

KL divergence measured from the model's distribution to the data's, D_KL(Q || P). Minimizing it tends to be mode-seeking. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Reverse-mode differentiation

Computing derivatives by multiplying the chain rule's local derivatives from the output side. One pass gives the derivatives of one output, such as a loss, with respect to every input. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Rule-based system

A system whose behaviour comes from rules written by people, usually in an "if… then…" form. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Sampling

Drawing an outcome at random according to a probability distribution, so likely outcomes come up more often. Generative models sample to produce output. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Scale

The size of a model and its training: the number of parameters, the amount of data and the amount of computation. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Self-supervised learning

Learning in which the answers come from the data itself, such as predicting the next word of a text. It's how large language models are mostly trained. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Shape

The size of an array along each axis, such as (3, 4) for a matrix with 3 rows and 4 columns. Most array bugs are shape mismatches. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Smoothing

Techniques that give some probability to contexts or continuations an n-gram model has never seen, often by borrowing from shorter contexts. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Softmax

A function that turns a list of real-valued scores into a probability distribution by exponentiating each score and dividing by the total. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Spaced repetition

Reviewing material at increasing intervals over days and weeks, which makes it last much longer than the same study time in one session. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Stationary distribution

A distribution over a Markov chain's states that one more step of the chain leaves unchanged. Under mild conditions, the chain's long-run frequencies converge to it. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Supervised learning

Learning from examples that each come with the correct answer, such as emails labelled "spam" or "not spam". *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Surprisal

The information in one outcome: minus the log of its probability. Rare outcomes have high surprisal; certain ones have zero. *Introduced in [L1-03](curriculum/level-1-foundations/03-information-basics/README.md).*

### Symbolic AI

AI built from hand-written symbols, rules and logic, rather than learned from data. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Tangent line

The straight line that just touches a curve at one point and has the same slope there. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Terminal

A text window where you type commands for the computer. Also called a command line or shell. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### TinyLM

The small character-level transformer language model you build in Level 2. Later lessons use it as a real, if tiny, model. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Token

A piece of text that a language model reads and predicts: a whole word, part of a word or a single character, depending on the model. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Training

The process of adjusting a model's numbers, using examples, until it performs its task well. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Training cutoff

The date after which a model's training data stops. The model knows nothing later unless it's given newer information. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Training data

The examples a model learns from during training. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Transformer

A neural network design built around attention, introduced in 2017. As of November 2026, nearly all large language models are transformers. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Transpose

A matrix flipped over its diagonal, so its rows become columns. Written with a superscript T. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Turing test

A test proposed by Alan Turing in 1950: can a machine hold a text conversation that an interrogator can't tell apart from a person's? *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Typosquatting

Publishing a malicious package under a name that looks like a popular one, hoping people mistype it. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Underflow

When a number is too close to zero for the computer to store, so it becomes exactly 0. Multiplying many small probabilities causes it. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Uniform distribution

A distribution in which every outcome (or every value in a range) is equally likely. *Introduced in [L1-02](curriculum/level-1-foundations/02-probability-for-generative-models/README.md).*

### Unit vector

A vector with length 1. Dividing any non-zero vector by its norm gives a unit vector pointing the same way. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Unsupervised learning

Learning to find structure in data that has no answers attached, such as grouping similar items. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Vanishing gradient

When gradients shrink toward zero as they pass back through many steps, because many slopes smaller than 1 multiply together. Early layers then barely learn. *Introduced in [L1-04](curriculum/level-1-foundations/04-derivatives-gradients-chain-rule/README.md).*

### Vector

An ordered list of numbers, which you can also picture as an arrow from the origin. Models represent words, images and states as vectors. *Introduced in [L1-01](curriculum/level-1-foundations/01-vectors-matrices-similarity/README.md).*

### Virtual environment

A private folder of Python packages for one project, so it can't affect, or be affected by, other projects. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*
