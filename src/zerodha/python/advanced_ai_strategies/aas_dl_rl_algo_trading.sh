
pip install tensorflow keras pandas numpy scikit-learn stable-baselines3 gym

nohup python3 algo_trading_ai.py > output.log 2>&1 &
crontab -e
10 9 * * 1-5 pkill -f algo_trading_ai.py && nohup python3 /home/username/algo_trading_ai.py > /home/username/output.log 2>&1 &
