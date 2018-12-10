import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import Aa_words

def get_tweets(filename):
    '''
    parameter: string filename
    return: list of tweets in file
    '''
    with open(filename) as infile:
        raw = json.load(infile)
    tweets = []
    for r in raw:   # call functions from other file
        tweets.append(Aa_words.preprocess(Aa_words.remove_special(Aa_words.remove_link(Aa_words.replace_amp_charcode(Aa_words.get_tweet_text(r))))))
    return tweets

def get_subpol(tweets, sub_png, pol_png):
    '''
    parameter: list of string tweets and string output filename
    return: a dict of the average subjectivity and polarity
            output a subjectivity histogram named sub_png and polarity histogram named pol_png
    '''
    sub_list = []
    pol_list = []
    for tweet in tweets:
        tb = TextBlob(tweet)
        sub_list.append(tb.sentiment.subjectivity)
        pol_list.append(tb.sentiment.polarity)
    # subjectivity histogram
    plt.hist(sub_list, bins=10)
    plt.xlabel('subjectivity score')
    plt.ylabel('tweet count')
    plt.grid(True)
    plt.savefig(sub_png)
    plt.close()
    # polarity histogram
    plt.hist(pol_list, bins=10)
    plt.xlabel('polarity score')
    plt.ylabel('tweet count')
    plt.grid(True)
    plt.savefig(pol_png)
    plt.close()
    return {
        'subjectivity': sum(sub_list)/len(sub_list),    # avg subjectivity
        'polarity': sum(pol_list)/len(pol_list)         # avg polarity
    }