# Decision 002 - Pagination API Contract

**Date:** 2026-10-31
**Review by:** 2027-01-29
**Status:** Active

**Decision:** Media item search pagination will use optional `page` and
`size` query parameters while preserving the existing plain JSON array
response.

**Rationale:** The existing React pages expect the API response to be an array.
Changing immediately to a page-envelope response such as
`{ content, totalElements }` would break existing consumers unless all of
them were changed at the same time. Keeping the current response shape allows
pagination to be introduced incrementally while preserving backward
compatibility.

When both pagination parameters are omitted, the API should preserve the
existing full-list behavior.

**Alternatives rejected:** A page-envelope response was deferred because it
would require coordinated frontend changes. Client-side-only pagination was
rejected because the server would still retrieve the complete result set.

**Current state:** The DAO pagination work has started, but the controller/API
portion is still incomplete.

**Review trigger:** Revisit this decision if the frontend requires total-page
metadata or the API response contract is deliberately redesigned.
