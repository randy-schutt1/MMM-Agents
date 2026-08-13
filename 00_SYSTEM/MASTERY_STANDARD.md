# LESSON MASTERY STANDARD

The Student Agent's self-assessment standard, applied at the end of every lesson.

Source: `MMM_MASTER_STUDENT_RESEARCH_AGENT.md` §21, §35.

**This standard produces a self-assessment, not an authorization.** Only a
reviewer `PASS` (see `REVIEW_PROTOCOL.md`) permits progression to the next lesson.

Output: `07_MASTERY_REPORTS/VXX_MASTERY_REPORT.md`, from
`TEMPLATES/MASTERY_REPORT_TEMPLATE.md`.

---

## THE TEN DIMENSIONS

Assess each honestly. An honest `REVIEW REQUIRED` is worth more to this project
than an optimistic `PASS`.

### A. Recall

Can the agent explain all major lesson concepts **without referring to the notes**?

### B. Recognition

Can the agent identify the taught concepts on historical charts **not used in the
lesson**?

### C. Discrimination

Can the agent distinguish valid patterns from similar-looking invalid patterns?
Ask directly: *what would make this NOT the setup?*

An agent that can only identify clean textbook examples has not demonstrated
mastery.

### D. Sequence

Can the agent explain:

- what should happen before,
- what defines the setup,
- what confirms it,
- what invalidates it,
- what typically follows?

### E. Exceptions

Can the agent identify known variations and exceptions taught in the course?

### F. Homework

Was all assigned work completed satisfactorily? Was the first attempt preserved?
Classify honestly:

```text
FIRST-PASS SUCCESS
SUCCESS AFTER CORRECTION
SUCCESS AFTER SOURCE REVIEW
UNRESOLVED
```

### G. Manual Backtesting

Was the lesson applied to historical GBP/USD examples, with future price hidden at
the decision point, losers retained, and rule application graded separately from
trade outcome?

**And, per `DECISIONS.md` D-026 / D-027:** was a baseline defined *before* testing, was
the period pre-registered, was the reserved holdout left closed, and is every quoted
rate reported with its sample size and interval? A test without a baseline is
`DESCRIPTIVE` at best and may **not** be cited as showing that a rule works
(`00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`).

### H. Provenance

Can every important rule be traced to a video timestamp, screenshot, chart, or
homework item? List any orphan rules explicitly — do not hide them.

### I. Ambiguity

Are unresolved and subjective concepts properly documented in
`10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` rather than quietly turned into rules?

### J. Contradictions

Are conflicts with earlier lessons documented in
`11_CONTRADICTIONS/CONTRADICTIONS.md` rather than silently reconciled?

---

## STATUS VALUES

The mastery report status must be **exactly one** of:

```text
PASS
REVIEW REQUIRED
BLOCKED
```

| Status | Meaning | Next action |
|---|---|---|
| `PASS` | The student believes all ten dimensions are satisfied and submits the lesson for independent audit. | Request a reviewer session. |
| `REVIEW REQUIRED` | The student is uncertain about one or more dimensions and wants the reviewer's judgement, or specific work is incomplete. | Request a reviewer session, naming the uncertainty. |
| `BLOCKED` | The student cannot complete the lesson — unusable source, foundational confusion, or a dependency on an unmastered earlier lesson. | Escalate; do not request a routine audit. |

> **Note on vocabulary.** The Student uses `PASS / REVIEW REQUIRED / BLOCKED`;
> the Reviewer uses `PASS / REVISE / BLOCKED`. These are two different actors'
> vocabularies and are deliberately kept distinct. See `SETUP_ISSUES.md` I-001.

A student `PASS` never advances the course by itself. It is a submission.

---

## QUALITY-CONTROL CHECKLIST

Before writing the mastery report, verify:

- [ ] Transcript exists
- [ ] Transcript timestamps are usable
- [ ] Source notes exist
- [ ] Interpretation is in a separate file from source notes
- [ ] Screenshots are captured and indexed
- [ ] Major rules have provenance
- [ ] Homework is complete (or documented as absent from the lesson)
- [ ] Manual chart testing is complete where appropriate
- [ ] Positive examples exist
- [ ] Negative examples exist
- [ ] Borderline examples exist where the concept is genuinely ambiguous
- [ ] Failed valid setups are recorded, not hidden
- [ ] Unresolved ambiguity is logged
- [ ] Contradictions are logged
- [ ] Concept library entries created/updated and indexed
- [ ] `COURSE_PROGRESS.md` updated
- [ ] `LOG.md` updated
- [ ] `scripts/validate_project.py` passes
- [ ] Git state clean after commit

Any unchecked box must be stated in the mastery report, not omitted.

---

## SELF-ASSESSMENT HONESTY

The mastery report is read by an adversarial reviewer who will inspect the source
material independently. Overstating mastery does not survive that process; it only
wastes a review cycle and adds a `REVISE` to the permanent record.

Specifically, do not:

- claim recognition ability that was demonstrated only on lesson examples,
- describe an inferred rule as explicit instruction,
- omit a losing or embarrassing backtest observation,
- present a rule as provenanced when the citation is vague,
- describe homework reconstructed after seeing the answer as first-pass success.

Perfection is not required. **Reliable understanding is.**
