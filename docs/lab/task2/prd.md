# Task 2 Product Requirements Document

## Workflow Name

MediaVault Backend Test Inventory Review

## Workflow Description

This workflow inspects the MediaVault backend test source tree and produces a report showing which Java test files exist.

## Trigger

A developer manually starts the backend test inventory workflow.

## Decision Events

1. If Java test files exist, list and count them.
2. If no test files exist, report that clearly.
3. Base the summary only on observed file names and paths.
4. Do not claim the tests were executed.
5. Do not modify source or test files.

## Ordered Actions

1. Inspect `backend/src/test`.
2. Find all `*Test.java` files.
3. Count them.
4. Record repository-relative paths.
5. Summarize represented backend areas.
6. Save the report.
7. Leave source and tests unchanged.

## Acceptance Criteria

1. `backend/src/test` is inspected.
2. Test-file count matches discovered files.
3. All discovered Java test paths are listed.
4. The report does not claim tests were executed.
5. Inventory is distinguished from runtime results.
6. Source and test files remain unchanged.

## Prompt

Inspect the MediaVault `backend/src/test` folder. Find all Java test files, count them, list their repository-relative paths, and summarize the backend areas represented by those tests. Do not execute or modify the tests. Save the report to `docs/lab/task2/backend-test-inventory.md`.
