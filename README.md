# twitter-analysis
Sentiment Analysis of the Twitter Live Stream

Requirements
------------
* mongodb
* python 3
* pymongo
* tweepy

Environment Setup
-----------------
1. Install all the necessary requirements
2. Clone this repository  
`git clone https://github.com/panchdevs/twitter-analysis.git`
3. Get your api keys from Twitter ([HOWTO](http://www.74by2.com/2014/06/easily-g    et-twitter-api-key-api-secret-access-token-access-secret-pictures/))
4. Enter your keys in `tweet_collector.py` and change the location of the mongodb server if required

How to run
----------
Simply run the `tweet_collector.py` script to store tweets in the database.  
`python tweet_collector.py`
