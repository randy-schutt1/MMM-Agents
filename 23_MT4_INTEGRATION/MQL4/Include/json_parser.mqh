//+------------------------------------------------------------------+
//|                                                  json_parser.mqh |
//|                                  Copyright 2026, MMM-Agents Team |
//|                                             https://github.com   |
//+------------------------------------------------------------------+
#property copyright "MMM-Agents"
#property link      "https://github.com"
#property strict

//+------------------------------------------------------------------+
//| Simple and robust JSON String Builder for MQL4                   |
//+------------------------------------------------------------------+
class CJsonBuilder {
private:
   string m_buffer;

public:
   CJsonBuilder() {
      m_buffer = "";
   }

   void Reset() {
      m_buffer = "";
   }

   void StartObject() {
      if (StringLen(m_buffer) > 0 && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '{' && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '[')
         m_buffer += ",";
      m_buffer += "{";
   }

   void EndObject() {
      m_buffer += "}";
   }

   void StartArray(string key = "") {
      if (StringLen(m_buffer) > 0 && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '{' && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '[')
         m_buffer += ",";
      if (key != "")
         m_buffer += "\"" + key + "\":[";
      else
         m_buffer += "[";
   }

   void EndArray() {
      m_buffer += "]";
   }

   void AddString(string key, string value) {
      if (StringLen(m_buffer) > 0 && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '{' && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '[')
         m_buffer += ",";
      m_buffer += "\"" + key + "\":\"" + value + "\"";
   }

   void AddNumber(string key, double value, int digits = 5) {
      if (StringLen(m_buffer) > 0 && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '{' && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '[')
         m_buffer += ",";
      m_buffer += "\"" + key + "\":" + DoubleToStr(value, digits);
   }

   void AddInt(string key, long value) {
      if (StringLen(m_buffer) > 0 && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '{' && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '[')
         m_buffer += ",";
      m_buffer += "\"" + key + "\":" + IntegerToString(value);
   }

   void AddBool(string key, bool value) {
      if (StringLen(m_buffer) > 0 && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '{' && StringGetChar(m_buffer, StringLen(m_buffer)-1) != '[')
         m_buffer += ",";
      m_buffer += "\"" + key + "\":" + (value ? "true" : "false");
   }

   string GetJson() {
      return m_buffer;
   }
};

//+------------------------------------------------------------------+
//| Simple Key-Value Extractor from JSON String for MQL4             |
//+------------------------------------------------------------------+
string JsonGetString(string json, string key) {
   string search = "\"" + key + "\":\"";
   int pos = StringFind(json, search);
   if (pos < 0) {
      search = "\"" + key + "\": \"";
      pos = StringFind(json, search);
      if (pos < 0) return "";
   }
   int start = pos + StringLen(search);
   int end = StringFind(json, "\"", start);
   if (end < 0) return "";
   return StringSubstr(json, start, end - start);
}

double JsonGetNumber(string json, string key) {
   string search = "\"" + key + "\":";
   int pos = StringFind(json, search);
   if (pos < 0) return 0.0;
   int start = pos + StringLen(search);
   while (start < StringLen(json) && (StringGetChar(json, start) == ' ' || StringGetChar(json, start) == '"'))
      start++;
   int end = start;
   while (end < StringLen(json) && (
      (StringGetChar(json, end) >= '0' && StringGetChar(json, end) <= '9') ||
      StringGetChar(json, end) == '.' ||
      StringGetChar(json, end) == '-'
   )) {
      end++;
   }
   string numStr = StringSubstr(json, start, end - start);
   return StrToDouble(numStr);
}

int JsonGetInt(string json, string key) {
   return (int)JsonGetNumber(json, key);
}
