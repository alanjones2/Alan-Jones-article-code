from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

s1 = "Britain's trade will be much worse if it doesn't have a good trade deal."
s2 = "Britain will have to abide by WTO rules if it doesn't have a trade deal."
s3 = "Britain will be very successful whether or not it has a trade deal."

vs = analyzer.polarity_scores(s1)
print("{}... {}".format(s1[:30], str(vs)))
vs = analyzer.polarity_scores(s2)
print("{}... {}".format(s2[:30], str(vs)))
vs = analyzer.polarity_scores(s3)
print("{}... {}".format(s3[:30], str(vs)))


import twitter

CONSUMER_KEY = '*****'
CONSUMER_SECRET = '*****'
OAUTH_TOKEN = '*****'
OAUTH_TOKEN_SECRET = '*****'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# search
import sys
import pandas as pd
import matplotlib.pyplot as plt

count=20

try:
  tweets = twitter_api.search.tweets(q="vaccine", count=count, lang='en', tweet_mode="extended")
  
except:
  print("Unexpected error:", sys.exc_info()[0])
  
if tweets['statuses'] == []:
  print("no data")

len(tweets['statuses'])

tweetsWithSent = []

for t in tweets['statuses']:
  text = (t['full_text'])
  ps = analyzer.polarity_scores(text)
  tweetsWithSent.append({'text':text, 'compound':ps['compound']})

tweetdf = pd.DataFrame(tweetsWithSent)

print(tweetdf)

tweetdf.plot.bar(figsize=(15,5),width=1)
plt.show()
