

###
def calculate_beta(asset_returns, market_returns):
    model = LinearRegression()
    model.fit(market_returns.values.reshape(-1, 1), asset_returns.values)
    return model.coef_[0]

# Example Usage
market_returns = df[df["Asset"] == "NIFTY"]["Price"].pct_change().dropna()
stock_returns = df[df["Asset"] == "RELIANCE"]["Price"].pct_change().dropna()

beta = calculate_beta(stock_returns, market_returns)
print(f"Portfolio Beta: {beta}")

✅ Measures exposure to market risk for hedging.

####
