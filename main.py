import os
import sys
import schedule
import time
from dotenv import load_dotenv
import tweepy

load_dotenv()

MAX_TWEETS = 1
keyword = 'cosmetic' or 'beauty' or 'deals' or 'beauty sale'
# 5000000000000000000000

# Api Keys
twitter_api_key = os.getenv('CONSUMER_KEY')
twitter_api_secret = os.getenv('CONSUMER_SECRET')
twitter_api_token = os.getenv('ACCESS_TOKEN')
twitter_api_secret_token = os.getenv('ACCESS_TOKEN_SECRET')

# Twitter API
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_api_token, twitter_api_secret_token)
twitter_api = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)


# #
#   Check for new tweets
# #

# 1. First check last 100 followers from sephora & other accounts.
# 2. Follow all the accounts
# 3. Filter tweets based on hashtags like #beauty, #cosmetics
# 4. Like every tweet and comment "This look beautiful!"
# Once bot has liked & commented on about 500 tweets


def fetchTweets(twitter_api):
    # Define vars
    twitterUser = ''

    # Fetch x amount of tweets and loop through them
    for tweet in tweepy.Cursor(
        twitter_api.search,
        q=('cosmetics OR beauty OR beauty sale OR deals OR beauty deals'),
        rpp=100
    ).items(MAX_TWEETS):
        try:
            # Current tweets poster username
            twitterUser = tweet.user.screen_name

            # Tweet reply
            tweet_reply = 'check out glitzher.com!'

            # Like each tweet
            print(f"Liking tweet {tweet.id} of {twitterUser}")
            twitter_api.create_favorite(tweet.id)

            # Reply to each tweet
            twitter_api.update_status(
                status=tweet_reply, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)

            # Confirmation Success
            print('Successfully liked and commented!')

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


fetchTweets(twitter_api)


# def followUsersFromBigAccounts(twitter_api):
#     # Define vars
#     twitterUsers = ['beautydealsbff', 'Sephora']

#     # For each follower of twitterUser, follow them
#     for user in twitterUsers:
#         for follower in twitter_api.followers(user):
#             time.sleep(3)
#             # Skip my account
#             if follower.screen_name == 'GlitzherBrand':
#                 pass
#             else:
#                 twitter_api.create_friendship(follower.screen_name)
#                 print('Followed :', follower.screen_name)


# followUsersFromBigAccounts(twitter_api)
