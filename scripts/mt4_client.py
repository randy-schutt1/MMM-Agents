#!/usr/bin/env python3
"""
scripts/mt4_client.py — High-Performance Python Client for MetaTrader 4
======================================================================
Communicates with the MMM_MT4_Bridge.mq4 socket server on localhost:5555:
- Real-time OHLC candlestick streaming
- Custom DLL indicator buffer querying (iCustom)
- Account information & margin monitoring
- Automated order entry, modification, and closing
- Seamless integration with scripts/mmm_engine.py
"""

import os
import sys
import json
import socket
import time
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple

from scripts.mmm_engine import MMMBar, MMMEngine


class MT4BridgeClient:
    """Python client for communicating with MetaTrader 4 via local TCP socket."""

    def __init__(self, host: str = "127.0.0.1", port: int = 5555, timeout_sec: float = 3.0, sock: Optional[socket.socket] = None):
        self.host = host
        self.port = port
        self.timeout_sec = timeout_sec
        self.sock: Optional[socket.socket] = sock

    def connect(self) -> bool:
        """Establishes connection to MT4 bridge server."""
        if self.sock:
            return True
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(self.timeout_sec)
            self.sock.connect((self.host, self.port))
            return True
        except Exception as e:
            self.sock = None
            return False

    def is_connected(self) -> bool:
        """Checks if socket is active."""
        if not self.sock:
            return False
        try:
            res = self.ping()
            return res.get("status") == "OK"
        except Exception:
            return False

    def close(self):
        """Closes active socket connection."""
        if self.sock:
            try:
                self.sock.close()
            except Exception:
                pass
            self.sock = None

    def send_command(self, cmd: Dict[str, Any]) -> Dict[str, Any]:
        """Sends a JSON command line to MT4 and parses the JSON response."""
        if not self.sock:
            if not self.connect():
                return {"status": "ERROR", "error": "Not connected to MT4 Bridge"}

        try:
            payload = json.dumps(cmd).encode('utf-8') + b"\n"
            self.sock.sendall(payload)

            # Read response until newline
            chunks = []
            while True:
                chunk = self.sock.recv(16384)
                if not chunk:
                    raise ConnectionResetError("MT4 closed connection unexpectedly")
                chunks.append(chunk)
                if b"\n" in chunk:
                    break

            raw_resp = b"".join(chunks).decode('utf-8').strip()
            return json.loads(raw_resp)
        except Exception as e:
            self.close()
            return {"status": "ERROR", "error": f"Socket communication error: {str(e)}"}

    def ping(self) -> Dict[str, Any]:
        """Tests bridge latency and heartbeat."""
        return self.send_command({"action": "PING"})

    def get_account_info(self) -> Dict[str, Any]:
        """Fetches account balance, equity, leverage, and margin details."""
        return self.send_command({"action": "GET_ACCOUNT"})

    def get_candlesticks(self, symbol: str = "GBPUSD", timeframe: int = 15, count: int = 200) -> List[MMMBar]:
        """
        Fetches OHLC bars from MT4 and converts them into MMMBar instances.
        Timeframe mapping: 1=M1, 5=M5, 15=M15, 60=H1, 240=H4, 1440=D1.
        """
        cmd = {
            "action": "GET_RATES",
            "symbol": symbol,
            "timeframe": timeframe,
            "count": count
        }
        res = self.send_command(cmd)
        if res.get("status") != "OK":
            raise RuntimeError(f"MT4 error fetching rates: {res.get('error', 'Unknown')}")

        rates_data = res.get("rates", [])
        bars = []
        for r in rates_data:
            try:
                # Format: "YYYY.MM.DD HH:MM"
                dt_str = r['time'].replace('.', '-')
                dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
                bars.append(MMMBar(
                    dt=dt,
                    open_=float(r['open']),
                    high=float(r['high']),
                    low=float(r['low']),
                    close=float(r['close']),
                    volume=int(r.get('volume', 0))
                ))
            except Exception:
                continue
        return bars

    def get_custom_indicator(
        self,
        indicator_name: str,
        buffer_idx: int = 0,
        shift: int = 0,
        symbol: str = "GBPUSD",
        timeframe: int = 15
    ) -> float:
        """
        Queries any custom DLL indicator buffer via iCustom() in MT4.
        """
        cmd = {
            "action": "GET_CUSTOM",
            "symbol": symbol,
            "timeframe": timeframe,
            "indicator": indicator_name,
            "buffer": buffer_idx,
            "shift": shift
        }
        res = self.send_command(cmd)
        if res.get("status") != "OK":
            raise RuntimeError(f"MT4 error reading indicator {indicator_name}: {res.get('error', 'Unknown')}")
        return float(res.get("value", 0.0))

    def get_open_positions(self) -> List[Dict[str, Any]]:
        """Returns list of all active market trades."""
        res = self.send_command({"action": "GET_POSITIONS"})
        if res.get("status") != "OK":
            return []
        return res.get("positions", [])

    def open_order(
        self,
        symbol: str,
        order_type: str,  # "BUY" or "SELL"
        volume: float = 0.01,
        sl: Optional[float] = None,
        tp: Optional[float] = None,
        comment: str = "MMM-Agent",
        magic: int = 888111
    ) -> Dict[str, Any]:
        """Sends a market execution order to MT4."""
        cmd = {
            "action": "ORDER_SEND",
            "symbol": symbol,
            "type": order_type.upper(),
            "volume": volume,
            "sl": sl if sl is not None else 0.0,
            "tp": tp if tp is not None else 0.0,
            "comment": comment,
            "magic": magic
        }
        return self.send_command(cmd)

    def modify_order(self, ticket: int, sl: float, tp: float) -> Dict[str, Any]:
        """Modifies SL and TP for an open ticket."""
        cmd = {
            "action": "ORDER_MODIFY",
            "ticket": ticket,
            "sl": sl,
            "tp": tp
        }
        return self.send_command(cmd)

    def close_order(self, ticket: int) -> Dict[str, Any]:
        """Closes an open position by ticket number."""
        cmd = {
            "action": "ORDER_CLOSE",
            "ticket": ticket
        }
        return self.send_command(cmd)


if __name__ == '__main__':
    client = MT4BridgeClient()
    print(f"MT4 Client initialized for {client.host}:{client.port}")
