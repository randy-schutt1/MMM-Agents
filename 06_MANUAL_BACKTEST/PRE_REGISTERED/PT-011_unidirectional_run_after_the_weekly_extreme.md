# PT-011 — Is the rest of the week a "unidirectional swing" after the extreme?

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V02 [00:14:37], [00:14:54]; V03 [00:33:36]–[00:34:19]
BLOCKERS:   I-007 · D-028 boundary dates unpinned
ATTESTATION: No chart in W-C was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

The payoff half of the whole weekly thesis is one phrase:

> *"Their goal is to tie up your margin, charge you swap or interest, and **move away from
> you in a unidirectional swing for the rest of the week**."* V02 `[00:14:37]`

Everything the method promises after the anchor — the hold, the target, the swing-trade
option — assumes the remainder of the week travels **in one direction**. That word is
measurable without any of the blocked vocabulary: directional efficiency is
`|net movement| ÷ path length`, and it needs a start point, an end point and the bars in
between.

The instructor also supplies the counter-example himself, which is what makes this test
fair rather than rhetorical:

> *"Net change for the week zero… the dealer starts on ends on Friday where he started on
> Sunday"* V03 `[00:33:36]`; *"Very little profit seen on swing trades. Well, very little
> none. How about that? None"* `[00:34:15]`

So the course's own position is *usually unidirectional, sometimes net-zero*. **The
question is the proportion**, and nobody has measured it.

---

## 2. THE QUESTION

> After the week's extreme prints, is the remainder of the week more directionally
> efficient than a matched span of the same length elsewhere?

Null hypothesis: **it is not.** Post-extreme efficiency matches what any equal-length span
delivers.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| Window | **W-C** — 2013-01-06 → 2017-12-29 |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| Anchor | The timestamp of the week's high **or** low, whichever the week's net direction runs away from. Both are computed; the choice rule is stated here and not decided per week |
| Metric — **efficiency** | `\|close(week end) − price(anchor)\| ÷ Σ\|bar-to-bar movement\|` over the post-anchor bars, in `[0,1]` |
| Metric — **monotonicity** | Largest counter-directional retracement after the anchor, in pips and as a share of the total move |
| Metric — **net-zero weeks** | Share of weeks whose Friday close sits within ±25 pips of the Sunday/Monday open — V03's own counter-case, counted rather than asserted |
| Post-hoc anchor, disclosed | The anchor is only knowable **after** the week ends. **This test is retrospective by construction and is therefore `DESCRIPTIVE` about structure, never a trading result.** It is labelled so in every report |
| Sample | ~260 weeks. ≥ 30 satisfied |

**The retrospective-anchor disclosure is load-bearing.** A trader cannot know on Wednesday
that Wednesday's high is the week's high. This test measures whether the *structure* the
course describes exists; it does not and cannot show that it is tradeable. Any report that
elides that is `E14` at the level of the whole test.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary — the natural control** | Efficiency over **equal-length spans anchored at a random bar** in the same week, 1,000 draws, seed `20260812`. Same week, same volatility, same length; only the anchor changes |
| **Second** | Efficiency over equal-length spans anchored at the **extreme of a randomly chosen other week's** relative position — controls for the mechanical fact that any span starting at a local extreme has elevated efficiency by construction |
| **Third** | **N3 — week-anchor shift**, 1,000 draws |

The second arm is the one that matters. *A span beginning at an extreme is directional
almost by definition* — that is arithmetic, not market-maker behaviour, and a test that
skipped this control would confirm the thesis every time.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Post-extreme efficiency exceeds **all three** controls | Genuine support for the unidirectional claim, beyond the extreme-anchoring artifact |
| Exceeds arm 1 but not arm 2 | **The claim is an artifact of anchoring at an extreme.** The most likely outcome and the most valuable one to establish early |
| Net-zero weeks are common (say >25%) | V03's counter-case is not rare, and any swing-hold instruction inherits that base rate. Report the share prominently either way |
| Arms A and B diverge | Report both; the anchor bar can move by an hour between arms |

## 6. MANDATORY SCOPE STATEMENT

> PT-011 measures directional efficiency after a **retrospectively identified** weekly
> extreme. It is **not** a trading test, **not** a test of the anchor point (`A-001`), and
> it adopts **no** day count (`C-001` untouched). It cannot support any claim that the
> post-extreme run is capturable in real time, because its anchor is unknowable in real
> time.

## 7. TO RUN THIS

1. Close `I-007`; confirm W-C is DEVELOPMENT.
2. Harvest with timestamps from DOM text only.
3. Compute the three controls **before** the observed efficiency distribution.
4. Report the net-zero share in the headline, not the appendix.
5. Write `BT_V02_NNNN.md` from the template, §0 referencing this file, classified
   `DESCRIPTIVE` per §3.
