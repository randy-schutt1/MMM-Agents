# 17_EXECUTION_ROBOT — PHASE 12

Automated execution. The final stage, not the starting point.

## STATUS: EMPTY — DO NOT BUILD YET

Requires: validated strategy (Phase 7–9), completed forward testing (Phase 10), and
a risk engine (Phase 11).

## MANDATORY CAPITAL-PROTECTION MECHANISMS

No execution system ships without all of these:

- maximum risk per trade
- maximum daily loss
- maximum weekly loss
- maximum concurrent exposure
- maximum number of trades
- spread filters
- stale-data checks
- duplicate-order protection
- disconnect handling
- broker-error handling
- **kill switch**
- manual override
- paper-trading phase
- small-capital deployment phase

## DEPLOYMENT SEQUENCE

```text
Paper trading
  → small capital, tightly capped
  → gradual increase, only on sustained evidence
  → normal operation
```

**Never transition directly from historical testing to unrestricted live trading.**

## THE STANDING WARNINGS

> Never treat backtested profitability as proof of live profitability.

> The robot is the final stage, not the starting point.

Every rule this system executes must be traceable — through the machine spec, the
master spec, and the lesson corpus — to either course evidence or explicitly
documented research. A rule nobody can trace is a rule nobody can defend when it
loses money.

**Master the method first. Formalize second. Automate third. Validate before
risking capital.**
