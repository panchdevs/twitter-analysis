def calculate_sentiment_score(tweet):
	d = {}
	fl = open("words.txt", 'r')
	for line in fl:
		word, score = line.split("\t")
		d[word] = int(score)
	fl.close()
	lst = tweet.split(' ')
	score = 0
	count = 0
	i = 0
	l = len(lst)
	while i < l:
		if i == l-1:
			if lst[i] in d:
				score += d[lst[i]]
				count += 1
		elif i == l-2:
			str2 = lst[i] + ' ' + lst[i+1]
			if str2 in d:
				score += d[str2]
				count += 1
				i += 1
			elif lst[i] in d:
				score += d[lst[i]]
				count += 1
		else:
			str3 = lst[i] + ' ' + lst[i+1] + ' ' + lst[i+2]
			str2 = lst[i] + ' ' + lst[i+1]
			if str3 in d:
				score += d[str3]
				i += 2
				count += 1
			elif str2 in d:
				score += d[str2]
				i += 1
				count += 1
			elif lst[i] in d:
				score += d[lst[i]]
				count += 1
		i += 1
	return score/count
