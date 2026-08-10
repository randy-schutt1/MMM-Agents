# 15_AUTOMATED_BACKTEST — PHASE 8–9

Repeatable historical strategy testing.

## STATUS: EMPTY — DO NOT BEGIN YET

Requires a validated recognition engine (Phase 6) and deterministic strategy rules
(Phase 7). Backtesting an unvalidated detector measures the detector's mistakes.

## BEST PRACTICES

- Prevent lookahead bias; avoid survivorship bias where relevant.
- Model spreads, commissions, and realistic slippage.
- Use realistic order assumptions.
- Define timezone and session boundaries **explicitly**.
- Do not tune on the entire dataset.
- Separate development and validation data; maintain true out-of-sample data.
- Perform walk-forward validation.
- Test multiple market regimes and parameter sensitivity.
- Inspect losing clusters and tail outcomes.
- Preserve raw trade records.
- Test rule ablations — which rules actually contribute?
- Test robustness rather than peak performance.

## PARAMETER SELECTION

> Prefer **stable parameter regions** over isolated optimal values.

A parameter that works only at exactly 1.7 and fails at 1.6 and 1.8 has found noise.
Never choose parameters because they produce the best equity curve.

## EVALUATION

Never validate a system on win rate alone. Evaluate win rate, expectancy, profit
factor, drawdown, average win, average loss, loss clustering, tail losses, regime
dependence, session dependence, spread and slippage sensitivity, sample size, and
stability.

> **Do not allow a beautiful equity curve to override methodological flaws.**

## THE CLAIMED ACCURACY

Any 90–95% claim from the course is a **hypothesis under test**, never a target
(`DECISIONS.md` D-009). If results do not match it, that is a finding — not a
reason to adjust the rules, the sample, or the labelling.

## AND THE STANDING WARNING

Never treat backtested profitability as proof of live profitability.
