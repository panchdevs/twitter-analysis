import csv
from tweet_sentiment import *
from tweetcleaner import process_tweet
from sklearn import svm
from sklearn.externals import joblib

if __name__ == '__main__':
    clf = joblib.load('data/classifier.pkl')
    with open('data/test.csv') as testfile:
        testset = csv.reader(testfile)
        features = []
        classes = []
        for row in testset:
            tweet = process_tweet(row[3])
            features.append(get_features(tweet))
            classes.append(row[1])
        print(clf.score(features, classes))
