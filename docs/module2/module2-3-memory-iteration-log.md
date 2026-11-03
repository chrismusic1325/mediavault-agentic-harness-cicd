# Module 2.3 Persistent Memory Iteration Log

## Target Codebase

MediaVault

## Memory-System Commit

`a78c7fe`

## Workflow

Frontend verification continuity across fresh Claude Code sessions.

## Continuity Problem

A fresh session can inspect source files and package configuration, but it
cannot reliably reconstruct why the project adopted the rule that verification
stages must only be labeled PASS or FAIL when they actually execute. It also
cannot safely infer temporary permission limitations from an earlier
conversation.

## Persistent Memory State

The system contains:

- a project scope declaration;
- a memory index;
- Decision 001 recording the evidence-based verification rule;
- a human-maintained Knowledge File containing stable MediaVault standards;
- an indexed-reference layer that is intentionally empty except for its index;
- CLAUDE.md instructions governing startup loading, writes, stale entries,
  scope, and repository authority.

## Verification Run 1 - Startup Memory Check

**Session type:** Fresh Claude Code session with no pasted memory.

**Command exit code:** 0

### Evidence

See:
`docs/module2/2.3-evidence/startup-memory-check.txt`

### Acceptance Criteria

The session should:

1. identify Decision 001;
2. summarize the evidence-based verification rule;
3. identify the coding standards Knowledge File;
4. state actual standards from the file;
5. distinguish writable Project Memory from read-only Knowledge and Reference
   content.

## Verification Run 2 - Task Resumption Check

**Session type:** Fresh Claude Code session with no pasted memory.

**Command exit code:** 0

### Evidence

See:
`docs/module2/2.3-evidence/task-resumption-check.txt`

### Acceptance Criteria

The session should:

1. identify the current verification rule;
2. preserve the read-only verification role;
3. use repository state as authoritative for implementation;
4. avoid inferring results from an earlier run;
5. recommend a next action consistent with current evidence.

## Memory Allocation Review

- Changing verification decisions belong in Project Memory.
- Stable coding and agent constraints belong in Knowledge.
- Large background documents belong in Indexed References when needed.
- Procedures remain in scripts or skills rather than memory.
- Temporary command output remains session-only.
- Secrets are excluded from all memory layers.

## Permission Policy

The Knowledge File is marked read-only and CLAUDE.md explicitly prohibits the
agent from modifying Knowledge or changing its permissions without human
instruction.

## Compaction or Transcript Reuse

None. The verification sessions were started independently with `claude -p`
and did not use `--continue` or `--resume`.

## Result

The submitted evidence files contain the actual fresh-session responses. They
are the source of truth for evaluating whether the startup-memory and
task-resumption checks passed.
