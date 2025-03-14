

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
