# VXX — INDEPENDENT REVIEW

> Copy to `18_REVIEW/VXX/VXX_REVIEW_R<n>.md`. **Never overwrite an earlier round.**
> Delete these instruction blocks.

| Field | Value |
|---|---|
| Lesson | VXX |
| Review version | R1 |
| Review date | |
| Previous review | (`VXX_REVIEW_R<n-1>.md`, or `none`) |

---

## FINAL DECISION

```text
PASS | REVISE | BLOCKED
```

**Decision:** 

**Confidence:** HIGH / MEDIUM / LOW

---

## SOURCE MATERIAL REVIEWED

What was inspected **first**, before the student's conclusions.

| Source | Timestamps / references | Purpose |
|---|---|---|

If source access was limited, say so — it caps the confidence of this review.

## STUDENT ARTIFACTS REVIEWED

| Artifact | Reviewed |
|---|---|

---

## CRITICAL FINDINGS

Issues that could materially alter the methodology or later trading logic. **A
lesson with unresolved CRITICAL issues cannot pass.**

| # | Finding | Error code | Evidence | Impact |
|---|---|---|---|---|

---

## RULE FIDELITY

Did the student accurately represent what was taught? Check for omitted qualifiers,
examples generalized into universal rules, shorthand mistaken for precise rules,
terminology drift, interpretation mislabelled as instruction.

**Grade:** PASS / MINOR ISSUE / MAJOR ISSUE

| Student's rule | Source says | Assessment |
|---|---|---|

## CHART RECOGNITION

Are valid examples genuinely valid? Are invalid examples rejected **for the correct
reason**? Boundaries, sequence, context, timing, confirmation, invalidation — and
was future price action used to justify the original classification?

Do not give credit merely because a chart later became profitable.

**Grade:** PASS / MINOR ISSUE / MAJOR ISSUE

## HOMEWORK

Was the assignment understood? Is the first attempt preserved? Was the answer
reconstructed after seeing the solution?

| # | Claimed result | Verified result | Assessment |
|---|---|---|---|

**Grade:** PASS / MINOR ISSUE / MAJOR ISSUE

## MANUAL BACKTESTING

Audit the procedure, not the results. All fourteen checks
(`REVIEW_PROTOCOL.md` §6.G):

| # | Check | Result |
|---|---|---|
| 1 | GBP/USD used as primary instrument | |
| 2 | Historical period selected reasonably | |
| 3 | Chart advanced sequentially | |
| 4 | Future price hidden at the decision point | |
| 5 | Rules known before the result | |
| 6 | No trades skipped after outcomes were visible | |
| 7 | Losers retained | |
| 8 | Borderline setups retained | |
| 9 | Invalid setups separated from valid losers | |
| 10 | Outcomes recorded consistently | |
| 11 | R calculated consistently | |
| 12 | Screenshots captured before and after | |
| 13 | Exact lesson rule identified per test | |
| 14 | Testing the lesson, not a later interpretation | |

**Grade:** PASS / MINOR ISSUE / MAJOR ISSUE

## HINDSIGHT / LOOKAHEAD AUDIT

Actively searched for: boundaries defined using future highs/lows; classification
requiring the later reversal; entries justified after the target was hit; ignored
losing examples; interpretation changed after the outcome; only clean setups
selected; information assumed that was unavailable at the decision candle.

| Observation | Contamination found | Severity |
|---|---|---|

**If hindsight materially compromised the testing → BLOCKED** until repeated
properly.

**Verdict:** CLEAN / MINOR CONCERNS / MATERIALLY COMPROMISED

## POSITIVE EXAMPLES

Are they genuinely valid? Spot-check independently.

## NEGATIVE EXAMPLES

Are they genuine lookalikes rejected for the right reason — or straw men that no
one would confuse with the setup?

## BORDERLINE CASES

Is the uncertainty genuine and well-reasoned?

## PROVENANCE AUDIT

| Rule | Cited source | Verified? | Status |
|---|---|---|---|
| | | | SUPPORTED / UNSUPPORTED |

Orphan rules:

```text
Rule:            "..."
Problem:         No course evidence cited.
Reviewer status: UNSUPPORTED.
```

## AMBIGUITIES

Has subjective language been prematurely turned into constants? Are ambiguities
honestly logged?

| Term | Student handling | Assessment |
|---|---|---|

## CONTRADICTIONS

| Conflict | Student resolution | Reviewer status |
|---|---|---|
| | | RESOLVED / PROVISIONAL / UNRESOLVED |

## MACHINE-RULE FIREWALL

Any unsupported quantification introduced?

| Proposed rule | Source support | Classification |
|---|---|---|
| | NONE | INFERRED MACHINE CANDIDATE — NOT A COURSE RULE |

## TEACH-BACK ASSESSMENT

Could the student explain the concept simply and accurately across all nine points?

## BLIND RECOGNITION TEST

| Chart | Student classification | Correct? | Notes |
|---|---|---|---|

Value correct uncertainty. `INSUFFICIENT INFORMATION` is not a wrong answer when
the methodology genuinely requires more confirmation.

---

## STUDENT MASTERY ASSESSMENT

Independent judgement on each of the ten dimensions — not an echo of the student's
self-assessment.

| Dimension | Student said | Reviewer assessment |
|---|---|---|
| A. Recall | | |
| B. Recognition | | |
| C. Discrimination | | |
| D. Sequence | | |
| E. Exceptions | | |
| F. Homework | | |
| G. Manual backtesting | | |
| H. Provenance | | |
| I. Ambiguity | | |
| J. Contradictions | | |

---

## ALL FINDINGS BY SEVERITY

| # | Severity | Code | Finding | Required action |
|---|---|---|---|---|
| 1 | CRITICAL / MAJOR / MINOR / NOTE | E0X | | |

---

## REQUIRED CORRECTIONS

Specific and actionable. Not "study this more", but:

> Reclassify `BT_V04_0013` because the candidate pattern lacks the instructor's
> stated confirmation from 31:10–33:04. Add one valid and two invalid comparison
> charts before resubmission.

1. 
2. 

**Redo vs edit** — for each correction, state which. Work whose underlying test was
invalid must be **redone**, not reworded (`REMEDIATION_PROTOCOL.md` §2).

## REVIEWER QUESTIONS

Questions the student must answer on resubmission.

## HUMAN REVIEW

```text
HUMAN REVIEW REQUIRED: yes / no
```

If yes — why: unclear audio, insufficient chart resolution, contradictory
instructor language, highly ambiguous visual interpretation, two plausible readings
that materially change trading logic, or a machine definition that would require an
arbitrary judgement.

---

## ADVANCEMENT DECISION

```text
LESSON: VXX
DECISION: PASS / REVISE / BLOCKED
CONFIDENCE: HIGH / MEDIUM / LOW

CRITICAL ISSUES:
-

MAJOR ISSUES:
-

REQUIRED ACTIONS:
1.
2.

ADVANCEMENT:
AUTHORIZED / NOT AUTHORIZED
```

---

## REVIEWER SELF-CHECK

- [ ] I inspected source evidence before the student's conclusions
- [ ] I did not assume polish equals correctness
- [ ] I attempted to falsify the student's rules, not to confirm them
- [ ] I did not import external trading frameworks
- [ ] I did not invent a resolution where evidence was insufficient
- [ ] I did not manufacture objections to appear rigorous
- [ ] Every required correction is specific enough to act on
- [ ] Would I let real-money execution eventually depend on this interpretation?
