# V08 — TRANSCRIPT

## SOURCE

| Field | Value |
|---|---|
| Video ID | V08 |
| Original filename | `Bootcamp1 Wk2 032612 Part3 (43mins).swf` |
| SHA-256 | `6beedb40b7c211cb019b37ff69002e8e625fca4521c3cf3155f946edc5f8b767` — re-verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session, on the flat `Bootcamp/` canonical path |
| Duration | 00:43:03 (audio measured **2583.75 s**; SWF header **7,752 frames ÷ 3.0 fps = 2584.00 s**; `SOURCE_MANIFEST.md` 00:43:03 = 2583 s — three independent figures, agreeing) |
| Lesson title | **"Jim's Journey in Learning and Trading MMFX"** — established **from the recording itself**: printed on the title slide, frame `V08_00-00-05_title-slide-jims-journey.png`. It is **not** taken from a filename and **not** from any pre-ingestion note. The quarantined per-lesson header calls the lesson *"Candlestick Reversal Triggers, Railroad Tracks, Multi-Timeframe Alignment"* — see `QUARANTINE_REGISTER.md` Q-009 for what that claim survives |
| Session date | **2012-03-26**, from the filename `032612` and `SOURCE_MANIFEST.md`. **Not printed inside this recording** (unlike V07, whose title slide printed `03-26-2012`). Shared with V06, V07 and V09 |
| Transcribed by | ASR, by a pre-ingestion session. Copied and verified 2026-08-13 — see VERIFICATION below |
| Transcription confidence | MEDIUM — see TRANSCRIPTION NOTES |

## COVERAGE

```text
STATUS: COMPLETE — no fenced tail, no gaps
Covered: 00:00:00 - 00:42:58
Entries: 848 markers, 848 distinct.
         Timestamps are STRICTLY INCREASING: zero decreasing transitions and
         zero same-second adjacent pairs. (Stated as MEASURED, by scanning the
         body for lines fully matching ^\[\d\d:\d\d:\d\d\]$ -- V03's coverage
         block was charged at R1 for asserting this property where it was false.)
         Largest inter-entry gap 10 s, at [00:07:14] -> [00:07:24]. Next
         largest 9 s, three times: [00:09:20], [00:33:30], [00:42:46].
         Final entry [00:42:58] against measured audio 2583.75 s (00:43:03.7).
```

**The ~5 s tail is not a gap and not a fence.** A Whisper `small.en` pass over
`00:42:40`–end returns *"And now what's inside? What could possibly be left inside this area
here?"* and nothing after it. The recording stops there. **The lesson ends mid-argument** — the
speaker has just posed a question about the innermost stage of his own four-stage model and the
file cuts before he answers it. That is a property of the source, not of the transcript.

## VERIFICATION — FOUR INDEPENDENT AXES

This transcript arrived from a pre-ingestion session and is therefore covered by
`SETUP_ISSUES.md` **I-008** (20 of 21 transcripts unverified). It was **not** trusted on
arrival. What was checked, and how:

**1. The audio the transcript was made from is this lesson's audio.** The pre-ingestion folder
holds `audio_09.mp3`. The `_09` is not an error and not evidence of the wrong file: folder
numbering under `Bootcamp Notes/` was changed by `D-017` §2 so that folder `NN` = video `VNN`,
and under the *pre-renumbering* alphabetical order this lesson sat at position 09. The claim was
still tested rather than reasoned about:

| Check | Result |
|---|---|
| Duration of `audio_09.mp3` vs audio extracted from the SWF by this session | **2583.745306 s vs 2583.745306 s** — identical to the microsecond |
| SHA-256 of the two files | **differ** — `audio_09.mp3` is a 64 kbit/s re-encode, this session's is 40 kbit/s |
| Waveform Pearson `r`, three 20 s windows | ≈ 0 — **a red flag that turned out to be an artifact**; see below |
| **Energy-envelope cross-correlation**, three 20 s windows, ±2 s lag search | **r = 0.978 / 0.978 / 0.981**, all at lag **−0.02 s** |

The near-zero waveform correlation is the mp3 re-encode's ~20 ms coder delay: at sample level a
20 ms phase shift destroys the correlation of a speech waveform completely while changing
nothing audible. Recorded because it looked like a disconfirmation for about a minute, and the
resolution is a general one — **a null waveform correlation between two encodes of the same
audio is expected, not diagnostic.**

**2. The transcript is an ASR of that audio, not a fabrication.** Six 45-second windows spread
across the lesson (`t = 0, 480, 1080, 1680, 2280, 2560 s`) were re-transcribed independently with
Whisper `small.en` and compared word-for-word:

| Window | Transcript words | Whisper words | Word-level similarity |
|---|---|---|---|
| 0 s | 132 | 114 | 0.797 |
| 480 s | 125 | 136 | 0.835 |
| 1080 s | 109 | 99 | 0.817 |
| 1680 s | 158 | 148 | 0.850 |
| 2280 s | 139 | 137 | 0.819 |
| 2560 s (to end) | 44 | 44 | **0.977** |

0.80–0.85 is what two *different* ASR systems on the same speech produce; the residual is
window-edge truncation plus genuine disagreement. **The disagreements are the evidence.** They
are the mishearings of two engines pointed at the same acoustic signal, and each engine keeps
its own:

| Marker | This transcript | Whisper `small.en` | The actual word, from context |
|---|---|---|---|
| `[00:00:06]` | *"FX method"* | *"effects method"* | FX |
| `[00:00:32]` | *"do something **for** 90 minutes"* | *"do something **from** 90 minutes"* | for |
| `[00:00:41]` | *"put up your **trade** tables"* | *"put up your **tray** tables"* | **tray** — Whisper is right here |
| `[00:08:32]` | *"**All of me** ask somebody"* | *"**oh let me** ask somebody"* | oh let me |
| `[00:18:11]` | *"**Caggyen**"* | *"**cad yin**"* | CAD/JPY |
| `[00:28:19]` | *"market maker **effects** training"* | *"Market Maker **Effects** training"* | MMFX — **both wrong, identically** |
| `[00:23:55]` | *"29th **Steve Marr** market maker FX trades"* | — | Steve Mauro |

**A fabricated transcript does not invent its own mishearings, and it certainly does not invent
mishearings that a second engine independently reproduces** (`market maker effects`) *while
disagreeing on others* (`trade`/`tray` tables). The final window's 0.977 is the strongest single
number: at the point where the file ends, two engines agree almost exactly, including that
nothing follows.

**3. The rendered slides match the words, at the timecode the words carry.** Required by
`SWF_CAPTURE_RECIPE.md` GOTCHA 4 and performed **before** any long capture was trusted. The
screenshot sweep's frame at presentation time **20:00** (its own burned-in timecode reads
`20:00 / 43:0x`) shows a **EUR/CAD M15 chart** with `EURCAD,M15` selected in the platform's pair
tab strip and an `EC` watermark. The transcript at `[00:19:57]` reads *"There's a multi-day W in
**E.C.**"* and at `[00:20:00]` *"Setting up last week on the **22nd**"* — the chart's x-axis
prints **21–22 Mar 2012**. Content, burned timecode and transcript marker agree.

**4. Timestamp structure.** Measured, not asserted — see COVERAGE above.

**What verification does NOT establish:** that every word is right. It establishes that this is
a real ASR of this file, complete to the file's own end, with its timestamps in order and its
markers landing on the right slides. Individual words remain MEDIUM confidence and every
quotation drawn from it in `03_LESSON_NOTES/` carries its marker so a reader can re-listen.

## ⚠ ONE SPEAKER, AND HE IS NOT THE COURSE AUTHOR — FOURTH CONSECUTIVE LESSON

**Speaker identification was performed BEFORE any note was written**, as `DECISIONS.md`
**D-033** provision 1 requires (re-adopting `D-025` consequence 3 verbatim), and as
`COURSE_PROGRESS.md`'s V07 GATE carry-forward item (a) instructs.

**V08 has no course-author segment at all.** This is the **fourth consecutive lesson** with zero
course-author runtime (V05, V06, V07, V08). Under **D-033** — owner direction 2026-08-13, *"all
knowledge is created equal"* — that **no longer demotes anything**: every statement below is
**NORMATIVE evidence at equal weight** with the course author's. It is recorded because `D-033`
keeps speaker attribution mandatory, not because it lowers the material's standing.

| Speaker tag | Runtime | Basis |
|---|---|---|
| `GUEST` | **00:00:00 – 00:42:58, 100%** | the four lines of evidence below |
| `INSTRUCTOR` (Steve Mauro, the course author) | **none** | — |

**1. He refers to Steve in the third person, fifteen times, and never once addresses the room as
Steve.** The token `Steve` occurs **15 times** in the verbatim body. Every one is third-person:

| Marker | Words |
|---|---|
| `[00:00:32]` | *"**Steve** asked me to do something for 90 minutes to two hours."* |
| `[00:04:16]` | *"Four months after my first class, I began sending **Steve** account statements…"* |
| `[00:07:46]` | *"you don't look at **Steve** or the DMR crew or the training as being the problem"* |
| `[00:08:30]` | *"is **Steve** crazy?"* |
| `[00:08:58]` | *"**Steve's** thing might be another FX sca[m]."* — the ASR prints `scan` |
| `[00:09:51]` | *"**Steve's** thing just doesn't work."* |
| `[00:10:42]` | *"**Steve's** cult as it were. I won't call it that."* |
| `[00:15:19]` | *"Is **Steve** full of shit or is the method valid?"* |
| `[00:18:45]` | *"I guess **Steve** might not be making this stuff up, huh?"* |
| `[00:19:52]` | *"**Steve**, take a breath of fresh air, you know? Take a bow or something."* |
| `[00:24:47]` | *"I believe **Steve's** thing works now."* |
| `[00:23:55]` | *"Ladies and gentlemen, 29th **Steve Marr** market maker FX trades from last week."* — `Steve Marr` is the ASR's rendering of Steve Mauro |
| `[00:32:17]` | *"box tool which is what **Steve** showed you"* |
| `[00:32:30]` | *"Our friend **Steve Wilson** created the screenshots EA"* — a **different Steve** |
| `[00:35:22]` | *"Go back and listen to **Steve** recording on that."* |

`[00:19:52]` is the decisive one and it is worth reading twice. *"Steve, take a breath of fresh
air, you know? Take a bow or something. This stuff really works. All right, buddy?"* — that is a
man **congratulating** the course author, in the second person, **from the podium**, in front of
the class. It is not something the course author says. `[00:32:17]` is the same shape from the
other side: he tells the class to go back to **Steve's** recording for the box tool rather than
re-teaching it.

**2. He positions himself as a student who took the course, not as its author.** `[00:04:16]`
*"Four months after **my first class**"*; `[00:28:19]` *"**Three months into** the market maker
[FX] training, I began to notice M's and W's after they formed"*; `[00:28:41]`–`[00:28:45]` *"I didn't go to
OTA. I didn't have a lot of time invested in trading. **I was a musician.**"* The course author
does not describe his own three-month struggle to learn his own method.

**3. He is programme staff who runs the DMR.** `[00:32:35]` *"**Every Monday in the DMR I show**
on the hard right edge motion flashcards"*; `[00:32:50]` *"**Come join me** for an hour or so in
the DMR"*; `[00:35:26]`–`[00:35:28]` *"**come join us** in the DMR. **We** can bring this to you every
Monday."* This is the same first-person-plural staff voice V06's and V07's presenters used.

**4. Acoustic screen — one voice, no handover.** `05_HOMEWORK/V06/scripts/f0_profile.py`, run
unmodified over this lesson's 8 kHz mono audio, returns **median F0 = 145.5 Hz** with **22**
two-minute block medians spanning **137.9 – 153.8 Hz**, **sd = 5.1 Hz**, and **no step
anywhere**. The same tool resolves V04's known mid-file handover as a visible step; there is
none here.

> **This screen is used ONLY as evidence of a handover WITHIN this file**, which is what it was
> validated for. It is **not** used to identify a speaker **across** files, and no claim in this
> transcript or in any V08 artifact depends on comparing this number to V05's, V06's or V07's.
> The prohibition is `COURSE_PROGRESS.md` V06 GATE item (a), observed in V07 and observed again
> here.

### WHO THE GUEST IS — PROVENANCE, AND ONE THING THIS SESSION COULD NOT RESOLVE

The title slide prints **"Jim's Journey in Learning and Trading MMFX"** (frame
`V08_00-00-05`), and the speaker narrates that deck in the first person throughout — *"**my**
trading sanctuary"* `[00:01:25]`, *"here's **my** hobby"* `[00:02:03]`, *"**my** trading partner,
number one, Josh"* `[00:02:21]`, *"**I was a musician**"* `[00:28:45]`. V07's presenter, a
different guest, announced at V07 `[00:07:38]` *"**Jim**, I'm going to do a presentation there
but he seems to be a master at the high of the day"* — and the second half of **this** lesson is
the **high-low drill**. The chain is coherent and the natural reading is that the speaker is Jim.

**One datum does not fit, and it is recorded rather than smoothed away.** At `[00:17:29]`, mid
chart-walkthrough, the speaker says *"Okay, **Jim's right** about that one."* Re-transcribed
independently with Whisper **`large-v3`** on the raw audio, which returns the same words. Three
readings are available — a second Jim among the participants (V07's audience carried sixteen
named questioners), a live chat comment being acknowledged, or a mishearing that two engines
share — and **this session does not choose between them.**

**Nothing in any V08 artifact depends on the identification being right.** That is `D-025`
consequence 4, re-adopted verbatim as `D-033` provision 2. The speaker tag used throughout is
`GUEST`, which is what carries evidentiary weight; the name is provenance and is recorded at the
confidence it actually has, which is *probable and unresolved*.

## TRANSCRIPTION NOTES

- **ASR mishearings are preserved, not corrected.** The body below is byte-identical to the
  pre-ingestion file's `# VERBATIM TRANSCRIPT` section. Where a word is plainly wrong the
  correction is made **in the notes, with the marker**, never in the transcript.
- Known systematic errors, established above and by reading in context: `effects` = **FX**;
  `Steve Marr` = **Steve Mauro**; `Caggyen` = **CAD/JPY**; `trade tables` = **tray tables**;
  `stop-homp box` `[00:21:19]` = **stop hunt box**; `ERO` = **EUR** throughout §"the 29 setups";
  `N's and W's` = **M's and W's** at `[00:28:19]`, `[00:29:14]` and `[00:31:56]`, against the correct `M's and W's` at `[00:11:26]`, `[00:15:11]` and `[00:24:12]` (the ASR renders the same
  phrase both ways within four minutes, which is itself an ASR signature).
- **Pair shorthand used by the speaker**, expanded here once so the notes need not re-derive it:
  `CJ` = CAD/JPY, `EC` = EUR/CAD, `EU` = EUR/USD, `EJ` = EUR/JPY, `GJ` = GBP/JPY, `GC` = GBP/CAD,
  `pound Aussie`/`pound Ozz` = GBP/AUD, `Aussie USD` = AUD/USD, `Aussie Yen` = AUD/JPY,
  `Swiss Yen` = CHF/JPY, `USD CAD` = USD/CAD. **This is the speaker's own usage read from
  context, and where a frame shows the platform's pair tab it is corroborated there.**
- No crosstalk, no second voice, no audience audio anywhere in the file. Unlike V07, **no
  questions are read out** — this lesson is a continuous presentation.

---

# VERBATIM TRANSCRIPT

[00:00:00]
I want to give you guys a little journey in how I learned and traded the Market Maker

[00:00:06]
FX method.

[00:00:07]
Okay, since we're doing this bootcamp, I've attempted to gear my presentation for various

[00:00:14]
levels of traders.

[00:00:17]
And essentially what we're going to do is blast through two sections of what I have

[00:00:23]
prepared.

[00:00:24]
We'll take a five minute break.

[00:00:26]
Then I'll come back and do the third section and the DMR.

[00:00:29]
Okay, so we're probably going to fill up about two hours.

[00:00:32]
Steve asked me to do something for 90 minutes to two hours.

[00:00:36]
And that's kind of what I have here.

[00:00:38]
So it's going to be a jam pack transmission for you guys.

[00:00:41]
Put up your trade tables in the upright and locked position and get ready for take off.

[00:00:46]
We have a lot of information to cover.

[00:00:49]
I may or may not be able to be as responsive as Ray was with the questions.

[00:00:55]
But you guys are asking a lot of great questions.

[00:00:57]
It makes me very happy to have a lot of material assembled here, which seems to be relating

[00:01:05]
to the questions that I've heard come up.

[00:01:07]
Okay, we want to make this boring and that's essentially how we want to trade.

[00:01:12]
All right, so hopefully my path can smooth the way for others.

[00:01:17]
And I know there's some new folks on board here.

[00:01:19]
I wanted to give you guys a kind of a little small bio of myself.

[00:01:25]
This is my trading sanctuary.

[00:01:27]
Okay, many, many hours logged here.

[00:01:30]
You can see it's got some musical instruments as well.

[00:01:33]
So we have a lot of fun in between the formations happening.

[00:01:38]
You can see three monitors of cross top.

[00:01:40]
That's where I keep my main trading platform.

[00:01:42]
I do a lot of trade execution off my laptop and the secondary monitor.

[00:01:46]
I have a television that also serves as a monitor off to my left.

[00:01:50]
And this one has since blown up.

[00:01:51]
So that's no longer there.

[00:01:52]
But you can see a good amount of screen real estate.

[00:01:55]
I can say clearly if one wants to get involved with fractional disparity, it's good to watch

[00:02:00]
a lot of pairs of ones.

[00:02:02]
All right.

[00:02:03]
And here's my hobby.

[00:02:04]
All right, I'm into power boards.

[00:02:06]
You got to have something that takes you away from the charts.

[00:02:08]
If you're a junkie, you got to have something.

[00:02:10]
So this is my passion, besides looking at charts.

[00:02:14]
We got a 30-mile-frouder in four seconds, 30-mile range, finally something which can

[00:02:18]
take me away from the charts.

[00:02:21]
This is my trading partner, number one, Josh.

[00:02:23]
All right, he can't keep up with the boards, so he doesn't come along with me.

[00:02:27]
And this is his brother, my trading partner, Bear.

[00:02:30]
Okay, that's enough about me.

[00:02:32]
Let me go into my background professionally for a second because it does relate to trading

[00:02:36]
and what I've brought to the method.

[00:02:40]
Okay.

[00:02:41]
So I've worked with a lot of big names, a lot of big companies, kind of high-pressure

[00:02:47]
stuff.

[00:02:48]
And it's mostly self-taught in my self-instruments.

[00:02:52]
As you'll find, you'll have to somewhat self-teach yourself this trading method.

[00:02:56]
Although we're all here for you, at a certain point in time, you'll realize there's an

[00:03:01]
amount of effort needed on your part.

[00:03:03]
Okay.

[00:03:05]
In order to master my business, I became a devout student of the mind, the emotions,

[00:03:11]
and the subconscious mind, slash spirit, creator, force, whatever you want to call it, that

[00:03:16]
something that is basically out there, that everybody's naming, but they can't really

[00:03:20]
peg it.

[00:03:21]
I was extremely interested in this for my business back in these days.

[00:03:25]
Why was this?

[00:03:26]
Okay.

[00:03:27]
The quest was, how do I eliminate writer's block?

[00:03:30]
Okay.

[00:03:31]
As well it became, how do I keep nasty co-employees from messing with my mojo?

[00:03:37]
How do I not get down on myself if I don't win the big United Nations commercial and

[00:03:41]
somebody else wins it?

[00:03:42]
You know, all these things were turned into a calculus that led me to investigate this

[00:03:49]
stuff.

[00:03:50]
And in order to become proficient at the market maker effects system, I drew from these same

[00:03:55]
tools of knowledge and transpersonal development.

[00:03:58]
All right.

[00:03:59]
Just as many do in learning forex, I spent many thousands of dollars on transpersonal

[00:04:04]
teachings and traveled extensively in search for data I was looking for.

[00:04:09]
And fortunately, I did find it and I once started to apply it to the market maker method in

[00:04:15]
my biography.

[00:04:16]
Four months after my first class, I began sending Steve account statements with steady equity

[00:04:21]
growth month after month.

[00:04:23]
Okay.

[00:04:24]
And our James Bond music comes in now.

[00:04:26]
I'm going down, down, down, down, down, down, down, down, down, down, down, down.

[00:04:29]
If you do a kill, and the best part, and how to not get killed.

[00:04:35]
All right.

[00:04:36]
Got our crosshairs there.

[00:04:38]
That one's for Nelson.

[00:04:40]
Okay.

[00:04:41]
Section one tonight is going to be a brief map of the stages of learning this method.

[00:04:47]
What are our vulnerabilities at each stage?

[00:04:51]
How can we identify which stage we are at with it?

[00:04:55]
Okay.

[00:04:56]
When I look back on my path and I see what I went through, I see these distinct stages

[00:05:01]
that I've outlined for you guys that hopefully will help a lot of people, especially those

[00:05:04]
people out here that haven't really broken through the outer barrier yet.

[00:05:07]
All right.

[00:05:08]
So I'm looking back at my path and I've put down everything that's gone into it.

[00:05:13]
So you guys can possibly take a piece of information forward with you.

[00:05:17]
Again, it's only my path.

[00:05:19]
So we all come about things differently, but we can learn from others mistakes hopefully.

[00:05:24]
And I see us as a group making big strides.

[00:05:26]
One person innovates, another person.

[00:05:28]
We were just, it's really good.

[00:05:30]
You guys are in a really good spot.

[00:05:31]
Okay.

[00:05:32]
Section two, of course, is of you a kill.

[00:05:35]
The high low drill and elements of mastery for dealing with intent pips of high day and

[00:05:40]
low day.

[00:05:41]
How doing the high low drill teaches one the timing aspect of price action or the speed

[00:05:47]
of price.

[00:05:48]
Okay, we have pattern and we have the speed of price.

[00:05:51]
We'll be going to that in the second half.

[00:05:53]
Take a break.

[00:05:55]
And then section three is how to not get killed.

[00:05:58]
Okay.

[00:05:59]
Some of the information that Ray was beginning to answer with people is leading excellently

[00:06:04]
into this topic.

[00:06:05]
It's going to be a defined risk lesson so that you will never again blow up an account.

[00:06:12]
Okay.

[00:06:14]
Now let's start with a map of the stages of learning the market maker forex system.

[00:06:20]
Okay.

[00:06:21]
I see it as four distinct levels and I'm going to go from the ideal on out and then

[00:06:27]
we'll go back in again slowly.

[00:06:29]
So what are you all here for?

[00:06:32]
Are you here to get good M&W trades?

[00:06:34]
Are you here to get your 50 pips?

[00:06:36]
Well, that's part of it.

[00:06:38]
What are you really, really here for?

[00:06:41]
You're here for steady equity growth.

[00:06:43]
Okay.

[00:06:44]
So the ultimate ideal, the inner circle of this method is steady equity growth.

[00:06:50]
That's when it gets very boring.

[00:06:52]
You're almost mechanical in what you do and week after week, you're pulling statements

[00:06:57]
that are going up, up, up, up.

[00:06:59]
That is the objective.

[00:07:00]
That's the ideal.

[00:07:01]
Okay.

[00:07:02]
The next area before this as we pan out from our ideal into the beginner side so we can

[00:07:08]
consider beginners out here advanced guys in here.

[00:07:11]
As guys, steady equity growth, they have that.

[00:07:14]
Just before they got to that, okay, they were able to instantly recognize confirmed M&W entries.

[00:07:24]
But what do I mean by that?

[00:07:27]
That's being able to spot the pattern before price moves in your favor.

[00:07:32]
Okay.

[00:07:33]
We're going to go into this.

[00:07:34]
This is sort of a preparatory on all these stages.

[00:07:38]
The next outer band is, I am no longer skeptical about the method as I look to my own actions

[00:07:44]
which need improvement.

[00:07:46]
This is where when a mistake is made, you don't look at Steve or the DMR crew or the training

[00:07:52]
as being the problem, you say, okay, where did I make a mistake?

[00:07:56]
What did I not see properly?

[00:07:58]
Okay.

[00:07:59]
This is another distinct area which is separated by a strong shell.

[00:08:03]
It's a metal case around here if you ask me.

[00:08:06]
Actually, these are very strong barriers between each of these sections.

[00:08:11]
At least they were for me.

[00:08:13]
That's why I'm bringing this to you guys.

[00:08:15]
The next band out from there is when someone is looking at the setups of the previous week

[00:08:21]
with their own eyes to see if the method works.

[00:08:26]
It's amazing how many people will study this material and they won't go back over the week

[00:08:30]
and say, you know, is Steve crazy?

[00:08:32]
All of me ask somebody about that.

[00:08:34]
Oh, you want to do it with your own eyes.

[00:08:36]
So this band out here is characterized by somebody looking at setups with their own

[00:08:41]
eyes.

[00:08:42]
Not asking what it's about.

[00:08:45]
Then we have the outer bands.

[00:08:49]
There are certainly people in our group that have not taken the time to validate the setups.

[00:08:54]
They're out here in this outer band and what are they asking?

[00:08:58]
Steve's thing might be another FX scan.

[00:09:01]
They say I may as well just trade the weather.

[00:09:04]
I wonder if anyone is really doing well live with this method.

[00:09:08]
I want to know what others think of it.

[00:09:11]
These are the thoughts that go on when you haven't grounded yourself.

[00:09:15]
And then the Darkstar approach of planet market maker.

[00:09:20]
Mythical trading ideas which induce retail traders to lose but sound cool.

[00:09:29]
This has got a gravitational pull when you're out here and you haven't put the time to validate

[00:09:33]
this method.

[00:09:34]
These things are going to pull you in.

[00:09:35]
The next thing that comes along, the next cool nice trading style comes along.

[00:09:40]
This is a draw.

[00:09:41]
It's going to be yanking at you.

[00:09:45]
As well what someone would say when they're out here.

[00:09:47]
I missed that trade.

[00:09:48]
I moved my stop loss and took a 25% hit on my account.

[00:09:51]
Steve's thing just doesn't work.

[00:09:53]
Hey man, check out these stochastic bands.

[00:09:58]
It's an indie that an FX, MFX student made.

[00:10:01]
Now you can't lose.

[00:10:04]
This next body approaches you when you're out in this area and you haven't grounded yourself

[00:10:08]
with your own eyes.

[00:10:09]
I call it planet FX marketing.

[00:10:12]
Indicators and trainings which are in fact scams as those who sell don't trade.

[00:10:16]
Of course, that's a generalization.

[00:10:19]
There are people out there that are making neat stuff.

[00:10:20]
There are ex-MMFX students.

[00:10:22]
No question about it.

[00:10:23]
I'm just giving a hyper example here.

[00:10:26]
You know what I mean?

[00:10:27]
This is like the next little dohic you can throw in your chart.

[00:10:30]
Sometimes you haven't put your own eyes on the setups.

[00:10:33]
You're susceptible to this poll of marketing people giving you a nice fancy thingies you

[00:10:38]
can put on your charts.

[00:10:39]
That stuff is going to pull you out of orbit.

[00:10:42]
Steve's cult as it were.

[00:10:44]
I won't call it that.

[00:10:47]
So how's it going with that indie?

[00:10:48]
Oh man, I think I'm going to have to take a break from trading.

[00:10:51]
This stuff is impossible.

[00:10:53]
These are the thoughts that are going to hit when you're out there.

[00:10:58]
What is our first objective when we first come in line with this method?

[00:11:01]
We want to break this first fine veil and that is that I'm not sure with my own eyes

[00:11:06]
if the method is valid.

[00:11:09]
And these people can bounce off.

[00:11:11]
They're repelled.

[00:11:13]
These people will often bounce off the method because they have not validated it for themselves.

[00:11:21]
Two hours a week after the market closes on Friday, by just looking at the charts across

[00:11:26]
ten or more pairs will show that M's and W's are setting up according to the method without

[00:11:31]
fail and have been doing so for years.

[00:11:38]
A person on the outer bands of the method will be subject to intense interferences of

[00:11:42]
opinion.

[00:11:45]
People will be faced with their true belief or lack of it when a large loss occurs from

[00:11:49]
trading life.

[00:11:51]
If they have not yet validated it with their own eyes, they will assume it's an invalid

[00:11:56]
method.

[00:11:57]
They will tend to gather in groups of such injured people and will nourish their belief

[00:12:02]
with idle chatter from the tree tops.

[00:12:05]
Like monkeys, aint it.

[00:12:07]
Back, back, back, back, back, back, back, back, back, back, back, back, back, back.

[00:12:11]
These people as well, they'll bounce off.

[00:12:14]
We are trying to at this point bring everybody that's in this outer circle back in.

[00:12:19]
This first entire section of this transmission is based on trying to form a stronger pull

[00:12:25]
of gravity.

[00:12:26]
If anybody is out here and they have bounced off, they're going to pull them in at least

[00:12:30]
to this first level, maybe to the second, maybe to the third and then time they'll come all

[00:12:34]
the way in.

[00:12:35]
In order to do that, we need to look at a little transpersonal stuff.

[00:12:41]
We're looking at the missing puzzle piece in our brain.

[00:12:44]
If we've been given the last piece of the puzzle from the guy that was taught from the

[00:12:48]
market maker, it's logical to assume that the thing missing is in us.

[00:12:54]
What is it that's missing?

[00:12:55]
Why are there people who are not inclined to look for themselves and validate the method?

[00:13:02]
Why are there some people like that?

[00:13:05]
The answer is we have been conditioned since early childhood to believe authority is the

[00:13:09]
truth and to not seek truth as the authority.

[00:13:16]
The power of what someone else says is a powerful motivator for us.

[00:13:20]
It's in our training.

[00:13:23]
The educational system since the late 1800s has been set up to encourage belief, not fact

[00:13:30]
seeking.

[00:13:33]
It has rewarded conformity and memorization and is not taught independent investigation,

[00:13:39]
analysis, nor critical thinking.

[00:13:44]
Depression-based origins of modern education have perpetuated a snow-white mentality where

[00:13:51]
we constantly look outside of ourselves for our answers.

[00:13:56]
What someone says about something also that we unquestionably follow the herd when told

[00:14:04]
to do so.

[00:14:06]
There are documents of the creation of the PhD and education system that prove this point

[00:14:13]
in the creator's own words.

[00:14:15]
They wanted to get people to be able to go to war easily.

[00:14:19]
Hate to be the bad guy.

[00:14:21]
Don't shoot the messenger.

[00:14:22]
It's true.

[00:14:23]
I'm sorry.

[00:14:24]
Not my fault.

[00:14:26]
The sooner you realize no one else can validate the method for you, the clearer you are about

[00:14:32]
what needs to happen.

[00:14:35]
Do it yourself.

[00:14:37]
No Skype group is going to be able to validate this method for you.

[00:14:42]
The more we go back into the week on the charts and find M&W's which worked out, the

[00:14:49]
more of these we see with our own eyes, the less we are going to look outside of ourselves

[00:14:56]
for someone else's opinion.

[00:14:59]
We want to validate the method.

[00:15:04]
We've broken through our outer shell.

[00:15:07]
First breakthrough.

[00:15:09]
Let's go validate the method.

[00:15:11]
How many M's and W's set up last week, not last year or last month, but last week.

[00:15:19]
Is Steve full of shit or is the method valid?

[00:15:24]
Here's your market maker FX weather report, week of March 19th, 2012.

[00:15:30]
Uh oh, the Death Star approaches.

[00:15:34]
And Planet Market team is approaching as well.

[00:15:38]
But that's okay.

[00:15:39]
You'll find a way out of this.

[00:15:41]
So we had two M&W set ups in the London session on Monday of last week.

[00:15:48]
We had one M&W set up in the New York session.

[00:15:53]
On Tuesday we had one at London.

[00:15:56]
We had one at New York.

[00:15:59]
On Wednesday we had five M&W set ups in the London session.

[00:16:03]
We had one M&W set up in the New York session.

[00:16:07]
On Thursday we had eight M&W set ups in the London session and one in the New York session.

[00:16:15]
On Friday we had six M&W set ups in the London session and three in the New York session.

[00:16:22]
Oh my God, that's 29 set ups.

[00:16:26]
Okay.

[00:16:27]
I hope some of these brain cells are frying here because that right there is the thing

[00:16:32]
that got me out of all this chatter that I was subjected to a couple hours after signing

[00:16:38]
up for the course, of course.

[00:16:40]
29 set ups last week guys and it's not the only week that's happened.

[00:16:44]
I've done this in CM35, 37, 40, 28.

[00:16:48]
Okay, the numbers up there.

[00:16:50]
These are verifiable.

[00:16:51]
So with this kind of information we can get rid of the Death Star.

[00:16:58]
By now, and we can possibly get rid of the marketing guys.

[00:17:04]
Watch the red dot.

[00:17:06]
Sorry dude, not buying a crap anymore.

[00:17:11]
Okay, we reduced them to what they should be, figments from our past.

[00:17:17]
Then we go.

[00:17:19]
You guys want to look at 29 set ups from last week?

[00:17:22]
That's what I'm here for.

[00:17:24]
Here's CJ.

[00:17:25]
It's a nice W coming right down into the stop hunt box.

[00:17:29]
Okay, Jim's right about that one.

[00:17:31]
Oh, another nice W picture perfect into the stop hunt box.

[00:17:35]
This was last Monday.

[00:17:37]
Okay.

[00:17:38]
In the New York session, we got a nice M pattern into the New York shadow box also in the stop

[00:17:46]
hunt box.

[00:17:47]
Beautiful.

[00:17:48]
And on to Tuesday, we have a beautiful level one rise and this one is in Asia.

[00:17:53]
I put this on here.

[00:17:54]
I kind of cheated.

[00:17:55]
I consider this London session because I'm up during this entire period and that's in

[00:17:59]
the pound Aussie.

[00:18:00]
Aussies will tend to move in Asia.

[00:18:02]
All right.

[00:18:03]
Either way, anchor in the bottom W off the mail in the middle of Asia.

[00:18:08]
Beautiful setup thing took off.

[00:18:11]
Continuing on, we have Caggyen, which set up in the European session through a nice

[00:18:15]
pin to the high, big multi-day M. Guess what?

[00:18:19]
I took it.

[00:18:21]
Okay.

[00:18:23]
Down she went.

[00:18:24]
A couple of high grabs.

[00:18:25]
We're getting into a little of that.

[00:18:26]
I'll show you guys what cooks in that department.

[00:18:29]
Let's continue on.

[00:18:30]
Okay.

[00:18:31]
This is the Aussie USD, European M formation last week.

[00:18:37]
We've got another New Zealand USD M formation right in the shadow box.

[00:18:44]
London.

[00:18:45]
I guess Steve might not be making this stuff up, huh?

[00:18:48]
But a beautiful M and GJ.

[00:18:50]
Okay.

[00:18:51]
We're on the Wednesday.

[00:18:52]
We got an M right in the stop hunt box.

[00:18:58]
Beautiful fade.

[00:18:59]
Easy 50 there, huh?

[00:19:01]
And we got a nice complex multi-session M in EU.

[00:19:05]
Right?

[00:19:06]
In the European session, beautiful trade.

[00:19:10]
Have another M three hits to the high and then descending pattern on the EJ.

[00:19:14]
Okay.

[00:19:15]
Up in the middle of the London session, hitting the stop hunt box.

[00:19:20]
We have a beautiful W and G.C.

[00:19:22]
Do you guys see this pair last week?

[00:19:25]
Unbelievable.

[00:19:26]
I mean, this is a gimme.

[00:19:28]
New York session, beautiful lawn.

[00:19:29]
Got your 50 easy.

[00:19:31]
Remember, this stop hunt box is 25 pips.

[00:19:33]
So you can always gauge what size these candles are.

[00:19:37]
Moving on, we have Euro laws.

[00:19:39]
Just gave this very nice end to the high railroad track.

[00:19:43]
Pull back inside the European session shadow box.

[00:19:46]
Okay.

[00:19:47]
We're up there in numbers now, guys.

[00:19:49]
These are all in front of us.

[00:19:50]
Last week.

[00:19:51]
Okay.

[00:19:52]
Steve, take a breath of fresh air, you know?

[00:19:54]
Take a bow or something.

[00:19:55]
This stuff really works.

[00:19:56]
All right, buddy?

[00:19:57]
There's a multi-day W in E.C.

[00:20:00]
Setting up last week on the 22nd.

[00:20:02]
All right.

[00:20:03]
22nd was a Thursday.

[00:20:05]
Beautiful.

[00:20:06]
Outside.

[00:20:08]
Inside formation here.

[00:20:09]
And up you went straight to profit in E.C.

[00:20:13]
And we had a very nice M. Actually, this is two setups.

[00:20:16]
Well, I'm going to look at this W off the anchor formation low.

[00:20:19]
This is a level one big multi-day W. Powerful trade.

[00:20:24]
Up it went.

[00:20:26]
Another trade back in the range from the shadow box.

[00:20:28]
Not quite for 50, but it was there.

[00:20:29]
All right.

[00:20:30]
Got an easy 50 on this one.

[00:20:32]
These are continuation Ws.

[00:20:34]
Continuation Ws are basically a W that has anchor formation off to the left.

[00:20:38]
Beautiful trade.

[00:20:40]
Moving on.

[00:20:41]
E.J.

[00:20:43]
Anchor formation to the top left.

[00:20:46]
These tight age range.

[00:20:47]
Information off the male.

[00:20:49]
Like Ray.

[00:20:50]
I jumped on this one as well.

[00:20:52]
I could not.

[00:20:53]
You have to like fight me to get to the mouse on this one.

[00:20:56]
All right.

[00:20:57]
Great trades.

[00:20:58]
Similar in the GJ, an M. Almost off the male.

[00:21:02]
Anchor formation off the left.

[00:21:04]
Can you believe this is all one week?

[00:21:06]
All right.

[00:21:07]
It's ironic, but it's true.

[00:21:08]
For people to go and say this is garbage.

[00:21:11]
All right.

[00:21:12]
I don't know how you can do that and actually look at the charts.

[00:21:14]
All right.

[00:21:15]
Again, these are 25-pip in size.

[00:21:19]
Stop-homp boxes.

[00:21:20]
Here you have a nice multi-session M, Asia session and London session.

[00:21:24]
Nice pin to the high.

[00:21:25]
You can do this the order is the other direction.

[00:21:27]
Pull it away.

[00:21:28]
Easy 50 back to the water in pound Ozz.

[00:21:31]
It's like we're getting almost into Friday here.

[00:21:33]
Having gotten to Friday, guys.

[00:21:35]
Okay.

[00:21:36]
A very nice continuation M formation on the ERO USD.

[00:21:42]
This was your high of weak.

[00:21:44]
Anchor to the high.

[00:21:45]
First leg, second leg, railroad track, entry.

[00:21:50]
Down you go.

[00:21:52]
Oh, goodness.

[00:21:53]
I got that one too.

[00:21:54]
Funny trading the DMR we talked about.

[00:21:56]
I fell asleep in my chair during this railroad tracker.

[00:21:59]
Probably would have gotten it at the top, but either way, it would have supposed to do

[00:22:02]
because we've studied these anchor formations a lot and we know that in level one, things

[00:22:07]
going to continue.

[00:22:08]
All right.

[00:22:09]
So levels are good stuff, guys.

[00:22:10]
No question.

[00:22:11]
And on to the Swiss Yen.

[00:22:13]
Also last week, we're in the 22nd, still Thursday, an M formation off the Mayo.

[00:22:19]
Now it looks like we're about to get into Friday and we have in the New York session

[00:22:25]
a nice W in your ERO USD.

[00:22:28]
All right.

[00:22:29]
Continuing on, we have a beautiful M formation on the Swiss Yen in New York on Friday.

[00:22:37]
Beautiful M to the high.

[00:22:38]
Down she went.

[00:22:39]
Easy 50 on that one.

[00:22:41]
ERO formation in the Aussie Yen.

[00:22:43]
Got a nice three hits to the high.

[00:22:45]
Multi session M.

[00:22:46]
Pull it away.

[00:22:47]
What a week, huh?

[00:22:50]
This happens a lot.

[00:22:51]
This is not anything unusual.

[00:22:54]
ERO Aussie, complex M to the high with a beautiful pin.

[00:22:58]
Break the range.

[00:22:59]
Pull it back down.

[00:23:00]
Easy entry.

[00:23:01]
Easy 50.

[00:23:02]
Okay.

[00:23:03]
We're almost done with the week.

[00:23:04]
M to the high.

[00:23:05]
ERO Yen.

[00:23:06]
Pull that away.

[00:23:07]
I mean, this stuff is crazy.

[00:23:09]
GJ, same thing.

[00:23:12]
M off the Mayo.

[00:23:15]
And pound dollar.

[00:23:16]
Really beautiful, nice multi-day M. Pulled through yesterday's high.

[00:23:21]
Pulled it away inside bar.

[00:23:23]
Easy 50 grab on that trade.

[00:23:26]
Aussie USD.

[00:23:28]
Beautiful.

[00:23:29]
Multi session W.

[00:23:30]
Three hits to the low.

[00:23:32]
Pin to expand the range and up we go.

[00:23:36]
Easy 50.

[00:23:39]
And Aussie.

[00:23:40]
M to the high.

[00:23:41]
Three hits to the high.

[00:23:42]
Nice pin to the ADR.

[00:23:45]
Back down and easy 50 or more.

[00:23:48]
And the USD CAD.

[00:23:49]
One of my all time favorites.

[00:23:51]
Beautiful.

[00:23:52]
M to the high and pull it away.

[00:23:54]
Down we go.

[00:23:55]
Ladies and gentlemen, 29th Steve Marr market maker FX trades from last week.

[00:23:59]
Are you still doubting?

[00:24:01]
I hope not.

[00:24:02]
You'd have to be kind of silly to doubt this stuff at this point.

[00:24:06]
Okay.

[00:24:07]
We validated the method.

[00:24:09]
We broke him through the first layer.

[00:24:12]
One knows these M's and W's are setting up as described.

[00:24:17]
Gravity is taken hold.

[00:24:18]
One is no longer led astray by others idle chatter.

[00:24:22]
It now becomes worth it to keep digging and to keep studying to get the next stage of

[00:24:27]
this learning of this method.

[00:24:30]
Once the facts are seen with one's own eyes, no amount of persuading can lead them away

[00:24:36]
from what they know to be true.

[00:24:37]
The dream is possible now.

[00:24:40]
Okay.

[00:24:43]
Our next threshold.

[00:24:44]
And it's like a piece of lead.

[00:24:46]
Okay.

[00:24:47]
I believe Steve's thing works now.

[00:24:48]
What's the next area of interference I'm going to hit?

[00:24:52]
It's when we are not able to fully act in line with the method.

[00:24:57]
Okay.

[00:24:58]
I'm still the slightest bit skeptical and can't yet act with precision according to the method.

[00:25:04]
I don't trust myself to carry through on it.

[00:25:08]
I am looking to bend the rules, pose my ideas on it, and when I get stopped out, I go back

[00:25:12]
and blame the method.

[00:25:14]
The only care for this is to take the first step and go back in the charts and validate

[00:25:19]
the method.

[00:25:20]
Explore W's and M's as they happen during the week and make flashcards of them.

[00:25:26]
Okay.

[00:25:27]
So you're going to hit this next area and you will tend to be pulled out again.

[00:25:30]
Gravity is going to pull you away.

[00:25:33]
When we know the method is valid, we then turn to the next layer in, which is working

[00:25:38]
with our ability to act in line with it.

[00:25:42]
When we take a stop out, we look at ourself and don't blame the method.

[00:25:46]
All right.

[00:25:47]
So the next layer in is to eliminate skepticism.

[00:25:50]
Okay.

[00:25:51]
And it's easy to see why we sometimes bend the rules on a method.

[00:25:55]
We've been given so much garbage that hasn't worked that we think we can only beat the

[00:26:00]
forex by fluke.

[00:26:02]
Okay.

[00:26:03]
This is where the Snow White mentality enters in.

[00:26:07]
The remaining skepticism will act as a drag on our ability to act within the method.

[00:26:14]
And I went through this stuff without question.

[00:26:17]
Honest engine, this is my journey and I'm just trying to lay it out.

[00:26:20]
So the few people that are going to have a similar journey, you can take my loss and

[00:26:24]
make it your gain as fast as possible.

[00:26:26]
All right.

[00:26:27]
So once you do find that these patterns are consistent, weekend and week out, a party

[00:26:32]
will start to tend to cause some drag, which is kind of the way it is.

[00:26:36]
Again, since we've been trained to seek approval of the herd before feeling good about doing

[00:26:42]
something, we know deep down we are going against the herd here and a part of us gets

[00:26:47]
rattled.

[00:26:50]
And this is a good thing because it just means we have to practice to become good at

[00:26:54]
something new.

[00:26:55]
All right.

[00:26:57]
I can't put enough emphasis on this.

[00:26:59]
It's a good thing to be at that stage.

[00:27:01]
All right.

[00:27:02]
So your frustration becomes your new order of opportunity to get better.

[00:27:07]
All right.

[00:27:08]
So to get good at something, it just takes experience and repetition.

[00:27:12]
We need to bring our actions in line with the method and leverage our subconscious mind

[00:27:18]
to internalize set up recognition and near automatic actions.

[00:27:23]
And there are two ways that we go about doing this.

[00:27:25]
One is the high low drill and the other is hard right edge pattern training.

[00:27:31]
I missed the tee there, but that's all right.

[00:27:33]
We get the idea.

[00:27:34]
So let's take a look at looking at these charts on the hard right edge and what that

[00:27:37]
means.

[00:27:38]
As soon as you're able to eliminate skepticism and you begin to hone your actions in line

[00:27:44]
with the method, you're going to come up against this next metal door.

[00:27:48]
It feels like it hit it with a thud.

[00:27:50]
All of a sudden you wake up and realize I can see him in W patterns clearly after they

[00:27:55]
form, but I can't see him before they form.

[00:28:00]
And so what we do is we take an ideal setup and then we chop it back.

[00:28:06]
So we're now looking at the setup as it would be at the best possible entry on the hard

[00:28:11]
right edge.

[00:28:12]
How do we come about getting to this place?

[00:28:14]
I want to kind of go into a little bit of history here because this is something that

[00:28:17]
plagued me.

[00:28:19]
Three months into the market maker effects training, I began to notice N's and W's after

[00:28:23]
they formed.

[00:28:24]
It took me that long to get to that next layer guys, three months before I could actually

[00:28:28]
get into the next ring and banging my head on that next pipe.

[00:28:34]
It was frustrating as heck.

[00:28:35]
So I look for a way to be able to spot them before they formed.

[00:28:39]
Couldn't figure out how to do it.

[00:28:41]
I didn't go to OTA.

[00:28:42]
I didn't have a lot of time invested in trading.

[00:28:45]
I was a musician.

[00:28:46]
So here I am trying to figure this out.

[00:28:49]
I would spend many hours on weekends marking up charts.

[00:28:52]
And one day I just decided to buy a bamboo tablet to be able to freehand mark up the

[00:28:56]
chart.

[00:28:57]
I figured if I'm going to sit here and mark up these charts for five hours, I can do it

[00:29:00]
by hand and maybe cut it down to two hours.

[00:29:02]
I knew the method worked so I was going at it.

[00:29:05]
The gravity had pulled in and I was going into it.

[00:29:08]
This bamboo right here is actually the cause of a lot of what we're all doing right now,

[00:29:13]
which is a good thing.

[00:29:14]
The issue was I was spending hours looking at fully formed N's and W's.

[00:29:18]
I wasn't looking at this kind of stuff.

[00:29:22]
This gets into a little bit of the transpersonal stuff, which takes just a minute to look at

[00:29:25]
it.

[00:29:26]
Hopefully you guys can see this.

[00:29:27]
I'm going to blow it up so you can very clearly sit.

[00:29:31]
And that is strong ideas held in the conscious mind will sink and lodge into the subconscious

[00:29:38]
mind.

[00:29:41]
The catch is those ideas or pictures have to be clear and exact.

[00:29:48]
I'm not going to go into why and how and all this stuff and the studies that actually

[00:29:52]
validate this and go off my faith here.

[00:29:55]
I spent 20 years studying this stuff for music and I can tell you it's absolutely true.

[00:30:00]
When you want something, you need to see a likeness of it almost to the T. You need

[00:30:04]
to see it almost exactly how it is.

[00:30:07]
Then you'll have instant recognition of what you want.

[00:30:14]
Like learning to forget the left hand while playing piano, our subconscious will alert

[00:30:19]
us that a setup is forming.

[00:30:22]
I'm sure there are people who have learned piano out there.

[00:30:25]
I can tell you this.

[00:30:26]
When you first learn piano, it's bizarre.

[00:30:30]
You can't figure out what the left hand does, what the right hand does.

[00:30:33]
The way you learn is that you train the left hand and then you forget about it.

[00:30:38]
And when you forget about it, the subconscious then takes that portion of activity and it

[00:30:43]
performs what the left hand is supposed to do.

[00:30:45]
You don't even have to think about it that much.

[00:30:47]
That's why a lot of guys here are saying this is really easy and in fact it really is.

[00:30:51]
So we're going to try to show you through this type of training that you can impress

[00:30:58]
your subconscious with an idea to the degree that when you walk up to a chart and you see

[00:31:04]
something like this, you go, honey, hang on, I got to put a trade on.

[00:31:09]
You will actually step up and execute because you've internalized exactly how it looks.

[00:31:16]
Big scientific reason that we're doing it this way guys.

[00:31:20]
So I knew at that moment my art had saved me three months into it.

[00:31:25]
I couldn't believe I hadn't taken 50 tips yet.

[00:31:28]
I know I can do this.

[00:31:29]
I know I can do this.

[00:31:30]
I'm good at computers.

[00:31:31]
But what was holding me back, I hadn't internalized what a setup looks like on the hard right

[00:31:36]
edge.

[00:31:37]
All I had to do was go back and erase the candles.

[00:31:40]
That's pretty much what I did.

[00:31:43]
I then took one step further.

[00:31:46]
Why not erase all the candles which lead up to the setup?

[00:31:50]
I could create many movies of the candles as they formed that could drill setups in a

[00:31:53]
more realistic way.

[00:31:56]
Although it took nearly eight hours on a salary to create ten movies of N's and W's from the

[00:32:01]
previous week.

[00:32:03]
My trading instantly improved.

[00:32:06]
That was June of 2011.

[00:32:12]
In the time that I learned in time I got better at it and got faster and then learned the

[00:32:17]
box tool which is what Steve showed you.

[00:32:19]
I don't have to repeat here because you guys can go back to the recording and see how you

[00:32:22]
can use the box tool to erase the part of the chart where the rest of the setup is.

[00:32:28]
Then the process became faster.

[00:32:30]
Our friend Steve Wilson created the screenshots EA which I use in the DMR.

[00:32:35]
Every Monday in the DMR I show on the hard right edge motion flashcards to help folks

[00:32:42]
who may not have the time to make these.

[00:32:44]
We understand a lot of you guys are holding one, two jobs or whatever and you don't have

[00:32:49]
the time to sit down and do this.

[00:32:50]
Come join me for an hour or so in the DMR drilling into as best I can.

[00:32:56]
I show five perfect M&W setups as they formed into Take Profit.

[00:33:01]
Every week there's been no week that there hasn't been at least five.

[00:33:04]
I have a tough time choosing which ones to take.

[00:33:06]
There's a ton of them.

[00:33:08]
This is one I missed actually from the 29th.

[00:33:11]
Here's the 30th setup.

[00:33:13]
This is CJ.

[00:33:14]
Oh no, this was the week before.

[00:33:15]
I'm sorry.

[00:33:16]
This is the 16th of March.

[00:33:17]
Anyhow, again the idea is to drill into your subconscious mind.

[00:33:21]
The exact look of a setup at the ideal point of entry.

[00:33:27]
Let's have a look at one example.

[00:33:29]
This is an M15 chart.

[00:33:30]
It's the CAD-YEN Monday, March 19th 2012, 1.30 AM Eastern Daylight Time.

[00:33:39]
Let's walk through this setup.

[00:33:41]
Okay, we're breaking the Asia range as we come down in the Asia range.

[00:33:46]
We hit the shadow box and we're looking at gap time in London.

[00:33:50]
We've taken out yesterday's low.

[00:33:53]
Continuing on, continuing on.

[00:33:57]
These are many flashcards strung together.

[00:33:59]
I'm just clicking this forward button to move through it.

[00:34:01]
This is an amazing way to study this stuff.

[00:34:04]
I can't say enough about it.

[00:34:06]
Okay, it looks like we have a first leg formed.

[00:34:08]
What are we expecting?

[00:34:09]
I'm expecting it to come down, test this low and not break it, and then take off.

[00:34:15]
Okay, what do we get?

[00:34:19]
Bing!

[00:34:20]
We get one of these beautiful candles that comes down, might have sat there for a few

[00:34:24]
minutes and pulled away.

[00:34:26]
It's your high-low drill candle right there.

[00:34:28]
You want to focus on that.

[00:34:31]
So there we have a beautiful confirmed entry.

[00:34:34]
We have a candle coming back the other way for you guys that like to take confirmed entries.

[00:34:38]
This is the look.

[00:34:39]
This is what you want to see.

[00:34:40]
This is a beautiful setup before it occurs.

[00:34:43]
Bang, we're in.

[00:34:45]
We're holding, holding.

[00:34:48]
Up we go.

[00:34:49]
We achieved an amount of profit past our two-hour mark where we can say we can hold this trade.

[00:34:55]
Up we go.

[00:34:56]
We're shifting out, feeling mighty nice.

[00:34:58]
We get our 50 on our next cycle up and bang 50.

[00:35:05]
Alright?

[00:35:06]
So, the idea is not to study this chart per se.

[00:35:11]
You want to look at it and see what the dynamics are that led to the shift bar, but you want

[00:35:15]
to focus on what it looked like before it happened.

[00:35:18]
Okay, that's the quick skinny on why that is so.

[00:35:21]
Okay?

[00:35:22]
Go back and listen to Steve recording on that.

[00:35:24]
I'm going to talk about a sense of how to do this in paint.

[00:35:26]
If not, come join us in the DMR.

[00:35:28]
We can bring this to you every Monday.

[00:35:30]
Alright, so let's get into the next section and that is the high, low drill.

[00:35:35]
Okay?

[00:35:36]
We all understand that we are not able to catch the high and low market ever.

[00:35:41]
Okay?

[00:35:42]
That's a myth.

[00:35:43]
It can be done.

[00:35:44]
It is done.

[00:35:45]
I've done it.

[00:35:46]
I've seen a lot of people do it.

[00:35:47]
I've seen a lot of people around me do it that I've been hanging out with lately.

[00:35:50]
It amazes me.

[00:35:51]
There's a ton of people who have taken their entries instead of being close to the confirmation

[00:35:56]
candle.

[00:35:57]
Now they're branching way down here.

[00:35:58]
I saw a couple of zen's charts actually.

[00:36:00]
He entered right near the bottom.

[00:36:02]
So as a group we're improving in this respect heavily.

[00:36:05]
Okay, we're moving forward.

[00:36:06]
It's great to see.

[00:36:07]
That's a fact.

[00:36:09]
The high low drill gives one insight into the timing of the market makers.

[00:36:15]
The fast move is false.

[00:36:16]
The slow and steady move is the correct move.

[00:36:19]
Okay?

[00:36:20]
We'll whip this secondly down real fast.

[00:36:23]
Hold it there and then gradually bring it back up.

[00:36:26]
Okay?

[00:36:27]
When one sits in front of the charts and tries to put entries at the extremes of the high

[00:36:32]
of the day or the low of the day, you will be filling yourself with the insight of how

[00:36:39]
these guys are using timing.

[00:36:42]
You're going to see how fast the candles paint.

[00:36:44]
That's a huge portion of your education right here because it's pattern and timing.

[00:36:50]
Because when they move this fast down here really fast, that's your cue.

[00:36:54]
Get in.

[00:36:55]
Load up.

[00:36:56]
It's coming.

[00:36:57]
All right.

[00:36:58]
The high low drill also flushes out the big trading myth that one needs confirmation in

[00:37:03]
the same direction to enter a trade.

[00:37:06]
Okay?

[00:37:07]
In our basic training, we do say that you want to have a confirmation candle.

[00:37:11]
There's a reversal candle and a candle in the direction that you want to go.

[00:37:14]
We say start there.

[00:37:16]
Enter after you see these two.

[00:37:18]
As you study the high low drill, you will begin to enter at the extremes and you will

[00:37:23]
not have a confirmation.

[00:37:25]
I know that's scary.

[00:37:26]
All right?

[00:37:27]
Contrary to the myth, it's actually the safest place to enter trades.

[00:37:33]
Obviously, you're not in stop out.

[00:37:36]
You're really not in drawdown, so you're not going to click out of your trade early.

[00:37:40]
Okay?

[00:37:41]
So the idea is instead of entering here, we want to enter here.

[00:37:48]
It's a very simple right?

[00:37:49]
That's the high low drill.

[00:37:51]
Second leg, when they come down to negotiate that area that they've defined as a trap area,

[00:37:57]
we want to get in and at extreme.

[00:37:59]
I want to ask you guys, is there an indicator on the market that'll tell you this?

[00:38:05]
Absolutely not and there never will be.

[00:38:06]
Think about it.

[00:38:07]
Everybody and his brother and his mother and his family and his training buddy and his

[00:38:11]
entire university are scared, shitless of going long here.

[00:38:16]
So you're one of an infinitesimal small amount of people that's actually going to be trying

[00:38:22]
to take this wick and go long.

[00:38:25]
Okay?

[00:38:26]
It's a numbers game.

[00:38:27]
This is a zero sum game.

[00:38:28]
There's a fixed amount of money that's in play.

[00:38:31]
Whatever is put in gets taken out on the other side.

[00:38:33]
Okay?

[00:38:34]
Even if you're dealing with a bucket shop or whatever the case may be, there are very

[00:38:38]
few people that are entering down here, so you have an advantage.

[00:38:42]
All right?

[00:38:43]
There's a lot of other reasons, but I wanted to point that one out because when you first

[00:38:46]
put on your long at this extreme, it's going to feel like the exact long thing to do.

[00:38:52]
Every bone in your body is going to go ouch.

[00:38:55]
That's why we do this drill on demo, demo this kind of stuff.

[00:39:00]
Take your trades at confirmed entries.

[00:39:02]
Yes, but make sure that when you're trying to catch these lows, you do this on demo.

[00:39:08]
Okay?

[00:39:09]
That gives you the flexibility to just black balls.

[00:39:12]
Like if you're on a driving range.

[00:39:14]
You're just trying to get your stroke down.

[00:39:15]
Okay?

[00:39:16]
You're going to enter it into the game at a later date, but you want to get proficient

[00:39:20]
at hitting balls off the driving range.

[00:39:22]
All right?

[00:39:23]
So this is your isolated skill that you want to learn in addition to the other aspects

[00:39:29]
that we're showing you with this teaching.

[00:39:31]
Okay?

[00:39:32]
When pulling it into live trading, the effects of this training are that entries will start

[00:39:37]
to migrate toward the extremes of M and W formations.

[00:39:42]
You'll start to get your entries more towards the outer side.

[00:39:44]
I know Fred McIntosh is just channeling it with this stuff.

[00:39:47]
All right?

[00:39:48]
His trades that he's sending once in a while, beautiful amazing.

[00:39:51]
Okay?

[00:39:53]
This high low drill becomes the crown jewel of the method as one can enter even tighter

[00:39:58]
stops thus bringing risk we reward to three to one or greater.

[00:40:04]
Okay?

[00:40:05]
That's going to have a lot of ramifications in about 35, 40 minutes when we get into that

[00:40:10]
section.

[00:40:11]
All right?

[00:40:13]
Back to the ball music, brah, brah, brah, brah, brah, brah, brah, brah, brah, brah, brah,

[00:40:20]
brah, brah, brah, brah.

[00:40:21]
Okay.

[00:40:22]
An additional aspect that I've used in trading at the extreme higher, extreme low is to

[00:40:28]
always have my chart blown out wide enough that I can see a previous trap area.

[00:40:34]
I will many times physically draw a line that corresponds to that trap area and try to

[00:40:40]
the answer is close as possible to that trap area if I see a reason to do so.

[00:40:45]
In this particular trade we have an anchor formation on the top.

[00:40:49]
We have a nice first leg pull away and it's gone up one, two, three, three and three

[00:40:57]
quarters.

[00:40:59]
This thing's made some serious inducements back up which are declining people to go

[00:41:05]
along here which is an ideal place to get in your high low drill.

[00:41:10]
So all we do is shut all that information down and we focus in on that.

[00:41:16]
Your entire world is right in here.

[00:41:18]
It's no longer all this other stuff.

[00:41:21]
Right inside here.

[00:41:22]
You have your game plan and you hit it.

[00:41:24]
I think I showed you I physically took this trade.

[00:41:27]
Let's look at another one.

[00:41:29]
This is a beautiful setup.

[00:41:30]
This is a GC from last week as well.

[00:41:33]
You want to see where ideal entry is.

[00:41:36]
Chop that away.

[00:41:38]
We look at our setup and your high low drill is going to be in the second leg.

[00:41:43]
You also had some nice context with this previous day low tracer.

[00:41:48]
You go get out your microscope.

[00:41:55]
Zoom in on this candle right here.

[00:41:56]
I'm almost convinced there's going to be an M on the one minute time frame.

[00:42:00]
I'm not going to go into that here for the Fainting Heart.

[00:42:03]
That's some advanced stuff.

[00:42:05]
But hey how?

[00:42:06]
You get the idea.

[00:42:08]
All right.

[00:42:09]
So now we're at our third area in and that is where we learn to instantly recognize confirmation

[00:42:16]
candles.

[00:42:18]
Each one of these stages took me a month or so.

[00:42:20]
Okay.

[00:42:21]
Hopefully you guys are saying well I understand that it looks kind of similar to my path.

[00:42:27]
We broke our first big barrier when we decided that we were going to take responsibility for

[00:42:32]
our actions and not blame the method because we always go back and validate the method.

[00:42:37]
We then say okay it's our stuff that we need to look at.

[00:42:40]
Then we pop through the next area and we start enlisting the subconscious mind to train in

[00:42:46]
a manner that would allow us to recognize confirmation candles on the hard right edge.

[00:42:55]
Now what's inside?

[00:42:58]
What could possibly be left inside this area here?
