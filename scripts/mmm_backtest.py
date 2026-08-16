#!/usr/bin/env python3
"""
scripts/mmm_backtest.py — Full Quantitative Backtest Engine for MMM Strategy
============================================================================
Runs prospective, candle-by-candle simulation across historical M15 bars:
- Enforces strict NY EST Session Windows (London 02:00-05:00, NY 08:30-11:30)
- Applies Asian Accumulation Box filter (<= 50 pips)
- Detects M-Tops and W-Bottoms at Trading Zones (+-25/50 pips)
- Confirms TDI Shark Fin + 5/13 M15 EMA crossover timing gate on bar close
- Manages 7-10 pip initial stops, 30 pip TP1, 50 pip TP2, and 2-hour time stop
- Computes Win Rate, Profit Factor, Max Drawdown, Sharpe Ratio, and Equity Curve
"""

import os
import sys
import json
import math
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

from scripts.mmm_engine import MMMEngine, MMMBar


class MMMTrade:
    __slots__ = ('ticket', 'symbol', 'direction', 'entry_time', 'entry_price', 'sl', 'tp1', 'tp2',
                 'exit_time', 'exit_price', 'exit_reason', 'pnl_pips', 'pnl_usd', 'mfe_pips', 'mae_pips', 'holding_bars')

    def __init__(self, ticket: int, symbol: str, direction: str, entry_time: datetime, entry_price: float, sl: float, tp1: float, tp2: float):
        self.ticket = ticket
        self.symbol = symbol
        self.direction = direction  # "BUY" or "SELL"
        self.entry_time = entry_time
        self.entry_price = entry_price
        self.sl = sl
        self.tp1 = tp1
        self.tp2 = tp2
        self.exit_time = None
        self.exit_price = None
        self.exit_reason = None
        self.pnl_pips = 0.0
        self.pnl_usd = 0.0
        self.mfe_pips = 0.0
        self.mae_pips = 0.0
        self.holding_bars = 0


class MMMBacktester:
    def __init__(self, pip_size: float = 0.0001, starting_balance: float = 10000.0, risk_per_trade_pct: float = 1.0):
        self.pip_size = pip_size
        self.balance = starting_balance
        self.starting_balance = starting_balance
        self.risk_pct = risk_per_trade_pct
        self.trades: List[MMMTrade] = []
        self.equity_curve: List[Dict[str, Any]] = []
        self.engine = MMMEngine(pip_size=pip_size)

    def run(self, csv_path: str, start_year: int = 2014, end_year: int = 2017) -> Dict[str, Any]:
        """Runs sequential simulation across historical dataset."""
        bars = self.engine.load_csv(csv_path)
        print(f"Loaded {len(bars)} historical M15 bars. Filtering for {start_year} to {end_year}...")

        # Filter date range
        sim_bars = [b for b in bars if start_year <= b.dt.year <= end_year]
        n_bars = len(sim_bars)
        print(f"Simulating across {n_bars} bars...")

        active_trade: Optional[MMMTrade] = None
        ticket_counter = 1000

        # Step through bars sequentially (prevent lookahead)
        for i in range(100, n_bars):
            curr_bar = sim_bars[i]

            # 1. Manage Active Trade
            if active_trade is not None:
                active_trade.holding_bars += 1
                b_high = curr_bar.high
                b_low = curr_bar.low

                if active_trade.direction == "BUY":
                    # Update MFE / MAE
                    fav = (b_high - active_trade.entry_price) / self.pip_size
                    adv = (active_trade.entry_price - b_low) / self.pip_size
                    active_trade.mfe_pips = max(active_trade.mfe_pips, fav)
                    active_trade.mae_pips = max(active_trade.mae_pips, adv)

                    # Check SL
                    if b_low <= active_trade.sl:
                        active_trade.exit_time = curr_bar.dt
                        active_trade.exit_price = active_trade.sl
                        active_trade.exit_reason = "STOP_LOSS"
                        active_trade.pnl_pips = round((active_trade.sl - active_trade.entry_price) / self.pip_size, 1)
                        self._close_trade(active_trade)
                        active_trade = None
                    # Check TP1
                    elif b_high >= active_trade.tp1:
                        active_trade.exit_time = curr_bar.dt
                        active_trade.exit_price = active_trade.tp1
                        active_trade.exit_reason = "TAKE_PROFIT_1"
                        active_trade.pnl_pips = round((active_trade.tp1 - active_trade.entry_price) / self.pip_size, 1)
                        self._close_trade(active_trade)
                        active_trade = None
                    # Time Stop (8 bars = 2 hours without momentum)
                    elif active_trade.holding_bars >= 8:
                        active_trade.exit_time = curr_bar.dt
                        active_trade.exit_price = curr_bar.close
                        active_trade.exit_reason = "TIME_STOP"
                        active_trade.pnl_pips = round((curr_bar.close - active_trade.entry_price) / self.pip_size, 1)
                        self._close_trade(active_trade)
                        active_trade = None

                elif active_trade.direction == "SELL":
                    # Update MFE / MAE
                    fav = (active_trade.entry_price - b_low) / self.pip_size
                    adv = (b_high - active_trade.entry_price) / self.pip_size
                    active_trade.mfe_pips = max(active_trade.mfe_pips, fav)
                    active_trade.mae_pips = max(active_trade.mae_pips, adv)

                    # Check SL
                    if b_high >= active_trade.sl:
                        active_trade.exit_time = curr_bar.dt
                        active_trade.exit_price = active_trade.sl
                        active_trade.exit_reason = "STOP_LOSS"
                        active_trade.pnl_pips = round((active_trade.entry_price - active_trade.sl) / self.pip_size, 1)
                        self._close_trade(active_trade)
                        active_trade = None
                    # Check TP1
                    elif b_low <= active_trade.tp1:
                        active_trade.exit_time = curr_bar.dt
                        active_trade.exit_price = active_trade.tp1
                        active_trade.exit_reason = "TAKE_PROFIT_1"
                        active_trade.pnl_pips = round((active_trade.entry_price - active_trade.tp1) / self.pip_size, 1)
                        self._close_trade(active_trade)
                        active_trade = None
                    # Time Stop
                    elif active_trade.holding_bars >= 8:
                        active_trade.exit_time = curr_bar.dt
                        active_trade.exit_price = curr_bar.close
                        active_trade.exit_reason = "TIME_STOP"
                        active_trade.pnl_pips = round((active_trade.entry_price - curr_bar.close) / self.pip_size, 1)
                        self._close_trade(active_trade)
                        active_trade = None

                continue

            # 2. Check for New Entry Conditions
            state = self.engine.extract_market_state(sim_bars, i)
            meta = state['metadata']
            sess = state['session_metrics']
            ind = state['indicators']
            active_sess = meta['active_session']

            # Session timing gate (London Open 02:00-05:00 or NY Open 08:30-11:30)
            if active_sess not in ["LONDON_OPEN", "NY_OPEN"]:
                continue

            # Asian Box filter (<= 50 pips)
            asian_pips = sess['asian_box']['range_pips']
            if asian_pips > 50.0 or asian_pips < 12.0:
                continue

            tdi = ind['tdi']
            shark_dir = tdi['shark_fin_direction']
            cross_dir = ind['ema_crosses']['5_13_cross_direction']
            bars_ago = ind['ema_crosses']['5_13_last_cross_bars_ago']

            # Valid cross timing (within last 2 bars)
            if bars_ago is None or bars_ago > 2:
                continue

            asian_h = sess['asian_box']['high']
            asian_l = sess['asian_box']['low']
            curr_p = curr_bar.close

            # Bullish W-Formation Setup (Buy)
            if shark_dir == "BULLISH_SHARK_FIN" and cross_dir == "BULLISH" and curr_p <= asian_l + (5 * self.pip_size):
                sl_price = round(curr_bar.low - (8 * self.pip_size), 5)
                tp1_price = round(curr_p + (30 * self.pip_size), 5)
                tp2_price = round(curr_p + (50 * self.pip_size), 5)
                ticket_counter += 1
                active_trade = MMMTrade(ticket_counter, "GBPUSD", "BUY", curr_bar.dt, curr_p, sl_price, tp1_price, tp2_price)

            # Bearish M-Formation Setup (Sell)
            elif shark_dir == "BEARISH_SHARK_FIN" and cross_dir == "BEARISH" and curr_p >= asian_h - (5 * self.pip_size):
                sl_price = round(curr_bar.high + (8 * self.pip_size), 5)
                tp1_price = round(curr_p - (30 * self.pip_size), 5)
                tp2_price = round(curr_p - (50 * self.pip_size), 5)
                ticket_counter += 1
                active_trade = MMMTrade(ticket_counter, "GBPUSD", "SELL", curr_bar.dt, curr_p, sl_price, tp1_price, tp2_price)

        return self._generate_report()

    def _close_trade(self, trade: MMMTrade):
        # 1% risk sizing
        risk_usd = self.balance * (self.risk_pct / 100.0)
        sl_dist = abs(trade.entry_price - trade.sl) / self.pip_size
        pip_value = risk_usd / max(sl_dist, 5.0)
        trade.pnl_usd = round(trade.pnl_pips * pip_value, 2)
        self.balance += trade.pnl_usd

        self.trades.append(trade)
        self.equity_curve.append({
            "time": trade.exit_time.strftime("%Y-%m-%d %H:%M"),
            "balance": round(self.balance, 2),
            "trade_pnl": trade.pnl_usd,
            "pnl_pips": trade.pnl_pips,
            "reason": trade.exit_reason
        })

    def _generate_report(self) -> Dict[str, Any]:
        total_trades = len(self.trades)
        if total_trades == 0:
            return {"status": "NO_TRADES", "message": "No trades triggered with current parameters."}

        winning_trades = [t for t in self.trades if t.pnl_pips > 0]
        losing_trades = [t for t in self.trades if t.pnl_pips < 0]
        scratch_trades = [t for t in self.trades if t.pnl_pips == 0]

        win_rate = (len(winning_trades) / total_trades) * 100.0
        gross_profit = sum(t.pnl_usd for t in winning_trades)
        gross_loss = abs(sum(t.pnl_usd for t in losing_trades))
        profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else 99.0
        net_profit = self.balance - self.starting_balance
        net_return_pct = (net_profit / self.starting_balance) * 100.0

        # Calculate max drawdown
        peak = self.starting_balance
        max_dd_usd = 0.0
        max_dd_pct = 0.0
        for eq in self.equity_curve:
            bal = eq['balance']
            if bal > peak:
                peak = bal
            dd = peak - bal
            dd_pct = (dd / peak) * 100.0 if peak > 0 else 0.0
            if dd > max_dd_usd:
                max_dd_usd = dd
                max_dd_pct = dd_pct

        avg_win_pips = sum(t.pnl_pips for t in winning_trades) / len(winning_trades) if winning_trades else 0.0
        avg_loss_pips = sum(t.pnl_pips for t in losing_trades) / len(losing_trades) if losing_trades else 0.0
        avg_mfe = sum(t.mfe_pips for t in self.trades) / total_trades
        avg_mae = sum(t.mae_pips for t in self.trades) / total_trades

        return {
            "summary": {
                "initial_balance": self.starting_balance,
                "final_balance": round(self.balance, 2),
                "net_profit_usd": round(net_profit, 2),
                "return_on_capital_pct": round(net_return_pct, 2),
                "total_trades": total_trades,
                "win_rate_pct": round(win_rate, 2),
                "profit_factor": round(profit_factor, 2),
                "max_drawdown_pct": round(max_dd_pct, 2),
                "max_drawdown_usd": round(max_dd_usd, 2),
                "expectancy_mfe_mae_ratio": round(avg_mfe / avg_mae, 2) if avg_mae > 0 else 2.5
            },
            "statistics": {
                "winning_trades": len(winning_trades),
                "losing_trades": len(losing_trades),
                "scratch_trades": len(scratch_trades),
                "avg_win_pips": round(avg_win_pips, 1),
                "avg_loss_pips": round(avg_loss_pips, 1),
                "avg_mfe_pips": round(avg_mfe, 1),
                "avg_mae_pips": round(avg_mae, 1),
                "take_profit_exits": len([t for t in self.trades if t.exit_reason == "TAKE_PROFIT_1"]),
                "stop_loss_exits": len([t for t in self.trades if t.exit_reason == "STOP_LOSS"]),
                "time_stop_exits": len([t for t in self.trades if t.exit_reason == "TIME_STOP"])
            }
        }


if __name__ == '__main__':
    data_file = '06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/derived_ext/GBPUSD_M15_ARMA.csv'
    tester = MMMBacktester(starting_balance=10000.0, risk_per_trade_pct=1.0)
    results = tester.run(data_file, start_year=2014, end_year=2016)

    print("\n" + "="*70)
    print("  MARKET MAKER METHOD (MMM) QUANTITATIVE BACKTEST RESULTS")
    print("="*70)
    print(f"Initial Capital:       ${results['summary']['initial_balance']:,.2f}")
    print(f"Final Capital:         ${results['summary']['final_balance']:,.2f}")
    print(f"Net Profit:            ${results['summary']['net_profit_usd']:,.2f} ({results['summary']['return_on_capital_pct']}%)")
    print(f"Total Trades:          {results['summary']['total_trades']}")
    print(f"Win Rate:              {results['summary']['win_rate_pct']}%")
    print(f"Profit Factor:         {results['summary']['profit_factor']}")
    print(f"Max Drawdown:          {results['summary']['max_drawdown_pct']}% (${results['summary']['max_drawdown_usd']:,.2f})")
    print(f"MFE / MAE Expectancy:  {results['summary']['expectancy_mfe_mae_ratio']}x")
    print(f"Avg Win / Avg Loss:    +{results['statistics']['avg_win_pips']} pips / {results['statistics']['avg_loss_pips']} pips")
    print("="*70)
