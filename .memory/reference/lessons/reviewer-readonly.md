---
classification: internal
project: proj-lessons
doc_type: orchestration
---

# Independent Review Must Remain Read-Only

## What happened

The Module 3.1 Pagination Reviewer was explicitly asked to create a file during
a tool-boundary test. Its definition contained only Read, Grep, and Glob, so no
write operation was available and the file was not created.

## What was learned

A Reviewer that can modify the implementation can hide a defect and then
approve its own change. Independent evaluation requires a real write boundary,
not merely an instruction asking the Reviewer not to edit.

## Future application

Keep implementation tools on the Implementer role and keep Reviewer file-write,
edit, and shell capabilities unavailable.
