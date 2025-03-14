'''
Step 1: AI Sentiment Analysis on Market Data
 We’ll use VADER & Transformer-based AI for sentiment scoring.
  Compute Sentiment Scores
  then
  Predict Market Movement Based on Sentiment
'''

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import collect_twitter_sentiment_data
import fetch_market_news_for_sentiment_analysis

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(texts):
    scores = [analyzer.polarity_scores(text)["compound"] for text in texts]
    return sum(scores) / len(scores)

news_sentiment = analyze_sentiment(news_headlines)
twitter_sentiment = analyze_sentiment(tweets)

print(f"News Sentiment Score: {news_sentiment}")
print(f"Twitter Sentiment Score: {twitter_sentiment}")

# Predict Market Movement Based on Sentiment


def predict_market_trend():
    combined_score = (news_sentiment + twitter_sentiment) / 2
    if combined_score > 0.2:
        return "Bullish"
    elif combined_score < -0.2:
        return "Bearish"
    else:
        return "Neutral"

market_trend = predict_market_trend()
print(f"Predicted Market Trend: {market_trend}")
