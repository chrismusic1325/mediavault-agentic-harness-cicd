# Decision 001 - Evidence-Based Verification Status

**Date:** 2026-10-27
**Review by:** 2027-01-25
**Status:** Active

**Decision:** Frontend verification stages may only be labeled PASS or FAIL
when that stage actually executes; a stage blocked before execution must be
reported as NOT RUN.

**Rationale:** Earlier verification work showed that runtime permission
requirements can prevent the verification command from executing. Treating an
unexecuted stage as passed or failed would create a conclusion without evidence.
Using PASS, FAIL, and NOT RUN preserves the distinction between application
results and environment limitations.

**Alternatives rejected:** Treating the overall verification attempt as a
simple pass/fail result was rejected because it hides whether individual stages
actually executed. Assuming results from a previous session was also rejected
because each verification report must use current evidence.

**Scope:** MediaVault frontend verification workflow.

**Review trigger:** Review this decision if the verification workflow,
permission model, or reporting requirements materially change.
