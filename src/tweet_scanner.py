import tweepy
import credentials
from pynotifier import Notification

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

detected_words = ['']

def notification():
    det = ''
    for x in detected_words:
        det += ',' + x

    Notification(
        title='Elon Tweet Crypto Notication',
        description=det,
        icon_path='tweet.ico',  # On Windows .ico is required, on Linux - .png
        duration=10,  # Duration in seconds
        urgency='normal'
    ).send()
    detected_words.clear()

def detector():
    """
    Detects if any recent tweets contain any top 30 crypto current names/acrnoms
    if so will activate notifcation
    """

    api = tweepy.API(auth)

    crppto_arco_lowered = [x.lower() for x in credentials.crypto_acronym]
    crypto_full_lowered = [x.lower() for x in credentials.cryptos_full_name]
    # Turns list to lower case, for standarization
    for status in api.user_timeline(screen_name = 'elonmusk', count = 1):

        print(status.text)
        for tweet_message in status.text.split():
            if tweet_message.lower() in (crypto_full_lowered): #String-List
                detected_words.append(tweet_message)
                notification()

            elif tweet_message in (crppto_arco_lowered):
                detected_words.append(tweet_message)
                notification()

            else:
                print("Negative")

detector()