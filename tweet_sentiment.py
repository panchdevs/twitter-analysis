import re

def get_features(tweet):
	sentiment_score = calculate_sentiment_score(tweet)
	no_of_pos, no_of_neg = calculate_emoticon_score(tweet)
	return [sentiment_score, no_of_pos, no_of_neg]

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
	while i < l:
		if i == l-1:
			if lst[i] in d:
				score += d[lst[i]]
		elif i == l-2:
			str2 = lst[i] + ' ' + lst[i+1]
			if str2 in d:
				score += d[str2]
				i += 1
			elif lst[i] in d:
				score += d[lst[i]]
		else:
			str3 = lst[i] + ' ' + lst[i+1] + ' ' + lst[i+2]
			str2 = lst[i] + ' ' + lst[i+1]
			if str3 in d:
				score += d[str3]
				i += 2
			elif str2 in d:
				score += d[str2]
				i += 1
			elif lst[i] in d:
				score += d[lst[i]]
		i += 1
	return score

def calculate_emoticon_score(tweet):
	no_of_pos = len(re.findall("positive\d emoticon", tweet))
	no_of_neg = len(re.findall("negative\d emoticon", tweet))
	return (no_of_pos, no_of_neg)
