# V16 — INDEPENDENT REVIEW, ROUND 2

**Round:** R2 — independent re-review of the owner-directed R1 fix round
**Reviewer:** Independent Reviewer / Teacher Agent (`D-003`)
**Date:** 2026-08-15
**Lesson:** `Bootcamp1 Wk7 050612 Part2 (45mins).swf` · V16 · 00:44:35
**Reviewed:** current `phase2/cross-lesson-review` tree at `43f1cb7`

## FINAL DECISION

> # **`PASS`**
>
> **0 CRITICAL, 0 MAJOR, 0 MINOR, 1 NOTE. Confidence: `HIGH`.**

Items **222–225 are `CLOSED — VERIFIED`**. This round did not author the historical fixes. It
re-read the three source images, re-measured their horizontal levels independently, re-ran
`PT-044` from the checksummed corpus, and re-performed the V15/V16 quarantine-file comparison.

## §1 — ITEM 222: CLOSED

`A-101` now limits the equal-spacing objection to the schematic slide. Independent row-density
measurement on `V16_00-25-10_price-fails-at-m3-pivot-4-times.png` recovers the labelled grid at
approximately `230 / 295 / 388.5 / 483.5 / 546.5 / 611 / 706.5` pixels. The four midpoint
relations hold within image-resolution tolerance. The second chart independently shows labelled
levels near `291.5 / 425 / 498 / 571.5 / 705.5`; its two unlabelled dashed rows are correctly
excluded. The corrected record therefore distinguishes measured visual corroboration from an
instructor-stated formula. `DO NOT CODE M1–M4` correctly remains in force because the construction
is unstated, partly assumption-dependent, and complicated by the unresolved `M5` passage.

## §2 — ITEM 223: CLOSED

The schematic now records all nine levels, including `R2`, and eight gaps. Direct inspection
confirms the complete ordering `R2 · M4 · R1 · M3 · CPP · M2 · S1 · M1 · S2`; the corrected
centres and gap series support the stated near-equal-spacing conclusion. The explicit
`R1→R2 = 107 px` versus `CPP→R1 = 105 px` comparison now tests the sentence that previously
omitted its required endpoint.

## §3 — ITEM 224: CLOSED

`PT-044` pre-registers `W-D = 2013-01-06 → 2016-06-30`. The runner now clips development bars to
`L.DEV_START` and `L.DEV_END` locally without changing the shared library. A clean re-run produced
output byte-identical to the committed text and left the result JSON unchanged:

- arm A: `n=894`, `O1=0.0727`;
- arm B: `n=777`, `O1=0.0798`;
- median arm delta: exactly `2.00` pips.

`BT_V16_0001.md` retains the superseded wider-window figures and cause, reports the corrected
scorecard as **5 of 5**, and warns that prediction 4 passes with zero margin. No verdict moved and
no sealed period was touched.

## §4 — ITEM 225: CLOSED

The V15/V16 `VISUAL_INDEX.md` comparison now reports **13 rewritten and 9 byte-identical content
lines**. The nine identical lines are the three screenshot headers, three timestamps, and three
`Visual Type` values. `Q-017` adds the exact `Visual Type` triple to the invariant and correctly
uses it, with the timestamp triple, as the cheap fixed-string detector before semantic subject
comparison. The correction strengthens rather than weakens the quarantine finding.

## §5 — CHECKS AND NOTE

- `PT-044` deterministic rerun: committed text output identical; result JSON unchanged;
- source-image level checks: both real-chart relations and the nine-level schematic reproduce;
- quarantine census and detector wording: verified;
- no ambiguity was falsely closed, no machine rule was promoted, and no trading edge was claimed.

**Note:** this R2 supplies the independent separation the owner-directed fix round lacked. The
historical self-verification warning remains append-only.
