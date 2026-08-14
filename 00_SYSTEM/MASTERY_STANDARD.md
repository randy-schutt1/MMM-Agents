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

## ⭐ DIMENSION DISPOSITIONS — `NOT APPLICABLE` · `DEFERRED` · `EXCLUDED BY DECISION`

**Added 2026-08-14 by `D-046`**, which refines `D-018` and `D-019`; both remain `ACTIVE` and
neither is superseded. A dimension that is not graded normally takes **exactly one** of three
dispositions, and they are not interchangeable:

| Disposition | Meaning | Effect | Who can grant it |
|---|---|---|---|
| `NOT APPLICABLE` | The lesson supplies **no subject matter** | Closed permanently | `D-018`, **dimensions F and G only** |
| `DEFERRED` | Subject matter exists; a prerequisite is missing and **may arrive** | Stays **open**, carried in `REVIEW_INDEX.md` | Any dimension |
| **`EXCLUDED BY DECISION`** | Subject matter exists; the work is **permanently barred by a numbered decision**, which is **cited** | Closed; **no debt accrues**; the exclusion is **auditable** | **Any dimension**, subject to reviewer audit |

**`EXCLUDED BY DECISION` requires ALL FOUR conditions. Failing any one, it is not available:**

| # | Condition |
|---|---|
| 1 | **Subject matter exists.** The lesson supplies material the dimension would otherwise grade. **This is what separates it from `NOT APPLICABLE`** |
| 2 | ⭐ **The work is permanently barred by a numbered decision in `DECISIONS.md`, and THE DECISION IS CITED BY NUMBER in the report.** An exclusion with no citable decision is **not available** — the disposition is `DEFERRED`, or the work is done |
| 3 | **No future lesson can lift the bar. This is what separates it from `DEFERRED`.** Where a future lesson *could* lift it — a definition the course has not yet given — the disposition is `DEFERRED` and `D-030` governs |
| 4 | **The record states WHAT was excluded**, specifically enough that a reader can see **the size of the hole** |

⚠️ **`EXCLUDED BY DECISION` IS NOT A PASS.** It is a claim the reviewer audits like any other, and
**a reviewer who finds the cited decision does not in fact bar the work returns `REVISE` with the
dimension reinstated.**

⚠️ **It creates no new licence to exclude. Condition 2 is the whole guard: NO NUMBERED DECISION, NO
EXCLUSION.** A session that cannot name the decision has not found a third disposition — **it has
found work it has not done.**

**Unlike `NOT APPLICABLE`, this disposition is a POSITIVE STATEMENT that material was withheld.**
That is the point of it: the exclusion becomes visible and auditable rather than invisible.

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
