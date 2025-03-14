'''
Step 1: Collect Market Sentiment Data
 We’ll extract news headlines & Twitter data for real-time analysis.
  Fetch Market News for Sentiment Analysis
'''

import requests
from bs4 import BeautifulSoup

def fetch_market_news():
    url = "https://news.google.com/search?q=stock+market"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    headlines = [h.text for h in soup.find_all("h3")][:10]
    return headlines

news_headlines = fetch_market_news()
print(news_headlines)
