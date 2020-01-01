import tweepy
import time

print("this is my twitter bot")

CONSUMER_KEY = 'kwbh7wUyLFhsmZ9WYzahXXRly'
CONSUMER_SECRET = 'Mt1N8cSVUla6YKw5D3bg5cNymXatigZMwSDObKDfCWafTQg7EY'
ACCESS_KEY = '3045426691-sm1ENWdt14Mr989tD7MJX3iz5AkNgpdLnliguWS'
ACCESS_SECRET = 'vrBRatAVVgnl9YcOZ6vJbtGd59pjmWfShDAyX2tUbBsZ5'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

def reply_to_tweets():
    print('retrieving and replying to tweets')
    for mention in mentions:
        print(str(mention.id) + " - " +  mention.text)
        if 'helloworld' in mention.text.lower():
            print('found #helloworld!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + '#helloworld back to you, this is a bot.', mention.id)

while True:
    reply_to_tweets()
    time.sleep(2)