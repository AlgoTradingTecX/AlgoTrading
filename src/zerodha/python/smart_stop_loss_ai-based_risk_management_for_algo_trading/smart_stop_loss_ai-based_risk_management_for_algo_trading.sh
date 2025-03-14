pip install numpy pandas scikit-learn
crontab -e
0 9 * * 1-5 nohup python3 ai-based_risk_management_and_trade_execution.py > ai-based_risk_management_and_trade_execution_output.log 2>&1 &

# Smart Stop Loss & Risk Management runs daily.
