*//
AI Model for Predicting Market Movements
We’ll use LSTM (Long Short-Term Memory) neural networks to predict stock trends.
1️⃣ Train LSTM Model for Market Prediction
//*

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

# Load Market Data (Replace with Live Data)
def load_data():
    df = pd.read_csv("market_data.csv")  # Replace with live API data
    return df["Close"].values.reshape(-1, 1)

# Normalize Data
scaler = MinMaxScaler(feature_range=(0,1))
data = load_data()
scaled_data = scaler.fit_transform(data)

# Prepare Data for LSTM
X, Y = [], []
for i in range(60, len(scaled_data)):  # 60 time steps
    X.append(scaled_data[i-60:i, 0])
    Y.append(scaled_data[i, 0])

X, Y = np.array(X), np.array(Y)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))  # Reshape for LSTM

# Build LSTM Model
model = keras.Sequential([
    keras.layers.LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)),
    keras.layers.LSTM(50, return_sequences=False),
    keras.layers.Dense(25),
    keras.layers.Dense(1)
])

# Compile Model
model.compile(optimizer="adam", loss="mean_squared_error")

# Train Model
model.fit(X, Y, batch_size=32, epochs=10)

# Predict Market Trend
def predict_trend():
    last_60_days = scaled_data[-60:]
    X_test = np.reshape(last_60_days, (1, last_60_days.shape[0], 1))
    prediction = model.predict(X_test)
    return scaler.inverse_transform(prediction)[0][0]

# Test Prediction
print(f"Predicted Market Price: {predict_trend()}")

# Predicts Market Trends using AI.
