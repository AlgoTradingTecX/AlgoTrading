import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import os

# 🔹 Load Market Data (Assumes market_data.csv has ALL stocks & exchanges)
df = pd.read_csv("market_data.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# 🔹 Get Unique Stocks & Exchanges
stocks = df["tradingsymbol"].unique()
exchanges = df["exchange"].unique()

# 🔹 LSTM Parameters
TIME_STEPS = 60
EPOCHS = 20
BATCH_SIZE = 32

# 🔹 Ensure "models" Directory Exists for Saving Models
if not os.path.exists("models"):
    os.makedirs("models")

# 🔹 Train LSTM Model for Each Stock
def prepare_data(series, time_steps=60):
    X, y = [], []
    for i in range(len(series) - time_steps):
        X.append(series[i : i + time_steps])
        y.append(series[i + time_steps])
    return np.array(X), np.array(y)

for stock in stocks:
    print(f"Training AI Model for {stock}...")

    stock_data = df[df["tradingsymbol"] == stock]["close"]
    
    if len(stock_data) < TIME_STEPS:
        print(f"❌ Not enough data for {stock}, skipping...")
        continue

    # Normalize Data
    scaler = MinMaxScaler(feature_range=(0,1))
    stock_data_scaled = scaler.fit_transform(stock_data.values.reshape(-1, 1))

    # Prepare Data
    X, y = prepare_data(stock_data_scaled, TIME_STEPS)
    X = X.reshape(X.shape[0], X.shape[1], 1)

    # Build Model
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(TIME_STEPS, 1)),
        LSTM(50),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mean_squared_error")

    # Train Model
    model.fit(X, y, epochs=EPOCHS, batch_size=BATCH_SIZE)

    # Save Model
    model.save(f"models/{stock}_lstm.h5")
    print(f"✅ Model for {stock} saved!")

print("✅ All Models Trained & Saved!")

# 🔹 Predict Future Prices for All Stocks
def predict_next_day(stock):
    model_path = f"models/{stock}_lstm.h5"
    
    if not os.path.exists(model_path):
        print(f"❌ Model for {stock} not found, skipping prediction...")
        return None

    model = load_model(model_path)
    stock_data = df[df["tradingsymbol"] == stock]["close"]

    if len(stock_data) < TIME_STEPS:
        print(f"❌ Not enough data for {stock}, skipping...")
        return None

    scaler = MinMaxScaler(feature_range=(0,1))
    stock_data_scaled = scaler.fit_transform(stock_data.values.reshape(-1, 1))

    last_60_days = stock_data_scaled[-TIME_STEPS:].reshape(1, TIME_STEPS, 1)
    predicted_price = model.predict(last_60_days)
    return scaler.inverse_transform(predicted_price)[0][0]

for stock in stocks:
    predicted_price = predict_next_day(stock)
    if predicted_price:
        today_price = df[df["tradingsymbol"] == stock]["close"].iloc[-1]
        print(f"{stock} | Today: {today_price} | Predicted: {predicted_price}")

print("✅ All Predictions Complete!")

# 🔹 AI-Based Automated Trading Decisions
def ai_trading(stock):
    predicted_price = predict_next_day(stock)
    if predicted_price is None:
        return

    today_price = df[df["tradingsymbol"] == stock]["close"].iloc[-1]
    return predicted_price ##
####
    ##if predicted_price > today_price:
        ##print(f"📈 AI recommends: BUY {stock}")
        # place_order(stock, "BUY", quantity)
    ##else:
        ##print(f"📉 AI recommends: SELL {stock}")
        # place_order(stock, "SELL", quantity)

#for stock in stocks: # loop for all stocks price prediction in once
    #ai_trading(stock) #

print("✅ AI Trading Decisions Executed!")
