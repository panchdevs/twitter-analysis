d={ }
def initialise():
	fl=open("words.txt",'r')
	for line in fl:
		word, score  = line.split("\t")
		d[word] = int(score)
	fl.close()
	#print(d.items())


def algorithm(s):
	initialise()
	lst={}
	lst=s.split(' ')
	#print(lst)
	score=0
	count=0
	i=0
	l=len(lst)
	while i<l:
		if i==l-1:
			if lst[i] in d:
				score+=d[lst[i]]
				count+=1
				#print(lst[i])
		elif i==l-2:
			str2=lst[i]+' '+lst[i+1]
			if str2 in d:
				score+=d[str2]
				count+=1
				i+=1
				#print(str2)
			elif lst[i] in d:
				score+=d[lst[i]]
				count+=1
				print(lst[i])
		else:
			str3=lst[i]+' '+lst[i+1]+' '+lst[i+2];
			str2=lst[i]+' '+lst[i+1];
			if str3 in d:
				score+=d[str3]
				i+=2
				count+=1
				print(str3)
			elif str2 in d:
				score+=d[str2]
				i+=1
				count+=1
				print(str2)
			elif lst[i] in d:
				score+=d[lst[i]]
				count+=1
				print(lst[i])
		i+=1
	print(score)
	return score/count