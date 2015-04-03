from tweepy.streaming import StreamListener
from tweetcleaner import process_tweet
from tweet_sentiment import algorithm

class TweetCollector(StreamListener):
    def __init__(self, collection, limit=None, api=None):
        super(TweetCollector, self).__init__()
        self.count = 0
        self.limit = limit
        self.collection = collection

    def on_status(self, tweet):
        cleantweet = tweet._json['text']
        cleantweet = process_tweet(cleantweet)
        tweet._json['cleantweet'] = cleantweet
        score=algorithm(cleantweet)
        tweet._json['score']=score
        self.collection.insert(tweet._json)
        self.count += 1
        if self.count % 10 == 0:
            print("Collected", self.count, "tweets")

        # If limit is reached return False to stop collecting tweets
        # Else if no limit specified or limit not reached return True to
        # collect more tweetsNN-111.txt file, you may find it useful to build a dictionary. Note that the AFINN-111.txt file format is tab-delimited, meaning that the term and the score are separated by
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
