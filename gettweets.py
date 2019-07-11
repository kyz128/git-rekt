import tweepy
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import os
import json
# We use OAuth 2 authentication in this app for read-only access.

# For OAuth 2 and OAuth 1 authentication; needed for read-only access
auth = tweepy.AppAuthHandler("Lfdjsisd57ew2Bc0nvEXeyBXL", "THNlus5JSo3mSJvli1y0Xgwe8adIjwlAKWHHuFhaagUWFywE05")

# For OAuth 1 authentication; unnecessary for us right now
# auth = tweepy.OAuthHandler("Lfdjsisd57ew2Bc0nvEXeyBXL", "THNlus5JSo3mSJvli1y0Xgwe8adIjwlAKWHHuFhaagUWFywE05")
# auth.set_access_token(access_token, access_secret)

auth_api = tweepy.API(auth)

f = open("team_names.txt", "r")
text = f.read()
#print(text.split())

account_list = text.split()


if len(account_list) > 0:
  for target in account_list:
    person_dict = dict()
    person_dict["contentItems"] = []
    #print("Getting data for " + target)
    try:
        item = auth_api.get_user(target, tweet_mode='extended')
    except:
        continue

    file_name = target+"_profile.json"

    """if os.path.exists(file_name):
        os.remove(file_name)
    text_file = open(file_name, "a")"""

    """account_created_date = item.created_at
    delta = datetime.utcnow() - account_created_date
    account_age = delta.days"""

    tweet_count = 0
    #end_date = datetime.utcnow() - timedelta(days=account_age)
    #for status in auth_api.user_timeline(id = target, tweet_mode="extended", count = 5000):
    for status in tweepy.Cursor(auth_api.user_timeline, screen_name= target, tweet_mode="extended", count = 5000).items():
        cont = dict()
        s = status.full_text
        if s.startswith("RT @") == False:
            check = s.split()
            if check[-1].startswith("https://") == True:
                check.pop()
                cont["content"] = " ".join(check)
                #text_file.write(" ".join(check)+"\n")
                #print(" ".join(check))
            else:
                cont["content"] = s

            person_dict["contentItems"].append(cont)
                #text_file.write(s+"\n")
                #print(s)
        tweet_count += 1
    with open(file_name, 'w') as fp:
        json.dump(person_dict, fp)

        #if status.created_at < end_date:
        #    break
    #text_file.close()
    #print(tweet_count)
