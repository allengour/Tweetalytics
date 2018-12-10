import json
import nltk

def get_hashtags(tweet):
    '''
    parameter: tweet json object
    return: list of hashtags in that tweet
    '''
    if 'retweeted_status' in tweet:
        tweet = tweet['retweeted_status']
    if 'extended_tweet' in tweet:
        hashtags = tweet['extended_tweet']['entities']['hashtags']
    else:
        hashtags = tweet['entities']['hashtags']
    tags = []
    for hashtag in hashtags:
        tags.append(hashtag['text'])    # get hashtag text only
    return tags

def all_hashtags(filename):
    '''
    parameter: string filename
    return: list of all hashtags
    '''
    with open(filename) as infile:
        tweets = json.load(infile)
    hashtags = []
    for tweet in tweets:
        hashtags += get_hashtags(tweet)
    return hashtags

# return top 10 hashtags
def ten_hashtags(filename):
    hashtags = all_hashtags(filename)
    return nltk.FreqDist(hashtags).most_common(10)