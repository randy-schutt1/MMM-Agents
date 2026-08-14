# V16 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | **V16** · `Bootcamp1 Wk7 050612 Part2 (45mins).swf` · session **2012-05-06, Week 7**, Part 2 of the two-part recording whose Part 1 is V15 · lesson title **`Pivot Points`** (PRINTED) |
| Review version | **R1** |
| Review date | 2026-08-14 |
| Previous review | none |
| Reviewer branch | `review/v16`, cut from the integration branch @ `cd6d1cb` (**post-`review/v15` merge**) |
| Submission reviewed | `video/v16` @ `e7a51cd` (10 commits, `588726c`…`e7a51cd`) |
| Independence | **`D-003` satisfied.** This session authored no V16 artifact. It located the source `.swf` from `SOURCE_MANIFEST.md` and **re-computed its SHA-256**; extracted the audio itself and **re-transcribed every load-bearing passage on a third engine** — `faster-whisper` / CTranslate2 `large-v3`, against the pre-ingestion ASR and the student's `openai-whisper` `large-v3-turbo`; **re-measured the pivot-grid slide's nine level positions in its own pixel code**; **re-derived `PT-044` end to end** in code sharing no line with `run_pt044.py` or `mmm_lib`, parsing the raw HistData CSVs directly, written from the pre-registration **at commit `9cc1cae`, before the runner existed**; **recomputed `A-106`'s Monday pivot fork from raw M1 bars**; re-hashed all three `Q-017` files and re-ran the `Q-016`/`Q-017` diff and the token census in its own parser; and **opened nine frames as images and read their burned-in timecodes** |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 4 MINOR, 11 NOTE.**

Under `DECISIONS.md` **D-024**, a round carrying zero `CRITICAL` and zero `MAJOR` **opens the gate
for V17.** The four minors are carried in `REVIEW_INDEX.md` as items **222–225** and are owed
before V16 can reach `COMPLETE`. **None of them changes a lesson conclusion, a record's
disposition, or `PT-044`'s verdict.**

**Confidence: HIGH.**

---

## §0 — ⚠ THE `D-004` TIMING QUESTION, ANSWERED FIRST BECAUSE EVERYTHING ELSE DEPENDS ON IT

The V16 session declared, in `COURSE_PROGRESS.md`, in `V16_MASTERY_REPORT.md` and in `LOG.md`, that
it **opened V16 with its `D-004` gate CLOSED** — V15's R1 had not returned — on the owner's
2026-08-14 authorisation to continue the pipeline for V16 onward. It declared this rather than
glossing it, and it invited the reviewer to treat the whole artifact set as **PROVISIONAL pending
V15's R1**.

**That condition is now discharged, and this review verified it rather than accepting it:**

| Check | Result |
|---|---|
| Does `18_REVIEW/V15/V15_REVIEW_R1.md` exist on integration? | ✅ **YES**, merged at `cd6d1cb` |
| Its verdict | ✅ `REVISE` — **0 CRITICAL / 0 MAJOR / 6 MINOR / 13 NOTE**, HIGH confidence |
| Was it independent (`D-003`)? | ✅ Yes — its own executive block and item 214 record an independent worktree and re-derivation |
| Does that open the V16 gate under `D-024`? | ✅ **YES, unconditionally.** Zero `CRITICAL`, zero `MAJOR` |
| Are V15's six minors (items 197–202) merged? | ⚠ **NO — all six still read `MINOR — OWED` on integration** |

**The finding is that the timing defect is fully cured and V16 is clear to be reviewed normally.**
The gate that would have held V16 opened **without conditions**, on the merits, by a review that
found nothing above `MINOR`. Under `D-024`'s own words a gate-opening round means *"work on lesson
N+1 may begin immediately; the minor corrections do not have to be applied first."* **V16's
parallelism was therefore procedurally irregular at the moment it happened and substantively
harmless in the outcome** — it took a risk that did not materialise.

⚠ **The outstanding V15 minors were checked for contamination of V16 specifically, not waved
through.** The one with any reach into V16 is item **197** (`A-095` misidentifies which of its own
three figures `PT-043` tested). **V16 writes an addendum to `A-095`.** That addendum was read
against item 197: it records V16 `[00:23:24]` as *durability evidence* for the weekly-range figure
and does **not** restate or inherit the misidentified-figure sentence. **No V16 artifact carries
item 197's error forward.** Items 198–202 touch V15's `INDEX.md` §0.3, `COURSE_PROGRESS.md`'s V15
row, `Q-016`, the Orlando conclusion and `C-022`'s `D-048` rung — **none is inherited by a V16
artifact.**

**Conclusion: V16 is reviewed here as an ordinary submission, not as a provisional one.** The
declaration itself is charged as a `NOTE` (item 226), not a defect — declaring a deviation in three
places and naming the reading that would go against you is the behaviour the protocol wants.

---

## §1 — SOURCE MATERIAL REVIEWED, BEFORE ANY STUDENT CONCLUSION

| Source | Reference | Result |
|---|---|---|
| The `.swf` itself | `Bootcamp/Bootcamp1 Wk7 050612 Part2 (45mins).swf` | **SHA-256 `ecac17c4…c538a` re-computed and MATCHES `SOURCE_MANIFEST.md`**; size **16,488,397 bytes** matches |
| Extracted audio | own `ffmpeg` extraction | duration **2675.827 s** — matches the submission's `2675.826939 s` |
| Audio, `[00:09:00]`–`[00:10:00]` | `A-100` lookback | third-engine transcription, below |
| Audio, `[00:14:15]`–`[00:14:50]` | correction #1, `A-105` | third-engine transcription |
| Audio, `[00:33:10]`–`[00:33:45]` | correction #3, `M5` | third-engine transcription |
| Audio, `[00:39:55]`–`[00:40:30]` | correction #6, `C-023` | third-engine transcription |
| Audio, `[00:34:55]`–`[00:35:40]` | the homework assignment | third-engine transcription |
| Audio, `[00:01:30]`–`[00:04:00]` | the pivot-construction span | third-engine transcription |
| Nine frames, opened as images | frames 2, 3, 10, 11, 15, 19, 23, 26, 27 | burned timecodes read; contents compared to names |
| Pre-ingestion transcript | `Bootcamp Notes/16_…/TRANSCRIPT.md` | body **SHA-256 identical** to the committed artifact |
| Quarantined notes | `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/16_…/` | all three SHA-256s re-computed |
| Raw M1 bars | `HISTDATA_GBPUSD_M1/raw/*.csv` | parsed directly for `PT-044` and `A-106` |

---

## §2 — WHAT WAS RE-DERIVED RATHER THAN READ

### ⭐⭐ `A-100`'s ADR lookback line — CONFIRMED VERBATIM BY A THIRD ENGINE

This is the single highest-value line in the file and the submission's headline claim. It was
attacked three ways.

**1. It is verbatim in the committed marker grid.** `[00:09:31]`:

> *"the ADR is calculated over the last two weeks, 15 days."*

**2. The committed transcript is not the student's own work product.** Its body is
**SHA-256 identical** (`503a54fb…16819`) to the pre-ingestion `TRANSCRIPT.md`, byte for byte across
1,130 lines. **The "copied byte-for-byte" claim is exact.**

**3. A third, independent engine returns the same words.** `faster-whisper` / CTranslate2
**`large-v3`** — a different runtime *and* a different model from the submission's
`openai-whisper large-v3-turbo` — on audio extracted from the SHA-verified `.swf`:

> `[571.6] the ADR is calculated over the last two weeks, 15 days.`

**Three engines, word for word, including the number.** `A-100`'s Tier 1 status is upheld.

The same pass independently **confirms four more of the submission's twelve corrections**:
**#1** (*"I'm getting ahead of myself. At the London Open, if the dealer breaks high in the top side
of the pivot grid, you're a seller"* — exact), **#2** (*"which is my 100 ADR, 100 pip ADR"*, so
*"180R"* is indeed ASR damage), **#3** (*"The M&W might form an M5. Oh, Steve, it wasn't M4, M3, it
was M5"* — **`M5` survives a third engine, twice in one sentence**), **#6** (*"Steve, why are you
stating the London session started on your slide when it's the daily candle that we're looking
at?"*), and **#11** (*"perhaps on the last leg of the last leg"*). **Not one correction was
contradicted.**

**The claimed internal inconsistency is arithmetically sound and is upheld.** *"Two weeks"* is
**10** trading days or **14** calendar days. **15 is neither.** The only reading that makes 15
natural is *three* five-day weeks, which contradicts *"two weeks"* directly. The record advances
`A-100` and does not close it, which is correct.

### ⭐⭐ `PT-044` — INDEPENDENTLY RE-DERIVED, AND IT REPRODUCES

Reviewer code written from `PT-044` §§3–6 **at commit `9cc1cae`, before `run_pt044.py` existed**,
sharing no line with the runner or `mmm_lib`: own CSV parser, own session-day rule, own
`America/New_York` DST handling, own 96-bucket completeness gate, own percentile function.

**The data clock was measured, not assumed** — the weekly gap-open sits at `Sun 17:00` in the raw
timestamps in **both** summer and winter, so the corpus is a fixed `UTC−5` clock, which is what
`D-031` arm A needs.

| | Reviewer | Committed | |
|---|---|---|---|
| **`W-D` arm A** `O1` | 0.0727 | 0.0725 | ✅ |
| **`W-D` arm A** `O2` | **102.60** | **102.6** | ✅ **exact** |
| **`W-D` arm A** `O3` | 115.74 | 115.8 | ✅ |
| **`W-D` arm A** `O5` | 284.35 | 284.3 | ✅ |
| **`W-E` arm A** `n` | **2175** | **2175** | ✅ **exact** |
| **`W-E` arm A** `O1` | **0.0492** | **0.0492** | ✅ **exact** |
| **`W-E` arm A** `O2` | **92.30** | **92.3** | ✅ **exact** |
| **`W-E` arm A** `O4` | **0.1163** | **0.1163** | ✅ **exact** |
| **`W-E` arm B** `n` | **1946** | **1946** | ✅ **exact** |
| **`W-E` arm B** `O2` | **93.10** | **93.1** | ✅ **exact** |
| `N2` `ADR₁₅` median `W-D` | 111.69 | 111.6 | ✅ |

**All three verdicts reproduce exactly:**

* **CEILING reading — `WEAKLY SUPPORTED`** (`O1` = 0.0727 vs 0.0725, both inside §6's `0.02–0.10`).
* **TYPICAL reading — `PARTIALLY SUPPORTED` in `W-D`** (`O2` = 102.6, inside §6's `100–150`).
* **TYPICAL reading — `CONTRADICTED AS STATED` in `W-E`** (`O2` = 92.3, below 100).

⭐ **And prediction 3 — the interesting one — is confirmed: the throwaway conspiratorial aside at
`[00:30:12]` scores better than the arithmetic the lesson is built on.** That is a real result and
it is reported the right way round.

**Pre-registration ordering re-proven from git rather than asserted:** `run_pt044.py` is **ABSENT**
from the tree at `9cc1cae` (16:14:52), present at `cc6d04e` (16:15:35), results at `59b0776`
(16:18:48). The one post-execution edit to the runner was inspected: it **clips `W-E` to
2017-01-01…2025-12-31 to enforce §4**, which the first execution had not done. **That edit tightens
compliance with the pre-registration rather than relaxing it, and the superseded figures are
preserved in `BT_V16_0001.md` §6a rather than discarded.** Correctly handled.

⚠ **One divergence, and it is item 224 below:** the reviewer's run scores **5 of 5** predictions
where the submission scores **4 of 5**. The cause is a four-day window over-run, traced exactly.

### ⭐ `A-106` — RECOMPUTED FROM RAW BARS, AND ALL FIVE FIGURES REPRODUCE

Own parse of `DAT_MT_GBPUSD_M1_2015.csv`, own floor-trader arithmetic:

| | `CPP` | `R1` | `S1` | **`R2`** | **`S2`** |
|---|---|---|---|---|---|
| **Reviewer** | −7.1 | −36.6 | +28.9 | **−72.6** | **+58.4** |
| **Committed** | −7.1 | −36.6 | +28.9 | **−72.6** | **+58.4** |

**Five of five exact.** The supporting figures reproduce too: Sunday **2015-05-31** carries
**418** M1 bars; Monday **2015-06-01**'s realised range is **133.9 pips**; the Sunday-basis `R1`
lands **0.9 pips** from the day's actual high and the Friday-basis `R1` misses by **37.5**.

⭐ **The 72.6-pip disagreement is 54.2% of the entire day's range.** `A-106`'s judgement that this
is the larger of the two forks and the one to escalate is **correct and is endorsed**.

### ⭐ `A-101`'s pixel measurement — RE-MEASURED, AND THE CONCLUSION IS STRONGER THAN CLAIMED

Own detection of the nine level-label centroids on `V16_00-01-40_…png`:

```text
R2 181.0 · M4 233.0 · R1 286.0 · M3 338.5 · CPP 391.5 · M2 444.5 · S1 497.0 · M1 549.5 · S2 602.5
gaps: 52.0 · 53.0 · 52.5 · 53.0 · 53.0 · 52.5 · 52.5 · 53.0
mean 52.69   min 52.0   max 53.0   spread ±0.50 px
```

**Nine levels, eight gaps, spread ±0.5 px — tighter than the claimed ±1 px.** The printed slide
**is** a schematic, and `A-101`'s reasoning that a real floor-trader grid cannot look like this is
**correct**: `R1→R2` measures 105.0 px against `CPP→R1`'s 105.5 px, a ratio of **0.995**, where any
real grid gives something else. **The midpoint hypothesis genuinely cannot be read off this slide.**

⚠ **Two problems with how that correct conclusion is evidenced — items 222 and 223 below.**

### `Q-017` — ALL THREE HASHES RE-COMPUTED, THE PARAPHRASE CLAIM CONFIRMED, THE CENSUS RE-RUN

| File | Bytes | SHA-256 re-computed | |
|---|---|---|---|
| `RULES.md` | 3,173 | `cd549eea…66e26` | ✅ |
| `NOTES.md` | 1,712 | `53d609ba…52ab952a`* | ✅ |
| `VISUAL_INDEX.md` | 1,253 | `733abb55…a0a0e` | ✅ |

<sub>*abbreviated; full value matches the register exactly.</sub>

⭐ **The new sub-pattern is REAL and the claim is upheld.** V16's `VISUAL_INDEX.md` is **not** a
byte clone of V15's — the SHA-256s differ and **26 lines differ** — while the structural invariant
survives intact: **same three timestamps** (`[00:02:00]`, `[00:15:00]`, `[00:30:00]`), **same three
subjects** (EMA template + Asian Box; London-open stop hunt; TDI shark fin + 5/13 cross). **A
`diff`-based duplicate check of the kind `Q-016` used would not have flagged this file.** That is
the finding, it is correct, and it matters for how the pattern is detected from here on.

**The token census reproduces 8 for 8** over the committed 377-marker body: `stop loss` 0,
`Asian box` 0, `shark` 0, `shark fin` 0, `railroad` 0, `peak formation` 0, `evening star` 0,
`5/13` 0. (`EMA` returns three hits, all of them inside the word *"email"* — so the indicator term
is absent too, which strengthens rather than weakens the entry.)

**The `[00:30:00]` row was checked against the actual frame.** `V16_00-29-10_…png` is the
`Pivots Are Intraday Support And Resistance` / `YOU Are The Filter!` bullet slide. **No TDI, no
shark fin, no EMA cross, no chart.** The fabrication is confirmed on the glass.

⚠ **`Q-017` understates its own invariant — item 225 below.**

### The frame names — 9 OPENED AND READ, INCLUDING BOTH SIDES OF THE SHARPEST SELF-CORRECTION

The session self-reported that **11 of its 34 frame names were first written from the transcript**
and did not describe their own frames, and asked the reviewer to treat those eleven as a sample and
re-check the other twenty-three. **Both halves of that instruction were followed.**

**The load-bearing self-correction is confirmed on the pixels:**

| Frame | Burned timecode | What is actually on the glass | Name |
|---|---|---|---|
| `V16_00-09-30_grid-annotated-right-column-circled` | **09:30** | `M2/M4` column enclosed in a yellow loop. **`ADR` is NOT written** | ✅ correct |
| `V16_00-10-00_grid-annotated-adr-written-top-left` | **10:00** | **`ADR` written in capitals at top-left**, column still looped | ✅ correct |

**The correction is real and the corrected names are accurate.** Moving the `A-100` lookback
citation off the frame and onto the audio was the right call — the word is genuinely not there at
`[00:09:31]`.

**Seven of the twenty-three unchecked frames were opened and read. All seven are accurate**, and
where the index quotes printed text, the quotations are verbatim:

| Frame | Verified |
|---|---|
| `V16_00-00-50_pivot-points-four-bullets-slide` | ✅ all four bullets verbatim, incl. `Red Candle Indicates M1/M3 Day` |
| `V16_00-01-40_pivot-grid-diagram-100-pips-annotated` | ✅ three columns, nine levels, yellow `100`, `PRICE AT LONDON OPEN` legend |
| `V16_00-14-25_london-session-start-2-to-3am-est-slide` | ✅ `London Session Start` / `2:00 To 3:00 AM, EST` / `SELL` / `BUY` |
| `V16_00-18-00_m3-m4-hods-m1-m2-lods-slide` | ✅ incl. `Ex: ( M1 – M3)` |
| `V16_00-25-10_price-fails-at-m3-pivot-4-times` | ✅ both printed captions |
| `V16_00-27-45_pp-are-an-adr-grid-slide` | ✅ both bullets verbatim |
| `V16_00-29-10_pivots-intraday-sr-you-are-the-filter-slide` | ✅ all four lines |

**No further naming defect was found.** The `§8a` zero-offset claim is independently corroborated
at every frame opened — filename second and burned timecode coincide in all nine.

### `A-105` — the printed slide, read off the pixels

`V16_00-14-25_…png` carries exactly `London Session Start` / `2:00 To 3:00 AM, EST` with a red
`SELL` and a green `BUY`. ⭐ **The corpus's first printed, timezone-stamped session boundary is
real.** `A-105`'s three reasons for not yet treating it as a parameter — the `EST`-in-May problem,
the competing timezone-free `[00:02:36]` window (*"At 1 o'clock or 2 o'clock or 3 o'clock depending
on when I feel like it"*, **confirmed on my own audio pass**), and the fact that it bounds only the
start — are all sound.

---

## §3 — FINDINGS

### `CRITICAL` — **NONE**

### `MAJOR` — **NONE**

> Item **222** was weighed for `MAJOR` and charged `MINOR`. The reasoning is set out in full below
> so the owner can overrule it.

### `MINOR`

#### `M1` — ⭐⭐ `A-101` DECLARES THE `M1`–`M4` CONSTRUCTION UNEVIDENCED IN V16 — AND V16'S OWN COMMITTED FRAMES CARRY THE EVIDENCE · `E20` · **item 222**

`A-101` is the record that, in its own words, *"BLOCKS the whole of V16's lesson."* It concludes:

> *"the slide is a SCHEMATIC and carries no information about the arithmetic — it would look
> exactly like this whatever the real formula is. The midpoint reading is neither confirmed nor
> refuted; it is **unsupported**."*

**The statement about the slide is correct** — this review re-measured it and got a tighter result
than the record claimed (§2). **The inference drawn about V16 as a whole is not.** `A-101`'s
`Required research` names V17–V21, the absent June 2012 web class, and a higher-resolution
re-capture of frames 17 and 18. **It does not name frames 20–25, which are in the committed set and
which answer the question.**

`V16_00-25-10_…png` shows the grid **on a real, correctly-scaled price chart**. Level lines were
detected by colour (R-levels green-tinted, S-levels red-tinted, M-levels and CPP white/yellow) and
measured:

```text
M4 230.0 · R1 294.5 · M3 388.5 · Pivot 483.5 · M2 546.5 · S1 611.0 · M1 706.5
```

**This grid is NOT equally spaced** — `Pivot→R1` = 189.0 px against `Pivot→S1` = 127.5 px. The
"schematic" objection therefore does not apply to it. And **four independent relations all hold**:

| Relation implied by the midpoint reading | Predicted | Measured | |
|---|---|---|---|
| `M3` bisects `Pivot…R1` | `R1→M3` = `M3→Pivot` | **94.0 vs 95.0** | ✅ |
| `M2` bisects `S1…Pivot` | `Pivot→M2` = `M2→S1` | **63.0 vs 64.5** | ✅ |
| `R1→M4` = ½(`R2−R1`) = ½(`Pivot−S1`) | 63.75 | **64.5** | ✅ |
| `S1→M1` = ½(`S2−S1`) = ½(`R1−Pivot`) | 94.5 | **95.5** | ✅ |

**Every one holds to within ~1.5 px, and the last two are non-trivial** — they connect the outer
levels to the inner spacing exactly as standard floor-trader arithmetic requires.

**Confirmed on a second, independent frame.** `V16_00-21-00_…png` gives dashed levels at
`291.5 · 357.0 · 425.0 · 498.0 · 571.5`, i.e. gaps of `65.5 · 68.0` then `73.0 · 73.5` — **equal in
pairs, unequal between pairs**, which is the midpoint construction over two spans of different
size, and is not reproducible by a schematic.

**Why this is `MINOR` and not `MAJOR`.** Nothing false entered the corpus. `A-101`'s operative
instruction — **`DO NOT CODE M1, M2, M3, M4`** — remains correct, because the instructor still never
*states* the formula and §25's machine-rule firewall is about what the course teaches, not about
what a chart can be measured to imply. The error is an **under-claim in the safe direction**: it
declares an evidential dead end where a live route exists. No V17 work inheriting `A-101` would be
corrupted by it; it would merely be more pessimistic than the evidence warrants. **It does not
close the V17 gate.**

**Why it is nevertheless a real finding.** `A-101` is load-bearing: `05_HOMEWORK/V16/` stopped two
numbers short *because* of it, and a later session reading *"it would look exactly like this
whatever the real formula is"* is being told not to look. **The submission measured the one frame
that could not answer the question and did not measure the five that could.**

> **Required action.** Amend `A-101`: (a) narrow the *"carries no information about the
> arithmetic"* sentence so it is scoped to the **schematic slide** and not to V16; (b) record the
> chart-frame measurement as `[VISUAL]` corroboration of the midpoint reading, explicitly **NOT** as
> a course rule and **NOT** as closure — `DO NOT CODE` stands; (c) add the chart frames to
> `Required research` in place of the claim that only a re-capture of frames 17–18 would help; and
> (d) add the one Tier-2 route the lesson itself supplies — **`mypivotcalculator.com`**, named at
> `[00:35:36]` and correctly declined for use by `V16_HOMEWORK.md` §0.3, is a tool the instructor
> directs students to for **exactly these levels**, and it is absent from `A-101`'s research list.

#### `M2` — `A-101`'s NINE-LEVEL MEASUREMENT REPORTS ONLY EIGHT LEVELS, AND THE MISSING ONE IS `R2` · `E20` · **item 223**

`A-101` states *"the y-pixel centres of the nine level labels are
`235 · 288 · 340 · 393 · 446 · 497 · 549.5 · 602.5`, giving gaps of `53 · 52 · 53 · 53 · 51 · 52.5 ·
53`"* and concludes *"**All nine levels are equally spaced.**"*

**That is eight centres and seven gaps.** Nine levels require nine centres and eight gaps. The
missing level is **`R2`**, which this review measured at **y = 181.0**, giving `R2→M4` = **52.0 px**
— inside the same band, so **the conclusion survives**.

⚠ **But `R2` is the level the record's own defeater sentence names**: *"Under every standard
floor-trader formula the `R1→R2` gap differs from the `CPP→R1` gap."* The reported measurement
contains only **one of the two** components of `R1→R2` and therefore cannot, as reported, evaluate
the very comparison it rests on. This review completed it — `R1→R2` = 105.0 px vs `CPP→R1` = 105.5
px — and the argument holds.

> **Required action.** Add `R2` at `181.0` to the measurement, restate the gaps as eight
> (`52.0 · 53.0 · 52.5 · 53.0 · 53.0 · 52.5 · 52.5 · 53.0`, mean **52.69**, spread **±0.5 px**), and
> state the `R1→R2` vs `CPP→R1` comparison explicitly, since it is the step the argument turns on.

#### `M3` — `PT-044`'s PRIMARY WINDOW STARTS FOUR DAYS BEFORE ITS PRE-REGISTERED BOUNDARY, UNDECLARED — AND THAT IS THE SOLE CAUSE OF ITS ONE "MISSED" PREDICTION · `E19` · **item 224**

`PT-044` §4 fixes `W-D` as **`2013-01-06 → 2016-06-30`**, which is `D-035`'s `DEVELOPMENT` window
exactly. **`pt044_output.txt` reports the run as `2013-01-02 -> 2016-06-30`.** Four days early.

`COMMON_PROTOCOL.md` §9 rule 7 requires that a runner/pre-registration disagreement be **reported
in `BT_V16_0001.md`**. The `W-E` clip was caught and reported this way; **the `W-D` start was not
caught at all.**

**The consequence was traced exactly, by running the reviewer's own code both ways:**

| | Pre-registered `W-D` (2013-01-06) | As actually run (2013-01-02) |
|---|---|---|
| arm A `n` | 894 | **897** ← matches committed |
| arm B `n` | 777 | **780** ← matches committed |
| arm A `O1` | 0.0727 | **0.0725** ← matches committed |
| **arm A/B `O2` delta** | **2.00 pips** | **2.05 pips** ← matches committed |
| **Prediction 4** (*"agree to within 2 pips"*) | ✅ **CORRECT** | ❌ **MISSED** |
| **Scorecard** | **5 of 5** | **4 of 5** |

⭐ **Run to its own pre-registration, `PT-044` scores 5 of 5 and prediction 4 is not a miss.** The
one failure the submission reports — and reports first, and at length — **is an artifact of a
window that was four days too wide.**

**This is charged `MINOR`, and three things keep it there.** No verdict moves (`O2` = 102.6 in both
runs; all three verdicts identical). **No seal is broken** — `2013-01-02…05` is corpus data lying
*before* `D-035`'s development window, not inside the `2016-07-01 → 2017-12-29` holdout, which
remains untouched. And **the error is self-penalising**: it made the submission look worse than the
data warranted, which is the opposite of the direction that would raise an integrity concern.

> **Required action.** Either clip `W-D` to `2013-01-06` and restate `n`, `O1`, the arm delta and
> the scorecard as **5 of 5**; or, if the wider window is preferred, declare it in `BT_V16_0001.md`
> as a §9 rule 7 disagreement and state that prediction 4's miss is a consequence of the deviation
> and not of the market. **Do not leave a reported prediction failure standing on an undeclared
> window.**

#### `M4` — `Q-017` SAYS *"every content line differs"*; THREE CONTENT LINES ARE BYTE-IDENTICAL — AND THEY BELONG TO THE INVARIANT IT IS PROPOSING AS THE NEW DETECTION KEY · `E20` · **item 225**

`Q-017` §0 records the `diff` as *"every content line differs, and NOTHING STRUCTURAL differs"* and
names the invariant as **three timestamps + three subjects**.

Re-run this session, **nine lines are byte-identical** across V15's and V16's `VISUAL_INDEX.md` —
the three `## Screenshot NNN` headers, the three `- Timestamp:` lines, **and the three
`- Visual Type:` lines**:

```text
- Visual Type: Chart / Slide Overview
- Visual Type: Annotated Chart Example
- Visual Type: Indicator / Strategy Diagram
```

**So `Q-017`'s thesis is right and its evidence is understated.** The invariant is not three
timestamps and three paraphrased subjects; it is **three timestamps, three subjects, and three
byte-identical `Visual Type` strings** — a fourth axis, and the only one that is still exact-match
detectable after the rewrite. **That makes the practical detector cheaper than `Q-017` implies**,
which is the whole point of the entry.

> **Required action.** Correct *"every content line differs"* to name the three identical
> `Visual Type` lines, and add the `Visual Type` triple to the stated invariant. The detection
> recommendation should key on it, since it survives paraphrase and is exact-match testable.

---

### `NOTE` — no action required

| # | Note |
|---|---|
| **226** | ⭐ **THE `D-004` DEVIATION IS DISCHARGED, AND THE WAY IT WAS DECLARED IS THE REASON THIS REVIEW COULD BE SHORT ABOUT IT.** V16 recorded the closed gate in three places, named the reading that goes against it (*"treat V16's whole artifact set as PROVISIONAL"*), and did not contest it. V15's R1 has since returned `0 CRITICAL / 0 MAJOR`, opening the gate unconditionally. The six outstanding V15 minors were checked individually for reach into V16; **only item 197 touches a record V16 amends (`A-095`), and V16's addendum does not inherit the error.** Procedurally irregular, substantively harmless. |
| **227** | ⭐⭐ **`D-047` NUMBERING COLLISION — SECOND CONSECUTIVE, RESOLVED AT THIS MERGE, AND CHARGED AGAINST THE PROJECT NOT THE SUBMISSION.** `video/v16` allocated items **195–200** correctly against the integration state it had synced. `review/v15` then landed at `cd6d1cb`, renumbering V15's student items to **189–196** and adding R1's findings as **197–215**. `video/v16` is the later arrival, so under `D-047` it renumbers: **V16 items 195–200 → 216–221**, applied at this merge in `REVIEW_INDEX.md`, `COURSE_PROGRESS.md`, `LOG.md` and `V16_MASTERY_REPORT.md`. **No item content changed.** ⚠ **This is the second consecutive occurrence** (V15 was the first, item 214) and item **188**'s proposed duplicate-number check in `validate_project.py` **is still unimplemented.** Two collisions in two lessons is the case for building it. |
| **228** | ⭐ **THE HOST/GUEST DETERMINATION IS UPHELD: 100% course author, 0% guest, HIGH confidence.** Re-tested rather than inherited, as `COURSE_PROGRESS.md`'s V16 GATE (d) required, even though the condition is weaker here than for V15 (V16 is Part 2 of the same recording). Across six audio segments this review transcribed independently, **no second presenting voice appears**; the only other voices are students being quoted or answered by name (*"oh, Steve"* at `[00:33:27]`, *"Okay, Frank. Franco"* at `[00:40:13]`, *"Scott, I'll answer you in a minute"* at `[00:35:02]`, *"Reese"* at `[00:41:09]`) — all of which **confirm** a single presenter fielding questions. The acoustic cross-file screen was correctly **not** run, per V07's prohibition. |
| **229** | ⭐ **THE MARKER-GRID INTEGRITY BATTERY REPRODUCES EXACTLY.** Recomputed in this session's own parser: **377** markers, strictly monotonic, **0** equal-adjacent pairs, **0** backwards steps, gaps **3 / 16 / 7.1 s**, first `[00:00:00]`, last `[00:44:30]` sitting **5.8 s** before the measured end of audio. Every figure matches. Duration agreement also reproduces — own `ffprobe` gives **2675.827 s** against the committed `2675.826939 s`. |
| **230** | **THE WORD COUNT IS 6,486, NOT 6,453 — AND NOTHING RESTS ON IT.** Whitespace tokenisation over the 377-marker body returns **6,486** (regex word tokens: 6,506), against the committed **6,453**; speech rate is therefore **145.4 wpm**, not 144.7. A ~0.5% tokenisation difference. Recorded only so a later session re-running the check is not alarmed by it. |
| **231** | **`A-106`'s COINCIDENCE WARNING COMPARES TWO DIFFERENT LEVELS.** The record notes the Sunday-basis `R1` landed 0.9 pips from the day's high while *"the same Sunday grid missed the day's low by 72.2 pips"*. The 72.2 figure is **`S2`** vs the low; the symmetric counterpart, **`S1`** vs the low, is **95.5 pips**. Both are re-derived here. The record's purpose — warning against selecting a convention from `n = 1` — is served either way, and the asymmetry makes the Sunday grid look *better* than a like-for-like comparison would. Worth one clause when `A-106` is next touched. |
| **232** | ⭐ **`A-101`'s `M5` ADDENDUM SURVIVES A THIRD ENGINE.** `faster-whisper large-v3` returns *"The M&W might form an M5. Oh, Steve, it wasn't M4, M3, it was M5"* — `M5` twice in one sentence, and the *"oh, Steve"* student-voice reading confirmed. **Three engines now.** The addendum's refusal to choose between *"his live grid has a tenth level"* and *"he misspoke twice"* is the correct disposition on this evidence. |
| **233** | **`A-105`'s SLIDE DESCRIPTION SAYS THE SLIDE *"carries nothing else"*; IT ALSO CARRIES THE RUNNING TITLE `Pivot Points`.** Trivial, and noted only because the same running title is the evidence `V16_TRANSCRIPT.md` uses for the printed lesson title. No action. |
| **234** | ⭐ **`C-023` IS CORRECTLY WEIGHTED, AND THE AMENDMENT THAT SHARPENS IT IS CONFIRMED FROM AUDIO.** Correction #6 reproduces on a third engine — the student's question **is** a single challenge sentence (*"why are you stating the London session started on your slide when it's the daily candle that we're looking at?"*), not two unrelated ones. `C-023`'s judgement that this **raises** the quality of the first answer and makes the second read as a declared teaching simplification, leaving severity unchanged and character changed, is sound. Logging a weak contradiction as weak, and saying why, is the behaviour `REVIEW_PROTOCOL.md` §23 asks for. |
| **235** | ⭐ **CALIBRATION, CHARGED AS NOTHING.** Recorded because a review listing only defects gives the next session no signal. **(1)** The **best decision in this submission is a negative one**: `A-101` tested the tempting midpoint reading, found a defeater, and wrote the defeater down **so that no later session re-derives the hypothesis as a finding.** That the defeater turns out to be too broadly scoped (item 222) does not diminish the instinct — most submissions never test their own tempting reading at all. **(2)** The **self-charge on the eleven frame names is the most valuable page in the set.** A session that filed `Q-017` for transcript-derived fabrication, then found the same failure in its own work, rendered the frames larger, looked, renamed all eleven, moved a citation from frame to audio, and told the reviewer to treat them as a sample — that is the protocol working. **This review re-checked seven of the twenty-three and found no further defect.** **(3)** `PT-044` §1a's declaration that **five of six of the lesson's propositions are untestable**, made *before* the run, is why the test's modest scope reads as honest rather than evasive. **(4)** The homework stopping **two numbers short** rather than computing `M3`/`M1` as midpoints anyway — with the first attempt that *did* compute them, and its plausible 104.8-pip answer, preserved and struck — is the single cleanest demonstration in the corpus of why `A-101` matters. |

---

## §4 — AUDIT DIMENSIONS (`REVIEW_PROTOCOL.md` §6)

| | Dimension | Grade |
|---|---|---|
| A | Source fidelity | **PASS** — every quotation checked was verbatim; three engines agree on the load-bearing line |
| B | Completeness | **MINOR** — item 222 (`A-101` misses in-set evidence) |
| C | Provenance | **PASS** — `[AUDIO]`/`[PRINTED]`/`[VISUAL]` tags are `grep`-checkable and correctly applied; the `A-100` citation was moved to audio when the frame did not support it |
| D | Explicit vs inferred | **PASS** — the midpoint reading is labelled unsupported, not adopted; `M5` is recorded without resolution |
| E | Chart recognition | **PASS** — no classification work in this lesson |
| F | Counterexamples | **PASS** — `A-101`'s defeater is a self-administered counterexample |
| G | Manual backtest | **PASS with MINOR** — item 224 (window), otherwise reproduces exactly |
| H | Hindsight / lookahead | **PASS** — pre-registration precedes the runner in git; no measure added after the run; the one post-run edit tightens compliance |
| I | Outcome vs rule application | **PASS** — the two readings are scored separately and the aside beating the arithmetic is reported as the finding |
| J | Sample quality | **PASS** — `n` = 894/2175 across two windows, both reported, never pooled |
| K | Homework | **PASS** — first attempt preserved and struck; stops where the source stops |
| L | Teach-back | **PASS** |
| M | Blind recognition | **N/A** |
| N | Ambiguity | **PASS** — `A-100`, `A-101`, `A-102`, `A-105`, `A-106` all `DO NOT CODE`; no subjective term became a constant |
| O | Contradictions | **PASS** — `C-023` logged with its mitigation and its severity argued both ways |
| P | Machine-rule firewall | **PASS** — `DO NOT CODE` on every M-level; item 222 does **not** disturb this |
| Q | Claimed accuracy | **PASS** — the 200-pip figure preserved, cited, tested, and not used as a pass criterion |

---

## §5 — REQUIRED CORRECTIONS

1. **`A-101`** — scope the *"carries no information about the arithmetic"* sentence to the schematic
   slide; record the chart-frame measurement as `[VISUAL]` corroboration (**not** closure, **not** a
   course rule, `DO NOT CODE` stands); add frames 20–25 and `mypivotcalculator.com` to
   `Required research`. **(item 222)**
2. **`A-101`** — add `R2` at `y = 181.0`; restate as nine levels / eight gaps, mean **52.69**,
   spread **±0.5 px**; state the `R1→R2` vs `CPP→R1` comparison explicitly. **(item 223)**
3. **`PT-044` / `BT_V16_0001.md`** — either clip `W-D` to `2013-01-06` and restate `n`, `O1`, the
   arm delta and the scorecard as **5 of 5**, or declare the wider window as a
   `COMMON_PROTOCOL.md` §9 rule 7 disagreement and state that prediction 4's miss follows from it.
   **(item 224)**
4. **`Q-017`** — correct *"every content line differs"*; add the three byte-identical `Visual Type`
   lines to the stated invariant and key the detection recommendation on them. **(item 225)**

**None of these is gating.** Under `D-024` they are owed before V16 can reach `COMPLETE`, and they
do not have to be applied before V17 work begins.

---

## §6 — REVIEWER QUESTIONS FOR THE OWNER

1. **Item 222's severity.** It was weighed for `MAJOR` and charged `MINOR` because nothing false
   entered the corpus and `DO NOT CODE` still stands. **If the owner reads "a blocking record
   declared an evidential dead end that its own evidence set refutes" as `MAJOR`, the V17 gate
   closes.** The reasoning is on the record so it can be overruled.
2. **Whether `A-101` may cite pixel geometry at all.** This review measured the instructor's own
   chart and recovered four consistent relations. That is evidence about **what his indicator
   computes**, not about **what he taught**. The project has no precedent for that distinction and
   `A-101` is where it will first bite.
3. **Items 195–200 → 216–221 is the second `D-047` collision in two lessons.** Item 188's validator
   check is still unbuilt. Should it now be scheduled rather than deferred?

---

## §7 — ADVANCEMENT

```text
LESSON: V16
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- NONE

MAJOR ISSUES:
- NONE
  (Item 222 was weighed for MAJOR and charged MINOR; the reasoning is on the
   record above so the owner can overrule it.)

MINOR ISSUES: 4   (items 222-225)
NOTES:       11   (items 226-235)

REQUIRED ACTIONS:
1. A-101 -- scope the "no information about the arithmetic" sentence to the
   slide; record the chart-frame measurement as VISUAL corroboration, not
   closure; add frames 20-25 and mypivotcalculator.com to Required research.
2. A-101 -- add R2 at y=181.0; restate as nine levels / eight gaps.
3. PT-044 -- clip W-D to 2013-01-06 and restate the scorecard as 5 of 5, or
   declare the window as a COMMON_PROTOCOL s9 rule 7 disagreement.
4. Q-017 -- correct "every content line differs"; add the three byte-identical
   Visual Type lines to the invariant.

ADVANCEMENT:
AUTHORIZED -- V17 GATE OPEN under D-024 (0 CRITICAL, 0 MAJOR).
  The four MINORs are owed before V16 can reach COMPLETE (D-004).
  V16's own D-004 deviation is DISCHARGED: V15's R1 returned 0C/0M and
  opened the gate unconditionally; no V16 artifact inherits a V15 R1 finding.
  The owner's comprehension/gap audit (item 185) is NOT discharged by this
  review and is not addressed by D-024.
```
