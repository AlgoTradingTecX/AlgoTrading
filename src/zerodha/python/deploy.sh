./Token_Generate_Request-Manual_Step.perl
python zerodha_login.py
python zerodha_login_Automate.py
nohup python3 algo_trading.py &
crontab -e
9 15 * * 1-5 /usr/bin/python3 ./algo_trading.py
#"9 15 * * 1-5 /usr/bin/python3 /path/to/algo_trading.py"
