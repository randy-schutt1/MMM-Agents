# V09 — TRANSCRIPT

## SOURCE

| Field | Value |
|---|---|
| Video ID | V09 |
| Original filename | `Bootcamp1 Wk2 032612 Part4 (53mins).swf` |
| SHA-256 | `b0f36b5540de7a76397c80202cf6a721a2a18aa9011c5698238c6bcc624168d4` — re-verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session, on the flat `Bootcamp/` canonical path. The `Bootcamp Notes/09_.../` duplicate hashes identically, as `D-017` §3 records |
| Duration | 00:52:26 (audio measured **3146.815 s**; SWF header **9,441 frames ÷ 3.0 fps = 3147.00 s**; `SOURCE_MANIFEST.md` 00:52:26 = 3146 s — three independent figures, agreeing) |
| Lesson title | **NONE PRINTED.** Unlike V07 and V08, this file opens with **no title slide** — the recording begins on the presenter already speaking (*"Welcome back everybody"*) over the closing ring diagram of the previous session. No title is asserted here. The quarantined per-lesson header calls the lesson *"Advanced Execution Review, Homework Chart Walkthroughs & Trade Filtering"*; see `QUARANTINE_REGISTER.md` **Q-010** for what that claim survives (nothing) |
| Session date | **2012-03-26**, from the filename `032612` and `SOURCE_MANIFEST.md`. **Not printed inside this recording.** Shared with V06, V07 and V08 |
| Transcribed by | ASR, by a pre-ingestion session. Copied and verified 2026-08-13 — see VERIFICATION below. The pre-ingestion file's own `# VIDEO` header block (*"Course Position: Video 10 of 21"*, *"Primary Topics: …"*) is **NOT carried over**: the position is wrong under `D-017` §2's renumbering and the topics line is unsourced. Only the verbatim body is copied |
| Transcription confidence | MEDIUM — see TRANSCRIPTION NOTES |

## COVERAGE

```text
STATUS: COMPLETE — no fenced tail, no gaps
Covered: 00:00:00 - 00:52:23
Entries: 721 markers, 718 distinct.
         Timestamps are MONOTONIC NON-DECREASING: zero decreasing transitions,
         and THREE same-second adjacent pairs -- [00:14:32], [00:16:51],
         [00:39:43]. They are therefore NOT "strictly increasing", and this
         block does not claim they are. (Stated as MEASURED, by scanning the
         body for lines fully matching ^\[\d\d:\d\d:\d\d\]$ -- V03's coverage
         block was charged at R1 for asserting strictness where it was false,
         and V08's was strict and said so. V09's is not, and says so.)
         Largest inter-entry gap 11 s, twice: at [00:07:03] and [00:44:56].
         Next largest 10 s, four times: [00:23:05], [00:45:41], [00:49:35],
         [00:49:47].
         Final entry [00:52:23] against measured audio 3146.815 s (00:52:26.8).
```

**The ~3.8 s tail is not a gap and not a fence.** A Whisper `small.en` pass over
`00:51:40`–end returns *"…that was the whole idea of this bird right here. He's got way"*
and nothing after it. The transcript's own final entry `[00:52:23]` reads *"I mean he's got
wings was using his legs at first"*. **Both engines stop at the same half-finished sentence.**

**The lesson ends mid-sentence, and that is a property of the source.** This is the second
consecutive file to do so — V08 ended mid-argument on an unanswered question about the
innermost ring of the presenter's own model. V09 ends mid-clause, on the same presenter's
closing metaphor about a bird learning to fly.

## VERIFICATION — FOUR INDEPENDENT AXES

This transcript arrived from a pre-ingestion session and is covered by `SETUP_ISSUES.md`
**I-008**. It was **not** trusted on arrival.

**1. The audio the transcript was made from is this lesson's audio.** The pre-ingestion folder
holds `audio_10.mp3`. The `_10` is not an error: folder numbering under `Bootcamp Notes/` was
changed by `D-017` §2 so that folder `NN` = video `VNN`, and under the *pre-renumbering*
alphabetical order this lesson sat at position 10. Tested rather than reasoned about:

| Check | Result |
|---|---|
| Duration of `audio_10.mp3` vs audio extracted from the SWF by this session | **3146.814694 s vs 3146.814694 s** — identical to the microsecond |
| SHA-256 of the two files | **differ** — `audio_10.mp3` is a 64 kbit/s re-encode, this session's is 40 kbit/s |
| Raw waveform Pearson `r`, four 20 s windows (`t = 300, 1200, 2100, 3000 s`) | **−0.008 / +0.042 / +0.059 / −0.015** — ≈ 0 |
| **Energy-envelope cross-correlation**, same four windows, ±2 s lag search | **r = 0.979 / 0.982 / 0.976 / 0.983**, all at lag **−0.02 s** |

The near-zero waveform correlation is the mp3 re-encode's ~20 ms coder delay, and V08's
transcript already established that **a null waveform correlation between two encodes of the
same audio is expected, not diagnostic.** V09 reproduces the V08 signature exactly — same
envelope range, same −0.02 s lag — on a different lesson, which is a useful confirmation that
the earlier reading was about the encoder and not about that one file.

**2. The transcript is an ASR of that audio, not a fabrication.** Six 45-second windows
(`t = 0, 600, 1200, 1800, 2400, 3100 s`) were re-transcribed independently with Whisper
`small.en` and compared word-for-word after case/punctuation normalisation:

| Window | Transcript words | Whisper words | Word-level similarity |
|---|---|---|---|
| 0 s | 127 | 128 | 0.965 |
| 600 s | 127 | 113 | 0.917 |
| 1200 s | 164 | 162 | 0.933 |
| 1800 s | 130 | 129 | 0.857 |
| 2400 s | 105 | 115 | 0.782 |
| 3100 s (to end) | — | 129 | tail check, quoted above |

**The disagreements are the evidence, and V09's are richer than V08's** because the second half
of the lesson is a live chart walkthrough full of pair abbreviations and single letters:

| Marker | This transcript | Whisper `small.en` | The actual word, from context |
|---|---|---|---|
| `[00:30:02]` | *"I am personally **staying** a reset"* | *"personally **seeing** a reset"* | **seeing** — Whisper is right |
| `[00:30:31]` | *"These are dynamic **candles**"* | *"dynamic **handles**"* | candles |
| `[00:40:28]` | *"might form an **end** and turn around"* | *"form an **m**"* | **M** — Whisper is right |
| `[00:40:36]` | *"take with a **green** salt"* | *"a **grain of** salt"* | **grain of** — Whisper is right |
| `[00:39:21]` | *"a really nice **amp complex emlement** one hour chart"* | — | *M, a complex M element* |
| `[00:10:44]` | *"I was just **miffed**"* | (window-edge truncation) | miffed |

> ### A SYSTEMATIC ASR DEFECT IN THIS TRANSCRIPT, NAMED HERE SO NO NOTE INHERITS IT
>
> The spoken letter **"M"** — the course's central pattern name — is rendered by this engine in
> **at least four different ways** across V09: `m` (correctly, e.g. `[00:30:40]` *"possible m
> forming"*), **`end`** (`[00:40:36]`), **`am`** (`[00:34:55]` *"if we see a nice am up here"*),
> and **`amp` / `amla` / `emlement`** (`[00:39:21]`, `[00:47:07]`). Whisper renders the same
> sounds as `m`. **Every quotation in `03_LESSON_NOTES/V09_*` that turns on an M or a W carries
> its marker so a reader can re-listen**, and no rule in this project is built on the token
> `end` occurring in this file.
>
> **A fabricated transcript does not invent "green salt" for "grain of salt", and it does not
> mishear one letter four different ways.**

**3. The rendered slides match the words, at the timecode the words carry.** Required by
`SWF_CAPTURE_RECIPE.md` GOTCHA 4 and performed **before** the long capture was trusted. A
10-second probe render at 10× speed produced a slide whose burned-in player timecode reads
`01:41 / 52:2x` and whose printed body reads *"Risk in FOREX is DEFINED as what % of our
account balance would be lost if our trade went to Stop Loss?"* and *"One of the great benefits
of trading with Defined Risk is that we are emotionally prepared if a Stop Loss happens. There
is no unknown drop in our account balance."* The transcript at `[00:01:17]`–`[00:01:21]` reads
*"Risk in forex is defined as what percent of your account balance would be lost if your trade
went to stop loss?"* and at `[00:01:31]`–`[00:01:45]` *"One of the great benefits of trading
with defined risk is that we are emotionally prepared if the stop loss happens… Because there
is no unknown drop in our account balance."* **Content, burned timecode and transcript marker
agree, and the slide is a near-verbatim source for the spoken line.**

**4. Timestamp structure.** Measured, not asserted — see COVERAGE above, including the three
same-second pairs that stop this transcript being strictly monotonic.

**What verification does NOT establish:** that every word is right. It establishes that this is
a real ASR of this file, complete to the file's own end, with its timestamps in order and its
markers landing on the right slides.

## ⚠ ONE SPEAKER, HE IS NOT THE COURSE AUTHOR, AND HE IS THE V08 PRESENTER — FIFTH CONSECUTIVE LESSON

**Speaker identification was performed BEFORE any note was written**, as `DECISIONS.md`
**D-033** provision 1 requires (re-adopting `D-025` consequence 3 verbatim), and as
`COURSE_PROGRESS.md`'s V08 GATE carry-forward item (a) instructs.

**V09 has no course-author segment at all.** This is the **fifth consecutive lesson** with zero
course-author runtime (V05, V06, V07, V08, V09). Under **D-033** — *"all knowledge is created
equal"* — that **demotes nothing**: every statement in this file is **NORMATIVE evidence at
equal weight** with the course author's.

| Evidence | Detail |
|---|---|
| Third-person references to Steve | **4**, all third-person, none self-referential: `[00:09:38]` *"I actually wrote this before **steve** said this the other night"*; `[00:14:05]` *"an incredible advantage using **Steve's** method"*; `[00:37:43]` *"our homework from last week that **steve** gave us"*; `[00:42:16]` *"**Steve** doesn't teach it… this is my my twist on it"* |
| Self-identification | `[00:27:30]`–`[00:27:37]` the presenter reads out his own contact address: *"**Jim Nicholson**… dmor at hotmail dot com… that's where I work with only dmor students"* |
| Handovers | **None.** One voice throughout, plus audience questions from `[00:41:25]` on (named participants: *Fred*, *Harvey*, *Susan*, *Card/Carl*) |

> ### THE V08 CARRY-FORWARD HYPOTHESIS WAS TESTED AND IT IS CONFIRMED
>
> `COURSE_PROGRESS.md`'s V09 GATE block set a specific, falsifiable test: *"V08 is the FRONT
> HALF of a talk its presenter says will run about two hours, and its section 3 — 'how to not
> GET killed', a defined-risk lesson — is announced twice and is NOT in the file. **If V09 opens
> with that section, V09 is the same presenter continuing. TEST IT, do not assume it, and do not
> use the acoustic screen across files.**"
>
> **V09 opens with that section.** Four independent strands, none of them acoustic:
>
> 1. **The first words are a resumption, not an opening.** `[00:00:00]` *"Welcome back
>    everybody. Hope your brains have rested… I wanted to make sure you guys are nice and
>    mentally refreshed for **this next section**."*
> 2. **It is the announced content.** `[00:00:51]` *"Reason was was that I wasn't trading with
>    **defined risk**."* The whole first 28 minutes is the defined-risk lesson.
> 3. **It resumes V08's own ring diagram, by name.** `[00:19:55]` *"that **inner shell** has
>    like I don't know what it's titanium or diamond, it's really thick"*; `[00:20:27]` *"it's
>    the **circle within the circle**"*; `[00:51:50]` *"Take that **outer shell** and break it,
>    come into the next layer."* V08's model is four concentric rings and its final frame is a
>    literal `?` at the centre. **V09 answers that question.**
> 4. **The recording opens on V08's closing frame.** The SWF's first rendered frame — before
>    playback starts — is the same ring diagram with the red `?`, carried over from the previous
>    file.
>
> **This is the first cross-file continuity in the corpus that was predicted in advance and then
> confirmed on non-acoustic evidence.** The prohibition on using the `f0_profile.py` acoustic
> screen across files (`COURSE_PROGRESS.md` V07 GATE item (a)) was observed: it was not run.
>
> **What the identification does and does not license.** Under `D-025` consequence 4, re-adopted
> by `D-033` provision 2, **identifying a speaker is provenance, not evidence** — nothing in any
> V09 artifact depends on the name *Jim Nicholson* being right, and nothing depends on V08 and
> V09 being one talk. Every rule below stands on its own marker in this file.

Every source-note row in `03_LESSON_NOTES/V09_SOURCE_NOTES.md` carries the speaker tag
**`GUEST`** for this reason, and the tag means *"not the course author"*, not *"lesser"*.

## TRANSCRIPTION NOTES

- Confidence **MEDIUM**. The risk-management first half (`[00:00:00]`–`[00:28:00]`) is read
  largely from prepared slides and transcribes cleanly. The chart-walkthrough second half is
  live speech over a screen share and carries the M/W defect named above, plus pair
  abbreviations that ASR mangles (`GAGG`, `GU`, `GJ`, `UJ`, `AJ`, `EC`, `swissy`/`swissie`,
  *"aussie"*, *"cat"* for CAD, *"frank"* for franc).
- Recurring garbles preserved rather than corrected: *"lead wall"* (brick wall), *"Subio"* /
  *"seebull"* (a named participant, also *"Isubio"* in V06), *"marfa"* / *"marth"* / *"tagmarth"*
  (a named participant), *"25-foot stop loss"* (25-pip), *"50 tips"* (pips), *"green salt"*
  (grain of salt), *"three million homework assignments"* (spoken as such).
- **Nothing has been silently corrected.** Where this project believes a word is wrong, the
  correction lives in a note with its marker, never in the transcript body.

---

# VERBATIM TRANSCRIPT


[00:00:00]
Welcome back everybody.

[00:00:02]
Hope your brains have rested. I am going to fill them full of information. Okay?

[00:00:08]
I wanted to make sure you guys are nice and mentally refreshed for this next section.

[00:00:14]
Because this was a big issue for me.

[00:00:16]
After having gotten all these areas, what was this last little section? And it just so happened to be I

[00:00:23]
cannot yet maintain

[00:00:26]
consistent equity growth.

[00:00:28]
Please don't fault me for that misspelling. That isn't he supposed to be I was flying on these cards.

[00:00:33]
All right, so the next lead wall that I hit and I mean it was a thick one. It was crazy.

[00:00:40]
I was like all right. I'm doing all this stuff. I've got this bar. Why can I not maintain?

[00:00:45]
consistent

[00:00:47]
equity growth.

[00:00:48]
What the heck is wrong and?

[00:00:51]
Reason was was that I wasn't trading with defined risk

[00:00:56]
All right, hello, Subio master this stuff. All right. There's a reason guys that have been trading 30 years

[00:01:03]
Deal with risk as one of the primary aspects is well Ray mentioned that you mentioned it as being a pinnacle of your trading system

[00:01:12]
Okay, so

[00:01:14]
What do we call risk?

[00:01:17]
Risk in forex is defined as

[00:01:21]
What percent of your account balance would be lost if your trade went to stop loss?

[00:01:29]
Okay

[00:01:31]
One of the great benefits of trading with defined risk is that we are emotionally prepared if the stop loss happens

[00:01:39]
I'm gonna show you you're gonna be actually happy. You don't believe me now. Wait. Give me a few minutes. All right

[00:01:45]
Because there is no unknown drop in our account balance

[00:01:51]
What?

[00:01:53]
Makes the risk defined is the lot size we choose to put on

[00:02:00]
We multiply our account balance by point

[00:02:03]
O2 and divide our stop loss and pips into that number that will determine the lot size

[00:02:10]
Okay, I'm gonna go over this a couple times. So hang on the questions

[00:02:13]
I know it's gonna sound a little funky and math and all this stuff. I hope I'm not

[00:02:18]
I'm not gonna bore you like some of your teachers. This is gonna be fun. I guarantee you there's a light at the end of the tunnel

[00:02:23]
Alright, so here's an example

[00:02:25]
So $12,500 USD account multiplied by 0.02 brings us a

[00:02:32]
$250 loss that would equal

[00:02:35]
2% of this account balance we take that

[00:02:38]
250 divided by say 25 pips as our stop loss that gives us 10 minis or one lot to trade

[00:02:48]
Kind of fortunately, there are many free lot size calculators on the web

[00:02:53]
Use one for the health of your equity curve

[00:02:56]
Okay, type in a lot size calculator 4x lot size calculator tons of free ones

[00:03:02]
You'll be able to get all your crosses any combination GAGG

[00:03:08]
Israel shekel pound doesn't matter you will be able to find what 2% of your balance is with one of these free lot size

[00:03:16]
Calculator I suggest you go get one right

[00:03:19]
With 2% risk at stop loss

[00:03:23]
One can lose three trades in a row and still have enough margin to come back and negate the loss with just one trade

[00:03:33]
Mastering the high low-day entries can allow one to trade with a pure three to one risk to reward ratio

[00:03:40]
meaning

[00:03:41]
One can lose three times in a row and with one winner they can negate the loss

[00:03:49]
Example solid high low-day entries can warrant a 15-pip stop loss

[00:03:56]
Three stop outs is then minus 45 pips one win is plus 50 pips that nets out to plus five pips

[00:04:05]
Big point this is the type of thinking necessary for consistent equity growth

[00:04:11]
This is the rest of the game. This is after you've been on the driving range. You've hit enough balls

[00:04:15]
You've done on the planning range

[00:04:17]
Done all the things you can to get your game together

[00:04:19]
But now you're gonna get on and play 18 and try to beat the other guy in this case

[00:04:24]
There's really nobody to beat except yourself

[00:04:27]
Okay, you've been given the method that will work

[00:04:29]
We are now trying to give you the tools of the math. They'll carry you over into the end zone

[00:04:35]
All right spike the football be happy

[00:04:37]
Okay, this is great stuff and this this came through huh?

[00:04:40]
I don't know how many counts. I had to blow to learn this guys. All right. I know you guys out there who have done this are going up

[00:04:45]
Thank God. It's about time all good. No question. Let's keep rolling

[00:04:49]
Until one develops the high low skill they can use a simple two to one risk to reward ratio

[00:04:55]
And this example will use 25 pips stop loss and a 50-pip take profit

[00:05:01]
In this case two stopouts can be negated with one win

[00:05:08]
After we take a stop out we come back with the same lot size

[00:05:12]
Until we negate the loss, right?

[00:05:14]
This is the slight spin that I'm gonna put on to this which will make it simpler for you guys and

[00:05:20]
Hopefully you'll put this to the test in a demo and improve me, right?

[00:05:24]
This is the way that I've done it and it allows me to come at my game in a much more simple manner

[00:05:30]
Okay, so I'm gonna repeat that after we take a stop out

[00:05:33]
We come back with the same lot size until we negate the loss

[00:05:36]
If our balance is only set back two percent at each loss

[00:05:40]
We are sure to avoid margin issues for the third or fourth trade which will be the one that negates the loss

[00:05:47]
Okay, so your first three or four losses are built on a risk reward basis once you get past that fourth trade

[00:05:54]
You then bring your your meltdown and let me make this clear if one takes four stop losses in a row

[00:06:01]
It's time to recalculate our lot size as the account balance has now drawn down eight percent of original equity

[00:06:08]
Believe it or not. This is still a rather aggressive approach to risk management. How are I believe that with our training?

[00:06:16]
It's highly unlikely. We're gonna lose three or four times in a row

[00:06:20]
If of course, we've put the time in to develop the rest of our game

[00:06:24]
All right, that's the reason that this is done this way and it's kept simple

[00:06:28]
So you guys don't have to be fiddling with

[00:06:31]
Lot size calculators when you have to come back at these guys the second or third time

[00:06:34]
I want you guys to just come back at them. Okay, you don't have to think about size once you've determined what your sizes are

[00:06:40]
You come back until you win. Okay, so in this scenario, we've lost four times. We're down eight percent of our original equity

[00:06:49]
12,500 is now 11,500

[00:06:52]
Okay, two percent of 11

[00:06:55]
500 is 9.2 minis or 0.92 lots. That's a now we're starting to dial down our leverage

[00:07:03]
With a two-to-one ratio minus 25 plus 50 our first-winning winning trade will bring us back up to 11,960

[00:07:14]
Okay, after each win we recalculate our lot size based on two percent risk of balance at stop loss

[00:07:21]
So every time you win a trade go into your stop loss calculator get the new number

[00:07:26]
It's going to be a little bit above what your previous number is. Okay. That's compounding working for you, all right?

[00:07:33]
Our second winning trade then brings the account balance up to 12,500 essentially we've come back

[00:07:40]
We've had four losses and in two losses and two wins we came back and we're back to where we were now think about this

[00:07:48]
How many times has that won loss or that second loss?

[00:07:52]
Got y'all frazzled you don't know what to do everything is

[00:07:56]
Confusing to you all right now is your moment of peace all right because you're going to have a plan

[00:08:03]
whereby you can attack this thing with the math on your side and

[00:08:08]
When you have a map on your side, it's it's a lot more peaceful

[00:08:12]
Okay, there's no way that you can be doing stupid stuff if you stick to this type of scenario

[00:08:17]
Okay, let's continue into this gets deeper

[00:08:20]
To recap we calculate lot size in relation to percent of balance drawdown at stop loss

[00:08:28]
2% is a good place to start

[00:08:30]
Okay, if we take a stop loss our first stop loss we come back with the same lot size you take your second loss

[00:08:37]
You come back with the same lot size

[00:08:40]
If you lose a third time you still come back with the same lot size

[00:08:43]
And if you lose a fourth time you recalculate your lot size as you are now down a percent of your original balance

[00:08:51]
This is what's worked best for me. This is allowing me to have a positive equity growth

[00:08:57]
This is my my spin on it. Of course there are a lot of experts here that are going to

[00:09:01]
Look to tweak this and that but i'm just giving it out there for the guys that possibly haven't even looked at our risk

[00:09:07]
Any relation to forex before i want you guys to have this okay, you will blow up accounts unless you work this way

[00:09:13]
All right

[00:09:14]
So the basic idea is that as you hit winning trades you increase your lot size and as you hit losing cycles of three or four consecutive stopouts

[00:09:23]
You diminish your lot size

[00:09:27]
All right

[00:09:28]
Managing leverage is the key to sustained equity growth

[00:09:32]
Without this last element of discipline it is quite easy to blow accounts

[00:09:38]
There is no where did i read this one before i actually wrote this before steve said this the other night i about fell out of my chair when he said it

[00:09:44]
There is no reason for a single loss nor even two consecutive losses to rattle s

[00:09:51]
Okay, I guess we're on the same frequency or some

[00:09:55]
If we have a strategy to manage risk we can simply come back

[00:10:00]
Clear-minded and can trade without fear when the signals reappear

[00:10:06]
And reappear they will 29 times last week guys

[00:10:11]
All right now let's just pretend we're five-year-olds the first time we've ever looked at this and let's approach this

[00:10:18]
Okay, i've made this graph of wins and losses the greens are the wins the reds of the losses

[00:10:23]
We have a win we have a loss a win a loss another loss a third loss

[00:10:28]
a win a win

[00:10:30]
And so on okay, you see an upward equity flow, but guess what

[00:10:35]
There's only eight wins and 11 losses and you have net positive equity

[00:10:42]
All right

[00:10:44]
When you from when this stuff first started rattling around in my brain i was just miffed

[00:10:50]
How could i not trade with the math on my side? It's crazy

[00:10:54]
All right, here's another scenario

[00:10:56]
You've gotten good at your high-low entries you've carved out a consistent 15-pip stop loss on all your entries

[00:11:04]
You're going for 50 take profit

[00:11:06]
You get a win a loss a win three losses in a row. You're still up another win two losses and so on

[00:11:12]
Okay, your equity quote is building you're losing you're not you're not have to be perfect here

[00:11:17]
What's the ratio on this seven wins and 12 losses and you still have a net positive equity curve

[00:11:24]
All right shaking your head going. Oh my god

[00:11:27]
I did when I first saw this stuff was like why did they tell me this why not to go buy all those robots and spend all this money on garbage

[00:11:34]
All right

[00:11:35]
Here's an even more aggressive one

[00:11:37]
Okay, you're using proper risk management you're being aggressive

[00:11:41]
You're really trying to catch the high and low day and you're jumping out when it hits you 15 take your 15 out

[00:11:46]
Next one get back in take your 15 out

[00:11:48]
You get a nice hit first and you get four against you one up and three against you another one up

[00:11:53]
Four against you one up only one against you another one up and then two against you and then one up

[00:11:59]
All right because you're using

[00:12:01]
defined risk

[00:12:03]
And making a ratio of your wins and losses guess what?

[00:12:06]
You had six wins and 14 count them 14 losses

[00:12:12]
All right, you still had a net positive equity curve

[00:12:15]
Think about that you've lost 14 times and won six times and you're still there got an equity curve

[00:12:20]
It's going up you're making money. You're doing exactly what you guys are all here to do

[00:12:25]
You know we're taking these high low drills not to like look cool by grabbing that pin at the high or the pin at the low

[00:12:30]
And posting it on the form that's not why we do it

[00:12:32]
We do it so we can manage a nice tight stop loss and risk through reward ratio

[00:12:38]
And this is exactly why six wins 14 losses. I'm still ahead. Oh my god

[00:12:43]
All right now

[00:12:46]
We define risk by choosing lot size which is minus 2 percent of balance at stop out

[00:12:53]
That means we can then be able to withstand three consecutive losses

[00:12:58]
Honey, I just lost. Oh, that's okay. You're gonna have an up balance today. Okay. I lost again second time

[00:13:04]
Oh, no problem

[00:13:05]
How many of you guys honestly have lost two times in a row and have actually felt clean and clear in your brain come back at it

[00:13:11]
Probably not that many. I know I couldn't before I learned this there was no way that I could maintain my composure

[00:13:17]
After two consecutive losses let alone three

[00:13:20]
Okay, so here we go

[00:13:22]
So keep driving this in

[00:13:25]
when you do

[00:13:27]
Restrict your lot size to 2 percent of balance at stop out you have no margin issues

[00:13:31]
You can come back with the same lot size

[00:13:34]
All right, you're gonna come back at them strong. You're not gonna have stuff rattler on your brain. There's no more mystery

[00:13:39]
No more. Oh my god. I'm losing and and every painful thought that ever happens when your childhood rushes into you and you go

[00:13:46]
Punch stuff. It's not gonna happen because you're making an architecture with which to generate gains based on math

[00:13:53]
All right, this map doesn't wake up tomorrow morning and decide to change. Okay. The number three is now 5.6

[00:13:59]
Number nine is now four

[00:14:01]
It never changes. So once you enlist the math on your side

[00:14:05]
We're doing this in two ways. I'll show you you are going to have an incredible advantage using Steve's method

[00:14:12]
Incredible okay. There's some here that this is the piece. It's gonna do it. All right. It was for me

[00:14:17]
All right, so just passing it forward. Okay, this defined risk by choosing lot size at 2 percent

[00:14:23]
Means no emotional turbulence because you have a plan now to absorb the losses

[00:14:28]
You just wait for the next and then fx signal

[00:14:32]
All right

[00:14:32]
The second aspect of our risk

[00:14:35]
Determination is to use a greater than one to one risk three ward ratio. That means our take profit is greater than our stop loss

[00:14:42]
Okay, we had a two to one. That's our sort of beginners one

[00:14:45]
That's minus 25 and 50 tips and then we have the three to one

[00:14:48]
Which is the ideal which most people who have traded this method for some time should should get pretty close to all right?

[00:14:54]
So three to one risk reward is our ideal

[00:14:57]
All right

[00:14:58]
That means that we can have

[00:15:00]
More losers than winners and still have upward equity

[00:15:03]
Wait a second. I'm still shaking my head. Why is there no late night fx info about this stuff? You know how come x y z indicator

[00:15:11]
EA doesn't talk about this stuff. You know, why do they have me put my number in and every trade is 10 percent risk

[00:15:17]
Now what's going on here? All right guys should

[00:15:19]
Get your antenna stuck out the next level and say, you know, okay

[00:15:21]
It might be a reason this stuff isn't isn't told does all right. So here it is no excuses anymore. Okay

[00:15:28]
The high a low day skills can enable a three to one risk to reward ratio

[00:15:35]
Right

[00:15:36]
Simply trading with greater than 50 percent accuracy will bring upward equity

[00:15:43]
Okay, I gotta just stop this whole thing and freeze this frame and just keep it here all night because this is an amazing thing

[00:15:49]
When you can simply trade greater than 50 50

[00:15:53]
And still have upward equity you're doing something right

[00:15:55]
Okay, and then we're showing you how that's done here

[00:15:59]
All right, think of what your equity curve will look like when you can hit 70 percent accuracy

[00:16:06]
And you're still within this risk management scenario

[00:16:11]
Okay, the basic idea again is to keep a consistent spell that right this time

[00:16:16]
Ratio of lot size as your account grows or falls

[00:16:20]
As your account gets bigger your lot sizes go up as your account goes smaller your lot sizes go down

[00:16:26]
Okay, you hear a lot of talk

[00:16:28]
About well, I started to lose a few and so I decided to crank my lot size up. Oh, whoops haven't heard from that guy in a while what happened?

[00:16:35]
All right, we don't need to go into this. I'm not going to beat anybody's head

[00:16:38]
But I've done it so many times myself. It's I have the right to bitch because I've spent you know tens of thousands not knowing this

[00:16:45]
Okay, so we're going to save you money by this section review it as many times as you can

[00:16:51]
All right

[00:16:51]
So the basic idea is to keep consistent ratio of lot size as your account grows and falls and to consistently take profits larger than our stop losses

[00:17:00]
Pretty basic stuff. Nothing really too insane

[00:17:03]
Now here's the interesting part. No impulsive increases in a lot size to make up for a loss

[00:17:09]
All right, we've all been with other groups that really poured on when you lose

[00:17:14]
Okay, I'm not recommending that okay

[00:17:17]
I strongly advised to keep your lot size the same and come back at them and just have a bigger take profit than your stop losses have been

[00:17:24]
All right, the math is on your side of that case

[00:17:27]
Okay, no chasing no hail mary trades to try to force the negation of losses

[00:17:32]
Okay, hail mary trades boy. I've done a bunch of those. I'm sure you guys have too. All right, we're talking about it

[00:17:37]
It's in the open now. You know why they don't work

[00:17:40]
Now you have a system that you can use that's going to keep you from doing that

[00:17:44]
All right, there's no reason to if you have the math on your side

[00:17:47]
What's what's the point of doing a hail mary trade where you're going to try to make one trade that's going to make up all your losses?

[00:17:52]
All right

[00:17:54]
It's silliness anyway

[00:17:57]
With this type of risk management, there is no bugging out emotionally

[00:18:00]
Even when a string of losses even with a string of losses because you have put the math on your side and it thus

[00:18:07]
Created certainty in a turbulent environment. Okay. Why do airplane pilots have altimeters?

[00:18:14]
Speed gauges

[00:18:16]
Why is all this stuff important when they're flying through a fog? They need certainty

[00:18:21]
In a turbulent environment. Okay, it's the same with us except no one teaches this stuff. Well, that changed

[00:18:29]
So risk eliminated

[00:18:31]
Right now let's look at possible errors to guard against

[00:18:39]
Okay, this is

[00:18:41]
Experience talking as well

[00:18:43]
one

[00:18:44]
Moving your stop loss after you've placed it

[00:18:48]
And the seebull always says the first stop loss is always the cheapest

[00:18:52]
Okay, because you have a system in mind that you can weather three losses and in that

[00:18:57]
Fourth trade come back and get them. You don't need to move your stop loss

[00:19:00]
Wait for the setup to happen again. You come back at them. All right. That's a measured approach. You planned it out

[00:19:08]
You're not going to get twig

[00:19:10]
All right, two

[00:19:11]
another possible error

[00:19:13]
Putting on multiple positions which add up to greater than your percent risk

[00:19:18]
Okay, when I say two percent of risk on your account. I don't mean two percent gj two percent gu two percent eu another two percent uj

[00:19:28]
Okay

[00:19:29]
Talking about a cumulative risk that's never greater than two percent across your account

[00:19:33]
If you're looking at three pairs to trade you want to carve that lot size and three to come out to two percent

[00:19:40]
You overall exposure should be two percent

[00:19:43]
Okay

[00:19:44]
Don't get into that. That's that's that's the slippery slope. Okay

[00:19:48]
Another possible error to guard against not having a discipline to keep to the risk plan as described

[00:19:55]
Okay, that's why that inner shell has like I don't know what it's it's titanium or diamond

[00:20:02]
It's really thick. Okay, you can be great at spotting ends and W's and getting in at the

[00:20:07]
Hargride edge and all this kind of stuff. But if you can't step with a risk plan that's

[00:20:11]
Worked out prior

[00:20:14]
You will eventually get hammered because your emotions are going to get involved

[00:20:18]
You're going to do a Hail Mary you're going to try to come it back come back at them with a huge position and all of a sudden

[00:20:23]
You won't have the margin with which to come negate a loss

[00:20:27]
Okay, so it's another level of discipline. It's the circle within the circle

[00:20:31]
All right

[00:20:32]
This is not as easy as it looks. I hope you guys understand the idea here

[00:20:36]
And then take it and try to do it and see where it is that you

[00:20:39]
Come up against your own internal friction because I guarantee you it's going to be there

[00:20:43]
All right greed and fear of loss it's huge

[00:20:46]
right

[00:20:47]
so

[00:20:48]
Another possible air to guard against this calculating lot size on non USD quote pairs. All right use a lot size calculator

[00:20:56]
USD JP why on a USD based account is going to be a larger unit than a

[00:21:03]
Pair that ends in USD. All right, I'm not going to get technical here

[00:21:07]
It's not you can find that anywhere on the internet

[00:21:10]
The idea is that many other pairs out there will have different weightings in relation to the us dollar

[00:21:15]
So

[00:21:16]
Simply don't take the last size on the pair that ends with USD

[00:21:20]
I think that's going to work on the pair that ends with JP why or chf they're different

[00:21:24]
Okay, so use a lot size calculator you punch in USD CHF

[00:21:30]
Balance

[00:21:31]
Percent of risk at stop loss 2% it'll spit you out a lot size. Okay

[00:21:37]
Strongly encouraging this if you haven't gotten the point but now

[00:21:41]
All right possible errors to guard against number five

[00:21:44]
Not having hard stop losses and take profits with the broker

[00:21:49]
Okay, we all love the idea of having that cool EA that's stealthily

[00:21:53]
Putting in the take profit and the stop loss because we think the brokers after our

[00:21:58]
$25,000 account. Okay, let me tell you something

[00:22:02]
They're lap bigger fish in the ocean this kind of stuff. I really wouldn't be concerned with you're getting in at the right time

[00:22:09]
Okay, it's not going to be an issue to put those numbers with the broker

[00:22:13]
There's going to be times where your platform goes down

[00:22:16]
God knows what happens. All right. You want to always have hard stop losses and take profits with the broker

[00:22:22]
Okay, so every EA or or indie that that I'm using in regard to my trading and I'm bringing into the dmr

[00:22:29]
To help people

[00:22:30]
Always is putting hard stop losses and take profits with the broker. Okay. We have some trade management EAs

[00:22:35]
We're working on all that kind of stuff. It's making it easy, but it always throws that stuff in there

[00:22:40]
You always want that hard stop loss and hard take profit with the broker big big point

[00:22:45]
Okay, so what would we get?

[00:22:47]
If we had an 85 win rate

[00:22:50]
With a two two to one risk reward profile. All right here. We have seven wins and six losses

[00:22:57]
Oh my goodness, honey. We're going to tahiti

[00:22:59]
All right

[00:23:00]
Now you guys see that and I did this so our romper room part of our brain can

[00:23:05]
Internalize this stuff. This is a risk reward of 50. Here's 25. Here's 50 25 25 50 25 50 25 50

[00:23:15]
25 and 50 and 50

[00:23:17]
Okay, this is the kind of stuff that I'm seeing a lot of students

[00:23:21]
Doing every week. Oh, I lose a couple during the week

[00:23:24]
You know lose six and win seven how many times have you had a seven to six win loss ratio and your equity was flat or rolling over?

[00:23:31]
Okay, this

[00:23:33]
Last half hour of lessons is exactly why

[00:23:37]
Okay, if this is new to you or it seems unusual go back study it do what you can

[00:23:43]
You know take notes heavily because this is everything

[00:23:47]
You should be able to have an 85 win rate and have your equity just climb like a rocket ship

[00:23:52]
Okay with the math on your side. That is what's going to happen

[00:23:56]
Okay. So now let's look at a realistic

[00:23:59]
possible equity gain scenario

[00:24:03]
Okay, this is about planning we were talking about what do you plan to get for a week for a month

[00:24:09]
What are your objectives? You come into the week you say i'm cold breaking even by friday. All right, great. You have your plan ahead of you

[00:24:16]
Okay, what do I what am I looking for? Okay

[00:24:20]
Number one 2% risk at stop loss

[00:24:23]
Number two two to one or greater risk for reward

[00:24:27]
So a 25-foot stop loss and a 50-foot take profit

[00:24:31]
with that in mind

[00:24:33]
Your 25-foot stop loss is going to be minus 2% of the count balance and your plus 50 take profit will be

[00:24:40]
4% and that's compounded because we're going to be

[00:24:44]
Upping our lot size every time we win, right?

[00:24:46]
So we're looking at 4% per trade if we get it 2% if we don't get it

[00:24:52]
All right, so only five successful trades per week

[00:24:57]
It brings 20% gains

[00:24:59]
for the week

[00:25:01]
Oh my goodness. I had to do some more on that one. All right, so that's my personal target. This is what I like and i'll show you why

[00:25:09]
How hard is it to get five trades a week that are good

[00:25:11]
All right, you stand back and look at 29 that happened last week. You say yourself. Well, i'm a new york trader

[00:25:18]
Well, you've definitely had more than five in New York

[00:25:21]
All right, you're a european guy you pick them

[00:25:25]
You know the only thing that's going to keep you from messing

[00:25:28]
From not doing this is something inside yourself at this point. All the information has been given to you

[00:25:34]
All right, this stuff is is coming from street wisdom. This is actually being

[00:25:39]
Beaten up by the market where all this comes from. So hope you guys take that idea

[00:25:44]
All right, so we're looking at five successful trades per week each one of these grabbing 50

[00:25:49]
And it's going to be 4% per trade. That's going to give us 20% gains on the week

[00:25:55]
Now's where the math gets fun. All right, this is light at the end of the tunnel guys

[00:26:00]
In four weeks you doubled your account with a $5,000 account. You now have 10,000

[00:26:07]
368

[00:26:08]
Okay, another four weeks you doubled it again

[00:26:14]
Get another four weeks double her

[00:26:17]
another four weeks double her

[00:26:19]
You basically got almost 100 grand in four months of doing this if you can keep consistently finding the best trades

[00:26:27]
I know a lot of guys that can find five six seven good trades a week

[00:26:30]
All right, Casey's been doing it. She's getting six or seven. I hear you know this stuff was possible

[00:26:35]
Okay, then you double it again double it again

[00:26:38]
You're close to a million in seven months guys

[00:26:40]
And why because you're using the math on your side in addition to a real method

[00:26:46]
Okay, something that actually works. All right, so this is exciting stuff. This is why you

[00:26:52]
Attend these trainings. This is what you work for

[00:26:55]
This gives you your plan

[00:26:57]
You can look ahead and say okay. This is what i'm looking to do. Can I do can I have a discipline to only trade five times a week?

[00:27:04]
Okay, this is why i'm going to do that. All right, so you plan out as much as possible ahead of time

[00:27:08]
so that it allows you to

[00:27:11]
roll with the punches when they come

[00:27:13]
all right, so

[00:27:15]
It's a nice day out there. All right, you can leave the jail cell the door is wide open

[00:27:21]
Okay, this stuff is all in your hands now

[00:27:24]
And i hope you guys join us in the dmor

[00:27:27]
Okay

[00:27:28]
Okay, so

[00:27:30]
Jim Nicholson got dmor

[00:27:33]
at hotmail

[00:27:35]
dot com

[00:27:37]
Okay, that's where i work with only dmor students. That's also where you guys can send me questions

[00:27:42]
in relation to

[00:27:43]
This presentation regarding the risk scenarios and i'll try to get them

[00:27:49]
Answer it as best i can if i get killed i'll let you know

[00:27:52]
All right, so there we go. Let's then

[00:27:56]
go over the dmor

[00:27:58]
And

[00:28:00]
We are looking at the euro usd tonight

[00:28:04]
Just a brief explanation of my charts so you all can

[00:28:08]
Figure out what it is that you're looking at

[00:28:11]
I divide the week with a weekly divider. I draw in by hand

[00:28:14]
We do have an indicator in process to be made that will do this for us

[00:28:19]
And our days are depicted by the high low tracer as you can see monday tuesday wednesday thursday friday

[00:28:27]
All right, this is the euro usd last friday seemed to form a reset with the level one two three

[00:28:35]
Pulled back formed another reset

[00:28:39]
And now has shot above previous highs into what i am going to call a level one

[00:28:46]
And i'm going to back out the chart for a second and show you how

[00:28:50]
Price came up and negotiated this previous trap area nicely three times the first time it pulled away

[00:28:57]
very quickly

[00:28:58]
Third times it pulled away as well and now we've busted this range i would not be at all surprised

[00:29:05]
For this to come back

[00:29:07]
Tap this area and take off all right so for tonight we're expecting

[00:29:13]
a stop hunt drop

[00:29:16]
And rise in this pair so level one to the long side

[00:29:20]
in euro usd

[00:29:24]
Okay guys getting a free dmor out of the deal it's awesome

[00:29:27]
all right

[00:29:29]
euro yen

[00:29:31]
Same bat story

[00:29:33]
We're looking for an upward bias based on a large w formation that formed out thursday and friday

[00:29:40]
Of last week as a multi-day w on it went into level one created its beautiful

[00:29:46]
Straightaway and now we're in level two to the long side

[00:29:51]
in euro yen pair

[00:29:54]
Okay, we're looking at the euro cad

[00:29:57]
And in this particular count it looks a bit more stretched out

[00:30:02]
I am personally staying a reset that formed the beginning of last week

[00:30:08]
We have a level one we have a level two and I believe we're going to see a level three in this pair

[00:30:15]
A bit higher. So i'm saying we're also in level two long in this pair

[00:30:19]
but look for

[00:30:21]
trapping action to the high and a possible level three forming anywhere

[00:30:26]
Above this area. This in fact could be the first leg of a level three

[00:30:31]
These are dynamic candles. We've got some depth

[00:30:34]
Lot of volume always at level three. It's characterized by heavy volume and big moves both direction

[00:30:40]
Okay, so possible m forming up here and roll back down

[00:30:44]
But we're at level two so it can as well form an m

[00:30:47]
Independently of this previous trap area and hit level three sometimes tomorrow

[00:30:52]
Right so level two long in euro cad that's what i'm seeing here

[00:30:56]
Okay

[00:30:58]
GU pound dollar cable

[00:31:01]
Looks to have formed a reset interesting laughter after a one two down

[00:31:06]
Okay last week peak low was on thursday

[00:31:09]
Came back and i'm calling this a reset

[00:31:12]
Into a level one long just like the USD

[00:31:16]
euro USD pair

[00:31:18]
And counting out on a four hour chart. We do see a possible trap area coming up

[00:31:22]
This will be a lovely short when it hits here

[00:31:25]
Guarantee you want to be short when it does that

[00:31:27]
Okay, it might only come five or ten pips to that area so they don't free up anything. They have long here

[00:31:33]
But we do have a trap area that's

[00:31:36]
Pretty close now. All right, so pull back off this trap area and continue rises what i'm seeing in the pound dollar level one to the upside

[00:31:44]
And we always look to the left to see what we have to define where we are and the

[00:31:50]
Gj or pound yen looks to have had another nice multi-day w thursday into friday

[00:31:59]
It had a level one overnight last night yesterday

[00:32:04]
Beautiful straightaway on this pair looks to be in a level two to the long side as well

[00:32:10]
All right

[00:32:11]
Moving on to the pound swissy

[00:32:14]
And we get into some more complex levels in this pair of the last couple weeks

[00:32:19]
As you can see a lot of chop

[00:32:23]
A little bit more difficult to discern a count out of it, but I did spend some time on this earlier to

[00:32:28]
Bring something to you guys that can be tradable

[00:32:32]
And I do see a peak formation monday of last week. I think we call this accurately in the room

[00:32:37]
We had a one two three to the low

[00:32:41]
And i've negated any of this information because it looks like it's actually wing

[00:32:45]
That's a word w wing. I don't think so it looks like it's finding a w formation

[00:32:51]
Which is a multi-week w which sure would be nice. Okay, so in this pair. We're looking for a level three to the long side

[00:32:59]
Okay, one two three down

[00:33:01]
Looking for this pair to go along

[00:33:04]
And

[00:33:06]
Lovely aussie USD

[00:33:09]
Looks to be in a level three at this time

[00:33:12]
However, we do have the euro USD and pound USD wanting to go higher

[00:33:17]
So I haven't designated exactly where this level three is yet

[00:33:21]
Leaving this somewhat open. Okay. We have the grape up here, which I dedicate to marfa

[00:33:26]
Which is an 800 on the one hour. She loves the 800 on the one hour. It's pretty crazy

[00:33:31]
It's actually

[00:33:32]
Found a lot of good trains off this so I call with a grape on my charts

[00:33:36]
You guys don't have to follow suit. No big deal. So in the aussie USD we can see a nice one two three to the high

[00:33:43]
information pull it back level one

[00:33:46]
information against but with

[00:33:49]
The peak in line with the peak beautiful ham comes down level two

[00:33:53]
Level three is always characterized by expansion and acceleration

[00:33:57]
We certainly had extension and acceleration on Thursday in this pair

[00:34:02]
To peak out on a nice w look like an intraday w in aussie USD

[00:34:06]
These are two pins on an one hour chart on a 15 minute chart. That would be a nice w down there

[00:34:12]
We had our level one

[00:34:14]
Or level two and now it looks like we're going into level three

[00:34:18]
All right and the caveat to all of this is our lovely market maker cycle

[00:34:24]
Which we bring into play as soon as we start seeing

[00:34:27]
That form and we all know what that is right. I don't need to draw that out for you guys, but

[00:34:33]
Because i'm crazy. I will

[00:34:35]
Just do

[00:34:37]
paper rush and we know

[00:34:40]
That we're looking for this

[00:34:44]
The dinosaur pattern, okay

[00:34:48]
This pattern can always impose itself on the week. All right, so

[00:34:52]
Our level count many times will have to change

[00:34:55]
Did week if we see a nice am up here we expect three levels

[00:34:59]
Dropping back of course these guys don't move it much between these two areas because they're killing people on this side

[00:35:04]
And they're killing people on this side. All right

[00:35:06]
So with that in mind, it's possible that we can see an m form here

[00:35:11]
And then it can drop back down three levels for the rest of the week

[00:35:14]
Okay

[00:35:15]
So even though it's somewhat against fractional disparity on euro USD and pound USD

[00:35:21]
I'm calling it like I see it in the charts

[00:35:23]
This to me looks like it's forming a level three to the downside possibly will come up

[00:35:28]
Tagmarth is great here and fall away

[00:35:31]
All right aussie yen

[00:35:34]
Also like many of the jpe pairs last week if you guys were watching the USD JPY it was quite a show let's pull that up

[00:35:41]
Okay, we had a nice multi week m in this pair. All right, let me

[00:35:47]
drag my

[00:35:48]
2 3 4 5 drag my week indicator and will show you

[00:35:52]
That uj actually started falling away wednesday

[00:35:57]
Giving all of us ample time to look at yen pairs on thursday

[00:36:02]
All right now i'm gonna jump back to aj and show you what happened

[00:36:06]
Okay

[00:36:07]
Here's wednesday

[00:36:10]
And here's thursday, okay as that m was forming in aj

[00:36:15]
All right, look at this second leg m here basically second leg monster m was forming

[00:36:21]
Okay, it was starting to push this pair down

[00:36:25]
All right, so we had nice follow through the end of last week beautiful

[00:36:29]
1 2 3 3 3 trade to the low on this one

[00:36:33]
All right, so we had a level three form thursday into friday beautiful pin

[00:36:38]
Exceeding the range pulling in all the pending shorts driving them crazy sending them to all those four x educations that all of us

[00:36:45]
Don't associate with anymore because we know this works. All right

[00:36:49]
Anyhow, no for ranting looks like we had a nice level one rise straight away as curd

[00:36:54]
Over monday and now it looks like wearing level two to the long side

[00:36:59]
All right calling it like I see it

[00:37:01]
This as well could form out a fourth leg

[00:37:04]
Okay, aussie usd could easily go for here calling it level three because that's

[00:37:09]
The constraints of what we're dealing with all right level one level two calling this is a level two long

[00:37:15]
Much of that has to do with what's going on in the j all right j over time has ran up

[00:37:21]
a while

[00:37:22]
Okay, looks like it's

[00:37:25]
Had a nice run will it fall away? I'm banking on it and hence why I'm calling

[00:37:31]
Another up cycle in the aussie j

[00:37:34]
All right possible fade in the a you all right

[00:37:38]
Now let's look at the uf uf s t wissy

[00:37:41]
Okay, this pair has been

[00:37:43]
Very nice level count. I think our homework from last week that steve gave us was to mark up this chart

[00:37:50]
All right, I purposely left that free so you guys are sending in your homework of levels on last week

[00:37:56]
I'm not doing your homework for you. All right. That was the first week of bootcamp

[00:38:00]
He told you to mark up this chart. All right. I do see wednesday peak formation into friday level one

[00:38:07]
level two and level three to the downside and it looks like we

[00:38:12]
Packed that area again tried to form it upward bias and then it reset on us again at the grape

[00:38:18]
Or this previous trap area. I can easily see

[00:38:23]
Nice trap area. They came just right to it. All right pulled away heavily and down we go

[00:38:29]
All right, so it looks like we've had a level one and level two

[00:38:33]
Looks like we're starting to look at a level three turnaround. So I'm looking for a level three long in this pair

[00:38:39]
Going into tomorrow. So stop on low rise is what I'd be looking personally to trade in USD

[00:38:45]
Swiss frank

[00:38:47]
And last but very not least my favorite pair for the consistency of the second legs in New York

[00:38:53]
the USD cat

[00:38:55]
Okay, and this has been a real problem child and getting level counts as you can see it's been chop city coming

[00:39:03]
Coming back here. So many times we get on the dmr and this is the one we really have to think about

[00:39:08]
All right, but it's all good because we've been right more times than we've been wrong. I know that's for fact

[00:39:13]
All right, so

[00:39:14]
Looking at a one two three to the high it's come down once come down a second time

[00:39:21]
Looking at a peak formation last friday. This is a really nice amp complex emlement one hour chart that on a 15 minute chart

[00:39:29]
It's just beautiful

[00:39:31]
All right came down to its first consolidation

[00:39:33]
Came down to a second consolidation

[00:39:35]
Looking for this to be a level two to the downside

[00:39:39]
Meaning i'm looking for this pair to stop on high

[00:39:43]
and

[00:39:43]
Drop. All right. Let's do a quick recap for biases

[00:39:48]
Euro USD looking for a level one long

[00:39:53]
Euro yen looking for a level two to the long side

[00:39:59]
Euro cat is a level two to the long side with a three looming very close by

[00:40:04]
I

[00:40:05]
Pound dollar is a level one to the long side

[00:40:10]
Pound yen is a level two to the long side

[00:40:15]
Pound swissy is a level three to the long side

[00:40:21]
Aussie USD looks like a level three to the downside

[00:40:25]
And

[00:40:28]
Aussie yen looks like a level two to the upside however this as well might form an end and turn around on level two

[00:40:36]
Okay, we don't know this pair follows the Aussie so this one take with a green salt

[00:40:40]
Still calling it like I see it w in the bottom one two

[00:40:44]
Looking for a level two long on this pair

[00:40:46]
Hopefully you guys see these aren't exact science. This is potentials we're dealing with

[00:40:51]
Okay, enough study of this stuff also will tell you that it's good to know if you see it

[00:40:55]
Alternate count going one way or the other I've written down multiple counts a lot or I'll have a one up and a three down

[00:41:02]
Okay, not not a bad idea to to get fluent in that all right USD swissy

[00:41:07]
We have a level three to the long side. It's our bias on this pair

[00:41:13]
And finally USD cat is a level two to the downside

[00:41:16]
We have a stop on high drop bias to the downside in this pair and we can

[00:41:23]
Open the floor for questions

[00:41:25]
What is the grade Fred? That's the name that I've given to the 800 moving average on

[00:41:31]
The one hour chart don't concern yourself with it. It's just my own little twist twist of the thing that will be your blueberry

[00:41:39]
On your charts. Okay

[00:41:41]
This is the blueberry

[00:41:43]
The blueberry is the 800 on the 15 minute time frame

[00:41:48]
Okay, which makes this a 200 I synchronized my emas. I'm a little out of the box

[00:41:53]
All right, that's just the way I've done it. It's helped me and you know, fortunately we're

[00:41:58]
We're all coming together in terms of how we do this and uh, this is my way

[00:42:02]
This is the blueberry on the 15 right to coming through the second leg

[00:42:05]
I flip up to the one hour time frame that blueberry is still there

[00:42:09]
All right, I like to keep my emas consistent throughout all time regiments

[00:42:16]
Steve doesn't teach it. It's okay. This is my my twist on it. Just what I'm bringing to the table

[00:42:20]
Okay

[00:42:22]
Okay

[00:42:24]
So you're saying that eu and dollar Swiss are both me long

[00:42:30]
eu

[00:42:32]
This looks like it's going along

[00:42:35]
And the dollar swiss. I'm seeing three inducements to the downside

[00:42:40]
Okay

[00:42:43]
And that would mean that the swiss frank would be what would drive this pair

[00:42:47]
Okay, when we don't have alignment, okay, we all see this we want to have alignment with the u side

[00:42:54]
Okay, if usd decides to be the dominant pair of course

[00:42:57]
This is going to move against your usd if the frank

[00:43:02]
Is the dominant pair it won't matter what the usd does the frank will take over

[00:43:06]
And that's the same actually with the j pairs

[00:43:09]
When the j decides to be the dominant pair

[00:43:12]
Then it's going to affect all the j pairs ending with j and they won't have any correlation to the first part which is actually the base

[00:43:20]
currency, okay, so

[00:43:23]
I'm making this blow count based on what we see here. I'm not

[00:43:27]
Basing it purely on correlation of the usdollar

[00:43:30]
All right, if you were to correlate it, of course, it doesn't make sense

[00:43:34]
All right, that would mean that you're basing your entire decision on the usd the actual usdollar

[00:43:40]
All right, but the swiss can come out and do something based on the f which is the frank

[00:43:46]
okay

[00:43:47]
and that is just

[00:43:49]
Kind of kind of the way it goes. All right. You asked all or is not the only pair traded in the world

[00:43:56]
All right

[00:43:57]
Okay on the euro can what was the reasoning for your decision to class or reset in the uptrend?

[00:44:03]
I

[00:44:05]
Saw three levels of inducement to the upside and a distinct pullback

[00:44:13]
with

[00:44:14]
Two legs to the downside

[00:44:16]
Okay, this look to me looks like trapping activity

[00:44:19]
As well it trapped above the previous trap high over here

[00:44:24]
And never even came down and dealt with that area that to me is an upward bias

[00:44:29]
When the market makers start their cycle induce once induce twice induce the third time

[00:44:34]
We want to try to get people long

[00:44:36]
They form a pin up here

[00:44:39]
Because they're going to pull it back the other way and they're going to grab their pips and experiences show me that they can grab

[00:44:44]
All their stuff at 50 pips. They can easily

[00:44:48]
Get enough people trap pull it back and that can reset the count

[00:44:52]
So in my eyes, I saw a clean one two three

[00:44:56]
Pullback w three legs actually and then a new count forming

[00:45:07]
Okay, and the last question is if the if the dollar swiss did a reset at the blueberry

[00:45:13]
Aren't we in level two but he do is level three

[00:45:17]
We very well candy and for you guys that want to have a literal

[00:45:21]
Uh translation of a us dollar based correlation. Yeah, you can call that too

[00:45:27]
Definitely and the way that I would mark that I know this is a little out of the box

[00:45:30]
But I did this a lot and it was very very successful

[00:45:34]
Is that I would mark it a two

[00:45:37]
To the downside I would actually make that

[00:45:41]
Tomato color put that here and then I would actually

[00:45:51]
Throw in a bracket after it and so I would have an alternate count

[00:45:54]
Okay, there's nothing wrong with alternate counts. We like to have everything solid in the sand

[00:45:58]
You know line in the sand

[00:46:00]
But in this business you're looking a lot of times at potentialities

[00:46:04]
And when I see a pair possibly going in two different directions. I'm not afraid to throw in an alternate count

[00:46:09]
That's just my personal way of trading. I don't want to pose that on anybody

[00:46:13]
But I've had count list

[00:46:14]
From 17 pairs with at least half of them having alternate counts on them. So

[00:46:20]
Because it is off a large m.a. Yeah, that might might be the reason it does that. I honestly look more towards

[00:46:28]
Inducements which would be three pushes three

[00:46:31]
Accelerations the third being the longest. Okay. I see a nice long acceleration here. All right. That's my own reasoning

[00:46:38]
Okay, we don't claim to be 100% with these. I don't think anybody can be

[00:46:42]
But these do help us form a bias that overall wins more times than loses

[00:46:47]
And the pattern is what's going to dominate our trading. We want to see what this pair does

[00:46:52]
When it comes out of the asia range, all right in asia right now, so

[00:46:57]
If there's bear comes out and does a stop on loan forms a nice w there

[00:47:02]
Then that level three information is going to be nice because it's going to be a nice trade in the upside

[00:47:07]
Okay, if it in fact starts to stop on high and forms an amla up here to the downside

[00:47:12]
I personally would avoid it level two, but that would validate your level two. So we're looking for

[00:47:17]
Pattern to determine what our bias ultimately is on this pair

[00:47:22]
Knowing that it possibly could be two or three, right

[00:47:26]
Hope I've confused you is it asking me is usd jpy in your level account? How harvey? How are you buddy?

[00:47:35]
I always look at usd jpy. However in the dmor we haven't included it in the pairs

[00:47:43]
and

[00:47:45]
I was working with my friend joe a couple days ago

[00:47:47]
And he's asking me, you know, give him an assignment to help with the levels

[00:47:50]
All right, what what can I what can I do is what he was asking?

[00:47:54]
He gave me something concrete so I can study the levels and get better at it

[00:47:57]
And what I told him to do was I told him to take usd jpy for the specific reason that we don't cover it in the dmor

[00:48:05]
Okay

[00:48:06]
And what he's going to do is he's going to try to sus levels in it

[00:48:10]
And then at the end of every day

[00:48:13]
He's going to pop in an arrow

[00:48:16]
Hopefully bigger than that

[00:48:18]
in the direction that he thinks

[00:48:20]
This bad boy is going to go

[00:48:22]
And then see what it does tomorrow

[00:48:24]
Come back at it on tuesday. All right. What do I think i'm in tuesday? Am I in level xyz?

[00:48:30]
Okay, the end of the trading session look at that pop an arrow in there see how you do

[00:48:35]
Okay, that's

[00:48:36]
Inmeasurable benefit as far as training is concerned because you're taking a pair

[00:48:41]
And I wouldn't even talk about it with anybody. I'd frankly do this on your own

[00:48:45]
Don't say oh did it go up did it go down

[00:48:47]
Next day look at your chart. Where did it go?

[00:48:50]
If you had it going long did it work? Okay, so i'm going to pass that out to you guys in addition to the three million homework assignments

[00:48:57]
You've already gotten

[00:48:58]
You know take the uj start adding arrows at the end of the day

[00:49:01]
Based on levels of see where it's going to go

[00:49:03]
All right, so I love the j because it drives five other crosses that are all very tradable

[00:49:09]
All right

[00:49:10]
Stuff on

[00:49:11]
Eu you said you had a reset today

[00:49:14]
But after two levels of drop there is the w on

[00:49:18]
322

[00:49:20]
And on 323 price broke the high of 322. Why isn't that the reset? Oh?

[00:49:27]
Why isn't this the reset up here?

[00:49:31]
Is that what you're saying card you think is yeah

[00:49:35]
Uh, no where you have the reset where you wrote reset right now. I think that

[00:49:45]
Broke out of three

[00:49:47]
Yeah, I don't think it broke out of three susan. I think it's still still the same level when it when it

[00:49:57]
I don't know. Yeah, yeah, that's what that exactly. I think that's what she's talking about that area. Oh, okay. Oh, I see

[00:50:04]
Yeah, I always look at a reset to have some type of context

[00:50:09]
multi-day

[00:50:10]
And in this case we definitely have what can be considered a trap area

[00:50:15]
Now let me show you guys because this is actually pretty cool went into this in New York with the car group

[00:50:19]
It was great. That's uh go into it again some other point

[00:50:23]
All right, here's a nice trap

[00:50:25]
to low and it

[00:50:27]
Conforms to this area didn't necessarily trap up to it. So it didn't do its typical trap high than trap low

[00:50:34]
But you can see pins forming the beginning of friday and then a last final pin here forming

[00:50:41]
Little of friday that then becomes the context for this second leg. So i'm seeing a multi-day w here

[00:50:48]
so I based my resets

[00:50:50]
on the fact that it actually has a correlation back to a previous trap volume area

[00:50:57]
That trap volume means what they sent the market down to get shorts

[00:51:01]
Committed this direction and they've pulled away from them and they haven't come back to them market makers are still

[00:51:07]
Toying with this level and pulling away from it twice. Okay to me that shows a

[00:51:13]
Reset of their count

[00:51:19]
Okay, so she got a she said she got a rough guard and what we were saying. Okay. Yeah, good stuff

[00:51:25]
One last comment on levels guys your best possible

[00:51:31]
Teacher and all in levels is not if someone sees it or if they think it's right slap some arrows on there

[00:51:37]
And see what it does the next day

[00:51:39]
You know all the stuff that we're being asked constantly is answerable in the homework

[00:51:43]
That's why homework is the authority and I guess now we're calling it research and development is the authority

[00:51:49]
You know

[00:51:50]
Take that out or shell and break it all right come into the next layer and say okay

[00:51:54]
I am going to go look at the chart find out what this does

[00:51:57]
In this and that circumstance i'm going to take the step and try to answer my own question by going back in the charts

[00:52:03]
All right very important. We want to set you guys free

[00:52:06]
We don't want to enslave you guys. We don't want to be here two years from now explaining him and w's

[00:52:10]
We want you guys to get on your yachts your children in good colleges and you know

[00:52:15]
Happy health and good life. All right. We're here for this time period to get you past the line

[00:52:20]
And then kind of cut you free and that was the whole idea of this bird right here

[00:52:23]
I mean he's got wings was using his legs at first
