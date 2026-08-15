# DECISION DRAFT — `D-051` (proposed) — THE OWNER'S ADR INDICATOR AND `A-100`

> ## ⛔ NOTHING IN THIS FILE IS A DECISION. NOTHING HERE IS ADOPTED.
>
> One **draft**, prepared on the owner's remark *"In the indicator folder, I have an ADR indicator
> that we could use."* It is written out to the point where the owner can answer
> **yes / no / edit**, and the approved text can be appended to `DECISIONS.md` unchanged. It
> mirrors `DECISION_DRAFTS_2026-08-14.md`'s `D1`→`D-045` exactly, including the discipline that
> made `D-045` survivable: **admission is not reading, and closure on this rung is provisional.**
>
> Until the owner rules:
>
> - **`DECISIONS.md` is unchanged.** No `D-051` exists.
> - **`A-100` remains `OPEN` and `DO NOT CODE`.** `A-038` and `C-022` are untouched.
> - **`SOURCING_HIERARCHY.md` §1's `TOOLING` rung is unchanged** — it admits
>   `Ultimate Blue.tpl` / `!SM_TDI` **and nothing else**, per `D-045` rule 1.
>
> **Numbering.** `D-050` is the highest existing entry, so this draft claims **`D-051`**.

---

## 0. THE ONE-PARAGRAPH SUMMARY, INCLUDING THE PART THAT DID NOT GO THE OWNER'S WAY

The indicator folder was found and it does contain an ADR indicator — `mm_adr`, **with readable
MQL4 source**, which is better evidence than `!SM_TDI` ever was (that one was compiled). **But it
is not the indicator on the course's own charts, and this draft says so before it says anything
else.** The V07 charts are stamped `ADR 1.5 20100528 01 Mod 01` and print a nine-field readout
`mm_adr` cannot produce. `mm_adr` is a *different* ADR indicator that happens to be in the owner's
possession.

⭐ **And then the interesting thing happened.** Working out *why* the two disagree required
reconstructing the course indicator's arithmetic from the V07 frames — and **that reconstruction
closes, exactly, on Tier 1 evidence the corpus has held since V07 and never solved.** Two of
`A-100`'s five open rows are answered by the course's own charts, at Tier 1, with **no TOOLING
rung needed at all**. A third is answered by `mm_adr` at TOOLING tier. **The lookback — the row the
owner most wants closed — is NOT answered, and `mm_adr` makes it worse, not better:** it supplies
a fourth candidate number.

---

## 1. WHAT WAS SEARCHED, AND WHAT WAS FOUND

**The folder.** `/Users/randyschutt/Documents/Forex indicator/` — literally named "Forex indicator",
outside this repo, with `Forex222/` inside it. Also searched: this repo in full, `14_PINE/`,
`06_MANUAL_BACKTEST/tools/`, `/Users/randyschutt/Desktop/Trading/Indicators/`, the Wine MT4
install under `~/Library/Application Support/net.metaquotes.wine.metatrader4/`, and a
Spotlight sweep of the whole volume for `*adr*` and for every `.ex4 / .mq4 / .ex5 / .mq5 / .tpl`.

| # | Artifact | Path | md5 | What it is |
|---|---|---|---|---|
| **1** | `mm_adr.mq4` | `Documents/Forex indicator/Forex222/` | `807876a6334579af6b95dcbdee7d8004` | ⭐ **Full MQL4 SOURCE, 2,042 bytes, 75 lines.** Not compiled. Every line readable |
| **2** | `mm_adr.ex4` | same folder | `95e6063e026f810ad2a10856c145e416` | The compiled build of #1 |
| **3** | `Bo.tpl` | `Desktop/Trading/Indicators/` | `cfa32805fbc37a089dc4e17b4c3fafb7` | An MT4 template with `mm_adr` **attached and saved**: `name=MM_ADR`, `<inputs> ADRPeriod=21.0`, and the live comment `ADR=104 Pips to High=103 Pips to Low=81` |
| **4** | `3M-shadow-boxes-15M.tpl` | `Desktop/Trading/Indicators/` | `19187de9ac84dce672849c5cfa52a795` | ⭐ **A SIBLING OF THE COURSE'S OWN INDICATOR** — chart comment `ADR 1.00 20051027 01 Mod 01`, plus the `[ADR] ADR High Line / ADR Low Line / today start` object family |
| **5** | `FX dynasty.tpl` | `Desktop/Trading/Indicators/` | — | Same `[ADR]` object family, later dates |
| **6** | `Ultimate Blue.tpl` | `Desktop/Trading/Indicators/` | `ea22c8cf527921cef072586b6fa28296` | ⭐ **The exact artifact `D-045` already admitted** — and it carries a **third, different** ADR: `Daily Range PeterE`, `NumOfDays=10`, printing `ADR = 118.7  (10 days)  Today = 135.3` |

⚠ **NOT FOUND anywhere on the volume:** the course's own `ADR 1.5 20100528 01 Mod 01`, in either
source or compiled form. A grep for its distinctive strings (`Reached=`, `To ADR High`,
`Today's Range`) across every indicator folder and the MT4 install returns **zero files**.

Note for the record: `Documents/Forex indicator/Forex222/` also holds `MM4XSF_TDI (1).ex4` —
**the TDI family that grounded `D-045` lives in this same folder.** The `mm_` / `MM4XSF_` prefix
is common to both. That is provenance, not proof.

---

## 2. `mm_adr.mq4` — THE COMPLETE CONSTRUCTION, READ OFF THE SOURCE

```mql4
extern double ADRPeriod = 21;

int SundayCount = 0;
for (i = 1; i <= ADRPeriod; i++)
    if (TimeDayOfWeek(iTime(NULL, PERIOD_D1, i)) == 0) SundayCount++;
Periods = ADRPeriod + SundayCount;

for (i = 1; i <= Periods; i++)
    if (TimeDayOfWeek(iTime(NULL, PERIOD_D1, i)) != 0)
        ADR += iHigh(NULL, PERIOD_D1, i) - iLow(NULL, PERIOD_D1, i);
ADR /= ADRPeriod;

PipsToHighD = (iLow (NULL, PERIOD_D1, 0) + ADR) - Bid;
PipsToLowD  =  Bid - (iHigh(NULL, PERIOD_D1, 0) - ADR);
```

| `A-100` open row | What `mm_adr` states |
|---|---|
| Lookback window | `ADRPeriod`, **default 21**, user-settable; `Bo.tpl` saves it at **21** |
| What is averaged | ⭐ **`iHigh − iLow` of the D1 bar. PLAIN RANGE, NOT TRUE RANGE.** No `iATR`, no gap term, no previous close anywhere in the file |
| Marker anchor | ⭐ **Upper = today's LOW + ADR. Lower = today's HIGH − ADR.** Not open-centred, not midpoint-centred, not previous-close-centred |
| Day boundary | The `PERIOD_D1` bar boundary of the chart's own server clock. **No absolute offset is asserted and none can be read off the source** |
| Intraday update | Recomputed every tick from `iHigh/iLow(D1, 0)`, which only ever widen ⇒ **both markers move monotonically outward as the day develops.** `C-022`'s *"creep up or creep down"* is the first half; ⚠ **it does not produce "creep down", so this does NOT resolve `C-022` and is not offered as doing so** |
| Bar #0 | Excluded from the average (loop starts at `i = 1`) — today never averages itself |
| Sundays | ⭐ Excluded, and the window **extends** to compensate, so exactly `ADRPeriod` non-Sunday days are averaged. **This is the mechanism by which a "two week" intent and a bar count can legitimately differ** — see §5 |

---

## 3. ⭐⭐ THE PART THAT NEEDS NO TOOLING RUNG: THE V07 FRAMES DETERMINE THE ANCHOR AT TIER 1

`04_SCREENSHOTS/V07/INDEX.md` frames 14 and 15 have printed the course indicator's whole output
since V07 and the corpus has read them as *"an observation about the indicator's display, not a
course rule."* **They are arithmetically determinate and nobody had run the arithmetic.**

**Frame 14, `V07_00-13-55`, EURJPYm M15 — `ADR Value= 1081, Reached= No, Today's Range= 732,
T's High= 110.451, T's Low= 109.719, Target High= 110.800, Target Low= 109.370,
To ADR High= 989, To ADR Low= 441`:**

| Hypothesis | Computation | Printed | |
|---|---|---|---|
| Today's Range = `T's High − T's Low` | `110.451 − 109.719 = 0.732` | `732` | ✅ exact |
| **Target High = `T's Low + ADR`** | `109.719 + 1.081 = 110.800` | `110.800` | ✅ **exact** |
| **Target Low = `T's High − ADR`** | `110.451 − 1.081 = 109.370` | `109.370` | ✅ **exact** |
| Reached = (Range ≥ ADR) | `732 < 1081` | `No` | ✅ |
| Bid, recovered from the high side | `110.800 − 0.989` | `109.811` | ✅ agrees… |
| Bid, recovered from the low side | `109.370 + 0.441` | `109.811` | ✅ …**with itself** |

**Six equations, zero residual, on a frame that was never built to be checked.** The last two are
the strong ones: the two distance fields are independent and they reconcile to a single price.

**Frame 15, `V07_00-16-20`, EURUSDm M15 — `ADR Value= 1023, Reached= Yes, Today's Range= 1030,
T's High= 1.32537, T's Low= 1.31507, Target High= 1.32537, Target Low= 1.31514,
To ADR High= 8?6, To ADR Low= 137`:**

| | Computation | Printed | |
|---|---|---|---|
| Today's Range | `1.32537 − 1.31507 = 0.01030` | `1030` | ✅ exact |
| Target Low = `T's High − ADR` | `1.32537 − 0.01023 = 1.31514` | `1.31514` | ✅ **exact** |
| Reached | `1030 ≥ 1023` | `Yes` | ✅ |
| Bid, from the low side | `1.31514 + 0.00137 = 1.31651` | symbol line reads `1.31651` | ✅ **independent** |
| Target High = `T's Low + ADR` | `1.31507 + 0.01023 = 1.32530` | `1.32537` = **`T's High`** | ⚠ **clamped** |

⭐ **The clamp is the point, not a defect.** Once the ADR is consumed, `T's Low + ADR` falls
*inside* the day's realised range, so the indicator reports the realised high instead:
`Target High = max(T's Low + ADR, T's High)`. **That is `Reached= Yes` doing something**, and it is
consistent with `[00:25:26]`'s *"it turns red when [it's met]"*.

⚠ **ONE DIGIT IS UNRESOLVED AND IT IS THE TEST OF THE CLAMP.** `To ADR High` reads `866` or `886`
at the 1024-px capture. The clamp predicts `1.32537 − 1.31651 = 0.00886` → **`886`**, which would
make frame 15 exact in every field. `866` leaves a 20-pip residual and the clamp would need
another explanation. **This is a five-minute re-verification against the original `.swf` at native
resolution under `SWF_CAPTURE_RECIPE.md`, and it should be done before this draft is adopted.**

⭐ **`mm_adr`'s anchor formula is the same rule, line for line** — `iLow(D1,0) + ADR` and
`iHigh(D1,0) − ADR`. Two independently-authored indicators, one of them the course's own, agree on
the anchor. **So the anchor row of `A-100` closes on TIER 1, from the course's own frames, and
`mm_adr` merely corroborates it.**

---

## 4. THE SIBLING ARTIFACT — `3M-shadow-boxes-15M.tpl`

The course chart's first comment line reads `ADR 1.5 20100528 01 Mod 01`. `3M-shadow-boxes-15M.tpl`
carries, as its saved chart comment, `ADR 1.00 20051027 01 Mod 01` — **the same
`ADR <version> <yyyymmdd> 01 Mod 01` stamp, five years earlier.** It also persists the drawn
objects the course frames show:

- `[ADR] ADR High Line` / `ADR Low Line` — horizontal rays, style 2 (dotted), colour `42495`,
  with labels `ADR High: 1.57256` / `ADR Low: 1.55412`. **Separation 184.4 pips.**
- `[ADR] today start` + label `ADR Start` — ⭐ **a vertical line marking the ADR's day boundary**,
  drawn at epoch `1431388800` = **exactly 00:00** in the chart's clock. `FX dynasty.tpl`'s is at
  `1437523200`, also **exactly 00:00**. Three instances, all exact midnights.

⚠ **What that does and does not settle.** It settles that the indicator's day boundary is the
*platform's* midnight D1 boundary — the same object `mm_adr` reads via `iTime(PERIOD_D1)`. **It
does NOT settle the UTC offset**, because MT4 writes template times in *server* time and the
server is unidentified. **Transplanting V16 `[00:40:22]`'s *"midnight to midnight"* from the
PIVOTS onto the ADR is still the `A-082` error and this draft does not do it.** `A-100`'s
day-boundary row therefore moves from *"stated nowhere"* to *"a D1 boundary, offset unknown"* —
progress, not closure.

---

## 5. ⚠ THE LOOKBACK: THIS MAKES IT WORSE, AND THE DRAFT SAYS SO

The corpus already had a three-way conflict. It now has four candidates:

| Candidate | Source | Tier |
|---|---|---|
| **10** (two trading weeks) | Mauro PDF *"the last 2 weeks"*, one reading | Tier 2 |
| **10**, stated as a number | ⭐ `Ultimate Blue.tpl` → `Daily Range PeterE`, `NumOfDays=10`, printing `(10 days)` — **inside the artifact `D-045` already admitted** | `TOOLING` |
| **14** (two calendar weeks) | the other reading of *"the last 2 weeks"* | Tier 2 |
| **15** | ⭐ V16 `[00:09:31]` *"the last two weeks, **15 days**"* — **the course author's own mouth** | **Tier 1** |
| **21** | `mm_adr`'s default; `Bo.tpl` saves it at 21 | `TOOLING` |

⭐ **`mm_adr` does contribute one real idea to the contradiction, and it is not a number.** Its
Sunday-skip loop shows that in MT4 **a "day" is a D1 bar, and brokers ship a stub Sunday bar**. A
window meant as *two weeks* spans **15 daily bars** on a broker with Sunday bars: 10 weekday bars
+ 2 Sundays + … — the arithmetic depends on the broker's exact bar set, and *this is the only
mechanism found anywhere in the corpus by which "two weeks" and "15 days" are both true of the
same window.* ⚠ **It is a hypothesis with a mechanism, not evidence.** No artifact found states
15, and `mm_adr` itself would need `ADRPeriod` set to something other than its default to produce
it. **This draft does NOT adopt it and `A-100`'s lookback row does NOT close.**

### ⭐ THE DECISIVE TEST, PRE-REGISTERED HERE AND DELIBERATELY NOT RUN

The two V07 frames print the course indicator's ADR **as a number, on a dated chart**:

- **`ADR Value = 1023`** — EURUSD, chart date **2012-03-21**
- **`ADR Value = 1081`** — EURJPY, chart date **2012-03-22**

Under §2's construction (mean of D1 `high − low`, bar 0 excluded, Sundays skipped), **each
candidate `N` predicts one number.** Compute the trailing mean for `N ∈ {10, 14, 15, 21}` on 2012
EURUSD and EURJPY daily bars and compare. **A single candidate matching both instruments to
within a pip or two, when the others miss, resolves `A-100`'s lookback row on TIER 1 arithmetic —
not on TOOLING, not on the Mauro PDF, and not on picking one of the author's two numbers.**

⛔ **NOT RUN, and the reason is a scope rule, not a shrug.** `06_MANUAL_BACKTEST/datasets/` holds
**GBP/USD only, 2013 onward** (`D-036a`, `D-044`). 2012 EURUSD/EURJPY daily data is not in this
repo, and acquiring it is a `D-036a`-class data-source decision that belongs to the owner, not to
a session drafting a proposal. **Pre-registering the test before the data exists is the point** —
it cannot then be tuned to the answer. ⚠ Note the residual risk that would have to be disclosed
in the run: the course's broker feed is unidentified, so a 1–3 pip mismatch is uninformative and
only a **clean separation between candidates** counts.

---

## 6. THE PROPOSED LEDGER ENTRY — TEXT FOR THE OWNER TO APPROVE, EDIT OR REJECT

> ## D-051 — The owner's `mm_adr` MQL4 source is admitted to the `D-045` `TOOLING` rung; `A-100`'s RANGE DEFINITION closes PROVISIONALLY; its ANCHOR closes on TIER 1 independently; and its LOOKBACK does NOT close
>
> **Date:** 2026-08-14
> **Extends:** `D-045` Part 1 (the `TOOLING` rung), whose per-artifact admission rule requires a
> separate entry for every artifact. `D-045` is not superseded and its three travelling rules apply
> here unchanged.
>
> **Part 1 — the artifact.** `mm_adr.mq4` (md5 `807876a6334579af6b95dcbdee7d8004`) and its build
> `mm_adr.ex4` (md5 `95e6063e026f810ad2a10856c145e416`), supplied by the owner from
> `Documents/Forex indicator/Forex222/` and attested by the owner, are admitted to the
> **`TOOLING — OWNER-ATTESTED PLATFORM ARTIFACT`** rung. ⭐ **It is SOURCE, not a compiled binary
> or a saved parameter block** — the strongest artifact yet admitted to this rung, and the first
> whose every field can be read rather than inferred. Admission is **per-artifact** and covers
> these two files and nothing else. Citations carry **`[TOOLING] mm_adr.mq4`**.
>
> **Part 2 — what closes on TIER 1, and therefore does NOT need this rung.** ⭐ `A-100`'s
> **MARKER ANCHOR** row closes **`RESOLVED BY COURSE`**: `Target High = today's Low + ADR`,
> `Target Low = today's High − ADR`, clamped to the realised extreme once `Reached`. The evidence
> is `V07_00-13-55` and `V07_00-16-20` — Tier 1, the instructor's own chart — which satisfy the
> rule in **six independent equations with zero residual**, including two distance fields that
> reconcile to a single Bid. **`mm_adr` corroborates this and is not what closes it.**
>
> **Part 3 — what closes PROVISIONALLY on this rung.** `A-100`'s **RANGE DEFINITION** row closes
> **`PROVISIONALLY RESOLVED — TOOLING`**: the averaged quantity is **`high − low` of the daily bar,
> NOT true range**, with the current day excluded. ⚠ **The weakness, stated at the closure and not
> glossed: `mm_adr` is not the indicator on the course's charts.** The course's is stamped
> `ADR 1.5 20100528 01 Mod 01` and prints nine fields `mm_adr` cannot produce; `mm_adr` is a
> different tool the owner happens to hold. The two are shown to share an **anchor**; they are
> **not** shown to share a **range definition**, and the frames do not constrain it. Any artifact
> relying on plain-range cites this decision and inherits this paragraph.
>
> **Part 4 — what does NOT close, and the entry is written so this cannot be misread.** ⛔ **The
> LOOKBACK row of `A-100` remains `OPEN`, and this decision makes the conflict WORSE: 10 / 14 / 15
> / 21.** `mm_adr`'s default of 21 has no course support of any kind. `Ultimate Blue.tpl`'s
> `NumOfDays=10` is a *different* ADR indicator in an already-admitted artifact and is likewise not
> the course's. **The ADR marker remains `DO NOT CODE` on the lookback**, and every `PT`/`BT`
> touching it still pre-registers its own lookback as an `ASSUMPTION` under `D-027`. `C-022` is
> **untouched** — `mm_adr` widens both markers monotonically and cannot produce *"creep down"*.
> `A-113`'s completion threshold is untouched. `A-038` is untouched.
>
> **Part 5 — the day boundary, half-answered.** The `[ADR] today start` object in
> `3M-shadow-boxes-15M.tpl` and `FX dynasty.tpl` fixes the ADR's own boundary at the **D1 bar
> boundary of the platform clock** — three instances, all exact midnights. ⚠ **The UTC offset stays
> unknown**, MT4 writing template times in unidentified server time. **Importing V16's pivot
> *"midnight to midnight"* onto the ADR remains the `A-082` error and is not done here.**
>
> **Reason:** `A-100` blocks the whole of V15's lesson and rows of V16–V17 behind it, and three
> lessons have failed to state a construction — `A-093`'s pattern, which is why `A-100` exists. The
> owner's offer of a platform artifact is the same move that broke `A-084`, and it partly works
> again. It also produced something better than itself: forcing the comparison surfaced that the
> corpus's own V07 frames were arithmetically determinate and had never been solved.
>
> **Evidence:** `mm_adr.mq4` and `.ex4` (md5s above); `Bo.tpl` (`ADRPeriod=21.0`);
> `3M-shadow-boxes-15M.tpl` (md5 `19187de9ac84dce672849c5cfa52a795`, chart comment
> `ADR 1.00 20051027 01 Mod 01`, `[ADR]` object family); `Ultimate Blue.tpl` (md5
> `ea22c8cf527921cef072586b6fa28296` — the `D-045` artifact — `Daily Range PeterE`, `NumOfDays=10`);
> `04_SCREENSHOTS/V07/INDEX.md` frames 14–15 and the frames themselves; V16 `[00:09:31]`; the
> Mauro PDF p. 43 (`D-039`); `A-100`, `A-038`, `A-082`, `A-093`, `C-022`; `D-045`;
> `SOURCING_HIERARCHY.md` §1 `TOOLING` rung and §3.4. Owner attestation, 2026-08-14.
>
> **Alternatives considered:** *Closing `A-100` outright on `mm_adr`* — **rejected, and this is the
> whole discipline of the entry.** `mm_adr` is demonstrably not the course's indicator; a full
> closure would assert far more than the evidence carries and would be the `A-082` error committed
> deliberately. *Adopting `ADRPeriod = 21` as the lookback* — rejected; 21 is a shipped default
> with zero course support and would overwrite the author's own Tier 1 *"15 days"* with a stranger's
> constant. *Adopting `10` from `Ultimate Blue.tpl`* — rejected for the same reason, and it is a
> third indicator again. *Declining `mm_adr` entirely because it is the wrong tool* — rejected; the
> range-definition question is genuinely unanswerable from Tier 1 and this is the only artifact in
> the corpus that answers it at all, provisionally. *Running the §5 lookback test in this session* —
> rejected; the 2012 data is not in the repo and acquiring it is an owner-level `D-036a`-class
> decision.
>
> **Consequences:**
>
> 1. `SOURCING_HIERARCHY.md` §1's `TOOLING` rung gains `mm_adr.mq4` / `.ex4` as its **second**
>    admitted artifact, with md5s and a pointer here. The rung's rules are unchanged.
> 2. `A-100` is amended row by row: **anchor → `RESOLVED BY COURSE`** (Tier 1, Part 2);
>    **range definition → `PROVISIONALLY RESOLVED — TOOLING`** with Part 3 quoted in full;
>    **day boundary → PARTIAL** per Part 5; **lookback and intraday update → `OPEN`, unchanged.**
>    ⛔ **`A-100` as a whole remains `OPEN`.**
> 3. The §3.4 re-check obligation attaches to `A-100`'s range-definition row, which joins `A-014`,
>    `A-023`, `A-020` and `A-084` on that list. **A later Tier 1 statement overturns it under
>    `D-040` §3.1.** Any session reaching a lesson that shows an **ADR properties dialog**, a
>    **Navigator/inputs panel**, or states a **day count or a range definition in speech** must run
>    §3.1 against `A-100`.
> 4. ⭐ **`A-038` (V07's own ADR-lookback record) becomes ELIGIBLE and is NOT closed here** — the
>    `D-045` rule-2 caution repeated deliberately. A session that reads the frames against `A-038`
>    closes it, or does not.
> 5. The §5 lookback test is **pre-registered by this entry**. A session acquiring 2012 EURUSD /
>    EURJPY daily data runs it as specified — including the "clean separation only" criterion —
>    and reports the result **whether or not it helps**.
> 6. ⚠ **`To ADR High` on `V07_00-16-20` must be re-read at native `.swf` resolution before Part 2
>    is cited as six-of-six.** If it reads `886` the clamp is exact; if `866`, Part 2's clamp
>    sentence is reopened. Part 2's anchor closure does **not** depend on it — frame 14 is exact
>    without it — but the clamp sentence does.
> 7. Every `PT`/`BT` using the plain-range definition states in its own pre-registration that the
>    value is `TOOLING`-tier and provisional, so a later overturn is traceable to the runs it
>    affected.
>
> **Status:** ACTIVE — `A-100`'s range-definition closure under it is PROVISIONAL; `A-100` itself
> remains OPEN

---

## 7. THE THREE QUESTIONS FOR THE OWNER

1. ⭐ **Is `mm_adr` the indicator you meant?** The folder is
   `Documents/Forex indicator/Forex222/` and it is the only ADR indicator on the volume. **It is
   not the one on the course charts** (§1) — if you have or can get
   `ADR 1.5 20100528 01 Mod 01`, or any `.ex4` printing `Reached=` / `To ADR High`, **that
   artifact would let `A-100` close properly rather than provisionally, including the lookback.**
   It is the single highest-value item this project could be handed.
2. **Do you attest `mm_adr` as your working configuration for this method**, in the same sense you
   attested `!SM_TDI` for `D-045`? Part 1 of the draft depends on it and nothing else does.
3. **Do you want the §5 lookback test run?** It needs 2012 EURUSD and EURJPY daily bars, which is
   a `D-036a`-class data decision. It is cheap, it is pre-registered above, and it is the only
   route found that could settle **10 / 14 / 15 / 21** on arithmetic instead of on choosing.
