# Decision 003 - Pagination Validation Rules

**Date:** 2026-10-31
**Review by:** 2027-01-29
**Status:** Active

**Decision:** Pagination input validation belongs at the controller boundary.
`page` is zero-based, `page < 0` is invalid, `size < 1` is invalid, and
supplying only one of `page` or `size` should return HTTP 400.

**Rationale:** Invalid client input should be rejected before it reaches the
DAO. Requiring page and size together avoids silently interpreting an
incomplete pagination request as a full-list request. HTTP 400 matches the
existing controller pattern for invalid request parameters.

**Alternatives rejected:** Silently ignoring a lone `page` or `size`
parameter was rejected because the client could believe pagination occurred
when the server actually returned the full list. Supplying an automatic
default for the missing parameter was also rejected because no project-wide
default has been established.

**Current state:** DAO pagination support exists, but controller validation
and controller tests remain to be implemented.

**Review trigger:** Review this rule if the public API adopts documented
default pagination parameters or changes its validation contract.
