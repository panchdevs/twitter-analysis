from pymongo import MongoClient
from tweepy import OAuthHandler
from tweepy import Stream
from collector import TweetCollector

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

if __name__ == '__main__':
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    client = MongoClient(MONGO_HOST, MONGO_PORT)
    tweet_collection = client.TwitterAnalysis.tweets
    collector = TweetCollector(tweet_collection, 5)
    stream = Stream(auth, collector)
    stream.sample(languages=["en"])
    print('Finished collecting tweets')
