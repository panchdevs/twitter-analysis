from tweepy.streaming import StreamListener
from tweetcleaner import process_tweet
from tweet_sentiment import *

class TweetListener(StreamListener):
    def __init__(self, limit=100, api=None):
        super(TweetListener, self).__init__()
        self.count = 0
        self.limit = limit

    def on_status(self, tweet):
        self.count += 1
        if self.count % 10 == 0:
            print("Collected", self.count, "tweets")

        return not self.limit_reached()

    def limit_reached(self):
        if self.limit is None:
            return False
        elif self.count == self.limit:
            return True
        else:
            return False
