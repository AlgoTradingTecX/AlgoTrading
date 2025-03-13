pip install stable-baselines3 gym numpy pandas
crontab -e
0 9 * * 1-5 nohup python3 rl_trading.py > output.log 2>&1 &
