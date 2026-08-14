# DECISION DRAFTS — 2026-08-14

> ## ⛔ NOTHING IN THIS FILE IS A DECISION. NOTHING HERE IS ADOPTED.
>
> Six **drafts**, one per owner decision queued by `00_SYSTEM/GAP_AUDIT_2026-08-14.md` §6
> (`D1`…`D6` in that document's own numbering). Each is written out to the point where the owner
> can answer **yes / no / edit** and the approved text can be appended to `DECISIONS.md`
> unchanged.
>
> **No status here is `CLOSED`, `ADOPTED` or `ACTIVE`.** The `Status:` line inside each proposed
> ledger entry is the status the entry **would carry once approved** — it is part of the proposed
> text, not a claim about the present. Until the owner rules:
>
> - **`DECISIONS.md` is unchanged.** No `D-045`…`D-050` exists.
> - **No `A-xxx`, `C-xxx`, `I-xxx` or `REVIEW_INDEX.md` item changes status.**
> - **`A-084` remains an `ACTIVE BLOCKER`, `DO NOT CODE`.** `C-021` remains `UNADJUDICATED`.
>   `I-010` Q1 and Q2 remain `OPEN`. Items 36, 91, 157, 168, 179 remain open.
>
> **Prepared on branch `docs/decision-drafts`** per `D-038`'s branch-per-task rule. Note that
> `DECISIONS.md` and `SETUP_ISSUES.md` are **POLICY ledgers** under `D-038a` and are edited **on
> the integration branch only** — so the approved entries must be applied there, not merged from
> this branch. This file is a proposal document, not a ledger.
>
> **Numbering.** `D-044` is the highest existing entry. The drafts claim `D-045`…`D-050` in the
> order `D1`…`D6` below. If the owner approves only some, the survivors renumber contiguously
> before they are written, and the mapping is recorded in the `LOG.md` entry that applies them.

---

## CONTENTS

| Draft | Proposed ID | Subject | Ledger item | Audit § |
|---|---|---|---|---|
| **D1** | `D-045` | Is the owner's `!SM_TDI` MT4 template admissible, and at what tier? | `REVIEW_INDEX.md` item **157** | §3, §6 |
| **D2** | `D-046` | Adopt `EXCLUDED BY DECISION` as a third mastery disposition | item **36** | §6 |
| **D3** | `D-047` | `D-038a`'s mergeability premise is false: fix the consequence | item **91** (policy half) | §6 |
| **D4** | `D-048` | The general rule for **Tier 1 against itself**, and `C-021` under it | item **168** / `C-021` | §1d, §6 |
| **D5** | `D-049` | The forward-read precedent, clause (d) especially | item **179** | §6 |
| **D6** | `D-050` | `I-010` Q1 (FXCM winter probe) and Q2 (which clock states the `D-035` boundary) | `I-010` Q1/Q2 | §6 |

> **Not drafted, deliberately — M/W anatomy (`A-011`).** The audit's §1c and §7b(1) name **M/W
> formation anatomy** among the foundational undefined terms. The owner has advised that *"M/W
> anatomy is coming soon in one of the videos."* It is therefore **not a project gap requiring an
> owner decision** and no draft is written for it; it is expected to close through Tier 1 course
> content in an upcoming lesson, at which point `SOURCING_HIERARCHY.md` §3.1 runs in the ordinary
> way. A corresponding note has been added to the audit's vocabulary-status section. **`A-011`
> stays `OPEN` and `DO NOT CODE` in the meantime** — an expected future closure is not a closure,
> and `D-030` still forbids anticipating it.

---
---

# DRAFT D1 — Item 157: is `!SM_TDI` admissible, and at what tier?

**Proposed ID:** `D-045` · **Source:** audit §3 and §6 `D1`; `REVIEW_INDEX.md` item 157 (V13 R1
`N2`, ⬜ `PUT TO THE OWNER`) · **Records touched if approved:** `A-084`, `A-086`, `A-032`,
`A-039`, `SOURCING_HIERARCHY.md`

## The question being decided

> **Is the owner's `!SM_TDI` MT4 template (`Ultimate Blue.tpl`, md5
> `ea22c8cf527921cef072586b6fa28296`) admissible as evidence about the course's TDI construction,
> and at what tier — such that `RSI_Price_Line=2` / `RSI_Price_Type=0` (`MODE_SMA`) closes
> `A-084` at `k = 2`?**

What is in the file, verbatim:

```text
name=!SM_TDI
RSI_Period=21              RSI_Price=0            (0 = PRICE_CLOSE)
Volatility_Band=34         RSI_Price_Line=2       RSI_Price_Type=0   (0 = SMA)
Trade_Signal_Line=7        Trade_Signal_Type=0    (0 = SMA)
SharkFin_Upper_Level=63    SharkFin_Lower_Level=37
```

## Why it is on the owner's desk and not a session's

`A-084` is an `ACTIVE BLOCKER`. Three lessons have attacked it by three different routes and all
three failed: the **empirical** route (`PT-040` returned `MATERIAL` — 10.481 pp at `k = 5, t = 50`,
and 5.16 pp even at `k = 2`), the **spoken-identity** route (V13 `[00:54:51]`, defeated four ways
in `A-087`), and the corpus's **best spoken opportunity** (V14 `[00:44:45]`–`[00:44:56]`, defeated
five ways, the fifth added by V14 R1 — the student's question is phrased in the TDI's own
**published buffer names**, so affirming it affirms the vocabulary and not a construction). The
**legend** route is closed corpus-wide (`TDI_MMM <values>`, no parameter tuple) and **2,047 frames
across V12–V14 contain no properties dialog.** `A-093` converts this from bad luck into a
structural fact: the speaker answers what the indicator *feels like*, never what it computes.

The template is an **evidence class with no tier and no admitting decision** — `MMM_TDI.txt` says
so itself — and `D-039` required an explicit owner attestation before the Mauro PDF could close
anything. A lesson session may not admit an evidence class on its own authority.

## Options considered, with the audit's own tradeoffs

| # | Option | For | Against |
|---|---|---|---|
| **1** | **Admit it now, at full weight — `A-084` closes at `k = 2`** | `A-084` closes on an arm `PT-040` has already measured; V11's entire RSI threshold family unblocks (the 50 bias baseline, 80/40, 60/20, 80/20, the 38–42 pullback band, both divergence forms, the `[00:36:19]` composite); probably carries `A-086`'s `Volatility_Band=34` — a period **the corpus has never stated anywhere** — and firms `A-032`'s 63/37. **Costs one decision** | The template is dated **2016/2019** against a **2012** course. **The corroborated fields and the load-bearing field are not the same fields:** V13 frame `00:53:35` (2012, Tier 1, instructor's own chart) corroborates `63`/`37` and the `21`; it does **not** corroborate `RSI_Price_Line=2`. Full-weight admission would gloss that |
| **2** | **Keep waiting for a course-verified answer** | The evidentiary standard stays clean; nothing closes on a 2016 file | The remaining routes are three and **two are empirically dead**; the third is **structurally** weak, not merely untried. `A-084` stays an `ACTIVE BLOCKER` and the TDI is a *required* entry criterion the course has never taught (`A-039`). And a fourth possibility — smoothing outside the swept simple-MA family (EMA, Wilder) — would make even `PT-040`'s `M` the wrong quantity; `PT-040` §6 names it and does not cover it. **The template answers that; waiting does not** |
| **3 ⭐** | **Admit it as a NEW, EXPLICITLY-TIERED evidence class, closing `A-084` PROVISIONALLY at `k = 2` with the dating weakness recorded at the closure** | Unblocks the downstream work now, keeps the weakness visible, gives the class a **tier** so the next artifact does not re-litigate it, and leaves any future Tier 1 statement free to overturn it under `D-040` §3.1 — the mechanism the project already has for exactly this | It is still a 2016 file answering a 2012 question, and a `PROVISIONAL` label is only as good as the re-check obligation attached to it |

## Recommended default — the audit's own

**Option 3.** The audit names it as *"a middle option [that] exists and should be named"* (§3d) and
Step 1 of §8 recommends ruling it in provisionally with a named tier and the 2016-vs-2012 weakness
recorded at the closure. The V14 reviewer, writing independently and before the audit: *"ruling on
`!SM_TDI`'s admissibility is the high-probability one, and it costs one owner decision rather than
seven more lessons."*

---

## PROPOSED LEDGER ENTRY — write to `DECISIONS.md` only on approval

```markdown
## D-045 — The owner's `!SM_TDI` MT4 template is admitted as a NEW TIERED EVIDENCE CLASS, and `A-084` closes PROVISIONALLY at k = 2

**Date:** 2026-08-14
**Decision:** Two parts, and the second does not follow from the first without it.

**Part 1 — the evidence class.** The owner's own MT4 platform artifacts, supplied by the owner and
attested by the owner as his working configuration for this method, are admitted as a named
evidence class: **`TOOLING — OWNER-ATTESTED PLATFORM ARTIFACT`**. It ranks **below Tier 1 and above
`[DEFAULT]`** in `SOURCING_HIERARCHY.md`, exactly as `D-042` already does for owner colour
attestations. Admission is **per-artifact**, as `D-039` is per-document: this entry admits
`Ultimate Blue.tpl` / `!SM_TDI` (md5 `ea22c8cf527921cef072586b6fa28296`) and nothing else.
A citation from this class carries the tag **`[TOOLING]`** with the artifact name.

**Part 2 — what it closes, and how weakly.** `RSI_Price_Line=2` with `RSI_Price_Type=0`
(MT4 `MODE_SMA`) states that the plotted green line is `SMA(2)` of `RSI(21)`. **`A-084` closes
`PROVISIONALLY RESOLVED — TOOLING` at `k = 2`**, and the closure carries, in the record itself,
the weakness in Part 3. `A-084`'s `ACTIVE BLOCKER` status is lifted **to the extent of `k`, and no
further**: V11's RSI threshold family (the 50 bias baseline, 80/40, 60/20, 80/20, the 38-42
pullback band, both divergence forms, the `[00:36:19]` composite) is unblocked **as against
`A-084`** and remains subject to every other blocker it carries.

**Part 3 — the weakness, stated at the closure and not glossed.** The template is dated **2016 and
2019**; the course was recorded in **2012**. V13 frame `00:53:35` — a 2012, Tier-1,
instructor's-own-chart datum — carries the template's **non-default** `63`/`37` pair, and the audio
ties `37` to the shark fin (`[00:51:09]`); the public Dean Malone TDI ships 68/50/32, so this is
**not** the public default. `RSI_Period=21` matches `A-080`'s Tier-1 closure exactly. **But
`RSI_Price_Line=2` — the one field that answers `A-084` — is NOT among the corroborated fields.**
The corroboration establishes that the template is of this lineage and plausibly this
instructor's; it does not establish the load-bearing value. Any artifact relying on `k = 2` cites
this decision and inherits this paragraph.

**Reason:** `A-084` is an `ACTIVE BLOCKER` on a *required* entry criterion the course has never
taught (`A-039`), and three lessons have now attacked it by three routes and failed. The legend
route is closed corpus-wide; 2,047 frames across V12-V14 contain no properties dialog; and
`A-093` shows the spoken route is structurally weak rather than merely untried — the speaker
answers what the indicator feels like, never what it computes. `PT-040` measured the cost of
guessing at **10.481 pp** at `k = 5, t = 50` and **5.16 pp** at `k = 2`, concentrated at `t = 50`,
V11's bias baseline. Waiting is not free and is not likely to work; and a fourth possibility -
smoothing outside the swept simple-MA family — would make even `PT-040`'s `M` the wrong quantity,
which the template answers and waiting does not.

**Evidence:** `06_MANUAL_BACKTEST/tools/MMM_TDI.txt` and `Ultimate Blue.tpl` (branch
`feature/tradingview-mmm-indicator`, **unmerged** — re-verify against the merged tree before
citing); V13 frame `00:53:35` and `[00:51:09]`; `A-080`; `PT-040` and its pre-registered
2 pp / 5 pp decision rule; `A-084`, `A-087`, `A-093`; `REVIEW_INDEX.md` item 157 (V13 R1 `N2`);
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §3. Owner attestation, 2026-08-14, that the template is his
own working configuration for this method.

**Alternatives considered:** *Admitting it at full weight and closing `A-084` outright* — rejected;
the dating gap is real and the corroborated fields are not the load-bearing field, so a
non-provisional closure would assert more than the evidence carries. *Continuing to wait for a
course-verified answer* — rejected on the record above; two of the three remaining routes are
empirically dead and the third is structurally weak, and the cost is up to seven more lessons with
a low prior. *Admitting the artifact without giving the class a tier* — rejected; an untiered
admission is re-litigated by the next artifact, which is the failure `D-040` was written to end.
*Closing `A-086`'s band period on `Volatility_Band=34` in this entry* — **rejected, and this is the
`D-039` caution repeated: admitting a source is not reading it against a record.** `A-086` is
**eligible** and is not closed here; a session that does the reading closes it, or does not.

**Consequences:**

1. `SOURCING_HIERARCHY.md` gains the `TOOLING` rung, its per-artifact admission rule, and a
   pointer to this entry. `EXTERNAL_REFERENCE/README.md`'s default is untouched.
2. **`A-084` moves to `PROVISIONALLY RESOLVED — TOOLING`, `k = 2`**, with Part 3 quoted in the
   record. It does **not** become `RESOLVED BY COURSE`.
3. **The re-check obligation of `SOURCING_HIERARCHY.md` §3.4 attaches to `A-084`**, and `A-084`
   joins `A-014`, `A-023` and `A-020` on that list. **A later Tier 1 statement overturns this
   under `D-040` §3.1**, and any session reaching a lesson that shows a TDI properties dialog,
   a Navigator panel or a smoothing length must run §3.1.
4. **`A-086` (`Volatility_Band=34`) and `A-032` (63/37) become ELIGIBLE and are NOT closed here.**
   Each needs a session that reads the artifact against the record and cites it.
5. **Nothing else is unblocked.** `A-085` is a mechanism claim with no construction and is
   untouched. `A-039` stays open on the TDI as a taught entry criterion. `D-030` is untouched.
6. Every `PT` or `BT` artifact that uses `k = 2` states in its own pre-registration that the value
   is `TOOLING`-tier and provisional, so a later overturn is traceable to the runs it affected.

**Status:** ACTIVE — `A-084`'s closure under it is PROVISIONAL
```

---
---

# DRAFT D2 — Item 36: adopt `EXCLUDED BY DECISION`

**Proposed ID:** `D-046` · **Source:** audit §6 `D2`; `REVIEW_INDEX.md` item 36 — **ruled at V05 R1
on 2026-08-11, `OPEN` only on the owner's adoption step**, restated at V06, V07 ×2, V08, V09, V10
· **Records touched if approved:** `D-018`, `D-019`, `MASTERY_STANDARD.md`, V05 dimensions B and G

## The question being decided

> **Does the project adopt a third mastery disposition, `EXCLUDED BY DECISION`, for work whose
> subject matter exists but is permanently barred by a numbered decision?**

## Why the existing two do not fit

`D-019`'s table grants exactly two, and **V05 is a case neither contemplates**: it *states* several
testable-shaped rules and they are **withheld by decision**.

- `NOT APPLICABLE` says *there was never anything here.* **False — there is an hour of it.**
- `DEFERRED` says *this becomes possible later.* **False — no future lesson makes a V05 guest rule
  testable.**

The V05 R1 reviewer **upheld the escalation** and recommended adoption. The consequence of leaving
it open is concrete: mastery **dimension B** has been carried un-graded or `NOT SATISFIED WITH NO
SEVERITY CHARGE` for **six-plus consecutive lessons**, because the project has no vocabulary for
its actual state — and reviewers keep saying, correctly, that charging it would penalise the very
`D-030` discipline the project mandates. **This is a vocabulary gap in the project's own standards,
not a defect in any lesson.**

## Options considered

| # | Option | For | Against |
|---|---|---|---|
| **1 ⭐** | **Adopt `EXCLUDED BY DECISION`, available to any dimension** | The reviewer's own recommendation; costs one sentence; un-sticks a dimension mis-labelled for six lessons; the exclusion becomes **auditable** (it names *what* and *under which decision*) rather than invisible | A third label is a third thing to get wrong; needs a hard rule that it is unavailable without a citable numbered decision |
| **2** | **Widen `NOT APPLICABLE` to cover excluded work** | No new vocabulary | Makes `D-018`'s eligibility test false on its face and re-opens the exact confusion `D-019` was written to end |
| **3** | **Leave it open** | Nothing changes | Dimension B stays mis-labelled for V15–V21 too, and the item takes a seventh escalation. **It is the oldest unpaid item in the file** |

## Recommended default — the audit's own

**Option 1.** Audit §8 Step 2: *"a one-sentence vocabulary adoption on its sixth escalation, and it
un-sticks a mastery dimension that has been mis-labelled for six lessons."*

---

## PROPOSED LEDGER ENTRY — write to `DECISIONS.md` only on approval

```markdown
## D-046 — `EXCLUDED BY DECISION` is adopted as a third mastery disposition, available to any dimension

**Date:** 2026-08-14
**Refines:** `D-018` and `D-019`, both of which remain `ACTIVE` and neither of which is superseded.
`D-019`'s two-row table becomes three rows.
**Resolves:** `18_REVIEW/REVIEW_INDEX.md` open item **36**, ruled at V05 R1 on 2026-08-11 and open
since then **only on this adoption step**.

**Decision:** A mastery dimension may be recorded as **`EXCLUDED BY DECISION`** when **all four**
hold:

| # | Condition |
|---|---|
| 1 | **Subject matter exists.** The lesson supplies material the dimension would otherwise grade. This is what separates it from `NOT APPLICABLE`. |
| 2 | **The work is permanently barred by a numbered decision in this file**, and **the decision is cited by number in the report.** An exclusion with no citable decision is not available — the disposition is `DEFERRED`, or the work is done. |
| 3 | **No future lesson can lift the bar.** This is what separates it from `DEFERRED`. Where a future lesson *could* lift it — a definition the course has not yet given — the disposition is `DEFERRED` and `D-030` governs. |
| 4 | **The record states WHAT was excluded**, specifically enough that a reader can see the size of the hole. |

**Effect:** the item **closes like `NOT APPLICABLE` and accrues no debt** — it is not carried in
`REVIEW_INDEX.md` as open research — **and, unlike `NOT APPLICABLE`, it is a positive statement
that material was withheld.** It is available to **any** dimension, not only F and G.
`EXCLUDED BY DECISION` is **not a pass**; it is a claim the reviewer audits like any other, and a
reviewer who finds the cited decision does not in fact bar the work returns `REVISE` with the
dimension reinstated.

`D-019`'s table, as amended:

| Disposition | Meaning | Effect | Who can grant it |
|---|---|---|---|
| `NOT APPLICABLE` | The lesson supplies **no subject matter** | Closed permanently | `D-018`, dimensions F and G only |
| `DEFERRED` | Subject matter exists; a prerequisite is missing and **may arrive** | Stays open, carried in `REVIEW_INDEX.md` | Any dimension |
| **`EXCLUDED BY DECISION`** | Subject matter exists; the work is **permanently barred by a numbered decision**, which is cited | Closed; **no debt accrues**; the exclusion is auditable | **Any dimension**, subject to reviewer audit |

**Reason:** V05 forced it and five later lessons have restated it. V05 states several
testable-shaped rules that are withheld by `D-025`. `NOT APPLICABLE` asserts there was never
anything there, which is false — there is an hour of it. `DEFERRED` asserts the work becomes
possible later, which is also false — no future lesson makes a V05 guest rule testable. With
neither label fitting, mastery dimension **B** has been carried un-graded or
`NOT SATISFIED WITH NO SEVERITY CHARGE` for **six-plus consecutive lessons**, and reviewers have
correctly declined to charge it, because charging it would penalise the `D-030` discipline the
project mandates. **The gap is in the project's own standards, not in any lesson's understanding.**

**Evidence:** `REVIEW_INDEX.md` item 36 and its V05 R1 ruling (2026-08-11), which **upheld** the
escalation and recommended this adoption in these terms; restatements at V06, V07 (x2), V08, V09,
V10, each *"restated, not re-counted"*; `V05_MASTERY_REPORT.md` § F, G and Escalation;
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §5b, §6 `D2`, §7a.

**Alternatives considered:** *Widening `NOT APPLICABLE`* — rejected; it makes `D-018`'s own
eligibility test false and re-creates the confusion `D-019` exists to end. *Using `DEFERRED` and
letting the debt sit forever* — rejected; a debt that can never be discharged is not a debt, it is
a permanently misleading open item. *Leaving it open* — rejected; the ruling is fourteen weeks
of escalations old and costs one sentence.

**Consequences:**

1. `MASTERY_STANDARD.md` and the mastery report template gain the third disposition and the
   four-condition test. `REVIEW_PROTOCOL.md` gains the reviewer's audit of it.
2. **V05 dimensions B and G take `EXCLUDED BY DECISION`, citing `D-025`**; **dimension F stays as
   graded** (`SUCCESS AFTER SOURCE REVIEW`) — it correctly refused `NOT APPLICABLE` because the
   assignment is partly performable and the performable part was performed.
3. **Dimension G's reason changes from *"states no testable rule"* to *"states rules excluded by
   `D-025`"***, so V06-V21 do not inherit the wrong precedent — this was the V05 R1 ruling's
   specific requirement.
4. **No grade, verdict or gate state changes by operation of this entry**, and **no lesson is
   re-reviewed on account of it.** Re-labelling a disposition is not re-grading. Where an earlier
   report used a disposition this entry would have changed, the report is annotated in place per
   `REMEDIATION_PROTOCOL.md` §2 and the superseded text stays visible.
5. **It creates no new licence to exclude.** Condition 2 is the whole guard: **no numbered
   decision, no exclusion.** A session that cannot name the decision has not found a third
   disposition, it has found work it has not done.

**Status:** ACTIVE
```

---
---

# DRAFT D3 — Item 91: `D-038a`'s mergeability premise is measurably false

**Proposed ID:** `D-047` (alternative: `D-038b`, on the `D-038a` precedent for an entry that
clarifies rather than stands alone — **owner's choice; `D-047` is proposed** because this one
*corrects a premise* rather than clarifying a rule) · **Source:** audit §6 `D3`;
`REVIEW_INDEX.md` item 91, policy half, 🔶 `OPEN` · **Records touched if approved:** `D-038a`

## The question being decided

> **`D-038a` classifies `REVIEW_INDEX.md` as an evidence ledger on the ground that "evidence
> ledgers are append-only and their additions are `git`-mergeable by construction." They are not.
> What replaces that premise?**

## The evidence — a measurement, not an argument

The `review/v10` → integration merge **conflicted in three files**: `REVIEW_INDEX.md` (3 hunks),
`LOG.md` (2 hunks), `COURSE_PROGRESS.md` (1 hunk) — **every one of them a file `D-038a` calls
mergeable.** Both branches appended to the same table tails, so git could not order them, and
`LOG.md`'s conflict **interleaved two session entries**, splicing one session's
Decision/Files/Git blocks into the middle of another's. Separately and earlier, two branches
allocated open items **81–85** and **81–83** concurrently — git cannot detect that at all, because
the two branches append to different regions of the same file.

`D-038a`'s safety evidence re-derived `A-`, `C-` and `Q-` identifier sets after the V08 merge.
**Open-item numbers were not in that check, and they are the one series in the list that is not
mergeable by construction.**

## Options considered

| # | Option | For | Against |
|---|---|---|---|
| **1 ⭐** | **Keep the policy/evidence split; replace the false premise with two explicit consequences — integration-allocated open-item numbers, and single-threaded merge-back for tail-appended ledgers** | Targets the measured failure exactly; `PT-036` §0 already does the same for `PT` numbers, so it is a pattern the project has run successfully; costs one amendment | Adds a merge-ordering constraint that a concurrent session must respect |
| **2** | **Reverse `D-038a` — move the evidence ledgers back to integration-only** | No conflicts by construction | Rejected once already, on the record: it forces every isolated session to reach across to the integration branch mid-work — re-introducing the shared write path `D-038` exists to remove — or to defer its own records to a later session, which is worse |
| **3** | **Leave it** | Nothing changes | **The risk grows with concurrency and this project runs concurrent sessions by design.** The last occurrence cost a hand-repaired three-file conflict and a spliced `LOG.md` entry |

## Recommended default — the audit's own

**Option 1.** Audit §6 `D3`: *"`D-038a` gains an explicit consequence that `REVIEW_INDEX.md`
open-item numbers are allocated against the integration branch's state … and that tail-appended
ledgers require a single-threaded merge-back."* A reviewer cannot amend a `DECISIONS.md` entry;
only the owner can.

---

## PROPOSED LEDGER ENTRY — write to `DECISIONS.md` only on approval

```markdown
## D-047 — `D-038a`'s mergeability premise is CORRECTED: tail-appended evidence ledgers are NOT mergeable by construction, and two consequences attach

**Date:** 2026-08-14
**Amends:** `D-038a`, **its stated reason only.** `D-038a`'s operative split — POLICY ledgers on
the integration branch, EVIDENCE ledgers on the task branch with the work — is **kept unchanged
and is not superseded.** `D-038` is untouched.
**Resolves:** `18_REVIEW/REVIEW_INDEX.md` open item **91**, policy half. The numbering instance was
discharged mechanically at merge-back (V10's items renumbered 86-90) and is not reopened.

**Decision:** `D-038a`'s premise that *"evidence ledgers are append-only and their additions are
`git`-mergeable by construction"* is **false as stated, and is withdrawn.** Append-only makes a
ledger **conflict-tolerant**, not conflict-free: two branches appending to the **same tail** of the
same table produce a conflict git cannot order, and two branches allocating from the **same number
series** produce a collision git cannot see. Both have happened in this project. `D-038a`'s split
stands on its remaining and sufficient ground — **an isolated session's evidence must travel with
the work that produced it, and the alternative re-introduces the shared write path `D-038` exists
to remove** — and gains two consequences:

**Consequence A — identifier allocation is against the INTEGRATION branch.** Every project-wide
number series — `REVIEW_INDEX.md` **open-item numbers**, `A-`, `C-`, `Q-`, `PT-`, `BT-`, `I-` — is
allocated against **the latest integration branch's state**, never against the task branch alone,
and is **re-checked at merge-back**. This is what `PT-036` §0 already does for `PT` numbers; it is
now general. The merging session renumbers the later arrival and fixes its cross-references, and
**discloses the renumbering in the merge rather than absorbing it.**

**Consequence B — tail-appended ledgers merge single-threaded.** `LOG.md`,
`00_SYSTEM/COURSE_PROGRESS.md` and `18_REVIEW/REVIEW_INDEX.md` are **tail-appended** ledgers: their
additions land at the end of the same table or status block every time. Merge-back of any branch
touching them is **single-threaded** — one branch merges to integration at a time, completely,
before the next begins — which `D-038` already requires and this entry makes explicit for these
three files by name. A session that must wait, waits; it does not merge in parallel and repair
afterwards.

**Consequence C — `REVIEW_INDEX.md` merges promptly.** Unchanged from `D-038a` obligation 2 and
restated because B makes it sharper: its gate rows govern whether the next lesson may start, and a
verdict left unmerged holds a gate closed that is actually open.

**Reason:** The premise was tested and failed, and the test is direct rather than argumentative.
The `review/v10` -> integration merge **conflicted in three files** — `REVIEW_INDEX.md` (3 hunks),
`LOG.md` (2 hunks), `COURSE_PROGRESS.md` (1 hunk) — **every one of them a file `D-038a` names as
mergeable.** `LOG.md`'s conflict **interleaved two session entries**, splicing the V09 R2 entry's
Decision/Files/Git/Next-Action sections into the middle of the V10 R1 entry's fenced Decision
block: a silent corruption of the project's own audit trail, caught only because a human resolved
the conflict by hand. Separately, `video/v10` allocated open items **81-85** while the integration
branch concurrently allocated **81-83** to V09 R2. `D-038a`'s own safety evidence re-derived `A-`,
`C-` and `Q-` sets after the V08 merge and **did not check open-item numbers**, which are the one
series in its list that is not mergeable by construction. **The risk grows with concurrency, and
this project runs concurrent sessions by design.**

**Evidence:** `18_REVIEW/V10/V10_REVIEW_R1.md` `M1` and its RENUMBERING DISCLOSURE; the
`review/v10` -> integration merge commit's own conflict set; `REVIEW_INDEX.md` item 91;
`D-038a`'s reason paragraph and its safety-evidence paragraph; `PT-036` §0;
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §6 `D3`.

**Alternatives considered:** *Reversing `D-038a` and returning the evidence ledgers to
integration-only* — rejected on `D-038a`'s own reasoning, which this entry does not disturb:
it forces an isolated session to reach across mid-work or to defer its own records to a session
that did not do the work. *Leaving the premise in place and treating the V10 merge as bad luck* -
rejected; it happened twice in different forms and the second form corrupted a `LOG.md` entry.
*Locking `REVIEW_INDEX.md` numbering behind a tool* — **not rejected, deferred**: a validator
check that no open-item number appears twice is cheap and would enforce Consequence A
mechanically. Recorded as a follow-up, not required by this entry.

**Consequences:** `D-038a` gains a pointer to this entry; **its text is not edited**, per this
file's append-only rule. `D-038`'s merge-back paragraph gains the three named files.
`scripts/validate_project.py` may add a duplicate-open-item-number check. No branch, merge or
ledger row already made is invalidated by this entry.
**Status:** ACTIVE
```

---
---

# DRAFT D4 — Item 168 / `C-021`, and the general rule behind it

**Proposed ID:** `D-048` · **Source:** audit §1d, §6 `D4`; `REVIEW_INDEX.md` item 168 (V14 student,
forwarded **unchanged** by V14 R1); `C-021` · **Records touched if approved:** `C-021`, `A-086`,
`C-017`, `SOURCING_HIERARCHY.md`

## The question being decided

Two, and the audit is explicit that the second is worth more than the first:

> **(a) `C-021` — the TDI volatility bands' basis. V12 `[00:15:47]`–`[00:16:20]` retracts it to
> the RSI line under a chat correction; V14 `[00:45:09]` states it back as the market base,
> unhedged and unprompted, one week later; and Tier 2 (`MMM-NOTES` p.45) sides with V14. Which
> stands?**
>
> **(b) ⭐ What is the STANDING rule when Tier 1 contradicts itself?**

`SOURCING_HIERARCHY.md`'s *"the recording wins"* **presupposes a recording that is clear.** It
ranks *sources*, not two things one speaker said. The class has now arisen **three times** —
`C-017` (printed vs spoken, item 88), `C-021` (Tier 1 vs Tier 1 one week apart), and the
`D-041`/`D-043` family — and has consumed **two owner rulings and one reversal**. **It will arise
again.**

## Options considered

### On (b), the general rule

| # | Option | For | Against |
|---|---|---|---|
| **1 ⭐** | **A standing tie-break ladder, with owner adjudication as the last rung** | Retires a recurring stoppage; most instances resolve without an owner ruling; the residue that reaches the owner is genuinely irreducible | Any ladder encodes a preference that will occasionally be wrong |
| **2** | **Owner adjudicates every instance, as with `D-041`/`D-043`** | Never encodes a wrong preference | Three instances, two rulings and a reversal already; and the reversal shows owner rulings are themselves revisable, so this does not buy certainty either |
| **3** | **Leave unruled; each contradiction stays `UNADJUDICATED`** | Zero risk of adopting the wrong statement | The register grows, `A-086` is *"out of date whichever way this is decided"*, and each new instance costs a session's deliberation to reach the same non-answer |

### On (a), `C-021` specifically — the three readings `C-021` §4 states and adopts none of

| Reading | Argument | Against |
|---|---|---|
| **V14 wins** — later, unhedged, unprompted, Tier 2 corroborates | The speaker's standing position is his latest confident one | Confidence is not accuracy, and V12 `[00:15:40]` *"I don't know the math on it"* applies to V14's sentence too |
| **V12 wins** — it was corrected on the record (`[00:16:20]` *"Thank you"*) | Someone supplied a correction he accepted | The corrector is unidentified, and Dean Malone's shipped TDI **does** build the bands on the RSI line — so the chat may have been right about the **public** build and wrong about **this altered one** (V12 `[00:07:20]`) |
| **Neither — the speaker does not know** | He says so, twice, in V12 | V14 carries no hedge, so *"he doesn't know"* is the project's inference, not his statement |

**⚠️ Whichever way (a) goes, it changes nothing operationally.** The bands stay unconstructible and
`A-086` stays `DO NOT CODE`, **because the period is never stated in Tier 1 or Tier 2.** A
multiplier and a basis do not build a band without a lookback. `A-031` and `A-032` stay
uncomputable. **A ruling on (a) buys clarity in the record, not an unblock.**

## Recommended default

**On (b): Option 1.** Audit §6 `D4`: *"One general rule retires a recurring stoppage; deciding
`C-021` alone does not."*

**On (a): the audit names no default, and this draft does not invent one.** Applying the proposed
ladder mechanically would select **V14** (later + unhedged, with independent Tier 2 corroboration)
— which is why the ladder's rung 4 exists: the owner may take the general rule and still rule
`C-021` differently, or decline (a) entirely and leave `C-021` `UNADJUDICATED` on the ground that
nothing turns on it.

---

## PROPOSED LEDGER ENTRY — write to `DECISIONS.md` only on approval

```markdown
## D-048 — TIER 1 AGAINST ITSELF: a standing tie-break ladder, and `C-021`'s disposition under it

**Date:** 2026-08-14
**Resolves:** `18_REVIEW/REVIEW_INDEX.md` open item **168**; the standing gap
`SOURCING_HIERARCHY.md` §3.3 leaves open; and, at Part 2, `C-021`.
**Does not disturb:** `D-039`, `D-040`, `D-030`, `D-025`/`D-033`, or `SOURCING_HIERARCHY.md`'s
between-tier rules. This entry governs **within Tier 1 only.**

**PART 1 — THE GENERAL RULE.** Where two Tier 1 statements conflict — printed against spoken, one
lesson against another, or one sentence against another in the same hour — `SOURCING_HIERARCHY.md`
§3.3's *"the recording wins"* does not apply, because both are the recording. A session applies
this ladder **in order** and **stops at the first rung that answers**, and **records which rung
answered**:

| Rung | Test | Outcome |
|---|---|---|
| **1** | **Is one statement a demonstrable misspeak, corrected by the same speaker in the same passage?** | The correction governs. Record both; note the correction. |
| **2** | **Does one statement carry a construction and the other only a characterisation?** A statement of *how a thing is computed* outranks a statement of *what it feels like or is built upon* (`A-093`) | The constructive statement governs. |
| **3** | **Is one statement unhedged, unprompted and LATER, with the earlier one hedged, prompted or retracted under correction?** | The later unhedged statement is the speaker's **standing position** — **but this rung records a POSITION, not a FACT.** Anything closed on it closes **`PROVISIONALLY RESOLVED — TIER 1 STANDING POSITION`**, never `RESOLVED BY COURSE`, and carries the conflicting statement in the record. |
| **4** | **Anything else — including any case where the rungs disagree, or where a rung would close a load-bearing record** | **DO NOT ADJUDICATE.** File/keep the `C-xxx`, keep the record `DO NOT CODE`, and put it to the owner. Owner adjudication sits **outside** the ladder, as `D-041` established it sits outside the tiers. |

**Three hard limits, and they are what makes the ladder safe:**

1. **The ladder never produces `RESOLVED BY COURSE`.** Only an *uncontradicted* Tier 1 statement
   does. A resolved internal conflict yields a **provisional** status at best.
2. **The `C-xxx` is never deleted or downgraded.** Both statements stay on the record, visible, per
   `REMEDIATION_PROTOCOL.md` §2. **A divergence is a finding about the corpus** — the same
   principle `SOURCING_HIERARCHY.md` §3.3 already states for Tier 1 vs Tier 2.
3. **Tier 2 corroboration is a tiebreaker input, never a warrant.** Where Tier 2 agrees with one
   arm it may be **noted** at rung 3, and it does not promote the outcome above provisional -
   `D-039`'s Tier 2 cannot outrank Tier 1, so it certainly cannot arbitrate between two Tier 1
   statements.

**PART 2 — `C-021`, ruled under Part 1.** [OWNER: SELECT ONE — this draft proposes none.]

> **(i) V14 governs.** Rung 3 answers: V14 `[00:45:09]` is later, unhedged and unprompted; V12's
> `[00:16:03]`-`[00:16:20]` position was reached under a chat correction and is the least
> confident statement in that lesson; Tier 2 (`MMM-NOTES` p.45) independently agrees. `A-086`'s
> basis is recorded **`PROVISIONALLY RESOLVED — TIER 1 STANDING POSITION`: the market baseline.**
> `C-021` moves to `RESOLVED — D-048 RUNG 3`, both statements retained.
>
> **(ii) V12 governs.** Rung 1 answers: the `[00:16:20]` *"Thank you"* is an accepted correction.
> `A-086`'s basis is the RSI line. `C-021` moves to `RESOLVED — D-048 RUNG 1`.
>
> **(iii) Neither — rung 4.** The speaker disclaims knowledge twice in V12
> (*"I don't really know because I didn't invent it"*), and this is a load-bearing record.
> `C-021` stays **`OPEN — UNADJUDICATED`**, `A-086` stays `DO NOT CODE`.

**AND IN EVERY CASE, INCLUDING (i) AND (ii): NOTHING IS UNBLOCKED.** **The bands' PERIOD is never
stated in Tier 1 or Tier 2**, so `A-086` stays `DO NOT CODE`, and `A-031`
(*"blood in the water"*) and `A-032` (*"shark fin"*) stay uncomputable. **A multiplier and a basis
do not build a band without a lookback.** This ruling settles the record; it does not settle the
indicator. Any session that reads Part 2 as an unblock has made the `D-039` error by another route.

**Reason:** The class has arisen **three times** — `C-017` (printed vs spoken, item 88), `C-021`
(Tier 1 vs Tier 1 one week apart), and the `D-041`/`D-043` EMA-nickname family — and has consumed
**two owner rulings and one reversal**, and `SOURCING_HIERARCHY.md` has no rule for it because it
ranks *sources*, not two things one speaker said in one hour. Both the V14 session and the V14
reviewer declined `C-021` and forwarded it unchanged, correctly, on the ground that it is neither
a session's nor a reviewer's call. **A general rule retires a recurring stoppage; ruling `C-021`
alone does not** — and the next instance is already predictable, because the corpus keeps
producing them.

**Evidence:** `C-021` in full, including §4's three readings and §5's operational note; `C-017`
and `REVIEW_INDEX.md` item 88; `D-041`, `D-042`, `D-043` and the reversal between them;
`SOURCING_HIERARCHY.md` §3.2 Case C and §3.3; `A-086`, `A-093`;
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §1d, §6 `D4`.

**Alternatives considered:** *Ruling `C-021` and nothing more* — rejected; it is the third instance
and would leave the fourth to another owner session. *Owner adjudication of every instance* -
rejected as the standing rule, and **retained as rung 4** for the instances that deserve it;
`D-043`'s reversal of `D-041` shows that routing everything to the owner does not by itself
produce correctness. *A pure "latest statement wins" rule* — rejected; it would have adopted
whichever EMA mapping was stated last and cannot see a misspeak, which rung 1 catches.
*Deleting the superseded `C-xxx` once a rung answers* — rejected outright; the divergence is
evidence about the corpus, and §3.3's principle applies unchanged.

**Consequences:** `SOURCING_HIERARCHY.md` gains a §3.5 stating the ladder and pointing here.
`C-021` and `A-086` take the Part 2 disposition **and no other record changes status** -
in particular `C-017` is **not** ruled by this entry; it becomes eligible for a session to apply
the ladder to it, which is a different act. **No `A-xxx` is unblocked and no test becomes
runnable.** `REVIEW_PROTOCOL.md` gains a check that a session claiming a rung names it.
**Status:** ACTIVE
```

---
---

# DRAFT D5 — Item 179: the forward-read precedent

**Proposed ID:** `D-049` · **Source:** audit §6 `D5`; `REVIEW_INDEX.md` item 179 (V14 R1), 🔷
`PUT TO THE OWNER — method precedent` · **Blocks:** item 176's second calendar gap
(`Wk9 052012` → `Wk10 061712`) is **currently blocked on this ruling**

## The question being decided

> **May a session read a not-yet-studied lesson's files, and under what conditions?**

V14 read a V15 file to settle a bibliographic fact. V14 R1's finding: **legitimate in kind,
unnecessary in fact, unverified in substance.**

- **In kind, it is not a boundary violation.** A bibliographic string check creates no V15
  artifact and engages neither `D-004` (the gate) nor `D-017` (ingestion).
- **It was not needed.** `SOURCE_MANIFEST.md` and the library tree already show
  `Wk5 041512` → `Wk7 050612` with no `Wk6` at all.
- **⭐ The real defect: the datum imported is UNVERIFIED.** The file read is a pre-ingestion
  supplied transcript of exactly the class `Q-008`…`Q-015` show to be fabricated in its headers —
  **its own header reads *"Course Position: Video 16 of 21"* and a *"Primary Topics"* line, the two
  fields `Q-015` §5 quarantines by name** — and the session applied `I-008` rigorously to V14's
  body and **none of it** to the V15 body it made load-bearing for `A-092`.

**No finding was charged**, because the manifest independently supports the conclusion. **The risk
did not bite here.**

## Options considered

| # | Option | For | Against |
|---|---|---|---|
| **1 ⭐** | **Adopt the four-clause test (a)–(d) as a standing precedent** | Keeps a legitimate, cheap capability; clause (d) closes the actual defect; **unblocks item 176's second calendar gap**, whose cheap decider is a forward read | Four clauses is four things to check; needs the disclosure to be at the point of use, not buried in a log |
| **2** | **Prohibit forward reads entirely** | Zero risk of doctrine leaking backwards | Costs the corpus a cheap calendar decider and would have forbidden a read that was, in form, harmless. The second calendar gap stays unexamined |
| **3** | **Permit them with disclosure only — clauses (a)–(c), drop (d)** | Simplest | **Drops the only clause that addresses what actually went wrong.** V14 satisfied (a)–(c) and failed (d) |

## Recommended default — the audit's own

**Option 1**, with the audit's emphasis: *"Clause (d) is the part worth making policy."*

---

## PROPOSED LEDGER ENTRY — write to `DECISIONS.md` only on approval

```markdown
## D-049 — A forward read of a not-yet-studied lesson is permitted under four cumulative conditions, and the fourth is the one that matters

**Date:** 2026-08-14
**Resolves:** `18_REVIEW/REVIEW_INDEX.md` open item **179**, raised by V14 R1 as a proposed
standing precedent. **Unblocks** item 176's second calendar gap.
**Does not disturb:** `D-004` (the progression gate), `D-002` (one lesson per session), `D-017`
(ingestion), `I-008` (unverified supplied transcripts). Nothing here permits **studying** a future
lesson.

**Decision:** A session may read files belonging to a lesson it is not studying — including a
lesson beyond the gate — **if and only if all four conditions hold. They are cumulative; failing
any one makes the read impermissible:**

| Clause | Condition |
|---|---|
| **(a)** | **It seeks a BIBLIOGRAPHIC fact** — a filename, a week label, a duration, a checksum, a spoken week number, an ordering. **Never doctrine, never a rule, never a value, never a definition.** A read that would answer an `A-xxx` is forbidden outright, whatever it finds. |
| **(b)** | **It is disclosed AT THE POINT OF USE** — in the artifact that relies on it, not only in `LOG.md`. A reader landing on the claim sees where it came from. |
| **(c)** | **No artifact, note or interpretation about the future lesson is created.** No `03_LESSON_NOTES/` entry, no screenshot index, no `A-xxx`, no mastery work. The read leaves no forward footprint. |
| **(d)** | ⭐ **The imported datum carries the SAME `I-008` VERIFICATION as any other evidence, or is labelled `UNVERIFIED` wherever it is used.** A supplied pre-ingestion transcript is not evidence merely because it is on disk. |

**Clause (d) is the operative one and the reason this entry exists.** V14's `D3` satisfied
(a)-(c) and **failed (d)**: the file it read is a pre-ingestion supplied transcript of exactly the
class `Q-008`...`Q-015` show to be fabricated in its headers — **its own header carries
*"Course Position: Video 16 of 21"* and a *"Primary Topics"* line, the two fields `Q-015` §5
quarantines by name** — and the session applied `I-008` rigorously to V14's own body and **none of
it** to the V15 body it made load-bearing for `A-092`.

**A fifth condition, implied by (a) and stated so it is not missed: PREFER THE INGESTED SOURCE.**
Where `SOURCE_MANIFEST.md`, the library tree or an already-studied lesson answers the question, the
forward read is **not permitted** — not because it is dangerous, but because it is unnecessary and
imports an unverified body for no gain. V14's `D3` failed this too: the manifest already showed
`Wk5 041512` -> `Wk7 050612` with no `Wk6`.

**Reason:** The capability is genuinely useful and genuinely cheap — the second calendar anomaly
(`Wk9 052012` -> `Wk10 061712`, a four-week jump with three missing weeks recorded nowhere) has a
forward read as its cheap decider, and that work is currently blocked on this ruling. Prohibiting
forward reads outright would forbid an act that is, in form, harmless: a bibliographic string check
creates no artifact and engages neither `D-004` nor `D-017`. But permitting them on disclosure
alone would leave untouched the thing that actually went wrong, which was not the boundary and not
the disclosure — **it was importing an unverified datum from a quarantined class and treating it as
established.** This project quarantined 72 files to avoid exactly that, and the hazard does not
change because the datum is bibliographic rather than doctrinal.

**Evidence:** `18_REVIEW/V14/V14_REVIEW_R1.md` § `D3` and `REVIEW_INDEX.md` item 179, which
proposed these four clauses; item 165; `A-092`; `SOURCE_MANIFEST.md`; `Q-015` §5 and
`Q-008`...`Q-015`; `I-008`; `COURSE_PROGRESS.md` V15 GATE (c);
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §6 `D5`, §7b.

**Alternatives considered:** *Prohibiting forward reads outright* — rejected; it forbids a
harmless and useful act and leaves the second calendar region unexamined. *Permitting on
disclosure alone, clauses (a)-(c)* — rejected; V14 satisfied all three and the defect survived
all three. *Charging V14 a finding retrospectively* — rejected and explicitly not done: V14 R1
charged nothing because the manifest independently supports the conclusion, and this entry is a
forward precedent, not a re-grading.

**Consequences:**

1. `STUDY_PROTOCOL.md` and both session prompts gain the four clauses and the prefer-the-ingested-
   source rule. `REVIEW_PROTOCOL.md` gains a check that a disclosed forward read names its clause
   (d) status.
2. **Item 176's second calendar gap is unblocked** and may be decided — by the manifest and the
   library tree first, and by a clause-compliant forward read only if those are silent, with any
   imported datum labelled `UNVERIFIED` wherever used.
3. **V14's `D3` is annotated, not reversed.** `A-092`'s conclusion stands on the manifest;
   the V15-sourced half is labelled `UNVERIFIED` at its point of use per clause (d).
4. **`I-008` is unchanged and is not weakened.** This entry extends its reach to imported data;
   it grants no exemption from it.

**Status:** ACTIVE
```

---
---

# DRAFT D6 — `I-010` Q1 and Q2: two clock questions

**Proposed ID:** `D-050` · **Source:** audit §6 `D6`; `SETUP_ISSUES.md` `I-010`, both questions
`OPEN` (Q2 amended 2026-08-14 with the `H1` measurement; **the question is unchanged**) ·
**Records touched if approved:** `I-010`, `D-034` (Q1), `D-035` (Q2)

## The questions being decided

> **Q1 — Is FXCM's 21:00 UTC week open a vendor constant, or a summer artifact?**
>
> **Q2 — Which arm's clock is the `D-035` DEVELOPMENT/HOLDOUT boundary stated in?**

### Q1, in one table

`D-034` records as a **standing vendor fact** that FXCM opens the week at 21:00 UTC *"consistently,
week after week"*, and binds `W-C` and `PT-008`–`PT-013` to that boundary **by name**. The evidence
is `PT-023` §1's depth probe over **2026-05-31 → 2026-08-13 — entirely inside northern-hemisphere
summer**, over which two different vendor behaviours are **indistinguishable**:

| Hypothesis | Summer week open | Winter week open |
|---|---|---|
| Fixed offset, 21:00 UTC year-round | 21:00 UTC | 21:00 UTC |
| New York 17:00, DST-anchored | 21:00 UTC (17:00 EDT) | **22:00 UTC** (17:00 EST) |

HistData is **provably** fixed at 22:00 UTC year-round. **If FXCM is DST-anchored, the V02–V06
homework and the `PT` corpus sit on different session grids for part of the year, in a way nobody
would notice, because each is internally consistent.**

### Q2, in one table

`D-035` pins the boundary at **2016-07-01** on calendar grounds. `D-031` runs every
session-dependent test on **two clocks**. **Nobody has said which clock the boundary is in.**
Measured spillage under Arm B:

| Timeframe | Arm A last bar | Arm B last bar | Bars stamped `2016-07-01` under Arm B |
|---|---|---|---|
| `M15` | `2016-06-30 23:45` | `2016-07-01 00:45` | **4** |
| `H1` | `2016-06-30 23:00` | `2016-07-01 00:00` | **1** |

**Neither reading is wrong; leaving it unstated is.** Four bars will not move a result — **but the
same ambiguity applies at the start of every window and to every future timeframe**, which is why
the `H1` amendment strengthens the case for pinning the clock **once, generally**, rather than
per-dataset.

## Options considered

| Q | # | Option | For | Against |
|---|---|---|---|---|
| Q1 | **1 ⭐** | **Probe FXCM's week open on a week between November and February; amend or confirm `D-034` fact 1 on the measurement** | **Costs one probe.** Settles a standing vendor fact that four pre-registered tests are bound to by name | Needs a winter week, so it is the one item here that cannot be closed today by a sentence |
| Q1 | 2 | Confirm `D-034` as written from the existing evidence | Free | **The probe cannot separate the hypotheses.** `I-010` says in terms: *"Do not amend `D-034` fact 1 from memory or inference — measure it"* |
| Q1 | 3 | Leave open | Nothing changes | It *"will silently corrupt a week-boundary result"* the moment someone compares across sources |
| Q2 | **1 ⭐** | **Absolute, in the corpus's native UTC−5 (Arm A) clock** | The boundary was computed on **calendar** grounds independent of any arm; one rule covers every window start, every window end and every future timeframe; **costs one appended line** | Arm B then reads 4 M15 bars / 1 H1 bar of development data at a wall-clock stamp of `2016-07-01`, which must be documented so it is not read as a holdout leak |
| Q2 | 2 | Per-arm — each arm cuts in its own clock | Each arm is internally tidy | Arm B's development block is 4 bars shorter than Arm A's, so the two arms are no longer measuring the same period — which is the one thing the two-arm design exists to control |

## Recommended defaults

**Q1: Option 1** — the audit and `I-010` agree: *"Costs one winter probe."*
**Q2: Option 1** — recommendation already on record in `I-010` and repeated in the audit:
**absolute, in the corpus's native UTC−5 (Arm A) clock.** *"Costs one appended line."*

---

## PROPOSED LEDGER ENTRY — write to `DECISIONS.md` only on approval

```markdown
## D-050 — The two `I-010` clock questions are ruled: the `D-035` boundary is ABSOLUTE in the UTC-5 clock, and `D-034`'s FXCM week-open fact is REDUCED TO ITS EVIDENCE pending a winter probe

**Date:** 2026-08-14
**Resolves:** `00_SYSTEM/SETUP_ISSUES.md` `I-010` **Q2** outright; `I-010` **Q1** conditionally -
Q1 stays `OPEN` until the probe is run, but its handling is now decided rather than undecided.
**Amends:** `D-035` (Q2, one appended line); `D-034` fact 1 (Q1, scope of the claim only).
`D-031`'s two-arm requirement is untouched.

**PART 1 — Q2. THE `D-035` BOUNDARY IS ABSOLUTE, IN THE CORPUS'S NATIVE UTC-5 (ARM A) CLOCK.**

`D-035`'s DEVELOPMENT/HOLDOUT boundary at **2016-07-01** is **one instant**, expressed in the
corpus's native **UTC-5** clock, and it is **the same instant for both `D-031` arms.** It is **not**
re-cut per arm. **This rule is general**: it governs the start and end of **every** pre-registered
window, at **every** timeframe, now and in future, unless a later decision says otherwise for a
named window.

**The measured consequence, stated so it is never mistaken for a holdout leak:** under Arm B
(`America/New_York`, `+1h` during US DST) the aggregation stamps **4 fifteen-minute bars** and
**1 one-hour bar** with a wall-clock date of `2016-07-01`:

```text
M15:  2016.07.01,00:00 — 00:15 — 00:30 — 00:45
H1:   2016.07.01,00:00
```

**Those bars are DEVELOPMENT data.** Their underlying M1 data is entirely `<= 2016-06-30` in the
file's own UTC-5 clock; they are the same development-side minutes wearing a different clock label.
**The `D-035` holdout remains sealed and unopened, and this entry opens nothing.**

**PART 2 — Q1. `D-034` FACT 1 IS REDUCED TO WHAT ITS EVIDENCE SUPPORTS, AND A PROBE IS OWED.**

`D-034`'s statement that FXCM opens the week at 21:00 UTC *"consistently, week after week"* is
**true of its sample and is not established year-round.** The sample — `PT-023` §1's depth probe,
**2026-05-31 -> 2026-08-13** — lies entirely inside northern-hemisphere summer, over which
*"fixed 21:00 UTC year-round"* and *"DST-anchored New York 17:00"* are **indistinguishable.**
`D-034` fact 1 is therefore **restated as: FXCM's week open is 21:00 UTC over the observed summer
window; its winter behaviour is UNMEASURED.**

**Until the probe is run:**

1. **No new test may bind to a year-round FXCM week open by name.** Existing tests bound to it -
   `W-C`, `PT-008`-`PT-013` — **stand and are not re-run**; their windows are summer-side or
   HistData-sourced, and the exposure is recorded here rather than assumed away.
2. **Any cross-vendor comparison** between the FXCM-sourced and HistData-sourced series **states
   this open question at the point of comparison.** HistData is provably fixed at 22:00 UTC
   year-round; if FXCM is DST-anchored the two **agree in winter and differ by an hour in summer**,
   and each series is internally consistent, so **nothing in the data would flag it.**
3. **The probe is a standing obligation on the first session running after 1 November 2026:**
   probe FXCM's week open on any week between **November and February** and compare against
   22:00 UTC. Record the result by appending to `D-034`. **`D-034` fact 1 is NOT amended from
   memory or inference — it is measured.** `I-010` Q1 closes on that measurement and not before.

**Reason:** Both questions have the same shape — **a convention nobody stated, that no result
currently depends on, and that will silently corrupt a comparison the first time one does.** Q2's
spillage is 4 bars at `M15` and 1 at `H1`, which will not move a result; but the ambiguity recurs
at every window start and at every future timeframe, and the `H1` measurement taken 2026-08-14
established exactly that — it is not an `M15` artifact. Pinning it once, generally, costs one line.
Q1 is the more serious of the two because `D-034` states as a standing vendor fact something its
own evidence cannot support, and four pre-registered tests are bound to it **by name**; the failure
mode is invisible by construction, because each series is internally consistent.

**Absolute rather than per-arm, for Q2:** the boundary was computed on **calendar** grounds before
any chart existed, independent of any arm. Cutting per-arm would make Arm B's development block
4 bars shorter than Arm A's — so the two arms would no longer cover the same period, which
defeats the one thing `D-031`'s two-arm design exists to control.

**Evidence:** `SETUP_ISSUES.md` `I-010` Q1 and Q2 in full, including the 2026-08-14 `H1`
amendment; `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M15_H1/QA_REPORT_H1_ARMB.txt` check `C8`
and that dataset's `README.md` (branch `feature/m15-h1-chart-backtest`, **unmerged** — re-verify
against the merged tree before citing); `D-034` fact 1 and `PT-023` §1; `D-035`; `D-036a`'s three
independent confirmations of HistData's 22:00 UTC; `D-031`;
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §6 `D6`.

**Alternatives considered:** *Per-arm boundaries (Q2)* — rejected for the reason above.
*Leaving Q2 unstated because 4 bars cannot move a result* — rejected; the cost of stating it is one
line and the cost of discovering it in a review is a re-run. *Confirming `D-034` fact 1 as written
(Q1)* — rejected; `I-010` says in terms that it must be measured, not inferred, and the existing
probe provably cannot separate the two hypotheses. *Re-running `PT-008`-`PT-013` now against a
22:00 UTC boundary (Q1)* — rejected as premature: it would spend real work on a hypothesis nobody
has tested, and the winter probe costs one probe and settles it.

**Consequences:** `D-035` gains one appended line stating the clock. `D-034` fact 1 gains its
scope restatement and the probe obligation, appended rather than edited. `I-010` **Q2 closes**;
**Q1 stays `OPEN`** with its handling now decided and its closing test named and dated.
`BACKTEST_EVIDENCE_STANDARD.md` gains the general rule that a pre-registered window's boundaries
are absolute instants in the corpus's native clock, identical across `D-031` arms. **No existing
result is invalidated, no test is re-run, and the `D-035` holdout stays sealed.**
**Status:** ACTIVE — Q1 half PENDING the winter probe
```

---
---

## WHAT HAPPENS NEXT

1. **The owner answers yes / no / edit on each of the six**, independently — approving one does not
   commit any other.
2. For each approved draft, the proposed entry is appended to `00_SYSTEM/DECISIONS.md` **on the
   integration branch** (`D-038a`: `DECISIONS.md` is a POLICY ledger), renumbered contiguously if
   some are declined, and the downstream files each entry's *Consequences* names are updated in the
   same commit.
3. `REVIEW_INDEX.md` items **36, 91, 157, 168, 179** and `SETUP_ISSUES.md` `I-010` are dispositioned
   to match, citing the new `D-0xx` by number.
4. `LOG.md` records the session, the approvals, the declines, and the final numbering map.

**Until step 2 runs for a given draft, that draft is a proposal and nothing more.**

---

*Drafted 2026-08-14 on branch `docs/decision-drafts`. Adopts nothing, closes nothing, changes no
`A-xxx`, `C-xxx`, `I-xxx`, `D-0xx`, disposition or grade. Every quotation and count in it was taken
from the file named beside it.*
