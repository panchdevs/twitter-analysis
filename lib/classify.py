from sklearn.externals import joblib
from tweepy import OAuthHandler
from tweepy import Stream
from tweet_listener import TweetListener

import os, sys

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

def main():
    hashtag = sys.argv[1]
    limit = int(sys.argv[2])

    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    classifier = joblib.load('data/classifier.pkl')

    collector = TweetListener(classifier, limit)

    stream = Stream(auth, collector)
    stream.filter(track=[hashtag], languages=['en'])

if __name__ == '__main__':
    main()