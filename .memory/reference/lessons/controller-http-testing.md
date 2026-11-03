---
classification: internal
project: proj-lessons
doc_type: testing
---

# Controller Tests Must Prove the HTTP Contract

## What happened

The pagination review found that checking only whether an exception occurred
could not prove whether invalid pagination produced HTTP 400 rather than
another error status.

## What was learned

Tests should verify externally observable behavior, not just that something
failed internally.

## Future application

Controller pagination tests should assert `BAD_REQUEST` for invalid parameters,
verify exact DAO arguments for valid requests, and prove the DAO is never
called when validation fails.
