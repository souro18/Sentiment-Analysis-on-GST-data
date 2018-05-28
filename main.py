import sys
from TweetC import TweetC
from TweetManage import TweetManage
def fetch_tweet(keyword,starting_date,end_date,count_tweets):

	def printTweet(descr, t):
		print(descr)
		print("Username: %s" % t.username)
		print("Retweets: %d" % t.retweets)
		print("Date: %s" % t.date)
		print("Text: %s" % t.text)
		print("Mentions: %s" % t.mentions)
		print("Hashtags: %s\n" % t.hashtags)

	tweetCriteria = TweetC().setQuerySearch(keyword).setSince(starting_date).setUntil(end_date).setMaxTweets(count_tweets)
	tweet = TweetManage.getTweets(tweetCriteria)
	print(len(tweet))
	all_tweets=[]
	for t in tweet:
		all_tweets.append(t.text)
		#print(t.text)
	return all_tweets

