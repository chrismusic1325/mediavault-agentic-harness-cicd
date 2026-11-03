---
classification: internal
project: proj-lessons
doc_type: implementation
---

# Stable and Bounded SQL Pagination

## What happened

Pagination needed deterministic ordering and protection from excessively large
page sizes.

## What was learned

Use parameterized `LIMIT ? OFFSET ?`, cap requested page size with
`MAX_PAGE_SIZE = 100`, compute large offsets safely, and use `id` as a
secondary deterministic sort key when the primary sort field is not unique.

## Future application

Keep pagination values parameterized, preserve deterministic sorting, and test
the maximum-page-size behavior rather than relying only on controller logic.
