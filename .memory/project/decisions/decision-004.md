# Decision 004 - Stable SQL Pagination

**Date:** 2026-10-31
**Review by:** 2027-01-29
**Status:** Active

**Decision:** Media item pagination will use parameterized SQL
`LIMIT ? OFFSET ?`, cap the requested page size at 100, and add `id` as a
deterministic secondary sort key.

**Rationale:** Binding LIMIT and OFFSET values keeps pagination values out of
the SQL string and follows the existing parameterized-query approach.
Capping page size at 100 prevents unexpectedly large paginated result sets.
Adding `id` as a secondary sort produces deterministic ordering when
multiple records have the same primary sort value, reducing the risk of items
moving between pages.

**Alternatives rejected:** Unbounded page sizes were rejected because a
client could request excessively large result sets. Sorting only by a
non-unique field was rejected because ties can produce unstable page
boundaries.

**Current state:** The DAO implementation and DAO tests contain this behavior.
The controller still needs to expose pagination parameters before the feature
is reachable through the HTTP API.

**Review trigger:** Review this decision if the database technology, paging
strategy, maximum page-size requirement, or sorting model changes.
