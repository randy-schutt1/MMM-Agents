# CONTRADICTIONS

Conflicting teachings found within the course.

Template: `00_SYSTEM/TEMPLATES/CONTRADICTION_TEMPLATE.md`

---

## STATUS

```text
RECORDS: 0
```

**Intentionally empty.** No course material has been studied, so no course
contradiction has been observed.

> Infrastructure conflicts — including disagreements between the two governing
> agent files — are **not** recorded here. They belong in
> `00_SYSTEM/SETUP_ISSUES.md`. This file is exclusively about the Market Maker
> Method as taught.

---

## PURPOSE

**Never silently reconcile conflicting teachings.**

When lesson 3 and lesson 9 appear to disagree, the tempting move is to pick the
reading that makes the corpus tidy. That invents a rule the instructor never
taught, and the invention is untraceable afterwards.

A contradiction may turn out to be:

- a timeframe difference,
- a market-phase difference,
- a setup-subtype difference,
- a later lesson refining an earlier one,
- an instrument difference,
- a context difference,
- a stated exception,
- instructor shorthand,
- or a genuine inconsistency in the course.

All nine are worth knowing. Collapsing them into a guess destroys that information.

---

## RESOLUTION STATES

| Status | Meaning |
|---|---|
| `UNRESOLVED` | No evidence yet distinguishes the readings. **Default, and often the correct end state during the Student Phase.** |
| `PROVISIONAL` | A working interpretation is adopted with evidence, flagged for confirmation. Must not be written into the concept library as fact. |
| `RESOLVED` | Later course material settles it. Cite the resolving evidence. |
| `HUMAN REVIEW REQUIRED` | Two plausible readings materially change trading logic. |

A **foundational** unresolved contradiction may justify a reviewer `BLOCKED`. A
non-foundational one may permit `PASS` with an open research item carried in
`18_REVIEW/REVIEW_INDEX.md`.

---

## REVIEW CADENCE

Re-examine every open contradiction at each cumulative checkpoint (25/50/75/100%).
Later lessons frequently resolve earlier conflicts — and occasionally create new
ones that are invisible within any single lesson.

An ignored contradiction is reviewer error code E13.

---

## INDEX

| ID | Concept | Sources | Status | Foundational? |
|---|---|---|---|---|
| C-001 | How long price runs away from the anchor point | V01 `[00:35:05]` vs V01 `[00:35:15]` / `[00:35:55]` | UNRESOLVED | **Yes** |
| C-002 | Whether the trading-zone / blue-box filter and the one-direction rule are mandatory | V01 `[00:44:15]` / `[00:51:22]` vs V01 `[00:44:03]` / `[00:51:34]` | STATED EXCEPTION — condition unmeasurable | No, but blocking for implementation |

---

## RECORDS

## C-001 — Duration of the move away from the anchor point

### Concept

How many days price continues away from the anchor point once the anchor is
established. This sets the holding period for every weekly-cycle trade.

### Source A

| Field | Value |
|---|---|
| Video | V01 |
| Timestamp | `[00:35:05]` |
| Screenshot | None — I-006 |
| What is said/shown | "Now you know one thing **for sure**. If the anchor point is in place, you trade away from the anchor for **two and a half to three more days**." |

### Source B

| Field | Value |
|---|---|
| Video | V01 |
| Timestamp | `[00:35:15]`, `[00:35:55]` |
| Screenshot | None — I-006 |
| What is said/shown | `[00:35:15]` "if the anchor point comes in on a Tuesday, it is **likely** that they will rise for what's perceived as **four days, three and a half days, three days**." `[00:35:55]` "if the dealer anchors in on Tuesday and rises Tuesday, [Asian] session, half a day, he'll rise Wednesday, Thursday and **complete the cycle on Friday**." |

### Conflict

Source A gives 2.5–3 days and asserts it as certain. Source B, ten seconds later,
gives a three-value range topping out at 4 days and hedges it as "likely". Source B's
worked Tuesday example spans Tuesday-half through Friday — roughly 3.5 days —
which is inside B's range and outside A's.

These cannot both be stated certainties about the same quantity. Either the "for
sure" in A is loose speech, or A and B are describing different things that the
lesson does not distinguish.

**The instructor is aware of the conflict and does not resolve it.** At `[00:36:07]`
he quotes students back at himself — "Steve, you said three days, three levels. Four
days or three and a half days, everyone['s] counting. It's more than what I've told
you. I understand that." He then moves to a different point at `[00:36:38]`. This is
a source-level inconsistency, not a transcription artifact.

### Possible Explanations

| # | Explanation | Supporting evidence | Assessment |
|---|---|---|---|
| 1 | Different timeframe | None. Both statements concern days within one week. | Rejected |
| 2 | Different market phase | None stated. | No evidence |
| 3 | Different setup subtype | None stated. | No evidence |
| 4 | Later lesson refines the earlier one | Not applicable within V01; possible for V02–V21. | **Open — most likely route to resolution** |
| 5 | Different instrument | None. No instrument is attached to either statement. | Rejected |
| 6 | Different context | Partially: A speaks of "trading away from the anchor", B of the market "rising". These may be a trader-side window and a market-side move, which need not be identical — the trade window could reasonably be shorter than the move. **The lesson never says this.** | **Plausible, unstated — do not adopt** |
| 7 | Stated exception | `[00:35:43]` adds "an extra day if it happens to fall on Friday", which extends but does not reconcile. | Partial |
| 8 | Instructor shorthand | `[00:36:17]` — "It's more than what I've told you. I understand that." — reads as an admission of loose prior teaching. | **Plausible** |
| 9 | Actual inconsistency in the course | The instructor's own acknowledgement at `[00:36:07]`–`[00:36:17]` is direct evidence for this. | **Most strongly supported** |

Explanations 6, 8 and 9 are all live. 6 is the only one that would make both
statements true; it is also the one with no textual support, and adopting it would be
inventing a distinction to make the course consistent. That is exactly the silent
reconciliation this log forbids.

### Resolution

```text
UNRESOLVED
```

**Foundational: yes.** Holding period is a first-order parameter. Any weekly-cycle
rule, backtest, or specification that commits to a day count is committing to one
side of an unresolved conflict.

### Required to resolve

A later lesson stating the day count unambiguously, or — failing that — manual
backtest observation across enough weeks to distinguish the readings empirically.
Note that empirical resolution answers "what the market did", not "what the course
taught"; only the former is available if the course never clarifies.

### Interim handling

`DO NOT CODE` any day count. Where a holding period is needed downstream, carry the
conflict forward explicitly rather than picking a value.

---

## C-002 — Whether the entry filter and direction restriction are mandatory

### Concept

Whether (a) taking only trading-zone / blue-box setups and (b) trading only one
direction after a mid-week anchor are absolute rules or training constraints.

### Source A

| Field | Value |
|---|---|
| Video | V01 |
| Timestamp | `[00:44:15]`, `[00:51:22]` |
| Screenshot | None — I-006 |
| What is said/shown | `[00:44:15]` "if you are struggling… then I need you to take **only** those trades that are established by the proper formation of the trading zone." `[00:51:22]` "**Only** short trades will be warranted." |

### Source B

| Field | Value |
|---|---|
| Video | V01 |
| Timestamp | `[00:44:03]`, `[00:51:34]` |
| Screenshot | None — I-006 |
| What is said/shown | `[00:44:03]` "When you become more experienced… you can start to see that the blue box is **more of a guide**." `[00:51:34]` "When you become more proficient, you can **trade both ways**." |

### Conflict

Both pairs sit within seconds of each other and the instructor plainly intends them
as a strict form for beginners and a relaxed form for the experienced. **This is a
stated exception, not a genuine contradiction** — logged here because the condition
that selects between the two forms is unmeasurable (A-013), so downstream the two
forms are indistinguishable in practice.

### Possible Explanations

| # | Explanation | Supporting evidence | Assessment |
|---|---|---|---|
| 7 | Stated exception | Explicit in both pairs — "when you become more experienced", "when you become more proficient". | **Confirmed** |
| 9 | Actual inconsistency | None. The conditional is stated openly each time. | Rejected |

### Resolution

```text
RESOLVED AS STATED EXCEPTION — CONDITION UNMEASURABLE
```

The course's position is clear. What is missing is any test for which side of the
condition a given trader is on. See A-013.

**Foundational: no** — but blocking for implementation. Any specification must state
which form it encodes, and must record that the course offers both. Encoding the
relaxed form silently would drop a constraint the course places on its stated target
audience; encoding the strict form silently would present a training constraint as
doctrine.

### Interim handling

Encode neither form as unconditional. Carry both, tagged with the skill condition,
until A-013 resolves or is declared permanently unmeasurable.
