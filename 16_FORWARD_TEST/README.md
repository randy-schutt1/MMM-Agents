# 16_FORWARD_TEST — PHASE 10

Paper trading / shadow trading in live conditions.

## STATUS: EMPTY — DO NOT BEGIN YET

Requires a validated strategy with robustness testing complete (Phase 9).

## WHY THIS PHASE EXISTS

Historical testing cannot reveal: real spread behaviour at signal time, slippage on
actual fills, data-feed differences between the backtest source and the live feed,
latency, signal timing against live candle closes, or the operational failures that
only appear when a system runs unattended.

A strategy that passes backtesting and fails forward testing has not been unlucky —
it has been measured properly for the first time.

## RECORD FOR EVERY SIGNAL

Timestamp, instrument, timeframe, setup type, signal per the system, whether it
matched a manual reading, entry / stop / target, spread at signal, actual vs
expected fill, outcome, R, and any discrepancy between backtest and live behaviour.

Discrepancies are the **primary output** of this phase. Log them all.

## RULES

- Frozen system. No rule changes mid-test; a change restarts the sample.
- No discretionary overrides — that measures the trader, not the system.
- Run long enough to cover multiple market conditions.
- Compare forward results honestly against backtested expectations, and record
  material divergence as a finding rather than absorbing it.

Forward testing precedes any real-capital deployment, which precedes any
unrestricted deployment.
