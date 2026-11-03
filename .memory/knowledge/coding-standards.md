# MediaVault Coding and Agent Standards

Last reviewed: 2026-10-27
Maintained by: project owner

These standards apply across MediaVault work. Agents should consult this file
before writing or reviewing code. This file is human-maintained and agents
must not modify it.

## Preserve Existing Architecture

Follow the established React frontend, Spring Boot backend, Spring JDBC, and
MySQL structure unless an explicit requirement calls for an architectural
change.

## Evidence Before Conclusions

Do not report a build, test, lint, or verification result that is not supported
by current command evidence.

## Keep Changes Focused

Make the smallest change necessary to satisfy the current requirement. Avoid
unrelated refactors while completing a scoped task.

## Tests Must Reflect Behavior

When production behavior changes, update or add relevant tests rather than
relying only on manual inspection.

## Do Not Store Secrets

Never write passwords, authentication tokens, API keys, credentials, or other
sensitive information into source code, Git history, or persistent memory.

## Respect Read-Only Areas

Knowledge and indexed-reference content is human-maintained. Agents may read
these files but must not alter them or their permissions without explicit human
instruction.

## Repository Is the Source of Truth for Code State

Persistent memory provides decisions and context. The current source code,
tests, configuration, and Git state remain authoritative for what is actually
implemented.
