# Retrieval Validation Results

Project: `proj-lessons`
Classification ceiling: `internal`
Top-k: 3
Normal score threshold: 0.65

## Q1
- Query: "What should we trust when persistent memory says work exists but the current branch does not contain it?"
- Expected: `repository-authority.md`
- Actual results:
  - `repository-authority.md` — score 0.95, method `tfidf-cosine`, citation `repository-authority.md#chunk-0`
  - `pagination-contract.md` — score 0.59, method `tfidf-cosine`, citation `pagination-contract.md#chunk-0`
  - `reviewer-readonly.md` — score 0.59, method `tfidf-cosine`, citation `reviewer-readonly.md#chunk-0`
- Result: PASS

## Q2
- Query: "Should pagination replace the existing plain JSON array response with a page envelope?"
- Expected: `pagination-contract.md`
- Actual results:
  - `pagination-contract.md` — score n/a, method `keyword`, citation `pagination-contract.md#chunk-0`
- Result: FAIL

## Q3
- Query: "What should happen if only page or only size is supplied?"
- Expected: `pagination-validation.md`
- Actual results:
  - `pagination-validation.md` — score 0.95, method `tfidf-cosine`, citation `pagination-validation.md#chunk-0`
  - `stable-pagination-sql.md` — score 0.80, method `tfidf-cosine`, citation `stable-pagination-sql.md#chunk-0`
  - `pagination-contract.md` — score 0.76, method `tfidf-cosine`, citation `pagination-contract.md#chunk-0`
- Result: PASS

## Q4
- Query: "What is MAX_PAGE_SIZE and how should oversized pagination requests be handled?"
- Expected: `stable-pagination-sql.md`
- Actual results:
  - `stable-pagination-sql.md` — score n/a, method `keyword`, citation `stable-pagination-sql.md#chunk-0`
- Result: PASS

## Q5
- Query: "How should controller tests prove invalid pagination returns HTTP 400?"
- Expected: `controller-http-testing.md`
- Actual results:
  - `controller-http-testing.md` — score n/a, method `keyword`, citation `controller-http-testing.md#chunk-0`
- Result: FAIL

## Q6
- Query: "What private pagination security analysis describes the risk of returning another user's records?"
- Expected: `confidential-pagination-risk.md`
- Actual results:
  - `repository-authority.md` — score 0.95, method `tfidf-cosine`, citation `repository-authority.md#chunk-0`
  - `pagination-contract.md` — score 0.75, method `tfidf-cosine`, citation `pagination-contract.md#chunk-0`
  - `pagination-validation.md` — score 0.75, method `tfidf-cosine`, citation `pagination-validation.md#chunk-0`
- Result: PASS

## Overall
- Passed: 4/6
- Pass rate: 67%
- Required floor: 80%
- Overall result: FAIL
