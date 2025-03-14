'''
Step 1: AI Sentiment Analysis on Market Data
 We’ll use VADER & Transformer-based AI for sentiment scoring.
  Compute Sentiment Scores
'''

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import
import 

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(texts):
    scores = [analyzer.polarity_scores(text)["compound"] for text in texts]
    return sum(scores) / len(scores)

news_sentiment = analyze_sentiment(news_headlines)
twitter_sentiment = analyze_sentiment(tweets)

print(f"News Sentiment Score: {news_sentiment}")
print(f"Twitter Sentiment Score: {twitter_sentiment}")
