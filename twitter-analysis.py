from sklearn import svm
from tweet_sentiment import get_features
from tweetcleaner import process_tweet
from tweepy import OAuthHandler, Stream
from tweet_listener import TweetListener

import csv

if __name__ == '__main__':
    with open('dataset.csv') as dataset_file:
        dataset = csv.reader(dataset_file)
        features = []
        classes = []
        for tweet_data in dataset:
            tweet = process_tweet(tweet_data[3])
            tweet_features = get_features(tweet)
            features.append(tweet_features)
            classes.append(tweet_data[1])

    classifier = svm.SVC()
    classifier.fit(features, classes)
