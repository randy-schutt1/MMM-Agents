# HistData.com does not publish M15 or H1 — a NEGATIVE RESULT, measured

> **Status:** `ESTABLISHED — VENDOR-DOCUMENTED` · **Measured:** 2026-08-13 (UTC 2026-08-14T02:38Z)
> **Governs:** this dataset's provenance, and the scope of `CROSSCHECK_REPORT.md`.

---

## THE QUESTION THIS FILE ANSWERS

This dataset was commissioned as an **import of HistData.com's native M15 and H1 GBP/USD
corpora**, to be cross-checked against M15/H1 bars aggregated locally from the existing
`D-036a` M1 corpus. The comparison would have been the strongest possible evidence about
our bucket boundaries: an independent party, drawing the same bars from the same tick
stream, agreeing or disagreeing with us candle by candle.

**That comparison cannot be run. HistData publishes no M15 and no H1, in any format, on
any platform it serves.** This is not a retrieval that failed and could be retried. It is
a property of the vendor.

---

## THE EVIDENCE

### 1. The vendor's FAQ, verbatim

> **For Which TimeFrames?**
> *"We can only deliver you time ordered Tick and M1 (1 minute) data."*
>
> — `https://www.histdata.com/f-a-q/`, retrieved 2026-08-13

### 2. The download page enumerates every platform, and every one is M1 or tick

Retrieved from `https://www.histdata.com/download-free-forex-data/` the same day. The page
offers five platforms; the timeframe list is exhaustive and there is no M15 or H1 anywhere
in it:

| Platform offered | Timeframes offered |
|---|---|
| MetaTrader 4 / MetaTrader 5 | M1 only — *"This platform allows the usage of M1 (1 Minute Bar) Data only"* |
| Generic ASCII | M1, Tick |
| Microsoft Excel | M1 only |
| NinjaTrader | M1, Tick (1-second, last/bid/ask) |
| MetaStock | M1 only |

The paid tiers the same page advertises (FTP/SFTP access, Google Drive automatic updates)
are **delivery-speed** products for the same five file formats. **Paying HistData does not
buy a coarser bar** — there is no coarser bar to buy.

### 3. This is what the project already believed, and had already written down

Two committed artifacts state it, and this measurement confirms both rather than
discovering anything:

- `D-036a`, describing the corpus: *"`MetaTrader` format, **M1 (1-minute) bid bars** — the
  finest the vendor publishes"*.
- `06_MANUAL_BACKTEST/scripts/aggregate_m15.py`, in its own docstring: *"Why an aggregator
  instead of downloading M15 directly. The vendor's own M1 file is the finest thing it
  publishes; every coarser bar is a derived object."*

The commissioning brief for this dataset asked for something the repository's own
documentation already said did not exist. **Checked rather than assumed, in both
directions** — the docs could have been stale, and they were not.

### 4. Captured pages, hashed

Both pages are archived in `_evidence/` (gitignored bulk; the hashes are the record):

```text
443fc91d9b3ecea07f0b6c5c73ca685f31b7fef6848f5dc052b70f4384df7db9  download-free-forex-data.html
c2bd6c258cbde4ff5792888a09f9b32823d8491c1480c115ed1b2498412742af  f-a-q.html
```

---

## WHAT FOLLOWS, AND WHAT DOES NOT

**What follows.** The M15 and H1 bars in `derived/` are **ours**. Their bucket boundaries
were chosen by `aggregate_m15.py` and are auditable, reproducible and internally
cross-checked seven ways (`CROSSCHECK_REPORT.md`). They are **not** validated against any
independent feed, and no work in this repository may describe them as though they were.

**What does NOT follow — and this is the part worth being careful about.** The absence of
a comparison is not evidence that our boundaries are right, and it is not evidence they are
wrong. It is an *unmeasured* quantity, and an unmeasured quantity is not a passing grade.
Anyone reading `CROSSCHECK_REPORT.md`'s seven PASSes should read this paragraph first: they
establish that our aggregation is *self-consistent*, which is a genuinely useful thing to
know and is a strictly weaker claim than *correct*.

**`D-036a` already made this trade deliberately, and its reasoning is unaffected.** It
rejected *"trusting a vendor-published M15 file instead of aggregating locally"* on the
grounds that **`D-031` makes the bucket boundary the tested variable, so the boundaries must
be ours and auditable.** Under that reasoning a native vendor M15 would have been a
*cross-check*, never the *source* — which is exactly the role it is missing from here.
Nothing in `D-036a` needs revisiting.

---

## HOW THIS GAP COULD BE CLOSED — NOT A SESSION'S CALL

Closing it means introducing a **second data vendor**, which changes what the corpus *is*.
That is a decision of the `D-034` / `D-036` / `D-036a` class: it belongs in `DECISIONS.md`,
on the integration branch, with an owner ruling — and `D-038a` puts `DECISIONS.md` out of
reach of a task branch like this one. **This session deliberately did not adopt one.**

Recorded for whoever takes that decision, as options and not as recommendations:

| Option | What it would buy | What it would cost |
|---|---|---|
| **Leave it open** | Nothing changes. The boundaries stay ours, unvalidated, and honestly labelled. | The gap persists — permanently, for these windows. |
| **A second free vendor with native M15/H1** (e.g. a Dukascopy-derived feed) | A genuine external boundary check. | A new vendor is a new provenance chain, a new timezone convention, a new QA gate, and a new `D-034`-class entry. Vendors also disagree on *levels* (`D-034` fact 2), so a mismatch would need attributing between "our boundary is wrong" and "their prices differ", which is not always separable. |
| **Reconstruct from an independent tick source** | The strongest check available — same instrument, different tick stream. | The most work by a wide margin, and it re-opens every question `D-036a` settled. |

Until one of those happens, the honest sentence is the one at the top of every rendered
chart and every QA report: **the bucket boundaries are ours, cross-checked internally, and
unvalidated against any outside feed.**
