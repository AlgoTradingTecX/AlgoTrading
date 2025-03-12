printf"Implement Options Trading Strategies We’ll implement Iron Condor, Straddle, and Spread strategies using Zerodha’s Kite API."

pip install pandas numpy
chmod +x algo_trading.py
nohup python3 algo_trading.py > output.log 2>&1 &
ps aux | grep algo_trading.py
printf "Stop the script if needed bt the command: pkill -f algo_trading.py"
crontab -e
30 9 * * 1-5 nohup python3 options_trading.py > output.log 2>&1 &

echo "30 9 * * 1-5 pkill -f algo_trading.py && nohup python3 /home/$USER/algo_trading.py > /home/$USER/output.log 2>&1 &"
30 9 * * 1-5 pkill -f algo_trading.py && nohup python3 /workspace/AlgoTrading/src/zerodha/python/simple/algo_trading.py > /workspace/AlgoTrading/src/zerodha/python/simple
//output.log 2>&1 &
tail -f output.log
printf "Manually restart script if needed : "pkill -f algo_trading.py" then type: "nohup python3 algo_trading.py > output.log 2>&1 &""


printf"Executes Iron Condor & Smart Hedging automatically at market open."
printf"✔ Options Trading (Iron Condor, Straddles, Spreads) ✔ Smart Hedging for Risk Management ✔ Cloud Automation for Daily Execution"
