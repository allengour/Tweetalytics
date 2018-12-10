import os
import json

# parameter: path as a string
# return None, create a file with x JSON files merged into one
def merge_json(path, dest, keyword):
    files = sorted(os.listdir(path))
    # initiate empty lists
    tweets_7200 = []
    tweets_2400_1, tweets_2400_2, tweets_2400_3 = [], [], []
    tweets_1000 = []
    i = 0   # counter for file number
    while len(tweets_7200) < 7200:
        if not files[i].endswith('.json'):  # skip if not json file
            i += 1
            continue
        with open('{}/{}'.format(path, files[i])) as infile:
            tweets = json.load(infile)
            # add tweets to 7200 file
            tweets_7200 += tweets
            # partition into appropriate 2400 file
            if len(tweets_2400_1) < 2400:
                tweets_2400_1 += tweets
            elif len(tweets_2400_2) < 2400:
                tweets_2400_2 += tweets
            else:
                tweets_2400_3 += tweets
            # 1000 file
            if len(tweets_1000) < 1000:
                tweets_1000 += tweets
            # print('\nfile #{}: {} (length: {})'.format(i, files[i], len(tweets)))
            # print('  tweets_7200 length: {}'.format(len(tweets_7200)))
            # print('  tweets_2400_1 length: {}'.format(len(tweets_2400_1)))
            # print('  tweets_7200_2 length: {}'.format(len(tweets_2400_2)))
            # print('  tweets_7200_3 length: {}'.format(len(tweets_2400_3)))
            # print('  tweets_1000 length: {}'.format(len(tweets_1000)))
        i += 1
    
    with open('{}/{}_7200.json'.format(dest, keyword), 'w') as outfile:
        json.dump(tweets_7200, outfile, indent=4)
    with open('{}/{}_2400_1.json'.format(dest, keyword), 'w') as outfile:
        json.dump(tweets_2400_1, outfile, indent=4)
    with open('{}/{}_2400_2.json'.format(dest, keyword), 'w') as outfile:
        json.dump(tweets_2400_2, outfile, indent=4)
    with open('{}/{}_2400_3.json'.format(dest, keyword), 'w') as outfile:
        json.dump(tweets_2400_3, outfile, indent=4)
    with open('{}/{}_1000.json'.format(dest, keyword), 'w') as outfile:
        json.dump(tweets_1000, outfile, indent=4)
    

lyft = '/Users/allengour/Documents/UNIVERSITY OF BRITISH COLUMBIA/2018W/Term 1/COMM 337/Project/tweets_lyft'
uber = '/Users/allengour/Documents/UNIVERSITY OF BRITISH COLUMBIA/2018W/Term 1/COMM 337/Project/tweets_uber'

merge_json(uber, 'tweets', 'uber')
merge_json(lyft, 'tweets', 'lyft')

# verifying
def verify(file):
    with open(file) as infile:
        tweets = json.load(infile)
        print('{} FILE LENGTH: {}'.format(file, len(tweets)))

verify('tweets/uber_7200.json')
verify('tweets/uber_2400_1.json')
verify('tweets/uber_2400_2.json')
verify('tweets/uber_2400_3.json')
verify('tweets/uber_1000.json')

verify('tweets/lyft_7200.json')
verify('tweets/lyft_2400_1.json')
verify('tweets/lyft_2400_2.json')
verify('tweets/lyft_2400_3.json')
verify('tweets/lyft_1000.json')