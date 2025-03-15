import pandas as pd
import datetime as dt
from kiteconnect import KiteConnect
import zerodha_login_Automate as zla

# 🔹 Replace with your API credentials
# api_key = "your_api_key"
# access_token = "your_access_token"
kite=zla.kite # #
# kite = KiteConnect(api_key=api_key)
# kite.set_access_token(access_token)

# 🔹 Load instruments list from Zerodha CSV (Download latest file from: https://api.kite.trade/instruments)
instruments_df = pd.read_csv("instruments.csv")  # Ensure this file is downloaded

# 🔹 Filter to include only stocks from NSE & BSE (modify for other exchanges)
exchange_filter = ["NSE", "BSE"]  
stocks_df = instruments_df[instruments_df["exchange"].isin(exchange_filter)]

# 🔹 Define Start & End Year
start_year = 2000
end_year = 2025  # Fetch up to the current year

# 🔹 Time Interval (Supported: "minute", "day", "5minute", etc.)
interval = "day"  # Use "day" for historical data

# 🔹 Empty List to Store All Stock Data
all_stock_data = []

# 🔹 Loop through each stock
for _, row in stocks_df.iterrows():
    instrument_token = row["instrument_token"]
    trading_symbol = row["tradingsymbol"]
    exchange = row["exchange"]

    print(f"Fetching data for {exchange}:{trading_symbol} ({instrument_token})...")

    # Loop through years and fetch data in chunks (60 days at a time)
    for year in range(start_year, end_year + 1):
        from_date = dt.datetime(year, 1, 1)
        to_date = dt.datetime(year, 12, 31)

        while from_date < to_date:
            chunk_end = from_date + dt.timedelta(days=60)  # API allows max 60 days per request
            if chunk_end > to_date:
                chunk_end = to_date

            try:
                data = kite.historical_data(instrument_token, from_date.strftime('%Y-%m-%d'), chunk_end.strftime('%Y-%m-%d'), interval)
                
                # Add stock symbol & exchange to data
                for entry in data:
                    entry["tradingsymbol"] = trading_symbol
                    entry["exchange"] = exchange
                    all_stock_data.append(entry)

                print(f"✅ Data fetched from {from_date.strftime('%Y-%m-%d')} to {chunk_end.strftime('%Y-%m-%d')}")

            except Exception as e:
                print(f"❌ Error fetching {trading_symbol} data: {e}")

            from_date = chunk_end + dt.timedelta(days=1)  # Move to next 60-day window

# 🔹 Convert to DataFrame & Save
df = pd.DataFrame(all_stock_data)
df.to_csv("market_data.csv", index=False)
print("✅ All stock data saved to market_data.csv!")
