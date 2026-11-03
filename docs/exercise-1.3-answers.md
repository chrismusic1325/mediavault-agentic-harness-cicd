# Exercise 1.3 Answers

## Question 1

Run 001 revealed that the workflow could execute the MediaVault frontend
verification process and determine the overall result, but the initial prompt
left too much flexibility in how the results were presented. The baseline was
less standardized when separating the build, test, and lint stages, which made
the output require more reviewer interpretation. This showed that a workflow
can produce useful technical evidence while still benefiting from a more
precise reporting contract.

## Question 2

Between Run 001 and Run 002, I changed the instructions so the result had to
use a fixed structure with separate Overall Result, Build, Tests, Lint,
Warnings or Errors, and Recommendation sections. I also required explicit
stage results and a distinction between warnings and errors. Run 002 therefore
produced a more structured result that mapped more directly to the rubric and
was easier to review consistently.

## Question 3

The same MediaVault frontend validation command and project configuration were
used across both runs, so the core verification workflow stayed consistent.
The main change was the precision and structure of the reporting. Run 002 made
the individual stages and final recommendation easier to evaluate while
preserving the same underlying verification task. Based on the repeated
execution and consistent evidence, the workflow appears stable enough to
repeat, and the improved prompt provides a better format for future runs.

### Recorded Evidence

Run 001:
- Overall result: PASS
- Build: PASS
- Tests: PASS
- Lint: PASS
- Cycle time: 2m 47s
- Review latency: 0m 26s
- Rubric score: 8/12
- Quality decision: FAIL

Run 002:
- Overall result: PASS
- Build: PASS
- Tests: PASS
- Lint: PASS
- Cycle time: 0m 43s
- Review latency: 0m 46s
- Rubric score: 12/12
- Quality decision: PASS
