
# coding: utf-8


import re
import numpy as np
import pandas as pd
from textblob import TextBlob


def clean_tweet(tweet):
    # removing linkss and special characters using regx
    return ''.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def analize_sentiment(tweet):
    # classify the polarity of a tweet using textblob.

    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


data = pd.read_csv('realDonaldTrumptweets.csv')


data['SA'] = np.array([analize_sentiment(tweet) for tweet in data['text']])
# print(data.head(10))


pos_tweets = [tweet for index, tweet in enumerate(data['text']) if data['SA'][index] > 0]
neu_tweets = [tweet for index, tweet in enumerate(data['text']) if data['SA'][index] == 0]
neg_tweets = [tweet for index, tweet in enumerate(data['text']) if data['SA'][index] < 0]

print("Percentage of positive tweets: {}%".format(len(pos_tweets) * 100 / len(data['text'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets) * 100 / len(data['text'])))
print("Percentage de negative tweets: {}%".format(len(neg_tweets) * 100 / len(data['text'])))
