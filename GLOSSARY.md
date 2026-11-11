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

### Backpropagation

The method used to train neural networks: it works out how much each parameter contributed to an error, so each can be adjusted to reduce it. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Bias

In AI, systematic unfairness or skew in a system's outputs, often inherited from its training data. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Bigram

A pair of neighbouring items, such as two words in a row. A bigram model predicts each word from only the one before it. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Calibration

How well a model's confidence matches its accuracy. A well-calibrated model that is "90% sure" is right about 90% of the time. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Chatbot

A program that converses with people in text or speech. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Confabulation

Another word for hallucination, used in NIST's Generative AI Profile. Some researchers prefer it because "hallucination" wrongly suggests the system perceives things. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Conventional software

A program that follows step-by-step instructions written by people, rather than behaviour learned from data. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Deep learning

Machine learning that uses neural networks with many layers. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Dependency pinning

Fixing the exact version of every package a project uses (for example numpy==2.4.6), so everyone gets the same behaviour. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Deterministic

Giving exactly the same output every time it runs with the same input. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Discriminative model

A model that chooses between categories or predicts a value for an input, such as "spam or not spam". Contrast with a generative model. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Docstring

The descriptive text at the start of a Python file or function. In this catalog, every example's docstring ends with its expected output. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Expert system

A program that captures a specialist's knowledge as many hand-written "if… then…" rules. Popular in the 1980s. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Foundation model

A very large model trained on broad data that can be adapted to many different tasks. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Generative AI

AI whose main output is new content, such as text, images, audio, video or code. Today the term usually means deep learning models that create content. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Generative model

A model that learns the patterns of a kind of data well enough to produce new examples of it. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Graphics processing unit (GPU)

A chip originally designed for graphics that performs many calculations in parallel, which makes it well suited to neural networks. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Grounding

Connecting a model's output to specific, checkable sources, so its claims can be verified. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Hallucination

When a generative model produces content that sounds plausible but is false or made up, such as an invented fact or citation. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Human in the loop

A design in which a person reviews, approves or corrects an AI system's output before it is used. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Language model

A model trained to predict the next piece of text, given the text so far. Repeating that prediction produces new text. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Large language model (LLM)

A language model trained on an enormous amount of text, with billions of parameters. Chat assistants are built on them. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Layer

One stage of a neural network, which transforms the output of the stage before it. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Learning path

A recommended route through the catalog's lessons for a particular role or goal. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Leitner system

A simple spaced-repetition method using boxes: remembered cards move up a box and are reviewed less often, forgotten cards go back to box 1. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Machine learning (ML)

The part of AI in which systems learn their behaviour from data, instead of following rules written by people. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Memorization

When a model reproduces parts of its training data word for word, instead of producing new combinations. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### MockLLM

The catalog's scripted stand-in for a language model. It gives fixed, predictable replies, so examples run offline and repeatably. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Model

The result of training: a set of learned numbers, plus the calculation that uses them to turn inputs into outputs. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### N-gram model

A model that predicts the next word or character from counts of the previous few (n minus 1) items. A bigram model is the simplest kind. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Narrow AI

AI built and validated for a particular range of tasks. Most researchers would describe every AI system in use today (as of November 2026) as narrow, though some argue the largest models show meaningful generality. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Neural network

A model built from many simple calculating units, connected in layers, whose connection strengths are learned from data. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### NumPy

A free Python package for fast arithmetic on arrays of numbers. Almost every AI project in Python uses it. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Package

A bundle of ready-made code that you install and use in your own programs. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Parameter

One of the numbers inside a model that is adjusted during training. Large language models have billions of them. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Prerequisite

A lesson you should read before another one, because the later lesson builds on it. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Probability distribution

A description of how likely each possible outcome is. The probabilities of all outcomes add up to 1. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Prompt

The instruction, question or other input you give a generative model. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Prompt injection

An attack in which text the model reads, such as a web page or email, contains instructions that hijack the model's behaviour. *Introduced in [L0-04](curriculum/level-0-orientation/04-capabilities-limits-responsible-use/README.md).*

### Python

A popular, free programming language, and the program that runs code written in it. Every example in this catalog uses it. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Random seed

The starting number for a random-number generator. The same seed always produces the same sequence of "random" choices. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Retrieval practice

Learning by recalling information from memory, for example by answering quiz questions. It strengthens memory more than re-reading. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Rule-based system

A system whose behaviour comes from rules written by people, usually in an "if… then…" form. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Sampling

Drawing an outcome at random according to a probability distribution, so likely outcomes come up more often. Generative models sample to produce output. *Introduced in [L0-01](curriculum/level-0-orientation/01-what-generative-ai-is/README.md).*

### Scale

The size of a model and its training: the number of parameters, the amount of data and the amount of computation. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Self-supervised learning

Learning in which the answers come from the data itself, such as predicting the next word of a text. It's how large language models are mostly trained. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Smoothing

Techniques that give some probability to contexts or continuations an n-gram model has never seen, often by borrowing from shorter contexts. *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Spaced repetition

Reviewing material at increasing intervals over days and weeks, which makes it last much longer than the same study time in one session. *Introduced in [L0-05](curriculum/level-0-orientation/05-how-to-use-this-catalog/README.md).*

### Supervised learning

Learning from examples that each come with the correct answer, such as emails labelled "spam" or "not spam". *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Symbolic AI

AI built from hand-written symbols, rules and logic, rather than learned from data. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

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

### Turing test

A test proposed by Alan Turing in 1950: can a machine hold a text conversation that an interrogator can't tell apart from a person's? *Introduced in [L0-03](curriculum/level-0-orientation/03-a-short-history/README.md).*

### Typosquatting

Publishing a malicious package under a name that looks like a popular one, hoping people mistype it. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*

### Unsupervised learning

Learning to find structure in data that has no answers attached, such as grouping similar items. *Introduced in [L0-02](curriculum/level-0-orientation/02-the-nested-map/README.md).*

### Virtual environment

A private folder of Python packages for one project, so it can't affect, or be affected by, other projects. *Introduced in [L0-06](curriculum/level-0-orientation/06-your-toolkit/README.md).*
