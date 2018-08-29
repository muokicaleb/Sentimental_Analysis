import re
import numpy as np
import pandas as pd
from textblob import TextBlob


def clean_verse(verse):
    # removing linkss and special characters using regx
    return ''.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", verse).split())


def analize_sentiment(verse):
    # classify the polarity of a verse using textblob.

    analysis = TextBlob(clean_verse(verse))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


data = pd.read_csv('bible_data_set.csv')


data['SA'] = np.array([analize_sentiment(verse) for verse in data['text']])
# print(data.head(10))


pos_verses = [verse for index, verse in enumerate(data['text']) if data['SA'][index] > 0]
neu_verses = [verse for index, verse in enumerate(data['text']) if data['SA'][index] == 0]
neg_verses = [verse for index, verse in enumerate(data['text']) if data['SA'][index] < 0]

print("Percentage of positive verses: {}%".format(len(pos_verses) * 100 / len(data['text'])))
print("Percentage of neutral verses: {}%".format(len(neu_verses) * 100 / len(data['text'])))
print("Percentage de negative verses: {}%".format(len(neg_verses) * 100 / len(data['text'])))
