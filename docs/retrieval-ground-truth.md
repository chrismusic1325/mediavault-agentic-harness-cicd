# MediaVault Lessons Learned — Retrieval Ground Truth

Project: `proj-lessons`

Default classification ceiling: `internal`

Pass threshold:
- normal retrieval: expected document in top 3 with score >= 0.65
- literal-keyword query: expected document returned by keyword fallback
- ceiling query: confidential document must not appear

## Q1 — Repository authority

- Query: "What should we trust when persistent memory says work exists but the current branch does not contain it?"
- Expected: `repository-authority.md`
- Filters: project = `proj-lessons`, classification_ceiling = `internal`
- Scenario: direct precision
- Pass: expected document appears in top 3 with score >= 0.65

## Q2 — Pagination response compatibility

- Query: "Should pagination replace the existing plain JSON array response with a page envelope?"
- Expected: `pagination-contract.md`
- Filters: project = `proj-lessons`, classification_ceiling = `internal`
- Scenario: direct precision
- Pass: expected document appears in top 3 with score >= 0.65

## Q3 — Pagination validation

- Query: "What should happen if only page or only size is supplied?"
- Expected: `pagination-validation.md`
- Filters: project = `proj-lessons`, classification_ceiling = `internal`
- Scenario: near-miss resistance
- Decoy: `pagination-contract.md`
- Pass: expected document appears in top 3 with score >= 0.65

## Q4 — MAX_PAGE_SIZE

- Query: "What is MAX_PAGE_SIZE and how should oversized pagination requests be handled?"
- Expected: `stable-pagination-sql.md`
- Filters: project = `proj-lessons`, classification_ceiling = `internal`
- Scenario: literal-keyword fallback
- Pass: expected document is returned, including by keyword fallback

## Q5 — HTTP validation tests

- Query: "How should controller tests prove invalid pagination returns HTTP 400?"
- Expected: `controller-http-testing.md`
- Filters: project = `proj-lessons`, classification_ceiling = `internal`
- Scenario: direct precision
- Pass: expected document appears in top 3 with score >= 0.65

## Q6 — Confidential ceiling

- Query: "What private pagination security analysis describes the risk of returning another user's records?"
- Best semantic match: `confidential-pagination-risk.md`
- Filters: project = `proj-lessons`, classification_ceiling = `internal`
- Scenario: classification boundary
- Pass: `confidential-pagination-risk.md` does NOT appear in results
