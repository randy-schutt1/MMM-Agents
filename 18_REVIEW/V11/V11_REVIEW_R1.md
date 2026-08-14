# V11 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | **V11** · `Bootcamp1 Wk4 040812 Part1 (51mins).swf` · session 2012-04-08 (Easter Sunday) |
| Review version | **R1** |
| Review date | 2026-08-13 |
| Previous review | none |
| Reviewer branch | `review/v11`, cut from the integration branch @ `e63e85e` (`D-038`), own worktree at `MMM-Agents-v11-review` |
| Submission reviewed | `video/v11` @ `dbeb327` (11 commits, `e5aad04`…`dbeb327`) |
| Independence | **`D-003` satisfied.** This session authored no V11 artifact. It read the full transcript before any student conclusion was opened, re-derived every quantitative claim with code sharing nothing with `mmm_lib`/`run_pt039.py`, and re-ran the `Q-012` `diff` and the `A-080` frame audit at source |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 5 MINOR, 7 NOTE.**

Under `DECISIONS.md` **D-024**, a round carrying zero `CRITICAL` and zero `MAJOR` **opens the
gate for V12**, which the owner has already begun. **Nothing in this review holds that gate**, and
nothing in it should be read as a reason to pause V12 — the strongest finding (`M1`) makes the
V12 look-for list *more* specific, not less urgent. The five minors are carried in
`REVIEW_INDEX.md` as items **109–113** and are owed before V11 can reach `COMPLETE`.

**Confidence: HIGH.**

Confidence is high because the load-bearing claims were **re-derived rather than read**:

- **`PT-039`'s entire numeric output was independently reproduced** from the raw HistData CSVs by
  reviewer-written code that shares no line with the student's runner or with `mmm_lib`. **Every
  figure in all four cells reproduced exactly** — the `O1` curve to four decimal places, every
  `n(T)`, every Wilson bound, all six `N3` strata, `O3`, `O4`, `O5`, the session-day counts and
  the exclusion counts.
- **The `Q-012` fabrication `diff` was re-run at source** and returns exactly what the register
  claims: twelve differing lines, six substitutions, zero content lines.
- **The homework H6 RSI sensitivity table was independently recomputed** and reproduced to two
  decimal places on all 36 cells.
- **The two load-bearing frames were opened and read as images**, and this is where `M1` came from.
- **The whole 643-marker transcript body was read before any student artifact was opened.**

---

## SOURCE MATERIAL REVIEWED — **FIRST, BEFORE ANY STUDENT CONCLUSION**

| Source | References | Purpose |
|---|---|---|
| `02_TRANSCRIPTS/V11/V11_TRANSCRIPT.md` verbatim body | **All 643 markers, `[00:00:00]`–`[00:50:56]`, read in full** | Primary evidence for every finding below. Read **before** the source notes, interpretation, homework, backtest or mastery report were opened |
| Frame `31:25` — the `Parameters of RSI` slide | Opened and read as an image | Verify the six printed parameters and the absence of the lookback |
| Frame `46:45` — the *"mayonnaise / the 50"* chart | Opened and read as an image | Adjudicate `C-018`'s "the frame does not settle it" |
| Frame `27:35` — the `CAN YOU DECIDE??` chart | Opened and read as an image | **This is where `M1` came from** |
| Frames `47:35`, `03:00` | Opened and read as images | Test the categorical "no legend anywhere" claim |
| `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/11_…/{RULES,NOTES,VISUAL_INDEX}.md` | Read in full; `RULES.md` `diff`ed against V01's | Independent re-derivation of `Q-012` §1–§3 |
| `…/11_…/SCREENSHOTS/VIDEO_12_SCREENSHOT_001_00-02-00.jpg` | Opened and looked at | Verify `Q-012` §3a's title-card claim |
| All 21 `SCREENSHOT_001` files | MD5'd | Re-derive `Q-012` §3b's negative duplicate check |
| `datasets/HISTDATA_GBPUSD_M1/raw/*.csv` | 1,297,781 M1 bars parsed directly | Independent re-derivation of the whole of `PT-039` |
| `datasets/HISTDATA_GBPUSD_M1/GBPUSD_M15_ARMA.csv` | 86,536 M15 bars in `W-C′` | Independent re-derivation of homework H6 |
| `00_SYSTEM/EXTERNAL_REFERENCE/EXTERNAL_Mauro_MMM_seminar_notes_TEXT_EXTRACT.md` | RSI/TDI chapter pp.44–46, plus a full numeric sweep | Verify `A-080`'s "Tier 2 is also silent" |
| `02_TRANSCRIPTS/V01–V10` | Nickname census, body-only; V01 `[00:43:53]` blue-box passage | Verify `D-041`'s corpus claims and a new host strand |
| `00_SYSTEM/DECISIONS.md` `D-003`, `D-024`, `D-026`/`D-027`, `D-030`, `D-031`, `D-038`/`D-038a`, `D-039`, `D-040`, **`D-041`** | Read in full | Governing policy |

**Source access was not limited.** The `.swf`, the transcript, all 27 curated frames, the
quarantined tree and the full M1 corpus were available. Nothing in this review is capped by
missing evidence.

## STUDENT ARTIFACTS REVIEWED

| Artifact | Reviewed |
|---|---|
| `02_TRANSCRIPTS/V11/V11_TRANSCRIPT.md` header, speaker table, coverage, verification, spot-checks | ✅ in full |
| `03_LESSON_NOTES/V11_SOURCE_NOTES.md` · `V11_INTERPRETATION.md` | ✅ in full |
| `04_SCREENSHOTS/V11/INDEX.md` + **5 frames opened** | ✅ |
| `05_HOMEWORK/V11/` — homework, script, output | ✅ |
| `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-039_…md` · `V11/BT_V11_0001.md` · `data/pt039_output.txt` · `scripts/run_pt039.py` | ✅ in full |
| `07_MASTERY_REPORTS/V11_MASTERY_REPORT.md` | ✅ in full |
| `00_SYSTEM/QUARANTINE_REGISTER.md` `Q-012` · `A-039`/`A-011`/`A-020` updates · `A-080`–`A-083` · `C-018` | ✅ |
| `LOG.md`, `COURSE_PROGRESS.md`, `REVIEW_INDEX.md` items 97–108 (V11's additions) | ✅ |

---

## CRITICAL FINDINGS

**NONE.**

| # | Finding | Error code | Evidence | Impact |
|---|---|---|---|---|
| — | *No finding in this round could materially alter the methodology or later trading logic.* | — | — | — |

The three places a `CRITICAL` could plausibly have arisen were checked directly and all three are
clean:

1. **Lookahead in `PT-039`.** Checked by re-derivation of the predicate, not by reading the
   submission's assurance. `held(T) := (superseded ∧ Δ ≥ T) ∨ (never superseded)` is **logically
   identical to `¬(superseded within [t, t+T))`**, which is fully knowable at `t+T`. The eligibility
   rule `R ≥ T` uses only the candidate's own timestamp and the fixed 17:00 close. `FINAL` is the
   *outcome*, not a conditioner. **There is no path by which post-`t+T` information enters the
   conditioning set.** The submission asserts this; I re-derived it and it holds.
2. **A number invented for the RSI period.** `A-080` refuses the TDI's distributed default of 13
   explicitly, and **no V11 artifact anywhere adopts a period.** The homework's sensitivity table
   carries a `NO PERIOD IS ADOPTED` banner in its own output header. **This is the single most
   important thing V11 got right**, and `M1` below does not disturb it.
3. **The owner's `D-041` ruling reframed as something stronger than it is.** Checked line by line
   in `C-018`'s closure. It is **not** reframed. See § `C-018` below.

---

## ⭐ THE HOST-VS-GUEST DETERMINATION — RE-VERIFIED INDEPENDENTLY

**Reviewer verdict: the determination is CORRECT. Confidence HIGH. It is over-determined, and
this reviewer found five further strands the submission does not cite — one of which is
cross-file and checkable against the corpus itself.**

Each of the submission's four strands was checked against the transcript by this reviewer.

| Strand | Reviewer finding |
|---|---|
| **1 — first-person mailbox** | **CONFIRMED and decisive on its own.** `[00:02:21]` *"My only valid email address is Steve at marketmakersforks.com"*, repeated verbatim at `[00:02:40]`. First-person possessive; *Steve* is the object of it, not a third party. `[00:02:32]` *"I'm gonna cut the account off"* — he controls the mailbox |
| **2 — the `Steve` tokens** | **COUNT CONFIRMED — exactly 5 in the verbatim body**, by word-boundary match after stripping marker lines. I printed all five with their markers and inspected each. **The characterisation is also correct**, which is worth stating because V10 R1 had to correct the parallel claim: `[00:02:21]` and `[00:02:40]` are his own address; `[00:15:18]`, `[00:22:19]` and `[00:23:31]` are all the speaker **voicing a student addressing him** and answering in the first person. **Not one token is the speaker referring to an absent Steve** |
| **3 — claims authorship of the method** | **CONFIRMED at all four cited markers**, verbatim. `[00:15:29]` *"a trade or a flashcard that **I've ever taught in any one of my classes** since I've been born"*; `[00:23:45]` *"They're not what **I teach**"*; `[00:24:50]` *"your belief in **my methods**"*; `[00:36:47]` *"the price action in the timing that **i've taught** you"* |
| **4 — owns the logistics** | **CONFIRMED at all five cited markers.** `[00:01:48]` forum policy; `[00:02:32]` email cut-off; `[00:18:07]` imposes the new protocol; `[00:21:11]` *"**I have ordered** bracelets"*; `[00:22:51]` *"you asked me to be here for bootcamp"* |
| **Negative check — handover language** | **CONFIRMED ZERO — and I widened the scan.** I ran my own case-insensitive sweep over the body with a **superset** of the submission's list, adding *joining us · our guest · I'll turn · give you the (mic\|screen\|controls) · you're up · take over*: **zero matches in 51 minutes**, 17 patterns |

### Five further strands this reviewer found that the submission does not cite

Recorded because independence means adding evidence, not only checking it.

1. **⭐ `[00:23:06]` — a checkable back-reference to the corpus's own week 1.** *"I said right out
   of the box. I think the first week I said **quit taking shit in the blue box**."* This is a
   claim to have personally taught **V01/V02**. I checked it: V01 `[00:43:53]`–`[00:44:13]` is a
   blue-box instruction in the same voice and the same idiom, and V01's own speaker says at
   `[00:03:1x]` *"I'm not having any guest speakers in here."* **This is the only strand in the
   determination that is verifiable against a different file in the corpus**, and it is therefore
   the most resistant to a single-file impersonation hypothesis.
2. `[00:14:46]`–`[00:14:54]` — **ownership of the course's flashcard collection**: *"If you have
   done your flashcards and **I've done them** so you can't bullshit me. There are not one
   flashcard **in my collection** that looks like that."*
3. `[00:18:47]` — **he sizes the membership**: *"That **1,100 of us** are sitting staring at your
   screen."* A guest does not carry the roll count.
4. `[00:21:11]`–`[00:21:29]` — **commissions merchandise and schedules live events**: bracelets
   *"given out at the next live event in **new jersey** and at the meetups"*, in *"limit order
   green"*.
5. `[00:00:22]`–`[00:00:31]` — **he brags on a member's behalf to the room**, reporting Subio's
   *"2335 pips … plus 50 percent risking only 1% per trade"*. The person who publicises a member's
   result is the person who runs the room.

### Could this still be a guest impersonating or quoting the host?

**No, and strand 1 above is why the answer is stronger here than it was for V10.**

The impersonation hypothesis now requires an unbroken 51-minute performance in which the speaker
claims Steve's mailbox, Steve's forum policy, Steve's authorship of the method, Steve's flashcard
collection, Steve's membership roll, Steve's merchandise budget and Steve's live events — **and
also correctly back-references, in the first person, content this project has independently
ingested as V01.** There is no motive on the record, no seam in the audio, and the only two named
third parties (*"Subio"* `[00:00:12]`, *"doc Ken"* `[00:17:38]`) neither speak nor are handed to.
The quoting hypothesis has the direction wrong: he is quoted **to**, never **about**.

**The acoustic screen was correctly not run.** V07's prohibition is honoured, as in V08–V10.

### And the safeguard is the part that matters most

`D-025` consequence 4 — re-adopted by `D-033` — requires that **nothing depend on the
identification being right.** I checked rather than accepted this: `PT-039` reads OHLC and never a
speaker; every `V11_SOURCE_NOTES.md` row is tagged `AUDIO`/`PRINTED`/`AUDIO+PRINTED` rather than
speaker-weighted; `D-033` makes all speakers equal in authority in any case. **If this
determination were overturned tomorrow, not one rule, record, number or verdict in V11 would
move.**

**One limit, stated rather than glossed** — identical to V10's and correctly handled the same way:
what the file establishes internally is that the speaker *is the course's author and is named
Steve*. That he is *Steve Mauro* is a corpus-external attribution, and the transcript header keeps
it parenthetical.

---

## RULE FIDELITY

**Grade: PASS.**

The lesson's one printed parameter block is its most codable-looking content. **I opened frame
`31:25` and read it against the transcription character by character.**

| Student's rendering (`V11_SOURCE_NOTES.md` §4b, `INDEX.md` §1, `A-080`, `V11_MASTERY_REPORT.md`) | Slide at `31:25` as read by the reviewer | Assessment |
|---|---|---|
| `RANGE ANALYSIS WITH RSI` | identical | **EXACT** |
| `Parameters of RSI:` | identical | **EXACT** |
| `1. Value of RSI:  0 - 100` | identical, including the spaced hyphen | **EXACT** |
| `2. Normal Range:  70/30` | identical | **EXACT** |
| `3. Bull Range:    80/40` | identical | **EXACT** |
| `4. Bear Range:    60/20` | identical | **EXACT** |
| `5. Overbought/Oversold  80/20` | identical, **including the missing colon** a tidying transcription would have added | **EXACT** |
| `6. Mid Point or Basis Level of 50` | identical, including `Mid Point` as two words | **EXACT** |

**Six printed parameters transcribed without a single substitution, including two typographic
infelicities.** The slide is reproduced identically at **four** independent sites in the
submission and all four agree.

**Spoken corroboration re-checked at source.** All six are also spoken at `[00:31:28]`–`[00:32:04]`
and `[00:30:13]`, and I confirmed each at its marker. The submission's claim that *"print and
speech corroborate; nothing is added by either"* is **correct**.

**Spoken quotations spot-checked at fourteen markers** spanning the file — `[00:02:21]`,
`[00:07:36]`, `[00:07:52]`, `[00:10:26]`, `[00:12:42]`, `[00:14:31]`, `[00:15:29]`, `[00:23:06]`,
`[00:25:33]`, `[00:29:52]`, `[00:32:34]`, `[00:36:19]`, `[00:46:45]`, `[00:46:52]`. **All fourteen
resolve verbatim at the cited marker.**

**Qualifiers are carried, not dropped.** The three most convenient to lose are all present: the
30-minute case's *"railroad tracks"* condition (`PT-039` §1a refuses to use it as an exclusion —
the reading **least** favourable to the session and **most** favourable to the claim), the *"up to
two hours"* ceiling (carried and explicitly labelled the agent's extension, not the
instructor's), and `[00:23:36]`–`[00:23:48]`'s *"No argument for me… they're 50/50 guesses… they're
not what I teach"* — a concession preserved with its withdrawal intact.

---

## ⭐ `M1` — THE ROUND'S PRINCIPAL FINDING: A CATEGORICAL CLAIM FALSIFIED BY V11'S OWN FRAME 14

**This is the only finding in the round that a reviewer could not have reached by reading. It came
from opening an image.**

### The claim

Six V11 artifacts state, categorically, that **no frame in the lesson shows an indicator legend or
a settings dialog**:

| Site | Text |
|---|---|
| `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` `A-080` | *"**No frame in the lesson shows an indicator-settings dialog, a legend with a period, or a Navigator/Indicators list.**"* |
| `03_LESSON_NOTES/V11_SOURCE_NOTES.md` §4b | *"**No frame in the lesson shows an indicator-settings dialog or a legend with a period.**"* |
| `03_LESSON_NOTES/V11_INTERPRETATION.md` Q3 | *"Silent. 33 `rsi` tokens, no period; **no frame shows a settings dialog or legend**"* |
| `04_SCREENSHOTS/V11/INDEX.md` §1 | *"The slide … does not state the RSI period. **Neither does any other frame in the lesson**"* |
| `07_MASTERY_REPORTS/V11_MASTERY_REPORT.md` | *"**no frame among 28 detected screen states shows a settings dialog or a legend**"* |
| `LOG.md`; `REVIEW_INDEX.md` item **98** | same sentence, twice more |

### It is false, and V11's own committed evidence set falsifies it

**Frame 14 — `V11_00-27-35_can-you-decide-cluttered-subgraph-chart.png` — carries a full MT4
legend stack with periods, legible without magnification:**

```text
GBPUSD,H1  1.6671 1.6696 1.6668 1.6692
RSI(21) 57.5053
ATR(14) 0.0037
CCI(14) 68.3929
MACD(12,26,9) 0.00240 …
Sto(5,3,3) 69.3396 71.8350
Mom(N) 100.4997
AO 0.00684
```

**`RSI(21)` is an RSI period, printed, on a V11 frame, in the submission's own curated set.** The
`INDEX.md` row for frame 14 describes it only as *"a chart with **six** stacked sub-graph indicator
panes"* — the pane count was read and **the legends were not**, despite §8's rule that every frame
was *"opened and looked at before it was named"*.

### ⭐ Why this does NOT move `A-080`, and why it is a `MINOR` rather than a `MAJOR`

**The disposition is correct and is untouched. `A-080` stays `OPEN — DO NOT CODE`, every RSI
threshold stays blocked, and no test is unblocked. Nothing in the method changes.** The reason:

1. **The chart is the lesson's disowned anti-example.** `[00:27:30]` *"this was **Cars chart when i
   met them**… it's kind of half of a joke"*; `[00:27:42]` *"they have all the indicator windows in
   the subgraph and **absolutely ridiculous**"*; `[00:27:54]` *"get rid of all this crap and pick
   one indicator"*. The slide is headed **`CAN YOU DECIDE??`**. Adopting `RSI(21)` from it would
   attribute a **student's** setting to the instructor — a worse error than the `13` trap `A-080`
   already names.
2. **It is an `H1` chart** (`GBPUSD,H1` in the price-pane legend), not the 15-minute frame of
   reference V11 works in.
3. **The instructor's own charts confirm the negative.** I opened frames `46:45` and `47:35`: the
   price panes are occluded or cropped and the sub-graph carries **no legend at all**. The
   substantive claim — *the course never states its own RSI period* — **survives intact.**

### But the finding is not cosmetic, and the reason is `A-080`'s own argument

`A-080` exists because *"the near-miss is the hazard"*. **It names the `13` trap (the TDI's
distributed default, plus `MMM-NOTES` p.38's 13 EMA) and does not name the nearer one.** A future
session — including the V12 session, which is explicitly told to hunt frames for an
indicator-properties dialog — that greps V11's frames for an RSI period **will find `RSI(21)` and
will be wrong**, and the six categorical sentences above actively discourage it from looking hard
enough to notice whose chart it is. `A-080` illustrates its own point with the phrase *"RSI(2),
RSI(9) and RSI(21)"* — the exact legend format sitting in its own screenshot folder, unremarked.

### Required correction

Rescope the six sentences from *"no frame shows a legend"* to the true and stronger form:
**"no frame of the INSTRUCTOR's OWN chart shows a legend or a period; the one frame that does
(`27:35`) is the disowned student anti-example, is on `H1`, and its `RSI(21)` must not be adopted"**
— and add `RSI(21)` to `A-080`'s named-trap list beside `13`. **Superseded text retained in place
per `REMEDIATION_PROTOCOL.md` §2.** `INDEX.md`'s frame-14 row should record the legend stack it
actually shows.

**Charged as `MINOR` (`REVIEW_PROTOCOL.md` §8 — *"completeness problem that does not alter the
method"*), not `MAJOR`.** It is not a misunderstanding: the submission's conclusion is right, its
fence is right, and the correction makes the record stronger. Inflating it would hold a gate the
owner has correctly already opened, which §8 forbids in terms.

---

## THE `A-080` DETERMINATION ITSELF — VERIFIED ON BOTH ADMISSIBLE TIERS

Setting `M1` aside, the substance of `A-080` was checked independently and is **correct**.

| Claim | Reviewer verification |
|---|---|
| The slide is headed *"Parameters of RSI"*, gives six parameters, and the lookback is not among them | **CONFIRMED by opening the image.** See § RULE FIDELITY |
| `rsi` occurs 33 times with no period attached | **COUNT CONFIRMED — exactly 33**, word-boundary, markers stripped. I then printed **every** line containing `rsi`/`tdi` **and** an integer: three lines, `[00:36:19]` (*"25 to 50 pips… 80 to 90 range"*), `[00:46:52]` and `[00:47:00]` (*"resistance… around 60"*). **None is a lookback.** The negative is exhaustive, not sampled |
| **Tier 2 (`MMM-NOTES`) is silent too** | **CONFIRMED, and I widened the search beyond the submission's.** I swept every line of the text extract containing `RSI` for a numeral: pp.44–46 describe the TDI's four components with **no lookback for any**; pp.48–49 give *"RSI in the 80 to 40 range"* / *"60 to 20"* and no period. **No RSI period appears anywhere in the 84 pages** |
| The `13` trap is real | **CONFIRMED at source.** `MMM-NOTES` p.38: *"The **5 and 13 EMA's happen to match up the TDI** used by Mauro"* — precisely the conflation a session could reach and feel sourced doing |
| The cost was measured, not asserted: `0.04% → 5.66%`, ratio `144×`; adjacent 13 vs 14 differ ~20% | **RE-DERIVED INDEPENDENTLY AND REPRODUCED EXACTLY.** My own Wilder RSI over the committed `GBPUSD_M15_ARMA.csv`, 86,536 bars in `W-C′`, reproduces **all 36 cells to two decimal places**, `144.04×`, `561.15×`, and 13-vs-14 at **21.8%** relative. One cell differs by 0.01 pp (`60-20` at `n=13`), which is float rounding |

**The homework output's own `NO PERIOD IS ADOPTED` banner and its `WHAT THIS DOES NOT SHOW`
section are the correct handling** and are the reason the sensitivity table cannot be mined as
doctrine.

---

## `C-018` — THE DISPOSITION, AND WHETHER `D-041` IS FAITHFULLY REPRESENTED

**Reviewer verdict: the closure is CORRECT, faithful, and NOT silently strengthened. This is the
best-handled item in the submission.**

I read `D-041` in full **before** opening `C-018`'s closure, and then compared them clause by
clause. The four ways a closure like this typically inflates itself were each checked:

| Way it could have been overstated | What `C-018`'s closure actually says |
|---|---|
| Present the owner as **outranking Tier 1** | *"**`SOURCING_HIERARCHY.md` §3.3's 'the recording wins' was NOT applied, and was NOT overridden.**… The owner supplied the missing **DISAMBIGUATION**, not a trump card."* **Faithful to `D-041` verbatim** |
| Invent a **"Tier 0"** | *"**There is no 'Tier 0' and the owner does not outrank the recordings.**"* — and it goes further than `D-041` needed to, restating that `RESOLVED — OWNER ATTESTATION` is still the **weakest** resolved status |
| Quietly **discharge** `SOURCING_HIERARCHY.md` §3.4's standing re-check on `A-020` | *"**§3.4's standing re-check obligation on `A-020` REMAINS LIVE**… the cheap next step this record names — V12 — is still worth taking, and `A-020`'s *Required Research* is still unsatisfied."* Correct: a closure on attestation is not closure for good |
| Convert `A-020` to **`RESOLVED BY COURSE`** on the strength of a Tier 1 utterance | Not done anywhere. `A-020` stays `RESOLVED — OWNER ATTESTATION`, and the closure is explicit that `[00:46:45]` **leaves `A-020` untouched** rather than confirming it |

**The superseded status line is retained in place** (`⚠ CONFLICT — OWNER ADJUDICATION REQUIRED.
NOT ADJUDICATED HERE.`), and **the entire pre-closure record below the banner is unedited** — I
diffed `dbeb327` and confirmed the closure is a pure prepend of 78 lines plus a two-line status
change. `REMEDIATION_PROTOCOL.md` §2 satisfied.

**The ketchup/mustard inversion is flagged, not buried** — `C-018`, the mastery report, `LOG.md`
and `REVIEW_INDEX.md` item 97 all carry it with the ⚠ marker and all four say a reviewer may put
it back to the owner.

### Was the session right to refuse to adjudicate? **Yes, and I re-derived its three grounds.**

1. **The plural.** `[00:46:45]` opens *"Look where the **averages** are"* — plural, and I opened
   the frame: **at least four moving averages are on screen** (cyan, red, yellow, white), with
   price below the slowest two. **CONFIRMED.**
2. **⭐ The `[00:46:52]` recurrence.** *"Remember I told you **there's the 50**. Rsi will find
   resistance where? Around 60, right?"* — that *"the 50"* is unambiguously the RSI baseline.
   **CONFIRMED at source.** This is the load-bearing point and it holds.
3. **The frame cannot arbitrate.** **CONFIRMED by opening it.** The price pane's upper-left is
   occluded by the MT4 `Line Studies` toolbar; there is no legend, no period label, no settings
   dialog, and the sub-graph carries a bare yellow line with unlabelled dashed levels. **`A-020`'s
   *Required Research* is still unsatisfied at the one timestamp in the corpus that finally met its
   first condition** — exactly as the record says.

### `M2` — but one supporting sentence is false, and correcting it strengthens the conclusion

`C-018` and `REVIEW_INDEX.md` item 97 both state:

> *"The phrase *'the 50'* occurs **14 times in V11** and **every unambiguous instance is the
> sub-graph baseline.**"*

**The count is right — I measured exactly 14.** The characterisation is not. I printed all
fourteen with their markers, and **`[00:12:42]` is a counterexample**:

> *"You got in right before the shift candle and **you were out to the 50 in no time**."*

That is at minute **12** — **fourteen minutes before RSI is introduced at `[00:26:18]`** — inside a
price-chart markup discussion, and *"out to"* is destination language. Price does not travel *out
to* an oscillator reading. **This *"the 50"* is unambiguously a price-pane object**, and under
`D-041` it is the **water / 50 EMA**.

**The correction runs IN THE CLAIM'S FAVOUR, which is why it is worth making rather than
suppressing.** It establishes that *"the 50"* in this very lesson **already denotes a price-pane
moving average in at least one place**, which is direct evidence that `[00:46:45]`'s *"There's the
mayonnaise. There's the 50"* can enumerate **two price-pane averages** — and it forecloses any
future argument that in V11 *"the 50"* can only mean the baseline. **Reading B gains a fourth
independent ground, and it is one the session had in hand and did not use.**

Charged as **`MINOR`**: `C-018` is closed, but `SOURCING_HIERARCHY.md` §3.4's obligation on
`A-020` is **live**, and the session that performs that re-check will read this sentence.

---

## MANUAL BACKTESTING — **`PT-039` RE-DERIVED INDEPENDENTLY, END TO END**

### The re-derivation

I wrote `reviewer_pt039.py` from `PT-039` §§3–6 alone. It parses the four raw HistData CSVs
directly (**not** the student's `_cache/m1_raw_v2.npz`), implements its own US-DST rule, its own
`C-1` session-day labelling, its own 96-bucket completeness gate, its own candidate/supersession
detector, its own Wilson interval and its own stratification. **It shares no line with
`run_pt039.py` or `mmm_lib`.**

**Every number reproduced.** Arm A, low — the pre-registered primary cell:

| Quantity | Submission | **Reviewer, independently** | |
|---|---|---|---|
| Session days included / excluded | 894 / 11 | **894** / 10 in-window + `2016-07-01` = **11** | ✅ |
| Candidates · `FINAL` · unresolved | 26,028 · 894 · 0 | **26,028 · 894 · 0** | ✅ |
| `N1` base rate | 3.43% | **3.4348%** | ✅ |
| `P(FINAL \| held ≥ 30)`, `n` | 19.24%, 4,491 | **0.19238, 4,491** | ✅ |
| `P(FINAL \| held ≥ 90)`, `n` | 31.41%, 2,674 | **0.31413, 2,674** | ✅ |
| Wilson 95% at `T=30` | 18.11–20.42 | **[0.1811, 0.2042]** | ✅ |
| Every other `T` in `{5,10,15,45,60,120,180,240}` | — | **all ten rows, `n` and `p`, exact** | ✅ |
| `O3` median / q25 / q75 / p95 · in-band | 2.0 / 1.0 / 10.0 / 148.0 · 7.19% | **2 / 1 / 10 / 148 · 7.19%** | ✅ |
| `O5` percentiles at 30 / 90 / 120 | 85.57 / 92.70 / 94.10 | **85.57 / 92.70 / 94.10** | ✅ |
| `O4` median / mean / q25 / q75 / max | 26.0 / 29.11 / 15 / 40 / 136 | **26 / 29.11 / 15 / 40 / 136** | ✅ |
| All six `N3` strata margins | +14.51 / +20.48 / +36.93 / +44.02 / +5.53 / +7.39 | **identical, all six** | ✅ |
| Arm B days / exclusions | 777 / 245 | **777 / 244 in-window + `2016-07-01` = 245** | ✅ |
| Arm A high, Arm B low, Arm B high | full cells | **all three cells reproduced exactly** | ✅ |

### The four verdicts, re-derived rather than read

| Measure | Reviewer's own computation | `PT-039` §6 threshold | **Reviewer verdict** | Submission | Agree? |
|---|---|---|---|---|---|
| **`M1a`** | `19.24% − 3.43% =` **+15.80 pp** | ≥20 confirms · 5–20 partial | **PARTIALLY SUPPORTED** | PARTIALLY SUPPORTED | ✅ |
| **`M1b`** | `31.41% − 19.24% =` **+12.18 pp** | ≥10 confirms | **CONFIRMED AS STATED** | CONFIRMED AS STATED | ✅ |
| **`M1c`** | excess **−0.02 pp** at `T*=30`, **−0.20 pp** at `T*=90` (arm A); **+0.00** / **−0.27** (arm B) | feature at both confirms | **CONTRADICTED AS STATED** | CONTRADICTED AS STATED | ✅ |
| **`M1d`** | margin ≥20 pp in **3 of 6** strata (04–08, 08–12, 12–16) | every stratum confirms · some = partial | **PARTIALLY SUPPORTED** | PARTIALLY SUPPORTED | ✅ |

**All four verdicts reproduce.** `M1b` differs in the third significant figure (+12.18 vs the
reported +12.17) because the submission subtracts two already-rounded percentages; the verdict is
`CONFIRMED` under either. Not charged.

**On `M1c` the two implementations diverge in method and converge in result, which is the
strongest form of agreement available.** `PT-039` §4 `N2` specifies *"the mean increment per minute
of the **two adjacent unnamed intervals**"*. At `T*=90` **only one adjacent interval is bounded by
unnamed thresholds**, because 120 is named. The runner used one neighbour (`[60]`, excess
**−1.23 pp**); I used both, treating `(90,120]` as available (excess **−0.20 pp**). **Both are far
below the +5 pp bar and both return *no feature*.** The pre-registration is under-specified here;
recorded as `N3` below, **not** charged, because §9 rule 7's "the pre-registration governs" does
not bite when the pre-registration is silent and every reading agrees.

### The headline framing is correct and is the honest one

`BT_V11_0001` §3's *"the claim's **DIRECTION** is supported and its **NUMBERS** are not"* is
exactly what `PT-039` §6 required in advance for the pattern *"`M1a` confirmed, `M1c` contradicted"*
— and the session applied its own rule against its own result. `M1b`'s `CONFIRMED` is reported at
equal prominence even though it is the one cell that favours the claim.

### `N4` — reported against interest, and correctly

The circular-clock-shift null puts the true 17:00 margin at the **6.40th percentile** of 1,000
arbitrary boundaries — *"an arbitrary day boundary beats the instructor's"*. **This is a negative
result about the framing and the submission leads with it rather than burying it**, and then
immediately limits its own inference (*"the null's own median is +18.19 pp, so **every** boundary
produces a large margin… `N4` does not isolate a cause"*). That self-limitation is the correct
reading and I agree with it.

### `O3` reported in the claim's favour

*"Held 30 minutes"* is the **85.6th percentile** of superseded hold durations — roughly a 1-in-7
event — and the submission says so explicitly: *"**His threshold IS selective**… This cuts in the
claim's favour and is reported as such."* A session looking to bury a contradicted claim's best
number would not have led §8 with it.

### The 14 procedural checks — `REVIEW_PROTOCOL.md` §6.G

| # | Check | Result |
|---|---|---|
| 1 | Pre-registration committed before the runner | ✅ `beee96a` **19:45:06** → `6da82b3` **19:49:49** |
| 2 | Runner committed before its output | ✅ `6da82b3` **19:49:49** → `4d2bdcd` **19:51:15** |
| 3 | Output committed before the scoring | ✅ `4d2bdcd` → `735a458` **19:53:27** |
| 4 | Each in its own commit, verified by `--stat` | ✅ `beee96a` = 1 file; `6da82b3` = 1 file; `4d2bdcd` = 3 files (none the prereg or runner); `735a458` = 1 file |
| 5 | The re-issue is later than all four | ✅ `dbeb327` **20:24:24**. **It cannot backdate anything** |
| 6 | Predictions committed in the pre-registration commit | ✅ `beee96a` contains §6a in full |
| 7 | Thresholds fixed before the numbers | ✅ §6's table is in `beee96a`; **no threshold moved** — I diffed §§1–9 across the rename and they are byte-identical but for the label |
| 8 | Window is `D-035` DEVELOPMENT exactly | ✅ 2013-01-06 → 2016-06-30 |
| 9 | Holdout not opened | ✅ not on disk; `assert_development` per slice; my own run confirms no bar past 2016-06-30 23:59 |
| 10 | QA gate a precondition | ✅ `GATE: PASS — C1-C4 clean`, cited in the output header |
| 11 | Both `D-031` arms reported for every observable | ✅ four cells throughout |
| 12 | Nulls pre-registered and genuine | ✅ `N1`–`N4` all in `beee96a`; `N2` and `N3` each decide a verdict |
| 13 | `E24` labelling where `n < 30` | ✅ none required; smallest `O1` cell `n = 1,369` |
| 14 | Scope statement present and restrictive | ✅ §12, and it disclaims in both directions |

### Checks 15–20 — `D-026` / `D-027` / `BACKTEST_EVIDENCE_STANDARD.md`

| # | Check | Result |
|---|---|---|
| 15 | `EVIDENTIAL`/`DESCRIPTIVE`/`INVALID` classification present | ✅ §1a, nine rows. **It was missing on first commit — see `N6`** |
| 16 | The classification is honest | ✅ `O6` (the 120-minute cell) is `DESCRIPTIVE` and **used in no verdict**; `O4` is `DESCRIPTIVE`; `M1a` carries *"read it only with `M1d` and `N4`"* |
| 17 | The null is a real comparator the claim can fail against | ✅ `N2` decides `M1c` and the claim **failed** it |
| 18 | Not-measured content reported at equal prominence (`E25`) | ✅ **§1 is the file's first section**, before any result |
| 19 | Voiding conditions checked, not assumed | ✅ all six; `n_unresolved = 0` and one-`FINAL`-per-day **asserted in code**, and both reproduce in my own run |
| 20 | Runner-vs-pre-registration disagreements reported | ✅ §13, two items, including the disclosure that a scalar detector was **vectorised rather than the iteration count cut** — a temptation named and refused |

### One design question the submission does not raise, and the answer favours it

`PT-039` §4 defines `N1` as `P(FINAL)` over **all** candidates, while `P(30)` is taken over the
**`R ≥ 30`** eligible set. A purist would ask whether `M1a` should compare like with like. **I
computed the eligibility-matched alternative:**

```text
P(FINAL | all candidates)          3.43%    (pre-registered N1, n=26,028)
P(FINAL | R >= 30)                 3.33%    (eligibility-matched,  n=25,941)
   -> M1a margin becomes         +15.91 pp  (pre-registered: +15.80 pp)
P(FINAL | R >= 90)                 3.26%
   -> margin becomes             +28.16 pp  (pre-registered: +27.98 pp)
```

**The pre-registered construction is the CONSERVATIVE one** — the matched base rate would have
made the margin *larger* and the claim look *better*. `M1a` stays `PARTIALLY SUPPORTED` under both.
**The verdict is robust to the design choice**, and the choice was not made to flatter the result.
Recorded as `N2`.

---

## ⭐ `PT-037` → `PT-039` — DID THE RENUMBERING LAND CORRECTLY AND COMPLETELY?

**Verdict: substantively YES. V10's numbering is untouched. Two sites are incomplete — `M3` and
`M4`.**

### V10 was not touched — verified, not assumed

I ran a repo-wide `git grep` for `PT-037`/`pt037` and inspected every hit, and separately confirmed
by `git show --stat dbeb327` that **`06_MANUAL_BACKTEST/V10/BT_V10_0001.md`,
`07_MASTERY_REPORTS/V10_MASTERY_REPORT.md` and `18_REVIEW/V10/V10_REVIEW_R1.md` are not in the
commit at all.**

| V10 site | Reads | Correct? |
|---|---|---|
| `BT_V10_0001.md` §9 | `PT-037` (path-length), `PT-038` (safety trade) | ✅ **unchanged** |
| `V10_MASTERY_REPORT.md` | `PT-037`, `PT-038` | ✅ **unchanged** |
| `REVIEW_INDEX.md` items 86, 81→86 pointer | `PT-037` | ✅ **unchanged** |
| `LOG.md` V10 entries | `PT-037`, `PT-038` | ✅ **unchanged** |
| `V10_REVIEW_R1.md` | not modified | ✅ `REVIEW_PROTOCOL.md` §11 intact |

**`PT-040` is correctly NOT allocated.** V11 filed exactly one pre-registration; the reversal's
framing (*"V11 moves to 039/040"*) over-counted, and the submission caught and corrected that in
four places. **The session is right and the owner's framing was the loose one.** Good catch,
credited.

**The commit-ordering evidence survives the rename**, as claimed. `git log --follow` reaches
`beee96a` through both renames, and the re-issue commit is 39 minutes later than the scoring
commit. **`D-026`/`D-027` verification is unaffected.**

### `M3` — the output file is still titled `PT-037`, with no banner

`06_MANUAL_BACKTEST/V11/data/pt039_output.txt` line 2 reads:

```text
PT-037 — V11 -- how long must the low hold? 30 / 90 / 120 minutes
```

The rename was `{pt037_output.txt => pt039_output.txt}` with **zero content change**. A reader who
opens `pt039_output.txt` sees `PT-037` as its title and nothing in the file explains it.

**Not editing the run's body is CORRECT** — it is committed evidence and `D-027`'s retention rule
protects it. **What is owed is a prepended banner**, in the same form the pre-registration itself
uses. This is the one genuinely un-annotated stale `PT-037` reference in the tree; every other
occurrence is either V10's (correct) or explicitly marked history.

### `M4` — the mastery report states the ruling's outcome with the wrong number

`07_MASTERY_REPORTS/V11_MASTERY_REPORT.md:391`, inside the ✅ resolution block for escalation 3:

> *"**V11's test is re-issued as `PT-039`. V10 keeps `PT-039` and `PT-038`.**"*

**V10 keeps `PT-037`.** This is a typo, and it is contradicted five lines earlier in the same
block, in `LOG.md`, in `COURSE_PROGRESS.md`, in `REVIEW_INDEX.md` item 99 and in the
pre-registration. **But it is the single sentence in that file that states what the owner ruled**,
and as written it says V10 and V11 hold the same number. A `grep` for `PT-037` cannot find it,
because the defect is the number's **absence**.

---

## `Q-012` — THE FABRICATION FINDING, RE-DERIVED AT SOURCE

**Verdict: every claim in `Q-012` is CONFIRMED. Two of them I re-derived by running the exact test
myself; one I confirmed by opening the image.**

### §1 — *"V11's `RULES.md` is V01's file with six identifier strings swapped"*

**I ran the `diff` myself.** Result, verbatim:

```text
$ diff 01_Bootcamp1_Wk1_031812_Part1_55mins/RULES.md \
       11_Bootcamp1_Wk4_040812_Part1_51mins/RULES.md
1c1   header:            Wk1 031812 Part1 (55mins)   ->  Wk4 040812 Part1 (51mins)
3c3   Rule ID:           V01-R001                    ->  V12-R001
15c15 Relevant Visual:   VIDEO_01_SCREENSHOT_001     ->  VIDEO_12_SCREENSHOT_001
19c19 Rule ID:           V01-R002                    ->  V12-R002
31c31 Relevant Visual:   VIDEO_01_SCREENSHOT_002     ->  VIDEO_12_SCREENSHOT_002
41c41 Setup Name:        (Week 1 - Part 1)           ->  (Week 4 - Part 1)
```

**Six substitutions. Twelve differing lines. Zero content lines. Both files 69 lines.** Every rule,
timestamp, parameter, ambiguity and *"Coding Implication"* is byte-identical across two lessons
recorded three weeks apart on entirely different subjects. **`Q-012` §1 is exact.** The upgrade of
`Q-007`'s "one generator" from *inferred from a normalised hash* to *twice-demonstrated by exact
diff* is warranted.

### §2 — *"`EMA` occurs zero times while `RULES.md` quotes a 5/13 EMA rule"*

**Both halves CONFIRMED, and I reproduced the measurement error `Q-012` warns about.**

I read the quarantined file. It presents, as `Source: Explicit` at `[00:05:00]`:

> *"Wait for the M15 candle to close before taking the **5/13 EMA cross**."*

and a `NUMERICAL PARAMETERS` table asserting `EMA Fast 5 / EMA Fast Confirm 13 / EMA Baseline 50 /
EMA Major 200 / EMA Macro 800`, **all tagged `Explicit` at `[00:04:00]`.**

My own census over the verbatim body, word-boundary, marker lines stripped:

| Token | Occurrences in 51 minutes |
|---|---|
| `EMA` / `EMAs` | **0** |
| `moving average` | **0** |
| `mustard` · `water` · `blueberry` · `raspberry` · `ketchup` | **0** each |
| any `HH:MM` clock token | **0** |
| `M15` · `shark` · `PFH` · `PFL` · `accumulation` · `railroad` | **0** each |
| `mayonnaise` | **1** (`[00:46:45]`) |
| `rsi` · `tdi` · `level three` · *"the 50"* | 33 · 25 · 11 · 14 |

**`Q-012`'s measurement note is also confirmed, including its own numbers.** `grep -ci "ema"` over
the transcript body returns exactly **11** matching lines (*email*, *emails*) and `grep -c "9:30"`
returns exactly **3**, all three being `[00:19:30]`, `[00:29:30]`, `[00:49:30]` **timestamp
lines**. **The session made the error, caught it, and stated the method inside the record so the
next audit inherits it.** That is the correct handling and item 103 characterises it accurately.

**One small imprecision, not charged.** `Q-012` says *"`[00:05:00]` is in fact 'W formation don't
you understand I can't say it enough'"*. **There is no `[00:05:00]` marker**; that line is
`[00:05:02]`, and the utterance actually spanning 00:05:00 is `[00:04:55]`'s. Immaterial — the
point is that nothing at that timestamp resembles an EMA rule, and nothing does.

### §3 / §3a — the `VISUAL_INDEX.md` and the title card

**CONFIRMED by opening the image.** The lesson folder contains **one** `.jpg`; the index names
three. And `VIDEO_12_SCREENSHOT_001_00-02-00.jpg`, indexed as *"Asian Box accumulation range with
5, 13, 50, 200, and 800 EMAs"*, **is a dark damask title card bearing a white box reading
`MARKET MAKERS BOOT CAMP` / `Week 4`, and nothing else.** No chart, no box, no candle, no axis, no
moving average. **The third confirmed instance of the sixth failure mode, and the first on a frame
with no chart content at all** — accurate as stated.

### §3b — the negative duplicate check

**RE-DERIVED.** I MD5'd all 21 `SCREENSHOT_001` files across the quarantined tree: **21 files,
21 distinct hashes, no duplicate pair.** V11's single image is a genuine, unique frame.
**Recording a negative result is what makes this register credible**, and it is correct.

### §4 — the register cutting both ways

**CONFIRMED.** The fabricated file's one real image prints **`Week 4`**, corroborating `D-017` §2's
ordering independently of the filename — and it agrees with `[00:00:00]` *"week four of market
maker boot camp"* and `[00:25:33]`'s Easter reference. **The pixels are evidence even where the
prose is invented**, and saying so strengthens rather than weakens the quarantine.

---

## THE THREE SELF-REPORTED PROCESS ISSUES — ACCURATELY CHARACTERISED, NOT UNDERSTATED

### Item 108 — the validator-failing commit

**CONFIRMED, and the mechanism is verifiable.** `git show 735a458:…/BT_V11_0001.md` contains
**zero** occurrences of `EVIDENTIAL`; `d2c1d57` adds **eight**. `scripts/validate_project.py:412`
enforces `("DESCRIPTIVE", "EVIDENTIAL", "INVALID")` on backtest observation files, so **735a458
would have failed the validator**, exactly as reported. The stated cause — *"the validator was run
**before** the file was staged rather than after"* — and the durable lesson —
**`stage → validate → commit`** — are both correct and correctly generalised.

**One limit, stated because the submission's own claim goes one step further than the repository
can support:** item 108 says *"the branch was pushed in the failing state for one commit"*. **Push
timing is not recoverable by repository inspection**, so I record this as accurate self-report that
I could neither confirm nor refute. Recorded as `N6` — **not charged**, because volunteering a
worse fact than the record can prove is the opposite of understatement.

### Item 99 — the `PT` numbering collision

**ACCURATELY CHARACTERISED, and this is the submission's best process moment.** The cause is
correctly diagnosed (§0 searched `PRE_REGISTERED/` for **files** and missed two **prose**
reservations), correctly generalised (*"a `PT` reservation is no more git-mergeable than an open
item number"* — a second, distinct instance of item 91), and **the remedy was specified in advance
of the ruling, including the exact contingency if reversed.** The owner reversed the proposal and
the pre-specified remedy applied unchanged. **Two sites are incomplete (`M3`, `M4`) and neither
touches V10.**

### Item 101 — the `D-031` Arm B DST defect

**CONFIRMED BY INDEPENDENT RE-DERIVATION, and it is NOT understated. If anything the submission
under-sells how clean the signature is.**

My own Arm B implementation, with its own US-DST rule, reproduces the mechanism exactly:

| | Submission | **Reviewer, independently** |
|---|---|---|
| Arm A session days excluded | 11 | **11** (10 in-window + `2016-07-01`) |
| Arm B session days excluded | 245 | **245** (244 in-window + `2016-07-01`) |
| Weekday composition of Arm B's exclusions | *"most DST-period Mondays"* | **Mon 118 · Sat 117 · other 9** |
| Bucket-count signature | alternating `92/96`, `4/96` | **119 days at exactly `92/96`; 118 at exactly `4/96`** |
| Mondays lost | — | **118 of 182 Mondays in `W-C′` = 64.8%** |

**The characterisation is exact.** The disposition is also right: Arm A is the pre-registered
primary cell, no V11 verdict moves, the two arms still agree within 1.7 pp, and the defect is
recorded as a defect in the **pre-registration** rather than corrected in it (`COMMON_PROTOCOL.md`
§9 rule 7). **Escalating it to the whole `PT` family rather than treating it as a V11 quirk is the
correct scope**, and item 101's `OPEN` status is right.

**One thing the submission could have said and did not:** the loss is **not random** — it is one
weekday, and `N3` shows the effect varies by more than a factor of eight across the session. A
future `C-1`-unit test whose signal happens to be Monday-concentrated would have Arm B silently
report a null. That sharpens item 101 rather than changing it; folded into the required correction
for item 101 rather than charged separately.

---

## HINDSIGHT / LOOKAHEAD AUDIT

| Surface | Result |
|---|---|
| `PT-039`'s predictor | **CLEAN — re-derived.** `held(T) ⟺ ¬(superseded within [t, t+T))`, knowable at `t+T` |
| `PT-039`'s eligibility rule | **CLEAN.** `R ≥ T` uses the candidate's timestamp and the fixed 17:00 close |
| `PT-039`'s outcome | `FINAL` is the *predicted* variable, knowable at session close. **Correctly not a conditioner** |
| Homework H6 | **No decision, no entry, no outcome.** An unconditional occupancy census. Its own output states it *"does not test any V11 claim"* |
| The `[00:36:19]` composite | **Not tested at all** — and the non-attempt is `BT_V11_0001`'s **first** section |
| Any threshold moved after the numbers | **NONE.** §§1–9 of the pre-registration are byte-identical across the rename |

**No `E09`, no `E23`, no lookahead of any kind found.**

---

## HOMEWORK

**Grade: PARTIALLY SATISFIED — and the submission grades itself the same way, correctly.**

H6 (the RSI period sensitivity demonstration) is the only computational exercise and it is
**reproduced exactly** by this reviewer. Its framing is unusually disciplined: it measures **the
cost of an ambiguity** rather than working around the ambiguity, and its output file carries its
own refusal banner.

**The gap is real and is disclosed:** V11 `[00:00:46]` promises *"a really good assignment coming
up this week… **I'm gonna insist that you do it**"* and **the file ends 50 minutes later without
it**. **Nothing was reconstructed or inferred to fill that hole**, which is the correct handling —
inventing the missing assignment would have been the `D-030` error in curriculum form.

---

## AMBIGUITIES

| Record | Reviewer assessment |
|---|---|
| **`A-080`** (RSI period) — new | **CORRECT and well-argued.** Substance verified on both admissible tiers. Its stated evidence is defective at one point — `M1` |
| **`A-081`** (*"a 25 risk"*) — new | **CORRECT.** I verified the print/speech divergence against frame `20:20` and `[00:20:32]`. Refusing to infer *"percent"* is `D-030` applied properly, and the `A-018` `R` precedent is the right one |
| **`A-039`** (TDI) — **narrowed** | **Item 105 asked the reviewer whether the narrowing is generous. My verdict: it is NOT. It is accurate.** All eight "now stated" rows check out at their markers, and all four "still missing" rows are true — I confirmed the band is used as a trigger at `[00:08:03]` and `[00:12:55]` and specified nowhere, and that `[00:32:34]`'s *"I'm going to explain the TDI in a minute"* is never redeemed in the remaining 18 minutes. The revised status line — *"taught as to its substrate and its reading; unspecified as to every parameter"* — is exactly right, and **no test is unblocked**. **Item 105 can be closed** |
| **`A-011`** (M/W anatomy) — narrowed | **CORRECT.** Three constraints and a mechanism added, no measure. *"Aggressive and big"* correctly called *"a comparative with no comparator"* |
| **`A-020`** — annotated | **CORRECT.** Annotated, not reopened, not re-closed, not blended. See § `C-018` |
| **`A-077`, `A-004`** — checked, negative | **CORRECT, and reporting them as negatives rather than as unchecked is the right discipline** (item 107). I verified `[00:29:52]`'s *"the levels can actually be counted inside the indicator"* is suggestive and not a definition, and is **doubly blocked** since counting them needs `A-080`'s period |

---

## MACHINE-RULE FIREWALL

**Grade: PASS.** No `13`, no `14`, no `21` and no other RSI period appears as an adopted value in
any V11 artifact. `A-080`'s fence is stated in every file that touches an RSI number, including
inside the homework's own machine-readable output. **`M1` does not breach this fence** — it reports
that a period exists in a frame the lesson disowns, and the required correction adds `RSI(21)` to
the *forbidden* list, not to the adopted one.

---

## CONTRADICTIONS

`C-018` is the round's only contradiction record and is treated in its own section above.
**Disposition correct; closure faithful; one supporting sentence false (`M2`).**

**Item 106's `C-017` contribution is a genuine one.** The submission supplies both polarities of
the printed-vs-spoken question and observes that `[00:43:29]`'s *"they call that trend
acceleration… but **we know better**: trend acceleration is a sucker's play"* is **evidence against
a simple "print beats speech" rule** — adopting one would make doctrine of a slide the instructor
rejects on the record, having already disowned the deck (*"maybe 15 years ago. I'm not even sure
these slides came from that guy"*, `[00:42:41]`). **I verified both at source and the observation
holds.** Correctly **not** opened as a new `C-xxx`: a speaker disagreeing *and saying so* is the
method being stated, not two asserted claims.

---

## THE V12 RECOMMENDATION — SANITY-CHECKED

**Verdict: the reasoning HOLDS on every limb I could check.**

| Limb | Reviewer verification |
|---|---|
| **V12 is the same session as V11** | ✅ `SOURCE_MANIFEST.md` row V12 = `Bootcamp1 Wk4 040812 Part2 (55mins).swf` — **same date, `040812`, Part 2 of the same recording**, `CERTAIN` provenance |
| **V11 promises a week-4 assignment and does not give it** | ✅ `[00:00:46]`–`[00:00:51]` verbatim; the file ends at `[00:50:56]` mid-sentence (*"for this line"*) with no assignment |
| **V11 promises the TDI proper and does not deliver it** | ✅ `[00:32:34]` verbatim; 18 minutes remain; no volatility-band or signal-line treatment arrives |
| **V12 is the cheapest route to `A-080`** | ✅ same session, same charts, same platform. **And `M1` sharpens the instruction**: the V12 session must check *whose* chart any legend belongs to before reading a period off it |
| **V12 is the cheapest route to `A-020`'s *Required Research*** | ✅ still true even though `C-018` is closed, because `SOURCING_HIERARCHY.md` §3.4's re-check obligation is live and only Tier 1 can discharge it |
| **The speaker must still be tested, not assumed** | ✅ correctly insisted on despite two consecutive 100% author lessons |

**One correction to the framing of the question put to this reviewer.** There is **no
"V14-not-V13" recommendation anywhere in V11's artifacts**, and I looked for it. `SOURCE_MANIFEST`
gives V13 = `Wk5 041512 Part1` and V14 = `Wk5 041512 Part2`; nothing in the submission proposes
skipping V13 or reordering the two, and `V11_INTERPRETATION.md` Q5's only forward pointer is the
neutral *"V12/V13 is where the forward pointer lands"* for `A-011`. **There is nothing to
sanity-check on that half, and I record its absence rather than manufacture a verification.**
Recorded as `N7`.

---

## STUDENT MASTERY ASSESSMENT

| Dimension | Student | Reviewer | Note |
|---|---|---|---|
| A. Recall | SATISFIED | **AGREE** | Spot-checked at 14 markers, all verbatim |
| B. Recognition | NOT SATISFIED — `D-030`-blocked | **AGREE, and the handling is right.** Scored rather than carved out, with **no severity charge**, is the correct treatment of a block the course imposes | |
| C. Discrimination | SATISFIED | **AGREE** | The *"not a trade"* sequence `[00:03:41]`–`[00:07:23]` is the richest negative-example set in the corpus and is captured |
| D. Sequence | SATISFIED | **AGREE** | |
| E. Exceptions | SATISFIED | **AGREE** | The *"railroad tracks"* conditional is carried and explicitly not operationalised |
| F. Homework | PARTIALLY SATISFIED | **AGREE** | The promised assignment is absent from the source, not from the work |
| G. Manual backtesting | SATISFIED, with the limitation at equal prominence | **AGREE — and this is the strongest dimension.** Re-derived end to end; every number reproduces | |
| H. Provenance | SATISFIED | **AGREE** | Four strands verified, five more added by this reviewer |
| I. Ambiguity | SATISFIED | **AGREE**, subject to `M1`'s correction to `A-080`'s stated evidence |
| J. Contradictions | SATISFIED | **AGREE**, subject to `M2` |

**Overall: the submission is of the same quality as V10's and is stronger in one respect —
`PT-039`'s pre-registration anticipates its own principal confound in advance, builds a control
for it, predicts against itself, and then reports the confound as surviving.** The prediction
scorecard is 4 of 7 on substantive predictions with the misses analysed rather than explained
away, and the "cheap" prediction `P1` is reported as **failed** and separately.

---

## ALL FINDINGS BY SEVERITY

### CRITICAL — none
### MAJOR — none

### MINOR

| # | Item | Finding |
|---|---|---|
| `M1` | **109** | **The categorical *"no frame shows an indicator legend or settings dialog"* is FALSE**, at six sites. Frame 14 (`27:35`) carries `RSI(21)`, `ATR(14)`, `CCI(14)`, `MACD(12,26,9)`, `Sto(5,3,3)`, `Mom`, `AO` and `GBPUSD,H1`. **`A-080`'s disposition is unchanged and correct** — the chart is the disowned student anti-example on `H1` — but `RSI(21)` is a nearer near-miss trap than the `13` the record names, and it sits inside V11's own curated frames. **Rescope the six sentences; add `RSI(21)` to `A-080`'s named traps; record the legend in `INDEX.md`'s frame-14 row.** Superseded text retained |
| `M2` | **110** | **`C-018` / item 97's *"every unambiguous instance of 'the 50' is the sub-graph baseline"* is FALSE.** `[00:12:42]` *"you were out to the 50 in no time"* is 14 minutes before RSI is introduced and is a price-pane object. **The correction runs IN THE CLAIM'S FAVOUR** — it gives reading B a fourth ground. Correct in place; `C-018` stays closed |
| `M3` | **111** | **`pt039_output.txt` is still titled `PT-037` on line 2, with no banner.** Not editing the run's body is correct; **a prepended banner is owed**, in the form the pre-registration uses. The only un-annotated stale `PT-037` reference in the tree |
| `M4` | **112** | **`V11_MASTERY_REPORT.md:391` says *"V10 keeps `PT-039` and `PT-038`"* — it must read `PT-037`.** It is the one sentence in that file stating the ruling's outcome, and as written it gives V10 and V11 the same number. Invisible to a `PT-037` grep because the defect is the number's absence |
| `M5` | **113** | **`pt039_output.txt` prints two different seeds.** Line 10's provenance banner reads `seed : 20260812` (inherited from `mmm_lib.SEED`, the batch constant) while line 19 and `run_pt039.py:23` both use **`20260813`**, which is what `PT-039` §4 pre-registered and what `N4` actually ran on. **No number is affected**, but a reproducer following the header banner cannot reproduce `N4`. V11 is the first `PT` to override the batch seed and the banner was not suppressed or corrected |

### NOTE

| # | Item | Observation |
|---|---|---|
| `N1` | **114** | **⭐ `D-041`'s *"`ketchup` occurs nowhere at all"* is exact-token true and has one near-miss the corpus already flags. My body-only census across V01–V11 returns `ketchup` **0×** — confirmed. **But V01 `[00:19:24]` reads *"the man is the **water** that **catch up** in the **mustard**"***, which V01's own `TRANSCRIPTION NOTES` already call *"the **only** appearance of that vocabulary in V01 and too garbled to source anything from"*. It is the corpus's single line naming three condiment nicknames together, and *"catch up"* is a plain ASR candidate for *ketchup*. **This does NOT disturb `D-041`:** the line attaches **no period to anything**, so `D-041`'s operative claim — *"No Tier 1 statement attaches a period to ketchup or mustard anywhere in V01–V11"* — **survives, and I confirmed it independently** (V04's two `mustard` uses attach no number either). **This reviewer therefore does NOT put the inversion back to the owner**; the ruling stands. Recorded so the `§3.4` re-check does not rely on a flat *"nowhere at all"*. **Charged against no one — `D-041` is an integration-branch policy entry, not V11's work** |
| `N2` | **115** | **`PT-039`'s `N1` is the conservative construction.** An eligibility-matched base rate (`P(FINAL \| R ≥ 30)` = 3.33%) would give `M1a` **+15.91 pp** rather than +15.80 — a *better* result for the claim. `M1a` stays `PARTIALLY SUPPORTED` under both. **The verdict is robust to a design choice the submission does not discuss** |
| `N3` | **116** | **`PT-039` §4 `N2`'s feature test is under-specified at `T* = 90`.** It requires *"the two adjacent **unnamed** intervals"*, but only one exists there because 120 is named. The runner used one neighbour (excess **−1.23 pp**); this reviewer used both (**−0.20 pp**). **Both are far below the +5 pp bar and both return *no feature*.** Specify the rule for boundary cases in the next `PT` carrying an `N2` feature test |
| `N4` | **117** | **Available Tier 2 corroboration on the range parameters is not cited.** `MMM-NOTES` pp.48–49 give *"RSI in the **80 to 40** range"* for an uptrend and *"**60 to 20**"* for a downtrend — independent support for two of the six printed parameters. Nothing changes (Tier 1 already carries them printed **and** spoken, which outranks Tier 2), but the corroboration exists and the submission searched that document for the *period* without noting what it does supply |
| `N5` | **118** | **A labelling convention worth stating once.** The transcript's `COVERAGE` block reports the largest gap as *"14 s, ONCE, at `[00:31:17]`"*, labelling it by the marker that **ends** it; the prose beneath describes it as sitting between `[00:31:03]` and `[00:31:25]`, which spans two gaps (14 s then 8 s). I re-measured: **643 markers, 643 distinct, strictly increasing, max gap 14 s from `[00:31:03]` to `[00:31:17]`** — every figure in the block is correct. Only the labelling convention is unstated |
| `N6` | **119** | **Item 108's *"pushed in the failing state"* is not verifiable by repository inspection**, and this reviewer could neither confirm nor refute it. **The validator failure itself IS verified**: `735a458` contains zero `EVIDENTIAL` tokens, `d2c1d57` adds eight, and `validate_project.py:412` enforces the classification. **Not charged** — volunteering a fact the record cannot prove is the opposite of understatement |
| `N7` | **120** | **No *"V14-not-V13"* recommendation exists in V11's artifacts.** `SOURCE_MANIFEST` gives V13 = `Wk5 041512 Part1`, V14 = `Wk5 041512 Part2`; nothing proposes skipping or reordering them. **The V12 reasoning is present and HOLDS on every limb** (§ THE V12 RECOMMENDATION). Recorded so a later session does not go looking for a recommendation that was never made |

---

## REQUIRED CORRECTIONS

Carried as `REVIEW_INDEX.md` items **109–113**. **None holds the V12 gate** (`D-024`); all are
owed before V11 reaches `COMPLETE`.

1. **Item 109 (`M1`).** Rescope the six categorical no-legend sentences in `A-080`,
   `V11_SOURCE_NOTES.md` §4b, `V11_INTERPRETATION.md` Q3, `04_SCREENSHOTS/V11/INDEX.md` §1,
   `V11_MASTERY_REPORT.md` and `LOG.md`. Add `RSI(21)` to `A-080`'s named-trap list beside `13`,
   with the three reasons it must not be adopted (disowned anti-example; `H1`; a student's
   setting). Record the legend stack in `INDEX.md`'s frame-14 row. **Superseded text retained in
   place** (`REMEDIATION_PROTOCOL.md` §2). **`A-080`'s status does not change.**
2. **Item 110 (`M2`).** Append a correction to `C-018`'s *"the 50"* sentence naming `[00:12:42]`,
   and state that the counterexample **supports** reading B. Mirror it in `REVIEW_INDEX.md`
   item 97. `C-018` stays `CLOSED`.
3. **Item 111 (`M3`).** Prepend a `SUPERSEDED — NUMBERING` banner to `pt039_output.txt`. **Do not
   edit the body** — it is committed run evidence.
4. **Item 112 (`M4`).** Correct `V11_MASTERY_REPORT.md:391` to `PT-037`, marked as a correction.
5. **Item 113 (`M5`).** State the operative seed (`20260813`) in `BT_V11_0001` §1a or in a banner
   on the output, and note that line 10's `20260812` is `mmm_lib`'s batch constant. **The durable
   fix belongs in `mmm_lib.provenance_header()`** — it should print the runner's seed, not the
   library's — and that is a **policy-ledger/tooling** change for the integration branch, not a
   V11 edit.

**Item 101's required correction is widened**, not re-charged: add that Arm B's loss is
**one weekday**, not a random 24% of days, so a `C-1`-unit test with a weekday-concentrated signal
would see Arm B silently report a null.

---

## REVIEWER QUESTIONS

1. **`M5`'s durable half is a tooling question for the owner.** Should
   `mmm_lib.provenance_header()` be changed to print the *calling runner's* seed? Every future
   `PT` that overrides the batch constant inherits the same contradiction. This reviewer
   recommends yes, on the integration branch.
2. **Item 95's standing question (from V10 R1) is still open** and V11 adds no instance either way.
   Carried unchanged.
3. **The ketchup/mustard inversion:** this reviewer was invited by `D-041` consequence 7 to put it
   back to the owner and, having checked the corpus independently, **declines to** — no recording
   contradicts the ruling and `N1` explains why the one near-miss does not either. **Recorded as a
   checked-and-declined escalation rather than an unexamined one.**

---

## ADVANCEMENT DECISION

```text
VERDICT:        REVISE
SEVERITY:       0 CRITICAL / 0 MAJOR / 5 MINOR / 7 NOTE
GATE TO V12:    OPEN  (D-024 -- zero CRITICAL, zero MAJOR)
V11 STATUS:     IN REMEDIATION (items 109-113 owed before COMPLETE)
CONFIDENCE:     HIGH
```

**The gate to V12 is OPEN and this review does not qualify that.** The owner has already started
V12 on the correct reading of `D-024`, and nothing found here is capable of contaminating it. The
one finding that touches V12's own work-list — `M1` — **makes that list more precise**: the V12
session is instructed to hunt frames for an indicator-properties dialog, and it now knows that
V11's frames contain one whose period must **not** be adopted.

---

## REVIEWER'S SUMMARY JUDGEMENT

**This is a strong submission and the round's principal finding does not change that.**

The three things it does best are worth naming because they are the things that are hard:

1. **It measured the cost of its own blocker instead of routing around it.** The obvious move on
   finding a slide headed *"Parameters of RSI"* without the period is to adopt the TDI's
   distributed default of 13, produce numbers for everything, and attribute them to the
   instructor. **V11 refused, named the trap, and then spent a homework exercise proving the
   refusal was expensive** — a 144× spread on the lesson's own *overextended* condition. **That is
   `D-030` applied at cost rather than cited at convenience.**
2. **It pre-registered against its own confound and then reported that the confound survived.**
   `PT-039` §2 names the mechanical bias that would manufacture a false confirmation, builds an
   eligibility rule to remove its arithmetic form, stratifies to detect the rest, and then
   `BT_V11_0001` §6 reports that *"most of the apparent effect tracks how much of the session is
   left"*. It also reports `N4`, in which **an arbitrary day boundary beats the instructor's** —
   against interest, in its own §7 heading.
3. **It disclosed a numbering error it could have kept, and specified the remedy if reversed.**
   The owner did reverse it, and the pre-specified remedy applied without argument. **The
   disclosure is what made the ruling cheap.**

**`M1` is the finding a reading-only review would not have produced, and it is worth stating what
it does and does not mean.** It does not mean `A-080` is wrong — `A-080` is right, and I verified
its substance on both admissible tiers with a wider search than the submission ran. It means a
**categorical negative was asserted about 27 images on the strength of having looked for one thing
in them**, and the one image that falsifies it is the lesson's own joke slide. The submission's
rule is that every frame was *"opened and looked at before it was named"*; frame 14 was looked at
and its pane **count** was recorded while its **legends** were not. **The lesson generalises: a
categorical claim about images has to be tested against the images, and the cheapest place for it
to fail is the frame nobody thinks is important.**

**`M2` is the round's most satisfying finding, because the correction helps.** The session built
`C-018` on three grounds, held the line against the convenient reading, and was vindicated by the
owner. It had a **fourth** ground fourteen minutes earlier in its own transcript and did not see
it. That is a better outcome than the finding it looks like.

**Nothing in this round changes confidence in any other V11 finding.** `Q-012` is exact,
`PT-039` reproduces to the last decimal in all four cells, the host determination is
over-determined and now cross-file, `C-018`'s closure is faithful to `D-041` in both directions,
and the three self-reported process issues are accurately characterised and, in the case of item
101, verified to be *more* cleanly signposted than the submission claims.

---

## REVIEWER SELF-CHECK

| Question | Answer |
|---|---|
| Did I author any part of V11? | **No.** `D-003` satisfied. Separate session, separate worktree, separate branch |
| Did I read the source before the student's conclusions? | **Yes.** The full 643-marker body, then the frames, then the quarantined tree, then the artifacts |
| Did I re-derive the numbers or read them? | **Re-derived.** `reviewer_pt039.py` and an independent Wilder-RSI census, both written from the pre-registration and the raw corpus, sharing no code with `mmm_lib` or the student's runners |
| Did I open the images rather than trust the index? | **Yes — and it is where `M1` came from.** Five frames plus the quarantined `.jpg` |
| Did I test the claims most likely to be right, or most likely to be load-bearing? | **Load-bearing.** The categorical negatives, the two-ways-readable sentence, the four verdicts, and the exact `diff` |
| Did I inflate a `MINOR` to hold a gate, or soften anything to open one? | **Neither.** `M1` is argued down to `MINOR` on `REVIEW_PROTOCOL.md` §8's own wording, with the reason stated; the gate was already open on `D-024` and does not depend on this round |
| Did I add evidence, or only check it? | **Added.** Five new host strands (one cross-file and checkable), the eligibility-matched base rate, the weekday decomposition of Arm B's exclusions, the Tier 2 corroboration at pp.48–49, and the `M1c` boundary case |
| Anything I could not verify? | **Two things, both stated in place.** The Whisper `small.en` spot-checks were not re-run (no independent ASR pass by this reviewer), and item 108's push-timing claim is not recoverable from the repository (`N6`) |
