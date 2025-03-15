import pandas as pd
import datetime as dt
from kiteconnect import KiteConnect

# Replace with your API credentials
api_key = "your_api_key"
access_token = "your_access_token"

kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

# 🔹 Instrument Token for the Stock (Example: NIFTY 50)
instrument_token = 256265  # Change for other stocks

# 🔹 Define Start & End Year (Modify as needed)
start_year = 2000
end_year = 2025  # Fetch up to current year

# 🔹 Time Interval (Supported: "minute", "day", "5minute", etc.)
interval = "day"  # Use "day" for historical decade data

# 🔹 Empty List to Store Data
all_data = []

# 🔹 Loop through years and fetch data in chunks (60 days at a time)
for year in range(start_year, end_year + 1):
    from_date = dt.datetime(year, 1, 1)
    to_date = dt.datetime(year, 12, 31)
    
    while from_date < to_date:
        chunk_end = from_date + dt.timedelta(days=60)  # Fetch 60 days at a time
        if chunk_end > to_date:
            chunk_end = to_date

        try:
            data = kite.historical_data(instrument_token, from_date.strftime('%Y-%m-%d'), chunk_end.strftime('%Y-%m-%d'), interval)
            all_data.extend(data)
            print(f"Fetched data from {from_date.strftime('%Y-%m-%d')} to {chunk_end.strftime('%Y-%m-%d')}")
        except Exception as e:
            print(f"Error fetching data: {e}")

        from_date = chunk_end + dt.timedelta(days=1)  # Move to the next 60-day window

# 🔹 Convert to DataFrame & Save
df = pd.DataFrame(all_data)
df.to_csv("historical_data.csv", index=False)
print("✅ Data saved to historical_data.csv!")
