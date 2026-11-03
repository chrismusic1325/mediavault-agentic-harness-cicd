---
classification: internal
project: proj-lessons
doc_type: lesson
---

# Repository State Is the Implementation Authority

## What happened

During pagination planning, persistent memory described DAO pagination support
as already implemented, but the current `main` branch did not contain the
pagination overload, `MAX_PAGE_SIZE`, or parameterized LIMIT/OFFSET behavior.

## What was learned

Persistent memory records intent and continuity, but current source code,
tests, configuration, and Git state determine what is actually implemented.

## Future application

Before planning from a status-oriented memory entry, compare its claim with the
current repository. When they disagree, report the disagreement rather than
silently assuming either source is correct.
