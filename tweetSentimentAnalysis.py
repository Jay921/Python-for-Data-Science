import tweepy
from textblob import TextBlob
# import nltk
import csv
# import re

api_key = "V6VQRl9MrLdB9p7vpx0pAMDlq"
api_secret = "KyGoqBzpMw2M6LTHDP2oFkcMQmxBML3xo8pN5krx27a8E8pryV"
access_token_key = "852189415338377216-kYGoN0zG8JZeeWEj6pf0RLYaIlXH3ZP"
access_token_secret = "arrdZ6HOJmXKqnWffujzHe5VNybMR9T5dHYQBufa4Gl37"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

tweets = {}

with open('tweetSentiments.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)


    for tweet in public_tweets:
        # print (tweet)
        analysis = TextBlob(tweet.text)

        tweets["text"] = str(analysis)
        # print(tweets) 
        # print(analysis)

        # print(analysis.tags)
        if (analysis.sentiment.polarity >= 0):
            # tweetSentiment = True
            tweets["sentimentPolarity"] = "Positive"
            # print("Positive")
        elif(analysis.sentiment.polarity < 0):
            # tweetSentiment = False
            tweets["sentimentPolarity"] = "Negative"
            # print("Negative")
        else:
            print("Something went wrong!").encode("utf-8")
        
        #Print 'text' and 'sentimentPolarity' into the csv file
        filewriter.writerow([tweets["text"].encode("utf-8"), tweets["sentimentPolarity"].encode("utf-8")])
      


    