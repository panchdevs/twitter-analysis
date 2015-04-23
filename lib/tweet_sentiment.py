import re
import nltk

def get_features(tweet):
    sentiment_score, neg_words, pos_words = calculate_sentiment_score(tweet)
    pos_emoticon, neg_emoticon = calculate_emoticon_score(tweet)
    return [sentiment_score, pos_words, neg_words, pos_emoticon, neg_emoticon]

def calculate_sentiment_score(tweet):
    pos={'PRP':1,'NN':1,'DT':2,'VBP':3,'JJ':4}
    d = {}
    with open("data/words.txt", 'r') as fl:
        for line in fl:
            word, score = line.split("\t")
            d[word] = float(score)
    lst = nltk.word_tokenize(tweet)
    tokens = nltk.pos_tag(lst)
    score = 0
    i = 0
    l = len(tokens)
    positive = 0
    negative = 0
    while i < l:
        if(tokens[i][0] in d and tokens[i][1] in pos):
            if(d[tokens[i][0]] < 5):
                score += (d[tokens[i][0]]*pos[tokens[i][1]]*(-1))
            else:
                score += d[tokens[i][0]]*pos[tokens[i][1]]
        elif (tokens[i][0] in d):
            if(d[tokens[i][0]] < 5):
                score += (d[tokens[i][0]]*(-1))
            else:
                score += d[tokens[i][0]]
        if(tokens[i][0] in d):
            if(d[tokens[i][0]] < 5):
                negative += 1
            else:
                positive += 1
        i += 1
    return (score, negative, positive)

def calculate_emoticon_score(tweet):
    no_of_pos = len(re.findall("positive\d emoticon", tweet))
    no_of_neg = len(re.findall("negative\d emoticon", tweet))
    return (no_of_pos, no_of_neg)
