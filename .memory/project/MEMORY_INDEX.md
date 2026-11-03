# Project Memory Index

Last updated: 2026-11-03

## Active entries

- `decisions/decision-001.md` — Defines MediaVault's evidence-based frontend
  verification rule: stages that do not execute must be reported as NOT RUN
  rather than inferred as PASS or FAIL. Recorded 2026-10-27. Review by 2027-01-25.

- `../knowledge/coding-standards.md` — Stable MediaVault coding and agent
  standards covering architecture, evidence, focused changes, testing,
  sensitive information, read-only knowledge, and repository authority.
  Human-maintained and read-only. Last reviewed 2026-10-27.


- `decisions/decision-002.md` — Defines the backward-compatible API contract
  for MediaVault media-item pagination: optional page/size parameters while
  retaining the existing plain-array response. Recorded 2026-10-31.
  Review by 2027-01-29.

- `decisions/decision-003.md` — Defines pagination request validation:
  zero-based pages, invalid values return HTTP 400, and page/size must be
  supplied together. Recorded 2026-10-31. Review by 2027-01-29.

- `decisions/decision-004.md` — Defines the SQL pagination strategy:
  parameterized LIMIT/OFFSET, maximum page size 100, and deterministic id
  tie-breaking. Recorded 2026-10-31. Review by 2027-01-29.


- `status/pagination-continuation.md` — Current pagination continuation state,
  next implementation boundary, and explicitly deferred work. Recorded
  2026-11-03. Review by 2027-02-01.

- `questions/pagination-open-questions.md` — Unresolved pagination design
  questions that should remain deferred until the current controller work is
  complete. Recorded 2026-11-03. Review by 2027-02-01.

## Archived entries

(none yet)

## Pruning schedule

- Workflow-scoped entries: review when the workflow or feature completes.
- Project-scoped entries: review every 90 days.
- Superseded entries: archive when a newer authoritative entry replaces them.
