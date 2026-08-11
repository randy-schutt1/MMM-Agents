# V05 — INDEPENDENT REVIEW R1B (parallel second opinion)

| Field | Value |
|---|---|
| Lesson | V05 — `Bootcamp1 Wk2 032512 Part3 (68mins).swf` |
| Review round | **R1B** — a *second, independent* R1, run in parallel. **`V05_REVIEW_R1.md` is NOT superseded, NOT corrected and NOT overwritten** |
| Reviewed | 2026-08-11 |
| Reviewer | Independent Reviewer / Teacher Agent, fresh session (`D-003` satisfied — this session authored no V05 artifact) |
| Protocol | `00_SYSTEM/REVIEW_PROTOCOL.md` (17 dimensions, error taxonomy, severity) |
| Standard | `00_SYSTEM/MASTERY_STANDARD.md`; `DECISIONS.md` D-001 … D-025 |

---

## EXECUTIVE BLOCK

```text
LESSON:     V05
DECISION:   REVISE
CONFIDENCE: HIGH

CRITICAL:   0
MAJOR:      0
MINOR:      4   (m1 … m4, all NEW — additional to R1's M1-M6)
NOTE:       4   (n1 … n4)

ADVANCEMENT: AUTHORIZED — the V06 gate OPENS under D-024
             (0 CRITICAL, 0 MAJOR). Agrees with R1.

CONCURRENT-SESSION DAMAGE: NONE in the V05 student pipeline.
             ONE LIVE COLLISION IN THE REVIEW LAYER — see §0.
```

**This round agrees with `V05_REVIEW_R1.md` on the verdict, the gate, and every finding it
raised.** It exists because it was run concurrently and independently, and it did not know
R1 existed until R1's file appeared on disk mid-session. Having found four defects R1 did
not, discarding it would have destroyed the only thing a duplicated session is good for.

**Two of the four are defects that have now propagated *into* `V05_REVIEW_R1.md` itself**
(`m1`, `m2`). That is not a criticism of R1, which is a strong review; it is the reason
this file is being kept.

---

## 0. REPOSITORY STATE — AND A LIVE COLLISION IN THE REVIEW LAYER

### 0.1 The student pipeline: no collision, no damage

Verified before anything else, independently of R1's identical conclusion:

| Check | Result |
|---|---|
| `git log --oneline -25` | `HEAD` = `b4b690b`. The V05 pipeline is exactly **9 commits**, `a34d2f2` → `b4b690b`, in protocol order. **No extra commits from any duplicate session reached this repository.** |
| Ambiguity IDs | `A-001` … `A-049`, **49 headings, 49 unique, zero duplicates, zero gaps** |
| Contradiction IDs | `C-001` … `C-005`, no duplicates. (A naive `^#+ *C-\d+` scan reports 9 headings; the four extras are `###` sub-heads inside the `V03 EVIDENCE ADDED TO EXISTING RECORDS` block. Not a collision.) |
| `validate_project.py` | **97 passed, 0 warnings, 0 failures** |
| Untracked `05_HOMEWORK/V02/measure_usdchf_week.py` | `REVIEW_INDEX.md` **open item 13** — deliberately left in place since V02 R2. Not debris. Untouched by this round |

**Answer to the question as asked: the V05 *student* work carries no duplication, no ID
collision and no orphaned content. It needs no cleanup.**

### 0.2 The review layer: a live, active collision — FLAGGED FOR THE OWNER

This is the finding the session was actually needed for, and it is a **process** finding,
charged against the project's session management rather than against V05.

At this session's start, `18_REVIEW/V05/` **did not exist** and `REVIEW_INDEX.md`'s STATUS
block read `LESSONS REVIEWED: 4 / AWAITING REVIEW: 0`. Partway through this review, without
any action by this session:

| Time (observed) | Event |
|---|---|
| 06:08 | `18_REVIEW/V05/V05_REVIEW_R1.md` appeared — 36 KB, complete, `REVISE`, 0/0/6 |
| 06:10:11 | `18_REVIEW/REVIEW_INDEX.md` modified — `+106 / −6`, STATUS rewritten to `LESSONS REVIEWED: 5 … IN REMEDIATION: 1 (V05 — R1 REVISE, 0 CRITICAL / 0 MAJOR / 6 MINOR)` |
| 06:10:16 | This session observed both. Both **uncommitted** at that moment |
| shortly after | The other session committed them as **`c41e686`** (`REVIEW_INDEX.md`, `V05_REVIEW_R1.md`, `LOG.md`), cleanly. **`R1B` is committed on top of `c41e686` and conflicts with nothing** |

**A second reviewer session is, or recently was, live in this working tree.** The duplication
the owner reported in the *student* layer did not reach the repository; the duplication in
the *reviewer* layer did.

**What this session did about it, and why:**

1. **It did not write `V05_REVIEW_R1.md`.** The session prompt named that path, on the
   reasonable belief that no V05 review existed. `SETUP_ISSUES.md` **I-002** and
   `REVIEW_PROTOCOL.md` **§11** both forbid overwriting a round; doing so would have
   destroyed a complete independent review. **This file is `R1B` for that reason alone.**
2. **It did not touch `REVIEW_INDEX.md`.** That file has another session's uncommitted
   changes in it. Editing it would race. **`REVIEW_INDEX.md` is therefore NOT updated for
   this round — that is a deliberate omission, and it is owed.**
3. **It staged explicit paths only**, so nothing of the other session's work is swept into
   this session's commit.

> #### ⚠ OWNER ACTION REQUIRED — the only cleanup this review asks for
>
> 1. **Confirm `R1B`'s filename**, or rename it. The project has no convention for two
>    independent reviewers on one round; `R1B` was chosen as the least surprising reading of
>    I-002. **`R2` would have been wrong** — R2 is the remediation-verification round, and no
>    remediation has occurred.
> 2. **Reconcile `REVIEW_INDEX.md`.** Its STATUS block and delta rows currently describe
>    R1's six minors only. The true R1-round total is **10 minors** (R1's `M1`–`M6` +
>    this round's `m1`–`m4`). The gate is unaffected — 0 CRITICAL, 0 MAJOR either way.
> 3. **Decide whether parallel reviews are wanted.** They cost double and they caught four
>    real defects here, two of them inside the first review. That is a genuine result, but it
>    should be a choice rather than a tooling accident.

---

## 1. SOURCE REVIEWED FIRST (`REVIEW_PROTOCOL.md` §3)

Everything below was re-derived from the transcript body, the committed JSON and the PNG
files in this session. Nothing was read from a student summary, a commit message, or R1.

### 1.1 The transcript's own coverage claims — all reproduce exactly

Scanned by regex over lines fully matching `^\[\d\d:\d\d:\d\d\]$`, body only:

| Claim | Measured | Verdict |
|---|---|---|
| 1,353 markers, 1,353 distinct | **1,353 / 1,353** | ✅ |
| Strictly increasing; zero decreasing, zero same-second adjacent | **0 and 0** | ✅ |
| Largest gap 13 s at `[00:08:38]` and `[00:19:38]` | **13 s, at exactly those two** | ✅ |
| Final entry `[01:08:20]` | ✅ | ✅ |

**The `E20` monotonicity class stays empty project-wide.** V05 states the strong property and
the strong property is true — the first transcript in the corpus for which that holds.

### 1.2 The speaker finding — independently confirmed

| Claim | Measured (body only, word-boundary) | Verdict |
|---|---|---|
| 21 third-person references to Steve | **21.** Each read in context; **all 21 are third-person**, none addresses or voices the speaker | ✅ |
| Not V04's guest — Diana/Diane 0, Orlando 0, "my son" 0, "12 pairs" 0 | **0, 0, 0, 0** in the body (all four occur only in the header, stating the claim) | ✅ |
| "Carl" not present | **0** in body | ✅ |
| Nearest token *"Cara"* | **1** in body | ✅ |

**The 0%-instructor finding is correct, and it is the single most consequential fact in the
lesson.** D-025 applies to the whole file.

### 1.3 The ASR-garble list — 30 of 30 citations resolve

Every marker in `TRANSCRIPTION NOTES` criterion 3 and the notes beneath it was opened and
read. **All thirty carry the words attributed to them**, including the low-frequency ones a
fabricator would not invent: *"COW cow is a quart of wood"* `[00:21:33]`, *"Until I CNN."*
`[00:47:28]`, *"55 bibs"* `[00:56:56]`, *"empty-fold platform"* `[00:57:09]`, *"It's an anal
pattern."* `[00:41:40]` immediately after *"I'm a little anal"* `[00:41:29]`.

`TDI` = **6**, at the six markers named. Template tokens `5/13`, `5 EMA`, `13 EMA`, `800`,
`Asian Box`, `PFH`, `PFL`, `LOD`, `10 to 15 pips` = **0 each**. `HOD` case-insensitive
returns exactly one hit and it is *"This method works."* `[00:51:33]` — the transcript's own
account, confirmed.

### 1.4 Fabrication quarantine (`Q-005`) — re-measured at the byte level

| `Q-005` claim | This session | Verdict |
|---|---|---|
| `[00:05:00]`, `[00:02:00]`, `[00:04:00]`, `[00:22:00]` are not markers | **None of the four is a marker** | ✅ |
| `[00:18:00]` exists and reads *"We have our levels."* | ✅ exact | ✅ |
| *"peak formation"* occurs once, `[00:11:48]` | **1** | ✅ |
| `VISUAL_INDEX.md`: 27 files, twelve byte-identical `extracted_jpeg_NNNN` / `raw_extracted_NNNN` pairs | **12/12 SHA-256 matches**, all twelve of the named indices | ✅ |
| **15 distinct images across 27 files** | 25 `.jpg` (13 distinct: 12 pairs + 1 singleton) + 2 `.png` = **15 distinct**, hashed | ✅ **exact** |

**The `Q-005` audit is the strongest quarantine record in the project.** Its `VISUAL_INDEX`
finding is a failure mode V01's and V04's checks would not have caught, and it says so.

---

## 2. CITATION AND QUOTATION AUDIT

Every `*"…"*` fragment in the six V05 artifacts plus the two registers was extracted
mechanically and matched against the transcript at marker resolution, with elided quotes
split on `…` and each fragment checked separately.

| File | Quoted fragments | Resolved | Genuine defects |
|---|---|---|---|
| `V05_TRANSCRIPT.md` | 73 | 73 | 0 — the 17 apparent misses are all quotations *of the Whisper re-transcription* or of the dropped pre-ingestion header, each labelled as such |
| `V05_SOURCE_NOTES.md` | 186 | 185 | **1** (R1's `M3`) |
| `V05_INTERPRETATION.md` | 12 | 12 | 0 |
| `04_SCREENSHOTS/V05/INDEX.md` | 65 | 65 | 0 — the unmatched ones are **slide text**, correctly not in the audio |
| `V05_HOMEWORK.md` | 16 | 16 | 0 |
| `V05_MASTERY_REPORT.md` | 3 | 3 | 0 quotation defects (but see `m2`) |
| Registers, V05-labelled rows | 39 | 39 | 0 |

**Cross-lesson citations were checked against the other lessons' transcripts and all resolve:**
V04 `[00:18:24]` *"try to identify the high of the week and the low of the week"* ✅ exact;
V04 `[00:15:43]` *"25 to 50 pips above and below the blue box"* ✅ exact; V02 `[00:20:37]`
*"half-batman"* ✅; V04 `[00:26:56]`/`[00:26:59]` — the handover boundary ✅.

**Nonexistent-marker sweep.** Three V05 citations name a timestamp that is not a marker, and
**all three point into the same 15-second window** — see `m1`. Every other nonexistent marker
in the V05 files is either explicitly labelled as another lesson's, or is a deliberate
quotation of a fabricated file's invented timestamp in `QUARANTINE_REGISTER.md`.

---

## 3. HOMEWORK — THE DATA QUESTION, ANSWERED DIRECTLY

**The requirement was that prices come from TradingView's OHLC legend and not from pixel
colours. They do, and it is verifiable in the committed script.**

`scripts/tv_harvest_v05.mjs` opens the Data Window with `Alt+D`, reads
`.widgetbar-page` `innerText`, and parses
`/Open\s+([\d.]+)\s+High\s+([\d.]+)\s+Low\s+([\d.]+)\s+Close\s+([\d.]+)/`.
**There is no canvas read, no `getImageData`, and no colour comparison anywhere in the
harvester.** The V02 `MAJOR` (`E06`/`E19`) — a price line drawn in the bullish-candle colour
corrupting a pixel read — cannot recur through this pipeline.

**Every figure in `V05_HOMEWORK.md` was recomputed from the committed JSON this session:**

| Claim | Recomputed | Verdict |
|---|---|---|
| 480 / 480 / 480 / **476** week bars | identical | ✅ |
| First/last bar `2026-08-02 21:00` → `2026-08-07 20:45` (USDCHF from `22:00`) | identical | ✅ |
| **1,916 bars, 1,912 transitions, 1,912 continuous, 0 breaks** | **1,912 / 1,912** | ✅ |
| Per-day bar counts, incl. USDCHF's **8** on 08-02 vs 12 | identical, all four pairs | ✅ |
| EURUSD `1.15808` @ `08-07 12:45` / `1.15003` @ `08-03 15:30`, 80.5 pips | identical | ✅ |
| GBPUSD `1.35089` @ `08-07 13:15` / `1.34175` @ `08-03 18:00`, 91.4 pips | identical | ✅ |
| USDJPY `158.572` @ `08-07 00:45` / `155.228` @ `08-03 00:45`, 334.4 pips | identical | ✅ |
| USDCHF `0.81356` @ `08-06 15:45` / `0.80552` @ `08-02 22:00`, 80.4 pips | identical | ✅ |
| Last pre-week bar `2026-07-31 20:45`, all four | identical | ✅ |
| 687 raw bars per pair | **687 × 4** | ✅ |

**The USDCHF exclusion is correct and is the mark of an honest submission.** Its week low
`0.80552` is the *open of its first available bar*, so it sits on the data boundary; the file
flags it, excludes USDCHF from the scoped result, and reports 3-of-4 separately. The
Friday-high / Monday-low observation is explicitly refused as a finding at n = 3. Verified:
all three non-excluded highs fall on Fri 08-07 and all three lows on Mon 08-03.

**The V04 `M1` defect is fixed at source and the fix is independently corroborated.** V04's
remediation derived USDCHF's `476 = 12 + 29×16` from cadence; V05 derives 476 from
timestamps, on a different week, a different year and a different harvester, and shows the
*cause* — the feed publishes no USDCHF bar between 21:00 and 22:00 on the Sunday open. **This
is the project's second true cross-session replication.**

**The D-025 discipline in the homework is exemplary.** The charts mark day separators, the
week extremes and the drawing convention; they refuse levels, anchor, cycle labels, entries,
stops and targets. The footer burned into every image states the exclusion, so a frame that
escapes the directory carries its own provenance. **A homework artifact that marked levels
would have looked more like the lesson and been wrong.**

---

## 4. SCREENSHOT CLAIMS vs THE ACTUAL IMAGES

Frames were opened and magnified. Claims were not read for plausibility.

| Frame | Claim | Verdict |
|---|---|---|
| 4a `00-06-20` (2×) | Available: `Fibonacci Arcs`, `Fibonacci Expansion`, `Fibonacci Channel`, **`Rectangle`** (highlighted), `Triangle`, `Andrews' Pitchfork`, `Cycle Lines`, **`Text label`** (boxed **T**). Selected: `Crosshair`, `Vertical Line`, `Horizontal Line`, `Trendline`, `Ellipse`, **`Text`** (plain **A**), `Arrows`. Annotations *"Select"*, *"then Click"*, `Insert ->` | ✅ **exact, every item, both icons** |
| 21 `00-36-54` (2×) | Header `GBPUSD,M15  1.58700 1.58719 1.58691 1.58703`; sub-panel `TDI_MMM 54.6718 55.0688 53.6150`; `Shark Fin` boxed on the sub-panel; `1/2 Batman`; `Enter`; axis `14 Feb 2012`, `07:30`–`18:30` | ✅ **exact, all five readings** |
| 26 `00-40-04` | Title `67342442: FXDD - MetaTrader - Demo Account - [GBPUSD,M15]`; taskbar `10:31 PM 3/25/2012`; status bar `4 Majors`, `2012.01.04 01:15`, `O: 1.56413 H: 1.56418 L: 1.56374 C: 1.56381 V: 352`; `3 Hits to the Hi`, `Level 3` | ✅ **exact** — and see `m3` for what the row omits |
| 27 `01-04-58` | Status-bar OHLC **declined as illegible** | ✅ **the right call**, and the V04 `M6` precedent for saying so |

**The OHLC ordering check is real, not decorative.** Frame 21: `L 1.58691 ≤ O 1.58700 ≤
C 1.58703 ≤ H 1.58719`. Frame 26: `L 1.56374 ≤ C 1.56381 ≤ O 1.56413 ≤ H 1.56418`. A misread
digit would very likely break the ordering; it does not.

**The on-screen session date is a genuine addition.** `10:31 PM 3/25/2012` corroborates from
*inside* the recording a date the transcript header derived from the filename alone.

---

## 5. FINDINGS — NEW THIS ROUND

All four are **additional to** R1's `M1`–`M6`, which this session independently reached the
same conclusion on where it examined the same ground (`M1` and `M6` in particular).

### MINOR

#### m1 — `C-003` is named three times for a check that belongs to `C-004`, and the error has propagated into `V05_REVIEW_R1.md` (`E20`)

The record actually checked against V05 and struck off is **`C-004` — "London session open:
3:30am printed against 4:00 spoken"**. The strike-off is written correctly and in the right
place, at `CONTRADICTIONS.md` line 798, inside the `C-004` record, and its reasoning is sound.

**`C-003` is "Whether M and W formations can fail."** It has nothing to do with clock times,
it names no next candidate, and **no V05 check was performed on it at all** — there is no V05
text anywhere inside the `C-003` record.

Four sites name the wrong record:

| File | Text |
|---|---|
| `CONTRADICTIONS.md` STATUS block, line 23 | *"`C-003` was checked against V05 and struck off as negative."* |
| `CONTRADICTIONS.md` § "V05 PASS", line 845 | *"**`C-003` was additionally checked…**"* and *"See the update inside the `C-003` record."* (two references) |
| `V05_MASTERY_REPORT.md` §J | *"`C-003` named V05 as its next candidate; checked and struck off as negative"* |
| **`18_REVIEW/V05/V05_REVIEW_R1.md` §6, dimension O** | *"`C-003` struck off: zero clock-time tokens in the body, re-measured this session with markers excluded"* |

**The substance is right and the underlying check reproduces exactly** — re-measured this
session over the body with markers excluded: `HH:MM` **0**; `N am/pm` **2**, both the ASR
garble *"the 50 am in"* at `[00:20:57]` and `[00:22:14]`; `o'clock` **0**; `GMT` **0**;
`EST` **0**; *"New York time"* **0**; `London` **2**, at `[00:24:46]` and `[00:31:26]`, with
no hour attached to either. Nothing about `C-004`'s disposition changes.

**Why it is charged rather than waved through.** A future session reading the STATUS block
learns that `C-003` — the *"M's and W's will not fail"* record — was tested against V05 and
came back negative. It was not tested at all. This is the same class as V04 R1's `M3`
(ambiguity cross-references pointing at the wrong records), and R1's `N5` claim that *"all
four status blocks are current"* does not survive it: `CONTRADICTIONS.md`'s status block
contains a false statement about its own contents.

**Required:** correct all four sites to `C-004`. `V05_REVIEW_R1.md` must **not** be edited
(`REVIEW_PROTOCOL.md` §11) — the correction is recorded here and belongs in R2's verification.

#### m2 — the escape clause is quoted verbatim with a count that the verbatim string does not support, and R1 affirmed it (`E01`)

`V05_MASTERY_REPORT.md` §E:

> Recorded: the day count's own escape clause (*"but up to five days"*, **four times**)…

**The literal string *"but up to five days"* occurs twice**, at `[00:11:11]` (*"This could be
after two to three days of rise or fall, but up to five days."*) and `[00:24:37]` (*"After
three days of drop, but up to five days."*). The string *"five days"* occurs four times, but
the other two — `[00:11:16]` *"sometimes five days depending"* and `[00:12:39]` *"Remember
three to five days"* — do not contain the quoted words.

**`V05_REVIEW_R1.md` §6 dimension A repeats it**: *"the 'but up to five days' escape clause is
preserved at all four occurrences"*. R1 verified that each of the four §4c rows carries the
words attributed to *it*, which is true, and did not test the separate proposition that the
escape clause appears in all four.

**This is the project's recurring verbatim-count defect, third instance and second live one.**
Open item 15 (`V02` *"level count"*, zero occurrences) is still open; open item 39 (`EMA`
*"3 times"*, actually twice) was self-caught by this very student session. The pattern is
consistent: a count is asserted over a quoted string without re-measuring the string.

**Required:** restate as *"twice verbatim, at `[00:11:11]` and `[00:24:37]`; the day-count
expectation itself is stated four times"*.

#### m3 — the same defect R1 charges as `M6` extends to a second object in the same frame (`E20`)

R1's `M6` correctly charges frame 26's unrecorded oscillator sub-panel. **The same row also
omits four printed `R = <number>` labels** — read this session at 5× on the committed PNG:
**`R = 74.6`, `R = 40.9`, `R = 40.6`, `R = 41.1`**.

This matters to a specific record. `A-018`'s V05 evidence row reads *"Printed chart labels
`R = 24.6`, `R = 18.8`, `R = 29.5` (frame `V05_00-25-54`) and `R = 39.0` (frame
`V05_00-24-24`)"* and concludes *"V05 adds four more labels"*. **V05 adds at least eight**,
and the four unrecorded ones are a different evidentiary class from the other four: they are
on the presenter's **live platform**, not on a deck slide, which is the stronger form of the
observation `A-018` is accumulating — that `R` is a routine auto-generated annotation rather
than a risk multiple.

**It does not narrow `A-018`.** Guest material, `D-025`; and V05 still states no stop and no
target, so nothing checks an R-multiple reading.

**Required:** add the four labels to frame 26's `INDEX.md` row and to `A-018`'s V05 row, and
correct *"four more labels"* to the true count, scoped *"printed, not spoken; live platform"*.

#### m4 — §4c's framing sentence over-generalises its own table (`E02`)

`V05_SOURCE_NOTES.md` §4c heads its four-row table:

> Repeated four times, **always with the same escape clause**:

**Two of the four rows carry no escape clause**, in the quoted text or in the adjacent
context, verified by reading the surrounding markers:

| Row | Transcript | Escape clause? |
|---|---|---|
| `[00:11:11]` | *"…but up to five days."* | ✅ |
| `[00:15:47]` | *"So you notice three days of drops you're expecting a reversal."* → `[00:15:52]` *"I'm letting my money out."* | ❌ none |
| `[00:16:35]` | *"Three days of drop."* → `[00:16:36]` *"Expect a reversal."* → `[00:16:39]` *"You know how to draw the trend lines."* | ❌ none |
| `[00:24:34]` | → `[00:24:37]` *"After three days of drop, but up to five days."* | ✅ |

**The rows themselves are accurate; the sentence above them is not.** It is the source of
`m2` — the mastery report compressed *"repeated four times, always with the escape clause"*
into *"the escape clause, four times"*, which is how a framing sentence becomes a false
verbatim count one file downstream. **Charged here rather than only at `m2` because this is
where it originates.**

**Required:** restate as *"Repeated four times; two of the four carry the explicit
`up to five days` escape clause"*.

### NOTE

- **`n1` — this session independently reached R1's `M1` and `M6`, and adds one site to `M1`.**
  R1 lists two wrong citations for the `[00:57:35]`–`[00:57:36]` passage. There is a **third**
  in the same cluster: `AUTOMATION_AMBIGUITIES.md` `A-042` cites `[01:01:39]` for *"for the
  DMR, I kind of use the ellipse to show the moving average crossover"*; the words are at
  **`[00:57:39]`**. All three defects map `00:57:3x` → `01:0x:3x`, which looks like one bad
  offset applied to a cluster rather than three independent slips. **Fix all three together
  and check for a fourth.**
- **`n2` — `E11` has re-escalated.** V04 R1 de-escalated the citation class after three clean
  lessons. V05 carries four nonexistent-marker citations (`n1`'s three plus R1's `M2`
  off-by-one). Open item 7's proposed `STUDY_PROTOCOL.md` amendment — cite the marker the
  quoted sentence's *first words* fall under — would have caught the off-by-one but not the
  cluster; the cluster needs a mechanical existence check. **Worth raising at
  `CUMULATIVE_25.md` with open items 7 and 14.**
- **`n3` — `A-043`'s closure is AFFIRMED, on a narrower basis than the record claims.** The
  toolbar dialog was verified at 2×: MT4's two text objects carry icons that are literally
  `A` (`Text`) and `T` (`Text label`), so *"use the one that says A, don't use the one that
  says T"* means **use `Text`**, and *"E"* is a mishearing of *"A"*. The record's *"MT4
  carries exactly two text objects"* is one step beyond what the frame shows — the `Available`
  list is scrolled and scrollable — but **both named objects and both icons are visible, which
  is all the argument needs.** The closure concerns a platform artifact and this lesson's own
  ASR, not methodology, so no instructor record is closed on guest evidence. **Affirmed, not
  downgraded.** Suggest scoping the sentence to *"the two text objects MT4 offers here"*.
- **`n4` — the mastery report's honesty is the reason this lesson is cheap to review.**
  `REVIEW REQUIRED` rather than `PASS`, with the single reason stated in the first screen;
  five self-nominated weak points; a correction issued against the session's own committed
  files rather than silently patched; `NOT APPLICABLE` explicitly refused for dimension F
  where it would have hidden real work. **`REVIEW_PROTOCOL.md` §18 is satisfied.**

---

## 6. THE SEVENTEEN DIMENSIONS

| | Dimension | Grade | Basis |
|---|---|---|---|
| A | Source fidelity | **PASS** | 73/73 transcript, 185/186 source-note fragments verified at marker resolution. One smoothed quotation (R1 `M3`). `m2`/`m4` are counting defects, not misquotations |
| B | Completeness | **PASS** | Ten blocks, whole runtime, no fenced tail; the frames close the coverage claim at the replay button |
| C | Provenance | **PASS with `E11` recurrence** | Every claim carries a marker or a named frame. Four citations point at nonexistent or adjacent markers (`n1`, `n2`, R1 `M1`/`M2`) |
| D | Explicit vs inferred | **PASS** | Classifications present and used; `INTERPRETED RULES` is deliberately empty and says so |
| E | Chart recognition | **NOT APPLICABLE — upheld** | No admissible pattern criterion exists in V05 to recognise |
| F | Counterexample testing | **PASS, excluded** | Nine worked passes recorded and correctly not promoted (`A-049`) |
| G | Manual backtest | **NOT PERFORMED — upheld** | Backtesting guest criteria would grant them the standing `D-025` denies. See §7 |
| H | Hindsight / lookahead | **PASS** | Flashcard crops cut **at** the decision candle with nothing to the right — the hard-right-edge discipline made into a file |
| I | Outcome vs rule application | **NOT APPLICABLE** | No trades, no outcomes |
| J | Sample quality | **PASS** | n = 3 refused as a finding, in the file that produced it |
| K | Homework review | **PASS** | Every figure recomputed from committed JSON; 1,912/1,912; the H3 substitution declared rather than counted silently |
| L | Teach-back | **PASS** | The one-paragraph summary is accurate and does not over-read |
| M | Blind recognition | **NOT APPLICABLE** | Same ground as E |
| N | Ambiguity review | **PASS** | `A-042`–`A-049` sound; six records extended, none narrowed; `A-043` affirmed (`n3`) |
| O | Contradiction review | **PASS on substance, `MINOR` on record identity** | Nil return correctly reasoned; the struck-off record is `C-004`, named as `C-003` four times (`m1`) |
| P | Machine-rule firewall | **PASS** | Every V05 record `DO NOT CODE`; no constant proposed anywhere; `D-010` intact |
| Q | Claimed accuracy | **PASS** | The guest's *"80%+"* / *"80, 80, 85%"* recorded with provenance as a hypothesis under `D-009`, explicitly not reconciled with V01's 90–95% and explicitly not evidence about the method |

---

## 7. THE ESCALATED RULINGS

This round **concurs with `V05_REVIEW_R1.md`** on all three and adds nothing except the
observation at `m1`'s end. Recorded briefly so R1B stands alone:

1. **Dimension G `NOT APPLICABLE` — UPHELD**, but the *recorded reason* must change. It is
   not *"states no testable rule"*; it is *"states rules excluded by `D-025`"*. Left as
   written, V06–V21 will read it as precedent for the wrong proposition.
2. **Dimension F `SUCCESS AFTER SOURCE REVIEW` — UPHELD.** Refusing `NOT APPLICABLE` was
   correct; the performable half was performed on real data and grading it away would have
   hidden it.
3. **Dimension B `NOT APPLICABLE` — NOT AVAILABLE AS LABELLED.** `D-018` names B among the
   eight dimensions that *"always apply and are never waived"*, and `D-019`'s table grants
   `NOT APPLICABLE` **for F and G only**. Same mis-disposition as V04 R1's `N1`. The prose
   beneath the label is accurate, so this is a **relabelling**, not a regrade. **The student's
   own escalation (open item 36) covers F and G but not B — it should cover B too.**
4. **The third disposition (open item 36) is genuinely needed.** V05 is the first lesson whose
   work is *excluded by decision* rather than absent (`NOT APPLICABLE`) or postponed
   (`DEFERRED`). **Owner decision**, not a reviewer's.
5. **`A-042`'s out-of-corpus dependency (open item 35) is real and correctly escalated.**
   `DMR` occurs **9** times in the body, and the operative detail for levels/reset, nameable
   patterns, railroad-track size, traps and checklists is deferred to it at five of them.
   **The record's warning is the important part and must survive: an unavailable source is a
   reason to leave a record OPEN, never a reason to infer what it said.**
6. **Open item 39 — the `EMA` correction.** Re-measured: the token occurs **twice**, at
   `[00:23:52]` and `[01:05:53]`. **Confirmed.** The fix belongs in `V05_TRANSCRIPT.md`
   § TRANSCRIPTION NOTES and `QUARANTINE_REGISTER.md` `Q-005`, applied in place with the
   superseded text retained per `REMEDIATION_PROTOCOL.md` §2. `A-020`'s V05 row already
   states the corrected figure and needs no change.

---

## 8. REQUIRED ACTIONS (this round only — R1's eight stand alongside)

1. **`m1`** — correct `C-003` → `C-004` at `CONTRADICTIONS.md` line 23, line 845 (×2) and
   `V05_MASTERY_REPORT.md` §J. **Do not edit `V05_REVIEW_R1.md`** (§11); its instance is
   recorded here and verified at R2.
2. **`m2`** — `V05_MASTERY_REPORT.md` §E: restate the count. Verbatim twice; expectation four
   times.
3. **`m3`** — add `R = 74.6 / 40.9 / 40.6 / 41.1` to frame 26's `INDEX.md` row and to
   `A-018`'s V05 row; correct *"four more labels"*.
4. **`m4`** — `V05_SOURCE_NOTES.md` §4c: restate the framing sentence.
5. **`n1`** — correct `A-042`'s `[01:01:39]` → `[00:57:39]` together with R1's `M1` pair.
6. **Dimension B** — re-dispose, retaining the present text verbatim (concurs with R1 §8.8).
7. **Owner** — resolve §0.2: the `R1B` filename, the `REVIEW_INDEX.md` reconciliation to
   **10 minors**, and whether parallel reviews are intended.
8. **Owner** — open items 35 and 36 (the out-of-corpus dependency; the third disposition).

---

## 9. WHAT THIS ROUND DID NOT RE-AUDIT (`REVIEW_PROTOCOL.md` §4)

- The 829-frame sweep was not re-run. The 30 curated frames were opened; the sweep's integrity
  rests on the byte-level proof in `INDEX.md` § CAPTURE PROVENANCE, which is internally sound
  (one differing byte at offset 18, the `frameRate` `UI16`) and which R1 examined.
- V01–V04 artifacts were touched only where V05 cites them.
- `V05_REVIEW_R1.md` was **read but not audited**. Where this round's measurements contradict
  it (`m1`, `m2`), that is stated as a finding about the underlying artifacts, not as a review
  of the reviewer.

---

## 10. DECISION

```text
LESSON: V05
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- None.

MAJOR ISSUES:
- None.

MINOR ISSUES (new this round, additional to R1's M1-M6):
- m1 (E20) C-003 named four times for a C-004 check; propagated into R1
- m2 (E01) "but up to five days" counted four times; verbatim twice
- m3 (E20) four unrecorded printed R = labels in curated frame 26
- m4 (E02) §4c "always with the same escape clause" false for 2 of 4 rows

CONCURRENT-SESSION DAMAGE:
- STUDENT LAYER: NONE. One pipeline, nine commits, A-001..A-049 and
  C-001..C-005 contiguous and duplicate-free. No cleanup required.
- REVIEW LAYER: ONE LIVE COLLISION. A second reviewer session wrote
  18_REVIEW/V05/V05_REVIEW_R1.md and +106 lines of REVIEW_INDEX.md
  during this session. Neither was overwritten. REVIEW_INDEX.md is
  deliberately NOT updated by this round. Owner action, §0.2.

REQUIRED ACTIONS: 6 (§8), plus 2 owner actions
ADVANCEMENT: AUTHORIZED — V06 gate OPEN under D-024
V05 STATUS: NOT COMPLETE until all ten minors are applied and re-reviewed
```

**Would I be comfortable letting future code depend on this interpretation?**
(`REVIEW_PROTOCOL.md` §18.) **Yes.** V05's interpretation makes one load-bearing claim — that
the method is not in this lesson — and that claim survived an audit of the audio, the frames,
the committed data and the registers. The four defects found here are all in *counting and
cross-referencing*, none of them in what V05 was understood to mean. **A lesson that yields no
doctrine cannot corrupt downstream learning, and this submission resisted the temptation to
manufacture some.**

---

*Round R1B — a parallel second opinion, not a superseding round. `V05_REVIEW_R1.md` stands
unaltered (`SETUP_ISSUES.md` I-002, `REVIEW_PROTOCOL.md` §11). Remediation of both rounds →
`V05_REVIEW_R2.md`.*

---

## ⚠ STATUS — APPENDED AT V05 R2, 2026-08-11 (append-only; nothing above was altered)

**This round is FOLDED into the V05 R1/R2 lineage. `18_REVIEW/V05/V05_REVIEW_R2.md` is now
the operative list of what V05 owes; §5 and §8 above should be read as historical. This file is NOT
superseded, NOT invalid, and NOT to be edited or deleted — it stands as written
(`SETUP_ISSUES.md` I-002, `REVIEW_PROTOCOL.md` §11).**

R2 re-derived all four minors and note `n1` from the transcript and the pixels, independently
of this file's prose, and **confirmed every one of them as real and unremediated at `HEAD`**:

| This round | Adopted at R2 as | Open item | R2 verdict |
|---|---|---|---|
| `m1` — `C-003` named for a `C-004` check | `M7` | 47 | ✅ **CONFIRMED VALID** |
| `m2` — *"but up to five days"*, four times vs twice verbatim | `M8` | 48 | ✅ **CONFIRMED VALID** |
| `m3` — unrecorded printed `R =` labels in frame 26 | `M9` | 49 | ✅ **CONFIRMED VALID** (with one correction to this round's reading — see R2 §2) |
| `m4` — §4c *"always with the same escape clause"* | `M10` | 50 | ✅ **CONFIRMED VALID** |
| `n1` — `A-042` cites `[01:01:39]`; words at `[00:57:39]` | `M11` | 51 | ✅ **CONFIRMED VALID — escalated `NOTE` → `MINOR`** |

**Why this file was kept rather than voided.** `REVIEW_PROTOCOL.md` §11 and `SETUP_ISSUES.md`
I-002 forbid overwriting a review round, and a valid review is not made invalid by having been
produced concurrently. This round's two refusals — declining to write over `V05_REVIEW_R1.md`,
and declining to race another session's uncommitted `REVIEW_INDEX.md` — were **correct**, and
its §0.2 disclosure is why the collision was reconstructable at R2 at all.

**The defect this round left behind** was not its existence but its invisibility: at R2 it was
referenced **zero times** in `REVIEW_INDEX.md` and **zero times** in `LOG.md`, so the
remediation session never saw its four findings. **That is now fixed** — R1B is recorded in
`REVIEW_INDEX.md` as a parallel round of the V05 R1 lineage, and its findings are tracked as
open items 47–51 under the labels `M7`–`M11`. The R1 round's true minor total is **10**
(`M1`–`M6` + `m1`–`m4`), as this round asked. The gate is unaffected either way: 0 `CRITICAL`,
0 `MAJOR`.

**No further `R<n>B` file may be created** unless the owner adopts parallel review as policy —
carried as R2 §8 owner action **D**.

*See `V05_REVIEW_R2.md` §0 for the full reconciliation.*
