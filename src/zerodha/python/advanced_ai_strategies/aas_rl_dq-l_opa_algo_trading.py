import gym
import numpy as np
import pandas as pd
from stable_baselines3 import DQN
from kiteconnect import KiteConnect

API_KEY = "your_api_key"
ACCESS_TOKEN = "your_access_token"

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

# Create a trading environment
class TradingEnv(gym.Env):
    def __init__(self, symbol):
        self.symbol = symbol
        self.df = get_historical_data(symbol)
        self.current_step = 50
        self.balance = 100000  # Initial cash
        self.holdings = 0  # Stocks owned
        self.done = False

    def get_observation(self):
        return self.df.iloc[self.current_step-50:self.current_step][['close']].values

    def step(self, action):
        current_price = self.df.iloc[self.current_step]["close"]
        
        if action == 1:  # Buy
            self.holdings += 1
            self.balance -= current_price
        elif action == 2:  # Sell
            if self.holdings > 0:
                self.holdings -= 1
                self.balance += current_price
        
        self.current_step += 1
        if self.current_step >= len(self.df):
            self.done = True

        reward = self.balance + (self.holdings * current_price)
        return self.get_observation(), reward, self.done, {}

    def reset(self):
        self.current_step = 50
        self.balance = 100000
        self.holdings = 0
        self.done = False
        return self.get_observation()

# Train RL Model
env = TradingEnv("INFY")
model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

# Use RL for Trading
def rl_trading_strategy(symbol):
    obs = env.reset()
    action, _states = model.predict(obs)
    
    if action == 1:
        print("RL Prediction: BUY")
        place_order(symbol, "BUY")
    elif action == 2:
        print("RL Prediction: SELL")
        place_order(symbol, "SELL")

# Run every 5 minutes
while True:
    rl_trading_strategy("INFY")
    time.sleep(300)
