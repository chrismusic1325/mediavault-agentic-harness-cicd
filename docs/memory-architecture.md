# Memory Architecture

## What this workflow needs to remember

The MediaVault agentic workflow supports development and verification work
across multiple Claude Code sessions. A fresh session needs to retain important
project decisions, current limitations, active priorities, and stable project
constraints that cannot be recovered reliably from source code alone. It does
not need to duplicate information already represented by source code, tests,
package configuration, or Git history. Temporary terminal output and one-time
errors should remain session-only. Credentials, authentication information,
personal data, and other secrets must never be stored in persistent memory.

## Layer 1: Project memory directory

Path: `.memory/project/`

### Belongs here

- The decision that frontend verification stages must only be labeled PASS or
  FAIL when they actually execute.
- The rule that blocked verification stages are reported as NOT RUN.
- Current limitations that affect how a future session should interpret
  verification evidence.
- Current project priorities or unresolved implementation decisions.
- Deferred work that a future session needs in order to resume accurately.

### Does not belong here

- Full terminal transcripts, because they are temporary evidence rather than
  durable project state.
- Credentials or authentication data, because secrets must never be stored in
  project memory.
- Step-by-step test procedures, because recurring procedures belong in skills
  or existing project scripts.

### Scope

Project-scoped to the MediaVault repository.

### Write permissions

The agent may add or update project-memory entries when a significant project
decision or state change needs to survive future sessions. It must first check
the memory index and update an existing topic instead of creating duplicates.

### Pruning policy

Feature- or workflow-specific entries are reviewed when the related work is
completed. Project-wide entries are reviewed every 90 days. Superseded
decisions are archived or replaced when a newer decision becomes authoritative.

## Layer 2: Knowledge files

Path: `.memory/knowledge/`

### Belongs here

- Stable coding standards for MediaVault.
- The rule that verification conclusions must be supported by current evidence.
- The rule that agents must preserve existing project architecture unless a
  change is explicitly requested.
- The rule that secrets must not be committed or written to memory.
- Stable expectations about testing and scope.

### Does not belong here

- Current feature status, because that changes and belongs in Project Memory.
- Temporary error messages, because those belong in the current session.
- Agent-generated decisions that have not been reviewed by a human.

### Scope

Project-scoped to MediaVault.

### Write permissions

Human-maintained and read-only for the agent. The agent may consult these files
but must not modify them or change their permissions without explicit human
instruction.

### Pruning policy

Reviewed when project standards change and at least every 90 days. Obsolete
standards are replaced by a human rather than silently changed by the agent.

## Layer 3: Indexed reference documents

Path: `.memory/reference/`

### Belongs here

Large or infrequently needed background documents such as future architecture
documents, historical design discussions, or other materials that would be
wasteful to load during every session.

### Does not belong here

- Current project decisions that need to be visible through Project Memory.
- Coding standards that should guide routine work.
- Source code or tests already available directly in the repository.

### Scope

Project-scoped to MediaVault.

### Write permissions

Human-maintained and read-only for the agent.

### Pruning policy

Review a reference when its source document is replaced or becomes obsolete.
Remove references whose source material is no longer authoritative.

The reference layer is currently intentionally empty except for its index.
MediaVault does not yet have a large reference document that provides enough
value to justify indexed retrieval. Larger architecture or historical design
documents would justify populating this layer later.

## Allocation decision table

| Information | Location | Reason |
| --- | --- | --- |
| Verification evidence rule | Project Memory | A project decision that affects future sessions |
| Coding standards | Knowledge | Stable, human-maintained rules |
| Large future design documents | Indexed Reference | Retrieve only when relevant |
| How to run npm verification | Skill/existing scripts | Procedure, not memory |
| Source and tests | Repository | Already authoritative |
| Temporary command errors | Current session | Short-lived information |
| Credentials/secrets | Nowhere in memory | Sensitive information |

## Alternatives considered

I considered placing the frontend verification reporting rule in the Knowledge
layer because it behaves like a standard. I chose Project Memory because the
rule was learned from an actual project iteration and may be refined as the
verification workflow evolves. Stable coding and security rules remain in the
human-controlled Knowledge layer.
