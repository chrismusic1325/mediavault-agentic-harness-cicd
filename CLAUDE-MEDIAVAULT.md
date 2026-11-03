# Agent Instructions

# Persistent Memory Configuration

At the start of every session:

1. Read `.memory/SCOPE.md`.
2. Confirm the scope identifies this repository as MediaVault.
3. If the scope does not match, stop and report the mismatch.
4. Read `.memory/project/MEMORY_INDEX.md`.
5. Read active project-memory entries relevant to the current task.
6. Consult `.memory/knowledge/` before making decisions involving coding
   standards or architectural constraints.
7. Consult `.memory/reference/REFERENCE_INDEX.md` only when background
   reference material is relevant.

## Memory Layers

- `.memory/project/` contains changing project state and decisions. You may
  update this layer when a significant project decision or state change must
  survive future sessions.

- `.memory/knowledge/` contains stable human-maintained rules. It is read-only
  to the agent. Never modify it or change its permissions without explicit
  human instruction.

- `.memory/reference/` contains indexed background material. It is read-only
  to the agent and should be consulted selectively.

## Write Policy

Before creating a new project-memory entry, check
`.memory/project/MEMORY_INDEX.md` for an existing entry on the same topic.
Update or supersede an existing entry rather than creating duplicates.

Never write credentials, authentication information, private personal data, or
other secrets into any memory layer.

Never modify file permissions in `.memory/knowledge/` or `.memory/reference/`
without explicit human instruction.

## Stale Memory Policy

Before acting on any entry in `.memory/project/`, check its `Review by` date.

If the review date has passed:

1. Treat the entry as untrusted.
2. Do not use it to make a recommendation, implementation decision, or project change.
3. State the filename and expired review date clearly.
4. Ask the human to confirm whether the entry is still current.
5. Wait for confirmation before treating the entry as authoritative.
6. Use current source code, tests, configuration, and Git history only to explain any conflict; do not silently choose the expired memory over current repository evidence.

This applies to every Project Memory entry.
## Repository Authority

Memory supplies context and decisions. Current source code, tests,
configuration, and Git state remain the source of truth for implementation
state.

## Module 3.1 Orchestrated Workflow

For MediaVault pagination work:

1. Invoke `pagination-planner` first.
2. Check that it returns scope, ordered steps, exact files, acceptance criteria, and open questions.
3. Require human approval before implementation.
4. After changes exist, invoke `pagination-reviewer`.
5. If Reviewer returns REVISE, route back to Implementer.
6. If Reviewer returns PASS, route to Tester.
7. Test failure routes back to Implementer.
8. If the same gate fails twice, stop and escalate to the human.

Pass only bounded task context, relevant paths, prior required output, constraints, acceptance criteria, and the required response format.

The Reviewer must remain read-only.
