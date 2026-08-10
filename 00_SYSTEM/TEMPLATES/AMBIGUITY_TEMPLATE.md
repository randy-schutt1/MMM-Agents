# AMBIGUITY RECORD TEMPLATE

> Copy this block into `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` as a new `A-NNN`
> section. Do not create separate files.

Log every subjective phrase that would be dangerous to code prematurely — *strong
push, clean move, obvious level, nice M, enough space, significant move, strong
reversal, good setup, too extended, trapped traders, market maker behaviour.*

The purpose is to keep judgement-based language **visible as judgement** so it does
not quietly become a numeric constant (`DECISIONS.md` D-010).

---

```markdown
## A-NNN — "<exact phrase as used>"

### Course Meaning

What the instructor appears to mean, in the instructor's framing. If unclear, say
so — do not supply a definition the course does not give.

### Evidence

| Video | Timestamp | Usage in context |
|---|---|---|
| VXX | `[HH:MM:SS]` | "..." |

### Visual Characteristics

What the examples have in common on the chart. Describe what is observable, not a
threshold.

| Example | Screenshot | Observed characteristic |
|---|---|---|

### Counter-examples

Cases where the phrase was NOT applied, or was explicitly rejected. These bound the
concept more tightly than positive examples do.

| Video | Timestamp | What was rejected | Apparent reason |
|---|---|---|---|

### Possible Measurable Features

Candidate representations for **eventual** research. These are hypotheses.

| # | Candidate measure | Rationale | Course support |
|---|---|---|---|
| 1 | | | NONE / PARTIAL |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

### Current Status

```text
DO NOT CODE
```

Statuses: `DO NOT CODE` (default during Student Phase) → `RESEARCH CANDIDATE`
(Phase 4, hypothesis defined) → `EMPIRICALLY VALIDATED` (Phase 6, tested against
labelled history) → `RESOLVED BY COURSE` (a later lesson defines it explicitly).

### Required Research

What would resolve this — a later lesson, more examples, a labelled dataset,
comparison of positive and negative cases, or human judgement.

### Impact If Wrong

What breaks downstream if this is quantified incorrectly. This determines how much
evidence is needed before promotion.

### Related

| Type | Reference |
|---|---|
| Concept | CL-0NN |
| Contradiction | C-0NN |
```

---

## RULES

1. **Never assign a number during the Student Phase**, however reasonable it seems.
2. Never promote a status without evidence — a later lesson, or empirical
   validation against labelled charts.
3. Never delete a record because a concept later became clear. Update the status and
   append the resolution; the history matters.
4. The reviewer checks this log specifically for premature quantification (E12,
   E15).
