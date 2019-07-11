import tweepy
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
# We use OAuth 2 authentication in this app for read-only access.

# For OAuth 2 and OAuth 1 authentication; needed for read-only access
auth = tweepy.AppAuthHandler("Lfdjsisd57ew2Bc0nvEXeyBXL", "THNlus5JSo3mSJvli1y0Xgwe8adIjwlAKWHHuFhaagUWFywE05")

# For OAuth 1 authentication; unnecessary for us right now
# auth = tweepy.OAuthHandler("Lfdjsisd57ew2Bc0nvEXeyBXL", "THNlus5JSo3mSJvli1y0Xgwe8adIjwlAKWHHuFhaagUWFywE05")
# auth.set_access_token(access_token, access_secret)

auth_api = tweepy.API(auth)


account_list = ["KingJames"]


if len(account_list) > 0:
  for target in account_list:
    #print("Getting data for " + target)
    #item = auth_api.get_user(target, tweet_mode='extended')
    #print(item)
    #print("name: " + item.name)
    #print("screen_name: " + item.screen_name)

    tweet_count = 0
    end_date = datetime.utcnow() - timedelta(days=30)
    for status in auth_api.user_timeline(id = target, tweet_mode="extended", count = 200):
        s = status.full_text
        if s.startswith("RT @") == False:
            check = s.split()
            if check[-1].startswith("https://") == True:
                check.pop()
                print(" ".join(check))
            else:
                print(s)
            tweet_count += 1
        if status.created_at < end_date:
            break
    print(tweet_count)


