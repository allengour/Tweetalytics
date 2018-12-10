import json
import nltk
import Aa_words

def get_influence_score(tweet):
    '''
    parameter: tweet json object
    return: influence score of that tweet (the original tweet, in case of a retweet)
            influence score = # retweets + # replies + # favorites + # quotes
    '''
    if 'retweeted_status' in tweet:
        tweet = tweet['retweeted_status']
    return tweet['retweet_count'] + tweet['reply_count'] + tweet['favorite_count'] + tweet['quote_count']

def top_tweet(filename):
    '''
    parameter: string filename
    return: tweet with the highest influence score
    '''
    with open(filename) as infile:
        tweets = json.load(infile)
    high = 0
    top = ''
    for tweet in tweets: # get tweet with highest score
        score = get_influence_score(tweet)
        if score > high:
            high = score
            top = tweet
    # get original author
    if 'retweeted_status' in top:
        top = top['retweeted_status']
    author = top['user']['screen_name']
    return {    # return info of that tweet
        'text': Aa_words.replace_amp_charcode(Aa_words.get_tweet_text(top)), # get original text
        'retweets': top['retweet_count'],
        'replies': top['reply_count'],
        'favorites': top['favorite_count'],
        'quotes': top['quote_count'],
        'author': author,
        'score': high
    }
    