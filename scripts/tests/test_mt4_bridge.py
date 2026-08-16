#!/usr/bin/env python3
"""
scripts/tests/test_mt4_bridge.py — Test Suite & Mock MT4 Bridge Verification
===========================================================================
Spins up an in-process Mock MT4 Server (via socketpair transport) and tests:
- Socket handshakes & PING latency
- Account info deserialization
- Candlestick rates fetching & MMMBar conversion
- Custom DLL indicator buffer querying (iCustom)
- Open order submission, modification, and closing
- MCP tool dispatching & schema validation
"""

import os
import sys
import time
import json
import socket
import threading
import unittest
from datetime import datetime

from scripts.mt4_client import MT4BridgeClient
from scripts.mt4_mcp_server import MT4MCPServer
from scripts.mmm_engine import MMMEngine


class MockMT4Handler:
    """Handles JSON requests in-memory matching MMM_MT4_Bridge.mq4."""

    @staticmethod
    def dispatch(req: dict) -> dict:
        action = req.get("action")
        if action == "PING":
            return {"status": "OK", "message": "PONG", "timestamp": int(time.time())}
        elif action == "GET_ACCOUNT":
            return {
                "status": "OK",
                "login": 123456,
                "currency": "USD",
                "balance": 10000.0,
                "equity": 10050.25,
                "margin": 150.0,
                "free_margin": 9900.25,
                "leverage": 100,
                "company": "Mock Broker Ltd",
                "server": "Demo-Server"
            }
        elif action == "GET_RATES":
            count = req.get("count", 10)
            rates = []
            base_p = 1.2500
            for i in range(count):
                rates.append({
                    "time": f"2026.08.15 12:{i:02d}",
                    "open": round(base_p + (i * 0.0002), 5),
                    "high": round(base_p + (i * 0.0002) + 0.0005, 5),
                    "low": round(base_p + (i * 0.0002) - 0.0003, 5),
                    "close": round(base_p + (i * 0.0002) + 0.0001, 5),
                    "volume": 150 + i
                })
            return {"status": "OK", "symbol": req.get("symbol", "GBPUSD"), "timeframe": req.get("timeframe", 15), "rates": rates}
        elif action == "GET_CUSTOM":
            return {
                "status": "OK",
                "symbol": req.get("symbol", "GBPUSD"),
                "timeframe": req.get("timeframe", 15),
                "indicator": req.get("indicator", "CustomTDI"),
                "buffer": req.get("buffer", 0),
                "shift": req.get("shift", 0),
                "value": 58.42
            }
        elif action == "GET_POSITIONS":
            return {
                "status": "OK",
                "positions": [
                    {
                        "ticket": 991122,
                        "symbol": "GBPUSD",
                        "type": "BUY",
                        "lots": 0.05,
                        "open_price": 1.25100,
                        "sl": 1.24900,
                        "tp": 1.25500,
                        "profit": 35.50,
                        "magic": 888111,
                        "comment": "MMM-Test"
                    }
                ]
            }
        elif action == "ORDER_SEND":
            return {
                "status": "OK",
                "ticket": 100200,
                "symbol": req.get("symbol", "GBPUSD"),
                "type": req.get("type", "BUY"),
                "price": 1.25200,
                "lots": req.get("volume", 0.01),
                "sl": req.get("sl", 0.0),
                "tp": req.get("tp", 0.0)
            }
        elif action == "ORDER_MODIFY":
            return {
                "status": "OK",
                "ticket": req.get("ticket"),
                "sl": req.get("sl"),
                "tp": req.get("tp")
            }
        elif action == "ORDER_CLOSE":
            return {
                "status": "OK",
                "ticket": req.get("ticket")
            }
        else:
            return {"status": "ERROR", "error": f"Unknown action {action}"}


class SocketPairBridgeServer:
    """Manages an in-process bridge using socketpair."""

    def __init__(self):
        self.server_sock, self.client_sock = socket.socketpair()
        self.running = True
        self.thread = threading.Thread(target=self._server_loop, daemon=True)
        self.thread.start()

    def _server_loop(self):
        buf = b""
        while self.running:
            try:
                data = self.server_sock.recv(4096)
                if not data:
                    break
                buf += data
                while b"\n" in buf:
                    line, buf = buf.split(b"\n", 1)
                    if not line:
                        continue
                    req = json.loads(line.decode('utf-8'))
                    resp = MockMT4Handler.dispatch(req)
                    self.server_sock.sendall(json.dumps(resp).encode('utf-8') + b"\n")
            except Exception:
                break

    def stop(self):
        self.running = False
        try:
            self.server_sock.close()
        except Exception:
            pass


class TestMT4Bridge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_server = SocketPairBridgeServer()
        cls.client = MT4BridgeClient(sock=cls.mock_server.client_sock)

    @classmethod
    def tearDownClass(cls):
        cls.client.close()
        cls.mock_server.stop()

    def test_01_ping(self):
        res = self.client.ping()
        self.assertEqual(res.get("status"), "OK")
        self.assertEqual(res.get("message"), "PONG")

    def test_02_get_account(self):
        acc = self.client.get_account_info()
        self.assertEqual(acc.get("status"), "OK")
        self.assertEqual(acc.get("balance"), 10000.0)
        self.assertEqual(acc.get("leverage"), 100)

    def test_03_get_candlesticks(self):
        bars = self.client.get_candlesticks("GBPUSD", timeframe=15, count=20)
        self.assertEqual(len(bars), 20)
        self.assertTrue(bars[0].high >= bars[0].low)
        self.assertEqual(bars[0].dt.year, 2026)

    def test_04_get_custom_indicator(self):
        val = self.client.get_custom_indicator("CustomTDI_DLL", buffer_idx=1, shift=0)
        self.assertEqual(val, 58.42)

    def test_05_orders(self):
        # Open
        order_res = self.client.open_order("GBPUSD", "BUY", volume=0.02, sl=1.2480, tp=1.2560)
        self.assertEqual(order_res.get("status"), "OK")
        ticket = order_res.get("ticket")
        self.assertGreater(ticket, 0)

        # Modify
        mod_res = self.client.modify_order(ticket, sl=1.2490, tp=1.2570)
        self.assertEqual(mod_res.get("status"), "OK")

        # Close
        close_res = self.client.close_order(ticket)
        self.assertEqual(close_res.get("status"), "OK")

    def test_06_mcp_server_tools(self):
        mcp = MT4MCPServer(client=self.client)
        tools = mcp.get_tool_definitions()
        self.assertTrue(len(tools) >= 7)

        # Test tool execution
        res_acc = mcp.execute_tool("mt4_get_account_info", {})
        self.assertEqual(res_acc.get("status"), "OK")

        res_bars = mcp.execute_tool("mt4_get_candlesticks", {"symbol": "GBPUSD", "count": 5})
        self.assertEqual(res_bars.get("status"), "OK")
        self.assertEqual(res_bars.get("count"), 5)

        res_ind = mcp.execute_tool("mt4_get_custom_indicator", {"indicator_name": "CustomTDI_DLL", "buffer_index": 0})
        self.assertEqual(res_ind.get("status"), "OK")
        self.assertEqual(res_ind.get("value"), 58.42)


if __name__ == '__main__':
    unittest.main()
