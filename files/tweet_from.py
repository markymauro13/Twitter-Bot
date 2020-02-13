import tweepy

print("this is my twitter bot")

CONSUMER_KEY = 'x'
CONSUMER_SECRET = 'x'
ACCESS_KEY = 'x'
ACCESS_SECRET = 'x'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("tweet")
