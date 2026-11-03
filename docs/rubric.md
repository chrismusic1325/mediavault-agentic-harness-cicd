# Quality Rubric

## Workflow

MediaVault Frontend Verification Review

## Dimension 1: Verification Result Accuracy

Measures whether the workflow correctly identifies the overall result and
the build, test, and lint stages that actually executed.

### 1 - Does Not Meet
Reports an incorrect overall result or materially incorrect stage result.

Example: Verification fails during Jest, but the report says PASS.

### 2 - Partially Meets
Gets the overall result correct but describes stage results incompletely.

Example: Reports that tests failed but does not explain that build passed
and lint never executed.

### 3 - Meets
Correctly reports the overall result and every stage that actually executed.

Example: Overall FAIL; Build PASS; Tests FAIL; Lint did not run.

### 4 - Exceeds
Meets level 3 and includes concise supporting terminal evidence.

Example: Overall FAIL; Build PASS; Jest exited non-zero with two failed
suites, so lint did not execute.

---

## Dimension 2: Error and Warning Coverage

Measures whether material errors and relevant warnings are captured and
correctly distinguished.

### 1 - Does Not Meet
Omits a material error or incorrectly labels an error as a warning.

### 2 - Partially Meets
Captures the primary error but omits relevant secondary information.

### 3 - Meets
Captures the material errors and relevant warnings and distinguishes them.

### 4 - Exceeds
Meets level 3 and separates blocking failures from informational warnings.

---

## Dimension 3: Report Clarity and Actionability

Measures whether the result is easy to review and leads to an appropriate
next action.

### 1 - Does Not Meet
The report is confusing or recommends proceeding despite a failure.

### 2 - Partially Meets
The conclusion is generally correct but vague or poorly structured.

### 3 - Meets
Clearly states the result, supporting evidence, and an appropriate
recommendation.

### 4 - Exceeds
Provides a highly scannable result and a focused next step directly
supported by the evidence.

---

## Binary Gate: Scope Compliance

PASS if the verification workflow leaves application source files unchanged.

FAIL if the workflow edits, deletes, stages, commits, or pushes application
files as part of the review.

## Pass Threshold

Every scored dimension must receive a score of 3 or higher, and the Scope
Compliance gate must PASS.

## Alternatives Considered

An aggregate score such as 9/12 was considered but rejected because strong
clarity should not compensate for an incorrect verification result.

A completely binary checklist was also rejected because it would make it
harder to measure incremental improvement between runs.
