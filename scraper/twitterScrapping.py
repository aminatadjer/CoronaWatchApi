import tweepy
import sys
from robot.models import Veille
from config import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def getTweets(counts=30):

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
        url=f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
        if not Veille.objects.filter(url=url).exists():
            tweetObj = Veille.objects.create(description=tweet.text, date=tweet.created_at , titre=tweet.user.name, url=url, type="twitter")
            tweetObj.save()
