# V16 — TRANSCRIPT

## ⭐ TIMESTAMP CONVENTION — STATED ONCE, AT THE TOP (`V14_REVIEW_R1.md` GATE, open item 173)

**Every `[HH:MM:SS]` in this file and in every V16 artifact is the committed marker grid of
THIS file — the 377 markers below — and nothing else.** An independent ASR pass was run this
session (VERIFICATION §5) and **its clock is never cited**; where it arbitrates a word, the
correction is attached to the *marker grid's* timestamp, not to the second pass's.

**The marker grid and the player's burned-in timecode are the SAME CLOCK, and here the sweep
offset was MEASURED AT ZERO at ten points rather than argued.** See `04_SCREENSHOTS/V16/INDEX.md`
§0 for the full `SWF_CAPTURE_RECIPE.md` §8a table. Screenshot filenames carry the player timecode;
because the clocks coincide, a screenshot name and a marker are directly comparable and **no
conversion is used anywhere in this artifact set.**

Corroboration at four content points where a printed slide changes on a sentence. **Quotations are
verbatim from the marker grid, ASR defects included:**

| Marker | Transcript line, VERBATIM | Slide change, burned player timecode | Δ |
|---|---|---|---|
| `[00:14:23]` | *"At the moment open, if the dealer breaks high,"* (ASR; see correction **#1**) | `London Session Start / 2:00 To 3:00 AM, EST` at **14:25** | +2 s |
| `[00:17:53]` | *"it's that M3 and M4"* → `[00:18:01]` *"are possible day highs"* | `M3 And M4 Are Possible HODs` at **18:00** | −1 s |
| `[00:27:36]` | *"Pivot points are essentially if you haven't figured out. They're an"* → `[00:27:44]` *"ADR grid that's fixed."* | `PP Are An ADR Grid…` at **27:45** | +1 s |
| `[00:35:03]` | *"Find the expected high and low for the day on six majors using pivot calculations."* | `R&D` homework slide at **35:05** | +2 s |

Slide-change granularity is the 5-second sweep grid, so ±5 s is the measurement floor. **There is
no systematic offset between the two clocks.**

---

## SOURCE

| Field | Value |
|---|---|
| Video ID | **V16** |
| Original filename | `Bootcamp1 Wk7 050612 Part2 (45mins).swf` |
| SHA-256 | `ecac17c41700839beb4091de94b61fe0cb5a4922e9de764ad482eb8d318c538a` — verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session on the flat `Bootcamp/` canonical path, **and re-verified after the frame-rate patch** to prove the original was not modified (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| Duration | 00:44:35 (audio measured **2675.826939 s**; SWF header **8,029 frames ÷ 3.0 fps = 2676.333 s**; `SOURCE_MANIFEST.md` 00:44:35 = 2675 s — **three independent figures agreeing to within 1.33 s**) |
| Lesson title | ⭐ **PRINTED, AND IT IS A REAL TOPIC TITLE.** The opening slide reads `Pivot Points` over *"How to Project High and Low / Intra-Day Support and Resistance / Possible Trading Range"* (`V16_00-00-20_…png`), and **every slide from `00:00:15` to `00:34:55` carries the running title `Pivot Points`**. The quarantined per-lesson header's *"Primary Topics: Steve Mauro Beat The Market Maker (BTMM) Methodology"* is a generic non-answer, and its `RULES.md` / `VISUAL_INDEX.md` are fabricated — see `QUARANTINE_REGISTER.md` **Q-017** |
| Session date | **2012-05-06**, from the filename `050612` and `SOURCE_MANIFEST.md`. ⚠ **NOT corroborated from inside this file.** V16 states no week number, no date and no session number anywhere in 377 markers — `week` returns two hits (`[00:20:20]` *"three week pushes"*, `[00:23:24]` *"for the week"*) and neither is a session label. It is **Part 2 of the same recording session as V15** and inherits V15's internal dating. See `V16_INTERPRETATION.md` Q1 and open item **196** |
| Continuity with V15 | ⭐ **DIRECT AND MID-SENTENCE.** V16 `[00:00:00]` opens on the bare words *"pivot points."* — no greeting, no title read, no re-introduction — and V15 `[00:35:00]` had promised *"I'm going to tie pivots in the blue tracer into it in a minute."* **The two files are one continuous lecture split at a file boundary** |
| Frame rate | **3.0 fps** in the SWF header — read from **this file's own header**, not assumed (`SWF_CAPTURE_RECIPE.md` §10 as corrected by V10 R1 open item 87). The 10× sweep patch is therefore **3.0 → 30.0** here |
| Stage size | **1024 × 786** — the majority class. `GOTCHA 5`'s table gives `(512, 300)`, and the pre-click / post-click guard **confirmed it fired** rather than assuming it (`sweep.log`: *"play click confirmed: stage changed"*) |
| Transcribed by | ASR, by a pre-ingestion session. Copied **byte-for-byte** and verified 2026-08-14 — see VERIFICATION below. The pre-ingestion file's own `# VIDEO` header block is **NOT carried over**: its *"Course Position: Video 17 of 21"* is wrong under `D-017` §2's renumbering (this file is **V16**), and its *"Primary Topics"* line names the methodology rather than the lesson |
| Transcription confidence | **MEDIUM–HIGH.** 377 markers, strictly monotonic, **zero** equal-adjacent pairs, **zero** backwards steps, gaps 3–16 s (mean 7.1 s), last marker `[00:44:30]` sitting **5.8 s** before the measured end of audio, and a speech rate of **144.7 wpm** across 6,453 words. It preserves its own mishearings — *"180R"*, *"GVP"*, *"the doggie outside structure"*, *"at the moment open"*, *"an an an an an an"*, *"M3 was M5"*, *"F XDD"*, *"my G's"*, *"in due commodity crosses"*, *"the clothes back in the consolidation"*, *"three week pushes"*, *"a load of come in"*. **A fabricated transcript does not invent its own mishearings.** Defects are ordinary ASR failures on domain vocabulary, numbers and proper nouns; **the load-bearing ones are corrected below, each arbitrated by an independent ASR pass** |

---

## SPEAKER TABLE — MANDATORY UNDER `D-025` consequence 3, re-adopted by `D-033`

| Speaker | Runtime | Basis |
|---|---|---|
| **Course author (Steve Mauro)** | **100%** — `[00:00:00]`–`[00:44:30]`, the whole file | Six non-acoustic strands, below. **HIGH confidence** |
| Guest presenter | **0%** | No second voice is introduced, addressed, thanked or handed to anywhere in the file |

**`COURSE_PROGRESS.md`'s V16 GATE (d) required this be TESTED, and noted the condition is WEAKER
here than for V15 because V16 is Part 2 of the SAME recording session. It was tested anyway, on
strands fixed before the answer was known**, and the acoustic cross-file screen was **NOT** run,
per V07's prohibition.

### THE SIX STRANDS — non-acoustic, `D-025`/`D-033` method

| # | Strand | Evidence, VERBATIM |
|---|---|---|
| **1** | ⭐ **He reads a student question addressed to "Steve" and answers it in the same voice, with no pause for anyone else** | `[00:40:07]`–`[00:40:22]`: *"Frank, Franco, **Steve, are you stating the London** \| session starter on your slide? What is the daily candle that we were looking at? Okay. Good question. \| **I wanted** the pivot points of price action to be as fresh as possible right before we trade."* |
| **2** | ⭐ **He ventriloquises a student mocking him in the third person and finishes the same sentence in the first person** | `[00:35:40]`–`[00:35:50]`: *"**I want you** to train your biceps by taking the six majors using a pivot calculator and getting a deeper understanding of these \| stupid lines that **Steve put on the chart** that I don't even know what the hell they're there for."* The mockery is the student's; the chart is his |
| **3** | **He sets and owns the course's calendar, first person, for the next six months** | `[00:36:50]` *"At the end of this bootcamp, **I'm** going to leave the bootcamp recordings up."*; `[00:36:59]` *"**I'm** going to teach a couple of classes. **I'm** going to take two months off."*; `[00:37:41]` *"**I'll** start another bootcamp cycle, and we'll go through this stuff again together."* |
| **4** | **He owns the forum, the homework, the indicator and the coder** | `[00:35:26]` *"post them in the forum **for me to see**"*; `[00:38:21]` *"all right, **Steve**, I'm rolling up my sleeves"* (again the student's voice); `[00:43:24]` *"**Ray is working on** with some good coders"*; `[00:44:11]` *"**My G's** got to be tried on all different platforms before **we** can just give it out."* |
| **5** | **He grades and assigns in the second person and no one answers back** | `[00:35:03]` *"Find the expected high and low for the day on six majors using pivot calculations."*; `[00:35:26]` *"Do the six majors for two nights, that's all."*; `[00:38:18]` *"come on, man. When are you going to give it up to me and say,"* |
| **6** | **Handover scan: ZERO.** | The same **17-pattern** superset V12–V15 used returns **ZERO hits across all 377 markers**: `take it away` / `turn it over` / `hand over` / `back to you` / `thanks Steve` / `my guest` / `joining us` / `over to you` / `take over` / `passing it` / `go ahead Steve` / `let me hand` / `let me pass` / `you're up` / `floor is yours` / `I'll let` / `welcome back` — **all ZERO.** ⚠ This is a **cleaner** zero than V15's, which returned two benign false positives; V16 opens mid-sentence and greets nobody, so there is no greeting to misfire on |

⚠ **WHAT THIS DOES NOT ESTABLISH, STATED BECAUSE IT IS THE WEAK POINT.** The token *"Steve"*
occurs **five** times and **not one is a self-naming** — every occurrence is a student's voice,
quoted or imagined. V15's strongest strand (*"Steve's going to suck… you're going to hate me"*, a
pronoun switch inside one breath) has **no counterpart here.** The identification rests on
ownership and on answering-in-the-same-voice, which is the V13/V14 pattern rather than the V15
pattern. It is **HIGH, not CERTAIN**, and a reviewer who strikes strands 1 and 2 as
*"quoting a student"* is left with 3, 4 and 5, which are still first-person ownership of the
course itself.

---
## VERIFICATION — `SETUP_ISSUES.md` `I-008`

`I-008` records that most committed transcripts in this project are **unverified**. This one is
verified, and the five checks below are the same battery V13–V15 used. Every figure was produced
by running something, not by reading.

### §1 — DURATION AGREEMENT, THREE INDEPENDENT SOURCES

| Source | Value |
|---|---|
| `ffprobe` on the extracted `audio.mp3` (last audio packet PTS) | **2675.826939 s** = `00:44:35.8` |
| SWF header, read this session: `frameCount 8029 ÷ frameRate 3.0` | **2676.333 s** = `00:44:36.3` |
| `SOURCE_MANIFEST.md` row V16 | `00:44:35` = **2675 s** |

**Spread: 1.33 s across three methods that share no code.** The filename label `(45mins)` agrees
to within 25 s.

### §2 — MARKER-GRID INTEGRITY

| Check | Result |
|---|---|
| Markers | **377** |
| Strictly monotonic | **YES** |
| Equal-adjacent pairs | **0** |
| Backwards steps | **0** |
| Gap min / max / mean | **3 s / 16 s / 7.1 s** |
| First marker | `[00:00:00]` |
| Last marker | `[00:44:30]` — **5.8 s** before the measured end of audio |

**A transcript whose last marker landed after its own audio, or whose markers repeated or went
backwards, would be evidence of fabrication or of a mismatched file. None of those is present.**

### §3 — THE CONTENT MATCHES THE FILM, CHECKED EARLY (`GOTCHA 4`)

`GOTCHA 4` requires one screenshot compared against the transcript **before** any long capture is
trusted. Done at sweep frame `i=20`, burned timecode `01:40`:

* **Transcript `[00:01:40]`:** *"Right? Of my hundred pips, how will I allot those pips?"*
* **Frame `V16_00-01-40_…png`:** the `Pivot Points` grid slide with a **hand-written yellow `100`**
  in the top-left of the whiteboard, drawn seconds earlier.

**The right film is on the right port at the right clock.** Three further content anchors are in
the TIMESTAMP CONVENTION table above.

### §4 — IT PRESERVES ITS OWN MISHEARINGS

Twelve independent ASR failures survive in the committed text, and they are the kind a transcript
written from a summary would never invent: *"180R"* `[00:03:26]`, *"a load of come in"*
`[00:06:02]`, *"the clothes back in the consolidation"* `[00:10:27]`, *"camels overlap"*
`[00:11:25]`, *"the doggie outside structure"* `[00:12:45]`, *"at the moment open"* `[00:14:23]`,
*"three week pushes"* `[00:20:20]`, *"GVP"* `[00:23:38]`, *"an an an an an an an an an an an a
long M2"* `[00:26:39]`, *"M3 was M5"* `[00:33:30]`, *"in due commodity crosses"* `[00:41:02]`,
*"F XDD"* / *"My G's"* `[00:44:11]`.

⚠ **`[00:26:39]`'s eleven-fold stutter is worth naming separately.** It is a decoder failure on
a passage the speaker delivers at speed, and it means **that sentence's content is unrecoverable
from this transcript alone**; it is arbitrated in §5 and, where the arbitration is not clean, the
claim is dropped rather than reconstructed.

### §5 — INDEPENDENT ASR ARBITRATION

**STATUS: PENDING — the second pass is still running at the time of this checkpoint commit.**
The committed text below is byte-for-byte the pre-ingestion transcript; **no word of it has been
edited.** Corrections arrive as a table in this section, each attached to the marker grid's
timestamp, and the body is never rewritten. Load-bearing candidates already identified and queued
for arbitration:

| # | Marker | Committed ASR | Why it is load-bearing |
|---|---|---|---|
| 1 | `[00:14:23]` | *"At the moment open"* | The slide two seconds later prints `London Session Start / 2:00 To 3:00 AM, EST`; if the word is **London**, this is the corpus's clearest statement of *when* the pivot-grid read is taken |
| 2 | `[00:03:26]` | *"which is my 180R, 100 pips ADR"* | `180R` is not a term in this corpus; it sits inside the one worked arithmetic example in the lesson |
| 3 | `[00:33:30]` | *"Most of you, it wasn't M4, M3 was M5"* | There is **no M5** on the printed pivot grid (`R2 M4 R1 M3 CPP M2 S1 M1 S2`). Either the ASR is wrong or an undefined level exists |
| 4 | `[00:26:39]` | *"an an an an an an an an an an an a long M2"* | Eleven-fold decoder stutter; the sentence's content is unrecoverable from this transcript |
| 5 | `[00:09:31]` | *"the ADR is calculated over the last two weeks, 15 days"* | ⭐ **The single highest-value line in the file** — it is the lookback `A-100` says the corpus does not have. It must be confirmed verbatim before anything is built on it |

---

## TRANSCRIPT — VERBATIM, 377 MARKERS

> Copied byte-for-byte from the pre-ingestion `TRANSCRIPT.md`. **Nothing below has been edited,
> normalised or re-punctuated.** Its ASR defects are left in place; corrections live in
> VERIFICATION §5 and nowhere else.

[00:00:00]
pivot points. Okay, how can you project the high and low and have a rough idea

[00:00:09]
where it's coming out what price is going to do? Your intraday support and

[00:00:13]
resistance if you will because the high of the day is the strongest resistance

[00:00:18]
there is and the low of the day is the strongest support there is. But we

[00:00:26]
understanding how to use pivots will give you a possible idea of where the

[00:00:33]
high might fall or the low might fall. Why? Because we're taking an average or

[00:00:38]
I'm sorry we're taking yesterday's price action and projecting it on

[00:00:41]
tomorrow's chart. Okay, so here's how pivots points are worked. They're calculated

[00:00:47]
on daily candles. Yesterday's price action gives you tomorrow's pivot points.

[00:00:59]
Okay, if yesterday's candle was red then it's understood that you're in a

[00:01:05]
downtrend but we know a little better about the cycle. So the projection

[00:01:10]
would come in as an M1 M3 day. If the daily candles green were in an uptrend we

[00:01:20]
expect price to come into M2 M4. Okay, so let's break it down a little further.

[00:01:27]
Let's talk about it. Understand I'm a dealer. I have a hundred pips to work with.

[00:01:40]
Right? Of my hundred pips, how will I allot those pips? Okay, Steve, you're

[00:01:50]
coming to the market, you're ready to go. At 1 am I want you to start your work.

[00:01:55]
You got a hundred pips for your average daily range or you're allowed to work

[00:01:59]
with. So what am I going to do with those hundred pips? I'm going to use 25% of

[00:02:05]
them or in this example 25 pips to hit the stops and fake traders out. 75% of

[00:02:14]
what's left for me to work. I'm going to use to make my trend run and then I'm

[00:02:21]
going to end off with a higher low and close the day. Okay, so in this example the

[00:02:29]
central pivot point price comes out and forms the Asian range right at the central pivot

[00:02:36]
point. At 1 o'clock or 2 o'clock or 3 o'clock depending on when I feel like it because

[00:02:43]
I'm a dealer I can do what I want. I decide that I'm going to trigger the stops and pick

[00:02:51]
up the breakout traders by widening the swing and then breaking to the upside and going

[00:02:59]
somewhere around the M3 number and making my M formation. Now this move I took the top

[00:03:06]
of the Asian range and I exceeded it by 25 pips. Okay, I cut the Asian high by 25 pips

[00:03:17]
because I want to save my 75 to get everybody out. That went long. I make my M formation

[00:03:26]
around the M3 pivot. My downside target is the M1 pivot which is my 180R, 100 pips ADR

[00:03:33]
that I'm allotted today from here to here. And along the way I got to pick up some stops

[00:03:41]
to take some traders out. Knock a couple of people out of the business maybe make some

[00:03:46]
margin calls stop by having a cup of tea and mess everybody up. That's the business right.

[00:03:53]
So now I fall quickly I shift the zone away from higher level long holders by quickly

[00:03:58]
getting away from the M3 level. Okay now get the stops, get the stops drop level 1 is formed

[00:04:09]
I'm in level 2. Okay, maybe I go to lunch mid session. I come back I show some consolidation.

[00:04:18]
I come back from a big fat lasagna meal and I'm a little lazy and I don't feel like working

[00:04:23]
so hard so that I just kind of drift down and make level 3 and I pull back here. There's

[00:04:30]
been three intraday pushes. I've made my trap move to end the day. I had a big fat lunch

[00:04:38]
in here that's why I went sideways for a while mid session break. And then I closed the session

[00:04:45]
strong by making my W formation to end the day and I pass it off to the US guy and he takes it

[00:04:53]
back into the range and consolidates. And then since I'm such a ball buster I decide I'm going to go

[00:04:59]
ahead and consolidate right around level 2 to make up some fake support and resistance for everybody

[00:05:04]
on the chart. So when they draw their line tomorrow I could just laugh at them. Okay, so now

[00:05:17]
think about what happened here. We used the pivot points as a as a guide of where the high

[00:05:24]
and where the lows will come in. So we can look at the projections right up the London open but

[00:05:32]
they're painted on your chart for you. You can have a rough idea of where the high might form.

[00:05:41]
So if I go M3 is at 106 27 Canadian. Okay, well guess what the high of the day might come in around 106 27.

[00:05:52]
Give or take a few pips variance for the deal to hit the stops or whatever. But that's a rough

[00:05:58]
idea where the high should come in. Then I could look at the M1 number and go okay I expect a

[00:06:02]
load of come in at 102.14. I could subtract the two and get the range. And I know that there's about

[00:06:15]
120 pips ADR and that so happens to match or what the meter has been tracking. So I have a rough

[00:06:21]
idea of how to use a pivot grid to make projections. There's a software out there that's like

[00:06:29]
I want to say $8,000. I don't know for sure $79.99 or something like that.

[00:06:35]
That uses these calculations to give you projected highs and lows and I just showed you how to do it.

[00:06:40]
You don't need a software to give you the highs and lows. I'm telling you how to project them.

[00:06:47]
Okay, I think it's like predictive moving average and it's possible highs and lows.

[00:06:51]
You know better than any software package or anything else of where price is going to go based on

[00:06:59]
what I've shown you and what was shown to me. The projections when you get comfortable with the

[00:07:05]
method are uncanny. It's unbelievable how you could say price is going to go here. I know some

[00:07:10]
guys in the group that could pretty much give you the numbers of where price is going to go.

[00:07:16]
I don't know if you remember or not, but if you take the anchor point when we talk about trend

[00:07:25]
and add the ADRs for three days you can have a good projection of where price will terminate

[00:07:32]
and make the reversal. I know pound has been rise as Steve. It doesn't always work of course.

[00:07:39]
There's other things going on in the world. Fundamentals, the families have to get money

[00:07:45]
and price where they need it to be, but along the way the dealers will give you the signals.

[00:07:52]
And most of the time, most of the time the dealer will issue the signals that I've illustrated for you.

[00:08:01]
Okay, so if you have ADR, let's say your anchor point is here. You have ADR 100.

[00:08:07]
Okay, then you know that whatever the anchor point is, take the anchor point and add 300 to it,

[00:08:14]
and you got a rough idea where price will terminate. And if you're a swing trader,

[00:08:19]
you can have a rough top side target. Of course, the signal is always prevailed more importantly.

[00:08:27]
Okay, now let's go over here. You raise this. Let's just talk about it the other way.

[00:08:36]
Picture a daily candle. Here's your daily candle, right? There's your wicks and everything.

[00:08:41]
The pivot grid gives you the range or the ADR gives you the range

[00:08:47]
of what you expected to move within one day, right? But within that one day, all this stuff is going on.

[00:08:55]
They're consolidating at the central pivot point. They're breaking to the downside in this example.

[00:09:01]
They're making their formation, trap the traders the other way. They're making their intraday

[00:09:06]
pushes until they find, and even in here, perhaps on the last leg, you get a 33 trade.

[00:09:16]
Right? And then they make that spike to the high, and then they pull back and end the day in

[00:09:21]
consolidation. Okay? So understand that when the pivot grid matches up with the ADR,

[00:09:31]
the ADR is calculated over the last two weeks, 15 days.

[00:09:37]
We have an average of what prices moved over the last two weeks. The ranges will tighten up when

[00:09:42]
the market is quiet. The ranges will expand when the market is more volatile because it's an average.

[00:09:47]
We're averaging what the move is. Okay? So now understanding this,

[00:09:57]
intraday you got your intraday pushes, you got your 33 trade inside of a daily candle,

[00:10:03]
all this activity is going on. It's not, when you look at that, it's not just, oh, that was a big red

[00:10:08]
candle today. That's not what's going on here. What's going on here is that the dealer comes in,

[00:10:19]
he has his allotment of pips. He works the high, he works the low, he spikes, right? The W

[00:10:27]
formation, the M formation, and you get the clothes back in the consolidation

[00:10:37]
at the edge of the candle, where it closes. All this activity, when you look at one candle,

[00:10:43]
all that activity is what's transpired for the course of the day, for the course of 24 hours.

[00:10:46]
And that gives you the 24-hour dealer cycle. Asian range, London, reverse, go down New York,

[00:10:55]
come back in the day, or come back in here and end the day by to be correct,

[00:11:03]
to be correct. They end the day in consolidation off of a wick, let's say this candle's red,

[00:11:11]
they end the day off in consolidation where that candle closes. Think about this,

[00:11:18]
channels aren't stacked straight up and down on each other. Are they no? They're not like this.

[00:11:25]
That's not a downtrend, or if it's going this way and uptrend, they're not stacked,

[00:11:29]
camels overlap. So the central pivot point, which is where price comes out and encloses,

[00:11:37]
then the next day the central pivot point will adjust for tomorrow's allotment, hence

[00:11:44]
candles overlap because of the stop-hunch. What's happening is the dealer goes back inside

[00:11:50]
of yesterday's range to pick up the stops and the traders at the stragglers that he needs to grab,

[00:11:57]
right? So when you see the candles overlapping, what's happening is in a downtrend, the dealer

[00:12:04]
comes out at the central, makes the M formation, corrects pulls back at the close of this candle,

[00:12:10]
opens correctly on. It's important to see it correctly.

[00:12:18]
All right, at the close of this candle, the opens here spikes up, hits the stops, drops,

[00:12:24]
hits the low, pulls back and ends here. Then the next candle, same thing, it opens on the overlap.

[00:12:30]
So in a three-day cycle, the pivot points will be accurate.

[00:12:39]
Okay? Now at the end of the three-day cycle, depending on what the trend is, if the pair is in

[00:12:45]
consolidation, you'll see maybe the doggie outside structure, inside structure, that garbage.

[00:12:51]
And then you expect it to reverse and either continue or reset. So for a couple of days during the cycle,

[00:12:58]
the pivot will be at a whack, especially after this candle is pointing down red,

[00:13:07]
right? A red candle projects an M1M3 move. But at the end of a three-day run, we know better,

[00:13:14]
going into the end of the week, the dealer will reverse. Okay? So if we know ahead of everyone else,

[00:13:23]
that the dealer will probably reverse, then we simply adjust the pivot points to the next day ahead

[00:13:32]
of everybody else, M2M4 projections. Okay? So now, we know there's a three-day three-level cycle.

[00:13:42]
You can look at three candles and see that they've been dropping. You might get an outside

[00:13:47]
outside structure on the fourth day. One or two things are going to happen. The dealer is going

[00:13:54]
to reset and correct. He's going to reverse and start a new cycle. So now, we can take on the fourth

[00:14:05]
day, we will not project M1M3, we'll project M2M4 ahead of the crowd because we know how the dealer

[00:14:12]
moves in threes. Okay? You with me? So what I want you to understand is that the possible highs,

[00:14:23]
okay, get ahead of myself. At the moment open, if the dealer breaks high,

[00:14:28]
then the top, upside of the pivot grid, you're a seller. If the dealer breaks low, at the bottom

[00:14:34]
side of the pivot grid, if he hits M1, gives you a nice setup, if he hits M2, he gives you a nice

[00:14:43]
setup. That's the possible low, top side projection, M3, and M4, sorry about my penmanship. I'm scared

[00:14:50]
to hold the pen down too long. Okay? So if you understand that those are M1M3 is projected range

[00:15:01]
when the daily candle closes red. Okay? When the daily candle closes green, the projections are

[00:15:11]
that price will move between the M2 and M4 grid. All right? So now, the fourth day of the cycle

[00:15:22]
in a downtrend, the dealer issues the W, M2M4 is your projection. The fourth day in an uptrend,

[00:15:36]
the dealer issues an M4, the projection goes back to M1M3. Everybody understand that?

[00:15:43]
This is where pivots fail because you're taking the daily candle and projecting it onto

[00:15:49]
morrows chart. Well, normal technicals don't understand what we know about the market maker.

[00:15:57]
We know that the market maker moves on average of a three-day cycle. So if you get three levels of

[00:16:04]
rise over three days and the candle closes green, we are expecting a reversal. So you simply adjust

[00:16:15]
your pivots from M1M3 to M2M4 or vice versa. You understand? Because we know the dealer,

[00:16:27]
we know that the dealer will have to get his money back after a couple of days.

[00:16:36]
Okay? All right. So here's your pivot grid. It looks like

[00:16:44]
All right, let's say you're on an M3M1 day or M1M3. That means that this is going to be the high,

[00:16:51]
this is going to be the low. So you take 33-19 and subtract it from 31 in a quarter,

[00:16:59]
and I don't know if I had to do it real quick about 150 pips. Okay? So there's 150 pips

[00:17:06]
possible for the day, and I can tell you what, your central pivot point, the dealer is going to come

[00:17:13]
out at the open. He's going to tap M3, maybe slightly above it. He's going to correct in three moves

[00:17:18]
down to M1. He's going to end the day back in consolidation. That's the daily cycle. That's what we've

[00:17:24]
all learned, all learned together. Okay? We're expecting to do it in three moves. Maybe, maybe not.

[00:17:33]
Maybe two moves. But we can have a rough idea of where the trade will begin and where it will

[00:17:39]
based on ADR and projection, right? ADR and projection of where the high and low will fall. Okay?

[00:17:53]
All right. Just understand this. If you get anything out of this at all, it's that M3 and M4

[00:18:01]
are possible day highs. They are located above the central pivot point. All right? Central pivot point,

[00:18:10]
yellow, M3 above, M4 above, M1 and M2 are below the central pivot point and they're possible

[00:18:19]
low projections. Okay? So I can tell you, let's say this is tomorrow's grid. I can tell you

[00:18:27]
EJ, what's the projection? Okay. So then one M3 day. Price has been dropping. I expect the

[00:18:34]
high of the day to be 3319. I expected to be worked. And I expect 31 and a quarter to be the low

[00:18:41]
for the day if the dealer meets the ADR. Okay? Obviously, other shit can come up. They could have

[00:18:48]
other fundamentals, news announcements. The dealer might spike to the M4 level and then come off

[00:18:54]
at that level and hold sideways for the rest of the session and then not make that projection

[00:18:59]
for the day. But I can tell you that 3416 and 31 and a quarter high, low for the day in EJ, tomorrow,

[00:19:08]
come tomorrow. That's what I'm expecting. So now what happens if the dealer goes to 3471?

[00:19:18]
I hate him again if he makes an information. I'm looking for an area of where I can project

[00:19:26]
that the high and low will form. So if I know roughly where that's going to be, I simply need

[00:19:35]
the weight for the dealer to issue an M or W at those areas. Okay? All right. To get your range

[00:19:49]
in the example, you're subtracting M1 from M3 or M2 from M4. That gives you the range. Okay,

[00:19:57]
right here. You'll know how many fifths it is. Okay? All right. Good stuff. I'm Jacked. Okay,

[00:20:07]
look, this is exactly what I'm talking about. I know these are like prime examples, but I just

[00:20:11]
want you to see the dealer made the M formation slightly above the M3 pivot and he corrected in

[00:20:20]
three week pushes, but man, if he didn't bounce right off of there and respect that pivot level

[00:20:24]
exactly, then pull right back and end the day. Okay? So I could have told you the pounds going

[00:20:35]
to the high of the day is going to be around 6460 and it's going to make a low around 6330.

[00:20:43]
125, so whatever it is, that's the ADR roughly and I could make the projection for tomorrow where

[00:20:49]
the high and low is going to form. Okay, prices laying. This was an example of Euro CHF a few weeks

[00:20:58]
ago. Price was laying like a dead dog sideways flat for like I can't even tell you. And

[00:21:09]
Zann called me up and he goes, Hey, are you long Euro CHF playing a chance? I've been long for

[00:21:12]
days. I'm waiting for the break. Price had dropped dropped dropped dropped dropped and it was laying

[00:21:17]
on the bottom like a dead dog man and I grabbed a position. Well, I wanted to go right now, right?

[00:21:22]
I want profit. I want profit. I want it now. Like everybody else. I'm the same. I'm human,

[00:21:27]
but it was laying on the low and it kept bouncing around. It wouldn't go, wouldn't go. And then

[00:21:31]
like Thursday night, they waited and then they spiked it hard Friday and they rose up big.

[00:21:38]
It's just understanding that they already made the correction. They formed the low and that they

[00:21:43]
were laying on the bottom of the run like a dead dog and they already had hit all their stops

[00:21:49]
and they pulled away and they were just laying there like this and it would not come off of that

[00:21:54]
range. It was so tight. It was crazy. I knew price was going to pop up. Okay. And this is one of those

[00:22:01]
examples. Price comes in, consolidates all session at the M2 level low. The averages, if you

[00:22:09]
you noticed, they're coming from up. So it settled in made its consolidation. Okay. Hit the stops,

[00:22:18]
hit the stops, but you know that this is the directional bias because you're in the cycle

[00:22:26]
and they're consolidating the averages coming back together like spaghetti. Okay. But I want

[00:22:31]
you to notice what it did. Hit M2 spiked up to M4, worked M4 a little bit and went back into

[00:22:37]
consolidation. Why? Because this distance from here to here was the average daily range

[00:22:44]
based on yesterday's projection that the dealer had to work with approximately what? 200

[00:22:50]
pips in every pair except GJ and some of the crosses. Okay. Why 200 pips? Because they

[00:23:01]
would destroy the economy if they moved it more than one day. Now other things make the market

[00:23:07]
volatile. 9, 11 crazy things happen. The bomb in the subway in Europe. Those things make

[00:23:15]
price become erratic. But if you notice that it made the spikes, but it always comes back within

[00:23:24]
a range within a 600 to 1000 pips range for the week or within a reasonable amount of pips for

[00:23:29]
the cycle, it will come back in that range. The only exception to that is when the dealer shifts

[00:23:38]
the zone to meet their quarterly semi annual targets. Think about it for a minute. GVP,

[00:23:51]
all the way up to $2.10. I don't know, four years ago, I don't even remember, three, four years ago

[00:23:56]
now it's all the way back down to 130 then it went to 160. Think about that. It goes up and down

[00:24:02]
it fluctuates against the dollar crazily. It shows something that huge, oh my god it's going to $2

[00:24:09]
the dollar's falling apart. They're burning the country down. We're losing everything. And then

[00:24:14]
more accurately a few months later it's right back where it was. Okay. Extended stop hunts.

[00:24:22]
Target's that are part of a bigger picture. Destruction of the world economy. I don't know what

[00:24:28]
the reasons are. I can go on all night. My speculation. Right. The adjusting of the currencies to

[00:24:36]
be in line for the Amero to be launched. Understand those things are going on. We can't control

[00:24:44]
those things out of our reach. But we can control one thing. Our platform, our emotions and the

[00:24:51]
signals that the dealer shows you before he makes those moves are there. That's where you take control.

[00:25:01]
Okay. All right. Next slide.

[00:25:07]
Okay. Again, this is a choppy day. This was a level three day. Notice how the averages are all tight.

[00:25:12]
The 50s flat. The averages are tight. We're in level three. But the dealer worked the prize

[00:25:22]
between the pivot levels and level three. It was kind of cool to see. He worked between the

[00:25:29]
projected high and projected low. He tapped it a bunch of times, grabbed some order, shifted it

[00:25:36]
back away. He worked the range. His average daily allotment in a level three type behavior.

[00:25:44]
Perhaps he was handling some crosses. Perhaps he was picking up stops and using traders. All the

[00:25:49]
reasons they hold a level. You guys know what they are. Okay. But I just thought it was pretty cool to

[00:25:57]
see him working those that range for the whole day in between M1 and M3.

[00:26:06]
Okay. The dealer comes out at M4, possible high of the day, right? And it was. He shifts the zone

[00:26:13]
down and then he works right around M3 and then he corrects down to M1. Back into the range. Notice

[00:26:23]
he came back to where it started, back to the M3.

[00:26:26]
All right. This stuff is useful and predictable. Here is a Asian range consolidation, half a

[00:26:39]
batman, and an an an an an an an an an an an a long M2. M4, he broke the projection outside the

[00:26:49]
ADR. The dealer has to correct above the ADR above the anticipated range. Okay. Part to count three

[00:26:58]
pushes in here. I agree. But you know what? He met his range. And he came back and he closed. He

[00:27:10]
closed within the M4, the projection. He ended the day within the projection. So he went above.

[00:27:18]
Okay. Your ADR would be probably around here somewhere exceeded. The dealer makes the

[00:27:23]
M formation. He tops out. He stops extending the high. He stops extending the high. Then he

[00:27:31]
corrects back into the range to end the day. Same thing down here. Spike the low, half a batman.

[00:27:36]
He rose. Okay. All right. Pivot points are essentially if you haven't figured out. They're an

[00:27:44]
ADR grid that's fixed. The extremes of the pivot pivot grid represent the ADR high and low in essence.

[00:27:53]
So M1 and ADR line line up or M3 or M4 and the ADR high line up. That's given you the floating grid

[00:28:01]
and the fixed grid coming together. That's a pretty good area for an M or W to four.

[00:28:06]
All right. Since the grid is fixed and does not move. But the trading range is obviously

[00:28:14]
you're not fixed. They float. We can couple pivot points with the ADR marker for strong

[00:28:20]
conformations. So now you take the information I've given you about the pivot points.

[00:28:25]
Couple it with ADR high or low. It's an M1 or M2 and ADR lows lay in there. And if you happen

[00:28:34]
to see off in the distance right around slightly below M1 a big fat blueberry line line there.

[00:28:41]
I'm pretty sure a price will go there or false just short of it for fake. Fake and people out.

[00:28:48]
All right. Here's what I mean. All right. I showed you the slides. But look, these lines come together

[00:28:53]
and then low and behold there's a little blueberry right there. Guess what's going to happen.

[00:28:56]
It's going to come in and do this probably. Okay. All right.

[00:29:06]
Pivot points are essentially intraday support and resistance.

[00:29:13]
Right there. It's a grid of support and resistance and you're projecting where price should settle

[00:29:18]
in and make it smooth. Where the high and low is going to form. Okay. Once it starts

[00:29:26]
it's move. Once it starts it's move a break of the level is almost certain to give way to the

[00:29:33]
next pivot level. So what happens is it starts falling. It's the stops drops again. It's the stop

[00:29:39]
breaks that pivot level until the ADR is overextended or exhausted.

[00:29:48]
Understand the dealers are limited by the IMF and what they can do.

[00:29:57]
He has limitations. The dealer is not. Oh, I'll just take everybody's money, run a mock

[00:30:02]
to destroy the country. That's not how it's set up. The businesses set up in such a way that

[00:30:08]
I don't know who tells who I don't know where it is comes from. It's deep, man. There's a lot of

[00:30:12]
shit going on. But these guys are told do not exceed 200 pips on the average day because of

[00:30:19]
you'll do this. You'll destroy trade. You'll mess up the deficit. I don't know the reasons.

[00:30:26]
But there are reasons and they are told by somebody what they're allowed to do, what they can and cannot do.

[00:30:33]
Okay. They cannot destroy trade balance in the world economy, even though it's happening,

[00:30:38]
things will be worse than they are. They are limited by the world bank, by the families, by whoever

[00:30:45]
tells them what they're supposed to do. Hideo is joking around there. So when you start talking about

[00:30:51]
the shit, look down and see if there's a red dot on you anywhere. It sucks, but this stuff is real,

[00:30:59]
man. I'm not the bare in bad news. It is what it is. If Bowser Bowser was in here, he would probably,

[00:31:06]
he would let me know, man. He is like, he knows 10 times more in depth about the stuff than I do.

[00:31:14]
Anyway, I don't want to get off on the wrong tangent. I want to talk about the business.

[00:31:19]
This stuff is real. They have limitations placed on them. So the AER grids and the pivot grids are good

[00:31:25]
indications of where support and resistance high and low will fall in for the day. It will give you

[00:31:32]
a good area of where the M&W will form. Remember that during the cycle, because the dealers make

[00:31:41]
three red candles or three ring candles, that the fourth day, the pivot will be off. So take away from

[00:31:48]
that on the fourth day, use the next offset of pivots for the projections. I can't say this enough.

[00:32:01]
Wow, I don't know where it went. Man, just like jumped a bunch of slides. Marker makers are in

[00:32:08]
here messing with me here. You, my friend, are the filter. You're the filter. Some of the guys have

[00:32:15]
taken all this stuff off the chart and are just trading M&W's. That's fine. You're trading the

[00:32:21]
M&W's with the timing element. That's it. That's okay. I'm okay with that. But a lot of you are

[00:32:27]
struggling. You asked me for help. And this is the help. I'm telling you, we're breaking down the

[00:32:31]
individual components on my template and showing you how to use each individual component. But remember,

[00:32:38]
your brain, the space between your ears is the filter. You have to understand that if the

[00:32:44]
pivots are blown out from an aggressive run, if there was a news release or something tragic

[00:32:49]
happened like the nuclear meltdown in Japan, the pivot numbers are going to be off. So you become

[00:32:55]
the filter to understand that, hey, man, the pivots are messed up because there was a 250-pit move

[00:33:02]
yesterday and yet. So those numbers will be, remember, if there's a 250-pit move on Tuesday,

[00:33:09]
Wednesday's pivots will be based on the open high, low close of Tuesday's price.

[00:33:17]
Okay? You've got to identify the market condition and candle pattern for next support and

[00:33:24]
resistance level. You have to understand the M&W might form an M5. Most of you, it wasn't M4,

[00:33:30]
M3 was M5. Okay, but the dealer issued the pattern as I laid it out for you. Okay, if price

[00:33:36]
comes out in the wrong segment of the pivot grid, I just went over this. Big market moves will

[00:33:43]
disrupt the pivots for the following trading session. In order to find opportunity, you got to set

[00:33:47]
some rules for trading when the price comes out of the wrong segment of the trading zone. You

[00:33:52]
know what the rule is? Ignore the pivots and identify what I've taught you, the pattern, the pattern,

[00:33:58]
that's the answer. Okay? And the example of that is going to be, comes out in the wrong segment,

[00:34:07]
maybe makes a straightaway. Okay? Notice that price came out below the central pivot point,

[00:34:13]
made the M formation, there's your hammer or here, either one of these is acceptable entry,

[00:34:18]
there's your run outside the ADR. Okay?

[00:34:27]
Inside below the central pivot point, at the London open, reconfigure the blue box, M formation,

[00:34:35]
doge to the high, there's your move. Inside the wrong segment of the pivot grid, straightaway cell,

[00:34:44]
now example. Okay? Pins to the 50 at the open. Okay? So here's some more in D for you. We're

[00:34:53]
winding now, we got about five, six minutes left for time together. Okay. Scott, I'll answer you in a

[00:35:03]
minute. Find the expected high and low for the day on six majors using pivot calculations. Do

[00:35:09]
it free London from Monday and Tuesday. So tomorrow night, Monday night and Tuesday night,

[00:35:16]
go to mypivotcalculator.com, take the daily candle, take the open high, low close, calculate the

[00:35:26]
values, post them in the forum for me to see. Okay? Do the six majors for two nights, that's all.

[00:35:36]
I know the indicator does it for you, but I want you to understand what you're doing. Again,

[00:35:40]
and we're breaking down with training individual body parts. I want you to train your biceps

[00:35:46]
by taking the six majors using a pivot calculator and getting a deeper understanding of these

[00:35:50]
stupid lines that Steve put on the chart that I don't even know what the hell they're there for.

[00:35:57]
This is how pivots are used. Not everybody knows how to use them. In eight more minutes or seven

[00:36:03]
more minutes, my goal is that you know how to use the ADR, the blue tracer, and pivot

[00:36:09]
lengths on your chart now. Jerry, that's okay. Dumping. If you can't see the pattern clearly,

[00:36:22]
I'm going through these things to help you understand where the pattern may or may not form.

[00:36:31]
Okay? So next set of homework is

[00:36:34]
all right, look. We're getting to a couple of weeks left of the bootcamp. If you haven't done

[00:36:41]
any of this stuff, it's not too late, man. Reminds me, here's what I'm going to do by the way.

[00:36:50]
At the end of this bootcamp, I'm going to leave the bootcamp recordings up.

[00:36:59]
Okay? So when bootcamp is over, I'm going to teach a couple of classes. I'm going to take two months off.

[00:37:09]
If you want to find me, I will be in a bathing suit. I'll be the guy in the bathing suit.

[00:37:16]
I'm going to answer emails and stuff, but I'm going to kind of take an easy and spend some time

[00:37:20]
with my new kid. I've been riding for you guys for the last couple of weeks, and I'm not

[00:37:25]
complaining, it's letting you know. But what I'm going to do is I'm going to leave up my new

[00:37:29]
class recordings for the summer, and I'm going to leave the bootcamp up for the summer.

[00:37:33]
After Labor Day, when I come home,

[00:37:41]
I'll start another bootcamp cycle, and we'll go through this stuff again together.

[00:37:45]
It's going to be for the new students that join us, and it's going to be for the guys that are

[00:37:49]
thickheaded to haven't got it yet, Luther. I saw that. Okay, so

[00:37:56]
what I want you to do,

[00:38:01]
if you haven't rolled up your sleeves and got busy, it's not too late. Make your flashcards,

[00:38:06]
TDI only trades, big board only trades, moving averages, estimate the high and low,

[00:38:11]
using pivot points. These are the things you're supposed to be doing, okay? So if you're not doing them,

[00:38:18]
come on, man. When are you going to give it up to me and say,

[00:38:21]
all right, Steve, I'm rolling up my sleeves, I'm going to do it. Sitting here with me and getting

[00:38:25]
jacked up every Sunday is not enough. You've got to put the lead to the paper, man. You've got to

[00:38:31]
do some work. Okay? So here's the program. Finish up bootcamp, teach you a couple classes.

[00:38:41]
I'm going to take a summer break. I'll answer your emails. I'll keep an eye on the form,

[00:38:46]
and then I'm going to come back after Labor Day. We'll have two classes under our belt. We'll

[00:38:50]
have a web class and a live class. And then what we're going to do is we're going to start

[00:38:57]
another cycle of bootcamp, probably September, October, and maybe end right before Thanksgiving.

[00:39:03]
And then I don't know where I'm going to be. Not going to be in a bathing suit. It'll be too cold.

[00:39:08]
All right. And that's the year. Can you believe it? That's the year. The year is half down.

[00:39:13]
Did you get what you came here for yet? If you didn't roll up your sleeves and let's go, man,

[00:39:20]
come on. All right. All right, man. Labor Day, people that don't know Labor Day. Labor Day is the

[00:39:31]
first weekend in September. Okay. The first, I can't remember, it's like the first full week,

[00:39:39]
and then the weekend that Monday, that's when I come home. Okay, man, I appreciate all you guys.

[00:39:45]
All right. So here's your homework. You should be doing this stuff. If not, do it.

[00:39:49]
It's never too late. Okay. Nope. Nope. Good night. Next Sunday. Wait. Now, yeah. Hold on. I've got to answer

[00:39:57]
somebody's questions. It's going too fast. Stop typing. There was a dude that I promised

[00:40:02]
I was going to answer was a good question. Where was it? All right. I'll do questions for like five

[00:40:07]
minutes and we'll book here at 830. All right. Okay. Frank, Franco, Steve, are you stating the London

[00:40:16]
session starter on your slide? What is the daily candle that we were looking at? Okay. Good question.

[00:40:22]
I wanted the pivot points of price action to be as fresh as possible right before we trade.

[00:40:27]
So we calculate our pivot points from midnight to midnight. I know they're based on the

[00:40:34]
daily candle, but they're based on price action from the 24 hour period from midnight to midnight.

[00:40:39]
Okay. Hey. Somebody asked me what the six majors are. Don't feel stupid, man. There's no

[00:40:46]
stupid questions, but that one's pretty close to being stupid, but it's not. I'm kidding.

[00:40:52]
Javan, here you go. Pound dollar, Euro dollar. Dollar yen. Dollar Swissy. Australian. Canadian.

[00:41:02]
All right. It's actually four majors in due commodity crosses if you want to get technical.

[00:41:09]
Okay. Reese, when we calculate pivot points from the open high, low close from midnight,

[00:41:15]
time to midnight, no, just do it on the daily candle for right now. You don't have to get all

[00:41:18]
technical. I just want you to understand what you're doing. That's all. Just take the daily candle.

[00:41:24]
You can mouse over the open high, low close. Put those in there.

[00:41:31]
And that's it. You'll get your values for tomorrow and then take if it's a red candle, M1, M3,

[00:41:37]
if it's a green candle, M2, M4. Okay. Post them in the form.

[00:41:44]
Thank you, Daniel. I appreciate being the bomb.

[00:41:49]
Probably every time we say that, calling for is listening to me, right?

[00:41:54]
Thank you guys, Russ. Thank you. Patricia, thank you.

[00:41:57]
Mark, thank you, buddy. Co, thanks, man. I appreciate you guys. I really do.

[00:42:08]
I can't wait to see you guys all in New Jersey, man. I hope you all can make it.

[00:42:16]
Jerry, thank you. Susan, don't forget to write me for the monitor.

[00:42:22]
Daniel, thank you. John, thank you.

[00:42:27]
Yes, whatever works for you. If you can answer the homework later, that's fine.

[00:42:43]
Car and SSE, buddy. I need to talk to you this week.

[00:42:51]
That was a good one. Susan doesn't write with her information.

[00:42:55]
Jerry asked for the monitor, send it in.

[00:43:02]
Hey, Susan, I see you. Okay. Congratulations. Thank you, Helen.

[00:43:14]
Dax and I see you, buddy.

[00:43:17]
Oh, just so one more thing for you guys, bail out of here.

[00:43:24]
Now I'm going to hang up. Ray is working on with some good coders. I don't want to say his name,

[00:43:30]
because he might get bombarded to where you just put the box ribbon on the chart and drag the

[00:43:37]
line to the candle time. One candle. Like you drag it to the one o'clock candle, then everything else

[00:43:42]
falls in the place. We're working on that for you guys. That's probably the best and easy

[00:43:46]
as fix. I can't think of any way to make it simpler. If anyone has any ideas, I mean email, man,

[00:43:51]
but I think that's the fix. Is that let's say you drag a line to your one o'clock candle,

[00:43:56]
then all the boxes snap in place. That seems like the best fix to me.

[00:44:01]
That will be available as soon as he's coded. Understand he's got to code it. He's got to write it.

[00:44:07]
We got to try it on an array of platforms. We got to try it across the board and be trading at

[00:44:11]
F XDD. My G's got to be tried on all different platforms before we can just give it out.

[00:44:16]
It's going to be a little time. Maybe if we're lucky, we'll have it ready for the web class

[00:44:20]
for in June, another month, a couple of weeks out. Okay. All right, man. Yeah, that works, Jerry.

[00:44:30]
It works. Daniel, thank you. You guys have a good night, man. Always enjoy this time together.
