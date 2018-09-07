import re
import tweepy
import twitter_credentials
from tweepy import API
from tweepy import OAuthHandler
from textblob import TextBlob


class Twitter_Authenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.Consumer_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN)
        return auth


class Twitter_Client():
    def __init__(self, twitter_user=None):
        self.auth = Twitter_Authenticator().authenticate_twitter_app()
        self.Twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.Twitter_client


def get_sentiment(tweet):
    analysis_


def get_tweets(query, count=200):
    tweets = []
    try:
        fetched_tweets = api.search(q=query, count=count)
        for tweet in fetched_tweets:
            analysed_tweet = {}

            analysed_tweet['text'] = tweet.text
            analysed_tweet['SA'] = get_sentiment(tweet.text)

    except tweepy.TweepError as e:
        print("Error : " + str(e))
