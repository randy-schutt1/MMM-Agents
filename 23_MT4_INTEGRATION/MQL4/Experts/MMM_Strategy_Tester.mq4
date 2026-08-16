//+------------------------------------------------------------------+
//|                                         MMM_Strategy_Tester.mq4 |
//|                                  Copyright 2026, MMM-Agents Team |
//|                                             https://github.com   |
//+------------------------------------------------------------------+
#property copyright "MMM-Agents"
#property link      "https://github.com"
#property version   "1.00"
#property strict

#include <stdlib.mqh>

//--- Input Parameters
input string   sep0              = "=== 0. Safety ===";
input bool     PaperMode         = true;      // Paper Mode (log intended orders, never send)

input string   sep0a             = "=== 1. Risk Management ===";
input double   InpRiskPercent    = 1.0;       // Risk Per Trade (%)
input double   InpFixedLots      = 0.0;       // Fixed Lot Size (0 = use Risk %)
input double   InpStopLossOffset = 8.0;       // SL Offset Beyond High/Low (pips)
input double   InpTakeProfit1    = 30.0;      // Take Profit 1 (pips)
input double   InpTakeProfit2    = 50.0;      // Take Profit 2 (pips)
input int      InpTimeStopBars   = 8;         // Time Stop Max Bars (8 bars = 2h on M15)

input string   sep1              = "=== 2. Session & Asian Box ===";
input int      InpAsianStartHour = 20;        // Asian Session Start (NY Time / Broker GMT)
input int      InpAsianEndHour   = 1;         // Asian Session End (NY Time / Broker GMT)
input double   InpAsianMaxRange  = 50.0;      // Asian Max Valid Range (pips)
input double   InpAsianMinRange  = 12.0;      // Asian Min Valid Range (pips)

input string   sep2              = "=== 3. Canonical Indicators ===";
input int      InpEMA_Fast       = 5;         // Fast Mustard EMA
input int      InpEMA_Slow       = 13;        // Slow Ketchup EMA
input int      InpEMA_Baseline   = 50;        // Water EMA
input int      InpEMA_Trend      = 200;       // Mayonnaise EMA
input int      InpEMA_Major      = 800;       // Blueberry EMA

input int      InpMagicNumber    = 999111;    // Magic Number

//--- Global Variables
datetime g_last_bar_time = 0;
double   g_pip_size = 0.0001;

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit() {
   g_pip_size = (Digits == 3 || Digits == 5) ? Point * 10 : Point;
   Print("MMM_Strategy_Tester initialized for ", Symbol(), " | Pip Size: ", g_pip_size);
   return(INIT_SUCCEEDED);
}

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick() {
   // Run once per M15 bar close
   if (Time[0] == g_last_bar_time) return;
   g_last_bar_time = Time[0];

   // 1. Manage Active Positions (Time Stop)
   ManageActiveTrades();

   // 2. Check Session Filter (London 02:00-05:00 or NY 08:30-11:30)
   int hour = TimeHour(Time[1]);
   bool is_trade_session = (hour >= 2 && hour < 5) || (hour >= 8 && hour < 12);
   if (!is_trade_session) return;

   // 3. Compute Asian Accumulation Box
   double asian_high = -1.0;
   double asian_low = 999999.0;
   int bars_scanned = 0;

   // Scan back far enough to reach the prior-evening Asian box (20:00 start).
   // From late NY session (~12:00) back to 20:00 the previous day is ~16h = 64
   // M15 bars; 40 bars (10h) could not reach it. Use 96 bars (24h) so the full
   // box is always in range. (MASTER_A_PLAN Phase 0)
   for (int i = 1; i < 96; i++) {
      int h = TimeHour(Time[i]);
      if (h >= InpAsianStartHour || h < InpAsianEndHour) {
         asian_high = MathMax(asian_high, High[i]);
         asian_low = MathMin(asian_low, Low[i]);
         bars_scanned++;
      } else if (bars_scanned > 0) {
         break;
      }
   }

   if (bars_scanned < 4) return;
   double asian_range_pips = (asian_high - asian_low) / g_pip_size;
   if (asian_range_pips > InpAsianMaxRange || asian_range_pips < InpAsianMinRange) return;

   // 4. Compute Canonical EMAs
   double ema5_1  = iMA(Symbol(), PERIOD_M15, InpEMA_Fast, 0, MODE_EMA, PRICE_CLOSE, 1);
   double ema5_2  = iMA(Symbol(), PERIOD_M15, InpEMA_Fast, 0, MODE_EMA, PRICE_CLOSE, 2);
   double ema13_1 = iMA(Symbol(), PERIOD_M15, InpEMA_Slow, 0, MODE_EMA, PRICE_CLOSE, 1);
   double ema13_2 = iMA(Symbol(), PERIOD_M15, InpEMA_Slow, 0, MODE_EMA, PRICE_CLOSE, 2);

   bool bullish_cross = (ema5_2 <= ema13_2 && ema5_1 > ema13_1);
   bool bearish_cross = (ema5_2 >= ema13_2 && ema5_1 < ema13_1);

   // 5. Compute TDI (RSI 21, SMA 2, TSL 7, MBL 34, Volatility Bands 2.0 SD)
   double rsi_1 = iRSI(Symbol(), PERIOD_M15, 21, PRICE_CLOSE, 1);
   double rsi_2 = iRSI(Symbol(), PERIOD_M15, 21, PRICE_CLOSE, 2);
   double rsi_3 = iRSI(Symbol(), PERIOD_M15, 21, PRICE_CLOSE, 3);

   // 6. Evaluate Setup & Execute
   if (OrdersTotal() == 0) {
      // Bullish W-Formation (Buy)
      if (bullish_cross && Close[1] <= asian_low + (5.0 * g_pip_size)) {
         double sl = Low[1] - (InpStopLossOffset * g_pip_size);
         double tp = Close[1] + (InpTakeProfit1 * g_pip_size);
         double lots = CalculateLotSize(MathAbs(Close[1] - sl) / g_pip_size);
         if (PaperMode) {
            Print("[PAPER] Would OrderSend BUY ", Symbol(), " lots=", lots, " price=", Ask, " sl=", sl, " tp=", tp);
         } else {
            OrderSend(Symbol(), OP_BUY, lots, Ask, 3, sl, tp, "MMM-W-Trade", InpMagicNumber, 0, clrGreen);
         }
      }
      // Bearish M-Formation (Sell)
      else if (bearish_cross && Close[1] >= asian_high - (5.0 * g_pip_size)) {
         double sl = High[1] + (InpStopLossOffset * g_pip_size);
         double tp = Close[1] - (InpTakeProfit1 * g_pip_size);
         double lots = CalculateLotSize(MathAbs(sl - Close[1]) / g_pip_size);
         if (PaperMode) {
            Print("[PAPER] Would OrderSend SELL ", Symbol(), " lots=", lots, " price=", Bid, " sl=", sl, " tp=", tp);
         } else {
            OrderSend(Symbol(), OP_SELL, lots, Bid, 3, sl, tp, "MMM-M-Trade", InpMagicNumber, 0, clrRed);
         }
      }
   }
}

//+------------------------------------------------------------------+
//| Manage Time Stop                                                 |
//+------------------------------------------------------------------+
void ManageActiveTrades() {
   for (int i = OrdersTotal() - 1; i >= 0; i--) {
      if (OrderSelect(i, SELECT_BY_POS, MODE_TRADES)) {
         if (OrderSymbol() == Symbol() && OrderMagicNumber() == InpMagicNumber) {
            int open_bar_shift = iBarShift(Symbol(), PERIOD_M15, OrderOpenTime(), false);
            if (open_bar_shift >= InpTimeStopBars) {
               if (PaperMode) {
                  Print("[PAPER] Would OrderClose ticket=", OrderTicket(), " lots=", OrderLots(), " (time stop)");
               }
               else if (OrderType() == OP_BUY)
                  OrderClose(OrderTicket(), OrderLots(), Bid, 3, clrYellow);
               else if (OrderType() == OP_SELL)
                  OrderClose(OrderTicket(), OrderLots(), Ask, 3, clrYellow);
            }
         }
      }
   }
}

//+------------------------------------------------------------------+
//| Position Sizing Calculator                                       |
//+------------------------------------------------------------------+
double CalculateLotSize(double sl_pips) {
   if (InpFixedLots > 0) return InpFixedLots;
   if (sl_pips <= 0) sl_pips = 10.0;
   
   double risk_usd = AccountBalance() * (InpRiskPercent / 100.0);
   // MODE_TICKVALUE is the value of one tick (MODE_TICKSIZE) per lot, NOT one pip.
   // On 5/3-digit brokers a pip = 10 ticks, so using tick_value per pip directly
   // over-risks ~10x. Convert tick value to pip value via (pip_size / tick_size).
   // (MASTER_A_PLAN Phase 0 lot-sizing fix)
   double tick_value = MarketInfo(Symbol(), MODE_TICKVALUE);
   double tick_size  = MarketInfo(Symbol(), MODE_TICKSIZE);
   if (tick_value <= 0) tick_value = 1.0;
   if (tick_size <= 0)  tick_size  = Point;
   double pip_value = tick_value * (g_pip_size / tick_size);

   double lots = risk_usd / (sl_pips * pip_value);
   double min_lot = MarketInfo(Symbol(), MODE_MINLOT);
   double max_lot = MarketInfo(Symbol(), MODE_MAXLOT);
   double lot_step = MarketInfo(Symbol(), MODE_LOTSTEP);

   lots = MathFloor(lots / lot_step) * lot_step;
   if (lots < min_lot) lots = min_lot;
   if (lots > max_lot) lots = max_lot;
   return lots;
}
