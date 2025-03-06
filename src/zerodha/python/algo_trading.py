import datetime
import time
import pandas as pd

def fetch_historical_data(symbol, interval="5minute", days=7):
    instrument_token = kite.ltp(f"NSE:{symbol}")[f"NSE:{symbol}"]["instrument_token"]
    from_date = datetime.datetime.now() - datetime.timedelta(days=days)
    to_date = datetime.datetime.now()
    
    data = kite.historical_data(instrument_token, from_date, to_date, interval)
    df = pd.DataFrame(data)
    return df

def calculate_rsi(data, period=14):
    delta = data["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def rsi_trading_strategy(symbol):
    df = fetch_historical_data(symbol)
    df["RSI"] = calculate_rsi(df)

    latest_rsi = df["RSI"].iloc[-1]
    print(f"Current RSI for {symbol}: {latest_rsi}")

    if latest_rsi < 30:
        print("Oversold! Buying...")
        place_order(symbol, "BUY")
    elif latest_rsi > 70:
        print("Overbought! Selling...")
        place_order(symbol, "SELL")

while True:
    print("Running RSI strategy...")
    rsi_trading_strategy("INFY")
    time.sleep(300)  # Runs every 5 minutes
