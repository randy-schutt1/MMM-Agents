# V15 — TRANSCRIPT

## ⭐ TIMESTAMP CONVENTION — STATED ONCE, AT THE TOP (`V14_REVIEW_R1.md` GATE, open item 173)

**Every `[HH:MM:SS]` in this file and in every V15 artifact is the committed marker grid of
THIS file — the 492 markers below — and nothing else.** This session ran an independent ASR
pass (see VERIFICATION §5) and **its clock is never cited**; where it corrects a word, the
correction is attached to the *marker grid's* timestamp, not to the second pass's.

**The marker grid and the player's burned-in timecode are the SAME CLOCK.** That was measured,
not assumed, at four independent points where a printed slide changes on a sentence:

| Marker | Transcript line | Slide change, burned-in player timecode | Δ |
|---|---|---|---|
| `[00:04:36]` | *"Okay, some announcements."* | `Announcements` slide at **04:35** | −1 s |
| `[00:07:17]` | *"Let's check your pulse. Where are you?"* | `Where are you?` slide at **07:15** | −2 s |
| `[00:27:00]` | *"We're going to talk about ADR high and low"* | `ADR High and LOW` slide at **27:05** | +5 s |
| `[00:41:19]` | *"when the 80 are high low couples with the pivot point"* | confluence slide at **41:30** | +11 s |

Slide-change granularity is the 5-second sweep grid, so ±5 s is the measurement floor; the
`41:30` row is the speaker running ahead of his own deck, which he says out loud twice
(`[00:31:53]` *"Was that the slide I was on? I don't think so. I think it jumped"*).
**There is no systematic offset between the two clocks.** Screenshot filenames carry the
player timecode; because the clocks coincide, a screenshot name and a marker are directly
comparable, and no conversion is needed anywhere in this artifact set.

---

## SOURCE

| Field | Value |
|---|---|
| Video ID | V15 |
| Original filename | `Bootcamp1 Wk7 050612 Part1 (52mins).swf` |
| SHA-256 | `5308c350193b7cf9471ecb3f534b27fc7e8c1cd21e1cd94eb9521e7e56482b49` — verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session on the flat `Bootcamp/` canonical path, **and re-verified after the frame-rate patch** to prove the original was not modified (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| Duration | 00:52:05 (audio measured **3125.446531 s**; SWF header **9,379 frames ÷ 3.0 fps = 3126.333 s**; `SOURCE_MANIFEST.md` 00:52:05 = 3125 s — **three independent figures agreeing to within 1.33 s**) |
| Lesson title | **PRINTED, and it is the lesson's own subject line rather than a topic title.** The opening slide reads `Market Makers Boot Camp` / **`Week 7`** (`V15_00-00-15_…png`). From `[00:26:57]` to the end every slide is titled **`ADR`** or **`ADR High/Low`**, which is the nearest thing this file has to a topic title. The quarantined per-lesson header's *"Primary Topics: Trap Moves, Level 1/2/3 Progression & Fake Breakouts Identification"* is fabricated — see `QUARANTINE_REGISTER.md` **Q-016** |
| Session date | **2012-05-06**, from the filename `050612` and `SOURCE_MANIFEST.md`. **Corroborated from inside the file, and the corroboration is load-bearing for the corpus gap** — `[00:00:02]` and `[00:00:23]` both say *"week seven"*, and the opening slide prints `Week 7`. Week 1 is `031812` (2012-03-18); seven weekly sessions from 03-18 lands on **2012-04-29**, not 05-06, and the one-week discrepancy is the missing Week 6 (`A-092`) plus the announced two-week break. See `V15_INTERPRETATION.md` Q1 |
| Frame rate | **3.0 fps** in the SWF header — read from **this file's own header**, not assumed (`SWF_CAPTURE_RECIPE.md` §10 as corrected by V10 R1 open item 87). The 10× sweep patch is therefore **3.0 → 30.0** here |
| Stage size | **1024 × 786** — the majority class. `GOTCHA 5`'s table gives `(512, 300)`, and the pre-click/post-click guard **confirmed it fired** rather than assuming it (`sweep.log`: *"play click confirmed: stage changed"*) |
| Delivery platform | **GoToMeeting** — printed on screen at `32:50`, where the platform's own `GoToMeeting: Hide Desktop` banner covers the top 60% of the slide for ~5 s (`V15_00-32-50_…png`). First frame in the corpus to name the broadcast tool |
| Transcribed by | ASR, by a pre-ingestion session. Copied and verified 2026-08-14 — see VERIFICATION below. The pre-ingestion file's own `# VIDEO` header block is **NOT carried over**: its *"Course Position: Video 16 of 21"* is wrong under `D-017` §2's renumbering (this file is **V15**), and its *"Primary Topics"* line is unsourced and wrong on this lesson — there is no "Level 1/2/3 progression" segment and no "fake breakout" segment in the file at all |
| Transcription confidence | **MEDIUM–HIGH.** 492 markers, strictly monotonic, zero equal-adjacent pairs, and it preserves its own mishearings (*"Steve Socks"*, *"GVP"*, *"manage"* for mayonnaise, *"the 80 are high low"*, *"ADM"* for *out of me*, *"Candice Shop"* 17 s before a correctly-rendered *"Candy Shop"*, *"who's my voice"*, *"the only race"*, *"Australian corrected big"*). Defects are ordinary ASR failures on domain vocabulary and proper nouns; **twelve are load-bearing and are corrected below, each arbitrated by an independent ASR pass** |

---

## SPEAKER TABLE — MANDATORY UNDER `D-025` consequence 3, re-adopted by `D-033`

| Speaker | Runtime | Basis |
|---|---|---|
| **Course author (Steve Mauro)** | **100%** — `[00:00:00]`–`[00:51:56]`, the whole file | Six non-acoustic strands, below. **HIGH confidence** |
| Guest presenter | **0%** | No second voice is introduced, addressed, thanked or handed to anywhere in the file |

**`COURSE_PROGRESS.md` V14 GATE (d) required this be TESTED rather than inherited, on the
explicit ground that V15 is a NEW WEEK and a NEW DATE after a multi-week gap — the exact
condition under which this corpus's author runtime has broken before (V03→V04). It was tested
on strands fixed before the answer was known, and the acoustic cross-file screen was NOT run,
per V07's prohibition.**

### THE SIX STRANDS — non-acoustic, `D-025`/`D-033` method

| # | Strand | Evidence |
|---|---|---|
| **1** | ⭐ **He names himself, in his own voice, twice within ten seconds** | `[00:04:04]` *"If you start mumbling under your breath, **Steve Socks** \[Steve sucks\], he's crazy, I hate him"* → `[00:04:12]` *"**Steve's going to suck.** **You're going to hate me.** I'm kidding, but halfway."* The pronoun switch from *"Steve"* to *"me"* inside one breath is the identification, and it is the strongest single strand in this file |
| **2** | **He reads student questions addressed to "Steve" and answers them in the same voice** | `[00:20:25]` *"**Steve, what's going to happen tonight with the pound?** I don't know."*; `[00:23:54]` *"**How come you don't know Steve?** I thought you know everything. I don't know everything, but here's the reason why"*; `[00:49:31]` *"The question is, **Steve**, if this was the low of the day and the number changed on the big board, right? Yes, it did, but he closed all the way back above."* **In every case the answering line is the same voice continuing** |
| **3** | **He sets and owns the course's calendar** | `[00:00:33]` *"The week of the 10th, there's not going to be a boot camp"*; `[00:00:40]` *"the final boot camp will be on the 17th"*; `[00:06:00]` *"**I'm** doing a web class"*; `[00:04:45]` *"**The venue's paid for**, locked in for these dates"* |
| **4** | **He owns the forum and the recordings** | `[00:16:03]` *"go look at these posts on the forum. **That's why I'm showing you**"*; `[00:06:36]` *"The recording from this class **will replace** the recordings that are up right now"*; `[00:07:12]` *"**I'm just going to leave them up**"* |
| **5** | **He grades and assigns, in the second person, and no one answers back** | `[00:07:16]` *"Let's check your pulse"*; `[00:09:32]` *"**I'm going to make you** study two or three crosses"*; `[00:09:41]` *"**I'm writing it right now.** It's in the process"*; `[00:13:37]` *"put everything aside and do this shit for a couple of weeks"* |
| **6** | **Handover scan: ZERO.** | The same **17-pattern** superset V12, V13 and V14 used returns **two** lines across all 492 markers and **neither is a handover**: `[00:00:22]` *"Alright, **welcome back**"* (the speaker greeting his own class — the identical false positive V13 logged) and `[00:04:12]` *"**Steve's** going to suck"* (strand 1, which identifies the speaker rather than introducing one). **`take it away` / `turn it over` / `hand over` / `back to you` / `thanks Steve` / `my guest` / `joining us` / `over to you` / `take over` / `passing it` / `go ahead Steve` / `let me hand` / `let me pass` / `you're up` / `floor is yours` / `I'll let` → all ZERO** |

**Named third parties appear and NONE of them speaks.** Twenty names occur: *Kevin* `[00:00:58]`,
*Peter* `[00:07:36]`, *Clara* `[00:11:26]`, *Antonio* `[00:18:28]`, *Subio/Suvio/Asubio*
(one student, three ASR spellings) `[00:02:53]`/`[00:23:38]`/`[00:30:27]`, *Casey* `[00:02:57]`,
*Stephen* `[00:24:48]`, *Dach* `[00:05:58]`, *Luther* `[00:39:12]`, *Kirk* `[00:39:31]`,
*Heidi* `[00:04:58]`, *Zen* `[00:29:25]`, *Kim K* `[00:37:41]`, and the three forum posters
*Gilbert Ellis* `[00:14:15]`, *Peter Brown* `[00:15:55]`, *Ron Vara* `[00:17:05]`.
**Every one is a student being answered, congratulated or shown; the next line is always the
same voice continuing.** Two further names are referents, not participants: *Neo* `[00:24:55]`
(the film) and *the creature from Jekyll Island* `[00:38:46]` (a book).
**Recorded because a name in a transcript is the commonest false positive for a second speaker.**

---

## VERIFICATION — `SETUP_ISSUES.md` `I-008`

**The supplied transcript was verified before it was trusted, not after.**

| # | Check | Result |
|---|---|---|
| 1 | **Marker count** | **492** markers, `[00:00:00]` → `[00:51:56]` |
| 2 | **Monotonicity** | **0 non-monotonic pairs**, **0 equal-adjacent pairs** — cleaner than V14's grid, which carried one |
| 3 | **Final marker vs measured duration** | last marker **3116 s**, measured audio **3125.45 s** — a **9.4 s** tail. The sweep confirms it: the last content frame is `52:06` and the player's own total reads `52:0x`, so the tail is the closing seconds after the final sentence, not missing transcript |
| 4 | **Does it preserve its own errors?** | ✅ **Yes, extensively** — *"Steve Socks"*, *"GVP"* for GBP (six occurrences across four markers), *"manage"* for mayonnaise (×4), *"the 80 are high low"* for *the ADR high/low*, *"ADM"* for *out of me*, *"Candice Shop"* alongside a correctly-rendered *"Candy Shop"* 17 s later, *"the only race"*, *"Australian corrected big"*, *"22-trade"*. **A fabricated transcript does not invent its own mishearings, and it certainly does not mis-hear the same word three different ways.** |
| 5 | **Independent ASR pass** | Run this session on the extracted audio (`whisper`, `large-v3-turbo`, `--language en`). Run as **25 short clips** (12–22 s) cut around each disputed marker, `whisper medium.en`, **plus a completed full-file `large-v3-turbo` pass**. Used **only** to arbitrate the disputed words below — and, once, to measure a negative: the full pass contains **zero** occurrences of `smoothing`, `period`, `standard deviation`, `volatility band`, `market base`, `63` or `37` (`A-099`). It is **not** committed and its clock is **never** cited |
| 6 | **Against the frames** | Four independent marker↔slide-change alignments, table at the top of this file. **No systematic offset** |

### THE TWELVE LOAD-BEARING CORRECTIONS

Load-bearing means: **a V15 artifact quotes it, or a record turns on it.** Everything else in the
body is left exactly as the pre-ingestion pass produced it, mishearings included, per `I-008`.
**The body below is NOT edited** — these corrections live here and are cited from here.

**Method, stated so it can be checked:** 25 clips of 12–22 s were cut from the extracted audio
around each disputed marker and transcribed independently with `whisper medium.en`. A clip is
**CONFIRMED** only where the second pass produced the corrected reading **without having seen the
first**. Where the second pass reproduced the first pass's oddity, the reading is **NOT adopted**
and moves to the flag list below.

| # | Marker | As transcribed | Reading adopted | Second pass | Why it is load-bearing |
|---|---|---|---|---|---|
| 1 | `[00:04:04]` | *"Steve **Socks**"* | *"Steve **sucks**"* | ✅ *"If you start mumbling under your breath, **Steve sucks**, he's crazy, I hate him"* | Speaker strand 1. The self-identification turns on it |
| 2 | `[00:09:07]`, `[00:09:15]`, `[00:09:49]` (×2), `[00:09:54]` (×2) | *"**GVP**"* | *"**GBP**"* | ⚠ **NOT confirmed** — the second pass renders it *"GDP"*, also wrong. **Adopted on internal evidence only:** the same sentences say *"Euro GVP"*, *"GJ"* and *"GVP odds"*, which read as **EUR/GBP, GBP/JPY and GBP/AUD**, and the lesson's own chart is `GBPUSD,H4` | The pair under discussion in §5 of the source notes |
| 3 | `[00:41:19]` | *"the **80 are** high low"* | *"the **ADR** high low"* | ✅ *"so when **the ADR high low** couples with the pivot point, the blue tracer"* | The lesson's central object, in the sentence that states the confluence rule |
| 4 | `[00:34:01]` | *"It's all you get in **ADM** this week"* | *"That's all you're getting **out of me** this week"* | ✅ *"Alright, that's it. **That's all you're getting out of me this week.**"* | ⭐ See the self-correction note below |
| 5 | `[00:33:44]` | *"Welcome to the **Candice** Shop"* | *"Welcome to the **Candy** Shop"* | ✅ *"Welcome to the **candy shop**. Don't trade until they hit the stops"* | Quoted in `V15_SOURCE_NOTES.md` §8. The transcript itself renders it correctly 17 s later |
| 6 | `[00:41:39]` | *"**Manage** or the waters"* | *"**mayonnaise** or the waters"* | ✅ *"maybe the 50, **mayonnaise** or the waters laying near the blueberries"* | Bears on `D-043` |
| 7 | `[00:43:53]` | *"a piece of **manage** … a jar **manage**"* | *"a piece of **mayonnaise** … a jar mayonnaise"* | ✅ *"with a piece of **mayonnaise** running over there, a jar mayonnaise running across there"* | Same |
| 8 | `[00:44:53]` | *"There's your **manage**, your M3"* | *"Here's your **mayonnaise**, your M3"* | ✅ *"**Here's your mayonnaise, your M3.**"* | Same, and it is the only line pairing an EMA nickname with a pivot label |
| 9 | `[00:21:38]` | *"**Who's** my voice?"* | *"**I'm losing** my voice"* | ✅ *"Excuse me, **I'm losing my voice.**"* | Otherwise reads as a second speaker being addressed. **Directly a speaker-table hazard**, and the transcript corroborates it at `[00:46:36]` (*"hope they're losing my voice"*) |
| 10 | `[00:40:03]` | *"taken **3540** trades a piece a week"* | *"taking **35, 40** trades apiece a week"* | ✅ *"they were taken **35 40 trades apiece**"* | The number is quoted in `V15_SOURCE_NOTES.md` §4 and in `A-098` |
| 11 | `[00:31:27]` | *"twenty-five to fifty pips off of the **higher low**"* | *"twenty-five to fifty pips off of the **high or low**"* | ✅ *"**25 to 50 pips off of the high or low**, depending on the pair"* | ⚠ **`A-082`-class.** Quoted verbatim in `A-095`. The uncorrected reading would have made it a claim about **a higher low** (a structure) instead of about **two levels** |
| 12 | `[00:45:47]` | *"**Find and** support on a pivot"* | *"**finding** support on a pivot"* | ✅ *"ADR, met or exceeded, **finding support on a pivot**. This is an M1, M3 day"* | Quoted in `V15_SOURCE_NOTES.md` §7 |

> ### ⭐ SELF-CORRECTION ON #4, RECORDED RATHER THAN QUIETLY FIXED
> This session's **first** reading of `[00:34:01]` was that *"ADM"* was a mishearing of **`ADR`**
> — an obvious, plausible, in-domain guess, and it would have created **a fifth ADR mention that
> the speaker never made**, inside the lesson whose whole subject is the ADR. The second pass
> shows the phrase is *"out of me"* and has nothing to do with the indicator. **A domain-primed
> guess is the exact failure mode the second-pass rule exists to catch, and here it caught one.**

### WHAT WAS **NOT** CORRECTED, AND IS FLAGGED INSTEAD

Five renderings were disputed and are **left standing in the body**. Two because the second pass
*reproduced* them, and three because the passes disagree or the word is a proper noun.

| Marker | Rendering | Second pass | Disposition |
|---|---|---|---|
| `[00:03:16]` | *"what I'm teaching you is in the **charge** every day"* | ⚠ **Reproduced it** — *"is in the charge every day, every week"* | **NOT corrected.** *"in the charts"* is the obvious repair and **two independent passes decline to make it.** Left as-is; `V15_SOURCE_NOTES.md` does not quote the phrase |
| `[00:38:55]` | *"the dealer behaves exactly as an **illustrator**"* | ⚠ **Reproduced it** — *"exactly as a illustrator"* | **NOT corrected.** Candidate *"facilitator"* is **withdrawn** as unsupported. Two passes agree on the word; the sentence is about dealer intent and is not quoted as method anywhere |
| `[00:21:34]`, `[00:21:55]` | *"a **22-trade** on the four-hour chart"* | ⚠ **Reproduced it three times** — *"twenty two trade"*, *"twenty-two trade"*, *"22 trade"* | **NOT an ASR error.** It is a term the lesson uses twice and never defines → **`A-097`** |
| `[00:43:17]` | *"The **3333** trade might show"* | ⚠ **Disagrees** — *"The **3.33** trade might show"* | **NOT corrected.** Neither rendering is safe → **`A-097`** |
| `[00:01:36]` | *"at the pace of, say, a **wreck or a car**"* | ⚠ **Disagrees** — *"a **rick** or a car"* | **NOT corrected.** Two student names, almost certainly; a student named **Kar** is the subject of a separate file in this library (`More videos/SteveMauro060212 Part08 (60mins) - Kar on Homework.swf`). **A name is not worth a guess** |

---

# VERBATIM TRANSCRIPT

[00:00:00]
Okay, let's get rolling.

[00:00:02]
Alright, week seven.

[00:00:03]
Listen, I got about two or three more weeks of boot camp.

[00:00:06]
We're going to wind up around 10 or 11 weeks.

[00:00:09]
And that's going to be it.

[00:00:12]
Then we're going to have some classes coming up.

[00:00:14]
We'll meet in New Jersey and hang out.

[00:00:16]
And then I'm going to take off about two months for the summer.

[00:00:19]
If you want me, I'll be at the beach.

[00:00:22]
Alright, welcome back.

[00:00:23]
Week seven.

[00:00:24]
I mentioned what I'm thinking is we'll have a few more boot camps

[00:00:29]
the week.

[00:00:31]
Let's see.

[00:00:33]
The week of the 10th, there's not going to be a boot camp.

[00:00:36]
June the 10th, because we have the web class.

[00:00:38]
You'll have the recordings to review for a week.

[00:00:40]
And then the final boot camp will be on the 17th, which is Father's Day.

[00:00:45]
And then I'll fly into Jersey.

[00:00:48]
We'll hang out the following week.

[00:00:50]
And then I'm going to take off for the summer.

[00:00:52]
If you want me, I'll be at the beach.

[00:00:54]
You want to talk to me?

[00:00:55]
Put on your swim trunks and try to find me.

[00:00:58]
Now I'm still talking, Kevin.

[00:01:00]
You should be hearing something.

[00:01:02]
Okay.

[00:01:03]
Alright, manage your expectations.

[00:01:07]
I got to tell you this every week.

[00:01:10]
Give me two hours.

[00:01:12]
The next hour in 45 minutes, whatever's left.

[00:01:15]
Focus.

[00:01:16]
I want to talk about this a step further.

[00:01:20]
Man, I'm getting a lot of emails from a lot of people that are doing really well

[00:01:24]
because of the boot camp.

[00:01:26]
Nothing makes me happier.

[00:01:28]
Very excited to hear this.

[00:01:32]
But also, I want you to not beat yourself up

[00:01:36]
if you're not turning the corner at the pace of, say, a wreck or a car.

[00:01:40]
I mean, everybody's journey is different and everyone has their own baggage, their own fears

[00:01:45]
about making money or losing money.

[00:01:47]
Everyone's different.

[00:01:48]
You have to understand that.

[00:01:50]
So you can't say, oh, well, this guy turned the corner and I'm not getting it, so I suck.

[00:01:55]
It doesn't work like that.

[00:01:59]
The beautiful part of the trading business

[00:02:01]
is that it's a one-on-one game with you versus the market maker.

[00:02:06]
You can't compare yourself to someone else's journey

[00:02:11]
because you don't know what they've been through before they got here.

[00:02:15]
There's a saying that was on Pinterest, my wife sent it to me,

[00:02:21]
and I'll try to give you the clean version,

[00:02:25]
but it made me think of talking about this this week.

[00:02:28]
It said,

[00:02:30]
success is like pregnancy.

[00:02:33]
Everyone congratulates you, but they don't know how many times you got screwed to achieve it.

[00:02:39]
I thought that was pretty good.

[00:02:45]
So what I'm trying to say is, everyone has their own journey.

[00:02:51]
Everyone is different.

[00:02:53]
Not everybody can be a Suvio.

[00:02:57]
Not everybody can be Casey.

[00:02:59]
Everybody has to have their own journey, their own path.

[00:03:04]
Success is in every one of you.

[00:03:06]
You have to manage your expectations.

[00:03:08]
You cannot expect to take this class, and in five days,

[00:03:11]
come out of here making seven figures.

[00:03:13]
It's just not how it works.

[00:03:16]
I can promise you that what I'm teaching you is in the charge every day, every week.

[00:03:21]
If you roll up your sleeves and follow the bootcamp and do the work,

[00:03:25]
success that you're seeking will find you, or you will find it.

[00:03:29]
It's there.

[00:03:31]
Everybody has a different level of expectation of what success is.

[00:03:36]
You cannot compare your journey to somebody else's.

[00:03:40]
It's your journey.

[00:03:43]
It's your journey.

[00:03:44]
So keep that in mind when things aren't going your way,

[00:03:51]
or when you're not seeing the setups clearly.

[00:03:55]
Hope that helps you.

[00:03:58]
Refrain from negativity in your mind.

[00:04:00]
That's the biggest thing.

[00:04:01]
Negativity breeds negativity.

[00:04:04]
If you start mumbling under your breath, Steve Socks, he's crazy, I hate him.

[00:04:08]
Guess what?

[00:04:10]
That's going to become your reality.

[00:04:12]
Steve's going to suck.

[00:04:13]
You're going to hate me.

[00:04:14]
I'm kidding, but halfway.

[00:04:17]
You're not going to see the setups if you block your mind from it.

[00:04:23]
Okay?

[00:04:25]
Trade strong, man.

[00:04:27]
All right, chat box.

[00:04:28]
Still love you, still ignoring you.

[00:04:30]
Not going to change.

[00:04:32]
Not going to spend any more time on that.

[00:04:36]
Okay, some announcements.

[00:04:38]
You guys know the live class is coming up.

[00:04:41]
New Jersey, Stevens Institute.

[00:04:43]
This is a lock.

[00:04:44]
It's happening.

[00:04:45]
The venue's paid for, locked in for these dates, June 23rd to the 27th.

[00:04:50]
6 to 11.

[00:04:53]
If you're lost, don't know what's going on.

[00:04:55]
Visit the New Jersey or bus section on the forum for details.

[00:04:58]
Heidi built a tinyurl.com slash MMFX lodging.

[00:05:03]
It gives you a selection of the hotels that are near the venue.

[00:05:06]
Okay?

[00:05:07]
The class will not be recorded or streamed.

[00:05:10]
Okay?

[00:05:12]
I'm not recording it.

[00:05:14]
I'm going to go in there and do my job, not being interrupted with moving the microphone

[00:05:19]
around and internet issues.

[00:05:21]
The same shit that happened in Orlando where I didn't get a recording out of there is exactly

[00:05:26]
why I'm not streaming this class or doing it again.

[00:05:29]
Okay?

[00:05:30]
You guys were mad at me, but I'm telling you well in advance.

[00:05:34]
Okay?

[00:05:35]
The recording and stuff has been a hindrance.

[00:05:37]
It's been holding back the flow of the class.

[00:05:39]
For the people that took the time to come over there live, it's not right, man.

[00:05:44]
So we're going to have a good live class.

[00:05:45]
If you want to see me, come on.

[00:05:47]
There's room for you.

[00:05:49]
Okay?

[00:05:51]
All right.

[00:05:54]
Prior to the live class.

[00:05:58]
Dach, here you go, buddy.

[00:06:00]
I'm doing a web class.

[00:06:02]
June the 2nd through the 6th.

[00:06:04]
The days may be shifted a little bit.

[00:06:06]
It's not 100% lock on these times.

[00:06:08]
I'm pretty sure, but it might be the 3rd through the 7th.

[00:06:10]
I don't know yet.

[00:06:11]
We're working on some other stuff to try to get this locked in, but this is what we got

[00:06:16]
tentatively right now.

[00:06:17]
It looks like it's going to be the 2nd through the 6th, 6 to 10, 6 to 11.

[00:06:22]
Usually what I do is I go 6 to 10, 10, 15.

[00:06:25]
I know it gets late in the UK.

[00:06:28]
And what we'll do is I'll do maybe questions for the last 20 minutes or half hour, whatever

[00:06:34]
that works out.

[00:06:36]
The recording from this class will replace the recordings that are up right now.

[00:06:43]
And they will be up.

[00:06:46]
They're going to be available to you guys.

[00:06:48]
Okay?

[00:06:49]
Hopefully this will be my best class ever.

[00:06:51]
If the other class is better, we'll leave the other one up.

[00:06:53]
Whatever you guys want.

[00:06:55]
Okay?

[00:06:56]
The newest class will replace the class that's up there now, and it will be up there for

[00:07:04]
you guys to have access to.

[00:07:06]
All right?

[00:07:07]
I try leaving them up.

[00:07:08]
Not leaving them.

[00:07:09]
Doesn't matter.

[00:07:10]
They're getting stolen or posted.

[00:07:11]
It doesn't matter.

[00:07:12]
I'm just going to leave them up.

[00:07:13]
All right?

[00:07:14]
Best way to handle it.

[00:07:15]
Okay.

[00:07:16]
Let's check your pulse.

[00:07:17]
Where are you?

[00:07:18]
You should have a set of flashcards by now, right?

[00:07:20]
You should have your 4 hour markups.

[00:07:22]
You should have taken TDI-only trades.

[00:07:25]
You should have worked a big board.

[00:07:29]
And you should have done some moving average-only trades.

[00:07:35]
Okay?

[00:07:36]
Peter, you're good to hear.

[00:07:38]
If you don't have this stuff yet, it's not too late.

[00:07:41]
It's never too late, man.

[00:07:45]
Okay?

[00:07:46]
What should you have taken away after 7 weeks of hanging out with me?

[00:07:51]
Can you spot a clean setup pattern?

[00:07:53]
If not, make some flashcards.

[00:07:56]
Can you understand the big picture on the 4 hour?

[00:07:59]
How the dealer spikes the high?

[00:08:01]
Sets the high of the week and reverses off at that level.

[00:08:04]
Sets the low of the week and trades back into the range.

[00:08:07]
You need to have a deeper understanding as to how the dealer extends the high or low.

[00:08:11]
Holds the level and comes back above it or below the same level for stop triggers and trap moves.

[00:08:16]
That's what you should be getting out of this.

[00:08:18]
If you were watching the big board, a lot of you cursed me out on an email and said you hated it, you ain't doing it.

[00:08:23]
It's garbage.

[00:08:24]
Okay, I understand.

[00:08:26]
It's not easy.

[00:08:28]
But here's the deal.

[00:08:30]
If you watch how the dealer handles the high and the low on the big board, it starts to give you an idea how price just sits there and pulsates.

[00:08:38]
And then he extends it and comes back.

[00:08:41]
Okay?

[00:08:42]
Those are the things you're supposed to be seeing.

[00:08:45]
Why am I making you do that?

[00:08:47]
Because the next step, the next thing we're going to cover, not tonight, but it's in the works, is that if you could understand how the dealer works the big board near the high and near the low, then you're going to start to understand fractional disparity a little more clearly.

[00:09:02]
And we'll address that in the weeks to follow.

[00:09:05]
Okay?

[00:09:07]
So what's going to happen is you're going to realize, hey, the dealer tapped the high in GVP and stayed right off of it and didn't move.

[00:09:13]
But Euro was taking off.

[00:09:15]
These are the things you have to see on the big board, which will help you understand how Euro GVP is being moved, how the Euro crosses are being moved.

[00:09:27]
We're going to do some drills pertinent to that when we talk about fractional disparity.

[00:09:32]
I'm going to make you study two or three crosses and the triggers, and we're going to see if you can spot the moves.

[00:09:39]
That's going to be one of the drills coming up.

[00:09:41]
Okay? I'm writing it right now. It's in the process.

[00:09:43]
It's going to be good for you. You're going to start to see things that maybe you haven't seen before.

[00:09:49]
People have been telling me, oh, GVP's been choppy lately. GVP's choppy. There's a reason.

[00:09:54]
Euro GVP's moving, GJ's moving, GVP odds moving, Australian crosses are moving, other things are going on.

[00:10:02]
Okay? You notice some stuff traded in a range, Australian corrected big? What happened?

[00:10:07]
Australian crosses were handled. Aussie crosses. How are you guys like to say it?

[00:10:12]
Okay? These are the things we're going to talk about coming up.

[00:10:15]
All right. By now, you should understand how to really use the TDI and how to manage your trades with it.

[00:10:22]
If this is not what you're getting out of the work, you're not doing enough of it. Get back on it.

[00:10:27]
You should start to realize some things about the TDI.

[00:10:31]
You should start to realize that at the extreme overbought or oversold zones above the 68, below the 32,

[00:10:44]
when the shark fin appears, those trades are gold. When it crosses back inside the band and crosses the one hour blood in the water, those trades are gold.

[00:10:53]
You should start to realize that. We're going to review the TDI in the coming weeks.

[00:10:58]
Some other things I want to add, and we'll add some higher time frame, some other things to look at.

[00:11:03]
Okay? Confirm a trade signal and combine with dealer price action timing in a larger cycle.

[00:11:08]
These are the things you're supposed to be getting. Okay? A lot of you are getting it. I couldn't be more proud, but some of you are still not where you need to be.

[00:11:21]
The deal is this, you can't look at a couple trades and go, oh yeah, I see that. I don't have to do the work.

[00:11:26]
Thank you, Clara. Show me the TDI's helping to make better trades.

[00:11:33]
Listen, it's like I talked about the gym. You don't go in and work your whole body. You work individual body parts to make the complete body better looking.

[00:11:41]
You work chest, shoulder, and back. The next day you work bods and tris. The next day you work legs. The next day you might work your abs.

[00:11:48]
But at the end of the week you've worked your entire body, and then the whole picture looks good, right? Hopefully.

[00:11:56]
So now, what I'm trying to teach you to do, the TDI is work in chest. The moving averages by themselves is work in your shoulders.

[00:12:05]
The big board is work in your abs. When you put all these together back on the chart, now think about this, how powerful.

[00:12:12]
I know how to use the TDI the right way. I understand how the dealer works the high and low with the big board. When he hits it, taps it, holds it.

[00:12:19]
I understand the candle patterns that present because of this and the behavior.

[00:12:25]
I know what the moving averages are supposed to look like on a nice run. If they look like spaghetti, it's not a nice run.

[00:12:32]
Understand how these things start to tie together the individual pieces of the template to give you the broad spectrum or the big, I guess, the eagle-eyed view of every single person.

[00:12:41]
When you put it all together, you should be sharp as a tack at each individual area.

[00:12:48]
When they're put on the chart, you won't just simply walk up to a chart and stare at it and go, yeah, that's my TDI. That's my template.

[00:12:55]
You need to know what each individual component represents on a good dealer cycle.

[00:13:02]
Then you're going to have multiple confirmations at a glance. You're going to look, TDI's shark fin to the high side.

[00:13:07]
The dealer broke above the Asian box. Do you understand? The moving averages have painted an M with the mustard.

[00:13:15]
It crossed back over the ketchup. It bounced off of the blueberries.

[00:13:20]
These are what those drills are supposed to help you see and do.

[00:13:24]
So if you're just glancing at it going, yes, that's a good drill, but I'm too busy, my kids are screaming.

[00:13:28]
My wife's yelling at me, I got to make some money. I don't have the time.

[00:13:32]
How much time have you wasted from January to June or to May, rather?

[00:13:37]
If you're not at the level you want to be, put everything aside and do this shit for a couple of weeks.

[00:13:43]
I promise you it's going to make a difference.

[00:13:47]
Okay?

[00:13:50]
All right. I already said this stuff.

[00:13:52]
You can see how to read the moving averages for trade management, for entry, and exit confirmations.

[00:13:57]
See where you're at in the cycle.

[00:13:59]
Blah, blah, blah. Right? Tired of hearing me say it, I bet.

[00:14:02]
All right. Some R&D examples that were going on in the form. I thought they were pretty good.

[00:14:06]
A lot of you doing some really nice work in there. I might not answer all of you, but I am looking at it.

[00:14:11]
And these are some examples that I saw I thought looked really good this week.

[00:14:15]
All right. This was from Gilbert Ellis.

[00:14:18]
He, what I like what he did is he took the high and low drill,

[00:14:24]
then he went back and marked it on the chart, and he wrote price down.

[00:14:28]
So let me blow up one or two of his charts. Let me show you what he did.

[00:14:33]
See, he wrote the times right in here. Can you guys see that? One o'clock in the morning with the high low was 115, 130.

[00:14:41]
He wrote in what the times were for the high and low. I thought this was great.

[00:14:46]
He saw that they extended the high. He took an entry,

[00:14:51]
and then he took an exit. 445 stopped for the night, closed it out, went to bed.

[00:14:56]
If you're not doing it like this, this is a good way to do it, man.

[00:15:01]
I thought that was pretty good. And then here's another example.

[00:15:06]
And he wrote, this is my accidental entry. Wish all of my accents worked out like this one.

[00:15:12]
Well, it's no accident, man. He probably would have got in a little bit later if you waited for one hour.

[00:15:18]
One, two, three, four, five, maybe an hour would have ended him on this railroad tracks.

[00:15:23]
But that's a nice trade, man. Same thing. One o'clock noted the time.

[00:15:28]
115, no change. 215. The high was extended. 245 would have entered.

[00:15:35]
No change off of the high. Ended the trade at 445. Obviously, that's his bedtime.

[00:15:40]
Okay, trade was profitable. This is the stuff you're supposed to be doing or seeing.

[00:15:45]
This is a good way to go about the drill if you're not doing it.

[00:15:50]
That's the way to do it, okay?

[00:15:55]
All right. This is from Peter Brown in Sydney. His TDI only trades.

[00:16:00]
I thought these were pretty nice. They were clean.

[00:16:03]
By the way, go look at these posts on the forum. That's why I'm showing you.

[00:16:06]
I forgot to mention that. Go have a look, man. It's good work.

[00:16:10]
It's good stuff these guys are doing. All right?

[00:16:14]
He didn't fall for this. He waited for a nice clean W formation and a crossover.

[00:16:19]
Blood in the water. And he counted his levels. One, pull back two, pull back three,

[00:16:26]
M formation. He took exit on the re-cross. Perfect, perfect setup. Clean.

[00:16:32]
Okay? And he has, he's trading, he's trading micros, which is fine, man.

[00:16:38]
Some people need to use real money and pennies a pip is fine.

[00:16:42]
If it makes you pay attention better. If you treat demo like a cowboy

[00:16:46]
and perhaps you should use micros, throw like 50 bucks in an account

[00:16:53]
and treat it as real and try to grow it. More valuable, okay?

[00:16:59]
All right. Let's see what else.

[00:17:05]
This was Ron Vara from New Jersey. I thought this was a nice grab.

[00:17:10]
And I wanted to just throw it up there for you guys.

[00:17:13]
I want you to notice pins, pull back. Man, it gets me every time.

[00:17:22]
Okay, sorry about that. All right. Pins, pull back. Pins, again.

[00:17:27]
Notice how the deal are slightly spiked right before the news release.

[00:17:31]
Right there. He grabbed it here. The news took him to his limit.

[00:17:35]
He had to take a little heat on the pushback up.

[00:17:38]
But it was a nice perfect M formation setup to deal with work the previous high.

[00:17:44]
Okay? Thought it was a nice grab.

[00:17:48]
All right. I want to over this real quick, but what I'm trying to accomplish with these sessions

[00:17:51]
is breaking down the chart template, helping you guys see the big picture

[00:17:55]
by taking the smaller segments. Right? What's the word for that?

[00:18:00]
I think it's symbiotic. The sum of the parts are greater than the whole, I guess.

[00:18:06]
Symbiotic relationship between each component of that's the right thing.

[00:18:09]
It's probably synergy. Anyway, a scholar I am not.

[00:18:14]
Here's what I'm trying to point. I'm trying to make break down the individual components

[00:18:18]
when you put them all back together. It creates a bigger picture for you guys,

[00:18:22]
a cleaner picture.

[00:18:28]
The whole is greater than the sum of its parts. Thank you, Antonio. Absolutely right, buddy.

[00:18:32]
Okay. This week's breakdown. Let's look at your own GBT. What happened on the four hour?

[00:18:38]
Take a look at that. And then we'll get into the lesson. All right.

[00:18:45]
Pound dollar. Okay. Think about what's going on with the pound dollar.

[00:18:49]
It's been rising like crazy, right? It's been going up. It's been going up.

[00:18:54]
Trend has been beautiful on a nice up run all last week. The week before it's been rising.

[00:19:01]
Okay. You've got to think to yourself.

[00:19:06]
It cannot continue to rise without a correction, a reset, whatever you want to call it.

[00:19:14]
The dealer has to pull back. Okay. On aggregate, he's heavy at the highest point.

[00:19:22]
Short, he'll make his pull back and come out of his trade in a profit.

[00:19:27]
That's just the nature of the businessman. That's what he does. All right. So,

[00:19:32]
you draw your psychological support and resistance level. First eight hours of the week,

[00:19:37]
the Asian range of the week. In the pound, the dealer spikes above. He spikes right above it.

[00:19:44]
He breaks high, ends with the pin. You're looking for a sell.

[00:19:50]
He made a unidirectional swing for the week. Three pushes down. Simple, right? TDI was extremely high.

[00:20:03]
See it in here? Okay. Now, is this the end of the run? I don't know. We'll know tonight.

[00:20:10]
If the dealer comes out and makes a W formation,

[00:20:17]
trend reset continuation is warranted. If the dealer breaks high and makes an M formation,

[00:20:25]
he's going to continue down. Steve, what's going to happen tonight with the pound?

[00:20:30]
I don't know. That's the way to see what happens between three and five in the morning.

[00:20:34]
When I move, you move. When the dealer makes his move and gives us a signal,

[00:20:39]
that's when we make our move. Okay? All right. Euro wasn't as clean. Euro was choppy.

[00:20:53]
Okay. Looked like he formed up an M. He spiked. This trade would have scratched out with a few pips.

[00:20:59]
But he did something really neat. He was divergent on TDI, and he went back right to the blueberry

[00:21:06]
and made a bigger, bigger M formation. Now, if you're looking at your charts,

[00:21:12]
remember not micro, not getting caught up in this small view, getting understanding the bigger picture?

[00:21:20]
This level in here is part of another multi-session, right?

[00:21:26]
This is actually leg two of a bigger picture. Let me pull that picture up for you.

[00:21:34]
And what you have in essence is a 22-trade on the four-hour chart.

[00:21:38]
Excuse me. Who's my voice? All right. Here's what I mean. Let me go back to this and switch it for you.

[00:21:48]
Here's what I'm talking about. Okay? I don't know if you guys caught this or not.

[00:21:55]
On the four-hour chart, you have a bigger, bigger thing going on. You have a 22-trade.

[00:22:02]
We grab the pen.

[00:22:08]
Okay. Notice how the deal or just misses the previous high? Just misses the previous high in here.

[00:22:20]
Very important to see that. The fact that he came near it, remember the spread, he works the spread.

[00:22:29]
The dealer works the spread by coming near the high and opening the spread above that level,

[00:22:35]
above these pens right here. Why would he do that? Some stop losses right in here and possibly some

[00:22:41]
pending to go long for the breakout traders. So when he gets in there, he activates those orders, right?

[00:22:49]
Activates the orders and pulls away. There's a clean entry right there on a hammer.

[00:22:58]
A big fat multi-session over a couple weeks, two weeks. Hope you guys saw that.

[00:23:05]
Then when you get into the micro view, this would be your... I'm sorry, clean this. This would be your M.

[00:23:19]
Wow, that's weird, the only race. Okay. This would be your bigger M. This would be your second leg of a second leg.

[00:23:29]
Okay. Slightly higher, but understand what the dealer did. He hit it and closed back below aggressively.

[00:23:38]
Okay. Everybody see that? Okay. It's awful quiet in here. Thank you, Subio. All right, we're still alive.

[00:23:46]
Okay. Is this level three yet? I don't know.

[00:23:54]
How come you don't know Steve? I thought you know everything. I don't know everything, but here's the reason why.

[00:23:58]
I want to see some of this. I got to see it bottom out a little bit. Okay. We need to see something bottoming out.

[00:24:04]
Then we can make our anticipated move. Is this level three or are we still developing level three? We don't know yet.

[00:24:11]
Let's see what happens. Time will tell. Time reveals everything.

[00:24:17]
Patient, let's see if the dealer makes the W or if he comes right back and breaks the high. Let's see what he does.

[00:24:24]
Don't make a decision on anything. Open your mind. Open your mind to the possibilities that the dealer can go either way.

[00:24:33]
Remember I told you, trade both ways without fear. The dealers do. They don't go like, oh shit, that's against the trend. I better go long.

[00:24:40]
They don't care. You shouldn't care either. The dealer issues you a signal. You take it.

[00:24:48]
Yes, Stephen, E.U. dropped over 123 PIP, and I'm sure you called every last one of them, my friend.

[00:24:55]
Okay. The coin of phrase from that movie, you can't think of it for your mind, Neo, right?

[00:25:06]
The matrix. Open your mind. Just open your mind to the concept that when the dealer shows you his hand, you pounce on that opportunity.

[00:25:15]
Nothing else. A lot of you are anticipating the spike to the low as the actual low of the day and you're jumping on that. That's not a trade.

[00:25:24]
The trade is when the dealer settles in or bottoms out, throws some spikes to the downside or the upside. You take the opposite of those behaviors.

[00:25:35]
Okay. That's what I want you to see. All right, let me race. Let's get on with it.

[00:25:48]
All right. Hope you saw this. I don't know what's going to happen in here. I don't know if the dealer on your own.

[00:25:58]
Okay. Let's see what happens. Let's see what he does.

[00:26:07]
Okay. I don't know if he spiked slightly past here to grab up the orders and he's going to reverse. Let's see what he does tonight or because he broke below this level, he's going to pull back and correct.

[00:26:19]
Okay. All right.

[00:26:27]
If you're not seeing this stuff on the four hour chart, go and open up the four hour chart and start marking it. Remember, the first four hours, the Asian session.

[00:26:36]
Okay. The Asian session of the week is the first two four hour bars, eight hours. That sets the psychological support and resistance zone that the dealer will exploit for the week.

[00:26:48]
He'll spike to the low. He might spike to the high. Understand what he's doing. That's the point of the drills. Okay.

[00:26:55]
The answers are in here, man. Everything that you need is here. It's right here.

[00:27:00]
We're going to talk about ADR high and low, some pivots and how this stuff ties together with the big picture. Okay. All right. Let's talk about ADR and how to use it.

[00:27:15]
The ADR is more useful for the New York reversal. Not saying you can't use it during other times of the day, if the dealers made the move during the Asian session.

[00:27:26]
Remember, the ADR is a range that they have to work with for the day. It's the average daily range for those you don't remember what it stands for.

[00:27:39]
They have limitations of about 200 pips. I'm getting out of context here with the slides. Let me catch back up. Okay. The ADR, my whole life of what we've seen it plotted as an oscillator.

[00:27:52]
And it looks like this. Average true range ADR. I've seen it plotted as a line graph. I can't do anything with this. To me, that it's worthless.

[00:28:05]
So, let's see if that works.

[00:28:12]
It's hard to read this. So what we did is we took the values and plotted them for hard targets on the chart.

[00:28:24]
So at the open, the ADR will straddle price. Okay. The ADR moves. It changes during the day. Keep that in mind.

[00:28:34]
That you'll notice the red lines before their hit, their light orange, they'll move. They'll creep up or creep down to try to fit price action, so to speak.

[00:28:44]
Okay. They're a moving grid. If you didn't know they moved, they move. Okay. Not repaint. They adjust for price action.

[00:28:57]
Okay. So now, if, let's just say for example, it goes up and hits the ADR high and starts to correct. Okay.

[00:29:08]
You're looking for the New York reversal trade to come somewhere in around the ADR or past it for the W formation.

[00:29:14]
Is that always true? No. But this should be part of your subset of rules for you to take those trades. Okay.

[00:29:25]
Zen has his checklist. I'm pretty sure it's in the forum. But part of his checklist for looking for a New York reversal trade is that price has met or exceeded the ADR.

[00:29:37]
It's overextended. Price has ran past the average daily range. The dealer will correct back in when he throws a signal to get back into the range so that the open and close is less of a distance.

[00:29:57]
Okay. If the ADR is met or exceeded, then that pair should get on your radar. Okay. If you have your pairs like this and you're looking for the new trade,

[00:30:06]
you have your pairs like this and you're looking at them, you come and you see Euro, EU, and GU, right, have met the ADR or exceeded the ADR, then you could stop monitoring the other stuff that haven't reached.

[00:30:21]
And this should become the two pairs you're stalking for your US reversal trade. Okay.

[00:30:27]
Asubio puts it as they should get your attention. This should be, I get my attention guideline, meaning that you're monitoring your six or twelve pairs.

[00:30:36]
Nothing's reached the ADR today. Maybe EU, GU has. Everything else is off your radar. These two pairs move to your screens. And this is what you're looking for a setup for.

[00:30:46]
They got your attention now by exceeding the ADR. Okay.

[00:30:58]
All right. They act as intraday support and resistance. All right. You know, I hate the word support and resistance, but it is what it is as part of the business.

[00:31:08]
If the ADR is triggered and the dealer forms the patterns that we talk about at the ADR, that's telling.

[00:31:20]
That tells you that the dealer has made his entire run for the day. We know that they always complete the cycle.

[00:31:27]
Twenty-five to fifty pips off of the higher low, depending on the pair, right? And they want to end back in the range to trap the traders for tomorrow.

[00:31:39]
Okay.

[00:31:43]
So, if we know that this is coming to end the day, and we know that the dealer has made the pattern when we approach the screen, and ADR has been met or exceeded.

[00:31:53]
Try to tie this together over here. Yeah. Okay. So we know it acts as intraday support and resistance. Was that the slide I was on? I don't think so. I think it jumped.

[00:32:02]
Yeah. Okay. All right. Access intraday support and resistance. It might line up with a pivot point, which is also a fixed grid.

[00:32:16]
Okay. So, what do I mean by a fixed grid and a floating grid? ADR is a floating grid. It moves. The pivots are a fixed grid.

[00:32:26]
So, if the floating grid floats over to the fixed grid and they line up, it's a good place to look for the reversal.

[00:32:41]
It lets you know where you are in the move. What do I mean by that? Well, if you come to your terminal and you miss most of the move, and you see that you are...

[00:32:50]
Okay. So, anyway, let's you know which type of move might be warranted. What do I mean by that?

[00:32:56]
Well, if price has been dropping all night and the ADR has exceeded, if you don't expect it to continue to drop, you expect it to reverse back into the range.

[00:33:10]
You expect to see three levels of push, right? Three intraday bursts of price. Okay. Levels push. Everyone's got a different term for them, so I'm trying to cover them all.

[00:33:23]
But when the ADR is met, you usually will see your three levels. Not always. The third level might develop above or below the ADR.

[00:33:35]
Now, think for a minute. You come to your terminal, you're looking for a New York reversal. Price has been running up all night.

[00:33:44]
It's exceeded the ADR, but it's 8.30 in the morning. What do you got? What do you do? Welcome to the Candice Shop. Don't trade until they hit the stops.

[00:34:01]
All right, that's it. It's all you get in ADM this week. If it's 8.30, the best thing to do is to wait until 9.30, 9.45 into the new session. Why? How many times have I said, welcome to the Candy Shop. Don't trade until the dealer hits the stops.

[00:34:23]
When do they hit the stops? Session beginning, session end. Okay. So if it's the end of the session going into the U.S. session, ADR has been exceeded. They're chopping around that level. It's 8.30, 8.45. You know that at 9.30, the new session, the new market maker comes on, and he has different idea of what he's supposed to do.

[00:34:46]
So now you take the ADR, the timing, and the fact that the dealer needs to hit the stops. You tie those things together, that will give you a solid New York entry.

[00:35:00]
Okay, I'm going to tie pivots in the blue tracer into it in a minute. The other three elements that are on the chart.

[00:35:09]
If you're in a trade, and it happens to be Wednesday, Thursday, Friday towards the end of the week, most of the time with the exception of non-farm towards the end of the week, the dealers meet or exceed the ADRs.

[00:35:28]
Why is that? Because think about this for a minute.

[00:35:34]
The pattern, the pattern, the pattern. Okay. That's the Asian session for the week. So if you understand how the week develops, Sunday, they set the psychological support and resistance.

[00:35:51]
Monday, perhaps they make a false move. Tuesday, the high of the week is formed. Wednesday, Thursday, Friday. Okay. Obviously this is textbook, it doesn't play out like this every week.

[00:36:12]
The dealers have other targets in mind. They have to meet some fundamentals. They have to do other stuff. But if you break this down like this, then the micro pattern within the pattern is in here.

[00:36:26]
Consolidation hit the stops high drop. Consolidation hit the stops high drop. End of the week reverse to end Friday back into the range. So you'll have the pattern of this.

[00:36:38]
Okay. What we're essentially doing is breaking the pattern down into smaller pieces. And for the week beginning, you might have this to move up.

[00:36:48]
So when you look at this, it's days of rise or fall spread out over the course of the week with the micro pattern in mind.

[00:37:04]
The micro behaviors that the dealer makes intraday to form up the major pattern intradique, which forms up the daily charts, the weeklies, which is all the same shit.

[00:37:14]
Go look on the four hour. You'll find the big multi session M or W. You'll find a simple W within the week. You'll find an M. I showed you an M on Euro, which was part of a larger M from the week previous.

[00:37:30]
If you understand that the week on the four hour chart is this pattern and that the intraday pattern is the pattern, right?

[00:37:41]
It's all the same thing. And to take it one further, I guess the micro would be with Kim likes to trade. Kim K from the DMR likes to trade the intraday pushes.

[00:37:52]
Right? We talk about the intraday safety trade after the peak comes in. She trades the pushes within the levels, intraday pushes.

[00:38:03]
Okay, I think that's what they call them over there. I'm kidding. You understand breaking it down and putting dates on it or days on it helps you understand the bigger picture.

[00:38:17]
Okay, helps you realize that the ADR has merit because the dealer has a limited amount that he can work with.

[00:38:26]
The weekly range is 600 to 1000 pips. Can you notice that they've been shifting the zone aggressively in the pound? Why? Because quarterly and seasonally, they have targets that they have to meet.

[00:38:46]
They're probably set by the creature from Jekyll Island, the families. That's the, that's like deep shit. I don't even know. Shouldn't even say it. It's just there. Read the book.

[00:38:55]
They have fundamental targets where they need price to be. But understand that along the way the dealer behaves exactly as an illustrator for all of us to reach those targets.

[00:39:12]
Okay, trade in line with the dealer when the signals appear. Don't get bent on trying to short the pound and it's rising, Luther.

[00:39:25]
Eventually it will correct, but only when he displays a signal.

[00:39:31]
Okay, by the way, I'm picking on him, but I wanted to congratulate. I forgot earlier to mention it. I wanted to congratulate Luther and Kirk.

[00:39:39]
They went five for five this week. And they had a fantastic week trading man. I'm proud of those guys. They came to the meetup. Well, Kirk flew into the meetup.

[00:39:47]
And hung out and they're getting their shit together man. I'm proud of them.

[00:39:53]
So anyway, that was pretty good. Luther wrote Yeah, bitches, but I probably shouldn't have said it, but I did anyway. I'm proud of you guys man.

[00:40:03]
Okay, back to the stuff. By the way, they were taken 3540 trades a piece a week and they realized that that's not the answer. The answer is quality setups less often confirmed trades that will pay out. That's how you go five for five.

[00:40:20]
That's one trade a day. Every day without a loss. Think about that. Pretty powerful stuff.

[00:40:29]
Okay. The daily low or the high low marker. The blue tracer is an area where the deal, I'm scared to draw. I'm scared to do that thing.

[00:40:45]
Where the dealer sets his traps. There's a lot of people that trade breakouts. They trade breakouts above yesterday's high and below yesterday's low. There's a guy's name. I'm not going to say it. But that's his whole method is based on that.

[00:41:02]
And in a way, it makes sense that if the trend is up, that it should break the high and that would be a good run.

[00:41:10]
But you understand the dealer swings. That's what they do. They swing back and forth. So what happens is you get whipsawed out of those breakout trades.

[00:41:19]
Okay. So when the 80 are high low couples with the pivot point, the blue tracer.

[00:41:30]
And then maybe something else gets thrown in the mix. The blueberry. We saw Euro M form to the blueberry.

[00:41:39]
Right. Maybe the 50. Manage or the waters laying near the blueberries. And then the dealer hits the ADR right at those levels.

[00:41:52]
Spikes past it. You got to think, man, what's going on here? The dealer has a ready exceed the ADR.

[00:41:58]
It's been three days of rise. He just closed above the blueberry. I'm looking for the M back into the range, man.

[00:42:10]
Okay. As soon as I say that, he'll run right past the blueberry. But think for a minute.

[00:42:15]
That is why you use a stop loss. Okay. A tight stop loss. If you're wrong and he cuts the blueberry and extends the high, that's the wrong direction.

[00:42:30]
Okay. What you're looking for is a set of clues or all these pieces of the puzzle coming together.

[00:42:38]
At the appropriate time to give you your setups. Okay. So let's go through the list.

[00:42:45]
TDI shark fin blood in the water. You've done the drill. ADR met or exceeded.

[00:42:55]
Yesterday's high lows laying there, blue tracer, a pivot point. That's a pretty good zone of where at 9.30 in the morning.

[00:43:08]
You're going to get the reversal. Okay. You might have outside structure to the high. You might have another push. Three little pushes inside.

[00:43:17]
The 3333 trade might show. Right. Three intraday pushes with the last batch of acceleration being three pushes. All right. You guys remember that?

[00:43:28]
Right. Intraday three. One. Two. And then right before the dealer makes the reversal, he pushes three little babies. Right. Right to the high. And then he pulls back.

[00:43:43]
That shows trend acceleration and gets everybody to bite long. And then he says, just kidding. Takes it all back.

[00:43:53]
Okay. These little pieces tie to the ADR, tie to the light blue tracer with a piece of manage running over there. A jar manage running across there.

[00:44:03]
That's a pretty good indication it's going to reverse.

[00:44:11]
Those are the things you're looking for to come together at the right timing. This so happens to be 9.30. That's a setup.

[00:44:19]
9.45 the dealer makes the second leg. Hits the stops and corrects. Okay. Seems like we've seen that one already. Okay.

[00:44:31]
Yep. We did that. Okay. So here's what I'm talking about. All these things coming together. This is your zone. You expect to deal with your work in here.

[00:44:40]
Okay. You expect to see some action in there. You expect to see the dealer make the M or the W. In this example, it's the W because we're at the support side of the structure.

[00:44:53]
All right. Okay. So now. Here's a couple of examples of the zone coming together. Okay. There's your manage, your M3.

[00:45:07]
Your ADR marker, the ADR marker shifted. But down here, look what happened. The dealer came into the zone. There's your M1. He exceeded.

[00:45:19]
Right. Here's the micro pattern within the pattern. Don't trade until I hit the stops. Oh, got him. 9.45 reverse back into the range. There's the micro pattern. Right.

[00:45:31]
Right. It's the pattern within the pattern. The dealer hits the stops to the downside, snatches it away, runs back into the middle of the range.

[00:45:40]
ADR, what do you got here? You got yesterday's blue tracer. ADR, met or exceeded.

[00:45:47]
Find and support on a pivot. This is an M1 M3 day. I'll talk about that next. If you're confused.

[00:45:55]
Okay. ADR high, pivot point, just inside the session. Actually later in the day, sorry.

[00:46:09]
Okay. Look what's going on here. Okay. The dealer is working right past the low, spiking it, pulling it back. He spikes it, pulls it back.

[00:46:17]
Spikes it, pulls it back. Hits it again, pulls it back. I want you to think about this for a minute. This is important.

[00:46:27]
This is going to help you with your decisions. This pin right here and this railroad track right here. Okay.

[00:46:36]
The dealer's working the low, right? Sorry. All right. Hold on. Someone said to take a sip of coke, hope they're losing my voice.

[00:46:48]
Okay. I'm trying to present strong. I noticed right the meter wasn't pegging. Okay. Let me adjust this a little bit into my face.

[00:46:59]
All right. I'm back. I'm strong. It's hitting red. Okay. Here's what you need. Here's what's going on.

[00:47:06]
I want you to think about what's going on here with these pins when they're slightly lower than the W formation.

[00:47:13]
Okay. Think about the psychology. Think about what's happened here. All right. Let me clean it up. All right. Hang with me a minute. The dealer spikes the low and pulls it back.

[00:47:29]
He picked up some orders. He spiked the low and pulls it back. During this 45 minutes to an hour, some amount of training is going to be in the middle of the road.

[00:47:42]
The traders went long, right? Some volume, 100 million, 200 million. I don't know. No one knows. But some amount of traders saw this coming and went long, right? Now, some amount of traders placed pending orders in here as a break opportunity to go short.

[00:48:08]
Okay. That's why the dealer comes back and spikes below this zone. It's a twofold or two-pronged approach.

[00:48:24]
He triggers the stops of the people that went long and put their stop-loss, right? In those textbooks, stop-loss goes three pips below the entry bar.

[00:48:31]
I've read it a thousand times. This is the stupidest thing I've ever read. I've read some stupid shit in my life, and that's pretty stupid.

[00:48:41]
Okay. The dealer comes right back, picks up those stops with this spike that's slightly lower, and he also grabs the pending orders of the people that were looking to break short.

[00:48:58]
That's what he's doing. Okay? So he pulls back again, and he looks at his book, and he says, ah, I need a few more bucks. Besides, it was fun to take all that money off the table.

[00:49:09]
He goes back, and he does it again. Okay?

[00:49:16]
Understand that it's not normal to make three or four hits to the low, and I've said it a hundred times. Don't hit the low or high in front of me three times.

[00:49:31]
Okay? The question is, Steve, if this was the low of the day and the number changed on the big board, right? Yes, it did, but he closed all the way back above.

[00:49:41]
By closing aggressively high off of that low, he induced a boatload of traders to take it long.

[00:49:49]
Then he comes right back, right? Hit the stops this way. Hit the stops this way. Think about it. Hit the stops. Hit the stops drop. Hit the stops. Hit the stops rise.

[00:50:00]
Look at that. Hit the stops. Hit the stops. Okay? He comes back one more time, shows a close-up of the day.

[00:50:10]
He goes below the previous number. And then within 15 minutes, he takes it back. That's what's going on in this context right here. All that. That little pattern right there. Understand when you see this structure, when you see this stuff, this is what's going on in here.

[00:50:30]
Hit the stops high. Hit the stops low. Induced traders to take positions. But notice that the behavior is at the low. The ADR low is lit locked. It's slightly exceeded. He's working the tracer to pick up the pending orders. And then he comes right back above. This is the anticipated direction of this move, and that's how it played out. That's what I want you to understand what's going on, the structure. Okay?

[00:51:00]
This one was quick. He went right down past the ADR. He spiked it to the M1. And then he reversed away quickly. Those are the A or V formations. You can't always get those unless they're part of a bigger structure.

[00:51:17]
Okay? If you're not, if you're missing these or passing up on those, I commend you. I want you to trade this, and this, and nothing else. I want you to learn to trade only those.

[00:51:29]
Some of you can't stand it. That's fine. If you see it and it's clear to you, take it. Perhaps there'd be a W in the TDI RSI line. That would confirm this. You got other stuff going on.

[00:51:45]
Just by looking at this chart, look where you're at. You're in the US session. The ADR has been exceeded. You're at the pivot. The dealer spikes and pulls back.

[00:51:56]
That's an OK entry. This is a better entry, always. Always, always, always. Okay.
