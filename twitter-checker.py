# Verfasor.com, 2023
# The script lets you check Twitter username status and availability
# Grab your credentials from https://developer.twitter.com/en/portal/petition/essential/basic-info
# Note: import the API keys keys as environment variables

import sys
import tweepy

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = input("Enter username:")

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

try:
    user = api.get_user(screen_name=username)
    print ('\33[32m' + '\33[1m' +  f"User {username} is active" + '\033[0m')
except tweepy.errors.TweepyException as e:
    if e.response.status_code == 404:
        print('\33[90m' + '\33[1m' +  f"User {username} does not exist." + '\033[0m')
    elif e.response.status_code == 403:
        print('\033[91m' + '\33[1m' + f"User {username} is still suspended." + '\033[0m')
    else:
        print(f"Error: {e.response.status_code}")