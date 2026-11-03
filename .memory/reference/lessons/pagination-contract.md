---
classification: internal
project: proj-lessons
doc_type: decision
---

# Preserve the Plain-Array Pagination Contract

## What happened

MediaVault needed server-side pagination, but existing consumers expected a
plain JSON array response.

## What was learned

Pagination can be introduced incrementally with optional `page` and `size`
parameters without immediately replacing the response with a page envelope.

## Future application

When controller pagination is implemented, preserve full-list behavior when
both parameters are omitted and keep the existing plain-array response until a
deliberate API-contract revision is approved.
