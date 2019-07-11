import tweepy

# We use OAuth 2 authentication in this app for read-only access.

# For OAuth 2 and OAuth 1 authentication; needed for read-only access
auth = tweepy.AppAuthHandler("Lfdjsisd57ew2Bc0nvEXeyBXL", "THNlus5JSo3mSJvli1y0Xgwe8adIjwlAKWHHuFhaagUWFywE05")

# For OAuth 1 authentication; unnecessary for us right now
# auth = tweepy.OAuthHandler("Lfdjsisd57ew2Bc0nvEXeyBXL", "THNlus5JSo3mSJvli1y0Xgwe8adIjwlAKWHHuFhaagUWFywE05")
# auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Example OAuth 2 authentication function
for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
    print(tweet.text)

# Example OAuth 1 authentication function
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
