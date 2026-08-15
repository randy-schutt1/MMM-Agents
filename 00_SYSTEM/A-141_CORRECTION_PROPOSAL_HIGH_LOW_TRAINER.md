# PROPOSED CORRECTION TO `A-141` — the `High / Low Trainer` is NOT a total void

> ## ⛔ THIS FILE AMENDS NO LEDGER. IT IS A PROPOSED CORRECTION FOR THE V21 SESSION TO APPLY.
>
> **`A-141` does not exist on integration.** It lives on **`origin/video/v21`, unmerged** — so this
> correction **cannot** be written into `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` from here without
> editing a record that is not in this branch's tree. It is therefore written as a **proposal**,
> in the project's *"propose, don't auto-close"* pattern, for the V21 student/review session to
> apply when V21 merges.
>
> **Raised by:** owner attestation, 2026-08-15. **Tier:** `OWNER EMPIRICAL PREFERENCE` (`D-052`) —
> the owner describing **his own tooling**, not what the course taught.
>
> ⚠️ **`A-141` STAYS OPEN either way.** This correction changes its *shape*, not its status.

---

## 1. THE OWNER'S STATEMENT

> *"The high low trainer is part of the sessions indicator. It's embedded in it. It just doesn't
> have the auto-places."* — owner, 2026-08-15

**Claim, decomposed:** (a) the Trainer's logic is **inside the session indicator** the project
already holds; (b) the **only** missing piece is **automatic order placement**.

---

## 2. WHAT `A-141` CURRENTLY SAYS, AND WHY IT NEEDS CORRECTING

`A-141` (V21) reads, in part:

> *"⛔ **The artifact itself is not in this repository and no part of the lesson exposes it.**"*
> *"⭐ **This is a different shape from every other `D-030` blocker in the corpus.** Elsewhere the
> course names a concept and withholds a definition. **Here the course SHIPPED a complete
> implementation and the copy did not reach this project.**"*

⚠️ **That framing is a TOTAL-VOID framing, and the owner says it is wrong on the level-tracking
half.** The correction is not that the tool is present — **it is not** — but that **the project
already holds a working implementation of a substantial part of its logic**, which changes what is
actually missing and therefore what would have to be supplied.

---

## 3. ⭐ THE RE-EXAMINATION — WHAT THE SESSION INDICATOR ACTUALLY CONTAINS

**Artifact re-examined:** `!sm_WorkTime_v1.5b.ex4` (md5 `b938ee1df8cf16a44bc16db71795e9f2`), the
session ribbon — indicator #8 of 14 in `MMM.tpl`, the subject of `DECISION_DRAFT_D-056`. Because
v1.5b is MT4 build-600+ packed, the readable evidence comes from its **pre-600 sibling**
`sm_WorkTime_no_autogmt.ex4` (md5 `8f0059bd2abf728b53198bb59f5ecaa2`), whose strings are legible,
plus the **saved parameter block in `MMM.tpl`**.

### 3.1 Strings recovered — verbatim

```text
 25 Pips above blue box          Alert25BlueBox      DrawStopHuntBox
 25 Pips below blue box          Alert50BlueBox      DrawStopHuntBox_as_outline
 50 Pips above blue box          Alert50EMA          StopHuntBoxColor
 50 Pips below blue box          Alert50Pips  (=20)  HighRange
 Check for 200EMA bounce         Alert200EMA         SoundOn / SoundFile
 Check for 800EMA bounce         Alert200Pips (=20)  WT_1..WT_5, WT_T1..WT_T5, WT_SH
                                 Alert800EMA
                                 Alert800Pips (=30)
```

### 3.2 The comparison, feature by feature

| High/Low Trainer, per `A-141` | Session ribbon | Verdict |
|---|---|---|
| Tracks a **session high and low** | ✅ the session boxes track high/low per band (Asian, Euro, NY, two market-open windows) | ⭐ **PRESENT** |
| **Fixed pip offsets** from that extreme | ✅ `Alert25BlueBox` / `Alert50BlueBox` — literally *"25/50 Pips above/below **blue box**"* | ⭐ **PRESENT IN KIND** |
| The offsets are **+20 and +40** | ⚠️ the ribbon's are **+25 and +50** | ⚠️⚠️ **DIFFERENT NUMBERS** |
| **Alerting** at those levels | ✅ `SoundOn` / `SoundFile` / `PopUp`-style alert flags | ⭐ **PRESENT** |
| **A market order + two pendings** | ⛔ nothing — **no order logic of any kind** | ⛔ **ABSENT** |
| **Hard stop on all three** | ⛔ nothing | ⛔ **ABSENT** |
| **Take profit `+30` from order 1** | ⛔ nothing | ⛔ **ABSENT** |
| **Cycle `30 + 50 + 70 = 150`** | ⛔ nothing | ⛔ **ABSENT** |
| **`MAX RISK 5%`, risk dial 1–5%, "by order percent"** | ⛔ nothing — no risk, lot or percent input exists | ⛔ **ABSENT** |
| **Four shipped variants** | ⛔ n/a | ⛔ **ABSENT** |

### 3.3 ⭐⭐ THE STRUCTURAL FACT THAT SUPPORTS THE OWNER, AND IT IS CHECKABLE

> **An MT4 INDICATOR cannot place orders. Only an EXPERT ADVISOR or a SCRIPT can.**

`!sm_WorkTime_v1.5b` is an **indicator** (`#property indicator_chart_window` family; it draws
objects and raises alerts). ⭐ **And V21 calls the Trainer a SCRIPT** — `[00:41:49]` *"four
**scripts** in there"*, and `[00:26:52]` *"the one I recommend using is by order percent"*.

⭐ **So the owner's *"it just doesn't have the auto-places"* is not a vague hand-wave — it names a
REAL AND CATEGORICAL DIVISION IN THE MT4 PROGRAM MODEL.** The level geometry belongs to an
indicator; the order placement belongs to a script. **A tool that draws the levels and a tool that
fires the orders are different MT4 program types by necessity, not by choice.** That is exactly the
division the owner describes, and it is verifiable independently of anyone's memory.

---

## 4. ⚠️ WHERE THE OWNER'S CLAIM DOES **NOT** CHECK OUT, AND THIS FILE SAYS SO

⛔ **The pip offsets do not match. The Trainer is `+20` / `+40`; the ribbon is `+25` / `+50`.**

That is not a rounding difference — it is a **25% divergence on every level**, and `A-141`'s figures
come from V21's own screen. Two readings survive and **neither is adopted**:

| Reading | Consequence |
|---|---|
| **(a)** *"Embedded"* means **the same idea**, re-parameterised — the ribbon is a **structural analogue**, not the Trainer's code | Most consistent with the evidence. The Trainer remains **absent**; what exists is a tool of the same family |
| **(b)** *"Embedded"* means **the same code**, and one of the two number-pairs is misremembered or belongs to a different variant (`A-141` records **four** variants) | Possible — but it requires the owner's or V21's figures to be wrong, and **nothing here decides that** |

⚠️ **`D-030` bars picking one.** The correction below states the *partial match* as fact and leaves
the *identity* question open, because the numbers are the only hard evidence and they disagree.

⚠️ **A second, smaller mismatch:** the ribbon's offsets hang off the **"blue box"** (the Asian
session box). ⛔ **`A-141` never says the Trainer's `+20`/`+40` hang off a session box at all** — V21
describes a market order plus two pendings, which could be anchored to the *fill price*, not to a
session extreme. **If the Trainer's grid is anchored to the entry rather than to a session high/low,
the resemblance is weaker than it first looks**, and §6 Q2 asks.

⚠️ **A third check, run and negative:** `Sessions.mq4` / `Sessions (1).mq4` — the *other* session
indicator in the project materials (KimIV's `i-Sessions`) — was also re-examined. **It has session
boxes and NOTHING else** — no pip offsets, no alerts, no orders. **If the owner means "the sessions
indicator" generically, `!sm_WorkTime_v1.5b` is the only candidate that matches at all.**

---

## 5. ⭐ THE PROPOSED CORRECTED RECORD

> ### `A-141` — the `High / Low Trainer` script is described, installed on camera, and NOT PRESENT — ⚠️ **BUT ITS LEVEL-TRACKING HALF HAS A WORKING ANALOGUE IN THE PROJECT**
>
> **Opened:** 2026-08-15 (V21). **Amended:** 2026-08-15 on owner attestation. **Status: OPEN.**
>
> *(Original text retained unedited per `REMEDIATION_PROTOCOL.md` §2.)*
>
> ⭐ **AMENDMENT — the owner attests:** *"The high low trainer is part of the sessions indicator.
> It's embedded in it. It just doesn't have the auto-places."*
>
> **This record's original *"total void"* framing is CORRECTED. It is a PARTIAL MATCH with a
> specific, nameable missing piece:**
>
> | | |
> |---|---|
> | ⭐ **PRESENT**, in `!sm_WorkTime_v1.5b` (md5 `b938ee1df8cf16a44bc16db71795e9f2`) | session **high/low tracking**; **fixed pip offsets** from that extreme, shipped as the alerts *"25/50 Pips above/below blue box"*; **alerting** at those levels |
> | ⛔ **ABSENT** | **all order placement** — market order, the two pendings, the hard stop, the `+30` take profit, the `30+50+70` cycle, the `MAX RISK 5%` / by-order-percent risk dial, and the four variants |
> | ⚠️ **DIVERGENT** | the Trainer's offsets are **`+20` / `+40`**; the ribbon's are **`+25` / `+50`** |
>
> ⭐⭐ **The missing piece is CATEGORICAL, not incidental: an MT4 INDICATOR CANNOT PLACE ORDERS —
> only an EA or a SCRIPT can — and V21 calls the Trainer a *"script"* (`[00:41:49]`).** The owner's
> *"it just doesn't have the auto-places"* therefore names a real division in the MT4 program model:
> **the levels belong to an indicator, the orders to a script.**
>
> ⛔ **WHAT THIS DOES NOT DO.** The Trainer is **still not in this repository** and `D-030` still
> bars reconstructing it. ⚠️ **The `+20`/`+40` vs `+25`/`+50` divergence means the ribbon is
> demonstrably NOT the Trainer's code at the Trainer's settings** — it is a **structural analogue**.
> Whether *"embedded"* means the same code re-parameterised, or the same idea in a sibling tool, is
> **not decided here**. ⚠️ It is also **unestablished that the Trainer's grid hangs off a session
> extreme at all** — V21 describes pendings relative to an order, which may not be the ribbon's
> anchor.
>
> ⭐ **WHAT IT CHANGES IN PRACTICE.** `A-141` no longer reads as *"nothing to work from."* The
> shortfall is now **specific**: what is missing is an **order-placement layer** over a level
> geometry the project already has a working implementation of
> (`06_MANUAL_BACKTEST/tools/MMM_SESSION_RIBBON.txt`, itself a draft). ⛔ **This is NOT a licence to
> build that layer** — `D-030`, and the entry trigger, fill logic and exit management remain
> unstated. **It localises the gap; it does not fill it.**
>
> **Related:** `A-056` (*Hi-Lo*, the untaught entry method this tool automates); `D-056` (the ribbon's
> admission, a draft); `D-058` (the owner's entry rule, whose tier 3 is the only other order-type
> statement in the project); `D-045` rule 2 — **admission is not reading.**

---

## 6. QUESTIONS FOR THE OWNER

1. ⭐⭐ **`+20`/`+40` or `+25`/`+50`?** §4 — V21's screen says the Trainer used `+20`/`+40`; your
   ribbon alerts are `+25`/`+50`. **Which does the Trainer actually use** — and is the difference a
   setting you changed, or two different tools?
2. ⭐ **Are the Trainer's two pendings measured from the SESSION HIGH/LOW, or from the entry/fill
   price?** §4 — the ribbon's offsets hang off the Asian box. If the Trainer's hang off the order,
   the resemblance is much weaker than it looks.
3. **Do you still have the four scripts?** `A-141` records *"four scripts in there"* and
   *"by order percent"* as the recommended one. ⭐ **A copy of any of them would move `A-141` from
   OPEN to closable** — it is the single highest-value artifact for this record, in the way
   `PivotPoints.mq4` is for `A-101`.
4. **By *"the sessions indicator"* do you mean `!sm_WorkTime_v1.5b`** (the one on `MMM.tpl`), or a
   different one? §4's third check found the only other session indicator in the materials —
   KimIV's `Sessions.mq4` — has **no** pip offsets at all.

---

## 7. ⚠️ DOES `MMM_SESSION_RIBBON.txt` NEED RE-CHECKING OR UPDATING?

**Re-checked. It needs a cross-reference, not a rewrite** — and it already implements the relevant
half.

| | |
|---|---|
| ✅ **Already implements the level geometry** | The `show25` / `show50` inputs draw lines at **±25 and ±50 pips from the Asian box high/low** — the direct port of `Alert25BlueBox` / `Alert50BlueBox` |
| ✅ **Already defaults them OFF** | Matching `MMM.tpl`, which saves both `false`. **Correct and unchanged** |
| ✅ **Already refuses to treat them as a course rule** | Its own comment: *"NOT a course rule — `A-005` is blocked on `A-019`/`D-031`"* |
| ⭐ **ADDED by this correction** | A note recording that these bands are the **level-tracking half of `A-141`'s High/Low Trainer**, that the Trainer's own offsets are **`+20`/`+40`** and differ, and that **no order-placement layer may be added** |
| ⛔ **NOT added, and deliberately** | **No `+20`/`+40` option.** Adding one would put V21's Trainer numbers into a tool that replicates `MMM.tpl`, blending two artifacts — `SOURCING_HIERARCHY.md` §3.2's *"do not blend"*. If the owner answers Q1, the answer is implemented then, not now |

⭐ **The file was updated with exactly that note in this commit** — a comment block, no behaviour
change, defaults untouched.
