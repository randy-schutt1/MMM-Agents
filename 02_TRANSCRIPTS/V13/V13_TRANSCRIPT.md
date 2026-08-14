# V13 — TRANSCRIPT

## SOURCE

| Field | Value |
|---|---|
| Video ID | V13 |
| Original filename | `Bootcamp1 Wk5 041512 Part1 (65mins).swf` |
| SHA-256 | `106bb8631c7d2274d1be99eeaa583e35bd0a49892a22fdf9eae378c700367807` — verified against `00_SYSTEM/SOURCE_MANIFEST.md` this session on the flat `Bootcamp/` canonical path, **and re-verified after the frame-rate patch** to prove the original was not modified (`SOURCE_INGESTION_PROTOCOL.md` §2) |
| Duration | 01:05:22 (audio measured **3922.311837 s**; SWF header **11,768 frames ÷ 3.0 fps = 3922.667 s**; `SOURCE_MANIFEST.md` 01:05:22 = 3922 s — **three independent figures agreeing to within 0.36 s**) |
| Lesson title | **NOT PRINTED as a topic title.** The opening frame is the generic banner `MARKET MAKER BOOT CAMP`, subtitled *"Welcome Back / Trade Strong!"* (`V13_00-00-15_title-card-welcome-back-trade-strong.png`). Every subsequent slide carries the same `MARKET MAKERS BOOT CAMP` header and no topic line. **This survived the screenshot pass**, unlike V12's, where the pass corrected an audio-only *"NOT PRINTED"* draft. The nearest thing to a title is the printed word **`TEST`** on its own slide at `[00:24:55]`. The quarantined per-lesson header's *"Primary Topics: Risk Management Fundamentals, Stop Loss Placement & Position Sizing"* is fabricated — see `QUARANTINE_REGISTER.md` **Q-014** |
| Session date | **2012-04-15**, from the filename `041512` and `SOURCE_MANIFEST.md`. **Corroborated from inside the recording, forward-dated, three ways:** `[00:02:00]` the Orlando meetup is *"Saturday"* and `[00:07:41]` names it **April 21st** — the Saturday six days after 2012-04-15; `[00:05:20]` *"Next session is going to be Sunday the 29th. That's two weeks"* — 2012-04-29 is a Sunday and is exactly 14 days later; `[00:17:52]` *"this is week five"*. **First lesson of Week 5**, and `SOURCE_MANIFEST.md` gives V14 as `Wk5 041512 Part2` — same date, same session |
| Frame rate | **3.0 fps** in the SWF header — read from **this file's own header**, not assumed (`SWF_CAPTURE_RECIPE.md` §10 as corrected by V10 R1 open item 87). The 10× sweep patch is therefore **3.0 → 30.0** here |
| Stage size | **1024 × 786** — the majority class. `GOTCHA 5`'s table gives `(512, 300)`, and the pre-click/post-click guard **confirmed it fired** rather than assuming it (`sweep.log`: *"play click confirmed: stage changed"*) |
| Transcribed by | ASR, by a pre-ingestion session. Copied and verified 2026-08-14 — see VERIFICATION below. The pre-ingestion file's own `# VIDEO` header block is **NOT carried over**: its *"Course Position: Video 14 of 21"* is wrong under `D-017` §2's renumbering (this file is **V13**), and its *"Primary Topics"* line is unsourced and, on this lesson, demonstrably wrong. Only the verbatim body is copied |
| Transcription confidence | **MEDIUM–HIGH.** Well-segmented, strictly monotonic, and it preserves its own mishearings. Defects are ordinary ASR failures on domain vocabulary and proper nouns, and **three of them are load-bearing and are corrected below from an independent ASR pass** |

---

## SPEAKER TABLE — MANDATORY UNDER `D-025` consequence 3, re-adopted by `D-033`

| Speaker | Runtime | Basis |
|---|---|---|
| **Course author (Steve Mauro)** | **100%** — `[00:00:00]`–`[01:05:21]`, the whole file | Eight non-acoustic strands, below. **HIGH confidence, over-determined** |
| Guest presenter | **0%** | No second voice is introduced, addressed, thanked or handed to anywhere in the file |

**`COURSE_PROGRESS.md` V13 GATE (b) required this be TESTED, not assumed, because V13 is a NEW WEEK
and a NEW DATE — the exact condition under which this corpus's author runtime has broken before
(100% V03 → 31% V04 → 0% for five lessons → 100% V10). It was tested, on strands fixed before the
answer was known, and the acoustic cross-file screen was NOT run, per V07's prohibition.**

### THE EIGHT STRANDS — non-acoustic, `D-025`/`D-033` method

| # | Strand | Evidence |
|---|---|---|
| **1** | **He is addressed as, and answers to, "Steve"** | `[00:16:15]` *"Like, hey, **Steve**, I had all of them indicators"* — quoting what students say **to him**; `[00:35:00]` *"Then you'll be like, **Steve**, there's 35 levels up"* |
| **2** | **He owns the course's email address and is closing the old one** | `[00:18:30]` *"**Steve at MarketmakersForks.com**"* (ASR for `steve@marketmakersforex.com`, printed on the slide at `[00:16:15]`); `[00:17:57]` *"I'm trying to close that down"*; `[00:18:13]` *"I keep saying **I'm going to terminate the address**"* |
| **3** | **He owns the student folder and the templates** | `[00:02:58]` *"**The student folder is up**… **I stripped everything out of there**"*; `[00:03:03]` *"It's just the simple worktime ribbon with no GMT offset"*; `[00:28:32]` *"**my template's** paying the S"* |
| **4** | **He sets, grades and schedules the course's own work** | `[00:24:47]` *"Since we're taking next week off, **we're going to take a test right now**"*; `[00:25:46]` *"**We're going over the material for the first four weeks. I want to make sure you're grasping everything that I've covered thus far**"*; `[00:04:38]` *"**I want you to** spend another week with the TDI"* |
| **5** | **He owns the schedule and can cancel a week of it** | `[00:01:55]` *"**There's going to be no boot camp next week**"*; `[00:05:20]` *"**Next session is going to be Sunday the 29th**"*; `[00:05:33]` *"we'll get started again with **week six through ten**"* |
| **6** | **He runs the live events and pays for them** | `[00:08:08]` *"**I'm going to be doing a live class in June**… **The venue is locked up**"*; `[00:09:50]` *"**The venue is paid for and the insurance is bought. It will happen**"*; `[00:09:56]` *"**I am not going to stream or record this class**"* — a unilateral policy change |
| **7** | **He authorises and schedules the meetups other people host** | `[00:13:15]` *"**I've spoken to Casey and asked her if she would consider hosting** the meetup"*; `[00:12:57]` *"**Contact me through email**"* if you want to start one; `[00:14:37]` *"**I like Dick to host it**"* |
| **8** | **Handover scan: ZERO.** | The same **17-pattern** superset V12 used (`take it away`, `turn it over`, `hand over`, `back to you`, `thanks Steve`, `my guest`, `joining us`, `welcome back`, `over to you`, `take over`, `passing it`, `go ahead Steve`, `Steve's/Steve is/Steve will`, `let me hand/pass`, `you're up`, `floor is yours`, `I'll let`) returns **two** lines, and **neither is a handover**: `[00:00:00]` *"**Welcome back**"* — the speaker greeting the class, and `[00:19:39]`-class *"I'll let"* forms absent. **No handover language exists in this file** |

**Named third parties appear and NONE of them speaks.** *"Kim Kay"* / *"Kim Cage"* / *"Kim K"* /
*"Kim Krompass"* `[00:00:10]`, `[00:05:55]`, `[00:13:39]` (ASR renders the name four ways — one
person, the San Francisco meetup host, and the printed forum post at `[00:12:15]` settles the
spelling); *"Car"* / *"Cars car"* (**Kar**) and *"Ray"* `[00:00:18]`; *"Jeff"* `[00:01:10]`;
*"Adam"* `[00:01:44]`; *"Zann"* / *"Zen"* `[00:02:15]`, `[00:16:38]`; *"Kainan"* / *"Kane in"*
`[00:02:58]`, `[00:18:13]`; *"Gordon"* `[00:05:02]`; *"Francisco"* / *"Francisco Casellas"*
`[00:15:09]`, `[00:41:56]`; *"Luther"* `[00:09:25]`; *"Jim"* / *"Jim Norsch"* `[00:08:48]`,
`[00:10:28]`; *"Casey"* `[00:13:15]`; *"Dick"*, *"Dave"*, *"Pat"*, *"Tom"*, *"Jenny"* `[00:14:04]`–
`[00:14:37]`; *"Rusty"* `[00:16:22]`, `[00:17:59]`, `[00:38:18]`, `[00:43:03]`; *"Ian"* `[00:21:32]`;
*"Gary"* `[00:21:49]`; *"Dana"* `[00:22:22]`; *"Jerry"* `[00:23:17]`, `[00:60:30]`; *"Gloria"*
`[00:58:39]`; *"Keith"* `[01:01:51]`; *"Ralph"* `[00:55:58]`; *"Chris"* `[01:05:05]`; *"Bodie"*
`[00:38:23]` (a film character). **Every one is a name the speaker reads off the chat window or
refers to in the third person; in each case the next line is the same voice continuing.** Recorded
because a name in a transcript is the commonest false positive for a second speaker.

---

## VERIFICATION — `SETUP_ISSUES.md` `I-008`

**Status: SPOT-CHECKED, NOT FULLY RE-TRANSCRIBED.** `I-008` is **not** discharged for V13 and is
recorded as still open. What was done:

| Check | Result |
|---|---|
| Final timestamp vs measured audio | `[01:05:21]` against **3922.31 s = 01:05:22**. **1 s** |
| Monotonicity | **1,183 timestamps, strictly monotonic, zero regressions, zero adjacent duplicates** |
| Largest inter-entry gap | **17 s**, at `[00:09:02]`. Consistent with the long silent stretches the lesson itself announces (`[00:27:22]` *"There is no audio because we're testing"*) |
| Preserves its own mishearings | **YES** — *"Marketmakers**Forks**.com"*, *"cars car"* for **Kar**, *"25 to 75 **pits**"*, *"rim rant"* for **Rembrandt**, *"Fennie indicator"*. A fabricated transcript does not invent its own mishearings |
| Independent ASR spot-checks | **FIVE segments, ~5 min 10 s of 65 min (7.9%)**, re-transcribed from the extracted audio with `faster-whisper small.en`, beam 5, **chosen for being load-bearing rather than convenient**. All five matched near-verbatim. **Three ASR garbles corrected — see below** |

### THE THREE CORRECTIONS, AND WHY EACH MATTERS

Corrections are recorded here and the body below is **left as supplied** (`REMEDIATION_PROTOCOL.md`
§2 — the superseded text is the point). Every downstream artifact quotes the corrected form and
cites this block.

| # | `[ts]` | Supplied (retained in body) | Independent ASR | Why it is load-bearing |
|---|---|---|---|---|
| **1** | `[00:54:51]`–`[00:55:04]` | *"here's the weakness with **Fennie** indicator… **We have a set to** 21"* | *"here's the weakness with **any** indicator… **we have it set to** 21"* | ⭐ **This is `A-084`'s passage.** *"We have it set to 21"* is a **first-person configuration statement about this deployment**; *"we have a set to 21"* is ASR noise. The corrected form is what `A-087` and the `A-084` narrowing rest on |
| **2** | `[00:55:22]` | *"it's limited **and when it sees**"* | *"it's limited **in what it sees**"* | Same passage. The corrected form is the one that makes the lookback argument coherent |
| **3** | `[00:30:23]` | *"So **25 pips box**"* | *"**It's a 25 pip box**"* | The stop-hunt-box distance, which `C-020` turns on |

**BOTH ENGINES AGREE on the two things a reader would most want to be an ASR error, so neither is:**

- *"It only looks back **21 periods**"* — **confirmed by both**, twice, `[00:55:04]` and `[00:55:28]`.
- The internal inconsistency *"on a one hour chart, it looks back **15 hours**"* `[00:55:07]` against
  *"it only looks back **21 hours**"* `[00:55:28]` — **confirmed by both engines, verbatim.** It is
  **the speaker's own misstatement**, not a transcription defect, and it is recorded as such in
  `A-087`. A session that assumed ASR here would have deleted real evidence.

Also confirmed verbatim by the independent pass, each in a different segment: the shadow-box
**self-correction** `[00:29:13]` *"3 to 4 a.m. New York, 9 to 10, **I'm sorry**, 3 to 4 a.m. London,
and 9 to 10 U.S."* (`C-020`); the safety-trade anchor distance `[00:39:28]` *"**25 to 75** pips"*;
and the drill stop `[00:19:04]` *"Use a **25 or 30 pip** stop loss, no limit order"*.

---

# VERBATIM TRANSCRIPT

[00:00:00]
Welcome back. Don't forget our trade strong. The bracelets are in transit. I got a note that they're shipping.

[00:00:10]
And what we're going to do is I'm going to ship some out to California for Kim Kay and she'll have them for her meetup.

[00:00:18]
And cars car and Ray are coming to Orlando. I'm going to give them out in Orlando and send Ray and car back with the set for themselves for their meetup groups.

[00:00:28]
So the bracelets will start infiltrating into the group over the next week or two. And then we'll have them for the live event.

[00:00:38]
Okay. All right. Manage your expectations. Look, I read this to you every week for a reason. All right.

[00:00:45]
The reason is that I want you to get the most out of this time together. All right. So I'm asking you again two hours a week.

[00:00:53]
I ask you this every week because you're still looking at stuff you're distracted. Try to pay attention, right?

[00:01:00]
Make an honest effort to do this stuff.

[00:01:03]
Execute and demo everything that we talk about and refrain from negativity in your own mind.

[00:01:10]
You've got to believe you've got to give yourself over to me. All right. Not that way, Jeff. I know you are, man.

[00:01:17]
Mentally. All right. You've got to give yourself over to me 100% and just trust that I'm telling you is right, man.

[00:01:26]
Really soak this stuff in.

[00:01:30]
All right. Chat box. I'm trying to ignore you. It's hard. You guys are really big typers.

[00:01:35]
But during the teaching time, I'm going to ignore the box. I'm not going to change this.

[00:01:39]
It's too distracting. It's not fair for the people that are doing the previous slide paying attention to me.

[00:01:44]
Hey, Adam. Hey, do me a minute.

[00:01:48]
All right. I got a lot of announcements. I want to cover. I'm excited. We got some classes locked up.

[00:01:55]
All right. There's going to be no boot camp next week.

[00:02:00]
I'm going to be hosting the meetup in Orlando on Saturday. I'm actually going over for a couple days.

[00:02:05]
I'm going to go Friday and hang out with Car and Ray and talk about student folders and other stuff.

[00:02:10]
Worktime ribbons. Things that drive you guys crazy. And then we'll have the meetup.

[00:02:15]
It's going to be Zann and I'm not sure if his wife is going to teach. It's going to be Ray and Car.

[00:02:22]
And I'm going to have a limited role over there. I'm kind of just going to be hosting and hanging out.

[00:02:26]
But we will try to either stream it and record it or just record it.

[00:02:30]
So we'll hang it in the forum in place of the boot camp for next Sunday.

[00:02:35]
But here's the deal. The reason we're taking a break in addition to the meetup is because I've gotten a lot of emails that you guys are falling behind in the boot camp.

[00:02:47]
All right. You haven't done the homework. You kind of half-assed it. You haven't really taken the time to do the flashcards.

[00:02:54]
Some of you are blaming me for the student folder. Or I guess what?

[00:02:58]
The student folder is up. I'm not sure if Kainan hasn't hung yet, but it will be up today.

[00:03:03]
I stripped everything out of there. It's just the simple worktime ribbon with no GMT offset.

[00:03:13]
It's a clock to help you find your broker's time. And then the basic basic stuff that we need.

[00:03:20]
Worktime ribbon, moving averages, TDI, not a bunch of garbage in there. Big price in the corner. That's it.

[00:03:30]
All right. So what I want you to do is you got to essentially have two full weeks until I come back.

[00:03:36]
So I want you to take the time to catch up with the group and get on target.

[00:03:40]
There's a lot of good stuff happening, man. If you're not doing the homework and you feel left behind, shame on you.

[00:03:46]
I'm getting letters every single day. People traded better blindfolded with the TDI.

[00:03:51]
Or should I say with one hand tied behind their back and they've traded in their life.

[00:03:55]
Just looking for the signals and executing based on what the TDI is showing them.

[00:04:01]
A lot of you got stopped out and then you wind and didn't try again.

[00:04:07]
It's a drill and it's demo. Okay? The point of it is to learn. To learn how to execute.

[00:04:15]
Get in there, roll up your sleeves, open up a $100,000, $500,000 demo account, and trade your ass off.

[00:04:23]
It's free practice money. Learn with TDI, showing you what works, what doesn't work.

[00:04:29]
Take note of the ranges and the important things that I've pointed out that I'll review here again to make sure you're getting it right.

[00:04:36]
Okay?

[00:04:38]
I want you to spend another week with the TDI. I want you to finish the flashcards and execute the drills, man.

[00:04:46]
We got another drill coming up, another blindfolded drill that's going to be awesome.

[00:04:51]
Get caught up and join the group and start trading strong, man.

[00:04:56]
So listen, two full weeks to do the drill. Make your flashcards.

[00:05:02]
Okay? Somebody Gordon, fantastic, man. Made over 500 pips on the pound and over 600 pips on the euro.

[00:05:09]
That's what I'm talking about, man. Fantastic. Did you feed your family on 1100 pips?

[00:05:16]
I think so, brother. All right.

[00:05:20]
Next session is going to be Sunday the 29th. That's two weeks.

[00:05:28]
Okay? You have plenty of time to do this stuff and get caught up. We're going five weeks out.

[00:05:33]
It's perfect. We'll take a two-week break and then we'll get started again with week six through ten or six through.

[00:05:39]
I don't know how many we're going to do yet. Okay?

[00:05:44]
All right.

[00:05:47]
Location for the meetup.

[00:05:50]
There's actually two meetups going on this week. If you live on the West Coast in California,

[00:05:55]
Kim Cage doing it and I'll post her location in a minute.

[00:06:00]
Those of you that are Georgia, North Carolina, South Carolina, Alabama,

[00:06:05]
Southeast United States, Miami, Florida, anywhere around here, anywhere in Florida.

[00:06:12]
Get in the freaking car and come hang out.

[00:06:16]
Okay? I know there's some really inexpensive hotels in Orlando in the celebration area.

[00:06:21]
It's like a days in, a holiday in. I'm telling you, I think there are 50 to 80 bucks a night

[00:06:26]
if you book them online. Take a ride down here Friday. Spend the night. Hang out.

[00:06:34]
Let's get together so that we'll go eat somewhere. Screw around after the meetup.

[00:06:40]
And just talk. We're going to do stuff that we're not going to teach lessons.

[00:06:46]
We're going to do trouble with your laptop, load your indicators, the stuff that's been plaguing you

[00:06:51]
that you don't want to talk about. All right?

[00:06:54]
All right. We're staying at the Bohemian in celebration. The address is on the bottom.

[00:06:59]
I think I blew it up. Let me see.

[00:07:03]
Yeah. We're on the water over here. Here we go.

[00:07:06]
Set 700 Bloom Street celebration, Florida. Write this down. Get the phone number.

[00:07:14]
Okay. 407566,000. We reserved a meeting room over there in the hotel, and I'm staying there.

[00:07:23]
So I'll be there Friday night. We'll be hanging out. We'll be eating in celebration in the square

[00:07:28]
around there, walking around. There's a good ice cream place over there. And then Saturday we'll have the meetup.

[00:07:34]
And we'll go out afterwards and hang out for a little bit. All right?

[00:07:41]
Okay. Oh, yeah. I forgot. It's 6 p.m. Saturday, April 21st at the Bohemian Hotel in celebration, Florida.

[00:07:51]
All right? So if you can make it, if you're just screwing around your board, you want to come down and just jump in the car,

[00:07:56]
don't think too hard about it, just come home. We'll figure it out, okay?

[00:08:01]
Come over there. We'll hang out. And if there's a thousand people, we'll have it outside in the courtyard or something.

[00:08:08]
Hope to see everybody that can make it there. All right. Upcoming class. I'm going to be doing a live class in June.

[00:08:15]
It's a lock. It's done. The venue is locked up. It's going to be June 23rd through the 27th.

[00:08:22]
It's going to be at Stevens Institute in Hoboken, New Jersey.

[00:08:26]
From that, you have a fantastic view of the city from that side.

[00:08:29]
Class is going to be as always 6 p.m. to 11 p.m. Not changing my sleep for you, suckers.

[00:08:35]
All right? Everyone is always welcome.

[00:08:41]
If you take the time to come see me, you're going to have a seat, man. If I have to give you my seat, because you know how much I sit down.

[00:08:48]
All right? What we're working on right now, we'll get this figured out, is I don't know if Jim wants to do it or we'll figure out how to handle it.

[00:08:57]
There's a contact person up there.

[00:09:02]
What I want to do is either put a posting on the board or maybe we'll put Stevens Institute or your bus or New Jersey or bus.

[00:09:11]
We'll figure something out.

[00:09:14]
There's dorm rooms available for a fraction of what it costs to stay in New York City and New Jersey.

[00:09:20]
I think they're like, I want to say 69 bucks a night and they house two people.

[00:09:25]
The only thing I want to remind you is that talking to some guys that stayed there, Luther in particular, is like, you've got to bring your stuff.

[00:09:32]
You've got to bring like paper plates and forks and paper cups and they just give you an empty room to stay in.

[00:09:38]
What a mattress. I'm not even sure if they give you sheets. I think you've got to bring your own sheets.

[00:09:42]
I can't remember.

[00:09:43]
But I'll figure this stuff out for you guys. We'll post it in the forum to keep everybody up to date on what's going on.

[00:09:50]
These are the dates they're locked. The venue is paid for and the insurance is bought. It will happen.

[00:09:56]
A major change that I'm doing, I mentioned to you guys, I am not going to stream or record this class.

[00:10:04]
In an effort to please the entire group, I pissed everybody off. It will not happen anymore.

[00:10:11]
Here's what we're going to do.

[00:10:15]
I'm going to do some type of web class a couple of weeks before I do the live event.

[00:10:23]
Those recordings will be left up.

[00:10:28]
Jim Norsch, from Post It For Me, let me read this because he knows.

[00:10:34]
The dorm rooms are now $75 a day, $375 for the week. Sheets are $5 to $10 for the week.

[00:10:42]
Let's just say $10 for the week, $375 and $10, $4.75. If you split it with two guys, I guess you'd have to double the sheet cost.

[00:10:51]
Two dudes in a room, two ladies in a room, or if you want to mix a mattress on to my business.

[00:11:00]
You're looking about $200 a week each. Not bad. Consider that you can't even get a room for $200 a night in New York.

[00:11:09]
I think you can under the steps. They put you in the broom closet for $195 a night.

[00:11:16]
All right, man.

[00:11:19]
Some of you just hemmed and hawed that I'm not going to stream or record.

[00:11:23]
Here's the deal. The people that come to see me live and take the time and spend the money and make the effort, I really appreciate that.

[00:11:30]
It's very nice of you to do that.

[00:11:33]
It's not fair to try to have this microphone thing and running around and try to stream it and all the technical issues that we've had over the last couple of classes.

[00:11:42]
So you'll have yourself a clean set of recordings if you can't make it.

[00:11:48]
The ones that are there will have a good class.

[00:11:51]
I just want to give everybody their money's worth when they come to see me.

[00:11:57]
The last class was atrocious with technical issues.

[00:12:00]
The classes are getting so big I have to run to the back to take a question.

[00:12:04]
It just eats up a lot of time and it's very difficult.

[00:12:09]
Don't be mad at me. Be happy. It's going to be a good class.

[00:12:15]
So to help those that can't make it, the next live class, I don't have to date yet.

[00:12:19]
I'm thinking first week of June, last week of May, but the memorial day's in there.

[00:12:23]
I'll get it figured out, man.

[00:12:25]
It's going to be two to three weeks before the live class.

[00:12:29]
Two weeks out I can take a break and then head back out.

[00:12:33]
The recording's going to be up for you guys.

[00:12:36]
No matter what you'll have recordings to listen to.

[00:12:39]
Ongoing meetups.

[00:12:41]
Many of you are not aware that there are meetup groups being held throughout the United States.

[00:12:46]
You don't even know this.

[00:12:48]
I don't mean meetup like the website. I mean our group, Marketmakers Forest, is meeting up.

[00:12:54]
I'll be posting this information in the form if you want to start one in your area.

[00:12:57]
Contact me through email.

[00:12:59]
If you want to get together with some other traders and you want to host it or you want to just

[00:13:05]
meet up and talk about charts, let me know that you're interested and we'll figure it out.

[00:13:11]
There's going to be a meetup coming to Dallas.

[00:13:15]
I've spoken to Casey and asked her if she would consider hosting the meetup and she said,

[00:13:21]
yes, it's not going to be every week.

[00:13:23]
It's going to be maybe once a month or once a quarter, we'll figure it out.

[00:13:27]
We're going to add it to the schedule for that area.

[00:13:32]
Currently, if you didn't know this, the meetups that are available to you are New York, New Jersey car host that.

[00:13:39]
San Francisco Bay Area, Kim K, the next one is the same day we're doing one April 21st,

[00:13:46]
Las Vegas, Ray, and Orlando, Zann, and I'll show up over there and whoever else we can get.

[00:13:55]
You're interested in doing one.

[00:13:57]
I know there's a meeting in California, but I think it's where I met a lot of you in that area.

[00:14:04]
I think it's a different meetup.

[00:14:05]
If you want to break out as a small group and do a separate meeting where you just talk about my stuff,

[00:14:13]
I know like Tom, Jenny, Dave, Pat, Dave, you guys had talked about that before.

[00:14:17]
I'm all for that.

[00:14:18]
If you guys want to get together somewhere and screw around and talk about trades and stuff, that's cool.

[00:14:23]
Miami would be good.

[00:14:27]
Yeah, Fort Selle is a little different, but if some guys want to break out from there and do a Steve Morrow meeting or a market maker sports meeting, I'm okay with that.

[00:14:37]
I like Dick to host it and maybe Dave, Pat, and those guys because they have experienced it holding the meetings.

[00:14:44]
They've been doing it for a long time.

[00:14:45]
I don't know if they're interested in doing that, but if you want to talk to them and tell them to contact me, we can do it.

[00:14:52]
No, we don't have nothing in the Midwest yet, so let's send me some emails and we'll try to put some stuff together, man.

[00:14:58]
We'll try to get some meetups, maybe at least once a quarter.

[00:15:01]
You guys can get together, meet, talk.

[00:15:06]
The reason why I want you to go, here's Kim's.

[00:15:08]
Let me get to that.

[00:15:09]
Okay, I don't know where this is in California, I'm not familiar with it, but it's in Napa and contact Francisco.

[00:15:18]
I'm proud of him too, by the way.

[00:15:19]
I didn't know he was helping Kim with the meetup.

[00:15:22]
That's awesome.

[00:15:23]
All right, it's going to be April 21st at 10 a.m.

[00:15:27]
So a little early for me.

[00:15:32]
And it's the same place that she's been going.

[00:15:34]
Rabble Bank, 700, Trankas, St. Napa, 94558, second floor boardroom, put this in your GPS or write it down or contact her on the board.

[00:15:45]
Okay.

[00:15:46]
If you haven't been, you need to go.

[00:15:48]
You need to check it out.

[00:15:49]
And if the bracelets come this week in time, she'll have them.

[00:15:52]
If they come Wednesday or Thursday, I'm going to FedEx them to her.

[00:15:55]
She'll have them Friday or Saturday morning.

[00:15:57]
Well, Saturday morning, it's going to work.

[00:15:58]
She'll have to have them by Friday.

[00:16:00]
If I get them in time Thursday, she'll have them in her hand Friday and she'll be giving them out.

[00:16:04]
Don't go over there for a stupid rubber bracelet.

[00:16:06]
Go over there to learn something.

[00:16:08]
All right.

[00:16:09]
Why should you go?

[00:16:11]
You can get help with some stuff that you're embarrassed to ask me.

[00:16:15]
Like, hey, Steve, I had all of them indicators.

[00:16:17]
I used the scripts.

[00:16:19]
That stuff.

[00:16:21]
All right.

[00:16:22]
Hey, Rusty, I would say I'll send you some over there.

[00:16:25]
You may hear something that I teach from a different perspective and it may help you.

[00:16:30]
Listen, I understand that I might say something a hundred times.

[00:16:34]
And then when someone else says it, you're like, wow, that Kim's something else.

[00:16:38]
Or you'll be like, oh, wow, that Zen really helped me turn the corner.

[00:16:41]
Listen, that happens.

[00:16:42]
It's part of the business.

[00:16:43]
I get it.

[00:16:44]
Maybe he puts it in such a way that it just clicks for you.

[00:16:48]
I understand that's part of the business.

[00:16:50]
But whatever it takes for you to turn the corner, that's fine.

[00:16:53]
All right.

[00:16:54]
You can get help with your laptops, platform issues, indicators, and yes, the damn boxes.

[00:16:58]
Screw around, figure out your broker's offset, and get your charts lined up on your laptop.

[00:17:05]
Look at some charts as a group.

[00:17:08]
Maybe look at some recent trades together and see if you were right.

[00:17:12]
Or if you took this stuff that other people were taken.

[00:17:15]
And you can find comfort in your struggles and realize you're not alone.

[00:17:20]
And that we have a pretty great group of people.

[00:17:23]
Sometimes you forget you're sitting at home by yourself in the middle of the night, depending on where you live.

[00:17:27]
And you're staring at your screen.

[00:17:30]
And you have no support or no one to talk to.

[00:17:32]
These groups offer support, but you realize it or not.

[00:17:40]
Okay.

[00:17:42]
So anyway, that's why I want you to try to make one and see if you can do it.

[00:17:47]
Okay, look, real quick on this email stuff.

[00:17:49]
Many of you guys are still using the wrong email address.

[00:17:52]
Please, this is week five.

[00:17:54]
Some of you are sending it to MMM4X.

[00:17:57]
I'm trying to close that down.

[00:17:59]
I know, Rusty, oh my God, all right.

[00:18:01]
Change over to the new address to avoid any miscommunications between us.

[00:18:04]
I'm trying not to answer that mailbox.

[00:18:06]
I'm only checking it once or twice a week now, but I go in there and I'm like,

[00:18:10]
oh, damn it, there's people still writing to me, all right.

[00:18:13]
I keep saying I'm going to terminate the address, but I think I'm going to talk to Kane in this week

[00:18:18]
and see if I can put an auto responder on it.

[00:18:21]
If I put an auto responder and you'll get it back saying that this address is no good anymore.

[00:18:26]
Let me work on that.

[00:18:28]
I know, just do it already, right?

[00:18:30]
Steve at MarketmakersForks.com.

[00:18:36]
Okay, TDI drill.

[00:18:39]
I'm going through the email stuff now.

[00:18:41]
A lot of you did not understand the drill, it was intended, so let me lay it out one more time for you.

[00:18:46]
All right, open a fresh demo account separate from your other stuff.

[00:18:52]
Remove everything from the chart, accept the TDI and blow it up, stretch it out.

[00:19:00]
Enter and exit the trades from what I've shown you last week.

[00:19:04]
Use a 25 or 30-pip stop loss, no limit order.

[00:19:07]
Don't get all, people are like, oh my God, what size am I stopping us supposed to be?

[00:19:11]
What am I doing?

[00:19:12]
It's not about a stop loss and a take profit, it's not about those items.

[00:19:16]
It's about seeing the signals.

[00:19:18]
Just throw a 30, 25, 30-pip stop loss on there and don't worry about it.

[00:19:23]
Don't put a limit order.

[00:19:25]
It's about trying to understand what the indicator is indicating.

[00:19:30]
All right, it's not about, oh, I got to have my stop on.

[00:19:33]
It should be 22.7-pip.

[00:19:35]
I don't care about that stuff for the drill.

[00:19:37]
I don't care about it for the drill.

[00:19:39]
You're trying to get clean entries as a shark fin.

[00:19:43]
That's the cleanest entry, that's what you're trying to find, nothing else.

[00:19:46]
Okay, the pullback in the TDI to the market baseline is a checkpoint or an entry.

[00:19:51]
Anytime you see a shark fin that turns over and crosses what?

[00:19:55]
That's an entry.

[00:19:57]
The best entries are outside the volatility bands at the extremes.

[00:20:02]
Okay, at checkpoints, market baseline, a volatility band break and a volatility band return.

[00:20:10]
These are reasons to hold or fold.

[00:20:13]
If you got stopped out once or twice and slammed your mouse and threw your keyboard at your wife and got all pissed off, you didn't learn anything.

[00:20:22]
Open up a fresh demo and burn some trades, man.

[00:20:26]
Keep after it until you have success.

[00:20:29]
I hope you got frustrated.

[00:20:31]
That's the point.

[00:20:33]
It's a learning experience.

[00:20:35]
The goal is to see what works and doesn't work.

[00:20:39]
And then once you put pride back on the chart, you're going to be that much better for it.

[00:20:43]
Alright, you're going to see improvements.

[00:20:46]
A lot of people had some improvements this week just from doing the drill.

[00:20:51]
Some of you didn't do it.

[00:20:53]
Shame on you.

[00:20:55]
You got another week to get on it, alright?

[00:20:59]
Okay.

[00:21:01]
The takeaway from this stuff that we're doing, most traders rarely take the time to do the exercise.

[00:21:07]
Therefore, most really don't understand how to use an indicator.

[00:21:11]
Doesn't have to be TDI.

[00:21:13]
Could be MACD.

[00:21:15]
Most people that I've met really don't know how to use an indicator.

[00:21:20]
They just put it on there and they go, oh yeah, I'm going to add it to below or above a line.

[00:21:27]
Okay.

[00:21:29]
What you're trying to understand is what the signals look like.

[00:21:32]
Alright, Ian just brought up a very good point.

[00:21:35]
He got frustrated waiting for a good entry.

[00:21:37]
Guess what?

[00:21:38]
That's the business.

[00:21:40]
Your job is to wait for pristine, clean, solid entries.

[00:21:45]
Alright, it says on someone's email, I can't remember who I get paid to wait enough to try.

[00:21:49]
I think it's Gary's.

[00:21:52]
Okay.

[00:21:55]
Danger attitude about what a good setup is and forcing stuff and learn to wait.

[00:22:01]
Learn to be patient.

[00:22:04]
The whole point is to wait for the shark fins to come out of the water, high on the band or low on the band,

[00:22:13]
below the support and above the resistance levels.

[00:22:16]
Cross blood in the water, come back inside the band.

[00:22:20]
Okay.

[00:22:22]
Dana shame on you for not doing it.

[00:22:24]
You've been around too long.

[00:22:25]
I called you out.

[00:22:26]
Sorry.

[00:22:27]
Alright.

[00:22:28]
What a valid signal looks like or setup.

[00:22:30]
If you can grasp the understanding, one's price action is added back to the chart, you're going to trade better.

[00:22:36]
What I'm asking you to do, what we're doing here together as a group is we're breaking the little segments down of stuff that you should know.

[00:22:45]
And I take it for granted because I've been around for a while that everyone just knows this stuff and that's my fault.

[00:22:51]
It's stopping now.

[00:22:52]
I'm trying to help you guys.

[00:22:54]
Right now you're trading blind with just the TDI.

[00:22:56]
Next week, I have another blindfolded drill for you.

[00:22:59]
I'll get to it.

[00:23:01]
Okay.

[00:23:04]
All I want you to understand is that what is the TDI showing you how to truly use that?

[00:23:08]
And look, if you use Rainbow Stocasics or MACD, I don't really want you to use that shit, but if you do,

[00:23:14]
then do that stuff blindfolded.

[00:23:17]
Jerry wrote that it works so well, it might just trade like that.

[00:23:22]
Yeah, some of you are frustrated with the amount.

[00:23:25]
Go ahead and add a couple pairs this week.

[00:23:27]
That's fine.

[00:23:28]
In fact, why don't you open it up for the full spectrum of the majors and it may be GBPCHF and EJ for the crosses.

[00:23:36]
That's 10 pairs to look at for the shark fans and stuff.

[00:23:40]
I just want you to learn how to do the drill.

[00:23:42]
The reason I have limited it to two pairs, so we're all looking at the same stuff, but I just want you to get it.

[00:23:47]
I want you to understand.

[00:23:48]
So open it up to the majors plus two crosses, EJ and GC.

[00:23:54]
Okay.

[00:23:55]
I'm telling you it's going to make a huge difference in your trading.

[00:23:59]
I did it.

[00:24:00]
I was forced to do it and I did it.

[00:24:03]
Okay, I can't hold a gun to your head, but listen, accountability to the group, trade strong.

[00:24:09]
This is going to make you stronger.

[00:24:11]
When you work out at the gym, you don't go in and work your entire body in one sitting.

[00:24:16]
You won't be able to move the next day.

[00:24:18]
But what do you do?

[00:24:19]
You work buys and tries one day.

[00:24:21]
You do chest shoulders and back.

[00:24:22]
Then you come back and do legs.

[00:24:24]
This is what I'm trying to do.

[00:24:25]
I'm trying to work the individual parts of the chart.

[00:24:28]
And then when we put it all back together, you're going to have a hot body for the beach, all right?

[00:24:33]
Okay.

[00:24:34]
You understand?

[00:24:35]
We're breaking segments down.

[00:24:37]
Next week, TDI, you're working your arms.

[00:24:39]
Next week, you're going to work your back.

[00:24:42]
Okay.

[00:24:45]
All right.

[00:24:47]
Since we're taking next week off, we're going to take a test right now.

[00:24:50]
Pop quiz.

[00:24:52]
Take out a piece of paper and a pencil.

[00:24:54]
I don't really have the stuff numbered, but I want you just to number your paper and try to keep track.

[00:25:00]
All right.

[00:25:02]
What I'll do is I'm going to shut my mouth.

[00:25:04]
I'm going to put some screens up.

[00:25:06]
I'll leave them up for, I don't know, a couple minutes each screen.

[00:25:11]
Then we'll take a break.

[00:25:12]
I'll go over the answers.

[00:25:14]
And then we'll get into the lesson.

[00:25:16]
Okay.

[00:25:17]
Everybody ready?

[00:25:18]
Got your paper?

[00:25:21]
Okay.

[00:25:28]
The questions, the screens were a lot of questions on there.

[00:25:31]
I'll leave up for five minutes.

[00:25:32]
And the ones that wanted to questions, I'll leave up for three minutes.

[00:25:37]
All right.

[00:25:38]
We'll get through it.

[00:25:39]
Okay.

[00:25:45]
All right.

[00:25:46]
We're going over the material for the first four weeks.

[00:25:48]
I want to make sure you're grasping everything that I've covered thus far.

[00:25:52]
If you don't see this stuff in the test, if you're failing the test,

[00:25:56]
then this is what you need to work on over the next two weeks.

[00:25:59]
Okay.

[00:26:01]
All right.

[00:26:02]
I'm going to shut up.

[00:26:03]
Knock them out.

[00:26:04]
All right.

[00:26:05]
Next step.

[00:26:07]
All right.

[00:26:12]
Next slide.

[00:26:16]
Yes.

[00:26:17]
Next slide.

[00:26:20]
All right.

[00:26:21]
Next slide.

[00:26:28]
Okay.

[00:26:34]
Obviously, you don't have the charts.

[00:26:35]
So I'm going to put up a couple of charts, draw a line on your paper or just make points along the way and mark it.

[00:26:43]
Figure out some way to mark it on a piece of paper so you can get an idea.

[00:26:46]
Okay.

[00:26:47]
All right.

[00:26:53]
All right.

[00:26:54]
You guys good?

[00:26:55]
All right.

[00:27:01]
I hope you're not just sitting there with your arms folded and not trying to do it.

[00:27:07]
Waiting for me to come back.

[00:27:08]
All right.

[00:27:09]
Next chart, man.

[00:27:16]
Okay.

[00:27:17]
I'll be back.

[00:27:22]
There's no sound because we're taking a test.

[00:27:24]
There is no audio because we're testing.

[00:27:26]
All right.

[00:27:27]
Next chart.

[00:27:34]
Okay.

[00:27:35]
The arrow is pointing to a setup.

[00:27:37]
What is it?

[00:27:39]
Okay.

[00:27:40]
Next.

[00:27:43]
Now, I'll simply leave the note or you don't.

[00:27:45]
Okay.

[00:27:46]
Next chart.

[00:27:49]
All right.

[00:27:50]
I don't know how you can do it, but mark the TDI.

[00:27:54]
Okay.

[00:27:55]
You got three of those.

[00:27:56]
Take a snapshot of it, mark it on your screen, whatever.

[00:27:58]
Write it on a piece of paper.

[00:28:00]
Okay.

[00:28:01]
I'll give you three minutes per slide.

[00:28:03]
There's three of them.

[00:28:04]
All right.

[00:28:05]
You're ready for the next one?

[00:28:15]
Okay.

[00:28:16]
Next chart.

[00:28:19]
Mark it up.

[00:28:21]
All right.

[00:28:24]
What time should the blue box stop painting?

[00:28:27]
Depending on where you're dealing, how you set it up, 1 or 2 a.m.

[00:28:30]
New York is fine.

[00:28:31]
Okay.

[00:28:32]
The reason for the variance is daylight saving time, I don't change all my computers back.

[00:28:38]
And my template's paying the S.

[00:28:40]
But if you're setting it up new, you can make a winter

[00:28:45]
and a summer template.

[00:28:47]
So the box will adjust the same.

[00:28:49]
If you're going to make it stop painting, make it 1 a.m.

[00:28:52]
If you haven't done it yet, or you want to go back and change it, if you have a choice, make it 1 a.m.

[00:28:59]
New York time, by the way.

[00:29:01]
Sorry if you guys down under.

[00:29:03]
All right.

[00:29:04]
What's the purpose of the blue box?

[00:29:06]
The notes, the market maker spread, measures the Asian range.

[00:29:11]
Simple.

[00:29:13]
What time should the shadow box paint?

[00:29:15]
3 to 4 a.m. New York?

[00:29:18]
9 to 10.

[00:29:20]
I'm sorry, 3 to 4 a.m. London?

[00:29:22]
And 9 to 10.

[00:29:26]
U.S.

[00:29:29]
What trade sets up in the shadow box?

[00:29:33]
The Brinks?

[00:29:34]
And there's two times for that.

[00:29:36]
What are they?

[00:29:37]
3 45 and 9 45.

[00:29:40]
If you're going to do summer or winter, 1 o'clock summertime.

[00:29:47]
If you're going to do summer or winter, make the box always 1 o'clock.

[00:29:51]
If you're going to make two templates, make the box always 1 o'clock, New York time.

[00:29:58]
All right.

[00:29:59]
What time roughly should the red box start to appear on your chart?

[00:30:04]
8 to noon.

[00:30:07]
What's the purpose of the red box?

[00:30:09]
New York City reversal, I think I missed one.

[00:30:11]
What distance should the stop hunt box be from the blue box?

[00:30:16]
25 at the bottom or start?

[00:30:19]
50 pips on the top side of the range.

[00:30:22]
Okay.

[00:30:23]
So 25 pips box.

[00:30:27]
25 pips away from the top or bottom of the blue box.

[00:30:31]
All right.

[00:30:37]
All right.

[00:30:38]
What did the first four hour, first two four hour candles determine in the weekly cycle?

[00:30:45]
Simple answer is psychological support and resistance level.

[00:30:48]
Okay.

[00:30:49]
It's the Asian range of the week, right?

[00:30:52]
We talked about on the bigger pattern.

[00:30:55]
What's the how?

[00:30:57]
HOW, high of the week.

[00:30:59]
What's the LOW or low of the week?

[00:31:03]
If the peak formation is identified, what is the direction of the trades?

[00:31:10]
Simple answer away from the peak or stop hunt in line with the peak reverse.

[00:31:16]
How many days should the bias be expected?

[00:31:20]
2 to 3.

[00:31:21]
Can it go 4 or 5?

[00:31:24]
Yes.

[00:31:25]
Okay.

[00:31:26]
2 to 3, trade away from the peak.

[00:31:31]
Look for something to settle in and then look for the reversal signals.

[00:31:35]
What's the reason to vacate any trade before the stop loss is triggered?

[00:31:41]
Dealer hits the level again and closes above or below it on a 15 minute chart.

[00:31:46]
So what does that mean?

[00:31:48]
The dealer extends the high again or extends the low again and stays above.

[00:31:55]
He's probably going to extend the level to the next strike zone.

[00:31:59]
So if you're in a trade, you don't have to sit there like a moron and watch your stop

[00:32:04]
get taken out.

[00:32:05]
Okay.

[00:32:06]
No offense if you do that.

[00:32:07]
I'm not calling you a moron.

[00:32:09]
But here's the deal.

[00:32:10]
This is one of my pet peeves.

[00:32:12]
And this is in every textbook that's out there and I freaking hate it.

[00:32:16]
It's stupid.

[00:32:17]
It's the difference between an amateur and a professional.

[00:32:20]
Here's the statement.

[00:32:22]
Take your entry, put your stop and your limit, and let the market prove you wrong.

[00:32:28]
You ever heard that?

[00:32:33]
Look, if you let the market prove you wrong, guess what?

[00:32:37]
It's going to prove you wrong.

[00:32:40]
You're smarter than these stupid cliches and these statements that have been out there.

[00:32:44]
So what I'm telling you is that if you get a setup that looks good and you take it and the dealer comes back

[00:32:52]
and extends the high or low that you traded off of, that trade is now invalidated.

[00:33:00]
Why not scratch yourself out with 10 or 12 pips instead of sitting there and giving the dealer 25?

[00:33:06]
Or a total of 25?

[00:33:09]
If you know he's going to move to the next level, scratch yourself out with a small loss,

[00:33:14]
control the amount of money you lose, look for a re-entry on the next level strike zone,

[00:33:19]
and then make it back faster.

[00:33:23]
If you cough up 25 pips to the dealer and you make 50 on the next trade, you're only plus 25 or 27.

[00:33:34]
If you cough up 10 or 12 to the dealer and you make 50 on the next trade, you'll have a net positive 35, 40 pip day.

[00:33:42]
The difference between an amateur and a professional.

[00:33:44]
Don't sit there on your hands and let the market prove you wrong.

[00:33:47]
Look for good solid entries. If the dealer strikes the high again or strikes the low again while you're sitting there, scratch it out.

[00:33:53]
If he closes above that level, we'll talk about it more.

[00:33:58]
Today.

[00:34:01]
One other deal is trap set, week beginning, week ending, session, beginning of the session, end of the session, end of the day, end of the week.

[00:34:12]
That's stuff. That's what you should have put.

[00:34:15]
False move, week beginning, sets the trap to get people to go short or long, pulls away, starts to rise, makes the midweek reversal when everybody jumps in that direction.

[00:34:26]
Then he reverses off of that number to catch everybody off guard and ends back in the middle of the range.

[00:34:32]
The exceptions to this.

[00:34:36]
When the dealer has to shift the zone, it is targets.

[00:34:40]
If you're on an ongoing basis, these things are seen over and over and over.

[00:34:49]
Once in a while, end of the quarter, couple times a year, the dealer has to shift the zone.

[00:34:56]
Then you'll be like, Steve, there's 35 levels up.

[00:35:00]
As long as he keeps giving you up signals, take them.

[00:35:09]
If you trade both ways without fear, stop thinking too much about it and go, this is absolutely going to correct, this is absolutely going to rise.

[00:35:16]
That's where you're getting jammed up.

[00:35:19]
The pattern, the pattern, the pattern.

[00:35:24]
If you think about this, and I've said it 100 times, and this will be 101 for you guys, kidding, but if the Asian range is 25 to 50 pips, and the dealer makes a 25 to 50 pips stop hunt,

[00:35:38]
that's 50 to 100 pips on the table.

[00:35:41]
If you're trying to carve out 50 of that, and you catch absolute zero, the bottom or the top, and the dealer comes back into the Asian levels, you'll hit your 50 pips.

[00:35:52]
You'll hit 40, your stop should be a break even, you should not get hurt.

[00:35:59]
I'm going to talk more about this today in a few minutes when we get to the lesson part.

[00:36:05]
All right.

[00:36:08]
How many days of data is needed to evaluate the market at any given time?

[00:36:12]
The answer is three to five.

[00:36:14]
Think about this for a minute.

[00:36:17]
I'm absolutely debunking all the crap about, oh, draw your support and resistance from 1905 and drag it into your current chart, and go back on the one hour, four hour, daily, weekly, a monthly, quarterly, semi-annually, ten years, and then you'll get to the end of the day.

[00:36:33]
You'll get to the end of the day, 10 years, 10 years, 10 years, and you'll get to the end of the day.

[00:36:40]
If you've done that shit in the past, you know it doesn't work.

[00:36:43]
You know it's a waste of your time.

[00:36:46]
My goal for all of you is to be able to look at the last three to five days on a chart and know which way the dealer is going to go.

[00:36:57]
Think about the freedom that gives you just from that idea, you don't have to draw support and resistance, you don't have to sit there in front of a million charts.

[00:37:02]
You walk up to the chart, you open the screen, three to five days you go, man, dealer made a peak formation high, he dropped, dropped, dropped, dropped.

[00:37:12]
It looks like he's bottoming out, turn sideways, the price action is flat, I expect stop-hunt low rise.

[00:37:21]
Okay, someone asked me to repeat what time does the red box paint, 8 to 11, 8 to 12 depending on how you want to set it up.

[00:37:29]
The purpose of that is to capture the last hour of the London session going into the U.S., the gap time, and to about 11 or 12 noon, because that's when these guys go to lunch on Wall Street and they eat spaghetti and pasta and come back and they don't do anything.

[00:37:46]
I don't know what it is, there's an Italian restaurant right outside of Wall Street, I can't think of the name of it.

[00:37:51]
It's got flags outside, it's like some high-end restaurant over there, and all those assholes, I mean, I'm sorry, all those guys go over there and sit and eat, and I think when they come back they don't work the desk anymore, I think the food's too heavy.

[00:38:05]
Anyway, if you've ever been there and you know what I'm talking about and you've seen those guys, you know exactly what I'm talking about.

[00:38:12]
Okay, they're really full of themselves over there.

[00:38:18]
Yep, Rusty, Rusty said fat bastards from the movie.

[00:38:23]
All right, hey, I got a cool email from, I can't remember who, I probably shouldn't say his name, but he told me he went back and watched the point break clip or movie and he said he actually went to the beach in Australia where Bodie was waiting for the 50-year storm,

[00:38:38]
and then he went off on a rant about how he was hooking up with some chick and banger roommate and I was like, oh my goodness.

[00:38:45]
So anyway, it was a good story, thank you, I enjoyed it, and I'm not going to say your name, you're probably married now and I don't know if your wife knows that story.

[00:38:54]
Okay, I love the emails.

[00:38:58]
Pictures, not only pictures of that man.

[00:39:01]
All right, list the rules for the safety trade setup.

[00:39:08]
Okay, you're looking at your chart.

[00:39:11]
The peak formation is clearly identified.

[00:39:14]
You see it?

[00:39:15]
High of the week or low of the week, it's clear, I got the peak.

[00:39:20]
Level one consolidation is identified.

[00:39:22]
The dealer shifted off of that level and went into consolidation to end the day.

[00:39:28]
The dealer is trading 25 to 75 pits off of the previous high or low, away from the peak.

[00:39:36]
The dealer issues a visible stop hunt in the form of an M or W, above or below the Asian level, second leg.

[00:39:47]
Okay, that's the answer.

[00:39:50]
What's the rule?

[00:39:51]
Peak formation identified, level one consolidation on the chart.

[00:39:54]
Dealer comes out of that area and makes a visible stop hunt on the chart.

[00:40:00]
What's the difference between a safety trade and a straightaway trade?

[00:40:03]
The answer is there is no visible stop hunt issued by the dealer on a straightaway and there is on a safety.

[00:40:13]
Price appears as if it's a straight rise out of the area.

[00:40:18]
Okay, that's the difference.

[00:40:24]
All right, label the chart.

[00:40:27]
Basically, this is what I'm looking for.

[00:40:29]
You got, look, you walk up to a chart, three to five days of data, level three on the left-hand side.

[00:40:34]
Somebody asked me this and I got to say it.

[00:40:37]
You answered your own question.

[00:40:39]
The double black tracer is Sunday Monday.

[00:40:43]
Some dealers do not have a double black tracer.

[00:40:50]
Okay.

[00:40:51]
Some dealers don't have the double black tracer for Sunday.

[00:40:56]
Okay, so look, this is what you should have had.

[00:41:00]
You got your consolidation.

[00:41:01]
Dealer makes the vectors three to the low, pulls back, hits it again, actually hit it three times.

[00:41:06]
There it is.

[00:41:07]
The next night, W formation stop hunt.

[00:41:09]
And all of a sudden, he switches directions, traps to the high side.

[00:41:12]
Remember my little song?

[00:41:13]
Welcome to the candy shop.

[00:41:14]
I'm traded to the hit the stops.

[00:41:16]
Ooh, there they go.

[00:41:17]
All right.

[00:41:18]
And they drop three levels.

[00:41:20]
They're stop hunt high drop.

[00:41:21]
This is, look, straight away.

[00:41:23]
He hits the stops here, drops straight away.

[00:41:27]
Why?

[00:41:28]
Because he doesn't go above the box, but there it is.

[00:41:30]
Pins to the 50 drops.

[00:41:32]
Then he reverses directions again.

[00:41:34]
Same exact thing.

[00:41:35]
Dealer took it all back.

[00:41:37]
Notice how he stays off of or worked this blue tracer in here where their volume was trapped, but did not release here.

[00:41:45]
These are the things you need to be seeing.

[00:41:48]
Okay.

[00:41:49]
I guess I could grab a pen that would be helpful.

[00:41:52]
Let me go over here.

[00:41:54]
Actually, I got something pretty cool.

[00:41:56]
My good friend Francisco sent me a screen marker for my birthday.

[00:42:03]
Hold on.

[00:42:04]
Let me find it.

[00:42:06]
It's in the tray.

[00:42:11]
It was in the tray, where is it?

[00:42:18]
I think when I rebooted, I lost it.

[00:42:23]
All right.

[00:42:24]
We're at a look.

[00:42:25]
I'll use the regular pen.

[00:42:31]
Okay.

[00:42:32]
Look, you walk up to the chart.

[00:42:34]
You see head and shoulders right there.

[00:42:36]
That means you're in level three.

[00:42:37]
This is level three.

[00:42:38]
You know you got it.

[00:42:39]
Okay.

[00:42:40]
The next move you expect, this is the LOW, low of the week.

[00:42:44]
Dealer starts working it.

[00:42:47]
This is interesting right here because this is the low of last week.

[00:42:52]
This is the low of this week.

[00:42:54]
Notice how it ties into the cycle.

[00:42:57]
This is the answer.

[00:43:02]
Yeah, I don't know.

[00:43:03]
You're right Rusty.

[00:43:04]
Hold on.

[00:43:05]
You guys are all going to want a different color.

[00:43:07]
Let me save you the trouble.

[00:43:08]
I don't know why that brown came up.

[00:43:10]
It's disgusting.

[00:43:12]
I'll try white.

[00:43:17]
All right.

[00:43:18]
Let's see.

[00:43:19]
No.

[00:43:20]
Man.

[00:43:21]
It's really gross.

[00:43:22]
Choose pen color.

[00:43:25]
Can you see that?

[00:43:26]
You got to see that.

[00:43:27]
Okay.

[00:43:28]
All right.

[00:43:29]
So look.

[00:43:30]
You know you ask me sometimes, you go Steve, there's only two levels in a week.

[00:43:32]
Or only see one level.

[00:43:34]
This is the answer.

[00:43:36]
It's carryover from the previous cycle.

[00:43:39]
Okay.

[00:43:40]
It's carryover from part of the previous cycle.

[00:43:42]
Right.

[00:43:43]
This is the low of the week.

[00:43:45]
And I got jumbled.

[00:43:47]
Look.

[00:43:48]
This is the low of the week over here.

[00:43:50]
This is Thursday.

[00:43:52]
Friday.

[00:43:54]
Now we got Sunday Monday right here, right?

[00:43:59]
Okay.

[00:44:00]
Now what happens?

[00:44:01]
You have false move week beginning, which is in continuation with this show.

[00:44:05]
Over here, the cycle.

[00:44:07]
Okay.

[00:44:08]
And then the dealer only gives you one level of rise.

[00:44:11]
Gives you an aggressive move, which comes off of this.

[00:44:16]
So together, one, two, three days of rise.

[00:44:21]
Then the dealer starts doing his high side work.

[00:44:23]
Trapping, trapping, trapping.

[00:44:25]
Get everybody short.

[00:44:26]
Hit the stops.

[00:44:27]
Whoa.

[00:44:28]
And drops.

[00:44:29]
Okay.

[00:44:30]
I had to throw that in there when nobody's looking.

[00:44:31]
All right.

[00:44:32]
This is a straightaway.

[00:44:33]
Pins it a 50.

[00:44:34]
Why is that at a straightaway?

[00:44:36]
There is no visible stop hunt above the age and range.

[00:44:42]
Okay.

[00:44:43]
There's a stop hunt to the low side.

[00:44:45]
Look.

[00:44:46]
What is that for?

[00:44:47]
Breakout traders.

[00:44:49]
But you know better now.

[00:44:52]
You know the direction for the next couple of days.

[00:44:54]
One, two, two and a half, perhaps.

[00:45:00]
Okay.

[00:45:01]
This is two days of work.

[00:45:03]
You can go one, two, three.

[00:45:07]
The dealer makes his aggressive move and you're getting to the end of the week.

[00:45:11]
Remember I asked you when does the dealer make its trap moves?

[00:45:17]
End of the week.

[00:45:18]
If you know he makes his trap moves at the end of the week, don't be a sucker and go short on Friday afternoon at 12 o'clock.

[00:45:26]
If the price has been dropping, you're like, oh, look at that.

[00:45:29]
I know that sometimes it will continue to drop, but you know that the dealer has to set the trap to carry you into the week and gap you.

[00:45:38]
So all the suckers that come on and pile on short in there, look at all that work in there, how he's working it towards the end.

[00:45:43]
Right?

[00:45:44]
He's chopping it up.

[00:45:45]
He's grabbing everybody's short, hitting the stops in both directions.

[00:45:47]
And then right before the end of the day, he makes his pull off.

[00:45:50]
Let me clean this up.

[00:45:54]
He makes his pull off right here and those fat bastards go to lunch.

[00:45:58]
And then that's it.

[00:46:00]
You've got everybody trapped.

[00:46:01]
And they can go eat a big fat lasagna dinner, throw their keys to their Bentley's at the valet, walk around in their $5,000 Armanis.

[00:46:10]
Right?

[00:46:11]
That's what they do, man.

[00:46:12]
If you haven't seen it, you need to go to New York just for that.

[00:46:16]
All right?

[00:46:17]
That's what they do.

[00:46:18]
They line up their cars or lined up down the street for this place and they throw in the keys at the valet like who the hell they are.

[00:46:23]
And they're all getting out of there and it's like comical almost.

[00:46:27]
I know, man.

[00:46:28]
All right.

[00:46:29]
Good stuff.

[00:46:30]
Okay.

[00:46:31]
That's what your charge should look like if you didn't have it, I understand.

[00:46:38]
All right.

[00:46:39]
Walk me through the four hour.

[00:46:40]
Look, first eight hours.

[00:46:42]
Okay.

[00:46:43]
Asian range for the week.

[00:46:45]
Psychological support and resistance.

[00:46:48]
Do you feel it gets the false move breaks?

[00:46:50]
Right?

[00:46:51]
Breakout traders go short.

[00:46:52]
He pulls it back.

[00:46:53]
Runs it up.

[00:46:55]
Makes the M formation.

[00:46:57]
Drops down.

[00:46:58]
Punches through the psychological support and resistance.

[00:47:01]
The second time he doesn't go as far.

[00:47:05]
Then he ends the week back towards the high.

[00:47:09]
Slightly breaks it and pulls back and ends out.

[00:47:13]
Okay.

[00:47:14]
Understand?

[00:47:15]
That's roughly what you should be looking at.

[00:47:18]
If you got it, great.

[00:47:20]
If you didn't, go back and do some more four hour charts.

[00:47:22]
That's the point of the break this week.

[00:47:25]
Okay.

[00:47:26]
Good.

[00:47:27]
We're good.

[00:47:28]
All right.

[00:47:30]
What setup is this?

[00:47:32]
Straightaway.

[00:47:33]
Why?

[00:47:34]
No visible stop hunt.

[00:47:37]
Okay.

[00:47:38]
You walk up to the chart.

[00:47:39]
Where are you in the cycle?

[00:47:41]
Head and shoulders.

[00:47:42]
Bam.

[00:47:43]
I see it.

[00:47:44]
Clean.

[00:47:45]
Okay.

[00:47:46]
We are now looking for longs.

[00:47:47]
Okay.

[00:47:48]
Straightaway.

[00:47:50]
Do not short this.

[00:47:52]
Thinking that it's going to go this way.

[00:47:54]
You're trading back towards the peak.

[00:47:56]
What did I tell you about trading back towards the peak?

[00:47:58]
It's for suckers.

[00:47:59]
Okay.

[00:48:00]
What happens here?

[00:48:03]
The dealer pins the mayonnaise right out of the box.

[00:48:06]
Gives you a W or gives you a railroad track entry.

[00:48:09]
Either one's good.

[00:48:10]
Stop loss goes below the low.

[00:48:12]
And if you look at this.

[00:48:15]
If you look at that, there's a multi-session W spread out from early Asia to stop hunt zone in London, late Asia.

[00:48:24]
Okay.

[00:48:25]
Straightaway.

[00:48:26]
Why?

[00:48:27]
Straightaway.

[00:48:28]
Just a dealer didn't come in here.

[00:48:29]
If the dealer comes in here, this is a safety trade.

[00:48:33]
You can be long from the mayo right here.

[00:48:37]
At the railroad tracks to the mayonnaise, you can't get a lot of money.

[00:48:42]
Right here.

[00:48:43]
At the railroad tracks to the mayonnaise, long.

[00:48:45]
Okay.

[00:48:46]
This is a straightaway trade because there is no visible stop hunt above or below the Asian range.

[00:48:53]
I'm going to talk about this in a few minutes and if I don't remind me, I know why you guys are taking trades in the blue box now.

[00:49:00]
And it's my fault and I'm going to explain it tonight.

[00:49:04]
The white arrow was pointing in here.

[00:49:07]
Sorry if it wasn't clear the arrow.

[00:49:09]
I don't know.

[00:49:10]
Should I drew the arrow?

[00:49:13]
Some of you got it wrong because of technical error on my part.

[00:49:17]
Next time I do it, I'll draw the arrow like that.

[00:49:19]
I didn't want to totally give it away.

[00:49:21]
What trade is that?

[00:49:24]
All right.

[00:49:27]
Okay.

[00:49:28]
I'm busting chops.

[00:49:29]
I love you guys.

[00:49:30]
I hope you're getting a lot out of this stuff.

[00:49:32]
I really do.

[00:49:34]
Okay.

[00:49:35]
Next.

[00:49:36]
What is this trade and why?

[00:49:38]
This is a safety trade because the dealer issues a visible stop hunt in line with the peak.

[00:49:44]
Okay.

[00:49:45]
You walk up to a chart.

[00:49:47]
You go, hmm, what do I got here?

[00:49:50]
Peak formation high.

[00:49:52]
This is not the trade.

[00:49:54]
Right?

[00:49:55]
You're tempted to take this, but this is what the dealer gives you.

[00:50:01]
Okay.

[00:50:07]
That's right past the mayonnaise.

[00:50:08]
He fakes past the mayonnaise and comes back below the mayonnaise.

[00:50:12]
Then he makes a second push towards the mayonnaise, goes into consolidation.

[00:50:16]
You own him.

[00:50:17]
Then he shifts the zone for away from all the suckers.

[00:50:20]
Okay.

[00:50:21]
And then ends the day in the W formation back into consolidation.

[00:50:25]
The pattern, the pattern, the pattern.

[00:50:29]
Okay.

[00:50:30]
All right.

[00:50:33]
Next.

[00:50:35]
Okay.

[00:50:36]
TDI stuff.

[00:50:39]
The reason I put these up there is because I asked you to mark some of the signals.

[00:50:45]
Some of you got them, some of you didn't get them.

[00:50:48]
That's okay.

[00:50:50]
But this is what you should be looking for on the TDI.

[00:50:54]
If you're not, it's completely fine.

[00:50:56]
But take a picture of this.

[00:51:01]
Okay.

[00:51:02]
And then this is your model.

[00:51:04]
You should see the stuff crystal clear.

[00:51:06]
Let me walk you through what we got.

[00:51:08]
All right.

[00:51:09]
Grab the pen.

[00:51:12]
Okay.

[00:51:13]
Look.

[00:51:14]
Shark fin below the support.

[00:51:16]
37, right?

[00:51:18]
Shark fin low outside the band.

[00:51:20]
Okay.

[00:51:21]
Blood in the water.

[00:51:22]
Level one rise.

[00:51:24]
In consolidation, there's a mini pattern.

[00:51:26]
Stop hunt low.

[00:51:28]
Rise.

[00:51:29]
Cross the market baseline.

[00:51:31]
Separation between blood and RSI.

[00:51:34]
Consolidation.

[00:51:35]
And possible some divergence.

[00:51:37]
How this is running up.

[00:51:38]
And maybe there was a spike to the high and then the dealer comes all the way back.

[00:51:42]
This section of action is level one.

[00:51:47]
There's three swipes or three pushes of energy inside there.

[00:51:51]
But this is all level one.

[00:51:53]
Then what happens the next day?

[00:51:55]
The dealer comes back and he gives you a shark fin low right past the market baseline.

[00:52:02]
Remember I told you that the dealer will trade slightly below the market baseline in an uptrend.

[00:52:09]
And then rise.

[00:52:13]
Okay.

[00:52:16]
Then he hits it again.

[00:52:17]
How do you know that this is not, you can't take this M?

[00:52:22]
Because you're in an up cycle from the anchor.

[00:52:27]
Okay.

[00:52:28]
The next day you don't have a clean rise.

[00:52:30]
You have a lot of chop.

[00:52:31]
Maybe the dealer worked the crosses.

[00:52:33]
Maybe he didn't give you a nice run.

[00:52:34]
Maybe he went up, formed his level, and he only moved a little bit.

[00:52:38]
Now the dealer comes back.

[00:52:40]
What does he do?

[00:52:41]
The dealer comes back below the market baseline.

[00:52:48]
The crosses blood in the water and the market baseline at the same time.

[00:52:52]
That's a signal.

[00:52:53]
Remember the sign failed?

[00:52:54]
That's a trade.

[00:52:58]
You understand?

[00:52:59]
An extreme move.

[00:53:03]
An extreme move outside the band shark fin is your anchor point.

[00:53:07]
Let me clean this up.

[00:53:10]
A clean move outside the band is your anchor point.

[00:53:13]
You happen to have three bursts in there.

[00:53:15]
That's fine.

[00:53:16]
The next day the dealer shark fins below the market baseline and rises.

[00:53:23]
The next day the dealer goes below the market baseline and rises.

[00:53:28]
Now you're looking for a break outside the band.

[00:53:35]
This would be your exit all units when it crosses back inside.

[00:53:38]
If you were long from here, you picked up some nice run.

[00:53:44]
This is three days of rise.

[00:53:47]
This is three days broken up.

[00:53:49]
I drew the international date lines in there for you.

[00:53:52]
The date changeovers right here.

[00:53:55]
Look, here's what happened.

[00:53:59]
The dealer breaks outside and comes back in.

[00:54:01]
Now if you didn't take this signal as a reversal, that's fine.

[00:54:04]
If you took it and got stopped out, this is possible divergence right here.

[00:54:09]
Why?

[00:54:10]
Because you're out of the band and back in the band and there's blood in the water.

[00:54:15]
What probably happened with price action, just imagine in your head TDI is the same height or the RSI line is the same height.

[00:54:22]
You probably had this and probably had a spike to the high and it comes back in.

[00:54:29]
Understand, now you get blood in the water and then look what you got.

[00:54:33]
Cross on the market baseline.

[00:54:35]
You got one push, two breaks outside.

[00:54:37]
This is considered trend acceleration.

[00:54:40]
You're looking for the return back inside the band for the exit.

[00:54:45]
Okay, one, two, three.

[00:54:51]
This did not break out the level, but here's the weakness with Fennie indicator.

[00:54:58]
The indicator averages back in this example.

[00:55:01]
RSI is typically 14.

[00:55:02]
We have a set to 21.

[00:55:04]
It only looks back 21 periods.

[00:55:07]
So if it looks back, let's say you're on a one hour chart, it looks back 15 hours.

[00:55:12]
So it's taking this data into consideration and if price breaks below, it'll trade below.

[00:55:19]
How come this didn't rise very high?

[00:55:22]
There could be a level of rise in the price, but because it only looks back, it's limited and when it sees.

[00:55:28]
If you compare this whole structure to the low down here, then yes, it should plot higher, but it may not because it only looks back 21 hours.

[00:55:38]
If you're on a 15 minute chart, it's 21 15 minute periods.

[00:55:43]
Understand?

[00:55:45]
That's the limitation in any indicator is that it doesn't take into consideration anything more than what it's programmed to look back at.

[00:55:56]
Okay.

[00:55:58]
Ralph, if you don't like TDI, then use the RSI.

[00:56:01]
RSI is very cool.

[00:56:03]
In fact, I used the RSI for a long time.

[00:56:06]
I learned RSI and loved it and I thought that this was TDI was cleaner for good signals because there's a lot going on here.

[00:56:14]
Okay.

[00:56:16]
All right.

[00:56:18]
If you weren't marking it up like this,

[00:56:22]
you should be, okay, again, look, we're looking for it.

[00:56:25]
Add to the band, end the band.

[00:56:27]
Blood in the water.

[00:56:29]
Possible divergence here, right?

[00:56:31]
Because they make the stop hunt higher and TDI is already falling off based on the clothes.

[00:56:36]
You should be able to know just by looking at this with the candles look like in your head.

[00:56:40]
If you don't, then you need to take some snapshots.

[00:56:43]
I can tell you right now that TDI is lower than the previous swing high.

[00:56:48]
It probably spiked to the high, came back and ended on a hammer or some quasi-type or hammer.

[00:56:54]
Picture the candle what it would look like.

[00:56:56]
Then it crosses over, gives you blood in the water.

[00:56:59]
You got separation here, crosses the market baseline.

[00:57:02]
Acceleration, comes back in.

[00:57:06]
Out.

[00:57:07]
Okay.

[00:57:08]
Now, short here.

[00:57:09]
Why?

[00:57:10]
Prices went above the market baseline ever so slightly and turned over.

[00:57:14]
Do not trade this.

[00:57:17]
Why?

[00:57:18]
Doesn't come back to the market baseline.

[00:57:20]
It's nothing.

[00:57:21]
It means nothing.

[00:57:23]
Okay.

[00:57:25]
Market baseline break.

[00:57:28]
An M formation back to the market baseline cell.

[00:57:32]
Exit.

[00:57:33]
It didn't break outside the band but an exit.

[00:57:38]
Okay.

[00:57:39]
That's a three day cycle in there.

[00:57:40]
That's a cycle.

[00:57:41]
Now, the thing that's crazy is I'm going to tell you something pretty neat.

[00:57:45]
I saw someone ask what time frames are these.

[00:57:47]
Guess what?

[00:57:48]
I mixed them up.

[00:57:50]
The first one's a 15 minute.

[00:57:53]
The second one's a four hour and the third one's a one hour.

[00:57:58]
It's the same shit.

[00:58:00]
I wanted to trick you to see.

[00:58:02]
If you understand the indicator, it's all the same.

[00:58:08]
The patterns are in the indicator exactly the way I've illustrated for you.

[00:58:14]
If you understand how to use the indicator better than anybody else or better than any other

[00:58:21]
component, then you're going to trade better than anybody else.

[00:58:25]
People don't take the time to do this.

[00:58:27]
This drill is invaluable.

[00:58:29]
The signals are the same.

[00:58:34]
Okay.

[00:58:39]
Gloria, that's a matter of choice.

[00:58:40]
She said it looks clear on the one hour.

[00:58:42]
Some people like the four hour.

[00:58:44]
Some people like the 15 minute.

[00:58:46]
But I wanted you to see that.

[00:58:47]
I took the three charts or four charts that we look at and three charts.

[00:58:53]
15 minute, one hour, four hour.

[00:58:54]
Look what you got.

[00:58:55]
Same shit.

[00:58:56]
Different day.

[00:58:59]
Okay.

[00:59:01]
Last one.

[00:59:04]
Look at it.

[00:59:06]
Okay.

[00:59:07]
Dealer makes the shark fin out.

[00:59:08]
He rises off there.

[00:59:09]
Comes back.

[00:59:11]
Tangles with blood a little bit.

[00:59:15]
If you took this here, that's fine.

[00:59:17]
Your stop loss is out here.

[00:59:18]
You're good.

[00:59:19]
Stop loss goes below the day.

[00:59:22]
Everybody knows that.

[00:59:23]
Okay.

[00:59:24]
There's another good entry, but I want you to notice what's going on here.

[00:59:28]
Okay.

[00:59:29]
This is in fact a second leg.

[00:59:32]
This is the better entry.

[00:59:34]
That's a second leg trade.

[00:59:36]
That in essence is a W and it could be divergent.

[00:59:40]
Get sure the candles in your head.

[00:59:41]
What do the candles look like?

[00:59:43]
Possibly the second leg issued out as a hammer.

[00:59:46]
Like that.

[00:59:47]
Right?

[00:59:48]
Right in here.

[00:59:49]
This is probably what was formed.

[00:59:51]
The dealer might have spiked to the low on an outside structure like that.

[00:59:54]
Picture that.

[00:59:55]
Look how big this move is.

[00:59:56]
An aggressive move.

[00:59:57]
Vector candles to the low.

[00:59:59]
The dealer consolidated in here.

[01:00:01]
Came back towards the low.

[01:00:02]
Spiked it.

[01:00:03]
Ended on a hammer.

[01:00:04]
And then this is what you ended up with.

[01:00:07]
Okay.

[01:00:08]
Picture the candles in your mind what you're looking at.

[01:00:11]
Part of being visual.

[01:00:13]
Part of pattern recognition.

[01:00:15]
If you can see the TDI and visualize the candles, then you don't need candles.

[01:00:20]
Okay.

[01:00:23]
That's what the one hand tied behind the back is.

[01:00:26]
Okay.

[01:00:30]
Jerry's nothing wrong with that buddy.

[01:00:32]
There's your one, two, three.

[01:00:34]
Exit.

[01:00:35]
Stop, hunt low.

[01:00:37]
Second leg.

[01:00:38]
Rise.

[01:00:39]
Crosses the market baseline.

[01:00:40]
Gives you one push.

[01:00:42]
Two pushes.

[01:00:44]
Three pushes.

[01:00:45]
And he ends to the outside.

[01:00:47]
Barely goes outside the band.

[01:00:49]
Exit there.

[01:00:50]
Back below the market baseline.

[01:00:53]
Long.

[01:00:54]
Three pushes within three pushes.

[01:01:00]
Right?

[01:01:01]
How many times I got to tell you that?

[01:01:02]
The number three is there for a reason because we're stubborn.

[01:01:05]
I've said it a hundred times.

[01:01:06]
Three pushes inside of three pushes.

[01:01:09]
And then the last leg in here.

[01:01:14]
Check this out how this ends.

[01:01:16]
This is like my favorite one.

[01:01:18]
This goes next to the Mona Lisa of this would be the rim rant of TDI.

[01:01:22]
Rim rant.

[01:01:23]
If I said it right.

[01:01:24]
Okay.

[01:01:25]
Look.

[01:01:26]
One, two, three.

[01:01:27]
That's a 33 trade, right?

[01:01:29]
Why?

[01:01:30]
There's three pushes on the third day of rise.

[01:01:35]
Okay.

[01:01:36]
So issues are 33.

[01:01:38]
One, two, three.

[01:01:40]
The dealer exits here.

[01:01:41]
Slightly outside the band comes back in.

[01:01:43]
Chops on both sides.

[01:01:45]
Hit the stops.

[01:01:46]
Hit the stops.

[01:01:47]
End the week in consolidation.

[01:01:48]
Or end the cycling consolidation.

[01:01:51]
Yes, Keith.

[01:01:52]
It is possible to trade just on TDI.

[01:01:55]
Once you learn how to use it.

[01:01:57]
If you didn't do the drill and you're looking at this now, go in holy shit.

[01:02:01]
Look at that.

[01:02:02]
Do it for me next week, man.

[01:02:03]
I'm taking a break.

[01:02:04]
I'm doing the meetup.

[01:02:05]
You have two weeks to get caught up, man.

[01:02:07]
Post your stuff in the forum.

[01:02:09]
If you've just been going, ah, guys, crazy, I ain't doing this shit.

[01:02:12]
Come on.

[01:02:13]
Stop saying that.

[01:02:14]
I'm not crazy.

[01:02:16]
Okay.

[01:02:17]
What I want you to do is go back and do these drills.

[01:02:24]
Understand that there's three pushes inside of here.

[01:02:28]
Almost every day.

[01:02:29]
This is pretty cool.

[01:02:32]
Okay.

[01:02:34]
This is how you should have marked it.

[01:02:36]
If you didn't mark your charts like this, I cleaned it off.

[01:02:40]
Let me move my pen.

[01:02:41]
Take a picture of it right now.

[01:02:43]
Okay.

[01:02:45]
Take a snapshot.

[01:02:48]
In fact, let me go back on the three of these and let you take three pictures.

[01:02:52]
Is that all right?

[01:02:53]
I'm going to go back.

[01:02:54]
Give me a chance to take a picture of it.

[01:02:55]
Print these out, man.

[01:02:56]
And this is what you should be looking for.

[01:02:57]
Train your eyes, all right.

[01:02:59]
Let me back up.

[01:03:00]
I don't know if you guys, I know you guys take pictures of my slides anyway.

[01:03:03]
But anyway, look, for real.

[01:03:05]
All right.

[01:03:06]
Take a picture of that.

[01:03:07]
Pull out your snag it.

[01:03:08]
Take a picture of that.

[01:03:09]
And let me know when you're done.

[01:03:10]
Just put a D up if you want to take a picture of that.

[01:03:13]
It shouldn't take that long.

[01:03:16]
Thirty seconds.

[01:03:18]
All right.

[01:03:19]
Take a picture of that.

[01:03:21]
All right.

[01:03:22]
Next one.

[01:03:23]
Okay.

[01:03:24]
Okay.

[01:03:25]
Cool.

[01:03:26]
All right.

[01:03:27]
Do this one.

[01:03:28]
Take a snag into that.

[01:03:30]
Since you have the software up, then you should be able to just hit the hot key and do it.

[01:03:35]
Okay.

[01:03:36]
You got that one?

[01:03:38]
Okay.

[01:03:39]
Do it again.

[01:03:41]
Grab that one.

[01:03:46]
All right.

[01:03:48]
This one is like, this is beautiful to me.

[01:03:50]
There's like three moves within three moves.

[01:03:53]
Okay.

[01:03:54]
Everybody have that?

[01:03:55]
Cool.

[01:03:56]
All right.

[01:03:58]
That's it.

[01:04:03]
The last one was one hour.

[01:04:05]
I'm not sure if it was E.J.

[01:04:06]
Joe.

[01:04:07]
I forgot.

[01:04:08]
I was looking at so many of them.

[01:04:10]
They were 15 minutes, four hours, and one hour.

[01:04:13]
And you can't, can anybody tell the difference?

[01:04:16]
Honestly, you can't.

[01:04:18]
When you blow it up and just look at it, you can't see the difference.

[01:04:24]
But understand that once you know how to read the indicator, this is the point.

[01:04:28]
Once you know how to read the indicator, it doesn't matter the time frame.

[01:04:33]
It's the same shit.

[01:04:35]
The dealer only has a handful of moves.

[01:04:38]
Now, I don't want you to go, oh, well, since there's no difference, I'm going to start

[01:04:42]
trading in one minute.

[01:04:43]
It's not what I'm telling you.

[01:04:44]
What I'm telling you is learn how to use the indicator above and below the market.

[01:04:51]
And then you can find the break of the bands and the things that are essential.

[01:04:58]
Things that are essential for you to see within the indicator in any time frame.

[01:05:02]
Okay, one more time.

[01:05:03]
You froze up.

[01:05:04]
All right.

[01:05:05]
Chris, how about instead of doing it, how about we're times really tight tonight?

[01:05:09]
How about you go and do it on the recordings, buddy?

[01:05:12]
Mark the time right now.

[01:05:13]
It's 8.10.

[01:05:14]
8.13, actually.

[01:05:16]
All right.

[01:05:18]
Okay, I hope you come, man.

[01:05:21]
I'm excited, buddy.
