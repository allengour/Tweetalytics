import json
import nltk

def get_author(tweet):
    '''
    parameter: tweet json object
    return: the author of that tweet (the retweeter, in case of a retweet)
    '''
    return tweet['user']['screen_name'] # the @ name

def all_authors(filename):
    '''
    parameter: string filename
    return: list of all authors
    '''
    with open(filename) as infile:
        tweets = json.load(infile)
    authors = []
    for tweet in tweets:
        authors.append(get_author(tweet))
    return authors

# return the most frequent author
def top_author(filename):
    authors = all_authors(filename)
    return nltk.FreqDist(authors).most_common(1)[0]
