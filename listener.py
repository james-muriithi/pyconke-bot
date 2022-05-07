import tweepy


class SimpleListener(tweepy.StreamingClient):
    def __init__(self, bearer_token, tweepy_client):
        self.tweepy_client = tweepy_client
        self.me = self.tweepy_client.get_me().data

        response = {'expansions':'author_id'}
        super().__init__(bearer_token=bearer_token, return_type=response)

    # When a user tweeets
    def on_tweet(self, status):
        if self.me.id is not status.author_id:
            try:
                self.tweepy_client.retweet(tweet_id=status.id)
                self.tweepy_client.like(tweet_id=status.id)
            except Exception as e:
                print(e)

    def on_errors(self, status_code):
        print("Error in twitter stream: %s", status_code)
        return super().on_error(status_code)
