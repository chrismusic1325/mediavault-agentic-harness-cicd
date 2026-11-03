# Module 3 Calibration Log

## Calibration Cycle — November 3, 2026

Failure mode: retrieval fallback misclassification.

Development task: evaluate the MediaVault Lessons Learned retrieval system
against the fixed ground-truth set.

Before fix: the retrieval keyword detector treated ordinary uppercase terms
such as JSON and HTTP as literal identifiers. The system scored 4/6, or 67%,
below the required 80% floor.

Detection: the deterministic retrieval evaluation showed that Q2 and Q5 found
the expected documents through the wrong retrieval path.

Root cause: the keyword pattern was too broad.

Fix layer: tool / retrieval configuration.

Targeted fix: keyword fallback was limited to code-like identifiers containing
an underscore or digit. Ordinary terms such as JSON and HTTP now use semantic
retrieval, while MAX_PAGE_SIZE still uses keyword fallback.

After fix: the same unchanged ground-truth set scored 6/6, or 100%.

Before-fix evidence:
docs/module3-lab-evidence/before-fix.md

After-fix evidence:
docs/module3-lab-evidence/after-fix.md

Regression evidence:
docs/module3-lab-evidence/regression-results.md

Remaining limitation: the harness evaluates the failure modes currently covered
by its checks. New failure modes may require additional checks.
