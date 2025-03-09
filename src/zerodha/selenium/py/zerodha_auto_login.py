import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from kiteconnect import KiteConnect

# 🔹 Zerodha Credentials (Replace with your details)
USER_ID = "HVK662"
PASSWORD = "mrRASAI333#"
PIN = "9742"
API_KEY = "ds4yskil8l9lrbfo"
API_SECRET = ""
ACCESS_TOKEN_FILE = "D:\\Users\\TECX\\Automation\\Zerodha\\access_token.txt"  # Change path if needed

# Function to log in & fetch request token
def fetch_request_token():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run without GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        login_url = f"https://kite.zerodha.com/connect/login?v=3&api_key={API_KEY}"
        driver.get(login_url)
        time.sleep(2)

        # Step 1: Enter username and password
        driver.find_element(By.ID, "userid").send_keys(USER_ID)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        # Step 2: Enter PIN
        driver.find_element(By.ID, "pin").send_keys(PIN)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        # Step 3: Fetch request token from URL
        request_token_url = driver.current_url
        if "request_token=" in request_token_url:
            request_token = request_token_url.split("request_token=")[1].split("&")[0]
            print(f"✅ Request Token: {request_token}")
            return request_token
        else:
            print("❌ Failed to retrieve request token.")
            return None

    finally:
        driver.quit()

# Function to generate access token & store it
def generate_access_token():
    request_token = fetch_request_token()
    if request_token:
        kite = KiteConnect(api_key=API_KEY)
        try:
            data = kite.generate_session(request_token, api_secret=API_SECRET)
            access_token = data["access_token"]
            print(f"✅ Access Token: {access_token}")

            # Save access token for reuse
            with open(ACCESS_TOKEN_FILE, "w") as file:
                file.write(access_token)
            
            return access_token
        except Exception as e:
            print(f"❌ Error generating access token: {e}")
            return None
    return None

# Run the script at market opening time (before 9 AM)
schedule.every().day.at("08:50").do(generate_access_token)

print("✅ Automated Access Token Fetcher Running...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
