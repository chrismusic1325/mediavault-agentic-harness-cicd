# MediaVault Pagination Orchestration Diagram

Human
  |
  v
Orchestrator
  |
  +--> Pagination Planner
  |      Input: pagination task + repo context
  |      Output: ordered plan + files + acceptance criteria
  |
  +--> Human approval
  |
  +--> Implementer
  |      Input: approved plan
  |      Output: modified files
  |
  +--> Pagination Reviewer
  |      Input: modified files + acceptance criteria
  |      Output: PASS or REVISE review
  |
  +--> Tester
  |      Input: reviewed implementation
  |      Output: PASS or FAIL test evidence
  |
  +--> Human final approval

## Routing Rules

- Incomplete plan -> return to Planner.
- Human rejects plan -> return to Planner.
- Reviewer returns REVISE -> return to Implementer.
- Tester returns FAIL -> return to Implementer.
- Same gate fails twice -> stop and escalate to the human.
- Human approval is required before implementation and before consequential final actions.
