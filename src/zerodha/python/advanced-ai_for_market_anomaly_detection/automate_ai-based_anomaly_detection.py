'''
Step 1: Load Market Data & Detect Anomalies
 We’ll use Unsupervised Learning to find unusual price movements.
  Load & Preprocess Data
Step 2: AI-Based Anomaly Detection
 We’ll use the Autoencoder Neural Network to detect abnormal market behavior.
  Build Autoencoder Model
Step 3: Detect Market Anomalies
 We’ll use reconstruction error to find outliers.
  Identify Anomalies
 Step 4: AI-Based Trading Strategy for Anomaly Detection
  The AI will flag unusual events & prevent high-risk trades.
'''
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout


df = pd.read_csv("market_data.csv")  # Columns: Date, Open, High, Low, Close, Volume
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)

###
# Build Autoencoder Model

model = Sequential([
    Dense(32, activation="relu", input_shape=(scaled_data.shape[1],)),
    Dropout(0.2),
    Dense(16, activation="relu"),
    Dense(32, activation="relu"),
    Dense(scaled_data.shape[1], activation="sigmoid")
])

model.compile(optimizer="adam", loss="mse")
model.fit(scaled_data, scaled_data, epochs=50, batch_size=16)

####

###
# Identify Anomalies
reconstructions = model.predict(scaled_data)
loss = np.mean(np.abs(scaled_data - reconstructions), axis=1)
threshold = np.percentile(loss, 95)  # Top 5% considered anomalies

df["Anomaly"] = loss > threshold
print(df[df["Anomaly"] == True])  # Show anomalies
####

###
# The AI will flag unusual events & prevent high-risk trades.
def trade_based_on_anomalies():
    if df["Anomaly"].iloc[-1]:  
        print("⚠️ Market anomaly detected! Stopping trade execution.")
    else:
        print("✅ No anomalies detected. Trading as usual.")
        place_order("NIFTY", "BUY", 50)  # Example trade

trade_based_on_anomalies()
####
