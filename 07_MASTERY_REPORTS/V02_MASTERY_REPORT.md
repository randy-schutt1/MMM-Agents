# V02 — MASTERY REPORT

**Self-assessment by the Student session. Not an authorization.** Only a reviewer `PASS`
(`REVIEW_PROTOCOL.md`) permits progression.

| Field | Value |
|---|---|
| Video ID | V02 |
| Lesson | Bootcamp1 Wk1 031812 Part2 — 18 March 2012, second half of the same session as V01 |
| Duration | 01:00:19 |
| Assessed | 2026-08-10 |
| Standard | `00_SYSTEM/MASTERY_STANDARD.md` |

```text
STATUS:  REVIEW REQUIRED
```

Not `PASS`. Two dimensions are incomplete for reasons I judge legitimate but which a
reviewer must adjudicate, and one process failure in this session needs independent
scrutiny even though I believe I contained it.

---

## 0. READ THIS FIRST — A PROCESS FAILURE IN THIS SESSION

I produced, and reported as findings, three confident conclusions that were **wrong**:

1. that the SWF frame-rate speedup does not work;
2. that V02's `.swf` contains V01's video track;
3. that all 21 lessons declare an identical 54:44 duration.

All three came from one cause. A stale `python3 -m http.server 8899` left running by the
V01 session owned the port the recipe told me to use. `python3 -m http.server` exits
silently when a port is busy, so my server never started, and the `curl -sI` returning
`200` that I used to confirm it was answered by **their** server — whose `index.html`
hardcodes `v01.swf` and ignores the `?swf=` parameter. Every browser render I made,
including a 61-minute capture, played V01.

The frame-rate experiment had a control, and the control did not save me, because the
treatment and the control were the same file. **A control only isolates the variable you
believe you are changing if you have independently verified that you changed it.**

What caught it was that the slides did not match what the instructor was saying. That
check costs one screenshot and I ran it after an hour instead of after two minutes.

**Corrections made:** D-020 retracted in place with the reasoning preserved; D-021 (the
speedup works, 40×) and D-022 (verify port and bytes) added; `SWF_CAPTURE_RECIPE.md` §10
rewritten and GOTCHA 4 added; I-009 opened; the invalid capture renamed
`INVALID_actually-V01_do-not-use.mp4`.

**Unaffected work** — none of it went through the HTTP server: transcript verification
(audio read from disk with `ffmpeg`), the Q-002 fabrication audit, `V02_SOURCE_NOTES.md`
§§1–3 and 5–14, `V02_INTERPRETATION.md` §§1–9, and the A-019…A-025 / C-003 register
entries. The screenshots and §4/§10 come from the corrected capture, which was validated
against the transcript at four independent timestamps before anything was named.

**I am asking the reviewer to treat this as a finding against me and to check my
containment**, particularly whether anything derived from the bad capture survived into
the notes. I believe nothing did, but I am the wrong party to certify that.

---

## 1. THE TEN DIMENSIONS

### A. Recall — **PASS**

I can state V02's content without the notes: the weekly chart is the intraday pattern
drawn larger; Sunday/Monday is "the Asian session for the week"; the dealer's false move
out of that range traps traders; the midweek reversal is the anchor point; the run away
from it lasts at least three days and is projected with ADR × 3 (three cycles, not days);
the dealer holds beyond the trapped level to exhaust them and will not cross back because
that would release them; outside structure high is the first sign the run is over, with
two named continuations; take profit at session changeover with a limit; two hours without
substantial profit means out; a second leg restarts the clock; scratch at −15; only take
second-leg trades.

### B. Recognition — **FAIL (honest)**

I applied the vocabulary to an unseen USD/CHF week (`05_HOMEWORK/V02/V02_HOMEWORK.md`
§1) and produced a plausible markup. **That is not recognition.** There is no answer key
for that week, so nothing confirms my labels are right.

> **CORRECTED 2026-08-10 (V02 review R1, required correction 4).** This paragraph
> continued: *"…and the exercise surfaced a real ambiguity I could not resolve — the
> decisive extreme fell on Monday, in a lesson that locates the anchor midweek."*
> **That is withdrawn.** The markup it rested on had misread the chart (R1 MAJOR 1). On
> re-measurement, **the week's decisive extreme is on Thursday 6 Aug** — the week's high,
> 0.81356 at 15:00 UTC. Monday's high was 0.81151, the week's *first* extreme, not its
> decisive one.
>
> **The observation that survives is a different and better one.** Thursday makes the
> week's high at 15:00 and its own low at 02:00 — so the day that terminates the downward
> legs and the day that produces the week's largest advance are **the same day**, hours
> apart. The instructor's scheme labels "Level 3", "Reverse" and the terminal extreme as
> distinct structural events; it has **no label for them collapsing onto one day**. That
> is a genuine gap in the taught scheme, and unlike the withdrawn claim it is measured.
>
> **The grade does not change. Dimension B remains FAIL** — and the correction makes the
> FAIL better-founded, not worse: the first pass could not identify the week's extremes
> correctly, which is precisely what recognition would require.

Per `MASTERY_STANDARD.md`'s honesty rule I will not claim recognition demonstrated only
on my own unverified markup.

### C. Discrimination — **FAIL (honest)**

*What would make this NOT the setup?* For the 22 trade I can answer partially: it fails
if the dealer breaks the level rather than returning to it and falling back below
(`[00:01:38]`). That test is genuinely objective in form.

For everything else I cannot answer, because the discriminating terms are undefined:
what makes a leg a **second** leg (A-007), what "the box" is (A-006), what a **perfect**
M or W is (A-011). I can identify the instructor's clean examples on his own slides. That
is precisely the ability the standard says does not count.

### D. Sequence — **PARTIAL**

| Stage | Can I state it? |
|---|---|
| What happens before | **Yes** — accumulation Sun/Mon, then the false move |
| What defines the setup | **No** — routes through "second leg", undefined |
| What confirms it | **Partial** — for the 22, return to the level without breaking it |
| What invalidates it | **Partial** — for the 22 only; nothing general |
| What typically follows | **Yes** — a run of at least three days, then outside structure high, then reverse |

Three of five. The two I cannot state are the two that would make it tradeable.

### E. Exceptions — **PASS**

The lesson names its own variations and I have them catalogued in
`V02_SOURCE_NOTES.md` §9 (eleven), reinforced by the printed "Variations On The Theme"
slide's closed list of four. This is the dimension V02 is strongest on — the instructor
repeatedly labels his own material "variations on the theme".

### F. Homework — **DEFERRED (11b) / ATTEMPTED-UNGRADED (11a)**

Applying **D-019**, which distinguishes `DEFERRED` from `NOT APPLICABLE`:

| Item | Disposition | Basis |
|---|---|---|
| 11a — label the weekly cycle, USD/CHF 1H | **Attempted on a substituted week; first pass preserved; ungraded** | 2012 hourly data is account-gated (TradingView 5,000-bar cap reaches only to Jan 2025 — evidence captured). Exercise performed on Sun 2 – Fri 7 Aug 2026. No answer key exists for any week. |
| 11b — 40 flashcards | **DEFERRED** | **Not blocked by data** — all four majors captured. Blocked by **A-011** (M/W anatomy never defined) and **A-007**. Producing forty cards would require inventing the formation criteria and presenting the invention as coursework. |
| Post to the 2012 forum, collect the answer key, email the survey, download the student folder | `NOT APPLICABLE` | 2012 infrastructure; the instructor takes the student folder offline in this very lesson |

I flag for the reviewer that **F is the dimension where D-019 was created by V01's R1
review after two items were wrongly closed as `NOT APPLICABLE`.** I have tried to apply
that lesson: 11b is blocked by missing *evidence*, which keeps it open, not by missing
tooling.

### G. Manual Backtesting — **DEFERRED**

Not `NOT APPLICABLE`. V02 contains at least one structural claim that is observationally
testable without any entry rule — **"the dealer will not cross the level for at least
three days"** (`[00:16:23]`, and printed on the Weekly Structure slide). That is a
falsifiable statement about price behaviour and there is subject matter to test.

It is blocked by **A-004**: "the level" is now known to be an ordinal leg rather than a
price line, so I cannot say *which price* must not be crossed. Also blocked by `I-007`
(no declared chart data source or timezone for reproducible observation) — noting that
the TradingView access established for the homework partially relieves I-007 and the
reviewer may wish to revisit it.

The dimension as written also asks for GBP/USD examples with future price hidden at the
decision point. **V02 states no entry, so there is no decision point to hide.**

### H. Provenance — **PASS**

Every item in `V02_SOURCE_NOTES.md` §§2, 6, 7, 9, 10 carries a timestamp. Every visual
claim in §4 carries a screenshot filename whose frame burns in its own timecode. Nothing
is carried over from the quarantined files.

**Orphan items, listed rather than hidden:**

| Item | Why it is an orphan |
|---|---|
| "Swing Traders Book- Day Traders Book" | Printed on the `[00:18:00]` chart, never spoken, never explained → A-027 |
| `V-3` | Printed beside `PFL`, never spoken → A-028 |
| `HOW` | Printed on the Weekly Structure slide, never expanded → A-026 |
| The `R =` values (eight on one chart) | Never read aloud → A-018 |
| "( NYC Reversal)" | Printed only | 
| The 89.1%/81.9% backtest figure | Retracted by the instructor as he says it; recorded as unusable |

### I. Ambiguity — **PASS**

Ten new records (A-019 … A-028) and six existing records extended with V02 evidence.
Nothing subjective was quietly promoted to a rule. Two records exist specifically to stop
attractive inferences being adopted — A-027 (a chart label that reads like a target rule)
and A-026 (an abbreviation with an obvious-looking expansion).

The one I want the reviewer to check hardest is **A-019**. The visuals recovered the full
session table and only the timezone is missing; New York is strongly indicated by three
converging pieces of evidence. I chose **not** to close it, because the slide does not
print a timezone and closing it would be resolution by inference. A reviewer may
reasonably judge that over-cautious.

### J. Contradictions — **PASS**

C-003 (M's and W's "will not fail", self-contradicted in one sentence) and C-004 (London
open 3:30 printed vs 4:00 spoken) added. C-001 re-tested against V02 and **not resolved**
— which is itself the finding, since C-001 had named "a later lesson refines it" as its
most likely route out, and V02 is that lesson. The printed "For At Least 3 Days"
constrains it without closing it.

---

## 2. THE HONEST ANSWER ON A COMPLETE TESTABLE RULE

**V02 does not contain one, and I am not going to force a pass by assembling one.**

V01 failed this the same way. V02 is a much better lesson — denser teaching, real worked
charts, precise homework, and a genuinely clarifying central analogy — and it adds real
parameters the audio never gave (the 2-hour window, the full session table). But the gap
sits in exactly the same place:

| Component | Status in V02 |
|---|---|
| Entry trigger | **Absent.** Everything routes through "second leg". He says at `[00:35:22]` "And I'm going to define what a second leg is", then defines it only by pointing: "If you see this, that's not a trade. This is not a trade. That's a trade." |
| Entry filter | **Deferred again.** The trading zone went V01 → V02 → V03. |
| Stop loss | **Explicitly deferred** — "we're going to talk about that in here. Probably not today." |
| Position size | **Absent.** "10 or 20 standards" is an aspiration, not a rule. |
| Target | **Partial but ungrounded.** ADR × 3 is a real formula, but "cycle" is undefined and no ADR lookback is stated, so it cannot be computed. |
| Exit / management | **Present and the strongest part** — session changeover, 2-hour clock, −15 scratch, limit orders. |

So V02 supplies **exit and management parameters for a trade whose entry the course has
not yet specified.** For lesson 2 of 21 that is a coherent thing to do and is not a defect
in the lesson. It does mean the lesson cannot pass a standard requiring a complete
testable rule, and the honest disposition is to say so.

---

## 3. QUALITY-CONTROL CHECKLIST

| Item | Status |
|---|---|
| Transcript exists | ✅ `02_TRANSCRIPTS/V02/V02_TRANSCRIPT.md` |
| Transcript timestamps usable | ✅ 1,026 entries, monotonic, verified against audio at four points |
| Source notes exist | ✅ |
| Interpretation in a separate file | ✅ §§1–9 written before any screenshot; §10 added after, §§1–9 unedited |
| Screenshots captured and indexed | ✅ 25 + `INDEX.md`, from the corrected capture |
| Major rules have provenance | ✅ orphans listed in §H |
| Homework complete | ⚠️ 11a attempted-ungraded, 11b DEFERRED — §F |
| Manual chart testing complete | ⚠️ DEFERRED — §G |
| Positive examples exist | ✅ his worked charts |
| Negative examples exist | ⚠️ partial — "don't short this" `[00:19:35]`, "not every move out of the box pays" `[00:22:00]`, but no failed setup is worked through |
| Borderline examples | ✅ the 22-trade overshoot variation `[00:01:28]` |
| Failed valid setups recorded | ❌ **the lesson shows none.** Recorded as a gap in the source, not hidden |
| Unresolved ambiguity logged | ✅ A-019 … A-028 |
| Contradictions logged | ✅ C-003, C-004; C-001 re-tested |
| Concept library updated | ❌ **not done this session** — stated rather than omitted |
| `COURSE_PROGRESS.md` updated | ✅ |
| `LOG.md` updated | ✅ |
| `validate_project.py` passes | ✅ |
| Git state clean after commit | ✅ explicit paths only (I-009) |

---

## 4. WHAT I AM ASKING THE REVIEWER TO AUDIT

1. **The process failure in §0** — specifically whether any conclusion derived from the
   wrong-file capture survived into the notes. I believe none did; I should not be the
   one to certify it.
2. **Dimension F.** Is 11b's `DEFERRED` correct, or am I hiding behind A-011? My argument
   is that producing forty flashcards requires inventing the M/W anatomy. A reviewer could
   reasonably hold that a documented best-effort attempt, clearly labelled as using an
   invented working definition, would be more useful than nothing.
3. **Dimension G.** Same question for the "does not cross the level for 3 days" test.
4. **A-019.** Should it be closed as New York time on the converging evidence, or does
   leaving it open on the absence of a printed timezone serve the project better?
5. **The homework substitution.** Is performing 11a on a 2026 week instead of the
   assigned 2012 week acceptable, or should it have been `DEFERRED` outright?
6. **My §2 conclusion** that V02 states no complete testable rule — the same finding as
   V01, and a reviewer should confirm I have not simply repeated V01's verdict by habit.

---

## Revision R1 — 2026-08-10

Appended per `REMEDIATION_PROTOCOL.md` §3.5. **This report is not overwritten.** All ten
required corrections from `18_REVIEW/V02/V02_REVIEW_R1.md` are applied.

### The MAJOR finding, in my own words

The one place this lesson's work left the documents and touched a chart, it read the
chart wrong — and the wrong reading produced a **false confirmation of `C-001`**, the
project's foundational unresolved contradiction. That is the worst available outcome for
an error in this lesson, and the reviewer is right that it is worse than the pip counts
make it look.

The root cause is not carelessness about one number. It is that **I applied two different
evidential standards in the same session without noticing.** Every claim drawn from the
transcript carries a timestamp and was verified against the marker. Every price drawn
from the chart was eyeballed off axis ticks and written down as though it had been
measured — and then a tolerance (`±5 pips`) was asserted for it that had never been
tested. A chart is a source document. It did not get the discipline a source document
gets.

### What was redone rather than reworded

| Item | Action |
|---|---|
| 11a markup | **Redone from measurement.** Original preserved in place, marked `SUPERSEDED — INVALID READING (R1 MAJOR 1)`. New reading in `V02_HOMEWORK.md` §1.2, method in §1.1. |
| Measurement method | New — candle-pixel detection, least-squares axis calibration (52.27 px/0.00100, max residual 0.10 pip), day boundaries from the x-axis label lattice. Self-validates: measured open = prior close on all six day boundaries. |
| "three days" confirmation | **Withdrawn.** Replaced by the measured result and an explicit statement of why it resolves nothing (`V02_HOMEWORK.md` §1.3). |
| `±5 pips` accuracy claim | Withdrawn as untrue. Corrected table states **±0.5 pip**, derived from ±1 px quantisation plus calibration residual, not asserted. |
| §B "decisive extreme fell on Monday" | Corrected — it fell on **Thursday**. Replaced with the observation that survives. Grade unchanged: **FAIL**. |

### What the corrected week actually showed

Price held below Monday's high for **exactly 72 hours** before exceeding it. I want to be
explicit that this is *not* the vindication it could be dressed up as. Three defensible
counting conventions give three different answers from the same series, and the choice of
Monday's high as "the level" is mine, not the instructor's — `A-004` says the course's
"level" is an ordinal leg, not a price. **Effect on C-001: none.** It is recorded in
`CONTRADICTIONS.md` under that framing and no day-count value is committed anywhere.

Recording a 72-hour result and then declining to claim it is the correct handling, and it
is the same discipline that should have been applied the first time.

### Scope control

The reviewer noted the error **did not propagate** — neither `V02_SOURCE_NOTES.md` nor
`V02_INTERPRETATION.md` cites the homework, and `C-001`'s record was built from the
transcript. **That containment is preserved deliberately.** The corrected numbers were
added *only* to the homework file (source), the mastery report §B (which cited the wrong
claim), and `CONTRADICTIONS.md` (explicitly as a non-resolving datum, because R1 required
the result be recorded either way). Nothing was retro-fitted into the source notes or the
interpretation, and no new claim was introduced anywhere on the strength of one week.

### Minor findings

All five applied: occurrence counts recounted by regex over the verbatim body (2–5, 6→9,
2→1); both ASR repairs disclosed at the point of quotation with the transcript's actual
wording, plus a third repair in the same quote that R1 did not catch; `CONTRADICTIONS.md`
`UNRESOLVED: 3`; `COURSE_PROGRESS.md` Phase 1 row; TradingView history figure reconciled.

Findings 4 and 5 are the same defect — a hand-maintained summary duplicating state held
elsewhere in its own file — and R1 notes finding 4 is the **fourth** occurrence of it. I
have not just corrected the values; each file now names which block is **authoritative**
so the duplicate is reconciled rather than re-incremented. Whether that is sufficient is a
question for R2.

### Carried to R2 — not fixed, flagged

While recounting §3 I found something R1 did not raise and **explicitly endorsed**:
`V02_SOURCE_NOTES.md` §3 and `V02_TRANSCRIPT.md`'s "One thing was removed" both state that
`PFH` and `PFL` *"each appear once"* in the hour. Counting the verbatim body, the
**abbreviations appear zero times**; spelled out, "peak formation high" occurs once and
"peak formation low" twice. I have **not** edited this — it is outside the required
corrections, it sits in a source-adjacent file, and R1 recorded verifying it. R2 should
settle it. Flagging rather than silently fixing, because a reviewer needs to know when a
check they signed off on does not reproduce.

### Dimension grades after remediation

Unchanged. **B remains FAIL**, and is now better-founded. F (11a) moves from
`ATTEMPTED — UNGRADED` to `REDONE FROM MEASUREMENT — LABELS STILL UNVERIFIED`; 11b stays
`DEFERRED`; G stays `DEFERRED`; A-019 stays open; the 2026-week substitution stands.

### What I am asking R2 to audit

1. **Re-measure the chart independently.** Do not accept my §1.1 pipeline because it
   describes itself as reproducible — the last table also described itself as ±5 pips.
2. Whether §1.3 genuinely declines to claim the 72-hour result, or whether it claims it
   while saying it does not.
3. Whether adding the datum to `CONTRADICTIONS.md` at all was correct, or whether the
   safer disposition was to leave `C-001` untouched by homework entirely.
4. The `PFH`/`PFL` count above.
