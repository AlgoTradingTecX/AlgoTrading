pip install pandas numpy scikit-learn
crontab -e
18 9 * * 1-5 pkill -f algo_trading.py && nohup python3 /home/#USER/ml-based_algo_trading_strategy.py > /home/#USER/output_ml-based_algo_trading_strategy.log 2>&1 &
18 9 * * 1-5 pkill -f algo_trading.py && nohup python3 /workspace/AlgoTrading/src/zerodha/python/advanced/ml-based_algo_trading_strategy.py > /workspace/AlgoTrading/src/zerodha/python/advanced/output_ml-based_algo_trading_strategy.log 2>&1 &
tail -f output_ml-based_algo_trading_strategy.log
