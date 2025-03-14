'''
Step 1: Collect Market Sentiment Data
We’ll fetch real-time financial news & Twitter feeds.
 Fetch News Sentiment Data
'''

import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_news_sentiment():
    url = "https://newsapi.org/v2/everything?q=stocks&apiKey=YOUR_NEWSAPI_KEY"
    news_data = requests.get(url).json()

    sentiment_scores = []
    for article in news_data["articles"]:
        sentiment = analyzer.polarity_scores(article["title"])
        sentiment_scores.append(sentiment["compound"])

    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    return avg_sentiment

print(f"News Sentiment Score: {get_news_sentiment()}")

✅ Analyzes market sentiment from news headlines.
