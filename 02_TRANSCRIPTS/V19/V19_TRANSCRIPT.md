# V19 — TRANSCRIPT

## ⭐ TIMESTAMP CONVENTION — STATED ONCE, AT THE TOP (`V14_REVIEW_R1.md` GATE, open item 173)

**Every `[HH:MM:SS]` in this file and in every V19 artifact is the committed marker grid of THIS
file — the 841 markers below — and nothing else.** Independent ASR was run this session
(VERIFICATION §5) and **its clock is never cited**; where it arbitrates a word, the correction is
attached to the *marker grid's* timestamp, not to the second pass's.

⚠️ **THE SCREENSHOT CLOCK AND THE MARKER CLOCK DO NOT COINCIDE EXACTLY, AND V19 DRIFTS THE SAME
DIRECTION V18 DID — BUT ONLY ONCE.** V16 and V17 measured a flat zero; V18 drifted `0 → −3 s`
monotonically. **V19's sweep offset is `0 s` from `02:00` to `49:10`, and `−1 s` from `49:59` to the
end** — a single one-second step, bracketed to the interval `49:10`–`49:59`
(`04_SCREENSHOTS/V19/INDEX.md` §0). This is handled the way `SWF_CAPTURE_RECIPE.md` §8a step 4
requires and **not** by a fudge factor: **every screenshot is named from its OWN burned-in player
timecode, read from its own pixels.** A screenshot name is therefore a *player-clock* fact and a
marker is a *transcript-clock* fact, and the two agree to within **≤1 s** of measurement drift plus
the 5-second sweep-sampling floor. **Nothing in this artifact set depends on a sub-5-second
alignment.**

Corroboration at five content points where the screen changes on a sentence. **Quotations are
verbatim from the marker grid, ASR defects included:**

| Marker | Transcript line, VERBATIM | Screen, burned player timecode | Δ |
|---|---|---|---|
| `[00:11:59]` | *"Okay, here's what we're gonna talk about for the next hour"* → `[00:12:02]` *"Track King patterns fuel structures behavioral analysis"* | the `Trap Candle Patterns / Dealer Structures / Behavioral Analysis` agenda slide is up at **12:00** | +1 s / −2 s |
| `[00:13:10]` | *"The definition of a half a bad man"* | the `Half-A-Batman:` four-clause definition slide at **13:15** | +5 s |
| `[00:22:58]` | *"Okay 30 minutes, I'm gonna write I'm gonna change the slide"* | the **PowerPoint editing window** is on screen at **23:10** | +12 s |
| `[00:45:03]` | *"It's an aggressive move by the deal of the settle low of the day or lower the session"* | the `W` slide, pre-edit, at **45:00** | −3 s |
| `[01:02:36]` | *"Simple easy to understand"* → `[01:02:39]` *"Evening star mowling star"* | the `Evening Star / Morning Star` definition slide at **62:44** | +8 s / +5 s |

Screen-change granularity is the 5-second sweep grid, so ±5 s is the measurement floor. **The
`+12 s` on the PowerPoint row is the edit taking twelve seconds to open, not drift** — the frame at
`23:10` is the first sweep sample on which the editor appears, and `21:15` and `23:25` bracket it
with the slide before and after the change.

---

## SOURCE

| Field | Value |
|---|---|
| Video ID | **V19** |
| Original filename | `Bootcamp1 Wk9 052012 Part1 (67mins).swf` |
| SHA-256 | `7e8a1c2bd25b7f15a2b67458d666d16444c9ce7990cc666a71943cba5c1ab28e` — verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session on the flat `Bootcamp/` canonical path, **and re-verified after the frame-rate patch** to prove the original was not modified (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| Byte length | **25,694,598** — matches `SOURCE_MANIFEST.md` exactly |
| Duration | 01:07:21 (audio measured **4042.004898 s**; SWF header **12,127 frames ÷ 3.0 fps = 4042.333 s**; `SOURCE_MANIFEST.md` 01:07:21 = 4041 s — **three independent figures agreeing to within 1.33 s**). ⭐ A fourth, independent of all three: the player's own burned readout **clamps at `67:22`** on the final sweep frame, which is `4042 s` |
| Lesson title | ⭐ **PRINTED, AND UNAMBIGUOUS THIS TIME.** The section title `MARKET MAKER TRAP MOVE` / `MARKET MAKER TRAP MOVES` runs from `12:00` to the end of the file, and the agenda slide at `12:00` prints the three subjects in full: **`Trap Candle Patterns`**, **`Dealer Structures`**, **`Behavioral Analysis`**. This is exactly what V18's closing slide announced as next week's subject. The quarantined per-lesson header's *"Primary Topics: Steve Mauro Beat The Market Maker (BTMM) Methodology"* is the same generic non-answer it gives every lesson, and its `RULES.md` / `NOTES.md` / `VISUAL_INDEX.md` are fabricated — see `QUARANTINE_REGISTER.md` **Q-020** |
| Session date | **2012-05-20**, from the filename and `SOURCE_MANIFEST.md` — ⭐ **AND CORROBORATED FROM INSIDE THE FILE, IN PRINT.** The schedule slide standing from `00:16` to `≈04:00` prints `May 20th — Regular session` as the *current* row of a forward calendar whose next entries are `May 27th`, `June 3rd`, `June 10th`, `June 17th`, `June 24th`, `July 1st`. Spoken corroboration at `[00:00:00]` *"Welcome back week nine"* and `[00:00:05]` *"regular session tonight the 27th Memorial Day. There will be no session"* |
| Week number | **Week 9** — stated at `[00:00:00]` and printed on the deck's cover slide. ⚠ **V19 therefore does NOT reproduce V18's silence**, and this is a second data point for open item 179: V17 (Part 1) states its week, V18 (Part 2) does not, V19 (Part 1) states its week. See VERIFICATION §4 |
| Continuity with V18 | ⭐ **ANNOUNCED IN ADVANCE BY V18 AND DELIVERED.** V18's final slide printed `Trap Candle Patterns` as next week's subject and `[00:45:01]` said *"Next week, we're going to talk about trap candle patterns"*. V19 is that lesson. ⚠ But V19 is **not** a continuation of V18's recording: it opens with a full greeting, a week number, and eleven minutes of announcements — the pattern of a Part 1, not V18's mid-thought *"Back to the cycle"* |
| Frame rate | **3.0 fps** in the SWF header — read from **this file's own header**, not assumed (`SWF_CAPTURE_RECIPE.md` §10 as corrected by V10 R1 open item 87). The 10× sweep patch is therefore **3.0 → 30.0** here, and the patched copy was re-read to confirm `30.0` exactly |
| Stage size | **1024 × 786** — the majority class. `GOTCHA 5`'s table gives `(512, 300)`, and the pre-click / post-click guard **confirmed it fired** rather than assuming it (`sweep.log`: *"play click CONFIRMED"*). ⚠ See VERIFICATION §6 — the same coordinate **failed** on the *unpatched* copy of this same file, and the guard caught it |
| Transcribed by | ASR, by a pre-ingestion session. Copied **byte-for-byte** and verified 2026-08-14 — see VERIFICATION below. The pre-ingestion file's own `# VIDEO` header block is **NOT carried over**: its *"Course Position: Video 20 of 21"* is wrong under `D-017` §2's renumbering (this file is **V19**), and its *"Primary Topics"* line names the methodology rather than the lesson |
| Transcription confidence | **MEDIUM–HIGH.** 841 markers, strictly monotonic, **zero** backwards steps, **one** equal-adjacent pair (at `[00:41:32]`), gaps 0–13 s (mean 4.80 s), last marker `[01:07:13]` sitting **9.0 s** before the measured end of audio, and a speech rate of **145.4 wpm** across 9,794 words. It preserves its own mishearings — *"half a bad man"*, *"Track King patterns"*, *"the lobby bed"*, *"Jim Norshan"* / *"Jim Knickers and"*, *"a yard"*, *"the big boy"*, *"movie average"*, *"15 to 25 trips"* / *"pits"*, *"emeraldo information"*, *"Nader and vortex"*, *"orange hearts blue stars green clovers"*, *"it's free like a pizza"*, *"knocking that beat"*, *"they're a pudic"*. **A fabricated transcript does not invent its own mishearings.** ⚠⚠ **BUT ITS SINGLE MOST FREQUENT DEFECT IS SYSTEMATIC AND IT HIDES THE LESSON'S OWN TITLE** — see VERIFICATION §5 correction **#1** |

---

## SPEAKER TABLE — MANDATORY UNDER `D-025` consequence 3, re-adopted by `D-033`

| Speaker | Runtime | Basis |
|---|---|---|
| **Course author (Steve Mauro)** | **100%** — `[00:00:00]`–`[01:07:13]`, the whole file | Six non-acoustic strands, below. **CERTAIN** |
| Guest presenter | **0%** | No second voice is introduced, addressed, thanked or handed to anywhere in the file. Students are named in the **third person**, quoted in reported speech, or addressed directly by the instructor (*"Thank you Jim"*, *"there you go, Coke. Thank you buddy"*), never handed the floor |

**Tested on strands fixed before the answer was known, not inherited from V18.** The acoustic
cross-file screen was **NOT** run, per V07's prohibition.

### THE SIX STRANDS — non-acoustic, `D-025`/`D-033` method

| # | Strand | Evidence, VERBATIM |
|---|---|---|
| **1** | ⭐⭐ **He claims authorship of the boot camp itself, in the first person** | `[00:10:42]` *"they made a boot camp **before I even invented boot camp**"* |
| **2** | ⭐ **Students address him by name and he answers in the same voice, with no attribution break** | `[00:28:03]` *"He's one of those guys. I said **Steve** your full shit. I don't believe you. I said, okay"*; `[00:56:53]` *"That looks like some level three ship that **Steve** told me"*; `[00:58:11]` *"**Steve** the railroad tracks are too big my stop loss has to be 35 pips"*; `[00:59:04]` *"if you normally are one lot trader and said **Steve** this is 30 pips distance on my stop"* |
| **3** | ⭐ **He owns the course's schedule and syllabus in the first person, against a printed calendar** | `[00:00:52]` *"the 17th is the final boot camp"*; `[00:03:53]` *"after Labor Day. **I'll set up another schedule** and start doing the boot camps"*; `[00:03:57]` *"We'll use some of the material I used and **I'll try to write some more stuff for you guys**"*; `[00:05:17]` *"The class will not be recorded or streamed … **I've done it. It's a pain in the ass**"* |
| **4** | ⭐ **He owns the strategy being released at the end of the course, and names his testers** — the *same* strand V18 carried | `[00:01:59]` *"Using this technique **there were my guinea pigs**"* [*"they were my guinea pigs"*]; `[00:02:12]` *"**We're gonna release the scripts** on the last night of boot camp"*; `[00:02:16]` *"**I'll go over how to set them up**"* |
| **5** | **He sets homework in the first person and is the addressee of the students' progress mail** | `[00:08:26]` *"**I have taken the segments that you need and broken them down** for two hours a week for you guys"*; `[00:05:50]` *"This is **an email that came to me**"*; `[00:06:33]` *"anyways **from Ron. Thank you, Ronnie. I appreciate the letter**"* |
| **6** | ⭐⭐ **It is his birthday and the students sing to him — on a slide made for him by name** | `[00:11:31]` *"Thank you guys. Thank you. Thank you. Thank you. **I'm old today**"*; `[00:11:55]` *"Thank you **some of you sing really well**"*; and the slide at **11:15** prints *"Happy Birthday, **Steve**! We love you very much! Love, Heidi, Chase, and Gemma"* |

**No strand depends on voice timbre.** Strand 6 is the strongest and is **new to the corpus**: the
deck itself names the speaker, in a slide inserted by a third party, and the speaker responds to it
in the first person inside the same minute.

---

## VERIFICATION — RUN THIS SESSION, 2026-08-14

### §1 — STRUCTURAL INTEGRITY OF THE MARKER GRID

Re-derived in this session's shell over the committed body:

```text
markers            841
first / last       [00:00:00] / [01:07:13]   (last = 4,033 s)
monotonic          YES  -- 0 backwards steps
equal-adjacent     1     ([00:41:32], twice)
gaps               min 0 s / max 13 s / mean 4.80 s
words              9,794      speech rate 145.4 wpm over 4,042 s
tail margin        9.0 s before the measured end of audio
```

**The 9.0 s tail margin is the largest in the corpus so far** (V18's was 1.0 s). The final marker
`[01:07:13]` carries a complete sentence and the audio does not obviously continue past it, but
**this session did not verify the last nine seconds are silent** and does not claim they are. Open
as `A-132`.

### §2 — DURATION AGREES ON FOUR INDEPENDENT MEASUREMENTS

`ffprobe` on the extracted audio **4042.004898 s**; SWF header **12,127 ÷ 3.0 = 4042.333 s**;
`SOURCE_MANIFEST.md` **4,041 s**; the player's own burned readout **clamping at `67:22` = 4,042 s**
on the last sweep frame. **Spread 1.33 s across four methods.**

### §3 — THE SOURCE FILE WAS NOT MODIFIED

`shasum -a 256` on the original, re-run **after** the frame-rate patch was written to a *copy*:
`7e8a1c2b…1ab28e`, identical to `SOURCE_MANIFEST.md`. The patch was applied to
`serve/v19_x10.swf` and never to the library file (`SOURCE_INGESTION_PROTOCOL.md` §2).

### §4 — WHAT V19 SAYS ABOUT ITS OWN DATE, AND WHY IT MATTERS TO OPEN ITEM 179

⭐ **V19 dates itself twice over, and one of the two is printed.** `[00:00:00]` *"Welcome back week
nine"*, and the schedule slide standing from `00:16` prints `May 20th — Regular session` at the head
of a forward calendar. **This is the first lesson since V17 to corroborate its own date internally.**

⚠ **Offered for item 179's ruling, not as an argument for either side.** V18's R1 observed that a
lesson's silence about its own date is *"a property of which half of the night you are in"* — Part 1s
state it, Part 2s do not. **V19 is a Part 1 and it states it, which is consistent with that
generalisation and does not test it.** V20 (`Wk9 052012 Part2`) is the case that would.

### §5 — INDEPENDENT ASR, AND THE CORRECTIONS IT FORCES

⚠⚠ **STATE OF THIS CHECK, STATED FIRST: THIS IS A PRE-REGISTERED SEGMENT PASS, NOT A FULL-FILE
PASS.** V15, V16 and V18 each completed a full-file independent transcription. **This session did
not.** Two engines were started on the whole 67-minute file — `faster-whisper large-v3` (CTranslate2,
int8) and `openai-whisper large-v3-turbo` — and both projected multi-hour runtimes on this machine
while the screenshot sweep was running; the second was still projecting **4h28m** when it was
stopped. **The full-file pass is OWED and is listed as an open item.**

**What was run instead is stronger than an ad-hoc spot check and weaker than a full pass:** a
**twelve-segment pre-registration**, written to
`06_MANUAL_BACKTEST/V19/data/asr_segments_PREREGISTERED.txt` **before any segment was transcribed**,
choosing segments because a V19 rule, number or TDI claim rests on them — **not** because anything
looked wrong. Engine: **`openai-whisper medium.en`**, independent of the pre-ingestion transcript.
**Seven of the twelve returned in time for this commit** (`S1`, `S2`, `S4`, `S5`, `S6`, `S7`, `S11`)
and they cover every load-bearing rule in the lesson. **Its clock is never cited below**; corrections
are attached to the marker grid's own timestamps.

#### ⚠⚠ CORRECTION #1 — THE LESSON'S CENTRAL STRUCTURE IS SYSTEMATICALLY MIS-TRANSCRIBED, AND SO IS ITS TITLE

**This is the most important entry in this file and it is not one line — it is a class of line.**

**(a) The letter `M`.** The committed transcript renders the spoken letter *"M"* as **`end`**,
**`an`**, **`and`** or **`the end`** throughout. A reader of the committed file alone meets *"the
end is an aggressive move by the dealer"*, *"that's how the end is formed"*, *"a good
information"*, *"that's a pretty damn good end"*, and cannot recover that the subject is the **M
formation**.

| Source | Text |
|---|---|
| Committed, `[00:27:45]` | *"Will consist of a minimum of eight bars a"* |
| Independent engine (`S7`) | *"**A good M formation** will consist of a minimum of eight bars."* |
| Committed, `[00:27:37]` | *"Appendings waiting there. That's how **the end** is formed a"* |
| Independent engine (`S7`) | *"…that have pendings waiting there. That's how the **M** is formed."* |

⚠️ **The independent engine makes the same mistake in places** (it gives *"a good and valid **end**
formation"* at `S6`), which is why this is recorded as a **property of the audio**, not a defect of
one transcriber. **The printed deck settles it** — the slides read `The " M " Formation` and
`The W:` — and every V19 artifact writes **`M`**, citing the marker but not quoting the raw token as
a term.

**(b) The lesson's title.** `[00:12:02]` reads *"**Track King patterns fuel structures** behavioral
analysis"*. **The printed agenda slide at `12:00` reads `Trap Candle Patterns` / `Dealer
Structures` / `Behavioral Analysis`.** Two of the lesson's three announced subjects are
unrecoverable from the transcript alone.

**(c) `Half-A-Batman`.** Rendered *"half a bad man"*, *"half of that man"*, *"half a Batman"*,
*"Back man"* and *"Day and bird it"* across the file. The independent engine gives *"half of
Batman"* (`S1`); the deck prints `Half-A-Batman`.

⚠️ **CONSEQUENCE: no V19 artifact quotes a raw structure name from the committed body as a term of
art.** The body is byte-for-byte and is not edited; the names are established from the deck and
cited here.

#### ⭐⭐ CORRECTION #2 — `[00:23:57]` AND `[00:24:32]` — `25 to 55` IS `25 to 50`

| Source | Text |
|---|---|
| Committed `[00:23:57]` | *"extend that high to the next level strike zone **25 to 55** higher"* |
| Committed `[00:24:32]` | *"To the next level strike zone **25 to 55**th out"* |
| Independent engine (`S5`) | *"…to the next level strike zone, **25 to 50 pips higher**."* and *"…he will extend to the next level strike zone, **25 to 50 pips out**."* |

**Both disputed markers read `50` on the second engine — and the committed file itself reads `50` at
`[00:25:06]` and `[00:25:31]`, in the same rule, 70 seconds later.** All four instances are
`25 to 50 pips`.

⚠️ **This closes a conflict rather than opening one.** An ambiguity record was drafted for the
`55`/`50` split and **withdrawn in the same session**; it is not carried forward. Load-bearing for
`V19_SOURCE_NOTES.md` §5.3 and `V19_INTERPRETATION.md` §2.2.

#### ⭐ CORRECTION #3 — `[00:16:05]` — `"of two hours"` → **`"up to two hours"`**

| Source | Text |
|---|---|
| Committed | *"30 to 90 minutes **of** two hours to deal or holds the level"* |
| Independent engine (`S2`) | *"thirty to ninety minutes **up to** two hours **the dealer holds the level**"* |

**The committed preposition makes the sentence meaningless; the corrected one makes it a bounded
range.** The Half-A-Batman hold is **30–90 minutes, up to two hours**. Load-bearing for
`Q-020` §2, where the fabricated file's `Peak Time Gap 30-90 mins` row is scored against it.

#### ⭐ CORRECTION #4 — `[00:27:00]`–`[00:27:16]` — THE DIVERGENCE DEFINITION IS GARBLED, AND IT IS THE TDI PASSAGE

| Marker | Committed | Independent engine (`S6`) |
|---|---|---|
| `[00:27:00]` | *"That's why we understand **our herds and stiffens** everybody else"* | *"that's why **we understand divergence different than** everybody else"* |
| `[00:27:07]` | *"since TDI RSI **mine** tracks the closes"* | ⭐⭐ *"since **TDI RSI line** tracks the closes"* |
| `[00:27:16]` | *"So I heard it's **a spot it**"* | *"**divergence is spotted**"* |

⭐⭐ **`RSI mine` is `RSI line`.** This matters beyond a typo: `[00:27:07]` is one of the two markers
in V19 that name the TDI's operative line, and the committed token obscures it. **With the
correction, V19 says plainly that the *RSI line* is what tracks the closes.**

#### ⭐ CORRECTION #5 — `[00:29:21]` — `"not only for one"` → **`"not only for London"`**

| Source | Text |
|---|---|
| Committed | *"it's **not only for one** and it's for formation itself"* |
| Independent engine (`S7`) | *"It's **not only for London**, it's the formation itself."* |

**This changes the scope of the eight-bar rule from meaningless to session-general.** The minimum is
asserted to hold outside the London session too.

#### CORRECTION #6 — `[00:28:27]` — `"he sent the astring to you then"` → **`"he sent me a spreadsheet"`**

Independent engine (`S7`): *"he sent me a **spreadsheet**, man, that is like 397 pages long"*. The
`397 pages` figure is **verbatim on both engines**; the medium it was delivered in was not
recoverable from the committed file.

#### CORRECTION #7 — three names

| Marker | Committed | Independent engine |
|---|---|---|
| `[00:27:48]` | *"my friends I need"* | *"my friend **Zain**"* (`S7`) |
| `[00:28:03]` | *"I said Steve your full shit"* | *"…said, Steve, **you're full of shit**"* (`S7`) |
| `[00:29:00]` | *"**people may should** highs"* | *"**P[eak] formation** highs"* (`S7`) — ⚠ the engine's own reading is indistinct here and this correction is graded **LOW**; it is recorded, not relied on |

#### ✅ CONFIRMED VERBATIM BY THE SECOND ENGINE — the lines the rules rest on

Every one of these was read back **identically** by the independent engine:

| Marker | Line | Status |
|---|---|---|
| `[00:22:43]`–`[00:22:48]` | *"The second leg rise can be slightly above the first but must close back below"* / *"Within 30 minutes"* | ✅ **verbatim** (`S4`) — **and written into the deck on camera at `23:25`** |
| `[00:23:39]`, `[00:23:47]` | *"come back below that number within 30 minutes"* / *"45 minutes tops"* | ✅ verbatim (`S5`) |
| `[00:27:18]` | *"because we base TDI on the closes"* | ✅ **verbatim** (`S6`) |
| `[00:27:25]` | *"averaging the closes on TDI"* | ✅ verbatim (`S6`) |
| `[00:56:25]`–`[00:56:30]` | ⭐⭐ *"possibly divergence on the TDI or the RSI line"* | ✅ **VERBATIM** (`S11`) — the single most cited line of this lesson |
| `[00:27:45]`, `[00:29:13]`, `[00:29:21]` | *"a minimum of eight bars"* | ✅ verbatim, all three (`S7`) |
| `[00:28:45]` | *"eight bars or more without any other filter is in the high 80 percent"* | ✅ **verbatim** (`S7`) — ⚠ confirming the *quotation*, not the *claim*; see `V19_INTERPRETATION.md` §2.3 |
| `[00:28:30]` | *"397 pages long of every m and w that he saw in euro in pound in Australian"* | ✅ verbatim (`S7`) |
| `[00:13:14]`–`[00:13:52]` | the four Half-A-Batman definition clauses | ✅ verbatim in substance (`S1`) — with the two corrections at #8 below |
| `[00:16:09]` | *"Sometimes he'll take this into the next day"* | ✅ verbatim (`S2`) |
| `[00:24:12]` | *"he grabbed some volume down in here that he needed"* | ✅ verbatim (`S5`) |

#### CORRECTION #8 — `[00:13:37]` / `[00:13:42]` — the Half-A-Batman definition, two words

| Source | Text |
|---|---|
| Committed `[00:13:37]` | *"**You** will not repeat that level again"* |
| Independent engine + ⭐ the printed slide at `13:15` | *"**He** will not repeat…"* |
| Committed `[00:13:42]` | *"If he does you will allow some type of **profit-looking**"* |
| Independent engine (`S1`) | *"if he does, **he** will allow some type of **profit booking**"* |
| ⭐ The printed slide at `13:15` | *"**or** he will allow some type of **profit booking** by the traders."* |

⚠ **Note a genuine speech/deck divergence inside this correction:** the slide reads *"**or** he will
allow"*, and the independent engine confirms he *said* *"**if he does**, he will allow"*. **That is
the instructor departing from his own slide, not an ASR defect.** The ASR defects are `you` for `he`
and `profit-looking` for `profit booking`.

#### ⚠ WHAT THE SEGMENT PASS DOES **NOT** COVER

Five of the twelve pre-registered segments (`S3`, `S8`, `S9`, `S10`, `S12`) had not returned when
this file was committed. They cover the `15 to 25` pip consolidation figures, the bar-1 counting
convention, the `eight candles = two hours` identity, the W time cap, and the star-formation
`15 in / 15 out`. **Those five passages are therefore carried on the committed transcript alone plus,
where applicable, the printed deck.** Listed as an open item together with the full-file pass.

### §6 — ⚠ `GOTCHA 5`'s GUARD FIRED THIS SESSION, ON A FILE WHOSE COORDINATE IS "KNOWN"

**Recorded because it is a live instance of the failure `GOTCHA 5` exists to catch, not a
hypothetical.** V19 declares a `1024 × 786` stage, for which the recipe's table gives `(512, 300)`,
and on the **patched 10× copy that coordinate worked** — the guard passed and 817 frames of real
lesson content followed.

**On the UNPATCHED copy of the same file, at 1×, the same coordinate did not start playback.** The
unpatched file opens on a Camtasia poster frame whose play control sits elsewhere; a follow-up
attempt at `(512, 358)` **also** missed and the guard returned `PLAY CLICK MISSED` and exited
non-zero, as designed.

⭐ **The consequence for the record: the play coordinate is a property of the file *as served*, not
of the stage size alone.** Nothing downstream was harmed — the guard converted it into an immediate
non-zero exit both times, and the 1× pass was an optional extra (an attempt to capture the deck's
cover slide, which the 10× sweep cannot reach because its first frame is already at `00:16`).
**The cover slide is therefore NOT in this lesson's screenshot set**, and its `WEEK 9` legend is
recorded here as *not* independently captured by this session.

---

# VERBATIM TRANSCRIPT

[00:00:00]
Welcome back week nine welcome everybody not going to go through and say hello and all my stupid jokes again

[00:00:05]
Let's get rolling all right announcements. I was going over regular session tonight the 27th Memorial Day. There will be no session

[00:00:14]
All right the web class starts June 3rd. That's the following weekend after the holiday the recordings that are up will be taken down

[00:00:23]
Will replace the recordings that are up with this new class that's going up, okay?

[00:00:28]
Find a boot camp June the 17th that is the week before go to New Jersey for the lobby bed

[00:00:38]
No, we're not having a boot camp on the 10th or having a class

[00:00:42]
The web class will be up following week, okay, so the 10 there will be the recordings for you to review you have the recordings to go over

[00:00:49]
I'm gonna do the class you'll have a week

[00:00:52]
Through your huge recordings before we get back into boot camp the 17th is the final boot camp

[00:00:59]
Raise your work enough some scripts for us

[00:01:01]
We're gonna talk about some different ways to manage money actually now that we brought it up to good point

[00:01:06]
I am gonna post an article this week on

[00:01:10]
Wednesday probably

[00:01:13]
Yeah, Wednesday's good. I'll post an article for you guys Wednesday or tonight tomorrow

[00:01:18]
I'll get it up there, but the latest will be Wednesday go to the forum and check it

[00:01:24]
It is about manage your money like a dealer

[00:01:28]
And had a handle

[00:01:30]
entries on taking trades

[00:01:31]
I'm gonna set this up the article be in there and then on the final boot camp I'll release the scripts on how to do this

[00:01:38]
Okay, I can tell you that Luther and Kirk

[00:01:43]
Different sides of the world one to California ones that Carolina

[00:01:46]
Have been doing this and they went 10 for 10 on their trading over the last week and a half

[00:01:51]
They took a hit and then they got right back and had another win

[00:01:54]
So I think they're like 11 for 12 over their last 12 trades

[00:01:59]
Using this technique there were my guinea pigs

[00:02:02]
So what we're gonna do is we're gonna release the scripts

[00:02:09]
10 for 12 he just posted for me Luther was 10 for 12

[00:02:12]
We're gonna release the scripts on the last night of boot camp

[00:02:16]
I'll go over how to set them up and stall them will go through all the box checks and all the stuff you need to do

[00:02:22]
So what I'll do is I'll post an article for everyone why Wednesday come in and check the form

[00:02:30]
Read the article and get ready for the final hook in on the 17th, but in the meantime, we're gonna have a class

[00:02:37]
Go on a holiday weekend and then we'll get back together and then on June the 24th

[00:02:42]
We'll be in New Jersey hey, just to show it hands put up a wire and how many thinking about coming to hang out in New Jersey

[00:02:52]
Okay, we'll get the links up and get a head count

[00:02:57]
We'll figure out if we have enough space and all that it'll be fun man if you could make it come on over and hang out

[00:03:03]
It's nice to meet you guys in person

[00:03:08]
And it's also nice to be around other traders

[00:03:12]
That are going through the same things you're going through it's very I don't know cathartic

[00:03:17]
I guess is the right word or they're a pudic. Maybe that's a better word. I don't know

[00:03:21]
What are this fun?

[00:03:25]
That's a good question. I you have to ask go on the form and post that who's in charge of parking up there. I don't know man

[00:03:32]
Okay, anyway, okay, so that's it. Then we're gonna take a few months break. Did you lie?

[00:03:37]
The recording is when the boot camp will be up if you haven't done the work for the boot camp go back and start watching the recordings and just

[00:03:45]
treat it

[00:03:46]
Start at the beginning and just go over and over and over again and do it until we get back after Labor Day

[00:03:53]
Okay after Labor Day. I'll set up another schedule and start doing the boot camps

[00:03:57]
Again, we'll do a different cycle. We'll use some of the material I used and I'll try to write some more stuff for you guys

[00:04:02]
All right, that's what we're gonna do. That's the sketch

[00:04:05]
All right, let me pick up the patient a little bit because I lost about 10 50 minutes with this scrap

[00:04:09]
All right, I'm not gonna read this to you. It's a waste time man your expectations

[00:04:15]
All right Jim Norshan just posted New Jersey or Boston the form has the parking information. Thank you Jim

[00:04:22]
Okay, oh Labor Day is the first Monday of September

[00:04:27]
So we'll start shortly after that. Maybe mid-September. We'll get back to boot camping all right

[00:04:33]
Sorry about that. I know somebody guys. I know what that is

[00:04:37]
It's one day when everybody works. It's Labor Day and the rest of the time you take the rest of the year off

[00:04:42]
That's how we do it here in America

[00:04:44]
All right

[00:04:45]
You already know you two hours a week stop me a negative all that stuff

[00:04:50]
All right chat box. I'm trying not to read it, but you guys I can't help but sometimes, but I'm still ignoring it

[00:04:56]
announcements

[00:04:57]
We just went over the live class on the schedule any information you need go to the New Jersey or bus section in the form and

[00:05:04]
use time you are about com slash mm-fx lodging how you set that up. It's a list of all the

[00:05:10]
hotels that are nearby

[00:05:15]
Very important

[00:05:17]
The class will not be recorded or streamed

[00:05:20]
I've done it. It's a pain in the ass. It slows down the pace of the class and the people that have made the effort to get there

[00:05:26]
Don't get a good product. So the class will not be recorded and will not be streamed

[00:05:31]
This is gonna be a regular class. We're gonna hang out talk

[00:05:35]
We'll probably have a good face class the streaming and recording. I know it helps everyone, but the read that's why I'm doing the web class right before

[00:05:44]
Okay

[00:05:46]
All right, I already mentioned the dates on that

[00:05:50]
Progress I wanted to read this first line. This is an email that came to me. I thought it was great

[00:05:54]
There's actually two emails and I didn't get to post one, but since the boot camp trading has been presented

[00:06:00]
By the way, are you marine not a marine spend a lot of years as a firefighter and you're just a strict

[00:06:05]
Maybe not not so much. We don't kill each other or a few pounds of each other, but they're pretty strict

[00:06:10]
I have improved my trading. Thank you so much for going that extra mile for the last two weeks

[00:06:15]
I'm taking 12 trades 10 wins two losses where I lost about a thousand bucks, but nearly just under 16

[00:06:22]
Now, I don't think you can do much right on that canyon

[00:06:25]
That's a 16 to one ratio

[00:06:28]
for dollars

[00:06:29]
paint versus lost not bad

[00:06:33]
Okay, anyways from Ron. Thank you, Ronnie. I appreciate the letter. Appreciate the thank you's

[00:06:39]
Very excited to hear that

[00:06:42]
Another one that I did mention that's on here is Dave McCoy

[00:06:46]
So many notice or he's to hate me to push me out all the time on a weekly basis

[00:06:51]
And he turned the cooler. I didn't get to post a email day, but I'm really proud of you during this big market shift

[00:06:56]
Or when they shifted his own you aggressive moves at the scene

[00:06:59]
He had the patience to sit on his hands and not take any trades and he only grabbed two trades last week

[00:07:05]
But they were perfect setups and he went a hundred percent in this dude too and

[00:07:08]
bats to kind of discipline

[00:07:11]
Now, I don't know where you get that from but I'm proud of them

[00:07:13]
That's the kind of discipline you want to be able to

[00:07:16]
In spite of all these big shifts and exciting movements you think you're missing something he was able to sit on his hands and

[00:07:22]
wait for the deal to show

[00:07:24]
Well, I set up saw and take him and he went he went too for two

[00:07:28]
probably Dave fear in here, man

[00:07:31]
Can't say enough good things about what a trader you become. He went from courtesy me out to being a master

[00:07:37]
pretty good stuff

[00:07:40]
Right, you should notice by now to keep adding things every week. You have your flashcards

[00:07:44]
Some of you gave me gave me handle last week. You can't remember

[00:07:48]
To me out up and down and then you wrote back said never mind. I wasn't even looking at my flashcards

[00:07:53]
All right, well look if you don't have your flashcards

[00:07:57]
You have to mark up the four hour chart and you have it taking your TDI only trades

[00:08:01]
If you haven't worked the big boy, don't your movie average only

[00:08:06]
If you haven't worked on the pivot points and review the recording used to I low market the blue tracer

[00:08:11]
A yard

[00:08:12]
Come on. Let's do it

[00:08:15]
These are the things you have to do if you're struggling in the business and you can't check off every single one of those things on the list

[00:08:23]
You're failing yourself

[00:08:26]
You're letting yourself down. I have taken the segments that you need and broken them down for two hours a week for you guys

[00:08:32]
If you don't do

[00:08:36]
The two hours a week and then some homework or I'm sorry research and development R&D

[00:08:42]
That's what's causing you not have to success that you deserve in this business

[00:08:46]
It's never too late to roll up your sleeves

[00:08:49]
Here it is May's almost over we're down the home structure may begin into a holiday weekend in bandage June

[00:08:56]
The gear top over

[00:08:59]
If you haven't got what you wanted from me

[00:09:05]
I'm telling you it's not too late. I'm giving it to you

[00:09:08]
Get back in there roll up your sleeves do some R&D look at these recordings

[00:09:15]
You know Jim Knickers and wrote something pretty interesting to someone on the forum and I think the question was is that a lot of

[00:09:22]
town is that demo is that you will never out on remember the question

[00:09:26]
But here's the deal stop focus in I

[00:09:30]
Got a money got a money got to make money

[00:09:34]
So I'm UK to the can your visit presentation

[00:09:37]
He talked about the process

[00:09:40]
The business is about mastering the process the money will come

[00:09:45]
This is gonna go see I got money right now. We guess what these struggle with me in January

[00:09:50]
It's almost June

[00:09:52]
If you would have focused on the process for the last six months

[00:09:56]
You'd be making money now instead of in there trying to trade trying to trade trying to trade not seeing it and cursing me out like they used to do one to your breath

[00:10:07]
Okay

[00:10:09]
It's never too late to roll up your sleeves and get it on

[00:10:15]
All right tomorrow is a new game for out of us

[00:10:18]
Stocks in the week I

[00:10:22]
Can't tell you enough the tools are here man

[00:10:27]
How can one sooner be fairly visibly and one student bang an out 250 grand a week knocking that beat

[00:10:34]
The differences you do in the work I promise you the guys bang it up those numbers have done the work

[00:10:42]
Okay, they made a boot camp before I even invented boot camp they were doing looking

[00:10:47]
TMI I'm not gonna charge doing the homework. They were doing the things necessary to get here, okay?

[00:10:56]
All right takeaways if you already know

[00:11:01]
You should have a deeper understanding of how the deal behaves

[00:11:06]
So let me say how to use the average TMI other things I just listed

[00:11:13]
All right

[00:11:15]
Okay, so I mean you didn't know I can't believe she snuffed that in there pretty sneaky

[00:11:20]
Tame my co-op there, man, and Heidi when she did this live show if she snuck a little birthday cake in there for my

[00:11:26]
Slosh I don't know it was in there. Maybe small. Okay, here we go. Here's the lesson

[00:11:31]
Thank you guys. Thank you. Thank you. Thank you. I'm old today

[00:11:38]
Thank you. I'll be appreciated

[00:11:41]
The best birthday present you could give me is success

[00:11:47]
Yeah, I'm a tourist right on the end if you guys have success that's the best present for me, man

[00:11:55]
Thank you some of you sing really well all right come on

[00:11:59]
Okay, here's what we're gonna talk about for the next hour

[00:12:02]
Track King patterns fuel structures behavioral analysis

[00:12:06]
We're in the eyes of deals behavior. We're gonna look it and break down

[00:12:14]
Disstructures that set up a high low to the day

[00:12:17]
okay

[00:12:21]
Okay, I could make your track moves

[00:12:24]
half a bad man

[00:12:26]
okay

[00:12:28]
Some of you see it in here some of you don't for those of you that are new

[00:12:33]
Outside to the high human rolls over

[00:12:37]
But half a bad man that's what happened bad man is where the ear

[00:12:42]
forms a higher low of the day

[00:12:45]
And then you burn it half a bad man is the opposite to the downside forms below of the day

[00:12:50]
This forms the high of the day

[00:12:54]
Okay, the ear this is the high of the day to deal with goes back

[00:12:58]
You can solidate off of the head and rolls over shifts his own away from the traders that is a half a bad man

[00:13:06]
Okay, so let's talk about this for a second

[00:13:10]
The definition of a half a bad man

[00:13:14]
But deal with a spike the high or low as a means to set it for the session or the day

[00:13:21]
Okay, the viewer is now trading off of that level

[00:13:26]
It's pretty fun and anything else go on today

[00:13:28]
The dealer is now trading off of that level as an outside structure

[00:13:37]
Okay, you will not repeat that level again

[00:13:42]
If he does you will allow some type of profit-looking by the traders

[00:13:48]
Price appears to roll off of the level and the trend is now underway

[00:13:52]
That is the true definition

[00:13:55]
of a half a bad man

[00:13:57]
And every time you see that set up Friday you then and then and then and then that's the best which you should be thinking to yourself

[00:14:05]
Okay

[00:14:07]
Here's a couple snaps off of what it looks like

[00:14:13]
Okay, exactly like a this explain the deal makes a vector

[00:14:18]
Okay, he comes in you can solidate or

[00:14:24]
Accumulates in this area, right?

[00:14:26]
You know what I'm showing my second salvation. It's the same as accumulation. Those those two synonymous

[00:14:32]
consolidation and accumulation is in essence he's consolidating his book

[00:14:37]
Okay, so he makes his vector move

[00:14:40]
He sets the high of the day right here. He pulls off of that high now. He's like, okay

[00:14:46]
Well, I got do I got?

[00:14:49]
Two trillion long one trillion short. I got to punish the longs

[00:14:55]
By snatching the mark in the way for them or do I have three trillion short one trillion long?

[00:15:01]
Do I have to correct?

[00:15:03]
He's consolidating and accumulating his book. He's trying to see where the numbers that he was told he asked to achieve

[00:15:12]
So once the numbers or where they're at the balance

[00:15:16]
He does not want to go back because if he goes back

[00:15:20]
He's going to release the higher level long holds that are here. So he quickly shifts his own away

[00:15:28]
from that area

[00:15:31]
Okay

[00:15:33]
So understanding the inverted half of that mean is the same thing this way

[00:15:39]
No, that was an end. Let me do that

[00:15:43]
There's some more on my mouse man. I'm having a little to David. All right, look

[00:15:47]
The inverted half of that man is this

[00:15:50]
Where he sets the low of the day

[00:15:53]
This is the factor coming in here

[00:15:58]
Right your entries in here in the consolidation when the low has been established

[00:16:03]
for how long

[00:16:05]
30 to 90 minutes of two hours to deal or holds the level and

[00:16:09]
Sometimes he'll take this into the next day

[00:16:13]
All right

[00:16:15]
And where we'd have a bad man same thing

[00:16:27]
Okay without my super drawings on there

[00:16:31]
You

[00:16:36]
Yeah

[00:16:38]
Back man, okay, shift his own way now notice something in the picture blue tracer baby

[00:16:46]
The dealer half of Batman right above the tracer to catch the breakout trade is that take the break

[00:16:54]
Plus the clothes, right? How many people open right there?

[00:16:57]
All right, they took that trade one right there break plus the clothes

[00:17:03]
And they never got what they wanted how many candles the highest set one two

[00:17:09]
three

[00:17:10]
four

[00:17:11]
Five the dealerships away one hour 15 minutes after the high is locked

[00:17:18]
Okay

[00:17:20]
The dealer never comes back to the high that is the definition

[00:17:24]
a

[00:17:25]
Half a bad man

[00:17:27]
Day and bird it same thing

[00:17:29]
He throws an extra spike right there remember I told you he'll push it 15 to 20 trips push it 15 to 25

[00:17:36]
It's half it five to 10 pips open the spread to reach the world at level

[00:17:41]
consolidate or accumulate

[00:17:45]
Above

[00:17:48]
The low wants established

[00:17:53]
Again, he betters in different okay, he does one

[00:17:57]
He taps here to and then he goes down to three here

[00:18:01]
And then he just barely breaks it right there

[00:18:04]
Okay same thing the consolidation off of the low

[00:18:09]
Should be the pending on the pair 15 to 25 pips

[00:18:16]
Okay, the deal will consolidate off of the low or the high

[00:18:23]
15 to 25 pips pound me in

[00:18:26]
GBCHF about 50

[00:18:31]
We'll make an aggressive move and get off the number don't get off right they got the traps here

[00:18:37]
Trade is struck in here. They'll get off the number and consolidate a

[00:18:41]
Good distance 15 to 25 on average the highest 50 on some of the crosses, okay

[00:18:51]
All right

[00:18:54]
Next slide

[00:18:56]
Same things looking at it again variations on the theme

[00:19:00]
The half of that then the deal does not come back and make an M formation. He will not come back for the second leg

[00:19:07]
But in his a trap setup he might even make a mild stop hunt that does not exceed the higher lower the day or higher lower the session, okay?

[00:19:19]
Understand that

[00:19:21]
All right, I got I got a comment on this slide. How are you so proud of it?

[00:19:25]
It's a she found an and made out of a spider web which is a trap

[00:19:29]
I thought that was awesome can't do much more better than that program right again an and spider web for you guys

[00:19:37]
All right, I think it's it let's talk about the information

[00:19:45]
Okay, here's the physical definition to the end

[00:19:50]
The end is an aggressive move by the dealer to set the high of the day. Here's a new term for you or the HLS

[00:19:58]
high of the session

[00:20:01]
Okay

[00:20:03]
A lot of comments and emails you guys get confused when the deal comes back in New York and extends the higher

[00:20:08]
It extends the low and if you're trading one then you get confused. So what I'm telling you is that

[00:20:14]
There's a high of a session high of the Asian session, which is the market maker spread the deal

[00:20:20]
It's what it's that session high the Asian range and sets a new high for the London a lot of times it would be the high or low with the day

[00:20:28]
But sometimes the deal it could make a wider swing during New York and extend for the session the high or the previous low

[00:20:36]
Okay, understand

[00:20:38]
So the grass is moved by the deal with the impact and aggressive move by the dealer to set the high of the day with a high of the session

[00:20:46]
The first leg rise induces trace to take long

[00:20:50]
What is it what is the graph breakout traders?

[00:20:53]
That it grabs the breakout traders

[00:20:55]
So the first leg of the rise induces traders to get wrong especially if it's coming out of the Asian Asian blue box, right?

[00:21:05]
The center of the end this piece right here

[00:21:10]
this piece right here

[00:21:12]
Okay

[00:21:14]
triggers

[00:21:17]
The stops and gets the trades to stop and reverse to a short position

[00:21:21]
So he makes the aggressive move up he pulls back quickly. What happens anybody that got long?

[00:21:28]
from the breakout

[00:21:30]
that

[00:21:31]
puts their shop in here in this area

[00:21:36]
Well, guess what they're stopped out because there was telling you use a tight stop and you want to lose any money

[00:21:42]
You want to lose as little as possible, right?

[00:21:45]
So you put a tight stop below the entry candle and when the dealer pulls back to make the I don't know

[00:21:50]
That's called the apex or not whatever it's called when he comes back to make the center of the end

[00:21:55]
He's triggering the stops and inducing people to turn the other way

[00:21:59]
Okay, then he goes back up

[00:22:02]
near the high

[00:22:05]
And pulls back the second leg rise triggers the stops of the people that cut short in here

[00:22:14]
Okay, second leg rise. This is way one of the M like two of the M formation

[00:22:23]
The second way rise triggers the stops of anybody that got short and makes them think man

[00:22:29]
I should have got long I should have stayed long

[00:22:32]
It's an aggressive confusing move

[00:22:37]
Very important point right here

[00:22:40]
The second leg rise

[00:22:43]
Can be slightly above the first but must close back below

[00:22:48]
Within 30 minutes

[00:22:51]
All right, I should write them all in there. It's important. I forgot to write it

[00:22:58]
Okay 30 minutes, I'm gonna write I'm gonna change the slide

[00:23:02]
Let me a second

[00:23:10]
Okay

[00:23:12]
All right 30 minutes

[00:23:17]
Save it and we're back in business and we'll let's back up. Okay, so look

[00:23:23]
Here's what I need

[00:23:26]
And then the webinar did it you can't see it. All right, there we go grab my pen

[00:23:35]
If the dealer is right here at the high of the day

[00:23:39]
And he spikes this right above he's got to come back below that number within 30 minutes

[00:23:47]
45 minutes tops

[00:23:49]
Here's why

[00:23:51]
If he stays above the previous high or a high of the day

[00:23:57]
He is gonna extend that high to the next level strike zone 25 to 55 higher

[00:24:05]
Okay, why

[00:24:07]
Has it behaved here? I'll stay above the previous high

[00:24:12]
Means that he grabbed some volume down in here that you need it

[00:24:21]
Okay, the business is about taking your money

[00:24:24]
If the dealer has shifted above the previous high and pulls above that level

[00:24:30]
He will extend

[00:24:32]
To the next level strike zone 25 to 55th out

[00:24:37]
So now

[00:24:39]
You're in a trade you wait 30 minutes the dealer is consolidating above and you're like man

[00:24:46]
I'm down 10 picks my stop is 23 away having gotten hit yet the deal of just close above the previous number

[00:24:54]
previous high of the day what are your options?

[00:24:58]
Give the deal over the other 15 picks

[00:25:02]
Or scratch yourself out because you know better and

[00:25:06]
Look for another entry 25 to 50 pips higher

[00:25:12]
Or

[00:25:13]
Scratch yourself out and find another pair that's behaving the way you need it to behave

[00:25:18]
If the dealer can't say enough if the dealer extends the high

[00:25:23]
above the previous high

[00:25:25]
On the second leg formation and stays above that number. He will rise

[00:25:31]
25 to 50 pips for next level strikes them

[00:25:34]
As soon as I say you won't do it, but I'm telling you 90% of the time

[00:25:40]
The money he was seeking wasn't achieved and he'll say all right, you don't believe it's wrong

[00:25:44]
Let me show you long buddy and her price to the next level

[00:25:48]
Okay, he must come back a little previous high first leg

[00:25:53]
He must come back a little the previous side within 30 to 45 minutes. So what does that mean? We can get an M pull up

[00:25:59]
You can get a set of railroad tracks right here

[00:26:01]
And you can get a doge add in the middle evening start formation and then the deal must come back below and

[00:26:10]
close below

[00:26:12]
That number in 30 to 45 minutes 30 minutes is a good rule

[00:26:19]
So yes the answer the question is is you got to give him the opportunity to make some railroad tracks

[00:26:25]
If he goes up where goes up solid green it comes right back red and close this below

[00:26:31]
That's a good valid information. He does this right you're right here

[00:26:37]
And he goes like that band comes right back below in 30 minutes

[00:26:41]
You got it. You're still good. That's a valid information and you probably will see divergence on TDI to help you spot this

[00:26:48]
Why because he's spiking up and he's pulling back and the closes are lower

[00:26:54]
He's averaging lows of lower closes, but prices may be one more swing high, which is what stop hunt

[00:27:00]
That's why we understand our herds and stiffens everybody else divergence is the act of triggering the stops

[00:27:07]
With closing below a level and since TDI RSI mine tracks the closes

[00:27:16]
So I heard it's a spot it

[00:27:18]
Okay, because we base TDI on the closes and price we spike up and spike back down to close lower

[00:27:25]
You're averaging the closes on TDI, okay? All right, so

[00:27:31]
The move triggers the stops of the traders have taken short positions off of the first leg and grabs any breakout trades that

[00:27:37]
Appendings waiting there. That's how the end is formed a

[00:27:41]
good information

[00:27:45]
Will consist of a minimum of eight bars a

[00:27:48]
Nice pretty one will consist of a minimum of eight bars now I mentioned you before my friends I need

[00:27:55]
I hope he's doing okay. I haven't seen him. He's having some family issues and health issues. I hope you're okay. I'll be fine

[00:28:00]
You can hear me

[00:28:03]
He's one of those guys. I said Steve your full shit. I don't believe you. I said, okay

[00:28:08]
How are we gonna fix this problem?

[00:28:11]
He has an engineer mind. He's very very technical and he's very very intelligent guy

[00:28:19]
What he did was

[00:28:22]
He took four majors and I'm leaving it how far he went back

[00:28:27]
But he sent the astring to you then that is like

[00:28:30]
397 pages long of every m and w that he saw in euro in pound in Australian and

[00:28:37]
He counted the number of bars in between the successful ones the bail once and

[00:28:42]
And he came back with an

[00:28:45]
M or w that consists of eight bars or more without any other filter is in the high 80 percent

[00:28:54]
Okay, now add the other filters

[00:28:58]
people may should highs

[00:29:00]
spike candles

[00:29:02]
22 trades

[00:29:04]
You understand he just broke down the ends and w's for months and months and months and

[00:29:10]
He came back with a

[00:29:13]
Good solid m or w formation consists of a minimum of eight bars

[00:29:21]
Okay, it's not only for one and it's for formation itself the m or w that consists of eight bars minimum

[00:29:31]
to solve

[00:29:33]
You okay?

[00:29:36]
All right, where are we in the world? Okay, let me give it to this pen and move through some slides. Okay, so let's look at a couple ends

[00:29:45]
All right, here's your informations typical I

[00:29:49]
Want you to notice how

[00:29:51]
the dealer

[00:29:54]
Is working the blue tracer on this example

[00:29:57]
Okay, you cannot go back above the high this example

[00:30:04]
But if you spike this candle slightly higher you came right back down and close below all this action

[00:30:11]
It was in 15 minutes right

[00:30:15]
That's what I'm talking about this is wait was a little higher you went up that means you can a little solid green and then in 15 minutes

[00:30:22]
you turned it inside out and

[00:30:25]
Reverse here's your entry

[00:30:28]
Now here's something very interesting. I want you to take note of in this example

[00:30:35]
The dealer has closed below two structures and

[00:30:39]
Created a quasi hammer

[00:30:42]
To help you see the entry anybody want to take a stab at it?

[00:30:50]
Okay, no takers here's what you got

[00:30:54]
The dealer broke a bottle of the blue tracer. Let me raise all this crap

[00:31:01]
The dealer broke above the blue tracer

[00:31:07]
He formed the higher the day

[00:31:10]
Yes, Mary

[00:31:13]
He did his business right he hit all the stops in the air screw everybody up confused them

[00:31:20]
Morningstar continuation all that stuff

[00:31:24]
He then went back by the high and in one swipe

[00:31:29]
He closed below the blue tracer and collapsed inside the mustard moving average only trade here's your hand on the mustard

[00:31:36]
Your entry is right there a closing side the mustard and it closed back below the blue tracer

[00:31:44]
After forming the high today on a vector run straight up at the Asian session at 3 30 in the morning

[00:31:51]
God help the dealer you got

[00:31:54]
Okay

[00:31:55]
To have a state start to tie together the blue tracers coming in with the mustard moving average only stuff

[00:32:00]
The candle patterns forming the information at a certain time during the day working the blue tracer coming back below

[00:32:07]
Making an ad if you took the candles off and took the time to look behind

[00:32:14]
The price action to see the movie averages and just see them by themselves

[00:32:17]
You can see that holy crap. That is the perfect information by every single

[00:32:24]
Okay

[00:32:27]
That's the kind of stuff I want you to see that's what looking at just moving averages the appropriate time will do for you

[00:32:36]
All right good stuff good stuff good stuff

[00:32:40]
Okay next

[00:32:44]
Same thing this is in essence an M formation

[00:32:48]
But it's not a bar

[00:32:51]
When you count to a far as this is borrowing the bar that forms the high by the way

[00:32:58]
Okay

[00:32:59]
If you're looking for the formation bar one is the bar that forms the high of the day or higher this session

[00:33:07]
All right good question that was a very good question

[00:33:14]
Okay

[00:33:15]
Again, what's present right here?

[00:33:19]
Tracer the dealer does the money grab with the pins

[00:33:26]
Okay, in essence what you have

[00:33:30]
It's too free-hand

[00:33:38]
Okay, look at all those pins

[00:33:40]
Pinch go up

[00:33:41]
This candle is solid green all the way to the top

[00:33:44]
It's still closed green, but notice how he closed below the high and he closed below the high on the breast of the candles

[00:33:53]
Break us down in your mind Steve. What the hell's going on here?

[00:33:57]
You know spikes above gravity orders

[00:34:00]
Those back blows is below those up again. It's the stops of anybody that needs to be hit

[00:34:06]
goes the other way gets to stop the other way

[00:34:09]
Okay

[00:34:11]
Okay, comes back one more time to grab any orders that are built in here built up in here

[00:34:17]
Take some out

[00:34:19]
That's when you should be in if you got in here you're good at it stop losses just out of the deal is reached

[00:34:27]
Okay

[00:34:30]
Just had it right here this two hammers with the evening's quasi evening star

[00:34:36]
Probably makes people think it's going on

[00:34:38]
But if this comes in at the tracer at the high of the day you got the deal in maybe you want them

[00:34:43]
Try to get on before he shifts the zone

[00:34:47]
What's the time element here deal or set the high and forgot 45 to 50 minutes?

[00:34:53]
Has worked high

[00:34:55]
How do I know in here?

[00:34:57]
I really don't if we broke this down for a five minute chart

[00:35:00]
We know there's three divisions in here. This might be the first five minutes of rise

[00:35:04]
This might be the second five minutes of rise and then you went all the way up to the top and pull back and end it here

[00:35:10]
We know that they fake those candles out and he probably sat right at the high for four minutes and

[00:35:18]
52 seconds and then right in the last eight seconds snatches down and made the clothes

[00:35:22]
Okay

[00:35:25]
You can

[00:35:26]
Same thing one up there solid green ends up closing down here red

[00:35:31]
That's what you have to be asking yourself. What's going on? What's the deal? We're doing? He's grabbing the money on the other side of yesterday's high

[00:35:41]
validating

[00:35:44]
Any orders of pending that are sitting above there

[00:35:49]
Activating them pull them in snatch them pull them in pull them in pull them in grab all the long holders trigger some some long stops

[00:35:58]
And then shift his own way and say sorry about your day buddy

[00:36:01]
Okay

[00:36:05]
Okay

[00:36:08]
This is the exact example

[00:36:12]
Of what I told you about the 30 minutes, okay, the deal of breaks to the high

[00:36:18]
You works it and the mouse is so weird. I don't know what the hell's going on

[00:36:23]
Just every time I let go of the button. It just keeps dragging

[00:36:26]
I

[00:36:28]
Surely someone tell me I've fixed that but not now I'm not going to do it in the middle of the presentation

[00:36:33]
All right, look what happened here. There's the blue tracer

[00:36:38]
The dealer went up there. You know this thread got opened right here

[00:36:44]
All right, let me talk about opening the spread for a second

[00:36:47]
Some of your dealers don't do it. They're not all doing it

[00:36:50]
So a lot of you will like oh man, I don't see the spread opening up and you're confused by that

[00:36:55]
Like oh, you said the spread opens up, so that's not the higher the day

[00:36:59]
If your deal is being kind and not open in the spread or if the broker is calming that down and he's taking the

[00:37:07]
Open and close and just averaging it in at the high low and not opening his deal in spread

[00:37:13]
And banking for that because those spreads

[00:37:17]
Have a tendency to hit your stop

[00:37:21]
Without warning so if your dealer's maintaining

[00:37:27]
An even spread for you

[00:37:30]
Then it's very nice of them

[00:37:33]
Okay

[00:37:36]
So now

[00:37:38]
Back to our list. This is the example of where the dealer has exceeded

[00:37:45]
The original high today the number that was formed right okay, I don't know. Let's say this was 31 or seven

[00:37:56]
The deal formed the high this is from your big wardrobe

[00:37:59]
31 or seven the dealer forms the high he comes back and spikes it to 31 10

[00:38:05]
Nice to low

[00:38:06]
31 18 he spikes it to 31 18

[00:38:10]
Then what does he do within 15 minutes? He ends on a hammer closes back below right here

[00:38:15]
Okay, if the dealer had closed above this line right here above

[00:38:20]
Now you got to wait a minute

[00:38:23]
Well, we actually got to wait 15 more if he stays above that for 30 minutes

[00:38:29]
Right it's the opposite he doesn't close back below in 30 minutes

[00:38:33]
It means he stays above in 30 minutes. He will extend that level to the next level strike zone period

[00:38:40]
Remember I told you we're not in the 50 50 business

[00:38:46]
Of course as soon as I tell you this tonight as soon as you go off

[00:38:49]
He's gonna get out and it's gonna correct. It's like I said, but here's what happened

[00:38:54]
Whatever number the deal we're seeking is destroying he didn't get the number

[00:38:59]
So he's hanging out up there above or below whatever if it's at the low. It's a below above it's the highest below

[00:39:05]
We're staying above him. I'm trying myself crazy

[00:39:09]
The deal is holding above the high for a reason

[00:39:13]
He's getting people to induce to hang on breakout traders. He's hanging above the high if he doesn't get what he needs in

[00:39:21]
30 minutes to an hour

[00:39:22]
He will extend the high to the next level strike zone. That's all you need to be concerned about so what I'm telling you is

[00:39:31]
Your family

[00:39:34]
It becomes a gamble

[00:39:36]
Because you're guessing if his book is gonna balance and he's gonna fall back below the high

[00:39:44]
The difference is a

[00:39:47]
Confirmed M or a gambling M that's the difference why not wait for a confirmed and pattern the deal closes back below

[00:39:56]
The blue tracer you make an end in the mustard or he collapses inside the mustard and catch it those are the confirmations

[00:40:04]
That make that a lot instead of a gamble

[00:40:09]
If your goal is to trade large number of contracts

[00:40:13]
You cannot gamble in this business. You will lose your account

[00:40:19]
That's not what I'm teaching. I always say this in today's no exception if you want a gamble

[00:40:25]
Google the nearest Indian reservation that has a casino and knock yourself out

[00:40:30]
Do not gamble with your equity

[00:40:34]
Because the business is difficult enough without taking random shots in the door and getting lucky that is not what I'm teaching you

[00:40:43]
Confirmed ends confirm W formations if the deal of breaks above the level and stage above he will extend

[00:40:51]
That's the rule

[00:40:53]
Is it hard and fast? No, he could correct

[00:40:56]
But why not wait for a confirmation a better pattern, okay? All right

[00:41:03]
Now back to this

[00:41:07]
Yes, the difference between the amateur is a professional

[00:41:11]
It's the way for the right setups the dealer backers to the high we have a number one

[00:41:16]
number two number three four five

[00:41:21]
six seven

[00:41:24]
eight

[00:41:26]
Nine then the dealership's the zone starts his method it starts his work

[00:41:32]
An

[00:41:32]
Information that is eight candles or greater to form which is by the way two hours

[00:41:40]
And if the dealer comes back one more time and nails the stops and closes below

[00:41:46]
That's a pretty damn good end

[00:41:48]
Okay

[00:41:52]
County from when the high is formed eight bars or greater

[00:41:58]
Is a solid information where I got to make it slide for this where the dealer pulls off of the initial high

[00:42:08]
Anybody

[00:42:10]
15 to 25 pits on average and

[00:42:15]
As much as 50 pits before repeating that level again

[00:42:24]
Okay

[00:42:28]
Confirmed solid and of eight bars or greater where the mid section the apex section

[00:42:34]
It's called something the someone looked it up for me was before English professor and I forgot the piece of the end that comes in the middle

[00:42:40]
from

[00:42:44]
The initial high or the high to the low is

[00:42:50]
15 to 25 pits and as much as 50 pits that's a solid end

[00:42:55]
Why?

[00:42:57]
Where do you put your stops where do retail traders not us where do retail traders put their stops?

[00:43:02]
15 to 25 pits in

[00:43:04]
That range they grab a trade they put it seven to ten pips below the entry bar

[00:43:09]
The deal will correct inside the information at the apex

[00:43:14]
Nader and vortex whatever the hell you guys are writing naders to the low. Thank you for it. All right

[00:43:20]
So Ralph when he naders to the low

[00:43:25]
All right

[00:43:28]
He's hitting the stops of the traders that are in here

[00:43:32]
That's what you needed to concern about and notice something pretty cool

[00:43:35]
Is that anybody that got long on this bar their stop is right here and he just he just gives you nothing

[00:43:43]
Okay

[00:43:44]
All right

[00:43:45]
This was a flashcard extent to me. I forgot who sent it when I took it

[00:43:49]
I was like oh, I'll remember that dude and now this is you own up. It's a great great great flash far

[00:43:53]
I'm wanting you to see an example

[00:43:56]
I think I showed this already

[00:43:58]
He told himself the pattern the pattern

[00:44:01]
He talks about short trade part here long trade part here. Yeah, old trades at 50-pits artists

[00:44:09]
What's pretty crazy is that he managed to trade from both sides of the extreme and on a day where there was only like

[00:44:19]
107 pips for 80 are he was able to grab a hundred of them

[00:44:23]
That's sick man that is unheard of in the business people if you saw someone that you're removed a hundred and twenty pips today

[00:44:30]
I grabbed a hundred of it. You'll call you a liar nine out of ten times guarantee

[00:44:36]
Trading in both ways off the high and off the low

[00:44:40]
It's a beautiful thing

[00:44:42]
We're talking about do a trap moves

[00:44:44]
So far we go and happy about made it and we're looking at the W now same thing same principles

[00:44:52]
Okay, the W is no different

[00:44:54]
The W is exactly the opposite of the information

[00:45:03]
It's an aggressive move by the deal of the settle low of the day or lower the session

[00:45:09]
Now people talk about risk appetite and volatility

[00:45:12]
That usually comes in when they're forming the higher low of the day. That's the stuff that scares people

[00:45:18]
They don't understand what's going on

[00:45:20]
It's the same thing the first like correction induces trades to take short positions the deal it comes out of the box out of the Asian range

[00:45:30]
gets the ball rolling

[00:45:36]
Right he's in here screwing around and all of a sudden he was banned

[00:45:41]
That volatility or excitement or whatever you want to call it starts the action for the one-in-session

[00:45:48]
It usually forms leg one of the emeraldo information

[00:45:54]
That's what we call vector three to the low deep pumps below or it stands below in three moves

[00:46:00]
I covered that a few

[00:46:03]
recordings back if not it's in the class how to hit it goes back and works that level

[00:46:10]
Okay

[00:46:14]
Once the low is formed

[00:46:18]
Now I think this is gonna be the apex right he pulls back and forms the apex

[00:46:23]
But understand the center of the structure triggers all the stops you get traders to stop and reverse long

[00:46:29]
Right anybody that went short pulls back it's the stops get some three bursts and then he pulls back again

[00:46:36]
The second leg of the correction

[00:46:38]
Can be slightly below the first but must close above how fast anybody

[00:46:46]
Come on, just question

[00:46:48]
Really tight that slow there you go. Thank you Jack Kevin. Thank you. Hey, there you go

[00:46:55]
Coke having another coat. That what you talking about

[00:47:00]
Tanya element tiny element

[00:47:02]
Not pickle it no not picks. Tiny

[00:47:06]
Okay

[00:47:08]
He must close back and forth

[00:47:10]
In 30 minutes 45 max

[00:47:14]
There you go, Coke. Thank you buddy. I don't know. I know what we see

[00:47:21]
90 minutes is too long 30 to 45 minutes back above the previous low

[00:47:27]
The deal is got to come back above this number, right?

[00:47:30]
He's got a spike it or allowed him a doji in there and then some railroad tracks

[00:47:37]
Because when he stays down he induces people to go short

[00:47:44]
Okay

[00:47:46]
Then you're gonna run

[00:47:48]
Format the other piece of the debit all right, so if you extend the second leg below the first which means that the number on the board will change to this number

[00:47:59]
He's got to come back above this number

[00:48:04]
That number 30 to 45 minutes, okay

[00:48:09]
That's what I'm talking about

[00:48:12]
Same thing I said on the information

[00:48:15]
The second leg correction will not go below the first if their orders built up there

[00:48:18]
He's not just gonna go down there because he's bored. He wants to trigger the stops

[00:48:23]
That's why he goes down there to trigger the stops. It's quick and he comes right back up

[00:48:27]
He's got nothing to do down there except collect stops. He's already induced enough traders to go short

[00:48:33]
So my spiking down and coming back above the hits to stops

[00:48:39]
picks up the pending with doesn't allow anybody to book a profit

[00:48:44]
Okay

[00:48:46]
If he stays down there, there's some type of profit-looking

[00:48:50]
So that means the bigger target

[00:48:53]
It's not acquired. Okay. Look. That becomes in goes back. He's here. He's looking at it looking at it

[00:48:59]
He analyzes here's your number right here. Whatever that number is and he's like, yeah, shit

[00:49:05]
There's some money down here. So he goes like this. No, he'll say there's some stop. Oh, what's yours down there?

[00:49:09]
Lost water than it go bam bam from right back above

[00:49:13]
He has to come right back above if he does that then that validates that this was in fact the stop hunt

[00:49:21]
Okay, if he stays below

[00:49:26]
Then you got to change your mentality the apex was the stop hunt and he's gonna continue down

[00:49:32]
Okay

[00:49:37]
It's about his behavior that gives you the clue which way he's gonna go

[00:49:42]
There's some number of pending orders and stop loss orders which are pending as well

[00:49:47]
Built up down here and he's such a greedy bastard. You can't stand it

[00:49:51]
So he comes in and 30 to 45 minutes and spikes them hits it and pulls away

[00:49:59]
Okay

[00:50:02]
There you go

[00:50:04]
Yes, I do need to add that to this lot as well. Thank you

[00:50:12]
All right, where we at secondly must be slightly below the vertical most goes above within

[00:50:19]
32

[00:50:21]
45 minutes

[00:50:24]
All right, say it like that. I'll go back to see a little later. You got any time for this right now. We're busy. All right

[00:50:31]
Same thing he's triggering the stops of the trader that taking long positions off of the first light whoever sees the first leg

[00:50:41]
And gets excited and acts hastily

[00:50:46]
He's coming right back hitting the stops and doing that now the exception is to have a Batman

[00:50:52]
Why because when he made the trap move on the ear he got what he was seeking so he doesn't have to come back and trigger anything

[00:50:59]
He's got it

[00:51:01]
Usually half of a Batman I

[00:51:05]
Need to make this no to half of a Batman higher low will come after the grasses move and

[00:51:11]
He will in essence shift the zone without going back. So let's say there's been a big drop in euro

[00:51:18]
He makes the half a Batman to the downside and rolls back long

[00:51:22]
He already had everybody thinking short. There was enough volume in there that he's like my book is good

[00:51:27]
I hit the number and a ball that I was told I needed

[00:51:30]
There's no reason for you to go back there and brisk giving some of that money back

[00:51:34]
Getting opening my hands so to speak while the people that take it away take it back, okay?

[00:51:40]
I made a note of that one paper. Okay, so here's a big beautiful structure

[00:51:46]
This is one of those those that is slightly bigger than eight barbs

[00:51:52]
Right he poured a hoods

[00:51:57]
On both sides with just enough to trigger the stops

[00:52:02]
Here and here this is one of those big structures

[00:52:07]
That you know is gonna pay out right the distance from here to here is how much?

[00:52:13]
Anybody

[00:52:16]
All right fashion you guys 15 to 25 up to 50 yes

[00:52:22]
Up to 50 any on the pair

[00:52:29]
Think about this for a minute you see this developing you draw a line right here

[00:52:34]
Okay, that's your

[00:52:36]
Intraday dare I say it I won't say it's below it's not supported below you draw your line right there, right?

[00:52:44]
The deal it pulls back aggressively he comes all the way back down and he turns flat

[00:52:49]
And he just spikes it with one pin and slightly trades off of it in program hour look one two three four five six

[00:52:58]
He's working the love to work in the low he's working the love

[00:53:02]
And then look what does he do? He's just the zone and it's over off the graces

[00:53:07]
He's got him. This is a big beautiful W

[00:53:12]
It's kind of crazy because it's got a W in a W in the

[00:53:15]
Moving average look right here. There's a W

[00:53:19]
And then there's that's what there's a W right there too

[00:53:26]
That's a double W trade no we don't have that okay, but look look at the distance in here look at that

[00:53:34]
Gaff what you have to understand

[00:53:36]
You guys send me some pictures and you get like a candle gear and a candle gear and a candle gear

[00:53:42]
You go see that so that much like that

[00:53:44]
You know what sometimes it won't sometimes it does it but I want you to understand the difference between a structure like this

[00:53:52]
And the structure like this there's a huge difference in those structures

[00:54:00]
They understand same thing on the air man I

[00:54:06]
Know there's a W in here and you could have grabbed this maybe off the US session

[00:54:09]
Understand that when he comes back to that level and he gets the stops on that level

[00:54:15]
Right here's the low I

[00:54:17]
Can't draw straight signal like the look

[00:54:20]
You know the spray about why in a little bit and he grabbed just like he needed right there

[00:54:25]
When he does that and he stays again off of that level you got him

[00:54:29]
There's only one direction look. Let's talk about some things that are telling on this chart right up the back

[00:54:35]
Okay

[00:54:36]
Look at this look at this right here

[00:54:39]
Holy crap there's a mile and a half between the averages

[00:54:42]
Okay, what does that tell you I don't have to look at another chart

[00:54:46]
I could walk up to this chart and tell you that prices been falling for at least three days

[00:54:52]
Right right up the back

[00:54:55]
Hello, it's right can fall it least three days. See how do you know the answer to that? Are you clear boy?

[00:55:00]
No the separation from doing the average only trades and understanding the separation between those averages

[00:55:10]
Tells me that in order for the 50 to cross the 200 and to get separation on it

[00:55:15]
You got to be dropping for two and a half three days maybe four days

[00:55:19]
Now what behavior is this my friends?

[00:55:25]
Right on Danny level three

[00:55:30]
Okay, so if I showed you a flash part of this right here you look at that and you go

[00:55:37]
The lowest and formed

[00:55:40]
The lowest and formed there's a ton of separation between the moving averages the dealer made the apex back towards the water and pulled back again

[00:55:48]
That looks like some level three ship that Steve told me the dealer is in the stops

[00:55:53]
You hit the stops one more time if you walk up to this chart in this section right here and you don't go along

[00:55:59]
I'm gonna come over your house and hang in myself

[00:56:01]
Okay, what are the clues moving average separation level three erratic behavior space between the apex off of the low

[00:56:14]
Right all these things down in

[00:56:16]
W in the averages starting the form the average is starting to pull together and collapse the distance between here to there

[00:56:25]
Right those are the things you're supposed to be looking for possibly divergence on the TDI or

[00:56:30]
the RSI line

[00:56:33]
More than eight bars there's a lot of crap on that chart isn't there it's not just some candles paint on a gray background

[00:56:40]
The W's in the mustard right you got to go check this out. You got you got this little baby W

[00:56:46]
You got this quasi baby W there you got this W

[00:56:51]
You understand that's a set up

[00:56:55]
Big monster mustard you W

[00:56:58]
With the second leg is higher than the first

[00:57:02]
And the only

[00:57:04]
Variations that the deal and trigger the stops right there now it might confusing because when he goes down there he's that it's solid red

[00:57:11]
But he doesn't close below the first set of numbers, right?

[00:57:15]
The entire business is about the high and the low and how the dealer hands those areas on the chart

[00:57:23]
If you saw this and you were an amateur you go see risk appetizers into the market

[00:57:28]
It's quite volatile. I believe I'll stay on the side for the afternoon

[00:57:33]
And then I'm gonna beat you myself

[00:57:35]
That is the perfect behavior of the dealer

[00:57:42]
And how he sets everybody up to go the wrong way

[00:57:48]
Okay

[00:57:51]
And I get on a higher time frame you have

[00:57:55]
Same thing with the tracer

[00:57:57]
Beautiful set of railroad tracks look

[00:58:00]
The dealer comes in the afternoon he steps below

[00:58:04]
He pulls back and makes a beautiful move

[00:58:08]
Okay, here's what happens with this trade

[00:58:11]
Steve the railroad tracks are too big my stop loss has to be 35 pips. I don't like that

[00:58:18]
Okay

[00:58:20]
If you take one lot

[00:58:25]
What a 15 pips stop

[00:58:28]
Is the value of that stop loss the same as if you took five minis with a 30 pips stop loss

[00:58:37]
answer yes

[00:58:40]
So what I'm telling you is that that shows up and you don't take it because the stop loss is too big and

[00:58:48]
If you don't cut your lot size in half and stretch the stop loss out it's same on you

[00:58:57]
Okay, you understand what I'm saying if you normally are one lot trader and said Steve this is 30 pips distance on my stop

[00:59:04]
It's too big

[00:59:06]
Why could you take this to a point five and

[00:59:09]
Use the 30 pips stop loss right there

[00:59:14]
Understand the trade takes a little heat

[00:59:17]
Goes right into profit

[00:59:21]
Okay

[00:59:25]
If the volatility I'm sorry if the risk appetite and volatility is so deep that you

[00:59:32]
Feel like you should pass and this set up is staring you in the face the deal of railroad tracks right to yesterday

[00:59:38]
Glutrates are yesterday's low and he closes right back above and how long anybody

[00:59:43]
He comes right back above in 30 minutes 15 minutes really

[00:59:49]
Yes 30 minutes or less or it's free like a pizza

[00:59:54]
Think about that when you're trading 30 minutes or it's free

[00:59:57]
Becomes back above it is free free money juris for the taking

[01:00:04]
Okay

[01:00:05]
So cut your lot size in half or three quarters to accommodate the risk percentage in your

[01:00:12]
account if you're a two percent trader and this trade comes in at three percent

[01:00:18]
Scale back in the number of watts to make this a two percent risk trade, but take it because it's a good structure

[01:00:27]
This

[01:00:29]
Is almost as good as me writing you a check

[01:00:35]
See you in the right shape check with

[01:00:39]
Probably not gonna happen

[01:00:41]
All right

[01:00:44]
Another W variation on the theme of France

[01:00:48]
One while it's a sink close again this one two three and then he nails it

[01:00:58]
Comes back

[01:01:00]
outside structure

[01:01:02]
The dealer has worked big aggressive moves to the low

[01:01:11]
For about 30 45 minutes and then he starts to take off

[01:01:15]
But this in essence

[01:01:21]
To go yeah, it's half a batman I think the slide actually came out of sync. I'm no more. I feel I got a beater

[01:01:27]
I'm kidding. All right. Look. Here's another W

[01:01:30]
one

[01:01:31]
two

[01:01:33]
Read it below a nice move coming down

[01:01:36]
Okay, it pulls back

[01:01:39]
How many bars does anybody one two

[01:01:44]
Three four five six seven eight at least right this is a nice value formation look at them look at the mustard W

[01:01:52]
Okay, right out of Asia

[01:01:58]
Okay

[01:02:01]
Only rates to slide I guess I can't do it when I'm in there that's like shouldn't be there. Okay, so now

[01:02:09]
Right now get rid of that all right

[01:02:12]
Okay, so formation star patterns. Okay, so far where we at and W half a batman

[01:02:20]
Aggressive moves towards the high dressing move towards the low risk appetite when you're hungry to lose as entered the market volatility momentum

[01:02:27]
Whatever the hell they call it they're wrong

[01:02:33]
Okay definition for star formation

[01:02:36]
Simple easy to understand

[01:02:39]
Evening star mowling star

[01:02:42]
It's just an extra 15 minutes for the market maker to take your money. That's what it is

[01:02:52]
All right

[01:02:56]
Where we're tracking since the 30 minutes 15 and 15 out

[01:03:01]
Right 15 in

[01:03:04]
15 out

[01:03:07]
The deal will throw the star formation

[01:03:10]
He gets an extra 15 minutes to screw around you

[01:03:13]
Right here. This is 15 minutes

[01:03:15]
What happens when you see the link like that? This was green

[01:03:20]
What happens on the five-minute traders they get three 15-minute divisions, right?

[01:03:28]
So what happens he goes above the high

[01:03:31]
He stays above the high and probably in the last five minutes he pulls all the way back turns it inside out

[01:03:36]
Makes a low close, but what did he do in essence he closed the low?

[01:03:41]
The previous number high within 15 minutes and then he shifts the zone away

[01:03:49]
From those traders immediately

[01:03:51]
Anybody that's trading one minute five minutes all the candles got jacked up in here long they're in trouble

[01:04:01]
This formation

[01:04:04]
Does not matter

[01:04:07]
Okay, this formation does not matter it could be it could be this

[01:04:13]
It could be a spinning top

[01:04:18]
What matters is this right there that's what matters the next 15 minutes

[01:04:23]
Okay, here's what I mean

[01:04:26]
If the deal it throws a hammer evening star moving star orange hearts blue stars green clovers. I don't care

[01:04:32]
I want to see he does in the next 15 minutes

[01:04:37]
Because in essence

[01:04:38]
He's made a railroad track for me. We're an extra 15 minutes. He's made this

[01:04:45]
He's done this right that could be did the only difference is he hung around 15 more minutes for the little tiny baby right there

[01:04:58]
And he can

[01:05:00]
Or cannot extend the high or low with that

[01:05:05]
Activity he does that

[01:05:07]
You still don't have a trade right here. This is nothing you have leg one and an a star formation

[01:05:13]
It's the next candle that's telling in this structure the next candle that's telling in this structure tells you

[01:05:22]
What he's gonna do how do you know he closed back below?

[01:05:27]
The previous highs

[01:05:30]
He closed below this high and this high within 15 minutes

[01:05:37]
The hey girl analysis or analyzing the deals behavior at the high and at the low

[01:05:43]
Okay, extra 15 minutes to take your money. There's the example of quasi-roar tracks

[01:05:49]
They look

[01:05:53]
Okay, start of the day to deal or tap the highs just to down he then consolidates at that level. He has some mill retract here alone

[01:06:03]
Okay, he spikes down

[01:06:06]
Right, we could say he extended the age and low maybe one

[01:06:10]
two and then tap on the three he hangs around for 15 more minutes and

[01:06:17]
then in 30 minutes

[01:06:20]
15 15 he takes back the exact amount

[01:06:25]
These two handles

[01:06:28]
Equal the body of this candle see that it's important

[01:06:33]
confirmation

[01:06:35]
This candle

[01:06:38]
Is equivalent to the length of these two candles

[01:06:41]
If you stack them on top, they're almost the same. I know this the stock runs a little lower. We'll move this candle over there

[01:06:50]
terrible artist

[01:06:52]
They're about the same

[01:06:54]
That in essence is a railroad track broken in the four pieces

[01:06:58]
We're a spike down vector evening star 15 minutes. I need some more money and greedy bastard and then pull away and two

[01:07:05]
Okay

[01:07:11]
Understand that this

[01:07:13]
It's a star formation, but it's an essence broken down railroad tracks which gives you an extra entry and earlier entry
