# Module 3.2 — Lessons Learned Knowledge Workflow Final Report

## Scope

Project identifier: `proj-lessons`

The workflow separates two kinds of durable knowledge:

1. a curated, versioned reference corpus containing reviewed lessons from
   MediaVault work; and
2. persistent run-time storage for a new lesson discovered during workflow
   execution.

## Reference Corpus

Seven classified lessons were created from real MediaVault work:

- repository authority when memory and Git disagree;
- preservation of the plain-array pagination contract;
- controller-boundary pagination validation;
- stable and bounded SQL pagination;
- read-only independent review;
- HTTP-level controller testing;
- a confidential pagination exposure analysis.

Every corpus document has project and classification metadata.

## Ground-Truth Evaluation

Six queries were fixed before evaluation.

The set includes:

- direct precision;
- near-miss resistance;
- literal-keyword retrieval;
- classification-ceiling enforcement.

Final pass rate: 100%

The course floor is 80%.

See `docs/retrieval-validation-results.md` for returned documents, scores or
retrieval methods, citations, and PASS/FAIL results.

## Citation Verification

Every returned retrieval result identifies its source as:

`<source-document>#chunk-0`

This makes retrieved knowledge traceable to the curated corpus.

## Classification Boundary

The confidential lesson
`confidential-pagination-risk.md` is a deliberately attractive match for the
security query.

When retrieval was performed with an `internal` ceiling, the confidential
document was filtered before results were returned.

Evidence:
`docs/module3/retrieval-ceiling-evidence.txt`

## Persistent Storage

The Implementer-equivalent workflow stored a new internal lesson through the
structured storage operation.

The lesson was subsequently read in a completely new Python process, proving
that the entry persisted outside process/conversation state.

Evidence:
`docs/module3/storage-persistence-evidence.txt`

## Auditability

The storage write appended an audit entry containing:

- timestamp;
- operation;
- project ID;
- entry ID;
- classification;
- calling role.

Evidence:
`docs/module3/storage-audit-evidence.txt`

## Storage Classification Enforcement

A deliberate confidential write was rejected by the storage boundary.

Evidence:
`docs/module3/storage-classification-evidence.txt`

## Role Access

The Planner retrieves prior lessons before planning.

The Implementer owns the narrow storage-write responsibility.

The Reviewer retrieves relevant lessons while remaining unable to write
persistent knowledge.

Roles that do not need knowledge access receive none.

## Conclusion

The workflow demonstrates curated retrieval, citations, ground-truth
evaluation, persistent storage, audit logging, project scoping, role-specific
access, and classification-ceiling enforcement.

The reference corpus is treated as reviewed, versioned input. New discoveries
created during a run enter persistent storage through a bounded operation
instead of being silently added to the curated corpus.
