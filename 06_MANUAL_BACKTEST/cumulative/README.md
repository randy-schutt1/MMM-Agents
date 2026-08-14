# CUMULATIVE BACKTEST SUMMARIES

## STATUS: `CUMULATIVE_SUMMARY.md` COVERS ALL 31 TESTS EXECUTED AND REPORTED TO DATE

*(was: "EMPTY — NO OBSERVATIONS TO SUMMARIZE", then "COVERS ALL 21 TESTS RUN TO DATE",
both retained rather than deleted so the progression is visible. The "21" line was
**stale and wrong in both of its numbers** when `GAP_AUDIT_2026-08-14.md` found it —
see the `⚠ WHY THIS FILE WAS REWRITTEN` block at the head of `CUMULATIVE_SUMMARY.md`.
40 PT files exist; 32 have a committed `BT_*` record; **31 were executed and
reported**; 8 have never been run.)*

Aggregate views across lessons: `CUMULATIVE_SUMMARY.md`,
`CUMULATIVE_VXX_TO_VYY.md`.

## RULES

- **Summaries never replace individual observations.** Every underlying record
  stays in `06_MANUAL_BACKTEST/VXX/`, permanently.
- Report **rule-application** statistics first; trade outcomes are secondary during
  the Student Phase.
- Never present a win rate as validation of the method. Metrics worth tracking once
  enough observations exist: total, wins, losses, breakevens, win rate, average win,
  average loss, expectancy, profit factor, max drawdown, consecutive
  losses/wins, average and median R, MAE, MFE, time in trade, session, weekday,
  setup type, market regime, spread and slippage sensitivity.
- Never exclude observations from a summary to improve it. If a subset is excluded
  for a legitimate methodological reason, state the exclusion and the count
  explicitly — silent truncation reads as full coverage.
- Any claimed accuracy figure from the course is a **hypothesis being tested**, not
  a target to reach (`DECISIONS.md` D-009).
