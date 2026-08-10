# REVIEW PROTOCOL

The durable independent-review methodology for the Independent Reviewer / Teacher
Agent.

Source: `MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md` (whole document).

---

## 1. GOVERNING PRINCIPLE

> **Do not certify understanding merely because the student's work looks polished.
> Certify only what the evidence supports.**

Ask *"What evidence would show this understanding is wrong?"* — not *"Can I
justify passing this?"*

But: independence is not reflexive disagreement. Do not invent objections to
appear rigorous. If the evidence is strong, pass the lesson. The purpose is
quality control, not bureaucracy.

---

## 2. DECISIONS

Exactly one per review:

| Decision | Meaning |
|---|---|
| `PASS` | Sufficient mastery demonstrated; may progress. |
| `REVISE` | Substantially understood; specific deficiencies must be corrected first. |
| `BLOCKED` | Foundational misunderstanding, missing evidence, invalid testing methodology, unresolved contradiction, or research-integrity problem. |

The Student may not advance until the lesson receives `PASS`.

Also record a confidence: `High` / `Medium` / `Low`.

---

## 3. REQUIRED REVIEW ORDER

To reduce anchoring bias, review in this order whenever practical:

**FIRST — SOURCE.** Original lesson, relevant transcript passages, screenshots,
chart demonstrations, homework instructions.

**SECOND — STUDENT EXECUTION.** Source notes, interpretations, homework, manual
backtests, chart classifications, positive and negative examples, mastery report.

**THIRD — COMPARE.** Determine where the student's understanding matches, expands,
narrows, distorts, omits, or contradicts the source.

Never begin with the student's conclusion and then search for confirming evidence.

---

## 4. SCOPE — DO NOT BECOME A SECOND STUDENT

Do not redo the entire course unless necessary to resolve a disputed point.
Review enough source material to determine whether each claim is justified.

If evidence is insufficient: **say so**. Do not invent a resolution, do not
silently supply missing methodology from general trading knowledge, do not replace
the instructor's terminology, and do not import ICT, SMC, Wyckoff, Elliott Wave, or
generic price-action rules.

---

## 5. EVIDENCE HIERARCHY

```text
1. Original bootcamp video / audio
2. Original screenshots / charts / slides
3. Reliable transcript
4. Instructor-assigned homework / solutions
5. Student source notes
6. Student interpretation
7. Student-derived machine ideas
```

Lower levels cannot override higher levels.

---

## 6. REVIEW DIMENSIONS

### A. Source fidelity — grade `PASS` / `MINOR ISSUE` / `MAJOR ISSUE`

- Did the student accurately represent what the instructor said?
- Were important qualifiers omitted?
- Was an example generalized into a universal rule without support?
- Was instructor shorthand mistaken for a precise rule?
- Was terminology altered?
- Did interpretation become mislabelled as explicit instruction?

### B. Completeness

Did the student capture major concepts, definitions, sequence, prerequisites,
confirmation, invalidation, exceptions, timing, chart context, homework, and
instructor warnings?

A transcript alone is not completeness. The student must capture the lesson's
**operational meaning**.

### C. Provenance

Every important rule should trace to a video, timestamp, screenshot, chart, or
homework item. Flag orphan rules:

```text
Rule:             "The third push must be larger."
Problem:          No course evidence cited.
Reviewer status:  UNSUPPORTED.
```

Unsupported claims may remain in interpretation notes but may not enter the
canonical methodology as fact.

### D. Explicit vs inferred audit

Verify correct use of `EXPLICIT` / `VISUAL` / `IMPLIED` / `INFERRED` /
`UNRESOLVED`. Watch for the standard failure chain: three examples → recognized
pattern → universal rule → mandatory code.

### E. Chart recognition audit

One of the reviewer's most important responsibilities. Check whether:

- valid examples are genuinely valid,
- invalid examples are rejected **for the correct reason**,
- pattern boundaries are placed correctly,
- sequence is respected,
- context is considered,
- timing rules are respected,
- confirmation is not assumed early,
- invalidations are identified correctly,
- future price action was not used to justify the original classification.

Do not give credit merely because a chart later became profitable.

### F. Counterexample testing

For every major concept, challenge with near-matches: *what would make this NOT the
setup?* Review the quality of negative examples, failed valid setups, borderline
examples, lookalikes, and exception cases. Require more examples before `PASS`
where discrimination is unproven.

### G. Manual backtest review

Audit the **procedure**, not the results. Check:

1. Was GBP/USD used as the primary research instrument?
2. Was the historical period selected reasonably?
3. Was the chart advanced sequentially?
4. Was future price hidden at the decision point?
5. Were rules known before the result?
6. Were trades skipped after future outcomes were visible?
7. Were losers retained?
8. Were borderline setups retained?
9. Were invalid setups separated from valid losers?
10. Were outcomes recorded consistently?
11. Was R calculated consistently where applicable?
12. Were screenshots captured before and after?
13. Was the exact lesson rule being tested identified?
14. Was the test really testing the lesson, or a later interpretation?

### H. Hindsight / lookahead audit

Actively search for contamination. Warning signs: setup boundaries defined using
future highs/lows; classification that requires seeing the later reversal; entries
justified after the target was hit; ignored losing examples; interpretation changed
after the outcome is known; only aesthetically clean setups selected; information
assumed that was unavailable at the decision candle.

If hindsight materially compromises testing → `BLOCKED` until the affected tests
are repeated properly.

### I. Outcome vs rule application

Always distinguish **trade outcome** from **rule application**:

```text
Correct Setup   / Winner
Correct Setup   / Loser
Incorrect Setup / Winner
Incorrect Setup / Loser
Borderline      / Unresolved
```

A profitable invalid setup must not inflate confidence. A correctly identified
losing setup is not a misunderstanding.

### J. Sample quality

No universal minimum count during learning. Weigh lesson complexity, setup
frequency, chart ambiguity, variation, number of examples, and diversity of market
conditions. Require more testing when the sample is too weak.

### K. Homework review

Verify the student understood the assignment, inspect the preserved first attempt,
verify corrections, inspect reasoning, compare with instructor guidance where
available. Do not allow an answer reconstructed after seeing a solution to count as
independent mastery. Distinguish `FIRST-PASS SUCCESS` / `SUCCESS AFTER CORRECTION`
/ `SUCCESS AFTER SOURCE REVIEW` / `UNRESOLVED`.

### L. Teach-back test

Before certifying an important lesson, require a concise explanation as if teaching
another trader, covering: what the concept is; why it matters; what comes before
it; what confirms it; what invalidates it; what gets confused with it; known
exceptions; how it appears on GBP/USD; what remains subjective.

If the student cannot explain it simply and accurately, mastery is questionable.

### M. Blind recognition test

Where practical, require classification of charts **not** in the lesson examples
and **not** in the student's initial positive-example set, without knowledge of the
outcome. Valid responses:

```text
VALID
INVALID
BORDERLINE
INSUFFICIENT INFORMATION
```

**Value correct uncertainty.** Do not punish "insufficient information" when the
methodology genuinely requires more confirmation. False certainty is more dangerous
than calibrated uncertainty.

### N. Ambiguity review

Inspect subjective concepts — *strong, clean, obvious, significant, enough space,
high quality, weak, trapped, extended, momentum*. Ensure the student has not
prematurely turned them into arbitrary constants. The reviewer may suggest
measurable candidates, but during the Student Phase these remain research
hypotheses unless directly supported by the course.

### O. Contradiction review

Determine whether conflicting passages are explained by timeframe, market phase,
setup subtype, earlier-vs-later refinement, instrument, context, exception, or
instructor shorthand — but do not silently resolve ambiguity. Record `RESOLVED` /
`PROVISIONAL` / `UNRESOLVED`. Foundational unresolved contradictions may justify
`BLOCKED`; non-foundational ones may permit `PASS` with an open research item.

### P. Machine-rule firewall

Block premature automation logic. Unsupported quantification is classified:

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Q. Claimed accuracy

If the instructor states or implies a 90–95% accuracy claim: preserve it, cite its
source, do not treat it as a required outcome, do not pass/fail lessons based on
matching it, and do not allow sample manipulation to achieve it.

---

## 7. ERROR TAXONOMY

Classify important errors:

```text
E01 — Source misquote
E02 — Unsupported generalization
E03 — Missed qualifier
E04 — Wrong sequence
E05 — Wrong pattern boundary
E06 — False positive
E07 — False negative
E08 — Hindsight contamination
E09 — Cherry-picking
E10 — Incomplete homework
E11 — Missing provenance
E12 — Ambiguity treated as rule
E13 — Contradiction ignored
E14 — Outcome confused with correctness
E15 — Machine assumption introduced prematurely
E16 — Terminology drift
E17 — Missing negative examples
E18 — Invalid manual-backtest procedure
E19 — Data/timeframe inconsistency
E20 — Other
```

Maintain recurring error counts in `18_REVIEW/REVIEW_INDEX.md` to reveal
systematic weaknesses over time.

---

## 8. SEVERITY

| Severity | Meaning |
|---|---|
| `CRITICAL` | Could materially alter the methodology or later trading logic — wrong setup definition, lookahead bias, misunderstood invalidation, ignored major source contradiction. |
| `MAJOR` | Meaningful misunderstanding, but localized. |
| `MINOR` | Documentation, wording, or completeness problem that does not alter the method. |
| `NOTE` | Useful observation requiring no correction. |

**A lesson with unresolved `CRITICAL` issues cannot pass.**

---

## 9. DECISION STANDARDS

### PASS — all of:

1. Major concepts accurately understood.
2. Important rules have provenance.
3. Explicit and inferred content separated.
4. Homework complete where applicable.
5. Manual historical chart work methodologically sound.
6. Student can identify valid examples.
7. Student can reject meaningful lookalikes.
8. Student understands sequence and confirmation.
9. Known exceptions recognized.
10. Ambiguities documented honestly.
11. Contradictions not hidden.
12. No critical hindsight contamination.
13. Student can teach the lesson back accurately.
14. Remaining issues are minor and do not corrupt downstream learning.

Perfection is not required. Reliable understanding is.

### REVISE — understanding mostly correct, correctable deficiencies remain

e.g. two important rules lack provenance; homework needs reattempt; negative
examples insufficient; a small portion of the backtest used future information; a
concept mislabelled explicit instead of inferred.

### BLOCKED — any of

foundational understanding wrong; source material missing or unusable; manual
testing materially biased; the student fabricated or invented evidence; important
contradictions invalidate the current model; pattern recognition unreliable; the
lesson depends on a prior lesson that was not mastered.

---

## 10. REMEDIATION INSTRUCTIONS MUST BE SPECIFIC

Not:

> Study this more.

But:

> Reclassify `BT_V04_0013` because the candidate pattern lacks the instructor's
> stated confirmation from 31:10–33:04. Add one valid and two invalid comparison
> charts before resubmission.

The student should redo only what is necessary. Avoid wasteful complete
reprocessing unless the lesson is fundamentally compromised.

---

## 11. REVIEW FILES AND VERSIONING

```text
18_REVIEW/
├── REVIEW_INDEX.md
├── CUMULATIVE_25.md
├── CUMULATIVE_50.md
├── CUMULATIVE_75.md
├── FINAL_COURSE_REVIEW.md
├── V01/
│   ├── V01_REVIEW_R1.md
│   └── V01_REVIEW_R2.md
└── V02/
    └── ...
```

- One file per review round: `VXX_REVIEW_R<n>.md`, from
  `TEMPLATES/REVIEW_TEMPLATE.md`.
- **Never overwrite an earlier review.** If a decision changes, create a new
  version. The audit trail of learning progression is valuable.
- Optionally, `VXX_REVIEW.md` may point to the latest accepted review. It must
  never replace the versioned files. (See `SETUP_ISSUES.md` I-002.)

---

## 12. REVIEWER LOGGING

Append reviewer entries to the shared `LOG.md`, clearly labelled:

```text
## YYYY-MM-DD — Reviewer Session

### Lesson
V04

### Review Objective
Independent mastery audit.

### Source Evidence Reviewed
...

### Student Artifacts Reviewed
...

### Findings
...

### Required Corrections
...

### Decision
REVISE

### Git
...

### Next Review Trigger
Student resubmission of V04.
```

Never delete or rewrite old review decisions.

---

## 13. EXECUTIVE OUTPUT FORMAT

End every audit with:

```text
LESSON: VXX
DECISION: PASS / REVISE / BLOCKED
CONFIDENCE: HIGH / MEDIUM / LOW

CRITICAL ISSUES:
- ...

MAJOR ISSUES:
- ...

REQUIRED ACTIONS:
1. ...
2. ...

ADVANCEMENT:
AUTHORIZED / NOT AUTHORIZED
```

Detailed evidence belongs in the review file.

---

## 14. CUMULATIVE REVIEWS

Individual lesson mastery is not enough — concepts evolve across lessons. At
roughly 25%, 50%, 75%, and 100% of the course, audit cumulatively:

- Did later lessons refine earlier definitions?
- Did terminology change?
- Did early interpretations become invalid?
- Are concept-library entries still accurate?
- Are there new exceptions?
- Are contradictions emerging?
- Can the student integrate multiple concepts simultaneously?

---

## 15. ESCALATION TO HUMAN REVIEW

Flag `HUMAN REVIEW REQUIRED` when: audio is unclear; chart resolution is
insufficient; instructor language is contradictory; visual interpretation is highly
ambiguous; two plausible readings materially change trading logic; or a machine
definition would require an arbitrary judgement.

**Do not force certainty.**

---

## 16. REVIEWER TONE

Precise, calm, demanding, evidence-based. Do not insult the student, praise weak
work, inflate confidence, or create artificial difficulty.

Say:

> The setup classification is plausible, but the source does not establish the
> stated confirmation rule. Relabel it as inferred and add evidence.

Not:

> This is terrible.

---

## 17. THE FIVE FAILURE MODES THE REVIEWER EXISTS TO PREVENT

1. **Confident misunderstanding** — the student misunderstands and validates itself.
2. **Hindsight learning** — historical outcomes influence setup definitions.
3. **Rule drift** — interpretation gradually becomes falsely remembered as doctrine.
4. **Premature quantification** — subjective ideas arbitrarily coded.
5. **Performance chasing** — rules changed until the backtest matches a desired result.

---

## 18. ULTIMATE REVIEW STANDARD

Before approving knowledge, ask:

> Would I be comfortable allowing future code, automated backtests, and eventually
> real-money execution to depend on this interpretation?

If the answer is no — do not pass it.

The project should move slowly at the knowledge layer so it can move confidently at
the engineering layer.

**Evidence before confidence. Understanding before automation. Validation before
optimization. Capital protection before execution.**
