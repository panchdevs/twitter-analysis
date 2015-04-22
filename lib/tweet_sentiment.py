import re

def get_features(tweet):
    sentiment_score, neg_words, pos_words = calculate_sentiment_score(tweet)
    pos_emoticon, neg_emoticon = calculate_emoticon_score(tweet)
    return [sentiment_score, pos_words, neg_words, pos_emoticon, neg_emoticon]

def calculate_sentiment_score(tweet):
    d = {}
    fl = open("data/words.txt", 'r')
    for line in fl:
        word, score = line.split("\t")
        d[word] = float(score)
    fl.close()
    lst = tweet.split(' ')
    score = 0
    i = 0
    l = len(lst)
    pos = 0
    neg = 0
    while i < l:
        if lst[i] in d:
            score += d[lst[i]]
            if d[lst[i]] < 5:
                neg += 1
            else:
                pos += 1
        i += 1
    return (score, neg, pos)

def calculate_emoticon_score(tweet):
    no_of_pos = len(re.findall("positive\d emoticon", tweet))
    no_of_neg = len(re.findall("negative\d emoticon", tweet))
    return (no_of_pos, no_of_neg)