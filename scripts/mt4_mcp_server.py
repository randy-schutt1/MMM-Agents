#!/usr/bin/env python3
"""
scripts/mt4_mcp_server.py — Model Context Protocol (MCP) Server for MetaTrader 4
================================================================================
Exposes MetaTrader 4 trading and analysis tools to AI Assistants via the
standard Model Context Protocol (JSON-RPC over STDIO):
- Market Data: Live candlesticks, ticks, and custom DLL indicator buffer values
- Account & Risk: Balance, equity, margin, active positions
- Intelligence Layer: Full MMM state extraction and AI setup analysis

READ-ONLY: order execution tools were removed per MASTER_A_PLAN Phase 0
(code safety). The AI agent cannot place, modify, or close orders via MCP.
"""

import os
import sys
import json
import argparse
from typing import Dict, Any, List, Optional

from scripts.mt4_client import MT4BridgeClient
from scripts.mmm_engine import MMMEngine
from scripts.mmm_chart_generator import render_mmm_chart


class MT4MCPServer:
    """Standard Model Context Protocol Server for MetaTrader 4."""

    def __init__(self, host: str = "127.0.0.1", port: int = 5555, client: Optional[MT4BridgeClient] = None):
        self.client = client or MT4BridgeClient(host=host, port=port)
        self.engine = MMMEngine()

    def get_tool_definitions(self) -> List[Dict[str, Any]]:
        """Returns MCP tool schema definitions."""
        return [
            {
                "name": "mt4_get_account_info",
                "description": "Get current MetaTrader 4 account details including balance, equity, free margin, and leverage.",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "mt4_get_candlesticks",
                "description": "Fetch OHLC candlestick bars from MetaTrader 4 for any symbol and timeframe.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string", "description": "Currency pair symbol (e.g. 'GBPUSD', 'EURUSD')", "default": "GBPUSD"},
                        "timeframe": {"type": "integer", "description": "Timeframe in minutes: 1=M1, 5=M5, 15=M15, 60=H1, 240=H4, 1440=D1", "default": 15},
                        "count": {"type": "integer", "description": "Number of bars to fetch", "default": 100}
                    },
                    "required": []
                }
            },
            {
                "name": "mt4_get_custom_indicator",
                "description": "Read buffer values from custom DLL indicators attached to MetaTrader 4 (e.g., custom TDI, Asian Box, EMA levels).",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "indicator_name": {"type": "string", "description": "Exact name of the custom indicator in MT4"},
                        "buffer_index": {"type": "integer", "description": "Buffer index (0 to 7) to read", "default": 0},
                        "shift": {"type": "integer", "description": "Bar shift index (0 = current live bar, 1 = last closed bar)", "default": 0},
                        "symbol": {"type": "string", "description": "Symbol", "default": "GBPUSD"},
                        "timeframe": {"type": "integer", "description": "Timeframe in minutes", "default": 15}
                    },
                    "required": ["indicator_name"]
                }
            },
            {
                "name": "mt4_get_open_positions",
                "description": "Get all active open positions and floating PnL in MetaTrader 4.",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            # SAFETY (MASTER_A_PLAN Phase 0): the mt4_open_order, mt4_modify_order,
            # and mt4_close_order tools have been removed so the AI agent cannot
            # place, modify, or close orders via MCP. Only read-only tools remain.
            # Do not re-add execution tools before Phase 8.
            {
                "name": "mmm_analyze_live_chart",
                "description": "Fetch live MT4 M15 bars, compute complete Market Maker Method metrics (Asian Box, Trading Zones, EMAs, TDI Shark Fin), and generate visual chart + state vector.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string", "description": "Symbol to analyze", "default": "GBPUSD"},
                        "output_chart_path": {"type": "string", "description": "File path to save the generated SVG chart", "default": "live_mmm_chart.svg"}
                    },
                    "required": []
                }
            }
        ]

    def execute_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Executes the requested tool action."""
        if name == "mt4_get_account_info":
            return self.client.get_account_info()

        elif name == "mt4_get_candlesticks":
            symbol = arguments.get("symbol", "GBPUSD")
            tf = arguments.get("timeframe", 15)
            count = arguments.get("count", 100)
            bars = self.client.get_candlesticks(symbol, tf, count)
            return {"status": "OK", "count": len(bars), "bars": [b.to_dict() for b in bars]}

        elif name == "mt4_get_custom_indicator":
            ind_name = arguments.get("indicator_name")
            buf = arguments.get("buffer_index", 0)
            shift = arguments.get("shift", 0)
            sym = arguments.get("symbol", "GBPUSD")
            tf = arguments.get("timeframe", 15)
            val = self.client.get_custom_indicator(ind_name, buf, shift, sym, tf)
            return {"status": "OK", "indicator": ind_name, "buffer": buf, "shift": shift, "value": val}

        elif name == "mt4_get_open_positions":
            positions = self.client.get_open_positions()
            return {"status": "OK", "count": len(positions), "positions": positions}

        # SAFETY (MASTER_A_PLAN Phase 0): order execution handlers
        # (mt4_open_order / mt4_modify_order / mt4_close_order) removed.
        elif name in ("mt4_open_order", "mt4_modify_order", "mt4_close_order"):
            return {
                "status": "ERROR",
                "error": "Order execution tools are disabled per MASTER_A_PLAN Phase 0 (safety). This MCP server is read-only."
            }

        elif name == "mmm_analyze_live_chart":
            sym = arguments.get("symbol", "GBPUSD")
            out_path = arguments.get("output_chart_path", "live_mmm_chart.svg")
            bars = self.client.get_candlesticks(sym, 15, count=250)
            if len(bars) < 50:
                return {"status": "ERROR", "error": f"Insufficient bars returned from MT4 ({len(bars)} bars)."}
            
            state = render_mmm_chart(bars, len(bars) - 1, self.engine, out_path, lookback_bars=192, title=f"Live MMM Chart — {sym} M15")
            return {
                "status": "OK",
                "symbol": sym,
                "chart_path": out_path,
                "state_vector": state
            }

        else:
            return {"status": "ERROR", "error": f"Unknown tool: {name}"}

    def run_stdio_server(self):
        """Standard MCP JSON-RPC Stdio Loop."""
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                req = json.loads(line)
                req_id = req.get("id")
                method = req.get("method")
                params = req.get("params", {})

                if method == "tools/list":
                    resp = {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": {"tools": self.get_tool_definitions()}
                    }
                elif method == "tools/call":
                    tool_name = params.get("name")
                    tool_args = params.get("arguments", {})
                    result = self.execute_tool(tool_name, tool_args)
                    resp = {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}
                    }
                elif method == "initialize":
                    resp = {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": {
                            "protocolVersion": "2024-11-05",
                            "capabilities": {"tools": {}},
                            "serverInfo": {"name": "metatrader4-mcp-server", "version": "1.0.0"}
                        }
                    }
                else:
                    resp = {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "error": {"code": -32601, "message": f"Method {method} not found"}
                    }

                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
            except Exception as e:
                err_resp = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32603, "message": str(e)}
                }
                sys.stdout.write(json.dumps(err_resp) + "\n")
                sys.stdout.flush()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="MetaTrader 4 MCP Server")
    parser.add_argument("--host", default="127.0.0.1", help="MT4 Bridge Host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5555, help="MT4 Bridge Port (default: 5555)")
    args = parser.parse_args()

    server = MT4MCPServer(host=args.host, port=args.port)
    server.run_stdio_server()
