import tweepy
from listener import SimpleListener
from decouple import config


def create_client():
    consumer_key = config('TWITTER_CONSUMER_KEY', default='')
    consumer_secret = config('TWITTER_CONSUMER_SECRET', default='')

    access_key = config('TWITTER_ACCESS_TOKEN', default='')
    access_secret = config('TWITTER_ACCESS_TOKEN_SECRET', default='')
    # Authorization to consumer key and consumer secret
    return tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,
                         access_token=access_key, access_token_secret=access_secret)


if __name__ == "__main__":
    client = create_client()
    tweepy_stream = SimpleListener(config('BEARER_TOKEN', default=''), client)
    tweepy_stream.add_rules(tweepy.StreamRule(
        '#PyConKE2022 OR #PyconKe2022 OR #PyconKe'))
    tweepy_stream.filter()
