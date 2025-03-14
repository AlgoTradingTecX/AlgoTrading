'''
Step 1: Define AI Trading Environment
 We’ll create a custom reinforcement learning environment for market simulation.
   Create TradingEnv for AI Training
'''
import gym
from gym import spaces
import numpy as np
import pandas as pd

class TradingEnv(gym.Env):
    def __init__(self, df):
        super(TradingEnv, self).__init__()
        self.df = df
        self.current_step = 0

        # Define action space (Buy, Sell, Hold)
        self.action_space = spaces.Discrete(3)

        # Define state space (Stock Prices, Indicators)
        self.observation_space = spaces.Box(low=0, high=1, shape=(df.shape[1],), dtype=np.float32)

    def reset(self):
        self.current_step = 0
        return self.df.iloc[self.current_step].values

    def step(self, action):
        reward = 0
        done = False

        if action == 0:  # Buy
            reward = self.df.iloc[self.current_step]["Close"] * 0.01
        elif action == 1:  # Sell
            reward = -self.df.iloc[self.current_step]["Close"] * 0.01

        self.current_step += 1
        if self.current_step >= len(self.df) - 1:
            done = True

        return self.df.iloc[self.current_step].values, reward, done, {}

df = pd.read_csv("market_data.csv")
env = TradingEnv(df)

# Defines an AI environment that learns trading actions.
