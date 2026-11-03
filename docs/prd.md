# Product Requirements Document

## Workflow Name

MediaVault Frontend Verification Review

## Workflow Description

This workflow runs MediaVault's existing frontend verification command and
produces a concise report describing whether the build, automated tests, and
lint checks passed or failed.

## Trigger

A developer manually starts the workflow from the MediaVault repository and
asks for the frontend verification results to be reviewed.

## Decision Events

1. If `npm run verify` succeeds, report that frontend verification passed.
2. If it fails, identify the stage that caused the failure.
3. If warnings occur without causing failure, report them separately.
4. If a later stage does not execute because an earlier chained command fails,
   do not claim that the unexecuted stage passed.
5. Do not modify application source code while reviewing verification output.

## Ordered Actions

1. Inspect `frontend/package.json`.
2. Confirm the frontend validation command.
3. Enter the `frontend` directory.
4. Run `npm run verify`.
5. Capture terminal output and exit status.
6. Determine the build result.
7. Determine the Jest test result.
8. Determine the ESLint result.
9. Identify relevant warnings or errors.
10. Report the overall result and recommendation.
11. Leave project source files unchanged.

## Acceptance Criteria

1. The workflow runs the existing `npm run verify` command.
2. The overall PASS/FAIL result matches the command exit status.
3. Results are reported only for stages that actually executed.
4. Material errors are included in the report.
5. Warnings are not incorrectly classified as errors.
6. The recommendation agrees with the verification result.
7. The output is concise and understandable without reading the complete log.
8. No application source files are modified.

## Run 001 Prompt

Run the MediaVault frontend verification workflow. Inspect
`frontend/package.json`, run `npm run verify` from the frontend directory,
and summarize whether verification passed or failed. Do not modify project
files.

## Run 002 Prompt

Run the MediaVault frontend verification workflow. Inspect
`frontend/package.json`, then run `npm run verify` from the frontend
directory. Report using these sections: Overall Result, Build, Tests, Lint,
Warnings or Errors, and Recommendation. State PASS or FAIL for each stage
that actually ran, distinguish warnings from errors, and do not modify
project files.
