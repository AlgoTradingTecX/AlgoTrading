'''
Step 1: Load & Prepare Market Data
 We’ll preprocess data to detect anomalies in stock price movements.
  Load & Normalize Stock Data

Step 2: Train an AI Anomaly Detection Model
 We’ll use an Autoencoder (Deep Learning) to detect unusual market behavior.
  Train an Autoencoder Model

Step 3: Detect Market Anomalies in Real-Time
 Now, we’ll flag unusual market movements using AI.
  Identify Anomalies
'''

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
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


###
# Trains AI to detect market anomalie# Build Autoencoder Model
model = Sequential([
    Dense(32, activation="relu", input_shape=(df_scaled.shape[1],)),
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(16, activation="relu"),
    Dense(32, activation="relu"),
    Dense(df_scaled.shape[1], activation="linear")
])

model.compile(optimizer="adam", loss="mse")
model.fit(df_scaled, df_scaled, epochs=50, batch_size=32)

model.save("anomaly_detector.h5")

####

###
# Load Trained Model
model = load_model("anomaly_detector.h5")

# Detect Anomalies
def detect_anomalies(df):
    df_scaled = scaler.transform(df)
    reconstructed = model.predict(df_scaled)
    loss = np.mean(np.abs(df_scaled - reconstructed), axis=1)

    threshold = np.percentile(loss, 99)  # Set anomaly threshold
    anomalies = df.index[loss > threshold]
    
    return anomalies

anomalies = detect_anomalies(df)
print(f"Market Anomalies Detected On: {anomalies}")

# Flags unusual stock price movements in real-time.
####
