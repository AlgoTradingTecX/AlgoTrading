sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
python3 -m venv TecX
source TecX/bin/activate
pip install -r requirements.txt

chmod +x deploy.sh
deploy.sh
