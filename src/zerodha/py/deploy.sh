chmod +x /Token_Request.perl
./Token_Request.perl
/Token_Request.perl
chmod +x zerodha_login_Automate.py
python3 zerodha_login_Automate.py

chmod +x algo_trading.py
crontab -e
18 9 * * 1-5 pkill -f algo_trading.py && nohup python3 /workspace/AlgoTrading/src/zerodha/py/algo_trading.py > /workspace/AlgoTrading/src/zerodha/py/output.log 2>&1 &
ps aux | grep algo_trading.py
tail -f output.log
echo "18 9 * * 1-5 pkill -f algo_trading.py && nohup python3 /home/$USER/algo_trading.py > /home/$USER/output.log 2>&1 &"
printf "Manually restart script if needed : "pkill -f algo_trading.py" then type: "nohup python3 algo_trading.py > output.log 2>&1 &""

chmod +x historical_data_csv.py
python3 historical_data_csv.py
chmod +x /instrument_csv.perl
instrument_csv.perl
chmod +x market_data_csv.py
python3 market_data_csv.py
chmod +x execute_ai_based_trading_based_on_prediction.py
python3 execute_ai_based_trading_based_on_prediction.py
