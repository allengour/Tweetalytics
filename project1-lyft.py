# from twython package import TwythonStreamer module
from twython import TwythonStreamer
import sys
import json
import time
import datetime

# global variable to store tweets
tweets = []

# we are inheriting from TwythonStreamer class
# Github Code: https://github.com/ryanmcgrath/twython/blob/master/twython/streaming/api.py
class MyStreamer(TwythonStreamer):
    '''our own subclass of TwythonStreamer'''

    # overriding
    def on_success(self, data):
        # check if the received tweet dictionary is in English
        if 'lang' in data and data['lang'] == 'en':
            tweets.append(data)
            print('received tweet #', len(tweets), data['text'][:100])
            #time.sleep(1)

        # if we have enough tweets, store it into JSON file and disconnect API
        if len(tweets) >= 100:
            self.store_json()
            self.disconnect()

    # overriding
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

    # our new method to store tweets into JSON file
    def store_json(self):
        now = datetime.datetime.now()
        with open('{}-{}-{}-{}-{}.json'.format(now.year, now.month, now.day, now.hour, keyword), 'w') as f:
            json.dump(tweets, f, indent=4)

# check if we are running this code as top-level module
if __name__ == '__main__':

    #with open('your_twitter_credentials.json', 'r') as f:
    with open('twitter_credentials.json', 'r') as f:
        credentials = json.load(f)

    # create your own app to get consumer key and secret
    CONSUMER_KEY = credentials['CONSUMER_KEY']
    CONSUMER_SECRET = credentials['CONSUMER_SECRET']
    ACCESS_TOKEN = credentials['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']

    # Twitter Streaming API needs all four credentials
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # we will get system arguments to get keyword
    # you can run this code by:
    # python 3_test_twitter_stream.py MyKeyword
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    else:
        keyword = 'Uber'

    # Github Code: https://github.com/ryanmcgrath/twython/blob/master/twython/streaming/api.py
    # Accepted parameters: https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter
    stream.statuses.filter(track=keyword)
