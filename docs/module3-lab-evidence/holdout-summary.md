# Module 3 Clean Holdout Measurement

Six locked holdout tasks were run using six fresh Claude Code invocations.

No `--continue` or `--resume` option was used.

The same calibrated system version was used for every task, and no retrieval,
routing, prompt, rubric, or tool changes were made between runs.

## Measurement artifacts

- HO-01.md — retrieval and citation behavior
- HO-02.md — orchestration routing
- HO-03.md — MAX_PAGE_SIZE literal retrieval
- HO-04.md — Reviewer read-only boundary
- HO-05.md — repository versus memory evidence
- HO-06.md — conflicting review outcomes

## Calibration status

Before targeted fix: 4/6 retrieval checks passing (67%).

After targeted fix: 6/6 retrieval checks passing (100%).

Regression run: 6/6 passing with no previously passing retrieval check lost.

The targeted retrieval fix therefore held beyond the original failing cases.
The remaining limitation is that future failure modes outside the existing
deterministic and rubric coverage may require additional evaluation checks.
