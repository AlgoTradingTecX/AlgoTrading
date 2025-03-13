'''Step 1: AI-Powered Smart Stop Loss Calculation
We’ll use Machine Learning to calculate optimal stop-loss levels dynamically.
 Calculate Dynamic Stop Loss Based on Volatility'''


import numpy as np
import pandas as pd

# Load Market Data (Replace with Live API)
df = pd.read_csv("market_data.csv")
df["returns"] = df["Close"].pct_change()

# Calculate Historical Volatility
def calculate_volatility(df, period=14):
    return np.std(df["returns"].rolling(window=period).mean())

# Smart Stop Loss Function
def smart_stop_loss(current_price):
    volatility = calculate_volatility(df)
    stop_loss = current_price - (current_price * volatility * 2)  # Adjust for risk tolerance
    return round(stop_loss, 2)

# Example Usage
current_price = 22500
print(f"Smart Stop Loss: {smart_stop_loss(current_price)}")

✅ Dynamically adjusts stop-loss based on market volatility.
