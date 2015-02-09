from pymongo import MongoClient
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Stream
from collector import TweetCollector

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)

    tweet_collection = MongoClient('localhost', 27017).TwitterAnalysis.tweets
    collector = TweetCollector(tweet_collection)
    stream = Stream(auth, collector)
    stream.sample(languages = ["en"])
    print('Finished collecting tweets')
