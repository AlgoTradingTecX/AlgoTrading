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
chmod +x /src/zerodha/python/simple/deploy.sh
src/zerodha/python/simple/deploy.sh
