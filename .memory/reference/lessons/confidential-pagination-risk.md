---
classification: confidential
project: proj-lessons
doc_type: risk
---

# Confidential Pagination Exposure Analysis

## What happened

A private design review considered the risk of future pagination changes
accidentally returning records outside the requesting user's authorized scope.

## What was learned

Pagination must never weaken authorization filtering. A technically correct
LIMIT/OFFSET implementation could still create a serious exposure if filtering
were applied after pagination or omitted from the query.

## Future application

Treat authorization filtering as a prerequisite to pagination and independently
verify tenant/user scoping before any broader pagination rollout.

This document is intentionally confidential for classification-ceiling testing.
