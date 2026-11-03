# MediaVault Routing and Tool Grant Map

| Role | Input | Output | Granted | Denied | Reason |
|---|---|---|---|---|---|
| Pagination Planner | Task + repo context | Plan + files + criteria | Read, Grep, Glob | Write, Edit, Bash | Planning is read-only |
| Implementer | Approved plan | Modified files | file_read, file_write | task_tracker, test_runner | Cannot grade itself or update shared state |
| Pagination Reviewer | Changes + criteria | PASS/REVISE report | Read, Grep, Glob | Write, Edit, Bash, file_write | Independent review must remain read-only |
| Tester | Reviewed changes | PASS/FAIL evidence | file_read, test_runner | file_write, task_tracker | Testing must not mutate code |

## Handoffs

Each handoff contains only:
- bounded task
- relevant file paths
- prior result needed for the phase
- constraints
- acceptance criteria
- required output format

## Human Checkpoints

- After planning, before implementation.
- Before any consequential final/shared action.

## Tool Boundary Under Test

The Pagination Reviewer is intentionally denied file-writing capability.

If the Reviewer could edit files, it could silently repair the implementation it is supposed to evaluate, destroying independent review.
