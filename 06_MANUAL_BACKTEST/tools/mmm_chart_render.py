#!/usr/bin/env python3
"""
===============================================================================
mmm_chart_render.py — MMM visual study-chart renderer  (M15 / H1, GBP/USD)
===============================================================================

WHAT THIS IS
  A batch renderer that turns the derived M15 / H1 GBP/USD bars into PNG chart
  images a human can look at: candles, the five EMAs, an optional session-box
  overlay, and a TDI panel underneath. It is a PYTHON PORT of the two Pine
  Script chart-marking tools that live beside it —
      MMM_Indicator.txt   (EMAs + session boxes, overlay)
      MMM_TDI.txt         (TDI, separate pane)
  — and it inherits every provenance caveat those files carry. Where a value
  below is tagged, the tag is copied from them, not re-derived here.

WHAT THIS IS FOR — AND THE DISTINCTION THAT MATTERS MOST
  This is PATTERN-RECOGNITION PRACTICE. It is a different activity from the
  PT-series numerical backtests under `06_MANUAL_BACKTEST/`, and it must never
  be mistaken for one.

      A PT test states a prediction in advance, pre-registers it, runs it once
      against a fixed window, and reports the number it gets — including when
      the number is unwelcome. Its discipline exists because a hypothesis you
      can revise after seeing the data is not a hypothesis.

      THIS TOOL MAKES NO PREDICTION. It draws a chart. There is nothing to
      pre-register because nothing is being tested, and a picture cannot be
      evidence for or against a rule.

  The corollary is the part that gets forgotten: BECAUSE THIS MAKES NO
  PREDICTION, IT ALSO PRODUCES NO EVIDENCE. Studying two hundred rendered
  windows and forming an impression is not a finding, does not close an
  ambiguity, does not support a rule, and may not be cited in a mastery report
  as though it did. What it legitimately produces is a student who recognises a
  shape faster. That is worth having and it is not a result.

  See the README beside this file for the fuller statement.

WHAT THIS IS NOT
  Not a strategy, not a signal generator, not a Phase-5 Observer component, and
  not in `14_PINE/`. `D-006` gates Pine Script and machine translation of rules
  behind the Master Spec (Phase 3) and Machine Spec (Phase 4), which do not
  exist. This is a drawing aid for a human, and it sits under
  `06_MANUAL_BACKTEST/tools/` for the same reason the Pine files do. If you find
  yourself adding an entry condition to it, stop.

E06 — NO PRICE IS EVER READ FROM A RENDERING
  `COMMON_PROTOCOL.md` §2, restated by `D-036a`: a chart may be LOOKED AT;
  nothing may be MEASURED OFF one. This script writes pixels and reads none. Any
  number that reaches a result comes from the checksummed CSV, via a committed
  script — never off one of these images. That rule is the reason this tool can
  exist at all without weakening anything.

DATA PROVENANCE — READ BEFORE TRUSTING A BOUNDARY
  Input is the DERIVED M15 / H1 corpus in
  `../datasets/HISTDATA_GBPUSD_M15_H1/`, aggregated from the `D-036a` HistData
  M1 bars by `../scripts/aggregate_m15.py`.

  HISTDATA PUBLISHES NO NATIVE M15 OR H1. Its own FAQ: "We can only deliver you
  time ordered Tick and M1 (1 minute) data." So these bucket boundaries are
  OURS. They are internally cross-checked (`crosscheck_htf.py`, seven checks,
  all passing) and they are NOT validated against any independent vendor,
  because no free comparison feed is in evidence. See that dataset's
  `VENDOR_TIMEFRAME_AVAILABILITY.md`.

D-031 — THE CLOCK IS A TESTED VARIABLE, NOT A SETTING
  Arm A = fixed UTC-5, no DST (the corpus's native stamp).
  Arm B = America/New_York, DST-tracking.
  `A-019` — the course states a session table and NO TIMEZONE — is still OPEN.
  Every rendered image is stamped with its arm, because a session box drawn on
  an unstated clock is a claim nobody can check.

  Measured, at M15 and H1 (`CROSSCHECK_REPORT.txt`, X5): the two arms produce
  BAR-FOR-BAR IDENTICAL candles and differ only in the label on each bar. So the
  arm cannot change a candle's shape at these timeframes — it changes only which
  SESSION a candle falls in. That makes the session boxes, not the price, the
  thing the arm choice actually moves.

usage:
  python3 mmm_chart_render.py --data FILE --timeframe {M15,H1} --arm {A,B} \
        --start 2015-03-02 [--window 2d] [--out DIR] [--no-boxes] [--no-tdi]
  python3 mmm_chart_render.py --data FILE --timeframe M15 --arm A \
        --batch 2015-03-02,2015-06-15,2015-08-24        # many windows at once
"""
import argparse
import os
import sys
from datetime import datetime, timedelta

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import FuncFormatter

# =============================================================================
# SECTION 1 — EMAs
# =============================================================================
#
# PERIODS
#   5 / 13 / 50 / 200   [TIER 2]  MMM-NOTES p.38: "The specific EMA's used in
#       Mauro's charts are the 5, 13, 50 and 200 bar EMA's." Roles on the same
#       page: 5 and 13 are the signal lines, 50 is the balance line, 200 is the
#       home base.
#   800                 [TIER 1]  V09 [00:41:43]: "This is the blueberry. The
#       blueberry is the 800 on the 15 minute time frame." The 15-MINUTE
#       TIMEFRAME IS PART OF THE DEFINITION — on the H1 charts this tool also
#       renders, the 800 is being drawn on a timeframe no source puts it on.
#       That is flagged on the image itself, not silently allowed.
#   ⚠ C-010: MMM-NOTES enumerates 5/13/50/200 and contains ZERO occurrences of
#       800 across 84 pages. Tier 1 outranks Tier 2 so the 800 stands, but the
#       two sources genuinely disagree about the SIZE OF THE SET. Unresolved.
#
# COLOURS — ALL FIVE ARE [OWNER-ATTESTED], D-043. NOT OBSERVED ON-SCREEN.
#   D-043 (2026-08-13) is the owner's FINAL mapping and it REVERSED D-041's
#   nickname<->period and D-042 §2's period<->colour. Both reversed; their
#   composition, nickname<->colour, did not change.
#
#       5    "mustard"      YELLOW   [OWNER-ATTESTED] + [TIER 1] on the COLOUR
#       13   "ketchup"      RED      [OWNER-ATTESTED] only
#       50   "water"        AQUA     [OWNER-ATTESTED] + [TOOLING]
#       200  "mayonnaise"   WHITE    [OWNER-ATTESTED] + [TOOLING]
#       800  "blueberry"    BLUE     [OWNER-ATTESTED] + [TOOLING]
#
#   Cite as "OWNER-ATTESTED (D-043), not observed on-screen." No frame in
#   04_SCREENSHOTS/ carries a legend and no speaker in V01-V11 names a colour
#   and a NICKNAME in one sentence. The ONE exception is the 5's COLOUR:
#   V07 [00:25:34] "this yellow one is a five moving average" joins yellow to
#   the 5 directly — that cell alone is additionally [TIER 1]. It does NOT
#   extend to the nickname: "mustard = 5" still needs a chain no speaker makes.
#   [TOOLING] = the owner's MT4 template 3M-shadow-boxes-15M.tpl (50 aqua,
#   200 white, 800 blue), a NEW evidence class scoped to PARAMETERS ONLY.
#
#   NICKNAMES are deliberately NOT used as plot labels. Only "blueberry = 800"
#   has a Tier 1 period (V09). Labelling the 200 "Mayo" would invent the
#   mapping A-020 records as still open.
EMA_SPEC = [
    # (period, colour, label, warrant summary printed in the legend)
    (5,   "#FFFF00", "EMA 5",   "OWNER-ATTESTED D-043 + TIER 1 colour"),
    (13,  "#FF0000", "EMA 13",  "OWNER-ATTESTED D-043"),
    (50,  "#00FFFF", "EMA 50",  "OWNER-ATTESTED D-043 + TOOLING"),
    (200, "#FFFFFF", "EMA 200", "OWNER-ATTESTED D-043 + TOOLING"),
    (800, "#0000FF", "EMA 800", "OWNER-ATTESTED D-043 + TOOLING"),
]

# =============================================================================
# SECTION 2 — TDI
# =============================================================================
#
# ⚠ THE COMMISSIONING BRIEF FOR THIS SCRIPT DESCRIBED THESE AS "Tier 3 defaults
#   only". THAT IS OUT OF DATE and porting it forward unchanged would have
#   understated what is known. `MMM_TDI.txt` was rewritten on 2026-08-13: four
#   of the five numbers are now [TOOLING], recovered from the owner's actual MT4
#   artifacts, and the headline change was RSI_Period 13 -> 21. The Tier-3
#   internet default this project previously shipped was WRONG on the single
#   most consequential number in the indicator, and everything drawn with RSI 13
#   was a different oscillator. The current tags are carried below verbatim.
#
# THE ARTIFACTS (owner's machine, ~/Desktop/Trading/Indicators/)
#   `Ultimate Blue.tpl` block `name=!SM_TDI`, and `MM4XSF_TDI.ex4` (CompassFX,
#   2011; internal name "mm4x-tdi"), whose parameter list is identical to the
#   template's. Verbatim:
#       RSI_Period=21   RSI_Price=0 (PRICE_CLOSE)   Volatility_Band=34
#       RSI_Price_Line=2   RSI_Price_Type=0 (SMA)
#       Trade_Signal_Line=7   Trade_Signal_Type=0 (SMA)
#       SharkFin_Upper_Level=63   SharkFin_Lower_Level=37
#       levels: 68 / 63 / 50 / 37 / 32
#
# ⚠ STILL NOT RECOVERED — THE STANDARD-DEVIATION MULTIPLE. The MT4 indicator
#   exposes no input for it, so it is compiled into the binary and the template
#   cannot reveal it. `BAND_MULT` below is STILL the Tier-3 public 1.6185 and is
#   STILL A GUESS. Four of the five numbers that shape this oscillator are
#   sourced; this one is not, and the bands on every image below are drawn with
#   a number nobody has verified.
#
# ⚠ `A-039` IS STILL OPEN AND STILL `DO NOT CODE` (D-030).
#   An MT4 template on the owner's disk is neither Tier 1 (the recordings) nor
#   Tier 2 (the Mauro PDF). It is an evidence class with no tier and no
#   admitting decision — the Mauro PDF itself needed `D-039` before it could
#   close anything. Provenance is weaker than it looks: the artifacts are dated
#   2015-2019, the bootcamp was recorded in 2012, and nothing in them proves a
#   setting is the instructor's rather than a later user's.
#   CONSEQUENCE: this panel may not be used to close `A-039`, `A-031` ("blood in
#   the water") or `A-032` ("shark fin"), and no backtest depending on these
#   numbers may be reported as a test of the method. What has changed is only
#   that the numbers trace to an artifact instead of to a forum post.
RSI_LEN    = 21      # [TOOLING] !SM_TDI RSI_Period=21 — NOT the Tier-3 13
FAST_LEN   = 2       # [TOOLING] RSI_Price_Line=2,   RSI_Price_Type=0 (SMA)
SLOW_LEN   = 7       # [TOOLING] Trade_Signal_Line=7, Trade_Signal_Type=0 (SMA)
BAND_LEN   = 34      # [TOOLING] Volatility_Band=34
BAND_MULT  = 1.6185  # [DEFAULT] ⚠ STILL A GUESS — not exposed by the MT4 indicator
TDI_LEVELS = (68, 50, 32)          # [TOOLING] template levels
SHARK      = (63, 37)              # [TOOLING] SharkFin_Upper/Lower_Level — A-032 OPEN

# TDI line colours [TOOLING], decoded from the template's MT4 BGR integers.
# ⚠ The buffer->line mapping is INFERRED: the template does not name its
# buffers, and buffers 1 and 3 share a colour and weight so they read as the two
# bands, leaving 2/4/5 for the price line, base line and signal line. Sensible,
# not proven.
COL_FAST  = "#B0C4DE"   # LightSteelBlue — RSI Price Line
COL_SLOW  = "#B22222"   # FireBrick      — Trade Signal Line
COL_BASE  = "#6A6AC8"   # MidnightBlue, lightened for legibility on a dark ground
COL_BANDS = "#1E90FF"   # DodgerBlue     — Volatility Bands
COL_SHARK = "#FF9800"

# =============================================================================
# SECTION 3 — SESSION BOXES  (A-019 OPEN / D-031)
# =============================================================================
#
# THE SESSION TABLE — [TIER 1], V02 slide [00:45:55], transcribed verbatim at
# 03_LESSON_NOTES/V02_SOURCE_NOTES.md §4b:
#       5pm High / Low Reset (The MM Spread Is Set)
#       5pm to 8pm Dead Gap
#       Asian Session:    8:30pm - 3:00am    Gap 3-3:30a
#       London Session:   3:30am - 9:00am    Gap 9-9:30a
#       New York Session: 9:30-5pm
# The times are Tier 1. THE TIMEZONE THEY ARE READ IN IS `A-019`, STILL OPEN —
# the instructor declines to specify (V02 [00:49:52] "Listen, don't analyse it…
# These are the times") and the man who taught him has died (V02 [00:49:22]).
# The `--arm` flag is how both D-031 arms actually get run. Run both.
#
# THE BOX CONCEPT — [TIER 2] MMM-NOTES p.40: two boxes, one around the Asian
# session ("the area of consolidation… It is just a guide"), one smaller box at
# "the beginning of the NY open… for about 3 hours" (the New York Reversal).
#
# ⚠ "PRIME BOX" IS NOT A TERM FROM ANY SOURCE IN THIS REPOSITORY. It occurs ZERO
#   times in 03_LESSON_NOTES/ and ZERO times in MMM-NOTES. It came with a build
#   request. The NY prime box maps onto a REAL documented object (p.40's second
#   box) so only its NAME is unsourced; the LONDON prime box has no source at
#   all and is defaulted OFF, exactly as in MMM_Indicator.txt.
#
# `slot` stacks the on-chart label so a NESTED box does not print on top of its
# parent. NY prime opens at the same 09:30 as the NY session it nests inside, and
# London prime at the same 03:30 as London, so without this the two labels land on
# the same pixel and neither is readable. Parents take slot 0, nested boxes drop.
SESSIONS = [
    # (key, label, start "HH:MM", end "HH:MM", face, edge, default_on, slot, tag)
    ("gap",   "DEAD GAP",           "17:00", "20:00", "#9E9E9E", "#9E9E9E", True, 0,
     "TIER 1 — same V02 slide"),
    ("asia",  "ASIAN RANGE",        "20:30", "03:00", "#FFEB3B", "#FFEB3B", True, 0,
     "TIER 1 times"),
    ("lon",   "LONDON",             "03:30", "09:00", "#4CAF50", "#4CAF50", True, 0,
     "TIER 1 times"),
    ("ny",    "NEW YORK",           "09:30", "17:00", "#2196F3", "#2196F3", True, 0,
     "TIER 1 times"),
    ("nyp",   "NY PRIME/REVERSAL",  "09:30", "12:30", "#FF5722", "#FF5722", True, 1,
     "TIER 2 window · the NAME 'prime' is DEFAULT"),
    ("lonp",  "LONDON PRIME",       "03:30", "07:30", "#00BCD4", "#00BCD4", False, 1,
     "⚠ DEFAULT — NO SOURCE DEFINES A LONDON SUB-BOX"),
]

# Window presets. LEGIBILITY IS THE CONSTRAINT, NOT BAR COUNT — this was raised
# explicitly with the owner. A window that crams a month of M15 into 1800px
# produces candles two pixels wide, which is not a chart a human can read a
# shape off, and reading shapes is the entire purpose. These defaults keep a
# candle at roughly 6-14px of body width at the default figure size.
WINDOW_PRESETS = {
    "M15": {"default": "2d",  "sane_max_bars": 400},   # 2 days ~ 192 bars
    "H1":  {"default": "7d",  "sane_max_bars": 400},   # 1 week ~ 120 bars
}

BG      = "#131722"
GRID    = "#2A2E39"
FG      = "#D1D4DC"
UP      = "#26A69A"
DOWN    = "#EF5350"


# ---------------------------------------------------------------------------
# Indicator maths — ported to match Pine's semantics, not merely to be "an EMA"
# ---------------------------------------------------------------------------
def ema(x, length):
    """Pine `ta.ema`: SMA seed over the first `length` values, then alpha=2/(n+1).

    The seed matters. A naive recursive EMA started from x[0] converges to the
    same series eventually, but "eventually" for the 800 is hundreds of bars,
    and every one of those bars would be drawn wrong. See `warmup_bars` below.
    """
    out = np.full(len(x), np.nan)
    if len(x) < length:
        return out
    a = 2.0 / (length + 1.0)
    out[length - 1] = x[:length].mean()
    for i in range(length, len(x)):
        out[i] = a * x[i] + (1 - a) * out[i - 1]
    return out


def rma(x, length):
    """Wilder's smoothing — what Pine's `ta.rsi` uses internally. NOT an SMA."""
    out = np.full(len(x), np.nan)
    if len(x) < length:
        return out
    a = 1.0 / length
    out[length - 1] = x[:length].mean()
    for i in range(length, len(x)):
        out[i] = a * x[i] + (1 - a) * out[i - 1]
    return out


def rsi(x, length):
    """Pine `ta.rsi`: RMA of gains / RMA of losses."""
    d = np.diff(x, prepend=x[0])
    up = rma(np.where(d > 0, d, 0.0), length)
    dn = rma(np.where(d < 0, -d, 0.0), length)
    with np.errstate(divide="ignore", invalid="ignore"):
        rs = np.where(dn == 0, np.inf, up / dn)
    return np.where(np.isnan(up), np.nan, 100.0 - 100.0 / (1.0 + rs))


def sma(x, length):
    out = np.full(len(x), np.nan)
    if len(x) < length:
        return out
    csum = np.nancumsum(np.nan_to_num(x))
    out[length - 1:] = (csum[length - 1:] - np.concatenate(([0.0], csum[:-length]))) / length
    out[: length - 1] = np.nan
    # any window containing a NaN must stay NaN
    isn = np.isnan(x).astype(float)
    bad = np.convolve(isn, np.ones(length), mode="full")[length - 1: len(x) + length - 1]
    out[bad > 0] = np.nan
    return out


def stdev(x, length):
    """Pine `ta.stdev` is POPULATION stdev (biased=true by default). Divisor n, not n-1."""
    out = np.full(len(x), np.nan)
    for i in range(length - 1, len(x)):
        w = x[i - length + 1: i + 1]
        if np.isnan(w).any():
            continue
        out[i] = w.std(ddof=0)
    return out


def warmup_bars():
    """How much history must precede the window for every plotted series to be valid.

    THE SINGLE EASIEST WAY TO SHIP A WRONG CHART is to load only the requested
    window and compute an 800 EMA on it: the line appears, it looks like an EMA,
    and it is meaningless. `ema()` returns NaN until the seed exists and then
    needs several time-constants before the seed stops dominating. 5x the longest
    period is generous and costs nothing — the whole corpus is 86k rows.
    """
    longest = max(max(p for p, *_ in EMA_SPEC), RSI_LEN + BAND_LEN, RSI_LEN + SLOW_LEN)
    return longest * 5


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
def load_bars(path):
    ts, o, h, l, c = [], [], [], [], []
    with open(path) as fh:
        for line in fh:
            p = line.strip().split(",")
            if len(p) != 7:
                continue
            ts.append(datetime.strptime(p[0] + " " + p[1], "%Y.%m.%d %H:%M"))
            o.append(float(p[2])); h.append(float(p[3]))
            l.append(float(p[4])); c.append(float(p[5]))
    order = np.argsort(np.array(ts))
    ts = [ts[i] for i in order]
    return (ts, np.array(o)[order], np.array(h)[order],
            np.array(l)[order], np.array(c)[order])


def parse_window(spec):
    unit = spec[-1].lower()
    n = float(spec[:-1])
    if unit == "d":
        return timedelta(days=n)
    if unit == "w":
        return timedelta(weeks=n)
    if unit == "h":
        return timedelta(hours=n)
    raise ValueError(f"window '{spec}': use Nd, Nw or Nh")


def hhmm(s):
    hh, mm = s.split(":")
    return int(hh) * 60 + int(mm)


def in_session(ts, start, end):
    """Clock-window membership, wrap-around aware (the Asian box crosses midnight)."""
    m = ts.hour * 60 + ts.minute
    a, b = hhmm(start), hhmm(end)
    return (a <= m < b) if a < b else (m >= a or m < b)


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
def render(bars, i0, i1, args, out_path):
    """Draw [i0, i1) of the loaded series. Indicators are computed on the FULL series."""
    ts, o, h, l, c = bars
    n = i1 - i0
    x = np.arange(n)
    wts = ts[i0:i1]

    emas = {p: ema(c, p)[i0:i1] for p, *_ in EMA_SPEC}

    r = rsi(c, RSI_LEN)
    base = sma(r, BAND_LEN)
    dev = BAND_MULT * stdev(r, BAND_LEN)
    tdi = {
        "fast": sma(r, FAST_LEN)[i0:i1],
        "slow": sma(r, SLOW_LEN)[i0:i1],
        "base": base[i0:i1],
        "up":   (base + dev)[i0:i1],
        "dn":   (base - dev)[i0:i1],
    }

    show_tdi = not args.no_tdi
    heights = [3.2, 1.15] if show_tdi else [3.2]
    fig, axes = plt.subplots(
        len(heights), 1, figsize=(args.width / 100.0, args.height / 100.0),
        dpi=args.dpi, gridspec_kw={"height_ratios": heights, "hspace": 0.06},
        squeeze=False)
    axes = [a[0] for a in axes]
    ax = axes[0]
    fig.patch.set_facecolor(BG)

    for a in axes:
        a.set_facecolor(BG)
        a.grid(True, color=GRID, linewidth=0.5, alpha=0.6)
        a.tick_params(colors=FG, labelsize=8)
        for s in a.spines.values():
            s.set_color(GRID)

    # --- session boxes, drawn UNDER the candles -----------------------------
    drawn_sessions = []
    if not args.no_boxes:
        enabled = {k for k, _lb, _s, _e, _f, _ed, on, _sl, _t in SESSIONS if on}
        if args.london_prime:
            enabled.add("lonp")
        for key, label, start, end, face, edge, _on, slot, _tag in SESSIONS:
            if key not in enabled:
                continue
            # contiguous runs of in-session bars become one box each
            mask = np.array([in_session(t, start, end) for t in wts])
            if not mask.any():
                continue
            drawn_sessions.append(label)
            j = 0
            while j < n:
                if not mask[j]:
                    j += 1
                    continue
                k = j
                while k + 1 < n and mask[k + 1]:
                    k += 1
                hi = h[i0 + j:i0 + k + 1].max()
                lo = l[i0 + j:i0 + k + 1].min()
                ax.add_patch(Rectangle(
                    (j - 0.5, lo), (k - j + 1), hi - lo,
                    facecolor=face, alpha=0.07, edgecolor=edge, linewidth=0.8, zorder=1))
                if k - j >= 3:
                    # offset in POINTS, so nested boxes stack cleanly regardless of
                    # the window's price scale
                    ax.annotate(label, (j - 0.3, hi), textcoords="offset points",
                                xytext=(0, 2 - slot * 9), color=edge, fontsize=6.5,
                                va="bottom", ha="left", alpha=0.9, zorder=6)
                j = k + 1

        # The 5pm High/Low Reset — [TIER 1], the SAME 17:00 boundary as the dead
        # gap's left edge, so the two cannot drift apart.
        for j, t in enumerate(wts):
            if t.hour == 17 and t.minute == 0:
                ax.axvline(j - 0.5, color="#FFFFFF", alpha=0.30,
                           linestyle=":", linewidth=1.0, zorder=2)

    # --- candles ------------------------------------------------------------
    body_w = 0.62
    for j in range(n):
        col = UP if c[i0 + j] >= o[i0 + j] else DOWN
        ax.vlines(j, l[i0 + j], h[i0 + j], color=col, linewidth=0.8, zorder=3)
        lo_b, hi_b = sorted((o[i0 + j], c[i0 + j]))
        ax.add_patch(Rectangle((j - body_w / 2, lo_b), body_w,
                               max(hi_b - lo_b, 1e-6),
                               facecolor=col, edgecolor=col, linewidth=0.5, zorder=4))

    # --- EMAs ---------------------------------------------------------------
    for period, colour, label, _warrant in EMA_SPEC:
        if period in args.hide_ema:
            continue
        ax.plot(x, emas[period], color=colour, linewidth=1.1,
                label=f"{label}", zorder=5)

    ax.set_xlim(-1, n)
    ax.yaxis.tick_right()
    ax.set_ylabel("")
    leg = ax.legend(loc="upper left", fontsize=7, framealpha=0.25,
                    facecolor=BG, edgecolor=GRID, ncol=5)
    for t in leg.get_texts():
        t.set_color(FG)

    # --- TDI panel ----------------------------------------------------------
    if show_tdi:
        tax = axes[1]
        tax.fill_between(x, tdi["dn"], tdi["up"], color=COL_BANDS, alpha=0.08, zorder=1)
        tax.plot(x, tdi["up"], color=COL_BANDS, linewidth=0.8, zorder=2)
        tax.plot(x, tdi["dn"], color=COL_BANDS, linewidth=0.8, zorder=2)
        tax.plot(x, tdi["base"], color=COL_BASE, linewidth=1.4,
                 label="Market Base Line", zorder=3)
        tax.plot(x, tdi["fast"], color=COL_FAST, linewidth=1.4,
                 label=f"Fast MA ({FAST_LEN})", zorder=4)
        tax.plot(x, tdi["slow"], color=COL_SLOW, linewidth=1.4,
                 label=f"Slow MA ({SLOW_LEN})", zorder=4)
        for lv in TDI_LEVELS:
            tax.axhline(lv, color="#808080", linewidth=0.6,
                        alpha=0.6 if lv == 50 else 0.35)
        for lv in SHARK:
            tax.axhline(lv, color=COL_SHARK, linewidth=0.6, alpha=0.45,
                        linestyle="--")
        tax.set_ylim(0, 100)
        tax.set_xlim(-1, n)
        tax.yaxis.tick_right()
        tleg = tax.legend(loc="upper left", fontsize=6.5, framealpha=0.25,
                          facecolor=BG, edgecolor=GRID, ncol=3)
        for t in tleg.get_texts():
            t.set_color(FG)
        tax.text(0.995, 0.04,
                 f"TDI  RSI {RSI_LEN} · fast {FAST_LEN} · slow {SLOW_LEN} · "
                 f"band {BAND_LEN} @ {BAND_MULT} — [TOOLING] except the ×{BAND_MULT} "
                 f"multiple, which is [DEFAULT] and STILL A GUESS.  A-039 OPEN.",
                 transform=tax.transAxes, ha="right", va="bottom",
                 color="#FFA726", fontsize=6.0, alpha=0.95)
        ax.set_xticklabels([])

    # --- x axis: positional, so weekends and holidays do not open dead space -
    bottom = axes[-1]
    step = max(1, n // 12)
    ticks = list(range(0, n, step))
    bottom.set_xticks(ticks)
    bottom.set_xticklabels([wts[t].strftime("%a %d %b\n%H:%M") for t in ticks],
                           fontsize=7, color=FG)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, p: ""))

    # --- titles and the provenance strip that travels with every image ------
    arm_txt = ("Arm A — fixed UTC−5, no DST (corpus native)" if args.arm == "A"
               else "Arm B — America/New_York, DST-tracking")
    ax.set_title(
        f"GBP/USD  {args.timeframe}   {wts[0]:%Y-%m-%d %H:%M} → {wts[-1]:%Y-%m-%d %H:%M}"
        f"   ({n} bars)\nD-031 {arm_txt}   ·   A-019 OPEN: the course states the session"
        f" times and NO timezone",
        color=FG, fontsize=10, loc="left", pad=10)

    notes = [
        "VISUAL STUDY AID — NOT A BACKTEST. Makes no prediction, so nothing is "
        "pre-registered; produces no evidence, so nothing here may be cited as a finding.",
        "EMA colours: OWNER-ATTESTED (D-043), NOT observed on-screen. Only the 5's "
        "colour is corroborated on tape (V07 [00:25:34]); only the 800's period is "
        "Tier 1 (V09 [00:41:43]).",
        "E06: a chart may be LOOKED AT; nothing may be MEASURED OFF one. Every number "
        "comes from the checksummed CSV.",
        "Bars DERIVED from the D-036a HistData M1 corpus — HistData publishes no native "
        f"{args.timeframe}. Bucket boundaries are ours, cross-checked internally, "
        "unvalidated against any outside feed.",
    ]
    if args.timeframe == "H1":
        notes.insert(1,
                     "⚠ The 800 EMA is defined by V09 ON THE 15-MINUTE TIMEFRAME. On this "
                     "H1 chart it is drawn on a timeframe no source places it on.")
    if args.hole_warning:
        notes.insert(0, "⚠ " + args.hole_warning)

    fig.text(0.008, 0.010, "\n".join(notes), color="#8A8F98", fontsize=6.0,
             va="bottom", ha="left", linespacing=1.5)
    fig.subplots_adjust(left=0.035, right=0.935, top=0.90,
                        bottom=0.055 + 0.0135 * len(notes))
    fig.savefig(out_path, facecolor=BG)
    plt.close(fig)
    return n, drawn_sessions


# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description="Render MMM study charts (EMAs + TDI + session boxes) from M15/H1 bars.")
    ap.add_argument("--data", required=True, help="derived GBPUSD_{M15,H1}_ARM{A,B}.csv")
    ap.add_argument("--timeframe", required=True, choices=["M15", "H1"])
    ap.add_argument("--arm", required=True, choices=["A", "B"],
                    help="D-031 arm the FILE is stamped in. Run both. Report both.")
    ap.add_argument("--start", help="window start, YYYY-MM-DD or YYYY-MM-DDTHH:MM")
    ap.add_argument("--batch", help="comma-separated list of start dates")
    ap.add_argument("--window", default=None, help="Nd / Nw / Nh (default per timeframe)")
    ap.add_argument("--out", default="renders", help="output directory")
    ap.add_argument("--label", default="", help="suffix appended to the filename")
    ap.add_argument("--no-boxes", action="store_true", help="suppress session boxes")
    ap.add_argument("--no-tdi", action="store_true", help="suppress the TDI panel")
    ap.add_argument("--london-prime", action="store_true",
                    help="⚠ enable the LONDON PRIME box — NO SOURCE DEFINES IT (DEFAULT, off)")
    ap.add_argument("--hide-ema", default="", help="comma-separated periods to hide")
    ap.add_argument("--width", type=int, default=1800)
    ap.add_argument("--height", type=int, default=1150)
    ap.add_argument("--dpi", type=int, default=110)
    args = ap.parse_args()

    args.hide_ema = {int(v) for v in args.hide_ema.split(",") if v.strip()}
    args.hole_warning = None
    if not args.start and not args.batch:
        ap.error("give --start or --batch")

    window = parse_window(args.window or WINDOW_PRESETS[args.timeframe]["default"])
    bars = load_bars(args.data)
    ts = bars[0]
    os.makedirs(args.out, exist_ok=True)
    warm = warmup_bars()

    starts = [args.start] if args.start else [s.strip() for s in args.batch.split(",")]
    written = []
    for s in starts:
        t0 = datetime.fromisoformat(s)
        t1 = t0 + window
        idx = [i for i, t in enumerate(ts) if t0 <= t < t1]
        if not idx:
            print(f"  {s}: NO BARS in [{t0}, {t1}) — skipped", file=sys.stderr)
            continue
        i0, i1 = idx[0], idx[-1] + 1

        # LEGIBILITY GUARD — the constraint the owner flagged as the important one.
        cap = WINDOW_PRESETS[args.timeframe]["sane_max_bars"]
        if i1 - i0 > cap:
            print(f"  {s}: {i1-i0} bars exceeds the legibility cap of {cap} for "
                  f"{args.timeframe}. Rendering anyway; candles will be thin. Shorten "
                  f"--window if you want to read shapes off this.", file=sys.stderr)

        # A KNOWN HOLE INSIDE A WINDOW MUST BE NAMED ON THE IMAGE, never left to
        # look like a quiet market. D-036a records exactly one (2014-06-01/02).
        hole_lo = datetime(2014, 6, 1, 17, 0) + (timedelta(hours=1) if args.arm == "B" else timedelta())
        hole_hi = datetime(2014, 6, 2, 15, 1) + (timedelta(hours=1) if args.arm == "B" else timedelta())
        args.hole_warning = None
        if t0 < hole_hi and hole_lo < t1:
            args.hole_warning = (
                "THIS WINDOW SPANS THE DOCUMENTED 2014-06-01/02 CORPUS HOLE "
                "(~22 trading hours absent, D-036a). The flat stretch is MISSING DATA, "
                "not a quiet market.")

        if i0 < warm:
            print(f"  {s}: only {i0} bars of history precede this window; the 800 EMA "
                  f"needs ~{warm} to be trustworthy. Long EMAs may be absent or wrong.",
                  file=sys.stderr)

        name = (f"GBPUSD_{args.timeframe}_ARM{args.arm}_{t0:%Y%m%d_%H%M}"
                f"{'_' + args.label if args.label else ''}.png")
        path = os.path.join(args.out, name)
        n, sess = render(bars, i0, i1, args, path)
        written.append((path, n, ts[i0], ts[i1 - 1]))
        print(f"  {path}  —  {n} bars  {ts[i0]} → {ts[i1-1]}"
              f"{'  [HOLE SPANNED]' if args.hole_warning else ''}")

    print(f"\n{len(written)} image(s) written to {args.out}/")
    print("These images are STUDY MATERIAL. They are not evidence, they close no")
    print("ambiguity, and no number may be measured off them (E06).")
    return 0 if written else 1


if __name__ == "__main__":
    sys.exit(main())
