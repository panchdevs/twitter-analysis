from sklearn import svm
from tweepy.streaming import StreamListener
from tweetcleaner import process_tweet
from tweet_sentiment import *

class TweetListener(StreamListener):
    def __init__(self, classifier, limit=None, api=None):
        super(TweetListener, self).__init__()
        self.count = 0
        self.limit = limit
        self.classifier = classifier

    def on_status(self, tweet):
        cleantweet = process_tweet(tweet._json['text'])
        score = calculate_sentiment_score(cleantweet)
        no_of_pos, no_of_neg = calculate_emoticon_score(cleantweet)

        polarity = self.classifier.predict([score, no_of_neg, no_of_pos])

        print(tweet._json['text'], polarity[0], sep="<-||->")

        self.count += 1

        # If limit is reached return False to stop collecting tweets
        # Else if no limit specified or limit not reached return True to
        # collect more tweets
        return not self.limit_reached()

    def limit_reached(self):
        if self.limit is None:
            return False
        elif self.count == self.limit:
            return True
        else:
            return False

