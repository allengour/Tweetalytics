import nltk
import Aa_words
import Ab_hashtags
import Ac_mentions
import Ad_author
import Ae_influence
import B_wordcloud
import C_sentiments

def analytics(file, outname):
    '''
    parameters: file - the string filename
                outname - string prefix of output files
    return: None - prints all the important bits
    '''
    out = open('{}.txt'.format(outname), 'w')
    # --PART A--
    out.write('--PART A--\n')
    # a.
    out.write('\na. 10 most popular words\n')

    out.write('\twith stopwords:\n')
    words_with = Aa_words.ten_words(file, False)
    for i in range(len(words_with)):
        out.write('\t\t{}. {}: {}\n'.format(i, words_with[i][0], words_with[i][1]))
    
    #allen
    out.write('\n')
    for i in range(len(words_with)):
        out.write('{} ({}), '.format(words_with[i][0], words_with[i][1]))
    out.write('\n')
    
    out.write('\twithout stopwords:\n')
    words_without = Aa_words.ten_words(file)
    for i in range(len(words_without)):
        out.write('\t\t{}. {}: {}\n'.format(i, words_without[i][0], words_without[i][1]))

    #allen
    out.write('\n')
    for i in range(len(words_without)):
        out.write('{} ({}), '.format(words_without[i][0], words_without[i][1]))
    out.write('\n')

    # b.
    out.write('\nb. 10 most popular hashtags:\n')
    hashtags = Ab_hashtags.ten_hashtags(file)
    for i in range(len(hashtags)):
        out.write('\t{}. {}: {}\n'.format(i, hashtags[i][0], hashtags[i][1]))

    #allen
    out.write('\n')
    for i in range(len(hashtags)):
        out.write('{} ({}), '.format(hashtags[i][0], hashtags[i][1]))
    out.write('\n')

    # c.
    out.write('\nc. 10 most frequently mentioned usernames:\n')
    mentions = Ac_mentions.ten_mentions(file)
    for i in range(len(mentions)):
        out.write('\t{}. {}: {}\n'.format(i, mentions[i][0], mentions[i][1]))

    #allen
    out.write('\n')
    for i in range(len(mentions)):
        out.write('{} ({}), '.format(mentions[i][0], mentions[i][1]))
    out.write('\n')

    # d.
    out.write('\nd. most frequent author:\n')
    author = Ad_author.top_author(file)
    out.write('@{}, who tweeted {} times!\n'.format(author[0], author[1]))

    # e.
    out.write('\ne. most influential tweet:\n')
    tweet = Ae_influence.top_tweet(file)
    out.write('"{}" tweeted by @{}, with {} retweets, {} replies, {} favorites, and {} quotes for a total influence score of {}!\n'
    .format(tweet['text'], tweet['author'], tweet['retweets'], tweet['replies'], tweet['favorites'], tweet['quotes'], tweet['score']))

    # -- PART B --
    out.write('\n--PART B--\n')
    B_wordcloud.gen_wordcloud(file, '{}_cloud.png'.format(outname))
    out.write('wordcloud created under file named \'{}_cloud.png\'\n'.format(outname))

    # -- PART C --
    out.write('\n--PART C--\n')
    scores = C_sentiments.get_subpol(C_sentiments.get_tweets(file), '{}_sub.png'.format(outname), '{}_pol.png'.format(outname))
    out.write('subjectivity and polarity histograms created under files named \'{}_sub.png\' and \'{}.pol.png\'\n'.format(outname, outname))
    out.write('average subjectivity: {}\n'.format(scores['subjectivity']))
    out.write('average polarity: {}'.format(scores['polarity']))

# 7200 files
analytics('tweets/lyft_7200.json', 'analytics/lyft_7200')
analytics('tweets/uber_7200.json', 'analytics/uber_7200')

# 2400 files
analytics('tweets/lyft_2400_1.json', 'analytics/lyft_2400_1')
analytics('tweets/lyft_2400_2.json', 'analytics/lyft_2400_2')
analytics('tweets/lyft_2400_3.json', 'analytics/lyft_2400_3')

analytics('tweets/uber_2400_1.json', 'analytics/uber_2400_1')
analytics('tweets/uber_2400_2.json', 'analytics/uber_2400_2')
analytics('tweets/uber_2400_3.json', 'analytics/uber_2400_3')
