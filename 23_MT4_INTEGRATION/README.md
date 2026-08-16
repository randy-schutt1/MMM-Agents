# MetaTrader 4 (MT4) MCP Server & Custom Indicator Integration

A production-grade, zero-cost integration suite connecting **MetaTrader 4** to Python and AI agent frameworks (Claude Desktop, Antigravity, Open WebUI) using the **Model Context Protocol (MCP)**.

---

## 🌟 Key Features
- **Zero-Cost & 100% Open Source**: Built using pure Python and standard Windows Winsock (`ws2_32.dll`), requiring no paid third-party software.
- **Custom DLL Indicator Support**: Reads proprietary MQL4 and C++ DLL indicator buffers via `iCustom()` in real time.
- **Full MCP Tool Suite**: Exposes 8 structured tools for account details, candlestick rates, custom indicator buffers, and automated trade execution.
- **Real-Time MMM Intelligence Pipeline**: Automatically streams live M15 bars, extracts the complete Market Maker Method state vector, and auto-generates visual SVG charts.

---

## 🏗️ Architecture

```
 ┌──────────────────────────────────────────────┐
 │             MetaTrader 4 Terminal            │
 │                                              │
 │  ┌────────────────────────────────────────┐  │
 │  │      Your Custom DLL Indicators        │  │
 │  │   (TDI, Asian Box, EMA templates)      │  │
 │  └───────────────────┬────────────────────┘  │
 │                      │ (iCustom buffer read) │
 │  ┌───────────────────▼────────────────────┐  │
 │  │          MMM_MT4_Bridge.mq4            │  │
 │  │    (Non-blocking Winsock TCP Server)   │  │
 │  └───────────────────┬────────────────────┘  │
 └──────────────────────┼───────────────────────┘
                        │ Local TCP Socket (127.0.0.1:5555)
 ┌──────────────────────▼───────────────────────┐
 │               Python Intelligence            │
 │                                              │
 │  ┌────────────────────────────────────────┐  │
 │  │        scripts/mt4_client.py           │  │
 │  │   (Socket Client & MMMBar Deserializer)│  │
 │  └───────────────────┬────────────────────┘  │
 │                      │                       │
 │  ┌───────────────────┴────────────────────┐  │
 │  ▼                                        ▼  │
 │ ┌────────────────────────┐  ┌────────────────────────┐
 │ │scripts/mt4_mcp_server  │  │scripts/mt4_live_stream │
 │ │(MCP Tool Protocol)     │  │(Live MMM Intelligence) │
 │ └───────────┬────────────┘  └───────────┬────────────┘
 └─────────────┼───────────────────────────┼────────────┘
               ▼                           ▼
        Claude Desktop /            Live SVG Charts &
       AI Trading Agent             Trade Signals
```

---

## 🚀 Setup Instructions

### Step 1: Install MQL4 Bridge Files in MT4
1. Open your **MetaTrader 4** terminal.
2. Click **File** $\rightarrow$ **Open Data Folder**.
3. Copy [`23_MT4_INTEGRATION/MQL4/Include/json_parser.mqh`](file:///Users/randyschutt/Desktop/Trading/MMM-Agents/23_MT4_INTEGRATION/MQL4/Include/json_parser.mqh) into the `MQL4/Include/` directory.
4. Copy [`23_MT4_INTEGRATION/MQL4/Experts/MMM_MT4_Bridge.mq4`](file:///Users/randyschutt/Desktop/Trading/MMM-Agents/23_MT4_INTEGRATION/MQL4/Experts/MMM_MT4_Bridge.mq4) into the `MQL4/Experts/` directory.
5. Open **MetaEditor** (F4), open `MMM_MT4_Bridge.mq4`, and press **Compile** (F7).

### Step 2: Enable Algorithmic Trading in MT4
1. In MT4, go to **Tools** $\rightarrow$ **Options** $\rightarrow$ **Expert Advisors**.
2. Check:
   - ✅ **Allow automated trading**
   - ✅ **Allow DLL imports** (required for `ws2_32.dll` and your custom indicators)
3. Attach `MMM_MT4_Bridge` from the Navigator onto any open chart (e.g., GBPUSD M15).
4. Verify the Experts tab displays: `MMM_MT4_Bridge: Server listening on 127.0.0.1:5555`.

---

## 🤖 Configuring AI Assistants (Claude Desktop / Antigravity)

Add the server to your `claude_desktop_config.json`:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "metatrader4": {
      "command": "python3",
      "args": [
        "/Users/randyschutt/Desktop/Trading/MMM-Agents/scripts/mt4_mcp_server.py",
        "--host", "127.0.0.1",
        "--port", "5555"
      ]
    }
  }
}
```

---

## 🛠️ Available MCP Tools

| Tool Name | Parameters | Description |
|---|---|---|
| `mt4_get_account_info` | `{}` | Returns balance, equity, margin, free margin, leverage, currency. |
| `mt4_get_candlesticks` | `symbol`, `timeframe`, `count` | Fetches historical OHLC bars for any timeframe (M1=1, M5=5, M15=15, H1=60, D1=1440). |
| `mt4_get_custom_indicator` | `indicator_name`, `buffer_index`, `shift` | Reads exact numeric buffer value from any custom DLL or MQL4 indicator. |
| `mt4_get_open_positions` | `{}` | Lists all active open trade tickets with profit and SL/TP levels. |
| `mt4_open_order` | `symbol`, `order_type`, `volume`, `sl`, `tp` | Executes market BUY or SELL order with exact SL/TP parameters. |
| `mt4_modify_order` | `ticket`, `sl`, `tp` | Adjusts Stop Loss and Take Profit levels for an open trade. |
| `mt4_close_order` | `ticket` | Closes an open position by ticket number. |
| `mmm_analyze_live_chart` | `symbol`, `output_chart_path` | Pulls live bars, runs the complete MMM engine, generates SVG chart, and returns state vector. |

---

## 📊 Running Live Market Streamer (Shadow Mode)

To run the live candle-by-candle evaluation loop during London/NY trading sessions:

```bash
PYTHONPATH=. python3 scripts/mt4_live_stream.py --symbol GBPUSD --interval 10.0 --custom-ind "YourCustomTDI"
```

Console output prints live session state, Asian box metrics, TDI Shark Fin alerts, and prospective trade decisions on every bar close.
