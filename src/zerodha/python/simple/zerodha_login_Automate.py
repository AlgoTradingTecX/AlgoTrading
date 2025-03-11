import os
from kiteconnect import KiteConnect

API_KEY = ""
API_SECRET = ""

def get_access_token():
    if os.path.exists("access_token.txt"):
        with open("access_token.txt", "r") as f:
            return f.read().strip()
    return None

def authenticate():
    kite = KiteConnect(api_key=API_KEY)
    
    access_token = get_access_token()
    if access_token:
        kite.set_access_token(access_token)
        print("Using saved access token.")
        return kite

    request_token = input("Enter your request token: ")  # Get manually once
    session = kite.generate_session(request_token, api_secret=API_SECRET)
    access_token = session["access_token"]

    with open("access_token.txt", "w") as f:
        f.write(access_token)

    print("New access token saved.")
    return kite

kite = authenticate()
