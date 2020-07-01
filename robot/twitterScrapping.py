import tweepy
import sys
from .models import Tweets
from config import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def getTweets(counts):

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print('Authentication Successful')
    except:
        print('Error while authenticating API')
        sys.exit(1)

    covid_tweets = tweepy.Cursor(api.search, q='فيروس كورونا').items(counts)
    for tweet in covid_tweets:
        tweetObj = Tweets.objects.create(
            content=tweet.text, date=tweet.created_at, proprio=tweet.user.name)
        tweetObj.save()
