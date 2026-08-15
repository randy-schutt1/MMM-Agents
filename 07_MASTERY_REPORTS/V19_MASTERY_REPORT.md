# V19 — MASTERY REPORT

**Lesson:** `Bootcamp1 Wk9 052012 Part1 (67mins).swf` — Week 9 Part 1, 2012-05-20
**Printed subject:** `MARKET MAKER TRAP MOVE(S)` — `Trap Candle Patterns` / `Dealer Structures` /
`Behavioral Analysis`
**Branch:** `video/v19`, in an isolated worktree per `D-038`
**Student status:** ⚠ **REVIEW REQUIRED** — not `PASS`. `D-004`: a student `PASS` is not a gate.

---

## §0 — ⚠⚠ GATE STATUS, DECLARED FIRST AND VERIFIED, NOT REPEATED

**This session was briefed that V18's R1 had returned and merged and that V19's gate was open. It
checked rather than trusting the briefing** — which is the discipline V17's and V18's reviews both
recorded as the thing that had been missing.

| Check | Result |
|---|---|
| Integration branch | `claude/add-documents-repository-fdfb3u`, `origin/HEAD` |
| Its tip at fork time | **`847ebd2`** |
| What `847ebd2` is | `merge(review/v18): V18 student work + R1 independent review — REVISE 0C/0M/5 MINOR/16 NOTE, HIGH confidence, V19 GATE OPEN under D-024` |
| `origin/review/v18` | **also `847ebd2`** — the review branch and integration are the same commit |
| This branch forked from | **`847ebd2`**, before any V19 content commit existed |

⭐ **THE GATE IS OPEN AND IT IS OPEN ON THE MERITS.** V18's R1 returned **0 CRITICAL / 0 MAJOR**, and
`D-024` makes finding severity — not verdict — the gate. **There is no timing defect to disclose
this round**: unlike V17's and V18's addenda, V18's review was merged into integration *before* this
worktree was created, and the graph shows it.

⚠️ **AN OPEN GATE IS NOT A `PASS`.** V18 remains **IN REMEDIATION** on items **264–268**, and V17 on
**244–249**. Neither set is discharged by this session and neither is claimed to be.

### §0.1 — DOES EITHER REMEDIATION SET TOUCH V19's SUBJECT MATTER? **TWO DO.**

Checked item by item, because the briefing asked and because "probably not" is not an answer.

| Item | Touches V19? | How |
|---|---|---|
| **245** (V17) | ⭐⭐ **YES, DIRECTLY** | It corrects `A-010`'s addendum to *"how many candles does it take to form a good M and W? On a 15-minute chart, eight…"*. **V19 restates the eight-bar minimum FIVE times and adds the `= two hours` identity that fixes the timeframe arithmetically** (`[00:41:32]`). **The remediation of 245 should see V19's §5.4.** |
| **249** (V17) | ⭐ **YES, METHODOLOGICALLY** | It charged `Q-018` with a diff count that its own enumeration contradicted. **`Q-020` §0 states counts AND enumerates them, and the two agree** (5=5, 1=1, 4=4). Honoured, not just noted. |
| 244 (V17) | partially | Week-counting. V19 states *"week nine"* and prints its date, so it is a clean data point but does not bear on 244's correction |
| 248 (V17) | as a caution | *"17:00 dealer time"* as an unmarked inference. **V19 gives one clock reference with no timezone** (`[00:31:44]`), and `PT-047` §2e refuses to condition on a named session because of it |
| 264 (V18) | ⭐ **YES, AS AN OBLIGATION** | `CONCEPT_INDEX.md` was not updated for V18. **This session updated it for V19.** |
| 265 (V18) | as a caution | An arithmetic figure wrong in three files. **Every V19 figure is computed in the runner and read from JSON, not retyped** |
| 266 (V18) | as a caution | A §8a counterfactual that did not derive from its own table. **`INDEX.md` §0's `−1 s` claim is derived from the published table and bracketed to a 49-second interval** |
| 267 (V18) | as a caution | A runner departing from its pre-registration. **`BT_V19_0001.md` §6 reports the one place `PT-047` and the runner diverge** — a wording defect, not a behavioural one |
| 268 (V18) | as a caution | A two-marker quote cited under one marker. **Multi-marker quotes in the V19 set carry every marker they span** |

**Neither set blocks V19's content.** Item 245 is the one a remediation session should route through
this lesson.

---

## §1 — WHAT V19 IS, IN ONE PARAGRAPH

V19 is the lesson V18's closing slide promised. It argues that the high and low of the day are
**manufactured**, that the manufacture leaves a **countable** signature — an M or W of at least
eight 15-minute bars, counted from the bar that set the extreme — and that the signature has a
**clock** on it: a second leg may exceed the first, but must close back beyond it **within 30
minutes**, or the level extends **25–50 pips** to the next strike zone. The **Half-A-Batman** is the
stated exception and the piece that makes the system one idea rather than three patterns: if the
dealer filled his book on the first move, there is no second leg, and he shifts the zone without
returning. The lesson closes by stripping candlestick patterns of predictive content entirely — a
star formation *"does not matter"*; what matters is *"the next 15 minutes"*.

---

## §2 — ⚠ DECLARED DEVIATIONS AND SELF-CORRECTIONS, BEFORE ANY GRADE

**Stated before the dimension table so no grade is read without them.**

1. ⚠⚠ **THE `SWF_CAPTURE_RECIPE.md` §9 TWO-PASS ORDER WAS NOT FOLLOWED.** Frames were examined
   before the source notes were written. Two mandatory steps forced part of it (§8a's offset
   verification and `GOTCHA 4`'s early content check) and one was discretionary (refuting the
   fabricated `VISUAL_INDEX.md` at its own three timestamps). **Disclosed at
   `V19_SOURCE_NOTES.md` §0, with the structural mitigation — §§1–9 cite transcript markers only,
   §10 is the visual pass. This is the session's most serious process defect and it is
   self-reported, not found.**
2. ⚠⚠ **THE FULL-FILE INDEPENDENT ASR PASS WAS NOT COMPLETED.** Two engines were started; both
   projected multi-hour runtimes under load. **What ran instead is a twelve-segment pre-registration
   fixed in writing before any result was seen, of which seven returned.** They cover every
   load-bearing rule. **This is weaker than V15's, V16's and V18's full-file passes and is owed.**
3. ⚠ **`PT-047`'s pre-registration missed a structural objection** — the classifier's own bars sat
   inside the outcome window. **Raised, tested post-hoc over a disjoint window, and the effect grew
   rather than shrank** (`BT_V19_0001.md` §4). **The omission is still a defect in the
   pre-registration.**
4. ⚠ **`PT-047` §3 called `W-B` an *"out-of-window"* replication. It is not — `W-B` contains
   `W-A`.** Corrected in `BT_V19_0001.md` §5 and §6; the pre-registration is left unedited per
   `COMMON_PROTOCOL.md` §9 rule 7.
5. ⚠ **The deck's cover slide was not captured.** Two 1× attempts failed at the play click and the
   guard aborted both, as designed. `WEEK 9` in print is therefore **not** independently evidenced
   by this session.
6. ⚠ **Three tracked `QA_REPORT*.txt` files were briefly replaced by symlinks** while wiring the
   Git-ignored corpus into the worktree. **Caught by `git status` and restored with
   `git checkout --` before any commit.** No commit contains them. Recorded because it was a real
   mistake against a tracked file, not a near-miss.

---

## §3 — THE TEN DIMENSIONS

| # | Dimension | Status | Basis |
|---|---|---|---|
| **A** | **Recall** | ✅ **SATISFIED** | Every structure, number and rule is recorded with its marker in `V19_SOURCE_NOTES.md` §§4–9, and the numbers are tabulated rather than prose-buried |
| **B** | **Recognition** | ⚠️ **BLOCKED — `D-030`** | Recognising an M requires the eight-bar count **and** the *"blue tracer"* confirmation. **The tracer is undefined** (`A-133`), and the charts carry two candidate blue lines. **Sixth lesson running that B is blocked, and V19 is the lesson where it hurts most**, because V19 is the lesson that would otherwise supply it |
| **C** | **Discrimination** | ✅ **SATISFIED** | The lesson's own discriminators are recorded and kept apart: `CLOSED_BACK` vs `HELD_ABOVE` (`[00:22:43]`), *"confirmed M or a gambling M"* (`[00:39:47]`), M/W vs Half-A-Batman (`[00:50:46]`), and ⭐ the `30–90 min` hold vs the `30–45 min` close-back — **two different quantities the lesson keeps separate and `Q-020` §1 shows the fabricated file conflating** |
| **D** | **Sequence** | ✅ **SATISFIED** | The M's five stages are ordered with markers (`V19_SOURCE_NOTES.md` §5.1), bar-1 is fixed at `[00:32:59]`, and the W is recorded as the mirror with its own markers rather than assumed |
| **E** | **Exceptions** | ✅ **SATISFIED** | ⭐ V19's central exception — the Half-A-Batman as the case where no second leg comes — is recorded at `[00:50:46]` **and identified as the unifying idea** rather than filed as a footnote. The `[00:40:53]` *"Is it hard and fast? No"* qualifier is carried everywhere the `25–50` rule is cited |
| **F** | **Homework** | ✅ **SATISFIED** | `V19_HOMEWORK.md`. ⭐ The finding is that **V19 sets no new assignment**; the standing checklist is enumerated, **six of seven items are recorded NOT DONE with reasons** (four on `D-030`), and the one executable item is run with its convention declared |
| **G** | **Manual backtesting** | ✅ **SATISFIED** | `PT-047` pre-registered at `b34d1a1` **before the runner existed**; `BT_V19_0001.md` reports **CONFIRMED** on all eight cells with `N3` not fired, **plus the objection the pre-registration missed, tested post-hoc and reported as post-hoc** |
| **H** | **Provenance** | ✅ **SATISFIED** | SHA-256 verified before and after patching; four independent duration measurements agreeing to 1.33 s; port and served bytes verified (`D-022`); §8a offset measured, published and bracketed; **27 of 27 frames named from their own burned timecodes** |
| **I** | **Ambiguity** | ✅ **SATISFIED** | `A-132`–`A-134` opened. ⭐ **And `A-135` was opened for the `25 to 55`/`25 to 50` split and CLOSED in the same session** when an independent engine read `50` at both disputed markers — **recorded as opened-and-closed rather than quietly dropped** |
| **J** | **Contradictions** | ✅ **SATISFIED** | `C-029` — ⭐ the deck states the M cap as `30M` and the W cap as `30 to 45 m`, **on camera, forty-five minutes apart**, for a rule the audio states identically for both |

**Nine satisfied, one blocked by `D-030`.** ⚠ **Dimension B is NOT claimed as `NOT APPLICABLE`
under `D-018`** — V19 *does* state a testable recognition rule; the project simply cannot execute
it. `D-019` is explicit that those are different dispositions, so B is recorded as **BLOCKED**, which
is a debt, not a pass.

---

## §4 — WHAT V19 CONTRIBUTES

### §4.1 — ⭐⭐ THE HEADLINE: TWO RULE LINES ARE WRITTEN INTO THE DECK **ON CAMERA**, AND BOTH ARE CAPTURED

**A first for this corpus.** The `"M" Formation` slide at `21:15` ends *"…but must close below."*;
the **PowerPoint editing window** is on screen at `23:10`; the slide at `23:25` reads *"…but must
close below **with in 30M**"*. Forty-five minutes later the same thing happens to the `"W"` slide —
`45:00`, `50:19`, `50:34` — and it is given ***"with in 30 to 45 m"***.

**The narration matches frame for frame** (`[00:22:51]` *"I forgot to write it"* → `[00:22:58]`
*"I'm gonna change the slide"* → `[00:23:17]` *"Save it and we're back in business"*).

⭐ **Why this is evidence and not an anecdote:** these two rule lines **did not exist in the course
material before 2012-05-20**. Any earlier lesson's copy of these slides will not carry the time cap;
any later one will. **That is a checkable, dateable fact about the deck itself**, and it is the
strongest provenance the corpus has yet produced for a single rule.

⚠️ **And the two edits disagree with each other** — `30M` vs `30 to 45 m` — which is `C-029`.

### §4.2 — ⭐⭐ `PT-047` CONFIRMS, AND THE OBJECTION THE PRE-REGISTRATION MISSED MAKES IT STRONGER

Primary cell **Δ = +25.75 pips, p = 0.0007, median MFE(`HELD_ABOVE`) = 43.2 pips** inside the
lesson's own `[25, 50]` band. **All eight cells positive, all p ≤ 0.004, `N3` did not fire.**

⭐ **The part worth reading is §4 of the report, not the verdict.** The pre-registration failed to
notice that the classifier's own bars sat inside the outcome window — a mechanical contamination the
permutation test does not repair. **Re-measured over a disjoint window, Δ rises to +26.90 and
p falls to 0.0005.** The effect is in the extension *after* the decision, which is what the lesson
claims.

⭐ **And `O4` — the outcome the pre-registration measured but declined to score — separates the
groups more cleanly than the one it did score**: 31.85 pips of roll-off below the level for
`CLOSED_BACK` against 9.2 for `HELD_ABOVE`.

### §4.3 — ⭐ `Q-020`: THE TEMPLATE PREDICTION IS CONFIRMED, AND THE TRIO SCORES **TWO** COINCIDENTAL HITS

The V17 review predicted V16–V20 share one template and V21 breaks it. **Tested from inside the
block by direct diff and confirmed**: V19's trio differs from V16's, V17's, V18's and V20's by
`2 / 10 / 8` lines, **all identifier tokens, zero content lines** — and from V15's **and V21's** by
`32 / 30 / 26`. **V21 diffs against V19 exactly as V15 does**, corroborating the predicted break.

⚠ **"Byte clone" is corrected to "identifier-substituted clone"** — all nine SHA-256 values differ.

⭐⭐ **`Q-019` predicted the trio would start landing coincidental true cells as the lessons vary.
V18 landed one; V19 lands two.** And one of them is worse than V18's: the `Peak Time Gap 30-90 mins`
row attaches a real number to *"Between M/W Legs"* — **the very quantity V19 caps BELOW 90 thirty-one
minutes later** (`[00:47:21]` *"90 minutes is too long"*).

⭐ **`EMA` is a clean zero.** The raw census returns 4; **all four are the substring inside
*"email"*.** A census that stopped at the number would have credited the fabricated table with four
hits it does not have — **the same defect class as open items 249 and 265.**

### §4.4 — ⭐ §8a RETURNS A FOURTH SHAPE, AND THE FIRST FRAMES EXPLAIN THE CORPUS'S OLD VALUES

V12 `+16 s`, V13 `+15 s`, V14 `+16 s`, V16/V17 flat zero, V18 `0 → −3 s`. **V19: `0 s` to `49:10`,
`−1 s` after, with the step bracketed to a 49-second interval by five probes run to narrow it.**

⭐ **And frames `i = 0,1` read `+16 s` and `+11 s`** — the latency-times-speed effect §8a warns
about, visible and then **absorbed**, because this session's loop schedules against an absolute
deadline rather than incrementally. **A session using an incremental sleep on this same file would
have measured a constant `+16 s` — which is exactly the value V12 and V14 recorded.** That is a
mechanism for the corpus's spread of §8a values, offered as a hypothesis for the reviewer.

### §4.5 — ⭐ THE TRANSCRIPT CANNOT RENDER THE LETTER `M`, AND IT HIDES THE LESSON'S TITLE

The committed transcript renders spoken *"M"* as `end` / `an` / `and` throughout, so its central
structure reads as *"the end is an aggressive move by the dealer"*. **The independent engine makes
the same error in places, so this is a property of the audio, not of one transcriber** — and the
printed slides settle it (`The " M " Formation`).

**And two of the lesson's three printed subjects are unrecoverable from audio**: *"Track King
patterns fuel structures"* is `Trap Candle Patterns` / `Dealer Structures`.

⭐ **This is the §9 two-pass argument making itself, in the session that failed to follow §9's
order.** Recorded that way rather than presented as a win.

### §4.6 — TDI: CORROBORATION FOR THE OWNER'S RULING, WITH ITS LIMIT STATED

`[00:27:07]` *"since **TDI RSI line** tracks the closes"* (the committed *"RSI mine"* corrected on an
independent engine) and `[00:56:25]`–`[00:56:30]` *"divergence on the TDI or **the RSI line**"*
(**confirmed verbatim**).

⭐ **Consistent with the owner's 2026-08-14 ruling that the volatility bands are a deviation of the
RSI line** — being recorded by a parallel session as `D-052`, **not yet on `847ebd2`**, and cited
throughout the V19 set as **a recent owner ruling pending its own commit**. **Not re-litigated.**

⚠️⚠️ **AND THE LIMIT IS STATED EVERYWHERE IT IS CITED: V19 NEVER MENTIONS THE BANDS.** *"band"*,
*"volatility band"* and *"shark fin"* return **zero**. V19 establishes what the **RSI line** is; it
says nothing about what the **bands** are computed from. ⭐ **`Q-020` §3 exists specifically to stop
the fabricated `NOTES.md` TDI row — which names the bands and reads as corroboration — from being
cashed in for this.**

---

## §5 — WHY THIS IS SUBMITTED AS **REVIEW REQUIRED** AND NOT **PASS**

1. **`D-004`.** A student `PASS` is not a gate and never has been.
2. **Dimension B is blocked**, and V19 is the lesson that should have unblocked it.
3. **The §9 two-pass order was violated** (§2.1). A reviewer cannot verify from the file that no
   visual knowledge leaked into the transcript-only sections.
4. **The full-file ASR pass is missing** (§2.2). R1 item 303 corrects the census: eight of twelve
   returned; four (`S3`, `S9`, `S10`, `S12`) were owed and were later run by R1 (item 309).
5. **`PT-047`'s pre-registration had a hole in it** (§2.3), found by the session that wrote it —
   which is better than not finding it and worse than not having it.

---

## §6 — WHERE I WOULD MARK MYSELF DOWN

* ⚠️ **The two-pass violation is the one I would lead with as a reviewer.** The mitigation is
  structural, not chronological, and structural mitigations are checkable only by re-deriving every
  claim. **That is real work I have pushed onto the reviewer.**
* ⚠️ **`PT-047`'s missing objection should have been in §2 of the pre-registration**, not in §4 of
  the report. Declaring five weaknesses and missing the most obvious one is a **worse** outcome than
  declaring three, because the list reads as exhaustive.
* ⚠️ **`W-B` was described as an out-of-window replication when it contains `W-A`.** I corrected it,
  but I wrote it, and it is the kind of overstatement that survives when nobody checks.
* ⚠️ **The `n < 30` fragility guard came within one event of firing** (`n_held = 31`). The
  `CONFIRMED` verdict is real and its margin on that guard is thin. **A reviewer should re-run with
  a 60-minute robustness arm.**
* ⚠️ **I nearly recorded `[00:17:11]`'s *"one hour 15 minutes"* as a parameter** before the candle
  count in the same marker showed he was reading a chart.
* ⚠️ **The symlink slip against three tracked files** (§2.6). Caught by `git status`, but I caused
  it.

---

## §7 — OPEN ITEMS RAISED FOR THE REVIEWER

| # | Item |
|---|---|
| 1 | **The full-file independent ASR pass was incomplete at submission.** R1 item 303 corrects the returned set to eight of twelve and the owed set to `S3`, `S9`, `S10`, `S12`; R1 item 309 subsequently ran all four and found no overturned claim. A full-file pass, as distinct from the segment debt, remains absent |
| 2 | **`A-133` — the `blue tracer` is undefined**, and it blocks dimension B and every V19 entry rule |
| 3 | **`A-134` / `C-029` — the time cap is `30` / `30–45` / `45 tops` / `30–60`, and the two on-camera slide edits disagree.** Needs an owner call or a later lesson |
| 4 | **`A-132` — the 9.0-second gap** between the last marker and the end of audio is unverified |
| 5 | ⭐ **Item 245's remediation should route through V19 §5.4**, which restates the eight-bar rule five times and supplies the `= two hours` identity |
| 6 | ⭐ **The `06:45` frame is Tier 1 evidence for `DECISION_DRAFT_D-051_ADR_INDICATOR.md`** — *"A yard"* is `ADR`, prescribed as standing homework. **No adoption proposed** |
| 7 | **`PT-047` should be re-run with a 60-minute robustness arm** (§6) |
| 8 | ⚠ **`D-052` is cited throughout as a recent owner ruling pending its own commit.** If it lands renumbered, every V19 citation needs updating |
| 9 | **The deck's cover slide is uncaptured**; a reviewer with a working 1× play coordinate could close it |

---

## §8 — SESSION HYGIENE

| Item | State |
|---|---|
| Branch | `video/v19`, created from `847ebd2` |
| Worktree | `/Users/randyschutt/Desktop/Trading/MMM-Agents-v19` — **isolated per `D-038`**, never the shared checkout |
| Staging | `git commit -m "…" -- <explicit paths>` on every commit; **no `git add -A` anywhere** (`I-009`) |
| Ledgers written on this branch | `QUARANTINE_REGISTER.md`, `COURSE_PROGRESS.md`, `LOG.md`, `REVIEW_INDEX.md`, `AUTOMATION_AMBIGUITIES.md`, `CONTRADICTIONS.md`, `CONCEPT_INDEX.md` — **evidence ledgers, per `D-038a`** |
| Policy ledgers touched | **NONE.** `DECISIONS.md`, `SETUP_ISSUES.md` and every protocol file are untouched on this branch |
| Merged to integration | ❌ **NO — and deliberately not.** `D-003`: review runs in a separate session first |
| Record IDs allocated against | `847ebd2`, the integration tip. **`D-047` re-check owed at merge-back** |
