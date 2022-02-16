import tweepy
import credentials

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

def detector():
    """
    Detects if any recent tweets contain any top 30 crypto current names/acrnoms
    """

    api = tweepy.API(auth)

    for status in api.user_timeline(screen_name = 'elonmusk', count = 1):
        print(status.text)


detector()