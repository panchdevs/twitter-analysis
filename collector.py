import pymongo

from tweepy.streaming import StreamListener

class TweetCollector(StreamListener):
    def __init__(self, collection, limit = None, api = None):
        super(TweetCollector, self).__init__()
        self.count = 0
        self.limit = limit
        self.collection = collection

    def on_status(self, tweet):
        self.collection.insert(tweet._json)
        self.count += 1
        if self.count % 10 == 0:
            print("Collected", self.count, "tweets")

        # If limit is reached return False to stop collecting tweets
        # Else if no limit specified or limit not reached return True to
        # collect more tweets
        return not self.limit_reached()

    def on_error(self, status):
        print(status, "An error occured.")

    def limit_reached(self):
        if self.limit is None:
            return False
        elif self.count == self.limit:
            return True
        else:
            return False
