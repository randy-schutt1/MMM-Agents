# V09 — INDEPENDENT REVIEW R1

| Field | Value |
|---|---|
| Lesson | V09 — **no printed title** (`Bootcamp1 Wk2 032612 Part4 (53mins).swf`, 00:52:26) |
| Review round | R1 |
| Reviewed | 2026-08-13 |
| Reviewer | Independent Reviewer / Teacher Agent |
| Student submission | `STUDENT STATUS: REVIEW REQUIRED`, `07_MASTERY_REPORTS/V09_MASTERY_REPORT.md` |
| `D-003` separation of duties | **SATISFIED.** This session authored **no** V09 artifact. It went to the source first (`REVIEW_PROTOCOL.md` §3): re-hashed the `.swf`, re-extracted and re-measured the audio, re-derived the transcript's timestamp structure mechanically, re-derived every closed-form probability from scratch rather than from the runner, re-ran every committed script, read the load-bearing frames as images, and parsed the SWF headers of all 21 source files |
| **Review basis — READ THIS** | Branch **`review/v09`, created FROM `video/v09` at `bb4097b`** (`D-038`). **`video/v09` is NOT merged into the integration branch at the moment the review was taken**, and the two had diverged 11 commits each way. See §3 |
| Process disclosure | No owner directive was issued for this round. **Dimension B is scored under the standard protocol**, as V07 R1 and V08 R1 scored it — not carved out. See §14 |

---

## EXECUTIVE BLOCK

```text
LESSON:     V09
DECISION:   REVISE
CONFIDENCE: HIGH

CRITICAL:   0
MAJOR:      0
MINOR:      6   (M1 — E01 quote fidelity; M2 — E20 a pre-registered
                 INDETERMINATE trigger not applied; M3 — E19 a false
                 MEASURED count in the coverage block; M4 — E11 frame
                 cross-references off by one in five files; M5 — E02 an
                 unadopted reconciliation held at MEDIUM that fails at
                 the set level; M6 — E20 the capture-bug escalation
                 mischaracterises the coordinate's history)
NOTE:       8

DIMENSION B: NOT SATISFIED — blocked by D-030, structural and NOT
             attributable to the student. Scored, not carved out.
             Carries NO severity charge (see §14). Owner ruling owed on
             REVIEW_INDEX.md open item 36 — FIFTH lesson running.

CONTINUITY:  THE PREDICTION IS GENUINE AND IT IS VERIFIED IN GIT. The
             falsifiable test was committed by the V08 session at
             11:10:45 and 11:59:51; V09's transcript at 13:21:36. All
             four corroborating strands hold; strand 4 was confirmed by
             this reviewer comparing V08's end card against V09's
             opening frame image-to-image. The missing acoustic screen
             is NOT a gap — running it was PROHIBITED.

BACKTEST:    PT-035 / BT_V09_0001 REPRODUCED BYTE-FOR-BYTE by this
             reviewer. The binomial result was RE-DERIVED INDEPENDENTLY
             from first principles and CONFIRMS every figure. The N3
             self-correction is REAL: the runner printed CLUSTERING
             CONFIRMED and scored P4 RIGHT; the observation withdraws
             both. M2 is the one place the same discipline was not
             applied twice.

A-020:       RESOLVED BY COURSE — UPHELD, verified at [00:41:43].
C-010:       REFUSAL TO CLOSE — UPHELD, and on stronger ground than the
             submission gives (M5).

ADVANCEMENT: AUTHORIZED under D-024 (0 CRITICAL, 0 MAJOR).
             V10 gate OPENS. The six MINORs are carried as owed and
             must be applied before V09 reaches COMPLETE.
```

---

## 0. WHAT THIS REVIEWER VERIFIED INDEPENDENTLY, BEFORE ANY DIMENSION WAS GRADED

Nothing below was taken from a V09 artifact's own say-so. Each row is this session's own
measurement, with the method stated so it can be re-run.

| # | Claim under test | Method used here | Result |
|---|---|---|---|
| 1 | Source identity | `shasum -a 256` on the `.swf` at the canonical `Bootcamp/` path | **`b0f36b5540de…4168d4` — matches `SOURCE_MANIFEST.md` exactly** |
| 2 | Runtime 3146.815 s | `ffmpeg -vn -c copy` extract → `ffprobe` | **3146.814694 s** |
| 3 | The pre-ingestion `audio_10.mp3` is this lesson's audio | `ffprobe` on both files | **3146.814694 s vs 3146.814694 s — identical to the microsecond.** Bit rates **64001 vs 40000**, exactly the 64 k/40 k re-encode difference the transcript states. Axis 1 of the transcript's verification block is confirmed |
| 4 | SWF header: 9,441 frames at 3.0 fps | parsed the compressed header directly | **9,441 frames.** 9441 ÷ 3 = **3147.00 s.** Three independent figures agree, as claimed |
| 5 | 721 markers, 718 distinct, monotonic non-decreasing | regex `^\[\d\d:\d\d:\d\d\]$` over the verbatim body only | **721 / 718. Zero decreasing transitions. Three same-second adjacent pairs at exactly `[00:14:32]`, `[00:16:51]`, `[00:39:43]`** — the transcript's own list. First `[00:00:00]`, last `[00:52:23]` |
| 6 | Largest gap 11 s twice | same scan | **11 s twice, at `[00:07:03]` and `[00:44:56]`** — exactly as stated |
| 7 | *"Next largest 10 s, four times"* | same scan | ❌ **SEVEN times.** See **`M3`** |
| 8 | The continuity prediction genuinely preceded the answer | `git log -S` on the predicting text, then `merge-base --is-ancestor` | **CONFIRMED.** `3026a81` (V08 interpretation, *"does V09 open with section 3"*) **2026-08-13T11:10:45**; `d9e4f9e` (the `COURSE_PROGRESS.md` V09 GATE test) **11:59:51**; V09's transcript `5cd3680` **13:21:36**. Both predicting commits are ancestors of `video/v09`, both authored by a **different session**, and both precede the first V09 artifact by 1 h 22 m and 2 h 11 m |
| 9 | Strand 4 — V09 opens on V08's closing frame | **opened both PNGs and compared them** | **CONFIRMED.** `V08_00-43-10_end-card…` (burned `43:04`) and `V09_00-00-10_ring-diagram…` (burned `00:10`) are the same diagram: four rings, the same three green labels, the same two black annotations, the same two blue arrows, a red `?` at the centre. V08's carries the `replay` button; V09's does not |
| 10 | The position-sizing formula is printed, not merely spoken | **read the PNG directly** | **CONFIRMED.** Frame at burned `02:05` prints *"What makes the Risk DEFINED is the lot size we CHOOSE to put on. We multiply our account balance by .02 and divide our Stop Loss in pips into that number. That will determine the lot size."* |
| 11 | `C-012` — *"85% Win Rate"* captioning a *"7 Wins, 6 Losses"* curve | **read the PNG directly** | **CONFIRMED.** Burned `22:45`. Both lines present on one slide, the second in the presenter's own green/red |
| 12 | Broker/platform provenance | **read the PNG directly** | **CONFIRMED.** Title bar reads `67352016: FXDD - MetaTrader - Demo Account - [EURUSD,H1]`, hand-drawn `1`/`2`/`3`/`Reset` labels and week dividers visible |
| 13 | Every V09 arithmetic claim | re-derived from scratch in my own code | **All reproduce**, including the `C-014` shortfall at exactly **$61.60**, `4 × 2% = 8.0%`, `$5,000 × 1.2⁴ = $10,368.00`, `× 1.2²⁸ = $824,223.31`, break-evens 33.33 / 23.08%, and all four equity staircases |
| 14 | The binomial loss-run result | **re-derived independently** by a run-length DP recursion I wrote, not by the runner | **CONFIRMED to the reported precision.** P(≥1 four-loss run in 200) = **99.93%** at p=0.50, **54.13%** at p=0.73, **~100%** at p=0.333. Threshold for ≤5% in 100 trades: **p ≥ 84.19%** (reported 84.2%) |
| 15 | `PT-035` reproduces | re-ran `run_pt035.py` from the committed tree | **`data/pt035_output.txt` BYTE-IDENTICAL.** `pt035_results.json` unchanged |
| 16 | The homework scripts reproduce | re-ran all three | **All three rewrote their outputs and `git status` stayed clean — byte-identical** |
| 17 | The `N3` self-correction is real, not a narrative | read the committed runner output | **CONFIRMED.** `data/pt035_output.txt` line 173 prints `VERDICT on clustering: CLUSTERING CONFIRMED` and line 181 `P4 … RIGHT`. `BT_V09_0001` withdraws both and scores `P4` **VOID**. The runner's `v1` decision code (lines 356–366) does **not** encode the `N3` gate — see **`M2`** |
| 18 | Pre-registration ordering | `git log --stat` on the three commits | **`0f709d2` prereg 14:16:56 → `7c3fe2d` runner 14:18:40 → `572c87a` results 14:23:33.** §2c's closed-form anchors are present in the prereg commit. Neither file has more than one commit |
| 19 | Homework answers preceded the scorer | `git show --stat` on both commits | **`97d2c1b` 14:25:59 commits `v09_comprehension_ANSWERS.json` and no scorer; `1b29c61` 14:29:25 commits `comprehension_probe.py`.** `P-E1`–`P-E4` are inside the answers file at `97d2c1b`, before `run_equity_path.py` existed |
| 20 | Every marker citation resolves | parsed all `` `[hh:mm:ss]` `` citations in the seven V09-scoped artifacts | **230 citations, ZERO orphans** |
| 21 | The new register records' citations resolve | same, scoped to `A-065`–`A-075` and `C-012`–`C-015` | **82 distinct citations across 15 records, ZERO orphans** |
| 22 | Every quotation is verbatim | ellipsis-aware substring match of all `*"…"*` passages against the marker-stripped body | **217 quoted passages. The great majority are verbatim or correctly attributed printed slide text. FOUR are silent ASR corrections inside quote marks under an `AUDIO` tag — see `M1`** |
| 23 | The mastery report's citation counts | re-derived each file's distinct-citation count | **All seven reconcile exactly** on the distinct-citation convention: 36 / 39 / 112 / 7 / 16 / 6 / 7. **The count class is clean this round** — see `N3` |
| 24 | The capture bug is real and not a fluke | parsed the stage `RECT` from every Bootcamp `.swf` header; measured letterbox bands on committed frames | **CONFIRMED, and it generalises.** **V08, V09 and V21** declare a **1280×738** stage; the other 18 files declare **1024×786**. The recipe renders at a 1024×786 viewport, so the 1280×738 files are letterboxed — measured on the committed PNGs, uniform bands at rows 0–160 and 685–785 on V08/V09 frames and **none** on V06/V07 frames. **See `M6` and §16** |
| 25 | Validator | `python3 scripts/validate_project.py` | **103 passed, 0 warnings, 0 failures** |

### 0a. What this reviewer could NOT verify independently, stated plainly

**The Whisper re-transcription was not re-run.** The transcript's axis-2 table (six 45-second
windows, word-level similarity 0.78–0.97, and the six named ASR disagreements) is taken on the
submission's word. What was verified instead is that **every disagreement it names is present in
the transcript body as claimed** — *"staying a reset"*, *"dynamic candles"*, *"form an end"*,
*"green salt"*, *"amp complex emlement"*, *"miffed"* — and that the **M-rendering defect it names
is real**: `end`, `am`, `amp`, `amla` and `emlement` all occur at the markers given. A fabricated
verification block would not have to name its own transcript's worst defects.

**The frames were not independently re-captured.** No Ruffle/Playwright rig was stood up; that
needs an external download and was not undertaken for this round, as at V08 R1. **What was done
instead:** the load-bearing frames were **read as images**, and each carries its own burned-in
player timecode which was checked against its filename. Every one examined matched. The stage-
geometry finding in row 24 was reached from the SWF headers and the committed pixels, which is
independent of any re-capture.

**The acoustic screen was not run — and running it would have been a violation.**
`COURSE_PROGRESS.md`'s V07 GATE carry-forward prohibits using `f0_profile.py` across files. See
§2 item 1.

---

## 1. FINDINGS

### M1 — `MINOR` (`E01`, source misquote) — four silent ASR corrections inside quotation marks, under `AUDIO` basis tags

`V09_SOURCE_NOTES.md` tags each row `AUDIO` / `PRINTED` / `AUDIO+PRINTED` / `VISUAL` precisely so
a reviewer can strike the non-`AUDIO` rows and see what survives on audio alone (§0 of that
file). That mechanism only works if an `AUDIO`-tagged quotation is what the audio says. In four
places it is not:

| Where | Quoted as | The transcript reads | Tag |
|---|---|---|---|
| §3, *"His own arithmetic on the 3:1 arm"* | *"Example solid **HOD/LOD** entries can warrant a 15-pip stop loss…"* | *"Example solid **high low-day** entries…"* `[00:03:49]` | **`AUDIO`** |
| §9a, introduced as *"`AUDIO`, verbatim across five markers"* | *"What is the **grape**, Fred?"* | *"What is the **grade** Fred?"* `[00:41:25]` | **`AUDIO`** |
| §7e | *"**experience shows** me that they can grab"* | *"**experiences show** me that they can grab"* `[00:44:39]` | **`AUDIO`** |
| §5 error 3 | *"that inner shell has like I don't know what **it's** titanium or diamond"* | *"…what **it's it's** titanium or diamond"* `[00:19:55]` | **`AUDIO`** |

**Why this is charged rather than waved through.** This is the project's most durable defect
class — V02 R1, V04 `M2`, V05 `M3`, V07 `M3` — and the standard is settled: the correction lives
in a note beside the quote, never inside the quote marks. V08 met that standard by building a
checker that caught **22** instances before commit. V09's sweep verified that every cited marker
**exists** (230/230, and it is excellent — §0 row 20) but did **not** verify that the quoted
words are the words at that marker.

**Why it is `MINOR` and not `MAJOR`, stated fairly:**

1. **No conclusion moves.** `HOD/LOD` is the right expansion and is established from printed
   slides two paragraphs above the offending quote, with the ASR form named. *Grape* is correct
   and the transcript itself renders it correctly at `[00:33:21]` and `[00:41:31]`. The other two
   are a plural and a stutter.
2. **The transcript body is untouched.** Every garble is preserved there, as the transcript's own
   TRANSCRIPTION NOTES promise. Nothing was smoothed at the source.
3. **The tool that would have caught it did not exist on this branch.** `05_HOMEWORK/V07/scripts/verify_quotes.py`
   was committed to the integration branch at the V07 R2/R3 remediation, *after* `video/v09`
   branched — and it is V07-specific in any case. This is a genuine mitigating fact, not an excuse
   offered for the student.

**Required:** run `verify_quotes.py` (now reachable from integration) over the seven V09
artifacts, and for each hit either move the correction outside the quote marks with its marker,
or retag the row `PRINTED` where a slide is the actual source. **Do not edit the transcript
body.**

---

### M2 — `MINOR` (`E20`, pre-registered decision rule not applied) — `PT-035` §6 makes an `N3` failure `INDETERMINATE` for the empirical arm too, and `BT_V09_0001` neither applies that clause nor discloses it

`PT-035` §6's decision table for the claim under test reads, in the pre-registration committed at
`0f709d2` before any bar was read:

```text
| INDETERMINATE | Cells disagree across the 5%/10% boundaries, or `N3` fails |
```

and §7b is headed **"WHAT WOULD MAKE THIS TEST VOID"**, whose first item is *"`N3` fails"*.

**`N3` failed.** `BT_V09_0001` says so at length, voids the clustering arm on it, and identifies
the runner's failure to encode §7b as a defect — *"the runner applied §6's clustering rule
unconditionally; §7b makes that rule conditional on `N3` passing, and the runner does not encode
the dependency."* **That is exactly right, and the identical defect sits one decision above it.**
`run_pt035.py` lines 356–366 derive `v1` from the `run4_obs` medians alone, with no `N3` term.
The observation applies `v1`'s verdict word, and the string `INDETERMINATE` appears nowhere in
`BT_V09_0001`, the mastery report, or `LOG.md`'s V09 entry.

**What survives, and it is the larger part.** The `CONTRADICTED AS STATED` conclusion does **not**
depend on the measurement, and `BT_V09_0001` §1 says so in its own first sentence — it follows
from §2c's closed form, which was committed before the corpus was touched. **This reviewer
re-derived that closed form independently** (§0 row 14) and it holds at every hit rate the corpus
has ever measured. §5's separate argument — that `N3` condemns the comparator `(1 − p̂)⁴` while
`run4_obs` is a raw count that never touches it — is also correct on the merits, and is disclosed.

**But a pre-registration is not a document you get to read narrowly after seeing which way it
cuts.** §6's INDETERMINATE row is unambiguous and it was not mentioned. The submission
anticipated the §7b half of this and offered it for challenge; it did not see the §6 half.

**Required, and it is small:**

1. Add a block to `BT_V09_0001` §5 recording that **`PT-035` §6's own decision table returns
   `INDETERMINATE` for the empirical arm on the `N3` failure**, that the arm is therefore
   reported as `INDETERMINATE`, and that **`CONTRADICTED AS STATED` is carried on the §2c / `O4`
   closed-form basis alone** — which needs no measurement, was pre-committed, and is independently
   reproducible.
2. **Do not edit `PT-035` and do not edit `run_pt035.py`** — `COMMON_PROTOCOL.md` §9 rule 7, and
   the student is right about that.
3. The successor test already owed (escalation 3) must **encode both gates in code**, not in
   prose. A decision rule that lives only in a markdown section will be missed again.

---

### M3 — `MINOR` (`E19`, data inconsistency) — the transcript's COVERAGE block states a MEASURED count that is wrong

> *"Largest inter-entry gap 11 s, twice: at `[00:07:03]` and `[00:44:56]`. **Next largest 10 s,
> four times**: `[00:23:05]`, `[00:45:41]`, `[00:49:35]`, `[00:49:47]`."*

Re-measured by this reviewer with the block's own stated method — lines fully matching
`^\[\d\d:\d\d:\d\d\]$` in the verbatim body — there are **seven** 10-second gaps:

```text
[00:02:38]  [00:03:23]  [00:19:18]  [00:23:05]  [00:45:41]  [00:49:35]  [00:49:47]
```

Three are unlisted and the count is understated by three. **Every other assertion in the block
reproduces exactly** (§0 rows 5–6), which is why this is a defect in one cell and not a defect in
the block.

**Charged because the block declares itself MEASURED and invites the check** — *"Stated as
MEASURED, by scanning the body…"* — and because **V03 R1 charged this same block, in this same
file family, for asserting a false property of the timestamps**. V09's block corrects V03's error
(it explicitly declines to claim strict monotonicity, and it is right not to) and then introduces
a new one two sentences later.

**Required:** correct the count to **seven** and list all seven markers, with the superseded text
retained per `REMEDIATION_PROTOCOL.md` §2.

---

### M4 — `MINOR` (`E11`, provenance) — every frame cross-reference at 15 or above is off by one, in five files

`ff7b8bd` inserted a 27th frame — `V09_00-15-00_can-have-more-losers-than-winners.png` — at
**position 15** and renumbered the `INDEX.md` table. The back-references written against the
earlier 26-frame numbering were not renumbered with it. Confirmed by this reviewer against the
current table and, where it mattered, against the images:

| File | Says | The frame it means is |
|---|---|---|
| `V09_SOURCE_NOTES.md` §2d, §5 | *"frame 17 error 2"*, *"Printed complete on frame 17"* | **18** (the five-errors slide, burned `21:40`) |
| `V09_SOURCE_NOTES.md` §3 (`A-067`) | *"printed on frames 15 and 16"* | **16 and 17** |
| `V09_SOURCE_NOTES.md` §4 | *"frame 18"* for the 85% staircase | **19** (burned `22:45`, read by this reviewer) |
| `V09_SOURCE_NOTES.md` §6 | *"frames 19–21"*, *"Spreadsheet (frame 21)"* | **20–22**, **22** |
| `V09_SOURCE_NOTES.md` §7a | *"visible on frames 22–23"* | **23–24** |
| `04_SCREENSHOTS/V09/INDEX.md` | *"The broker and platform are legible (frame 22)"* | **23** (read by this reviewer: `FXDD … [EURUSD,H1]`) |
| `04_SCREENSHOTS/V09/INDEX.md` ×2 | *"frames 22, 23 and 25"*, *"frame 21"* | **23, 24 and 26**; **22** |
| `AUTOMATION_AMBIGUITIES.md` `A-065` | *"frame 17 error 2"* | **18** |
| `CONTRADICTIONS.md` `C-013` | *"frames 19–21"*, *"Frames 12, 13, 15, 18"* | **20–22**; the 85% frame is **19** |
| `CONTRADICTIONS.md` `C-015` | *"printed, frame 16"* for *"No Impulsive Increases"* | **17** |
| `V09_MASTERY_REPORT.md` | *"printed on frame 24"* for the email | **25** |

**Every content claim these references support is correct** — this reviewer read the four
load-bearing frames and each says what the index says it says. The defect is the pointer, not the
finding.

**Charged, and not treated as cosmetic, for one reason.** These numbers are the **provenance
handle for every `PRINTED`-basis row in the submission**. A reviewer or a later session following
*"frame 17 error 2"* lands on the no-impulsive-increases slide, which does not contain error 2 —
and `Q-010`, in this same submission, establishes that *"a real frame from the right lesson with
an invented description"* is the fabrication mode its own screens are weakest against. Internal
consistency between an index and the rows that cite it is worth more here than a numbering slip
normally would be.

**Required:** renumber all fourteen references above; or, better, replace the bare ordinals with
the frames' **timecodes or filenames**, which cannot be invalidated by an insertion.

---

### M5 — `MINOR` (`E02`, unsupported generalization) — the candidate `C-010` reconciliation is held at *"more likely than not"* and it fails once applied to the whole enumerated set

**The refusal to close `C-010` is CORRECT and is upheld — see §5 item 4.** This finding is
against the *confidence*, not the *decision*.

`V09_INTERPRETATION.md` Q5 records, at `MEDIUM`:

> *"the 800/200 identity is probably why the two sources disagree… this session believes it is
> more likely than not."*

and Q8 lists, as the evidence that would promote the hypothesis:

> *"`MMM-NOTES` or a lesson showing the notes' `200` is plotted on the 1-hour."*

**Neither survives the arithmetic once it is applied to the whole set rather than to its last
member.** `MMM-NOTES` p.38 enumerates **four** averages — *"the 5, 13, 50 and 200"* — and the
corpus's attested set (`A-020`, owner attestation plus `MMM-NOTES` p.66) is **five**: mustard 5,
ketchup 13, water 50, mayo 200, blueberry 800. The identity the guest states is a factor of four
(`800 × 15m = 200 × 60m`), so applying it consistently:

| Read the notes' set on the 1-hour → | maps to, on the 15-minute |
|---|---|
| 5, 13, 50, 200 | **20, 52, 200, 800** |

The `200 → 800` member lands. **The other three do not**: the corpus has a 5, a 13 and a 50 on
the same chart, not a 20, a 52 and a 200. And the corpus's own nickname mapping requires **200
(mayo) and 800 (blueberry) to be two different lines on one chart** — so identifying them as one
line seen from two timeframes contradicts `A-020` directly.

So the hypothesis reconciles **one member of a four-member enumeration and breaks the other
three**, and it collides with the record it would have to be consistent with. `C-010`'s own
Assessment block already names the better explanation — **chronology**, that the 800 entered the
method after the notes were written, which the notes' *"any other rapidly moving pair of EMA's
would achieve the same goal"* supports.

**Required:**

1. Annotate `V09_INTERPRETATION.md` Q5 with the set-level arithmetic and **downgrade the grade
   from `MEDIUM` to `LOW`**, retaining the superseded text.
2. Correct Q8's falsification row: evidence that the notes' `200` sits on the 1-hour would **not**
   promote the hypothesis on its own, because the notes' 5, 13 and 50 would then have to map onto
   a 20, a 52 and a 200 that the corpus does not carry.
3. Record the same reasoning in `C-010`'s V09 block. **`C-010` stays OPEN and the disposition
   does not change.**

---

### M6 — `MINOR` (`E20`) — the capture-bug escalation says the recipe's coordinate works *"on V01–V08"*; it does not, and V08's own index records the identical failure

**The bug itself is CONFIRMED — see §16, where this reviewer establishes it on stronger and more
general evidence than the submission had.** This finding is about how it is characterised.

`04_SCREENSHOTS/V09/INDEX.md` and `V09_MASTERY_REPORT.md` escalation 2 both state:

> *"`SWF_CAPTURE_RECIPE.md` §3's `mouse.click(512, 300)` — **the coordinate that starts the
> Camtasia player on V01–V08** — misses on this file."*

`04_SCREENSHOTS/V08/INDEX.md`, on a branch this session merged from, records:

> *"The first 529-frame sweep produced **one distinct image, 529 times**: the Camtasia splash with
> its play button still showing. `SWF_CAPTURE_RECIPE.md` §3's `mouse.click(512, 300)` **misses the
> play target on this file** — V08's splash centres its play button at approximately
> **`(512, 325)`**."*

**Same coordinate, same failure, same corrected coordinate, one lesson earlier.** V09 is the
second occurrence, not the first, and citing V08 would have converted a one-file oddity into a
reproducible defect — which is what it is.

**This is V08 R1 `M1`'s sub-class exactly: omitted available corroboration, as distinct from a
wrong or absent citation.** It is charged at `MINOR` for the same reason: the finding is sound,
the escalation is correct, the disposition (`D-038a` policy edit, owed on integration) is
correct, and nothing downstream depends on the claim that V01–V08 worked.

**Required:** correct the sentence in both files to state that the coordinate **also failed on
V08**, cite `04_SCREENSHOTS/V08/INDEX.md`, and note the stage-geometry cause established in §16.
**The recipe fix itself is not owed by the student** — it is a policy ledger, and this reviewer
has made it (§16).

---

### N1 — `NOTE` — the branch and merge state this review was taken against

**Findings of fact, established by `git fetch` and inspection at the start of this round:**

```text
video/v09          bb4097b   NOT MERGED into claude/add-documents-repository-fdfb3u
                             DIVERGED: 11 commits each way at a6ee013. Not a fast-forward.
                             Integration advanced to 4a291fe (V08 R2 merge) mid-round.
origin/video/v09   bb4097b   in sync — the work is pushed
review/v09                   THIS REVIEW. Branched FROM video/v09 at bb4097b.
```

The integration side of the divergence is the V07 R2/R3 rounds, the V08 R1 minors remediation
(`fix/v08-r1-minors`, items 64–66 applied) and — landing **during** this round — the V08 R2 round
that verified them and made **V08 `COMPLETE`**. **None of it touches a V09 artifact**, so
the review is unaffected by it — but three of its files are ledgers `video/v09` also appended to
(`LOG.md`, `CONTRADICTIONS.md`, `REVIEW_INDEX.md`), and `REVIEW_INDEX.md` in particular is
**217 lines newer on integration**.

**Consequence for this round, recorded because it changes the order of operations.** Writing this
review's `REVIEW_INDEX.md` and `LOG.md` rows against `video/v09`'s older copies and then merging
would risk reverting the newer integration content. So integration was merged **into** `review/v09`
first, and the ledger rows were written against the merged, current state. That is disclosed here
rather than left to be inferred from the graph.

One visible artefact of the divergence, and **not** a V09 defect: `04_SCREENSHOTS/V08/V08_00-43-10_…png`
still carries its pre-remediation name on `video/v09`, because V08 R1 `M3`'s rename landed on
integration after this branch point.

---

### N2 — `NOTE`, not charged — the oscillator sub-panel IS legible, and the refusal to transcribe it was conservative in the right direction

`04_SCREENSHOTS/V09/INDEX.md` records the sub-panel beneath the price pane as present, describes
it as *"at the edge of legibility"*, declines to transcribe it, and states that the row **does not
narrow `A-039`**.

This reviewer cropped and magnified the region of the frame at burned `28:45`. The header reads:

```text
TDI  MMM   59.8444 66.7359 68.0841
```

— i.e. **the same `TDI_MMM` object already recorded from V05 frame 26**, with three live values.

**No finding, and the student's disposition is upheld unchanged.** The conclusion that matters is
`INDEX.md`'s own: *"Displayed, not taught — the presenter never refers to it."* This reviewer
re-checked that: `TDI` occurs **0×** in V09's body, as `Q-010` independently measures. A legible
indicator name on a chart the presenter never mentions is provenance, not doctrine, and it does
not narrow `A-039`. **Recorded as corroboration of the frame's contents, and so that a future
session does not spend the magnification again.**

---

### N3 — `NOTE`, not charged — the count class is clean this round, and it was checked

`REVIEW_INDEX.md` carries the token/verbatim-count class as *"the single most durable defect class
in the project"* (open items 15, 39, 48, 58, 59, 61, 62). **It did not recur here.** Every
citation count in `V09_MASTERY_REPORT.md` §H was re-derived by this reviewer and every one
reconciles on the distinct-citation convention:

```text
transcript header 36   INDEX 39   SOURCE_NOTES 112   INTERPRETATION 7
HOMEWORK 16   BT_V09_0001 6   PT-035 7        -- all verified, zero orphans
```

Stated because a class this reviewer would have charged on sight deserves to be recorded when it
is met.

---

### N4 — `NOTE` — dimension B has now cost FIVE lessons and still has no vocabulary

V05, V06, V07, V08, V09. Open item 36 is owed for the **fifth** consecutive round. See §14. The
student's handling is correct and is not the problem; the absence of a ruling is.

---

### N5 — `NOTE` — the censoring concern is well-founded, and `PT-034`'s own null already shows the signature

See §5 item 7 for the full ruling. Recorded here as a finding of fact: `PT-034`'s `N1` returned
**0.2424 / 0.2426 / 0.2429 / 0.2450** against a closed-form break-even of **0.2500** — below it in
**all four cells**, consistently, in a test whose geometry is a 50-pip target against a 16.67-pip
stop inside a within-day horizon. V08 R1 read that as a null landing on its analytic value, which
it very nearly does. It is also **exactly the direction and rough magnitude a target-censoring
bias predicts**, and that reading was not available before `PT-035` §3 named the mechanism.

---

### N6 — `NOTE` — the evidence-order deviation is NOT charged, and §5 item 8 gives the reasoning

---

### N7 — `NOTE` — `C-014`'s disposition is upheld as filed

The mastery report offers `C-014` for downgrade to a note. **No change is needed.** It is already
filed at `NOTED — SELF-HEDGED BY THE SPEAKER`, its own text says the speaker's *"essentially"*
covers a 0.49% gap, and it explicitly carries the $11,960 figure as exact and the $12,500 as
approximate. The structural observation attached to it — that full restoration after four 2%
losses needs `4 / (1 − 0.08) ≈ 4.35` winning units, not 4 — is **correct**, re-derived here, and
is the useful part of the record.

### N8 — `NOTE` — a process collision this round CAUSED, disclosed against this reviewer

**One further fact belongs here and it is against this reviewer, not against the student.**
`REVIEW_INDEX.md` open item **72**, filed by the V08 R2 round, records that *"a concurrent session
moved the shared main working directory onto `review/v09` (`bb4097b`) partway through this
review"*. **That session was this one.** This review was launched in the repository's **shared
main working directory**, which was on `review/v08-r2` at the time, and creating `review/v09` there
moved it out from under a review that was still running. Two things follow, both stated plainly:

1. **`D-038` recommends a dedicated worktree and this round did not use one.** That is the exact
   condition `D-038` exists to remove, and it was not met here.
2. **The V08 R2 round detected it and absorbed it** — it re-ran every affected read in its own
   clean worktree and discarded two stale `REVIEW_INDEX.md` reads. No conclusion of that round
   rests on a read from the wrong tree, and none of this round's measurements were taken from a
   tree another session was writing to.

Recorded because item 72 is charged to `PROCESS` rather than to a lesson, and the process it
names is this reviewer's.

---

## 2. THE NINE ITEMS THE SUBMISSION AND THE REVIEW BRIEF ASKED TO BE CHECKED — ADJUDICATED

| # | Claim under test | Reviewer verdict |
|---|---|---|
| 1 | **Speaker / continuity**: 100% `GUEST`, 5th consecutive lesson; and V09's opening with V08's missing section 3 was **predicted in advance**, then confirmed on four non-acoustic strands — with the acoustic screen *not* run | **CONFIRMED ON EVERY COMPONENT, and the prediction is the strongest single thing in this submission.** The prediction is **timestamped in Git and was authored by a different session**: `3026a81` 11:10:45 and `d9e4f9e` 11:59:51, against V09's first artifact at 13:21:36 (§0 row 8). All four strands hold: (1) `[00:00:00]`–`[00:00:08]` is a resumption, verified in the body; (2) `[00:00:51]` names defined risk and the first 28 minutes are that lesson; (3) `[00:19:55]` / `[00:20:27]` / `[00:51:50]` resume V08's ring model **by name**; (4) **this reviewer compared the two frames directly** and V09's opening card is V08's closing card (§0 row 9). Speaker: four third-person `steve` references verified in the body, plus self-identification at `[00:27:30]` and the MS Paint email frame. **The missing acoustic screen is NOT a gap — see below** |
| 2 | **New content**: the corpus's first position-sizing rule (`balance × 0.02 ÷ stop_pips`, size held through losses 1–3, recalculated on loss 4 and after every win); and V09 answers V08's unanswered innermost-ring question | **CONFIRMED, both halves, at source.** The formula is spoken at `[00:02:00]`–`[00:02:03]` and **printed** — this reviewer read the slide (§0 row 10). The cycle is spoken at `[00:08:30]`–`[00:08:51]` and printed on the recap slide. The worked example reconciles exactly, re-derived here (§0 row 13). **The "first in the corpus" claim was spot-checked**: no V01–V08 artifact states a lot-size or risk-percentage rule, and `V08_INTERPRETATION.md`'s own R1–R10 table — the most rule-dense inventory before V09 — contains no sizing rule of any kind. The innermost-ring answer is at `[00:19:48]`–`[00:20:27]`, is printed as error 3, and matches the `?` this reviewer read in both frames |
| 3 | **`A-020` reconciliation** — the blueberry is now stated as the 800 **on the 15-minute** | **CONFIRMED, and `RESOLVED BY COURSE` is the correct status.** `[00:41:43]`: *"The blueberry is the 800 on the 15 minute time frame."* Addressed to the audience as *"**your** blueberry on your charts"* `[00:41:31]`, which is what makes it shared course furniture rather than the speaker's own — and the submission's §9e records that it first misread this and corrected itself from the surrounding markers. **The `grape` is correctly kept OUT** of `A-020` on the speaker's own *"Steve doesn't teach it"* disclaimer `[00:42:16]`. The timeframe is genuinely new: no prior source carried one |
| 4 | **`C-010` refusal to close** — was refusing the *"800 on 15m ≡ 200 on 1h"* equivalence correct, or over-conservative? | **THE REFUSAL IS CORRECT, AND IT IS NOT CONSERVATISM — it is the right answer for a better reason than the one given.** The submission refuses on `SOURCING_HIERARCHY.md` §3.2's *"Do not blend"*, which is sound. But the equivalence does not merely lack support: **applied to the notes' full enumeration it breaks three of four members and collides with `A-020`'s own mapping**, which requires 200 and 800 to be two lines on one chart. See **`M5`** for the arithmetic. **`C-010` stays OPEN.** This also answers the submission's escalation 5 to the owner: closing `C-010` on this route is not an owner judgement call about blending — the route does not reach |
| 5 | **`PT-035`**: `CONTRADICTED AS STATED`, `P(4-loss run in 200)` = 99.9% at the course's own claimed accuracy; and the self-correction voiding `CLUSTERING CONFIRMED` | **THE MATHEMATICS IS CONFIRMED, INDEPENDENTLY RE-DERIVED, AND THE SELF-CORRECTION IS REAL.** This reviewer wrote its own run-length recursion and got **99.93%** at p=0.50, **54.13%** at p=0.73, **~100%** at the 2:1 break-even, and **p ≥ 84.19%** for the ≤5%-in-100 threshold — matching every reported figure (§0 row 14). `run_pt035.py` reproduces **byte-identically** (§0 row 15). **The self-correction is verifiable in the committed output, not merely narrated**: the runner prints `CLUSTERING CONFIRMED` and `P4 … RIGHT`; the observation withdraws both and scores `P4` **VOID** with the sampling-without-replacement diagnosis, which is correct algebra. **One defect: the same gate was not applied to the empirical arm — `M2`.** The verdict survives it on closed form |
| 6 | **Capture bug** — `SWF_CAPTURE_RECIPE.md`'s hardcoded `mouse.click(512,300)` fails on V09; real, or a fluke? | **REAL, REPRODUCIBLE, AND STRUCTURAL — and it is broader than the submission claims.** This reviewer parsed the stage rectangle from every Bootcamp `.swf`: **V08, V09 and V21 declare a 1280×738 stage; the other 18 declare 1024×786.** The recipe renders in a 1024×786 viewport, so those three are letterboxed — confirmed on committed pixels (§0 row 24). Any viewport coordinate calibrated on a 1024×786 file is displaced on them. **It also already failed on V08, and V08's index says so — `M6`.** `SWF_CAPTURE_RECIPE.md` is FIXED by this reviewer on the integration branch; see **§16** |
| 7 | **Flagged methodology concern** — resolution/censoring bias may also affect `PT-002`…`PT-032` | **WELL-FOUNDED AND WORTH ESCALATING — with the scope tightened.** The mechanism is real and correctly diagnosed: within a bounded horizon a distant target is censored more often than a near stop, so conditioning on resolution over-weights stop-outs. **The `PT-002`…`PT-032` framing is too broad** — most of that family measures range, weekday, gap and barrier statistics with no stop/target race and no discard. **Where it lands it lands hard:** `PT-033`, `PT-034` and `PT-035`, and any successor racing asymmetric barriers inside a day. **`PT-034` already shows the signature** — `N1` at 0.2424–0.2450 against a 0.2500 closed form, low in all four cells (`N5`). **Escalated as a new open item.** Not resolved here, and it does **not** retroactively invalidate `PT-034`: a small consistent downward bias in a null makes the rule-arm gap it was compared against slightly *wider*, not narrower |
| 8 | **Self-disclosed protocol deviation** — transcript-first evidence ordering was not followed | **NOT CHARGED. A reasonable practical deviation, disclosed correctly, with a replacement that is genuinely stronger.** Three reasons. (a) The transcript **was** read end to end first and the reading formed from it; what came later was frame-dependent auditing. (b) The two steps that forced it — auditing a fabricated `VISUAL_INDEX.md` and naming 27 frames — **have no transcript-only version**; `Q-010` §2 cannot be performed without opening images. (c) The replacement is auditable in a way the ordering claim never was, and **this reviewer tested it**: strike every non-`AUDIO` row and the position-sizing formula, the full loss-recovery cycle, the innermost-ring answer and the `A-020` blueberry resolution **all still stand**, because each is `AUDIO` or `AUDIO+PRINTED`. The only load-bearing thing that is `PRINTED`-only is the **spelling** `HOD/LOD`, and it is flagged as such. The project's precedent (`V05` R1 `M4`) charges *files that disagree about their own process* — the opposite of what happened here |
| 9 | **Dimension B** — still blocked by `D-030`, fifth lesson | **CONFIRMED, and handled correctly.** *Level* (`A-004`) is used at 50 markers in this file and is undefined at the ninth lesson; *reset* (`A-073`) is new and equally undefined. **The refusal of `A-072` is the right call and is the one worth checking**: *"three pushes… the third being the longest"* `[00:46:28]` looks codable and is not, because *longest* presupposes the segmentation that is the undefined step. Recorded as an **extension**, never a closure. **No severity charge — the cause is structural.** See §14 |

---

## 3. THE BRANCH AND MERGE STATE — RESOLVED THIS ROUND, NOT LEFT OPEN

Unlike V08 R1, this round **does** perform the merge-back, because it must: the capture-recipe
fix (§16) is a **policy ledger** under `D-038a` and can only be made on the integration branch.
The sequence, performed deliberately and single-threaded per `D-038`:

```text
1. review/v09 branched FROM video/v09 (bb4097b). Review written and committed.
2. integration merged INTO review/v09 (divergence resolved on the task branch, N1).
3. REVIEW_INDEX.md and LOG.md rows written against the merged, current ledgers.
4. review/v09 pushed.
5. review/v09 merged INTO the integration branch — which carries video/v09 with it.
6. SWF_CAPTURE_RECIPE.md fixed on the integration branch, as its own commit.
```

**Step 5 merges the student's V09 work as well as this review, and that is deliberate.** It
follows the V08 precedent (`46d09ed`, `a025b97`) and `D-024`: a `REVISE` with 0 `CRITICAL` and 0
`MAJOR` opens the gate with the minors deferred, so the work is not held. The six MINORs remain
owed and V09 reaches `COMPLETE` only at R2.

---

## 4. THE 17 DIMENSIONS

### A. Source fidelity — **PASS**, with `M1`

Verified mechanically rather than accepted: **230 marker citations across the seven V09-scoped
artifacts, zero orphans**, plus **82 distinct citations across the fifteen new register records,
zero orphans**. Of 217 quoted passages, the great majority are verbatim or correctly attributed
printed slide text; **four are silent ASR corrections inside quote marks under an `AUDIO` tag**
(`M1`).

The submission's terminology discipline is otherwise strong and in one place unusually so: the
transcript **names its own systematic ASR defect** — that the spoken letter *M* is rendered four
different ways in this file — and requires every M/W quotation in the notes to carry its marker so
a reader can re-listen. That is the right response to a defect of that class, and this reviewer
confirmed all four renderings exist at the markers given.

### B. Completeness / Recognition — **NOT SATISFIED — BLOCKED BY `D-030`. Scored, not carved out. No severity charge.**

See §14.

### C. Provenance — **PASS**, with `M4`

Every rule traces to a marker or a named frame, and the marker half is in excellent health
(zero orphans in 312 checked citations). The frame half is where `M4` sits: the pointers are
systematically off by one above frame 15, so a reader following a `PRINTED` basis tag lands on the
wrong slide. The claims themselves are correct — this reviewer read the frames.

The **basis-tag mechanism** deserves separate credit under this dimension. It converts an
unverifiable claim about process order into a per-row, checkable property, and it survives the
check (§2 item 8).

### D. Explicit vs inferred audit — **PASS**, and it is again this submission's strongest habit

The `A-065` status is the notable case and it is **UPHELD**: `CODABLE AS STATED (candidate 1) —
DO NOT EXTEND` is correct, because coding 2% exactly as V09 gives it imports nothing the lesson
did not say, while any rule that **varies** it would import `MMM-NOTES` p.67 against a Tier 1
statement — which `SOURCING_HIERARCHY.md` §3.3 forbids and `C-015` records. The record says
exactly that, and forbids the extension in its own status block.

The failure chain `REVIEW_PROTOCOL.md` §6D warns about is not entered anywhere. Two attractive
inventions were refused **in writing**: `V09_INTERPRETATION.md` Q3's *"stop = extreme ± 15"* — a
placement rule assembled from V08's 10-pip tolerance and V09's 15-pip stop, recorded at `LOW` and
explicitly not adopted — and the earlier draft of a substitute predictor for H3, dropped with the
superseded text retained. **Refusing an attractive reading and leaving the refusal visible is the
behaviour this dimension exists to reward.**

### E. Chart recognition audit — **PASS (scope limited by `D-030`)**

No pattern was classified against an undefined definition. Part B's twelve level calls are
recorded as **observations of the speaker's method in use**, explicitly not as classifications
this project endorses, and `A-004` is cited as the blocker each time. Future price was not used to
justify anything: nothing in V09's artifacts scores a directional call, because H3 — the one
exercise that would have — is `DEFERRED`.

### F. Counterexample testing — **PASS**

`Q-010` is the negative battery here, and it is a strong one: **seven fabricated claim families
from this lesson's own quarantined `NOTES.md`, each falsified by a measured zero** in a 9,164-word
body — six clock figures, six zeroes; `PFH`/`PFL` 0; `railroad`/`pin bar`/`rejection` 0; `TDI` 0;
`shark` 0; `institutional`/`order flow`/`news` 0. This reviewer spot-checked the `TDI` and
`blueberry`/`grape` counts against the body and they hold.

**The register's own self-correction is the valuable part.** Q-010 first concluded the one real
image had been *stolen from V08*, then established it is V09's own splash frame, and records the
correction with the observation that this is a **worse** failure mode — a genuine frame from the
right lesson with an invented description defeats the cross-lesson hashing screen `Q-009`
proposed. That is a finding against the project's own tooling, published by the session that
built the case for the tooling.

### G. Manual backtest review — **PASS**, audited against checks 1–20, with `M2`

| Check | Finding |
|---|---|
| 1 GBP/USD primary | ✅ `D-007` |
| 2 period reasonable | ✅ `W-C′` 2013-01-06 → 2016-06-30 |
| 3–4 sequential / future hidden | ✅ sequences drawn in chronological order without replacement; resolution is forward-only first-touch on M1 |
| 5 rules known before result | ✅ **verified in Git**, §0 row 18 |
| 6–9 skipping / losers / borderline / invalid | ✅ nothing dropped for its result. The two `C8` exclusions are named **in the pre-registration** and are data-hole exclusions, with the `E09` line drawn explicitly. Unresolved draws are **counted and reported** (34.6–49.8%), not silently scored |
| 10–11 outcomes / R consistent | ✅ |
| 12 screenshots | n/a — a corpus computation. `E06` honoured: nothing measured off a rendering |
| 13–14 the right rule tested | ✅ and the scope statement is mandatory and carried: it bounds a conditional claim **from below**, and says so on every report |
| **15 baseline present** | ✅ `N1` matched-random, 1,000 × 200, distribution reported; plus `N2` closed-form and `N3` a shuffled sanity control |
| **16 baseline pre-registered** | ✅ `PT-035` §4, committed at `0f709d2`. **Including the entry-PRICE convention — this discharges open item 65** |
| **17 period pre-registered** | ✅ §7, unchanged |
| **18 holdout intact** | ✅ no post-2016-06-30 row on disk. `E23` cannot occur |
| **19 sample / interval** | ✅ n far above the 30 floor; Wilson 95% on every rate; the <30 rule pre-labelled |
| **20 negatives retained** | ✅ **`P2` WRONG and `P4` VOID are both reported at full length**, and `P2`'s cause is diagnosed against the run's own interest |

**V08 R1 `M2`'s forward requirement is independently discharged here.** That finding required
the next `PT` carrying a matched-random null to fix the null's entry price **in the
pre-registration**. `PT-035` §4's `N1` table does exactly that — *"The CLOSE of the selected M15
bar. Identical in every arm and every cell of this test"* — and states why. This reviewer
confirmed the text is in the `0f709d2` commit, i.e. in the pre-registration and not in the runner.
**Open item 65 was already `CLOSED — VERIFIED` at V08 R2** on the `BACKTEST_EVIDENCE_STANDARD.md`
§2.1a route; this is a second, independent discharge of the same requirement by the first test
that had to obey it, and it is recorded rather than double-counted.

**What raises this above a routine pass**, and it is worth stating plainly: **the test killed
half of its own result with a control it wrote in advance.** `N3` was not required by any project
rule; the session added it, specified in advance what its failure would forbid, and then honoured
that specification against a runner that printed the opposite. `M2` is the one place the same gate
was not applied twice — and the conclusion it affects survives on arithmetic the same
pre-registration committed before the corpus was touched.

### H. Hindsight / lookahead audit — **PASS**

There is little surface for it — `PT-035` measures a run distribution on random entries, so there
is no rule arm to contaminate. The two places contamination could have entered are both
controlled: the comprehension answers were committed **before** the scorer existed, and the
equity-path predictions **before** the script that tests them (§0 row 19). The `O3` estimator
failure is a bias, not a lookahead, and is treated as one.

The strongest anti-hindsight property in the round is `M2`'s subject read the other way: when the
registered statistic failed, the session **named** the correct statistic (chronological vs
shuffled, composition held fixed), explicitly declined to compute it because it was not
pre-registered, and specified it for a successor under a new `PT` number. Inventing it there and
then is precisely the move `D-026` exists to prevent, and it was refused.

### I. Outcome vs rule application — **PASS**

Kept distinct throughout, and the clearest instance is the equity simulation. It measures median
drawdowns of 62–76% under V09's own sizing rule and then states, as prominently as the finding,
that this shows **nothing** about the rule: the streams are matched-random at a below-break-even,
censoring-biased hit rate, and no sizing rule survives a negative edge. It then reports the one
thing the rule genuinely delivers — **0 wipeouts in 4,000 sequences** — with equal prominence. A
bad outcome is explicitly refused as evidence of a bad rule.

### J. Sample quality — **PASS**

n = 1,000 sequences × 200 trades per cell, four cells, both `D-031` arms. The comprehension probe's
n = 10 is treated as what it is — a comprehension check, not an inference — and the report says so
in its own words, directing the reviewer to the four questions with attractive wrong answers
rather than to the score.

### K. Homework review — **PASS.** Disposition `SUCCESS AFTER CORRECTION` is **UPHELD**

| Item | Reviewer ruling |
|---|---|
| **H1 (lot-size calculator) DONE** | **UPHELD, and the substitution is better than the assignment.** Downloading a web calculator would be unauditable; deriving the formula from V09's own words and checking it against **two sources that do not cite each other** is stronger. The `SOURCING_HIERARCHY.md` §1.3 trap — Tier 3 agreeing with Tier 2 being one document quoted twice — is named and genuinely does not apply: this is Tier 1 against Tier 2, 16/16 cells, with the two rounded cells declared |
| **H2 (study the section) DONE** | **UPHELD** |
| **H3 / H4 `DEFERRED`** | **UPHELD, and the `D-019` reasoning is exactly right.** Subject matter exists, the work is performable the moment *level* is defined, so `DEFERRED` and never `NOT APPLICABLE`. The observation that an arrow drill **produces a score, and a score acquires an authority a note never does** is the correct reason to refuse, and is a better statement of the `D-030` risk than the decision itself supplies |
| **H5** | **UPHELD** as a pointer. It is Steve's week-1 assignment referred to, not reissued |

**`SUCCESS AFTER CORRECTION` is right**, and the correction is on the record: an earlier draft
proposed running H3's structure with one of V09's own numbers as the predictor; it was dropped
because V09's numbers are risk parameters, not directional signals, and the superseded text is
retained under a `<details>` block rather than deleted.

### L. Teach-back — **PASS**

`V09_INTERPRETATION.md` Q2 states the whole risk system in one nine-line block — what it is, what
comes before it (a stop distance), what it does on a win, on losses 1–3, on loss 4, and the
cumulative constraint that changes its meaning. What confirms it, what invalidates it and what it
gets confused with are all addressable from `V09_MASTERY_REPORT.md` §C's confusion table, which is
the clearest thing of its kind in the corpus so far. What remains subjective is enumerated as
`A-065`–`A-075`.

Q2's treatment of the hold-size-through-three-losses clause is the strongest single paragraph:
it names the operational reading, names the martingale-flavoured alternative reading, and points
out that **the speaker names the second one himself** (*"this is still a rather aggressive
approach to risk management"*). Two readings held open, with the source's own hedge as the reason.

### M. Blind recognition — **NOT SATISFIED, with B.** Same `D-030` ground, same accounting (§14). Not separately charged.

V09 supplies no defined pattern to recognise. The comprehension probe is the nearest available
substitute and its four discriminating items are genuine near-misses — 7.76% vs 8%, the *">50%"*
sufficiency trap, the invented stop-placement rule, and the projection that is arithmetically
exact and still wrong.

### N. Ambiguity review — **PASS**

Eleven records, `A-065`–`A-075`, all with resolving citations. Two candidates were **considered
and not filed**, and both refusals are correct: the frame-8 *"drawn down to 8%"* wording (loose
English, correct arithmetic — a wording note, not an ambiguity) and a general stop-placement
record that would have duplicated `A-066`.

`A-065` is the important one and is a genuine first for the register — **a number that is not
ambiguous whose governing policy is**. Upheld (see D). `A-072` is the dangerous one and is
correctly held to `EXTENSION ONLY`.

**11 records is not inflationary.** Each names a distinct object the lesson uses fluently and never
defines, and three of them (`A-069` *tracer*, `A-071` *dinosaur*, plus *grape*, *reset*,
*inducement*, *alternate count*, *dominant*) carry **measured Tier 2 negatives** — 0 occurrences
in 84 pages — which is the `SOURCING_HIERARCHY.md` §2 step 3 discipline applied rather than cited.

### O. Contradiction review — **PASS**, with `M5`

Four records, each with the right disposition:

- **`C-012` `UNRESOLVED`** — **UPHELD.** This reviewer read the slide: caption and count are both
  printed on one frame and both spoken in one breath. The refusal to adopt either reading — even
  though reading 1 is plainly more likely and would flatter the lesson's own thesis — is correct,
  and the record's phrase for the alternative (*"that is `E13` inverted"*) is exactly right.
- **`C-013` `UNRESOLVED`** — **UPHELD.** Every arithmetic check re-derived here and every one is
  exact, which is what makes it a contradiction rather than an error. The separation the record
  draws — that this impugns the **projection** and not the **sizing rule** — is correct and is
  stated in both directions.
- **`C-014` `NOTED`** — **UPHELD.** See `N7`.
- **`C-015` `UNRESOLVED ON POLICY`** — **UPHELD, and it is the most careful record in the file.**
  It reports the **agreement** first and at greater length than the conflict, verifies it in code,
  and then applies `C-011`'s asymmetry precisely: Tier 2's scale-in ladder is defeated **without a
  replacement**, so the corpus ends with no scale-in doctrine at all rather than with V09's. That
  is the honest consequence and it is stated as one.

**`C-010`'s narrowing is upheld and its refusal to close is upheld** — on stronger ground than the
submission gives (`M5`).

### P. Machine-rule firewall — **PASS**, strictly

Nothing entered `08_CONCEPT_LIBRARY/`, `12_MASTER_SPEC/` or `13_MACHINE_SPEC/` — verified by diff:
**`video/v09` touches no file under any of the three.** The numbers most likely to leak are the
ones this lesson is made of, and each is fenced: 2% is `CODABLE AS STATED — DO NOT EXTEND`; the
15-pip stop is a size with `A-066` recording that placement is absent; *"three pushes, the third
being the longest"* is `EXTENSION ONLY`; the 85% is not carried as a rate at all.

### Q. Claimed accuracy — **PASS**

V09 makes no 90–95% claim, but it makes two accuracy claims and both are handled correctly. The
*">50% accuracy"* claim is preserved, sourced to audio and print, and correctly identified as
**sufficient stated in the rhetorical position of necessary** (`A-067`), with the true break-evens
computed and labelled as this project's arithmetic rather than the lesson's. The *"85% win rate"*
is preserved with provenance and **explicitly not carried as a course rate** (`C-012`). No sample
was manipulated toward either, and `PT-035` treats the `>50%` figure as an input to a falsification
rather than as a target — which is `D-009` operating as intended.

---

## 5. DISPOSITIONS THE SUBMISSION ASKED THE REVIEWER TO SET

Adjudicated in the order the mastery report's "what I expect to be challenged on" list gives them.

| # | Student's question | Reviewer's ruling |
|---|---|---|
| 1 | Is the **evidence-order deviation** a finding? | **NO — not charged.** See §2 item 8 for the full reasoning. The submission was right to expect this to be the most likely finding, and right to disclose it; the disclosure plus the basis-tag replacement is what takes it out of finding territory |
| 2 | Is reporting `run4_obs` after `N3` failed a violation of §7b? | **The stricter reading is the correct one, and there is a second instance the submission did not see — `M2`.** §5's argument (the bias is in the comparator; `run4_obs` never touches it) is technically right, and the shuffled control reproducing `run4_obs` to within 0.5 pp is real evidence for it. But §6's decision table has its own `INDETERMINATE`-on-`N3`-failure row, it was not applied, and it was not mentioned. **Charged at `MINOR` because the conclusion is carried by §2c's closed form, which was pre-committed and which this reviewer re-derived from scratch** |
| 3 | Is `A-065`'s `CODABLE AS STATED` too permissive? | **NO — UPHELD.** See §4 D |
| 4 | Should `C-014` be downgraded to a note? | **NO CHANGE NEEDED — it is already filed at the note grade.** See `N7` |
| 5 | Could the equity simulation be read as claiming V09's rule loses money? | **It could be misread that way and the submission has already done what is required.** The limit is stated as prominently as the finding, in a box, before the conclusions. **No action.** The finding that *is* carried — that the 8% figure is a resizing trigger and not a drawdown cap, and that the trigger fires every 7–9 trades rather than exceptionally — is correct, useful, and correctly scoped |
| 6 | Are 11 ambiguity records inflationary? | **NO — UPHELD.** See §4 N |
| 7 | Was `Q-010`'s self-correction handled right? | **YES, and it is a model of the class.** See §4 F |
| 8 | **Escalation 3** — is the `PT-035` successor owed? | **RECOMMENDED, NOT OWED.** The specification is correct: the shuffled `run4_obs` *is* the right comparator because it holds composition fixed and isolates arrangement. Pre-register it under a new `PT` number. Carried as an open item, not as debt against V09 |
| 9 | **Escalation 4** — the censoring bias in the wider `PT` family | **WELL-FOUNDED. ESCALATED as a new open item, with the scope tightened.** See §2 item 7 and `N5` |
| 10 | **Escalation 5** — should the owner rule on closing `C-010`? | **The owner does not need to.** `M5` shows the route does not reach, independently of the blending question. The escalation should be re-stated as *"here is why it fails"*, not as *"here is a call the owner could make either way"* |
| 11 | **Escalation 7** — `A-061` and `A-063` untouched | **CONFIRMED and not charged.** V09 genuinely says nothing about either. The characterisation of V08's stop-side promise as **half paid** — size supplied, placement absent — is accurate, and `A-066` is the right place for it |

---

## 14. DIMENSION B — EXPLICIT ACCOUNTING, AND WHY IT CARRIES NO SEVERITY CHARGE

**Graded `NOT SATISFIED`. Scored, not carved out.** No owner directive was issued for this round,
so the standard protocol applies, as it did at V07 R1 and V08 R1.

**No severity charge.** The cause is structural. V09's recognisable objects — *level* (`A-004`),
*reset* (`A-073`), *push*/*inducement* (`A-072`), M/W (`A-011`), *trap area* (`A-002`) — are
**named by the course and defined by nobody**. Recognising them would mean recognising the
student's own inventions and attributing the result to the course, which is what `D-030` forbids.
Refusing is compliance, not failure.

**V09 makes the refusal harder than any previous lesson, and it was still made.** `[00:46:28]` is
the most structurally specific push statement in V01–V09 and it is genuinely tempting; the
submission records it as an **extension** of `A-072` and states the reason the extension cannot
become a rule — *longest* presupposes the segmentation. This reviewer agrees, and notes that
`D-039`'s own text refuses this over-reach in advance, which the submission cites correctly.

**What the student did instead is the right response and is credited:** H3, an exercise the
submission itself calls the best-designed in the corpus, was `DEFERRED` rather than approximated,
and the substitute proposed for it was dropped in writing rather than quietly run.

**This is the fifth consecutive lesson (V05–V09) to be un-gradable on B, and the fifth round in
which `REVIEW_INDEX.md` open item 36 is owed and unanswered.** The vocabulary gap — a third
disposition for work `EXCLUDED BY DECISION`, distinct from `NOT APPLICABLE` and from `DEFERRED` —
is not a student problem and cannot be closed by a student or by this reviewer. **Escalated, for
the fifth time.**

**It does not gate.** Under `D-024` the progression gate follows severity, and B carries none.

---

## 15. REQUIRED CORRECTIONS

Specific, per `REVIEW_PROTOCOL.md` §10. **Six items, all `MINOR`. None blocks V10.**

1. **`M1`** — Run `05_HOMEWORK/V07/scripts/verify_quotes.py` (reachable from integration since the
   V07 R2/R3 rounds) over the seven V09 artifacts. **It needs generalising first** — its
   `TRANSCRIPT`, `ARTIFACTS` list and printed-slide allowlist are V07-specific — and generalising
   it so it takes a lesson identifier is the better fix, because this class has now been charged
   in five lessons. For each of the four hits named in `M1`, either move the correction
   **outside** the quote marks with its marker, or retag the row `PRINTED` where a slide is the
   real source. **Do not edit `02_TRANSCRIPTS/V09/V09_TRANSCRIPT.md`'s body.**

2. **`M2`** — Add a block to `BT_V09_0001` §5 recording that `PT-035` §6's decision table returns
   **`INDETERMINATE`** for the empirical arm on the `N3` failure; report the arm as
   `INDETERMINATE`; and state that **`CONTRADICTED AS STATED` is carried on the §2c / `O4`
   closed-form basis alone**. Propagate the same qualification to `V09_MASTERY_REPORT.md` §G and
   the `LOG.md` V09 entry. **`PT-035` and `run_pt035.py` must NOT be edited**
   (`COMMON_PROTOCOL.md` §9 rule 7).

3. **`M3`** — Correct `02_TRANSCRIPTS/V09/V09_TRANSCRIPT.md`'s COVERAGE block: the 10-second gaps
   are **seven**, at `[00:02:38]`, `[00:03:23]`, `[00:19:18]`, `[00:23:05]`, `[00:45:41]`,
   `[00:49:35]`, `[00:49:47]`. Retain the superseded text per `REMEDIATION_PROTOCOL.md` §2.

4. **`M4`** — Renumber the fourteen frame cross-references listed in `M4` across
   `V09_SOURCE_NOTES.md`, `04_SCREENSHOTS/V09/INDEX.md`, `AUTOMATION_AMBIGUITIES.md` (`A-065`),
   `CONTRADICTIONS.md` (`C-013`, `C-015`) and `V09_MASTERY_REPORT.md`. **Preferred:** replace the
   bare ordinals with the frames' burned timecodes or filenames, which an insertion cannot
   invalidate.

5. **`M5`** — Annotate `V09_INTERPRETATION.md` Q5 with the set-level arithmetic, **downgrade its
   grade from `MEDIUM` to `LOW`**, correct Q8's falsification row, and record the same reasoning
   in `C-010`'s V09 block. **`C-010` stays OPEN; its disposition does not change.**

6. **`M6`** — Correct the *"the coordinate that starts the Camtasia player on V01–V08"* sentence in
   `04_SCREENSHOTS/V09/INDEX.md` and `V09_MASTERY_REPORT.md` escalation 2 to state that it **also
   failed on V08**, citing `04_SCREENSHOTS/V08/INDEX.md`, and reference the stage-geometry cause
   in §16 of this review.

**Not required, recommended** (carried as open items, not as debt against V09):

7. Pre-register the `PT-035` successor described in §5 item 8 — chronological vs shuffled
   `run4_obs`, composition held fixed — under a new `PT` number, **with both `N3` gates encoded in
   code rather than in prose**.
8. Open a scoped investigation of the **resolution-censoring bias** across the `PT` family, bounded
   to tests that race asymmetric barriers inside a bounded horizon (`PT-033`, `PT-034`, `PT-035`).
   `N5` supplies the first evidence.
9. Owner ruling on **open item 36** (dimension B vocabulary) — **fifth** lesson running.

---

## 16. THE `SWF_CAPTURE_RECIPE.md` FIX — MADE BY THIS REVIEWER, ON THE INTEGRATION BRANCH

The submission escalated the capture bug and correctly declined to fix it, because
`SWF_CAPTURE_RECIPE.md` is a **POLICY ledger** under `D-038a` and a task-branch session may not
edit one. **This reviewer confirmed the bug, established its cause, and made the fix.**

**The finding, measured rather than reasoned about.** The stage rectangle was parsed from the
compressed header of every `.swf` in `01_SOURCE_VIDEOS/Forex Bootcamp/Bootcamp/`:

```text
1280 x 738   Bootcamp1 Wk2 032612 Part3 (43mins).swf     <- V08
1280 x 738   Bootcamp1 Wk2 032612 Part4 (53mins).swf     <- V09
1280 x 738   Bootcamp1 Wk10 061712 (75mins).swf          <- V21
1024 x 786   ...the other eighteen files
```

The recipe's Playwright context is `viewport: { width: 1024, height: 786 }`. Ruffle fits a
1280×738 stage into that viewport at scale 0.8, letterboxed vertically — which is visible in the
committed pixels: V08 and V09 frames carry uniform dark bands at rows **0–160** and **685–785**,
and V06/V07 frames carry **none**. **Every viewport coordinate calibrated on a 1024×786 file is
therefore displaced on the 1280×738 files**, which is why `(512, 300)` misses a play button that
sits at `(512, 325)` — on **both** V08 and V09.

**This is not a per-file oddity and it is not a fluke.** It is a property of a declared header
field, it affects a knowable set of files, and it is checkable in one line before a capture is
run.

**The edit made:** `SWF_CAPTURE_RECIPE.md` §3 and §10 no longer present `(512, 300)` as the play
coordinate. Both now require the stage size to be read from the header first, give the measured
two-class result, state the corrected coordinate for the 1280×738 class, and — the general fix,
which is V08's and is adopted rather than reinvented — require the sweep to **screenshot before
and after the play click and abort non-zero if the two are identical**. A `GOTCHA 5` block records
the failure history: V08's 529 splash frames, V09's 638, and the fact that both were caught only
by opening a frame and looking at it.

**Recorded as its own commit on the integration branch, after the merge-back, per `D-038a`.**

---

## 17. DECISION

```text
LESSON:     V09 — no printed title
DECISION:   REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- None.

MAJOR ISSUES:
- None.

MINOR ISSUES:
- M1  E01  Four silent ASR corrections inside quotation marks under AUDIO tags.
- M2  E20  PT-035 §6's INDETERMINATE-on-N3-failure clause is neither applied
           nor disclosed; the same gate the submission enforced on the
           clustering arm was not enforced on the empirical arm.
- M3  E19  The transcript COVERAGE block states four 10-second gaps; there
           are seven.
- M4  E11  Fourteen frame cross-references at 15+ are off by one across
           five files, after a 27th frame was inserted at position 15.
- M5  E02  The candidate C-010 reconciliation is held at "more likely than
           not"; applied to the full enumerated set it breaks three members
           of four and collides with A-020.
- M6  E20  The capture-bug escalation states the coordinate works on
           V01-V08; V08's own index records the identical failure.

REQUIRED ACTIONS:
1. Re-run the quote-fidelity checker and fix the four quotations.
2. Record PT-035 §6's INDETERMINATE trigger in BT_V09_0001 and carry the
   verdict on the closed form alone. Do not edit PT-035 or the runner.
3. Correct the COVERAGE block's 10-second gap count to seven.
4. Renumber the fourteen frame cross-references, preferably to timecodes.
5. Downgrade V09_INTERPRETATION Q5 to LOW, correct Q8, annotate C-010.
6. Correct the "V01-V08" claim in the capture-bug escalation.

ADVANCEMENT:
AUTHORIZED under D-024 (0 CRITICAL, 0 MAJOR). The V10 gate OPENS.
The six MINORs are deferred and still owed; V09 reaches COMPLETE
only at R2.
```

### Why `REVISE` and not `PASS`

`REVIEW_PROTOCOL.md` §9's fourteen `PASS` conditions are met on thirteen. The exception is
**condition 2** — *important rules have provenance* — which `M4` breaches across fourteen frame
pointers, and `M1` breaches in four quotations. Condition 14's *"remaining issues are minor and do
not corrupt downstream learning"* is satisfied, which is why the gate opens. This is the project's
established treatment and it is applied here without adjustment.

### Why `HIGH` and not `MEDIUM`

Nothing load-bearing was accepted on the submission's authority. The backtest was **re-executed
and reproduced byte-for-byte**; its headline result was **re-derived from first principles in this
reviewer's own code** rather than checked against the runner; all four committed scripts were
re-run to byte-identical output; the pre-registration and prediction ordering were **verified in
Git**, including that the continuity prediction was authored by a **different session two hours
before** the first V09 artifact; the source hash and both audio durations were **re-measured**;
the transcript's timestamp structure was **re-derived mechanically** and one claim in it falsified;
312 marker citations and 217 quotations were **machine-checked**; six load-bearing frames were
**read as images**, one of them magnified; and the capture bug was established from **the SWF
headers of all 21 source files**. The verifications not performed — Whisper re-transcription, the
acoustic screen, independent re-capture of frames — are disclosed in §0a with what was done
instead, and no finding in this review turns on any of them.

### A statement this review should make plainly

`REVIEW_PROTOCOL.md` §1 forbids reflexive disagreement as firmly as it forbids credulity, so the
following is recorded as a finding of fact rather than as praise.

**This submission's two most important results are both things it did to itself.** A control it
was not required to write, `N3`, failed, and the session honoured a specification it had made in
advance against a runner that printed the opposite verdict — deleting half its own headline rather
than reporting a number a script produced. And a prediction made by a *previous* session about
what this file would contain was tested rather than assumed, on evidence chosen before the file
was opened, with the one screen that would have made it easy left unused because a standing
instruction prohibited it.

The six corrections owed are labels, counts, pointers and one unapplied clause. **Nothing in the
method is wrong**, and the position-sizing rule this lesson contributes — the first in nine
lessons — is recorded accurately, fenced correctly, and verified against a second independent
source.

---

## 18. LOGGING

Logged in `LOG.md` under **2026-08-13 — Reviewer Session (V09 R1)**, on branch `review/v09`.
`18_REVIEW/REVIEW_INDEX.md` updated in the same round: decision-table row, STATUS block, error
counts, severity totals, and open items **73–78** (`M1`–`M6`) plus **79** (the `PT-035` successor)
and **80** (the censoring-bias investigation). Item numbering is allocated against the **merged**
integration state, whose highest existing item is **72** (V08 R2) — `D-038a` consequence 1.

**Merged**, and deliberately — see §3. The `SWF_CAPTURE_RECIPE.md` fix (§16) is a policy-ledger
edit and is committed separately on the integration branch.

**Next review trigger:** V09 R2, on student resubmission with `M1`–`M6` applied.
