# V09 — INTERPRETATION

**Companion to:** `03_LESSON_NOTES/V09_SOURCE_NOTES.md`
**Lesson:** V09 — no printed title · `Bootcamp1 Wk2 032612 Part4 (53mins).swf`
**Speaker:** 100% `GUEST` (fifth consecutive lesson with zero course-author runtime)

> **What this file is.** Reading, not record. `V09_SOURCE_NOTES.md` says what the lesson
> **states**; this file says what this session **thinks it means**, with a confidence grade on
> every claim. Under `D-008` nothing here outranks anything there, and nothing here may enter
> `12_MASTER_SPEC/`, `13_MACHINE_SPEC/` or `08_CONCEPT_LIBRARY/` on its own.
>
> **Process disclosure carries over from `V09_SOURCE_NOTES.md` §0**: this session had already
> seen the slides when both files were typed. Basis tags are used here too.

---

## CONFIDENCE SCALE

| Grade | Meaning |
|---|---|
| **HIGH** | The lesson states it outright, in more than one place, and the arithmetic closes |
| **MEDIUM** | A reasonable reading of what is said, with a stated alternative |
| **LOW** | A hypothesis this session finds attractive and the lesson does not support |
| **NONE** | Recorded because someone will otherwise infer it. Explicitly not held |

---

## Q1. Is V09 a continuation of V08, and does that change how V09 should be read?

**Answer: yes, and yes — but only in one direction.** `HIGH` confidence, `AUDIO`.

The evidence is in the transcript header and §15 of the source notes. What matters
interpretively is the **asymmetry**: V09 answers questions V08 posed, so V08 is a legitimate
context for reading V09. **The reverse is not licensed.** Nothing in V09 may be used to
retrofit meaning into a V08 sentence that stands on its own, and no V08 grade changes.

**What the continuity does change:** V08's `NOT APPLICABLE` / open items about the innermost
ring and the promised stop-side ramifications are now **answerable**, and §15 answers them. That
is a gain for V08's record and it belongs in V08's remediation, not in V09's.

---

## Q2. What exactly is the risk system, stated in one place?

`HIGH` confidence, `AUDIO+PRINTED`. This is the reading, not a machine rule (`D-010`).

```text
GIVEN a trade with a known stop distance S (pips) on an account of balance B:

  risk_dollars = B × 0.02
  size         = risk_dollars ÷ S            (in $ per pip)

  CUMULATIVE across all simultaneously open positions, not per trade.
  Three pairs at once => carve the 2% three ways.

  ON A LOSS:  keep the same size. Repeat for losses 2 and 3.
  ON LOSS 4:  recalculate size from the new (8%-reduced) balance.
  ON A WIN:   recalculate size from the new balance.

  TARGET >= 2 x STOP always; 3 x STOP once HOD/LOD entries are reliable.
```

**Why the loss-side rule is the interesting half.** Every part of this is conventional
fixed-fractional sizing **except the hold-size-through-three-losses clause**. Fixed-fractional
sizing recalculated after *every* trade would shrink size after each loss automatically. He
explicitly does not do that, and gives a reason at `[00:06:28]`–`[00:06:34]`: *"so you guys don't
have to be fiddling with lot size calculators when you have to come back at these guys the
second or third time… you don't have to think about size once you've determined what your sizes
are."*

**This session's reading, `MEDIUM`:** the deviation is **operational, not mathematical**. He is
trading a small amount of theoretical precision for the ability to re-enter without a
calculation under stress — which is consistent with the lesson's whole thesis that the enemy is
emotional turbulence. **The alternative reading, which the lesson does not exclude:** it is a
mild martingale-flavoured recovery scheme, in which the size is deliberately not reduced while
the trader is losing. `[00:06:08]` — *"believe it or not, this is still a rather aggressive
approach to risk management"* — is him **naming that reading himself**, which is why this is
recorded as a genuine ambiguity of intent rather than a criticism.

---

## Q3. Is the "3:1 with a 15-pip stop" claim reachable from anything the course has taught?

**Answer: partly, and the missing half is the one that matters.** `HIGH` confidence on the gap.

| Component | Supplied by | Status |
|---|---|---|
| Stop **size** (15 pips) | V09 `[00:03:49]` | ✅ Explicit |
| Target **size** (50 pips) | V09 `[00:03:56]` | ✅ Explicit |
| The **entry** that makes a 15-pip stop survivable | V08's high-low drill; V09 calls it *"mastering HOD/LOD entries"* | ⚠️ **Named, not taught** — `A-056` is extended by V09 and not closed |
| Stop **placement** relative to structure | **Nobody, anywhere in V01–V09** | ❌ **Absent** |

**The interpretive point, `HIGH`:** a 15-pip stop is not a risk parameter you choose, it is a
**consequence of entering close enough to the extreme that 15 pips is beyond it**. V08 prints a
10-pip tolerance from HOD/LOD; V09 asserts a 15-pip stop. **Those two numbers are consistent
with each other and with a stop just outside the extreme** — 10 pips of entry tolerance plus a
few pips of cushion.

> **This session finds that reading attractive and it is `LOW` confidence and NOT adopted.**
> Neither lesson states it. Writing *"stop = extreme ± 15"* into any artifact would be `D-010`
> and `D-030` in one move: it invents a placement rule out of two size numbers that were stated
> for different purposes, in different lessons, by the same speaker who never connects them.
> **Recorded here precisely so that a later session that notices the same coincidence can see it
> was noticed and refused.**

---

## Q4. Is the 20%-a-week projection dishonest, or is it a normal teaching simplification?

**Answer: this session declines to characterise intent, and the arithmetic gap is real either
way.** `HIGH` confidence on the gap (`C-013`), `NONE` on intent.

The gap is stated in the source notes §6 and does not need re-arguing. What belongs here is the
**interpretive question a reviewer will ask**: does `C-013` undermine the risk system?

**Reading, `MEDIUM`:** no, and they are separable. The **sizing rule** (Q2) is a policy about
how much to risk and is unaffected by whether the return projection is reachable. The
**projection** is a motivational passage whose function in the deck is to close the section —
it arrives after the material, is followed immediately by *"you can leave the jail cell, the
door is wide open"* `[00:27:15]`, and nothing later depends on it.

**The counter-reading, which is why `C-013` is logged as a contradiction and not a note:** the
projection is the last thing a student sees before the DMR pitch at `[00:27:24]`, and it is the
only place in the lesson where the printed slide, the spreadsheet and the spoken argument all
present a number that the lesson's own worked examples contradict. **A student who acts on it
would size their expectations by it.** That is a method-level consequence, so it is a `C-xxx`.

---

## Q5. What does the blueberry answer actually settle?

**Answer: one nickname, one timeframe, and it narrows a contradiction it cannot close.**
`HIGH` confidence — see source notes §9, which is the full treatment.

The interpretive residue not covered there:

**`LOW` — the 800/200 identity does NOT explain why the two sources disagree, and the arithmetic
is what settles it.** Downgraded from `MEDIUM` on 2026-08-13 per `V09_REVIEW_R1.md` `M5` (`E02`,
open item 77).

The tidy reading was: if the seminar notes describe a set plotted on one timeframe and the
recordings describe the same lines carried across timeframes, then *"5, 13, 50, 200"* and *"…and
the 800"* could be **the same lines seen from different charts**. **Applied to the whole
enumeration it fails.**

`MMM-NOTES` p.38 enumerates **four** averages — *"the 5, 13, 50 and 200"*. The identity the guest
states is a **factor of four** (`800 × 15m = 12,000 min = 200 × 60m`). So reading that set on the
1-hour maps it onto the 15-minute as:

```text
notes on H1:      5      13      50     200
same lines on M15:   20      52     200     800
corpus's set:      5      13      50     200     800   (A-020)
```

**One member lands. The other three do not** — the corpus carries a 5, a 13 and a 50, not a 20, a
52 and a 200. And the reading **collides with `A-020` itself**, whose attested mapping requires
**mayo = 200 and blueberry = 800 to be two different lines on one chart**; identifying them as one
line seen twice contradicts the very record the reconciliation would have to be consistent with.

**So the hypothesis reconciles one member of a four-member enumeration and breaks the other
three.** `C-010`'s own Assessment block already names the better explanation — **chronology**,
that the 800 entered the method after the notes were written, which the notes' *"any other rapidly
moving pair of EMA's would achieve the same goal"* supports.

**It was not adopted, and that refusal was correct — for two reasons now, not one.**
`SOURCING_HIERARCHY.md` §3.2 Case A ends *"**Do not blend**"*, and reading a timeframe into Tier 2
is exactly the composite definition the rule forbids. **The arithmetic above is the independent
second reason, and it is the stronger one:** the route does not reach even if the blending
objection is waived. `C-010` stays **open**.

> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — this passage previously graded
> the hypothesis **`MEDIUM`** and stated *"this session believes it is more likely than not"*,
> refusing it on the blending ground alone. The **decision** is unchanged; only the confidence and
> the reasoning are. `V09_REVIEW_R1.md` `M5`.)*

---

## Q6. Does *"three pushes, the third being the longest"* get us any closer to coding `push`?

**Answer: no. `MEDIUM` confidence that it moves the record at all, `HIGH` confidence that it
does not unblock it.**

It is the most structurally specific push statement in V01–V09 and it supplies an **ordering**
(third is longest) where the corpus previously had only a **count** (three). What it does not
supply: a size, a delimiter, a noise floor, or any way to identify pushes 1 and 2 **before**
push 3 exists — which is the only thing a recognition rule could use.

**The trap this session is refusing, stated so a reviewer can check the refusal:** *"third is
longest"* looks codable. It is not, because *longest* presupposes that you have already
segmented the move into three pushes, which is the undefined step. **`D-030` binds. Dimension B
stays BLOCKED for the fifth lesson running.**

---

## Q7. Where does V09 sit against the rest of the corpus?

`MEDIUM` confidence throughout — this is a map, not a claim.

| Layer | Supplied by | State after V09 |
|---|---|---|
| **Market model** (weekly cycle, sessions, market-maker intent) | V01–V04 | Reasonably complete as narrative, undefined as rules |
| **Pattern vocabulary** (M/W, levels, pushes, traps, resets) | V02–V09 | **Named throughout, defined nowhere.** V09 adds *reset*, *dinosaur*, *tracer*, *alternate count* to the undefined pile |
| **Entry location** | V04–V08 | Named (HOD/LOD, the box, the level) and not operationalised |
| **Exit / target** | V04 (35–50 pips), V08 (3:1), V09 (50 pips) | Three sources, consistent magnitudes |
| **Stop size** | **V09 only** (25 / 15 pips) | ✅ First statement in the corpus |
| **Stop placement** | — | ❌ Still absent at V09 |
| **Position size** | **V09 only** | ✅ First statement, and it is complete and closed |

**The shape this reveals, `MEDIUM`:** the course is being taught **outside-in**. The market
narrative came first, the payoff geometry second, and the money management ninth. The one layer
that is fully specified — position sizing — is the one that is **independent of pattern
recognition**, and that is not a coincidence: it is the only layer that *can* be fully specified
without first defining a push, a level or an M.

---

## Q8. What would falsify this session's reading of V09?

Required by `REVIEW_PROTOCOL.md` §1's standard (*"what evidence would show this understanding is
wrong?"*).

| If this were found | It would overturn |
|---|---|
| A lesson in which the course author states a **different** risk percentage or a **different** loss-recovery rule | Q2 entirely, and would convert §13's `C-015` from a Tier 1/Tier 2 conflict into a Tier 1-internal one |
| A slide or lesson defining *level* as a countable unit | Q7's map, and would unblock H3's arrow drill (`A-004`) |
| A later lesson stating a **stop-placement** rule that is not `extreme ± n` | Q3's refused hypothesis — confirming the refusal was right |
| A later lesson stating a stop placement that **is** `extreme ± 15` | Q3's refused hypothesis — confirming it was true, and confirming that **refusing to adopt it here was still correct**, because it was not this lesson's evidence |
| `MMM-NOTES` or a lesson showing the notes' `200` is plotted on the 1-hour | **Nothing, on its own** — corrected 2026-08-13, `V09_REVIEW_R1.md` `M5`. It would land the `200 → 800` member and leave the notes' `5`, `13` and `50` mapping onto a `20`, a `52` and a `200` the corpus does not carry, and would still collide with `A-020`'s mayo = 200. **What would promote the hypothesis is a source stating the timeframe of the WHOLE set on both sides**, not of one member. *(Superseded row: "Q5's hypothesis, promoting it from unadopted to supported".)* |
| Any V09 claim failing arithmetic re-derivation | §2 of the source notes — which is why `05_HOMEWORK/V09` re-derives all of it in committed code rather than asserting it |
