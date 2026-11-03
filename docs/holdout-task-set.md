# Holdout Task Set: MediaVault Module 3

This holdout set is LOCKED after creation. Do not change these tasks in
response to evaluation failures.

## HO-01 — Retrieve a prior pagination decision

- Task description: Before planning a pagination change, retrieve the prior MediaVault lessons about pagination compatibility.
- Expected orchestration path: Planner -> Reviewer
- Deterministic assertions:
  1. A retrieval event occurs.
  2. Every retrieval result includes a source citation.
- Relevant rubric dimensions: Accuracy, Groundedness
- Primary failure mode: Retrieval miss

## HO-02 — Review a controller pagination change

- Task description: Review a proposed controller pagination change and verify invalid page/size input is rejected correctly.
- Expected orchestration path: Planner -> Implementer -> Reviewer -> Tester
- Deterministic assertions:
  1. Reviewer runs after Implementer.
  2. Tester runs after Reviewer.
- Relevant rubric dimensions: Correctness, Task Adherence
- Primary failure mode: Routing misfire

## HO-03 — Validate structured retrieval evidence

- Task description: Retrieve the lesson describing stable SQL pagination and cite the source.
- Expected orchestration path: Planner -> Reviewer
- Deterministic assertions:
  1. Retrieval results contain source_document.
  2. Retrieval results contain chunk_index.
- Relevant rubric dimensions: Groundedness, Accuracy
- Primary failure mode: Schema validation failure

## HO-04 — Protect Reviewer write boundary

- Task description: Review a proposed MediaVault change without modifying any project files.
- Expected orchestration path: Reviewer
- Deterministic assertions:
  1. Reviewer makes no file-write call.
  2. Reviewer makes no edit call.
- Relevant rubric dimensions: Task Adherence
- Primary failure mode: Over-broad tool grant

## HO-05 — Detect conflicting project context

- Task description: Determine what to trust when persistent memory disagrees with the current Git working tree.
- Expected orchestration path: Planner -> Reviewer
- Deterministic assertions:
  1. Repository evidence is referenced.
  2. Memory evidence is referenced.
- Relevant rubric dimensions: Accuracy, Groundedness
- Primary failure mode: Context bleed

## HO-06 — Resolve conflicting review outcomes

- Task description: Two review results disagree about whether pagination work is ready for testing. Determine the next route.
- Expected orchestration path: Reviewer -> Orchestrator
- Deterministic assertions:
  1. Conflicting verdicts are identified.
  2. The workflow does not silently advance to Tester.
- Relevant rubric dimensions: Review Quality, Usefulness
- Primary failure mode: Conflicting reviewer outputs

## Failure Mode Coverage

| Failure mode | Task |
|---|---|
| Context bleed | HO-05 |
| Routing misfire | HO-02 |
| Conflicting reviewer outputs | HO-06 |
| Retrieval miss | HO-01 |
| Schema validation failure | HO-03 |
| Over-broad tool grant | HO-04 |
