# Paper Deep Reading Reference Templates

This reference distills the reusable reading structure inferred from the user's narrative-agent paper notes and generalizes it across domains.

## Core Note Pattern

Use this as the minimal high-signal structure:

1. 一句话
2. Motivation
3. 系统/方法架构
4. 核心创新点
5. 实验设计及结论
6. 局限性

The pattern works because it separates: problem pressure, proposed mechanism, novelty, evidence, and critique.

## One-Sentence Formula

Prefer one of these formulas:

- `<Paper> proposes <method/framework/dataset> that <key mechanism>, enabling/improving <target capability> under <setting>`.
- `<Paper> reframes <old problem> from <old paradigm> into <new paradigm>, using <mechanism> to address <failure mode>`.
- `<Paper> shows that <claim> by evaluating <method> on <task/data> against <baselines>, with strongest evidence in <result>`.

## Innovation Card

For each innovation, write:

```markdown
### Innovation N: <name>
- What: ...
- How: ...
- Why it matters: ...
- Evidence: ...
- Trade-off / hidden cost: ...
```

## Experiment Audit Checklist

- What is the task?
- What are the datasets and how were they created?
- Are baselines strong and current?
- Are metrics aligned with the claim?
- Are human evaluations reliable? Note annotator count, scale, agreement, and protocol.
- Are ablations isolating the claimed contribution?
- Are qualitative cases cherry-picked or systematic?
- Are cost, latency, compute, and data requirements reported?
- What does the evidence prove, and what does it not prove?

## Limitation Prompts

Ask these even if the paper has a limitations section:

- Scope: where does the method fail outside the tested domain?
- Dependency: what assumptions, tools, data, or models does it rely on?
- Scaling: what happens when sequence length, users, agents, modalities, or data size grow?
- Evaluation: could the metric reward the wrong behavior?
- Robustness: what adversarial, noisy, or distribution-shifted cases break it?
- Reproducibility: can another team reproduce the result from the paper alone?
- Productization: what blocks deployment—latency, UX, safety, cost, privacy, maintainability?

## Research-Idea Extraction

Convert limitations into opportunities:

| Limitation | Why it matters | Possible experiment | Expected contribution |
|---|---|---|---|
|  |  |  |  |

## Domain-Specific Evidence Questions

### Agent / Multi-Agent Systems

- What are the agent roles and communication channels?
- Is orchestration fixed, learned, emergent, or user-controllable?
- What is stored in memory/state, and how is it updated?
- How are conflicts, errors, deadlocks, and hallucinations handled?
- Does evaluation measure agentic behavior or only final text quality?

### Narrative / Creative Generation

- Does the method separate planning, world state, character state, and final narration?
- How are long-horizon consistency, character agency, conflict, pacing, and style measured?
- Does the system preserve controllability while allowing emergence?
- Are human preferences, pairwise comparisons, or LLM judges validated?

### General ML Methods

- What inductive bias or optimization change is introduced?
- Is improvement due to method, data, scale, prompting, or evaluation setup?
- Are ablations sufficient to isolate the mechanism?
- Are comparisons fair under compute and parameter budgets?

### Benchmarks / Datasets

- What capability is the benchmark supposed to measure?
- What is the data collection and filtering pipeline?
- What leakage or annotation artifacts may exist?
- Does the benchmark have enough diversity and difficulty headroom?

### Systems Papers

- What is the architecture and runtime path?
- What are throughput, latency, reliability, and failure recovery mechanisms?
- What workloads are evaluated, and are they representative?
- What engineering trade-offs are hidden by the abstraction?
