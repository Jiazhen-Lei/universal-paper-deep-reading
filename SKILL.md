---
name: universal-paper-deep-reading
description: This skill should be used when the user provides an academic paper, arXiv URL or ID, local PDF/HTML/Markdown manuscript, paper notes, or asks for 精读, deep reading, novelty analysis, experiment audit, limitation critique, SOTA positioning, or structured reusable notes for a research paper in any domain.
agent_created: true
---

# Universal Paper Deep Reading

## Overview

Perform rigorous, evidence-grounded deep reading of academic papers across domains. Convert a paper into structured research notes that capture the paper's one-sentence thesis, motivation, method or system architecture, core innovations, experimental evidence, limitations, and relevance to the user's work.

This skill generalizes the user's preferred note pattern: `一句话 → Motivation → 系统/方法架构 → 核心创新点 → 实验设计及结论 → 局限性`, then adds cross-domain checks for claims, assumptions, evidence quality, reproducibility, and future research value.

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
- Treat experiments as evidence, not decoration. Extract datasets, baselines, metrics, ablations, costs, and failure cases.
- Preserve uncertainty. Mark missing details, weak evidence, ambiguous claims, or unsupported causal conclusions.
- Produce notes in Chinese by default unless the user requests another language. Keep technical terms in English where precision matters.
- Be domain-adaptive: map the same reading skeleton to ML, systems, HCI, theory, security, science, medicine, social science, and survey papers.

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

## Multi-Pass Reading Procedure

### Pass 1: Map the Paper

Scan title, abstract, introduction, figures, method overview, experiment tables, limitations, and conclusion. Produce a short reading map:

- Research question: what problem is being solved?
- Claimed contribution: what is new according to the authors?
- Method shape: model, framework, algorithm, dataset, evaluation, or theory?
- Evidence shape: what experiments or arguments support the claim?
- Immediate concern: what may be weak, missing, or overclaimed?

### Pass 2: Reconstruct the Core Argument

Fill the user's preferred six-part note skeleton:

1. `一句话`: State the paper's essence in one dense sentence: `This paper does X by doing Y, to improve/enable Z under condition W`.
2. `Motivation`: List the concrete pain points, failure modes, gaps in prior work, and why existing methods are insufficient.
3. `系统/方法架构`: Explain the pipeline, modules, data flow, objective function, decision process, or theoretical structure. For systems, identify components and runtime workflow; for ML methods, identify inputs, outputs, training/inference, and losses; for empirical papers, identify study design and variables.
4. `核心创新点`: Extract 3-6 innovations. For each one, include `what`, `how`, `why it matters`, and `what trade-off it introduces`.
5. `实验设计及结论`: Extract datasets, baselines, metrics, protocol, main results, ablations, human evaluation, statistical tests, efficiency/cost, and what each result actually proves.
6. `局限性`: Combine stated limitations and independent critique: assumptions, scope, scalability, evaluation validity, reproducibility, hidden costs, ethical/safety concerns, and deployment risks.

### Pass 3: Audit the Evidence

Evaluate the paper's support for its claims:

- Dataset/task fit: whether the benchmark actually measures the intended capability.
- Baseline strength: whether baselines are current, well-tuned, and fairly compared.
- Metrics validity: whether metrics match human or domain-relevant quality.
- Ablation logic: whether each component is isolated and necessary.
- Generalization: whether results cover enough domains, languages, scales, or settings.
- Cost and practicality: runtime, training cost, annotation cost, data requirements, latency, memory, or deployment complexity.
- Reproducibility: code/data availability, hyperparameters, prompts, seeds, statistical uncertainty.

### Pass 4: Position the Paper

Place the work in context:

- Compare against prior work using a table when helpful: `Prior work → limitation → this paper's response → remaining gap`.
- Identify the paper's real novelty level: `incremental engineering`, `new framing`, `new mechanism`, `new dataset/benchmark`, `strong empirical result`, or `conceptual shift`.
- Note whether the novelty is in problem formulation, architecture, data, training, inference, evaluation, system integration, or application scenario.

### Pass 5: Extract Value for the User

End with actionable synthesis:

- `对我有什么用`: map insights to the user's project, research direction, implementation, evaluation, or writing.
- `可复用机制`: list reusable design patterns, prompts, modules, algorithms, metrics, or experimental protocols.
- `可追问问题`: identify 3-8 follow-up questions that would deepen understanding.
- `潜在研究机会`: list gaps that could become new experiments, papers, or engineering tasks.

## Domain Adaptation Guide

Use the same skeleton, but adapt the method/evidence questions:

- `ML/AI method paper`: architecture, training data, loss/objective, inference pipeline, ablations, compute, model scale, benchmark leakage risk.
- `Agent/system paper`: agents/roles, memory/state, orchestration, tool use, feedback loops, failure recovery, latency, controllability, evaluation of emergent behavior.
- `Dataset/benchmark paper`: data source, annotation protocol, quality control, task definition, leakage, coverage, metric reliability, benchmark saturation risk.
- `Theory paper`: definitions, assumptions, theorem statements, proof strategy, implications, counterexamples, relation to known results.
- `HCI/empirical study`: participant sampling, study design, variables, qualitative coding, statistical power, ecological validity.
- `Survey paper`: taxonomy, inclusion criteria, coverage, organizing axes, missing literature, actionable synthesis.
- `Applied science/medicine/social science`: hypothesis, intervention/exposure, controls, confounders, measurement validity, statistical robustness, external validity.

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

## 3. 方法 / 系统架构
...

## 4. 核心创新点
| 创新点 | 做了什么 | 为什么重要 | 代价/风险 |
|---|---|---|---|

## 5. 实验设计及结论
### 5.1 Datasets / Tasks
### 5.2 Baselines
### 5.3 Metrics
### 5.4 Main Results
### 5.5 Ablations / Analysis
### 5.6 Evidence Audit

## 6. 局限性与批判
### 作者承认的局限
### 独立判断的局限
### 最可能失败的场景

## 7. 与相关工作的关系
| 方向/工作 | 解决什么 | 本文差异 | 剩余问题 |
|---|---|---|---|

## 8. 对我的启发
- 可复用机制：
- 可借鉴实验：
- 可转化为项目/论文的想法：
- 下一步建议阅读：

## 9. 追问清单
1. ...
```

## Quality Gates Before Finalizing

Before answering, verify:

- The note contains enough paper-specific details that it could not apply to any random paper.
- Important numbers from experiments are preserved when available.
- Figures/tables are interpreted, not merely mentioned.
- Limitations include independent critique, not only author-provided statements.
- The final synthesis clearly distinguishes fact, interpretation, and speculation.
- If the source was incomplete, explicitly state what was unavailable and avoid pretending full coverage.

## Optional Resource

For HTML exports of paper notes, `scripts/example.py` can extract readable Markdown-like text from `.html`, `.htm`, `.md`, or `.txt` files. Use it only as a helper when direct reading is noisy; do not use it as a substitute for reading the original paper when the paper itself is available.
