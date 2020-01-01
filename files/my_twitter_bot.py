import tweepy
import time

print("this is my twitter bot")

'''the x's represent the keys. uncomment this if wanting to use

CONSUMER_KEY = 'x'
CONSUMER_SECRET = 'x'
ACCESS_KEY = 'x-x'
ACCESS_SECRET = 'x'

'''

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
