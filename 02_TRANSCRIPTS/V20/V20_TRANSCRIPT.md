# V20 — TRANSCRIPT

**Lesson:** `Bootcamp1 Wk9 052012 Part2 (46mins) (1).swf` — Week 9, Part 2, 2012-05-20
**Source `.swf` SHA-256:** `96eba8c82366de12b928c900397b58104dc8ae445d4ca5851b16ad5d522a43c6`
— **re-computed by this session and matching `SOURCE_MANIFEST.md` exactly**; 17,724,102 bytes.

---

## §1 — PROVENANCE OF THIS FILE

The body below is the **pre-ingestion supplied transcript**, copied verbatim from
`01_SOURCE_VIDEOS/Forex Bootcamp/Bootcamp/Bootcamp Notes/20_Bootcamp1_Wk9_052012_Part2_46mins/TRANSCRIPT.md`.

| Object | SHA-256 |
|---|---|
| supplied file, whole | `d2d1b673eb566581b19d785ebc62c4f32c65e2d813f18d59d373124a7a8ea88c` |
| its body, after the `# VERBATIM TRANSCRIPT` line | `316b474a103ad77d41c9e48a6e2b8b54b22c1ba684bfd5778df3fb4dda793143` |

⚠️⚠️ **THE SUPPLIED FILE'S HEADER IS OF THE FABRICATED CLASS AND IS NOT REPRODUCED ABOVE THE BODY.**
It carries *"Course Position: **Video 21 of 21**"* and a *"Primary Topics"* line — **the two fields
`Q-015` §5 quarantines by name.** ⭐ **And the position is WRONG in the direction `Q-019` and
`Q-020` already established: lesson 20's folder counts one ahead**, exactly as lesson 19's folder
carried `V20-` identifiers. **The header is recorded here as evidence about the fabricated layer and
is used for nothing else.** The body is a separate question and is verified in §2.

---

## §2 — VERIFICATION OF THE BODY (`I-008`)

| Check | Result |
|---|---|
| Markers | **957**, strictly monotonic |
| Backward steps | ⭐ **ZERO** |
| Equal-adjacent (duplicate) markers | ⭐ **ZERO** — cleaner than V19, which had one |
| Gaps between markers | min **1 s**, max **12 s**, mean **2.87 s** |
| First / last marker | `[00:00:00]` / `[00:45:45]` |
| Measured audio length | **2749.100 s = 00:45:49.1**, extracted independently by this session |
| Tail gap | **4.1 s** between the last marker and the end of audio |
| Header-implied length | `frameCount 8248 ÷ frameRate 3.0` = **2749.333 s** |
| `SOURCE_MANIFEST.md` | **00:45:49** |
| Words / speech rate | 7,299 / **159.5 wpm** |

⭐ **FOUR INDEPENDENT MEASURES OF LENGTH AGREE**: the SWF header (2749.333 s), the extracted audio
(2749.100 s), the manifest (2749 s) and the filename (*"46mins"*). **Spread: 0.33 s.**

⭐ **IT PRESERVES ITS OWN MISHEARINGS, WHICH A FABRICATED FILE DOES NOT INVENT** — *"half a bad
man"*, *"the manays"*, *"Lung and session"*, *"pins to the blueberry"*, *"at the blueberry"*,
*"Where are your tracks"* / *"Where will tracks"* / *"we're attracts"* / *"roo-tracts"* for
`railroad tracks`, *"25 to 50-50 candle"*, ⭐ *"t-handle"* / *"handle"* for `candle` (§2a), *"$1,000-pift"* / *"1,000-pifts"* for `1,000-pip`,
*"pits"* / *"picks"* / *"pitch"* for `pips`, *"shift his own"* for `shift his zone`, *"denim,
denim, denim"*, *"the AV equals"* for `the AB=CD`, *"L3"* / *"level three"*, *"GVPCHF"* /
*"GPCHF"* / *"pound swissy"* for `GBPCHF`, *"YW"* / *"Y W"*, *"stop on"* for `stop hunt`,
*"a rail system that nice pretty cars right on"*. **55 lines carry filler or floor crosstalk.**

⚠️ **THE MOST FREQUENT SYSTEMATIC DEFECT, AND IT IS THE SAME FAMILY AS V19's:** `shift his zone`
is rendered **`shift his own`** throughout (`[00:25:55]`, `[00:27:04]`, `[00:28:36]`, `[00:30:40]`,
`[00:24:55]`). **The phrase is load-bearing — it appears inside the railroad-track DEFINITION** —
and every V20 artifact quotes it with the correction marked `[zone]`. ⭐ **Unlike V19, this file
CAN render the letter `M`**: *"M or W"* appears at `[00:00:10]`, `[00:00:28]`, `[00:26:24]`,
and *"draws an M"* at `[00:33:57]`.

---

## §2a — ⚠️⚠️ ASR CORRECTIONS — ADDED 2026-08-15, V20 R1 `M2` (`REVIEW_INDEX.md` item **333**)

**The original filing of this artifact ran NO independent ASR pass** (item 326). **V20 R1 ran one
and it found a `MAJOR`.** The corrections are recorded here; ⛔ **the body in §3 is NOT edited.**

### ⭐⭐ CORRECTION #1 — `candle` IS MIS-HEARD AS `handle` AT EVERY NOUN POSITION

| Marker | Committed grid (§3, unedited) | ⭐ **Correct word** |
|---|---|---|
| `[00:22:41]` | *"on this **t-handle**"* | *"on this **candle**"* |
| `[00:28:36]` | *"shift his own in the next **handle**"* | *"shift his [zone] in the next **candle**"* |
| ⭐ `[00:29:16]` | *"distance of this **handle** divided by three"* | *"Take the distance of this **candle** divided by three"* |
| ⭐ `[00:29:25]` | *"one third off the high of this **handle**"* | *"take your entry one-third off the high of this **candle**"* |
| ⭐ `[00:29:43]` | *"Take the length of the **handle**"* | *"Take the length of the **candle**"* |
| ⭐ `[00:29:50]` | *"So **track** 33 pitch off the high"* | *"**Subtract** 33 pips off the high, a third"* |

⚠️ **The two genuine VERB uses are rendered correctly and are unaffected** — `[00:14:27]` *"handled
them"* and `[00:40:01]` *"this bullet handles this"*.

**VERIFICATION — FIVE INDEPENDENT DECODES, NONE RETURNING `handle`:**

* **V20 R1's four:** `faster-whisper large-v3` at `float32` and `medium.en` at `int8`, each under
  **both** `vad_filter` settings, `beam_size = 10`, temperature 0.
* ⭐ **This session's fifth, run before accepting the finding:** `openai-whisper medium.en`,
  `beam_size = 5`, temperature 0, over `00:29:05`–`00:30:10`, `00:28:20`–`00:28:40` and
  `00:22:35`–`00:22:50`. **All positions return `candle`.**

⭐⭐ **CONSEQUENCE — THE RULE IS COMPLETE.** With `candle`, `[00:29:16]`–`[00:29:53]` reads:

> *"Take the distance of this **candle**. Divide it by three […] take your entry **one-third off the
> high of this candle** […] Take the length of the **candle**, let's say it's **100 pips** […]
> **Subtract 33 pips off the high**, a third, and put an entry right here."*

**`entry = high − (candle range ÷ 3)`. Arithmetic on one bar, with a worked example.**
⛔ **`A-136` was opened on the premise that *"handle"* was an undefined term. There is no such word,
and the record is CLOSED as an ASR artifact.**

### CORRECTION #2 — `[00:29:47]`

Committed *"because I'm happy to guard it"* → independent *"because I'm half regarded"*. **Not
load-bearing; recorded for completeness.**

---

## §3 — BODY, VERBATIM AND UNEDITED

**Nothing below is corrected.** Every mishearing is retained. Corrections live in the artifacts
that quote a line, never here.


[00:00:00]
All trap moves. All trap moves will come in as an outside structure.

[00:00:10]
Okay? The outside structure is the vector side of the M or W formation.

[00:00:18]
But it's very telling. All right? Definition.

[00:00:24]
The vector portion of a half of Batman.

[00:00:28]
The vector portion of M or W formation.

[00:00:32]
I'm going to wear that line. Use to set the high or low of the day.

[00:00:38]
As a single leg only. The outside structure is a single leg.

[00:00:44]
It's also used to form.

[00:00:48]
The high and the weak in the low of the week.

[00:00:51]
The aggressive move that traps the traders at the absolute worst spot.

[00:00:57]
The hell is that? Whereas the stop on will come at a higher.

[00:01:05]
Low or lower level.

[00:01:08]
Okay? Here's what I mean.

[00:01:11]
Outside structure high. The deal will work it like this.

[00:01:17]
For a couple of days. And then correct.

[00:01:20]
I'll show you some examples.

[00:01:22]
Okay? He comes back in like that. I don't know if that'll happen.

[00:01:24]
The market crashed. All right.

[00:01:26]
Look. Outside structure to the low.

[00:01:29]
They'll work it. You make another stop on.

[00:01:34]
And then rise.

[00:01:36]
But his outside structure forms out the lowest or highest point on the chart.

[00:01:41]
This is an absolute sign of reversal.

[00:01:45]
An absolute sign of reversal.

[00:01:49]
Okay? Here's a picture.

[00:01:53]
Big monster railroad tracks forms an outside structure.

[00:01:59]
All right. Analyzing the chart immediately.

[00:02:01]
What he got down and dirty.

[00:02:03]
Moving averages are separated. Price has been dropping.

[00:02:05]
I don't know the position of the manays.

[00:02:07]
But I can tell you that.

[00:02:09]
You got good angle and separation on the averages.

[00:02:12]
You're coming to the end of the run.

[00:02:14]
The other spikes aggressively.

[00:02:17]
Pulls back quickly. Goes into half a bad man move.

[00:02:20]
Then and then and then and then and then and then.

[00:02:23]
What's his moves now from here?

[00:02:25]
One or two things.

[00:02:26]
Straight rise. Get the stops rise.

[00:02:29]
Straight rise. Get the stops rise.

[00:02:31]
The only options the deal has.

[00:02:32]
Be hit the stops for you.

[00:02:34]
You own them.

[00:02:35]
Be hit the stops above the low of the vector of the outside structure.

[00:02:40]
Be hit the stops above the low of the outside structure.

[00:02:43]
You don't.

[00:02:46]
Okay.

[00:02:48]
Outside structure to the low.

[00:02:51]
Coming in.

[00:02:53]
Your vectors with.

[00:02:55]
Is last aggressive push to the low.

[00:02:59]
Remember that sets up to three thirty three.

[00:03:02]
The last push to the low is in three bursts.

[00:03:06]
And then and then and then and then and then and then.

[00:03:09]
That then and then.

[00:03:11]
Okay.

[00:03:12]
Same thing to the high.

[00:03:14]
Set the high aggressive fashion.

[00:03:17]
Traits off of that number.

[00:03:20]
Okay.

[00:03:21]
Looks like half a bad man.

[00:03:22]
But I want you to understand.

[00:03:23]
Hold on in the circle.

[00:03:25]
Hold on.

[00:03:26]
Okay.

[00:03:33]
But I want you to understand that this is in essence a half a bad man is the first part of the batman.

[00:03:41]
But it's part of a bigger scheme.

[00:03:44]
And we're going to show you now what I need.

[00:03:46]
Okay.

[00:03:47]
This aggressive move that forms out.

[00:03:50]
Okay.

[00:03:51]
So if you're going to form out.

[00:03:53]
The high of the year.

[00:03:55]
The low of the year.

[00:03:57]
The high of the quarter.

[00:03:59]
The low of the quarter.

[00:04:01]
The high of the week.

[00:04:02]
The high of the month.

[00:04:03]
The low of the month.

[00:04:04]
The low of the week.

[00:04:09]
It's part of.

[00:04:11]
The bigger structure.

[00:04:13]
To help you understand it could also be the people.

[00:04:16]
don't have those periods as well.

[00:04:18]
But this is the move.

[00:04:21]
All right.

[00:04:22]
Here it is as part of a bigger structure.

[00:04:24]
So let's look at it and break it down.

[00:04:26]
This is a classic outside structure.

[00:04:29]
If there was such a thing in the classic.

[00:04:31]
If this terminology existed anywhere.

[00:04:33]
This is the classic one.

[00:04:35]
Okay.

[00:04:36]
Here's what you got.

[00:04:39]
The highs established in here.

[00:04:43]
Right?

[00:04:44]
That's your typical railroad tracks to the high.

[00:04:47]
The dealer pulls back.

[00:04:49]
He goes back towards that number and does not take it out.

[00:04:53]
By the way, this occurred in GPCHF, and this was an easy trade to grab, man.

[00:05:00]
Right?

[00:05:03]
He railroad tracks to the high, he sets the high at late U.S. session.

[00:05:08]
Going in, coming down to the shadow, right?

[00:05:10]
Ten, eleven, twelve o'clock in the morning.

[00:05:15]
He comes back towards that level and fails to break it once, twice.

[00:05:21]
He ain't coming back, baby.

[00:05:25]
Lung and session.

[00:05:35]
This is one of those trades that you have to understand the bigger picture to the

[00:05:40]
left.

[00:05:43]
This is why, I don't, right?

[00:05:45]
You go, oh, let's see if I took this W over here and I got stopped out with the hell's

[00:05:48]
wrong with your system, you stink.

[00:05:51]
Right?

[00:05:52]
And the whole time, this monster pattern is staring at you.

[00:05:58]
You're closer to me out and find different languages around the world.

[00:06:03]
And the whole time, this big monster outside structure staring at you.

[00:06:09]
Okay?

[00:06:10]
Let me erase it.

[00:06:11]
Let's go over this stuff.

[00:06:12]
Someone said to pen, follow sucks.

[00:06:13]
They never make you guys happy, man.

[00:06:15]
I love it.

[00:06:16]
Come on, it's my birthday, man.

[00:06:17]
Give me a break.

[00:06:19]
Okay.

[00:06:20]
You erase all this stuff.

[00:06:22]
All right, let's look at it again.

[00:06:24]
Okay.

[00:06:25]
The dealer and aggressive move, let's look at the things that are telling you on this chart

[00:06:29]
to know where you are in the cycle.

[00:06:32]
Holy crap, there's a mile and a half between the averages.

[00:06:35]
All right?

[00:06:36]
What kind of behavior is this?

[00:06:39]
Anybody?

[00:06:41]
Yeah, baby, you learn it.

[00:06:43]
L3.

[00:06:44]
All right.

[00:06:45]
Why is that level three behavior?

[00:06:46]
The dealer is shopping back and forth with no clear direction after a big rise, level

[00:06:53]
three behavior to track the traders to keep a lure back into the fray.

[00:06:59]
Okay?

[00:07:00]
To get all the guides that are thinking, oh, this is a monster up front street.

[00:07:06]
I must fake the measurement from here to here.

[00:07:08]
And I must extend it on to the measurement here.

[00:07:11]
And then I will see you in Hawaii.

[00:07:13]
All right, isn't that what they say?

[00:07:21]
Understand what's going on here.

[00:07:23]
The outside structure after a big rise, separation between the moving

[00:07:27]
averages, the dealer comes in here.

[00:07:30]
The dealer comes in here and he hits it, opens the spread just enough to grab him,

[00:07:36]
right?

[00:07:37]
He comes back away, hits it again, just enough to work the tracer.

[00:07:44]
The averages are starting to fly it now.

[00:07:51]
The monster makes an end.

[00:07:56]
The monster hits it in one bar.

[00:07:59]
The monster hits it in one bar.

[00:08:02]
What do I mean?

[00:08:04]
Look at that right there.

[00:08:07]
That is a stop killer.

[00:08:10]
That's a breakout trader, stop lost killer.

[00:08:13]
Sorry about your luck killer.

[00:08:18]
Okay?

[00:08:23]
You should be sure on that.

[00:08:26]
You could have got short on the railroad tracks here knowing that this is the bigger move.

[00:08:32]
You could add a really tight stop loss in here or here.

[00:08:37]
Look at the monster, man.

[00:08:41]
The monster is beautiful.

[00:08:43]
Yeah?

[00:08:44]
This is the classic, I think it's Phil Williams.

[00:08:48]
Somebody Phil.

[00:08:49]
This is the Gator, man, right?

[00:08:51]
Have you ever seen that?

[00:08:52]
The Gator's nose right here, there's the circles.

[00:08:54]
Those of you that like University of Florida, this is a Gator pattern.

[00:08:58]
There's this mouth, this teeth.

[00:09:01]
You guys see it?

[00:09:04]
There's this eyeball.

[00:09:05]
There's the bottom of his jaw.

[00:09:10]
Have you never seen that before?

[00:09:12]
That's Phil Williams, that's Gator.

[00:09:14]
Gator's mouth is opening.

[00:09:17]
Okay?

[00:09:18]
Go Gator's.

[00:09:19]
Understand, I'm losing it in here, right?

[00:09:21]
Understand that.

[00:09:22]
If you see this, this is, forget about all the alligator stuff.

[00:09:26]
I'm screaming around.

[00:09:27]
But look, this is what you've got to concern yourself with.

[00:09:32]
Man, there's a big outside structure to the high, and then prices shopping around,

[00:09:36]
but it ain't going anywhere.

[00:09:37]
Price hasn't moved.

[00:09:39]
It's shopping around.

[00:09:40]
The high has not been reached.

[00:09:42]
The high has not been breached.

[00:09:44]
What does that tell you?

[00:09:46]
If the deal, if he's coming back and not taken out the high,

[00:09:49]
he's got the trap volume.

[00:09:51]
He's working it, baby.

[00:09:57]
Okay?

[00:09:58]
This is one of those instances you could take in the aging session.

[00:10:01]
If you happen to be up.

[00:10:03]
If he makes your third hit, he doesn't take out this classic outside structure after you got separation.

[00:10:09]
Take it, Ninja.

[00:10:10]
It's okay.

[00:10:11]
The only thing that I want you to be aware of is that this bar right here can come back and get you.

[00:10:20]
That's just got to worry about it.

[00:10:22]
Remember, welcome to the change of stuff.

[00:10:24]
Don't forget to hit the stuff.

[00:10:26]
Whoo!

[00:10:27]
Right.

[00:10:28]
Remember that.

[00:10:29]
If you get taken out, don't be afraid to get back in because if he does it,

[00:10:38]
what else to happen here, right?

[00:10:40]
The same rules apply that I'm talking to you about.

[00:10:43]
The dealer comes up here like this.

[00:10:46]
It comes right back below.

[00:10:49]
The previous high in how long?

[00:10:52]
Coke.

[00:10:54]
Long enough to drink a classic Coke.

[00:10:56]
They're in the next.

[00:10:59]
You're still good, man.

[00:11:01]
Trade still good.

[00:11:03]
Okay?

[00:11:04]
All right.

[00:11:05]
It's a more stuff.

[00:11:06]
I hope you guys are starting to see this stuff, man.

[00:11:08]
I'm excited.

[00:11:09]
It's good stuff.

[00:11:10]
It's your day outside to the low.

[00:11:12]
It's your day outside structure to the low.

[00:11:15]
A big monster structure to the outside forms.

[00:11:21]
This could also form.

[00:11:24]
I'm sorry.

[00:11:26]
That doesn't come out.

[00:11:27]
It's the low.

[00:11:28]
Low to the week.

[00:11:31]
Don't forget.

[00:11:33]
Don't forget how the deals coordinate the session timings with the weekly, monthly and larger things.

[00:11:41]
That's how they work.

[00:11:42]
If you have a low of this, if you have a low of the week, it's going to come in as a low of the day in New York.

[00:11:50]
You understand?

[00:11:51]
The low's going to come in.

[00:11:53]
In New York.

[00:11:54]
At the same time, the low of the week comes in.

[00:11:57]
Right after the stop on starting the session.

[00:12:00]
Those are how those structures are formed.

[00:12:02]
They're all coordinating together.

[00:12:03]
You don't just look on there and go last the low of the week.

[00:12:06]
The low of the week is coordinated as the stop hunt structure outside to the low on Wednesday.

[00:12:13]
Going into the US session.

[00:12:14]
That might particularly remove my even low week.

[00:12:18]
Coordinating with the low in the day.

[00:12:21]
It could be the low of the quarter for all we know.

[00:12:24]
You've got to keep an eye on these things.

[00:12:27]
Okay?

[00:12:32]
Understand.

[00:12:33]
That's what we're talking about.

[00:12:36]
All right?

[00:12:37]
So here's a big multi day outside structure.

[00:12:42]
Okay?

[00:12:43]
This was intraday inside outside structure.

[00:12:46]
Intraday outside structure.

[00:12:49]
Multi day outside structure.

[00:12:52]
Okay?

[00:12:53]
What do you got?

[00:12:54]
Let's look at it.

[00:12:55]
Man, that's a monster vector.

[00:12:58]
This is also on this particular chart.

[00:13:01]
This was pound swissy.

[00:13:04]
That also happened to be the low of the week.

[00:13:07]
Right here.

[00:13:08]
It was established on that outside move.

[00:13:10]
Coordinated with what?

[00:13:12]
London.

[00:13:13]
Shadow box.

[00:13:16]
Thanks.

[00:13:17]
See how the things come together?

[00:13:18]
Understand how the things come together.

[00:13:20]
It's a combination of spiking the low for London on a Wednesday or Tuesday or Thursday

[00:13:28]
that ties in with the low the week.

[00:13:32]
Understand?

[00:13:33]
Okay.

[00:13:34]
Yeah.

[00:13:35]
Deal it pulls back aggressively.

[00:13:36]
That's an essence of W.

[00:13:40]
When he goes, he makes the outside structure.

[00:13:42]
He goes into extended consolidation.

[00:13:46]
Anybody know what level this is?

[00:13:49]
Is that the same?

[00:13:51]
Yes.

[00:13:52]
Look at this.

[00:13:53]
Distance between the average.

[00:13:56]
Yes.

[00:13:57]
This is level three.

[00:13:58]
Why?

[00:13:59]
Price is making a hell of a lot of moves and they go anywhere.

[00:14:02]
That's a clue.

[00:14:03]
A low has been established.

[00:14:05]
And the view has come near it several times but not broken it or taken it out.

[00:14:12]
Right?

[00:14:13]
That's the definition of level three.

[00:14:17]
Last time I checked.

[00:14:19]
Now here's something that screws everybody up.

[00:14:25]
Look what he did.

[00:14:27]
He nailed the breakout traders and handle them and made them pay.

[00:14:34]
Oh, I should be sure.

[00:14:37]
You know better.

[00:14:40]
You know better.

[00:14:41]
This is the only play here.

[00:14:46]
That's it because of this.

[00:14:50]
This is not a shorting opportunity.

[00:14:53]
Can you take that and maybe in this pair particularly squeeze 50 pits out of that or 30

[00:14:59]
pits maybe but it's a sucker straight.

[00:15:02]
Why would you?

[00:15:03]
He's handling the breakout traders by swinging in both directions, right?

[00:15:07]
Great plus a close offering in little to little pips.

[00:15:11]
I guess they come in somewhere around here.

[00:15:14]
Great plus a close is nothing there.

[00:15:17]
I don't want you countering this stuff.

[00:15:19]
Garbage.

[00:15:20]
This is the only trade from here man.

[00:15:24]
Okay?

[00:15:25]
Straight rise.

[00:15:26]
And if you can't get it.

[00:15:27]
This would be a safety trade if what?

[00:15:30]
Anybody?

[00:15:31]
Can't talk that fast or will you have to?

[00:15:36]
If the dealer comes back below the Asian range and triggers the stock losses clean, that's

[00:15:41]
a safety.

[00:15:44]
Okay?

[00:15:46]
He's established a load a week on a big nasty outside vector, outside structure to the

[00:15:53]
low.

[00:15:54]
He's chopped around 11th read.

[00:15:56]
Keep traders confused about which way the direction is.

[00:15:59]
You walk up to the chart, you know, the separation of the averages.

[00:16:02]
You know, it's the lowest established.

[00:16:04]
You know, the dealer is not taking out that low.

[00:16:07]
Price has been dropping.

[00:16:09]
Have your position.

[00:16:10]
There's a nasty aggressive spike to the low.

[00:16:13]
The only move here is this way.

[00:16:16]
Gotcha.

[00:16:17]
Okay?

[00:16:21]
See it?

[00:16:22]
See it?

[00:16:23]
See it?

[00:16:24]
See it?

[00:16:25]
All right.

[00:16:26]
Something pretty cool over here.

[00:16:27]
Just follow them out and you can make a slide for it.

[00:16:28]
But here, let me help you with this right here.

[00:16:29]
This is pretty cool.

[00:16:30]
All right.

[00:16:31]
Let's see how these two highs are the same with the lows arising.

[00:16:36]
That's telling that he's going to break to the high side.

[00:16:41]
All right?

[00:16:44]
Why?

[00:16:45]
Picture him snatching the money, snatching the money moving away.

[00:16:50]
If the stocks pull back, snatching the money, pulling away.

[00:16:54]
Snatching the money, pulling away.

[00:16:57]
If you're following this breakout, which we don't,

[00:17:00]
I'm not telling you to do that.

[00:17:02]
I'm just telling you that this is confirmation to give you an idea of which way it's going.

[00:17:07]
He's grabbing the money and pulling it away.

[00:17:10]
Grab the money, pulling away.

[00:17:11]
That's his job.

[00:17:12]
He doesn't come back down here in this range because he snagging people that are seeing the bigger picture of the trend

[00:17:18]
and doing that shit.

[00:17:20]
So when they put their orders on, he's hitting them, pulling it back, hitting them, pulling it back.

[00:17:26]
Okay?

[00:17:29]
That's how it's setting that up.

[00:17:32]
And the fact that these levels haven't gotten any higher in here,

[00:17:36]
lets you know that you can expect them to continue on the rise.

[00:17:40]
But this is our signal right here.

[00:17:42]
This is our signal right here.

[00:17:43]
This is this structure.

[00:17:45]
This big outside structure.

[00:17:47]
Level three behavior.

[00:17:48]
Separation of the average is trading off of yesterday's low.

[00:17:51]
It gives you straight rise as coming.

[00:17:53]
Plus the pins are all down side, I think again.

[00:17:56]
The pins, the pins, the pins, the pins.

[00:17:59]
Look at all those trap pins to the downside.

[00:18:02]
Snatching go, snatching go, snatching go.

[00:18:05]
That's his job.

[00:18:06]
Trap and trigger, trap and trigger.

[00:18:07]
All right, another big multi-day.

[00:18:10]
Beautiful vector to the low.

[00:18:13]
Aggressive.

[00:18:15]
Chopping it up.

[00:18:16]
He went right to the four hour in this example.

[00:18:20]
And he'd absolutely, as you may, people go short below the four hour chart.

[00:18:25]
And then what does he do?

[00:18:26]
He trades right off of that number.

[00:18:28]
Doesn't allow anyone to see a frothing.

[00:18:32]
Snatching's the market away.

[00:18:34]
First he snatches away from the first root.

[00:18:36]
It stops it, it stops it, it stops.

[00:18:38]
Snatches away from the second root.

[00:18:40]
It stops it, stops it, stops it, stops.

[00:18:41]
Snatches away from the third root.

[00:18:43]
Or that one who snatches away from here.

[00:18:45]
Each subsequent move, snatching goes away from the third root.

[00:18:49]
Snatches, price away from the lower level short sellers that are jammed.

[00:18:56]
And each subsequent move does not allow the previous group of traders to see or vote for often.

[00:19:04]
Okay?

[00:19:07]
Thank you opposite.

[00:19:09]
This is not this.

[00:19:11]
That's for suckers.

[00:19:13]
This is trapping trigger, trapping trigger, trapping trigger into tight consolidation

[00:19:21]
to analyze my book.

[00:19:24]
Make sure I got what I need and then straight rise that get the hell out of there

[00:19:29]
in one bar.

[00:19:31]
If you took that trade off of a low anywhere along this accumulation phase,

[00:19:37]
when one in open you'd be out in two bars, three bars.

[00:19:42]
Okay?

[00:19:45]
Pins to the blueberry.

[00:19:48]
All right, good stuff, good stuff, good stuff.

[00:19:51]
Okay?

[00:19:52]
The spike showed you some pretty ones.

[00:19:55]
That's a definition of what a spike is.

[00:19:57]
Okay?

[00:19:58]
So what do you got so far?

[00:20:00]
Outside structure and W at the Batman vector.

[00:20:05]
We're tying it together with the tracers.

[00:20:09]
Okay?

[00:20:12]
All right.

[00:20:14]
The spike.

[00:20:15]
I thought it was appropriate to use railroad spikes since we used railroad tracks.

[00:20:20]
Okay, so cool.

[00:20:21]
What's the spike by definition?

[00:20:23]
An aggressive change in price usually following a news announcement.

[00:20:28]
But sometimes they show up just for no reason at all.

[00:20:32]
You're used to trigger the stops or to move the trading zone away from the price point

[00:20:38]
that he's trying to trap.

[00:20:41]
So if you've got higher levels of arms,

[00:20:43]
those spikes are the downside and pull it away.

[00:20:46]
If you're trying to trap lower level shorts,

[00:20:48]
those spikes are the upside to pull it away.

[00:20:51]
The direction is based solely upon dealer open volume.

[00:20:56]
We'll see you've never talked about open volume before.

[00:20:59]
The other open volume is the net long search is the net short at least holding.

[00:21:03]
Okay?

[00:21:06]
We'll see how the deal is all known for Nate together.

[00:21:10]
Because if they show you a set of crap on the chart that you fall for,

[00:21:14]
collectively the public is all net short or net long.

[00:21:17]
And the majority of the dealers are holding the opposite side of those trades.

[00:21:23]
So guess what?

[00:21:25]
If the public is net long, the dealers are net short.

[00:21:29]
And vice versa.

[00:21:31]
If the public is net short, the deal isn't net long.

[00:21:34]
It's just the nature of the business.

[00:21:38]
Our group, a small elite group of cool traders,

[00:21:43]
knows better.

[00:21:44]
We're in line with the dealers.

[00:21:48]
All right?

[00:21:50]
Okay.

[00:21:51]
So it also, my last point on here,

[00:21:55]
has nothing to do with the retail trader's trend.

[00:21:57]
Nothing.

[00:22:00]
It's just about the money.

[00:22:01]
You're an open volume, collectively.

[00:22:04]
Okay.

[00:22:05]
You guys still all right?

[00:22:06]
I'm running out of time, but I ain't stopping.

[00:22:08]
You're stuck with me for a little while.

[00:22:10]
Here's a spike.

[00:22:15]
25 to 50-50 candle.

[00:22:22]
That's big ass.

[00:22:24]
I've seen him crazy.

[00:22:25]
I've seen him 200.

[00:22:27]
And you guys know, in the summertime last year,

[00:22:30]
there was a $1,000-pift candle.

[00:22:33]
And I feel sorry some people got beat up on that.

[00:22:37]
You guys remember that?

[00:22:40]
Okay.

[00:22:41]
If I remember correctly on this t-handle,

[00:22:45]
Rick, you guys know Rick is famous.

[00:22:48]
He brought $362,000 on that candle.

[00:22:59]
He was long off of the W formation.

[00:23:06]
And I don't know what happened.

[00:23:07]
I don't know why it was formed.

[00:23:09]
They could blame it on some bullshit,

[00:23:10]
but it was just a big fat spike candle.

[00:23:14]
Thank you, Roger.

[00:23:15]
It was 1,000-pifts and 8 minutes.

[00:23:22]
Okay.

[00:23:23]
Rick booked.

[00:23:24]
During that market move, he booked quite a bit of money.

[00:23:27]
He booked more money than most people

[00:23:29]
who learned to save her and see in their life.

[00:23:31]
And it was absolutely a beautiful thing.

[00:23:33]
He called it off of the W.

[00:23:35]
It was amazing.

[00:23:38]
All right.

[00:23:40]
You got to be in it too in it, my friends.

[00:23:43]
Okay.

[00:23:45]
Look.

[00:23:49]
That's a spike.

[00:23:51]
If you look at one chart,

[00:23:56]
30-minute chart, that'd be one big aggressive move.

[00:23:59]
Spikes.

[00:24:00]
Comes out at the news time.

[00:24:01]
Garbage.

[00:24:02]
Garbage.

[00:24:03]
Garbage.

[00:24:04]
Garbage.

[00:24:05]
By the door.

[00:24:08]
Okay.

[00:24:10]
A spike is simply a way to clear the stops.

[00:24:14]
Site you out.

[00:24:16]
The other reminds me of a story.

[00:24:18]
I don't know if he's in here.

[00:24:19]
My friend Dave from California, I'll say Dave.

[00:24:22]
I love him.

[00:24:23]
He's a fantastic guy.

[00:24:25]
I think the first day in my class or the second day in my class,

[00:24:29]
before I talked about this stuff, we were sitting there and you know

[00:24:33]
he started at 6 o'clock.

[00:24:35]
And he was like, look how it's drilling and it's going.

[00:24:40]
And I had to stop the class and I go, that is exactly what the deal

[00:24:45]
wants you to do.

[00:24:46]
He wants you to feel like you're missing something and jump

[00:24:51]
on that garbage.

[00:24:53]
You understand?

[00:24:55]
The dealer throws that spike to shift his own, create excitement,

[00:25:01]
usually as a news vector or a trigger for the news,

[00:25:07]
to making chase the wrong stuff.

[00:25:11]
Okay.

[00:25:16]
So Dave, if you're listening to the lobby, I always

[00:25:19]
think he wants to drop some of that but he's a good sport man.

[00:25:22]
But anyway, understand the spike is a tool by the dealer.

[00:25:26]
It's just another way to take your money, man.

[00:25:29]
Don't fall for it.

[00:25:30]
Don't jump on.

[00:25:32]
Yes.

[00:25:33]
Oh, he is.

[00:25:34]
Dave went to Israel.

[00:25:35]
That's awesome.

[00:25:36]
Thanks, Fred.

[00:25:38]
All right.

[00:25:41]
Where are your tracks?

[00:25:43]
Talk about them a little bit, but let's just, by definition,

[00:25:46]
let's figure out what they are.

[00:25:48]
Keep going.

[00:25:49]
Okay.

[00:25:50]
Where will tracks or 30 minutes structure where the market

[00:25:55]
makers trigger the stops, shift his own, and set the high or low

[00:25:59]
all in one move?

[00:26:04]
Good question, John.

[00:26:06]
Is there a way to spike for an entry?

[00:26:08]
No, avoid it.

[00:26:09]
Let it calm down and then look for your entry.

[00:26:12]
Stop your entry.

[00:26:15]
I know you're excited now.

[00:26:16]
So I told you Rick made a fortune on a spiger.

[00:26:18]
I want to trace spikes now.

[00:26:19]
That's not what I'm telling you.

[00:26:21]
That Rick was in.

[00:26:22]
Rick was in previously on the structure.

[00:26:24]
It was an M or W. He had a beautiful W formation.

[00:26:27]
He took it and he was up 15, 20 picks and then Blake and I was up

[00:26:32]
800 picks.

[00:26:33]
That's what happened.

[00:26:35]
You got to be in a tune.

[00:26:36]
It was that a fluke was it locked?

[00:26:38]
Is it locked that he could pick the M and W formations blindfolded?

[00:26:42]
It's not locked.

[00:26:44]
But he was in the right direction of bias based on the previous

[00:26:48]
track move that the dealer showed.

[00:26:53]
And he nailed it.

[00:26:59]
Okay?

[00:27:00]
No.

[00:27:02]
Spillary ministructures where the market maker triggers the

[00:27:04]
stops, shift his own and sets the high and low in one move.

[00:27:10]
Good?

[00:27:13]
That's the real track.

[00:27:14]
That's the definition by definition.

[00:27:16]
What it is.

[00:27:17]
I know somebody thought it was a rail system that nice pretty cars right

[00:27:20]
on, but that's not the definition.

[00:27:22]
All right.

[00:27:23]
Look, there are tracks.

[00:27:26]
Used by the dealer.

[00:27:29]
At the ADR high at the blueberry, he goes in and he goes out.

[00:27:35]
Bam.

[00:27:36]
It's the stop, stops.

[00:27:37]
Look what he does.

[00:27:39]
Oh, Steve, it's just coming together now and tying it together.

[00:27:44]
The previous high was broken.

[00:27:49]
In 30 minutes or less over you get three pepperoni on the pizza.

[00:27:53]
And he closed well, well, well, well, that area.

[00:27:59]
Okay?

[00:28:01]
Steve, I'm shorting here.

[00:28:03]
The dealer comes back and hits me.

[00:28:06]
In 15 minutes, do I get out?

[00:28:08]
No.

[00:28:09]
If the dealer stays above the previous high like this, I recommend you scratch the

[00:28:16]
trade out.

[00:28:17]
He's analyzing his book and the next likely move is extend the high burger to

[00:28:24]
next level strikes him.

[00:28:27]
The dealer comes back in and comes back below the previous high on a nice solid

[00:28:33]
close.

[00:28:34]
Take him.

[00:28:35]
You got him.

[00:28:36]
And he goes, shift his own in the next handle.

[00:28:39]
You should have opened right there.

[00:28:41]
Seeing that's too big of a stop loss for me.

[00:28:44]
Okay?

[00:28:45]
You're one or not trader wants to trade five minis or seven minis to adjust

[00:28:48]
for that stop loss.

[00:28:49]
You need to get both those verbal tracks.

[00:28:52]
Bam.

[00:28:53]
Here you go.

[00:28:55]
Deal the railroad tracks.

[00:28:58]
Right above the blue tracer.

[00:29:00]
Bam.

[00:29:01]
I know Ken K talks about how she tries to find a better entry on the pullback.

[00:29:05]
That's accepted.

[00:29:06]
But do you mean?

[00:29:07]
The board to heat, wait for a little pullback.

[00:29:12]
The best way.

[00:29:13]
Okay?

[00:29:14]
I'm going to give you the best way to decide the entry.

[00:29:16]
It's taken from distance of this handle divided by three.

[00:29:24]
All right?

[00:29:25]
Divide it by three and take your entry one third off the high of this handle.

[00:29:29]
That's the best way to grab that entry.

[00:29:32]
I think it's a fit.

[00:29:35]
Is it Jim Nicholson?

[00:29:38]
All right.

[00:29:41]
Okay.

[00:29:42]
Look seriously.

[00:29:43]
Take the length of the handle.

[00:29:45]
Let's say it's 100 pits just to make it easy because I'm happy to guard it.

[00:29:49]
Okay?

[00:29:50]
So track 33 pitch off the high, a third, and put an entry right here.

[00:29:54]
Look for it to come in there and pin around there and grab it.

[00:29:57]
Okay?

[00:29:58]
All right.

[00:30:00]
Where are tracks?

[00:30:07]
This is the epitome of everything, right?

[00:30:15]
Coming together.

[00:30:22]
Exit it, go back home.

[00:30:27]
All right?

[00:30:29]
That should be a Mona Lisa painting.

[00:30:34]
The dealer's fake right past the moving averages to the high side.

[00:30:38]
He ends on the rear tracks.

[00:30:40]
And the next bar he shifts his own.

[00:30:43]
And in one bar, takes back all of this work.

[00:30:48]
So all that work.

[00:30:49]
He took it back in one bar, a pretty bastard.

[00:30:53]
Okay?

[00:30:54]
Then he does a nice drop.

[00:30:58]
Hit the stops.

[00:30:59]
Hit the stops.

[00:31:00]
Hit the stops.

[00:31:01]
Hit the stops.

[00:31:02]
Drop.

[00:31:03]
Turn the pins to the down side.

[00:31:06]
Form out a nice big aggressive W.

[00:31:09]
And it's over.

[00:31:10]
You got them.

[00:31:11]
Wait for this to close inside the mustard right here.

[00:31:17]
Wait for back to close inside the mustard.

[00:31:22]
Okay.

[00:31:25]
Understand that the stuff that's going on out there, okay?

[00:31:28]
The prevailing theory's out there gets you to chase the stop hunt, which is deemed in the public

[00:31:33]
eye as momentum.

[00:31:35]
The stop hunt is momentum.

[00:31:38]
You ever heard that?

[00:31:40]
Oh, it spiked out.

[00:31:43]
It broke out high.

[00:31:44]
That's a momentum can.

[00:31:45]
Well, I got to take that.

[00:31:47]
It's not momentum.

[00:31:48]
It's a stop hunt.

[00:31:49]
But the prevailing theory out there that doesn't know any better views that as a stop

[00:31:55]
hunt and takes it long.

[00:31:57]
Then the dealer pulls back, gets you to chase the hunts.

[00:32:01]
Maybe you run a crit or two gym if you get bored.

[00:32:04]
On the ADCD projection, maybe take a break out or two.

[00:32:11]
Now, I'm insulting anybody.

[00:32:12]
I just want you to understand there's something else going on.

[00:32:16]
These things are market myths that will always lead to your failure.

[00:32:19]
But the problem is retail traders get it right so they keep refilling their account.

[00:32:26]
But I promise you there's slowly a road to equity and dragging from your separate

[00:32:31]
truth to your hard earned money.

[00:32:34]
Okay.

[00:32:35]
And Jim, you know I love you man.

[00:32:38]
I'm just picking all you.

[00:32:39]
You're going to man.

[00:32:40]
How could I be the man if you're the man?

[00:32:43]
Okay.

[00:32:44]
Fibonacci extensions.

[00:32:47]
Right.

[00:32:48]
The AV equals.

[00:32:49]
This is that famous lightning bolt pattern that everybody talks about.

[00:32:52]
The AV equals.

[00:32:53]
And I like to say the AV equals a little crap.

[00:32:55]
When you trade crap, you get crap.

[00:32:58]
Okay.

[00:32:59]
All right.

[00:33:02]
You guys hanging in there with me most done.

[00:33:05]
I went a little long.

[00:33:06]
I know.

[00:33:07]
Okay.

[00:33:08]
Fending tradesmen not.

[00:33:13]
Okay.

[00:33:16]
You're only defense against these guys is to learn and identify their behavior.

[00:33:28]
Trade in line with the market maker.

[00:33:31]
Don't be afraid to trade both ways of the signals present.

[00:33:35]
The hardest thing.

[00:33:38]
So I'm going to set it a few posts back.

[00:33:40]
Let go of your bias and see what the dealer does.

[00:33:45]
Steve, what's going to happen tonight at London?

[00:33:48]
You know, I don't know.

[00:33:49]
I'll tell you around four o'clock.

[00:33:52]
If the dealer comes out of the Asian range and betters to the high side and draws an

[00:33:57]
M, then I can tell you he's going to go short for London.

[00:34:02]
I can't tell you that right now.

[00:34:05]
But I can tell you around three thirty four o'clock New York time.

[00:34:08]
By the way, his behavior is.

[00:34:11]
I analyze his behavior for next move.

[00:34:15]
That's it.

[00:34:19]
Taking consideration of bigger track, those outside structures, the things that we talked about tonight,

[00:34:25]
validating those M's and W's over eight bars.

[00:34:30]
Atta few filters, tiny element, brick straight,

[00:34:34]
panels, spikes to the high low,

[00:34:38]
cap of batman's, denim, denim, denim, denim, your rich.

[00:34:43]
Get it?

[00:34:44]
Those are the things I'm talking about.

[00:34:46]
All right, quick test.

[00:34:49]
They got a little piece of paper, no book.

[00:34:51]
Sticky, I don't care.

[00:34:53]
We just covered a bunch of patterns.

[00:34:57]
Right in and down.

[00:34:58]
Tell me what they are.

[00:34:59]
I'll be quiet for two minutes.

[00:35:00]
I want to direct you to a post.

[00:35:02]
Fred just wrote to me.

[00:35:03]
Fred McIntosh, I'm me, don't know who's from the California Group.

[00:35:06]
He's a fantastic guy, great trader.

[00:35:08]
Him and his girlfriend, I don't know if they're still together.

[00:35:10]
But him and his girlfriend are hanging out.

[00:35:12]
They trade together.

[00:35:13]
They both have taken my class.

[00:35:15]
And he just grabbed a YW on AU, Australian USD.

[00:35:20]
And he said he nailed fifty while this was going on.

[00:35:24]
So he's going to post that for us in the form.

[00:35:27]
Okay?

[00:35:28]
You guys want to go take a look at that.

[00:35:30]
Thanks for it.

[00:35:31]
Appreciate it.

[00:35:34]
I know somebody who listens to me.

[00:35:43]
Not sure.

[00:35:44]
That's okay.

[00:35:45]
But Fred's been around for a while.

[00:35:51]
All right, Greg.

[00:35:58]
Greg got fifty-five on AU, fifty-six on A.J. and twenty-five on CJ.

[00:36:03]
Steven Shelley grabs CJ and A.J.

[00:36:06]
I love this stuff.

[00:36:07]
I love the hearing.

[00:36:12]
Mike got thirty-six.

[00:36:16]
Twenty-four.

[00:36:17]
Twenty percent.

[00:36:18]
I'll address it.

[00:36:19]
Twenty percent.

[00:36:20]
One is a count.

[00:36:21]
Good stuff, man.

[00:36:22]
This is the stuff I want to hear.

[00:36:23]
Love it.

[00:36:24]
Love it.

[00:36:25]
Love it.

[00:36:26]
Love it.

[00:36:27]
Thank you.

[00:36:28]
That's a nice birthday present for me.

[00:36:29]
Okay.

[00:36:30]
Look.

[00:36:31]
You should have the answers.

[00:36:32]
Okay, so what I want you to do is the stuff that we just covered, you need to incorporate

[00:36:37]
the flashcards to represent these outside structures, these bigger moves.

[00:36:41]
Go look at that GVPCHF tray that I just showed you on the slide.

[00:36:46]
That was an easy grab.

[00:36:48]
Make sure you take a picture of that.

[00:36:50]
GVPCHF outside to the high, wide open averages, and then two more hits after that.

[00:36:56]
Go get that picture for yourself.

[00:36:58]
It's a good picture.

[00:37:06]
Grace says the more I talk, the better you've done, I might just have to sit there and

[00:37:08]
laugh all night.

[00:37:15]
Gloria, I understand that you're confused that I'm not telling you not to trade it.

[00:37:19]
Yes, but here's the deal.

[00:37:21]
When you become more proficient, what I tell you is the beginners, I want you to trade

[00:37:26]
at the times I say and the trades I say because I want you to have success.

[00:37:30]
But once you start to see it, it's like that picture.

[00:37:33]
You can't unsee it.

[00:37:35]
So if you see these patterns clearly, there's absolutely no reason why you can't trade.

[00:37:41]
But if you're not having success, then you don't trade outside the times that I've illustrated

[00:37:46]
for you.

[00:37:48]
When you start having success and the times I illustrated, you can expand your window of

[00:37:52]
trading opportunities.

[00:37:53]
Okay, so while it wasn't clear on that, I hope that cleared it up.

[00:37:58]
And yes, Gloria, I still love you.

[00:38:00]
Okay, you should have the answers.

[00:38:02]
Let me pop them up.

[00:38:04]
We're almost done.

[00:38:05]
I'm going to have a barbeque outside for my birthday.

[00:38:08]
We're hanging out.

[00:38:09]
All right, you should have half a batman upside down half a batman.

[00:38:13]
Evening morning star, spike to the low vector, spike to the high vector.

[00:38:18]
Right, where we're attracts.

[00:38:20]
Two pins high, low, and we're W. Extended consolidation after a pattern, right?

[00:38:29]
That long length of consolidation followed right after an outside structure.

[00:38:34]
So you get the outside structure, extended consolidation off of the low or off of the

[00:38:39]
high.

[00:38:40]
That's a pattern.

[00:38:41]
That's part of the pattern.

[00:38:45]
Thanks, Guy.

[00:38:47]
Okay.

[00:38:48]
Okay.

[00:38:49]
Start on the graph it up here.

[00:38:57]
Very important.

[00:38:58]
I'm going to grow this last couple of slides and it's a wrap tonight.

[00:39:02]
Market makers create a sentiment and act against it.

[00:39:06]
Oh my God, the year old EU Union is falling apart, dropping, dropping, dropping.

[00:39:10]
What?

[00:39:11]
Well, the year old one up.

[00:39:12]
How did that happen?

[00:39:14]
Market makers turn the entire world short.

[00:39:17]
They buy from you and then they rise the market as a surprise.

[00:39:21]
Per depth somewhere before.

[00:39:22]
Because they're one of my classes.

[00:39:27]
Market makers use sentiment and act against it.

[00:39:30]
They use the news and rumors to take your money.

[00:39:35]
Okay.

[00:39:37]
Summary.

[00:39:38]
Market behavior.

[00:39:39]
Market makers behavior.

[00:39:40]
Fast move is false.

[00:39:45]
Spikes being roo-tracts.

[00:39:47]
Vectors false.

[00:39:48]
A quick move in Forex is done on low volume to create Dave from California type of

[00:39:56]
statement.

[00:39:57]
Someone asked me how did you enter the spike?

[00:40:01]
This bullet handles this right here.

[00:40:03]
Never chase right here falling currency.

[00:40:05]
It's a sucker's play.

[00:40:07]
Market makers drop the market to buy.

[00:40:12]
Market makers rise the market to dump.

[00:40:14]
They pump to dump, drop to buy.

[00:40:18]
The LOI and H-O-Y.

[00:40:20]
I mentioned this before.

[00:40:22]
Let me tell you what it is.

[00:40:23]
I mean, you remember.

[00:40:24]
Below of the year and high of the year quarter season or track moves.

[00:40:30]
Do not trade these as breakouts.

[00:40:33]
It is a sucker's play.

[00:40:37]
Okay.

[00:40:38]
If you're always at the low of the year for breaks and I'm taking a short, it's a sucker's

[00:40:41]
play.

[00:40:42]
Don't do it.

[00:40:43]
Ask Goldman Sachs if they're stuck holding pound short from less Christmas trading, falling

[00:40:53]
into the extremes as breakouts is a sucker's play by the market maker.

[00:40:59]
Don't fall forward.

[00:41:00]
Don't forget the market makers extend the high and low in three moves.

[00:41:05]
Is it always three moves?

[00:41:07]
No.

[00:41:08]
Of course not.

[00:41:09]
But if you watch the high and low board, you'll see what I mean.

[00:41:12]
How they cut or it's then high and low in bursts.

[00:41:17]
Usually three good ones.

[00:41:18]
It'll be a burst, a burst, and a track.

[00:41:21]
It could be a burst, a tack, and a burst.

[00:41:23]
But that's how they do it.

[00:41:25]
15 to 25 pits.

[00:41:26]
You blink an eye, bam, vector.

[00:41:28]
You hold, hold, hold, hold, hold, vector again.

[00:41:33]
Hold, hold, hold, tack reverse.

[00:41:36]
Do the high, low, drool.

[00:41:37]
You'll see the stuff.

[00:41:41]
And finally, nope, I missed one.

[00:41:43]
Market makers need to book a profit.

[00:41:46]
The trend will contain 20 to 25 pit pullbacks and three levels of move with corresponding

[00:41:53]
levels of consolidation.

[00:41:56]
That is the levels.

[00:41:57]
Intraday levels, weekly levels.

[00:42:00]
They have to book.

[00:42:02]
So they go, hit the high, vector, drop.

[00:42:05]
Hit the stop, hit the stop, hit the stop, hit the stop, flip the proper drop.

[00:42:10]
Hit the stop, set the downside.

[00:42:12]
Induced, induced.

[00:42:13]
Second, let it hit the stop, the rod is back in the consolidation of the day.

[00:42:17]
The pattern, the pattern, the cycle, the cycle.

[00:42:20]
It never changes.

[00:42:22]
That outside structure that I showed you, go back.

[00:42:25]
You'll find it for 20 years on the charts.

[00:42:29]
The moves are the same.

[00:42:32]
The timing and pit value on the right hand side of the chart is the only thing that changes.

[00:42:38]
The behaviors do not change.

[00:42:42]
It's a game.

[00:42:43]
Once you understand, they only got four plays.

[00:42:46]
You won't need these guys.

[00:42:51]
And finally, a powerful extended move is always followed by level three behavior.

[00:42:56]
Consolidation to bring traders back into the frame to confuse you about what the direction

[00:43:01]
is.

[00:43:02]
The outside structure is the first formation of this.

[00:43:04]
Then they will top within that structure.

[00:43:09]
The key you confuse about which way it's going.

[00:43:12]
Our group of traders is not confused.

[00:43:14]
Vector to the high outside structure, high to the weak, you're a seller.

[00:43:18]
Outside structure to the low, low of the weak, trading off that level, you're a buyer.

[00:43:23]
You are a market maker trader.

[00:43:25]
You know better.

[00:43:28]
Okay, getting close.

[00:43:33]
What the dealer shows you on the chart is to validate the technicals, to line his own pockets.

[00:43:37]
When he grabs at your pockets, I hope he comes up with my friends.

[00:43:44]
You now know better.

[00:43:51]
Okay, this is a wrap.

[00:43:55]
We'll not see you next Sunday.

[00:43:57]
We're off.

[00:43:58]
We're off.

[00:43:59]
We're off.

[00:44:00]
Let me erase this right here right now.

[00:44:02]
And now I'm going to see you next Sunday.

[00:44:06]
Okay, keep the drills going.

[00:44:08]
Do some R&D.

[00:44:09]
I mentioned it's never too late to roll up your sleeves and get it on.

[00:44:13]
Come on, man.

[00:44:15]
Okay.

[00:44:17]
I'm going to have a big fat ribeye on the grille and honor you guys tonight.

[00:44:21]
Here's what I want you to do.

[00:44:24]
Enjoy your meet.

[00:44:25]
Do some homework.

[00:44:29]
Thank you, Jeff.

[00:44:30]
What I'd like you to do next weekend is a holiday.

[00:44:34]
I want you to start planning this because you guys are like crazy obsessed.

[00:44:38]
You can't do it.

[00:44:39]
Unless you're brand new, if you're brand new, this doesn't apply to you.

[00:44:42]
If you've been around for a little while, I want you to maybe Friday night,

[00:44:47]
stick a week in all spending some time with your family and get away from the computer.

[00:44:51]
I promise you it's going to do you some good.

[00:44:55]
Relax your mind, spend some time with your family, reconnect with what's important in your life.

[00:45:02]
Stop thinking about the stupid marker maker stuff.

[00:45:04]
It'll be here when you get back.

[00:45:06]
Enjoy a nice weekend that you've been with me since January, so it's mid-May.

[00:45:12]
Five months, six months nonstop and give yourself a break.

[00:45:17]
I promise you it'll come back refreshed, recharge, and you might even start seeing things a little different.

[00:45:22]
Remember when you do those pictures, you'd have to blink, walk away, come back and look at it.

[00:45:27]
You see it?

[00:45:28]
This is no different.

[00:45:30]
Walk away, come back, come back, refresh for June.

[00:45:37]
We're going to have a class.

[00:45:38]
We're going to review.

[00:45:39]
Give yourself the much needed break right now.

[00:45:42]
Okay?

[00:45:43]
And if you're ready for the June web class, come to New Jersey.

[00:45:45]
We'll hang out and you'll be guys ready to go for July.
