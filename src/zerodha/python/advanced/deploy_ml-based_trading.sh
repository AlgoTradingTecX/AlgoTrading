sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
python3 -m venv TecX
source TecX/bin/activate
pip install kiteconnect pandas numpy scikit-learn
chmod +x ml-based_algo_trading_strategy.py
nohup python3 ml-based_algo_trading_strategy.py > utput_ml-based_algo_trading_strategy.log 2>&1 &
ps aux | grep ml-based_algo_trading_strategy.py
printf "Stop the script if needed bt the command: pkill -f ml-based_algo_trading_strategy.py.py"
crontab -e
18 9 * * 1-5 pkill -f algo_trading.py && nohup python3 /home/#USER/ml-based_algo_trading_strategy.py > /home/#USER/output_ml-based_algo_trading_strategy.log 2>&1 &
18 9 * * 1-5 pkill -f algo_trading.py && nohup python3 /workspace/AlgoTrading/src/zerodha/python/advanced/ml-based_algo_trading_strategy.py > /workspace/AlgoTrading/src/zerodha/python/advanced/output_ml-based_algo_trading_strategy.log 2>&1 &
tail -f output_ml-based_algo_trading_strategy.log
printf "Manually restart script if needed : "pkill -f ml-based_algo_trading_strategy.py" then type: "nohup python3 ml-based_algo_trading_strategy.py.py > output_ml-based_algo_trading_strategy.log 2>&1 &""
