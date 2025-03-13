
pip install numpy pandas scipy

crontab -e
0 9 * * 1-5 nohup python3 greeks_hedging.py > output.log 2>&1 &
