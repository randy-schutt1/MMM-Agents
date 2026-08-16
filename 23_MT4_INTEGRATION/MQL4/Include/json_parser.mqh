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

   void AddCommaIfNeeded() {
      int len = StringLen(m_buffer);
      if (len > 0) {
         string lastChar = StringSubstr(m_buffer, len - 1, 1);
         if (lastChar != "{" && lastChar != "[")
            m_buffer += ",";
      }
   }

public:
   CJsonBuilder() {
      m_buffer = "";
   }

   void Reset() {
      m_buffer = "";
   }

   void StartObject() {
      AddCommaIfNeeded();
      m_buffer += "{";
   }

   void EndObject() {
      m_buffer += "}";
   }

   void StartArray(string key = "") {
      AddCommaIfNeeded();
      if (key != "")
         m_buffer += "\"" + key + "\":[";
      else
         m_buffer += "[";
   }

   void EndArray() {
      m_buffer += "]";
   }

   void AddString(string key, string value) {
      AddCommaIfNeeded();
      m_buffer += "\"" + key + "\":\"" + value + "\"";
   }

   void AddNumber(string key, double value, int digits = 5) {
      AddCommaIfNeeded();
      m_buffer += "\"" + key + "\":" + DoubleToString(value, digits);
   }

   void AddInt(string key, long value) {
      AddCommaIfNeeded();
      m_buffer += "\"" + key + "\":" + IntegerToString(value);
   }

   void AddBool(string key, bool value) {
      AddCommaIfNeeded();
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
   while (start < StringLen(json)) {
      string ch = StringSubstr(json, start, 1);
      if (ch == " " || ch == "\"")
         start++;
      else
         break;
   }
   int end = start;
   while (end < StringLen(json)) {
      string ch = StringSubstr(json, end, 1);
      if ((ch >= "0" && ch <= "9") || ch == "." || ch == "-")
         end++;
      else
         break;
   }
   string numStr = StringSubstr(json, start, end - start);
   return StrToDouble(numStr);
}

int JsonGetInt(string json, string key) {
   return (int)JsonGetNumber(json, key);
}
