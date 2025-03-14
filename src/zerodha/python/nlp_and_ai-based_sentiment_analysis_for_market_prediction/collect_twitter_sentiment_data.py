# Collect Twitter Sentiment Data (Requires Twitter API)

import tweepy

api_key = "YOUR_TWITTER_API_KEY"
api_secret = "YOUR_TWITTER_API_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_secret = "YOUR_ACCESS_SECRET"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def fetch_tweets(keyword):
    tweets = api.search_tweets(q=keyword, count=10, lang="en")
    return [tweet.text for tweet in tweets]

tweets = fetch_tweets("Stock Market")
print(tweets)

