#!/usr/bin/env python3
"""
scripts/mmm_chart_generator.py — Multi-Panel MMM Chart Generator for AI Vision
=============================================================================
Renders high-resolution, high-contrast chart representations designed specifically
for multimodal AI agent interpretation:
- M15 48-72 hour candle window with EMAs (5, 13, 50, 200, 800)
- Asian Accumulation Session Shading (08:00 PM - 01:00 AM EST)
- Trading Zones (+25/+50 pips Upper & Lower)
- Blue Tracer Lines (Prior Day 5:00 PM EST High & Low)
- Synchronized TDI Sub-Panel with RSI 21, TSL 7, MBL 34, and Volatility Bands
- HUD Metadata Overlay Box in the upper left corner
- Pure Python SVG Vector Engine (100% portable, publication-grade crispness)
"""

import os
import sys
import math
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

from scripts.mmm_engine import MMMEngine, MMMBar


def render_mmm_svg_chart(
    bars: List[MMMBar],
    target_idx: int,
    engine: MMMEngine,
    output_path: str,
    lookback_bars: int = 192,  # 48 hours of M15 bars
    title: str = "Market Maker Method M15 Chart"
) -> Dict[str, Any]:
    """
    Renders an ultra-crisp 1920x1080 SVG vector chart at target_idx and returns the deterministic market state.
    """
    start_idx = max(0, target_idx - lookback_bars + 1)
    window_bars = bars[start_idx : target_idx + 1]
    n_bars = len(window_bars)

    if n_bars < 30:
        raise ValueError(f"Not enough bars in window ({n_bars} bars).")

    # Extract state vector
    state = engine.extract_market_state(bars, target_idx)

    # Compute indicator series across full history up to target_idx
    all_closes = [b.close for b in bars[: target_idx + 1]]
    ema5_all = engine.compute_ema(all_closes, 5)
    ema13_all = engine.compute_ema(all_closes, 13)
    ema50_all = engine.compute_ema(all_closes, 50)
    ema200_all = engine.compute_ema(all_closes, 200)
    ema800_all = engine.compute_ema(all_closes, 800)
    tdi_all = engine.compute_tdi(all_closes)

    # Slice to window
    ema5 = ema5_all[start_idx : target_idx + 1]
    ema13 = ema13_all[start_idx : target_idx + 1]
    ema50 = ema50_all[start_idx : target_idx + 1]
    ema200 = ema200_all[start_idx : target_idx + 1]
    ema800 = ema800_all[start_idx : target_idx + 1]

    tdi_pl = tdi_all['rsi_price_line'][start_idx : target_idx + 1]
    tdi_tsl = tdi_all['trade_signal_line'][start_idx : target_idx + 1]
    tdi_mbl = tdi_all['market_baseline'][start_idx : target_idx + 1]
    tdi_vbh = tdi_all['volatility_band_high'][start_idx : target_idx + 1]
    tdi_vbl = tdi_all['volatility_band_low'][start_idx : target_idx + 1]

    # Layout Dimensions
    width = 1920
    height = 1080
    margin_left = 70
    margin_right = 90
    margin_top = 40
    margin_bottom = 50
    gap = 30

    chart_w = width - margin_left - margin_right
    main_h = int((height - margin_top - margin_bottom - gap) * 0.73)
    tdi_h = int((height - margin_top - margin_bottom - gap) * 0.27)
    tdi_top = margin_top + main_h + gap

    # Determine Price Y-Scale
    min_p = min(b.low for b in window_bars)
    max_p = max(b.high for b in window_bars)
    
    # Include EMAs and levels in price scaling if present
    valid_emas = [v for series in [ema5, ema13, ema50, ema200, ema800] for v in series if v is not None]
    if valid_emas:
        min_p = min(min_p, min(valid_emas))
        max_p = max(max_p, max(valid_emas))
    
    sess = state['session_metrics']
    min_p = min(min_p, sess['trading_zone']['lower_hunt_zone_max'], sess['blue_tracer']['prior_day_low'])
    max_p = max(max_p, sess['trading_zone']['upper_hunt_zone_min'], sess['blue_tracer']['prior_day_high'])

    p_padding = (max_p - min_p) * 0.08
    min_p -= p_padding
    max_p += p_padding

    def price_to_y(p: float) -> float:
        return margin_top + main_h - ((p - min_p) / (max_p - min_p) * main_h)

    def tdi_to_y(val: float) -> float:
        # TDI range 20 to 80
        clamped = max(18.0, min(82.0, val))
        return tdi_top + tdi_h - ((clamped - 20.0) / 60.0 * tdi_h)

    def idx_to_x(i: int) -> float:
        return margin_left + (i / max(1, n_bars - 1)) * chart_w

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    svg.append('<defs>')
    svg.append('<style>')
    svg.append('text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace; }')
    svg.append('.grid { stroke: #1e222d; stroke-width: 1; }')
    svg.append('.axis-txt { fill: #787b86; font-size: 11px; }')
    svg.append('.hud-txt { fill: #d1d4dc; font-size: 13px; font-family: monospace; font-weight: 500; }')
    svg.append('</style>')
    svg.append('</defs>')

    # Background
    svg.append(f'<rect width="{width}" height="{height}" fill="#131722"/>')
    svg.append(f'<rect x="{margin_left}" y="{margin_top}" width="{chart_w}" height="{main_h}" fill="#131722" stroke="#2a2e39" stroke-width="1"/>')
    svg.append(f'<rect x="{margin_left}" y="{tdi_top}" width="{chart_w}" height="{tdi_h}" fill="#131722" stroke="#2a2e39" stroke-width="1"/>')

    # Grid Lines
    for p_step in range(1, 8):
        y_val = margin_top + (main_h * p_step / 8)
        p_val = max_p - ((max_p - min_p) * p_step / 8)
        svg.append(f'<line x1="{margin_left}" y1="{y_val:.1f}" x2="{margin_left + chart_w}" y2="{y_val:.1f}" class="grid"/>')
        svg.append(f'<text x="{margin_left + chart_w + 8}" y="{y_val + 4:.1f}" class="axis-txt">{p_val:.5f}</text>')

    # Asian Box Shading
    asian_in_progress = False
    asian_start_i = 0
    asian_highs = []
    asian_lows = []

    for i, b in enumerate(window_bars):
        hour = b.dt.hour
        is_asian = (hour >= 20 or hour == 0)
        if is_asian:
            if not asian_in_progress:
                asian_in_progress = True
                asian_start_i = i
                asian_highs = [b.high]
                asian_lows = [b.low]
            else:
                asian_highs.append(b.high)
                asian_lows.append(b.low)
        else:
            if asian_in_progress:
                asian_in_progress = False
                x1 = idx_to_x(asian_start_i)
                x2 = idx_to_x(i - 1)
                y_box_h = price_to_y(max(asian_highs))
                y_box_l = price_to_y(min(asian_lows))
                box_w = max(4.0, x2 - x1)
                box_h_px = max(2.0, y_box_l - y_box_h)
                svg.append(f'<rect x="{x1:.1f}" y="{y_box_h:.1f}" width="{box_w:.1f}" height="{box_h_px:.1f}" fill="#2a2e39" fill-opacity="0.45" stroke="#787b86" stroke-dasharray="4,4"/>')

    if asian_in_progress:
        x1 = idx_to_x(asian_start_i)
        x2 = idx_to_x(n_bars - 1)
        y_box_h = price_to_y(max(asian_highs))
        y_box_l = price_to_y(min(asian_lows))
        box_w = max(4.0, x2 - x1)
        box_h_px = max(2.0, y_box_l - y_box_h)
        svg.append(f'<rect x="{x1:.1f}" y="{y_box_h:.1f}" width="{box_w:.1f}" height="{box_h_px:.1f}" fill="#2a2e39" fill-opacity="0.45" stroke="#787b86" stroke-dasharray="4,4"/>')

    # Horizontal Key Lines: Blue Tracer & Trading Zones
    bt_h_y = price_to_y(sess['blue_tracer']['prior_day_high'])
    bt_l_y = price_to_y(sess['blue_tracer']['prior_day_low'])
    svg.append(f'<line x1="{margin_left}" y1="{bt_h_y:.1f}" x2="{margin_left + chart_w}" y2="{bt_h_y:.1f}" stroke="#29b6f6" stroke-width="1.5" opacity="0.85"/>')
    svg.append(f'<line x1="{margin_left}" y1="{bt_l_y:.1f}" x2="{margin_left + chart_w}" y2="{bt_l_y:.1f}" stroke="#29b6f6" stroke-width="1.5" opacity="0.85"/>')
    svg.append(f'<text x="{margin_left + chart_w - 180}" y="{bt_h_y - 4:.1f}" fill="#29b6f6" font-size="10">Blue Tracer (High)</text>')

    tz = sess['trading_zone']
    for level_key in ['upper_hunt_zone_min', 'upper_hunt_zone_max', 'lower_hunt_zone_min', 'lower_hunt_zone_max']:
        val_y = price_to_y(tz[level_key])
        svg.append(f'<line x1="{margin_left}" y1="{val_y:.1f}" x2="{margin_left + chart_w}" y2="{val_y:.1f}" stroke="#ab47bc" stroke-width="1.2" stroke-dasharray="2,3" opacity="0.75"/>')

    # Draw Candlesticks
    candle_w_px = max(2.0, (chart_w / n_bars) * 0.65)
    for i, b in enumerate(window_bars):
        cx = idx_to_x(i)
        is_bull = b.close >= b.open
        color = '#089981' if is_bull else '#f23645'
        
        y_high = price_to_y(b.high)
        y_low = price_to_y(b.low)
        y_open = price_to_y(b.open)
        y_close = price_to_y(b.close)
        
        # Wick
        svg.append(f'<line x1="{cx:.1f}" y1="{y_high:.1f}" x2="{cx:.1f}" y2="{y_low:.1f}" stroke="{color}" stroke-width="1.2"/>')
        
        # Body
        body_top = min(y_open, y_close)
        body_h = max(1.5, abs(y_close - y_open))
        svg.append(f'<rect x="{cx - candle_w_px / 2.0:.1f}" y="{body_top:.1f}" width="{candle_w_px:.1f}" height="{body_h:.1f}" fill="{color}" stroke="{color}"/>')

    # Draw EMAs
    def render_polyline(series: List[Optional[float]], color: str, width: float):
        pts = []
        for i, v in enumerate(series):
            if v is not None:
                pts.append(f"{idx_to_x(i):.1f},{price_to_y(v):.1f}")
        if pts:
            svg.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{width}"/>')

    render_polyline(ema5, '#ffff00', 1.2)   # Mustard
    render_polyline(ema13, '#ff0000', 1.2)  # Ketchup
    render_polyline(ema50, '#00e5ff', 1.6)  # Water
    render_polyline(ema200, '#ffffff', 2.0) # Mayonnaise
    render_polyline(ema800, '#2962ff', 2.4) # Blueberry

    # Draw TDI Sub-Panel
    for t_lvl, col, style in [(68, '#f23645', '4,4'), (63, '#ffa726', '2,2'), (50, '#787b86', 'none'), (37, '#ffa726', '2,2'), (32, '#089981', '4,4')]:
        y_lvl = tdi_to_y(t_lvl)
        dash = f'stroke-dasharray="{style}"' if style != 'none' else ''
        svg.append(f'<line x1="{margin_left}" y1="{y_lvl:.1f}" x2="{margin_left + chart_w}" y2="{y_lvl:.1f}" stroke="{col}" stroke-width="1" opacity="0.6" {dash}/>')
        svg.append(f'<text x="{margin_left + chart_w + 8}" y="{y_lvl + 4:.1f}" class="axis-txt">{t_lvl}</text>')

    def render_tdi_polyline(series: List[Optional[float]], color: str, width: float):
        pts = []
        for i, v in enumerate(series):
            if v is not None:
                pts.append(f"{idx_to_x(i):.1f},{tdi_to_y(v):.1f}")
        if pts:
            svg.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{width}"/>')

    render_tdi_polyline(tdi_vbh, '#2962ff', 1.0)
    render_tdi_polyline(tdi_vbl, '#2962ff', 1.0)
    render_tdi_polyline(tdi_mbl, '#ffd600', 1.5)
    render_tdi_polyline(tdi_tsl, '#f23645', 1.4)
    render_tdi_polyline(tdi_pl, '#00e676', 1.8)

    # Time Axis Ticks
    step = max(1, n_bars // 10)
    for i in range(0, n_bars, step):
        x_pos = idx_to_x(i)
        t_label = window_bars[i].dt.strftime('%m/%d %H:%M')
        svg.append(f'<line x1="{x_pos:.1f}" y1="{tdi_top + tdi_h}" x2="{x_pos:.1f}" y2="{tdi_top + tdi_h + 6}" stroke="#787b86"/>')
        svg.append(f'<text x="{x_pos:.1f}" y="{tdi_top + tdi_h + 20}" class="axis-txt" text-anchor="middle">{t_label}</text>')

    # HUD Metadata Box (Top-Left)
    curr_time = state['metadata']['timestamp_ny_est']
    active_sess = state['metadata']['active_session']
    asian_box_pips = sess['asian_box']['range_pips']
    asian_box_stat = sess['asian_box']['status']
    adr_val = sess['adr']['adr_14_pips']
    adr_pct = sess['adr']['adr_percentage_used']
    last_cross = state['indicators']['ema_crosses']['5_13_cross_direction']
    bars_ago = state['indicators']['ema_crosses']['5_13_last_cross_bars_ago']
    cross_text = f"{last_cross} ({bars_ago} bars ago)" if bars_ago is not None else "NONE"
    shark_stat = state['indicators']['tdi']['shark_fin_direction']

    hud_lines = [
        f"SYMBOL: GBPUSD (M15)  |  NY TIME: {curr_time}",
        f"SESSION: {active_sess}  |  DAY: {state['metadata']['day_of_week']}",
        f"ASIAN RANGE: {asian_box_pips} pips [{asian_box_stat}]",
        f"ADR (14d): {adr_val} pips  |  USED TODAY: {adr_pct}%",
        f"5/13 EMA CROSS: {cross_text}",
        f"TDI SHARK FIN: {shark_stat}"
    ]

    hud_w = 480
    hud_h = 135
    svg.append(f'<rect x="{margin_left + 15}" y="{margin_top + 15}" width="{hud_w}" height="{hud_h}" fill="#1e222d" fill-opacity="0.92" stroke="#363a45" rx="6"/>')
    for idx, line in enumerate(hud_lines):
        svg.append(f'<text x="{margin_left + 28}" y="{margin_top + 38 + (idx * 18)}" class="hud-txt">{line}</text>')

    # Title & Legend
    svg.append(f'<text x="{margin_left + 15}" y="{margin_top - 12}" fill="#d1d4dc" font-size="16" font-weight="600">{title}</text>')

    svg.append('</svg>')

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(svg))

    return state


def render_mmm_chart(
    bars: List[MMMBar],
    target_idx: int,
    engine: MMMEngine,
    output_path: str,
    lookback_bars: int = 192,
    title: str = "Market Maker Method M15 Chart"
) -> Dict[str, Any]:
    """Universal chart renderer that outputs SVG format for maximum fidelity."""
    if not output_path.endswith('.svg'):
        output_path = os.path.splitext(output_path)[0] + '.svg'
    return render_mmm_svg_chart(bars, target_idx, engine, output_path, lookback_bars, title)


if __name__ == '__main__':
    print("MMMChartGenerator (SVG Vector Engine) compiled successfully.")
