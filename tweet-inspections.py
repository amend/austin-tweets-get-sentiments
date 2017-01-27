import subprocess

from pymongo import MongoClient
from time import clock

import ast

db = MongoClient().tweets

def make_austintweets_sentiment_collection(n):
    tweets_cursor = db.austintweets.find()
    for i in range(0, n):
        text = "text="
        text += tweets_cursor[i]["text"]
        sentiment = get_sentiment(text)
        tweet = {
            "text": tweets_cursor[i]["text"],
            "geo": tweets_cursor[i]["geo"],
            "sentiment_label": sentiment[0],
            "sentiment_probability": sentiment[1]
            }
        print tweet
        db.make_austintweets_sentiment_collection_again.insert(tweet)

tweets_cursor = db.make_austintweets_sentiment_collection.find()
print 'tweets_cursor.count(): ' + str(tweets_cursor.count())
for i in range(0, tweets_cursor.count()):
    """
    print 'tweet.sentiment_label: ' + tweets_cursor[i]['sentiment_label']
    print 'tweet.geo: '
    print tweets_cursor[i]['geo']
    print 'tweet.geo.coordinates: '
    print tweets_cursor[i]['geo']['coordinates']
    """

    print 'tweet.sentiment_probability: '
    print tweets_cursor[i]['sentiment_probability']
    print 'tweet.sentiment_probability.label: '
    print tweets_cursor[i]['sentiment_probability']['label']
