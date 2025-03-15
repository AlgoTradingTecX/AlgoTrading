import datetime
import time
import pandas as pd
import numpy as np
import talib  # For technical indicators
import zerodha_login_Automate as zla
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

kite = zla.kite  # ✅ Zerodha API Connection

# 🔹 Fetch Historical Data for ANY Stock & Exchange
def fetch_historical_data(symbol, exchange="NSE", interval="5minute", days=7):
    instrument_token = kite.ltp(f"{exchange}:{symbol}")[f"{exchange}:{symbol}"]["instrument_token"]
    from_date = datetime.datetime.now() - datetime.timedelta(days=days)
    to_date = datetime.datetime.now()

    data = kite.historical_data(instrument_token, from_date, to_date, interval)
    df = pd.DataFrame(data)
    return df

# 🔹 Calculate Multiple Technical Indicators
def calculate_indicators(df):
    df["RSI"] = talib.RSI(df["close"], timeperiod=14)
    df["MACD"], df["MACD_signal"], _ = talib.MACD(df["close"], fastperiod=12, slowperiod=26, signalperiod=9)
    df["Bollinger_Upper"], df["Bollinger_Middle"], df["Bollinger_Lower"] = talib.BBANDS(df["close"], timeperiod=20)
    df["SMA"] = talib.SMA(df["close"], timeperiod=50)
    df["EMA"] = talib.EMA(df["close"], timeperiod=50)
    return df

# 🔹 AI Model for Predicting Future Stock Prices
model = load_model("lstm_stock_model.h5")
scaler = MinMaxScaler(feature_range=(0, 1))

def predict_next_day(df):
    if len(df) < 60:
        return None  # Not enough data
    
    last_60_days = scaler.fit_transform(df["close"].values[-60:].reshape(-1, 1))
    last_60_days = last_60_days.reshape(1, 60, 1)

    predicted_price = model.predict(last_60_days)
    return scaler.inverse_transform(predicted_price)[0][0]

# 🔹 Select Best Stocks for Trading
def select_best_stocks(stocks_data):
    best_stocks = []
    for stock, df in stocks_data.items():
        if len(df) < 60:
            continue  # Skip if not enough data

        predicted_price = predict_next_day(df)
        today_price = df["close"].iloc[-1]

        # Rank Stocks Based on Multiple Indicators
        if df["RSI"].iloc[-1] < 30 and predicted_price > today_price:  # Oversold + AI predicts rise
            best_stocks.append((stock, "BUY", predicted_price))
        elif df["RSI"].iloc[-1] > 70 and predicted_price < today_price:  # Overbought + AI predicts fall
            best_stocks.append((stock, "SELL", predicted_price))

    return sorted(best_stocks, key=lambda x: abs(x[2] - df["close"].iloc[-1]), reverse=True)  # Prioritize biggest move

# 🔹 Execute Trades
def execute_trades(best_stocks):
    for stock, action, predicted_price in best_stocks[:5]:  # Select Top 5 Stocks
        print(f"Executing Trade: {action} {stock} (Predicted: {predicted_price})")
        # kite.place_order(order_id, stock, action, quantity, exchange)

# 🔹 Main Trading Loop
stocks_list = ["RELIANCE", "TCS", "INFY", "HDFC", "SBIN"]  # Add more stocks
exchange = "NSE"
stocks_data = {}

while True:
    print("🔄 Fetching Stock Data & Calculating Indicators...")
    for stock in stocks_list:
        df = fetch_historical_data(stock, exchange)
        df = calculate_indicators(df)
        stocks_data[stock] = df
        df.to_csv(f"stock_data/{stock}_indicators.csv", index=False)  # Save Data

    print("✅ Selecting Best Stocks for Trading...")
    best_stocks = select_best_stocks(stocks_data)

    print("🚀 Executing Trades...")
    execute_trades(best_stocks)

    print("⏳ Sleeping for 5 minutes...")
    time.sleep(300)  # Run every 5 minutes
