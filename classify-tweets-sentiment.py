import subprocess

from pymongo import MongoClient
from time import clock

import ast

db = MongoClient().tweets

def get_sentiment(text):
    try:
        test = subprocess.Popen(["curl","-d",text,"http://text-processing.com/api/sentiment/"], stdout=subprocess.PIPE)
        output = test.communicate()[0]
        sentiment_label = output[output.find('label": "')+9:len(output)-2]
        sentiment_probability = ast.literal_eval(output)
        sentiment = (sentiment_label, sentiment_probability)
    except:
        sentiment = ("",{})
    return sentiment

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
        if i % 1000 == 0:
            print tweet
            print "i " + str(i)
        db.make_austintweets_sentiment_collection.insert(tweet)

def make_austintweets_sentiment(n):
    tweets_cursor = db.austintweets.find()
    for i in range(0, n):
        text = "text="
        text += tweets_cursor[i]["text"]
        sentiment = get_sentiment(text)
        tweet = {
            "text": tweets_cursor[i]["text"],
            "geo": tweets_cursor[i]["geo"],
            "sentiment_label": sentiment[0],
            "sentiment_probability": sentiment[1],
            "created_at": tweets_cursor[i]["created_at"]
            }
        print tweet
        db.make_austintweets_sentiment.insert(tweet)


# ***** do not execute these lines!!! *****
db.make_austintweets_sentiment_collection.drop()
make_austintweets_sentiment_collection(37900)

#db.drop_collection('make_austintweets_sentiment')
#make_austintweets_sentiment(37900)
