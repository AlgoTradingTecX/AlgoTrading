'''
Step 1: Load & Prepare Market Data
 We’ll preprocess data to detect anomalies in stock price movements.
  Load & Normalize Stock Data
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load Data (Replace with Live API Data)
df = pd.read_csv("market_data.csv")
df = df[["Date", "Close", "Volume"]]
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# Normalize Data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

print(df.head())

# Prepares market data for anomaly detection.
