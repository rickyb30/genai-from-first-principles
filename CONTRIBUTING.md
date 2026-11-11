# Contributing

Thank you for helping build an open, vendor-neutral generative AI catalog. This guide covers
the principles every contribution must follow, the lesson format, the style guide, the code and
diagram rules, and the review checklist.

By contributing, you agree that your text and diagrams are licensed under
[CC BY 4.0](LICENSE) and your code under the [MIT License](LICENSE-CODE). Please also follow the
[Code of Conduct](CODE_OF_CONDUCT.md).

## Contents

- [Non-negotiable principles](#non-negotiable-principles)
- [How lessons are organized](#how-lessons-are-organized)
- [Writing style guide](#writing-style-guide)
- [Terms and the glossary](#terms-and-the-glossary)
- [Sources, accuracy and dates](#sources-accuracy-and-dates)
- [Code guide](#code-guide)
- [Diagram guide](#diagram-guide)
- [Running the checks](#running-the-checks)
- [Lesson review checklist](#lesson-review-checklist)
- [Workflow, status and commits](#workflow-status-and-commits)

## Non-negotiable principles

### 1. Vendor-neutral, always

- Teach concepts, patterns and open standards, not products.
- Don't put vendor-specific code, SDKs, configuration, CLI commands, API keys, endpoints or
  pricing in lessons. This covers model providers, cloud platforms, vector database products,
  agent frameworks and orchestration libraries.
- Use generic vocabulary: "a model provider", "a vector index", "an API gateway", "an
  orchestration layer", "an inference server".
- Product and model names may appear **only** in a historical or citation context, for example a
  paper title, or "the 2017 *Attention Is All You Need* paper". Never put them in instructions,
  code or configuration. Mark a citation line with `<!-- citation -->` at the end, or put the
  reference under `## Further reading`.
- Open standards and open research are welcome: protocols, specifications, published papers,
  OWASP, NIST and ISO frameworks, and OpenTelemetry semantic conventions. Describe them as
  standards, not products.
- When the industry implements a pattern in different ways, describe the pattern and its
  trade-offs, not one implementation.
- Before merging, the maintainer runs an automated check for vendor and product names. That
  check is a safety net, not the definition. Reviewers judge the spirit of the rule.

### 2. Every code example runs offline, with no accounts

- Python 3.11 or newer.
- Levels 0–2 use only the standard library, NumPy and matplotlib. Learners build each concept
  from scratch first.
- scikit-learn and PyTorch may appear only **after** the from-scratch version has been taught,
  and only in files marked as library sections (see [Approved libraries](#approved-libraries)).
- No network calls, API keys or paid services. When a lesson needs a language model, code
  against the interface in `shared/` using `MockLLM` (scripted) or `TinyLM` (built in L2-15).
  Never ship an adapter for a real vendor.
- Every code file runs with `python file.py` and documents its exact expected output.

### 3. Accuracy over confidence

- Never invent facts, numbers, papers, authors or URLs. If you aren't sure a reference exists,
  leave it out or mark it `TODO(verify)`.
- Prefer primary sources: original papers, standards documents and university course material.
- Mark time-sensitive claims "As of Month YYYY", and update `last_reviewed` in the front matter.
- Label active research and open debate as such, separately from settled knowledge.
- No hype, no fear-mongering, and no predictions stated as fact.

### 4. Teach for understanding

- Define every term the first time it appears, and add it to [GLOSSARY.md](GLOSSARY.md).
- Go from intuition, to a concrete example, to the formal idea, to code, to practice.
- Use analogies, and always say where each one breaks down.
- Use plain language and short sentences. Assume intelligence, not prior knowledge.

## How lessons are organized

### Levels, modules and lessons

The catalog has 8 levels. Each level is split into modules of 3–7 lessons. The full map, with
each lesson's ID, objective, prerequisites, time and status, is in [CURRICULUM.md](CURRICULUM.md).

### Folder layout

```text
curriculum/level-2-deep-learning-and-generative-models/
├── README.md                 # Level overview, objectives, lesson list
├── requirements.txt          # Pinned dependencies for this level
└── 04-attention-explained/   # NN-slug, where NN is the lesson number
    ├── README.md             # The lesson, structured as described below
    ├── code/                 # Runnable examples
    ├── diagrams/             # name.py draws name.png
    └── exercises/
        ├── exercise.py       # Starter code with TODOs
        └── solutions/
            └── exercise.py   # Complete, runnable solution
```

### Lesson structure

Every lesson `README.md` starts with front matter, then uses these H2 sections, in this order:

```markdown
---
id: L2-04                         # matches CURRICULUM.md
title: Attention, Explained       # matches CURRICULUM.md
level: 2
module: 2B Attention and the transformer
prerequisites: [L2-02, L2-03]     # matches CURRICULUM.md
estimated_time: 50 min            # matches CURRICULUM.md
tags: [transformers, attention]
last_reviewed: 2026-11-09
---

# Attention, Explained

> **TL;DR** — Two or three sentences anyone can understand.

## Learning objectives            (3–5, with measurable verbs: explain, compute, implement, compare, evaluate)
## Why this matters
## 🟢 Core idea (everyone)
## 🟡 How it works (practitioner)
## 🔴 Going deeper (expert)
## Common misconceptions          (3–5 "Myth / Reality" pairs)
## Hands-on exercise              (solution in a collapsed <details> block and in exercises/solutions/)
## Check your understanding       (5 questions in the quiz format below)
## Key terms                      (each linked to GLOSSARY.md)
## Further reading                (3–6 vetted sources, each with 🟢/🟡/🔴 and a one-line note)
## Next
```

Published lessons are the best examples to copy from.

### Quiz format

"Check your understanding" has exactly 5 questions, and each question has its own collapsed
answer. This format reads naturally on GitHub, never shows an answer before the reader asks for
it, and lets the catalog's learning site turn each question into an interactive quiz.

```markdown
1. Which of these is a generative task?

   - A. Labelling an email as spam
   - B. Writing a reply to an email
   - C. Sorting photos by date

   <details>
   <summary>Answer</summary>

   **B.** Writing a reply creates new content. A and C assign labels or an order to
   existing data.

   </details>

2. Which of these are limits of language models? *(choose all that apply)*

   - A. They can state false things fluently
   - B. They can't produce text
   - C. Their knowledge stops at a training cutoff

   <details>
   <summary>Answer</summary>

   **A, C.** …

   </details>

3. **Explain it to a colleague:** why does a language model sometimes make things up?

   <details>
   <summary>Model answer</summary>

   …

   </details>
```

| Question type | How to write it |
|---|---|
| Single choice | Options `- A.`, `- B.`… in order. Summary `Answer`. The answer starts with the bold letter: `**B.**` |
| Multiple choice | Add *(choose all that apply)* to the question. The answer starts with the bold letters: `**A, C.**` |
| Open | No options. Summary `Model answer` |

Rules:

- Include exactly one open **Explain it to a colleague** question. Mix the rest between recall
  and application.
- After the letters, always explain *why* the answer is right, and why the tempting wrong
  options are wrong.
- Test the lesson's learning objectives, not trivia.

### Layered depth

The three middle sections are the depth layers:

| Layer | Reader | Rules |
|---|---|---|
| 🟢 Core idea | Everyone | Intuition, analogy (with where it breaks down), diagram, worked example with real numbers. **No code needed.** |
| 🟡 How it works | Practitioner | Mechanics, step-by-step walkthrough, runnable code, common pitfalls |
| 🔴 Going deeper | Expert | Math, design trade-offs, failure modes at scale, open questions, interactions with other components |

A newcomer who reads only the 🟢 sections across the whole catalog should come away with solid
AI literacy. A 🔴 section must add real depth, not restate the earlier sections.

### Length

Aim for 2,500–4,500 words (30–60 minutes). Capstones can be longer. If a lesson grows past
about 5,000 words, split it and update CURRICULUM.md.

## Writing style guide

### Voice and tone

- Friendly, direct and precise. Write like an expert colleague who enjoys teaching.
- Use the second person ("you") and the active voice.
- Keep paragraphs short (1–4 sentences).
- Lead with intuition, then formalism.
- Never claim that one vendor or model is "best". The catalog should still be correct in five
  years because it teaches durable ideas.

### Language

- **Canadian English spelling:** behaviour, colour, neighbour, modelling, centre, defence, and
  *-ize* endings (organize, optimize, tokenize). Use "catalog" for this project. When in doubt,
  follow the *Canadian Oxford Dictionary*.
- **Code is the exception.** Identifiers, keywords and library names keep their own spelling
  (`color=` in matplotlib, `normalize()`), even next to Canadian prose.
- Write for a global audience. Avoid idioms, sports metaphors, slang and cultural references
  that don't translate.
- Use inclusive examples: varied names, places and contexts. Prefer neutral settings (a
  library, a weather station, a town handbook) over culturally specific ones.
- Spell out an acronym the first time it appears: "retrieval-augmented generation (RAG)".

### Numbers and math

- Use concrete numbers in examples: "a vocabulary of 50,000 tokens", not "a large vocabulary".
- Use SI units and digits for measurements ("4 GB", "120 ms").
- Write inline math as `$...$` and display math as `$$...$$`. GitHub renders both. Explain
  every symbol in words right after the equation.
- Show worked examples step by step, and round consistently (usually 3 significant figures).

### Formatting

- One H1 per lesson (the title). Use the H2 headings from [Lesson structure](#lesson-structure) exactly. Use H3 for subsections.
- Use **bold** for a term on first use, and *italics* for emphasis (sparingly).
- Use a fenced code block with a language tag for every code or command sample.
- Use tables for comparisons, and callouts (`> **Note:**`, `> **Warning:**`) sparingly.
- Put quiz and exercise answers in collapsed `<details>` blocks.
- Use relative links between lessons, and link the lesson README, not the folder.

### Analogies

Every analogy needs a "Where the analogy breaks down" sentence. Example:

> Attention is like a reader skimming a page for the words that matter most to their question.
> **Where the analogy breaks down:** a reader skims once, but attention scores every word against
> every other word, in parallel, in every layer.

### Settled knowledge vs open questions

Label research and debate explicitly:

> **Open question (as of November 2026):** …

or

> **Active research:** …

## Terms and the glossary

- Bold a term and define it in plain language the first time it appears in the catalog.
- Add it to [GLOSSARY.md](GLOSSARY.md) in alphabetical order, linking the lesson that introduces it.
- List it under the lesson's `## Key terms`, linked to its glossary entry.
- If a term is already in the glossary, link to it instead of redefining it. A one-line reminder
  is fine.

## Sources, accuracy and dates

- **Further reading:** 3–6 sources per lesson, each with a level marker (🟢/🟡/🔴) and a one-line
  note on why it's worth reading.
- **Preferred sources:** original papers, standards documents, open textbooks and university
  course material. Avoid marketing pages, vendor blogs and paywalled sources where an open
  alternative exists.
- **Citation format:** `Title — Authors (Year). Venue or publisher, if useful.` Link to a stable
  URL (an arXiv abstract page, a DOI, or a standards body's page).
- **Unverified items:** write `TODO(verify)` next to anything you couldn't confirm. Each
  module's summary lists these, and they must be resolved before a lesson is "published".
- **Dates:** mark time-sensitive claims "As of Month YYYY". Regulations, standards versions,
  benchmark results and "state of the art" claims are always time-sensitive.
- **Legal topics:** governance and regulation lessons summarize, and state clearly that they are
  not legal advice.

## Code guide

### Rules for every `.py` file

1. **Runs on its own:** `python file.py`, from any working directory, with no arguments, no
   network and no keys.
2. **Docstring first:** what the file teaches, how to run it, and an `Expected output:` section
   at the end. Before merging, every example is run and its output must match exactly. A line
   that contains only `...` matches any number of lines.
3. **Deterministic:** fix every random seed (`np.random.default_rng(seed=0)`).
4. **Fast:** under 60 seconds on a laptop CPU. If a full run takes longer, read
   `AI_CATALOG_QUICK` and do less work when it's `"1"`. Automated runs use quick mode, so print
   only lines that don't change between modes, or use `...` for the lines that do.
5. **Readable over clever:** type hints, descriptive names, and comments that explain *why*.
   This is teaching code, not production code.
6. **Plots** use matplotlib's non-interactive backend (`matplotlib.use("Agg")`) and save a PNG
   next to the script, with the same name.

[shared/mock_llm.py](shared/mock_llm.py) follows all of these rules: run it and compare its
output with its docstring.

### Importing shared code

Lesson code that imports from `shared/` starts with this bootstrap, which finds the
repository root without any installation step:

```python
import sys
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "shared").is_dir())
sys.path.insert(0, str(ROOT))

from shared.mock_llm import MockLLM  # noqa: E402
```

### Helper modules

A file whose name starts with `_` (for example `code/_data.py`) is a helper imported by other
examples. The example runner skips it, so it doesn't need an expected output.

### Approved libraries

| Library | Where it's allowed |
|---|---|
| Python standard library | Everywhere |
| NumPy, matplotlib | Everywhere |
| scikit-learn, PyTorch | Only in files named `*_with_library.py`, and only after the from-scratch version is taught |

An automated check enforces this table. Every `requirements.txt` must pin exact versions
(`numpy==2.4.6`) of approved libraries only. To propose a new library, open an issue explaining
why the standard library and NumPy aren't enough.

### Language models in examples

- Use `shared.llm_interface` types (`Message`, `ToolSpec`, `GenerationResult`) and a model that
  satisfies the `LanguageModel` protocol.
- Use `MockLLM` to teach control flow (prompting patterns, tool calling, agents, RAG), and
  `TinyLM` (from Level 2 onwards) when a real, if tiny, model matters.
- Never ship an adapter for a real provider. [shared/README.md](shared/README.md) explains how
  readers can write their own.

## Diagram guide

Workflow and architecture diagrams are **PNG images drawn by Python scripts**. Mermaid and
other text-based diagram formats are not used.

- **One script per diagram.** Each script lives in the lesson's `diagrams/` folder and has the
  same name as its PNG (`agent_loop.py` draws `agent_loop.png`). Commit both. Never edit a PNG
  by hand.
- **Use the kit.** Build diagrams with [shared/diagram_kit.py](shared/diagram_kit.py). It
  provides boxes, arrows, curved arrows and dashed group boundaries in one consistent style.
  [assets/diagrams/level_map.py](assets/diagrams/level_map.py) is a complete example.
- **Colours have fixed meanings** (a colour-blind-safe palette):

  | Kind | Colour | Use for |
  |---|---|---|
  | `default` | Blue | A component or step |
  | `action` | Orange | Something that acts or changes state (a model call, a tool) |
  | `data` | Green | Stored data (an index, a database, a document set) |
  | `human` | Yellow | A person |
  | `external` | Grey | Anything outside the system boundary |
  | `risk` | Pink | Untrusted input, a threat or an attacker |

- **Accessibility.** Every image has descriptive alt text (what the diagram shows, not
  "diagram"), followed on the next line by a one-line italic description:

  ```markdown
  ![The agent loop: the model reasons, calls a tool, observes the result, and repeats until done](diagrams/agent_loop.png)

  *The agent loop cycles through reason, act and observe until a stop condition is met.*
  ```

- Colour must never be the only way to tell things apart. Repeat it in labels or line styles.
- Keep diagrams simple: about 3–9 boxes. Split a bigger diagram into two.

## Running the checks

Before you open a pull request, run every code file you added or changed, and confirm that its
output matches the `Expected output:` section of its docstring exactly:

```bash
python path/to/your_example.py
```

Before merging, the maintainer also runs automated checks for:

| Check | What it verifies |
|---|---|
| Vendor terms | No vendor or product names outside citation contexts |
| Imports and requirements | Only approved libraries are imported, and versions are pinned |
| Curriculum and lessons | CURRICULUM.md is consistent, and every lesson has valid front matter and all required sections |
| Diagrams and images | Every PNG has its source script, every image has alt text and a description, and no Mermaid appears |
| Examples | Every example runs offline and prints its documented output |
| Markdown and links | Markdown style is consistent, and links resolve |

If a check fails, the maintainer will point to the line and the rule it breaks.

## Lesson review checklist

Every lesson is reviewed by someone who didn't write it, using this checklist:

- [ ] **Beginner test:** can someone with no AI background follow every 🟢 section without outside help?
- [ ] **Expert test:** does the 🔴 section add real depth (trade-offs, failure modes, math, open questions) rather than restate earlier sections?
- [ ] Every new term is defined on first use and added to the glossary.
- [ ] **Vendor-neutral:** no product, SDK, cloud service or framework names in instructions, code or configuration, and the vendor-term check passes.
- [ ] All code runs offline with no keys, and the output matches the expected-output comments.
- [ ] Every factual claim is accurate. Time-sensitive claims are marked "As of". No invented references. Unverifiable items are marked `TODO(verify)`.
- [ ] Each objective is actually taught, and actually tested by the exercise or quiz.
- [ ] Every diagram is a script-generated PNG with descriptive alt text and a one-line text description. No image lacks alt text.
- [ ] Every analogy says where it breaks down.
- [ ] Settled knowledge is distinguished from open debate.
- [ ] The length is consistent with other lessons. Split the lesson if it covers too much.

## Workflow, status and commits

### Lesson status

| Status | Meaning |
|---|---|
| `planned` | In the outline. Not written yet |
| `drafted` | Written, code runs, automated checks pass |
| `reviewed` | Passed independent review against the checklist |
| `published` | Reviewed, merged and linked from the level README |

Update the lesson's row **and** the summary table in [CURRICULUM.md](CURRICULUM.md) in the same
change. The curriculum check fails if they disagree.

### Writing a module

1. Write or update the level `README.md`.
2. Write each lesson in the structure above, with its code, diagrams, exercises and solutions.
3. Run every example and fix any failure.
4. Get an independent review against the checklist, and fix what it finds.
5. Update GLOSSARY.md and CURRICULUM.md.
6. Commit.

### Commit messages

Write a single-line message in the [Conventional Commits](https://www.conventionalcommits.org/)
style, with the level as the scope:

```text
feat(L2): add attention lessons L2-04..L2-06
fix(L3): correct recall@k example in L3-10
docs: clarify diagram colour rules
```
