'''
Step 1: Load & Prepare Portfolio Data
 We’ll preprocess historical stock & options data for AI-based optimization.
  Load Portfolio Data

Step 3: AI-Based Hedging Strategy (Options & Futures)
 We’ll use AI to hedge against portfolio risk.
  Calculate Portfolio Risk Exposure (Beta)

Step 3: AI-Powered Portfolio Optimization
 We’ll optimize portfolio allocation using AI.
  AI-Optimized Portfolio Allocation
'''

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import cvxpy as cp

# Load Portfolio Data (Replace with Live API Data)
df = pd.read_csv("portfolio_data.csv")  # Columns: Date, Asset, Price, Volume
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

print(df.head())

# Prepares data for AI-based portfolio analysis.

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

# Measures exposure to market risk for hedging.

####

###
# AI-Optimized Hedge Ratio Calculation

def calculate_hedge_ratio(asset_beta, hedge_asset_beta):
    return asset_beta / hedge_asset_beta

hedge_ratio = calculate_hedge_ratio(beta, 1)  # Assuming NIFTY as hedge
print(f"Hedge Ratio: {hedge_ratio}")

# AI suggests the best hedge ratio for risk management.

####

###
def optimize_portfolio(returns, risk_tolerance=0.1):
    n_assets = returns.shape[1]
    weights = cp.Variable(n_assets)
    expected_return = returns.mean().values @ weights
    risk = cp.quad_form(weights, np.cov(returns.T))
    
    objective = cp.Maximize(expected_return - risk_tolerance * risk)
    constraints = [cp.sum(weights) == 1, weights >= 0]

    prob = cp.Problem(objective, constraints)
    prob.solve()

    return weights.value

# Example Usage
portfolio_returns = df.pivot(columns="Asset", values="Price").pct_change().dropna()
optimal_weights = optimize_portfolio(portfolio_returns)

print(f"Optimized Portfolio Weights: {optimal_weights}")

# AI optimally allocates capital for max returns & min risk.
####
