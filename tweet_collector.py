from pymongo import MongoClient
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Stream
from collector import TweetCollector

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

mongo_host = 'localhost'
mongo_port = 27017

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)

    client = MongoClient(mongo_host, mongo_port)
    tweet_collection = client.TwitterAnalysis.tweets
    collector = TweetCollector(tweet_collection)
    stream = Stream(auth, collector)
    stream.sample(languages = ["en"])
    print('Finished collecting tweets')
