# V20 — MASTERY REPORT

**Lesson:** `Bootcamp1 Wk9 052012 Part2 (46mins) (1).swf` — Week 9 Part 2, 2012-05-20
**Printed subject:** `MARKET MAKER BOOT CAMP` / **`THE OUT SIDE STRUCTURE`**
**Branch:** `video/v20`, in an isolated worktree per `D-038`
**Student status:** ⚠️ **IN REMEDIATION** — V20 R1 returned **REVISE, 2 `MAJOR`**, and this report is
**amended, not re-filed**. See §0a. `D-004`: a student `PASS` is not a gate, and a student **fix**
is not a verification.

---

## §0a — ⚠️⚠️ AMENDED 2026-08-15 AFTER V20 R1 — TWO `MAJOR` FINDINGS, BOTH ACCEPTED

**V20 R1 returned `REVISE` with `M1` and `M2`. Both are correct. Both were verified by this session
before being acted on, not taken on trust.**

| | Finding | What this session did |
|---|---|---|
| **`M1`** item 332 | `run_pt048.py` bypassed `PT-048` §3.1's `±3` swing scale for the primary measure, using a hardcoded `±1`; the divergence **flipped the verdict** and `BT_V20_0001.md` §6 asserted no such divergence existed | ⭐ **Confirmed by reading my own code.** Runner wired to `PIVOT_K`; re-run; **verdict `CONFIRMED` → `REFUTED`** (30.10 `[28.80, 31.25]`). **Sensitivity now published on every run.** `BT_V20_0001.md` §2a, §6 |
| **`M2`** item 333 | The committed transcript mis-hears `candle` as `handle`; **`A-136` was opened on a word the instructor never says**, and `PT-048` §1a excluded the one testable V20 rule because of it | ⭐ **Verified with my own fifth ASR decode before accepting it.** `A-136` **CLOSED as an ASR artifact**; `A-139` opened for what survives; **`PT-049` pre-registered** to test the rule the artifact suppressed |

⛔⛔ **NEITHER FIX IS SELF-VERIFIED, AND THAT IS DELIBERATE.** `D-024` holds the gate closed on any
`MAJOR` until it is fixed **and re-reviewed in a fresh round**. ⭐ **The V20 R1 reviewer raised the
concern that owner-authorised self-verify was becoming the default** (V19 item 302 was closed that
way). **This round does not use it.** **V20 R1 must re-check.**

⭐ **The root cause of BOTH findings is the same and it is item 326:** this session ran **no
independent ASR pass** and **no independent re-implementation** of its own runner. **The reviewer
ran both, and each found a `MAJOR`.**

---

## §0 — GATE STATUS, CHECKED RATHER THAN TRUSTED

| Check | Result |
|---|---|
| Integration tip at fork time | **`50edf5f`** |
| What it is | the V19 merge + the item-302 fix + the note-count reconciliation |
| V20 gate per `COURSE_PROGRESS.md` | ⭐ **OPEN** under `D-024` — V19's standing tally is `0C/0M/3 MINOR` |
| This branch forked from | **`50edf5f`**, before any V20 content commit existed |

⚠️ **AN OPEN GATE IS NOT A `PASS`.** V19 is **IN REMEDIATION** on items **303–304**, V18 on
**264–268**, V17 on **244–249**. **None is discharged by this session.**

⚠️⚠️ **AND ONE THING ABOUT THAT GATE MUST BE CARRIED FORWARD, NOT BURIED:** V19's `MAJOR` (item 302)
was **fixed and closed by the session that raised it**, on owner authorisation. **`D-003` is NOT
satisfied for that fix round.** A reviewer may reopen item 302 on the merits, and **if it reopens,
this branch was authorised by a gate that would not have been open.** Stated because this session
benefits from it.

### §0.1 — DOES ANY OPEN ITEM TOUCH V20's SUBJECT MATTER? **TWO DO.**

| Item | Touches V20? | How |
|---|---|---|
| **245** (V17) | ⭐⭐ **YES, DECISIVELY** | It corrects `A-010` to *"On a **15-minute chart**, eight"*. ⭐ **V20 prints `M15` on three charts across three instruments** — the first direct attestation of the course's timeframe in the corpus. **Route 245's remediation through `04_SCREENSHOTS/V20/INDEX.md` §11.** |
| **296** (V19) | ⭐ **YES** | Its §8a latency hypothesis is **corroborated by a second sweep** — `INDEX.md` §0 |
| 302 (V19) | ⭐ **YES, METHODOLOGICALLY** | It charged a `MAJOR` for a missing interval. **`PT-048` §3 makes the interval a CONDITION OF THE VERDICT, pre-registered**, and every rate in `BT_V20_0001.md` carries Wilson bounds |
| 249 / 293 / 317 | as a discipline | *"a count stated without checking what it counts"*. ⭐ **`V20_SOURCE_NOTES.md` §11 reports `RSI = 1` and then explains it is the substring inside *"unive**RSI**ty"***, and §5.3 reports `handle = 7` and explains that only 4 are the word |
| 303–304 (V19) | no | ASR bookkeeping and a cross-reference, both internal to V19 |

---

## §1 — WHAT V20 IS, IN ONE PARAGRAPH

V20 is the second half of V19's night and it opens mid-sentence. Its subject is the **outside
structure** — the aggressive **single-leg** move that sets the high or low of the day or week — and
its argument is that this one move is the thing the whole method trades off: the M, the W, the
Half-A-Batman, the spike and the railroad track are presented as its parts or its consequences. It
defines the **railroad track** properly for the first time (*a 30-minute structure where the market
maker triggers the stops, shifts the zone and sets the HOD or LOD in one move*), restates V19's
**30-minute cap** with an **action** and a **floor**, gives the corpus's first **mechanical entry
arithmetic** (one third off the high of the handle), and closes with a printed nine-item pattern
list and a nine-bullet summary.

---

## §2 — ⚠️ DECLARED DEVIATIONS, BEFORE ANY GRADE

1. ⭐ **The `SWF_CAPTURE_RECIPE.md` §9 two-pass order WAS followed** — §§1–9 of the source notes were
   written while the sweep was still running and **no V20 frame existed on disk**. **This is the
   defect V19 self-reported as item 286; it did not recur.** ⚠️ **It was achieved by scheduling
   luck, not by resolving item 306's contradiction**, which stands.
2. ⚠️⚠️ **NO INDEPENDENT ASR PASS WAS RUN — NOT FULL-FILE, NOT SEGMENTED.** V15/V16/V18 ran full-file
   passes; V19 ran a twelve-segment pre-registration. **This session ran none.** Its transcript
   corrections rest on **the printed deck plus internal consistency**. **This is the weakest
   verification position in six lessons and it is OWED.**
3. ⚠️⚠️ **`PT-048`'s pre-registration named the right null and did not wire it into the verdict**
   (`BT_V20_0001.md` §3a). **The `CONFIRMED` it produced is nearly vacuous and the report says so in
   its own §0.**
4. ⚠️ **`PT-048`'s `N1` ran 2,000 iterations against a committed 10,000** — a runtime reduction that
   departs from the spec. Reported at `BT_V20_0001.md` §6; **the pre-registration is not edited.**
5. ⚠️ **The homework's recall test was self-scored** (§2 of `V20_HOMEWORK.md`). The ordering claim —
   list written before the answer frame was opened — **is not verifiable from the files.**

---

## §3 — THE TEN DIMENSIONS

| # | Dimension | Status | Basis |
|---|---|---|---|
| **A** | **Recall** | ✅ **SATISFIED** | Every structure, number and rule recorded with its marker in `V20_SOURCE_NOTES.md` §§1–9; 23 frames transcribed from the pixels in `INDEX.md` |
| **B** | **Recognition** | ⚠️ **BLOCKED — `D-030`** | ⚠️ **SEVENTH lesson running**, and **on `A-133` alone.** The *"blue tracer"* is spoken once (`[00:28:58]`) and still undefined. ⭐ **CORRECTED 2026-08-15:** this row previously also cited *"handle"* (`A-136`); **that half is withdrawn** — the entry arithmetic is complete (`M2`, item 333) |
| **C** | **Discrimination** | ✅ **SATISFIED** | The lesson's own discriminators are kept apart: intraday vs multi-day outside structure (`[00:12:43]`), spike vs entry (`[00:26:06]` *"No, avoid it"*), stop hunt vs momentum (`[00:31:47]`), and ⭐ the `Rick` anecdote recorded as the **counter**-example the instructor makes it (`§4.1`) |
| **D** | **Sequence** | ✅ **SATISFIED** | The outside-structure → `L3` → resolution order is recorded with markers (`[00:42:51]`, `[00:43:02]`), and the cap's sequence (break → 30 min → close back / scratch) at `[00:27:44]`–`[00:28:35]` |
| **E** | **Exceptions** | ⚠️ **PARTIAL** | ⚠️ **V20 states an unqualified universal — *"an absolute sign of reversal"* `[00:01:41]`, twice — and supplies NO invalidation condition.** Recorded as taught, **not** as established (`V20_INTERPRETATION.md` §2.1). The only explicit exception in the lesson is *"is it always three moves? No"* `[00:41:05]` |
| **F** | **Homework** | ✅ **SATISFIED** | `V20_HOMEWORK.md`. ⭐ The recall test was attempted and **self-scored 8 of 9, with the miss recorded** — and the miss is the lesson's centrepiece, because the audio trails off where the slide names it |
| **G** | **Manual backtesting** | ⛔ **NOT SATISFIED — `M1`** | ⛔ **The runner did not implement its own pre-registration** and the divergence flipped the verdict (`M1`, item 332). ⭐ Corrected: **`REFUTED`**. **The pre-registration itself was right, was committed before the runner existed, and made intervals mandatory** — and `PT-049` now carries the baseline as a verdict condition too |
| **H** | **Provenance** | ✅ **SATISFIED** | `.swf` SHA-256 re-computed and matching the manifest; **four independent length measures agreeing to 0.33 s**; port and served bytes verified; §8a offset measured, published and bracketed; **23 of 23 frames named from their own burned timecodes**, including one inside the transient |
| **I** | **Ambiguity** | ✅ **SATISFIED** | `A-136`, `A-137`, `A-138` opened, each with the reason it blocks rather than merely noting vagueness |
| **J** | **Contradictions** | ✅ **SATISFIED** | `C-030` — ⭐ and it is recorded as **`PROVISIONAL`, narrowing `C-029` on the M side and explicitly silent on the W side**, rather than claimed as a closure |

**Eight satisfied, one partial, one blocked.** ⚠️ **Dimension B is NOT `NOT APPLICABLE`** — V20
states testable recognition rules; the project cannot execute them.

---

## §4 — WHAT V20 CONTRIBUTES

### 4.1 ⭐⭐⭐ `M15` IS PRINTED — THE TIMEFRAME STOPS BEING A DERIVATION

`GBPCHF,M15` (`04:35`), `GBPUSD,M15` (`18:20`), `USDCHF,M15` (`33:15`). Until now the corpus carried
this as arithmetic from V19's *"eight candles … which is by the way two hours"*. ⚠️ **V20 still never
SAYS `M15`** — this is evidence about the charts he uses, not a spoken instruction — **but it is
direct attestation on three instruments.** **Item 245's remediation should see it.**

### 4.2 ⭐⭐ THE DECK SETTLES AN ASR DEFECT **INSIDE A DEFINITION**

*"Shift his own"* — five occurrences, one of them inside the railroad-track definition — is
**`Shift the zone`** (`26:15`, printed). ⭐ **This is the §9 two-pass argument paying for itself in
the lesson that followed the order**, and it is the mirror image of V19, where the same argument had
to be made by a reviewer's leak test.

### 4.3 ⭐⭐ THE RAILROAD TRACK IS DEFINED AS A FUNCTION, NOT A SHAPE

> *"A **30 minute** structure where the Market Makers trigger the stops, **Shift the zone** and Set
> the **HOD or LOD** on one move."*

⭐ **Consistent with V19's geometry** (*"30 minutes, 15 in, 15 out"*, `[01:02:45]`): **V19 gave the
shape, V20 gives the purpose, and both say 30 minutes.**

### 4.4 ⭐⭐ THE TIME CAP GAINS AN ACTION AND A FLOOR

`30 minutes or less`; **15 minutes is explicitly refused**; **stays above ⇒ scratch the trade**;
re-entry needs **a nice solid close**. **`C-030`, and it narrows `C-029` without closing it.**

### 4.5 ⭐⭐ A MECHANICAL ENTRY — AND IT IS COMPLETE

> ⚠️⚠️ **CORRECTED 2026-08-15 — `M2`, item 333.** This section originally read *"A MECHANICAL ENTRY,
> BLOCKED BY ONE WORD"* and called `A-136` ***"the cheapest high-value blocker in the project"***.
> ⛔ **There is no such blocker.** The word is `candle`, not *"handle"*.

*"Take the distance of this **candle** divided by three […] take your entry **one-third off the high
of this candle**"*, worked at 100 pips → *"**Subtract 33 pips off the high**, a third."*

⭐⭐ **`entry = high − (candle range ÷ 3)` — the first entry rule in the studied corpus whose
arithmetic `D-030` does not block.** ⚠️ **What survives is narrower: WHICH candle is never stated in
words** (`A-139`). **`PT-049` tests it under three declared bar-selection conventions.**

### 4.6 ⭐ `A-019` GAINS ITS FIRST NAMED TIMEZONE — AND DOES NOT CLOSE

`[00:34:05]` *"three thirty, four o'clock **New York time**"*. ⛔ **It timestamps when the dealer's
intent becomes readable, not a session boundary**, and `EST`/`EDT` is not said. **EXTENDED, not
closed** (`V20_INTERPRETATION.md` §2.6).

### 4.7 ⭐ `Q-021` CLOSES THE V16–V20 TEMPLATE BLOCK

All five members diff at `2/10/8` internally and `32/30/26` against V15 and V21. ⭐ **V20 scores
ZERO coincidental true cells**, breaking V18's one and V19's two — **and that is one draw, not a
trend.**

---

## §5 — WHY THIS IS `REVIEW REQUIRED` AND NOT `PASS`

1. **`D-004`.** A student `PASS` is not a gate.
2. **No independent ASR pass of any kind was run** (§2.2). Every quoted correction rests on the deck.
3. **`PT-048`'s pre-registration was inadequate and its verdict is nearly vacuous** (§2.3).
4. **Dimension B is blocked for a seventh lesson**, and dimension E is partial.
5. **The homework's recall test is self-scored and its procedure is unverifiable** (§2.5).

---

## §6 — WHERE I WOULD MARK MYSELF DOWN

* ⚠️⚠️ **The missing ASR pass is what I would lead with as a reviewer.** V20's most quotable lines —
  *"three pepperoni on the pizza"*, *"25 to 50-50 candle"* — are garbled, and **I corrected the
  load-bearing ones from the deck and left the rest.** A reviewer with 20 minutes of `whisper` can
  do better than I did.
* ⚠️⚠️ **`PT-048` §4 states the null correctly and §5 never scores it.** Declaring the right baseline
  and then not making it a condition is worse than not declaring it, because the file reads as
  rigorous. **Same class as item 289.**
* ⚠️ **`N1` at 2,000 iterations against a committed 10,000.** Small, real, and mine.
* ⚠️ **I graded *"the outside structure is the vector of an M/W"* down to MEDIUM only after the deck
  showed the slide names the Half-A-Batman alone.** Had the frames not existed I would have carried
  it at HIGH.
* ⚠️ **I nearly recorded *"the AV equals"* as an unknown indicator** before the slide showed `AB=CD`
  — a pattern the lesson **dismisses**.

---

## §7 — OPEN ITEMS RAISED FOR THE REVIEWER

| # | Item |
|---|---|
| 1 | ⚠️⚠️ **An independent ASR pass is OWED for the whole lesson.** Priority passages: `[00:22:15]` *"25 to 50-50 candle"*, `[00:27:49]` *"three pepperoni on the pizza"*, `[00:41:18]` *"a burst, a burst, and a t[r]ack"* |
| 2 | ⚠️ **`PT-048`'s baseline was not a verdict condition** — `BT_V20_0001.md` §3a. **A reviewer is entitled to treat the `CONFIRMED` as a null** |
| 3 | ⛔ ~~`A-136` is the cheapest high-value blocker~~ — **WITHDRAWN. `M2`/item 333: the word is `candle` and there is no blocker.** ⭐ **`A-139`** carries what survives (which candle), and **`PT-049`** tests the rule |
| 4 | ⚠️ **`A-133` (*blue tracer*) survives V20** — dimension B blocked for a seventh lesson |
| 5 | ⭐ **Item 245's remediation should route through `INDEX.md` §11** — `M15` printed on three charts |
| 6 | ⚠️ **`C-030` is `PROVISIONAL` and I did not adjudicate `C-029`.** If a reviewer thinks V20's silence on the W side is itself evidence, that is a finding I declined to make |
| 7 | ⚠️ **The `44:00` closing slide contradicts the audio and I opened NO contradiction record** — reasoning at `INDEX.md` §10. **Charge it if you disagree** |
| 8 | ⚠️ **V20's *"absolute sign of reversal"* is an unqualified universal with no invalidation condition.** I recorded it as taught-not-established; a reviewer may want it flagged harder |
| 9 | ⭐ **Item 296 corroborated by a second sweep** — `INDEX.md` §0. It predicts an incremental-sleep sweep would show a constant `+16 s`; **I did not run one** |

---

## §8 — SESSION HYGIENE

| Item | State |
|---|---|
| Branch | `video/v20`, created from `50edf5f` |
| Worktree | `/Users/randyschutt/Desktop/Trading/MMM-Agents-v20` — **isolated per `D-038`**, never the shared checkout |
| Corpus wiring | ⭐ **CSVs symlinked individually, never a tracked directory**; `git status` checked for type-changes afterwards — **zero** (the trap item 300 records) |
| Staging | `git add` on explicit paths only; **no `git add -A` anywhere** (`I-009`) |
| Ledgers written | `QUARANTINE_REGISTER.md`, `AUTOMATION_AMBIGUITIES.md`, `CONTRADICTIONS.md`, `COURSE_PROGRESS.md`, `LOG.md`, `REVIEW_INDEX.md`, `CONCEPT_INDEX.md` — **evidence ledgers per `D-038a`** |
| Policy ledgers touched | **NONE.** `DECISIONS.md`, `SETUP_ISSUES.md` and every protocol file are untouched |
| Merged to integration | ❌ **NO — and deliberately not.** `D-003`: review runs in a separate session first |
| Record IDs allocated against | `50edf5f`. **`D-047` re-check owed at merge-back** |
