# V10 — SCREENSHOT INDEX

**Lesson:** V10 · `Bootcamp1 Wk3 040112 (96mins).swf` ·
SHA-256 `a37ba371ca2d5c807553c7b9a827a91c479509dd5223b64eadf85995481a3de1` · 01:36:16
**Session date:** 2012-04-01 (filename `040112`; **stated in-recording** at `[00:21:25]`)
**Speaker:** the **course author**, 100% of runtime — see `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md`
§ SPEAKER IDENTIFICATION. `D-033` makes this immaterial to weight and material to provenance.

---

## HOW THESE WERE CAPTURED

Per `00_SYSTEM/SWF_CAPTURE_RECIPE.md` §10 (fast sweep) **as patched by `GOTCHA 5`** at commit
`89bb858`. Every step that has historically failed silently was checked rather than assumed:

| Step | What was done | Result |
|---|---|---|
| **Stage size read FIRST** (`GOTCHA 5`) | SWF header RECT parsed before any capture | **1024 × 786** — the majority class, so the table gives `(512, 300)` |
| **Frame rate read, not assumed** | SWF header | **2.0 fps, NOT 3.0.** The recipe §10 quotes 3.0 from V01/V02; the 10× patch here is **2.0 → 20.0**. **A session that patched 3.0 → 30.0 on this file would have swept at 15×, not 10×, and silently under-sampled.** Recorded as a defect in the recipe's wording — see ESCALATIONS |
| **Original never modified** | `shasum -a 256` on the source before and after patching a working copy | **identical both times** (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| **Port ownership** (`GOTCHA 4`, `D-022`) | First candidate port **8963 was BUSY**, held by another session's `http.server`. Rejected; **8971** bound and confirmed by `lsof` to be this session's own PID | `D-022` **fired for real, again** — third consecutive lesson |
| **Bytes served == bytes on disk** (`D-022`) | `curl \| shasum` vs `shasum` of the served file | **match** |
| **Play-click guard** (`GOTCHA 5` general fix) | Screenshot before, click `(512, 300)`, screenshot 1.5 s after, abort non-zero if byte-identical | **`PLAY CLICK CONFIRMED` — the stage changed.** The table's coordinate was *verified*, not trusted |
| **Content sanity check vs transcript** (`GOTCHA 4`) | Frame at burned `08:38` read as an image and compared to the transcript at `[00:08:25]` | **Match.** The slide shows a student email asking about *"not to trade on Sunday/Monday … trade against the false move week beginning"*; the audio at that marker is answering exactly that question. **Right file, right lesson, confirmed in the first minutes rather than after an hour** |

**Sweep:** 1,164 frames at 5 presentation-seconds apart. **Screen-state detection:** pairwise
luminance diff on 256×196 downsamples, threshold 6.0, runs collapsed within 2 frames →
**38 distinct states**. Three are pure-black application-switch transitions (measured mean
luminance **exactly 0.0** at frames 462, 680, 759) and are **not** curated. **32 frames retained.**

### Timestamps are the player's own burned-in timecode, verified — not computed and asserted

The frame→time map is linear, `t = 5i + 18 s`. It was **not** trusted: the burned-in timecode of
**all 32 retained frames** was cropped into a single strip and **read**. Every one agrees with the
map to **≤ 2 s**, and **every value is at or below the 96:16 runtime**. The largest discrepancy is
2 s, at the end card.

**Frame cross-references in every V10 artifact name the frame by its burned-in player timecode**,
not by an ordinal — `V09_REVIEW_R1.md` `M4` / open item 76 established that rule and it is
followed here from the start. The ordinals in the table below are internal to this file and
nothing outside it cites them.

---

## THE INDEX

| # | File (`V10_…`) | Burned TC | What is VISIBLE | Why it matters | Class |
|---|---|---|---|---|---|
| 1 | `00-00-33_title-card-week-3` | `00:33` | Title card: **`Market Makers Boot Camp`** / **`Week 3`** | The lesson's only printed banner. **Independently corroborates `D-017` §2's ordering** for this file, which until now rested on the filename and the date derivation | PRINTED |
| 2 | `00-02-08_managing-your-expectations-slide` | `02:08` | *"Managing Your Expectations … Give me 2 Hrs a week! … Execute in demo the concepts as illustrated"* | Sets the week's contract with students; the demo instruction is the only execution-venue statement in the lesson | PRINTED |
| 3 | `00-03-08_reading-the-emails-intro-slide` | `03:08` | *"There is No question that some of you are mental!! … Reading through the e-mails here are some of the problems"* | Marks the start of the mailbag segment (`[00:03:08]`–`[00:17:22]`) | PRINTED |
| 4 | `00-04-13_list-of-student-problems-slide` | `04:13` | Bulleted list: *"Entering too soon (not confirmed second leg) / Exiting too early / Displacing the blame / Mental blocks from old systems / To many indicators / Lack Self Confidence"* | **The first bullet names *"not confirmed second leg"* as the #1 student error** — which is the exact element the safety trade later requires. It frames the whole lesson | PRINTED |
| 5 | `00-05-03_i-cannot-teach-you-this-slide` | `05:03` | *"I can teach you all day and all night / You have to get your head on straight / I can't teach you this!!"* | **This is the slide on screen at the marker `RULES.md` cites for *"Wait for the M15 candle to close before taking the 5/13 EMA cross"* (`Q-011` §3).** The refutation is visible, not merely counted | PRINTED |
| 6 | `00-06-53_ravizza-seminar-announcement-text` | `06:53` | Full-page text: Dr. Ken Ravizza, mental coach, California Angels; seminar Tuesday April 3rd 7:00 pm eastern; a `gotomeeting.com/register` link | Dates the recording precisely and corroborates the 2012-04-01 session date | PRINTED |
| 7 | `00-07-08_only-valid-email-address-slide` | `07:08` | *"My only Valid e-mail address:"* **`steve@marketmakersforex.com`** | **Speaker-identification strand 1 in printed form**, and it **corrected this session's transcript note**: the ASR's `marketmakers4x.com` is the *mis*-rendering (*forex* → *4x*), not the good one. See the transcript's TRANSCRIPTION NOTE 3 | PRINTED |
| 8 | `00-07-57_student-email-sunday-monday-question` | `07:57` | A student email: *"Hello Steve … I remember you and some of the other mentioning not to trade on Sunday/Monday. Would it not make sense to trade against the false move week beginning until the H/Low is met?"* | **The `GOTCHA 4` content check** — this slide against `[00:08:25]`. Also the printed *"Hello Steve"*, speaker strand 3 | PRINTED |
| 9 | `00-09-33_student-email-adr-question` | `09:33` | Student email about ADR and weekly range | Source of the 600–1000 pip answer at `[00:14:09]` | PRINTED |
| 10 | `00-12-57_student-email-adr-correction` | `12:57` | Email: *"Thanks for … the ADR correction on Friday … three times ADR high low divided by two"* | The setup for `[00:13:18]`–`[00:13:52]`, tested as `PT-036` measure **M2** | PRINTED |
| 11 | `00-14-57_student-email-price-not-coming-back` | `14:57` | Email asking why price *"won't come back to a certain price point"* | Sets up the *"he ain't coming back"* explanation — and the marker where the ASR garbles it (`[00:15:12]`) | PRINTED |
| 12 | `00-17-22_r-and-d-review-homework-slide` | `17:22` | *"R&D- Review / Asked for 4Hr Markups / Flash Cards / Going forward DO NOT MAIL ME THE HOME WORK / Hold it for review in here on Sunday / Compile your work in a Binder / Post it in the forum …"* | The **prior** weeks' assignments, restated. Establishes the 4-hour markup as standing homework | PRINTED |
| 13 | `00-21-47_audusd-annotated-cycle-headline` | `21:47` | Annotated AUD/USD chart, red/blue shaded boxes, `R = 39.1 / 32.5 / 55.3 / 43.6 / 38.3 / 34.1 / 102.6 / 43.3` labels; headline *"How many of you watched this cycle unfold, like I drew up for you???"* | The week's worked example. **The `R =` labels are the platform's own measurement overlay** — pip distances, printed, not pixel-measured | ANNOTATED CHART |
| 14 | `00-23-03_candy-shop-dont-trade-until-stops` | `23:03` | Same chart, headline *"Welcome to the candy shop…don't trade until they hit the stops!!!!"* | **The lesson's central timing prohibition, in print.** Repeated verbally ≥7 times | ANNOTATED CHART |
| 15 | `00-25-37_audusd-four-hour-first-eight-hours` | `25:37` | Title bar `AUDUSD,H4 1.03762 1.03843 1.03656 1.03735`; white horizontal lines extended across the chart | The **first-eight-hours** markup on the 4-hour, i.e. the standing homework rendered. **OHLC is legible platform text** | CHART |
| 16 | `00-29-12_audusd-four-hour-with-tdi-panel` | `29:12` | Same `AUDUSD,H4`; a sub-panel labelled `TDI_M###…` with red / yellow / green lines | **TDI is DISPLAYED here and explicitly NOT taught** (`[01:13:03]` defers it to next week). Extends `A-039`'s *"displayed, not taught"* to V10 | CHART |
| 17 | `00-31-37_flash-cards-slide` | `31:37` | *"Flash Cards"* | Section marker | PRINTED |
| 18 | `00-34-22_flashcard-example-w-is-false-sell` | `34:22` | A flashcard: chart plus a text block — *"W is False / Dealer Vectors to S/H Zone / M formation / Shark fin above Resist band / Price action above blue tracer / Multisession M / Level 3 / SELL!!!!!!!!!!!!!"*; a terminal row beneath dated `2011.09.30 16:37`, axis labels `30 Sep 23:45 … 30 Sep 09:45` | **The single most information-dense frame in the lesson.** It shows what a completed flashcard is required to contain, and the **September 2011 date corroborates `[00:34:30]`** *"this is dated September see it"* | ANNOTATED CHART |
| 19 | `00-36-52_collection-of-flashcards-slide` | `36:52` | *"You should have a nice collection of these now / If you don't it is not too late!! / Complete them this week!!"* | Homework enforcement | PRINTED |
| 20 | `00-42-07_signature-trade-designation-slide` | `42:07` | *"I am officially designating everyone's signature trade as of today!! / You all are now safety trade traders / This doesn't have to be your only trade, I insist that you add it to your sets and scan for it everyday / You should become comfortable enough that you can anticipate its arrival 12 to 24 hrs out / Let's go over the rules"* | The lesson's thesis in print, and the **12–24 hour anticipation claim** | PRINTED |
| 21 | `00-43-17_safety-trade-rules-slide-one` | `43:17` | **`Safety Trade Rules`** / *"PFH /PFL has formed as HOW or LOW (4hr Tie in)"* / *"Price has moved away from the area and has confirmed the formation"* / *"Level one consolidation is clear"* / *"DNC- Remember this is level 1 consolidation a sucker trades the breakout back towards the peak ( Don't be a sucker)"* | **THE RULE SET, PRINTED. Preconditions 1–4.** Note `PFH`/`PFL` and `HOW`/`LOW` appear here **as printed abbreviations**, so they are not ASR artifacts | PRINTED — LOAD-BEARING |
| 22 | `00-46-17_safety-trade-rules-slide-two` | `46:17` | *"Dealer Makes A visible stop hunt (preferably above or below blue box)"* / *"Remember the "Straight-Away" develops here"* / *"Obvious ones are still valid sets"* / *"Dealer Issues Second Leg M or W this locks the trade"* / *"If the Level is hit a third time….God help the dealer!!"* | **THE RULE SET, PRINTED. Trigger conditions 5–7.** Together with #21 this is the complete stated setup | PRINTED — LOAD-BEARING |
| 23 | `01-01-22_audusd-15m-safety-trade-walkthrough` | `61:22` | `AUDUSD,M15`; shaded boxes with `R = 46.2 / 46.9 / 46.5 / 45.2 / 20.1` | Worked example of the rule set on the execution timeframe | ANNOTATED CHART |
| 24 | `01-07-52_audusd-15m-no-visible-stop-hunt` | `67:52` | `AUDUSD,M15`; `R = 34.1 / 57.6 / 102.6`; a hand-drawn white ellipse around one formation | The **counter-example** — `[01:01:38]` *"He does not make a visible stop hunt … because he doesn't exploit the Asian range"*. A NEGATIVE example in the lesson's own voice | ANNOTATED CHART |
| 25 | `01-10-42_usdcad-15m-peak-formation-walkthrough` | `70:42` | `USDCAD,M15 0.99536 …`; `R = 59.3 / 21.1 / 31.9` | Second instrument. Evidence the claim is not GBP-specific (`D-007` note) | ANNOTATED CHART |
| 26 | `01-15-57_stop-hunt-25-to-75-pips-slide` | `75:57` | *"Add a moving average or Pivot for strong confluence"* / *"The dealer can repeat the level, but it must hold"* / **"Look for the stop hunt to come in around 25 to 75 pips off of the LOW/HOW anchor."** | **THE FIGURE, IN PRINT — and it settles a SEVEN-instance ASR wobble** (**corrected 2026-08-13 from *"six-way"*** under open item 92, `V10_REVIEW_R1.md` `M2`; superseded text retained per `REMEDIATION_PROTOCOL.md` §2 — `[01:00:20]` was missing from the census). **Spoken renderings ranged over *25–75 / 20–75 / 50–75 / 25–50*, and `[01:00:20]` drops the lower bound entirely (*"75 pips"*), which strengthens rather than weakens the case for the printed form.** The printed form is **25 to 75**, and the reference point is the **LOW/HOW anchor**, not the blue tracer. See `A-078` | PRINTED — LOAD-BEARING |
| 27 | `01-20-27_gbpjpy-15m-double-bottom-anchor` | `80:27` | `GBPJPY,M15 131.209 131.318 131.199 131.277`; `R = 104.5 / 66.6 / 93.5 / 51.0 / 54.0` | The *"how do I know to take the W and not the M"* example (`[01:21:48]`). **Third instrument** | ANNOTATED CHART |
| 28 | `01-23-42_gbpusd-15m-with-adr-low-and-pivot` | `83:42` | `GBPUSD,M15 1.60083 1.60098 1.60083 1.60088`; labelled `ADR Low`, `Pivot`, `M1`; TDI sub-panel; `R = 48.2 / 25.9 / 82.0 / 58.6` | **The project's primary instrument (`D-007`) in the instructor's own hands**, with the ADR and Pivot overlays the lesson mentions at `[01:16:02]` | ANNOTATED CHART |
| 29 | `01-27-17_audusd-15m-with-tdi-visual-panel` | `87:17` | `AUDUSD,M15`; a sub-panel captioned **`Traders Dynamic Index Visual`**; platform tabs `EURUSD,M15 / AUDUSD,M15 / AUDUSD,M30 / GBPCHF,H1`; an order row dated `2012.03.23 15:16 … buy 50.00 audusd` | **Second frame showing TDI displayed but untaught.** The tab strip is descriptive evidence of the multi-pair, multi-timeframe workspace the lesson describes at `[01:33:29]` | CHART |
| 30 | `01-28-02_lessons-learned-thus-far-slide` | `88:02` | *"Lessons learned thus far / Weekly Cycle Identify the big picture / Psychological Support and Resistance is set by the dealer, therefore it is exploited by the dealer / How to visualize entry from flash cards / Putting it all together 4hr HOW/ LOW / First 8 hours of the week / Adding the "Safety trade" to your arsenal"* | **The lesson's own cumulative syllabus.** The best single statement of where the course believes the student is at V10 | PRINTED |
| 31 | `01-34-27_homework-mark-ten-safety-setups` | `94:27` | *"R&D / Finish flash cards you should build your book every week by adding a few snapshots / **Mark 10 Safety setups in any pairs / 5 long / 5 short** / Post in the forum for review. / I will try to organize the forum better going forward"* | **THE HOMEWORK, PRINTED.** Ten setups, five long, five short. See `05_HOMEWORK/V10/` | PRINTED — LOAD-BEARING |
| 32 | `01-36-16_end-card-easter-sunday-good-night` | `96:16` | Dimmed end card with the player's `replay` button over it: *"Looks like I **will** have a session for Easter Sunday… / So same time next week / Thank you all GOOD NIGHT"* | **The formal close — PRINTED AND NEVER SPOKEN.** It corrected this session's audio-only conclusion that the lesson ends without a sign-off. *"Easter Sunday"* 2012 = **2012-04-08**, which is V11's filename date — a dated forward reference, recorded as a prediction for the V11 session to test | PRINTED |

---

## WHAT THE VISUALS ADDED THAT THE AUDIO DID NOT

`SWF_CAPTURE_RECIPE.md` §9 keeps the transcript pass and the screenshot pass separate precisely so
this section can exist. **On V10 the screenshots changed three things, and two of them were
corrections to conclusions this session had already written down.**

1. **They settled the safety trade's distance figure.** The audio gives it **seven** times
   (**corrected 2026-08-13 from *"six times"*** — `V10_REVIEW_R1.md` `M2`, open item 92;
   `[01:00:20]` was missing from the census, and superseded text is retained here per
   `REMEDIATION_PROTOCOL.md` §2) and the ASR renders it several different ways.
   **The slide prints `25 to 75 pips off of the LOW/HOW anchor`** (#26). Without it, `A-078` would have had to stay wholly open on the number *and* on the
   reference point; with it, the number is settled and only the *reference point* conflict
   survives (the speaker repeatedly says *"off of the blue tracer"*, which is a different object —
   see `C-017`).
2. **They corrected the email-address note — the transcript had ranked its own confidence exactly
   backwards** (#7). Recorded in place in the transcript rather than fixed silently.
3. **They corrected the ending.** The audio stops without a sign-off, and this session wrote that
   down as a property of the lesson. **It is a property of the audio.** The deck closes formally,
   in text nobody says (#32) — the same shape as V01's *"pendings"*.

**And one thing they did NOT do, which is worth as much:** the position of every substantive rule
in `03_LESSON_NOTES/V10_SOURCE_NOTES.md` is **unchanged** by the screenshot pass. The safety trade
rule set survives on audio alone; slides #21, #22 and #26 **corroborate** it in print rather than
supplying it. A reviewer can strike every `PRINTED`-only row and the lesson's contribution stands.

---

## ESCALATION — A DEFECT IN `SWF_CAPTURE_RECIPE.md` §10, FOUND HERE

> **REGISTER POINTER, ADDED 2026-08-13 — this escalation is `REVIEW_INDEX.md` open item 87, and it
> is ✅ CLOSED.** It was allocated **82** on `video/v10` and **renumbered 86–90 → this item 87** by
> the V10 R1 reviewer at merge-back, because the integration branch had concurrently given 81–83
> to V09 R2 (`V10_REVIEW_R1.md` `M1`, open item 91; the RENUMBERING DISCLOSURE beneath
> `REVIEW_INDEX.md`'s open-items table carries the full old→new map). **The escalation was
> answered:** `SWF_CAPTURE_RECIPE.md` §10 was fixed on the integration branch under `D-038a` at
> V10 R1 — the header table is relabelled as *measured examples, not the library's constant*,
> V10's 2.0 row is added with its three-way duration cross-check, and the prose now reads
> *"patch `declared_rate × 10`"* with a rule to read `frameRate` from the file in hand.
>
> **Stated for accuracy, against the review:** `V10_REVIEW_R1.md` `M1` records that this file
> *"cites open item 82"*. **It did not** — this section referred to the escalation by description
> and carried no item number at all, which is why the renumbering could not have orphaned it. The
> pointer above is therefore an **addition**, not a correction, and nothing here is superseded.

**§10 states the frame-rate patch as `3.0 → 30.0 fps`,** carried over from V01 and V02 which both
declare 3.0. **V10 declares 2.0.** The recipe's §10 prose (*"Patch 3.0 → **30.0** fps"*) and its
worked example (`v02_x10.swf`) both read as if 3.0 were the library's rate. Applied literally to
V10 it yields a **15× sweep**, not 10× — which does not fail loudly. It produces a complete,
well-formed, correctly-timecoded set of frames at **7.5-presentation-second spacing instead of 5**,
under-sampling the screen-state detector by a third.

**This is the same failure family as `GOTCHA 4` and `GOTCHA 5`:** a header field that varies across
the library, quoted in the recipe as a constant, with no loud failure when it is wrong.
**The fix is one line — read `frameRate` from the header and compute the patch as `rate × 10`** —
and `GOTCHA 5`'s stage-size probe already parses the header immediately before the field, so the
code is present and needs only extending.

**`SWF_CAPTURE_RECIPE.md` is a POLICY ledger under `D-038a` and MUST NOT be edited from this task
branch.** V09's session hit `GOTCHA 5` and correctly declined to fix it here; the same discipline
applies. **Escalated, not patched.** This session avoided the trap by reading the header first, as
`GOTCHA 5` instructs — the general lesson generalising once more.
