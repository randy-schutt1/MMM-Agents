//+------------------------------------------------------------------+
//|                                               MMM_MT4_Bridge.mq4 |
//|                                  Copyright 2026, MMM-Agents Team |
//|                                             https://github.com   |
//+------------------------------------------------------------------+
#property copyright "MMM-Agents"
#property link      "https://github.com"
#property version   "1.00"
#property strict

#include <json_parser.mqh>
#include <stdlib.mqh>

//+------------------------------------------------------------------+
//| Windows Winsock 2.2 API Imports (ws2_32.dll)                     |
//+------------------------------------------------------------------+
#import "ws2_32.dll"
   int WSAStartup(int wVersionRequested, int& lpWSAData[]);
   int WSACleanup();
   int socket(int af, int type, int protocol);
   int bind(int s, int& name[], int namelen);
   int listen(int s, int backlog);
   int accept(int s, int& addr[], int& addrlen[]);
   int closesocket(int s);
   int recv(int s, uchar& buf[], int len, int flags);
   int send(int s, uchar& buf[], int len, int flags);
   int ioctlsocket(int s, int cmd, int& argp[]);
   int htons(int hostshort);
   int htonl(int hostlong);
#import

// Constants
#define AF_INET        2
#define SOCK_STREAM    1
#define IPPROTO_TCP    6
#define FIONBIO        -2147195266   // 0x8004667E in 32-bit signed int
#define INVALID_SOCKET -1
#define SOCKET_ERROR   -1

// Input Parameters
input int InpServerPort    = 5555;      // TCP Listening Port
input int InpTimerInterval = 100;       // Socket Polling Timer (ms)
input int InpMagicNumber   = 888111;    // Default EA Magic Number
input int InpSlippage      = 3;         // Max Slippage (points)
input bool PaperMode       = true;      // Paper Mode (log intended orders, never send) — MASTER_A_PLAN Phase 0

// Global Variables
int g_server_sock = INVALID_SOCKET;
int g_client_sock = INVALID_SOCKET;
bool g_wsa_initialized = false;

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit() {
   Print("MMM_MT4_Bridge: Initializing Winsock on port ", InpServerPort);
   
   int wsaData[100];
   int res = WSAStartup(0x0202, wsaData);
   if (res != 0) {
      Print("MMM_MT4_Bridge: WSAStartup failed with error ", res);
      return(INIT_FAILED);
   }
   g_wsa_initialized = true;

   g_server_sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
   if (g_server_sock == INVALID_SOCKET) {
      Print("MMM_MT4_Bridge: Failed to create server socket.");
      return(INIT_FAILED);
   }

   // Set non-blocking mode
   int nonBlock[1];
   nonBlock[0] = 1;
   ioctlsocket(g_server_sock, FIONBIO, nonBlock);

   // Bind to 127.0.0.1
   int sockaddr[4];
   sockaddr[0] = (htons(InpServerPort) << 16) | AF_INET;
   sockaddr[1] = 0x0100007F; // 127.0.0.1 in network byte order
   sockaddr[2] = 0;
   sockaddr[3] = 0;

   if (bind(g_server_sock, sockaddr, 16) == SOCKET_ERROR) {
      Print("MMM_MT4_Bridge: Socket bind failed on port ", InpServerPort);
      closesocket(g_server_sock);
      g_server_sock = INVALID_SOCKET;
      return(INIT_FAILED);
   }

   if (listen(g_server_sock, 5) == SOCKET_ERROR) {
      Print("MMM_MT4_Bridge: Socket listen failed.");
      closesocket(g_server_sock);
      g_server_sock = INVALID_SOCKET;
      return(INIT_FAILED);
   }

   EventSetMillisecondTimer(InpTimerInterval);
   Print("MMM_MT4_Bridge: Server listening on 127.0.0.1:", InpServerPort);
   return(INIT_SUCCEEDED);
}

//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason) {
   EventKillTimer();
   if (g_client_sock != INVALID_SOCKET) {
      closesocket(g_client_sock);
      g_client_sock = INVALID_SOCKET;
   }
   if (g_server_sock != INVALID_SOCKET) {
      closesocket(g_server_sock);
      g_server_sock = INVALID_SOCKET;
   }
   if (g_wsa_initialized) {
      WSACleanup();
      g_wsa_initialized = false;
   }
   Print("MMM_MT4_Bridge: Shutdown complete.");
}

//+------------------------------------------------------------------+
//| Timer function for non-blocking socket handling                  |
//+------------------------------------------------------------------+
void OnTimer() {
   // Check for new incoming client connection
   if (g_client_sock == INVALID_SOCKET && g_server_sock != INVALID_SOCKET) {
      int clientAddr[4];
      int clientAddrLen[1];
      clientAddrLen[0] = 16;
      int new_sock = accept(g_server_sock, clientAddr, clientAddrLen);
      if (new_sock != INVALID_SOCKET) {
         g_client_sock = new_sock;
         int nonBlock[1];
         nonBlock[0] = 1;
         ioctlsocket(g_client_sock, FIONBIO, nonBlock);
         Print("MMM_MT4_Bridge: Python client connected.");
      }
   }

   // Process messages from connected client
   if (g_client_sock != INVALID_SOCKET) {
      uchar recv_buf[8192];
      int bytes_read = recv(g_client_sock, recv_buf, 8192, 0);
      if (bytes_read > 0) {
         string raw_msg = CharArrayToString(recv_buf, 0, bytes_read);
         ProcessJsonRequest(raw_msg);
      } else if (bytes_read == 0) {
         // Graceful disconnect
         closesocket(g_client_sock);
         g_client_sock = INVALID_SOCKET;
         Print("MMM_MT4_Bridge: Python client disconnected.");
      }
   }
}

void SendJsonResponse(string json) {
   if (g_client_sock == INVALID_SOCKET) return;
   json += "\n";
   uchar send_buf[];
   StringToCharArray(json, send_buf, 0, WHOLE_ARRAY);
   send(g_client_sock, send_buf, StringLen(json), 0);
}

//+------------------------------------------------------------------+
//| Main JSON Command Dispatcher                                     |
//+------------------------------------------------------------------+
void ProcessJsonRequest(string json) {
   string action = JsonGetString(json, "action");
   
   if (action == "PING") {
      CJsonBuilder jb;
      jb.StartObject();
      jb.AddString("status", "OK");
      jb.AddString("message", "PONG");
      jb.AddInt("timestamp", TimeCurrent());
      jb.EndObject();
      SendJsonResponse(jb.GetJson());
   }
   else if (action == "GET_ACCOUNT") {
      HandleGetAccount();
   }
   else if (action == "GET_RATES") {
      string symbol = JsonGetString(json, "symbol");
      if (symbol == "") symbol = Symbol();
      int tf = JsonGetInt(json, "timeframe");
      if (tf <= 0) tf = Period();
      int count = JsonGetInt(json, "count");
      if (count <= 0) count = 100;
      HandleGetRates(symbol, tf, count);
   }
   else if (action == "GET_CUSTOM") {
      string symbol = JsonGetString(json, "symbol");
      if (symbol == "") symbol = Symbol();
      int tf = JsonGetInt(json, "timeframe");
      if (tf <= 0) tf = Period();
      string ind_name = JsonGetString(json, "indicator");
      int buffer_idx = JsonGetInt(json, "buffer");
      int shift = JsonGetInt(json, "shift");
      HandleGetCustom(symbol, tf, ind_name, buffer_idx, shift);
   }
   else if (action == "GET_POSITIONS") {
      HandleGetPositions();
   }
   else if (action == "ORDER_SEND") {
      HandleOrderSend(json);
   }
   else if (action == "ORDER_MODIFY") {
      HandleOrderModify(json);
   }
   else if (action == "ORDER_CLOSE") {
      HandleOrderClose(json);
   }
   else {
      CJsonBuilder jb;
      jb.StartObject();
      jb.AddString("status", "ERROR");
      jb.AddString("error", "Unknown action: " + action);
      jb.EndObject();
      SendJsonResponse(jb.GetJson());
   }
}

//+------------------------------------------------------------------+
//| Handler: GET_ACCOUNT                                             |
//+------------------------------------------------------------------+
void HandleGetAccount() {
   CJsonBuilder jb;
   jb.StartObject();
   jb.AddString("status", "OK");
   jb.AddInt("login", AccountNumber());
   jb.AddString("currency", AccountCurrency());
   jb.AddNumber("balance", AccountBalance(), 2);
   jb.AddNumber("equity", AccountEquity(), 2);
   jb.AddNumber("margin", AccountMargin(), 2);
   jb.AddNumber("free_margin", AccountFreeMargin(), 2);
   jb.AddInt("leverage", AccountLeverage());
   jb.AddString("company", AccountCompany());
   jb.AddString("server", AccountServer());
   jb.EndObject();
   SendJsonResponse(jb.GetJson());
}

//+------------------------------------------------------------------+
//| Handler: GET_RATES                                               |
//+------------------------------------------------------------------+
void HandleGetRates(string symbol, int tf, int count) {
   CJsonBuilder jb;
   jb.StartObject();
   jb.AddString("status", "OK");
   jb.AddString("symbol", symbol);
   jb.AddInt("timeframe", tf);
   jb.StartArray("rates");

   int available = iBars(symbol, tf);
   int limit = MathMin(count, available);
   int digits = (int)MarketInfo(symbol, MODE_DIGITS);
   if (digits <= 0) digits = 5;

   for (int i = limit - 1; i >= 0; i--) {
      datetime t = iTime(symbol, tf, i);
      double o = iOpen(symbol, tf, i);
      double h = iHigh(symbol, tf, i);
      double l = iLow(symbol, tf, i);
      double c = iClose(symbol, tf, i);
      long v = iVolume(symbol, tf, i);

      jb.StartObject();
      jb.AddString("time", TimeToStr(t, TIME_DATE|TIME_MINUTES));
      jb.AddNumber("open", o, digits);
      jb.AddNumber("high", h, digits);
      jb.AddNumber("low", l, digits);
      jb.AddNumber("close", c, digits);
      jb.AddInt("volume", v);
      jb.EndObject();
   }

   jb.EndArray();
   jb.EndObject();
   SendJsonResponse(jb.GetJson());
}

//+------------------------------------------------------------------+
//| Handler: GET_CUSTOM (Reads custom DLL indicators)                |
//+------------------------------------------------------------------+
void HandleGetCustom(string symbol, int tf, string ind_name, int buffer_idx, int shift) {
   double val = iCustom(symbol, tf, ind_name, buffer_idx, shift);
   int digits = (int)MarketInfo(symbol, MODE_DIGITS);
   if (digits <= 0) digits = 5;

   CJsonBuilder jb;
   jb.StartObject();
   jb.AddString("status", "OK");
   jb.AddString("symbol", symbol);
   jb.AddInt("timeframe", tf);
   jb.AddString("indicator", ind_name);
   jb.AddInt("buffer", buffer_idx);
   jb.AddInt("shift", shift);
   jb.AddNumber("value", val, digits);
   jb.EndObject();
   SendJsonResponse(jb.GetJson());
}

//+------------------------------------------------------------------+
//| Handler: GET_POSITIONS                                           |
//+------------------------------------------------------------------+
void HandleGetPositions() {
   CJsonBuilder jb;
   jb.StartObject();
   jb.AddString("status", "OK");
   jb.StartArray("positions");

   int total = OrdersTotal();
   for (int i = 0; i < total; i++) {
      if (OrderSelect(i, SELECT_BY_POS, MODE_TRADES)) {
         jb.StartObject();
         jb.AddInt("ticket", OrderTicket());
         jb.AddString("symbol", OrderSymbol());
         jb.AddString("type", (OrderType() == OP_BUY ? "BUY" : (OrderType() == OP_SELL ? "SELL" : "PENDING")));
         jb.AddNumber("lots", OrderLots(), 2);
         jb.AddNumber("open_price", OrderOpenPrice(), 5);
         jb.AddNumber("sl", OrderStopLoss(), 5);
         jb.AddNumber("tp", OrderTakeProfit(), 5);
         jb.AddNumber("profit", OrderProfit(), 2);
         jb.AddInt("magic", OrderMagicNumber());
         jb.AddString("comment", OrderComment());
         jb.EndObject();
      }
   }

   jb.EndArray();
   jb.EndObject();
   SendJsonResponse(jb.GetJson());
}

//+------------------------------------------------------------------+
//| Handler: ORDER_SEND                                              |
//+------------------------------------------------------------------+
void HandleOrderSend(string json) {
   string symbol = JsonGetString(json, "symbol");
   if (symbol == "") symbol = Symbol();
   string type_str = JsonGetString(json, "type");
   double lots = JsonGetNumber(json, "volume");
   if (lots <= 0) lots = 0.01;
   double sl = JsonGetNumber(json, "sl");
   double tp = JsonGetNumber(json, "tp");
   string comment = JsonGetString(json, "comment");
   if (comment == "") comment = "MMM-Agent Order";
   int magic = JsonGetInt(json, "magic");
   if (magic <= 0) magic = InpMagicNumber;

   int cmd_type = (type_str == "BUY") ? OP_BUY : OP_SELL;
   double price = (cmd_type == OP_BUY) ? MarketInfo(symbol, MODE_ASK) : MarketInfo(symbol, MODE_BID);

   if (PaperMode) {
      Print("[PAPER] Would OrderSend ", type_str, " ", symbol, " lots=", lots, " price=", price, " sl=", sl, " tp=", tp);
      CJsonBuilder pjb;
      pjb.StartObject();
      pjb.AddString("status", "OK");
      pjb.AddBool("paper", true);
      pjb.AddInt("ticket", 0);
      pjb.AddString("symbol", symbol);
      pjb.AddString("type", type_str);
      pjb.AddNumber("price", price, 5);
      pjb.AddNumber("lots", lots, 2);
      pjb.AddNumber("sl", sl, 5);
      pjb.AddNumber("tp", tp, 5);
      pjb.EndObject();
      SendJsonResponse(pjb.GetJson());
      return;
   }

   int ticket = OrderSend(symbol, cmd_type, lots, price, InpSlippage, sl, tp, comment, magic, 0, (cmd_type == OP_BUY ? clrGreen : clrRed));
   
   CJsonBuilder jb;
   jb.StartObject();
   if (ticket > 0) {
      jb.AddString("status", "OK");
      jb.AddInt("ticket", ticket);
      jb.AddString("symbol", symbol);
      jb.AddString("type", type_str);
      jb.AddNumber("price", price, 5);
      jb.AddNumber("lots", lots, 2);
      jb.AddNumber("sl", sl, 5);
      jb.AddNumber("tp", tp, 5);
   } else {
      int err = GetLastError();
      jb.AddString("status", "ERROR");
      jb.AddInt("error_code", err);
      jb.AddString("error_message", ErrorDescription(err));
   }
   jb.EndObject();
   SendJsonResponse(jb.GetJson());
}

//+------------------------------------------------------------------+
//| Handler: ORDER_MODIFY                                            |
//+------------------------------------------------------------------+
void HandleOrderModify(string json) {
   int ticket = JsonGetInt(json, "ticket");
   double sl = JsonGetNumber(json, "sl");
   double tp = JsonGetNumber(json, "tp");

   if (PaperMode) {
      Print("[PAPER] Would OrderModify ticket=", ticket, " sl=", sl, " tp=", tp);
      CJsonBuilder pjb;
      pjb.StartObject();
      pjb.AddString("status", "OK");
      pjb.AddBool("paper", true);
      pjb.AddInt("ticket", ticket);
      pjb.AddNumber("sl", sl, 5);
      pjb.AddNumber("tp", tp, 5);
      pjb.EndObject();
      SendJsonResponse(pjb.GetJson());
      return;
   }

   bool success = false;
   int err = 0;
   if (OrderSelect(ticket, SELECT_BY_TICKET)) {
      success = OrderModify(ticket, OrderOpenPrice(), sl, tp, 0, clrBlue);
      if (!success) err = GetLastError();
   }

   CJsonBuilder jb;
   jb.StartObject();
   if (success) {
      jb.AddString("status", "OK");
      jb.AddInt("ticket", ticket);
      jb.AddNumber("sl", sl, 5);
      jb.AddNumber("tp", tp, 5);
   } else {
      jb.AddString("status", "ERROR");
      jb.AddInt("error_code", err);
   }
   jb.EndObject();
   SendJsonResponse(jb.GetJson());
}

//+------------------------------------------------------------------+
//| Handler: ORDER_CLOSE                                             |
//+------------------------------------------------------------------+
void HandleOrderClose(string json) {
   int ticket = JsonGetInt(json, "ticket");

   if (PaperMode) {
      Print("[PAPER] Would OrderClose ticket=", ticket);
      CJsonBuilder pjb;
      pjb.StartObject();
      pjb.AddString("status", "OK");
      pjb.AddBool("paper", true);
      pjb.AddInt("ticket", ticket);
      pjb.EndObject();
      SendJsonResponse(pjb.GetJson());
      return;
   }

   bool success = false;
   int err = 0;

   if (OrderSelect(ticket, SELECT_BY_TICKET)) {
      double close_price = (OrderType() == OP_BUY) ? MarketInfo(OrderSymbol(), MODE_BID) : MarketInfo(OrderSymbol(), MODE_ASK);
      success = OrderClose(ticket, OrderLots(), close_price, InpSlippage, clrYellow);
      if (!success) err = GetLastError();
   }

   CJsonBuilder jb;
   jb.StartObject();
   if (success) {
      jb.AddString("status", "OK");
      jb.AddInt("ticket", ticket);
   } else {
      jb.AddString("status", "ERROR");
      jb.AddInt("error_code", err);
   }
   jb.EndObject();
   SendJsonResponse(jb.GetJson());
}
