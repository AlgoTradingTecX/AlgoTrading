sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
python3 -m venv TecX
source TecX/bin/activate

pip install tensorflow keras pandas numpy scikit-learn stable-baselines3 gym

chmod +x ml-based_algo_trading_strategy.py
nohup python3 aas_algo_trading.py > aas_algo_trading_output.log 2>&1 &
nohup python3 aas_algo_trading.py > aas_algo_trading_output.log 2>&1 &

ps aux | grep ml-based_algo_trading_strategy.py
printf "Stop the script if needed bt the command: pkill -f ml-based_algo_trading_strategy.py.py"


crontab -e
11 9 * * 1-5 pkill -f aas_algo_trading.py && nohup python3 /home/$USER/aas_algo_trading.py > /home/$USER/aas_algo_trading_output.log 2>&1 &

11 9 * * 1-5 pkill -f aas_algo_trading.py && nohup python3 ./aas_algo_trading.py > ./aas_algo_trading_output.log 2>&1 &

printf "Manually restart script if needed : "pkill -f ml-based_algo_trading_strategy.py" then type: "nohup python3 ml-based_algo_trading_strategy.py.py > output_ml-based_algo_trading_strategy.log 2>&1 &""
