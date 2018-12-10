import json
import nltk

def get_mentions(tweet):
    '''
    parameter: tweet json object
    return: list of mentions in that tweet
    '''
    if 'retweeted_status' in tweet:
        tweet = tweet['retweeted_status']
    if 'extended_tweet' in tweet:
        mentions = tweet['extended_tweet']['entities']['user_mentions']
    else:
        mentions = tweet['entities']['user_mentions']
    usernames = []
    for mention in mentions:
        usernames.append(mention['screen_name'])    # get username only
    return usernames

def all_mentions(filename):
    '''
    parameter: string filename
    return: list of all mentions
    '''
    with open(filename) as infile:
        tweets = json.load(infile)
    mentions = []
    for tweet in tweets:
        mentions += get_mentions(tweet)
    return mentions

# return top 10 hashtags
def ten_mentions(filename):
    mentions = all_mentions(filename)
    return nltk.FreqDist(mentions).most_common(10)
