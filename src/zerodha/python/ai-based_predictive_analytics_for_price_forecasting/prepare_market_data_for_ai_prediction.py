'''
Step 1: Prepare Market Data for AI Prediction
 We’ll use historical stock prices to train our model.
 Load & Preprocess Stock Data
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

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
