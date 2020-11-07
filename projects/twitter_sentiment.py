import tweepy 
from textblob import TextBlob

consumer_key = 'kDihXHFjpWVvRu23n0QYeNOdQ'
consumer_secret = 'UYJTpNFWtVTiJZRrx2vO4ZcqN7VC00LakNlV8iTszao5FdRB0K'

access_token = '70255397-EBbsmtkiqDB7jEmEGmtU0rTERGrVt9Pz6VtEhxZ5O'
access_token_secret = 'Eab7ObDWgvY0YQzpPUy3tfMdraoDBMu8cbYd0CpPwPJFL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(q='Bitcoin', count=100)

count = 0
sentiment_avg = 0

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	#print(analysis.sentiment)
	count = count + 1
	sentiment_avg = sentiment_avg + analysis.sentiment.polarity

sentiment_avg = sentiment_avg/count
print(sentiment_avg)