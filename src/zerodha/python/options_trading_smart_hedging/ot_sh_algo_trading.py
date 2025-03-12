import datetime
from kiteconnect import KiteConnect

# Load API credentials
API_KEY = "your_api_key"
ACCESS_TOKEN = "your_access_token"

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

# Get ATM Strike Price
def get_atm_strike(symbol):
    ltp = kite.ltp(f"NSE:{symbol}")[f"NSE:{symbol}"]["last_price"]
    return round(ltp / 50) * 50  # Rounds to nearest strike

# Iron Condor Strategy
def iron_condor(symbol):
    strike = get_atm_strike(symbol)
    expiry = "2024-03-28"  # Modify for next expiry

    # Sell ATM Call & Put
    sell_call = f"{symbol}{expiry}{strike}CE"
    sell_put = f"{symbol}{expiry}{strike}PE"
    
    # Buy OTM Call & Put for hedging
    buy_call = f"{symbol}{expiry}{strike+100}CE"
    buy_put = f"{symbol}{expiry}{strike-100}PE"

    orders = [
        (sell_call, "SELL"), (sell_put, "SELL"),
        (buy_call, "BUY"), (buy_put, "BUY")
    ]

    for strike, action in orders:
        place_options_order(strike, action, 50)

# Place Options Order
def place_options_order(strike, action, quantity):
    order_id = kite.place_order(
        variety="regular",
        exchange="NFO",
        tradingsymbol=strike,
        transaction_type=action,
        quantity=quantity,
        order_type="MARKET",
        product="NRML"
    )
    print(f"{action} Order placed: {strike}")

# Run Iron Condor
iron_condor("NIFTY")

#Iron Condor sells ATM options and hedges with OTM options.
#Generates income with limited risk.
