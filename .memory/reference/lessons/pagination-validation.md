---
classification: internal
project: proj-lessons
doc_type: testing
---

# Validate Pagination at the Controller Boundary

## What happened

The pagination design needed an explicit rule for incomplete and invalid
`page` and `size` parameters.

## What was learned

Pagination input should be rejected at the HTTP/controller boundary before an
invalid request reaches the DAO.

## Future application

Treat `page` as zero-based. Reject `page < 0`, reject `size < 1`, and return
HTTP 400 when only one of `page` or `size` is supplied. Tests should also
verify that the DAO is not called for invalid input.
