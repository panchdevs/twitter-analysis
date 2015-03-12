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

    # trim
    tweet = tweet.strip('\'"')

    return tweet
