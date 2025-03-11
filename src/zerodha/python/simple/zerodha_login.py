from kiteconnect import KiteConnect

API_KEY = ""
API_SECRET = ""
REQUEST_TOKEN = ""  # Copy from the redirected URL

kite = KiteConnect(api_key=API_KEY)

# Exchange request token for access token
session = kite.generate_session(REQUEST_TOKEN, api_secret=API_SECRET)
ACCESS_TOKEN = session["access_token"]

print(f"Your Access Token: {ACCESS_TOKEN}")

# Save the access token for future use
with open("access_token.txt", "w") as f:
    f.write(ACCESS_TOKEN)
