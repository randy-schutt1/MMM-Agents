# V18 — HOMEWORK

## §1 — THE ASSIGNMENT, VERBATIM

V18 sets homework in one block, `[00:45:31]`–`[00:46:04]`. Quoted with its ASR defects intact:

> `[00:45:31]` *"OK, I really don't have any homework for you this week except the last seven and a
> half weeks of homework that I've been giving you."*
> `[00:45:43]` *"So what I need you to do, the end of the age and session this week is draw your
> line on"* → `[00:45:52]` *"24 hour charge look for peak formation."*
> `[00:45:58]` *"Look for the dealer to make the high and low of the week look for safety trade
> sets."*
> `[00:46:04]` *"Look for clean, seeable flashcards setups."*

⚠️ *"the end of the age and session"* is an ASR defect for **"the end of the Asian session"**;
*"24 hour charge"* for **"24-hour charts"**; *"safety trade sets"* for **"safety trade setups"**.
**These are read, not guessed:** *"Asian"* appears 9× elsewhere in the file and *"the end of the
sessions"* is his own phrasing at `[00:04:26]`.

**Four items:**

| # | Item | Measurable here? |
|---|---|---|
| 1 | Draw your lines at the end of the Asian session, on 24-hour charts | ❌ a drawing task |
| 2 | Look for peak formation | ❌ **V18 never constructs a peak formation** |
| 3 | **Look for the dealer to make the high and low of the week** | ✅ **YES** |
| 4 | Look for clean, seeable flashcard setups | ❌ needs the flashcard set |

⭐ **Item 3 is measurable because it needs no formation recognition — only an extreme and a clock.**
That is the whole of what was executed. **Items 1, 2 and 4 are recorded as NOT DONE, with reasons,
rather than approximated.**

---

## §2 — WHAT WAS RUN

`06_MANUAL_BACKTEST/scripts/hw_v18.py` → `data/hw_v18_output.txt`, `data/hw_v18_results.json`.

**This is HOMEWORK, not a test.** It states no hypothesis, scores no prediction, and returns no
verdict. Corpus: HistData GBP/USD M1, DEVELOPMENT scope, both `D-031` arms, **13/13 files verified
against `raw/SHA256SUMS.txt`**. A week is included only if built from complete session days
(all 96 fifteen-minute buckets present). **181 complete weeks on each arm.**

⚠️ **Session boundaries are `PT-046` §2a's DECLARED CONVENTION, not V18's** — the lesson states no
clock time for any session (`A-131`). Every percentage below inherits that caveat.

---

## §3 — RESULT: WHEN THE WEEKLY HIGH AND LOW ARE MADE

### §3.1 — BY DAY OF THE WEEK (arm A, 181 weeks)

| Day | Weekly HIGH | Weekly LOW |
|---|---|---|
| +0 (Mon) | **28.7%** (52) | **23.8%** (43) |
| +1 (Tue) | 13.3% (24) | 16.6% (30) |
| +2 (Wed) | 11.6% (21) | 16.0% (29) |
| +3 (Thu) | 19.3% (35) | 9.9% (18) |
| +4 (Fri) | **27.1%** (49) | **33.7%** (61) |

⭐ **A pronounced U-SHAPE on both extremes: the week's high and low are made at its ENDS.**
Monday + Friday account for **55.8%** of weekly highs and **57.5%** of weekly lows, against **40%**
if the five days were equally likely. **Midweek is where they are least often made** — Wednesday
takes 11.6% of highs, Thursday 9.9% of lows.

⚠️ **THE ARMS DISAGREE, AND NOT TRIVIALLY.** Arm B puts the weekly-high peak on Monday (33.7%) and
**Thursday** (24.9%) with Friday at only **10.5%** — where arm A has Friday at 27.1%. **A one-hour
DST shift should not move a day-of-week distribution by 17 points.** This is a **caution about the
measurement**, not a finding about the market, and it is stated as such. It most likely reflects the
interaction of Arm B's `+1 h` shift with the 17:00 session-day anchor near the Friday close, and it
is the reason no day-of-week claim is carried into any other V18 artifact.

### §3.2 — BY SESSION (arm A)

| Session | Length | Weekly HIGH | Weekly LOW | Highs **per hour** |
|---|---|---|---|---|
| `S1` Asian `17:00–03:00` | **10 h** | 27.1% (49) | 16.6% (30) | **2.7 %/h** |
| `S2` London `03:00–09:00` | **6 h** | 36.5% (66) | 43.1% (78) | **6.1 %/h** |
| `S3` US `09:00–17:00` | **8 h** | 36.5% (66) | 40.3% (73) | **4.6 %/h** |

⭐⭐ **This is the one robust result in the homework, and both arms agree on it.** The Asian session
is the **longest** of the three at 10 hours and produces the **fewest** weekly extremes. Normalised
per hour, **London is 2.3× as likely as Asian to contain the weekly high, and 4.8× as likely to
contain the weekly low.** Arm B reproduces the pattern (Asian 30.9% / 14.4%; London 32.6% / 37.6%;
US 36.5% / 48.1%).

**Read against V18:** it is consistent with — though it does not test — `[00:04:26]` *"Trade the
pairs at the beginning of the sessions or the end of the sessions when the dealer becomes active
above or below the Asian range"*, and with the lesson's treatment of the Asian range as the quiet
box that later gets broken rather than as where the work happens.

⚠️ **It is NOT evidence for any V18 rule.** No rule in V18 predicts this distribution. It is
descriptive, and it is reported because the assignment asked where the weekly extremes are made and
this is where they are made.

---

## §4 — WHAT WAS NOT DONE, AND WHY

| Item | Status | Reason |
|---|---|---|
| 1 — draw lines at the Asian close on 24 h charts | ⬜ **NOT DONE** | A drawing exercise with no measurable output. Approximating it would produce a number the assignment never asked for |
| 2 — look for peak formation | ⬜ **NOT DONE — BLOCKED** | **V18 never constructs a peak formation.** It is used 17× and defined 0 times. Implementing one would be testing my invention, which is the failure `PT-043` established for this project |
| 4 — clean, seeable flashcard setups | ⬜ **NOT DONE — BLOCKED** | The flashcard set is a V17 artifact (`V17_SOURCE_NOTES.md` §6) and V18 adds nothing to it. Carrying it forward would import a V17 reading into a V18 result |

**Three of four items are not done, and that ratio is the honest headline of this homework.** V18
sets an assignment that rests almost entirely on objects it does not construct.

---

## §5 — DISCLOSURES

1. The session partition is `PT-046` §2a's declared convention. **V18 supplies no session clock
   times.**
2. The week key is Monday-anchored on the 17:00 session day; `mmm_lib` has no committed week
   definition, so this one is **declared here** and is used nowhere else.
3. **Arm-B day-of-week figures disagree materially with Arm A (§3.1) and no day-of-week claim is
   carried forward from this file.** The by-session result (§3.2) is the only one both arms support.
4. Excluded incomplete session days: **11** (arm A), **245** (arm B). Reported, not dropped silently.
5. Nothing here is a test. **No verdict, no prediction, no score.**
