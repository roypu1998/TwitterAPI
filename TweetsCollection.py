import tweepy
import csv

'''
App Name = TweetCollect_karin_roi
'''

consumer_key='xvyJ2qK09KL4VPqeWlvcmLT7y'
consumer_secret='PUfNF2VtdkIAAKy7xpoJcdXkjyHm8pnNQnZZwXkWdCS9kGjfEm'
access_token='1462773831932825601-Y3QKjfBA1vzuG7u9A5ivp2z1MhUf0Z'
access_token_secret='dL1yrGknTLQnD33AFntm6PSNro09x4oJnmb11IppRa2ai'
bearer_token='AAAAAAAAAAAAAAAAAAAAAC5FWAEAAAAAuFvhytDv9%2F93gRviSEJd7mZv4IU%3DrJrR1XRCPxckWpUWRBZQLBuPX2Pe906oL1YU72LSWDpzeQXTsk'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth=auth)

try:
    print('trying...')
    print('Checking Authentication...')
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


def search_tweets():
    file = open('tweets.csv', 'w',encoding="utf-8", newline='')
    with file:
        # identifying header
        header =['Climate Change Crisis','Champions League','The Witcher']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerow({header[0]:[t for t in return_tweets(header[0])],
                         header[1]:[t for t in return_tweets(header[1])],
                         header[2]:[t for t in return_tweets(header[2])]})

    file.close()

def return_tweets(word):
    ls=[]
    count=1
    for tweet in tweepy.Cursor(api.search_tweets, q=word).items(200):
        if 'RT' in tweet.text:
            ls.append(f'{count}.- {tweet.text}\n\n')
            print(f'{count}.- {tweet.text}\n\n')
            count+=1
    return ls

search_tweets()





