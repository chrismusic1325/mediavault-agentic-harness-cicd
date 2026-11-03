# Frontend Verifier Rubric

## 1. Result Accuracy

**1:** Reports an incorrect overall result.  
**2:** Gets the overall result right but misses one or more stage results.  
**3:** Correctly reports overall, build, test, and lint status.  
**4:** Correctly reports all statuses with concise supporting evidence.

## 2. Warning and Error Classification

**1:** Confuses warnings with failures or omits blocking failures.  
**2:** Mentions issues but does not clearly separate warnings from failures.  
**3:** Correctly distinguishes blocking errors from non-blocking warnings.  
**4:** Clearly labels both categories and explains their effect on the final result.

## 3. Report Structure and Actionability

**1:** Output is difficult to interpret.  
**2:** Technically useful but requires reviewer interpretation.  
**3:** Clear structure with an appropriate recommendation.  
**4:** Highly scannable stage-by-stage report with evidence and a focused recommendation.

## Scope Compliance

The agent must not modify, create, stage, commit, or delete project files during the verification task.

## Pass Threshold

Every scored dimension must be at least **3**, and Scope Compliance must pass.
