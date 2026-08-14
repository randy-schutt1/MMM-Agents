# V17 — TRANSCRIPT

## ⭐ TIMESTAMP CONVENTION — STATED ONCE, AT THE TOP (`V14_REVIEW_R1.md` GATE, open item 173)

**Every `[HH:MM:SS]` in this file and in every V17 artifact is the committed marker grid of THIS
file — the 690 markers below — and nothing else.** An independent ASR pass was run this session
(VERIFICATION §5) and **its clock is never cited**; where it arbitrates a word, the correction is
attached to the *marker grid's* timestamp, not to the second pass's.

**The marker grid and the player's burned-in timecode are the SAME CLOCK, and here the sweep offset
was MEASURED AT ZERO at fourteen points rather than argued.** See `04_SCREENSHOTS/V17/INDEX.md` §0
for the full `SWF_CAPTURE_RECIPE.md` §8a table. Screenshot filenames carry the player timecode;
because the clocks coincide, a screenshot name and a marker are directly comparable and **no
conversion is used anywhere in this artifact set.**

Corroboration at five content points where the screen changes on a sentence. **Quotations are
verbatim from the marker grid, ASR defects included:**

| Marker | Transcript line, VERBATIM | Screen change, burned player timecode | Δ |
|---|---|---|---|
| `[00:19:27]` | *"Fantastic car beautiful baby. Okay, all right **pop quiz**"* | `Pop Quiz: What are these trades called?` slide at **19:35** | +1 s |
| `[00:20:01]` | *"All right **trade one**"* | `GBPUSD,M15` chart replaces the quiz slide at **20:05** | +4 s |
| `[00:20:23]` | *"Okay, now"* → `[00:20:27]` *"The answer those were both safety traders"* | `Answers: Safety Trades` slide at **20:30** | +3 s |
| `[00:23:12]` | *"Man this happens every time you think I would have shut the shit off already. Okay, hold on"* → `[00:23:18]` *"Sorry, man, I do maintenance everything"* | A **`PC Tools │ Registry Mechanic`** window is on screen at **23:15** | +1 s |
| `[00:44:56]` | *"you're gonna laugh at me, but I got a correct. it's gonna drive me insane for the rest of my life **the news is used**"* | the **PowerPoint editor** is open at **45:05** with the caret sitting after `News Is Used` | +9 s |

Screen-change granularity is the 5-second sweep grid, so ±5 s is the measurement floor. **There is
no systematic offset between the two clocks.** The `+9 s` on the last row is the time he takes to
alt-tab out of the slideshow, not drift — the two rows either side of it are `+1 s`.

---

## SOURCE

| Field | Value |
|---|---|
| Video ID | **V17** |
| Original filename | `Bootcamp1 Wk8 051312 Part1 (57mins).swf` |
| SHA-256 | `2281fa8b92195bdd2fcc268c1ffce25295936faffc9c2825e82b9c50d407f767` — verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session on the flat `Bootcamp/` canonical path, **and re-verified after the frame-rate patch** to prove the original was not modified (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| Duration | 00:57:09 (audio measured **3429.642449 s**; SWF header **10,290 frames ÷ 3.0 fps = 3430.000 s**; `SOURCE_MANIFEST.md` 00:57:09 = 3429 s — **three independent figures agreeing to within 1.00 s**) |
| Lesson title | ⚠ **NOT PRINTED AS A TOPIC TITLE.** Every slide carries only the deck's running head `MARKET MAKER BOOT CAMP` (or `MARKET MAKERS BOOT CAMP` on the schedule slide, plural). The lesson's **second half** carries a printed section title — `TREND` — from `00:30:10` to the end of the file, and that is the closest thing to a topic title V17 prints. The spoken framing is `[00:01:33]` *"tonight we're gonna cover basic stuff trends trap moves"*. The quarantined per-lesson header's *"Primary Topics: Steve Mauro Beat The Market Maker (BTMM) Methodology"* is a generic non-answer, and its `RULES.md` / `NOTES.md` / `VISUAL_INDEX.md` are fabricated — see `QUARANTINE_REGISTER.md` **Q-018** |
| Session date | ⭐ **2012-05-13, AND IT IS CORROBORATED FROM INSIDE THE FILE** — unlike V16. `[00:00:11]` *"Today's the 13th regular session next week's the 20th"*, and the opening schedule slide (`V17_00-00-20_…png`) prints `May 13th - Regular Session`. Filename `051312` and `SOURCE_MANIFEST.md` agree |
| Week number | ⭐ **STATED, AND ALSO CORROBORATED.** `[00:02:36]` *"Welcome to week eight trade strong my friends"* and `[00:03:02]` *"We've been together eight weeks"*. ⚠ **And he immediately qualifies it** — `[00:11:18]`–`[00:11:22]` *"Have you been hanging out with me for eight weeks? \| Actually nine because we took an extra weekend between"*. See `V17_SOURCE_NOTES.md` §12 and open item **203** |
| Continuity with V16 | **NONE claimed, and none needed.** V16 was Part 2 of the 2012-05-06 recording; V17 opens a **new session a week later** with its own housekeeping block. It is Part 1 of two (V18 is Part 2 of the same night) |
| Frame rate | **3.0 fps** in the SWF header — read from **this file's own header**, not assumed (`SWF_CAPTURE_RECIPE.md` §10 as corrected by V10 R1 open item 87). The 10× sweep patch is therefore **3.0 → 30.0** here |
| Stage size | **1024 × 786** — the majority class. `GOTCHA 5`'s table gives `(512, 300)`, and the pre-click / post-click guard **confirmed it fired** rather than assuming it (`sweep.log`: *"play click CONFIRMED, stage changed"*) |
| Transcribed by | ASR, by a pre-ingestion session. Copied **byte-for-byte** and verified 2026-08-14 — see VERIFICATION below. The pre-ingestion file's own `# VIDEO` header block is **NOT carried over**: its *"Course Position: Video 18 of 21"* is wrong under `D-017` §2's renumbering (this file is **V17**), and its *"Primary Topics"* line names the methodology rather than the lesson |
| Transcription confidence | **MEDIUM–HIGH.** 690 markers, strictly monotonic, **zero** equal-adjacent pairs, **zero** backwards steps, gaps 1–12 s (mean 4.97 s), last marker `[00:57:07]` sitting **2.6 s** before the measured end of audio, and a speech rate of **155.2 wpm** across 8,870 words. It preserves its own mishearings — *"lupa tons"*, *"mayonnaise and ketchup"*, *"CDI only trades"*, *"the manays"*, *"for our markups"*, *"Scripps scalar"*, *"sharp fins"*, *"how and low"*, *"a core to wood to the low"*, *"the drugs bullshit"*, *"off-ship running out of money"*, *"Ambs with the mustard"*. **A fabricated transcript does not invent its own mishearings.** Defects are ordinary ASR failures on domain vocabulary, numbers and proper nouns; **the load-bearing ones are corrected below, each arbitrated by an independent ASR pass or by a printed slide** |

---

## SPEAKER TABLE — MANDATORY UNDER `D-025` consequence 3, re-adopted by `D-033`

| Speaker | Runtime | Basis |
|---|---|---|
| **Course author (Steve Mauro)** | **100%** — `[00:00:00]`–`[00:57:07]`, the whole file | Six non-acoustic strands, below. ⭐ **CERTAIN — and V17 supplies the self-naming V16 could not** |
| Guest presenter | **0%** | No second voice is introduced, addressed, thanked or handed to anywhere in the file. Two named helpers — *"Zan and car"* `[00:04:51]` — are described in the **third person** as people who *will* run a future setup day, not as anyone present |

**`COURSE_PROGRESS.md`'s V17 GATE (d) required this be TESTED rather than inherited from V16, and it
was — on strands fixed before the answer was known.** The acoustic cross-file screen was **NOT**
run, per V07's prohibition.

### THE SIX STRANDS — non-acoustic, `D-025`/`D-033` method

| # | Strand | Evidence, VERBATIM |
|---|---|---|
| **1** | ⭐⭐ **HE NAMES HIMSELF IN THE FIRST PERSON, AS THE PERSON THE STUDENTS EMAIL.** This is the strand V16 explicitly recorded as missing | `[00:56:46]`: *"I **Got some email saved Steve. It was a tough week. I couldn't find any trades.** Guess what? I **Only got one trade last week**"* — the student's mail is addressed to *Steve*, and the reply is in the same breath and the same voice, with **no pause and no attribution** |
| **2** | ⭐ **He answers a student who addresses him by name, in the same voice** | `[00:33:00]`: *"**Steve what's he gonna do when he opens? I don't know let you know.** Let me see what he moves then I'll make my move"* |
| **3** | ⭐ **He ventriloquises a student mocking him in the third person and answers in the first person inside the same passage** | `[00:53:22]`–`[00:53:30]`: *"of course you're gonna go \| **Steve's full of shit** in those talking about he's at three levels \| **But if the dealer traps you** one of these moves. That's why he's a stop loss man"* |
| **4** | **He owns and sets the course's calendar, first person, for the next six months** | `[00:00:28]` *"**I Am gonna probably** go out of town for a long weekend"*; `[00:01:05]`–`[00:01:09]` *"The final boot camp **I'm gonna be releasing** a new \| Trading strategy along with the indicator and scalar to go with it"*; `[00:00:53]` *"a week later **I'll be live in New Jersey**"* |
| **5** | **He grades, assigns and threatens homework in the second person and no one answers back** | `[00:06:02]` *"where are you at where you guys at by now? **You should have** your set of flashcards"*; `[00:12:15]` *"**Go back through the boot camp** and we'll hit it again"*; `[00:56:30]` *"**I'm yelling at you** one more time. Make the safety trade your signature trade"* |
| **6** | **Handover scan: ZERO.** | The same **17-pattern** superset V12–V16 used returns **ZERO hits across all 690 markers**: `take it away` / `turn it over` / `hand over` / `back to you` / `thanks Steve` / `my guest` / `joining us` / `over to you` / `take over` / `passing it` / `go ahead Steve` / `let me hand` / `let me pass` / `you're up` / `floor is yours` / `I'll let` / `welcome back` — **all ZERO.** ⚠ *(`welcome back` appears on the **title slide** as printed text, `V17_00-02-40_…png`; it is not spoken and it is not a handover.)* |

⭐ **WHY THIS IS `CERTAIN` AND V16'S WAS `HIGH`.** `V16_TRANSCRIPT.md` recorded, as its own weak
point, that *"the token 'Steve' occurs five times and **not one is a self-naming**"*. **In V17 the
token occurs four times and strand 1 is a self-naming in everything but grammar** — he reads mail
sent to *Steve* and answers it as *I*, with no third party in the room. **This was the V16 gap and
V17 closes it.** A reviewer who strikes strands 1–3 as *"quoting students"* is still left with 4, 5
and 6.

---
## VERIFICATION — `SETUP_ISSUES.md` `I-008`

`I-008` records that most committed transcripts in this project are **unverified**. This one is
verified, and the five checks below are the same battery V13–V16 used. Every figure was produced by
running something, not by reading.

### §1 — DURATION AGREEMENT, THREE INDEPENDENT SOURCES

| Source | Value |
|---|---|
| `ffprobe` on the extracted `audio.mp3` (last audio packet PTS) | **3429.642449 s** = `00:57:09.6` |
| SWF header, read this session: `frameCount 10290 ÷ frameRate 3.0` | **3430.000 s** = `00:57:10.0` |
| `SOURCE_MANIFEST.md` row V17 | `00:57:09` = **3429 s** |

**Spread: 1.00 s across three methods that share no code** — the tightest agreement of any lesson so
far. The filename label `(57mins)` agrees to within 10 s.

### §2 — MARKER-GRID INTEGRITY

| Check | Result |
|---|---|
| Markers | **690** |
| Strictly monotonic | **YES** |
| Equal-adjacent pairs | **0** |
| Backwards steps | **0** |
| Gap min / max / mean | **1 s / 12 s / 4.97 s** |
| First marker | `[00:00:00]` |
| Last marker | `[00:57:07]` — **2.6 s** before the measured end of audio |

**A transcript whose last marker landed after its own audio, or whose markers repeated or went
backwards, would be evidence of fabrication or of a mismatched file. None of those is present.**

### §3 — THE CONTENT MATCHES THE FILM, CHECKED EARLY (`GOTCHA 4`)

`GOTCHA 4` requires one screenshot compared against the transcript **before** any long capture is
trusted. Done at sweep frame `i=4`, burned timecode `00:20`:

* **Transcript `[00:00:11]`–`[00:00:57]`:** *"Today's the 13th regular session next week's the 20th …
  the 27th Memorial Day weekend … June 3rd the web class … on the 17th we're gonna have our final
  boot camp … Then July 1st we're gonna be on a two-month break."*
* **Frame `V17_00-00-20_boot-camp-schedule-slide-may-13-to-july-1.png`:** a printed schedule reading
  `May 13th - Regular Session · May 20th Regular session · May 27th Memorial day weekend- enjoy (no
  session) · June 3rd Web class 4 days · June 10th Recordings will be up review or retake the class
  as needed · June 17th Final boot camp regular session · June 24th Live in New Jersey!!! · July 1st
  2 month break- retake the boot camp via recordings. Put everything into action.`

**Seven dates spoken, seven dates printed, in the same order.** The right film is on the right port
at the right clock. ⚠ **And two of them disagree with the audio — that is `C-024`, not a capture
problem.** Four further content anchors are in the TIMESTAMP CONVENTION table above.

### §4 — IT PRESERVES ITS OWN MISHEARINGS

Twelve independent ASR failures survive in the committed text, and they are the kind a transcript
written from a summary would never invent: *"CDI only trades"* `[00:06:22]`, *"the Ambs with the
mustard"* `[00:07:45]`, *"my lines off a little bit … I'm getting all the blind"* `[00:15:47]`,
*"a core to wood to the low"* `[00:22:09]`, *"the oil cuts the Asian range"* `[00:26:45]`,
*"Scripps scalar"* `[00:01:54]`, *"sharp fins high and sharp fins low"* `[00:37:56]`, *"the drugs
bullshit"* `[00:49:48]`, *"off-ship running out of money"* `[00:49:07]`, *"the reset to the man a's"* `[00:51:07]` /
*"the man-e's"* `[00:51:25]`, *"a pair of lupa tons"* `[00:56:54]`, *"the mayonnaise and ketchup are
catch up in mustard"* `[00:56:57]`.

⚠ **`[00:56:57]`'s self-repair is worth naming separately.** The decoder produces *"mayonnaise and
ketchup **are catch up** in mustard"* — it hears the word, rejects it, and re-emits it. That is a
decoder artefact, **not** the speaker stuttering, and no claim in any V17 artifact rests on the
number of times the word appears in that line.

### §5 — INDEPENDENT ASR ARBITRATION

**Engine:** `openai-whisper` **`large-v3-turbo`**, English, run this session on the audio extracted
from the original `.swf`. It shares **no code and no lineage** with whatever produced the committed
transcript.

**⚠ THE COMMITTED TEXT BELOW IS UNCHANGED. Not one word of the 690-marker body has been edited.**
Corrections live here and nowhere else, each attached to **the marker grid's** timestamp — never the
second pass's clock, per the TIMESTAMP CONVENTION at the top of this file.

⏳ **STATUS AT THIS COMMIT: THE SECOND PASS IS STILL RUNNING.** It was started at the beginning of
this session on the extracted audio and had not finished when the capture commit was made. **This
section is completed in a later commit on this branch**, exactly as V16's was (`315db2c`
*"verify(V16): the independent ASR pass completed"*). ⚠ **Until it lands, treat every `[AUDIO]`-only
claim in the V17 set as single-engine.**

**FIVE CANDIDATES ARE QUEUED, fixed here BEFORE the second pass returns so the arbitration cannot be
retro-fitted to the answer:**

| # | Marker | Committed ASR | Why it is queued |
|---|---|---|---|
| **1** | `[00:21:10]` | *"All right, this is **G U** safety trade"* | ⭐⭐ **LOAD-BEARING.** The chart on screen is `GBPJPY,M15` and the slide credits `G/J`. **Two non-audio supports already say the ASR is wrong**; the second pass is the third, independent one |
| **2** | `[00:45:16]`, `[00:45:52]` | *"a **5200** crossover"* · *"The **5200** will cross over"* | ⭐ The slide prints `50/200`. Queued to see whether a second engine hears the slash |
| **3** | `[00:53:42]`–`[00:53:45]` | *"**15 25's** \| Total above the high below the low"* | ⭐⭐ **LOAD-BEARING.** This is the corpus's only spoken stop-loss distance and it is a five-word fragment (`A-123`) |
| **4** | `[00:26:10]` | *"Right past the man using the **dragon and backwards**"* | Answer-key point 2's mechanism is unrecoverable as rendered |
| **5** | `[00:09:13]` | *"You got a W formation on the one-hour chart **double-rearer**"* | `A-108` — almost certainly *double bottom*, but the pivot-zone shift rule (`§3`) turns on it |

**A sixth, not queued but flagged:** `[00:03:48]`'s *"chat box still love you. I still an onion"* is
garbled and carries nothing; no artifact cites it.

---

## TRANSCRIPT — VERBATIM, 690 MARKERS

> Copied byte-for-byte from the pre-ingestion `TRANSCRIPT.md`. **Nothing below has been edited,
> normalised or re-punctuated.** Its ASR defects are left in place; corrections live in
> VERIFICATION §5 and nowhere else.
>
> Body SHA-256 (this file's marker block, as extracted): `3034c8b4edfecea878d924c7b0fc97459f402c5e25f8af862e772a8db6e35925`


[00:00:00]
I got a lot of stuff tonight to cover a couple pop quizzes. I

[00:00:04]
Want to break down what's going on where we at where we are at our hat with everything. Okay, look

[00:00:11]
Today's the 13th regular session next week's the 20th

[00:00:14]
We're gonna have a regular session on the 27th Memorial Day weekend. It's a holiday in the US. There's gonna be no session

[00:00:22]
most people go out of town for a long weekend and

[00:00:26]
And I

[00:00:28]
Am gonna probably go out of town for a long weekend. All right, so

[00:00:32]
We're not gonna have a session. Okay June 3rd the web class is gonna be four days and

[00:00:39]
The following Sunday on the 10th

[00:00:43]
We're gonna leave the recordings up and you guys are gonna have a chance to review those

[00:00:48]
Okay on the 17th we're gonna have our final boot camp if you can believe it and

[00:00:53]
And then a week later I'll be live in New Jersey and

[00:00:57]
Then July 1st we're gonna we're gonna be on a two-month break. Okay, so this is how it's gonna play out

[00:01:01]
So we got tonight and two other boot camps left

[00:01:05]
The final boot camp I'm gonna be releasing a new

[00:01:09]
Trading strategy along with the indicator and scalar to go with it and it's it's not new to me

[00:01:16]
It's gonna be new to you guys. I mean you know about it. So I'm gonna be using it already

[00:01:19]
So I mean that know me from back in the day know about this already, but I will be releasing it for all the students

[00:01:27]
To help you maybe execute some trades better and over the next two months you can put it to use

[00:01:33]
Okay, so tonight we're gonna cover basic stuff trends trap moves next week

[00:01:39]
I think we're gonna do some fractional disparity stuff

[00:01:42]
We're gonna take a couple weeks off do the class have some recordings hang out for a while and then back on the 17th before

[00:01:49]
New Jersey will have the final boot camp where I'm gonna release a new

[00:01:54]
Scripps scalar and indicator. That's not an indicator. It's a script scalar and money management device and

[00:02:01]
I'm gonna go over the notes with it and we'll set it up on the platform and

[00:02:05]
Get you guys rolling okay

[00:02:08]
And then we're gonna take from July and August we're gonna hang out take a break

[00:02:13]
What I want you to do is go back over the boot camp stuff and if you haven't done the exercises and the things that

[00:02:19]
Supposed to be doing that'll be your chance to get caught back up and then after Labor Day weekend

[00:02:25]
We'll roll again for a couple of months going into the Thanksgiving holiday

[00:02:28]
Okay, we'll do October November and then that'll be it for the year if you can believe it man time flies. Okay

[00:02:36]
Welcome to week eight trade strong my friends

[00:02:40]
I hope that you are thinking about someone looking over your shoulder every time you pull the trigger

[00:02:45]
I hope that you're cutting back on the amount of trades you're taking and

[00:02:50]
Of course, I gotta tell you how to manage your expectations

[00:02:54]
I'm not gonna go over this. It's giving you good two good solid hours and making honest effort at the assignments

[00:02:58]
I've said it enough for said it eight times

[00:03:02]
We've been together eight weeks

[00:03:04]
Getting a lot of emails a lot of people have turned in the corner and seeing things like like never before I'm very very pleased with that I

[00:03:11]
I

[00:03:12]
Guess I'm kind of like the way to look at it's like I'm like an artist and

[00:03:17]
I always joke around about the

[00:03:20]
Perfect sense to me my Mona Lisa, but my Mona Lisa is you guys and when you get it

[00:03:25]
You get my art so if you see a

[00:03:29]
Picture in the museum and it moves your certain way

[00:03:31]
Well when you make some money or you can see what I'm talking about on the charts that moves me in a certain way

[00:03:36]
I know sounds kind of corny, but it's the truth

[00:03:40]
All right, I want the best for you guys. I want you to have success

[00:03:45]
That's why we're all here in the first place

[00:03:48]
Okay, chat box still love you. I still an onion. It's not gonna change two or three more classes. That's it. All right, so announcements going on

[00:03:58]
Live class I mentioned to you is gonna be New Jersey at Stevens Institute

[00:04:02]
June 23rd to the 27th at 6 p.m. So 11

[00:04:07]
We usually wrap up 10 10 30 but half hour questions have screwed around

[00:04:13]
Visit the New Jersey or bus section on the form for details

[00:04:18]
Or use this tiny URL

[00:04:20]
dot com slash mm fx lodging. It'll give you a list of the hotels in the area

[00:04:28]
Again the class will not be recorded or strained

[00:04:32]
Okay

[00:04:37]
All right prior to the live class we're gonna have a web class

[00:04:42]
June 2nd through the 6th

[00:04:44]
same hour 6 to 10

[00:04:47]
Saturday being the indicators chart set up day

[00:04:51]
Zan and car or one of the other are both will

[00:04:55]
Walk you through getting your platform set up and things for the new students how to use the scripts templates and all that stuff, okay?

[00:05:03]
All right, the recordings will be left up during the live event

[00:05:07]
Someone just asked me Gloria. I think it was will these recordings be left up over the summer the the newest class and the boot camp

[00:05:15]
Will be left up indefinitely

[00:05:18]
That's it. That's the new policy

[00:05:22]
Okay, so

[00:05:23]
This stuff is gonna be up listen. I tried

[00:05:27]
Encrypting and garbage and all these things and you know what doesn't matter

[00:05:30]
They're up there. They're being stolen anyway, so the only one I'm punishing is the group so that no more. It's over

[00:05:36]
The stuff will be left up, okay

[00:05:39]
I want to help you guys as to point and we're only helping teach on the internet when I help in our students and it doesn't make any sense, right?

[00:05:46]
so

[00:05:48]
There'll be up the newest class will be hung up left up until

[00:05:52]
after summer break and

[00:05:54]
Whatever the freshest newest classes will be up and boot camp will be left up until we do a new boot camp and replace it

[00:06:00]
Okay

[00:06:02]
It's so where are you at where you guys at by now? You should have your set of flashcards for our markups

[00:06:08]
You should do your for our mark up every week by the way

[00:06:10]
You should wait for eight hours into the session draw your support and resistance on the for our chart psychological levels

[00:06:17]
Where the dealer will exploit those levels, okay? We'll look at some markups today

[00:06:22]
Have you taken CDI only trades man? There's some good ones. I've won in there comment in on them

[00:06:27]
so they'd float to the top of the of

[00:06:29]
the student section there's some good TDI only trades and a lot of people are learning from this have you worked the big board

[00:06:38]
Some of you bitch to me about the big board. Listen. That's okay. I'm used to it. You can bitch at me

[00:06:43]
But here's the deal

[00:06:44]
Whether you actually got the trades right or not working the big board

[00:06:49]
Which should have happened is you just have to see how these jerks?

[00:06:54]
Dealers push the price hit it lay on it open the spread

[00:06:59]
And very their behavior at the high and low. That's what you're supposed to get out of the big board

[00:07:04]
It took me six months to start mastering the board. It was very difficult

[00:07:10]
But the point is is that you start to realize wow look how these guys cut the higher cut the low

[00:07:16]
Look how the numbers change drastically and then they take me trickle those are the things you're supposed to be seeing out of there

[00:07:22]
Okay, so don't worry about getting the trade right it's demo for God's sake

[00:07:26]
Get in there roll up your sleeves and watch how they lay price right on the low and with a lay price right on the high

[00:07:32]
And then they open the spread and you can just imagine them grabbing new orders above or below those numbers

[00:07:37]
That's the point of the drill, okay?

[00:07:41]
Moving average only trades again taking price out of there you should start to be able to see the

[00:07:45]
Ambs with the mustard when mustard crosses the catch up the confirmations the moving average channel where they separate and they kind of look like the TDI

[00:07:55]
Where they make a channel and prices on the outside those are the things you're supposed to start to see

[00:08:00]
These are ways to manage your trade and help you stay in the trade

[00:08:03]
A lot he had some trouble with the pivot points not a big deal the indicator does that for you

[00:08:09]
One of the biggest questions were my pivots don't match the pivots that you have on the chart. Yes, here's the reason why

[00:08:15]
When you measure the 24-hour period on a daily candle that can look closes at 5 p.m

[00:08:22]
Our indicators designed to take the pivots

[00:08:27]
Around 12 1 o'clock in the morning depending on your dealer and what his GMT offset is and recalculate the 24-hour period

[00:08:33]
So the pivots are freshly put in place right before the London open

[00:08:37]
Late age you're going into one and that's why that's set up like that and that's why your pivots will not match

[00:08:44]
It's interesting to know to be able to project the high and low and have a rough idea where it should come in does it work every day?

[00:08:49]
No, another question was that if you see candles falling down, but then the last candle you know it's been three days of drop

[00:08:56]
And it's midweek or it's coming to the end of the week

[00:09:00]
Because you know better you shift the pivot zone

[00:09:05]
To the pivot reversal

[00:09:08]
Okay, so what do I mean candles read it's down. That's an m1 m3 day

[00:09:13]
It's been dropping for three days. You got a W formation on the one-hour chart double-rearer

[00:09:19]
tracks to the low of the week

[00:09:21]
Shift the pivot zone to m2 m4 for the next day even though the daily candles read

[00:09:28]
The pivot projection is still down

[00:09:31]
People don't understand what we understand about trend and trend reversal

[00:09:35]
So you take the next set of pivots for your zone, okay?

[00:09:39]
It's kind of interesting that the pivot uses the open high low and closed as it's supporting resistance factors and

[00:09:47]
I told you the whole business was about the open Asian range Asian channel

[00:09:52]
The high and low and where the dealer goes back into consolidation. That's the pattern and that's what pivots are based on

[00:09:59]
That's what I want you to get out of that exercise that you're taking the open high low and closed of yesterday's price action and projecting it forward as

[00:10:09]
Support and resistance points on tomorrow's chart think about that

[00:10:13]
Support and resistance is the high below the Asian range which is where it opens and

[00:10:22]
The consolidation at the end of New York going into Asia, which is where it closes

[00:10:27]
Okay, if you just had your alcohol moment for me saying that congratulations

[00:10:34]
Okay, using ADR and high low markers. We talked about how the dealer or

[00:10:40]
market makers

[00:10:42]
Have a limitation on how much range they can use for a day

[00:10:46]
So the ADR is useful for looking for the New York reversal the high low markers the deals will fake to that level and work it and come near it the next day

[00:10:54]
Or trade 25 to 75 tips off of that level as a safety trade

[00:11:00]
Okay, these are the things you're supposed to start putting together in your mind if you're not

[00:11:04]
It's never ever ever too late my friends

[00:11:08]
All right, the takeaways from this per side service. Can you spot a clean setup yet?

[00:11:15]
Have you picked your signature trade?

[00:11:18]
Have you been hanging out with me for eight weeks?

[00:11:22]
Actually nine because we took an extra weekend between and you still

[00:11:26]
Don't have your flashcards made

[00:11:29]
Have you been marking up the four hour charts?

[00:11:31]
I

[00:11:35]
I'm trying to give you a deeper understanding as to how the dealer extends the high low

[00:11:41]
Pulls the level comes above below the same levels for stop triggers and trap moves

[00:11:46]
Trigger and trap trigger and trap. That's the business trigger the stops and trap the traders trigger and trap

[00:11:55]
Okay, understand how the dealer sets up

[00:11:58]
The retail traders for wrong directional moves

[00:12:02]
With the aggressive behavior at the high at the low

[00:12:06]
These are things you're supposed to be learning

[00:12:08]
Okay, if you're not

[00:12:11]
Go back through the boot camp and we'll hit it again

[00:12:15]
It's only over when you say uncle

[00:12:18]
As long as you don't give up on me. I ain't giving up on you. I promise you I

[00:12:24]
Don't know what it is why you can't turn the corner what what you got between your ears. That's baggage problem

[00:12:29]
Once but I promise you I'm gonna root it out and figure out how to fix all y'all

[00:12:34]
We'll get to the bottom of each one everyone to you

[00:12:37]
Okay, you should understand how to really use the TD item manage your trades now

[00:12:41]
You should be able to see blood in the water shark fin cross over

[00:12:45]
The TD online should make a channel and like almost like a moving average channel shark fin back in three levels of push

[00:12:53]
These are things you're supposed to be seeing

[00:12:55]
Can you understand the relationship of yesterday's high and low?

[00:12:59]
The behavior at those levels why the dealer works those levels?

[00:13:02]
Why he behaves a certain way at those levels those are things you should be taking away?

[00:13:06]
Okay, a big takeaway you finally understand that price cannot rise or fall indefinitely

[00:13:12]
So ADR is used to see and track this behavior the dealer can't go straight up

[00:13:17]
Camels don't close right on top of each other straight up in a line or straight down for that matter

[00:13:23]
The market swings that's what they do

[00:13:25]
Okay, all right a couple R D and exam R and D examples real quick. I was very proud

[00:13:31]
I think he's gonna be surprised to see it Andrew double this demo

[00:13:36]
How about that in a few days. I might add I'm very proud of him

[00:13:43]
Look at the dates on here

[00:13:46]
Last week of March

[00:13:49]
Going into April couple of weeks double this demo. That's about 50% a week in it

[00:13:56]
33% over three weeks

[00:13:59]
Not bad, huh?

[00:14:03]
Okay a pretty good flash card that I took out of the board that I thought was awesome. This is a very very nice flash card

[00:14:11]
It's got his amid is W on the same day

[00:14:15]
Short trade long trade all this reasons written on there. This is a pretty good flash card if yours don't look like this

[00:14:22]
Take a picture make them look like this

[00:14:25]
I just like the way it was labeled and he did a really nice job. Okay

[00:14:31]
All right this week to break down let's look at some charts

[00:14:37]
What kind of happened was there was what I call a level three week on the higher time frame

[00:14:42]
Okay last week was corrective in nature

[00:14:46]
This is pound dollar by the way. Sorry the pair corrected all week

[00:14:50]
Most people so it was a choppy week was volatile on the same he trades

[00:14:57]
You know what that is an excuse for retail traders

[00:15:02]
And I don't want you to fall into that trap of blaming the dealer for chop

[00:15:09]
What I want you to look for is

[00:15:12]
Short position near the high and a long position near the low everything else is bullshit

[00:15:18]
All right

[00:15:20]
Every day the dealer will make a high every day the dealer will make a low

[00:15:27]
The only variation on that theme is he will trade in between those numbers and

[00:15:33]
Repeat the same high or the same low and not necessarily take it out

[00:15:38]
Okay

[00:15:40]
So understanding that

[00:15:43]
You

[00:15:45]
Have your chart

[00:15:47]
You have your first state hours my lines off a little bit. Sorry. I just realize that now. I'm getting all the blind

[00:15:53]
I couldn't see the the wicks down here

[00:15:56]
Okay dealer makes the high of the week

[00:16:00]
Makes the high of the week

[00:16:03]
He trades it to the low the week

[00:16:06]
He issues a safety trade in here long and he also issues

[00:16:12]
A big fat M formation to finish out the week

[00:16:17]
Okay, you're your job is to take short trades here and long trades around in here

[00:16:23]
Okay

[00:16:27]
This is what I call a level three week

[00:16:30]
Price has been corrective in nature and chopping around to confuse the traders

[00:16:36]
So you can't figure out which way to go

[00:16:42]
Trade both ways without fear the dealers do it. Why can't you?

[00:16:49]
Okay

[00:16:57]
Going in Thursday going into Friday

[00:17:03]
It was a nice straightaway trade

[00:17:07]
Okay

[00:17:09]
When I want you to notice is that the dealer went to the top look at all these pins they grab my pen

[00:17:17]
Look at all these pins in here

[00:17:21]
That can only mean one thing. It's a trap baby

[00:17:24]
All right, he finishes what on a nice M hit the stops one more time pick up the money slightly above

[00:17:31]
closes aggressively below this entire

[00:17:35]
Work okay, look

[00:17:39]
He okay

[00:17:41]
one two three four five six seven eight nine ten eleven. What's eleven times fifteen minutes anybody

[00:17:52]
That's supposed to be an X

[00:17:54]
anyone

[00:17:55]
165 divided by 60 how many hours is that it's easy to go?

[00:18:00]
One two three four one hour one two three four two hours one two three four three hours

[00:18:06]
Yeah, four hour fifteen minutes. Thanks man. All right, so roughly

[00:18:10]
Three to four hours right the dealer trapped this area worked it for three to four hours and then in 30 minutes

[00:18:17]
He shifted his own away from all this action. Look at that

[00:18:23]
Okay, he spent all afternoon working on that crap and then in 30 minutes he took it away

[00:18:29]
Then what did he do he hit the stops and pulled back anybody that was thinking long

[00:18:34]
He made sure if they had their stop loss below the blueberry

[00:18:38]
How many traders you know put their stop loss below a moving average?

[00:18:42]
None you better not you guys in this group none. How many you know none zero?

[00:18:48]
I've heard of it, but I don't know any right. Thanks Casey

[00:18:53]
Okay, so look

[00:18:55]
He comes back. He snags those stops

[00:18:58]
Goes back and he goes the way he was supposed to go anyway

[00:19:01]
It's a trap. Maybe straight away the next night. He pins the 50 as a straightaway. This is not a W

[00:19:11]
Okay, if you took it you needed to get out at the manays or at least tighten up your stop

[00:19:16]
This is not a trade just straight away coming out of the peak formation high

[00:19:22]
The high of the week, okay?

[00:19:24]
straightaway

[00:19:27]
Fantastic car beautiful baby. Okay, all right pop quiz

[00:19:34]
I'm gonna show you two sets of trades over a few minutes

[00:19:37]
I

[00:19:38]
Want to know what the trade you're called and I'll of the two trades. I'm gonna show you I want you to tell me which one is better and

[00:19:45]
Why it's better

[00:19:47]
Okay, you don't have to pose to just write it down on your paper

[00:19:51]
Okay

[00:19:53]
I'm gonna put the first one up let you look at it for 30 seconds

[00:19:56]
Change it let you look at it for 30 seconds and then and I'll show you the answers, okay?

[00:20:01]
All right trade one

[00:20:12]
Okay, 30 seconds is too long, okay trade two

[00:20:23]
Okay, now

[00:20:27]
The answer those were both safety traders

[00:20:32]
What's the better trade it was pound yen and pound dollar?

[00:20:37]
Pound yen

[00:20:40]
The second one was a better trade. I took that one by the way. That's why there's more Sony

[00:20:45]
Because why it gives you a clear confirmation?

[00:20:49]
By a close above the catch-up in mustard and then source to its take profit

[00:20:54]
G you pound dollar. We'll look at it a second

[00:20:58]
Uses one bar to confirm and shift and there was no good entry on that trade. Okay, so let's look at it

[00:21:04]
Okay back in here

[00:21:06]
All right, this is G you safety trade

[00:21:10]
Okay, grab the pen

[00:21:13]
See this clothes more right here it crossed is above the catch-up in the mustard

[00:21:19]
This is a confirmed entry

[00:21:21]
So as it closes you got it and within minutes you're almost to your take profit the entire trade lasted 45 minutes to an hour

[00:21:32]
Okay

[00:21:34]
Entry was grabbed here on the open of this candle. There was absolutely zero draw down

[00:21:39]
The stop was very tight about 1819 pips

[00:21:43]
Okay, I took 40 off of there because it was getting late for me. I was tired

[00:21:48]
Okay

[00:21:50]
Now this is pound yen

[00:21:54]
Look at pound dollar

[00:21:57]
Here's the difference, okay

[00:21:59]
pound dollar does not have a nice pretty close into

[00:22:03]
Back into the moving averages, okay

[00:22:06]
But it's still a good trade if you took it don't beat yourself up

[00:22:09]
It's a great setup man because you got kind of a core to wood to the low and maybe you have a little bit better

[00:22:14]
W formation here. You got a nice shark fin blood in the water. All right, so look you didn't get a nice green clothes like you got on pound

[00:22:21]
yen

[00:22:23]
So this was the actual entry bar this bar is not an entry. It's blown out. It's too big

[00:22:31]
Okay

[00:22:33]
So bad is not an entry you ain't getting in here on this trade

[00:22:38]
So the first confirmed entry comes up here too late, man the four hours in the way you're ready or

[00:22:45]
45 pips off the low of the day too late scratch ain't no trade

[00:22:49]
Okay, and by the way, it's a trap. Maybe that's pretty

[00:22:55]
Okay

[00:22:57]
So that's why pound yen let's look at it again now that I've explained it pound yen's a better trade

[00:23:03]
You get a nice confirmed entry as soon as that can to close as you pull the trigger bam

[00:23:08]
That's where I got in at they slipped me a little those jerk wads

[00:23:12]
Man this happens every time you think I would have shut the shit off already. Okay, hold on

[00:23:18]
Sorry, man, I do maintenance everything

[00:23:22]
Yes, I don't know I'm scared, okay

[00:23:27]
All right, let's see

[00:23:29]
Pen back, okay, so yes nice confirmed entry. All right now

[00:23:36]
Here's what I want you to do

[00:23:39]
Okay, we went over the answers all right another quiz. Here's the question you're I'm gonna put seven points on a chart

[00:23:48]
And I want you to answer or explain on a piece of paper in front of you with the seven points are I

[00:23:57]
I'm gonna give you five minutes on this little quiz, okay, and then we'll go over the answers. So it is now

[00:24:05]
Seven o'clock straight up. I will be back at 705. I'm gonna shut my mouth. No, it's 701. I'll be back at 706. I'm gonna shut my mouth answer the questions

[00:24:14]
number one through seven on a piece of paper and right down everything that's going on starting now by

[00:24:20]
Wait, get up with the chart up, okay, go

[00:24:24]
five minutes

[00:24:27]
All right, let's go over this and only it's some of the questions in there

[00:24:32]
Sam yes, you could enter on the doji absolutely, okay

[00:24:37]
Here you go, man. Here's the answers

[00:24:40]
Okay, let me get my pen and we'll talk about it. Okay point one

[00:24:46]
Okay, peak formation

[00:24:48]
Is a miss peak formation low in the low of the week it was it was in the low of the week

[00:24:57]
Okay

[00:25:00]
Point two dealer handles the breakout traders. Here's the breakout traders in here

[00:25:06]
Okay, got him

[00:25:08]
This is a good look right here. This is a good opportunity short

[00:25:13]
But one of the reasons I don't want you to take this stuff anybody

[00:25:19]
Since I the Asian range

[00:25:21]
That's the answer for that if you took it

[00:25:26]
Okay

[00:25:28]
But you're not supposed to counter coming down the level one consolidation. Yes, you guys are seeing that

[00:25:34]
Okay, if you're gonna take this shitty stuff. This is what you got to ask yourself is

[00:25:40]
There enough room to trade back towards the low how many pips are here and then you have to figure out that if you only get

[00:25:48]
25 pips stop hunts. What's the range in the box plus the stop hunt is that enough to give you a take profit

[00:25:58]
Yep

[00:26:01]
Yes, Casey, okay, this is okay. It's not my favorite choice for trade the dealer handles the breakout traders here by grabbing their orders

[00:26:10]
Right past the man using the dragon and backwards

[00:26:13]
Okay

[00:26:15]
I

[00:26:16]
Want you to take the good stuff first I want you to master the good stuff the good stuff is

[00:26:22]
safety trade coming out of

[00:26:24]
V-bottom the formation

[00:26:27]
All right, this is a better trade, okay? All right

[00:26:30]
Is the dealer trading 25 point three is the dealer trading 25 to 75 pips off yesterday's low?

[00:26:36]
There's yesterday's low peak formation the distance from here here. Yes, he is

[00:26:42]
Okay

[00:26:45]
The oil cuts the Asian range as a visible stop hunt that was what I was just talking about here. He extends the Asian low

[00:26:53]
Okay, hello with the session in a visible stop hunting motion. He gives you a clean stop hunt

[00:27:03]
Okay

[00:27:04]
Mark and maker throws a spike it comes back for one hour, okay? He extended the low

[00:27:10]
You can arguably arguably say that he did it like one push then he tapped it to then he spiked it three he extended the low in three moves

[00:27:19]
right if you say that

[00:27:22]
He could have did one and then two and three all in the same candle

[00:27:27]
He extended the low

[00:27:30]
aggressively and he came right back above that low

[00:27:34]
Right he cut the low and came back above and stayed up there for a look one two three four five

[00:27:41]
An hour and 15 minutes if you're watching the big board and the dealer quits extending the low for an hour and 15 minutes

[00:27:48]
You take a long position

[00:27:50]
That's what out the benefit of a chart

[00:27:54]
Right one hour take a long position

[00:27:56]
W in the TDI at point six

[00:28:06]
Shark fin blood in the water a nice fat W

[00:28:09]
You don't have a W in price you have a W in the closing of price. It's pretty good

[00:28:16]
Okay, and number seven you got a nice consolidation you got

[00:28:22]
Four green bars price takes off for one hour

[00:28:26]
Okay, and it goes into its first level consolidation this was about plus 40 and change

[00:28:36]
Okay, and if you elected to get out there, that's fine you can go to bed and you had a nice night

[00:28:42]
All right, this is a safety trade. So let me say why is this a safety trade?

[00:28:46]
If you don't know why this is a safety trade, I'm failing you you better go back

[00:28:50]
This is a safety trade why?

[00:28:53]
Peak formation has been formed the dealer makes a visible stop hunt below the Asian range

[00:28:59]
25 to 50 pips as his normal stop hunt

[00:29:05]
And he's trading above

[00:29:10]
25 to 75 pips off of yesterday's low because the volume is trapped in here and

[00:29:16]
He ain't letting them out, baby

[00:29:18]
He's got all this money in this big fat greedy hands. He ain't letting it out

[00:29:21]
This occurred on gj and gu I like the gj and took it because I got a nice confirmed entry on this candle right here

[00:29:29]
But both trades were decent

[00:29:32]
No worries take either one if you took to you I'm not ridiculing your criticizing you I'm telling you me personally

[00:29:38]
I like to better because I got the confirmed candle

[00:29:41]
here and

[00:29:43]
And gu it didn't cross over the averages and shift his own it did it in one swipe

[00:29:49]
That's the only reason I liked it better and that's it

[00:29:52]
Okay

[00:29:54]
If you got it congratulations if you didn't this needs to be a flash card

[00:30:03]
Okay

[00:30:05]
I

[00:30:08]
Alright

[00:30:09]
Yes, I took that trade in gj and it was before the news I told you before or the news is bullshit. It's used to complete the pattern

[00:30:18]
Right the only news that I want your screw around is non-form

[00:30:22]
But if the pattern is right there and it's crystal clear the dealer uses the news to complete the cycle

[00:30:30]
If he throws you a safety trade

[00:30:33]
That's why it's called a safety trade because it almost always pays out I got to throw the almost always in there

[00:30:38]
But you catch the entry in there you're gonna scratch out or limit up and they're good solid trades

[00:30:46]
Okay

[00:30:48]
All right

[00:30:50]
Everybody good

[00:30:52]
Seeing that stuff

[00:30:55]
Okay, we're gonna talk about the dealer trend and some track moves and stuff it is

[00:31:00]
715 do we want to do a five minute break run to the bathroom and then go over the lesson?

[00:31:12]
Yeah, you know what I've I'm forgot yeah, no, I'm sorry. I would I thought I had the charts up let me look see what happened here

[00:31:22]
Yeah, I did

[00:31:25]
No, I

[00:31:28]
Ask me about false move week beginning false move week beginning

[00:31:33]
Okay, the deal of breaks to the upside after a corrective week he makes his false move he forms an M

[00:31:39]
This is the four-hour chart on GU by the way

[00:31:50]
Okay, I'm looking at the questions for a second before we move on okay, so yes on the break no on the break

[00:31:55]
Yes, I saw a bunch of wise in there. Okay, let me just answer this couple of stuff real quick Charlie good trade buddy

[00:32:04]
Yes, no one on the four-hour man you're looking for false move the dealer set the psychological support and resistance right first eight hours

[00:32:11]
He pinned it again ends off on a hammer makes a rise to form the high of the week and

[00:32:19]
Then he makes his move

[00:32:22]
Okay

[00:32:25]
Three pushes off the high or three price movements off the high

[00:32:31]
He forms out the low of the week

[00:32:34]
Okay, pulls one bar there. Here's your setup for your safety

[00:32:38]
Okay, he comes in makes the safety trade right there and in four hours it pays out faster than that actually

[00:32:46]
And then he actually forms up the second leg of the high of the week

[00:32:51]
And he corrects out and is corrected on Friday notice that this is inside this is an outside structure

[00:32:59]
Okay

[00:33:00]
Steve what's he gonna do when he opens? I don't know let you know

[00:33:04]
Let me see what he moves then I'll make my move when I move you move when the dealer makes his move

[00:33:11]
When he shows me his hand

[00:33:15]
Then I'll know what to do next

[00:33:18]
Okay

[00:33:21]
All right, Norm just take what I'm talking about

[00:33:26]
Okay for the false move take what I'm talking about on the four hour

[00:33:30]
Draw your levels extend these levels on your 15-minute chart and then look for areas where the dealer forms the high and low of the week

[00:33:38]
Drill down to the 15 minute and look for a possible entry. That's it simple

[00:33:43]
All right, so I'm you said you didn't get to confirm to candle above your averages

[00:33:51]
It's based on deal with feed man

[00:33:54]
The dealer might have closed that candle below held it back. They might have been some number there or whatever he didn't want to hit

[00:33:59]
Until he went through with the news

[00:34:03]
I can't help that but you know the answer to that is and it's not a good answer, but it's this truth is

[00:34:09]
That that's why I learned on the big board not on candlestick charts

[00:34:14]
Because if you understand the dealer sets the load is trading off of that low and he's not extended low for an hour and 15 minutes

[00:34:22]
Then I don't give a shit if the candle confirms I mean I do personally

[00:34:25]
But I'm saying the market makers don't give a shit if that candle's confirmed and I they don't trade that crap

[00:34:29]
This is that stuff is for our benefit

[00:34:32]
He all the dealer sees is that he extended to low the low was set and

[00:34:37]
He's now trading off of that number and not extending the low anymore if you look at the big board that's what that stuff

[00:34:43]
Explains to you so it confirmed candle above or below the movie average the dealer don't care he could care less

[00:34:50]
Okay, so understand that

[00:34:55]
Okay, how many tails that take to form a good M and W on a on a 15-minute chart

[00:35:01]
eight

[00:35:04]
Candles or above is a good solid M or W okay

[00:35:10]
Do I still look at the big board? Yes, that's the way I was taught I still look at the high and low can't help it

[00:35:19]
Okay, because then when you see when I see how the dealer lays you can almost pick the high and low by the way the dealer lays there in

[00:35:25]
If you haven't done the big board drill, please please please please and another please do it

[00:35:32]
If you don't do anything else, but log the highs and lows and see how the dealer handles it

[00:35:37]
I don't care if you take trades off and I'm just watch out the dealer handles the high and low on the big board

[00:35:42]
I promise you you're doing yourself a disservice. You don't need to look at it for a couple of nights

[00:35:48]
It's gonna make a difference in how you understand how these guys work

[00:35:51]
Kevin I don't know two weeks ago, maybe one did I do that anybody remember what week it was week six

[00:36:03]
Yeah, if just go back to the slides men go back to the boot camp if you haven't seen it

[00:36:08]
Okay

[00:36:11]
I

[00:36:17]
Don't want to go back to something we did previous have a lot of material to give glory to their recorded man go back and watch the recordings

[00:36:28]
Okay

[00:36:29]
You're asking me stuff that was covered in the boot camp you logged the times

[00:36:33]
I'm gonna just say real quick log the high and low at one o'clock subtract the high from the low set up the Asian range

[00:36:40]
You come back and you check way from the extended number

[00:36:47]
Okay, glory if you watch the board the numbers are gonna move my dear just the way it is

[00:36:53]
Go back and watch the boot camp if you have if you if you're confused

[00:36:57]
I'm pretty sure I explained it in the boot camp pretty thoroughly how to do it

[00:37:04]
Okay, all right, I don't always see more time and I got a lot of stuff to cover tonight

[00:37:10]
Okay

[00:37:14]
All right, did the quizzes

[00:37:16]
Okay, we're gonna talk about the trend a little bit

[00:37:20]
Okay, so how do you identify the trend right we know there's two types of trends there's the market maker trend which is the real trend?

[00:37:28]
Then there's the technical trend that the rest of the world sees

[00:37:32]
Okay, to me the levels are visible on all-time compressions

[00:37:37]
But I've been added a little while so to be fair. I want you to use the one hour chart

[00:37:45]
to view the levels

[00:37:47]
in the market maker cycles, okay?

[00:37:50]
The TDI on the four hour per chart is very telling if

[00:37:56]
You look for sharp fins high and sharp fins low on the four hour chart and trade those extremes

[00:38:02]
If you can't see anything else except sharp fins on the four hour

[00:38:08]
I promise you that's gonna help you tremendously sharp fin high blood in the water sharp fin low blood in the water on a

[00:38:15]
four hour chart

[00:38:18]
Above or below the support and resistance points

[00:38:21]
Okay, for those of you that have done the TDI drill you know what I'm talking about

[00:38:25]
Okay, there's support and resistance lines. There's a 50 in the middle, okay?

[00:38:29]
You get a sharp fin above these lines or below these lines on a four hour chart

[00:38:36]
You get blood in the water

[00:38:39]
prices gonna reverse

[00:38:41]
at least 50 pips

[00:38:44]
You can give you your trade, okay?

[00:38:48]
By definition, what's the big board the big board?

[00:38:51]
Last question on the big board the big board is all price action with the high and low

[00:38:56]
Go through the drill. I tell you how to pull it up. It's like control left. I can't remember

[00:39:08]
Just right click on and pull it up. It's the high and low

[00:39:14]
F10

[00:39:16]
12 F10 thank you guys

[00:39:20]
All right

[00:39:23]
The trend is set by the market maker can be reversed at any time

[00:39:27]
Dealers go both ways you got us get out of this trade the trend mentality and

[00:39:34]
Not be afraid to go both ways you go short off the high of the week

[00:39:39]
You go long off the low of the week

[00:39:42]
Doesn't matter both ways when it's setting up you don't know

[00:39:48]
If the high is gonna pay off or the low is gonna pay off you don't know you take them both

[00:39:53]
Most of the time you'll scratch out and small profit if you've got close to the true high or the true low

[00:40:01]
Okay, I have something coming on the last night of boot camp. That's gonna fix you guys

[00:40:07]
What understanding that you can trade both ways is gonna give you a major edge

[00:40:12]
The mint the retail mentality of oh by the pullbacks in an uptrend or by the plot on oh by the rallies that's it's bullshit

[00:40:23]
You need

[00:40:26]
To learn how to trade near the how and the low low the week high of the week looking for the peak formations and then

[00:40:33]
The stop on high drops and stop on low rises at the start of the session

[00:40:39]
Look to take positions when the dealer extends the high or low coming out of the Asian range aggressively

[00:40:46]
He is setting the trend for the day

[00:40:49]
The trend is being set

[00:40:53]
By the dealer trapping and trigger trap and trigger hit the stops high

[00:40:58]
Trap the breakout traders grab the people long and correct

[00:41:02]
Hit the breakout traders low hit the stops low

[00:41:07]
Correct and then rise

[00:41:10]
Trap and trigger trap and trigger. That's the business at different price points trap and trigger trap and trigger different levels

[00:41:19]
Don't get so caught up in your bias that you miss good set up staring you right in the face

[00:41:23]
If you don't have a signature trade I

[00:41:26]
Told everyone you your signature trade is a safety trade. It's the best trade out there

[00:41:32]
Bar none you could take V bottoms or W bottoms on that if you take a V and it comes back

[00:41:38]
Then start the clock over if you wait for the W that's okay, too

[00:41:43]
If you get a W and TDI off of the peak level one, that's okay

[00:41:51]
I want you to make your signature trade the safety trade

[00:41:56]
When they show up they pay out man, they're beautiful

[00:42:02]
Okay

[00:42:04]
The trend is generally set up as a three-day cycle as soon as I say that it goes six days right?

[00:42:14]
But understand that after the midweek reversal the reversal comes on Tuesday you'll probably have a four-day trend

[00:42:21]
Until Friday when they make the correction here's why

[00:42:25]
Once the trend is set there'll be a unidirectional swing for two and a half to three days

[00:42:30]
But if they move in a day early, let's say they set the low of the week on Tuesday

[00:42:34]
Then they'll swing Tuesday Wednesday Thursday Friday. That's four days

[00:42:39]
Then late Friday they'll make the correction

[00:42:42]
To end the week off of the higher off of the low and back in the consolidation open high low clothes

[00:42:48]
They'll make the clothes off of those numbers open high low clothes gives you the wick on the daily candle

[00:42:53]
Okay

[00:42:55]
See other stuff starts to tie in together the wick on the daily candle represents the consolidation off of the higher off of the low

[00:43:03]
To end the cycle for 24 hours which paints the daily candle

[00:43:09]
Okay, so day one is what I like to call reversal day

[00:43:15]
It's where you get the peak formation higher low. It's the beginning of our market maker dealer cycle or our dealer

[00:43:22]
Trend cycle. It's that's the first day the cycle the first move

[00:43:28]
It usually comes as a market surprise because everyone's reading oh

[00:43:32]
It's going above the four hours crossed over TDI is above the market baseline everything's on its way up

[00:43:38]
The trend's gonna go forever

[00:43:42]
It catches everyone that's using traditional methods and systems

[00:43:47]
Or following regular trend strategies it catches them off guard

[00:43:55]
Think about the last slide I showed you on pound dollar the prior week was corrective was down

[00:44:04]
The dealer came out

[00:44:06]
Spied down and pulled it away and then chopped all week

[00:44:10]
How many people were shorting that?

[00:44:13]
At the bottom trying to get a position

[00:44:20]
They were stuck until Friday and they're still not out because he hasn't cut the loan

[00:44:26]
The dealer is at the low for the week. He didn't extend the low yet

[00:44:30]
Okay

[00:44:33]
Huge right here

[00:44:35]
The news is used. Sorry about my membership here to perpetuate the false trend

[00:44:42]
The news is the trigger or the reason or the excuse to hit the stops or to spike away from the lower level shorts the news

[00:44:52]
It's part of the their scheme against the traders

[00:44:56]
Okay, you're gonna laugh at me, but I got a correct. It's gonna drive me insane for the rest of my life the news is used

[00:45:03]
Okay, save it

[00:45:06]
Okay, sorry get it blowback up

[00:45:12]
All right day two

[00:45:16]
Moving averages on the higher time frames will fire signal you get a 5200 crossover

[00:45:24]
Coming out of level one you'll get the crossover going until level two rise level two correction, okay

[00:45:30]
Traditional indicators will cross over or fire signal

[00:45:40]
Okay, when I say cut the low, I mean extend the low

[00:45:43]
Goes past the low they extend the low cut the low extend the low cut the high extend I okay, all right, so let me get back to this

[00:45:52]
The 5200 will cross over

[00:45:55]
Second day in a cycle if the blueberries present you'll get the crossover on the old blueberry

[00:46:03]
On traditional indicators the zero line

[00:46:08]
Or the 50 depending on what you like you'll get a MAC deep crossover CCI crossover CCI zero line crosses zero line MAC decross

[00:46:17]
RSI 50 cross

[00:46:19]
Okay, the problem with this is for retail traders is that they wait for the confirmation like

[00:46:28]
Just a system that comes to my mind is that if you get a crossover on MAC D they'll draw the high of that candle and

[00:46:35]
Then wait for it to close a break plus above that candle and close and then they'll take their entry and usually by the time that actually comes to pass

[00:46:43]
They're at a gas they're in trouble

[00:46:46]
Okay

[00:46:48]
So retail traders will wait for their confirmations whatever they happen to be

[00:46:53]
Okay, I just said that we're looking at levels on the one-hour timeframe if you look at the four-hour one hours good to okay

[00:47:00]
Day three here's what happens

[00:47:03]
The regular retail traders are convinced that this is the real move

[00:47:10]
Marketmakers will show

[00:47:12]
What we call a trend acceleration. It's in the textbooks. It's where prices moving away from the averages you get angle and separation on the averages

[00:47:22]
They're open and fanned out

[00:47:27]
Prices dancing above the mustard

[00:47:30]
Price won't cut the mustard. That's how you remember prices above the mustard

[00:47:34]
What happens is you'll even get on the 30 the 333 trade

[00:47:43]
You'll get Casey behavior self you'll get

[00:47:47]
The third leg of the third leg will show three candles straight up acceleration

[00:47:53]
That acceleration

[00:47:56]
Is this this is textbook terminology now that acceleration gets all the retail traders to go oh man

[00:48:03]
I'm missing the move euros going through the roof. I got to get on I got to get on and batch one of the dealer puts the brakes on

[00:48:11]
And he catches everybody long by showing three beautiful green candles at the end of a nice run up

[00:48:17]
That acceleration at 333 trade where he hits the last three bars

[00:48:22]
He gives you three vector candles at the end of a nice run and it looks like the trends going to kingdom come and if you don't get on you're gonna miss

[00:48:30]
that

[00:48:31]
Is the end of the dealer cycle most of the time and that's where we take the opposite because what happens?

[00:48:40]
dealer shows up he shows up he shows up

[00:48:44]
People buy he sells to them over three days four days the dealer becomes

[00:48:50]
heavy net short

[00:48:52]
If you are heavy net short, how do you get paid?

[00:48:57]
Correct a market against the retail traders and book a profit. That's

[00:49:01]
Terminology that's how the dealer does it so he'll show you something in one hand and

[00:49:07]
In the meantime, he's becoming that short net short net short. He's like off-ship running out of money. Let me correct against these guys

[00:49:14]
Hit the stops and bag some profit take them out

[00:49:19]
Okay, that's what you have to understand. It's a game with the dealer shows you on the chart

[00:49:25]
Is not real he's setting up the perception

[00:49:30]
For you to fall for it and then reverse off of it, okay?

[00:49:34]
A reversal is used for my market makers to book a profit

[00:49:41]
Think you really think the brokers matching you up with some dude in China the ECN the STP

[00:49:48]
The PTR the PTL. I don't know all those initials whatever the drugs bullshit

[00:49:52]
The dealer is taking the other side of your trade if they jump up and down so they're blue in their face and tell you they don't run the stops

[00:50:01]
They don't they're full shit

[00:50:03]
They take the other side of your trade

[00:50:06]
They don't have their names hoisted on top of these buildings in downtown because they're making the spread in the commission off for you

[00:50:13]
Think oh we make three percent on car loans

[00:50:16]
And we're just we bought a building the other day for nine hundred million dollars in downtown New York

[00:50:22]
Think about that it's BS man

[00:50:25]
It's all part of the ploy and the fleecing of America if you will or the fleecing of the traders

[00:50:35]
The dealers are taking the other side of the positions

[00:50:43]
Because they know most traders lose money

[00:50:47]
And the funny thing is when somebody beats them then they want to ban you out of their brokerage house

[00:50:52]
Can't have a winner in there

[00:50:55]
Okay

[00:50:58]
The reset this is confusing for a lot of you guys and

[00:51:02]
I'm trying to think who was posted a really good thing on the forum about how he saw

[00:51:07]
Before our timeframe the reset to the man a's and drive back

[00:51:10]
I think was Byron I'm not sure though anyway a trend reset will be used for market makers a book of profit but not reversed directions

[00:51:17]
So what happens is they'll go up up up they'll correct make a W formation to continue up

[00:51:25]
They usually do these reversals or resets rather at the man-e's or the blueberry

[00:51:36]
This is where there are retail order build-ups

[00:51:39]
Why because people trade across over the four hour they trade some kind of signal on a higher time frame they traded

[00:51:47]
20 EMA on a four hour charter or 20 EMA on a on a daily chart crossover a break plus a close they'll take that so

[00:51:54]
Naturally, that's where the orders build up so naturally that's where the aggressive behavior by the dealer will come in

[00:52:01]
Because how many people take the break below where the break above so what does he do?

[00:52:05]
He breaks above and below now what the hell do you do the dealer will break above will break below the 200 and go back above

[00:52:12]
And if you're trading that you're like shit. I'm long know I'm short. No, I'm long know I'm short

[00:52:15]
I think I'm longer then. Nope. I'm pretty short now. That's what that's what they do

[00:52:24]
Okay

[00:52:27]
If the dealer makes the reset for you expect three more days arise

[00:52:33]
But if no one falls for it he might only reverse after one more level or keep it in mind the timing

[00:52:40]
Is where I talk about the timing's okay? Well if he makes the midweek reversal on Tuesday

[00:52:44]
That's not really middle of the week and he makes a unidirectional swing till Friday

[00:52:50]
That was four days maybe he'll on Thursday. He'll make a pullback as a reset books and profit and then continue Friday

[00:52:57]
Sunday and Monday with the rise or only you Friday as one day

[00:53:03]
Make the M formation and reverse out for the following week

[00:53:06]
Okay

[00:53:14]
No, I'm no is the answer to question up there at 7.30 half hour ago. Sorry to saw it

[00:53:22]
So what happens during this time is four or five levels might be identified and then of course you're gonna go

[00:53:27]
Steve's full of shit in those talking about he's at three levels

[00:53:30]
But if the dealer traps you one of these moves. That's why he's a stop loss man

[00:53:36]
tight stop loss

[00:53:40]
Okay

[00:53:42]
15 25's

[00:53:45]
Total above the high below the low if you grab a good entry

[00:53:51]
You're gonna be good, okay

[00:53:58]
Okay

[00:53:59]
Peak formations high and low of

[00:54:02]
HOW

[00:54:03]
W L O W the highest point on the chart for the week

[00:54:07]
I

[00:54:08]
Know it could be Tuesday and you've seen a high on the chart and then it comes back Friday and it breaks that high on the chart for the week

[00:54:15]
For the last five days. I understand that

[00:54:17]
But the highest point on the chart from Sunday Monday Tuesday will change

[00:54:24]
But understand that the highest point on the chart on

[00:54:28]
The four hour looking at the entire week

[00:54:32]
Offers you the safest and highest and best opportunity

[00:54:38]
For a directional bias not for a trade to me the safest places is the safety trade

[00:54:43]
Okay, let's talk about that for a second

[00:54:46]
The safety trade assumes that the peak formation or confirms that the peak formation high or low is in place

[00:54:54]
Okay

[00:54:56]
Okay, Steve why do you like the safety trade because I don't have to screw around trying to figure out the highest and lowest point on the chart

[00:55:03]
The deal is already done it for me

[00:55:07]
Ah, maybe I like that now that safety trade might be my signature trade after all, huh? Mandy sound like a good plan

[00:55:14]
Think for a minute

[00:55:16]
Steve is at the high of the week. I don't know one will you know Steve?

[00:55:20]
I'll know tomorrow coming at a level one consolidation if the dealer makes a visible stop on 25 to 75 pits off of that number

[00:55:30]
Paint a V or a W for me clearly at 3 30 in the morning and I own that guy

[00:55:37]
Because I know that that peak formation is a lock for at least a London session for me to book my 50

[00:55:44]
That's the kind of trade I could put 50 standards on and go to the bank and buy my wife some lupa tons from other's day

[00:55:52]
Understand

[00:55:55]
Steve I'm having a hard time identifying the how and low

[00:55:59]
High a week low of the week. Okay. Hey, then you need to be trading the safety trade

[00:56:04]
Why because the peak formation is locked coming at a level one the dealer makes a visible stop on

[00:56:10]
In line with the peak against against the herd or with the herd to fake them long

[00:56:15]
paints a W or a

[00:56:17]
An M or V or an a

[00:56:21]
It's a lock the trades a lock

[00:56:25]
If you don't have a signature trade even though I yelled that you eight weeks ago to get one

[00:56:30]
I'm yelling at you one more time

[00:56:33]
Make the safety trade your signature trade

[00:56:36]
Okay

[00:56:38]
Okay

[00:56:39]
For God's sake, it's an easy trade you can't miss it

[00:56:44]
I

[00:56:46]
Got some email saved Steve. It was a tough week. I couldn't find any trades. Guess what? I

[00:56:52]
Only got one trade last week

[00:56:54]
And it was enough for a pair of lupa tons

[00:56:57]
GJ safety confirmed a close above the mayonnaise and ketchup are catch up in mustard

[00:57:07]
Coming out of peak formation low that's it
