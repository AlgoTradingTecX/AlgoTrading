# ML-Based Trading Strategy (Random Forest)
# python

import pandas as pd
import numpy as np
from kiteconnect import KiteConnect
from sklearn.ensemble import RandomForestClassifier
import datetime

# Load API credentials
API_KEY = "your_api_key"
ACCESS_TOKEN = "your_access_token"

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

# Fetch historical data
def get_historical_data(symbol, interval="5minute", days=30):
    instrument_token = kite.ltp(f"NSE:{symbol}")[f"NSE:{symbol}"]["instrument_token"]
    from_date = datetime.datetime.now() - datetime.timedelta(days=days)
    to_date = datetime.datetime.now()

    data = kite.historical_data(instrument_token, from_date, to_date, interval)
    df = pd.DataFrame(data)
    return df

# Feature Engineering
def prepare_data(df):
    df["SMA_5"] = df["close"].rolling(window=5).mean()
    df["SMA_10"] = df["close"].rolling(window=10).mean()
    df["volatility"] = df["close"].rolling(5).std()
    df["label"] = np.where(df["close"].shift(-1) > df["close"], 1, 0)  # 1 = Buy, 0 = Sell
    return df.dropna()

# Train ML Model
def train_model(df):
    features = ["SMA_5", "SMA_10", "volatility"]
    X = df[features]
    y = df["label"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

# Run strategy
def ml_trading_strategy(symbol):
    df = get_historical_data(symbol)
    df = prepare_data(df)
    
    model = train_model(df)
    
    latest_data = df.iloc[-1:][["SMA_5", "SMA_10", "volatility"]]
    prediction = model.predict(latest_data)[0]

    if prediction == 1:
        print("ML Prediction: BUY")
        place_order(symbol, "BUY")
    else:
        print("ML Prediction: SELL")
        place_order(symbol, "SELL")

# Place order
def place_order(symbol, transaction_type, quantity=1):
    last_price = kite.ltp(f"NSE:{symbol}")[f"NSE:{symbol}"]["last_price"]
    stop_loss = round(last_price * 0.98, 2)  # 2% Stop Loss
    target_price = round(last_price * 1.05, 2)  # 5% Profit Target

    order_id = kite.place_order(
        variety="regular",
        exchange="NSE",
        tradingsymbol=symbol,
        transaction_type=transaction_type,
        quantity=quantity,
        order_type="LIMIT",
        price=last_price,
        stoploss=stop_loss,
        squareoff=target_price,
        product="MIS"
    )
    print(f"Order placed: {transaction_type} {symbol} at {last_price} with SL {stop_loss}")

# Run every 5 minutes
while True:
    ml_trading_strategy("INFY")
    time.sleep(300)

# This ML model uses historical prices to predict future trends.
# If prediction = Buy, it places a BUY order. If prediction = Sell, it places a SELL order
