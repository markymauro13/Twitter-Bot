import tweepy

print("this is my twitter bot")

CONSUMER_KEY = 'kwbh7wUyLFhsmZ9WYzahXXRly'
CONSUMER_SECRET = 'Mt1N8cSVUla6YKw5D3bg5cNymXatigZMwSDObKDfCWafTQg7EY'
ACCESS_KEY = '3045426691-sm1ENWdt14Mr989tD7MJX3iz5AkNgpdLnliguWS'
ACCESS_SECRET = 'vrBRatAVVgnl9YcOZ6vJbtGd59pjmWfShDAyX2tUbBsZ5'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("Y'all are still tweeting on iPhones? LMFAO!!!!!")