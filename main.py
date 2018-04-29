import sys
from TweetCriteria import TweetCriteria
from TweetManager import TweetManager
def fetch_tweet(keyword,starting_date,end_date,count_tweets):

	def printTweet(descr, t):
		print(descr)
		print("Username: %s" % t.username)
		print("Retweets: %d" % t.retweets)
		print("Date: %s" % t.date)
		print("Text: %s" % t.text)
		print("Mentions: %s" % t.mentions)
		print("Hashtags: %s\n" % t.hashtags)

	# Example 1 - Get tweets by query search
	tweetCriteria = TweetCriteria().setQuerySearch(keyword).setSince(starting_date).setUntil(end_date).setMaxTweets(count_tweets)
	tweet = TweetManager.getTweets(tweetCriteria)
	print(len(tweet))
	all_tweets=[]
	for t in tweet:
		# printTweet("### Example 2 - Get tweets by query search [demonetization]", t)
		all_tweets.append(t.text)
	return all_tweets

	# Example 2 - Get tweets by username and bound dates
	#tweetCriteria = TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
	#tweet = TweetManager.getTweets(tweetCriteria)[0]

	#printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)
