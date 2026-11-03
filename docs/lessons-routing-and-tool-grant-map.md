# Lessons Learned Routing and Tool Grant Map

| Role | Retrieval | Storage | Ceiling | Reason |
|---|---|---|---|---|
| Lessons Planner | retrieve | none | internal | Needs prior lessons before deciding how work should proceed |
| Lessons Implementer | none | write_entry | internal | Records one new lesson discovered during approved implementation |
| Lessons Reviewer | retrieve | none | internal | Uses prior standards and lessons while independently evaluating work |
| Tester | none | none | internal | Current test responsibility does not require knowledge mutation |
| Project Manager | none | none | public | Ticket/status responsibility does not require project knowledge access |

## Enforcement

Retrieval filters by both `project = proj-lessons` and the role's
classification ceiling before results are returned.

The Implementer writes through the named `write_entry` operation rather than
directly modifying the persistent data file.

Confidential and secret storage writes are rejected by the storage boundary.

The Planner and Reviewer have no persistent-storage write operation.

## Direct-access rule

Agents must not bypass the controlled interfaces by directly editing
`.memory/lessons-storage.json`, `.memory/lessons-storage-audit.log`, or the
reference corpus during a workflow run.
