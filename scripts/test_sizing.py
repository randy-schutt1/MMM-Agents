#!/usr/bin/env python3
"""
scripts/test_sizing.py — Unit tests for the corrected lot-sizing formula
========================================================================
Pure-Python replication of CalculateLotSize() in
23_MT4_INTEGRATION/MQL4/Experts/MMM_Strategy_Tester.mq4 after the
MASTER_A_PLAN Phase 0 fix.

Bug fixed: MODE_TICKVALUE is the account-currency value of ONE TICK
(MODE_TICKSIZE) per lot, not one pip. On 5-digit (and 3-digit JPY)
brokers a pip = 10 ticks, so dividing risk by (sl_pips * tick_value)
over-risked ~10x. Corrected formula converts tick value to pip value:

    pip_value = tick_value * (pip_size / tick_size)
    lots      = risk_usd / (sl_pips * pip_value)
"""

import math
import unittest


def calculate_lot_size(
    sl_pips: float,
    balance: float,
    risk_percent: float,
    digits: int,
    point: float,
    tick_value: float,
    tick_size: float,
    min_lot: float = 0.01,
    max_lot: float = 100.0,
    lot_step: float = 0.01,
    fixed_lots: float = 0.0,
) -> float:
    """Mirror of the corrected MQL4 CalculateLotSize()."""
    if fixed_lots > 0:
        return fixed_lots
    if sl_pips <= 0:
        sl_pips = 10.0

    pip_size = point * 10 if digits in (3, 5) else point

    risk_usd = balance * (risk_percent / 100.0)
    if tick_value <= 0:
        tick_value = 1.0
    if tick_size <= 0:
        tick_size = point
    pip_value = tick_value * (pip_size / tick_size)

    lots = risk_usd / (sl_pips * pip_value)
    lots = math.floor(lots / lot_step) * lot_step
    if lots < min_lot:
        lots = min_lot
    if lots > max_lot:
        lots = max_lot
    return lots


def realized_risk(lots: float, sl_pips: float, digits: int, point: float,
                  tick_value: float, tick_size: float) -> float:
    """Account-currency loss if SL is hit at the given lot size."""
    pip_size = point * 10 if digits in (3, 5) else point
    pip_value_per_lot = tick_value * (pip_size / tick_size)
    return lots * sl_pips * pip_value_per_lot


class TestLotSizing(unittest.TestCase):

    def test_5_digit_gbpusd(self):
        """GBPUSD on a 5-digit broker: tick_size 0.00001, tick_value $1/tick/lot."""
        balance, risk_pct, sl_pips = 10000.0, 1.0, 20.0
        digits, point = 5, 0.00001
        tick_value, tick_size = 1.0, 0.00001  # $1 per point per standard lot

        lots = calculate_lot_size(sl_pips, balance, risk_pct, digits, point,
                                  tick_value, tick_size)
        intended = balance * risk_pct / 100.0  # $100
        actual = realized_risk(lots, sl_pips, digits, point, tick_value, tick_size)

        # pip_value = $10/lot -> exact lots = 100 / (20*10) = 0.50
        self.assertAlmostEqual(lots, 0.50, places=8)
        self.assertLessEqual(abs(actual - intended) / intended, 0.01,
                             f"5-digit risk off by >1%: intended={intended}, actual={actual}")

    def test_3_digit_jpy(self):
        """USDJPY-style 3-digit symbol: tick_size 0.001, tick_value per tick/lot."""
        balance, risk_pct, sl_pips = 10000.0, 1.0, 25.0
        digits, point = 3, 0.001
        # e.g. ~$0.68 per tick per lot at USDJPY ~147
        tick_value, tick_size = 0.68, 0.001

        lots = calculate_lot_size(sl_pips, balance, risk_pct, digits, point,
                                  tick_value, tick_size)
        intended = balance * risk_pct / 100.0  # $100
        actual = realized_risk(lots, sl_pips, digits, point, tick_value, tick_size)

        # pip_value = $6.80/lot -> exact lots = 100 / (25*6.8) = 0.588 -> floor 0.58
        self.assertAlmostEqual(lots, 0.58, places=8)
        self.assertLessEqual(abs(actual - intended) / intended, 0.02,
                             f"3-digit risk off tolerance (lot-step floor): intended={intended}, actual={actual}")
        # Never over-risk after flooring to lot step
        self.assertLessEqual(actual, intended * 1.0000001)

    def test_4_digit_broker(self):
        """4-digit broker: pip == point == tick, formula reduces to old one."""
        lots = calculate_lot_size(20.0, 10000.0, 1.0, digits=4, point=0.0001,
                                  tick_value=10.0, tick_size=0.0001)
        self.assertAlmostEqual(lots, 0.50, places=8)

    def test_old_formula_over_risked_10x(self):
        """Document the bug: old formula on 5-digit broker sized ~10x too large."""
        balance, risk_pct, sl_pips = 10000.0, 1.0, 20.0
        tick_value = 1.0  # per point on 5-digit broker
        old_lots = (balance * risk_pct / 100.0) / (sl_pips * tick_value)  # 5.0 lots
        new_lots = calculate_lot_size(sl_pips, balance, risk_pct, 5, 0.00001,
                                      tick_value, 0.00001)
        self.assertAlmostEqual(old_lots / new_lots, 10.0, places=6)

    def test_clamping(self):
        # min lot clamp
        lots = calculate_lot_size(500.0, 100.0, 0.1, 5, 0.00001, 1.0, 0.00001)
        self.assertEqual(lots, 0.01)
        # max lot clamp
        lots = calculate_lot_size(1.0, 10_000_000.0, 5.0, 5, 0.00001, 1.0, 0.00001)
        self.assertEqual(lots, 100.0)

    def test_fixed_lots_override(self):
        self.assertEqual(
            calculate_lot_size(20.0, 10000.0, 1.0, 5, 0.00001, 1.0, 0.00001,
                               fixed_lots=0.25),
            0.25)


if __name__ == "__main__":
    unittest.main(verbosity=2)
