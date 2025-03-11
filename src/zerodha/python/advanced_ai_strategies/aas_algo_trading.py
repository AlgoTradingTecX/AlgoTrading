import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from kiteconnect import KiteConnect
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

# Prepare data for LSTM
def prepare_data(df):
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(df[['close']])

    X_train, y_train = [], []
    for i in range(50, len(scaled_data)):
        X_train.append(scaled_data[i-50:i, 0])
        y_train.append(scaled_data[i, 0])

    return np.array(X_train), np.array(y_train), scaler

# Build LSTM Model
def build_lstm():
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(50, 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Train LSTM Model
def train_lstm(symbol):
    df = get_historical_data(symbol)
    X_train, y_train, scaler = prepare_data(df)

    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

    model = build_lstm()
    model.fit(X_train, y_train, epochs=10, batch_size=16)

    return model, scaler

# Predict Future Price
def predict_price(symbol, model, scaler):
    df = get_historical_data(symbol)
    last_50_days = df[['close']].tail(50).values
    last_50_days_scaled = scaler.transform(last_50_days)

    X_test = np.array([last_50_days_scaled])
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    predicted_price = model.predict(X_test)
    return scaler.inverse_transform(predicted_price)[0][0]

# Trading Strategy Based on Prediction
def lstm_trading_strategy(symbol):
    model, scaler = train_lstm(symbol)
    predicted_price = predict_price(symbol, model, scaler)
    
    current_price = kite.ltp(f"NSE:{symbol}")[f"NSE:{symbol}"]["last_price"]

    if predicted_price > current_price:
        print(f"LSTM Prediction: BUY {symbol}")
        place_order(symbol, "BUY")
    else:
        print(f"LSTM Prediction: SELL {symbol}")
        place_order(symbol, "SELL")

def place_order(symbol, transaction_type, quantity=1):
    order_id = kite.place_order(
        variety="regular",
        exchange="NSE",
        tradingsymbol=symbol,
        transaction_type=transaction_type,
        quantity=quantity,
        order_type="MARKET",
        product="MIS"
    )
    print(f"Order placed: {transaction_type} {symbol}")

# Run every 5 minutes
while True:
    lstm_trading_strategy("INFY")
    time.sleep(300)

