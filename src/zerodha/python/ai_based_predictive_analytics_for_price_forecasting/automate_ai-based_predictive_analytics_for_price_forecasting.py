'''
Step 1: Prepare Historical Stock Data
 We’ll load & preprocess data for AI training.
  Load & Normalize Data
Step 2: Build AI Price Prediction Model
 We’ll use a Long Short-Term Memory (LSTM) neural network for time-series forecasting.
  Prepare Data for AI Training
  
  Define & Train AI Model
Step 3: Predict Future Prices Using AI
 We’ll use the trained LSTM model to predict future prices.
  Load Model & Predict
Step 5: AI-Based Trading Strategy Using Price Predictions
 The AI model will buy or sell based on predicted price trends.
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import load_model

df = pd.read_csv("market_data.csv")  # Columns: Date, Open, High, Low, Close, Volume
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df["Close"].values.reshape(-1, 1))

print(df.head())

###

def create_dataset(data, time_step=50):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        Y.append(data[i + time_step, 0])
    return np.array(X), np.array(Y)

time_step = 50
X, Y = create_dataset(scaled_data, time_step)
X = X.reshape(X.shape[0], X.shape[1], 1)


####
# Define & Train AI Model
###

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(time_step, 1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)
])

model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(X, Y, epochs=20, batch_size=32)
model.save("price_forecasting_model.h5")


####
# Load Model & Predict
###

model = load_model("price_forecasting_model.h5")

def predict_price(data):
    data = scaler.transform(data.reshape(-1, 1))
    data = data.reshape(1, time_step, 1)
    prediction = model.predict(data)
    return scaler.inverse_transform(prediction)

latest_data = df["Close"].values[-time_step:]
predicted_price = predict_price(latest_data)
print(f"Predicted Price: {predicted_price[0][0]}")

####

###
def trade_based_on_prediction():
    current_price = df["Close"].values[-1]
    if predicted_price > current_price * 1.01:
        place_order("NIFTY", "BUY", 50)
    elif predicted_price < current_price * 0.99:
        place_order("NIFTY", "SELL", 50)
    else:
        print("No action taken.")

trade_based_on_prediction()
####
