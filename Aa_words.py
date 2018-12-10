import json
import string
import nltk
import re
# nltk.download()

def get_tweet_text(tweet):
    '''
    parameter: a tweet object in json form
    return: the tweet text
    '''
    if 'retweeted_status' in tweet:
        tweet = tweet['retweeted_status']
    if 'extended_tweet' in tweet:
        return tweet['extended_tweet']['full_text']
    else:
        return tweet['text']

def preprocess(text):
    '''
    parameter: a string
    return: that string stripped of punctuation and digits
    '''
    punc = string.punctuation
    digi = string.digits
    table_punc = str.maketrans(punc, len(punc)*' ')
    table_digi = str.maketrans(digi, len(digi)*' ')
    answer = text.translate(table_punc)
    answer = answer.translate(table_digi)
    return answer

def remove_special(text):
    '''
    parameter: a string
    return: that string with special characters replaced by ' ' (i.e. no emojis)
        ref: https://stackoverflow.com/questions/20078816/replace-non-ascii-characters-with-a-single-space
    '''
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

def remove_link(text):
    '''
    parameter: a string
    return: that string with any links replaced by ' '
        ref: https://stackoverflow.com/questions/24399820/expression-to-remove-url-links-from-twitter-tweet/24399874
    '''
    return re.sub(r'http\S+', ' ', text)

def replace_amp_charcode(text):
    '''
    parameter: a string
    return: that string with any '&amp;' html character code replaced by '&'
    '''
    return re.sub(r'&amp;', '&', text)

def remove_stopwords(words):
    '''
    parameter: a list of strings
    return: that list with stop words removed
    '''
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.extend(['would', 'could'])                    # from Gene's text_part1_nltk_textblob_wordcloud
    return [word for word in words if word not in stopwords and len(word) > 1]

def stem_words(words):
    '''
    parameter: a list of strings
    return: that list with all words stemmed
    '''
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()
    stemmed = []
    for word in words:
        stemmed.append(ps.stem(word))
    return stemmed

def all_words(filename, no_stopwords, stem = False):
    '''
    parameter: string filename
               boolean flag to indicate inclusion of stopwords (default no stopwords)
               boolean flag to indicate stemming of words (default no stem)
    return: a list of all words processed according to the flags
    '''
    with open(filename) as infile:  # open the file
        tweets = json.load(infile)
    words = []
    for tweet in tweets:    # iterate over json tweets
        tweet_text = preprocess(remove_special(replace_amp_charcode(remove_link(get_tweet_text(tweet)))))    # get tweet and remove all noise
        tweet_words = nltk.word_tokenize(tweet_text.lower())    # tokenize tweet into list of words
        words += tweet_words
    if no_stopwords:    # remove stopwords if necessary
        words = remove_stopwords(words)
    if stem:
        words = stem_words(words)
    return words

# return top 10 words
def ten_words(filename, no_stopwords = True): 
    words = all_words(filename, no_stopwords)
    return nltk.FreqDist(words).most_common(10)