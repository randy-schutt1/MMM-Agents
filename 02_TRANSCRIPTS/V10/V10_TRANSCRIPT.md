# V10 — TRANSCRIPT

## SOURCE

| Field | Value |
|---|---|
| Video ID | V10 |
| Original filename | `Bootcamp1 Wk3 040112 (96mins).swf` |
| SHA-256 | `a37ba371ca2d5c807553c7b9a827a91c479509dd5223b64eadf85995481a3de1` — re-verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session, on the flat `Bootcamp/` canonical path, **and re-verified again after the frame-rate patch** to prove the original was not modified (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| Duration | 01:36:16 (audio measured **5776.222041 s**; SWF header **11,553 frames ÷ 2.0 fps = 5776.5 s**; `SOURCE_MANIFEST.md` 01:36:16 = 5776 s — three independent figures, agreeing) |
| Lesson title | **PRINTED — and this is the first title card in the corpus since V08.** The lesson opens on a slide reading **`Market Makers Boot Camp`** / **`Week 3`**. That is a **session banner**, not a topic title, and **no topic title is asserted here.** The quarantined per-lesson header's *"Primary Topics: Multi-Timeframe Alignment (H4/H1/M15), Structural Anchors & Intraday Execution"* is fabricated **and is contradicted in terms by the lesson itself** at `[01:13:47]` — see `QUARANTINE_REGISTER.md` **Q-011** §1 |
| Session date | **2012-04-01**, from the filename `040112` and `SOURCE_MANIFEST.md` — **and stated in the recording**, `[00:21:25]` *"Today's April 1st the quarter's over"*. **A new week and a new date**: V06–V09 all shared 2012-03-26. The printed *"Week 3"* independently corroborates `D-017` §2's ordering for this file |
| Frame rate | **2.0 fps** in the SWF header — **not the 3.0 fps of V01/V02.** The `SWF_CAPTURE_RECIPE.md` §10 patch for a 10× sweep is therefore **2.0 → 20.0**, not 3.0 → 30.0. Recorded because the recipe states the V01/V02 figure as if it were the library's |
| Stage size | **1024 × 786** — the majority class. `SWF_CAPTURE_RECIPE.md` `GOTCHA 5`'s table gives `(512, 300)`, and the pre-click/post-click guard **confirmed it fired** rather than assuming it |
| Transcribed by | ASR, by a pre-ingestion session. Copied and verified 2026-08-13 — see VERIFICATION below. The pre-ingestion file's own `# VIDEO` header block is **NOT carried over**: its *"Course Position: Video 11 of 21"* is wrong under `D-017` §2's renumbering, and its *"Primary Topics"* line is both unsourced and contradicted. Only the verbatim body is copied |
| Transcription confidence | MEDIUM–HIGH — the best-structured transcript the corpus has received; see TRANSCRIPTION NOTES for the defects that remain |

## SPEAKER TABLE — MANDATORY UNDER `D-025` consequence 3, re-adopted by `D-033`

| Speaker | Runtime | Basis |
|---|---|---|
| **The course author (Steve Mauro)** | **100% — the whole file, `[00:00:00]`–`[01:36:12]`** | See § SPEAKER IDENTIFICATION |
| Any guest | **NONE** | No second voice; no handover language anywhere in 96 minutes |

> ### ⭐ THE FIVE-LESSON GUEST RUN ENDS HERE
>
> **V05, V06, V07, V08 and V09 each carried ZERO course-author runtime.** V10 carries **100%**.
> `COURSE_PROGRESS.md`'s V10 GATE carry-forward item (a) called a new week and a new session date
> *"a REASON TO EXPECT A CHANGE, not a reason to assume one"* and instructed that it be **tested**.
> It was tested, on evidence chosen before the answer was known, and **the change is real.**

## SPEAKER IDENTIFICATION — HOW IT WAS ESTABLISHED

`D-033` makes every speaker's material equal in authority, so this determination changes **no
rule's weight**. It is provenance, and `D-025` consequence 4 binds: **nothing in any V10 artifact
depends on the identification being right.**

**Five independent strands, none acoustic.** The `f0_profile.py` acoustic screen was **NOT run
across files** — V07's carry-forward prohibits it, and V09 and this session both honoured that.

| # | Strand | Evidence |
|---|---|---|
| **1** | **The speaker owns the email address** | `[00:07:12]` *"my only valid email address right now is Steve at"* / `[00:07:16]` *"marketmakers4x.com"*. Not a reference to Steve — a **first-person claim of Steve's mailbox** |
| **2** | **Every one of the 13 `Steve` tokens is vocative or self-quoting** | The speaker voices students addressing **him**, then answers in the first person: `[00:35:53]` *"Why does Steve have this stupid little blue line on the chart"* → `[00:35:59]` *"No, it's on there because it serves a purpose"*. Also `[01:18:37]`, `[01:19:19]`, `[01:21:37]`, `[01:23:57]`, `[01:05:39]`. **In V04–V09 the guest speakers referred to Steve in the third person as an absent authority; here the name is only ever pointed at the microphone** |
| **3** | **He reads mail addressed to himself, and the slide shows it** | `[00:12:53]` *"Hi, Steve. Thanks for your turn to me so quickly about the ADR correction"*. The rendered slide at burned timecode `08:38` prints an email opening **`Hello Steve`** — an artifact of the recording, not of the ASR |
| **4** | **He claims authorship of the method and the course** | `[00:12:45]` *"Resemble what it is I do in fact teach you guys"*; `[00:04:14]` *"…said Steve I could rehearse **your** method"*; `[00:05:06]` *"on behalf of market makers 4x [and] compass FX we're gonna be hosting a seminar"*; `[01:28:11]`–`[01:28:22]` *"I wrote the lesson. I give it to my wife. She converts it to slides"* |
| **5** | **He owns the homework loop end to end** | `[00:17:49]` *"do not mail me the homework post it in the forum"*; `[00:20:38]` *"my mentor would not do the next lesson until he was handed by me my homework"*; `[01:34:26]` sets the week's assignment himself |

**Negative check, run deliberately:** a scan for handover language — *take it away, hand over,
turn it over, I'll let, introduce, thanks for having me, the floor is yours, passing it to* —
returns **zero matches in 96 minutes.** V04's handover was unannounced but produced an audible
topic seam; V10 has no seam, and its closing Q&A (`[01:35:14]`–end) is answered in the same voice
that opened it, in the first person, with personal preferences (*"I personally like London"*).

## COVERAGE

```text
STATUS: COMPLETE -- no fenced tail, no gaps
Covered: 00:00:00 - 01:36:12
Entries: 1,184 markers, 1,184 distinct.
         Timestamps are STRICTLY INCREASING: zero decreasing transitions AND
         zero same-second adjacent pairs. (Stated as MEASURED, by scanning the
         body for lines fully matching ^\[\d\d:\d\d:\d\d\]$. V03's coverage
         block was charged at R1 for asserting strictness where it was false
         and V09's was NON-strict and said so; V10's IS strict, and this block
         claims that only because it was checked.)
         Zero markers fall past the measured runtime.
         Largest inter-entry gap 12 s, FOUR times: [00:19:15], [00:41:10],
         [00:47:16], [01:29:41].
         Next largest 11 s, TEN times; 10 s, THIRTEEN times.
         Modal gap 4 s (194), then 6 s (188), 5 s (184), 3 s (177), 2 s (148).
         Final entry [01:36:12] against measured audio 5776.222 s (01:36:16.2).
```

**The ~4 s tail is not a gap and not a fence.** A Whisper `small.en` pass over `01:35:30`–end
returns a final clause *"…you don't want to do the work"* and nothing after it; the transcript's
own final entry `[01:36:12]` reads *"You felt too far behind you don't want to do the work"*.
**Both engines stop on the same words.**

**The lesson ends mid-exhortation**, on the third consecutive file to end without a formal close.
Unlike V08 (mid-argument) and V09 (mid-clause), V10's final sentence is **grammatically
complete**; what is missing is a sign-off, not a predicate.

## VERIFICATION — FOUR INDEPENDENT AXES

This transcript arrived from a pre-ingestion session and is covered by `SETUP_ISSUES.md`
**I-008**. It was **not** trusted on arrival.

**1. The audio the transcript was made from is this lesson's audio.** The pre-ingestion folder
holds `audio_11.mp3`. **The `_11` is not an error and it is not a red flag** — folder numbering
under `Bootcamp Notes/` was changed by `D-017` §2 so that folder `NN` = video `VNN`, and under the
*pre-renumbering* alphabetical order this lesson sat at position 11. The file sits inside folder
`10_Bootcamp1_Wk3_040112_96mins`, so the mismatch is the expected fossil of that renumbering.
Tested rather than reasoned about:

| Check | Result |
|---|---|
| Duration of `audio_11.mp3` vs audio extracted from the SWF by this session | **5776.222041 s vs 5776.222041 s** — identical to the microsecond |
| SHA-256 of the two files | **differ** — different encoder settings, as with V08 and V09 |
| Raw waveform Pearson `r`, five 20 s windows (`t = 300, 1500, 2900, 4300, 5500 s`) | **+0.001 / +0.004 / +0.054 / +0.005 / −0.002** — ≈ 0 |
| **Energy-envelope cross-correlation**, same five windows, ±2 s lag search | **r = 0.986 / 0.985 / 0.987 / 0.965 / 0.987**, all at lag **−0.02 s** |

The near-zero waveform correlation is the mp3 re-encode's ~20 ms coder delay. **V08 established
that a null waveform correlation between two encodes of the same audio is expected rather than
diagnostic; V09 reproduced it; V10 is the third reproduction** — same envelope range, same
−0.02 s lag, on a third lesson of a different length. The reading is now well-supported and
should be treated as the expected signature, not re-litigated per lesson.

**2. The transcript is an ASR of that audio, not a fabrication.** **Eight** 45-second windows
spanning the full 96 minutes (`t = 0, 900, 1800, 2700, 3600, 4500, 5400, 5730 s`) were
re-transcribed independently with Whisper `small.en` and compared word-for-word after
case/punctuation normalisation:

| Window | Transcript words | Whisper words | Word-level similarity |
|---|---|---|---|
| 0 s | 132 | 126 | 0.907 |
| 900 s | 147 | 146 | 0.853 |
| 1800 s | 84 | 69 | 0.889 |
| 2700 s | 53 | 47 | 0.900 |
| 3600 s | 130 | 108 | 0.874 |
| 4500 s | 122 | 124 | **0.967** |
| 5400 s | 147 | 145 | 0.904 |
| 5730 s (to end) | 113 | 116 | **0.961** |

**The disagreements are the evidence.** The decisive one is in the 900 s window:

| Marker | This transcript | Whisper `small.en` | The actual words, from context |
|---|---|---|---|
| `[00:15:12]` | *"I think it says **the incoming**, baby"* | *"…**they ain't coming**…"* | **they ain't coming** — Whisper is right. This is the lesson's own refrain, which *this same transcript renders correctly elsewhere*: `[00:16:37]` *"He **ain't coming** back baby"`, `[00:52:16]` *"because he **ain't coming** back, baby"*, `[01:17:05]` *"the price **ain't coming** back"* |
| `[00:15:12]` | *"that is **a lu** owns the rights to that"* | *"…**Lew**…"* | **Lou** — a person, named earlier at `[00:04:48]` *"Lou from New York is shot"* |
| `[00:15:24]` | *"Those you **scorn** at home"* | *"…**scoring**…"* | **scoring** — *"those of you scoring at home"* |
| `[00:15:02]` | *"and we **advise** the traders are trapped"* | *"…**are advised**…"* | are advised |

> **A fabricated transcript does not garble its own catchphrase in one place and get it right in
> three others.** `[00:15:12]`'s *"the incoming"* is the single most probative line in this file:
> the fabricating generator that produced `RULES.md` and `VISUAL_INDEX.md` writes fluent,
> confident, well-formed English (`Q-011`). It does not produce *"the incoming"*.

### TRANSCRIPTION NOTES — systematic defects, named here so no note inherits them

1. **Numeric ranges wobble, and one of them is load-bearing.** The safety trade's distance from
   the anchor is given **six times** and the ASR does not render it identically:
   `[00:49:39]` *"25 75 pips"*, `[00:52:03]`–`[00:52:09]` *"20 To 75 25 to 75 is easy to
   remember … 20 to 75 pits"*, `[00:58:30]` *"This box is 50 75 pips"*, `[01:15:36]` *"25 to 75
   pips"*, `[01:16:20]` *"25 to 75 pips"*, `[01:23:16]` *"25 to 50 25 to 75 pips"*.
   **The modal and self-corrected form is `25 to 75`** (the speaker says *"25 to 75 is easy to
   remember"*, which is the correction landing in real time). **This is recorded as an ambiguity,
   `A-078`, and no single figure is adopted.** `pits` is the engine's rendering of *pips*.
2. **`ain't` is unreliable.** See the table above. Any quotation in `03_LESSON_NOTES/V10_*` that
   turns on this phrase carries its marker so a reader can re-listen.
3. **Proper nouns are unreliable** — `a lu`/`Lou`, *"marketmakersforks.com"* and
   *"Steve at MMM forex"* at `[00:07:38]`–`[00:07:44]` against the correctly-rendered
   `marketmakers4x.com` at `[00:07:16]`. **No V10 artifact depends on a spelled-out domain.**
4. **The engine drops the leading "Re-" on "Remember"** — `[00:13:13]` *"**Member** to end the
   day with long holders trapped"*, `[00:11:43]` *"**Member** I told you the market makers only
   have a handful of moves"*. This is a **positive** authenticity signal, not a hazard.
5. **`[01:16:20]`'s `L. O. W. R. H. O. W` is `LOW or HOW`** — low-of-week / high-of-week, spelled
   out by the speaker. Rendered as spaced initials. The reading is confirmed by
   `[01:13:58]`–`[01:14:06]`, where both are spoken in full.

---

# VERBATIM TRANSCRIPT

*Body copied unaltered from the pre-ingestion file. **Nothing has been smoothed, corrected or
completed** — the defects catalogued above are left in place, because they are the evidence that
this is a machine transcription of real audio (`REMEDIATION_PROTOCOL.md` §2).*

[00:00:00]
I hope everybody's doing okay. Welcome back week three

[00:00:03]
Hope you guys are starting to turn the corner and having some improvement in your trading

[00:00:08]
Glad to see everybody here and I look forward to a good session tonight. All right, let's roll

[00:00:16]
Okay, welcome back. We're still in the no BS zone, man

[00:00:19]
All right, no excuses no stories everyone has problems do your homework

[00:00:26]
Mark up your charts make your flashcards. That's it

[00:00:30]
All right, thanks for all the warm and caring emails. I want to thank everybody for the well wishes

[00:00:35]
They sent me and the nice stuff that was said in those emails. Thank you guys

[00:00:39]
All right, let's get started chat box nothing's changed chat box is gonna be ignored till the end of the segment and

[00:00:45]
If I get carried away the chat box remind me

[00:00:48]
That I was supposed to be ignoring it all right it's hard sometimes

[00:00:51]
You guys make some harsh comments. I got a comment back all right

[00:00:54]
I'll open it up and take a few questions that are relevant to what I'm talking about at the end

[00:00:58]
All right, that's how I want to handle on a work a segment look at some questions take questions that are pertinent to the material

[00:01:04]
answer those

[00:01:05]
And move on I want to talk about the bulletin board and the student folder for a second

[00:01:12]
The bulletin board is kind of getting off on a tangent. It's going in different directions my hopes were that

[00:01:17]
You guys would discuss the topic at hand like this week for example the four-hour chart and not post a bunch of other stuff about levels and stuff

[00:01:25]
And give me a chance to teach it

[00:01:28]
So I guess the same would apply to the bulletin board or the forum

[00:01:31]
That's in here

[00:01:33]
Hold the questions that about trailing stops and other things that are not pertinent to what I'm talking about

[00:01:40]
Okay

[00:01:41]
So anyway, I hope that helps. I'm I know that the topic pages have gotten out of control

[00:01:46]
I'm probably gonna take all those pages condense them down and put them into like week one through three

[00:01:51]
And then we'll have week three through six or something like that

[00:01:54]
I know it's like 17 pages of correspondence now and it's out of control

[00:01:58]
I'll figure something out. All right. We'll get it handled

[00:02:02]
All right back to this page real quick, I've been talking about it managing your expectations what I expect from you

[00:02:08]
Follow along for free of distraction right now close the door kick your kid out run the dog out

[00:02:14]
Tell your wife to leave you alone for two hours. Nothing's changed man. Give me two hard hours a week

[00:02:19]
Someone's already writing nice gap on AU. It's rusty to a troublemaker rusty

[00:02:24]
I don't care right now. What I want you to do is focus on me the chart and AU were still gonna be there buddy at 830

[00:02:30]
Promise I had to bust your chops a little bit

[00:02:33]
Focus on me for two hours. I want two hours a week from you nutcases sit

[00:02:38]
All right, nice to see you buddy. All right refrain from negativity in your own mind and

[00:02:44]
Take your time to really soak up. All right. It was a good one. You got me rusty

[00:02:50]
Okay, man. There's no question that some of you are mental

[00:02:54]
All right, we just know that about you guys so all kidding aside no matter how well, you know my method

[00:03:01]
There's still a lot of you that are beating yourself in the business. Let me go full-screen

[00:03:08]
Okay, so reading through the emails

[00:03:12]
Here are some of the problems that I encountered a

[00:03:17]
Lot of you entering too soon not confirming the second leg

[00:03:21]
Exiting too early you don't believe that the mood it's gonna move in your favor for whatever reason

[00:03:28]
Displacing the blame not wanting to do the work. It's easier to point a finger at me your wife your kids your time your job

[00:03:38]
Mental blocks from your old system or baggage that you carry around

[00:03:41]
Too many indicators on your chart you just can't part with them for some reason

[00:03:45]
You love the rainbow stochastics and the MACD diamonds from 10 systems ago, and you just can't let them go

[00:03:52]
lack self-confidence you don't believe in yourself and

[00:03:55]
You don't have to discipline to execute the way you know you're supposed to the nine to five mentality the things I've talked about

[00:04:03]
Okay, these are some of the problems that I'm coming across on the emails now I

[00:04:09]
Can teach to you all day and all night. It's not gonna change anything

[00:04:14]
Somebody written me and said Steve I could rehearse your method, but I just don't understand why I can't see it

[00:04:20]
Well, you got to get your head on straight man. I can't teach you had a closure office sit quietly go through the charts

[00:04:27]
I can't teach you this. This is something that you got to commit on your own I

[00:04:32]
Absolutely have no experience in the psychological game, but I

[00:04:36]
Can ask a professional to have a look at your coconuts, so I

[00:04:41]
Know there's a lot of you out there that you far gone comes to mind. I'll go

[00:04:45]
Kim K's lost gone

[00:04:48]
Lou from New York is shot

[00:04:52]
So anyway, I'm kidding but those of you who aren't too far gone. I want you to join me for this

[00:04:59]
On behalf of market makers 4x and come up rest of your shot too, buddy

[00:05:03]
You're gone to put see ya

[00:05:06]
Anyway on behalf of market makers for us in compass FX

[00:05:09]
We're gonna be hosting a seminar Tuesday April 3rd at seven o'clock New York time seven New York

[00:05:16]
Okay, we're gonna feature dr. Ken revisit. We asked him to come to our Orlando class if you remember he had some health issues

[00:05:24]
Well, he's feeling better and he wants to come back

[00:05:27]
His title is he's the mine coach for the California Angels and now for you nut jobs

[00:05:34]
All right, so he's gonna be in here. He's gonna talk about the mental game how to up your game how to do your preparation

[00:05:41]
The mental part man the part that I cannot teach you

[00:05:46]
Okay, then's gonna be re-emailing the links

[00:05:50]
For those of you that are not encompassed as database if you're not gonna get a link from them

[00:05:54]
But compass FX will be handling all the links and signups for the event

[00:05:57]
It's on opening day, which is April 3rd for

[00:06:05]
Baseball cone size was his profession. He's a baseball coach mental coach. Okay. I think this is a nice addition

[00:06:12]
To help you guys with your mental game. I can't do it

[00:06:15]
I don't know what to tell you when I tell you do more charts. You don't want to hear that shit

[00:06:20]
So hopefully this guy can get inside your coconut and figure out the hell's rattling around in there or maybe not rattling around in there

[00:06:27]
Done everything I do is recorded the only issue is his copyright. I have not cleared that a hundred percent with him

[00:06:34]
I will get the answer and we'll announce it on Tuesday if it's gonna be recorded, okay?

[00:06:41]
All right

[00:06:44]
Good stuff. This is the email piece you should be getting if you want to write this down right now

[00:06:48]
Here's to go to meeting number six four zero four nine one nine one four

[00:06:52]
If you have that number you could sign in to go to meeting and join that meeting

[00:06:56]
Okay

[00:07:01]
All right cool

[00:07:03]
All right, let's get back to the bootcamp stuff

[00:07:06]
All right, let's look at some mail

[00:07:08]
Some of you are still emailing my old addresses. I'm looking at those for the next couple weeks

[00:07:12]
Then I'm shutting them down man. So please please please my only valid email address right now is Steve at

[00:07:20]
marketmakers4x.com

[00:07:22]
All other accounts are voided and will not be answered

[00:07:25]
I'm extending the courtesy for a couple of weeks of looking in there and letting letting people know to change

[00:07:31]
But I'm gonna shut those accounts down and not answer them anymore

[00:07:35]
All right, so I want to make sure I'm giving you fair and ample warning

[00:07:38]
This is the third week in a row morning you please move to Steve at marketmakersforks.com

[00:07:44]
Steve at MMM forex will be voided and

[00:07:47]
The Verizon address will be voided, okay?

[00:07:51]
All right

[00:07:53]
Email

[00:07:55]
I'm gonna read a couple letters that some people wrote and then we'll get back to the more stuff

[00:07:58]
All right. I hope all as well. I have attached the four-hour chart for EU as an example for the homework

[00:08:04]
By the way, I want you to put the homework in the forum. Don't mail it to me

[00:08:10]
Okay, I had noticed a pattern in the past however, I remember you and some of the other

[00:08:15]
Mentoring not to trade on Sunday Monday

[00:08:17]
Would it not make sense to trade against the false move week beginning until the high low is met just curious?

[00:08:22]
Is there any other reasons?

[00:08:25]
Okay, so here's what he's asking is it okay to take Sunday Monday off and

[00:08:30]
Wait for the market makers to make their false move and look for the peaks

[00:08:34]
The answer is yes, and no

[00:08:36]
If you're struggling and having problems seeing the dealer make their moves

[00:08:41]
Then the answer is it's okay to take Sunday Monday off till the dealer makes the false move and

[00:08:46]
Gets in the right segment of the market for you to trade

[00:08:50]
If you see this stuff clearly

[00:08:53]
And they're not having any problems then why would you take a day off because the pattern might come out perfect out of the box

[00:09:00]
All right, so if you're struggling or you're a newbie and you don't quite see it yet spend the time

[00:09:09]
And do some chart markups do some homework do some things that we've been talking about in here

[00:09:14]
And then look for the setups Tuesday through Friday

[00:09:17]
Okay, when I say Tuesday, I mean late Monday night going into Tuesday morning depending on the side of the world you live on

[00:09:24]
Okay

[00:09:27]
All right next email

[00:09:29]
Thank you very much for giving me more of your time and making all students understand your method

[00:09:32]
Just thinking about the last question you asked last Sunday about ways to improve your trading

[00:09:37]
I think entering a trade to early has to be one of the most popular mistakes

[00:09:41]
Because the biggest move can happen before in or after the London shadow. Yes, Jim. This is absolutely correct

[00:09:47]
One of the problems I listed a minute ago a lot of you're getting into early out of fear that you're gonna miss it

[00:09:55]
You got to get iron clad and you're thinking and wrap your head around this stuff

[00:09:58]
That's why we need a mental coach to get inside you nutcases

[00:10:04]
You got to become disciplined and strong and understand that the best trades

[00:10:09]
present in the second leg

[00:10:13]
Okay, remember I talk about what are the most important elements of my system

[00:10:17]
One through three the pattern the pattern the pattern

[00:10:20]
four and five timing and levels levels are a distant fifth to the pattern and the timings and

[00:10:29]
If inside that pattern

[00:10:31]
if we can add a 3a 3b it would be

[00:10:36]
the second leg M or W formation a

[00:10:40]
Confirm set up that collapses inside the averages and that will absolutely pay out

[00:10:47]
So someone said up your game

[00:10:49]
I'm up in mind rusty that you up your game stop taking shit trades and throwing your account under the bus and

[00:10:56]
Encouraging me out an email saying that I don't know what I'm talking about. I'm not mad. I'm just saying

[00:11:03]
All right, so listen

[00:11:05]
What I'm asking you to do is to find your discipline

[00:11:10]
That's the theme for this week cuz Ken's come in the town

[00:11:14]
Find your groove and stop taking everything that looks like an M or a W

[00:11:21]
Because you think it looks like an M or W. You just pull the trigger stop doing that to your account

[00:11:26]
Focus

[00:11:29]
Memorize the patterns through your flashcards and your sets and

[00:11:34]
Only take those trades that

[00:11:38]
have proven themselves in

[00:11:40]
history, okay

[00:11:43]
Member I told you the market makers only have a handful of moves when you start going through the charts

[00:11:49]
There's one high and there's one low every day. That's it

[00:11:53]
Wait for the high to set in take the trade short wait for the low to set in take the trade long

[00:12:01]
That's it

[00:12:03]
You can get a little more advanced and trade behind your back with the mouse between your ears

[00:12:09]
Running on your head as a mouse pad you can get cool. You can dribble it off the back wall and take a trade

[00:12:14]
You can do all that stuff later

[00:12:17]
But most of you are here because you asked for help

[00:12:22]
and help us here in the form of

[00:12:26]
You asked me to step up. I'm stepping up now. I'm asking you to step up

[00:12:30]
Stop taking shit trades in the middle of the range

[00:12:34]
Stop taking stuff that kind of resembles an M and kind of resembles a W

[00:12:40]
and only focus on those

[00:12:43]
setups that

[00:12:45]
Resemble what it is I do in fact teach you guys, okay? All right. Thanks for the email Jim good stuff

[00:12:53]
Hi, Steve. Thanks for your turn to me so quickly about the ADR correction on Friday

[00:12:57]
You mentioned three times ADR high load divided by two. All right. That was a mouthful, but here's what she's asking

[00:13:03]
If market makers run the ADR on Friday

[00:13:08]
What I expect them to do is

[00:13:11]
Return back into the middle of the range

[00:13:13]
Member to end the day with long holders trapped and short holders trapped

[00:13:18]
So the way to do that is to take the ADR

[00:13:23]
So track the high from the low divide by two that gives you about mid range

[00:13:28]
That's your 50% fib for Kali and Jim and Jim and the other fib guys that are in here

[00:13:35]
Okay, so if you like the fibs that's fine, but understand the dealer will end always

[00:13:41]
25 to 50 pips off of the high and

[00:13:44]
25 to 50 pips off of the low the reason for this is simple to trap the traders going into the weekend and

[00:13:52]
Hit them with the gap

[00:13:54]
Rusty

[00:13:57]
Okay

[00:14:00]
All right

[00:14:02]
Okay, another question when you mention the dealer only has limited make around 600 pips per week

[00:14:07]
Does that mean peak formation high ends of the week?

[00:14:09]
It means peak formation high to peak formation low 600 to 1000 pips

[00:14:17]
Is the range

[00:14:20]
And the dealer should correct or rise back off of that number into consolidation, okay?

[00:14:26]
Okay, why why 1000 pips you got account for pairs like GJ

[00:14:31]
GC you got to count for those big cross pairs that move a lot so

[00:14:35]
ADRs are a little higher

[00:14:38]
The range is about a thousand pips a week, but the dealer should come off that number and end back below that

[00:14:43]
Okay, unless he's shifting the zone or something else is going on all right

[00:14:48]
Okay

[00:14:50]
Just a quick question I've often heard I believe yourself in some of the DMR crew say the price won't come back to a certain price point

[00:14:56]
High or low as it would allow the longs or sorts to get out of the long trade or the losing trade

[00:15:02]
Also at different times the price will come back to the high low and we advise the traders are trapped

[00:15:07]
Or induced into entering your position and the stops are pending orders are activated. Yes, I

[00:15:12]
Think that is a lu owns the rights to that and I think it says the incoming back, baby

[00:15:17]
And what he's talking about is when the dealer goes up let me get my pen

[00:15:24]
Those you scorn at home

[00:15:27]
All right when the dealer goes up and makes the first leg of the M formation and pulls back

[00:15:33]
When he comes back in here

[00:15:36]
Right here's the high of the day and there's a same thing inverted applies for the low

[00:15:40]
If you want to see the low of the day hold it in the mirror later when I'm not around

[00:15:44]
All right, look that's the high of the day

[00:15:49]
When the dealer forms the high of the day when he extends the range coming out of the blue box

[00:15:55]
When he gets back near the high one or two things can occur

[00:16:01]
He will break that high and come back below it

[00:16:06]
If this isn't this is in fact the high holding right

[00:16:10]
He will break the high and come back below it as this type of move like this and end on a pin and

[00:16:16]
Then he will correct looks like he's almost flipping you off or he will make the M formation

[00:16:24]
Come near it and fail failure swing to take it out

[00:16:30]
Okay when he does this action when you get to this point

[00:16:35]
He

[00:16:37]
Ain't coming back baby

[00:16:39]
He's made his move. He's not coming back to this price point. He already has activated the orders

[00:16:48]
Hit the stops maybe above here or hit the stops in here for people that went short or long whatever the case may be

[00:16:58]
Okay

[00:17:01]
That's what I'm talking about when I say the price ain't coming back or he ain't coming back

[00:17:05]
Okay

[00:17:07]
Okay

[00:17:14]
All right next one

[00:17:16]
Okay, so those are the quick emails. There's a lot of similar questions, but

[00:17:22]
Those are the ones that stuck out of my mind that need to be addressed in focus on what we're doing right now

[00:17:27]
Okay, R&D review

[00:17:29]
All right, I'm gonna go over the homework for the last couple weeks of where you should be

[00:17:32]
You

[00:17:34]
Should I ask you for four-hour chart markups you should have them done posted in the former in your own personal possession?

[00:17:41]
You should have flashcards

[00:17:43]
Some amount a minimum of five and five at least

[00:17:47]
maybe more

[00:17:49]
Going forward from here do not mail me the homework post it in the forum hold it for review in here on Sunday

[00:17:57]
Can pile your work in a binder for your personal improvement?

[00:18:04]
We are not in grade school. I don't need to see your homework and bring it home and hang it on my fridge with a magnet

[00:18:11]
We're grown in here

[00:18:15]
But I need some accountability that you're doing it otherwise. I'm spinning my wheels in here

[00:18:20]
You should have a book of flashcards coming together like I showed you that I have

[00:18:25]
You should have a book of charts marked up coming together

[00:18:31]
These are the things in your idle time you should be referring to and looking at

[00:18:38]
Reminds me of a story about Zen and his wife I

[00:18:42]
Could tell you that the journey for everyone is about the same I

[00:18:48]
Think Jim Nicholson touched on a little bit where

[00:18:50]
You meet me you get excited you see the pattern after the fact and you're jacked up and you're like wow this guy's crazy

[00:18:57]
I believe him no

[00:18:59]
Then you go home

[00:19:01]
You do a little bit of work and maybe you have a run of success in the trading

[00:19:05]
Maybe something creeps back into your mind some negativity something happens you get distracted you get carried away with the levels

[00:19:13]
Something get creeps up in your head and gets you off track. I

[00:19:15]
Don't know how to get you back from there, but I can tell you

[00:19:26]
Right now

[00:19:28]
Today right this minute. I want you to clear the board. I want you to make plans to visit with Ken

[00:19:35]
And I want you to wipe the slate clean. I want you to take the shit off of your chart

[00:19:40]
I want you to get rid of the rainbow stochastics the MACD diamonds the garbage

[00:19:44]
I want it off of there and I want you to commit to the first three things on my list

[00:19:52]
The pattern the pattern the pattern

[00:19:56]
I'm gonna offer you up a simple trade set up today

[00:20:01]
You guys asked me what was the trade that I took last week I didn't post it on purpose because I'm gonna talk about it today

[00:20:08]
And I'm gonna show you how to identify a simple set

[00:20:14]
That will hopefully take you to the next level and it's gonna tie in with the work we've been doing here for the last two weeks, okay?

[00:20:22]
All right, so look back to what I was saying

[00:20:26]
Put a binder together have your flashcards keep the stuff handy if you're not trading Sunday Monday review it do some more markups

[00:20:34]
I want to remind you

[00:20:38]
That my mentor would not do the next lesson until he was

[00:20:43]
Handed by me my homework. I

[00:20:47]
Can't do that. There's too many of us here

[00:20:50]
So I'm trying to be I can't make you guys accountable and be disciplined in a mass setting

[00:20:54]
This is the best I can do post it in the forum

[00:20:59]
But here's the deal

[00:21:01]
When you don't turn in your homework to me or when you don't do the homework, you're not hurting me

[00:21:06]
You're hurting yourself. I

[00:21:08]
Want you to commit to me right now, okay? I'm asking you again for the third time for the third week in a row

[00:21:15]
Put away the bullshit get the crap off your chart and say this is it

[00:21:20]
The third the first quarter of the year is over. There's three more quarters

[00:21:25]
Today's April 1st the quarter's over you have three more quarters. Let's do it

[00:21:29]
All right, let's make up your mind right now going into the summer. I'm gonna turn it around. Let's do it

[00:21:34]
Let's get turned around right now

[00:21:37]
You pumped up come on do it

[00:21:40]
All right

[00:21:43]
How many of you watch the cycle unfold like I drew it for you anybody this was Australian last week

[00:21:51]
It was absolutely a work of art

[00:21:56]
Hey if you don't either can't see it here you go

[00:21:59]
Head and shoulders right there flipping the dealer off upside down

[00:22:06]
Okay, the next day

[00:22:09]
The dealer comes back issues a triple bottom in the shadow brinksy, baby

[00:22:16]
Okay, the next day the dealer comes back hits it again

[00:22:21]
Goes up guess what happened the dealer has all the retail traders thinking long

[00:22:27]
And what does he do he runs it up pulls it back runs it up pulls it back

[00:22:33]
One more time. What does the dealer do?

[00:22:36]
It's the stops and then the bottom falls out and the same pattern

[00:22:42]
develops going the other way

[00:22:46]
Right

[00:22:48]
Poetry baby. Yes, the subio it is poetry and if there was a textbook damn it this would be on the cover

[00:22:56]
All right

[00:22:58]
Here's my wrap rendition. This is it for the week. This is all the wrapping you're gonna get welcome to the candy shop

[00:23:04]
Don't trade until they hit the stops. Whoa. All right. That's all I got man. Look

[00:23:08]
Some of you took this right here and it is a valid M. Absolutely

[00:23:16]
But here's what happened

[00:23:18]
The dealer has to come out in the London session and hit the stops

[00:23:23]
Don't take the trade

[00:23:26]
Until they hit the stops

[00:23:28]
The reason the red box didn't work out is because the timing baby

[00:23:34]
number four

[00:23:36]
The pattern the pattern the pattern timing the levels. That's it

[00:23:42]
If you if you were in here and the dealer got your stops and you didn't bounce back on him shame on you

[00:23:50]
He gave it right back

[00:23:52]
Notice the blue tracer in play

[00:23:55]
He broke above yesterday's high

[00:23:58]
By the way, this is this is beautiful. This is this would be a multi-session. Not really. This is just a 22

[00:24:04]
Because it comes into the US session in the red box. It's a 22

[00:24:09]
Second leg of a second leg, but he gets why he comes back and he has different plans for you. Why?

[00:24:16]
US session trap move

[00:24:19]
Asian session the the W is invalidated by the way. This is not a valid entry. Why?

[00:24:26]
Because the dealer has been rising and he's holding the level you expect him to hit the stops and drop

[00:24:35]
Okay, beautiful

[00:24:37]
all right

[00:24:39]
Just remember our time you get ready take a trade and if you're in the session somewhere

[00:24:44]
You better welcome yourself to the candy shop and don't trade till the dealer hits the stops

[00:24:48]
And if you don't sing down your head before every trade shame on you because it's a fact of the business

[00:24:54]
The dealer must hit the stops

[00:24:58]
To take you out. That's the job. That's what he gets paid to do

[00:25:01]
So now before you take a trade I want you to sing this in your head

[00:25:09]
Did the dealer hit the stops before I pull the trigger?

[00:25:12]
You got railroad tracks above a consolidation zone or a cumulation cycle the answer is yes

[00:25:19]
Okay

[00:25:21]
Welcome to the candy shop, baby. If the dealer hits the stops, you've got them you own them. There it is

[00:25:27]
Okay

[00:25:30]
Alright next slide

[00:25:36]
Okay, I asked you

[00:25:39]
Last week is one the assignments to start highlighting the first eight hours of the business the open Sunday tonight

[00:25:49]
Mark the high low and extend those lines out through the course of the week

[00:25:53]
Okay

[00:25:55]
Now if you look at the week and a half from Australian that was just going on right now

[00:26:03]
Here's what you got

[00:26:06]
Is was purple a good pen color? What do you guys want black?

[00:26:11]
Why it what's better?

[00:26:14]
Okay

[00:26:22]
Okay, black black it is okay

[00:26:28]
Okay, here we go look this pattern right here is the head and shoulders that formed

[00:26:36]
Okay

[00:26:39]
Here's your first eight hours there they are marked in white right here's your lines right here and right here

[00:26:45]
Notice how this pattern carries into the second part of the week, but look hit the stops open high hit the stops low

[00:26:52]
That was the W first part of the week

[00:26:57]
Run up right that's the consolidation

[00:27:00]
Going into the middle of the week and there's your stop hunt high drop on the four-hour chart

[00:27:09]
Okay two weeks together. This is the bigger picture now understand that

[00:27:16]
Although these two weeks are tied together the dealer also

[00:27:24]
Took the week individually and broke it down. So if you miss this you still had this to work with

[00:27:32]
Pinch of the manneys on a four-hour chart solid gold

[00:27:35]
Okay confirmed on the four-hour punches through the average and collapses inside

[00:27:44]
Taking out the rest of the rest of the traders understand

[00:27:50]
Ends the week back in consolidation

[00:27:54]
Okay

[00:27:58]
So what I'm asking you to do big picture now is look at

[00:28:06]
the

[00:28:08]
Chart for the week using the Asian accumulation phase as the psychological support and resistance levels are

[00:28:16]
established

[00:28:19]
In the first eight hours of the week

[00:28:23]
The dealer then shows a move to get traders to commit

[00:28:27]
Okay, he broke short first part of the week. He got some level of traders taking shorts

[00:28:36]
He then went long and he got some level of traders to go long and short right he then hit the stops hit the stops drop

[00:28:45]
Gosh, I've said that once or twice since we've been together

[00:28:48]
That's the job

[00:28:51]
Don't trade till he hits the stops. Whoo. All right. I'll do that for you

[00:28:57]
Obviously, you know why I'm a trader because I am absolutely not our aper or a singer

[00:29:03]
Okay

[00:29:08]
All right next one

[00:29:11]
Okay, can you guys hear me someone said they lost sound see the only one okay cool all right take this chance to get a sip of guess what?

[00:29:18]
Diet Coke

[00:29:22]
All right here you go again look

[00:29:24]
a couple weeks back

[00:29:29]
First eight hours dealer cuts the psychological support and resistance levels and creates get some activity gets people to take a position

[00:29:39]
Forms the peak formation low for the week trades off of it Friday ends the week back in consolidation

[00:29:44]
He goes back. This is the two weeks together, right? This is the beginning of the week the dealer fails to extend

[00:29:51]
This would be the new psychological levels, right the dealer fails to extend above the previous set

[00:30:01]
Why because

[00:30:04]
Traders are trapped in this band up here so the dealer makes the move back towards it and gets the next batch of traders in this week's

[00:30:13]
level

[00:30:16]
Okay

[00:30:19]
Next

[00:30:25]
Okay, same thing first eight hours of the week look what the dealer does

[00:30:32]
He sets the high and low support and resistance cuts it

[00:30:37]
Pulls back and fails to break it fails to break it

[00:30:42]
Okay, if the dealer fails to break the Asian high at the beginning of the week

[00:30:49]
With the mid week right this is middle of the week. Here's the middle of the week Wednesday midnight

[00:30:57]
If the dealer goes back towards

[00:31:01]
The Asian high psychological resistance and hits it but slightly works it a little bit right there and right there

[00:31:09]
It's over shifts the zone away got him

[00:31:13]
On a 15-minute chart this will look like this and you got an entry in there promise

[00:31:19]
Okay

[00:31:21]
All right, this is the stuff you should be doing on your charts if you're not no worries. We're still together. We're still hanging

[00:31:28]
It's not too late to get back in there and remark these and try to see what I'm talking about

[00:31:34]
Okay, listen

[00:31:37]
It's not a race. I'm not going anywhere

[00:31:42]
I'm here for you guys every single one of you some of you met me a while back and I told the starfish story

[00:31:48]
I think it was in the summer. I'm gonna say it again real quick and I don't know it's gay. Some of you don't like it

[00:31:54]
But anyway, here's the deal

[00:31:56]
I'll stay at the beach with my wife and stay every year

[00:32:00]
June and July and August

[00:32:02]
This year is no different

[00:32:04]
Last year there was a big storm for four days. We were locked up in the condo. It couldn't get out

[00:32:08]
We had this we had the battle shields down storm shutters. You know talking about you put them down and

[00:32:14]
Then they lock it up and they they rattle the whole night and the winds blowing almost like a tornado

[00:32:19]
I guess we should have left but whatever so anyway, we're out there, right and

[00:32:24]
On the end of the fourth day I went down the sun was coming up. I had been up all night and

[00:32:28]
And not up all night. That was my regular waking hours. I was just up

[00:32:32]
I went down before while the sun was coming before I went to bed and

[00:32:36]
I

[00:32:37]
Guess from the storm. I don't know what happened

[00:32:41]
There was I don't know if there was one there was a thousand starfish laying on the beach

[00:32:47]
And Heidi was getting chased dressed and she was coming down

[00:32:50]
I was down and I started picking up starfish and chucking them back in one at a time one at a time one at a time

[00:32:54]
I was grabbing them

[00:32:56]
She said what are you doing? You're wasting your time. You're gonna be here all day. You will never get all these starfish back in

[00:33:02]
And I picked up the last one and chucked it in her. I told her to this one it matters

[00:33:09]
Okay, so what I'm telling you is you're my starfish man to everyone you in here it matters to me

[00:33:16]
Can't have you bad mouth to me all over the internet when it's not true

[00:33:21]
It matters to me that you understand and represent my family

[00:33:26]
And take money out of those bastards pockets it matters to me. That's why I'm committed to doing this

[00:33:33]
And that's why I'm here

[00:33:39]
Okay, so what I'm telling you right now is you if the first quarter of the years down is 2012

[00:33:47]
Okay, you're down seven nothing to the dealers big deal you still got three quarters left to play

[00:33:53]
Roll up your sleeves and do some freaking homework

[00:33:59]
Okay, it's not too late to put your book together. It's not too late to make your flashcards. It's not too late to mark up a chart

[00:34:07]
I'm here. I ain't going anywhere

[00:34:12]
Okay flashcards if you haven't done your flashcards

[00:34:18]
You should have something that looks like this if you've done them and they don't look like this guess why you got to redo

[00:34:25]
all right

[00:34:30]
This is exactly this is I want you to notice something this is dated September see it

[00:34:36]
The bottom right here, but this is the same play that they just made in Australian

[00:34:42]
That's why I'm telling you's the same shit over and over and over again

[00:34:46]
W is false didn't they make a W in Australia right before they hit the high one more time they vectored to the top

[00:34:53]
Hit the stops one more time and then drop

[00:34:58]
Okay

[00:35:02]
W is false dealer vectors to the stop on zone they just touch it nicely coming right out of the blue box

[00:35:07]
M formation shark fin above the band

[00:35:13]
See it

[00:35:16]
Price action above the blue tracer. There's that dang blasted blue tracer right notice how they went into consolidation

[00:35:24]
Right next to the high that's exactly what they just did in Australian last week

[00:35:28]
They went into consolidation near the previous day is high out here

[00:35:32]
The dealer comes out welcome to the candy shop don't trade until they hit the stops gotcha

[00:35:40]
Multi-session M, how do I know it's multi-session because they're working the tracer from yesterday

[00:35:47]
Okay, these are the things that you got to pick up on from homework realizing how they interact around the blue tracer

[00:35:53]
Why does Steve have this stupid little blue line on the chart is blue his favorite color?

[00:35:59]
No, it's on there because it serves a purpose for the dealers

[00:36:06]
Okay, so what I'm telling you is that if you see the dealer make the move

[00:36:10]
Above the blue tracer into the stop on zone just outside the shadow box and he forms the M

[00:36:17]
You own them

[00:36:18]
Take them the other way against the retail traders pack his lunch

[00:36:24]
Okay, I can't say it enough look

[00:36:26]
So okay

[00:36:30]
All right, this is what your flashcards should look like

[00:36:34]
And like I said, it's not too late man roll up your sleeves and let's get it on

[00:36:41]
All right next

[00:36:48]
Okay, so you should have a nice collection of these by now if you don't it's not too late complete them this week

[00:36:56]
Don't let yourself fall too far behind because then what happens is mentally become overwhelmed and you're just like oh god

[00:37:02]
I'll never catch up. I'm just gonna blow it all off. That's what happens

[00:37:06]
I'm giving you I'm feeding you a little bit every week and if you keep up you're gonna be it's kind of like

[00:37:12]
What's that movie the karate kid? I think wax on wax off. That's exactly what it's like man come over wax on my cars

[00:37:19]
I give you a little bit every week

[00:37:21]
And then at the very end I'm gonna let you show me saying the floor wax on wax off

[00:37:26]
You guys don't know I'm giving my age away if you haven't seen that movie, but

[00:37:29]
All right, understand I'm feeding you a little bit every week try to keep up

[00:37:35]
Okay, all right a question that came up two or three times

[00:37:39]
before the break was

[00:37:41]
The two choices are about forming the higher low

[00:37:45]
Is that they can either break it and come right back below or

[00:37:51]
They can fail to take it out completely. I'm talking about forming the M formation, right?

[00:37:55]
Remember this two minutes ago ten minutes ago. Whatever. I don't know one who was this I just did free, right?

[00:38:04]
Okay, that's that's the question, okay, so

[00:38:07]
The question is

[00:38:09]
Where the answer is choice one they fail to take out the high of the day and it holds or two

[00:38:15]
They tap the high of the day and come right back below it

[00:38:19]
Just like the railroad tracks on Australia and they went above and came right back below

[00:38:24]
Now the question is well, what if they keep going that's not the high of the day then this is not the high

[00:38:31]
This is still forming leg one if they keep rising then you this is not the high of the day. This is

[00:38:37]
void

[00:38:38]
these two structures

[00:38:41]
these two structures and

[00:38:43]
The inverse of these two structures

[00:38:47]
Will appear at

[00:38:49]
The high or low of the day period

[00:38:54]
Okay, this like that

[00:38:59]
That's what I'm talking about

[00:39:01]
Okay

[00:39:03]
If the high of the day is formed leg one the dealer comes up fails to take it out

[00:39:09]
So the dealer comes up in forms leg one

[00:39:14]
Comes above leg two for 15 to 30 minutes and comes back below

[00:39:20]
He will correct he took out the high I know the high jump to here

[00:39:27]
But understand

[00:39:30]
What's going on here? He had the high set he had a certain number of traders trapped stops were accumulated in here

[00:39:36]
He made the quick swing to take him out and any corrected

[00:39:41]
Okay

[00:39:43]
Same thing inverted same thing inverted over here. All right, okay

[00:39:49]
Look at the chat box at the end. I'm ignoring it. I'm at right now. I have my hands on my ears

[00:39:53]
But I'm not gonna run it right now. I'll look at it again. All right, okay, so I

[00:39:59]
Knew you guys think I'm not well. I'm not either. I need camera visit again inside my coconut too

[00:40:05]
But for things far worse than trading all right, man

[00:40:11]
Going through the emails again here's some of the questions that are asking me

[00:40:14]
Most often question. What is it? What is the best trade signal?

[00:40:18]
What's my Steve? What's your favorite trade?

[00:40:21]
What's the easiest setup for me to identify and hopefully it'll be for you? What's my signature trade?

[00:40:30]
Okay, so I'm gonna share that with you today, but I'm gonna break it down to show you some chart examples

[00:40:36]
We'll go from there. Okay, so

[00:40:40]
The answer drumroll, please the best trade to take in any market condition any market condition is

[00:40:47]
The safety trade with a second leg element

[00:40:50]
Ha ha you didn't know that was a trade did you?

[00:40:54]
Write it down or mark the tape

[00:40:58]
726 and 27 seconds

[00:41:03]
Safety trade with a second leg element why?

[00:41:07]
Okay

[00:41:10]
The safety trade identifies the top or bottom of the market at that moment in time

[00:41:15]
When it sets up

[00:41:19]
You have identified the top or bottom at this particular part of the week

[00:41:24]
Part of the month or wherever you are in the cycle

[00:41:27]
The safety trade allows you to trade in line with peak formation higher low as a confirmed directional move

[00:41:36]
What do I mean sounds like a mouthful when I'm saying simply is at the anchor points already been established the higher

[00:41:42]
Low of the weakest in the long

[00:41:45]
The dealer will rise from that level

[00:41:47]
For at least two days

[00:41:49]
Offering offering you 50 pips like he's handing out candy at the candy shop get it. I tied it in for you

[00:41:57]
Okay

[00:41:58]
Write it down mark the tape important stuff now

[00:42:04]
Here's the deal right now

[00:42:08]
727 not the airplane the time I'm officially designated everyone in here

[00:42:14]
Your signature trade as of today

[00:42:18]
All right, I annoyed you I gotta hit you on the forehead Arnie right on top of the head buddy

[00:42:23]
You're all now safety trade traders

[00:42:27]
This doesn't have to be your only trade, but I insist that you add it to your set right now and start looking forward every day

[00:42:35]
Here's the beauty of it when you understand it and can see it

[00:42:41]
You should be comfortable enough with it that you can anticipate its arrival 12 to 24 hours out

[00:42:49]
Okay

[00:42:50]
So you can look at the chart and go you know what?

[00:42:52]
I'm not trading today, but damn it. I'll be ready to go tomorrow or I'll be ready to go at 3 o'clock in the morning

[00:42:58]
This looks like it's setting up

[00:43:01]
Okay, let's go over the rules for you're now anointed safety trade traders

[00:43:11]
The peak formation high peak formation low has formed

[00:43:15]
The four-hour chart or the one-hour chart whatever it is you're using to identify this part of the cycle

[00:43:23]
The how or the low

[00:43:26]
High of the week or low of the week

[00:43:31]
Remember this is your four-hour tie-in now, okay

[00:43:33]
You've been marking the four-hour charts looking at the first eight hour simulation phase

[00:43:38]
False move peak formation higher low

[00:43:41]
dealer run to the extend the higher low peak formation low, right? Let's say he forms the high

[00:43:49]
Okay, when I have to count both it's hard confusing right look first eight hours

[00:43:55]
Blah blah blah blah blah first eight hours of the week dealer makes his false move week beginning dealer rises above on the four-hour chart makes his lock

[00:44:06]
This is your H.O.W. High of the week and this is also

[00:44:12]
Right, this is your how

[00:44:15]
This is also your peak formation high and your intraday high. It's gonna be an HOD

[00:44:21]
And it's gonna be what else a stop hunt

[00:44:25]
Holy shit all three of those things in one move the hell's wrong with those dealers

[00:44:31]
It's called leverage leverage their time and money

[00:44:33]
The dealer will form the high of the week the high of the day and the stop hunt in one fell swoop

[00:44:42]
If it's swoop, but it's something

[00:44:45]
Okay

[00:44:47]
Now price will move away from this area which confirms the formation

[00:44:52]
So if the dealer comes off the level and goes back into consolidation, this is a lock

[00:45:00]
It's locked in right

[00:45:03]
He goes into consolidation, this is level one consolidation

[00:45:15]
The DNC voids the counter-trend trade right here

[00:45:27]
Okay, do not counter back towards the peak formation

[00:45:33]
All right

[00:45:38]
Another very important rule remember that this is level one consolidation a sucker trades the breakout back towards the peak

[00:45:46]
I

[00:45:47]
Didn't call you a name, but I'm telling you if you're trading the breakout back towards the peak

[00:45:52]
If the shoe fits right don't be a sucker

[00:45:58]
Okay, don't be a sucker don't trade back towards the peak

[00:46:03]
Coming out of the peak formation high you guys know this stuff. I'm just pointing it out. I will change my pen color. Sorry

[00:46:10]
Okay, so now

[00:46:13]
What's the setup?

[00:46:16]
The dealer makes a visible stop hunt

[00:46:21]
Preferably above or below the blue box look above or below the blue box are the best

[00:46:27]
crystal clear

[00:46:29]
Remember what I'm telling you coming out of level one consolidation off of the peak formation high or low the straightaway develops

[00:46:43]
The obvious ones are still valid if he doesn't come above or below the blue box

[00:46:47]
That makes a perfect w or m formation as a stop hunt remember you're smarter than a box

[00:46:52]
They're still valid setups

[00:46:55]
The dealer issues a second leg m or w this locks in the trade as

[00:47:02]
The right direction. I'll draw it for you in a second. Just hang loose

[00:47:05]
If the level is hit a third time just like he did in Australia this week or last week

[00:47:12]
God help the dealer you own him

[00:47:16]
Okay

[00:47:20]
All right

[00:47:22]
Let's look at it in theory. Let me draw for you in theory

[00:47:29]
And then I'll go ahead and show you some chart examples, okay, you get a pen. Here's what I'm talking about

[00:47:38]
First eight hours of the week, right?

[00:47:46]
Okay, here's what happens peak formation is formed the dealer pulls away

[00:47:52]
This is the how

[00:47:55]
The high of the week

[00:47:58]
It's also the hod the high of the day

[00:48:03]
In some session it could be the u.s. Session could be the Asian session could be the London

[00:48:09]
Okay

[00:48:10]
now

[00:48:12]
The dealer makes his run off of the number and goes back into consolidation to end the day

[00:48:19]
Okay

[00:48:23]
The next day comes out that's the tracer

[00:48:30]
Okay, this is also the formation comes as a stop hunt

[00:48:36]
So all three elements were tied together in one move by the dealer

[00:48:41]
Now

[00:48:43]
You have peak formation high in this example

[00:48:47]
Pfh

[00:48:50]
What do we expect the dealer to do straight drop right

[00:48:58]
Richard I hope to God you're kidding. All right straight drop, right?

[00:49:06]
If the dealer

[00:49:10]
Doesn't make a straight drop, but he issues you a trade where he goes back towards the peak

[00:49:16]
and

[00:49:17]
Issues you a second leg

[00:49:23]
Setup which is the intraday HOD

[00:49:34]
And you have your three vectors in here

[00:49:39]
Remember this this trade is depending on the pair 25

[00:49:46]
75 pits off of the blue tracer. I know my pepper chips awful

[00:49:54]
Okay

[00:49:56]
So what happens is

[00:49:59]
The dealer comes out uses the stop hunting motion to lock in the high of the week

[00:50:04]
You observe it on the four-hour chart perhaps you know, it's a lock the dealer pulls away

[00:50:10]
He goes into level one consolidation

[00:50:13]
We expect straight drop out of here

[00:50:19]
We do not counter

[00:50:21]
If he drops

[00:50:23]
because if he drops

[00:50:25]
He's gonna jam us

[00:50:27]
we expect him to

[00:50:29]
Straight drop or give us a visible stop hunt does he always give you a visible stop hunt? No, that's why it's called a straightaway

[00:50:37]
But guess what?

[00:50:39]
When he gives you a visible stop hunt, it's lights out you own it. You can't miss it. It's right there in front of you

[00:50:48]
Okay, one more time go the other way

[00:50:51]
All right, here we go

[00:50:53]
Start of the week first eight hours Asian session

[00:50:57]
Boom boom boom boom boom boom dealer does his usual deal. He does this

[00:51:02]
He locks in peak formation low

[00:51:04]
Okay

[00:51:06]
Peak formation low also coincides with stop hunt

[00:51:12]
Right and LoW low of the week false move week beginning all these things come together

[00:51:18]
Wow that oh was brutal. We make a new L

[00:51:22]
Okay, low of the week now the dealer aggressively rises off this level comes back in the consolidation end of day

[00:51:30]
We know that he has a bunch of traders trapped in here from this behavior

[00:51:36]
Okay most of the time the dealer will straight rise

[00:51:42]
But what he will do from time to time as a gift from God is he will drop down and make a

[00:51:50]
perfect stop hunt formation

[00:51:55]
Okay, your job is to grab this trade right here

[00:51:59]
The set needs to be

[00:52:03]
20

[00:52:05]
To 75 25 to 75 is easy to remember

[00:52:09]
20 to 75 pits off of the blue tracer. Can it be more? Yes

[00:52:16]
But this is a better range why to go back to the email 20 slides ago because he ain't coming back, baby

[00:52:25]
You understand

[00:52:28]
This is the fury

[00:52:30]
This is how it's supposed to lay out dealer locks in peak formation low visible on any chart

[00:52:35]
But for our exercise purposes, let's say you lock it in on the four hour. You see it

[00:52:40]
Dealer makes the peak formation low midweek reversal. This is Sunday

[00:52:45]
Monday Tuesday

[00:52:50]
Richard I can't stop the class and explain what a stop on his dude. You need to email me

[00:52:54]
I'm shocked that you don't know so I'll spend some time with you privately send me an email right now generate an email

[00:53:02]
Okay now I

[00:53:06]
Don't know Richard stress me. I got to get a Diet Coke here

[00:53:11]
Thank you Russ, okay, so now in the theory

[00:53:16]
All right peak formation low visible on the four hour or one hour chart dealer makes a rise of

[00:53:23]
approximately 80 are off the number

[00:53:25]
Dealer rises a dr

[00:53:27]
Why because we know that in the three-day cycle. It's three times a dr, right?

[00:53:33]
So if the dealer should make one times a dr in the first leg of the cycle

[00:53:38]
Okay, tiny d a dr. I can't draw a man. Sorry. Okay, so now he comes back. He's gonna make his pullback off of the high

[00:53:45]
This is the HOD right here right the HOD Mike coincide with the agent session low

[00:53:51]
Right all these things tie together see okay now

[00:53:55]
He bounces off of here goes back in makes the stop hunt coming out of the blue box crystal clear invisible

[00:54:02]
25 to 50 pips the dealer falls into the shadow box on the Brinks issues a second leg you got them. It's over you own them

[00:54:10]
That trade will produce

[00:54:13]
This is the absolute same structure on the 15 I'm showing you how to identify

[00:54:20]
Okay, think for a minute Alex

[00:54:23]
The work that we've been doing is on the four hour chart. We've been identifying

[00:54:27]
The psychological support and resistance level on the four hour chart

[00:54:36]
When you notice that the dealer makes the peak formation high or low and pulls off of it

[00:54:42]
I'm giving you a trade

[00:54:46]
That absolutely pays out

[00:54:50]
Okay, so now how many pairs are there that you look at ten pairs

[00:54:56]
Maybe you look at the major six and a couple of crosses four more maybe you look at eight pairs

[00:55:04]
If the dealer makes a weekly high and a weekly low

[00:55:13]
I

[00:55:16]
Understand

[00:55:18]
That there will be two trades per pair per week

[00:55:24]
If you're scalping if you're stalking ten pairs not scalping take that off

[00:55:30]
He raised the tape

[00:55:31]
Kane and he raised that word if you're stalking stalking ten pairs and

[00:55:37]
There's two weekly reversals. That's 20 trades a week that are available to you for trade

[00:55:44]
Out of those 20 trades you may not get the second leg visible. You might get a V-bottom

[00:55:51]
You might get a cow on the lawn

[00:55:54]
Not on the lawn on the lawn

[00:55:57]
You might get a cow on the hot

[00:56:00]
But understand that if the dealer makes the trap move

[00:56:06]
In line with the peak

[00:56:09]
You own them and if you own them you're gonna start making some money with this trade. Do you understand?

[00:56:14]
I'll look at the questions in a minute. I just want to go over everything

[00:56:18]
Let's look at some charts when you see it visually it might start to clear up. Let me say this

[00:56:23]
Every single thing that we talk about is on the 15 minute chart

[00:56:29]
I'm trying to show you how to tie big picture into your 15 minute window

[00:56:34]
Okay, so we're taking big picture. I'm showing you a structure that the dealer builds deliberately to trap the traders

[00:56:43]
How do you exploit the structure? This is how you exploit the structure

[00:56:48]
Okay, you understand so let's get to exploiting

[00:56:54]
All right, so now let me close this and let's look at some chart pictures

[00:56:57]
All right, I know some of you still confused. I'm gonna go back. I see the I see the question marks and the the problems. Okay, look

[00:57:07]
Here you go

[00:57:09]
I need my pen

[00:57:13]
This is a 15 minute chart

[00:57:16]
Okay, what color purple I don't have white on here for some reason

[00:57:21]
Let's just let's use purple someone said they hated black it was against their religion. Okay

[00:57:27]
purple

[00:57:29]
Purple it is

[00:57:31]
All right, here we go

[00:57:33]
Okay

[00:57:35]
dealer comes out

[00:57:38]
extends the low peak formation low for the week

[00:57:42]
Okay, the formation low I

[00:57:46]
Know I'm a terrible artist. Sorry the dealer rises confused. They're by with this choppy crapping here

[00:57:51]
But we all know he's working the crosses. It's garbage

[00:57:54]
He ends the day high comes back into consolidation

[00:57:57]
Okay, do not counter trade this it's crap

[00:58:02]
DNC do not counter

[00:58:06]
You know better. What do you expect?

[00:58:09]
You expect peak formation low. This is what I expect

[00:58:12]
Guess what he offers it to you crystal clear boom boom boom boom take the trade you got a plus 50 all day

[00:58:20]
Okay, do you understand this is a safety trade it is?

[00:58:28]
75 pips in this example

[00:58:30]
This box is 50 75 pips off of the blue tracer the dealer comes out of the Asian session

[00:58:38]
Vectors and three moves to the low

[00:58:42]
Man, I just can't please you guys with this pen color thing

[00:58:45]
All right, I listen. I think why it would be best. How about yellow?

[00:58:50]
You guys are killing me. All right. Look peak formation is that better now that looks bad, too, right?

[00:58:56]
Let me see choose a pen color custom color custom ah I have to customize and make white something happen hot pink, okay?

[00:59:04]
Let's see

[00:59:07]
All right surely this is visible now

[00:59:11]
All right, here we go

[00:59:13]
I'm trying I'm trying guys. All right

[00:59:16]
How do we know that this is level three anybody?

[00:59:20]
Head and shoulders is present

[00:59:22]
Chop dealer makes the chop at level three head and shoulders. Okay, the dealer hits it amputate the shoulder over here

[00:59:28]
We don't care about this crap. It's in the past dealer makes the perfect W formation at the peak formation low of the week and rises by the way

[00:59:36]
This is Monday

[00:59:38]
Tuesday

[00:59:40]
The dealer makes a midweek reversal it would a head and shoulders pattern never saw that coming

[00:59:45]
Okay, we know he's been dropping because the EMA's are open wide open

[00:59:50]
Okay peak formation dealer rises off the W goes in the can chop confusing everybody works the crosses breaks out for the US

[00:59:58]
ends the day

[00:59:59]
high

[01:00:00]
minus the low divided by two about mid-range the

[01:00:05]
dealer comes back and makes a visible stop hunt

[01:00:09]
one

[01:00:10]
Two three hits to the low. I know he just misses the stop hunt box. Don't let that upset you. You good

[01:00:18]
Okay

[01:00:20]
75 pips off of the blue tracer

[01:00:23]
This trades a lock grab it in here plus 50. Got him

[01:00:28]
This is the kind of trade

[01:00:32]
That you back up the bring trucks on okay, it's gonna pay

[01:00:35]
Safety trade this is why it's safe because you know the direction

[01:00:41]
You have a one-day lock on the directional bias

[01:00:43]
You know the the lock is good for three days if the dealer comes out and does this and extends the low and doesn't make a second leg

[01:00:52]
He might come back to the low or he might come back and break this. That's why you don't counter

[01:00:58]
You're looking for this. You don't know what he's gonna do here if he

[01:01:02]
If you counter this and he straight rises he screwed you up, man

[01:01:08]
You only take

[01:01:10]
The W and M formations in line with the peak and that is it. That's the trade

[01:01:16]
Okay, let's look at another one

[01:01:20]
Okay, here it is again. This is an essence of

[01:01:24]
V-bottom, but I want to show you what happened averages are fanned out dealers been dropping boom boom boom

[01:01:29]
There's your kind of quasi head and shoulders

[01:01:32]
The dealer goes up makes the M ends the day back in consolidation now

[01:01:38]
He does not make a visible stop hunt

[01:01:42]
Why because he doesn't exploit the Asian range

[01:01:48]
He doesn't break the Asian range and those you that are struggling

[01:01:53]
Only take the ones where he breaks the Asian range

[01:01:56]
So you went from 20 trades down to five or six. Oh one trade a day. That'll kill me

[01:02:04]
You're gonna make plus 50 have no losers you could pile on the contracts as time goes on and you become successful

[01:02:10]
Okay, that's the point anyway, isn't it to leverage your time?

[01:02:16]
Okay, now

[01:02:19]
He did something for you. He offered you a gift in this chart anybody

[01:02:26]
Yeah, baby two pins in the mannees

[01:02:29]
Okay, look

[01:02:33]
The stop hunt is not below the Asian box

[01:02:37]
But if you know that you've got the peak formation lock with a head and shoulders to the low and this is this is locked in

[01:02:42]
He pulls away the pattern is confirmed

[01:02:45]
The dealer you expect to deal with a straight rise or you expect a dealer to make a visible stop hunt

[01:02:53]
He uses the 200 EMA of support

[01:02:58]
And you got him what I want you to learn is to stop

[01:03:04]
Counter trade trading this crap

[01:03:06]
And then accusing me of a failed system, okay?

[01:03:12]
This is the directional bias that's locked in from the h of

[01:03:16]
Lo w low of the week comes in around Tuesday instead of Wednesday

[01:03:20]
So now I saw the lock right? This is what I got

[01:03:23]
I come to my terminal in the afternoon because I wake up late around 3 o'clock in the afternoon and I look at the chart

[01:03:29]
Here's what I'm saying to myself

[01:03:31]
Okay

[01:03:33]
Let's do this. Let me see

[01:03:35]
I

[01:03:39]
Come to my terminal this day hasn't started yet, right? I'm here

[01:03:42]
I see the M formation and I know he's gonna end the day back in consolidation

[01:03:46]
I go out go to the cheesecake factory take my wife and go eat something go to the gym whatever right?

[01:03:53]
now I'm sitting here and it is

[01:03:57]
5 6 o'clock at night

[01:04:00]
Here's what I'm saying to myself the dealer made the LoW the low of the week

[01:04:08]
What do I expect I?

[01:04:11]
Expect him to one or two plays coming off the peak formation always straight rise or

[01:04:19]
a

[01:04:20]
visible stop hunt

[01:04:24]
That I can exploit in my favor

[01:04:26]
That's it that's all he's got what else can he do?

[01:04:31]
One or two things straight rise out of there and screw me up or

[01:04:37]
Make a clean visible stop hunt

[01:04:41]
In the shadow box and offer me a nice setup for the day

[01:04:46]
Okay, and he does just that and if you took this right here look

[01:04:50]
If you took this railroad track in the shadow box in line with the peak you got him look right there bam

[01:04:56]
Good entry right here a good entry right here. Neither one pins off the mannees into the London session

[01:05:03]
In line with the peak formation low

[01:05:10]
Okay

[01:05:11]
Tying your four-hour charts together you identified

[01:05:15]
Psychological support and resistance you saw a false move week beginning the dealer has made the peak formation low for the week

[01:05:22]
You saw the peak formation lock open up your four-hour chart you see man

[01:05:27]
There's a four-hour candle that happens to be all the way on the bottom the lowest point of the week

[01:05:31]
The dealer has now moved away from there for the last

[01:05:35]
15 hours 16 hours

[01:05:38]
Hmm

[01:05:39]
Pretty sure Steve told me that if the low is formed the dealer goes into consolidation

[01:05:45]
Tomorrow I can expect one of two things straight rise or

[01:05:49]
Visible stop hunt rise. I want the visible stop hunt. I want a clear concise move

[01:05:59]
Okay, Alex good question, and I don't have my time to say it one more time. How do we know that this is not the low?

[01:06:07]
All right, you ready welcome to the candy shop don't trade until they hit the stops. Whoo. All right, man. You got it

[01:06:15]
Don't trade until they freaking hit the stops. That's it end of story. Don't ask me again. Not you Alex anybody

[01:06:22]
Do not take a position until the dealer burns the stops

[01:06:27]
period

[01:06:29]
That's why you're getting burned because you're getting in on something that's not a

[01:06:34]
Stop hunt we trade the stop hunts in this business in this group

[01:06:38]
We wait for the dealer to show his hand by triggering the stops when he triggers the stops come to pop a baby

[01:06:47]
I got you

[01:06:49]
Any other setup without a stop hunt is a shit gamble

[01:06:55]
That made myself clear

[01:06:59]
Don't trade until he hits the stops

[01:07:02]
I'm a little fired up. I love this stuff man. I just want you guys to get it

[01:07:10]
Alex the answer to the rest of that question is time a day

[01:07:15]
You don't take stuff late in the US session

[01:07:18]
The recordings are up go look at them

[01:07:22]
Welcome to the candy shop don't trade until he hits the stops. Whoo. All right. I don't know how much worse I could sing than that for you guys

[01:07:29]
Okay, look

[01:07:32]
The dealer makes his rise goes into consolidation

[01:07:37]
He makes a visible W stop hunt

[01:07:41]
You take them you got it in line with the peak you own okay one more

[01:07:47]
Okay, look see this right here

[01:07:51]
You know why that exists

[01:07:54]
Especially if you came over to me from Craig Harris, you know why that exists that move exists

[01:08:02]
For the benefit of you breakout traders

[01:08:08]
Okay

[01:08:12]
Look at it again

[01:08:14]
Peak formation low shoulder W head shoulder

[01:08:22]
Oh, man, he hit it again right in my face

[01:08:24]
Okay

[01:08:30]
Okay, see it this is a no-go do not fall for that

[01:08:39]
Okay, that's the biggest problem a lot you're having you're taking any move out of the box and you're going with Steve

[01:08:45]
It went up some of those payouts some of those don't

[01:08:54]
Hellen you're right on baby

[01:08:59]
This is look obviously if he does this this is a better entry if he goes down to the stop hunt zone

[01:09:04]
But I want you to understand that these are valid aggressive sets the dealer has made

[01:09:09]
He widened the swing going into the session to knock everybody out. He stayed in the range

[01:09:14]
He worked the crosses. There's a whole slew of other things going on here

[01:09:18]
I

[01:09:21]
Did enter after the railroad tracks right there because that to me was a second leg

[01:09:25]
I had to take a little heat when he came back, but it wasn't that hot. I was good

[01:09:29]
Okay

[01:09:31]
There's a whole reason why the dealer chopped for the session and moved in the brink shadow in the US session

[01:09:37]
Dave I can't say it any better buddy trade away from the peak formation and you have one good set a week prepare

[01:09:43]
Maybe two right look if there's always a peak formation high that coincides with the stop hunt and the high of the week

[01:09:49]
Or low of the week in this example to high then you're in your trade is this boom every day every time that's your trade

[01:09:56]
Okay, the dealer makes the peak formation logos in the consolidation does this boom that's your trade

[01:10:01]
Okay, so if you make a high of the week and a low of the week, that's two trades per pair

[01:10:06]
per week if you only grab one prepare you got five or six trades available to you maybe more

[01:10:13]
How many do you want you greedy bastards?

[01:10:17]
I'm giving you trades that stack the odds extremely extremely high in your favor. Isn't that why you're in the business?

[01:10:28]
Understand I promise you it's a work of art when you start to realize it

[01:10:35]
Okay, one more one more to the downside

[01:10:39]
All right, look I wanted you to keep cognizant of this

[01:10:44]
Like that fancy word I looked at up right for started tonight. I want you to keep in your mind

[01:10:51]
One week flowing into the next although I got to get a sip of dico if you guys are drying me up over here

[01:11:01]
Okay

[01:11:04]
You have Friday trap move week ending right remember I was told today end the week on a trap they pull back going to consolidation

[01:11:12]
This happens to be Fridays peak formation high right?

[01:11:18]
It was also the end the high of the week they ended it and it was anybody want to take a stab at what level this is

[01:11:24]
Look at the separation on the average is okay now

[01:11:29]
Notice something pretty cool you bag the first eight hours of

[01:11:33]
The session of the beginning of the week. Sorry. I didn't include this over here. Okay

[01:11:38]
Listen the first eight hours of the week is the Asian session

[01:11:42]
psychological support and resistance are

[01:11:44]
established

[01:11:45]
Out to here right all the way out for the week now. Here's your peak formation high

[01:11:51]
peak

[01:11:53]
formation

[01:11:54]
Hi, I'm gonna have to I'm gonna have to take a class on how to draw with a mouse my goodness. Okay peak formation high

[01:12:01]
The dealer runs up. He cuts the psychological support and resistance. I'm sorry in this example

[01:12:07]
he

[01:12:08]
extends the psychological resistance level above break out traders go long the

[01:12:15]
dealer issues you a visible stop hunt

[01:12:19]
above the blue box and

[01:12:21]
This is yes can be considered a V bottom

[01:12:25]
But the dealer made the high pendant came back 45 minutes later hit it again failed to take it out remember your your choices are

[01:12:33]
The dealer fails to take out the high would a swing swing high or swing failure failure swing somebody failed. I don't know

[01:12:42]
and then

[01:12:45]
He takes out that high like this and then comes back below it

[01:12:50]
That's also valid setup dealer makes a visible setup you bagged them you got them boom

[01:12:57]
Okay, plus 50 to the four hour you're out

[01:13:03]
One of the questions is it's pertinent do we use TDI to confirm these yes, that's next week's lesson my friend

[01:13:11]
Okay

[01:13:16]
Everybody see that this is your set take a picture of this

[01:13:22]
Obviously, I'm gonna give you some homework on it. This is what you're looking for. This is the trade

[01:13:27]
This is your signature trade everybody in here is trading this now whether you realize it or not

[01:13:33]
That's your new job your job is to find these sets

[01:13:38]
Using the one hour four hour 15. I don't care what you want to use

[01:13:43]
Okay now I want to I want to tell you this

[01:13:47]
So people posted in the form and I'm not offended I understand is that I'm using multiple time frame analysis

[01:13:53]
That's what you want to call it. That's fine, but that's not what we're doing here

[01:13:56]
What we're doing is

[01:13:58]
We're identifying the peak formation high or high of the week and the peak formation low or

[01:14:05]
Low of the week

[01:14:06]
Which is the highest point on a chart within the week or the lowest point on the chart within the week?

[01:14:13]
We are simply waiting for the dealer to pull away from there and we are waiting for a visible stop hunt

[01:14:19]
From the dealer to confirm what we are seeing as a lock for the level

[01:14:25]
Okay, it sounds like a mouthful

[01:14:28]
Just take the safety trade man and be happy

[01:14:31]
All right, I promise you

[01:14:33]
Once you understand this and you start looking for this

[01:14:37]
You can anticipate it

[01:14:41]
Okay, if I see this right if I see this move right here, let me raise my little marks for you guys

[01:14:47]
If I see this and I happen to be sleeping or I wake up and see this and I go man

[01:14:52]
That's Friday's high. Okay. I could think about it all weekend Sunday Monday. All right. This was the peak formation high

[01:14:58]
What do I expect?

[01:15:00]
Okay, I

[01:15:01]
expect the dealer to make a stop hunt drop or straight drop if he makes the straight drop

[01:15:09]
I'm not countering him back to the high that suckers

[01:15:12]
Don't be a sucker

[01:15:13]
But I will take a move back towards the high short in line with the peak as long as the peak holds understand

[01:15:20]
And then if he goes back up here, that's a whole nother setup. That's a multi session

[01:15:25]
Okay, what I'm telling you is the safety trade is after the level is locked

[01:15:32]
After the level is locked the dealer makes a visible stop hunt

[01:15:36]
25 to 75 pips off of the previous higher previous low and he issues you a second leg lights out, baby

[01:15:45]
Okay, good good stuff. All right

[01:15:51]
Okay, now obviously to add to it we already said it

[01:15:59]
All right die-coking house, okay

[01:16:02]
Add a moving average or pivot point for strong confidence

[01:16:07]
The dealer can repeat the level I just

[01:16:10]
Illustrated this but it's got a hold he can make a stop hunt below and come right back above the level has to hold

[01:16:18]
Okay part of the rules

[01:16:20]
Look for the stop hunt to come in around 25 to 75 pips off of the L. O. W. R. H. O. W anchor point

[01:16:26]
So in essence what you have going on

[01:16:28]
Is your trading off of the anchor point some of you guys are saying I can't identify level three I could I can't identify this

[01:16:36]
I can't identify that I'm telling you how to identify

[01:16:39]
You take the trade

[01:16:42]
In line with the peak formation that was previously formed from yesterday

[01:16:46]
and that my friends as a walk

[01:16:49]
Okay, so you're taking V1 and a1 trades

[01:17:00]
Right remember the cycle anchor

[01:17:03]
V V M if you don't remember the cycle go look at Australian from last week in this week a work of art

[01:17:10]
V1

[01:17:12]
V2

[01:17:14]
Reversing

[01:17:16]
M R. Okay

[01:17:19]
Now

[01:17:21]
You got the lock right here

[01:17:23]
dealer comes back makes the V if he gives you a second leg very simple and easy to see

[01:17:31]
You got him

[01:17:34]
Okay, that's it and the exact opposite the other way M anchor point

[01:17:40]
a1 or carrot one. I don't know what that is inverted V2

[01:17:47]
WR reversal W as a reversal

[01:17:51]
Okay

[01:17:53]
Peak formation high dealer comes back if he gives you a second leg you own him. It gives you a second Em you own him

[01:18:03]
No

[01:18:05]
Al has a good question are V1 and a1 trades more reliable than then H you know I'm not saying they're more reliable

[01:18:12]
They're just absolutely easier to see the problem and a lot of people are having is that they're not understanding what level

[01:18:18]
They're in and they're counter trading back towards the peeps. So what I'm giving you is

[01:18:22]
I'm giving you the first two days of the cycle. I'm giving you anchor. Let me erase this. Hold on. Sorry

[01:18:29]
I'm giving you identify the anchor point. That's the only level you need to be concerned about right now is it anchored?

[01:18:37]
Yep, it's anchored. Well, what about intraday Steve? It went one two three and a half doesn't matter. I don't care

[01:18:43]
Okay dealer goes into consolidation

[01:18:45]
I'm telling you what he's gonna do next and what you expect him to do next

[01:18:50]
What I expect him to do next is this

[01:18:55]
Right this or this that's the only three plays from there

[01:19:04]
So now

[01:19:06]
Straightaway is tough to see and one of the problems that a lot of people are making and I've seen it is that

[01:19:11]
Remember the dealer makes a high from the u.s. Session off the peak, right?

[01:19:15]
This is the u.s. Hide and he pulls back and goes into

[01:19:19]
Consolidation and he breaks high as a straightaway movement and then you guys counter this back and go but Steve it was a multi session

[01:19:26]
Him and you trade back towards the peak, right? That's what's happening to a lot of you guys

[01:19:32]
I've seen it in emails. That's why I'm addressing it right now

[01:19:35]
So what I'm telling you is

[01:19:41]
That you're looking at two pieces of the cycle the most two important pieces

[01:19:45]
You're identifying understand that there's a tracer in here and separates the day. This is day one anchor day two

[01:19:52]
What I'm telling you is you become a day two trader with a visible stop hunt in line with the peak as a

[01:19:59]
safety set

[01:20:01]
And if that's the only trade you take

[01:20:05]
It's enough

[01:20:16]
Okay, good stuff

[01:20:25]
Here it is again, okay, this is what I wanted to show you there's actually

[01:20:30]
Two trades you could take in here. Here's your peak formation low from the u.s. Session, right? This is GJ by the way pound in

[01:20:42]
Okay, now what happens the dealer makes an M right here

[01:20:47]
But what did I tell you right here? Don't fall for that shit because he could continue to rise from here

[01:20:55]
Don't take this this is DNC baby

[01:20:59]
It's not the demilitarized zone. It's a do not counter. That's the DMZ, right?

[01:21:06]
All right, man, I can't draw it. It's DNC do not counter this back because the dealer can straight rise out of here

[01:21:13]
But what he does do in this example is he gives you a double bottom

[01:21:18]
multi-session W formation

[01:21:21]
In the shadow in the u.s. Session. That's a good trade. That's just as safe as the safety trade

[01:21:27]
Okay, that's just as clear as the safety trade now

[01:21:37]
Consolidations up here Steve I see an M and I see a W. Hell yeah, you see an M in a W. So do I

[01:21:44]
I'm not retarded or blind

[01:21:48]
How do I know to take the W and not the M?

[01:21:51]
Let me put it to bed for you once and for all so you know

[01:21:56]
the

[01:21:59]
Answer my friends is not blown in the wind. It's trading in line with the peak

[01:22:04]
The answer is you have a double bottom anchor

[01:22:10]
From Thursday and Friday Sunday and Monday the dealer makes a visible stop hunt

[01:22:18]
to the downside and

[01:22:23]
Rises

[01:22:25]
Okay, remember why this move exists this move exists for the I

[01:22:32]
Can't think of the name of that that breakout EA. I think it's our teamies

[01:22:38]
This move exists for the guys that bracket this information right here

[01:22:44]
Look what do people do they bracket and they trade the break high and the brake low and they keep swinging back and forth

[01:22:52]
What I'm telling you is that this maybe it can be conceived as a V-bottom. That's fine

[01:23:02]
Okay, the best possible confirmation for this trade is a second leg W. That's it

[01:23:13]
Okay

[01:23:16]
Understand that's the safety trade 25 to 50 25 to 75 pips off of the blue tracer

[01:23:26]
In line with the peak formation from the previous days

[01:23:32]
This is your trade

[01:23:36]
All right

[01:23:38]
One more this one's beautiful

[01:23:41]
Okay, this one's from the pound from not that long ago today's the 28th this might be last year though. I can't remember

[01:23:48]
Here you go comes in fakes in the US session past the four hour pulls back

[01:23:55]
Goes into consolidation

[01:23:57]
Steve I shorted the M and it didn't pay out that much. What's my problem?

[01:24:01]
Your problem is you missed this big monster W formation as an anchor right there, right?

[01:24:06]
But what does the dealer do he comes in he offers it up three times

[01:24:12]
Isn't that the same thing he just did in Australia and look at that

[01:24:23]
Okay Patricia I'll answer in a second you see it

[01:24:29]
Shark fin blood in the water

[01:24:31]
Just

[01:24:32]
Just outside the stop hunt zone and by the way, I thought it was kind of funny is

[01:24:39]
If you notice I dragged in the white lines from last week

[01:24:44]
Let me back up and clean this off. I forgot that I did that and I wanted to talk to you all about it. Okay, look

[01:24:50]
This is the age and range from last week. I

[01:24:54]
Popped it in here and look what he does the dealer pins to it

[01:24:57]
It doesn't break it and just so happens to have the four hour in there

[01:25:01]
Pretty crazy, right?

[01:25:07]
Okay

[01:25:09]
You could have got in here

[01:25:11]
Thinking it was a W formation, but guess what the dealer's generous. He doesn't come back too far to get you out

[01:25:16]
Okay, so you same thing like Australia. You got to take a little heat either one

[01:25:27]
Okay

[01:25:28]
Pins to the blueberry baby pins to the Mayo pins to the blueberry

[01:25:32]
Same stuff. This gives you a directional bias. So what you're looking at is

[01:25:38]
Peak formation higher low is formed the dealer pulls off aggressively

[01:25:43]
One times ADR perhaps the distance from here to here comes back into consolidation

[01:25:49]
Right blah blah blah the dealer makes a stop hunt in favor of the peak formation level in line with the peak formation level

[01:25:57]
Whatever you want to say and he rises like a nutcase

[01:26:03]
Straight through

[01:26:06]
Okay for novices, I want to see the dealer break the Asian low that is a true stop hunt a

[01:26:13]
True stop hunt is higher or lower than the blue box right here

[01:26:18]
Look at all that work man beautiful beautiful beautiful beautiful. You know it's coming. Okay. This is a do not counter situation

[01:26:25]
This will confuse you and what people are doing is taking this and it doesn't offer up many pips

[01:26:32]
And then you get mad at me

[01:26:37]
Okay

[01:26:39]
Sunday is not day one when the peak formation is formed. This is day one

[01:26:45]
Peak formation day two

[01:26:48]
day three

[01:26:50]
Looking for the reversal maybe one more day rise

[01:26:53]
Okay, you got rise from here to here

[01:26:57]
You got rise from

[01:26:59]
here

[01:27:00]
To the end of the day and then the next night you start to see some rise but chop also

[01:27:05]
Okay

[01:27:07]
All right, let me see

[01:27:10]
This is exactly

[01:27:15]
Look moving averages across over prices dropping dropping dropping dropping

[01:27:20]
Dealer makes the peak comes out the next night hits it three times

[01:27:26]
Okay, I took it on the second one just like you figured

[01:27:30]
guess what

[01:27:31]
He's my bitch

[01:27:36]
All right, and if I fended anybody with that comment, I'm sorry

[01:27:40]
Understand peak formation. It's a lock. I know which way it's going. I can anticipate this trade from the afternoon

[01:27:47]
All the way into the middle of the night

[01:27:49]
I know what he's gonna do. I don't fall for this crap because it's against the directional bias

[01:27:57]
Okay

[01:27:59]
All right now

[01:28:01]
Let's look at the lessons learned thus far. I don't know what happens, but

[01:28:06]
say 15 and I'm a little ahead of myself when I like

[01:28:11]
To understand what goes on in the process for my week. Okay. I wrote the lesson

[01:28:19]
I give it to my wife. She converts it to slides. I

[01:28:22]
Get all my chart pictures marked up and inserted into the slideshow then I do a dry run or like a

[01:28:28]
It's kind of weird. It's not a rehearsal, but I have to know how long it takes and

[01:28:33]
For some reason when I do it like without an audience without you guys it goes slower

[01:28:37]
I guess because I'm calmer, but then when I do it

[01:28:42]
For live for real it goes faster. I don't know if I'm jacked up on too much Diet Coke adrenaline excited

[01:28:48]
I don't know, but it's weird is like I do get nervous every time I pick up the mic man

[01:28:53]
I don't know why I've been doing it for a while you think I'd be more calm

[01:28:57]
But I tell my wife this all the time is I would be nervous if I didn't get nervous

[01:29:02]
Like if I was too relaxed or too cool. I would think maybe it's gonna be a bad session makes me nervous

[01:29:07]
But I still get like I don't know if it's butterflies or knots or bad case of diarrhea

[01:29:12]
I don't know what it is. I'm kidding, but my stomach gets rumbly right before the I have to go on for you guys

[01:29:17]
It's crazy anyway

[01:29:19]
All right, man. So look this is where we are. I'm a little ahead of schedule

[01:29:22]
I'll take some questions to round out the last few minutes. Here's the deal

[01:29:26]
so far

[01:29:30]
Since we started bootcamp, this is where you should be at weekly cycles should be identified

[01:29:35]
You should be looking at the big picture

[01:29:39]
Okay

[01:29:41]
You should understand what the psychological support and resistance levels are that are set by the dealer within the

[01:29:47]
First eight hours of the week

[01:29:50]
Since these levels are man-made they're exploited by man not all men just the dealer men

[01:29:58]
All right, you should understand how to visualize your entries from flashcards

[01:30:05]
Some you said you're waiting for me to fix the work time ribbon. That's a good one. I'll take it. I am gonna fix it

[01:30:11]
In fact since I brought it up. Let me talk about it

[01:30:14]
Dick Schmidt sent me over a work time ribbon that was coded from Sander and Robert I

[01:30:21]
Got it like Wednesday Thursday. I have not had a chance to test it on all platforms because I was

[01:30:27]
Finishing up the slides for the week. I

[01:30:30]
Will since the markets open now, I will get it on there see the adjustments and what needs what it needs

[01:30:35]
And if that is a viable option, I will put it in the student folder and the student folder will be hung in the forum

[01:30:41]
And

[01:30:43]
You guys will be notified via email or some way to let you know it's in there, okay?

[01:30:47]
All right, so now

[01:30:50]
You should be able to put it all together now looking at the four-hour chart. You should be able to see the high of the week below of the week I

[01:30:57]
Talked about the first eight hours of the week and now tying it all together. You're adding the safety tray to your arsenal

[01:31:05]
This is where you should be taking your pulse again your temperature

[01:31:08]
I'm checking in on you guys. Let's see where you're at you should have a book coming together a pictures of

[01:31:14]
Flashcards and entries you should be able to mark up your four-hour chart by just looking at it

[01:31:20]
And now you've identified one particular set that is I want to say never fails, but

[01:31:26]
I'll probably go to prison for saying that what I'm telling you is very high high high high high probability

[01:31:34]
Trading in line with the peak formation anchor point

[01:31:37]
from the dealer

[01:31:40]
Okay

[01:31:43]
Understand you're adding the safety trade to your arsenal if you like this trade and don't want to take anything else

[01:31:49]
This trade will provide for your family

[01:31:52]
It's enough

[01:31:54]
Start monitoring multiple pairs for this setup

[01:32:01]
Okay, remember sunny

[01:32:07]
Identifies the peak formation and trades away from it for two days

[01:32:11]
Identifies the peak formation low and trades away from it for two days goes long for two days

[01:32:15]
Then finds another pair that's in that part of the cycle the beauty of this trade is that because the dealers

[01:32:24]
Work the majors and then the crosses at different times during the course of the week and different times of the cycle

[01:32:31]
You will get some setups on Monday. You will get some setups on Tuesday

[01:32:34]
You will get some setups on Thursday

[01:32:38]
You're gonna have don't hold me to those exact days, but I'm saying is that

[01:32:43]
You now have a trade in your arsenal

[01:32:49]
That you can anticipate 12 to 24 hours out by

[01:32:53]
Identifying the simple high or low for the week

[01:32:56]
Waiting for the consolidation and then the next day waiting for the stop hunt in line with the run

[01:33:00]
but the peak right

[01:33:03]
If the dealer moves the pound off of level one goes into consolidation gives you a trade now you look at GBPC

[01:33:09]
HF GBP odd GBC CAD GBP CAD rather

[01:33:14]
because what happens is

[01:33:16]
The dealer has to come back and handle the crosses

[01:33:18]
So if he works majors first part of the week then you could jump over to GJ EJ

[01:33:23]
AJ and look for the dealer to handle the end crosses or the other exotics

[01:33:29]
later in the week

[01:33:31]
So now if you increase your window

[01:33:34]
of

[01:33:35]
Possible trades from four pairs to ten pairs or to fifteen pairs

[01:33:39]
You're simply monitoring all these pairs on the four hour

[01:33:43]
Identifying the higher low point of the week

[01:33:47]
12 hours out you already know man. There's looks like the lowest point on the chart right now

[01:33:51]
Let me draw a line draw a line on the lowest point of the chart

[01:33:58]
Okay, do you understand

[01:34:01]
Okay

[01:34:06]
Okay, that's it we're coming there we're getting there around in the corner

[01:34:15]
Okay, let's look at let me look at some questions

[01:34:21]
Well actually let me give you out the homework assignment. I'm done a little bit early, but I'll take some questions all right here

[01:34:26]
We go so R&D for the week

[01:34:29]
I

[01:34:30]
Finish your flashcards. You should build your book every week by adding a few snapshots. It's not too late, okay

[01:34:36]
Mark up ten safety setups in any pair you like look for them five long five short if

[01:34:41]
It's too easy five and five and five so easy increase it

[01:34:45]
Okay

[01:34:51]
Post in the form for your review

[01:34:58]
I'm gonna try to organize the form for you guys. Okay. I mentioned that

[01:35:09]
Okay, let me look at some of these questions

[01:35:14]
Two trades a week each for 50 pips. Yep, that's right Dave the math. Okay, remind me which pairs look for low and HOW Tom

[01:35:21]
Okay, he's asking what pair should he monitor look at the majors and then add a couple of crosses EJ GJ

[01:35:28]
Okay

[01:35:30]
Okay, okay. What is the best session to trade London or US?

[01:35:35]
Which came first chicken of the egg?

[01:35:39]
All sessions are good if you get a good setup I personally like London because none of the numbers have been exploited yet

[01:35:51]
Okay, someone's glad I said a couple times that's never too late start to do the homework. It's never too late

[01:35:58]
Get caught up man. Don't fall too far behind. I know it's gonna happen four or five weeks

[01:36:02]
You're gonna go by and you're gonna feel overwhelmed and you're not gonna do anything

[01:36:06]
Because you're gonna feel like

[01:36:12]
You felt too far behind you don't want to do the work