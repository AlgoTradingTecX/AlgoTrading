import datetime
import time
import pandas as pd
import zerodha_login_Automate as zla

kite=zla.kite # #
def fetch_historical_data(symbol, interval="5minute", days=7):
    instrument_token = kite.ltp(f"NSE:{symbol}")[f"NSE:{symbol}"]["instrument_token"]
    from_date = datetime.datetime.now() - datetime.timedelta(days=days)
    to_date = datetime.datetime.now()
    
    data = kite.historical_data(instrument_token, from_date, to_date, interval)
    df = pd.DataFrame(data)
    return df

def calculate_rsi(data, period=14):
    delta = data["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
###
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

###
def predictive_ai_trading():
    today_price = df["Close"].iloc[-1]
    predicted_price = predict_next_day(df["Close"])
    print(f"Today's Price: {today_price}, Predicted: {predicted_price}, Trade Executed!")
    return predicted_price

# AI automatically decides and executes trades based on predictions.
####

####
def rsi_trading_strategy(symbol):
    df = fetch_historical_data(symbol)
    df["RSI"] = calculate_rsi(df)

    latest_rsi = df["RSI"].iloc[-1]
    print(f"Current RSI for {symbol}: {latest_rsi}")
    # Run Predictive AI Trading
    predictive_ai_trading()
    if latest_rsi < 30:
        print("Oversold! Buying.../nlets predict future")
        if predicted_price > today_price:
           place_order("NIFTY", "BUY", 50)
     # place_order(symbol, "BUY")
    elif latest_rsi > 70:
        print("Overbought! Selling...")
        if predicted_price < today_price:
           place_order("NIFTY", "SELL", 50)
       # place_order(symbol, "SELL")

while True:
    print("Running RSI strategy...")
    rsi_trading_strategy("NSEI")
    time.sleep(300)  # Runs every 5 minutes
