# V18 — TRANSCRIPT

## ⭐ TIMESTAMP CONVENTION — STATED ONCE, AT THE TOP (`V14_REVIEW_R1.md` GATE, open item 173)

**Every `[HH:MM:SS]` in this file and in every V18 artifact is the committed marker grid of THIS
file — the 881 markers below — and nothing else.** An independent ASR pass was run this session
(VERIFICATION §5) and **its clock is never cited**; where it arbitrates a word, the correction is
attached to the *marker grid's* timestamp, not to the second pass's.

⚠️ **AND HERE THE TWO CLOCKS DO *NOT* COINCIDE EXACTLY — V18 IS THE FIRST LESSON IN THE CORPUS
WHERE THEY DRIFT.** V16 and V17 both measured a sweep offset of **flat zero**, so their screenshot
filenames and marker timestamps were directly comparable with no conversion. **V18's sweep offset
runs `0 → −1 → −2 → −3 s` monotonically across the file** (`04_SCREENSHOTS/V18/INDEX.md` §0). The
consequence is handled the way `SWF_CAPTURE_RECIPE.md` §8a step 4 requires and not by a fudge
factor: **every screenshot is named from its OWN burned-in player timecode**, read from its own
pixels. A screenshot name is therefore a *player-clock* fact and a marker is a *transcript-clock*
fact, and the two agree to within **≤3 s** rather than exactly. **Nothing in this artifact set
depends on a sub-3-second alignment**, and where a frame is used to corroborate a spoken line the
tolerance is stated at the point of use.

Corroboration at five content points where the screen changes on a sentence. **Quotations are
verbatim from the marker grid, ASR defects included:**

| Marker | Transcript line, VERBATIM | Screen, burned player timecode | Δ |
|---|---|---|---|
| `[00:03:28]` | *"All right, next slide if I can find the mouse."* → `[00:03:35]` *"Okay."* | the `TREND LONGER TERM` bullet slide is up at **03:34** | +6 s / −1 s |
| `[00:06:29]` | *"So intraday breaking this stuff down intraday."* | `TREND INTRA DAY` slide at **06:29** | **0 s** |
| `[00:11:34]` | *"Mark your maker trend."* → `[00:11:37]` *"An uptrend can be labeled as such."* | `Market Maker Up Trend Can Be Labeled As Such` slide at **11:29** | −5 s |
| `[00:19:31]` | *"The opposite is true of a downtrend."* | `Market Maker Down Trend Can Be Labeled as Such` slide at **19:34** | +3 s |
| `[00:45:01]` | *"Next week, we're going to talk about trap candle patterns."* | `Trap Candle Patterns` title slide at **44:52** | −9 s |

Screen-change granularity is the 5-second sweep grid, so ±5 s is the measurement floor; the sweep
drift adds up to a further 3 s. **The `−9 s` on the last row is the slide sitting up while he
finishes the previous thought, not drift** — the frame at `44:52` is the first sweep sample on
which that slide appears, and the two rows either side of it are `0 s` and `+3 s`.

---

## SOURCE

| Field | Value |
|---|---|
| Video ID | **V18** |
| Original filename | `Bootcamp1 Wk8 051312 Part2 (46mins).swf` |
| SHA-256 | `cfa425ab059573a17276d3ed7ce187b039309b49a6ab99e47291641d0b1f7181` — verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session on the flat `Bootcamp/` canonical path, **and re-verified after the frame-rate patch** to prove the original was not modified (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| Byte length | **17,852,174** — matches `SOURCE_MANIFEST.md` exactly |
| Duration | 00:46:08 (audio measured **2768.953469 s**; SWF header **8,308 frames ÷ 3.0 fps = 2769.333 s**; `SOURCE_MANIFEST.md` 00:46:08 = 2768 s — **three independent figures agreeing to within 1.33 s**) |
| Lesson title | ⚠ **NOT PRINTED AS A SINGLE TOPIC TITLE.** The deck carries **two** printed section titles in sequence: **`TREND`** from the start of the file to `≈35:00`, then **`MARKET MAKER TRAP MOVES`** / **`MARKET MAKER TRAP MOVE`** from `35:53` to the end. The final slide prints **`Trap Candle Patterns`** as *next week's* subject, not this one's. The spoken framing is `[00:00:00]` *"Back to the cycle"* — V18 opens mid-thought as Part 2 of the same night's recording. The quarantined per-lesson header's *"Primary Topics: Steve Mauro Beat The Market Maker (BTMM) Methodology"* is a generic non-answer, and its `RULES.md` / `NOTES.md` / `VISUAL_INDEX.md` are fabricated — see `QUARANTINE_REGISTER.md` **Q-019** |
| Session date | **2012-05-13**, from the filename and `SOURCE_MANIFEST.md`. ⚠ **NOT corroborated from inside this file** — V18 states no date, no week number and no session number (see VERIFICATION §4). Its dating rests on the filename and on being **Part 2 of V17's recording**; V17 *does* corroborate 2012-05-13 internally (`[00:00:11]` *"Today's the 13th"*, plus the printed schedule slide), and V18 is the same night's second half |
| Continuity with V17 | ⭐ **DIRECT AND EXPLICIT.** V17 is Part 1 and V18 is Part 2 of the **same recording session**. V18's first line is `[00:00:00]` *"Back to the cycle"* — a resumption, with no greeting, no housekeeping and no re-introduction. V17's own transcript records the relationship (*"It is Part 1 of two (V18 is Part 2 of the same night)"*) |
| Frame rate | **3.0 fps** in the SWF header — read from **this file's own header**, not assumed (`SWF_CAPTURE_RECIPE.md` §10 as corrected by V10 R1 open item 87). The 10× sweep patch is therefore **3.0 → 30.0** here, and the patched copy was re-read to confirm `30.0` exactly |
| Stage size | **1024 × 786** — the majority class. `GOTCHA 5`'s table gives `(512, 300)`, and the pre-click / post-click guard **confirmed it fired** rather than assuming it (`sweep.log`: *"play click confirmed: stage changed"*) |
| Transcribed by | ASR, by a pre-ingestion session. Copied **byte-for-byte** and verified 2026-08-14 — see VERIFICATION below. The pre-ingestion file's own `# VIDEO` header block is **NOT carried over**: its *"Course Position: Video 19 of 21"* is wrong under `D-017` §2's renumbering (this file is **V18**), and its *"Primary Topics"* line names the methodology rather than the lesson |
| Transcription confidence | **MEDIUM–HIGH.** 881 markers, strictly monotonic, **zero** backwards steps, **one** equal-adjacent pair, gaps 0–13 s (mean 3.15 s), last marker `[00:46:08]` sitting **1.0 s** before the measured end of audio, and a speech rate of **149.1 wpm** across 6,879 words. It preserves its own mishearings — *"mayonnaise"*, *"the manays"*, *"Charmin friends"*, *"blueberry"*, *"shark fin and blood in the water"*, *"three advised"*, *"switch physicians"*, *"I'm on when blank"*, *"the loin"*, *"W-R-O tracks"*, *"Brice is rising"*, *"a mall, son"*, *"to a 30"*, *"they were from sick"*. **A fabricated transcript does not invent its own mishearings.** ⚠⚠ **BUT ONE OF ITS DEFECTS INVERTS A RULE'S MEANING** — see VERIFICATION §5 correction **#1**, which is the most important line in this file |

---

## SPEAKER TABLE — MANDATORY UNDER `D-025` consequence 3, re-adopted by `D-033`

| Speaker | Runtime | Basis |
|---|---|---|
| **Course author (Steve Mauro)** | **100%** — `[00:00:00]`–`[00:46:08]`, the whole file | Five non-acoustic strands, below. **CERTAIN** |
| Guest presenter | **0%** | No second voice is introduced, addressed, thanked or handed to anywhere in the file. Students are named in the **third person** or addressed directly by the instructor (*"Scott, everything is recorded, buddy"*), never handed the floor |

**Tested on strands fixed before the answer was known, not inherited from V17.** The acoustic
cross-file screen was **NOT** run, per V07's prohibition.

### THE FIVE STRANDS — non-acoustic, `D-025`/`D-033` method

| # | Strand | Evidence, VERBATIM |
|---|---|---|
| **1** | ⭐ **Students address him by name and he answers in the same voice, with no attribution break** | `[00:13:08]` *"I know some of you go, O Steve, it was a good setup. \| I agree."*; `[00:15:21]` *"I know as soon as I say it, you'd be like Steve. \| There was like 35 trades that went back in his enough room. \| I know."*; `[00:07:30]` *"Missed you sent me a trade and you go, Steve, I took the vector to the high."* |
| **2** | ⭐ **He owns the course's schedule and syllabus in the first person** | `[00:41:28]` *"let me finish up to a section and then I'll move the other section I wrote for you guys to next week"*; `[00:41:35]` *"if I don't complete the material, **I'm going to add another week to the boot camp**"*; `[00:45:01]` *"Next week, **we're going to talk about** trap candle patterns"* |
| **3** | ⭐ **He owns the strategy being released at the end of the course, and names his testers** | `[00:44:38]` *"they are my guinea pigs. \| They are testing **the strategy that I will release on the last day of boot camp**"* |
| **4** | **He sets homework in the first person** | `[00:45:31]` *"I really don't have any homework for you this week except the last seven and a half weeks of homework **that I've been giving you**"* |
| **5** | **He speaks from a personal trading history the students do not share** | `[00:15:51]` *"We had this discussion, I don't know, two years ago in **the trading room that we used to run**. \| Me, Carr, Scott, Ray"* |

**No strand depends on voice timbre.** Strand 1 is the strongest: three separate students address
*Steve* and the reply follows inside the same marker with no speaker change.

---

## VERIFICATION — RUN 2026-08-14, THIS SESSION

### §1 — THE BODY IS BYTE-FOR-BYTE THE PRE-INGESTION FILE

Everything from `# VERBATIM TRANSCRIPT` onward is a **byte-for-byte copy**. The claim is
mechanical, not editorial: the body was sliced from the source file at that marker and written
without modification, then re-read and checked by containment and tail-match.

| Object | Bytes | SHA-256 |
|---|---|---|
| Pre-ingestion `TRANSCRIPT.md`, whole file | 46,768 | `6e3f73e80feb1eb822eb697ec847a6f8fc4ff3a03b2441638588b13b577644a1` |
| **Body carried over** (`# VERBATIM TRANSCRIPT` → EOF) | 46,572 | `1972a181197f86dfa9d646a4b5d33950ee27242903e25cf2b83789565ea7f4a7` |
| Header block **dropped** | 196 | *(the `# VIDEO` block — wrong course position, generic topics)* |

*(The two SHA-256 values above are recomputed and printed by `build_transcript.py` at build time;
the reviewer should re-run the slice rather than trust the table.)*

### §2 — THE MARKER GRID

| Property | Value |
|---|---|
| Markers | **881** |
| Monotonic | **YES** — zero backwards steps |
| Equal-adjacent pairs | **1** — `[00:39:07]` appears **twice**, carrying *"Okay."* and then *"When the volume is not met by the dealer, the market makers trying to obtain a certain amount"*. It is a **genuine second-boundary collision** (a one-word utterance and the start of the next sentence inside the same second), not a duplicated line |
| Gaps | min **0 s**, max **13 s**, mean **3.15 s** |
| Gap histogram | `0:1, 1:199, 2:215, 3:162, 4:114, 5:79, 6:42, 7:36, 8:12, 9:9, 10:6, 11:1, 12:2, 13:2` |
| First / last marker | `[00:00:00]` / `[00:46:08]` |
| Last marker vs measured end of audio | **1.0 s** before (2768 s vs 2768.953 s) |
| Words | **6,879** |
| Speech rate | **149.1 wpm** |

**Why this is evidence rather than decoration.** A grid fabricated to fit a stated duration tends
to be too regular or to stop short. This one has a **long tail** (single instances at 11 s, two at
12 s, two at 13 s), a **13-second maximum** landing on genuine silences where he is drawing, and a
**last marker 1.0 s before the end of the audio measured independently by `ffprobe`**. It also
carries **one duplicate timestamp**, which a generator has no reason to produce.

### §3 — IT PRESERVES ITS OWN MISHEARINGS

Fourteen domain/proper-noun failures are listed in the SOURCE table above. Three are worth calling
out because they are *recoverable* and were recovered from the screen or the second engine:

* *"the loin"* → **`LOY`** (Low Of Year), **printed on the slide** at `32:03`. He even self-corrects
  aloud: `[00:32:16]` *"What's the loin? Lower the year."*
* *"W-R-O tracks"* → **`W RR tracks`** (*railroad tracks*), **printed on the same slide**.
* *"switch physicians"* → **"switch positions"**, arbitrated by the second engine.

### §4 — ⚠ WHAT THIS FILE DOES **NOT** CONTAIN, AND ABSENCE IS EVIDENCE

**V18 carries no internal date, no week number and no session number.** Checked by `grep`:

* `week` — appears as *"for the week"*, *"9 weeks"*, *"2 1/2 weeks of chop"*, *"next week"*, *"last
  week"*, *"the last seven and a half weeks of homework"*. **None is a session label.**
* No *"welcome to week N"* line of the kind V17 carries at `[00:02:36]`.
* No date is spoken anywhere.

**This matters for the forward-read precedent (items 179, 192, 217).** Item 217 recorded that V16
also carries no internal week number, and offered that as a data point. **V18 is a second instance,
and a stronger one**: V17 — the *same night's first half* — states its week number twice and has it
printed on a schedule slide, while V18, recorded minutes later, states nothing. **A lesson's
silence on its own date is therefore not evidence about the calendar; it is a property of which
half of the night you are in.** Offered for item 179's ruling, not as an argument for either side.

### §5 — INDEPENDENT ASR PASS, AND THE CORRECTIONS IT FORCES

A **second engine** — `faster-whisper` / CTranslate2 **`large-v3`**, independent of the
pre-ingestion transcript — was run over **eight segments** chosen *before* the results were seen,
on the lines this lesson's rules actually rest on. **Its clock is never cited below**; corrections
are attached to the marker grid's own timestamps.

#### ⚠⚠ CORRECTION #1 — `[00:19:40]` — THE COMMITTED TRANSCRIPT STATES THE OPPOSITE OF THE LESSON

| Source | Text |
|---|---|
| **Committed transcript, `[00:19:40]`** | *"**Counter trends are advised.**"* |
| **Second ASR engine** | *"**countertrend is ill-advised**, going back towards the peak"* |
| ⭐ **THE PRINTED SLIDE** (`V18_00-11-29_…png`, `V18_00-19-34_…png`) | **`Counter Trend Is Ill Advised On V1`** and **`Counter Trend Is Ill Advised on A1`** |

**The committed line drops the word `ill` and inverts a rule.** It is refuted by **two independent
sources** — a second ASR engine and the deck itself, where the sentence is printed twice, on two
different slides, in two directional variants.

**It is also refuted by the three markers immediately after it**, which the committed file itself
carries: `[00:19:41]` *"Going back towards the peak."* `[00:19:42]` *"Don't trade back towards the
peak."* `[00:19:44]` *"If you're struggling with the business, the last thing I want you to do is
trade back towards the peak."*

⚠️ **CONSEQUENCE, STATED PLAINLY: `[00:19:40]` AS COMMITTED MUST NOT BE QUOTED AS A RULE.** The
rule is **`Counter Trend Is Ill Advised`**. This correction is load-bearing for `V18_SOURCE_NOTES.md`
§7 and for the `A1` / `V1` labels, and it is the single most important line in this file. The
defective line is **retained verbatim in the body** (the body is byte-for-byte and is not edited);
it is corrected **here**, and every V18 artifact cites the correction rather than the raw line.

#### CORRECTION #2 — `[00:09:19]` — `"the reversal double to pop and fall"` → **`"the reversal double top and fall"`**

Second engine: *"or this will be the reversal **double top** and fall"*. *"to pop"* is a mishearing
of *"top"*. Minor, but it is the name of a formation.

#### CORRECTION #3 — `[00:09:37]` — `"They switch physicians all the time."` → **`"they switch positions all the time"`**

Second engine, verbatim. The committed word makes the sentence meaningless; the corrected one
completes the *corrector / correctee* point in the preceding marker.

#### CORRECTION #4 — `[00:01:14]` — `"Jim Nichols"` → **`"Jim Nicholson('s)"`**

Second engine. A named student, not load-bearing, recorded for completeness.

#### CORRECTION #5 — `[00:01:09]` — `"You got them in."` → **`"You got him, man."`**

Second engine. *"Him"* = the dealer, which is the lesson's consistent referent.

#### ✅ CONFIRMED VERBATIM BY THE SECOND ENGINE — the numbers the rules rest on

Every one of these was read back **identically** by the independent engine:

| Marker | Line | Status |
|---|---|---|
| `[00:01:03]` | *"25 to 75 off of yesterday's low?"* | ✅ **verbatim** |
| `[00:08:19]` | *"The trend is slow and steady last six to eight hours."* | ✅ verbatim (*"lasts 6 to 8 hours"*), **and printed on the slide at `06:29`** |
| `[00:08:30]`, `[00:08:43]`, `[00:08:51]`, `[00:09:22]` | *"two sessions of rise or fall with the third session being corrective in nature"* | ✅ **verbatim, all four repetitions** |
| `[00:13:26]`–`[00:13:39]` | *"the 75 pips difference between the anchor point and the level one consolidation"* | ✅ verbatim (*"75 pip difference"*) |
| `[00:41:50]` | *"Two hours."* | ✅ verbatim, **and printed twice** — `( 2HR Time Cap)` at `35:53`, `Minimum 2 Hrs` at `41:28` |
| `[00:42:01]` | *"If he vectors in two or three bars, that's 45 minutes, right?"* | ✅ verbatim |
| `[00:42:14]` | *"30 to 90 minutes."* | ✅ verbatim |
| `[00:04:26]` | *"Trade the pairs at the beginning of the sessions or the end of the sessions when the dealer becomes active above or below the Asian range."* | ✅ **verbatim** |
| `[00:31:02]` | *"So 16, 64 candles, thank you, man."* | ✅ **verbatim — the on-air arithmetic slip is REAL, not an ASR artifact** (see `C-028`) |

#### ⚠ ONE READING THE SECOND ENGINE DOES **NOT** RESOLVE

`[00:42:35]` *"wait for a new move after 9.45"*. The second engine gives *"after 945"* — **the same
digits, no decimal, no colon, no am/pm and no time zone.** Both engines agree on `9`, `4`, `5` and
neither supplies a clock convention. **`9:45` is an INFERENCE, not a transcribed fact**, and it is
carried as one everywhere in this artifact set. See `A-127`.

---
# VERBATIM TRANSCRIPT

[00:00:00]
Back to the cycle.

[00:00:03]
All right, false move weak beginning.

[00:00:06]
The anchor point comes in.

[00:00:09]
Okay, false move.

[00:00:10]
The dealer opens the first aid hour.

[00:00:12]
He trades in the rain.

[00:00:14]
False move weak beginning.

[00:00:16]
He anchors out what a W.

[00:00:22]
Okay?

[00:00:24]
Maybe he makes three pushes.

[00:00:25]
Maybe he doesn't.

[00:00:26]
But he makes level one rise.

[00:00:28]
Day one, level one.

[00:00:29]
He goes into consolidation.

[00:00:31]
He gives you a stop hunt low.

[00:00:33]
There's only two moves out of here.

[00:00:35]
Straightaway rise or a visible stop hunt.

[00:00:41]
Right?

[00:00:42]
The straightaway is hard to grab.

[00:00:44]
They'll usually hit the average.

[00:00:46]
Not make a visible stop hunt below the Asian range.

[00:00:50]
That's the straight rise.

[00:00:51]
That's a hard trade to catch for a lot of people.

[00:00:53]
It takes a little more skill and patience to see it.

[00:00:56]
But if he gives you a stop hunt low rise of V or a W,

[00:01:01]
how many pips off the low?

[00:01:03]
25 to 75 off of yesterday's low?

[00:01:06]
This is the peak formation.

[00:01:09]
You got them in.

[00:01:10]
That's a safe trade.

[00:01:11]
That's why it's called a safety trade.

[00:01:13]
You got them.

[00:01:14]
Now I'm sure if Jim Nichols is in here,

[00:01:16]
he'll argue with you that the pullback is some Fibonacci

[00:01:19]
retracement bullshit number that gives you a lot of

[00:01:24]
good entry.

[00:01:25]
And I'm sure it is.

[00:01:28]
But what I'm telling you is the principle of what's going on here.

[00:01:33]
Yes, the 618 baby.

[00:01:35]
What I'm telling you is going on here is the dealer has made the

[00:01:38]
trap move in here.

[00:01:39]
He comes back to induce more traders to take shorts,

[00:01:44]
but to not release the money with his hand.

[00:01:47]
Okay, remember?

[00:01:48]
Money grab.

[00:01:50]
This is an easy trade to spot.

[00:01:52]
Please, please, please.

[00:01:53]
Please, please, it's your new signature trade.

[00:01:55]
I told you this eight weeks ago,

[00:01:57]
but I'm telling you again.

[00:01:59]
Okay?

[00:02:00]
And there you have it.

[00:02:04]
Okay, so false move week beginning.

[00:02:08]
There's your safety trade right there.

[00:02:14]
Man, any happen to use the mayonnaise for your enjoyment?

[00:02:19]
Okay?

[00:02:20]
Keep formation low, safety.

[00:02:21]
And he actually did a W, but it's weird.

[00:02:23]
He did more of a straightaway last day of the cycle.

[00:02:26]
And what does he do?

[00:02:28]
He head and shoulders you up to the high, flipping you off.

[00:02:33]
Laughing at you.

[00:02:35]
All right?

[00:02:38]
Sunday, Monday, Tuesday, Wednesday.

[00:02:47]
Okay, variations on the theme.

[00:02:49]
If he could stretch this out, he could chop for a whole day, work the crosses,

[00:02:53]
and stretch this out Thursday, and then make a correction for two days.

[00:02:57]
Thursday, Friday.

[00:02:58]
Okay?

[00:02:59]
Understand his variations on the theme.

[00:03:02]
Your job is to find the PFL and the PPH and tradeaway.

[00:03:08]
Remember, sunny?

[00:03:11]
She identified peak formation low, trades away for two days.

[00:03:14]
Peak formation high, trades away for two days.

[00:03:17]
You use the four-hour chart for this if you have to.

[00:03:20]
That's okay.

[00:03:23]
All right?

[00:03:24]
You guys are making a two-heart, man.

[00:03:25]
It's simple.

[00:03:28]
All right, next slide if I can find the mouse.

[00:03:33]
Oh, all right, here we go.

[00:03:35]
Okay.

[00:03:37]
Identify where you are in the count.

[00:03:39]
We're helping for Jack the Next move.

[00:03:41]
So here's what I want you to do to make it easier for yourself.

[00:03:44]
I said it and say it one more time.

[00:03:46]
I want you to look for safety setups after the peak is formed.

[00:03:49]
But once they're having a success, they're more advanced and no worries, man.

[00:03:54]
Okay?

[00:03:57]
If you're having a success, seeing the peaks are getting great.

[00:04:00]
But what I'm telling you is if you're struggling still can't see it,

[00:04:03]
I want you to look for the safetys after the peak formation higher low has been formed.

[00:04:08]
The safety trades are easy to spot because they're a lot conformation that the peak formation is in place.

[00:04:15]
Is the peak formation in place?

[00:04:16]
I can't tell you to come in at a level one, the dealer locks it in.

[00:04:20]
If he comes back to the peak and hits it again and turns there, you got him.

[00:04:26]
Trade the pairs at the beginning of the sessions or the end of the sessions when the dealer becomes active above or below the Asian range.

[00:04:34]
Simple.

[00:04:36]
I didn't make those timings up.

[00:04:38]
That's when they become active.

[00:04:41]
Most of the time, the activity will start just inside the shadow at the start of the one in session.

[00:04:46]
They'll start extending the lower, extending the high.

[00:04:49]
That's when you're looking for setups, okay?

[00:04:52]
You've got to always try to identify the peak formation.

[00:04:56]
I don't care what chart you're looking at if you use a four-hour one-hour, I don't care.

[00:05:00]
You need to know where the peaks are to help you get a directional bias for the rest of the week or for the next couple of days.

[00:05:07]
Okay?

[00:05:08]
I mentioned this before and I'll say it one more time.

[00:05:10]
If a double peak formation appears on a higher timeframe, it's lights out, man.

[00:05:15]
And I have a snapshot of that, but it happens all the time.

[00:05:19]
You just got to keep your eye out for it.

[00:05:21]
This is the pound dollar.

[00:05:26]
Okay?

[00:05:33]
You got to see that?

[00:05:34]
No one to answer your question.

[00:05:36]
If you see it on the four hours of two-late.

[00:05:38]
No, here.

[00:05:39]
If you see it on the higher timeframe, right?

[00:05:42]
Look, the dealer made three hits.

[00:05:44]
Three hits to the high.

[00:05:46]
Okay?

[00:05:48]
Come down on the lower timeframe.

[00:05:49]
Here's the highest point on the chart.

[00:05:51]
The dealer gives you the M formation in the U.S. session and he gives you

[00:05:56]
starts to roll over in the Asian session.

[00:05:58]
You expect him to come back here, but if you got the outside structure trap high,

[00:06:03]
on all time compressions, this is the outside structure to the high.

[00:06:07]
I'll talk about that in a few minutes.

[00:06:09]
He's trading inside the structure.

[00:06:11]
Just take him short, man.

[00:06:12]
Stop law school's right there.

[00:06:14]
It's safe.

[00:06:17]
I think Audi had it.

[00:06:21]
Yeah, Terry.

[00:06:22]
I'll strally did have it.

[00:06:25]
Okay.

[00:06:27]
All right.

[00:06:29]
So intraday breaking this stuff down intraday.

[00:06:31]
You have a rough idea where the peaks are, what you expect.

[00:06:36]
So intraday, you have the anticipated move in your head, lines up with the peak formation.

[00:06:44]
It comes after the stop-hounds.

[00:06:46]
Listen.

[00:06:47]
I don't know what happened there.

[00:06:49]
I'm doing that weird shit again.

[00:06:51]
Okay.

[00:06:52]
That's not a trade.

[00:06:54]
All right.

[00:06:55]
Some of you will argue with me, but that is not a trade.

[00:06:59]
That is nothing.

[00:07:01]
That's not a trade either.

[00:07:04]
All right.

[00:07:05]
That is nothing.

[00:07:07]
This does not become a trade until the dealer trades off of their,

[00:07:12]
off of that number for about an hour.

[00:07:17]
Okay.

[00:07:22]
A vector out of the Asian range high or low is not a trade.

[00:07:28]
Let's keep that in mind.

[00:07:30]
Missed you sent me a trade and you go, Steve, I took the vector to the high.

[00:07:34]
Why didn't it work out?

[00:07:36]
The dealer pulls back and hits it again because there's nothing there.

[00:07:39]
You don't, that's not a trade.

[00:07:44]
Okay.

[00:07:47]
The trend intraday starts after the stop-hounds and the high or low has been worked.

[00:07:55]
Remember, he has to work to make this, there's work involved.

[00:07:58]
To make this, there's work involved.

[00:08:01]
This takes time.

[00:08:03]
These take time to work those and form them up.

[00:08:06]
So a straight rise or straight drop is not a setup.

[00:08:10]
It is a vector for the beginning of the setup or for leg one of the setup.

[00:08:16]
Okay.

[00:08:19]
The trend is slow and steady last six to eight hours.

[00:08:22]
It lasts the session.

[00:08:23]
It could go both sessions and last 12 hours or so into the next, into the next U.S. session mid session.

[00:08:30]
But most of the time you'll get two sessions of rise or fall and the third session will be corrective in nature.

[00:08:40]
All right.

[00:08:41]
Write that down.

[00:08:43]
Two sessions of rise or fall with the third session being corrective in nature.

[00:08:48]
When I say corrective, I don't mean it's going to sell off.

[00:08:50]
I mean it corrects back.

[00:08:51]
So if you have two up, session one, session two, third session is corrective in nature.

[00:08:58]
Okay.

[00:08:59]
Session one, session two, third session is corrective in nature.

[00:09:03]
Even though that's a rise, that's not a market correction.

[00:09:06]
I'm just saying corrective in nature meaning it goes against the trend and then what happens?

[00:09:12]
The trend will resume or the right, the trend will resume or this will be the reversal double.

[00:09:19]
To be the reversal double to pop and fall.

[00:09:22]
Two sessions of rise or fall with the third session being corrective in nature.

[00:09:27]
Now I can't say the U.S. sessions always corrective in nature.

[00:09:30]
I cannot say that because the dealers change the session and who gets to be the corrector and who gets to be the correctee.

[00:09:37]
They switch physicians all the time.

[00:09:40]
Okay.

[00:09:44]
So right now it could be London corrects, U.S. corrects and ages corrective in nature.

[00:09:51]
It goes against those moves and then the trend will resume on the fourth session.

[00:09:57]
You understand?

[00:09:59]
Two sessions of rise or fall, third session corrective in nature, fourth session should resume the trend that was underway by the dealer.

[00:10:12]
Okay.

[00:10:16]
Listen, this is a retail traders trap trying to line up all the time frames.

[00:10:21]
What you're trying to do with the higher time compressions, I want to make sure I understand that I didn't give you the impression that you're trying to line up the four-hour rollover with the daily, the weekly, that's BS, that's for retail traders.

[00:10:33]
You're looking for peak formation high and it hit the stops in line with the peak to validate the retail traders the wrong way and then a correction.

[00:10:45]
Stop hunt rise if the peak formation is to the high side, stop hunt rise drop.

[00:10:51]
Right?

[00:10:53]
Retail traders trap to wait for the time frames to line up. It's garbage, don't do it.

[00:10:59]
And I want you, I can't say enough, I want you to have an open mind when looking at the charts.

[00:11:04]
Okay. Flying saucer pitchers, those dot things that try me crazy, I can't see them.

[00:11:10]
Then I talked about in sales presentation.

[00:11:13]
Open your mind to see the flying saucer and the dinosaurs and the things that are on there.

[00:11:20]
Stereo grams.

[00:11:21]
Try to open your mind and see the chart more objectively.

[00:11:24]
The dealer is trading both ways.

[00:11:28]
Why can't you?

[00:11:32]
Okay.

[00:11:34]
Mark your maker trend.

[00:11:37]
An uptrend can be labeled as such.

[00:11:41]
W-ank for point, right? Let me get my pen over here.

[00:11:44]
False move weak beginning comes into the anchor.

[00:11:48]
The L-O-W is formed the lower the weak, right?

[00:11:53]
V-1, V-2, reversal.

[00:11:57]
M-R. Right?

[00:12:02]
It's kind of funny that this is where the safety trade develops.

[00:12:13]
And I tell you do not counter that.

[00:12:20]
Okay.

[00:12:22]
So what I'm telling you is that if he gives you a secondary W, terrible drawing.

[00:12:30]
25, 75 pips off of the first W, the first W is low.

[00:12:39]
That's your safety trade.

[00:12:41]
Okay.

[00:12:42]
Sometimes look, these guys are crazy, man. They do this. They do this.

[00:12:45]
They do this. And then they do that.

[00:12:48]
And they just give you W's all the way up.

[00:12:51]
You'll go back and see it's crazy.

[00:12:53]
Sometimes the anchor point itself is a V, then the next time they give you a W coming out of here, safety.

[00:13:00]
Just understand the variations.

[00:13:03]
I do not want you to counter trend back here.

[00:13:06]
It's a sucker's play, man.

[00:13:08]
I know some of you go, O Steve, it was a good setup.

[00:13:11]
I agree.

[00:13:13]
If you're going to take these, here's how you figure it out.

[00:13:16]
Very important.

[00:13:18]
Because you don't listen anyway.

[00:13:20]
I know you're going to take them.

[00:13:21]
So I just had to tell you.

[00:13:23]
Here's how you figure it out.

[00:13:26]
The ones that pay out more often are the ones that have the 75 pips difference between the anchor point

[00:13:36]
and the level one consolidation.

[00:13:39]
Or greater, or greater, 75 plus.

[00:13:42]
Why?

[00:13:43]
Because if the A, let's say you're in here, the Asian range is 50.

[00:13:48]
What's 75 plus 50?

[00:13:49]
You buck in a quarter, right?

[00:13:51]
Okay.

[00:13:52]
There's 125 pips available from here, from here to here.

[00:13:57]
So if the dealer breaks high, or does it, is that one example?

[00:14:01]
Didn't break above the Asian range?

[00:14:05]
The Asian range was 34 pips plus 75.

[00:14:09]
You're still looking at 100.

[00:14:12]
I don't know.

[00:14:13]
Nine pips.

[00:14:14]
I think I got it right.

[00:14:15]
I don't know.

[00:14:16]
I hate math in front of everybody.

[00:14:18]
109 pips back towards the low, so you have a shot.

[00:14:21]
If he stalls in here, have enough presence of mind that the safety trade is setting up in your face

[00:14:30]
and to take whatever's available off the table before he spikes like he did on that trade

[00:14:36]
and takes you out for a loss.

[00:14:39]
This is this right here.

[00:14:47]
I can only say ill-advised.

[00:14:48]
It looks like it's three advised.

[00:14:50]
It's ill-advised.

[00:14:51]
I'd say all I can say about it.

[00:14:53]
Don't take the counter back on V1 because it messes up.

[00:15:01]
What you're looking for out of the W anchor is the safety trade.

[00:15:05]
That's what you're looking for.

[00:15:07]
The only way to take it is there's enough space between the peak formation low

[00:15:11]
and where they went into consolidation.

[00:15:13]
There's enough meat in here to carve some out for yourself.

[00:15:17]
You can do it, but I'm still sticking with this.

[00:15:20]
It's ill-advised.

[00:15:21]
I know as soon as I say it, you'd be like Steve.

[00:15:23]
There was like 35 trades that went back in his enough room.

[00:15:26]
I know.

[00:15:27]
But as a general rule as a whole, he doesn't offer enough because what you're doing

[00:15:32]
essentially is you're trading the stop hunt and trading the stop hunt is a sucker's trade.

[00:15:39]
Especially if he tightens up the ADRs.

[00:15:43]
If the ADRs are tightened up for the summer and they're smaller, then you're not going to get his deep a stop hunt,

[00:15:48]
you're going to get yourself jammed.

[00:15:51]
We had this discussion, I don't know, two years ago in the trading room that we used to run.

[00:15:56]
Me, Carr, Scott, Ray, I think we're else was in there.

[00:16:03]
I'm about trying to take the break, since you know the deal is going to make the stop hunt break.

[00:16:07]
Trying to take that back.

[00:16:09]
I was talking not to take it.

[00:16:11]
I know there's some good trades, but as a general rule, they don't pay out as well as

[00:16:21]
long near the low, short near the high, man.

[00:16:28]
All right.

[00:16:31]
False move week beginning.

[00:16:35]
Not above the Asian range, but essentially stop hunt high, drop.

[00:16:39]
Forms out of big fat W rises.

[00:16:45]
Okay.

[00:16:46]
Goes up.

[00:16:47]
Could you have shorted this?

[00:16:48]
Probably.

[00:16:49]
Is it advised?

[00:16:50]
No, it's only a 32-per-range.

[00:16:51]
But there's your stop hunt.

[00:16:53]
There's your V-patterns of the low.

[00:16:55]
There's your second leg off the mayonnaise.

[00:16:58]
Okay.

[00:16:59]
This is a better trade, but this is acceptable.

[00:17:05]
Next night, dealer does it again.

[00:17:09]
He actually gives you a baby head and shoulders in here.

[00:17:12]
If you can see that.

[00:17:14]
Then what happens?

[00:17:16]
Two days in the row, he stops by the high.

[00:17:21]
That's a clue, right?

[00:17:22]
Man, the dealer hit the high.

[00:17:25]
Day two of the cycle.

[00:17:28]
Missed it again.

[00:17:29]
Missed it again.

[00:17:30]
And then got the stops of whoever was in here or in here.

[00:17:37]
Then he corrected big.

[00:17:38]
And look what he gave you.

[00:17:40]
And he made the M-formation.

[00:17:43]
He hit the stops one more time at the London open.

[00:17:47]
And then corrected big.

[00:17:48]
If you tried to grab this W, you did not limit up.

[00:17:52]
Because the box is 41 pips.

[00:17:54]
This didn't go all the way.

[00:17:56]
But look at those pins.

[00:17:57]
It's a trap, baby.

[00:17:59]
Okay.

[00:18:00]
The pins, when the dealer leaves the pins on the table like that, they're a trap.

[00:18:04]
Look at something interesting about this chart.

[00:18:06]
Well, it is interesting to me anyway.

[00:18:08]
Look at all the pins at the trap.

[00:18:09]
Look at all those pins.

[00:18:11]
Pins, pins, pins, pins.

[00:18:12]
Look down there.

[00:18:13]
Pins.

[00:18:14]
Let me clean this off so you can see it.

[00:18:17]
Pins.

[00:18:18]
Trap, pins, pins.

[00:18:20]
Pins.

[00:18:21]
Pins.

[00:18:22]
Pins.

[00:18:23]
Pins.

[00:18:24]
I know.

[00:18:25]
Keep saying pins.

[00:18:26]
Look, it's kind of ironic.

[00:18:27]
Look at that little pin right there.

[00:18:29]
Baster, it's like I got the stops right there.

[00:18:31]
See that little tiny pin right there?

[00:18:33]
They grab the stops.

[00:18:35]
Pins.

[00:18:36]
Pins.

[00:18:37]
Pins.

[00:18:38]
Pins.

[00:18:39]
All right, enough of that with the pins.

[00:18:41]
But notice that the extremes of the chart, the pins turn to the higher to the low, and they

[00:18:47]
grab the snatch and grab price action away from the traders, man.

[00:18:52]
When you start to see the pins, like on that quiz I showed you on the GDP where he was

[00:18:57]
at the high working, it was a bunch of pins to the top side.

[00:19:00]
That's the end.

[00:19:03]
Okay.

[00:19:06]
Day one, anchor was a V or bigger Dub spread out W. Day two, rise, day three, rise.

[00:19:16]
Now we're looking for them to trap high and drop.

[00:19:19]
And that's what they did.

[00:19:20]
They took all the money back against the trend.

[00:19:21]
They made the crossovers and now it's now it's going the other way.

[00:19:25]
The formation, drop.

[00:19:27]
Now you're looking for ends.

[00:19:30]
Day.

[00:19:31]
The opposite is true of a downtrend.

[00:19:38]
Right?

[00:19:39]
A1.

[00:19:40]
Counter trends are advised.

[00:19:41]
Going back towards the peak.

[00:19:42]
Don't trade back towards the peak.

[00:19:44]
If you're struggling with the business, the last thing I want you to do is trade back towards

[00:19:50]
the peak.

[00:19:51]
It's not a trade for you, man.

[00:19:55]
Okay.

[00:19:57]
So what you're supposed to do right now is you're supposed to walk up to a chart.

[00:20:03]
Look at the last three to five days.

[00:20:06]
Identify the deal of trend like this.

[00:20:08]
What's the deal of doing?

[00:20:09]
Okay.

[00:20:10]
Last week in GDP he corrected.

[00:20:12]
This week he made the low.

[00:20:15]
He went up and he's in consolidation.

[00:20:19]
Okay.

[00:20:20]
What do I got?

[00:20:21]
I know 10 hours ahead of time that this is the lowest point on the week after a nice

[00:20:26]
correction.

[00:20:28]
I'm looking for a possible safety coming out of London or New York the next day because

[00:20:33]
he could extend this job all night to work the crosses and then late late London early

[00:20:40]
U.S.

[00:20:41]
He can make his he can make that move.

[00:20:43]
Okay.

[00:20:44]
But this trade is like a joke.

[00:20:46]
You could see it coming from a mile away, man.

[00:20:48]
It's like a freight train coming at you.

[00:20:49]
You know this train is coming because he made the peak formation over here.

[00:20:56]
Price has been corrective in nature for a week.

[00:20:58]
He goes in there and he puts on the brakes and looks a little choppy.

[00:21:02]
He pulls off and there he goes into consolidation the next day.

[00:21:05]
Okay.

[00:21:06]
I got one or two moves.

[00:21:07]
Straight rise or safety?

[00:21:09]
I like the safety trades I can bank on those.

[00:21:13]
So you know what?

[00:21:14]
If the dealer gives me a visible stop on doors and down side I got them.

[00:21:18]
If you straight rises I'm going to pass on that.

[00:21:20]
It's not a trade I want to risk my money on because I could take that long.

[00:21:24]
He can form an information and come back towards the peak and make a double peak formation

[00:21:28]
bottom like this.

[00:21:30]
Right?

[00:21:32]
I don't want this.

[00:21:33]
This will mess me up.

[00:21:34]
That will cost me money.

[00:21:35]
I want this.

[00:21:37]
And man if he gives me a 22 I really got him.

[00:21:42]
22 second leg gives you a second leg.

[00:21:44]
Okay.

[00:21:45]
This is an essence.

[00:21:46]
It's a 22 but it's a safety trade of sorts because he came back to the low, repeated

[00:21:52]
it and hit it twice.

[00:21:55]
Okay.

[00:21:57]
I just showed you on the pound how he did a 22 to the top side where he hit the high on

[00:22:02]
all the time compressions two or three times.

[00:22:05]
So yes they happen.

[00:22:08]
That chart was from last summer.

[00:22:11]
Okay.

[00:22:12]
Look peak formation high.

[00:22:19]
as far to the week comes out.

[00:22:23]
There's your safety man.

[00:22:24]
Okay.

[00:22:25]
Don't take this long.

[00:22:27]
A lot of you fall for that.

[00:22:31]
You're looking for the gym, the 786 retracement or no it's not that deep.

[00:22:35]
So what is it like the 0.25 or something?

[00:22:38]
You're looking for the retracement in here.

[00:22:42]
Stop on above the Asian range in line with the dealers peak down off of the high of the

[00:22:51]
day and that's exactly what he gives you for Christmas or Mother's Day and the 6th.

[00:22:56]
Okay.

[00:22:57]
And she's a beauty.

[00:23:01]
Okay.

[00:23:04]
Then he gives you the end of the run.

[00:23:08]
There is the pattern.

[00:23:13]
Straight back.

[00:23:17]
Those are the blind.

[00:23:19]
One, two, third day.

[00:23:23]
Start looking for the reversals.

[00:23:30]
Okay.

[00:23:31]
Variations.

[00:23:32]
There are variations to the cycle and just when you start cursing me under your breath.

[00:23:37]
The dealers got to observe orders from the powers that be.

[00:23:46]
I don't know who they be, but they be.

[00:23:49]
The cycle must vary to hit the larger targets.

[00:23:54]
Okay.

[00:23:55]
The objectives of the secret powers that be.

[00:23:59]
You know who they are, the Illuminati, the top family, the Fed, New World Order, Blabble,

[00:24:03]
Blabble, Blabble, all that garbage.

[00:24:05]
The reptilians.

[00:24:06]
Okay.

[00:24:07]
So look, they're told, look, we need the dollar at this price point by June.

[00:24:12]
We need the pound to be at this price point by December.

[00:24:16]
They have their targets and their toll where it needs to be.

[00:24:22]
These behaviors that I'm teaching you are going to all the way to their objectives.

[00:24:29]
They're going to hit the stops rise, hit the stops drop, hit the stops rise.

[00:24:32]
They're going to hit their objectives.

[00:24:34]
They're going to do the same bullshit between a dollar, 16 all the way to a dollar, 32.

[00:24:40]
That's what they do.

[00:24:43]
They do the same behaviors over and over and over again.

[00:24:50]
Okay.

[00:24:51]
Understand?

[00:24:52]
Nothing changes.

[00:24:53]
It's the same shit.

[00:24:54]
It doesn't matter what this side of the chart says.

[00:24:56]
You shouldn't care about that.

[00:24:57]
You shouldn't care about the price and the margins over here.

[00:24:59]
Who cares?

[00:25:00]
All you care about is that they make this or do they make this?

[00:25:04]
That's all you should care about.

[00:25:07]
Okay.

[00:25:08]
That's it.

[00:25:09]
Okay.

[00:25:12]
So what I'm telling you is that the variation on the cycle is that if let's say this comes

[00:25:20]
in sooner or later, they're going to add an extra rise.

[00:25:24]
Why would there be a variation?

[00:25:27]
Stop hunt.

[00:25:28]
Shift the trading zone away from players trapped at that particular level.

[00:25:33]
Increase or decrease their position size.

[00:25:35]
Dealer offloading.

[00:25:36]
I don't really know if I've talked about dealer offloading before, but I was thinking

[00:25:41]
about it the other day and decided I needed to write a line on it.

[00:25:45]
The dealer's look.

[00:25:46]
They're holding money, man.

[00:25:49]
They're holding large floats of money.

[00:25:51]
They have to offload their positions.

[00:25:56]
Okay.

[00:25:57]
They might want to increase their float on longs.

[00:25:59]
They might want to decrease their float on longs.

[00:26:01]
No one knows.

[00:26:02]
They might be like, ah, we don't want to hold too many more longs.

[00:26:04]
We want to get rid of some.

[00:26:06]
So they show you a way so that they can sell to you and offload their positions.

[00:26:13]
They'll show you something on the chart to make you want to be a buyer and they can sell

[00:26:19]
to you.

[00:26:20]
That's their job.

[00:26:24]
And do straighters to commit at the extreme levels based on fear or greed, human emotion,

[00:26:30]
things that screw you up.

[00:26:31]
That's how these trends are formed.

[00:26:34]
Then what do they do?

[00:26:38]
They stick these traders for the season, for the quarter, or even for the year.

[00:26:45]
Think about that for a minute.

[00:26:47]
Dealer's got a float.

[00:26:48]
He's got a trillion dollars in his pocket.

[00:26:50]
He's got to spend.

[00:26:51]
He's got 500 million.

[00:26:52]
He's got 500 million short.

[00:26:53]
He doesn't want to be balanced.

[00:26:54]
He wants to turn that float into all longs.

[00:27:03]
How is he going to turn that into all longs on his end?

[00:27:08]
He's going to turn that into all longs by show when you an extreme short position.

[00:27:18]
That makes you sell and he buys from you that turns him along.

[00:27:25]
It's the opposite of what your action is.

[00:27:28]
If you're in that long, if you're in that long, the dealer is in that short.

[00:27:32]
If retail traders see that long, then you bet the dealer is in that short.

[00:27:40]
It's the opposite of what the retail is showing you on the chart.

[00:27:45]
He'll make these extreme moves.

[00:27:51]
Here's an example of an extended run.

[00:27:57]
Previous three weeks, the dealer holds a level.

[00:28:01]
He gets in there and he chops it to the downside on the low side.

[00:28:05]
Then what happens?

[00:28:08]
You notice that each hit to the low is slightly higher because he's snatching the money, pulling away,

[00:28:15]
snatching the money, pulling away, snapping the lower level, short holders.

[00:28:22]
Then what does he do?

[00:28:25]
He starts his rise.

[00:28:27]
500 pips over two weeks.

[00:28:32]
What does he do?

[00:28:34]
Trap, snatch the money.

[00:28:37]
Look at that, look at the pins.

[00:28:39]
Hit it again, just miss it.

[00:28:41]
Hit it again, just miss it.

[00:28:43]
All these wicks to the downside, pulling it away, slightly off the blueberry.

[00:28:49]
Then he starts his move.

[00:28:50]
Hit the stops rise, hit the stops rise.

[00:28:54]
Next week, reset psychological support and resistance.

[00:29:00]
Hit the stops rise, hit the stops rise.

[00:29:04]
Acceleration on a higher time compression.

[00:29:07]
There's your three vector candles for our Charmin friends.

[00:29:13]
There's your three vector candles getting away from the averages.

[00:29:17]
Trend acceleration on the higher time frame.

[00:29:21]
If you see that coming to the terminal in your retail trader, you're like,

[00:29:26]
oh, I'm missing this move.

[00:29:29]
In the pound, what the hell am I missing?

[00:29:32]
Then what?

[00:29:33]
The next week, there's your psychological support and resistance.

[00:29:36]
He spikes one more time to the high.

[00:29:38]
Remember, this is solid green.

[00:29:40]
On a four-hour chart, continuation is warranted.

[00:29:43]
It puts on the brakes, turns that candle inside out and takes it back.

[00:29:49]
It hits the stops along, and away hits the stops high.

[00:29:53]
It's the stops to the high side drop.

[00:29:55]
It's the stops to the high side drop.

[00:29:57]
Back into the range.

[00:30:00]
You could say, excuse, you know, your WVVVVVVN cycle or your WVVN cycle is not true.

[00:30:09]
I understand that.

[00:30:10]
But you have minor corrections in here that pull back to where the stop hunt.

[00:30:15]
So essentially, the trap move, to the trap move,

[00:30:19]
gave the dealer a chance to breathe a little bit, take some money off the table, reset the trend,

[00:30:24]
and they continue on.

[00:30:26]
Hit the stops, hit the stops.

[00:30:29]
Repeat the level, W it out.

[00:30:33]
Continuation, vector, and these are the things that I've been talking about,

[00:30:36]
how he fakes the retail traders out with the trend.

[00:30:39]
You see three, this is four times three, four-hour chart, right?

[00:30:42]
Four times three, 12 hours.

[00:30:44]
When you look at a 15-minute chart, man, there is

[00:30:48]
four, let's see, there's four,

[00:30:52]
one hour candles in there, right?

[00:30:55]
So there's four, and then times four more of those.

[00:30:59]
So is there 16, 15-minute candles in there?

[00:31:02]
So 16, 64 candles, thank you, man.

[00:31:06]
I'm half retarded.

[00:31:07]
Can't do math in front of everybody, drives me crazy.

[00:31:09]
You see, it going straight up, right?

[00:31:11]
On a 15-minute chart, I'm sure it looks like that.

[00:31:13]
Brice is rising all night with little pullbacks in there.

[00:31:17]
So as a retail trader, you see that, and you feel like you're missing something.

[00:31:27]
So what happens is you chase this as a retail trader.

[00:31:31]
I hate when it gets all messed up like that.

[00:31:34]
And if you just step back and realize the bigger picture

[00:31:37]
that eventually this is going to have to correct,

[00:31:39]
price cannot rise indefinitely.

[00:31:41]
But if you saw this coming, if you saw the big hits

[00:31:46]
on the higher timeframe, three hits to the low would each

[00:31:50]
substitute one a little higher.

[00:31:51]
You knew that you had the cycle.

[00:31:53]
Okay, thanks for instance, my math is horrible.

[00:31:57]
Okay, so think about this for a minute.

[00:32:00]
How many hedge funds do you think are still holding

[00:32:04]
Euro at 1,950 by 75?

[00:32:07]
Or for that matter, how many hedge funds are holding

[00:32:11]
down dollar at 7,8 or 35,60 off the W-R-O tracks to the

[00:32:16]
loin? What's the loin? Lower the year.

[00:32:19]
Don't fall for these Pat and these traps, man.

[00:32:22]
They're garbage patterns.

[00:32:25]
Okay, garbage patterns.

[00:32:27]
Look at the chart I put the chart here for you.

[00:32:32]
Look where we're trading now in the middle.

[00:32:34]
How many traders saw this cliff fall off low?

[00:32:37]
This is the weekly in the pound by the way, pound dollar.

[00:32:40]
And took this push to the low, right?

[00:32:42]
They're like, oh, we got the pound short.

[00:32:44]
Look what they did. A big fat W-U-man on the weekly.

[00:32:48]
How many hedge funds are like, oh, we're,

[00:32:52]
we've taken a position trade on the pound short because

[00:32:55]
the G-U in the area over there is having a lot of problems.

[00:33:00]
Think about that.

[00:33:02]
That's how when spot traders become position traders,

[00:33:05]
when the market maker snatched the level away from a

[00:33:08]
a mall, son, they lift the stop and become position traders.

[00:33:11]
That's how that happens, man.

[00:33:13]
That's how you get hedge funds that become position traders

[00:33:16]
because they're stuck.

[00:33:19]
Position traders are something that holds it for a long period

[00:33:21]
of time because they're stuck.

[00:33:23]
Okay.

[00:33:26]
So that's what I'm asking you.

[00:33:28]
Based on fear and greed, these extremes,

[00:33:31]
the dealer shows you something.

[00:33:33]
Look at this trend acceleration pushing down, right?

[00:33:36]
This is a weekly handle.

[00:33:38]
Let me price drop crazy for a week.

[00:33:41]
Let me clean this off.

[00:33:43]
This is one week of straight drop, right?

[00:33:47]
Look at that.

[00:33:49]
Okay.

[00:33:50]
He pushes it down and pulls it all the way back within the next

[00:33:55]
week.

[00:33:56]
So one week straight down, one week straight up.

[00:33:58]
Then he ends up, he issues a hammer right there.

[00:34:01]
Jim, is this the 786 of the full move?

[00:34:05]
Right?

[00:34:08]
We can see that coming, Kevin.

[00:34:10]
We can see the divergence.

[00:34:11]
And we can see that.

[00:34:13]
But regular traders can't see this, man.

[00:34:15]
This is a downtrend.

[00:34:17]
On a big chart, you got moving averages crossed over.

[00:34:20]
You got trend acceleration.

[00:34:22]
Prices above the lower signal lines.

[00:34:24]
I mean, prices below the low signal lines.

[00:34:27]
Think about that.

[00:34:28]
And what happened?

[00:34:29]
How many hedge funds got jammed up in here?

[00:34:32]
And then look, the dealer made the second pass.

[00:34:35]
A couple months later.

[00:34:37]
Look, there's your W, right?

[00:34:40]
Then he comes back and he here and does it again.

[00:34:43]
Look at those hammers he ends on.

[00:34:44]
Same exact stuff.

[00:34:45]
Look at that shark fin and blood in the water.

[00:34:48]
Right there on the hammers.

[00:34:50]
There's a nice run straight.

[00:34:51]
Look, 1, 2, 3, 4, 5, 6, 7, 8, 9.

[00:34:55]
9 weeks, roughly, of rise with some corrections in there.

[00:34:58]
9 weeks.

[00:34:59]
Long enough for you to get your kids to get every four

[00:35:04]
card, isn't it?

[00:35:05]
9 weeks?

[00:35:06]
Wasn't I was in school?

[00:35:08]
OK, so look, it's beautiful, man.

[00:35:12]
But how many traders do you think?

[00:35:13]
How many hedge funds?

[00:35:14]
How many managed accounts are down there going, well,

[00:35:16]
we've taken a short position on the pound.

[00:35:19]
And we think it's going to correct back.

[00:35:23]
Well, guess what?

[00:35:24]
It has a C, it's at 161.

[00:35:26]
They're down big.

[00:35:27]
Open floats to you, to negative.

[00:35:28]
OK, and for that matter, how many traders do you think

[00:35:31]
are stuck here?

[00:35:32]
Long.

[00:35:33]
Don't fall for the breakout above.

[00:35:35]
Look, don't fall for the breakout above.

[00:35:37]
The seasonal high and don't fall for the breakout below.

[00:35:40]
The seasonal low or yearly low.

[00:35:42]
It is a suckers trade.

[00:35:44]
Don't do it.

[00:35:46]
There's your breakout below there.

[00:35:48]
Don't do it.

[00:35:50]
OK?

[00:35:51]
Market makers induce traders to take the wrong

[00:35:53]
directional move by sharp, aggressive price changes.

[00:35:57]
Adam near the high of the day.

[00:35:59]
And low of the day.

[00:36:00]
Guess what?

[00:36:01]
The same thing applies to low of the year.

[00:36:04]
Low with a quarter.

[00:36:05]
Low with a season.

[00:36:08]
When the payers get near, they're all times.

[00:36:11]
Don't think a break below short.

[00:36:15]
Don't think a break above long.

[00:36:18]
You think, look for the track move and pull it back the other way.

[00:36:22]
That's what you think.

[00:36:23]
You think like a market maker, not a retail trader.

[00:36:25]
Because everybody else has taken that break short.

[00:36:28]
And everybody else has taken the break above long.

[00:36:31]
And it's a mistake.

[00:36:32]
I know that sometimes they'll pay out, but they are suckers trades.

[00:36:37]
OK?

[00:36:38]
I mentioned before, the patterns will almost always reveal a reversal set up.

[00:36:43]
I mean, you could say, man, that W on that weekly.

[00:36:47]
I'm sure there's a couple hundred pips in here.

[00:36:49]
Look, none of them might be a thousand pips in here.

[00:36:52]
This is coming in at 44 in the lows 37, around 35-20.

[00:36:58]
There's a lot of pips in there.

[00:37:00]
But guess what?

[00:37:01]
In today, stop on high drop.

[00:37:05]
Stop on high drop.

[00:37:07]
W.

[00:37:08]
Anchor long.

[00:37:10]
Stop on low rise.

[00:37:11]
Stop on low rise.

[00:37:13]
Stop on low rise.

[00:37:14]
M formation back in.

[00:37:16]
Look, stop on high drop.

[00:37:18]
Stop on high drop.

[00:37:19]
Stop on high drop.

[00:37:20]
W track.

[00:37:21]
It's the same shit.

[00:37:22]
I don't care what timeframe you're looking at.

[00:37:25]
The behaviors are the same because on the 15 minute is responsible for making up these little

[00:37:32]
candles.

[00:37:33]
Right?

[00:37:34]
How many 15 minute charts?

[00:37:36]
A week's worth of 15 minute charts makes up and it ends on a hammer.

[00:37:41]
If price has been going peak formation, up, down, up drop, up drop, W, that ends on a hammer.

[00:37:48]
The next day, the next week.

[00:37:50]
The same shit over and over on every timeframe.

[00:37:54]
Understand that human nature is the same on a weekly, a daily, 15 minute, five minute people.

[00:38:03]
Don't know how to trade this stuff and they make irrational decisions on every timeframe.

[00:38:08]
But I'm just showing you that.

[00:38:11]
Below the year high, these are places where the dealers want to offload their positions.

[00:38:18]
They want to turn the traders a certain way.

[00:38:20]
So they make monster railroad tracks at the low of the year.

[00:38:25]
Monster railroad tracks at the low of the year.

[00:38:27]
They get everybody thinking short than the next week they snatch it all back when the

[00:38:32]
positions are taken.

[00:38:34]
And then what happens?

[00:38:35]
Almost out, almost out, almost out, almost out.

[00:38:37]
And that closes the week short because they think, right, what do they think?

[00:38:41]
They think this, right?

[00:38:43]
And they think, oh, it's going to break the low of the year and it's going to continue.

[00:38:48]
And when it doesn't break the low of the year and starts trailing away from them, they

[00:38:52]
lift their stops and they become hedge fund position traders.

[00:38:57]
And they carry a negative float for God knows how long.

[00:39:02]
Okay.

[00:39:07]
Okay.

[00:39:07]
When the volume is not met by the dealer, the market makers trying to obtain a certain amount

[00:39:13]
of open float.

[00:39:14]
And they get his book at 500 million short.

[00:39:17]
He's trying to get his book to a certain place.

[00:39:19]
When his book doesn't match what his orders were, he's only got two moves.

[00:39:24]
He's going to hit the stops and go up, hit the stops and go down.

[00:39:27]
He's going to rise or fall again.

[00:39:31]
Or he's going to hold that level trading between the high and low and handle the cross.

[00:39:38]
Okay.

[00:39:43]
Think about that for a minute.

[00:39:46]
What happens when the dealer is here and he doesn't get his book the way he needs his book.

[00:39:53]
What's he going to do?

[00:39:54]
He's going to do this trade slightly off the high for an extended session.

[00:40:01]
Or he's going to hit it again.

[00:40:03]
He's going to go, oh, you guys didn't think long was the move.

[00:40:06]
I'll show you long again and then I'll do my pattern up here and I'll get everyone to

[00:40:12]
by long and I'll correct all the way back.

[00:40:15]
Or he stays at this level and he gets people thinking A, B equals CD and he'll work

[00:40:23]
the cross over here.

[00:40:26]
Right.

[00:40:28]
Let's say this is G, you'll chop for a week, chop for a couple of days, you saw him

[00:40:32]
do it.

[00:40:33]
He'll chop for a week, chop for a day, chop for two days, chop for three days.

[00:40:37]
And if everyone bites on in the direction, right, that's stupid saying the trend comes

[00:40:42]
out, goes for a win, I can't lie, how it goes.

[00:40:44]
The trend comes, goes from when to came, I think it is.

[00:40:46]
I can't think of it right now.

[00:40:48]
I'm on when blank.

[00:40:49]
Some of you remember, write it.

[00:40:50]
The trend goes for when to came, I think that's it.

[00:40:54]
So what do people see?

[00:40:55]
Oh, the trend is going up.

[00:40:56]
The dealer made the breakup.

[00:40:57]
He's in consolidation.

[00:40:59]
We expect him to continue to rise, right?

[00:41:01]
Well, we know that he's going to make the stop hunt and drop.

[00:41:07]
So what happens is people think that the M formation, they don't see it as the high

[00:41:12]
they see it as a rest in the trend and they expect this,

[00:41:15]
HAB equal CD garbage.

[00:41:21]
Scott, everything is recorded, buddy.

[00:41:23]
You're asking.

[00:41:25]
OK, you know what?

[00:41:26]
I just realized I won't pass it to a 30.

[00:41:28]
OK, let me finish up to a section and then I'll move the other section I wrote

[00:41:33]
for you guys to next week, man.

[00:41:35]
And don't worry if the material is, if I don't complete the material, I'm going

[00:41:39]
to add another week to the boot camp.

[00:41:43]
OK?

[00:41:45]
If you're caught by this move, you must wait for the next level rise or fall.

[00:41:49]
What's the time constraint?

[00:41:50]
Two hours.

[00:41:51]
Why?

[00:41:52]
How long does it take to go from here to the next level where the dealer wants to

[00:41:59]
make the formation?

[00:42:01]
If he vectors in two or three bars, that's 45 minutes, right?

[00:42:07]
45 minutes of a move, three bars.

[00:42:10]
OK?

[00:42:11]
Then he's going to make the new formation.

[00:42:13]
That takes what?

[00:42:14]
30 to 90 minutes.

[00:42:17]
Add that together.

[00:42:19]
You need to wait about two hours for the dealer to make the next level stop hunt.

[00:42:24]
OK?

[00:42:29]
Session changeover.

[00:42:30]
If you get jammed up in something and the session changeover is coming, cut yourself

[00:42:35]
from the position and wait for a new move after 9.45.

[00:42:43]
The goal always, always, always.

[00:42:48]
The goal is the difference between a trader and a guy who makes money.

[00:42:53]
If you're trading to trade, that's not why you should be here.

[00:42:56]
Trading is not a hobby.

[00:42:57]
It's a profession.

[00:43:00]
So here's what you're trying to do.

[00:43:01]
You're trying to convert a losing cycle into a profitable trade.

[00:43:05]
The best way to do that is to mitigate your losses as quickly as possible.

[00:43:09]
OK?

[00:43:11]
How do you mitigate your losses?

[00:43:13]
Man, I've been in the trade for two hours.

[00:43:15]
If it's not moving the dealer cut to high, I'm down 15.

[00:43:19]
I feel like the session changeover is coming.

[00:43:21]
Let me cut to 15.

[00:43:23]
And then if I can make 16 pips next session, I'll be in profit, right?

[00:43:29]
Plus one.

[00:43:30]
I'm not telling you to go plus one.

[00:43:31]
I'm explaining to you that if this is a negative position, 15 or pips or so, why do you

[00:43:37]
have to sit there and wait for it to hit your stop of 23 or whatever number you're using.

[00:43:45]
Then that means you got to make 24 to turn a profit on the next trade.

[00:43:53]
So what I'm telling you is if you see them hanging around and it's negative 15, negative

[00:43:57]
10 back and forth and not going into profit, mitigate the loss and look for a better entry

[00:44:03]
at next level session changeover and convert a losing trading cycle into a profitable

[00:44:09]
one by hitting 40 or 50, let's say 40 minus 15, you're plus 25 for the day.

[00:44:16]
That's a winning cycle.

[00:44:18]
This will keep your equity curve growing steady and strong.

[00:44:22]
OK?

[00:44:23]
And by the way, I think Luther and Carter nine for nine.

[00:44:27]
And they took off Friday because they had to get one a trip.

[00:44:31]
There are nine attempts for nine wins, nine for nine.

[00:44:35]
Yes, that is 100%.

[00:44:38]
And they are my guinea pigs.

[00:44:40]
They are testing the strategy that I will release on the last day of boot camp that some

[00:44:45]
of you know about.

[00:44:46]
So they're doing very well with it.

[00:44:52]
They were from sick.

[00:44:53]
They were six for six.

[00:44:54]
Now they're nine for nine.

[00:44:55]
About three trades they traded I think three days for today's last week.

[00:44:59]
OK, I'm over.

[00:45:01]
Next week, we're going to talk about trap candle patterns.

[00:45:06]
We're going to go over outside structure spikes, the things that the dealer uses to trap

[00:45:19]
the traders and things you need to recognize as part of your flashcards.

[00:45:23]
I thought I would be able to cover that to none or what I was thinking.

[00:45:26]
OK?

[00:45:27]
But anyway, I thought it was a pretty good session.

[00:45:30]
I enjoyed it.

[00:45:31]
OK, I really don't have any homework for you this week except the last seven and a half

[00:45:38]
weeks of homework that I've been giving you.

[00:45:42]
OK?

[00:45:43]
So what I need you to do, the end of the age and session this week is draw your line on

[00:45:52]
24 hour charge look for peak formation.

[00:45:58]
Look for the dealer to make the high and low of the week look for safety trade sets.

[00:46:04]
Look for clean, seeable flashcards setups.

[00:46:08]
OK?
