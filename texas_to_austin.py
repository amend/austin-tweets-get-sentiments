from pymongo import MongoClient
from time import clock

db = MongoClient().tweets

# sw 30.167461, -97.650991
# nw 30.351388, -97.675908 top right second
# ne 30.371550, -97.757254
# se 30.246454, -97.822433 bottom left first

# query coordintes.coordinates instead of geo.coordinates bc mongodb requires longitude first
# insert autin area tweets in texastweets into austintweets collection

def texas_to_austin():
    tweets_cursor = db.texastweets.find( { "coordinates.coordinates": { "$geoWithin": { "$box":  [ [ -97.822433, 30.246454 ], [ -97.675908, 30.351388 ] ] } } }  )
    print "count of tweets_cursor: " + str(tweets_cursor.count())
    austintweets_cursor = db.austintweets.find()
    print "count of austintweets_cursor: " + str(austintweets_cursor.count())

def make_small_collection(n):
    db.small.drop()
    tweets_cursor = db.austintweets.find()
    for i in range(0, n):
        tweet = {
            "text": tweets_cursor[i]["text"],
            "geo": tweets_cursor[i]["geo"]
            }
        #db.small.insert(tweets_cursor[i])
        db.small.insert(tweet)

make_small_collection(1000)
