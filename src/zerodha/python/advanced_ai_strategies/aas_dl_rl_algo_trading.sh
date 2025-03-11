
pip install tensorflow keras pandas numpy scikit-learn stable-baselines3 gym

nohup python3 aas_algo_trading.py > aas_algo_trading_output.log 2>&1 &
nohup python3 aas_algo_trading.py > _output.log 2>&1 &
crontab -e
11 9 * * 1-5 pkill -f aas_algo_trading.py && nohup python3 /home/$USER/aas_algo_trading.py > /home/$USER/aas_algo_trading_output.log 2>&1 &

11 9 * * 1-5 pkill -f aas_algo_trading.py && nohup python3 ./aas_algo_trading.py > ./aas_algo_trading_output.log 2>&1 &
