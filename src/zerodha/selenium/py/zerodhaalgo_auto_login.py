import time
import requests
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from kiteconnect import KiteConnect
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(filename="C:\\Users\\YourUser\\Documents\\zerodha_auto_login.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Telegram Configuration
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

# Zerodha Credentials
ZERODHA_API_KEY = ""
ZERODHA_USER_ID = "HVK662"
ZERODHA_PASSWORD = "mrRASAI333#"
ZERODHA_PIN = "9742"

def send_telegram_message(message):
    """Send Telegram Notification."""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        requests.post(url, json=payload)
    except Exception as e:
        logging.error(f"❌ Telegram Notification Failed: {str(e)}")

def zerodha_auto_login():
    """Automate Zerodha login & fetch request token."""
    try:
        logging.info("🔄 Starting Zerodha Auto Login...")

        # Initialize Headless Chrome
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        # Open Zerodha Login Page
        driver.get(f"https://kite.zerodha.com/connect/login?v=3&api_key={ZERODHA_API_KEY}")
        time.sleep(3)

        # Enter User ID
        driver.find_element(By.ID, "userid").send_keys(ZERODHA_USER_ID)
        driver.find_element(By.ID, "password").send_keys(ZERODHA_PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

        # Enter PIN
        driver.find_element(By.ID, "pin").send_keys(ZERODHA_PIN)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        # Fetch Request Token from URL
        current_url = driver.current_url
        if "request_token=" not in current_url:
            logging.error("❌ Failed to fetch request token!")
            send_telegram_message("❌ Zerodha Login Failed! No request token found.")
            driver.quit()
            return None

        request_token = current_url.split("request_token=")[1].split("&")[0]
        logging.info(f"✅ Request Token: {request_token}")
        driver.quit()

        return request_token

    except Exception as e:
        logging.error(f"❌ Zerodha Login Failed: {str(e)}")
        send_telegram_message(f"❌ Zerodha Auto Login Failed: {str(e)}")
        return None

def generate_access_token(request_token):
    """Generate access token using request token."""
    try:
        kite = KiteConnect(api_key=ZERODHA_API_KEY)
        data = kite.generate_session(request_token, api_secret="YOUR_API_SECRET")
        access_token = data["access_token"]
        logging.info(f"✅ Access Token Generated: {access_token}")

        # Save access token
        with open("C:\\Users\\YourUser\\Documents\\zerodha_access_token.txt", "w") as f:
            f.write(access_token)

        send_telegram_message(f"✅ Zerodha Access Token Generated Successfully!")
        return access_token

    except Exception as e:
        logging.error(f"❌ Access Token Generation Failed: {str(e)}")
        send_telegram_message(f"❌ Access Token Generation Failed: {str(e)}")
        return None

if __name__ == "__main__":
    request_token = zerodha_auto_login()
    if request_token:
        generate_access_token(request_token)
