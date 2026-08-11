# V04 — TRANSCRIPT

## SOURCE

| Field | Value |
|---|---|
| Video ID | V04 |
| Original filename | `Bootcamp1 Wk2 032512 Part2 (86mins).swf` |
| SHA-256 | `10d8fe7e0410a12c605abb19cebaae8ad5f39ec78a4ab2e8da553117fe60fb7c` |
| Duration | 01:25:41 (audio measured 5141.03 s; SWF header 15,425 frames ÷ 3.0 fps = 5141.7 s; `00_SYSTEM/SOURCE_MANIFEST.md`) |
| Lesson title | UNKNOWN — no title is stated on the recording or in the library |
| Session date | 2012-03-25 (from filename `032512`; the instructor says "It's 809 Eastern Time on 325" at `[00:07:01]`) |
| Transcribed by | ASR, by a pre-ingestion session. Copied and verified 2026-08-10. |
| Transcription confidence | MEDIUM — see TRANSCRIPTION NOTES |

## COVERAGE

```text
STATUS: COMPLETE, with a fenced ASR-degeneration tail (see below)
Covered: 00:00:00 - 01:25:37  (genuine content)
Fenced:  01:25:40 - 01:26:04  (9 entries, ASR degeneration, NOT source evidence)
Entries: 1,601 total = 1,592 genuine + 9 fenced.
         Timestamps are NON-DECREASING throughout; they are NOT strictly
         monotonic — there are 6 benign same-second adjacent pairs, at
         [00:20:55], [00:21:29], [00:21:33], [00:22:06], [00:24:21] and
         [00:26:05]. No timestamp ever decreases.
         Largest inter-entry gap among genuine entries is 20 s, [01:05:45]->[01:06:05].
```

> **Wording note.** V03's coverage block claimed *"strictly monotonic, no duplicates"*
> and review R1 charged that as `M2`/`E20` because three same-second pairs existed.
> This block states the weaker, true property (non-decreasing, 6 same-second pairs)
> rather than repeating the overclaim. `REVIEW_INDEX.md` open item 19.

### The fenced tail — a real defect in the source transcript

The last 9 entries, `[01:25:40]` through `[01:26:04]`, are a **degenerate ASR repetition
loop**: the identical sentence *"And then you're going to get the cherry picks first."*
nine times at exactly 3-second intervals.

Two independent facts establish that they are not source evidence:

1. **Eight of the nine point past the end of the file.** The audio is 5141.03 s long
   (`01:25:41`). The markers `[01:25:43]`, `[01:25:46]`, `[01:25:49]`, `[01:25:52]`,
   `[01:25:55]`, `[01:25:58]`, `[01:26:01]` and `[01:26:04]` are 5143 s … 5164 s —
   **up to 23 seconds beyond the last sample that exists.** There is no audio there to
   have transcribed.
2. **An independent re-transcription of the real tail does not contain them.** The final
   81 s of audio (5061 s → end) was re-transcribed in this session with Whisper `base.en`.
   Its last segment ends at 5140.3 s with *"…what they're doing and you won't need any
   help"* — which is exactly the transcript's last **genuine** line, `[01:25:37]`. The
   recording simply stops there. Nothing resembling the repeated sentence occurs.

The 9 entries are **retained below, inside an explicit fence**, rather than deleted — the
project does not silently remove material from a source artifact. **No source note,
interpretation, ambiguity, contradiction or homework item may cite them.**

This is a transcription artifact, not fabrication: a repetition loop at end-of-audio is a
well-known ASR failure mode and is, if anything, further evidence the file is machine
output rather than hand-written invention.

## PROVENANCE AND VERIFICATION

This transcript was **not** produced by this session. It was found at
`01_SOURCE_VIDEOS/Forex Bootcamp/Bootcamp/Bootcamp Notes/04_Bootcamp1_Wk2_032512_Part2_86mins/TRANSCRIPT.md`,
alongside `NOTES.md`, `RULES.md` and `VISUAL_INDEX.md`, all three of which this session
examined and found **fabricated** (`00_SYSTEM/QUARANTINE_REGISTER.md`, Q-004 — the same
template-stamped fabrication already confirmed for V01, V02 and V03).

Sharing a folder with fabricated material is not evidence against the transcript, but it
required that the transcript be checked before adoption, per `SETUP_ISSUES.md` I-008. It
was checked against all four I-008 criteria and **passed**, with the tail defect above
fenced:

1. **Length matches the audio.** Last genuine entry `[01:25:37]` against a measured
   `01:25:41.0`. Independently, the SWF header's own frame count (15,425 at a declared
   3.0 fps = 5141.7 s) agrees with the audio to 0.7 s — two unrelated derivations of the
   duration that the transcript's body sits inside. Non-decreasing throughout; largest
   genuine gap 20 s. The only entries that fail this check are the 9 fenced ones.
2. **Spot-checked against the actual audio.** Four 60-second windows (`00:03:00`,
   `00:25:00`, `00:50:00`, `01:10:00`) plus the 81-second tail window were independently
   re-transcribed from the extracted audio with Whisper `base.en` and compared. **All
   five matched near-verbatim**, including low-frequency specifics a fabricator would not
   invent: *"GJ formed a perfect M formation inside the blue box"*; *"how many times do I
   have to tell you not to take shit that's inside the range of the blue box"*; *"you
   cannot go and tell somebody that you can pick the high and low and the reversal point
   … they will tell you that you are a berserk crazy, you need to be in a straight
   jacket"*; *"there was a bunch of money sitting up here and they had to go after it —
   this pair was the Euro"*; *"one two three swipes … gave you a nice ugly looking
   kindergarten [M] there"*; *"here's the 32 button and it's well below that, it's
   probably 25"*. Divergences are ASR-vs-ASR only and never of substance
   (*"corrected a hundred plus bibs"* vs *"a hundred-plus-pips"*; *"that stuff cuts man"*
   vs *"that's tough cuts, man"*; *"Variation on the fame"* vs *"variation on the
   theme"*). **One numeric divergence is recorded rather than resolved:** at
   `[00:50:11]` the adopted text reads *"when I'm up more than 20 pips, I generally move
   my stop-offs to break even"* where the re-transcription hears *"more than 15 or 20
   pips"*. Neither reading is preferred here; the figure is treated as uncertain wherever
   it is cited.
3. **It contains its own errors.** Garbled ASR is preserved rather than smoothed —
   *"corrected a hundred plus bibs"* for "pips" `[00:03:27]`, *"Essenture Consolidation
   Zone"* for "in essence, the consolidation zone" `[00:11:48]`, *"all these criteria are
   Matt"* for "met" `[00:13:57]`, *"the virgins"* for "divergence" `[00:49:58]`,
   *"row-well tracks"* for "railroad tracks" `[01:14:06]`, *"Made a beautiful lamb"* for
   "M" `[00:57:07]`, *"CZ's method"* for "Steve's method" `[00:51:50]`, *"the 80 R low"*
   for "ADR" `[00:53:17]`, *"Irregardless"* `[01:24:18]`. A fabricated transcript does not
   invent its own mishearings — and it does not invent a nine-fold repetition loop past
   the end of its own audio either.
4. **It reads as a live webinar, not a summary.** Named students are answered in real
   time (Greg, Joe, Whitney, Alex, Tom, Rob, Chris, Brian, James, Jerry, Max, Fred, Clem,
   Manny, Murray, Harvey, Helen, Gloria, Derry, John, Jose, Bill, Bruce, Poe, Steven,
   Jayne/Ian, Michael, Kim, Steve-the-student), there is crosstalk, and long
   administrative and personal stretches are retained (a rebuttal of student negativity,
   a newborn baby, Disney trips, a four-monitor hardware digression).

### One thing was removed

The original file opened with a metadata block claiming
`Course Position: Video 05 of 21` and
`Primary Topics: Session Overlaps, Time Mapping, London Trend Run, New York Reversal`.

That block is a **derived claim by the same pre-ingestion process that produced the
fabricated files**, not part of the transcription, and both of its load-bearing claims are
wrong. The position reflects the alphabetical-sort misordering corrected at ingestion
(D-017 — this is **V04**, not V05). The topic string is not a description of this
recording: *"overlap"*, *"time mapping"*, *"London trend"* and *"New York reversal"* each occur
**zero** times in the transcript body (they exist only in that header), and the
lesson's actual subjects are the prohibition on trading inside the Asian range, the
entry criteria for the second leg of an M/W after a stop hunt, flashcard construction, the
four-hour weekly-cycle homework, and — for the second half — a **guest presenter's**
personal US-session practice. It has been dropped rather than carried forward. The
verbatim body below is unaltered.

## TWO SPEAKERS — A PROVENANCE BOUNDARY THAT MATTERS

**This recording has (at least) two presenters, and the transcript carries no speaker
labels.** This is the single most important thing to know before citing anything from it.

| Segment | Speaker | Basis |
|---|---|---|
| `[00:00:00]` – `[00:26:56]` | **The instructor** (Steve Mauro, the course's author) | Continuous with V01–V03's voice; speaks of "my boot camp thread", "I'll post the answer key in my section", assigns the homework, is addressed by students as Steve |
| `[00:26:59]` – `[01:25:37]` | **An UNIDENTIFIED guest presenter — a student/coach, NOT the instructor** | Says *"if your student folder Steve gives you nine pairs to trade"* `[00:30:29]`; *"Steve, I mean, just nailed it on the head with the four-hour"* `[00:34:13]`; *"every single thing that I know about trading, I learned from Steve"* `[00:42:25]`–`[00:42:29]`; *"what has Steve taught us? What has he taught me?"* `[00:58:54]`–`[00:58:56]` |

**The transition is not announced.** There is no "let me hand over to…" line. The boundary
is placed between `[00:26:56]` (*"If you do, no need to send me an email"* — the
instructor closing his own segment) and `[00:26:59]` (*"So I wanted to cover some of the
timeframes…"*) on **content grounds only**, and that is the honest status of it.

The guest is **never named in the transcript.** What is known about him is only what he
says: his wife is Diana/Diane `[00:27:35]`, `[00:56:02]`; he has a son who trades with him
`[00:41:39]`; he lives in Orlando, Florida `[00:27:49]`; he has used the method for close
to three years `[01:11:09]`; he watches 12 pairs `[00:30:22]`; he trades roughly 08:15–11:00
US session `[00:28:33]`, `[01:24:10]`. A **third** presenter, "Carl"/"car", is queued to
take over after him (`[01:13:18]`, `[01:19:02]`) but does not speak inside this file.

**Consequence for every downstream artifact, under `DECISIONS.md` D-008.** The guest's
statements are *not* instructor doctrine. They are a practitioner's personal practice,
delivered inside a course session, and several of them **differ from what the instructor
teaches elsewhere** — most sharply on session (the instructor trades the London stop-hunt
window `[00:21:33]`; the guest explicitly does not and trades only the US session
`[01:20:55]`-`[01:21:12]`) and on second-leg entry (the instructor's core criterion `[00:15:43]`–
`[00:15:56]`; the guest says *"in the US session, you generally don't get a lot of second
legs. You just don't get them."* `[01:14:13]`–`[01:14:18]`). `V04_SOURCE_NOTES.md` tags every
row with its speaker for this reason, and `CONTRADICTIONS.md` C-005 records the conflict.

## TRANSCRIPTION NOTES

Confidence is **MEDIUM**, for the same reasons as V01–V03: the ASR is good enough to follow
the argument but mangles domain vocabulary and proper nouns. Notable recurring garble a
reader should not mistake for terminology:

- *"the mail"* (`[00:46:57]`, `[00:47:38]`, `[00:49:51]`, `[00:55:35]`, `[00:57:x]`,
  `[01:19:26]`) — almost certainly the same moving-average nickname V02 rendered as
  *"mayonnaise"* and V03 as *"manays"* / *"minis"* (**A-020**, still unresolved). Which
  average it denotes is still never stated in this lesson either.
- *"the water"* (20×) — spoken as-is, and distinct from *"the mail"*; both are used as
  take-profit destinations by the guest presenter. V03 has *"blood in the water"* and
  *"bloodline"* for a TDI line; whether the guest's *"water"* is the same object is
  **not** established here (**A-037**).
- *"lamb"* `[00:57:07]`, *"ma'am"* `[01:10:36]`, *"now"* `[01:11:47]`, `[01:12:09]`,
  *"AM"* `[00:21:53]`, `[00:21:59]`, *"M-o-form"* `[00:00:37]` — all garble for the
  letter **M** (the M formation).
- *"Essenture"* `[00:11:48]`, `[00:11:56]` — "in essence, the".
- *"80 R"* `[00:52:45]`, `[00:53:17]`, *"AVR"* `[01:09:06]`, *"T.T.S."* `[01:18:18]` —
  garble for **ADR** (average daily range), which is spoken clearly 17 other times.
- *"row-well tracks"* `[01:14:06]`, *"a railroad track type"* `[00:20:12]` — railroad tracks.
- *"the virgins"* `[00:49:58]` — divergence.
- *"CZ's method"* `[00:51:50]` — Steve's method.
- *"quarter wood"* `[01:07:47]` — the same term V03 fixed as "quarter of wood".
- *"bibs"* `[00:03:27]` — pips.
- *"Timing Shadow Box or the Brink Spox"* `[00:13:01]`, *"the Brink Shadow"* `[00:13:40]`,
  *"in the bricks"* `[00:10:53]` — one object, the "brick(s)" / shadow box; the rendering
  is unstable and the term is never defined in this lesson (**A-038**).
- *"the 19th of trade was, thanks Joe"* `[00:04:20]`, *"a small diet"* `[00:26:59]`,
  *"not the weather how to get my dig back in there"* `[00:19:34]`-`[00:19:42]`, *"the bottle box"*
  `[00:46:10]`, *"Gaby"* `[01:10:37]`, *"smypy"* `[00:30:58]`, *"Like sense?"* `[00:40:49]`
  — unresolved garble; none is load-bearing and none is cited in any downstream artifact.
- *"shark fin"*, *"blood in the water"*, *"vector candles"*, *"stop hunt"*, *"railroad
  tracks"*, *"doji"*, *"hammer"*, *"TDI"*, *"pivots / M2 / M4"*, *"blue box"*, *"flashcard"*
  are spoken as-is and are not garble.
- Speaker labels are absent throughout — see the section above. Student questions are
  identifiable only from context and from the presenters repeating the asker's name.

**No timestamp in this file has been independently re-derived** beyond the five spot-check
windows above. Treat a timestamp as accurate to roughly a few seconds.

---
# VERBATIM TRANSCRIPT

[00:00:00]
Let's just talk about this.

[00:00:02]
Don't confuse the vector candles or the three swipes at the stop-loss, right?

[00:00:07]
The dealer vectors.

[00:00:10]
Don't confuse that with the three levels of rise or three levels of fall.

[00:00:14]
It's two totally different things.

[00:00:17]
I think the DMR guys call them pushes, call them whatever you want.

[00:00:23]
Understand that when the dealer hits the stops.

[00:00:28]
He does it in three small bursts.

[00:00:34]
Okay and that's what you have to remember.

[00:00:36]
You're looking for the three bursts.

[00:00:37]
We're going to talk about stop-on-high, the M-o-form, stop-on-low W-form.

[00:00:42]
All right.

[00:00:43]
I was driving yesterday or didn't before I saw our lose track of time.

[00:00:48]
And there's a song by 50 cents, I know, the music stuff.

[00:00:52]
It's called Candy Shop.

[00:00:54]
You guys may or may not have heard of it.

[00:00:55]
You could look it up.

[00:00:56]
I was trying to find it and edit it in time for you guys, but I had too much going on this

[00:01:00]
week.

[00:01:01]
Had a lot of emails to read.

[00:01:02]
Okay, you love the song, Greg.

[00:01:04]
Okay.

[00:01:05]
All right.

[00:01:06]
This is what came to my mind when I was driving down a road listening to the song.

[00:01:09]
It says something like, welcome to the Candy Shop.

[00:01:12]
Something, something, something.

[00:01:14]
Okay, well.

[00:01:15]
It says, welcome to the Candy Shop.

[00:01:20]
Don't trade until they hit the stops.

[00:01:22]
That's what came to my head, man.

[00:01:23]
So now you have when I move you move and now you have the Candy Shop.

[00:01:29]
Welcome to the Candy Shop.

[00:01:30]
Don't trade until they hit the stops.

[00:01:32]
Okay.

[00:01:33]
Think.

[00:01:34]
Why am I saying that?

[00:01:35]
Why did that come to my head?

[00:01:37]
When the dealer hits the stops, that's when the signal starts to set up.

[00:01:43]
Okay.

[00:01:45]
That's when he is hit or broke into psychological support or resistance level.

[00:01:53]
Think about it now.

[00:01:55]
When's the best time to trade?

[00:01:57]
When the dealer hits the stops.

[00:01:58]
That's what I've been telling you since the beginning, but it's just a different way to articulate

[00:02:02]
it.

[00:02:04]
Welcome to the Candy Shop.

[00:02:05]
When the dealer hits the stops, you're going to get paid.

[00:02:07]
You're going to pick up your candy.

[00:02:09]
I'm not going to quit my day job.

[00:02:11]
I know I'm not a good singer.

[00:02:13]
All right.

[00:02:15]
Variation on the theme.

[00:02:16]
Welcome to the trading shop.

[00:02:18]
Don't trade until they hit the stops.

[00:02:20]
Okay.

[00:02:21]
That's our song, man.

[00:02:23]
I guess when I'm done making up all these songs, I'll go into the studio and make

[00:02:26]
like a cut of all the songs and sing over them to be hilarious.

[00:02:29]
All right.

[00:02:30]
So look, think about what I'm saying now.

[00:02:34]
You take a trade because you think you see an M or W and nothing's really happened in

[00:02:37]
the market.

[00:02:38]
You take a trade inside the blue box and then it doesn't work out.

[00:02:42]
The dealer comes back and hits the stops and you're like, why didn't that trade work out?

[00:02:47]
It was a formation inside.

[00:02:51]
It was an M. It was a perfect M and happened in GJ this week.

[00:02:54]
In fact, I got several emails on it and I meant to snap shoot and shoot and put it in there.

[00:02:58]
I'll do it for next week.

[00:02:59]
Let me make a note right now.

[00:03:01]
GJ trade for next week.

[00:03:02]
All right.

[00:03:03]
But here's the point.

[00:03:04]
GJ formed a perfect M formation inside the blue box.

[00:03:08]
How many times do I have to tell you not to take shit that's inside the range of the blue

[00:03:13]
box?

[00:03:16]
But today be the last time that I tell you this because here's what happened.

[00:03:22]
The dealer made an M formation in the blue box and then he hit the stops to the high side

[00:03:27]
and made the perfect M formation and corrected a hundred plus bibs.

[00:03:34]
Several emails said, I took this M and got stopped out and I cursed you out the rest

[00:03:37]
of the day.

[00:03:38]
They didn't say that but that's what they insinuated.

[00:03:45]
Why didn't you attack back?

[00:03:48]
If the dealer takes your money away from you and issues the perfect M formation at the next

[00:03:53]
level, you hit them again.

[00:03:56]
You don't go on vacation.

[00:04:01]
Control the losses to a reasonable amount.

[00:04:03]
Do not let your equity bleed out 25, 30, 40 pips stop loss levels.

[00:04:08]
That is not what I teach you.

[00:04:11]
I teach you second leg seven to ten pips.

[00:04:20]
The 19th of trade was, thanks Joe.

[00:04:24]
Look, if your entry is here, your stop loss is right there.

[00:04:30]
Ten fifteen pips.

[00:04:36]
For a minute, if the dealer comes back and extends this level, you need to be out of the market.

[00:04:43]
Control the loss to a ten or fifteen, eighteen pips stop loss.

[00:04:47]
You are now standing aside minus eighteen.

[00:04:49]
Big deal.

[00:04:52]
Don't stand aside minus one eighty.

[00:04:56]
It's going to take you a week to make that back.

[00:04:59]
If you take minus eighteen, you're out and then the dealer does this.

[00:05:03]
Again, you got them.

[00:05:05]
Take your eighteen plus back.

[00:05:07]
Go for your fifty, you'll be net positive thirty-two for the day.

[00:05:14]
Control the losses and hit them again.

[00:05:17]
The dealer hits the level again.

[00:05:19]
Why wouldn't you hit him again?

[00:05:22]
Don't be afraid of them.

[00:05:25]
They're not that magical.

[00:05:26]
They're not that mystical.

[00:05:27]
It's not Oz.

[00:05:28]
I'm pulling the curtain back.

[00:05:29]
Hit the stops high, drop, hit the stops low, rise, trade in the range.

[00:05:33]
That's all they got.

[00:05:35]
So what happened in GJ was this.

[00:05:39]
It did this inside the box.

[00:05:41]
I'm sorry, inside the blue range.

[00:05:44]
Everyone took this trade.

[00:05:45]
That sent me an email here.

[00:05:46]
Got all excited.

[00:05:48]
It went up about twenty pips and then the dealer went just kidding and he did this.

[00:05:53]
You got stopped out here for minus whatever your minus was.

[00:05:56]
None of my business, but it should be less than twenty.

[00:05:59]
A tight stop second leg.

[00:06:03]
You should have got in right here and then this is exactly what happened.

[00:06:07]
It's kind of funny that this chart is you're and a half old.

[00:06:14]
Maybe a year old.

[00:06:16]
This is the same shit.

[00:06:17]
That's what I'm trying to tell you.

[00:06:19]
You keep writing to me and saying, Steve, is it really the simple?

[00:06:21]
Is it that easy?

[00:06:23]
And the answer is yes, it is that easy.

[00:06:28]
This is all they got.

[00:06:29]
It will show you a pattern, exploit the level, psychological support and resistance.

[00:06:34]
What's the psychological support and resistance?

[00:06:37]
In today, the Asian accumulation range.

[00:06:40]
If the dealer doesn't break above the Asian accumulation range, you don't trade.

[00:06:46]
Welcome to the candy shop.

[00:06:48]
Don't trade until he hits the friggin stops.

[00:06:51]
He just hit him over here.

[00:06:52]
Now you can trade and save the trade.

[00:06:56]
Don't send me another friggin trade.

[00:06:58]
Right now, mark it down on your calendar.

[00:07:01]
It's 809 Eastern Time on 325.

[00:07:04]
Don't send me another friggin loser that you took inside the blue box asking me why the

[00:07:09]
hell is it in work out.

[00:07:12]
I'm putting it on you now.

[00:07:14]
I'm calling you out right now.

[00:07:19]
Do not take a trade that is within the Asian range.

[00:07:24]
The Asian range is the accumulation phase.

[00:07:29]
Will trades often work out in that range?

[00:07:31]
Yes, but the probability is not in your favor.

[00:07:37]
The probability becomes in your favor when the dealer hits the stops high or low and

[00:07:43]
issues the formation that's right in front of your eyes right now.

[00:07:47]
Flash card.

[00:07:49]
Okay?

[00:07:51]
This is another example of what a flash card should look like for you.

[00:07:57]
Here what do you do?

[00:07:58]
Where's the entry somewhere in here?

[00:07:59]
Right?

[00:08:00]
Right before they shift their zone.

[00:08:01]
Anyone of these bars?

[00:08:02]
So what do you do?

[00:08:03]
Take your paint, block all this crap out.

[00:08:07]
Start asking the questions.

[00:08:08]
What's the Asian range?

[00:08:09]
27 pips.

[00:08:10]
The dealer vectors to the high.

[00:08:12]
He pulls back, hits the stops of the long holders, comes back to the level, fails to

[00:08:17]
break it.

[00:08:18]
The high structure to the high, the dealer trades off of that high in consolidation.

[00:08:23]
Slash accumulation.

[00:08:25]
The dealer is accumulating contracts for the anticipated continuation long.

[00:08:30]
Alright, is my sound okay?

[00:08:34]
It's not me right?

[00:08:35]
You guys.

[00:08:36]
Okay.

[00:08:38]
The dealer makes the M formation.

[00:08:42]
You enter on the failure to break the high of the day somewhere in here.

[00:08:49]
This is your point of control, your point of entry, your point of contact.

[00:08:53]
You take over before he shifts the zone.

[00:08:56]
When you learn to grab these on the second leg close, you're going to be in profit in

[00:09:02]
15 to 45 minutes.

[00:09:04]
Guaranteed.

[00:09:06]
Right?

[00:09:12]
Absolutely correct.

[00:09:13]
So the second leg fails to break the high.

[00:09:17]
You are guessing.

[00:09:24]
Understand?

[00:09:25]
You're guessing until the dealer locks the high or locks the low for the day after the

[00:09:29]
stop hunt.

[00:09:33]
You build confidence by taking flashcards of these activities that you know pay out.

[00:09:42]
And you match them up to your chart.

[00:09:44]
Okay.

[00:09:46]
Ideally your flashcards should look exactly like this.

[00:09:53]
This is this should be a flashcard.

[00:09:54]
Go find this.

[00:09:55]
I don't even know what it is.

[00:09:56]
It's probably a euro.

[00:09:58]
Go find this chart.

[00:09:59]
This should be a flashcard.

[00:10:00]
Why?

[00:10:01]
The dealer vectors 25 to 50 pips above the agent's psychological resistance level.

[00:10:11]
He pulls back and forms the second leg at the session open inside the shadow.

[00:10:22]
He then holds the level for 30 minutes before he shifts away 45 minutes.

[00:10:27]
He spikes back here, pulls away, pulls it 15 more minutes and then lights out, shifts

[00:10:32]
the zone away.

[00:10:34]
If the stops hit the stops, shift it away again.

[00:10:38]
Run it down.

[00:10:40]
Yes, Whitney, these are textbook.

[00:10:45]
If there was a textbook, this should be in the top five.

[00:10:49]
This should be one of your signatures.

[00:10:50]
Why?

[00:10:52]
Stop hunt zone.

[00:10:53]
It hit the stop hunt shadow in the bricks.

[00:10:56]
The timing.

[00:10:57]
Think of all the elements that are right.

[00:10:59]
If we turn this into a flashcard right now, let's look at it.

[00:11:05]
If we turn this into a flashcard, we'd block all the crap out from here.

[00:11:11]
I can't do paint inside of the slideshow.

[00:11:14]
It'll mess up my slides, so I'm just drawing.

[00:11:17]
All this other crap is gone.

[00:11:19]
TDI is not here.

[00:11:21]
That's fine.

[00:11:22]
What I want you to see is this.

[00:11:25]
27 pips range.

[00:11:27]
It actually is less than 27 pips.

[00:11:29]
Here's why.

[00:11:31]
It's a low is 27 pips, correct?

[00:11:33]
The dealer, mid-Asia, snatches the low away from traders that were in this range right

[00:11:39]
here.

[00:11:42]
He shifts it higher, right?

[00:11:44]
Then he holds the level.

[00:11:48]
This is an Essenture Consolidation Zone, which 27 divided by 2, 28 is 14, so 13 and a half.

[00:11:56]
In Essenture, you have a 13.5 trading range.

[00:12:03]
No Joe, there are two boxes I'll talk about it.

[00:12:08]
Okay, look.

[00:12:11]
Your Asian range is technically 13 pips.

[00:12:14]
The dealer extends the high above the blue tracer of these are flashcard reasons.

[00:12:20]
Look, extends the high above the blue tracer, induces traders to take long positions.

[00:12:26]
He pulls back and warrants the Fibonacci continuation.

[00:12:30]
He validates those Fibonacci levels but fails to break the high.

[00:12:34]
When all the traders turn long, the dealer is net short.

[00:12:38]
He must correct against those intentions and trade and break back below the Asian range

[00:12:48]
to jam the traders that have taken positions.

[00:12:53]
Okay, now stop on Zone, Gray Box.

[00:13:01]
Timing Shadow Box or the Brink Spox.

[00:13:03]
If the trade sets up second leg or first leg in the shadow, when the first leg forms the

[00:13:08]
high of the day, that's the perfect entry.

[00:13:17]
If you hold your chart up to your flashcard up to your screen and you see everything

[00:13:25]
from the screen hammer right here, hold on.

[00:13:32]
You see everything from this green candle on showing right there.

[00:13:37]
The dealer breaks the highest formed.

[00:13:38]
He touched the stop on Zonebox.

[00:13:40]
It's in the shadow, the Brink Shadow.

[00:13:43]
Any else agrees TDI is overextended and forms an M or some type of divergence.

[00:13:48]
That's what TDI will be doing.

[00:13:50]
It'll be outside the volatility ban.

[00:13:51]
You'll have blood in the water on the secondary line.

[00:13:53]
I can't show you TDI because it's not here.

[00:13:57]
So if you see this and all these criteria are Matt, take the trade without hesitation.

[00:14:06]
You should hold your flashcard up to the screen.

[00:14:07]
Remember that stupid picture of me?

[00:14:09]
You should hold the flashcard up to the screen and you should go, man.

[00:14:15]
That looks exactly like this flashcard that I took pictures of and blacked out and it

[00:14:22]
happens to match all the criteria that Steve laid out for me.

[00:14:26]
That's a trade.

[00:14:28]
What do you have?

[00:14:29]
You have the pattern.

[00:14:32]
You have the timing element.

[00:14:35]
You have the vectors.

[00:14:36]
You have 25 to 50 pips higher than the Asian range.

[00:14:42]
You have the averages open making an M formation with the mustard.

[00:14:47]
There's your M formation in your mustard right there.

[00:14:53]
So where are we in the world?

[00:14:58]
Do not take any more garbage trades inside the range of the blue box.

[00:15:05]
Are you going to miss some good setups?

[00:15:07]
Absolutely.

[00:15:08]
You'll see them in hindsight.

[00:15:13]
You're going to say, oh, that was a good M. I'll take it.

[00:15:15]
Are you going to stay away from those for the rest of your life?

[00:15:17]
No.

[00:15:18]
But if you're struggling, it's because you're taking everything that resembles an M or

[00:15:22]
a W without any criteria and then you're pissed off at me that it's not paying out.

[00:15:28]
I'm laying out the criteria right now.

[00:15:31]
That's why I'm here for you guys.

[00:15:33]
We're doing it together.

[00:15:34]
The criteria is this.

[00:15:39]
Unless you have a deeper understanding, of course, the criteria is this.

[00:15:43]
25 to 50 pips above and below the blue box.

[00:15:49]
M formation second leg, W formation second leg, TDI confirms blood in the water shark fin

[00:15:55]
outside the band to back in.

[00:15:56]
That's the criteria.

[00:15:57]
Simple.

[00:15:58]
Okay.

[00:15:59]
So here, just sum it up for the week.

[00:16:06]
Look at the four hour chart.

[00:16:11]
Block off the first eight hours that draw a line all the way across your chart.

[00:16:15]
Those are your psychological support and resistance levels.

[00:16:18]
Go look at these charts.

[00:16:19]
It's the homework this week.

[00:16:20]
Look at them.

[00:16:24]
The dealer has to exploit.

[00:16:28]
He has to exploit the age and range of the week.

[00:16:31]
He has to because positions are built upon that spread.

[00:16:37]
Okay.

[00:16:38]
It's like I drew the chart here.

[00:16:41]
What's going on here?

[00:16:42]
Dealer opens high to snag the traders.

[00:16:45]
Traders think long.

[00:16:47]
He corrects.

[00:16:48]
Why?

[00:16:49]
If traders are thinking long and everything signals long, technically, the deal is

[00:16:54]
the dealer has to correct against that move because he's running out of cash.

[00:17:01]
Okay.

[00:17:06]
Mark the four hour chart, draw the psychological support and resistance.

[00:17:09]
Okay.

[00:17:10]
Next week's homework is going to be if you want to start messing with it now.

[00:17:13]
Since it is Sunday, it's the draw.

[00:17:15]
No, I'm not going to tell you never mind because here's why.

[00:17:19]
We got two more nights.

[00:17:20]
We got the rest of the night tonight to teach and we got a whole nother night lined up

[00:17:23]
for you tomorrow.

[00:17:24]
And everyone is same as me as put their heart and soul into teaching and making slides.

[00:17:29]
And I don't want you guys drawing lines on your chart and taking trades and then not paying

[00:17:32]
attention.

[00:17:33]
So I'll save that assignment for next week.

[00:17:35]
Let me make a note of what I want you to do.

[00:17:38]
Okay.

[00:17:39]
Big board.

[00:17:40]
Okay.

[00:17:41]
I don't want to say too much mumbling over here.

[00:17:45]
All right.

[00:17:46]
We got 10 minutes.

[00:17:47]
Let's do some questions.

[00:17:51]
We sum up where we're at.

[00:17:55]
I want you to start looking at the four hour chart or the one hour chart, whatever makes

[00:17:59]
you happy.

[00:18:00]
But I want you to do the assignment in the four hour chart.

[00:18:04]
The four majors, any time range.

[00:18:07]
I want you to start to understand the psychological support and resistance levels that

[00:18:14]
the dealer creates in the first eight hours of the week.

[00:18:21]
Okay.

[00:18:24]
Mark the chart, try to identify the high of the week and the low of the week and trade

[00:18:28]
away from those areas.

[00:18:33]
Drill down to a 15 minute chart.

[00:18:36]
Remember many view and start to identify the pattern within the pattern.

[00:18:43]
Every one of these patterns is going to have a sub pattern.

[00:18:45]
Here's what's going to happen.

[00:18:46]
The dealer is going to wear a track to the high on Sunday or Monday.

[00:18:52]
And within that pattern on a 15 minute chart, you will see an M or W formation.

[00:18:58]
That formation will coincide with the high of the week will be the high of the day.

[00:19:04]
You understand it's all connected.

[00:19:06]
The high of the week will form as some type of high of the day on the higher time frame

[00:19:13]
or in the lower time frame, the 15 minute.

[00:19:17]
So looking at the four hour and the 15 minute, you're going to have the four hour.

[00:19:23]
Let's pretend that this is the high of the week right here.

[00:19:28]
Okay.

[00:19:29]
So let's say this is the high of the week at the same time the high of the day is

[00:19:33]
forming.

[00:19:34]
You understand the HOW and the HOD are coordinated by the dealer on purpose to not the

[00:19:42]
weather how to get my dig back in there.

[00:19:46]
All right.

[00:19:47]
The high of the week and the high of the day are going to form at the same time on the

[00:19:52]
chart.

[00:19:53]
The only difference is that one, two, three, four, one, two, three, four, one, two, three,

[00:19:58]
four, all this will be one four hour candles straight up like that.

[00:20:03]
That's how it's going to look on the four hour chart.

[00:20:05]
Surely it'll paint better than I can draw.

[00:20:07]
And it's going to look like that.

[00:20:08]
Then what you'll have is you'll see it's hard to fall off.

[00:20:12]
But on the high of the week the one four hour bar will be a railroad track type.

[00:20:18]
Okay.

[00:20:19]
Four hour bar.

[00:20:20]
On the 15 minute chart it'll make the M formation.

[00:20:24]
Which is coordinated together.

[00:20:26]
So now you got the high of the week it's set.

[00:20:28]
Now you trade away from the high of the week for two and a half to three days until the dealer

[00:20:33]
issues another signal.

[00:20:43]
Alex I'm not telling you to enter on the four hour.

[00:20:47]
I'm telling you to start to understand the bigger picture and use the 15 minute for entries.

[00:20:55]
Okay.

[00:20:55]
How do you use paint to do the candles?

[00:20:57]
Go back to the recording.

[00:20:58]
It'll be up tonight.

[00:20:59]
I showed you exactly how to do it.

[00:21:01]
Slow it down, watch it several times.

[00:21:04]
Outside structure is when the dealer creates a spike vector to the high and then trade

[00:21:12]
off that level in here with these candles.

[00:21:16]
Outside structure, high outside structure.

[00:21:17]
Let me see if I got a I'll pull a flash card up for you.

[00:21:20]
Leave that.

[00:21:24]
Okay.

[00:21:25]
Let's see what else.

[00:21:29]
Okay.

[00:21:29]
What's the best time to be at the station trading hours?

[00:21:33]
Okay.

[00:21:33]
From one to five AM New York, one to four AM New York, four or five hours.

[00:21:37]
Take a break from eight to 11 New York time.

[00:21:41]
No, that's nothing's changed, man.

[00:21:44]
You're looking for the dealer to exploit the shadow at the start of the London and to start

[00:21:48]
of the US.

[00:21:53]
When you see an AM on the four hour charge that you laid the trade.

[00:21:55]
No, Alex, if you see an AM on the four hour that's your anchor point, if you got an

[00:21:59]
AM on the four hour charge that's your peak formation high, then you're looking for

[00:22:02]
stop on high drop, stop on high drop W get out.

[00:22:06]
Right.

[00:22:06]
Tom, I will.

[00:22:11]
I'm going to do the TDI next week.

[00:22:14]
Listen, if you're confused about some things, don't forget, I left a class up.

[00:22:18]
Tonight we'll post the next day.

[00:22:19]
Am I ready to be up?

[00:22:21]
When then comes on, I'll talk to them.

[00:22:24]
Listen, I told you you have day one and two.

[00:22:28]
Every Sunday, I'm going to add to my class roster until all four days are up in the

[00:22:33]
forum.

[00:22:35]
These recordings will be left up.

[00:22:41]
You guys can look at them over and over again.

[00:22:44]
So you get it.

[00:22:45]
Do me a favor.

[00:22:46]
We're going to go at Thursday night as the homework again, but don't mail it to me.

[00:22:49]
I don't need it posted in the forum.

[00:22:52]
Okay, I'm going to try to answer all the questions and there go through it.

[00:22:54]
Listen, somebody sent me an email and actually sent it to Zen too and I was a little

[00:22:58]
offended.

[00:22:59]
They put like Steve really looks at this stuff.

[00:23:01]
Yes, Steve really does look at this stuff.

[00:23:05]
I want to help you guys.

[00:23:07]
I wouldn't have committed my Sunday suspended time with you.

[00:23:09]
And I wouldn't I wouldn't dump 10, 15 hours of slides and production all week

[00:23:13]
because I hate you.

[00:23:16]
You guys are my extended family.

[00:23:18]
I want the best for you.

[00:23:19]
I love the business.

[00:23:21]
I'm passionate about it.

[00:23:22]
That doesn't show.

[00:23:23]
I can't help you.

[00:23:26]
That's what I mean about the negativity and the things that are into your head.

[00:23:30]
You really think that I'm sitting here pulling this out 20 minutes before Sunday.

[00:23:36]
I spent all week reading the emails.

[00:23:38]
I've answered 90% of them.

[00:23:39]
A lot of you got answers.

[00:23:40]
If you didn't, you'll have an answer this week.

[00:23:42]
I'm going through every single one of them.

[00:23:45]
I want to know what's going on with you guys.

[00:23:47]
I need to take a temperature of the group.

[00:23:49]
That's why I asked you to email me.

[00:23:50]
That's why I didn't use survey monkey because I'm reading all of them.

[00:23:54]
That's why I bought monitors because most you have equipment issues.

[00:24:00]
I'm not mad.

[00:24:02]
I'm just saying, come on, man.

[00:24:03]
I'm pouring my heart out to you guys out here.

[00:24:06]
I know there should be an asshole clause in the student agreement.

[00:24:09]
I don't have that.

[00:24:10]
Maybe I should write that in.

[00:24:15]
I know that you see me here two hours, but I promise you, it takes hours and hours to.

[00:24:19]
I got a right to rough draft.

[00:24:21]
I got to rehearse it.

[00:24:21]
Make sure it's enough time.

[00:24:22]
Get my words.

[00:24:23]
Heidi's got to convert my notes into a slideshow.

[00:24:27]
Don't forget, I got a newborn baby two and a half weeks old.

[00:24:30]
man, I'm doing everything I can.

[00:24:32]
I want you guys to get it and I appreciate all the nice emails.

[00:24:35]
But the negativity is, it's got to stop.

[00:24:38]
It's retarded.

[00:24:39]
It's crippling you.

[00:24:41]
Just open your mind like I asked you and give me a good solid two hours and put

[00:24:46]
all the negativity out of your mind and don't say negative things.

[00:24:50]
Be positive.

[00:24:51]
That's all I want for you.

[00:24:52]
We got to want you to be positive for two hours a week.

[00:25:00]
Okay, it is any more questions.

[00:25:03]
Thanks for all the positive stuff you guys are right now.

[00:25:05]
I really appreciate it.

[00:25:06]
I think you guys write to me, it's not you guys, but sometimes you forget,

[00:25:10]
I'm a person I have feelings man.

[00:25:11]
You say shit.

[00:25:13]
And it, you know what, that stuff cuts man.

[00:25:16]
I'm human.

[00:25:18]
I want to keep the negativity out of the business.

[00:25:20]
I want you to understand.

[00:25:23]
The comfort is in our group.

[00:25:24]
I've said it a hundred times.

[00:25:25]
You cannot go and tell somebody that you can pick the high and low and the

[00:25:29]
reversal point in the business.

[00:25:31]
They will tell you that you are a berserk crazy.

[00:25:34]
You need to be in a straight jacket.

[00:25:36]
I've heard it all my trading career.

[00:25:40]
And let me say this, the joke is on them.

[00:25:43]
You can pick the tops and bottoms in any market condition when you

[00:25:47]
understand the dealer's behavior.

[00:25:49]
And that's what we're working on together as a group.

[00:25:52]
No, I just want to thank everybody for being here.

[00:25:54]
I will be back next Sunday and we'll continue going far.

[00:25:57]
We're going to, we're getting through the class on a very slow pace.

[00:26:01]
You're doing the homework.

[00:26:02]
Things should start to be jelling in your mind coming together.

[00:26:05]
Okay.

[00:26:05]
So you're looking at right now, we're looking at the broad spectrum.

[00:26:09]
We're looking at the four hour chart on the bigger picture, understanding the

[00:26:13]
psychological support and resistance levels.

[00:26:15]
We're going to work on the trading zone.

[00:26:19]
We're going to start talking about the 22, 33 trades, multi session M and

[00:26:23]
W's.

[00:26:24]
Okay.

[00:26:25]
That's what's coming up.

[00:26:26]
So here's what I'm going to do.

[00:26:27]
As soon as I get off here, I'm going to go post the homework assignment in the

[00:26:31]
forum under my boot camp thread.

[00:26:34]
And then I want you to go ahead work your charts and post them in there.

[00:26:40]
I'll look through them, see where we're at.

[00:26:41]
I'll post my answer key.

[00:26:44]
Wanted to mark up.

[00:26:45]
I'm going to do the same thing.

[00:26:46]
I'll post the answer key in my section.

[00:26:48]
Compare your charts to that.

[00:26:51]
If you are lost, send me an email.

[00:26:53]
If you just don't see it in your blinds, I mean email.

[00:26:56]
If you do, no need to send me an email.

[00:26:59]
So I wanted to cover some of the timeframes for a small diet.

[00:27:02]
I would not trade on Mondays.

[00:27:04]
Now there's a lot of people that ask, well, why don't you trade?

[00:27:07]
There's a couple of reasons.

[00:27:09]
One, I used to trade every day of the week.

[00:27:11]
And when I traded on Mondays, now this was just my own findings.

[00:27:14]
I logged my own trades.

[00:27:16]
This has nothing to do with anything other than I'm telling you.

[00:27:19]
My own experience, for me personally, it seemed to me that I was only

[00:27:23]
catching a solid trade about every third week.

[00:27:26]
And so it just wasn't worth it for me to sit there.

[00:27:31]
For that timeframe and not be able to catch a good trade.

[00:27:35]
Now in addition to that, my wife and I love to spend time together.

[00:27:41]
So what a perfect day.

[00:27:42]
The kids are at school.

[00:27:43]
The market's kind of funky.

[00:27:45]
So we thought, you know what?

[00:27:46]
We're going to take Mondays off plus we like to go.

[00:27:49]
Most of you guys know that we live most of the time here in Orlando, Florida.

[00:27:52]
And we like to go to Disney.

[00:27:54]
And hang out and go eat it at all the different places there and stuff.

[00:27:58]
And so Mondays are fantastic days to go to Disney.

[00:28:01]
So that's part of the reason that we just, you know, the market wasn't

[00:28:05]
accommodating to my style, it's raining for one.

[00:28:07]
And I wanted some time after in the week to spend with Diana.

[00:28:10]
So we trade Tuesday, Wednesday, Thursday, Friday.

[00:28:14]
I don't trade nonform.

[00:28:16]
Do I know how to?

[00:28:18]
Could I do it? Sure.

[00:28:19]
But you know what?

[00:28:20]
Why would I want it?

[00:28:22]
You know, if I can take the day off and go spend it with my wife and go to the parks and hang out,

[00:28:26]
I don't need to mess with all the news.

[00:28:28]
It's just, it's no fun for me.

[00:28:30]
So we trade Tuesday, Wednesday, Thursday, and most Fridays.

[00:28:33]
And I start about 815 or so in the morning.

[00:28:37]
And the school that our kids go to is a block away from our house.

[00:28:41]
So we walk the kids to the school.

[00:28:43]
We come back.

[00:28:44]
And it's usually about 815.

[00:28:46]
And that's when we jump into the saddle and get busy.

[00:28:49]
Typically speaking, I'm done around 11 o'clock.

[00:28:53]
Now have I traded later than that?

[00:28:55]
Sure. If I'm in a trade in the set up happens at 10 30 or something,

[00:28:58]
I'm going to stick with it until, you know, I'm done with it.

[00:29:02]
But other times, you know, if there's nothing I like,

[00:29:05]
usually by 10 o'clock, I'm done.

[00:29:07]
You know, if it's not a signature trade or something that I really like,

[00:29:12]
I'm just going to pass on.

[00:29:14]
Okay.

[00:29:15]
So I wanted to share that with you.

[00:29:19]
Now let's go ahead and take a look here at,

[00:29:28]
a lot of you people have asked about, you know, what the screens should look like.

[00:29:32]
I'm just going to show you what mine looked like.

[00:29:34]
Here's what I look at.

[00:29:37]
Originally up until about six or eight weeks ago, I checked down 21 pairs.

[00:29:43]
I checked down 21 pairs because I was really hungry for opportunity.

[00:29:46]
And what I did, and for about 20 months or so,

[00:29:49]
or 22 months, have a long it was, I looked at the same 21 pairs.

[00:29:54]
And then I realized about six weeks ago,

[00:29:57]
because Diane traced quite a few pairs less than I did,

[00:30:01]
and so this was my son, Ken.

[00:30:03]
And I realized that, you know what?

[00:30:05]
I've got all these pairs, and a lot of them,

[00:30:07]
I don't think I really even trade much.

[00:30:09]
So I went through my trade journal and figured out that there was,

[00:30:14]
there was like nine of them that I had maybe taken one trade or had never even traded.

[00:30:18]
So I thought, why in the world am I wasting my time looking at these?

[00:30:22]
So I paired it down about six weeks ago to just 12 pairs.

[00:30:27]
And you know what the funny thing was,

[00:30:29]
if your student folder Steve gives you nine pairs to trade.

[00:30:34]
I had those nine pairs, and I added AJ,

[00:30:38]
I added EG, because I use EG for fractional disparity.

[00:30:43]
And then I added EC.

[00:30:45]
Now most people hate the Euro Swiss.

[00:30:48]
They just hate it.

[00:30:49]
But I've grown to love that guy, because you know what?

[00:30:52]
He's lazy and lays around forever,

[00:30:54]
but if you catch him at the right time,

[00:30:56]
the guy just takes off.

[00:30:58]
And so I've been very good at smypy, this guy, EC.

[00:31:03]
So anyway, I've paired it down to 12,

[00:31:04]
but here's what my charts look like.

[00:31:06]
You can see up here in the upper left hand corner,

[00:31:08]
I've alphabetized every single pair that I like to use or like to look at.

[00:31:13]
And now some of these pairs, I don't necessarily have them on my profiles,

[00:31:18]
but I still like to glance at them just in case there's a good setup.

[00:31:21]
I don't want to miss anything, you know?

[00:31:23]
So I have the hourly on top,

[00:31:26]
and then I have my 15 minutes on the bottom.

[00:31:30]
And I simply go through these charts,

[00:31:33]
I have four, 28 inch monitors like Steve does,

[00:31:37]
and I set them all up at once.

[00:31:39]
And then I, so each monitor is looking at the same setup that we have right here.

[00:31:44]
And then first, I look here,

[00:31:46]
and then I look down here,

[00:31:47]
and I'll cover a little bit more in depth exactly specifically how I do it here in just a couple of minutes.

[00:31:53]
So this is what my check down screens look like the hourly over the 15 minute.

[00:32:01]
And then here's what my trade view looks like.

[00:32:06]
And sometimes I got two pairs, so if I'm liking them,

[00:32:09]
and other times, you know, I'll expand one side on just have one pair,

[00:32:13]
because if I'm normally it seems like I ended with three or four pairs,

[00:32:17]
that I'm following to potentially trade that.

[00:32:21]
And since I have four screens, it's usually I have one up on each.

[00:32:25]
Sometimes if I got five or six, then I'll double up a screen like you see right here.

[00:32:29]
And I'm just waiting for the correct setup.

[00:32:34]
Now, Rob's asking a quick question.

[00:32:37]
He's asking how I use,

[00:32:39]
yes, I have one computer that accommodates four or 28 inch screens.

[00:32:44]
You know, that's just something you're going to have to get with a computer guy to do.

[00:32:48]
But there's a card that you could buy if you computer's fast enough that you can accommodate this.

[00:32:53]
If you'd like, or you can split it with two computers, two screens, it's up to you.

[00:32:57]
But if you go, you know, Google, trade computers or something like that,

[00:33:01]
you'll be able to figure it out from there.

[00:33:05]
Okay, so on my check down screen, I've even simplified it more.

[00:33:09]
I had something a little bit more complicated,

[00:33:11]
but more recently, about six weeks ago, I've really,

[00:33:14]
just tried to make my life as easy as possible.

[00:33:18]
And so if you see here on the left hand side,

[00:33:21]
these are the pairs that I'm looking at.

[00:33:26]
And then here's my notes. I'm trying to find what level it's at.

[00:33:30]
And generally what I'll do, because I don't have the, you know,

[00:33:34]
a bionic memory, I have to write down what direction, just so I can memorize.

[00:33:38]
And then over here, I'm going to write my notes of what the confluence is.

[00:33:41]
What's happening? What are my signals?

[00:33:43]
Why would I want to take this trade?

[00:33:46]
And why did I trade it? Because I can't log every trade I take.

[00:33:53]
Okay, so here's the questions. Everyone's saying, hey, what questions do you ask?

[00:33:57]
So here's what's going through my mind before I take a trade,

[00:34:01]
when I sit down at the terminal.

[00:34:03]
Okay, so the first thing I want to know is where we're at in the cycle.

[00:34:13]
And this backs up. Steve, I mean, just nailed it on the head with the four-hour.

[00:34:18]
You can look at it and draw things out on the four-hour, like Steve had talked about.

[00:34:23]
I happen to do it on the one hour, because that's the way I learned to do it.

[00:34:27]
So I like to find out where am I at, is it if we had a couple days of correction?

[00:34:32]
Or, you know, exactly where am I at, so I know what the next moves are.

[00:34:36]
So here's what I'm asking. Okay, has there been three levels of rise or correction or where am I at?

[00:34:41]
Has it risen maybe one day or two days or has it corrected one or two days?

[00:34:45]
Where exactly am I at? Because I don't know where I'm at.

[00:34:48]
How am I going to make a safe trade and meet these guys, right?

[00:34:50]
If I'm discussing, I'm going to get what?

[00:34:53]
The next question I'm asking myself are what are the anticipated moves for this week?

[00:34:58]
And I know that car and the DMR gang drills this in.

[00:35:03]
You write it down on your charts. When you're marking up your charts, you know,

[00:35:07]
I have one particular screen that I use that I just mark up my charts and it goes back,

[00:35:12]
a week after week after week. And I pencil in the levels.

[00:35:17]
And then I use the chart and I use some of the tools and I write where I think the next moves are going to be.

[00:35:22]
And those are the anticipated moves that I'm waiting for to happen so that I can make the trade.

[00:35:30]
Next question I'm asking myself are we at or near a midweek reversal? Again, I need to know where I'm at.

[00:35:38]
And this is another question that I asked myself, who has behaved in the London session? Who's behaved?

[00:35:44]
Now what do I mean by that? I am specifically looking for the pairs that follow what's happening.

[00:35:51]
That follow what Steve teaches me. The pairs that have risen for six days? Guess what? They have not behaved.

[00:35:59]
I kick them to the side. I don't want to trade them because they're not playing by the rules.

[00:36:05]
It's my playground. It's my football. You're going to play by my rules or I'm not playing with you.

[00:36:10]
That's what I mean by this. They're not behaved. If they've dropped two days and then resetting one up three or four days,

[00:36:16]
guess what? They're not playing by the rules. So therefore I do not want to deal with them.

[00:36:28]
Next, here's what I'm looking for. Has it presented its pattern that Steve teaches? Has there been three swipes? False move? Have they tracked the people? Was there a long sustained move or one?

[00:36:43]
Was the ADR met? If the pair says or you've acknowledged and known how long it's ADR is or understand it,

[00:36:55]
if it normally runs 110 pips and it's sitting at 80 but you're getting a signal, am I going to take that trade?

[00:37:01]
Normally I do not because it hasn't fully met all the parameters for me to take the trade.

[00:37:09]
The next question that I'm asking is what confluence is our present to justify my entry.

[00:37:15]
We're going to cover that here because I've got about 30 charts here that I want to show you.

[00:37:19]
There's some recent trades over the last three or four weeks that I've taken.

[00:37:23]
Again, if they haven't followed the rules and by the rules,

[00:37:28]
I mean if they haven't behaved like Steve teaches us, which is this information here.

[00:37:33]
And there's more to it but this is kind of a foundation of it.

[00:37:37]
If it's not doing this stuff here, I don't personally don't want to trade it.

[00:37:43]
Okay, now let me back up. Somebody's asking me and I'll answer a couple of these questions before we go into the setups.

[00:37:53]
Has to me to explain what is on each of my four monitors is one or more demo accounts.

[00:38:00]
I do not use a demo account.

[00:38:02]
Everyone in my accounts are live.

[00:38:05]
And this is exactly right here if what I'm looking at,

[00:38:12]
everyone of my monitors has that exact setup.

[00:38:15]
Every one of them.

[00:38:19]
And so I have 12 pairs that I look at.

[00:38:23]
If you take this screenshot here, you can stretch it over four screens.

[00:38:26]
That's exactly where I'm at when I'm looking at.

[00:38:29]
Occasionally, I'm in the DMRs but not a whole lot.

[00:38:34]
To be honest with you, car, camera, H.M., they do a fantastic job.

[00:38:39]
And there's no reason it all for me to be there.

[00:38:43]
Okay, James, I have one station.

[00:38:47]
Okay, Steven's asking, how do I basically run four copies of my platform or my broker?

[00:38:58]
I'm sorry. All you need to do, and I know that this is out there in the forum,

[00:39:04]
but you're just going to change the location of the folder that you copy the first one into.

[00:39:10]
Maybe the first one we're going to program A or whatever.

[00:39:15]
And then it asks for the next one.

[00:39:17]
You just change them to two, three, four, etc.

[00:39:19]
And then you'll be able to have three or four icons on your desktop.

[00:39:23]
And then you open up each one to each window.

[00:39:29]
Okay, so let's go ahead and move a little bit forward here.

[00:39:35]
So this is my macro check down right here.

[00:39:37]
These are the pairs.

[00:39:38]
And I'm going to take notes on this.

[00:39:40]
And I'm going to write, hey, the OSC Swiss is at level three.

[00:39:43]
I'm looking for it to go up.

[00:39:47]
So I'll draw an arrow with it up.

[00:39:49]
And maybe I'll notice that on H1, it's forming a W.

[00:39:53]
And on M15, it's forming a W.

[00:39:55]
That's going to cue me into looking at that.

[00:39:57]
Maybe I'll put an asterisk as it, because I think it's one of my best opportunities for the day.

[00:40:05]
We talked about this.

[00:40:06]
And then here's some of the stuff I'm looking for once I actually have put it onto the trade screen.

[00:40:12]
I'm looking at TDI, I'm looking for a shark fin.

[00:40:14]
Looking for a stop hunt.

[00:40:15]
Some of the market maker candles, divergence, what pivot it's at,

[00:40:20]
ADR, the high of the day, or low of the day from yesterday.

[00:40:25]
Now, let me just back up for a second.

[00:40:28]
If you don't understand this term and I want you to hear that I'm talking about,

[00:40:32]
then you need to go back to the recordings.

[00:40:35]
Because Steve teaches every bit of this in depth.

[00:40:38]
If you don't understand it, I can't help you right now.

[00:40:42]
I'm two steps ahead of you.

[00:40:44]
You've got to understand the foundation of this before you're going to get any more.

[00:40:49]
Like sense?

[00:40:58]
Okay, so what I wanted to do, what I thought would be best, is just try to teach you some of the setups that I look for.

[00:41:04]
So, here we go.

[00:41:11]
This is a trade that I took on Friday.

[00:41:14]
You can see right here.

[00:41:16]
Now, what was my clue to the entry on this one there?

[00:41:22]
I look at a lot of different things.

[00:41:24]
Obviously, I want the most confidence of event to give me the absolute best probability of winning.

[00:41:33]
But let me back up for a second.

[00:41:35]
A lot of people you have asked lots of questions to me.

[00:41:37]
And my wife can attest to this,

[00:41:39]
Jane and my son who trades with me.

[00:41:41]
Actually, we can attest to this.

[00:41:43]
Steve can attest to this.

[00:41:44]
I've had six losing days in the last ten months.

[00:41:47]
That's it.

[00:41:48]
Some people say that's incredible.

[00:41:50]
I'm pretty proud of that, but let me tell you, I learned it from Steve.

[00:41:53]
It's nothing that I did.

[00:41:55]
I simply listened to what Steve said.

[00:41:58]
And I paid attention to it.

[00:42:00]
And I just don't lose.

[00:42:04]
I hate freaking losing.

[00:42:06]
I'm a coach.

[00:42:07]
I was an athlete growing up.

[00:42:09]
And I absolutely hate to lose.

[00:42:11]
So, just like Les Brown says, it's not over until I win.

[00:42:14]
And that's how I feel.

[00:42:15]
But I'm not stupid about it.

[00:42:17]
And I'm going to show you a couple of trades here and show you how

[00:42:20]
if you want to increase your probability of wins,

[00:42:23]
you've got to stay in the game.

[00:42:25]
And again, guys, every single thing that I know about trading,

[00:42:29]
I learned from Steve.

[00:42:31]
I've been very fortunate and blessed.

[00:42:33]
I've not listened to one other person.

[00:42:35]
I've not had another coach.

[00:42:36]
He has been it for me.

[00:42:38]
So, some of you say it's blessing.

[00:42:40]
Some might think it's a curse, but I'm grateful to the guy.

[00:42:43]
I have taken everything that he has said.

[00:42:46]
I've got stacks of notes.

[00:42:48]
And I mean, just hundreds of pages of stuff,

[00:42:51]
because this was all three years ago.

[00:42:53]
I didn't know any of this.

[00:42:54]
I didn't know what a pit was.

[00:42:55]
I didn't.

[00:42:56]
I truly didn't know any of this.

[00:42:58]
And now, I'm absolutely fluent in it.

[00:43:03]
But anyway, so let's take a look at this.

[00:43:05]
So what I did was here, I watched what it did.

[00:43:08]
You can see that it gave a reversal signal here.

[00:43:11]
It came down.

[00:43:12]
But my entry, normally, I'm pretty good about the entry.

[00:43:16]
It's not a lot of times I jump up early.

[00:43:18]
And on this one, I actually took it here and wrote it up

[00:43:22]
and then it came back down.

[00:43:23]
It almost stopped me out.

[00:43:25]
And then it just took off.

[00:43:28]
But there was actually two opportunities here

[00:43:31]
in the US session for this trade.

[00:43:33]
One was here because it was a retest here of the low.

[00:43:37]
You can see, see teaches us about the pivots, right?

[00:43:41]
M2 and two generally goes to M4.

[00:43:43]
Look at exactly what it did.

[00:43:45]
It came down and kissed the ADR low right here, right?

[00:43:48]
Everybody see that?

[00:43:51]
It hit M2.

[00:43:53]
It came all the way up to past M4.

[00:43:56]
It came up here to the ADR high.

[00:43:58]
We also, you can see right here.

[00:44:01]
There's a confluence here.

[00:44:02]
There's an ugly looking W.

[00:44:04]
Maybe a preschool W right here.

[00:44:06]
So there was a handful of things that led me to believe

[00:44:09]
that this would be a betrayed for me.

[00:44:17]
Okay.

[00:44:18]
So I have somebody asking about the work time ribbon.

[00:44:21]
Don't even worry about my work time ribbon.

[00:44:23]
I've had the same one for a few years.

[00:44:25]
I'm not going to change it.

[00:44:26]
I understand it.

[00:44:27]
I'm sorry if it doesn't line up with yours.

[00:44:29]
But I leave mine the same.

[00:44:31]
Just like Steve, I've never touched it.

[00:44:33]
I set it up one time and I've left it.

[00:44:35]
So if you need something more accurate than this,

[00:44:38]
really all these boxes, the shadow boxes,

[00:44:41]
all the stuff they really don't matter, guys.

[00:44:43]
They just really do not matter.

[00:44:45]
Once you understand what's going on,

[00:44:47]
if you took all the stuff off there,

[00:44:48]
you would see the same thing.

[00:44:50]
Okay.

[00:44:51]
I'm getting that question here from Chris.

[00:44:55]
Chris is asking me, do I scale it to my trace?

[00:44:58]
No.

[00:44:59]
And here's why.

[00:45:00]
In the US session, you don't get the long sustained runs.

[00:45:04]
When I traded the London session,

[00:45:06]
and we'd get 800,1200 pips, yeah, you scale it.

[00:45:10]
Because you have a long sustained run,

[00:45:12]
somewhere between 70 and say 150 pips.

[00:45:16]
In the US session, I am happy to take profit at 35 to 50 pips.

[00:45:20]
Most of the time, it's around 40, 45 pips for me.

[00:45:23]
So I go in heavy.

[00:45:25]
I don't go in with a foot soldier.

[00:45:27]
I don't go in light and then add on to it.

[00:45:30]
I go in heavy.

[00:45:31]
Either I'm right or either I'm wrong.

[00:45:33]
And most of the time, I'm right now.

[00:45:35]
And if I'm wrong, Steve has taught me how to win.

[00:45:39]
I let it reset.

[00:45:41]
I let it go ahead and reveal the pattern.

[00:45:44]
And then I jump back in, go a little bit heavier than my initial entry.

[00:45:49]
And I win it back and then more.

[00:45:52]
Okay, so let's look at another setup here.

[00:45:55]
Okay, here's another setup.

[00:45:57]
This is a perfect London setup here.

[00:45:59]
You got one, two, three swipes to the high.

[00:46:01]
Right?

[00:46:02]
This is a perfect London trade here.

[00:46:04]
We get a reversal signal right here.

[00:46:06]
And it just drops all the way down.

[00:46:09]
So what happened here?

[00:46:10]
This is the bottle box for the US session.

[00:46:13]
It kind of rose up and it came back down.

[00:46:15]
And basically it gave me a retest right here.

[00:46:17]
I was all over this man, all over it.

[00:46:19]
And typically for me, and this is just me, my take profits

[00:46:24]
are at the water, generally at the water.

[00:46:27]
And it's usually three or four or five pips below the water in most cases.

[00:46:32]
Because a lot of times in the past, I put it right at the water.

[00:46:35]
And it would come one or two pips away from the water.

[00:46:39]
And then it would continue to move.

[00:46:41]
And I'd be up 44 pips.

[00:46:43]
And at the end of a 10 or 15, because I got green in one of my 15s

[00:46:47]
and then settled for my 46.

[00:46:51]
So again, this bottomed out here, the trade was right back to the water for me.

[00:46:57]
A lot of times, the second point would be right here, which would be the mail.

[00:47:03]
Or you can just buy it by your position.

[00:47:06]
I mean, by your take profit.

[00:47:09]
For me, again, US session, 35 to 50 pips, I'm happy.

[00:47:13]
You do that two or three times a day, three or four days a week, you know,

[00:47:17]
4,500 pips a week, going in with a pretty large position size.

[00:47:22]
And guess what?

[00:47:23]
It's a great way to live.

[00:47:26]
Okay, so let's take a look at this trade here.

[00:47:28]
Here's another trade that I took.

[00:47:30]
This one was on the AC dollar.

[00:47:32]
Can't remember what day this was.

[00:47:33]
I think this was last week.

[00:47:35]
And you can see that it came out of the box here, right?

[00:47:38]
It gave us a tiny railroad track here off the mail.

[00:47:42]
And then came all the way down.

[00:47:44]
You can see that my entry was right here.

[00:47:47]
This opaloss was below here.

[00:47:50]
For me, I do seven pips plus the spread.

[00:47:57]
So on this case, it might have been 13, 14 pips.

[00:48:02]
My take profit was up here, but you can see what happened here.

[00:48:05]
I think I only ended up with like 30 pips or so, 25, 30 pips.

[00:48:08]
I got out right here because after a couple of hours it was just consolidated.

[00:48:12]
So anyways, I didn't want to hang out all day.

[00:48:14]
So I should have laughed.

[00:48:20]
Let's take a look at the next trade here.

[00:48:25]
This was on the 20th.

[00:48:27]
Okay, this was on the 20th again.

[00:48:29]
This is sort of an ugly trade.

[00:48:32]
I didn't go real heavy on this one because I didn't really like it.

[00:48:36]
But I did trade it and I did do pretty well on it.

[00:48:40]
And you can see right here it came out of the session here.

[00:48:43]
It came all the way down.

[00:48:44]
We got a reversal sign here.

[00:48:46]
Also got a shark fin here.

[00:48:47]
It was not out of the water, but it wasn't shark fin.

[00:48:50]
And the clue for me was these pins.

[00:48:53]
It's the second time it pinned the mail here.

[00:48:55]
The reverse off of here came back, repeated itself here.

[00:48:58]
I knew it was going to rise.

[00:49:00]
So I took it up here.

[00:49:02]
I think this was 45 pips or so.

[00:49:07]
Okay, some people are asking what this is.

[00:49:12]
This is an old tool that we had in the forum.

[00:49:15]
I do not believe it's available anymore.

[00:49:19]
But we have a fantastic again.

[00:49:21]
For me guys, I don't like to change myself.

[00:49:24]
I like to leave it alone because I've been using the same thing over and over.

[00:49:28]
I don't care about the newest latest, greatest tools.

[00:49:32]
I'm happy and successful using what I have.

[00:49:35]
Okay, so here's one that I got beat on, but not really.

[00:49:46]
On this particular trade here, you can see one, two, three, four times.

[00:49:51]
It came up against the mail here.

[00:49:54]
You see four times.

[00:49:56]
So I anticipated it going short here.

[00:49:58]
There was the virgins.

[00:49:59]
This was dropping.

[00:50:00]
This was rising.

[00:50:01]
I took this trade.

[00:50:02]
It came down right, right actually to the water.

[00:50:05]
And I think I was up about 22 or 23 pips.

[00:50:09]
And then I just took off on me.

[00:50:11]
Luckily, when I'm up more than 20 pips, I generally move my stop-offs to break even.

[00:50:18]
And I ended up scratching out with about five or six pips on this.

[00:50:22]
So I didn't lose any money, but I didn't really make any money.

[00:50:25]
And on this particular trade, it wasn't anomaly.

[00:50:29]
I'm not really sure exactly what happened with it.

[00:50:32]
It just decided, well, actually I know what happened.

[00:50:34]
There was a bunch of money set up here and they had to go after it.

[00:50:40]
This pair was the Euro.

[00:50:42]
You can see it up here.

[00:50:43]
This was the Euro.

[00:50:52]
Okay, and here's another trade.

[00:50:58]
You can see sort of an ugly London session here.

[00:51:05]
I actually took this trade from here down to here.

[00:51:08]
Tooked up some pips.

[00:51:10]
I didn't actually go as far as I wanted it to.

[00:51:13]
And I ended up scratching out of it here.

[00:51:15]
Just so you guys know, I'm not a perfect trader.

[00:51:18]
I don't win every single trade I've ever taken.

[00:51:21]
I don't think anybody does.

[00:51:23]
But what I've learned from Steve is to protect the equity that we have in our account.

[00:51:28]
And when I was up 15 or 16, I moved my stop loss to break even.

[00:51:32]
And this retraced on me.

[00:51:33]
So I didn't really make money, but I lose money.

[00:51:43]
Now here's another trade.

[00:51:45]
And here's kind of something that will come with time, I guess,

[00:51:50]
when you studied CZ's method.

[00:51:53]
You're able to understand what the market cycle is at all times of the day.

[00:51:58]
And I knew on this particular trade this was the 15.

[00:52:02]
So I think it was two weeks ago.

[00:52:04]
It had bottomed out three times.

[00:52:05]
I was actually in the office here answering a bunch of emails.

[00:52:08]
And so I took this trade.

[00:52:09]
I saw a bottom out right here, bottomed out again.

[00:52:12]
I took it right here, wrote it up here for 50 pips.

[00:52:17]
This is the trade I just talked to you about.

[00:52:19]
So this was a scratch, but earlier that day, you know,

[00:52:22]
there's 50 pips made.

[00:52:24]
Yeah, I think this is a better view of it.

[00:52:27]
I took it here, actually, to the right here, right at the water.

[00:52:39]
Okay. And again, here's another trade.

[00:52:42]
This was from earlier in the month.

[00:52:45]
And again, I'm looking for the 80 R to be met.

[00:52:49]
You can see this one at bottomed out here.

[00:52:53]
Major shark fin down here.

[00:52:56]
I mean, look at this level.

[00:52:58]
Here's the 32.

[00:52:59]
This was down at like 22 or 23.

[00:53:01]
Remember what you said tonight about it?

[00:53:03]
If it's way overbought or way oversold, that's a huge indicator.

[00:53:09]
This one.

[00:53:12]
Here was the day low.

[00:53:15]
They exceeded that.

[00:53:17]
It was below the 80 R low.

[00:53:19]
Easy trade, man.

[00:53:25]
The date on that was March the 13th.

[00:53:28]
Fred.

[00:53:34]
Okay.

[00:53:35]
People are asking about scripts.

[00:53:36]
Yes, I do use the scripts that Steve provided.

[00:53:39]
Yes, we do.

[00:53:41]
It's today.

[00:53:43]
It's the easiest, fastest, execution that I've seen.

[00:53:46]
There are a few other things being developed right now that are out there,

[00:53:50]
but definitely what we have works very well.

[00:53:53]
So I'm going to pause for just a minute.

[00:53:55]
I have a half-volt, maybe another 10 slides or so.

[00:53:59]
But I want to address some of these questions that are coming up.

[00:54:02]
Let's see here.

[00:54:04]
Jayne is asking about second leg.

[00:54:07]
Ian, I do take second leg trades, but in the US session,

[00:54:11]
generally I would say more than 50% of the time.

[00:54:14]
It's a retracement, and then it continues the move.

[00:54:17]
So not all trades that are taken in the US session,

[00:54:20]
you're going to get a second leg.

[00:54:22]
And this is something that you're going to have to understand.

[00:54:24]
The pair of know the pair.

[00:54:25]
Like Steve said, go back and make your flashcards,

[00:54:28]
and you're going to see the behavior of each pair, for instance,

[00:54:33]
with the dollar cad, probably 70% of the time,

[00:54:37]
you're going to get that second leg

[00:54:39]
and the US session from the dollar cad.

[00:54:41]
You don't see that a whole lot with the Euro,

[00:54:44]
but with the dollar cad you do.

[00:54:45]
And that's just going to come from trading that particular pair

[00:54:48]
over and over and over and over and learning and watching it.

[00:54:51]
Okay, again, so we're coming out of the box here, right?

[00:54:55]
Now, is there reason for entry here?

[00:54:58]
This is a little bit older.

[00:54:59]
This is coming from last year.

[00:55:00]
Some of the charts that I did for the last class.

[00:55:13]
When I'm looking at here,

[00:55:14]
exactly how it's got it.

[00:55:15]
There's three hits to the bottom, right?

[00:55:17]
We got a hit here.

[00:55:19]
We got one here.

[00:55:20]
We got another one here.

[00:55:21]
So where's my take profit with this?

[00:55:23]
Remember, it can be either pip-based

[00:55:30]
or it can be somewhere like here or here,

[00:55:35]
the water, mail, whatever.

[00:55:37]
For me, if what we've learned,

[00:55:39]
yeah, it's my first targets right here.

[00:55:41]
Just shy of the water.

[00:55:46]
Yeah, Steve's seeing the mail.

[00:55:49]
He had the mail's up there.

[00:55:50]
That's going to be a long run.

[00:55:51]
That's a long way away.

[00:55:52]
Again, in the US session, what I found is

[00:55:55]
that you're going to end up getting someone

[00:55:57]
between 35 and 50 pips.

[00:55:58]
You're not going to get 100 pips out of the US session.

[00:56:00]
At least I can.

[00:56:01]
Maybe someone can.

[00:56:02]
But, yeah, Diana's here, baby.

[00:56:06]
Diana's here with me now.

[00:56:08]
She says, tell everybody hello.

[00:56:09]
There are occasions where you're going to get 100 pips

[00:56:12]
out of the US session, but oftentimes,

[00:56:15]
35 to 50 pips.

[00:56:22]
Brian's asking, can you use the scale in indicated?

[00:56:27]
Brian, I do not scale in in the US session.

[00:56:30]
The time I'm only here for, we're here for, you know,

[00:56:34]
two to three hours.

[00:56:35]
It's not a long sustained run.

[00:56:37]
35 to 50 pips.

[00:56:39]
So really, there's no reason to scale in.

[00:56:41]
We go a little bit heavier.

[00:56:43]
But, Charles, look like Christmas.

[00:56:44]
Okay, let's look at a few more here.

[00:56:49]
Again, some of the stuff we were messing with, you know,

[00:56:53]
some of the scripts, try to see what we can do to make it easier

[00:56:55]
for you guys.

[00:56:56]
Here's another fantastic setup here.

[00:56:58]
Okay?

[00:56:59]
Actually, for the London session, one, two, three swipes

[00:57:04]
to the high, right?

[00:57:05]
There's some vector candles here.

[00:57:07]
Made a beautiful lamb.

[00:57:08]
Came all the way down.

[00:57:10]
Touch the blueberry, right?

[00:57:12]
So, may I answer you here for us, you guys, as right here.

[00:57:15]
Right?

[00:57:16]
Now, I have just a quick question for you.

[00:57:19]
And this is, this is, you know, not intended to hurt anybody

[00:57:24]
especially my buddy Steve, because I know he likes to stay on up late.

[00:57:27]
But, you could be a whole night, say from here,

[00:57:30]
watching to go up, down, back up, and then finally coming down, right?

[00:57:35]
And that's, that's six to eight, that's six to eight hours there, right?

[00:57:39]
Or you could simply just spend two or three hours jumping right here

[00:57:43]
and write it up.

[00:57:45]
What makes more sense?

[00:57:47]
To me, to me, this makes more sense.

[00:57:51]
Now, they're asking the date on this.

[00:57:53]
This is September 13th.

[00:57:54]
This is an old chart.

[00:58:01]
Here we go again.

[00:58:02]
Here's another prime example, guys.

[00:58:04]
Prime example.

[00:58:06]
Beautiful U.S. trade right here.

[00:58:08]
I'm sorry.

[00:58:09]
London trade, right?

[00:58:10]
We got railroad tracks here.

[00:58:11]
123 pushes up.

[00:58:13]
Came down.

[00:58:14]
Oh, I may just row it all the way down.

[00:58:16]
Now, here's a mistake I made, guys.

[00:58:18]
And I'm not perfect.

[00:58:19]
I do not get every one of them right.

[00:58:21]
But you can see, my entry was right here.

[00:58:24]
What was I thinking?

[00:58:30]
Yeah, Bill.

[00:58:32]
I was thinking, man, I nailed it.

[00:58:34]
Beautiful W, right?

[00:58:35]
Came down, went up, came down.

[00:58:37]
Oh, man.

[00:58:38]
This is why I jumped in here.

[00:58:41]
Guess what?

[00:58:43]
I was wrong.

[00:58:45]
I was wrong.

[00:58:46]
Luckily, my losses were very minimal, right?

[00:58:51]
Stop losses right down here.

[00:58:53]
It was a small loss.

[00:58:54]
But what has Steve taught us?

[00:58:56]
What has he taught me?

[00:58:57]
What have I become very good at?

[00:59:02]
I'm pretty stubborn.

[00:59:04]
Ask my wife.

[00:59:05]
I was trying to tell her I'm pretty patient.

[00:59:07]
The other day, she says, no, you're not patient.

[00:59:09]
You're stubborn.

[00:59:10]
She's right.

[00:59:12]
So what it was, here's the opportunity, remember?

[00:59:15]
It came down here, right?

[00:59:17]
There was just more orders down here.

[00:59:18]
Came up.

[00:59:19]
There was another entry right here, right back to where?

[00:59:23]
The water.

[00:59:30]
Yeah, on this one, though, here's what's nice about the tools

[00:59:33]
that Steve has, Bill before, that car and rain, everybody.

[00:59:38]
Jim, and everybody's been able to tweak on some of the other

[00:59:41]
guys, Steve and Jose and everybody.

[00:59:44]
Listen, when you set a trade like this, you don't have to see

[00:59:47]
here all day long and why don't you?

[00:59:49]
I put my trade order in, right?

[00:59:52]
I know it's headed to the water.

[00:59:54]
Put my stop loss in.

[00:59:56]
If I lose, it's cost of doing business.

[01:00:00]
So I guess the question I would have for you is what's your

[01:00:03]
cost of doing business.

[01:00:04]
You have to, in my opinion, have some kind of cost of doing business

[01:00:08]
every day.

[01:00:10]
Now, that's simply just my opinion.

[01:00:13]
It's an amount of money that you're willing that you're all

[01:00:16]
comfortable with losing.

[01:00:17]
Now, remember, you know that I hate to lose.

[01:00:20]
But I have to, for me personally, I have to have a dollar

[01:00:22]
mountain in mind that I'm okay with losing because I know I'm going to go

[01:00:26]
back and get it anyway.

[01:00:28]
So just something for you to think about.

[01:00:30]
What I did was on this trade, you enter here.

[01:00:34]
You set your take profit and you take off.

[01:00:36]
You go to your thing.

[01:00:37]
You don't have to sit around with it if you don't want to.

[01:00:44]
But yeah, but that's my form of risk management.

[01:00:48]
That's how I do it.

[01:00:53]
Can you get a little bit of a couple more questions here.

[01:00:56]
I've got a handful more slides, maybe seven or eight left.

[01:00:59]
So let me take a few questions here because they're starting to build up.

[01:01:03]
Derry says, do you ignore the TDI will buy an oversold?

[01:01:06]
No, I do not.

[01:01:07]
Now, that's a huge indicator for me.

[01:01:09]
I'm watching that like a hawk.

[01:01:16]
It's the city of the city of John.

[01:01:18]
My friend John from Vegas.

[01:01:21]
It seems with the US entry, you can't really wait for a confirmed entry.

[01:01:25]
John, it essence that's sort of true because a lot of the times you're not going to get second or legs.

[01:01:32]
So you're looking forward to exceed the ADR.

[01:01:35]
You're looking for a confluence of ants, maybe oversold.

[01:01:38]
You're looking for all for bot.

[01:01:40]
You're looking for reversal signs in the candles.

[01:01:44]
And you're looking for generally the overall behavior of what it did last night in the London.

[01:01:49]
And if you behave itself in the London, it's generally going to behave itself and do what it's supposed to do.

[01:01:54]
in the US session, that makes sense.

[01:01:59]
Okay, James, from down under a stand, is there a script?

[01:02:09]
Which will allow the trade to close when it hits the water if you're not able to stay at the computer?

[01:02:14]
James, all you need to do is make an adjustment.

[01:02:19]
It's set your take profit to set it near the water, make the adjustment.

[01:02:23]
It's going to pop you out of the trade.

[01:02:25]
I know that there's a tool called the dragger that has been Ray and everybody's been experimenting with.

[01:02:33]
I don't think it's ready for full release yet.

[01:02:35]
But that's a pretty cool tool.

[01:02:37]
And I think that will become enough for a spawn entry down the road a little bit.

[01:02:41]
But anyway, yeah.

[01:02:42]
So James, what you need to do is just set it manually if you will and take off and let it go.

[01:02:53]
I do that a lot of the time.

[01:02:59]
I do that.

[01:03:00]
I'm not going to sit here and stare at candles.

[01:03:02]
Steve says it's like watching paint dry, even just waiting for it to do the right thing.

[01:03:07]
I'm doing other things.

[01:03:09]
Okay, Manny's asking how many trades do I take daily?

[01:03:13]
Manny, it depends.

[01:03:17]
I don't have a set number.

[01:03:19]
Some days it might be three or four, some days it's zero.

[01:03:22]
It just really depends on what the market is willing to give.

[01:03:25]
I'm not going to force a trade.

[01:03:27]
I'm looking for a pristine setup because I like to win.

[01:03:30]
If it's not telling me the trade it, I'm not going to trade it.

[01:03:36]
Okay, let's sit a few more of these slides here.

[01:03:43]
Okay, here's another trade.

[01:03:46]
This is GJ.

[01:03:47]
Now Steve talks about GJ.

[01:03:50]
Like GJ is the beast.

[01:03:51]
This thing is very aggressive.

[01:03:53]
If you're new to trading or new to Steve's method, it's probably going to take you a little while before you want to tackle this pair.

[01:03:58]
He's tough, man.

[01:04:00]
He's really tough.

[01:04:02]
But you can see what was the trade here.

[01:04:04]
First of all, the thing ran its course, right?

[01:04:06]
A long sustained run.

[01:04:08]
It came.

[01:04:09]
It bottomed out.

[01:04:10]
Came down.

[01:04:11]
Went back up bottom out.

[01:04:12]
Nice W here.

[01:04:13]
You can see my entry was right here.

[01:04:15]
Where did I take it to?

[01:04:20]
Anybody guess?

[01:04:22]
Right?

[01:04:23]
It's the water.

[01:04:30]
Okay, Poe.

[01:04:34]
I have to go back to that slide.

[01:04:36]
But Poe, here's what Steve is talking about.

[01:04:39]
Here's exactly what I do.

[01:04:41]
My stop loss is seven pips plus the spread below the low of the day.

[01:04:48]
So if this is the low of the day right here, right?

[01:04:52]
I'm going to take my crosshair and I'm going to measure down from here seven pips, add the spread, and whatever that number is, that's what my stop loss is.

[01:05:03]
Now generally, I'm pretty good about getting pretty low here.

[01:05:07]
Typically, when I add the spread, when I add the stop loss, I'm sorry, when I add the spread, when I add the distance of format, I'm generally 13 to 15 pips, including stop loss and everything.

[01:05:20]
So it's not like I've got 50 pips there.

[01:05:23]
So if I do get stopped out, it's not very much, you know, it's not killing me.

[01:05:31]
Gloria is asking, how do I know that it's the low of the day when it first hits?

[01:05:36]
Basically, what I'm doing is measuring off the ADR.

[01:05:41]
I'm watching the levels, right? I'm watching the behavior.

[01:05:45]
If it's behavior for the two previous days, and it's basically ran the same ADR, 110 pips, 80 pips, 120 pips, whatever it is, the two previous days, when it gets down to around 115 pips, let's say the two previous days it ran 120, when it's around 115 pips, man, I'm watching it like a hawk.

[01:06:05]
I'm looking for, it's a tell me, hey, I'm going to turn around now.

[01:06:09]
That's how I know it by measuring the ADR.

[01:06:11]
You're also going to learn and understand that by looking at TDI.

[01:06:15]
That's going to give you another clue.

[01:06:20]
Yeah, three swipes and everything.

[01:06:23]
Max is asking, what pair do you consider the better one to start with to learn these methods?

[01:06:28]
You're absolutely.

[01:06:31]
If I said, hey, look at two, if you just need to boil it down to one or two pairs that are going to give you the sweetest setups, in my opinion, this is just my opinion, I would trade the Euro and the Aussie dollar.

[01:06:45]
Low spreads and they behave.

[01:06:57]
Hey, man, he's asking, how do I determine the ADR?

[01:07:01]
There's two ways.

[01:07:02]
For one, man, I've been looking at these same pairs for nearly three years now.

[01:07:07]
At first, I basically have kept a tab, but a lot of these indicators they'll tell you.

[01:07:14]
If you look right up in here, let's see, previous day it ran.

[01:07:18]
It tells you right there, current day it ran, she tells you right there.

[01:07:22]
The candidates I know, we have another tool up here that tells you what they are.

[01:07:30]
I believe the one I use a lot says it as well, I think.

[01:07:37]
Okay, Max is asking, what do you mean by a reversal signs in the candles?

[01:07:41]
Max, you need to go back to the section that Steve teaches in the class.

[01:07:45]
There's candles, there's railroad tracks, right?

[01:07:47]
There's a quarter wood that teaches you that.

[01:07:50]
Hammer, Doji, all these things are signals that teach us or tell us or indicate to us that a reversal is about to happen.

[01:08:01]
But they have to be, now it has to be in the right context.

[01:08:05]
It can't be in the middle of the range.

[01:08:07]
Let's say the pair runs normally 120 pips and you're getting these reversal signs in 65 pips.

[01:08:12]
Guess what?

[01:08:13]
You're going to get taken now.

[01:08:15]
So that's what Steve's teaching about a confluence of events.

[01:08:18]
There has to be a handful of things that's telling you what's going on because they're going to do everything they can to trick you every time.

[01:08:25]
Because they want your money.

[01:08:32]
Okay, let's see, I think we got just a few more trades here.

[01:08:35]
This was a November trade.

[01:08:37]
Again, here's another trade that I happen to take.

[01:08:41]
Normally, guys, I'm not telling you here, I trade the Asian session.

[01:08:45]
There's been three or four times.

[01:08:47]
When I'm just sitting here answering everybody's email, I have to charge up.

[01:08:51]
I pull them up and see what's going on.

[01:08:53]
And if it gives me a lay down trade, then guess what I'm going to do.

[01:08:59]
Right, I'm going to take it.

[01:09:03]
If it's saying, hey, trade me, I'm going to take it.

[01:09:06]
You can see on this particular one, the AVR.

[01:09:09]
I mean, it ran a lot.

[01:09:10]
It gave me pins again twice here, right?

[01:09:13]
It gave me a beautiful reversal.

[01:09:16]
And you know how Steve says, he says this over and over.

[01:09:21]
That, you know, it's, I'm trying to think of how he says it, but basically he says that the times change.

[01:09:28]
It's not going to be at the exact same time every time.

[01:09:32]
So the patterns, the same, they just move the pattern if you know what I'm saying.

[01:09:37]
The timings, they rotate them.

[01:09:39]
All the trades don't always happen in the US.

[01:09:41]
That all always happen in the London.

[01:09:43]
I mean, they're constantly rotating them around.

[01:09:45]
So it's the same trades just different times of the day.

[01:09:48]
So this particular trade, you can see what was grabbed right here.

[01:09:53]
And you'll notice a lot of the trades that I have.

[01:09:56]
Almost as good as Steve.

[01:09:58]
His entry was right here and mine was up there.

[01:10:01]
Okay, so we got a few more trades here.

[01:10:08]
So you can look at this particular pair.

[01:10:13]
Now, who wants to guess what pair this is?

[01:10:19]
Variation on the fame.

[01:10:20]
Thanks, Bruce.

[01:10:25]
This is EC.

[01:10:26]
This guy just, this goes crazy on me, but you can look here.

[01:10:30]
Beautiful setup, right?

[01:10:32]
It ran.

[01:10:33]
One, two, three, swipes.

[01:10:36]
Gaby a nice ugly look in kindergarten ma'am there.

[01:10:39]
And then just rolled on down.

[01:10:41]
So the entry for me was right here.

[01:10:43]
US session, I mean, this is perfect.

[01:10:45]
This is exactly what Steve teaches.

[01:10:47]
Look at the TDI.

[01:10:48]
Here's the 32 button.

[01:10:50]
And it's well below that.

[01:10:51]
It's probably 25.

[01:10:54]
Okay, Fred is asking for it.

[01:10:56]
I mean, I'm in a Fred that many of you last names.

[01:10:58]
Ask me if I ever look at them five or M1.

[01:11:01]
Fred, I can honestly tell you in my entire life of trading

[01:11:03]
I've never, ever looked on M5 or M1.

[01:11:06]
Just never have.

[01:11:09]
Which Steve first started teaching in Diannali,

[01:11:12]
close to three years ago.

[01:11:13]
He told me to look at the 15.

[01:11:15]
Even though I tried to recreate some stuff,

[01:11:18]
I never changed the time frames.

[01:11:20]
So no, I have not.

[01:11:22]
I like the 15 in the hourly.

[01:11:24]
That's what I use.

[01:11:26]
Okay, let's see here.

[01:11:34]
Here's another trade.

[01:11:36]
This is again, this is just a picture,

[01:11:38]
perfect Mona Lisa here, if you will.

[01:11:41]
One, two, three.

[01:11:44]
Swipes the high, hit the daily high right here, right?

[01:11:47]
Gave a nice kindergarten now.

[01:11:49]
I'm right there.

[01:11:50]
Do you guys see that?

[01:11:51]
I remember when Steve first started teaching these

[01:11:54]
and I didn't know anything about candles or anything like that.

[01:11:57]
I'm thinking, I have no idea what the sky is talking about.

[01:11:59]
There's no M, there's no W, this guy's out there.

[01:12:02]
He's on that cochersome.

[01:12:05]
But now, after I've been hanging around him for so long,

[01:12:08]
I totally see it.

[01:12:09]
It's like a pre-school M or maybe a kindergarten now,

[01:12:14]
but it's in here.

[01:12:16]
So a cane, just drop, drop, drop, drop.

[01:12:19]
And boom, gave us a beautiful entry right here,

[01:12:22]
and there's a beautiful entry.

[01:12:24]
And there's the low here.

[01:12:26]
Second opportunity right here, and right on up.

[01:12:30]
Eventually this pair landed up here at the water.

[01:12:37]
Jose, I do not look for three pushes because there's no

[01:12:40]
pushes in the US session.

[01:12:42]
The pushes come in the London session.

[01:12:44]
One, two, three.

[01:12:47]
There's no, if there were three pushes in the US session,

[01:12:50]
the trade's gone.

[01:12:51]
There's nothing for me to look at.

[01:12:53]
It's already happened.

[01:12:54]
So the pushes generally occur in the London or late London session.

[01:13:02]
What's that, man?

[01:13:07]
Okay, Diane saying, she's adding to that Jose,

[01:13:10]
that it does help you see the reversal.

[01:13:11]
Yes, the pushes do.

[01:13:16]
Okay, I'm going to take a few more questions.

[01:13:18]
I have two more slides, Carl, if you can get yourself prepared.

[01:13:21]
I'll be probably another five minutes or so.

[01:13:24]
Okay, so Brian says, how do you know when to get in?

[01:13:28]
Do you wait for the WK?

[01:13:30]
Brian, again, what I'm looking at is, first of all,

[01:13:34]
I'm looking for the ADR to run.

[01:13:37]
What I mean by that is if the pair generally every day runs

[01:13:41]
100 pips, if it's not in the mid 90s, it's not ready.

[01:13:46]
And if it refers to say, 85 guess what?

[01:13:49]
It didn't behave.

[01:13:50]
I don't want to trade it anyway.

[01:13:52]
So I'm looking for one, the ADR to be met.

[01:13:55]
Two, I'm looking for where it's at on TDI.

[01:13:58]
Is it overbought?

[01:13:59]
Is it oversold?

[01:14:01]
Three, what type of reversal candles is it giving me?

[01:14:06]
Do I have row-well tracks?

[01:14:08]
Do I have a hammer or a doji?

[01:14:11]
In the London, I'm sorry, in the US session,

[01:14:13]
you generally don't get a lot of second lads.

[01:14:18]
You just don't get them.

[01:14:20]
So you have to use other skills and tools that Steve's taught us.

[01:14:25]
Now, Brian and I have gotten very good at it because we've been doing it for a long time.

[01:14:34]
You know, another key ingredient is also when the hourly,

[01:14:39]
the signals that you're seeing on the hour leaves line up with the 15 minutes.

[01:14:43]
That's like gold.

[01:14:45]
It's beautiful.

[01:14:47]
Okay, let's take a few questions and I got two more slides and we'll wrap it up here.

[01:14:57]
Okay, Jerry, very good question.

[01:14:59]
So then it looks like you get into some really early trades.

[01:15:03]
Or getting really early in the trades.

[01:15:06]
Would you say it comes with experience and homework?

[01:15:09]
Jerry, absolutely.

[01:15:10]
I've been looking at the same pairs for nearly three years.

[01:15:14]
I've done the flashcards.

[01:15:16]
I've done and I study that over and over and over.

[01:15:21]
I've looked at these pairs over and over.

[01:15:23]
I know their behaviors.

[01:15:24]
I know them.

[01:15:26]
They're like my kids.

[01:15:29]
Yeah, but yeah, yeah, you don't have to wait three years like I have.

[01:15:35]
You can just, you can go back on the charts and learn it.

[01:15:38]
Like Steve says, I thought it was just an incredible advice for Steve to say,

[01:15:41]
hey, look at, make these flashcards.

[01:15:44]
Look at your entries long, look at your entries short,

[01:15:47]
post them up in your trade room, put them on your wall.

[01:15:50]
I've a buddy Steve that lives here in Florida.

[01:15:53]
He and his wife are masters that put stuff up on their walls.

[01:15:56]
He's got stuff tossed and all over his walls to remind him of the right trades.

[01:16:00]
Time frames, the rules.

[01:16:02]
And he's getting it, man.

[01:16:03]
He's really, really getting it.

[01:16:05]
Each one of us learns a little bit different.

[01:16:07]
If you need to go and make these cards like Steve did,

[01:16:10]
or are recommended and throw yourself with them over and over and over and over and over and over.

[01:16:15]
Do it.

[01:16:16]
It's worth it.

[01:16:17]
Go, go do it.

[01:16:19]
Okay, a couple more questions here.

[01:16:23]
Let's see.

[01:16:29]
Okay, Clem is asking.

[01:16:32]
Let's see, if you're waiting for the reversal candle,

[01:16:35]
how do you get in near the low of the day?

[01:16:38]
Okay, here's what I'm looking for, Clem.

[01:16:40]
I am, first of all, what did I say I do?

[01:16:43]
The first thing I'm looking at is the ADR.

[01:16:46]
But let's back that up a little bit.

[01:16:48]
Did the pair behave, you know, for the last couple of days?

[01:16:51]
Is it behaving?

[01:16:52]
Is it somebody I want to play ball with?

[01:16:54]
If it's funky and all over the board, I don't even look at it.

[01:16:57]
But if it's been behaving the last couple of days, then I'm narrowing it down to today.

[01:17:01]
Okay, in the London session, did it give a false move?

[01:17:05]
Did it trap some folks?

[01:17:06]
Is it moving along to stained run?

[01:17:09]
Okay, yes, it did that.

[01:17:10]
Great.

[01:17:11]
I know that at some point it's not going to continue along run for a million pips.

[01:17:17]
So logic tells me based on my studies that if this pair runs 100 pips on average ADR,

[01:17:25]
and it's at 94.95 right now, and I can see that it's starting to give me a doji or reversal

[01:17:32]
or some other indication of a reversal, I'm going to get in.

[01:17:36]
Am I right every time?

[01:17:38]
No, I'm not right every time.

[01:17:40]
But most of the time, I'm right.

[01:17:43]
So I get in.

[01:17:48]
And here's what happens.

[01:17:49]
Either I get in and I'm two or three pips off the bottom and it takes off my way,

[01:17:52]
or I get stopped out for a handful of pips.

[01:17:55]
So what do I do?

[01:17:57]
I throw my mouse across the room, I kick my computer,

[01:18:01]
and I go outside and scream.

[01:18:03]
No, I don't do that.

[01:18:05]
I might have done that a couple of years ago, but no, I don't do that.

[01:18:09]
I will sit here and I will wait it out and I will let it complete its pattern.

[01:18:14]
A lot of times if it doesn't do it where the ADR is supposed to be,

[01:18:18]
what is T.T.S. 25 to 50 pips.

[01:18:20]
So it's going to go down or up another 25 to 50 pips and then it's going to give me the same signal.

[01:18:28]
It's going to give me a reversal sign.

[01:18:31]
So then I will go in and once it gives me the signal there,

[01:18:34]
I'm going to go in a little bit heavier than my previous trade,

[01:18:38]
so I make my money back plus plus.

[01:18:40]
That's how I've been able to go 10 months with like 6.

[01:18:44]
It might be 7, 6 or 7 losing days.

[01:18:47]
It because I'm patient or stubborn enough to let it complete its pattern

[01:18:52]
and it's not over till I win.

[01:18:57]
Okay, so let's look at these last two charts and we'll take a couple more questions

[01:19:02]
and we'll take a five minute break and we'll have car finish the night.

[01:19:06]
So it's on our end.

[01:19:10]
Okay, here we go.

[01:19:12]
This tree, this is from November.

[01:19:14]
Okay, you can see here and this is what Steve's talking about.

[01:19:18]
Basically we have extended it here, right?

[01:19:20]
We extended the consolidation here of 1, 2, 3 pips.

[01:19:25]
It actually came up.

[01:19:26]
I'm sorry, swipes came up here pinned the mail and then it just took off.

[01:19:30]
One, I mean look at all these vector candles.

[01:19:32]
It's tight, taken off.

[01:19:34]
So it came down.

[01:19:36]
Now here's a particular opportunity.

[01:19:39]
Again, I said most of the time you don't get a second leg,

[01:19:42]
here's a second leg trade, right?

[01:19:44]
So I entered here and what am I looking for?

[01:19:47]
Where am I headed?

[01:19:48]
Am I looking for 1,000 pips?

[01:19:51]
No.

[01:19:53]
I'm headed right back to the water.

[01:19:55]
35 to 50 pips that I'm happy, man.

[01:20:04]
Okay, last chart here and we'll take a few questions.

[01:20:09]
We'll call it a day.

[01:20:13]
This particular trade here, sort of an ugly deal.

[01:20:17]
Right up here you can see that it moved.

[01:20:20]
It gave us a couple indications here.

[01:20:23]
This one, again, this is a pretty ugly m.

[01:20:27]
Pretty ugly m.

[01:20:28]
This is the year old back in December.

[01:20:30]
So trade I took.

[01:20:31]
I got it right up here.

[01:20:33]
Can't remember exactly, but it's pretty close to the top.

[01:20:35]
I just wrote it down.

[01:20:37]
And actually, I made a, if somebody would have hung out with this

[01:20:42]
and this is a great payday, I'm just 200 pips.

[01:20:48]
So I guess the question I have for you is,

[01:20:51]
and it's really not even a question.

[01:20:53]
For those that just simply can't stay up all night,

[01:20:55]
Steve has taught us a method that we can trade the US session to make money.

[01:21:02]
And it's fantastic.

[01:21:04]
I think the only way I would ever trade the money session now is

[01:21:07]
if somebody forced me to move overseas.

[01:21:10]
Because I love the US session.

[01:21:12]
It's fantastic.

[01:21:13]
It's easy.

[01:21:14]
It's fun.

[01:21:15]
The timeframe short.

[01:21:20]
Okay, so let's take a few questions and then we'll move on to car.

[01:21:25]
Okay.

[01:21:28]
Okay, Harvey has a question.

[01:21:30]
What happens when the projected ADR has been exceeded?

[01:21:33]
Harvey, if it's been exceeded,

[01:21:35]
generally I pass on it.

[01:21:38]
Generally I pass on it.

[01:21:43]
Here's why.

[01:21:46]
It simply isn't behaving itself.

[01:21:48]
Now, if I took the trade and then it exceeded,

[01:21:51]
I guess what I want to do.

[01:21:53]
I'm going to hang out and get my money back and then some.

[01:21:55]
But if it's exceeded it before I really got serious about trading it,

[01:22:00]
it's overextended.

[01:22:01]
I just don't want to mess with it because it's not following the rules.

[01:22:04]
Does that make sense?

[01:22:11]
Okay, so next question.

[01:22:16]
Okay, James Jones is asking.

[01:22:18]
I didn't mean to use your last name, James.

[01:22:20]
Sorry about that.

[01:22:21]
James is asking to what red zone news events do you pay attention to?

[01:22:24]
Or ignore?

[01:22:26]
James, honestly, I haven't looked at the news in two years.

[01:22:30]
I don't look at the news.

[01:22:32]
I don't care.

[01:22:34]
I skip down on non-forn payroll because I just don't want to mess with it.

[01:22:38]
Do you want to be around the drama?

[01:22:40]
But every other news event, it doesn't face me.

[01:22:43]
I personally do not look at them because they're going to complete the pad anyway.

[01:22:50]
Now, until you get as confident as me or Diane Arcanon or some of the other traders car,

[01:22:57]
Kim, some of the other guys rage him, Steve, for that matter,

[01:23:01]
you may want to pay attention to the news.

[01:23:03]
But once you fully understand the cycle, remember, I'm going back and I'm looking

[01:23:08]
at a macro view of what's been happening over the last four or five days anyway.

[01:23:13]
So that's helping me filter out what I'm interested in trading.

[01:23:20]
Okay, Helen, so if it exceeded the ADR, you wouldn't look for a reversal.

[01:23:30]
You know, Helen, here's how I feel about that.

[01:23:33]
If the guy is not playing by the rules, why would I want to play with him?

[01:23:37]
I don't know what he's doing.

[01:23:39]
You know what I'm saying?

[01:23:40]
He's not following the rules.

[01:23:41]
So he could, he could, you know, just be falling off the earth or he could reverse any second.

[01:23:46]
But I have, I have no leverage with him because he's not following the rules.

[01:23:51]
So I just simply taking my ball and kicking him off my playground.

[01:23:56]
Okay, this one's coming from Murray.

[01:24:01]
If you get stopped out, how long would you wait to re-enter at the next level?

[01:24:10]
Murray, remember my trade time is from 8 to 11.

[01:24:15]
So if it doesn't happen between 8 and 11, I'm done.

[01:24:18]
Irregardless.

[01:24:20]
Irregardless.

[01:24:21]
So if I, if it doesn't reset itself off within that time for him, guess what?

[01:24:25]
That's a losing day for me.

[01:24:27]
And it takes me off, but you know what?

[01:24:29]
Those are my rules.

[01:24:31]
I have other things that I want to do to spend with my, my family.

[01:24:34]
So I just let it ride.

[01:24:36]
I take it as a loss.

[01:24:37]
And I'm okay with that.

[01:24:45]
Okay, let's see.

[01:24:50]
Let's go with a couple more questions here.

[01:24:53]
Steve is asking, do you ever take continuation trades?

[01:24:55]
Steve, I take, I take them a lot of the time.

[01:24:58]
What I'm simply showing you tonight is more safe for trades.

[01:25:02]
Are there other trades that I take or have taken?

[01:25:05]
Yes.

[01:25:06]
But I want you to get the easy cherry picks first.

[01:25:09]
When you understand they can take the easy cherry picks, then you're going to,

[01:25:12]
you're going to learn more than advanced trades, and you're going to know how to trade it up one side down the other.

[01:25:17]
I don't want to do that with you right now because, yeah, it's going to,

[01:25:22]
it's going to mess people up.

[01:25:24]
You need to get the safe cherry picks first.

[01:25:26]
When you can master the cherry picks, we'll talk about some more advanced stuff or

[01:25:29]
Steve will teach you some, you know, some other things.

[01:25:32]
And honestly, once you get good at the cherry picks, you're going to figure it out yourself,

[01:25:37]
what they're doing, and you won't need any help.

---

## ⛔ FENCED — ASR DEGENERATION, NOT SOURCE EVIDENCE ⛔

The 9 entries below are a degenerate ASR repetition loop. Eight of them are timestamped
**past the end of the audio file** (which is 5141.03 s / `01:25:41`); the real recording's
last words are the `[01:25:37]` line immediately above, confirmed by independent
re-transcription. They are retained for the record and **must not be cited by any
artifact.** See the COVERAGE section at the top of this file.

```text
[01:25:40]
And then you're going to get the cherry picks first.

[01:25:43]
And then you're going to get the cherry picks first.

[01:25:46]
And then you're going to get the cherry picks first.

[01:25:49]
And then you're going to get the cherry picks first.

[01:25:52]
And then you're going to get the cherry picks first.

[01:25:55]
And then you're going to get the cherry picks first.

[01:25:58]
And then you're going to get the cherry picks first.

[01:26:01]
And then you're going to get the cherry picks first.

[01:26:04]
And then you're going to get the cherry picks first.
```

⛔ END OF FENCED BLOCK — the genuine transcript ends at [01:25:37].
