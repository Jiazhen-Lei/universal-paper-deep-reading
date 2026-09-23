---
name: universal-paper-deep-reading
id: universal-paper-deep-reading
description: This skill should be used when the user provides an academic paper, arXiv URL or ID, local PDF/HTML/Markdown manuscript, paper notes, or asks for 精读, deep reading, novelty analysis, experiment audit, limitation critique, SOTA positioning, or structured reusable notes for a research paper in any domain.
agent_created: true
version: 2
contexts: any
activation: auto
match: /your regex pattern here/i
---

# Universal Paper Deep Reading

## Overview

Perform rigorous, evidence-grounded deep reading of academic papers across domains. Convert a paper into structured research notes that capture the paper's one-sentence thesis, motivation, method or system architecture, core innovations, theoretical foundations, experimental evidence, limitations, and relevance to the user's work.

Use a `关键图驱动 + 通俗/严谨双层讲解` approach. Let selected original figures anchor the explanation of the system or method, then cover the core theory, equations, and algorithms without turning the note into a formula dump.

This skill generalizes the user's preferred note pattern: `一句话 → Motivation → 关键配图与整体流程 → 方法/理论/算法 → 核心创新点 → 实验设计及结论 → 局限性`, then adds cross-domain checks for claims, assumptions, evidence quality, reproducibility, and future research value.

## Trigger Conditions

Use this skill for requests such as:

- “精读这篇论文”, “帮我读一下这个 PDF”, “deep read this paper”, “summarize this arXiv paper deeply”.
- Paper inputs in PDF, HTML, Markdown, text, DOI, arXiv URL/ID, OpenReview/ACL Anthology/ACM/IEEE page, or existing paper notes.
- Requests to analyze novelty, architecture, experiments, baselines, metrics, limitations, related-work positioning, or implementation implications.
- Requests to build a reusable literature note, paper card, SOTA comparison entry, rebuttal preparation note, or research-idea extraction.

Do not use this skill for casual one-paragraph summaries unless the user explicitly asks for deep reading or precision.

## Operating Principles

- Ground every substantive claim in the paper. Separate `作者声称` from `读者判断`.
- Prefer precise mechanisms over vague praise. Explain how the method works, what it changes, and why the change matters.
- Prefer visual anchors over detached prose. Use the paper's overview, architecture, workflow, algorithm, and decisive result figures when they materially improve understanding.
- Explain in two layers: first a plain-language mental model, then the precise mechanisms, notation, equations, algorithms, assumptions, and boundary conditions.
- Treat experiments as evidence, not decoration. Extract datasets, baselines, metrics, ablations, costs, and failure cases.
- Preserve uncertainty. Mark missing details, weak evidence, ambiguous claims, or unsupported causal conclusions.
- Produce notes in Chinese by default unless the user requests another language. Keep technical terms in English where precision matters.
- Be domain-adaptive: map the same reading skeleton to ML, systems, HCI, theory, security, science, medicine, social science, and survey papers.
- Never invent a figure, equation, variable meaning, algorithm step, or causal explanation. Label any reconstructed diagram or interpretation explicitly.

## Input Intake Workflow

1. Locate the source.
   - For a local PDF or image-based paper, read the file directly page by page and inspect figures/tables when available.
   - For HTML/Markdown/text notes, extract the readable content and preserve headings, tables, and code snippets.
   - For URLs, fetch the paper page and follow the PDF/arXiv/OpenReview/ACL/ACM link when needed.
   - If the paper is inaccessible or only a title is available, ask for the PDF or URL rather than hallucinating.

2. Establish metadata.
   - Extract title, authors, institutions, venue, year, paper type, domain, problem setting, artifacts, and code/data availability.
   - Identify whether the paper is primarily `method/system`, `benchmark/dataset`, `theory`, `empirical study`, `survey`, `application`, or `position paper`.

3. Choose reading depth.
   - `快速精读`: concise but structured; focus on main contribution and evidence.
   - `标准精读`: full section-by-section reconstruction and critique.
   - `研究型精读`: add comparison to adjacent work, implementation plan, and follow-up research ideas.
   - If unspecified, use `标准精读`.

4. Build two inventories before drafting.
   - `Figure Inventory`: figure/table number, page, caption, type, role in the argument, and whether it should appear in the final note.
   - `Formula & Algorithm Inventory`: equation/algorithm number, page, purpose, dependent concepts, and whether it is essential to understanding or reproducing the method.
   - Verify extracted captions, symbols, subscripts, and equation signs against the rendered page when text extraction or OCR may be unreliable.

## Multi-Pass Reading Procedure

### Pass 1: Map the Paper

Scan title, abstract, introduction, all figure/table captions, method overview, displayed equations, algorithms, experiment tables, limitations, and conclusion. Produce a short reading map:

- Research question: what problem is being solved?
- Claimed contribution: what is new according to the authors?
- Method shape: model, framework, algorithm, dataset, evaluation, or theory?
- Evidence shape: what experiments or arguments support the claim?
- Visual anchors: which figures best explain the problem, method, workflow, or decisive evidence?
- Formal anchors: which equations, theorems, objectives, or algorithms are indispensable?
- Immediate concern: what may be weak, missing, or overclaimed?

### Pass 2: Select and Explain the Key Figures

Select the smallest set of figures that makes the paper understandable. For a typical method or system paper, use 2-5 key figures; use fewer when the paper has fewer meaningful visuals. Do not add images merely to meet a quota.

Prioritize:

1. Overview, teaser, or problem-formulation figure.
2. System/method architecture.
3. Core algorithm, data flow, training, or inference workflow.
4. The result figure or table that most directly supports the main claim.
5. An ablation, failure case, or qualitative example needed to understand boundaries.

When image access allows, embed or crop the original figure in the final note. Preserve its `Figure/Table` number, original caption, and page. Use this fallback order when direct extraction fails:

1. Include a page or region screenshot containing the figure.
2. Cite the figure number/page and explain it without embedding.
3. Create a text or flowchart reconstruction only if it materially helps, labeled `根据论文重构，非论文原图`.

For each selected figure, explain:

- `它回答什么问题`: the figure's role in the paper.
- `如何读图`: the reading direction, legend, axes, colors, or symbols.
- `输入与输出`: what enters and leaves the depicted process.
- `逐步流程`: walk through each important module or stage in order.
- `连接为何存在`: what information, control, state, or gradient flows between modules.
- `最容易忽略的细节`: conditions, branches, shared parameters, feedback loops, or train/inference differences.
- `它能/不能证明什么`: distinguish illustration, mechanism, correlation, and experimental evidence.

After the figure walkthroughs, summarize the complete process as a numbered chain such as `① 输入 → ② 表征 → ③ 核心交互 → ④ 优化/决策 → ⑤ 输出`.

### Pass 3: Reconstruct the Core Argument

Fill the user's preferred note skeleton:

1. `一句话`: State the paper's essence in one dense sentence: `This paper does X by doing Y, to improve/enable Z under condition W`.
2. `Motivation`: List the concrete pain points, failure modes, gaps in prior work, and why existing methods are insufficient.
3. `关键配图与系统/方法架构`: Start with a plain-language overview, then use selected figures to explain the pipeline, modules, data/control flow, objective, decision process, or theoretical structure. For systems, identify components and runtime workflow; for ML methods, identify inputs, outputs, training/inference, and losses; for empirical papers, identify study design and variables.
4. `核心创新点`: Extract 3-6 innovations. For each one, include `what`, `how`, `why it matters`, and `what trade-off it introduces`.
5. `实验设计及结论`: Extract datasets, baselines, metrics, protocol, main results, ablations, human evaluation, statistical tests, efficiency/cost, and what each result actually proves.
6. `局限性`: Combine stated limitations and independent critique: assumptions, scope, scalability, evaluation validity, reproducibility, hidden costs, ethical/safety concerns, and deployment risks.

### Pass 4: Explain Theory, Equations, and Algorithms

Do not reproduce every formula. Select 1-5 core equations by default, adapting to the paper. Include an equation when removing it would make the method, proof, optimization target, or claimed novelty materially harder to understand.

For each core equation:

1. `解决什么问题`: its role in the method or argument.
2. `原始公式`: preserve the paper's symbols and equation number; use readable LaTeX.
3. `符号解释`: define every important variable, operator, index, dimension, and unit needed here.
4. `自然语言翻译`: explain the whole equation in one or two plain sentences.
5. `流程中的位置`: state when it is computed and what consumes its result.
6. `直觉与边界`: explain why it works, its assumptions, limiting cases, trade-offs, and failure modes.

For each core algorithm:

- State inputs, outputs, initialization, update rules, stopping condition, and returned result.
- Walk through the steps in execution order; use pseudocode only when it is clearer than prose.
- Distinguish training, inference, online, and offline stages.
- Explain the decisive difference from the baseline or standard algorithm.
- Report time, space, communication, sample, or optimization complexity when the paper provides it or it can be safely derived. Clearly label any derivation as independent analysis.

For theorem-heavy papers, also cover definitions, assumptions, theorem statement, proof strategy, and practical implication. Do not claim to have verified a proof unless the proof was actually checked.

### Pass 5: Audit the Evidence

Evaluate the paper's support for its claims:

- Dataset/task fit: whether the benchmark actually measures the intended capability.
- Baseline strength: whether baselines are current, well-tuned, and fairly compared.
- Metrics validity: whether metrics match human or domain-relevant quality.
- Ablation logic: whether each component is isolated and necessary.
- Generalization: whether results cover enough domains, languages, scales, or settings.
- Cost and practicality: runtime, training cost, annotation cost, data requirements, latency, memory, or deployment complexity.
- Reproducibility: code/data availability, hyperparameters, prompts, seeds, statistical uncertainty.

### Pass 6: Position the Paper

Place the work in context:

- Compare against prior work using a table when helpful: `Prior work → limitation → this paper's response → remaining gap`.
- Identify the paper's real novelty level: `incremental engineering`, `new framing`, `new mechanism`, `new dataset/benchmark`, `strong empirical result`, or `conceptual shift`.
- Note whether the novelty is in problem formulation, architecture, data, training, inference, evaluation, system integration, or application scenario.

### Pass 7: Extract Value for the User

End with actionable synthesis:

- `对我有什么用`: map insights to the user's project, research direction, implementation, evaluation, or writing.
- `可复用机制`: list reusable design patterns, prompts, modules, algorithms, metrics, or experimental protocols.
- `可追问问题`: identify 3-8 follow-up questions that would deepen understanding.
- `潜在研究机会`: list gaps that could become new experiments, papers, or engineering tasks.

## Writing Standard

- Lead with the conclusion, then explain causes, mechanisms, and evidence.
- Keep one main idea per paragraph. Use numbered steps for long workflows.
- Define a technical term in plain language at its first appearance; retain the English term when translation would reduce precision.
- Explain intuition before formalism, but never omit necessary conditions, assumptions, variables, or causal links for the sake of simplicity.
- Prefer concrete statements such as `module A passes retrieved evidence to module B` over empty praise such as `the framework is advanced`.
- Distinguish `论文事实`, `解释性理解`, and `独立判断`. Mark speculation explicitly.
- Avoid repeating the same architecture description in multiple sections. Let the figure walkthrough establish the flow and use the formal section for deeper mechanisms.

## Domain Adaptation Guide

Use the same skeleton, but adapt the method/evidence questions:

- `ML/AI method paper`: overview/architecture figure, training data, loss/objective, inference pipeline, ablations, compute, model scale, benchmark leakage risk.
- `Agent/system paper`: agents/roles, memory/state, orchestration, tool use, feedback loops, failure recovery, latency, controllability, evaluation of emergent behavior; prioritize architecture and execution-trace figures.
- `Dataset/benchmark paper`: data source, annotation protocol, quality control, task definition, leakage, coverage, metric reliability, benchmark saturation risk.
- `Theory paper`: definitions, assumptions, theorem statements, proof strategy, implications, counterexamples, relation to known results; use dependency or conceptual diagrams only when helpful and label reconstructions.
- `HCI/empirical study`: participant sampling, study design, variables, qualitative coding, statistical power, ecological validity; prioritize study-procedure and decisive result figures.
- `Survey paper`: taxonomy, inclusion criteria, coverage, organizing axes, missing literature, actionable synthesis; prioritize taxonomy and historical/relationship figures.
- `Applied science/medicine/social science`: hypothesis, intervention/exposure, controls, confounders, measurement validity, statistical robustness, external validity.

If a paper contains no meaningful architecture figure or core equation, do not invent one. Replace it with the most appropriate artifact for that paper type, such as a study-design diagram, taxonomy, theorem dependency map, or data-construction pipeline.

## Required Output Structure

Produce the final note in this order unless the user requests a different format:

```markdown
# 论文精读：<title>

## 0. 结论先行
- 一句话：...
- 核心判断：...
- 适合关注：...
- 不适合过度相信：...

## 1. 基本信息
| 项 | 内容 |
|---|---|
| Title | |
| Authors / Institution | |
| Venue / Year | |
| Paper Type | |
| Code / Data | |
| Reading Depth | |

## 2. Motivation
...

## 3. 关键配图与整体流程
### 3.1 一眼看懂系统 / 方法
### 3.2 核心配图索引
### 3.3 配图逐步讲解
#### Figure N：<图的作用>
![Figure N: <short description>](<image path or source URL>)
- 来源：Figure N，原始 caption，p.X
- 它回答什么问题：
- 如何读图：
- 输入与输出：
- 逐步流程：
- 容易忽略的细节：
- 它能/不能证明什么：
### 3.4 End-to-End 流程
① ... → ② ... → ③ ... → ④ ... → ⑤ ...

## 4. 方法、理论与算法
### 4.1 通俗版机制
### 4.2 严谨方法定义
### 4.3 核心公式逐项解释
### 4.4 算法步骤 / 伪代码
### 4.5 Training / Inference 或运行阶段
### 4.6 复杂度、假设与适用边界

## 5. 核心创新点
| 创新点 | 做了什么 | 为什么重要 | 代价/风险 |
|---|---|---|---|

## 6. 实验设计及结论
### 6.1 Datasets / Tasks
### 6.2 Baselines
### 6.3 Metrics
### 6.4 Main Results
### 6.5 Ablations / Analysis
### 6.6 Evidence Audit

## 7. 局限性与批判
### 作者承认的局限
### 独立判断的局限
### 最可能失败的场景

## 8. 与相关工作的关系
| 方向/工作 | 解决什么 | 本文差异 | 剩余问题 |
|---|---|---|---|

## 9. 对我的启发
- 可复用机制：
- 可借鉴实验：
- 可转化为项目/论文的想法：
- 下一步建议阅读：

## 10. 追问清单
1. ...
```

Adapt the template to the paper rather than leaving empty sections. Omit the image Markdown line when no extractable image exists, but retain the source reference and explanation.

## Quality Gates Before Finalizing

Before answering, verify:

- The note contains enough paper-specific details that it could not apply to any random paper.
- Important numbers from experiments are preserved when available.
- The most useful overview/architecture/workflow figures are embedded or precisely referenced when available.
- Every selected figure is interpreted step by step rather than merely mentioned or pasted.
- The note gives a clear end-to-end account of input, processing, interactions, and output.
- Core theory, equations, and algorithms are covered when present; no essential mechanism is hidden behind a purely intuitive summary.
- Every included equation defines its important symbols and connects back to the workflow.
- The explanation is understandable without sacrificing assumptions, boundary conditions, or technical precision.
- Limitations include independent critique, not only author-provided statements.
- The final synthesis clearly distinguishes fact, interpretation, and speculation.
- Original figures and reconstructed diagrams are clearly distinguished.
- If the source was incomplete, explicitly state what was unavailable and avoid pretending full coverage.

## Pitfalls

- Local PDF reading may return a binary-display error in some environments. If direct page reading fails, fall back to text extraction with an isolated Python environment and a PDF parser such as `pypdf`; wrap extracted text at a moderate line width before reading so long PDF lines are not truncated by the file reader.
- When extracting PDFs by script, preserve page boundaries and table captions; otherwise experimental numbers and appendix details can be separated from their context.
- PDF text extraction often corrupts equations, subscripts, superscripts, symbols, and multi-column captions. Verify critical notation and captions against rendered pages; if verification is impossible, report the uncertainty instead of guessing.
- Prefer the original figure over a recreated diagram. When reconstruction is necessary, preserve semantic relationships and label it as a reconstruction.

## Optional Resource

For HTML exports of paper notes, `scripts/example.py` can extract readable Markdown-like text from `.html`, `.htm`, `.md`, or `.txt` files. Use it only as a helper when direct reading is noisy; do not use it as a substitute for reading the original paper when the paper itself is available.
