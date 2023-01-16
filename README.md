# Twitter Handle Checker (Username Availability)

![Twitter Handle Checker (Username Availability)](https://github.com/verfasor/twitter-handle-checker/blob/main/twitter-handle-checker.gif)

According to birdman, Twitter will soon start freeing the name space of inactive accounts. Here's a script to check if your favorite Twitter handle is available, from the command line OR receive an email notification when the username is available.

## Prerequisites & dependencies

- Access to the [Twitter API](https://developer.twitter.com/en/portal/petition/essential/basic-info)
- Python (tested on v3.10.8)
- Tweepy (tested on v4.12.1) (`pip install tweepy`)
- schedule 1.1.0 (`pip install schedule`)

## How-to

1. Get your Twitter `consumer_key`, `consumer_secret`, `access_token`, and `access_token_secret`
2. Install Tweepy `pip install tweepy`
3. Edit the [twitter-checker.py](https://github.com/verfasor/twitter-handle-checker/blob/main/twitter-checker.py) script and add the variables
4. Run `python3 twitter-checker.py username` and wait for the results

## Recommended 

- Make twitter-checker.py executable, `chmod +x twitter-checker.py`
- Add twitter-checker.py to your dot file (.zshrc, .bashrc, etc.) 
- Set an alias like `alias twitter="python3 twittercheck.py"`
- Now you can check Twitter username availability with the command `twitter username`

## Get email notifications

Use the [twitter-checker-mail.py](https://github.com/verfasor/twitter-handle-checker/blob/main/twitter-checker-mail.py) and tweak the variables. You'll receive an email when the username is available. Be mindful about `schedule.every(5).minutes.do(check_user)`, though. Every five minutes, an API call is made. 
