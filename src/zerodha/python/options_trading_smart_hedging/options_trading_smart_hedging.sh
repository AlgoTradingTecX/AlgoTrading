printf"Implement Options Trading Strategies We’ll implement Iron Condor, Straddle, and Spread strategies using Zerodha’s Kite API."

pip install pandas numpy
chmod +x sh_ot_stocks_algo_trading.py
nohup python3 sh_ot_stocks_algo_trading.py > sh_ot_stocks_algo_trading_output.log 2>&1 &

printf "Stop the script if needed bt the command: pkill -f sh_ot_stocks_algo_trading.py"
crontab -e
30 9 * * 1-5 nohup python3 sh_ot_stocks_algo_trading.py > sh_ot_stocks_algo_trading_output.log 2>&1 &
ps aux | grep sh_ot_stocks_algo_trading.py
echo "30 9 * * 1-5 pkill -f ps aux | grep sh_ot_stocks_algo_trading.py && nohup python3 /home/$USER/sh_ot_stocks_algo_trading.py > /home/$USER/sh_ot_stocks_algo_trading_output.log 2>&1 &"
30 9 * * 1-5 pkill -f sh_ot_stocks_algo_trading.py && nohup python3 /workspace/AlgoTrading/src/zerodha/python//sh_ot_stocks_algo_trading.py > /workspace/AlgoTrading/src/zerodha/python//sh_ot_stocks_algo_trading_output.log 2>&1 &
tail -f output.log
printf "Manually restart script if needed : "pkill -f sh_ot_stocks_algo_trading.py" then type: "nohup python3 sh_ot_stocks_algo_trading.py > sh_ot_stocks_algo_trading_output.log 2>&1 &""


printf"Executes Iron Condor & Smart Hedging automatically at market open."
printf"✔ Options Trading (Iron Condor, Straddles, Spreads) ✔ Smart Hedging for Risk Management ✔ Cloud Automation for Daily Execution"
