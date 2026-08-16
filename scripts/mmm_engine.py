#!/usr/bin/env python3
"""
scripts/mmm_engine.py — Deterministic Feature Extraction Engine for MMM
======================================================================
Computes all mathematical and temporal indicators for the Market Maker Method:
- Session Windows & Clocks (EST/EDT)
- Asian Accumulation Box (<=50 pips filter)
- Upper & Lower Trading Zones (+25/+50 pips)
- Blue Tracer Lines (Prior Day 5:00 PM EST High & Low)
- 5, 13, 50, 200, 800 EMAs & 5/13 Crossover Detector
- Traders Dynamic Index (TDI): RSI 21, TSL 7, MBL 34, VB 2.0 SD off MBL
- 14-Day Average Daily Range (ADR) & Realized Daily Range
- Structured JSON Metadata Exporter
"""

import os
import json
import math
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Tuple

class MMMBar:
    __slots__ = ('dt', 'open', 'high', 'low', 'close', 'volume')
    def __init__(self, dt: datetime, open_: float, high: float, low: float, close: float, volume: int = 0):
        self.dt = dt
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def to_dict(self) -> Dict[str, Any]:
        return {
            'datetime': self.dt.strftime('%Y-%m-%d %H:%M:%S'),
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume
        }


class MMMEngine:
    def __init__(self, pip_size: float = 0.0001):
        self.pip_size = pip_size

    def load_csv(self, file_path: str) -> List[MMMBar]:
        """Loads HistData formatted CSV (YYYY.MM.DD,HH:MM,Open,High,Low,Close,Vol)."""
        bars = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) < 6:
                    continue
                try:
                    # e.g. 2013.01.01,17:00 or 2013-01-01,17:00
                    date_str = parts[0].replace('.', '-')
                    time_str = parts[1]
                    dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
                    o = float(parts[2])
                    h = float(parts[3])
                    l = float(parts[4])
                    c = float(parts[5])
                    v = int(parts[6]) if len(parts) > 6 else 0
                    bars.append(MMMBar(dt, o, h, l, c, v))
                except Exception:
                    continue
        bars.sort(key=lambda b: b.dt)
        return bars

    def compute_ema(self, prices: List[float], period: int) -> List[Optional[float]]:
        """Computes exponential moving average with SMA seed."""
        n = len(prices)
        ema = [None] * n
        if n < period:
            return ema
        
        # SMA seed
        sma = sum(prices[:period]) / period
        ema[period - 1] = sma
        k = 2.0 / (period + 1.0)
        
        for i in range(period, n):
            prev = ema[i - 1]
            ema[i] = (prices[i] * k) + (prev * (1.0 - k))
        return ema

    def compute_rsi(self, prices: List[float], period: int = 21) -> List[Optional[float]]:
        """Computes standard Wilder's RSI."""
        n = len(prices)
        rsi = [None] * n
        if n <= period:
            return rsi

        gains = [0.0] * n
        losses = [0.0] * n
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                gains[i] = diff
            else:
                losses[i] = -diff

        avg_gain = sum(gains[1:period + 1]) / period
        avg_loss = sum(losses[1:period + 1]) / period

        if avg_loss == 0:
            rsi[period] = 100.0
        else:
            rs = avg_gain / avg_loss
            rsi[period] = 100.0 - (100.0 / (1.0 + rs))

        for i in range(period + 1, n):
            avg_gain = (avg_gain * (period - 1) + gains[i]) / period
            avg_loss = (avg_loss * (period - 1) + losses[i]) / period
            if avg_loss == 0:
                rsi[i] = 100.0
            else:
                rs = avg_gain / avg_loss
                rsi[i] = 100.0 - (100.0 / (1.0 + rs))
        return rsi

    def compute_sma(self, values: List[Optional[float]], period: int) -> List[Optional[float]]:
        """Computes simple moving average over a series that may contain None."""
        n = len(values)
        sma = [None] * n
        for i in range(n):
            if i + 1 < period:
                continue
            window = values[i - period + 1 : i + 1]
            if any(v is None for v in window):
                continue
            sma[i] = sum(window) / period
        return sma

    def compute_tdi(self, closes: List[float]) -> Dict[str, List[Optional[float]]]:
        """
        Computes Canonical TDI series (D-065 basis):
        - RSI Price Line (Green): SMA(RSI(21), 2)
        - Trade Signal Line / TSL (Red): SMA(RSI Price Line, 7)
        - Market Baseline / MBL (Yellow): SMA(RSI Price Line, 34)
        - Volatility Bands (Blue): MBL +- 2.0 * StDev(RSI Price Line, 34)
        """
        rsi_raw = self.compute_rsi(closes, period=21)
        pl = self.compute_sma(rsi_raw, period=2)
        tsl = self.compute_sma(pl, period=7)
        mbl = self.compute_sma(pl, period=34)

        n = len(closes)
        vb_upper = [None] * n
        vb_lower = [None] * n

        for i in range(n):
            if i + 1 < 34 or mbl[i] is None:
                continue
            window = pl[i - 33 : i + 1]
            if any(v is None for v in window):
                continue
            mean = mbl[i]
            variance = sum((v - mean) ** 2 for v in window) / 34.0
            stdev = math.sqrt(variance)
            vb_upper[i] = mean + (2.0 * stdev)
            vb_lower[i] = mean - (2.0 * stdev)

        return {
            'rsi_price_line': pl,
            'trade_signal_line': tsl,
            'market_baseline': mbl,
            'volatility_band_high': vb_upper,
            'volatility_band_low': vb_lower
        }

    def compute_adr(self, bars: List[MMMBar], lookback_days: int = 14) -> Dict[datetime, float]:
        """Computes 14-day SMA of Daily Range (5:00 PM EST to 5:00 PM EST daily cycles)."""
        # Group bars into 5pm-5pm trading days
        days_data = {}
        for b in bars:
            # Shift by 7 hours so 17:00 EST belongs to the new trading day
            dt_shifted = b.dt + timedelta(hours=7)
            day_key = dt_shifted.date()
            if day_key not in days_data:
                days_data[day_key] = {'high': b.high, 'low': b.low}
            else:
                days_data[day_key]['high'] = max(days_data[day_key]['high'], b.high)
                days_data[day_key]['low'] = min(days_data[day_key]['low'], b.low)

        sorted_days = sorted(days_data.keys())
        adr_map = {}
        for i, d in enumerate(sorted_days):
            if i < lookback_days:
                # Approximate with available days if < 14
                prev_ranges = [(days_data[sorted_days[j]]['high'] - days_data[sorted_days[j]]['low']) / self.pip_size for j in range(i)]
                adr_map[d] = sum(prev_ranges) / len(prev_ranges) if prev_ranges else 100.0
            else:
                prev_ranges = [(days_data[sorted_days[j]]['high'] - days_data[sorted_days[j]]['low']) / self.pip_size for j in range(i - lookback_days, i)]
                adr_map[d] = sum(prev_ranges) / lookback_days
        return adr_map

    def get_session_type(self, dt: datetime) -> str:
        """Determines active session from NY Time (EST)."""
        hour = dt.hour
        minute = dt.minute
        time_dec = hour + (minute / 60.0)

        # 17:00 - 20:00 Dead Gap
        if 17.0 <= time_dec < 20.0:
            return "DEAD_GAP"
        # 20:00 - 01:00 Asian Box
        elif time_dec >= 20.0 or time_dec < 1.0:
            return "ASIAN"
        # 01:00 - 02:00 Pre-London
        elif 1.0 <= time_dec < 2.0:
            return "PRE_LONDON"
        # 02:00 - 05:00 London Stop Hunt & Zone Shift
        elif 2.0 <= time_dec < 5.0:
            return "LONDON_OPEN"
        # 05:00 - 08:30 London Mid
        elif 5.0 <= time_dec < 8.5:
            return "LONDON_MID"
        # 08:30 - 11:30 NY Open / Reversal
        elif 8.5 <= time_dec < 11.5:
            return "NY_OPEN"
        # 11:30 - 17:00 NY Mid / Close
        else:
            return "NY_MID"

    def extract_market_state(self, bars: List[MMMBar], target_idx: int) -> Dict[str, Any]:
        """
        Extracts comprehensive deterministic state vector for bar at target_idx.
        """
        if target_idx < 100 or target_idx >= len(bars):
            raise ValueError(f"target_idx {target_idx} out of range (need >=100 bars context).")

        curr_bar = bars[target_idx]
        closes = [b.close for b in bars[: target_idx + 1]]

        # EMAs
        ema5 = self.compute_ema(closes, 5)[-1]
        ema13 = self.compute_ema(closes, 13)[-1]
        ema50 = self.compute_ema(closes, 50)[-1]
        ema200 = self.compute_ema(closes, 200)[-1]
        ema800 = self.compute_ema(closes, 800)[-1]

        # 5/13 cross detection over last 10 bars
        ema5_series = self.compute_ema(closes, 5)
        ema13_series = self.compute_ema(closes, 13)
        last_cross_bars_ago = None
        cross_direction = "NONE"
        for k in range(1, min(20, len(ema5_series))):
            idx1 = -k
            idx0 = -k - 1
            if ema5_series[idx0] is not None and ema13_series[idx0] is not None and \
               ema5_series[idx1] is not None and ema13_series[idx1] is not None:
                # Bullish cross
                if ema5_series[idx0] <= ema13_series[idx0] and ema5_series[idx1] > ema13_series[idx1]:
                    last_cross_bars_ago = k - 1
                    cross_direction = "BULLISH"
                    break
                # Bearish cross
                elif ema5_series[idx0] >= ema13_series[idx0] and ema5_series[idx1] < ema13_series[idx1]:
                    last_cross_bars_ago = k - 1
                    cross_direction = "BEARISH"
                    break

        # TDI
        tdi_dict = self.compute_tdi(closes)
        pl = tdi_dict['rsi_price_line'][-1]
        tsl = tdi_dict['trade_signal_line'][-1]
        mbl = tdi_dict['market_baseline'][-1]
        vb_h = tdi_dict['volatility_band_high'][-1]
        vb_l = tdi_dict['volatility_band_low'][-1]

        # TDI event detection (Shark Fin & Blood in the Water over last 6 bars)
        shark_fin = False
        shark_fin_dir = "NONE"
        blood_in_water = False
        pl_series = tdi_dict['rsi_price_line']
        vb_h_series = tdi_dict['volatility_band_high']
        vb_l_series = tdi_dict['volatility_band_low']
        tsl_series = tdi_dict['trade_signal_line']

        for k in range(1, min(8, len(pl_series))):
            idx = -k
            if pl_series[idx] is not None and vb_h_series[idx] is not None:
                if pl_series[idx] >= vb_h_series[idx] and (pl is not None and pl < vb_h):
                    shark_fin = True
                    shark_fin_dir = "BEARISH_SHARK_FIN"
                    break
                elif pl_series[idx] <= vb_l_series[idx] and (pl is not None and pl > vb_l):
                    shark_fin = True
                    shark_fin_dir = "BULLISH_SHARK_FIN"
                    break

        if pl is not None and tsl is not None:
            if shark_fin_dir == "BEARISH_SHARK_FIN" and pl < tsl:
                blood_in_water = True
            elif shark_fin_dir == "BULLISH_SHARK_FIN" and pl > tsl:
                blood_in_water = True

        # Asian Box Calculation (find current or most recent Asian session 20:00 - 01:00 EST)
        asian_bars = []
        for i in range(target_idx, max(0, target_idx - 60), -1):
            b = bars[i]
            # Check if within 20:00 - 01:00
            hour = b.dt.hour
            if hour >= 20 or hour == 0:
                asian_bars.append(b)
            elif asian_bars:
                # Exited Asian box into prior session
                break

        if asian_bars:
            asian_high = max(b.high for b in asian_bars)
            asian_low = min(b.low for b in asian_bars)
            asian_range_pips = round((asian_high - asian_low) / self.pip_size, 1)
            asian_status = "VALID_ACCUMULATION" if asian_range_pips <= 50.0 else "BLOWN_ASIAN_BOX"
        else:
            asian_high = curr_bar.high
            asian_low = curr_bar.low
            asian_range_pips = 0.0
            asian_status = "UNKNOWN"

        # Trading Zones (+25/+50 pips)
        upper_zone_min = round(asian_high + (25.0 * self.pip_size), 5)
        upper_zone_max = round(asian_high + (50.0 * self.pip_size), 5)
        lower_zone_min = round(asian_low - (50.0 * self.pip_size), 5)
        lower_zone_max = round(asian_low - (25.0 * self.pip_size), 5)

        # Blue Tracer (Prior Day 5:00 PM EST High & Low)
        # Scan backward for prior trading day's 17:00 to 17:00 window
        dt_shifted = curr_bar.dt + timedelta(hours=7)
        curr_day = dt_shifted.date()
        prior_day_bars = []
        for i in range(target_idx, max(0, target_idx - 200), -1):
            b = bars[i]
            b_day = (b.dt + timedelta(hours=7)).date()
            if b_day < curr_day:
                if not prior_day_bars or b_day == (prior_day_bars[0].dt + timedelta(hours=7)).date():
                    prior_day_bars.append(b)
                else:
                    break

        if prior_day_bars:
            blue_tracer_high = round(max(b.high for b in prior_day_bars), 5)
            blue_tracer_low = round(min(b.low for b in prior_day_bars), 5)
        else:
            blue_tracer_high = curr_bar.high
            blue_tracer_low = curr_bar.low

        # ADR
        adr_map = self.compute_adr(bars[: target_idx + 1])
        adr_val = adr_map.get(curr_day, 100.0)

        # Today's realized high/low so far
        today_bars = [b for b in bars[max(0, target_idx - 40): target_idx + 1] if (b.dt + timedelta(hours=7)).date() == curr_day]
        today_high = max(b.high for b in today_bars) if today_bars else curr_bar.high
        today_low = min(b.low for b in today_bars) if today_bars else curr_bar.low
        today_range_pips = round((today_high - today_low) / self.pip_size, 1)
        adr_pct_used = round((today_range_pips / adr_val) * 100.0, 1) if adr_val > 0 else 0.0

        return {
            "metadata": {
                "symbol": "GBPUSD",
                "timestamp_ny_est": curr_bar.dt.strftime('%Y-%m-%d %H:%M:%S'),
                "day_of_week": curr_bar.dt.strftime('%A'),
                "active_session": self.get_session_type(curr_bar.dt)
            },
            "session_metrics": {
                "asian_box": {
                    "high": round(asian_high, 5),
                    "low": round(asian_low, 5),
                    "range_pips": asian_range_pips,
                    "status": asian_status
                },
                "trading_zone": {
                    "upper_hunt_zone_min": upper_zone_min,
                    "upper_hunt_zone_max": upper_zone_max,
                    "lower_hunt_zone_min": lower_zone_min,
                    "lower_hunt_zone_max": lower_zone_max
                },
                "blue_tracer": {
                    "prior_day_high": blue_tracer_high,
                    "prior_day_low": blue_tracer_low
                },
                "adr": {
                    "adr_14_pips": round(adr_val, 1),
                    "daily_range_so_far_pips": today_range_pips,
                    "adr_percentage_used": adr_pct_used
                }
            },
            "indicators": {
                "ema_values": {
                    "ema_5": round(ema5, 5) if ema5 else None,
                    "ema_13": round(ema13, 5) if ema13 else None,
                    "ema_50": round(ema50, 5) if ema50 else None,
                    "ema_200": round(ema200, 5) if ema200 else None,
                    "ema_800": round(ema800, 5) if ema800 else None
                },
                "ema_crosses": {
                    "5_13_last_cross_bars_ago": last_cross_bars_ago,
                    "5_13_cross_direction": cross_direction,
                    "price_vs_50_ema": "ABOVE" if (ema50 and curr_bar.close > ema50) else "BELOW",
                    "price_vs_200_ema": "ABOVE" if (ema200 and curr_bar.close > ema200) else "BELOW"
                },
                "tdi": {
                    "rsi_price_line": round(pl, 2) if pl else None,
                    "trade_signal_line": round(tsl, 2) if tsl else None,
                    "market_baseline": round(mbl, 2) if mbl else None,
                    "volatility_band_high": round(vb_h, 2) if vb_h else None,
                    "volatility_band_low": round(vb_l, 2) if vb_l else None,
                    "shark_fin_active": shark_fin,
                    "shark_fin_direction": shark_fin_dir,
                    "blood_in_water_active": blood_in_water
                }
            },
            "recent_price_action": {
                "current_price": round(curr_bar.close, 5),
                "session_high": round(today_high, 5),
                "session_low": round(today_low, 5),
                "vector_breakout_detected": (curr_bar.close > asian_high + (12 * self.pip_size)) or (curr_bar.close < asian_low - (12 * self.pip_size))
            }
        }


if __name__ == '__main__':
    print("MMMEngine module compiled successfully.")
