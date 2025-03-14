# Fetch Twitter Sentiment Data

import tweepy

# Twitter API Keys
api_key = "YOUR_TWITTER_API_KEY"
api_secret = "YOUR_TWITTER_API_SECRET"
access_token = "YOUR_TWITTER_ACCESS_TOKEN"
access_secret = "YOUR_TWITTER_ACCESS_SECRET"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def get_twitter_sentiment():
    tweets = api.search_tweets(q="NIFTY OR stocks", count=100, lang="en")
    sentiment_scores = [analyzer.polarity_scores(tweet.text)["compound"] for tweet in tweets]
    
    return sum(sentiment_scores) / len(sentiment_scores)

print(f"Twitter Sentiment Score: {get_twitter_sentiment()}")

# Analyzes Twitter sentiment for market trends.
