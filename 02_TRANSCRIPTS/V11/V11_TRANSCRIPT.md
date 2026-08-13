# V11 — TRANSCRIPT

## SOURCE

| Field | Value |
|---|---|
| Video ID | V11 |
| Original filename | `Bootcamp1 Wk4 040812 Part1 (51mins).swf` |
| SHA-256 | `606cc5a89a0a68aa08c18423342288307d267b65ebb79acd889e48af8c4d2101` — re-verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session on the flat `Bootcamp/` canonical path, **and re-verified again after the frame-rate patch** to prove the original was not modified (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| Duration | 00:50:56 (audio measured **3056.927347 s**; SWF header **9,171 frames ÷ 3.0 fps = 3057.0 s**; `SOURCE_MANIFEST.md` 00:50:56 = 3056 s — three independent figures, agreeing to within 1 s) |
| Lesson title | **NOT PRINTED as a topic title.** The speaker opens *"welcome to week four of market maker boot camp"* `[00:00:00]`, and names the day's subject in speech at `[00:25:38]`–`[00:25:43]` — *"let's get to today's lesson"* → *"TDI"*. **That is the lesson's own title for itself and it is a spoken one, not a printed one.** The quarantined per-lesson header's *"Primary Topics: High of Day (HOD) & Low of Day (LOD) Creation, 2nd Leg Peak Identification"* is fabricated — see `QUARANTINE_REGISTER.md` **Q-012** |
| Session date | **2012-04-08**, from the filename `040812` and `SOURCE_MANIFEST.md` — **and independently corroborated inside the recording**: `[00:25:33]` *"I figured it was sunday and it was easter i figured i'd get preach on you guys"*. **Easter Sunday 2012 was 8 April 2012.** The spoken *"week four"* `[00:00:00]` independently corroborates `D-017` §2's ordering for this file |
| Frame rate | **3.0 fps** in the SWF header — read from **this file's own header**, not assumed. V10 declared 2.0; V11 declares 3.0. The `SWF_CAPTURE_RECIPE.md` §10 patch for a 10× sweep is therefore **3.0 → 30.0** here. Recorded because §10's corrected text (open item 87) requires the field be read per file, and this file is the demonstration that the variance is real in both directions |
| Stage size | **1024 × 786** — the majority class. `GOTCHA 5`'s table gives `(512, 300)`, and the pre-click/post-click guard **confirmed it fired** rather than assuming it (`sweep.log`: *"play click confirmed: stage changed"*) |
| Transcribed by | ASR, by a pre-ingestion session. Copied and verified 2026-08-13 — see VERIFICATION below. The pre-ingestion file's own `# VIDEO` header block is **NOT carried over**: its *"Course Position: Video 12 of 21"* is wrong under `D-017` §2's renumbering, and its *"Primary Topics"* line is unsourced. Only the verbatim body is copied |
| Transcription confidence | **MEDIUM–HIGH.** Well-segmented and internally consistent; the defects are ordinary ASR mishearings of domain vocabulary, enumerated below |

## SPEAKER TABLE — MANDATORY UNDER `D-025` consequence 3, re-adopted by `D-033`

| Speaker | Runtime | Basis |
|---|---|---|
| **The course author (Steve Mauro)** | **100% — the whole file, `[00:00:00]`–`[00:50:56]`** | See § SPEAKER IDENTIFICATION |
| Any guest | **NONE** | No second voice; no handover language anywhere in 51 minutes |

**Two named third parties appear and NEITHER speaks:** *"Subio"* `[00:00:12]` (ASR, spelling
unverified — greeted, and his trading result is reported *by the speaker*), and *"doc Ken"*
`[00:17:38]` (a presenter at a **different** session that week, referred to in the past tense).
`[00:00:12]` *"Subio. How you doing buddy?"* is a greeting into a chat box, not a handover; the
next line is the same voice continuing. Recorded because a name in a transcript is the commonest
false positive for a second speaker.

## SPEAKER IDENTIFICATION — HOW IT WAS ESTABLISHED

`D-033` makes every speaker's material equal in authority, so this determination changes **no
rule's weight**. It is provenance, and `D-025` consequence 4 binds: **nothing in any V11 artifact
depends on the identification being right.**

**Four independent strands, none acoustic.** The `f0_profile.py` acoustic screen was **NOT run**
— V07's ruling prohibits acoustic voice comparison, and V08, V09 and V10 all honoured it, as does
this session.

| # | Strand | Evidence |
|---|---|---|
| **1** | **The speaker owns the email address** | `[00:02:21]` *"My only valid email address is Steve at marketmakersforks.com"*, repeated `[00:02:40]`. ASR renders the domain as *"marketmakersforks.com"* and *"MM M forex"* `[00:02:47]`; V10 strand 1 has the same construction with *"marketmakers4x.com"*. **This is a first-person claim of Steve's mailbox, not a reference to Steve** |
| **2** | **All five `Steve` tokens are the speaker's own address or vocative/self-quoting** | `[00:02:21]`, `[00:02:40]` = his own email. `[00:15:18]` *"You're sending in you're telling me Steve your method doesn't work"*, `[00:22:19]` *"you can't point the finger at me every day and say that oh well steve's nuts"*, `[00:23:31]` *"you can write me an email and say you know what steve I've taken M's and W's inside the box"* — in all three the speaker **voices students addressing him** and answers in the first person. **In V04–V09 the guest speakers referred to Steve in the third person as an absent authority; here the name is only ever pointed at the microphone** |
| **3** | **He claims authorship of the method and the course** | `[00:15:29]` *"Does that look like a trade or a flashcard that **I've ever taught in any one of my classes** since I've been born?"*; `[00:23:45]` *"They're not what **I teach**"*; `[00:24:50]` *"One trade should not break your belief in **my methods**"*; `[00:36:47]` *"the price action in the timing that **i've taught** you"* |
| **4** | **He owns the course's logistics end to end** | `[00:01:48]` sets the forum policy; `[00:02:32]` controls the email cut-off; `[00:18:07]` imposes the new protocol on the group; `[00:21:11]` *"**I have ordered** bracelets"* to be given out *"at the next live event in new jersey and at the meetups"*; `[00:22:51]` *"you asked me to be here for bootcamp, I'm here now"* |

**Negative check, run deliberately:** a case-insensitive scan for handover language — *take it
away, hand over, handing, turn it over, I'll let, introduce, thanks for having me, the floor is
yours, passing it to, welcome back, let me bring, over to you* — returns **zero matches in 51
minutes.**

**Confidence: HIGH.** Four strands, no counter-evidence, no seam. This is the second consecutive
lesson (with V10) carrying 100% course-author runtime after the five-lesson guest run V05–V09.

## COVERAGE

```text
STATUS: COMPLETE -- no fenced tail, no gaps
Covered: 00:00:00 - 00:50:56
Entries: 643 markers, 643 distinct.
         Timestamps are STRICTLY INCREASING: zero decreasing transitions AND
         zero same-second adjacent pairs. Stated as MEASURED, by scanning the
         body for lines fully matching ^\[\d\d:\d\d:\d\d\]$.
         Zero markers fall past the measured runtime (3056.93 s).
         Largest inter-entry gap 14 s, ONCE, at [00:31:17].
         Next 13 s once ([00:22:51]); 12 s x3; 11 s x2; 10 s x8.
         Modal gap 4 s (127), then 3 s (105), 6 s (97), 5 s (86),
         7 s (71) and 2 s (71).
         Final entry [00:50:56] against measured audio 3056.93 s (00:50:56.9).
```

**The 14 s gap at `[00:31:17]` is silence, not a hole.** It sits inside the RSI range-analysis
segment, immediately after *"below the 50 below the baseline the basis or biases to the downside"*
`[00:31:03]` and before *"so understanding range analysis"* `[00:31:25]` — i.e. across a slide
change. The speaker draws on screen during these pauses (`[00:30:20]` *"Trying to get this pen
going"*), which is exactly where an ASR emits nothing. The same reading applies to the 13 s gap at
`[00:22:51]`.

## VERIFICATION — `SETUP_ISSUES.md` I-008, ALL FOUR CRITERIA

| # | Criterion | Result |
|---|---|---|
| **1** | Final timestamp vs measured duration | ✅ `[00:50:56]` vs **3056.927347 s** = 00:50:56.93. **Under one second.** |
| **2** | Monotonic timestamps | ✅ **STRICTLY** increasing; 643 markers, 643 distinct, minimum gap 1 s |
| **3** | Preserves its own ASR errors and crosstalk | ✅ **Abundantly** — see the table below. A fabricated transcript does not invent its own mishearings |
| **4** | Content consistency against an independent engine | ✅ **Whisper `small.en` spot-checks at four timestamps** — see § AUDIO SPOT-CHECKS |

### Criterion 3 — the mishearings, enumerated

These are the evidence that the file is a real ASR pass over this audio, not a generated document.

| Timestamp | As transcribed | Almost certainly | Note |
|---|---|---|---|
| `[00:14:31]` | *"30 minutes is for **rarer tracks**"* | **railroad tracks** — a candlestick pattern named elsewhere in the corpus | The single most consequential mishearing in the file; it sits inside a claim this session pre-registers a test on |
| `[00:47:57]`, `[00:48:34]`, `[00:49:01]` | *"averaging the **clothes**"*, *"the **clothes** is average higher"* | **closes** | Alternates with the correct *"closers"*/*"closes"* in adjacent lines — a homophone slip no generator produces |
| `[00:02:21]`, `[00:02:47]` | *"marketmakers**forks**.com"*, *"MM M forex"* | **marketmakersforex / marketmakers4x** | |
| `[00:28:32]` | *"before using **cdi** use a plain rsi"* | **TDI** | The file otherwise renders `TDI` correctly 11 times |
| `[00:07:36]` | *"25 to 50 **pits**"* | **pips** | |
| `[00:19:21]` | *"stop tearing your account down and creating your own / **The my's** or end ruining yourself"* | **demise** | `[00:13:51]` and `[00:15:45]` render *"demise"* correctly |
| `[00:00:12]` | *"**Subio**"* | unresolved proper noun | Recorded as ASR, spelling unverified. **Nothing depends on it** |
| `[00:25:29]` | *"because of **Kenrevisa**"* | *"of Ken, revisit"* or a surname | Unresolved. Refers back to *"doc Ken"* `[00:17:38]` |
| `[00:11:16]` | *"I can't tell you enough how wrong **and** is"* | *"how wrong that is"* | |
| `[00:39:18]` | *"hold on. I just stepped on the speaker wire… I got it caught under my roller in the chair"* | — | **Live-room crosstalk, transcribed in place.** Criterion 3's strongest single item |
| `[00:04:04]` | *"lower the day or higher the day"* `[00:13:22]` | *"low of the day / high of the day"* | Recurs; the corpus's `LOD`/`HOD` |

### AUDIO SPOT-CHECKS — an independent engine on four passages

Four passages were re-transcribed from `v11_audio.mp3` with **Whisper `small.en`**, chosen
**before** the results were seen, on the criterion *"a passage this session is about to build an
artifact on"*:

| Clip | Span | Why chosen |
|---|---|---|
| `c1` | `00:46:30`–`00:47:15` | The ***"mayonnaise / the 50"*** line — this session opens a contradiction record on it (`C-018`) and an ASR-only basis would not be good enough |
| `c2` | `00:14:15`–`00:14:55` | The ***"30 to 90 minutes"*** hold claim — the claim `PT-037` pre-registers |
| `c3` | `00:07:25`–`00:08:20` | The ***"25 to 50 pips out of the box second leg W formation"*** protocol statement |
| `c4` | `00:30:05`–`00:31:10` | The **RSI baseline = 50** definition |

Results are recorded in § SPOT-CHECK RESULTS at the foot of this file, after the body, so that the
verbatim transcript is not interrupted.

---

## ⚠ WHAT IS NOT IN THIS FILE

**The pre-ingestion `NOTES.md`, `RULES.md` and `VISUAL_INDEX.md` for this lesson are FABRICATED
and are quarantined.** See `QUARANTINE_REGISTER.md` **Q-012**. In particular `RULES.md` presents
as *"Explicit"*, at `[00:05:00]`, a quotation — *"Wait for the M15 candle to close before taking
the 5/13 EMA cross"* — whose central token, **`EMA`, occurs ZERO times in this entire 51-minute
transcript.** Nothing in those three files may be used as source material for any V11 artifact.

---

# VERBATIM TRANSCRIPT

*Copied unaltered from `01_SOURCE_VIDEOS/Forex Bootcamp/Bootcamp/Bootcamp Notes/11_Bootcamp1_Wk4_040812_Part1_51mins/TRANSCRIPT.md`, body only. The source file's `# VIDEO` header block is deliberately not carried over (see SOURCE above).*

[00:00:00]
All right, welcome to week four of market maker boot camp

[00:00:04]
Hope you guys are doing really well. Hope everything's going good for you in your trading career

[00:00:08]
I'll be getting a lot of emails that people are doing well and turn in the corner

[00:00:12]
Glad to be back here with you guys as well. Subio. How you doing buddy?

[00:00:15]
All right, I didn't have time to fix my hair and take a shower and do all the webcam stuff. So I

[00:00:22]
Got a stop in brag for a Subio real quick. I have traded three days this week

[00:00:27]
2335 pips

[00:00:31]
Profit plus 50 percent risking only 1% per trade absolutely amazing stuff buddy

[00:00:38]
All right managing expectations look I expect you guys to do the work man. I want two hours a week now looking at charts

[00:00:44]
I know every time I sign in you guys put charts up there

[00:00:46]
Make an honor step for to do the assignments. We got a really good assignment coming up this week

[00:00:51]
This one I'm gonna that's coming up. I'm gonna insist that you do it. It's gonna. It's good. It's a good one

[00:00:56]
All right executing demo all the concepts illustrated refrain from negativity in your own mind and from those surrounding you that

[00:01:03]
Believe what a Subio has done or does consistently cannot be done

[00:01:07]
That's what people will say that there's no way some dude could bank 2300 pips and and

[00:01:13]
Increases account by 50% on 1% risk they'll tell you it's impossible

[00:01:19]
Okay

[00:01:22]
Take your time to really soak up what I'm going over

[00:01:26]
Try not to look at charge close the door kick your kid out run the dog outside whatever it takes to give me two hours of

[00:01:32]
Hard core paying attention. All right. I know it's hard for a lot. You have a DD all that other stuff

[00:01:37]
All right chat box. I'm ignoring you on purpose

[00:01:40]
All right a lot of people wrote me emails like I might have answered their questions

[00:01:44]
Listen the chat box is gonna be ignored till the end of the segment. I'll look at a few questions

[00:01:48]
That are relevant to this week's lessons. Please post all research work in the forum for review

[00:01:54]
Raise your work against my post or slides. This gives me more freedom to post and to help everyone else

[00:02:00]
as a group, okay

[00:02:02]
I'm trying to leverage my time to help all of us across the board. That's the point of the forum and the bootcamp

[00:02:09]
All right, so work with me on that

[00:02:12]
student mail time

[00:02:14]
alright

[00:02:16]
Some of you still writing at the old address, please, please, please

[00:02:20]
Marvin make some changes, man

[00:02:21]
My only valid email address is Steve at marketmakersforks.com

[00:02:27]
All other accounts are voided. I'm still answering on there because I'm trying to give you a grace period

[00:02:32]
But I'm gonna cut the account off. I keep saying any minute, but stop writing me there and then I'll just turn it off. All right

[00:02:40]
Steve at marketmakersforks.com stop writing me at my Verizon address and stop writing me at

[00:02:47]
MM M forex, all right, please, please, please. This is the address

[00:02:50]
All right

[00:02:54]
This mail came to me I saw the guy in here. I'm not gonna give him a hard time

[00:02:59]
But he's not the only one that sent me this and

[00:03:03]
Here's what he wrote. I get the direction of the move but too many times my stop losses hit before it moves my way

[00:03:09]
Stop loss on JPY Pierce's gigantic. That's a mistake if trying to aim at smaller stop loss

[00:03:15]
You missed the move 90% of the time. I am now holding these two positions for profit blah blah blah blah blah blah

[00:03:20]
Right

[00:03:21]
Okay, some of you know who this is

[00:03:25]
This is not he by the way if you recognize this email buddy, you're not the only person that sent me this you just happen to mark it up the prettiest

[00:03:34]
To post okay, so without further ado

[00:03:41]
This I don't know how many freaking times I have to say that this is not a trade

[00:03:47]
Is that lower than the blue box is that 25 to 50 pips in the stop-on zone?

[00:03:53]
It's not even in the shadow for God's sakes. It's not a trade

[00:03:57]
This is not a trade and

[00:04:00]
This is not a trade one leg straight down is not a trade. I don't know how many times I have to tell you guys this

[00:04:09]
This is why you're failing and you're blaming me. This is not a trade the only trade that he got right is

[00:04:15]
This one

[00:04:19]
Okay, and look what you have here you have divergence out of the band in the band and the crossover

[00:04:26]
All right

[00:04:27]
He's not listen. He's not the only guy that wrote this to me

[00:04:30]
You're trying so hard to anticipate the low of the day in this example that you're stepping in front of the pair

[00:04:36]
While it's still moving stepping in front of the old adage you're stepping in front of a moving train

[00:04:42]
Okay

[00:04:44]
Okay over here on GJ same thing

[00:04:48]
This is not a trade there is no vector. There's no distance between the blue box

[00:04:53]
And

[00:04:55]
Where the dealer is made a stop hunt you understand the only valid trade is the second leg?

[00:05:02]
W formation don't you understand I can't say it enough

[00:05:05]
Okay, I want you to notice something too very important. You see the band on TDI right here the lower band

[00:05:14]
The best trades come from

[00:05:17]
Below the band or above the band on the top side

[00:05:22]
Again, not a trade not a trade. This is the only valid trade. I don't know how I could explain to you any better

[00:05:31]
To wait for this wait for this and you wouldn't he gave up this stop loss this stop loss

[00:05:36]
This stop loss and this stop loss and this one three times

[00:05:41]
Okay, and something kind of funny if you notice he he went at it three times, which I'm proud of him for not giving up

[00:05:47]
But here's what's kind of funny to me

[00:05:52]
One two three to the low three pushes to the low

[00:05:58]
Okay, do you see that?

[00:06:01]
They push down the Asian session consolidation. They hit it. They pull back consolidated hit it again

[00:06:07]
one two three

[00:06:10]
If you took this and got stopped out that's fine

[00:06:13]
But damn it you come back in here and you take this you should have got stopped out one time and made the entry

[00:06:20]
That would have been acceptable. This is not a freaking trade. It's in the blue box for God's sakes

[00:06:26]
How many times do I have to jump up and down and yell at you guys and tell you?

[00:06:30]
The protocol is after the stop hunt vectors at above or below the blue box. I don't know how many other ways I can say it

[00:06:39]
All right, let's take it. Let's look at it in theory. Let's get off the chart for a second

[00:06:43]
Okay, look I've done this for you guys a thousand times today makes a thousand and one all right

[00:06:48]
There's the blue box. I know it's black, but it's blue right now for our purposes, okay

[00:06:52]
If the dealer does this

[00:06:58]
That's not a trade

[00:07:03]
Okay

[00:07:07]
This is this is not a trade see that if the dealer comes out of the box straight down is that a trade no

[00:07:14]
It's not a trade

[00:07:17]
Okay, the dealer pulls back is that a trade

[00:07:23]
No, it is not a trade this is a trade when the dealer makes the second attempt towards the low of the day

[00:07:32]
Or the high

[00:07:34]
The distance is what?

[00:07:36]
25 to 50 pits. I know you guys can rehearse this shit

[00:07:41]
You've heard me say it a thousand times, but when it comes to real trading you don't execute

[00:07:46]
It's like you your mind goes blank

[00:07:52]
How many times do I have to tell you 25 to 50 pips out of the box second leg W formation

[00:07:59]
Preferably below the support resistance

[00:08:03]
Inside the TDI or above or above the resistance inside the TDI the double band above the double band below the double band is gold

[00:08:11]
Why because it takes about three levels of drop an

[00:08:16]
Excessive drop or excessive rise to get to the outer band of the TDI

[00:08:22]
Because it's averaging the closes

[00:08:27]
You understand Lisa I understand what you're saying

[00:08:30]
But what I'm telling you in this room right now for the people that are struggling

[00:08:33]
This is the only acceptable trade going forward. That's it. This is it or

[00:08:39]
This one the safety trade

[00:08:43]
With this pattern if the dealer gives you the stop hunt. That's it

[00:08:47]
The reason you're struggling is because the candle comes out and he goes oh, that's good

[00:08:51]
Do take a trade does a little consolidation it hits it again. It looks good dude take a trade

[00:08:57]
Right, that's what he did. That's what his chart markup was

[00:09:02]
Then the dealer does this and this and he issues a perfect setup for him and then he got he got it back

[00:09:08]
He made a successful trade why not forget the crap and skip the crap and take the only acceptable trade

[00:09:17]
Here's the deal

[00:09:19]
You are never gonna ramp up to 10 15 20 standard locks if you take those careless first leg vector candle moves

[00:09:31]
Okay, you're forcing the trades you're never gonna ramp up to the level you need to be ramped up to it's just that simple I

[00:09:39]
Don't know what your net whoever wrote that letter or whoever's had this experience

[00:09:43]
I don't know what your net tips were for the data

[00:09:45]
No, if you got plus 50 out of that you said you were holding it

[00:09:47]
But I think non-farm was new and you should have you should have scratched out or took what you had before non-farm

[00:09:53]
Shouldn't have stayed through non-farm

[00:09:57]
Okay

[00:09:58]
This is this right here. Look we're not in the gambling business, but this right here. Here's the box

[00:10:10]
That is a gamble

[00:10:14]
That is another gamble

[00:10:18]
How many times have I explained the M&W to I'm gonna do it again next week, but understand that

[00:10:26]
In order for the M&W to be solid and valid it needs to have a

[00:10:34]
Pullback and another leg why because this pullback right here

[00:10:40]
This pullback right here

[00:10:44]
Hits the stops of the traders that are short

[00:10:47]
Induces people to go long and then when they're long the dealer comes back

[00:10:54]
And triggers their stops as well do you understand?

[00:10:59]
That's why the formation is aggressive and big the formation needs to look like that or like this if the formation

[00:11:07]
Doesn't look like that

[00:11:09]
It's it's a gamble. You're guessing you're trying to anticipate where the dealer's gonna stall and it's wrong

[00:11:16]
I can't tell you enough how wrong and is you're never gonna get to the level of trading you want to get to when you're gambling on this bullshit

[00:11:24]
Okay, I can't say it enough. It's got to stop. Okay

[00:11:29]
All right, this email was very common for some reason over the last two weeks when I went through the emails

[00:11:34]
That's why I'm picking on it and if you recognize this chart. I'm not picking on you particularly

[00:11:39]
I'm picking on the people that sent me this email. You know who you are

[00:11:44]
All right, I

[00:11:47]
Can't emphasize enough. This is in the blue box garbage. This is the first leg. You have nothing

[00:11:54]
This is the first time the dealer locks in and pulls back. There's no

[00:11:58]
Movement in here where he comes off the low and holds it's a tiny tap off the low

[00:12:03]
You want a big beautiful aggressive move, okay?

[00:12:07]
This W right here perfect the second leg forms in the shadow box

[00:12:11]
You notice that at the start of the session he comes back into the range

[00:12:18]
Okay

[00:12:20]
When the two legs hit they're beautiful by the way, this is inverted head and shoulders look head shoulder head shoulder that hammer

[00:12:28]
Right there's a great entry. He got in a little better. That's fine

[00:12:31]
But again, I like to see when they hold the low and they issue a couple hammers to the to the downside wick and then rise

[00:12:38]
And look what happened if you got in somewhere in here in the consolidation

[00:12:42]
You got in right before the shift candle and you were out to the 50 in no time

[00:12:50]
All right

[00:12:51]
Head and shoulders indicates what level three

[00:12:55]
TDI below the band indicates over extension

[00:13:02]
Beautiful W formation after the vector this is not a trade

[00:13:09]
Okay, next slide

[00:13:15]
Okay, so problems that are occurring as a group you're entering on the vector candles leg one with no confirmation

[00:13:22]
Before the lower the day or higher the day have locked in

[00:13:26]
Inside the blue box. I just showed you

[00:13:30]
Your entries are with no reason other than the dealer has made a move out of the box or a image simply made a move

[00:13:36]
You get excited you take it

[00:13:40]
You're also not taking the time in the consideration

[00:13:44]
You just pull in the trigger. Here's the reason why you're afraid you're gonna miss something which is in essence causing your own demise

[00:13:51]
You're so excited to get something and not fail that's your it's causing you to fail. It's like a catch 22

[00:13:58]
It's crazy, but that's what you're doing

[00:14:02]
This guy saw I'm picking on this guy because of his chart you guys are seeing a move out of the box

[00:14:11]
You're grabbing the trade anticipating that's gonna be the low because it's one candle the dealer goes into consolidation hits it again

[00:14:18]
You're like, oh well that wasn't below this ought to be the low you grab it again

[00:14:25]
Understand that the low has to hold

[00:14:31]
How long 30 to 90 minutes 30 minutes is for rarer tracks, but the long sideways consolidation should last up to

[00:14:39]
Two hours then calmly take a trade

[00:14:43]
Now I want to point out

[00:14:46]
If you have done your flashcards and I've done them so you can't bullshit me

[00:14:52]
There are not one flashcard in my collection

[00:14:54]
That looks like that shit that he called a trade and if you guys have it you've done them wrong

[00:14:59]
If you have one candle pointing straight down on your flashcard and you took that as a trade

[00:15:05]
Then you need to rip your damn flashcards up and do them over

[00:15:08]
Because they're wrong

[00:15:11]
All right, I'm not mad. I'm just jacked up little guy coke today

[00:15:14]
I'm just telling you you guys are crazy

[00:15:18]
You're sending in you're telling me Steve your method doesn't work

[00:15:21]
I don't understand and I pour through the emails excited to see the progress

[00:15:24]
And it's a straight friggin candle straight down out of the box and I'm like where in the world

[00:15:29]
Does that look like a trade or a flashcard that I've ever taught in any one of my classes since I've been born?

[00:15:35]
Does that look like a trade you show me where?

[00:15:38]
Okay, that's why you're not having the success in this business that you deserve

[00:15:45]
You're creating your own demise. You're fueling your own demise

[00:15:51]
Okay, these items are the only reason this is the this is the main thing that I'm seeing

[00:15:57]
You're trying so hard to anticipate where the low or high are gonna form that you're gambling

[00:16:03]
I

[00:16:05]
Said this a hundred times here at 101. I am not in the gambling business

[00:16:09]
I told you I live in Florida. We have indian owned and operated casinos

[00:16:13]
That's where I go to get that out of my system

[00:16:16]
I pull the arm for a few hours or roll the dice whatever it takes and then that's out of my system

[00:16:21]
When I come home and sit in front of the platform, that's not what we do here

[00:16:27]
If you want to gamble and can't get it out of your system take a ride to vegas

[00:16:31]
We are in the high probability trade business

[00:16:35]
the high probability trade business comes from

[00:16:39]
Vector formation w or m where the dealer hits the high and stops breaking it where the dealer sets the low and trades above it

[00:16:46]
Same thing

[00:16:47]
Different way of saying it

[00:16:49]
That's the business that I am in and that is the business that I want every single one of you in here to be in

[00:16:56]
Okay

[00:16:58]
So what I want you to do is this crap has to stop immediately if you didn't do the flashcards take the week off from trading and do the flashcards

[00:17:08]
It's got to stop it's killing you

[00:17:12]
In order for you to turn the coin you need to take a good hard look at yourself and how you're entering into trades

[00:17:18]
And if that email if you didn't send me one of those charts and that email resonates with you and your chart looks like that

[00:17:23]
Your trading looks like that

[00:17:25]
Then i'm talking to you as well

[00:17:29]
Okay, so with that off my chest we got a new protocol coming down the pipe

[00:17:38]
All right a lot of you made it to uh doc doc Ken's presentation this week

[00:17:45]
About rainout days and about wait for your pitch that kind of stuff he

[00:17:50]
basically

[00:17:51]
Took the mental side of it and applied it to baseball, but it applies to anything in life and trading as well

[00:17:59]
So what I want to do is I want to up the game a little bit. I want to make you guys accountable

[00:18:04]
Okay

[00:18:07]
From now on starting right now. Okay commit those guys are serious get serious commit

[00:18:12]
before you take any trade

[00:18:15]
Any trade at all in your live account or demo because you need to form the habits in demo that you'll take in life

[00:18:22]
You can't be a cowboy in demo and then go live you're going to burn your life account down

[00:18:29]
Okay

[00:18:30]
You got to treat the trade that you're about to pull the trigger on

[00:18:33]
Like i'm sitting with you and that you got to justify your entry to every single person in this group

[00:18:40]
We're going to be accountable to each other in this group

[00:18:45]
You got to pretend

[00:18:47]
That 1,100 of us are sitting staring at your screen same time as you and they're all saying dude why don't you take that trade?

[00:18:54]
And your answer better be

[00:18:56]
Vector candle to the low second leg formation tdi passed the bands

[00:19:01]
I got the dealer in my sites today that better be the answer

[00:19:05]
So what i'm asking you to do

[00:19:09]
Is to be like lance armstrong promotion if you remember that live strong i'm asking you to trade strong

[00:19:16]
To stop the bullshit and stop tearing your account down and creating your own

[00:19:21]
The my's or end ruining yourself in the business

[00:19:28]
Okay

[00:19:30]
I want you to up your level of accountability

[00:19:33]
Help to keep you out of bad entries and force you to look inside yourself at a different level

[00:19:40]
I want you as a person to find your inner strength everybody has inner strength when you realize it or not

[00:19:47]
I

[00:19:49]
Cannot teach you discipline

[00:19:52]
But I can ask you and make you be accountable to yourself and to the members of this group by posting your shit trades on the board

[00:20:01]
Or posting your good trades on the board for everybody to see

[00:20:07]
Okay, if you're embarrassed to put your name on it and hanging it on the board then dammit you shouldn't be trading your account

[00:20:14]
Okay, so here's what we're going to do

[00:20:18]
This is our new mantra trade strong. I will only take second leg setups

[00:20:24]
Trade strong. I will only take m or w outside the blue box dammit

[00:20:32]
I want you to trade strong. I will not over leverage my account. I will not take a 25 risk on one trade

[00:20:40]
I

[00:20:42]
Will execute with clarity free of distraction. I want to trade strong. I will never lift my stops

[00:20:52]
I will be strong therefore I will trade strong. Okay, that's our new motto

[00:20:58]
Here's the deal

[00:21:02]
After I read the same email I was pissed off for two days and I tried to figure out in my head

[00:21:06]
How can I turn it around for the group and make it better?

[00:21:09]
and fix this stuff

[00:21:11]
I have ordered bracelets

[00:21:14]
Just like the live strong ones that will be given out at the next live event in new jersey and at the meetups

[00:21:24]
They will have this stamped on them. They're going to say trade strong

[00:21:29]
The color that I ordered is limit order green

[00:21:37]
Okay

[00:21:38]
If you think it's stupid, that's fine. I'm not offended

[00:21:43]
But I want you to take this bracelet and put it on your wrist when you're trading

[00:21:49]
And I want you to feel everyone looking at the chart the same time as you

[00:21:54]
and understand

[00:21:57]
That and has that a good entry because I'm gonna have to explain this to everybody

[00:22:03]
Okay

[00:22:06]
Trade strong my friends

[00:22:09]
Here's what I want you to do as a person if you push your limits

[00:22:15]
You will hit your limit

[00:22:18]
Okay

[00:22:19]
You got to start being accountable. You can't point the finger at me every day and say that oh well steve's nuts

[00:22:26]
That's easy

[00:22:27]
It's easy to blame somebody else you turn that finger around and point it at yourself

[00:22:32]
You start taking trades like the whole group and your mother's watching

[00:22:37]
You start

[00:22:38]
Taking solid second leg entries based on the things that I've shown you not some anticipated guests of where the dealer's going to stall

[00:22:51]
Okay, that's what I want from you guys you asked me to be here for bootcamp

[00:22:57]
I'm here now. I'm asking you to step up your game and get the most out of this time that I'm sinking into this

[00:23:06]
I said right out of the box. I think the first week I said quit taking shit in the blue box

[00:23:12]
And dammit, I don't know how many emails I got but it was too many

[00:23:16]
Of people that took W's and M's inside the box

[00:23:19]
I

[00:23:21]
Don't know how else to say it this shit has to stop. You're never going to have the level of success taking that crap

[00:23:31]
Of course you can write me an email and say you know what steve I've taken M's and W's inside the box and they work

[00:23:36]
No argument for me

[00:23:38]
But I got to tell you they're 50 50 guesses. They're 60 40

[00:23:45]
They're not what I teach

[00:23:48]
Can you grab a W inside a box after three levels of rise or three levels of fall and get lucky? Yes, you can my friends

[00:23:56]
But we are not in the luck business

[00:23:59]
How are you going to put 10 standards on a guess?

[00:24:04]
How are you going to ramp up to the level that you want to be at that you came to me for

[00:24:11]
If you don't listen to what I'm asking you to do from week to week

[00:24:17]
Okay

[00:24:19]
All right

[00:24:23]
The one trade philosophy

[00:24:27]
Okay, I'm getting all philosophical and coaching on you this week because because of Kenrevisa all right

[00:24:32]
Tang with me

[00:24:34]
One trade should not break your account

[00:24:38]
One trade should not break your confidence

[00:24:41]
One trade should not break your spirit

[00:24:43]
One trade should never define you as a trader or define you as a person

[00:24:50]
One trade should not break your belief in my methods

[00:24:56]
in your system

[00:25:02]
Okay, think about what i'm telling you

[00:25:04]
Some of you get stopped out once or twice and you're like, oh man, this guy's crazy socks

[00:25:08]
I don't believe it you got to believe it yourself in order for it to work

[00:25:13]
You

[00:25:17]
One trade should not derail your success

[00:25:20]
And on the wind side one trade should not over excite you. It's just one trade

[00:25:25]
Okay winner lose one trade is simply one trade

[00:25:33]
All right, I figured it was sunday and it was easter i figured i'd get preach on you guys

[00:25:38]
I hope you understand what i'm saying. Okay, let's get to today's lesson

[00:25:43]
TDI

[00:25:46]
We're going to look at the TDI i'm going to break it down a little differently for you

[00:25:50]
Help you spot the right segments of the market

[00:25:53]
How to stay the course if you're in something a lot of you chicken out and bail out of stuff too soon

[00:26:01]
How to add to a winner scaling in

[00:26:04]
Using the TDI for confirmations

[00:26:07]
How to spot divergence in order to understand the TDI you got to understand what it's comprised of

[00:26:14]
the underlying indicator in order to understand

[00:26:18]
The TDI you got to look at the underlying indicator, which is rsi relative strength

[00:26:23]
Index indicator or whatever you want to call it. It's just relative strength

[00:26:28]
Okay rsi is the foundation

[00:26:34]
For TDI

[00:26:37]
I

[00:26:39]
Go back. We're sorry. Okay

[00:26:42]
Would you give me this would you say that all indicators measure the same thing?

[00:26:47]
They all plot above it and below

[00:26:51]
A zero line

[00:26:55]
Or a baseline a market baseline and if you use several of them which one wins

[00:27:01]
You don't have to use the TDI

[00:27:03]
You don't have to use the rsi but what i'm asking you to do

[00:27:07]
Is to master the use of one indicator

[00:27:10]
Better than anybody's ever asked you to master it

[00:27:15]
Okay, not just look at it and like oh yeah, it's below the baseline

[00:27:18]
That means sure it's above it means no

[00:27:21]
To understand the nuances of the indicator that you're using and understand its behavior

[00:27:27]
Okay, this was

[00:27:30]
Cars chart when i met them

[00:27:32]
And it's kind of half of a joke

[00:27:36]
But it's true a lot of people not really that's cars

[00:27:39]
It's a lot of people are like this

[00:27:42]
And they have all the indicator windows in the subgraph and absolutely ridiculous

[00:27:48]
You can't even see the price action

[00:27:53]
Okay

[00:27:54]
What i'm asking you to do is to get rid of all this crap and pick one indicator

[00:27:58]
Don't you don't need multiple confirmations of the things that

[00:28:03]
You know, we're true. It's not going to make a difference for you

[00:28:06]
What i need you to do is to get rid of all this garbage

[00:28:10]
And just pick one if it's

[00:28:12]
Stochastic that's fine

[00:28:16]
If it's the alligator ao whatever it just one just one indicator that's all i want you to do

[00:28:22]
But i want you to be so freaking good at it

[00:28:25]
You can trade a blindfold

[00:28:29]
Okay, why rsi i've always liked the rsi even back before using cdi use a plain rsi

[00:28:38]
The reason why is it plots based on the closing value it doesn't fall for the spikes

[00:28:44]
That's why divergent shows up so nicely

[00:28:47]
Is because

[00:28:49]
Usually in a candlestick

[00:28:52]
You guys know this you will get the spike

[00:28:55]
And it'll come back and close somewhere down here

[00:28:59]
Well, you have price moving higher with spikes, which is a dealer trick

[00:29:04]
But rsi is plotting down here on the closes and that's where divergent comes from and that's why

[00:29:12]
Rsi doesn't get carried away

[00:29:14]
If you notice mac D some of you will notice that when there's a spike in the market mac these histogram bars

[00:29:20]
Will push all the way down and follow price more closely

[00:29:26]
That to me is not helpful

[00:29:30]
Okay, besides if you have moving averages on your chart

[00:29:34]
It's exactly what mac D tells you the distance of uh the averages before they cross

[00:29:41]
Why not use something that measures strength based on closed rsi

[00:29:45]
Okay, if you know how to use it properly it will confirm shifts to momentum

[00:29:49]
And it's excellent for spotting divergence

[00:29:52]
And believe it or not the levels can actually be counted inside the indicator

[00:30:00]
In order to take or use tdi you got to understand the foundation of rsi

[00:30:09]
Okay rsi

[00:30:13]
Has the middle line in the center. Okay, that's the 50

[00:30:17]
Okay

[00:30:20]
Trying to get this pen going okay in the sub graph

[00:30:26]
On your chart

[00:30:28]
The market baseline is 50

[00:30:30]
Okay, it's zero another indicator cci mac D. It's it's zero

[00:30:35]
far aside for our purposes. It's 50

[00:30:38]
Okay

[00:30:40]
And then up here you got 70 or 80

[00:30:42]
And down here you got 30

[00:30:48]
Okay, typically

[00:30:50]
When price

[00:30:52]
Crosses above the market baseline basis the market baseline. What's the basis if it's above the 50 the basis is positive up

[00:31:01]
The trend is up, right

[00:31:03]
If it is below the 50 below the baseline the basis or biases to the downside

[00:31:17]
Okay

[00:31:25]
Okay, so understanding range analysis

[00:31:28]
Very important 0 to 100 is the whole graph normal range oscillates between 70 and 30

[00:31:37]
If the market is in an uptrend

[00:31:39]
Okay, one hour 15 minute even

[00:31:44]
The bull range I hate that terminology, but the uptrend or or price rising range is 80 to 40

[00:31:51]
Bear range is 60 to 20. I'm going to explain this in a second very important overbought or overextended

[00:31:57]
is

[00:32:00]
Above 80 and below 20

[00:32:04]
Okay

[00:32:05]
Now

[00:32:06]
Think about this for a minute. You've seen it a hundred times. Maybe you noticed it. Maybe it but it's very important

[00:32:14]
On the range analysis

[00:32:16]
Let's say in an uptrend 80 40. What does that mean exactly? Here's the deal

[00:32:22]
Let's take a two-day segment

[00:32:27]
Of rsi underlying indicator. It'll come from the bottom and make its w formation, right?

[00:32:34]
Let's say this is the market baseline the 50

[00:32:37]
This would be the trend reversal level three coming off the bottom

[00:32:42]
It will oscillate and cross the 50

[00:32:45]
And then pull back

[00:32:47]
to slightly below the 50 around 40 38 42

[00:32:52]
slightly below the 50

[00:32:55]
And then rise again towards 80

[00:32:58]
This segment right here where the rsi finds imaginary support

[00:33:06]
Slightly below the basis line the 50 slightly below the basis line and turns back up

[00:33:15]
Is the confirmation of the safety trade

[00:33:19]
Okay

[00:33:22]
Okay, how many times have you seen the thing oscillating and go slightly below and roll back over and then go back up

[00:33:29]
When scroll to your charts really fast, you'll see what i'm talking about

[00:33:34]
And then it'll do it one more time. It may or may not come back below the 50

[00:33:38]
It might find support on the 50 and then rise

[00:33:42]
You will find yourself understanding this you will find yourself in level three here

[00:33:49]
Okay

[00:33:51]
Day one day two safety trade day three

[00:33:59]
An extended move above 80

[00:34:02]
92 93 when it gets maxed out if you get a perfect signal

[00:34:08]
When tdi is overextended or rsi is overextended you're going to get you're going to get a pullback and it's tradable

[00:34:15]
Okay, the same thing goes for short side

[00:34:26]
Okay, man if a programmer is listening and you can put this

[00:34:33]
On the tdi subgraph you'd be my hero

[00:34:36]
I've mentioned it a couple times and and i don't know if it's doable that it would extend out

[00:34:40]
As the tdi moves it would follow you in the left hand corner

[00:34:43]
Like maybe you set the offset to be bottom left hand visible

[00:34:47]
I don't know how to do it

[00:34:48]
But any any of your programmers out here if this was on your screen and you were just plotting the line

[00:34:54]
This would be solid gold here's one

[00:34:58]
You need

[00:35:00]
To notice when it comes off the extreme areas

[00:35:05]
Pulls back find support slightly below

[00:35:09]
At around 40 and continues higher gets extreme again. You can expect it to come back

[00:35:18]
Okay

[00:35:20]
The things that i'm showing you on the tdi or rsi are present in every time frame

[00:35:26]
15 minute one hour or four hour

[00:35:30]
Okay, if you get an rsi on a daily all the way down here

[00:35:33]
Guarantee you it's going to pop off the bottom

[00:35:36]
Okay

[00:35:40]
But notice this graph this is the bands

[00:35:43]
Okay, this is the bands that are on there

[00:35:46]
Extreme is above 80 the extreme means that prices

[00:35:50]
Overbought i hate that term it just means it's exhausted

[00:35:53]
It's made it's run but i can tell you that when it gets into the extreme ranges of the band

[00:35:59]
You are more than likely at level three you will get a pullback

[00:36:04]
Okay

[00:36:06]
So now think for a minute

[00:36:08]
I know what an m looks like hopefully. I know what a w looks like hopefully

[00:36:13]
I know that i'm not as of today. I'm not going to take any more shit in the blue box

[00:36:19]
So now I know that if it's 25 to 50 pips below the blue box and the tdi or rsi is in the extreme

[00:36:26]
80 to 90 range and it gives me the formation

[00:36:31]
I got a pretty good trade on my hands

[00:36:34]
Okay, if this is not how you're using the indicator

[00:36:41]
Adopt this policy right now you take extreme overbought extreme oversold conditions

[00:36:47]
Pair it up with the price action in the timing that i've taught you

[00:36:51]
And you're going to up your game right now

[00:36:54]
Okay, let me say it again

[00:36:56]
You look for the pairs that are extremely overextended

[00:37:01]
Extremely overextended look for the price action and timing m formation on extreme here w formation on extreme here

[00:37:11]
Look for those locations on the chart

[00:37:15]
You're going to up your game immediately

[00:37:19]
Okay, all right

[00:37:22]
So now

[00:37:27]
Okay, range rules i just talked about this what happens is

[00:37:35]
Okay, here's your sub graph i'll put it on the bottom of the chart for argument's sake

[00:37:39]
Okay, i'm a terrible artist, but there's your middle

[00:37:45]
Price comes off the top

[00:37:48]
Level three pulls down pulls back fines

[00:37:52]
Resistance at around 60 which means it slightly crosses over and rolls back down

[00:37:59]
So when you're in this part of the market, this is peak formation high

[00:38:05]
right peak formation high

[00:38:11]
Level one day one drop pull back sideways consolidation stop hunt high

[00:38:18]
drop

[00:38:20]
Safety trade going into level two crosses back below the market baseline

[00:38:26]
May extend all the way down and pull back and it maybe gives you one more day where it finds

[00:38:32]
resistance at the market baseline and then drops again

[00:38:36]
That would be your level three extreme the bottom of the graph. It would probably read something like

[00:38:42]
12 or 14 or 10 very very low very low below 20

[00:38:47]
Okay, when you get in here, you're more than likely a found level three

[00:38:53]
And you can expect a signal to the downside which would be what anybody stop hunt low rise

[00:39:01]
That's what you're looking for. Okay

[00:39:04]
This is how I want you to use the indicator

[00:39:08]
There's no other way to do it

[00:39:12]
Okay

[00:39:14]
So looking at just the rsi line

[00:39:18]
Okay, hold on. I just stepped on the speaker wire. Okay, everyone can still hear me. Yeah, it's spiking. Okay. All right

[00:39:24]
I got it caught under my roller in the chair. All right

[00:39:27]
now

[00:39:29]
The 8040

[00:39:32]
Will switch to 60 20

[00:39:36]
Okay, and that's not the percentages

[00:39:39]
It's the oscillation in the sub graph of how it how it handles itself. So what happens is

[00:39:45]
You're oscillating up here

[00:39:49]
Right then all of a sudden you get to level three and it will make the switch over

[00:39:54]
And start oscillating around here on a normal normal basis right in the 50s right here

[00:40:01]
Process over makes a wave comes slightly back finds support on the 40

[00:40:08]
Goes all the way up and level three hits maybe

[00:40:11]
Find support slightly below the base or at the base

[00:40:15]
One i threw too many waves in here one two three

[00:40:19]
And then you'll either get a reset

[00:40:22]
Continuation or it will change trends where it will oscillate from 8040

[00:40:27]
We'll start doing the same exact thing on the downside of the sub graph. It will find resistance

[00:40:34]
slightly

[00:40:36]
Above the market baseline slightly above it'll come from the peak formation high

[00:40:42]
And you'll have two

[00:40:43]
Level three all the way over extended

[00:40:47]
Formation and back into the range. This is how it switches from an uptrend

[00:40:54]
To a downtrend

[00:40:56]
When you're watching the tdi and a neat little trick to do is

[00:41:00]
Hit the arrow on your the home key on your chart and open up your tdi or rsi all the way

[00:41:05]
And then scroll through

[00:41:07]
Kind of fast and you'll watch you'll see what it does

[00:41:10]
It goes like this

[00:41:12]
Then it drops down it goes like this and then it drops up goes like this

[00:41:15]
Drops down it goes like that. It's crazy when you roll it fast

[00:41:18]
It almost looks like an ekg on the top part ekg on the bottom part and you'll see it switching back and forth

[00:41:29]
Okay

[00:41:31]
So what i'm telling you to look for is the peak formation high and lows inside the tdi itself with the rsi line

[00:41:40]
They'll be they'll be marked they will extend down and come right above the base

[00:41:46]
Look for the m or vtop formation for the continuation inside the tdi thing

[00:41:54]
Okay

[00:42:01]
Okay

[00:42:03]
Okay, back to normal. Okay, so and then this is i'm not going to explain it again. It's the opposite goal in the other way

[00:42:09]
downtrend

[00:42:12]
Crosses over

[00:42:15]
Okay, understand is

[00:42:19]
Let me think of step

[00:42:23]
Understand

[00:42:24]
The rsi

[00:42:26]
Is the underlying component for the tdi?

[00:42:29]
Okay, i'm going to explain the tdi in a minute

[00:42:34]
Although this was cool because

[00:42:36]
These slides are labeled one two three in here and I thought it was crazy this thing was written

[00:42:41]
Maybe 15 years ago. I'm not even sure these slides came from that guy. I really like

[00:42:47]
Can't think of his name right now

[00:42:49]
Choking in front of under the pressure in front of all you guys. All right for any all you sacrilegious people. All right, man look

[00:42:59]
What happens what they call the short-term trends turning up when rsi starts to rise, right?

[00:43:06]
When it crosses the market baseline

[00:43:13]
When it crosses the market baseline the intermediate trends are turning over the one hour perhaps starting to rise

[00:43:20]
When it gets above the 60 or into the 80 90 range

[00:43:24]
Right, which is kind of ironic. It's level three

[00:43:29]
The longer term things starting to turn upside they call that right upside acceleration trend acceleration

[00:43:34]
But we know better as a group trend acceleration is a sucker's play, man

[00:43:41]
Okay

[00:43:42]
Trend acceleration is when the dealer

[00:43:45]
Separates away from moving averages and vectors straight up to catch all the suckers

[00:43:51]
To jump on to the tray and it gets excited and go damn look at the euros going up

[00:43:55]
I should have got some of that and jump on

[00:43:59]
And that's when the dealer applies the brakes

[00:44:02]
Okay

[00:44:07]
All right, same exact thing inverted for the downside

[00:44:13]
Same thing right peak formation high coming into level one dealer drops down crosses

[00:44:20]
the momentum

[00:44:21]
changer this confirms the downtrend

[00:44:25]
Then he gets to the extreme side trend acceleration begins we can expect

[00:44:31]
The dealer put the brakes on

[00:44:35]
Okay spotting divergence

[00:44:40]
Since the rsi line is based on the closing value not on the spike value. It's not based on price

[00:44:46]
It's based on the close of price for the period measured right

[00:44:50]
So if there's a spike to the high

[00:44:57]
R size is not going to fall for it

[00:45:01]
Hence you have divergence you have the indicator has already picked off the move to the downside price is still

[00:45:07]
spiking higher

[00:45:11]
Okay

[00:45:13]
Rsi values already swinging higher

[00:45:20]
But price gives you the spike to the low we know that this is depending on how it closes right

[00:45:26]
We know that this is most of the time the stop hunt

[00:45:33]
Right, this is the theory if you get a perfect

[00:45:36]
W formation and rsi at the extreme zone

[00:45:39]
But the dealer spikes to the low one more time and ends on a hammer or some quasi type of hammer

[00:45:46]
Based on the rsi itself, you know, you got them

[00:45:51]
Okay

[00:45:56]
All right hope everybody can see that

[00:45:59]
divergence

[00:46:00]
Simple to see rsi line stays flat actually makes the m formation

[00:46:06]
But the dealer hits the stops one more time

[00:46:09]
That's what it looks like and he crosses the 50

[00:46:14]
Shifts the zone away from the traders, okay

[00:46:21]
The other way what happened in this one price stayed flat

[00:46:25]
But rsi is averaging the closing value and it's starting to rock rise higher

[00:46:31]
Okay

[00:46:34]
They call that hidden divergence

[00:46:39]
Okay, here's a cleaner shot we're in a downtrend

[00:46:45]
How do I know look where the averages are there's the mayonnaise. There's the 50

[00:46:50]
Okay, we're in a downtrend

[00:46:52]
Notice how rsi spiked below and it came slightly above right? Remember I told you there's the 50

[00:47:00]
Rsi will find resistance where around 60 right?

[00:47:04]
It comes slightly above and makes the formation for us

[00:47:09]
Price waves higher rsi waves flat

[00:47:13]
And forms an m. This is not a w formation. This is an m in line with the stop hunt high

[00:47:25]
Okay

[00:47:27]
All right

[00:47:31]
This is beautiful you guys know I told you don't hit the high in front of me or the low in front of me three times there you go

[00:47:37]
Look look how the dealer has made the same level every time

[00:47:41]
But he's coming off the extreme value low and rising up higher and higher every time

[00:47:51]
Okay, so if you see the dealer hit it three times and you notice that he's averaging his closers higher

[00:47:57]
Well, what's significant about averaging the clothes is higher and i'm going to tell you

[00:48:01]
To redundant question right you know i'm going to answer it

[00:48:04]
Okay, the rhetorical question I guess redundant means over and over rhetorical all right i'm losing it man

[00:48:11]
Okay, look

[00:48:12]
What happens here?

[00:48:18]
Is that if the closers are averaging higher it means that the dealer pushes down and pulls back

[00:48:23]
dealer pushes down and pulls back the dealer pushes down and pulls back

[00:48:27]
every time he does that

[00:48:29]
The closers are averaging away from the original low

[00:48:34]
So each subsequent time he waves the clothes is higher

[00:48:38]
But price comes back to the same level what closes further away

[00:48:42]
It means that the dealer is grabbing the money and pulling the trading zone away from those traders

[00:48:49]
Every time he pushes down and pulls back pushes down pulls back pushes down pulls back

[00:48:55]
And you notice that the closers are averaging higher

[00:48:58]
Hmm, why would the clothes is average higher?

[00:49:01]
Because most people make decisions on closed candles. That's what they teach in the business. So if the dealer closes higher

[00:49:09]
But he already got some people from the previous candle and he snatches it away and closes it up in this example

[00:49:16]
He's simply trapping the volume at the lower levels

[00:49:22]
And jamming up those traders short in this example

[00:49:28]
Okay, so now

[00:49:30]
He did it three times he did it from mid london into the us session

[00:49:35]
To right around 11 12 o'clock and then he decided all right. I picked up all these jerk wads

[00:49:41]
I got them. They're all stuck

[00:49:44]
I jammed them up. They thought it was short and boy did I show them took it away from them or right back into the range

[00:49:52]
What gave that away was an average of rsi waving higher waving higher waving higher coming off of its support extreme band

[00:50:02]
And the low never being broken the low was never broken

[00:50:06]
Except for one spot and it closed back above

[00:50:10]
Right here. I want you to notice this right there

[00:50:14]
And we all know what that is he grabbed the stop I opened in the spread he's somewhere down in here

[00:50:20]
I price went to hear the guy opens the spread down into here

[00:50:24]
What happens?

[00:50:26]
He's able to grab up the orders

[00:50:31]
That are sitting just outside of that reach

[00:50:35]
Okay

[00:50:38]
All right

[00:50:40]
Again divergent top side

[00:50:44]
I

[00:50:45]
Vectors to the high holes it hits the stops one more time

[00:50:49]
But rsi already starts falling off. It's hard to see these because I stretch them out for the uh

[00:50:56]
for this line

---

# SPOT-CHECK RESULTS — WHISPER `small.en`, FOUR PASSAGES

Run 2026-08-13 against `v11_audio.mp3` (extracted `ffmpeg -vn -c copy` from the SWF; measured
3056.927347 s). Passages were chosen **before** any result was seen, on the stated criterion.
**All four agree with the ASR transcript on every load-bearing token.** Two of them *correct* an
ASR mishearing, and both corrections are recorded here rather than applied to the body — the
verbatim body is never edited (`SOURCE_INGESTION_PROTOCOL.md`).

### `c1` — `00:46:30`–`00:47:15` · the *"mayonnaise / the 50"* line

> Whisper: *"…They call that hidden divergence. Okay, here's a cleaner shot. We're in a downtrend.
> How do I know? **Look where the averages are. There's the mayonnaise. There's the 50.** Okay,
> we're in a downtrend. Notice how RSI spiked below and it came slightly above, right? Remember I
> told you, there's the 50. The RSI will find resistance where? Around 60, right?…"*

**VERBATIM AGREEMENT with the ASR transcript on the whole passage, including the sentence
`C-018` is opened on.** The two engines produce the same seven words: *"There's the mayonnaise.
There's the 50."*

**This does NOT resolve what the sentence means** — see `C-018` and `A-020`. Both engines heard
the same words; the words themselves are two-ways readable (apposition vs. enumeration), and the
screenshot at this timestamp shows four averages and **no legend**. **The audio question is
closed; the semantic question is not, and they are different questions.**

Note also that Whisper renders the following clause as *"and forms an end"* where the ASR has
*"And forms an m"* `[00:47:13]`. **The ASR is better here** — the subject is M and W formations
throughout, and `[00:47:13]` continues *"This is not a w formation. This is an m"*. Recorded
because an engine disagreement that goes *against* the newer engine is worth stating.

### `c2` — `00:14:15`–`00:14:55` · the *"30 to 90 minutes"* hold claim

> Whisper: *"…understand that the low has to hold, how long? **30 to 90 minutes. 30 minutes is for
> railroad tracks, but the long sideways consolidation should last up to two hours. Then calmly
> take a trade.**"*

**AGREEMENT on every number** — `30`, `90`, `30`, `two hours`. And it **resolves the ASR
mishearing**: the transcript's *"30 minutes is for **rarer tracks**"* is ***railroad tracks***, a
candlestick pattern. `PT-037` is pre-registered on this claim and **quotes the ASR body while
citing this correction**, per `REMEDIATION_PROTOCOL.md` §2.

### `c3` — `00:07:25`–`00:08:20` · the second-leg protocol

> Whisper: *"This is a trade when the dealer makes the second attempt towards the low of the day
> or the high. The distance is what? **25 to 50 pitts** [pips]… **25 to 50 pitts out of the box
> second leg W formation, preferably below the support resistance, inside the TDI** or above the
> resistance inside the TDI, **the double band, above the double band below the double band is
> gold**. Why? Because it takes about **three levels of drop**, an excessive drop or excessive
> rise, to get to the outer **base** [band]."*

**AGREEMENT on every number and every named object.** Both engines independently produce *"pitts"*
for *pips* — an identical mishearing from two different systems, which is evidence about the
speaker's diction, not about either transcript.

### `c4` — `00:30:05`–`00:31:10` · the RSI baseline

> Whisper: *"**RSI has the middle line in the center, that's the 50**… In the subgraph on your
> chart, **the market baseline is 50.** It's zero in other indicators, CCI, MACD, it's zero. RSI
> for our purposes, it's 50. Then up here you got **70 or 80**, and down here you got **30**.
> Typically when price crosses above the market baseline… **if it's above the 50, the basis is
> positive, up, the trend is up**, right? If it is below the 50…"*

**AGREEMENT on every number.** This is the passage in which the lesson's one fully explicit
definition is given, and it is confirmed by two engines.

### What the spot-checks do NOT establish

They cover **4 minutes of 51**. They are a sample chosen for consequence, not a re-transcription,
and they say nothing about the other 47 minutes beyond what criteria 1–3 already established.
`SETUP_ISSUES.md` `I-008` remains the standing item for transcripts that have had no full
independent pass.
