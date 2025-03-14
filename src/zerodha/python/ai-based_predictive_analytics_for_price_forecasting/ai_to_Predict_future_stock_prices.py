'''
Step 1: Prepare Market Data for AI Prediction
 We’ll use historical stock prices to train our model.
 Load & Preprocess Stock Data

Step 2: Build an AI-Powered LSTM Model
  We’ll use Long Short-Term Memory (LSTM) networks for time-series forecasting.
   Train the LSTM Model

Step 3: Use AI to Predict Future Stock Prices
  The AI will now predict & assist in trade execution.
   Predict Next Day’s Price

'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import load_model

# Load Data (Replace with Live API Data)
df = pd.read_csv("market_data.csv")
df = df[["Date", "Close"]]
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# Normalize Data
scaler = MinMaxScaler(feature_range=(0,1))
df["Close"] = scaler.fit_transform(df[["Close"]])

print(df.head())

# Prepares stock data for AI-based forecasting.

###


# Prepare Data for LSTM
def prepare_data(df, time_steps=60):
    X, y = [], []
    for i in range(len(df) - time_steps):
        X.append(df.iloc[i:i+time_steps, 0])
        y.append(df.iloc[i+time_steps, 0])
    return np.array(X), np.array(y)

time_steps = 60
X, y = prepare_data(df, time_steps)
X = X.reshape(X.shape[0], X.shape[1], 1)

# Build LSTM Model
model = Sequential([
    LSTM(units=50, return_sequences=True, input_shape=(time_steps, 1)),
    LSTM(units=50),
    Dense(units=1)
])

model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(X, y, epochs=20, batch_size=32)

model.save("lstm_stock_model.h5")

# Trains an AI model to predict future stock prices.

####

###

# Load Trained Model
model = load_model("lstm_stock_model.h5")

# Predict Future Price
def predict_next_day(df):
    last_60_days = df[-60:].values.reshape(1, 60, 1)
    predicted_price = model.predict(last_60_days)
    return scaler.inverse_transform(predicted_price)[0][0]

next_day_price = predict_next_day(df["Close"])
print(f"Predicted Next Day Price: {next_day_price}")

# Predicts future stock prices based on AI analytics.
####
