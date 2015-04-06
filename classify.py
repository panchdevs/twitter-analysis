from tweepy import OAuthHandler
from tweepy import Stream
from tweet_listener import TweetListener
import os, sys

CONSUMER_KEY = os.environ["consumer_key"]
CONSUMER_SECRET = os.environ["consumer_secret"]
ACCESS_TOKEN = os.environ["access_token"]
ACCESS_TOKEN_SECRET = os.environ["access_token_secret"]

LIMIT = None
  
def main():
    
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    collector = TweetListener(LIMIT)
    stream = Stream(auth, collector)
    stream.filter(track = [sys.argv[1]],languages = ['en'])
    
    
if __name__ == '__main__':
    main()

