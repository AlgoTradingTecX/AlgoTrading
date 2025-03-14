'''
Step 1: Create a Custom RL Trading Environment
 The AI will learn how to adapt trading strategies dynamically.
  Define the RL Trading Environment
'''
import gym
import numpy as np
import pandas as pd
from gym import spaces

class TradingEnv(gym.Env):
    def __init__(self):
        super(TradingEnv, self).__init__()

        self.data = self.load_market_data()
        self.current_step = 0

        # Actions: 0 = Hold, 1 = Buy, 2 = Sell
        self.action_space = spaces.Discrete(3)

        # Observations: [Price, Volatility, RSI, MACD]
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(4,), dtype=np.float32)
    
    def load_market_data(self):
        df = pd.read_csv("market_data.csv")  # Replace with live API data
        return df[["Close", "Volatility", "RSI", "MACD"]].values

    def step(self, action):
        current_price = self.data[self.current_step, 0]
        next_price = self.data[self.current_step + 1, 0]

        reward = 0
        if action == 1:  # Buy
            reward = next_price - current_price
        elif action == 2:  # Sell
            reward = current_price - next_price

        self.current_step += 1
        done = self.current_step >= len(self.data) - 1
        return self.data[self.current_step], reward, done, {}

    def reset(self):
        self.current_step = 0
        return self.data[self.current_step]

# The AI can now interact with the market & learn.
