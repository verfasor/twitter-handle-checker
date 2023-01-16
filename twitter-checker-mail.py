# m64.in, 2023
# The script will check username availability every 5 mins.
# And if the username is available, it'll send you an email.
# Grab your credentials from https://developer.twitter.com/en/portal/petition/essential/basic-info
# Note: import the API keys as environment variables

import tweepy
import time
import schedule
import smtplib
from email.message import EmailMessage

# Tested on a self-hosted setting
# If gmail is your thing, try the app password. I haven't tested it personally, though
mail_server = "mail.example.com" #or smtp.gmail.com
port = 465 #change accordingly
email_address = "alerts@example.com" #sender
email_password = "password"
receiver_address = "you@example.com" 

# Define the username you want to monitor
username = 'theusernameyouneed'

# Set up your Tweepy API client
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Twitter auth
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

# Connect API
api = tweepy.API(auth)

# Function to check username availability
def check_user():
    try:
        user = api.get_user(screen_name=username)
        print (f"The twitter handle @{username} is active.")
    except tweepy.errors.TweepyException as e:
        if e.response.status_code == 404:
            print(f"The twitter handle @{username} does not exist. Go get it now!")
            # Create email
            msg = EmailMessage()
            msg['Subject'] = "🐦 BREAKING: @" + username + " handle available"
            msg['From'] = email_address
            msg['To'] = receiver_address
            
            # If you want to send it to your team member(s)
            #recipients = ['alice@example.com', 'bob@example.com']
            #msg['To'] = ", ".join(recipients)
            
            msg.set_content("Hey, the handle @" + username + " is available now.")
            
            # Send email. Set mail server and port number correctly
            with smtplib.SMTP_SSL(mail_server, port) as smtp:
                smtp.login(email_address, email_password)
                smtp.send_message(msg)
                print(f"Mail sent.")                    
        elif e.response.status_code == 403:
            print(f"The twitter handle @{username} is a suspended account.")
        else:
            print(f"Error: {e.response.status_code}")
# Let it monitor every 5 minutes
schedule.every(5).minutes.do(check_user) 

while True:
    schedule.run_pending()
    time.sleep(1)      
