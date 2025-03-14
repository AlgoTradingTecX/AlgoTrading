sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
python3 -m venv TecX
source TecX/bin/activate
pip install kiteconnect pandas numpy
pip install pandas numpy scikit-learn
pip install tensorflow keras pandas numpy scikit-learn
pip install stable-baselines3 gym numpy pandas
pip install transformers torch nltk tweepy vaderSentiment
pip install numpy pandas scikit-learn tensorflow keras cvxpy scipy matplotlib
pip install numpy pandas tensorflow scikit-learn matplotlib pyod

chmod +x algo_trading.py
nohup python3 algo_trading.py > output.log 2>&1 &
ps aux | grep algo_trading.py
printf "Stop the script if needed bt the command: pkill -f algo_trading.py"
crontab -e
echo "18 9 * * 1-5 pkill -f algo_trading.py && nohup python3 /home/$USER/algo_trading.py > /home/$USER/output.log 2>&1 &"
18 9 * * 1-5 pkill -f algo_trading.py && nohup python3 /workspace/AlgoTrading/src/zerodha/python/simple/algo_trading.py > /workspace/AlgoTrading/src/zerodha/python/simple
//output.log 2>&1 &
tail -f output.log
printf "Manually restart script if needed : "pkill -f algo_trading.py" then type: "nohup python3 algo_trading.py > output.log 2>&1 &""

./Token_Generate_Request-Manual_Step.perl
python zerodha_login.py
python zerodha_login_Automate.py
nohup python3 algo_trading.py &
crontab -e
9 15 * * 1-5 /usr/bin/python3 ./algo_trading.py
#"9 15 * * 1-5 /usr/bin/python3 /path/to/algo_trading.py"
