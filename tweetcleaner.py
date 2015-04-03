import re

def process_tweet(tweet):
    tweet = tweet.lower()

    # Convert www.* or https?://* to URL
    tweet = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)

    # Convert @username to AT_USER
    tweet = re.sub(r'@[^\s]+', 'AT_USER', tweet)

    # Remove additional white spaces
    tweet = re.sub(r'[\s]+', ' ', tweet)

    # Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

    # Emoticons
    tweet = process_emoticons(tweet)
    
    # Trim
    tweet = tweet.strip('\'"')

    return tweet


# Function to process emoticons
def process_emoticons(tweet): 
    POS1 = ["(:","(-:",":)" , ":-)" , ":-]" , ":]" , ":-P" , ":P" , ":p" , ":-p", ":3" ,":>","=]", "8)", "=)"];
    POS2 = [":D" ,"=D",";D",";-D", ":-D" , ";-)", ";)","8-D", "8D", "x-D", "xD", "X-D", "XD",":'-)", ":')"];
    NEG1 = [":$",":-(" , ":("  , ":-/" ,"=/", "=(", ":/" , ":<", ":-[", ":[" ,":{"];
    NEG2 = [":-c", ":c",":-<",">:[",":'-(", ":'("];
    NEU  = [":|" , ":-|" , ":-O", ":O", ":-o", ":o", "8-0", "O_O", "o-o", "O_o", "o_O", "o_o", "O-O"];       

    tweetlist = tweet.split()

    for i in range(len(tweetlist)):
        if tweetlist[i] in POS1:
            tweetlist[i] = "POSITIVE1 EMOTICON"

        if tweetlist[i] in POS2:
            tweetlist[i] = "POSITIVE2 EMOTICON"

        if tweetlist[i] in NEG1:
           tweetlist[i] = "NEGATIVE1 EMOTICON"

    if tweetlist[i] in NEG2:
        tweetlist[i] = "NEGATIVE2 EMOTICON"

    if tweetlist[i] in NEU:
        tweetlist[i] = "NEUTRAL EMOTICON"
    
    tw = " ".join(tweetlist)
    return tw
