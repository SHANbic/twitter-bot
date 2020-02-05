import tweepy
import time

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)


"""
# tweets
public_tweets = api.home_timeline()
for tweet in public_tweets:
  print(tweet.text)
"""



"""
# user
user = api.me()
followers = user.followers()
for follower in followers:
  print(follower.name)
"""



"""
# friends
friends = user.friends()
for friend in friends:
  print(friend.name)
"""



"""
# follow a follower
def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
      time.sleep(300)
  except StopIteration:
    return

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
  if follower.name == 'JavaScript Kingdom':
    follower.follow()
    break
"""



"""
# like tweets
search_string = 'javascript'
numberOfTweets = 10

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
  try:
    tweet.favorite()
    print(tweet.text)
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break
"""