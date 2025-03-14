

Step 4: Deploy RL-Based Adaptive Trading
The AI will now predict & execute trades automatically.
 Live Trading with RL Model

# Load Trained Model
###

model = DQN.load("rl_trading_strategy")

# Execute Trades in Live Market
def rl_adaptive_trading():
    obs = env.reset()
    for _ in range(100):
        action, _ = model.predict(obs)

        if action == 1:
            place_order("NIFTY", "BUY", 50)
        elif action == 2:
            place_order("NIFTY", "SELL", 50)

        obs, _, done, _ = env.step(action)
        if done:
            break

# Run Adaptive AI-Based Trading
rl_adaptive_trading()

# AI continuously adapts & executes trades in real time.

####
