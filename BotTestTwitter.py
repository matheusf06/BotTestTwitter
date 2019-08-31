import tweepy
import time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

user = api.me()

number = 0

x = 1
while True:
    numberString = str(number)
    api.update_status('Post in Twiiter with Tweepy!#Test' + numberString)
    number += 1
    time.sleep(15)
