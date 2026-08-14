# V12 — TRANSCRIPT

## SOURCE

| Field | Value |
|---|---|
| Video ID | V12 |
| Original filename | `Bootcamp1 Wk4 040812 Part2 (55mins).swf` |
| SHA-256 | `10608e8ff01fb14b2980b36891e3c120fcb42510a5c7ee26bff86ff9f351159c` — verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session on the flat `Bootcamp/` canonical path, **and re-verified after the frame-rate patch** to prove the original was not modified (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| Duration | 00:55:18 (audio measured **3318.543673 s**; SWF header **9,956 frames ÷ 3.0 fps = 3318.667 s**; `SOURCE_MANIFEST.md` 00:55:18 = 3318 s — three independent figures agreeing to within 0.7 s) |
| Lesson title | ⚠️ **CORRECTED AFTER THE SCREENSHOT PASS — the transcript-only draft of this row said *"NOT PRINTED"* and was WRONG.** The title **is** printed, and it is the file's opening frame, held for **8½ minutes**: **`Traders Dynamic Index`**, subtitled *"Thank You Dean & CompassFX"* (`V12_00-00-16_title-card-traders-dynamic-index.png`). The speaker also names it in speech at `[00:07:04]` — *"All right now let's get to TDI"*. **The correction is recorded rather than silently applied** (`REMEDIATION_PROTOCOL.md` §2) because it is exactly the class of error `SWF_CAPTURE_RECIPE.md` §9 step 4 exists to expose: the audio never speaks the words *"Traders Dynamic Index"* in full, so an audio-only pass cannot see the title. *(Superseded text: "~~NOT PRINTED as a topic title in any swept frame.~~")* The quarantined per-lesson header's *"Primary Topics: M & W Anatomy, Time Gaps Between Peaks (30-90 Mins) & Rejection Signatures"* is fabricated — see `QUARANTINE_REGISTER.md` **Q-013** |
| Session date | **2012-04-08** (Easter Sunday), from the filename `040812` and `SOURCE_MANIFEST.md`. **Same session as V11** — V11 is `Part1 (51mins)`, this is `Part2 (55mins)`, same date. V11 `[00:25:33]` (*"i figured it was sunday and it was easter"*) dates the session from inside the recording; this file adds an independent forward-dated corroboration at `[00:51:04]` — *"We're shooting for **April 21st**"* — which is a Saturday **13 days after** 2012-04-08 |
| Frame rate | **3.0 fps** in the SWF header — read from **this file's own header**, not assumed (`SWF_CAPTURE_RECIPE.md` §10, as corrected by V10 R1 open item 87). V10 declared 2.0; V11 and V12 declare 3.0. The 10× sweep patch is therefore **3.0 → 30.0** here |
| Stage size | **1024 × 786** — the majority class. `GOTCHA 5`'s table gives `(512, 300)`, and the pre-click/post-click guard **confirmed it fired** rather than assuming it (`sweep.log`: *"play click confirmed: stage changed"*) |
| Transcribed by | ASR, by a pre-ingestion session. Copied and verified 2026-08-13 — see VERIFICATION below. The pre-ingestion file's own `# VIDEO` header block is **NOT carried over**: its *"Course Position: Video 13 of 21"* is wrong under `D-017` §2's renumbering (this file is **V12**), and its *"Primary Topics"* line is unsourced and, on this lesson, demonstrably wrong. Only the verbatim body is copied |
| Transcription confidence | **MEDIUM–HIGH.** Well-segmented, internally consistent, and it preserves its own mishearings. The defects are ordinary ASR failures on domain vocabulary and on proper nouns, enumerated below |

---

## SPEAKER TABLE — MANDATORY UNDER `D-025` consequence 3, re-adopted by `D-033`

| Speaker | Runtime | Basis |
|---|---|---|
| **Course author (Steve Mauro)** | **100%** — `[00:00:00]`–`[00:55:11]`, the whole file | Nine non-acoustic strands, below. **HIGH confidence, over-determined** |
| Guest presenter | **0%** | No second voice is introduced, addressed, thanked or handed to anywhere in the file |

**Named third parties appear and NONE of them speaks.** *"Zain"* / *"Zaim"* `[00:00:00]`, `[00:26:20]`
(ASR renders the name two ways — same person, the analytical friend who built the spreadsheet);
*"Taehyun"* `[00:03:08]`; *"Greg"* `[00:03:58]`; *"Gloria Goldman"* `[00:03:41]`; *"Dean Malone"*
and *"compass FX"* `[00:07:16]` (the TDI's authors, discussed, not present); *"Subio"* /
*"be oh"* `[00:04:03]` (**the same unresolved proper noun V11 `[00:00:12]` carries** — Whisper
renders it *"subio"* here, matching V11's rendering); *"Mark"* `[00:05:11]`; *"Don, Dave, Pradeep,
Casey"* `[00:45:03]`; *"Whitney"* `[00:47:59]`; *"Aaron"* `[00:48:15]`; *"Dick Schmidt"*, *"Ray"*,
*"Car"*, *"Zen"*, *"Jim Nicholson"*, *"Kim K"*, *"Luther"*, *"Mosh"* in the announcements block.
**Every one of these is a name the speaker reads off a chat window or refers to in the third
person; in each case the next line is the same voice continuing.** Recorded because a name in a
transcript is the commonest false positive for a second speaker.

### THE NINE STRANDS — fixed before the answer was known, non-acoustic, `D-025`/`D-033` method

| # | Strand | Evidence |
|---|---|---|
| **1** | **The speaker is addressed as, and answers to, "Steve"** | `[00:02:35]` *"I know that people will tell you **Steve**, there's no way you can take 90% out of the market"* — first person, quoting what is said **to him** |
| **2** | **He owns the course templates** | `[00:07:46]` *"the way it's **preset in the templates** is the way **I** want us to learn how to use it"*; `[00:55:02]`–`[00:55:11]` *"if you need **the old student folder**… send me an email… **I'll mail you the old one**, but when I finally get it right **I will post the new one**"* |
| **3** | **He owns the tooling and its development history** | `[00:21:58]` *"this was **before we coded the shadows**"* — the shadow boxes are this project's `3M-shadow-boxes-15M.tpl` (`D-042` `[TOOLING]` rows). `[00:54:32]`–`[00:54:41]` he is directing **Ray** to recode the work-time ribbon and receiving a clock from **Dick** |
| **4** | **He owns a forum section and sets the homework** | `[00:42:25]` *"in the forum **I post in the homework section**"*; `[00:42:37]` *"if you go under **my section** it says assignments are in here"*; `[00:45:43]` *"Post under **my homework section**"* |
| **5** | **He owns the paid business's other tier** | `[00:52:04]` *"I'm preparing some lessons for the **DMR**. I'm gonna be teaching a few times a month **on the other side for the paid subscribers**"* |
| **6** | **He runs the live events** | `[00:52:38]`–`[00:53:44]` *"**I'm working closely with the venue in New Jersey**… I'm gonna deliver a **web class** two weeks three weeks before I go… **I'll post the details as I lock down the availability**"*; `[00:50:52]` *"**we're gonna set up an additional training**"* |
| **7** | **He speaks the course's own catchphrase in the first person as its author** | `[00:03:05]` *"I don't know how I can teach you, all I can do is **make you accountable**… I need you guys to step it up and **trade strong**"* — `Trade Strong` is V11's printed slide `[00:14:xx]` (`A-081`) |
| **8** | **He disclaims authorship of the one thing he did not write, and claims the alteration** | `[00:07:13]` *"**TDI does not belong to me. I didn't invent it**, belongs to compass and Dean Malone… **I've altered it or tweaked it a little bit**"*. A guest would have no standing to alter the group's preset |
| **9** | **Handover scan: ZERO.** | A **17-pattern** superset (`take it away`, `turn it over`, `hand over`, `back to you`, `thanks Steve`, `my guest`, `joining us`, `welcome back`, `over to you`, `take over`, `passing it`, `go ahead Steve`, `Steve's/Steve is/Steve will`, `let me hand/pass`, `you're up`, `floor is yours`, `I'll let`) returns **one** line — `[00:52:25]` *"Okay, **I'll let you know** stand by"* — which is not a handover. **No handover language exists in this file** |

> **This is the same session as V11, and V11 R1 confirmed the course author at 100% / HIGH for
> Part 1.** Per `COURSE_PROGRESS.md` V12 GATE (a) the speaker was nonetheless **tested, not
> assumed**, on strands fixed before the answer was known and without using the acoustic screen
> across files. The result agrees, and strands 2, 3, 5 and 6 are **new evidence not available in
> Part 1** — Part 1 carries no forum-ownership, DMR, venue or template-distribution material.

---

## VERIFICATION — `SETUP_ISSUES.md` `I-008`

| # | Check | Result |
|---|---|---|
| **1** | Final marker vs measured duration | ✅ Final marker `[00:55:11]` = **3311 s**; measured audio **3318.543673 s**. The file ends **7.5 s** before the audio does, and the last line is a **complete sentence** (*"I will post the new one in the form, okay"*), i.e. the tail is the usual post-close silence, not truncation |
| **2** | Monotonic timestamps | ✅ **690 markers, 690 distinct, STRICTLY increasing.** No repeats, no reversals |
| **3** | Preserves its own ASR errors and crosstalk | ✅ **Abundantly** — see the table below. A fabricated transcript does not invent its own mishearings, and it certainly does not render one word (*mayonnaise*) four different wrong ways in one file |
| **4** | Content consistency against an independent engine | ✅ **Whisper `small.en` spot-checks at seven timestamps** — see § AUDIO SPOT-CHECKS |

**Largest gap: 14 s, ONCE, from `[00:04:34]` to `[00:04:48]`.** Second largest: 12 s, twice
(`[00:31:00]`→`[00:31:12]`, `[00:41:29]`→`[00:41:41]`). All three sit at slide changes where the
speaker is silent — the `[00:31:00]` one is explicitly *"okay, let's look at a picture"* followed
by the picture. **Labelling convention, stated once per V11 R1 item 118's forward requirement:
a gap is named here by the marker that ENDS it, and the pair of markers bounding it is given.**

---

## TRANSCRIPTION NOTES — THE DEFECTS, ENUMERATED

These are the evidence that the file is a real ASR pass over this audio.

| Marker | ASR renders | Almost certainly | Consequence |
|---|---|---|---|
| `[00:26:38]`, `[00:26:54]`, `[00:27:26]` | *"the **mannees**"* | ***the mayonnaise*** | ⭐ **LOAD-BEARING — resolved by Whisper, see `c4`** |
| `[00:31:22]` | *"held by the **man is**"* | ***held by the mayonnaise*** | ⭐ **LOAD-BEARING — resolved by Whisper, see `c5`** |
| `[00:31:27]` | *"**Tell** by the 200"* | ***Held** by the 200* | ⭐ **LOAD-BEARING — resolved by Whisper, see `c5`** |
| `[00:35:42]` | *"the **Manate's**"* | ***the mayonnaise*** | Fourth distinct rendering of the same word in one file |
| `[00:26:11]`, `[00:37:20]` | *"hold the **mail**"* | ***hold the mayo*** | Matches `A-064`'s `Mayo`/`mail`/`male` hazard exactly |
| `[00:00:00]` / `[00:26:20]` | *"**Zain**"* / *"**Zaim**"* | one person, spelling unverified | Nothing depends on it |
| `[00:04:03]` | *"**be oh** added in here"* | *"**Subio** added in here"* (Whisper) | Same unresolved proper noun as V11 `[00:00:12]` |
| `[00:07:29]` | *"matches up with the **average is**"* | *"matches up with the **averages**"* (Whisper) | Cosmetic |
| `[00:07:53]` | *"**smooth as** the line"* | *"**it smooths** the line"* (Whisper) | Cosmetic |
| `[00:09:53]`–`[00:10:03]` | *"trend direction… **momentum**… **volatility**"* | as rendered | Correct; this is Dean Malone's own definition being read off a slide |
| `[00:11:16]` | *"I just talked about **our side**"* | *"I just talked about **RSI**"* | ⚠ **The ASR renders `RSI` as *"our side"* / *"R sideline"* / *"our sideline"* throughout.** `[00:12:44]`, `[00:15:13]` (*"our SI"*), `[00:20:47]`, `[00:29:22]`, `[00:30:23]`, `[00:31:40]`, `[00:32:11]`, `[00:40:07]`. **Confirmed by Whisper in `c2`, `c3` and `c6`.** A session grepping `RSI` will UNDERCOUNT |
| `[00:15:40]` | *"**involuntarily** bands"* | *"**it's volatility** bands"* | Cosmetic |
| `[00:22:35]` | *"There's a **railroad tracks**"* | as rendered | Matches V11's `c3` finding — *railroad tracks* is a candlestick pattern, not V11's ASR *"rarer tracks"* |
| `[00:24:00]` | *"confirmed by **TDR**"* | *"confirmed by **TDI**"* | Cosmetic |
| `[00:27:59]` | *"this is the **67**"* | uncertain — possibly *"the 68"* or *"the 32"* | ⚠ **A number attached to a TDI level. NOT adopted.** Not spot-checked; recorded as unverified |
| `[00:47:33]` | *"**87.275 pits**"* | *"87.2, 75 **pips**"* — a joke about decimal precision | *pits* for *pips* recurs throughout |
| `[00:49:45]` | *"train **rocking**"*, *"**south fall**"* | *"train **Rocky**"*, *"**southpaw**"* | Cosmetic; the analogy is Rocky Balboa |

---

## COVERAGE

```text
markers            690
distinct           690
monotonic          STRICT
first              [00:00:00]
last               [00:55:11]   = 3311 s
measured audio     3318.543673 s
tail silence       7.5 s, sentence complete
largest gap        14 s, ONCE, [00:04:34] -> [00:04:48]
second largest     12 s, TWICE
```

---

## AUDIO SPOT-CHECKS — Whisper `small.en`, seven passages

Seven passages were re-transcribed from `v12_audio.mp3` with **Whisper `small.en`**, an engine
independent of the pre-ingestion ASR. They were **chosen for consequence** — six of the seven
carry a record closure — and are a sample, not a re-transcription. `SETUP_ISSUES.md` `I-008`
remains the standing item for transcripts that have had no full independent pass.


### `c1` — `00:03:48-00:04:33` — `C-018` / `A-020` — the student question that separates the TDI's 50 from the moving average's 50
> Whisper `small.en`, verbatim:
>
> it's fantastic okay is the 50 in the TDI the same as 50 in the MA water no Greg I don't know if
>  I read that right but no okay subio added in here I'd like to read it the problem on many trad
> ers with any indicators that they focus only on understanding its basic definitional formula ev
> en at extreme levels an indicator can mislead and indicators behavior to be helpful must always
>  be understood in the context of the movements what we want to catch we cannot escape the under
> standing of the pattern first and the indicator absolutely absolutely absolutely how many times
>  I gotta say it pattern the pattern the pattern price action okay but

### `c2` — `00:07:18-00:08:18` — ⭐ `A-080` — the RSI lookback period, first statement
> Whisper `small.en`, verbatim:
>
> than Dean Malone. I've altered it or tweaked it a little bit. I like the RSI line to be set at 
> 21. Why? It just matches up with the averages a little better and lines up a price action for o
> ur purposes. Am I right? Am I wrong? I don't know. Dean will tell you that I'm wrong. It says i
> ndicator. That says right. But what I'm telling you as a group, the way it's pre-set in the tem
> plates is the way I want us to learn how to use it. 21 slows it down a little bit. You don't se
> e as much noise. It smooths the line and it helps us see M's and W's more clearly than you woul
> d normally get on a more radical or shorter period line. That means we're looking at 21 closing
>  periods back for our line. We're averaging that out instead of 14 periods.

### `c3` — `00:10:40-00:11:25` — ⭐ `A-080` — the RSI lookback period, second statement
> Whisper `small.en`, verbatim:
>
> indicator that the TDI is built upon, okay? For our group in here, hey, that depend keeps falli
> ng off. We have this line set to 21, 21 look back periods, that's all, okay? And every time I s
> ee this line, it cracks me up because this is my pattern right here. If that was the box, there
> 's stop on low rise, and there's M formation divergence, okay? And there's a W formation back i
> nto the range. All right, man, can't carry it away. But anyway, I just talked about RSI and exp
> lained to you how it works and what you're supposed to look for with the RSI. So now, TDI has d
> eveloped...

### `c4` — `00:26:15-00:27:45` — ⭐ `A-064` / `A-020` — *mayonnaise* and *200 EMA* in one passage
> Whisper `small.en`, verbatim:
>
> But here's what I want you to notice. If you add an extra filter like my friend Zayim had menti
> oned, perhaps a 200 EMA, some other reason to confirm the trade, a spike to the mayonnaise woul
> d be it. You should have flashcards illustrating this, but I want you to notice this is almost 
> like a little baby safety trade within the same day cycle. Here's what you got. You got a nice 
> shark fin to the low right past the mayonnaise, almost like the mayonnaise offers support, but 
> the dealer spikes past it a couple of times and notice how he closed below twice, closed above 
> and then shifted it away. Closed above once and then shifted away. Why? To draw people in, to t
> hinking, people take a close below the 200 as a trade signal. He grabs them. He pulls away. You
> 're in profit. Your entry should be here. You're in profit for a while. He comes back to the le
> vel, but notice the mayonnaise has risen. Notice he's added the band and he makes the next form
> ation inside the band. Use your secondary signal if you haven't scratched out. That's a seconda
> ry entry because in essence, this is a big fat dummy.

### `c5` — `00:31:10-00:31:55` — ⭐⭐ `A-020` / `A-064` / `C-018` — *"held by the mayonnaise… held by the 200"*
> Whisper `small.en`, verbatim:
>
> Okay, here's what I'm talking about. Look what happens here. You have a 28 pip Asian range, per
> fect. Price comes out and it's held by the mayonnaise perfectly. Held by the 200, okay. Shark f
> in to the high side, it crosses back in the same side. You get blood in the water, beautiful si
> gnal. It crosses your entry, okay. The R-side line crosses back inside the water and the blood 
> at the same time. The blood happens to line up with the band, it's beautiful, okay. It crosses 
> the market baseline right around the...

### `c6` — `00:19:45-00:20:30` — `shark fin` and `blood in the water`, defined
> Whisper `small.en`, verbatim:
>
> and create the shark's dorsal fin. Okay? And since the band is colored blue for our purposes, i
> t looks like the shark fin is coming out of the water. That's where it came from, shark fin. Wh
> en the fin goes back under the water line, back inside the band, and crosses the signal line, t
> he trade signal line, TSL, that's where we get blood in the water. So it almost looks like the 
> shark's swimming around, his fins showing above the water, and he takes a bite out of somebody'
> s leg. In this example, I like to think it's the dealer's legs. We put blood in the water, we g
> ot a good solid confirmed entry.

### `c7` — `00:13:15-00:14:00` — `market baseline` — the *"moving or liquid 50"*
> Whisper `small.en`, verbatim:
>
> What Dean did is he took a moving average and lined it up very close to price action to give yo
> u a dynamic moving market basis line. Okay, do you understand? The gold line is a moving or liq
> uid 50 so to speak. Okay, there's your 50. Static on all under indicators except the TDI. So wh
> at happens is when you get a one hour signal, normally a trend change would be indicated on pri
> ce crossing above the 50. But because the market basis line went...


---

# VERBATIM TRANSCRIPT

[00:00:00]
Okay, this came from my friend Zain. I mentioned to you guys before he's very analytical very intelligent fellow

[00:00:07]
lives over in I think Ireland

[00:00:10]
No Scotland. Sorry buddy and

[00:00:15]
To him in order for him to have belief in what I'm talking about

[00:00:21]
He had to go back and we made a spreadsheet together. He did all the work actually

[00:00:27]
But I told him what he needed to look for

[00:00:29]
He had to physically go back and prove to himself

[00:00:33]
That what I'm saying is real and I'm a problem with that

[00:00:36]
Because what happens is that built his confidence to the level where he takes the trades without even thinking about it because he knows

[00:00:44]
statistically

[00:00:47]
Now he's got a very high percentage win ratio, so here's the deal

[00:00:51]
Simply taking the second leg and more W spread out over five bars

[00:00:57]
That presents itself above or below the blue box within the appropriate times

[00:01:04]
Irrespective of any other indicator or criterion is good for approximately 85%

[00:01:12]
Obviously the percent will increase as you as you start factoring in other filtration

[00:01:18]
Criterion such as TDI EMA's ADR etc. Etc. Maybe the statistical information helps the group

[00:01:26]
Okay, since you guys are hard-headed no listen anyway

[00:01:30]
Take the information that I'm telling you that this guy did the work

[00:01:34]
I'm telling you it was sick

[00:01:35]
He went back to like five years and all the majors and counted the bars and he really busted his ass proven

[00:01:41]
Himself because that's the way his mind works he put a lot of hours into the spreadsheet to prove

[00:01:48]
That second leg and where W spread out over five bars

[00:01:52]
Outside above or below the blue box a solid gold. I don't know how many times I could say it how many different ways

[00:02:00]
Now add some of the things that he didn't mention what if the W or M formation is part of a second leg top side or bottom side structure

[00:02:08]
Or what if it's at level three?

[00:02:11]
Where they hit the high slightly above and come back below those other things in there that I've taught you

[00:02:21]
Okay, what if second leg comes in off a safety trade off the peak formation

[00:02:29]
Okay, those are the things that will filter you out to the 90%

[00:02:33]
I

[00:02:35]
Know that people will tell you Steve. There's no way you can take 90% out of the market

[00:02:40]
This is too uncertain

[00:02:43]
If you guys haven't figured it out yet this business is rigged against the retail traders

[00:02:49]
The only difference is in here. We know how it's rigged

[00:02:53]
It's up to you to stop taking the shit that I showed you from the email and

[00:02:57]
Start taking the 85% plus trades that set up. I don't know how I can teach you all I can do is make you accountable

[00:03:05]
All right, I need you guys to step it up and trade strong

[00:03:08]
All right, thank you, Taehyun for adding that

[00:03:12]
We're also had a question TDI should want to be looking at TDI on the one-hour chart as well as the TDI on the 15-minute chart

[00:03:18]
Yes, and no if you want to look at the one hour chart, that's fine

[00:03:24]
But I want you to learn how to use the indicator on the 15-minute chart so you can understand and that we're gonna get to the drill tonight

[00:03:30]
How we're gonna fix that?

[00:03:33]
The drill is exciting man if you do it you're gonna have a good time

[00:03:39]
Wow

[00:03:41]
Some of you that know Gloria Goldman Gloria. I'm so proud of you. She had 90% for the week

[00:03:48]
It's fantastic

[00:03:53]
Okay, is the 50 in the TDI the same as

[00:03:58]
50 in the MA water no Greg

[00:04:00]
I don't know if I read that right, but no, okay

[00:04:03]
So be oh added in here I'd like to read it the problem on many traders with any indicators that they focus only on understanding

[00:04:09]
It's basic definitional formula even at extreme levels an indicator can mislead an

[00:04:15]
Indicators behavior to be helpful must always be understood in the context of the movements

[00:04:19]
What we want to catch we cannot escape the understanding of the pattern first in the indicator absolutely absolutely absolutely

[00:04:26]
How many times I got to say it pattern the pattern the pattern price action, okay, but

[00:04:34]
Understanding the indicator when the patterns present together collectively take you from 85% perhaps the 92.7. I think that's the knob kidding in the 90s

[00:04:48]
So I'm trying to tell you is that if you can see a trade set up

[00:04:54]
Which certainty that you know where it's gonna go

[00:04:57]
There's nothing better than that man

[00:05:00]
Those are the kind of trades that you don't have to be scared that you can put five standards on and say you know

[00:05:06]
What I'm on the 5% risk sides a little higher, but my goodness look at that structure. It's exactly Steve through it

[00:05:11]
Someone had a hundred percent win rate mark good job, buddy didn't take a lot of trades, but it doesn't matter

[00:05:18]
Do you guys remember point break I

[00:05:22]
Don't know I'm dating myself again. It was a surfer movie man was really good

[00:05:27]
Okay, if you haven't seen it you should watch it, but anyway

[00:05:32]
Keanu Reeves and the no longer with us

[00:05:36]
The hell's the guy's name Patrick Swayze, okay

[00:05:42]
Here's the whole point of why I brought it up

[00:05:47]
He was I think it was Bodie or whatever was had a surfboard and he was staring at the waves and he would just wouldn't move you staring

[00:05:56]
And Keanu Reeves walked up and he goes, what are you doing Bodie and he goes? I'm waiting for my set

[00:06:03]
So basically he was waiting for the perfect wave or the perfect setup

[00:06:07]
You got to be a surfer man. You got to wait for your set

[00:06:10]
You got to wait for the dealer to do exactly what I've illustrated for you and if he doesn't too bad

[00:06:18]
You don't take a trade I

[00:06:21]
Don't know how many different ways I can say it okay. I'm buying bracelets

[00:06:25]
I'm sending out monitors. I'm using surfer references. We had dr. Ken revisited to wait for your pitch

[00:06:30]
I don't know how many different ways I can convey to you that you got to wait for the dealer

[00:06:37]
To display the actions that I've illustrated for you

[00:06:40]
Okay, if you're bored you want to watch a good movie watch that movie on Netflix or the video or whatever

[00:06:46]
It's an awesome movie

[00:06:48]
But remember the part where he says what do you do and he's I'm waiting for my set

[00:06:53]
He's waiting for the waves waiting for the dealer to make the perfect opportunity for you to surf it into profit

[00:07:01]
Okay

[00:07:04]
All right now let's get to TDI

[00:07:09]
Look by the way

[00:07:13]
TDI does not belong to me. I didn't invent it

[00:07:16]
belongs to compass and Dean Malone

[00:07:20]
Okay, I've altered it or tweaked it a little bit

[00:07:23]
I

[00:07:24]
Like the RSI line to be set at 21

[00:07:29]
Why it just matches up with the average is a little better in lines up a price action for our purposes am I right am I wrong?

[00:07:36]
I don't know

[00:07:38]
Dean will tell you that I'm wrong says indicator that that's his right, but what I'm telling you as a group

[00:07:46]
The way it's preset in the templates is the way I want us to learn how to use it

[00:07:53]
Okay, 21 slows it down a little bit. You don't see as much noise smooth as the line

[00:08:00]
And it helps us see M's and W's more clearly than you would normally get on a more radical or a shorter period line

[00:08:07]
Okay

[00:08:09]
We're looking that means we're looking at 21 closing periods back for our for our line. We're averaging that out instead of 14 periods

[00:08:17]
Doesn't really mean anything semantics, but for our purposes in the group

[00:08:22]
I just happen to like it better that way you want to use it at 14 knock yourself out

[00:08:27]
Okay, so again TDI came from Dean Malone and compass FX. They're kind enough to let me use the slides. I appreciate it

[00:08:37]
But I think that's the only similarity we have we use it a little different I want you to understand how we use it for our group, okay

[00:08:43]
alright I

[00:08:46]
Used to use our side years ago, and I stumbled on to this indicator

[00:08:50]
from

[00:08:52]
I want to say I don't know if it was a group of traders my buddy. That's a rocket scientist some of you guys know them anyway

[00:08:59]
To me, it's a better RSI

[00:09:02]
It gives better signals and trade confirmations when used in the proper context of the market

[00:09:09]
It's powerful tool to scale in and add to your trade

[00:09:13]
or

[00:09:17]
It's a checkpoint if you will to stay with the trade

[00:09:22]
Using the TDI properly should help you build confidence in what you're seeing on the chart and

[00:09:28]
Again because of the band it identifies divergence pretty easily, okay

[00:09:37]
All right back up

[00:09:40]
This is Dean's definition a hybrid indicator developed indicate market conditions related to trend direction momentum and market volatility

[00:09:47]
Well, we know that we don't use this stuff

[00:09:51]
Okay trend direction that's fine

[00:09:53]
Momentum we know is bullshit

[00:09:56]
Momentum is usually stop hunt

[00:09:59]
Volatility is the speed of the candles during the stop hunt, okay?

[00:10:03]
It is in fact an all-in-one indicator and is very helpful

[00:10:08]
And listen man, I'm not I don't know that might have sound I'm not trying to disrespect Dean in any way

[00:10:13]
I think he's a great guy. I love the indicator. I use it on everything, okay, but for our purposes. I want you to understand

[00:10:22]
How we apply it to the chart in here, okay, and in the process. I'm not trying to disrespect anybody I

[00:10:29]
Certainly didn't invent an indicator

[00:10:31]
All right, I

[00:10:33]
Talked about the RSI line

[00:10:36]
The RSI line is simply the underlying indicator that the TDI is built upon

[00:10:45]
Okay for our group in here. Hey that the pen keeps falling off

[00:10:51]
We have this line set to 21 21 look back periods at all

[00:10:57]
Okay

[00:10:59]
And every time I see the slide it cracks me up because

[00:11:02]
This is my pattern right here if that was the box there's stop hunt low rise and there is

[00:11:09]
M formation divergence

[00:11:11]
Okay, and there's a W formation back into the range. All right, man. I can't care to wait. But anyway, I

[00:11:18]
Just talked about our side and explains to you how it works and what you're supposed to look for with the RSI

[00:11:22]
So now TDI is developed off of the RSI so there's your RSI line

[00:11:27]
What he did to take it a step further is he created a

[00:11:34]
Trade signal line or TSL

[00:11:37]
Okay

[00:11:39]
Someone asked me a few minutes ago about should I look at the one-hour chart? I'm gonna tell you a little secret about

[00:11:46]
the TSL

[00:11:49]
The TSL in essence is a polling of the one-hour chart

[00:11:55]
Brought into your view on the 15 minute

[00:11:59]
Okay, let me say it again so you understand the trade signal line pulls the one-hour chart and brings it into the 15 minute

[00:12:07]
So when you get a crossover right here in essence, you now have a signal on the one-hour chart

[00:12:18]
So you need to look at the one-hour chart not necessarily if you got a

[00:12:22]
Shark fin blood in the water

[00:12:24]
Blood in the water indicates that the one-hour signal one hour chart has fired a signal

[00:12:31]
At the same time or in

[00:12:34]
Congruency with the 15 minute chart

[00:12:37]
Day with me so far

[00:12:39]
Good because I'll you know if I'm with me

[00:12:42]
All right

[00:12:44]
So now our sideline green one hour trade signal line red

[00:12:50]
Bring it in

[00:12:52]
Okay, someone asked about this

[00:12:55]
This is a market baseline now. It's cool about the TDI

[00:13:01]
Okay, which brings it up to date is that on a standard indicator

[00:13:06]
The market basis line is fixed. It does not move it stays static on the chart

[00:13:14]
What Dean did is he took a moving average and

[00:13:20]
lined it up very close to price action

[00:13:25]
To give you a dynamic moving market basis line

[00:13:32]
Okay, you understand the gold line is a moving or liquid 50 so to speak, okay, there's your 50

[00:13:40]
Static on all under indicators except the TDI

[00:13:44]
So what happens is when you get a one-hour signal normally a trend change would be indicated on

[00:13:53]
price crossing above the 50

[00:13:56]
But because the market basis line went down there to meet the price action so to speak the signal came in here

[00:14:06]
instead of three or four bars later here

[00:14:10]
That's what's going on with it. You see that

[00:14:12]
Okay

[00:14:14]
The market baseline moved up the signal came in here instead of here

[00:14:20]
Okay

[00:14:24]
Now

[00:14:28]
The market baseline follows price action pretty closely

[00:14:33]
All right, you should be short right there should be peak formation safety trade short

[00:14:38]
Right inverted head and shoulders looking for longs

[00:14:41]
Right off of there and off of there. All right. I'm kidding around but they're in there

[00:14:49]
Okay

[00:14:53]
The market baseline

[00:14:55]
moves along with price in order to

[00:14:59]
meet

[00:15:01]
The signal lines several bars earlier

[00:15:07]
Okay, hope you guys understand that all right, so now

[00:15:13]
We have our SI set to 21

[00:15:18]
Blood in the water trade signal line TSL a moving liquid 50

[00:15:26]
And then he took

[00:15:29]
some bands that are very similar to Bollinger type bands

[00:15:36]
Okay

[00:15:40]
Because involuntarily bands I don't know the math on it, but I think it's very similar to Bollinger bands

[00:15:47]
There's some formula deviation 2% I don't know two standard deviations away from

[00:15:54]
The market baseline or something like that. I don't really know because I didn't invent it

[00:15:58]
But I'm telling you it's some formulation like that

[00:16:02]
Okay

[00:16:03]
They're essentially Bollinger bands

[00:16:07]
Based on the RSI line itself. That's what someone said telling me not sure

[00:16:12]
But anyway, it's two standard deviations away

[00:16:16]
from price action

[00:16:18]
Okay

[00:16:20]
From the RSI line. Thank you. Okay now

[00:16:23]
I want you to understand about the volatility bands is that they essentially act as support and resistance

[00:16:32]
But because they're based on the closing value

[00:16:36]
They're much stronger

[00:16:39]
and

[00:16:40]
Again, they won't fall for the spikes

[00:16:43]
When the bands contain the RSI line when the RSI line is inside the bands when it's contained after a break

[00:16:51]
It's divergent and usually in the stop-hunt segment. Okay. I'll show you a picture what I mean in a second

[00:17:00]
When viewed in the proper context

[00:17:03]
They can identify stop-hints scale ins and exits by using how the RSI line interacts with the band. Okay

[00:17:11]
All right, everybody with me so far. I'm trying to go slowly

[00:17:19]
I used to be talk a hundred miles an hour, but I want you guys to understand this stuff

[00:17:26]
Okay, cool

[00:17:28]
All right, so here's what I mean

[00:17:31]
During the Asian session price action was aggressive and the activity of that price action was outside the band

[00:17:42]
Okay, the next wave

[00:17:46]
The RSI line was contained by the band inside the band right out of the band in the band

[00:17:52]
Well, what happened the signal presented second leg?

[00:17:57]
Almost immediately on the next run towards the high

[00:18:02]
Okay, so now notice they shifted the zone. We're still all the other criteria there 58 trend is up

[00:18:10]
Line's just starting to come back together

[00:18:12]
The dealer makes an aggressive move towards the high out of the band

[00:18:17]
He makes another move towards the high, but that move is closing below the band and closing lower RSI based on the closes

[00:18:26]
Above the support resistance line below the resistance line out of the band

[00:18:32]
Inside the band contained by the band those are parts of the signal that you need to be identifying with

[00:18:40]
Okay, then the dealer member

[00:18:43]
The second wave and he broke out of the band and there's your perfect M formation that ended on two hammers

[00:18:53]
If your stop was above the high if you entered here or here, you were still good, okay

[00:19:02]
Okay, so

[00:19:05]
TDI signals

[00:19:10]
Starts off when the market's quiet during the Asian session you have a tight 50 pip range 35 pips perhaps the bands will be tight RSI

[00:19:20]
Bones or bands will come to rest and be tight

[00:19:23]
The RSI line breaks out of the band and comes right back in

[00:19:28]
This is where we get the shark fin from why the dealer makes a vector candle the vector candles will force the RSI line

[00:19:36]
outside of the band

[00:19:37]
Then when the dealer pulls back off of the high or off of the low it causes the RSI line to turn back over

[00:19:45]
and

[00:19:47]
Create the sharks dorsal fin, okay?

[00:19:51]
And since the band is colored blue for our purposes

[00:19:55]
It looks like the shark fins coming out of the water. That's where it came from shark fin

[00:20:00]
When the fin goes back under the water line back inside the band and

[00:20:07]
crosses the signal line to trade signal on TSL

[00:20:10]
That's where we get blood in the water

[00:20:14]
So it almost looks like the shark swimming around his fins and showing above the water and he takes a bite out of somebody's leg

[00:20:21]
In this example, I like to think it's the dealer's legs

[00:20:26]
We put blood in the water. We got a good solid confirmed entry

[00:20:30]
Okay, let's look at a picture

[00:20:36]
Okay, here we go

[00:20:38]
Very tight, right? Nothing going on nothing going on nothing going on

[00:20:41]
I want you to notice that the entire structure is slightly above

[00:20:47]
Slightly above RSI line slightly below finding resistance at the mid level

[00:20:54]
When the shark fin fires it goes to the extreme

[00:20:59]
Band very important part

[00:21:03]
Being in the right segment of the market

[00:21:07]
Okay

[00:21:09]
The dealer vectors exactly like I taught you he extends the Asian range

[00:21:14]
Possibly one two inside that one big candle and then a little tiny taps to the high three

[00:21:19]
Once you three to the high forms the shark fin

[00:21:22]
He shifts back and goes into consolidation

[00:21:26]
There's blood in the water and he's back inside the band

[00:21:30]
This price will correct

[00:21:32]
And you get your waves one

[00:21:35]
Two and then the downside outside three

[00:21:39]
starts waving

[00:21:41]
Okay, now you're back to the other side the extreme start looking for the door

[00:21:49]
Okay, all the other stuff is still in effect

[00:21:53]
31 pip Asian range start of the day the shadow box would be right here by the way, but

[00:21:58]
This was before we coded the shadows

[00:22:02]
Okay

[00:22:05]
Same thing

[00:22:06]
Shark fin long it's the exact opposite criteria

[00:22:11]
Okay

[00:22:12]
This is not a freaking long trade because it hit the Asian box twice

[00:22:18]
All right, I want you to notice what happened here the dealer extended the low and three moves he hit it

[00:22:27]
One he held it for 45 minutes

[00:22:30]
He hit it again and he hit it again and then he took it all right back in one swipe

[00:22:35]
There's a railroad tracks notice the RSI line is below

[00:22:41]
Below the support level, but only for a moment and what's pretty cool is when the railroad track closes

[00:22:48]
You get blood in the water and it crosses back inside the band at the same time right there

[00:22:55]
bad line right there

[00:22:57]
All those things occur

[00:22:59]
In conjunction with the railroad tracks with all the other criteria in place 37 pips three vectors to the low

[00:23:08]
Railroad tracks an overextended TDI

[00:23:12]
Pass the support band

[00:23:15]
Okay

[00:23:17]
So now you have two setups what do you have shark fin short shark fin long?

[00:23:24]
based on the TDI

[00:23:26]
So the shark fin long is the same criteria. We just talked about it's just inverted

[00:23:30]
The setups got a coincide with the under other indicators when I mean by that as I mean

[00:23:35]
Are you in the right phase of the market is it two to four o'clock in the morning eastern time?

[00:23:41]
Is it London open?

[00:23:43]
Is the blue box 25 to 50 pips is your tight trading range?

[00:23:48]
And you got to be in the right cycle of the market

[00:23:51]
Are we in the stop-hun zone or we at the time when the dealer makes the stop hunt or is that just two o'clock in the afternoon?

[00:23:57]
And I see an M or a W and TDI looks like it might give me something

[00:24:00]
I'm gonna take it. No, you've got to be in the right parts of the cycle

[00:24:08]
And you got to be at the right timings to have all these things come together

[00:24:12]
That's part of a confluence of events

[00:24:17]
Where things need to come together

[00:24:21]
Pattern the pattern the pattern the timing the levels confirmed by TDR moving averages other things three vectors out of the box

[00:24:29]
These things all have to come together at that moment in time to issue you a clean trade

[00:24:36]
And I need you guys to stop taking crap and I need you to trade strong

[00:24:40]
Okay, all right, so this is a V-bottom

[00:24:48]
But if you notice

[00:24:55]
What confirmed it here, okay, grab the pen 21 pip Asian range

[00:25:03]
Okay, look at this boom shoulder head shoulder

[00:25:10]
Okay

[00:25:12]
the same time

[00:25:14]
That the dealer issued a hammer he put blood in the water and came back below back inside the band shark fin low

[00:25:23]
Cross over blood in the water, which means you had a signal on the higher time frame at the same time

[00:25:28]
You are below you are below

[00:25:32]
The band

[00:25:34]
What is being below the band means it means that this should happen?

[00:25:38]
That you were probably in level three because in order to get down to the extreme extreme extreme on TDI

[00:25:48]
You have to be

[00:25:51]
Or have been dropping for a few days two and a half days three days four days in order for you to be passed

[00:25:58]
The low support band and be at this far of an extreme

[00:26:02]
You

[00:26:04]
Got to be below

[00:26:06]
Got to have been dropping

[00:26:09]
Okay

[00:26:11]
Shark fin hold the mail right it's like a sandwich

[00:26:17]
Here's what I want you to notice

[00:26:20]
If you add an extra filter like my friend Zaim had mentioned perhaps a 200 EMA

[00:26:27]
Some other reason

[00:26:35]
To confirm the trade

[00:26:38]
Spike to the mannees would be it you should have flashcards illustrating this I want you to notice

[00:26:46]
This is almost like a little baby safety trade within there within the same day cycle

[00:26:51]
Here's what you got you got a nice shark fin to the low

[00:26:54]
Right past the mannees almost like the mannees offer support

[00:26:57]
But the dealer spikes passed it a couple of times and notice how he closed below

[00:27:03]
twice

[00:27:04]
closed above and then shifted it away

[00:27:08]
Okay, close above once and then shifted away why?

[00:27:10]
To stop just draw people in and to thinking people remember people take a close below the 200 as a trade signal

[00:27:19]
He grabs them

[00:27:21]
Okay, he pulls away you're in profit your entry should be here

[00:27:26]
You're in profit for a while he comes back to the level but notice the mannees has risen

[00:27:32]
Notice he's out of the band and he makes the next formation inside the band

[00:27:36]
There's your secondary signal if you haven't scratched out. That's a secondary entry because in essence this is a

[00:27:43]
Big fat w

[00:27:45]
How do I know that the trend is up?

[00:27:51]
Because you're in day two of the cycle

[00:27:54]
You're below below below below the band

[00:27:59]
Slightly below this is the this is the 50 and I'm sorry. This is the 67. This is the 50

[00:28:04]
That's why I took that picture. Sorry, but what did I tell you he does it when he oscillates slightly below support

[00:28:12]
second leg

[00:28:14]
Below the support but not to the not to the other band not quite to the other band slightly below

[00:28:22]
Outside the band inside the band. These are the things you need to be looking for when you're looking at the indicator, okay now

[00:28:30]
Simple enough. It's not complicated. It's not a lot of stuff outside the band inside the band got them m formation a

[00:28:37]
Divide I divergent m or w formation with the TDI RSI line itself good enough got them

[00:28:45]
Okay now

[00:28:46]
Lot of you in the US don't scale in that's fine

[00:28:49]
It's hard with the low leverage and all the other garbage going on

[00:28:52]
But those you that still have the luxury of higher leverage you can scale in with TDI and you can take a typical run and elevate

[00:29:00]
the gain

[00:29:02]
That's available to you

[00:29:05]
Okay

[00:29:10]
Here's how you used TDI to scale in or add to your trade

[00:29:16]
And if you don't add to the trade

[00:29:21]
You simply use these markers as

[00:29:26]
Reasons to stay the trade, okay, so you're in the right segment of the market. You know what I'm talking about

[00:29:31]
There's only three segments of the market, right? What are they anybody?

[00:29:35]
I

[00:29:36]
Consolidation

[00:29:39]
Accumulation

[00:29:41]
What are they anybody remember?

[00:29:43]
No one's typing that fast

[00:29:47]
Okay, I'll wait I should have put a monitor on it and see the first one answered, okay?

[00:29:51]
Anyway, yeah all of a sudden everyone's typing now. Ha ha okay

[00:29:55]
All right, you're in the right segment of the market

[00:29:58]
Where are you in the market? Is it trending or are you trying to go against the trend or are you in the stop hunt?

[00:30:03]
Are you in the right segment of the market prices inside the channel you're in consolidation?

[00:30:08]
Okay prices in the channel the RSI line breaks outside the bands as a stop hunt

[00:30:13]
You know how do I know it's between one and four in the morning the beginning of the Asian session or it's between eight and

[00:30:20]
10 in the morning started the US session

[00:30:23]
Our sideline breaks outside the bands as a stop hunt the reversal is imminent

[00:30:28]
You're looking for the signals that coincide with the setup

[00:30:33]
Enter the trade stop lost 23 pips above the high or if your second leg trader

[00:30:37]
And you got a nice tight second leg seven to ten pips above the second leg because he ain't coming back, baby

[00:30:45]
You add to the trade at the market baseline break

[00:30:48]
member the gold baseline the gold line and

[00:30:52]
You add again at the vertical volatility band break

[00:30:58]
You will exit all units

[00:31:00]
When the he returns our sideline returns back inside the band, okay, let's look at a picture

[00:31:12]
Okay, here's what I'm talking about

[00:31:17]
Look what happens here. You have a 28 pip Asian range perfect

[00:31:22]
Price comes out and it's held by the man is perfectly

[00:31:27]
Tell by the 200

[00:31:30]
Okay shark fin to the high side

[00:31:34]
It crosses back in the same side you get blood in the water beautiful signal. There's your entry, okay?

[00:31:40]
The R sideline crosses back inside the water and the blood at the same time the blood happens to line up with the band

[00:31:47]
It's beautiful

[00:31:49]
Okay, it crosses the market baseline

[00:31:52]
Right around the same time it also crosses the static 50 pretty cool

[00:32:00]
Add your trade right here. Here's your initial entry. There's your second order placed

[00:32:06]
okay, it breaks outside the volatility band and

[00:32:11]
Almost is heading our sidelines pointing straight down

[00:32:15]
Standing on its head man if it's standing straight down

[00:32:18]
You're in trend acceleration. It's gonna start to run beautiful

[00:32:23]
You're in you get a nice shift

[00:32:26]
Right to the logo's in the consolidation

[00:32:29]
Coming off a level one

[00:32:32]
The dealer comes back inside and it calms down and crosses all the same criteria take your exit right here

[00:32:39]
That's a nice overnight London trade

[00:32:41]
About eight to ten hours eight hours on that

[00:32:44]
Okay, and you were able to take the run and

[00:32:48]
Escalate it or add to it two more times. So you would take

[00:32:53]
Camera with this was but it's a 400 pip total, but I think you'd let's say this was a 200 pip run

[00:33:00]
Then you got a hundred and fifty

[00:33:03]
And then maybe you got 75 or so. I don't know if that equals 400 but close enough to them saying

[00:33:09]
You know you got the right direction

[00:33:11]
You

[00:33:13]
Can add to the trade as it progresses you get the crossovers here angle and separation on the averages when it all comes back together and collapses inside

[00:33:23]
There's your stop hunt and bolt directions clean it out and then it continues

[00:33:27]
But again if you came to work here surely by here you're exhausted. That's a nice run overnight

[00:33:35]
Okay

[00:33:37]
TDI offers a few key points to scale them with after entry is made I went over this

[00:33:45]
But here's the writing add to your trade on the gold line the market baseline break

[00:33:51]
add again on the volatility band breakout not during the stop hunt but during the actual trend run and

[00:34:01]
Exit all units on

[00:34:03]
Volatility return back inside the Bollinger bands, okay?

[00:34:07]
When our sideline returns back inside the bands the excitement's over it's calming down

[00:34:15]
Okay

[00:34:19]
Another example this came to me from my good friend that

[00:34:24]
Who graduated Harvard business school and he's hanging with us. Okay, very cool. Love that. All right. Check it out, man

[00:34:30]
First first sign boxes a little overblown not the end of the world, but yesterday's blue trace remember add some signals

[00:34:40]
Divergence look high

[00:34:42]
flat

[00:34:44]
Hey, look how high that diverges

[00:34:47]
Okay now shark fin to the extreme

[00:34:54]
To the high side of the band right to the band, okay took his first order

[00:35:00]
The dealer shifted set the high shifted right back below

[00:35:07]
Close here he took his first order

[00:35:11]
It pushed down again

[00:35:15]
There's

[00:35:18]
Crossing of the gold right here. See the gold market baseline across

[00:35:22]
Okay, he added it broke outside the band right here. See it broke out right there. He took it again

[00:35:30]
It made a nice run hundred ten hundred and sixty-eight pips on each one of those orders

[00:35:37]
Right it made the pullback here I think this would have been a little bit better entry understanding how it pulls back to the to the

[00:35:42]
Manate's but it's still good man. It's beautiful

[00:35:45]
Add to the trade there took a little heat on that third order and then when it went into consolidation

[00:35:51]
Notice how TDI went back inside

[00:35:54]
And I want you to see something pretty cool. This is one of my favorite TDI charts. I'm gonna show you why

[00:36:01]
Look at TDI man

[00:36:03]
one

[00:36:05]
two

[00:36:07]
three

[00:36:09]
Doesn't it look like it looks like I drew it

[00:36:12]
Three levels man perfectly look at that

[00:36:15]
See it one pull back to pull back three three pushes a price action

[00:36:21]
Three

[00:36:23]
Three pushes a price action

[00:36:26]
Inside and outside the band's beautiful man if there was a textbook for TDI I just think there is that should be on there

[00:36:33]
Structures beautiful

[00:36:35]
Okay

[00:36:37]
And then notice how the dealer in this second leg right here

[00:36:40]
Look if you took this W formation back into the range the dealer came slightly below the market baseline on the second leg

[00:36:47]
Slightly below remember slightly below and then put blood back in the water

[00:36:54]
It's beautiful okay, then look what you have

[00:36:59]
It finds the RSI line fine supported the extreme band during the Asian session

[00:37:05]
This is 75th. It's blown out, but

[00:37:07]
See it RSI lines here and here it's a multi-session RSI W

[00:37:14]
Ah sneaky you didn't even know that existed digit all right here you go again

[00:37:20]
Another setup shark fin long hold the mail the dealer works the man is

[00:37:27]
Okay shark fin to the to the band to the extreme to the band blood in the water. That's the signal

[00:37:34]
Right in here blood in the water crosses the market baseline

[00:37:39]
Okay, if you're not adding to the trade this is the reason to stay with the trade

[00:37:45]
Okay, a lot of people wrote you Steve. I believe you I see it, but when I'm in it in real time I get scared

[00:37:53]
And I bow out

[00:37:57]
I click out with plus 10 plus 15 plus 20 because I just get scared okay, I understand

[00:38:05]
But these are the reasons to stay the trade when it crosses the baseline when it breaks outside the band

[00:38:12]
These are the reasons to stay use them as checkpoints if you will

[00:38:16]
Yeah, I think I told you just before you guys remember that stupid game

[00:38:18]
I think it's called cruising and it's like you drive the car you put a quarter in and your wife plays head to head with you

[00:38:24]
And the other one in your racing there's like chicks waving flags and all that I think Luther remembers that and then

[00:38:30]
Okay, well remember when you get like past the thing it goes checkpoint

[00:38:34]
All right, and you're going through and then it says it like the whole time like the squeaky voice and it goes checkpoint like that, right?

[00:38:40]
Okay, well, these are your checkpoints if you're in a trade and you're scared if

[00:38:45]
The dealer made the low and he hasn't broken the low

[00:38:49]
How do you stay with the trade?

[00:38:51]
Okay shark fin blood in the water got my trade man the trade looks good, but man's coming back towards the low darn

[00:38:57]
Hey, guess what it just crossed that gold baseline. I'm still good

[00:39:02]
It's going it's going man. It's coming back a little bit. I'm scared wait a minute

[00:39:05]
It's just one outside the volatility band checkpoint. I'm still good. Let me hang out with this dude for a while

[00:39:11]
See if it hits the 50

[00:39:13]
Now if you're at 48 pips and it comes back inside the band and hasn't delivered you better take your profit

[00:39:20]
Okay, I guess when it hit when it comes back inside the band I know in this example it went on higher

[00:39:27]
but

[00:39:28]
When it calms down so to speak and comes back inside the band

[00:39:33]
You should have hit your limit by now if you got three bursts and it comes back inside the band

[00:39:39]
You should be plus 50 you should take your profit if you're at 48 or 45 or 52 take it

[00:39:45]
A lot of times it will indicate the reversal if you notice it comes back in and then it makes one more push

[00:39:51]
And it looks like it's gonna come down, but it does not

[00:39:53]
But

[00:39:55]
This is enough for you to live off of right here my friends. This is enough

[00:40:00]
This structure right here is enough

[00:40:02]
Can't emphasize that

[00:40:07]
Okay a couple more examples. I just want you to see this is example with railroad tracks, okay, this is the formation

[00:40:16]
comes out railroad tracks below

[00:40:19]
Look at the W across the baseline shark fin at the same exact time

[00:40:26]
Okay variation on the theme just understand there's gonna be variances, but I should took these slides out because in here

[00:40:33]
I don't want you to have any variations. I want you to trade a certain way

[00:40:36]
Okay, look

[00:40:38]
Beautiful structure laid out perfectly market makers hit the stops

[00:40:43]
There's your entry on the hammer shark fin high look outside the band

[00:40:50]
Inside the band shark fin blood in the water

[00:40:54]
Outside the band inside the band the dealers shifted up consolidated high hit it again

[00:41:02]
Above the box

[00:41:05]
Add

[00:41:06]
Goes into level one consolidation. It's the stops. It's the stops drop add you got a break outside the band

[00:41:14]
Add and I want you to look at something pretty cool on the exit

[00:41:18]
Shoulder head back inside the band kind of a shoulder not really

[00:41:26]
Okay, sometimes the head and shoulders will be perfect, but you're below the band

[00:41:29]
Okay, cool, all right, so if you're not scaling in I want you to use the same signals

[00:41:41]
I just illustrated for you to stay the trade

[00:41:48]
We call it checkpoints right I was joking around told you how to do it your

[00:41:51]
Confirmation is to hold on or to let you know when to look for the exit just it helps you stay with the trade. That's all

[00:42:00]
Okay

[00:42:02]
now

[00:42:05]
Here's what I want you to do this is this is good stuff this week

[00:42:09]
Find and identify the trade signals. I just talked about using TDI

[00:42:15]
Use any pair you like

[00:42:19]
Black out the price action and check and see your knowledge. I want you to do about four of those

[00:42:23]
I'm gonna post it

[00:42:25]
You guys know that in the forum I post in the homework section, right? I'll go over that before I get off tonight

[00:42:29]
Let me make a note of this. I don't know if you knew this or not. I didn't mention it

[00:42:33]
I forgot to mention it last week, but if you go under my section

[00:42:37]
It says assignments are in here, so when I give the assignments

[00:42:41]
I turn around like when I run it off this webinar right now. I'm gonna post this assignment in the forum

[00:42:47]
So if you go, oh, what does he say to do? I forgot it's gonna be in there

[00:42:51]
Okay

[00:42:55]
All right, so now

[00:43:00]
Black out the price action and try to identify

[00:43:05]
The TDI signals I want you to do five of those on any pair you want any date ratings you want now

[00:43:11]
Here's the fun part after you mark it up and think you see it pretty good. Here's what I want you to do

[00:43:18]
This is a must-do for everybody in here if you do this I guarantee you you're gonna elevate yourself to the next level

[00:43:24]
You're gonna trade strong in demo. I have to say it a hundred times demo demo demo demo open up a

[00:43:33]
$10,000 demo account

[00:43:36]
Okay

[00:43:37]
Do not skip this drill take everything off of your chart and including the candles everything

[00:43:45]
Take the TDI and stretch it out the size of your screen

[00:43:51]
Okay, I

[00:43:53]
Want you to execute five live demo trades using nothing except the TDI as the signaling device as the criteria to enter and exit the market

[00:44:03]
nothing else

[00:44:05]
Don't cheat don't look at candles if you can't black your shit out put a piece of paper over your screen except for the bottom grid

[00:44:13]
And I want you to be accountable to everybody in this group. I want you to record the result

[00:44:18]
Take a screenshot of mark up the TDI after it's over and see how you did post it in the forum. I

[00:44:26]
Promise you it's gonna be fun. I've done it

[00:44:29]
It's gonna take your use of an indicator to the next level

[00:44:33]
Because you're not gonna see what the price is doing

[00:44:36]
You're gonna trade just based on the closes and you're gonna see if they get you a divergence if you can catch the second

[00:44:42]
Leg and you could understand the pushes with inside the TDI

[00:44:45]
Okay

[00:44:47]
Promise me you're gonna do this one promise me say right now pinky swear. I'm holding my pinky up if my webcam was on

[00:44:53]
I'd you'd see my pinky right now. It's elevated to you guys

[00:44:57]
Do this one this week?

[00:44:59]
It's really a good drill

[00:45:02]
Okay

[00:45:03]
Take everything off alright Don Dave Pradeep got you guys Casey

[00:45:08]
Take everything off your chart

[00:45:11]
except

[00:45:13]
The TDI

[00:45:15]
and

[00:45:17]
Your wristwatch

[00:45:19]
Okay

[00:45:20]
TDI wristwatch wire wristwatch because I don't want you trading

[00:45:25]
TDI signals at two in the afternoon

[00:45:27]
You're allowed to use your your wristwatch and the TDI nothing else like tonight if you're gonna do it tonight

[00:45:33]
Set up your screens now

[00:45:35]
So when you come on you don't see any other shit on there and it doesn't give you any kind of clue which way it's going

[00:45:43]
Post under my homework section in the forum

[00:45:46]
Okay, I'm gonna try to get that cleaned up tonight or tomorrow

[00:45:49]
I know it's gotten out of control a lot of you've posted and I and I want you guys to be accountable

[00:45:54]
I should make it I should make subtitles for each week for the homework. I'll do that tonight

[00:45:57]
I'm sorry. I said I was gonna do it and I forgot

[00:46:02]
Okay, so listen

[00:46:04]
Tonight take everything off your chart except TDI grab the subgraph and stretch it out. It's a fun thing to do

[00:46:11]
I'm telling you it's pretty cool, man

[00:46:13]
Put your wristwatch on and

[00:46:16]
I don't care if you trade euro if you trade one or two

[00:46:19]
Why don't we do this? Why don't we take?

[00:46:21]
Why don't we narrow down to two payers for the actual live trade so we're all trading the same shit?

[00:46:27]
Okay, let's do euro USD

[00:46:29]
and

[00:46:31]
GVP USD let's look for setups TDI only yes, I mean no candlesticks just TDI man yes Dean

[00:46:42]
Okay, so what I'm asking you to do is to take put those two pairs side by side

[00:46:47]
Black out your candles hang a piece of paper over your screen put a pillowcase on it

[00:46:52]
I don't care but all I want you to see is the TDI itself and

[00:46:58]
I want you to literally execute a demo order

[00:47:02]
Long or short based on what the TDI you see in the TDI and I want you to do it at least five times

[00:47:08]
If you're having fun with it do it more

[00:47:12]
And I want you to post

[00:47:14]
the results

[00:47:16]
In the forum say hey I took this TDI and this is what happened

[00:47:21]
I got stopped out from divergence or I got stopped out because of this or I was able to pick up a hundred pits trading off

[00:47:27]
That because I counted the three waves when it broke out the band and when I went back in I exited and got

[00:47:33]
87.275 pits

[00:47:36]
Okay, water was kind enough to tell us how to do this

[00:47:39]
Maybe I'll post that in the forum make it sticky says make the candles invisible

[00:47:44]
Set to line graph instead of candles

[00:47:48]
or bars then F8 for properties and give the line graph the same color as the background color. Yes, that's how you do it

[00:47:57]
Okay

[00:47:59]
Yes Whitney do five or ten trades if you can't get to ten if you're too busy if time doesn't permit I

[00:48:06]
Want you to trade euro USD and GBP USD

[00:48:12]
Using only

[00:48:15]
The TDI what size stop loss Aaron you tell me what size stop loss

[00:48:24]
Do you think you caught the second leg it should be what?

[00:48:29]
Okay, sounds like a good guess

[00:48:31]
Some are saying 10 23 25 you guys take a guess figure it out

[00:48:41]
This is how you learn you're experimenting you're playing you're learning how to read an indicator flawlessly

[00:48:50]
By putting some demo money on the line

[00:48:54]
Seven ten sounds great if you get a second leg in the TDI and you want to execute an order

[00:49:02]
All right, I'm telling you you're gonna have fun with this and I promise you it's gonna help you learn how to really read an indicator

[00:49:08]
And I got it to tell you and I'm not very few people I've ever met other than dragging it on their chart truly know how to read an indicator

[00:49:17]
This will teach you

[00:49:19]
Had a trade off the indicator blind now imagine this

[00:49:23]
You hit five out of five or nine out of ten using the indicator and then you add the few other nuances of price action

[00:49:31]
You hit seven out of ten using an indicator alone then you could visibly see price

[00:49:36]
Think about the difference in your trading think about what will happen

[00:49:42]
Okay, you ever see when they train rocking to be the other hand to keep his right hand

[00:49:47]
They trained him to be left handed or something. No, he was a south fall

[00:49:49]
They trained him to be right-handed. What do they do? They tie one of his arms up?

[00:49:55]
I'm tying up one of your arms price action charts candles can't see them I

[00:50:01]
Want you to learn to trade with the other hand

[00:50:05]
Okay

[00:50:08]
Live markets in demo live markets in demo mosh I

[00:50:13]
Want you to do this on a demo account. I want you to execute the orders

[00:50:19]
Using nothing but TDI don't cheat man. You're only cheating yourself if you look at the candles. It's fun. Trust me

[00:50:26]
All right, it's getting late. We got four minutes to go. I want to make a couple of announcements. Tell you what's going on in the world

[00:50:32]
Okay

[00:50:33]
announcement one

[00:50:35]
Car is working on your Lando meet it up and I mentioned this to a couple of people and it took off. It's got legs

[00:50:42]
If he's able to get it lined up, I'm gonna go. It's only about an hour and a half from my house. I'm gonna ride over there

[00:50:49]
What I'm thinking about doing is

[00:50:52]
We're gonna set up an additional training out of it somehow it's gonna be on a Saturday

[00:50:57]
I know you guys got better things to do than hang out with me on Saturday, but we're gonna stream it and record it

[00:51:04]
We're shooting for April 21st

[00:51:07]
Zen is trying to lock the venue up

[00:51:08]
We're trying to do it at Stetson University if it's available because it's a stadium seated venue

[00:51:16]
Okay, but I don't want you to get excited that we're trying to get it all worked out right now

[00:51:20]
It's wishful thinking but we're gonna try to make it happen. I'll keep you posted

[00:51:24]
Here's the deal if I get it this week

[00:51:26]
Zen's gonna try to lock up a venue for us if he gets it and I get everything locked down car gets his tickets Ray wants to come all

[00:51:33]
That stuff. I think Jim Nicholson supposed to see if he can make it. I

[00:51:37]
Don't know if Kim K is gonna make that long of a trek to hang out with us for a day

[00:51:41]
It's too far for her. I wouldn't expect her to but if she's bored and she wants to fly over here and see how hot it is

[00:51:46]
she's welcome

[00:51:49]
Anyway, as soon as I know we get it locked up. We're gonna hang out Saturday and Friday and Saturday and

[00:51:55]
Do a live meet up in Orlando and we're gonna stream it and record it for those you can't make it, okay?

[00:52:02]
All right next

[00:52:04]
I'm preparing some lessons for the DMR. I'm gonna be teaching a few times a month on the other side for the paid subscribers

[00:52:11]
I'm gonna spend some time in there with those people that have been in there and have been I guess tried and true and hung in there

[00:52:18]
I'm gonna get in there and work with those guys a little bit and offer some assistance on that side of the business and help them out

[00:52:25]
Okay, I'll let you know stand by don't know what I'm gonna teach yet, but I'm working on some stuff and

[00:52:31]
We'll get it in there. Okay. All right next

[00:52:36]
All right

[00:52:38]
I'm working closely with the venue in New Jersey

[00:52:41]
Stevens University or Steven Institute were there last year. It was great

[00:52:44]
We're trying to lock up the dates

[00:52:47]
I'm looking at like mid June

[00:52:50]
Maybe sooner. I don't know that's when they have availability sometime in June. I'm looking like I don't know like the 20th 21st

[00:52:57]
Something like that trying to coordinate it away from 4th of July not on Memorial Day all that stuff

[00:53:01]
So I know everybody goes on vacation and stuff

[00:53:05]
But what I'm gonna do is what I always do for you guys

[00:53:09]
I'm gonna deliver a web class two weeks three weeks before I go to New Jersey before I go to my trip to New Jersey

[00:53:16]
So I'm looking at maybe late May first week in June to do a web class for everyone as a retake

[00:53:24]
And then I'm gonna go over to New Jersey and we'll hang out and eat some pizza and

[00:53:30]
Do a live event, okay?

[00:53:33]
As always everyone is welcome. Do you tell me you're coming you got a seat

[00:53:38]
Excuse me, I'll post the details as I lock down the availability

[00:53:44]
I'm hoping to know something this week because I don't want to leave everybody hanging

[00:53:48]
I know some of you from the other side of the world need to get a visa and permission to travel over here

[00:53:53]
So as soon as I know I'll send out an email announce it posting in the forum

[00:53:57]
I'm hoping to get the meetup and the New Jersey venue locked down this week

[00:54:03]
So we can hang out together for our summer

[00:54:06]
Summer fun. All right

[00:54:09]
And I think I had one more

[00:54:12]
Announcement, but I don't think I made a slide for it. Yeah

[00:54:15]
Worktime ribbon

[00:54:17]
Everyone's asking me what the hell's going on with that

[00:54:19]
Dick Schmidt sent me over one that I liked but I think it was too complicated for you guys and I don't mean any disrespect to anybody

[00:54:26]
But because of the variance and brokers I wanted the lines to be in a certain place

[00:54:32]
Ray is working on recoding the existing one

[00:54:35]
To where it just hits the sideline and is fixed and then I also received the clock from dick

[00:54:41]
That will tell your brokers offset and you can make the adjustments. I haven't forgotten about it

[00:54:46]
I just thought it would be a lot simpler to throw it in there

[00:54:49]
But again, I don't want to just throw some shit up there and then it's not working for you guys

[00:54:53]
And then we go back to where we were same problem, so I'm trying to make sure it's a hundred percent right

[00:54:58]
Before I get it out if you need

[00:55:02]
The old student folder if you like man, I lost my indicators. I need the old template

[00:55:06]
Send me an email or send an email and we'll get it out to you. Okay, say hey need the old student folder

[00:55:11]
I'll mail you the old one, but when I finally get it right. I will post the new one in the form, okay
