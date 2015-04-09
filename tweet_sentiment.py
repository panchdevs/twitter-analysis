import re

def get_features(tweet):
    sentiment_score, neg_words, pos_words = calculate_sentiment_score(tweet)
    pos_emoticon, neg_emoticon = calculate_emoticon_score(tweet)
    return [sentiment_score, pos_words, neg_words, pos_emoticon, neg_emoticon]

def checkscore(points):
    if points < 0 :
        return -1
    elif points > 0:
        return 1

def calculate_sentiment_score(tweet):
    d = {}
    fl = open("words.txt", 'r')
    for line in fl:
        word, score = line.split("\t")
        d[word] = int(score)
    fl.close()
    lst = tweet.split(' ')
    score = 0
    i = 0
    l = len(lst)
    pos = 0
    neg = 0
    while i < l:
        if i == l-1:
            if lst[i] in d:
                score += d[lst[i]]
                if checkscore(d[lst[i]]<0):
                    neg += 1
                else:
                    pos += 1
        elif i == l-2:
            str2 = lst[i] + ' ' + lst[i+1]
            if str2 in d:
                score += d[str2]
                if checkscore(d[str2]<0):
                    neg += 1
                else:
                    pos += 1
                i += 1
            elif lst[i] in d:
                score += d[lst[i]]
                if checkscore(d[lst[i]]<0):
                    neg += 1
                else:
                    pos += 1
        else:
            str3 = lst[i] + ' ' + lst[i+1] + ' ' + lst[i+2]
            str2 = lst[i] + ' ' + lst[i+1]
            if str3 in d:
                score += d[str3]
                if checkscore(d[str3]<0):
                    neg += 1
                else:
                    pos += 1
                i += 2
            elif str2 in d:
                score += d[str2]
                if checkscore(d[str2]<0):
                    neg += 1
                else:
                    pos += 1
                i += 1
            elif lst[i] in d:
                score += d[lst[i]]
                if checkscore(d[lst[i]]<0):
                    neg += 1
                else:
                    pos += 1
        i += 1
    return (score,neg,pos)

def calculate_emoticon_score(tweet):
    no_of_pos = len(re.findall("positive\d emoticon", tweet))
    no_of_neg = len(re.findall("negative\d emoticon", tweet))
    return (no_of_pos, no_of_neg)
