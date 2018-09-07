import re
import tweepy
import twitter_credentials
from tweepy import API
from tweepy import OAuthHandler
from textblob import TextBlob


class Twitter_Authenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN)
        return auth


class Twitter_Client():
    def __init__(self, twitter_user=None):
        self.auth = Twitter_Authenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def get_sentiment(tweet):
    analysis_value = TextBlob(clean_tweet(tweet))
    if analysis_value.sentiment.polarity > 0:
        return 'positive'
    elif analysis_value.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


if __name__ == '__main__':
    tweets = []
    query = 'Kenya'
    count = 200
    twitter_client = Twitter_Client()
    try:
        api = twitter_client.get_twitter_client_api()
        fetched_tweets = api.search(query=query, count=count)
        for tweet in fetched_tweets:
            analysed_tweet = {}

            analysed_tweet['text'] = tweet.text
            analysed_tweet['SA'] = get_sentiment(tweet.text)

            if tweet.retweet_count > 0:
                if analysed_tweet not in tweets:
                    tweets.append(analysed_tweet)
            else:
                tweets.append(analysed_tweet)

    except tweepy.TweepError as e:
        print("Error : " + str(e))

    positive_tweets = [tweet for tweet in tweets if tweet['SA'] == 'positive']
    negative_tweets = [tweet for tweet in tweets if tweet['SA'] == 'negative']
    neutral_tweets = [tweet for tweet in tweets if tweet['SA'] == 'neutral']
    print(len(tweets))
    print("Positive tweets percentage: {} %".format(100 * len(positive_tweets) / len(tweets)))
    print("Negative tweets percentage: {} %".format(100 * len(negative_tweets) / len(tweets)))
    print("Neutral tweets percentage: {} % ".format(100 * len(neutral_tweets) / len(tweets)))
