# TwitterStats

import twitter

# Set up credentials for Twitter developer API
CONSUMER_KEY = 'xxxxxx'
CONSUMER_SECRET = 'xxxxxx'
OAUTH_TOKEN = 'xxxxxx'
OAUTH_TOKEN_SECRET = 'xxxxxx'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# search for tweets from CNN
tweets = twitter_api.search.tweets(q="from:CNN", count=10)

# Get the data into a Pandas dataframe
tweetData = pd.DataFrame(tweets['statuses'])

# Print the columns of the dataframe
print(tweetData.columns)

print(tweetData['favorite_count'])

tweetData['retweet_count'].plot.pie()
plt.show()

# Get the data
tweet_count = len(tweetData)
favorite_count = tweetData['favorite_count'].sum()
retweet_count = tweetData['retweet_count'].sum()

# Print it out
print('Number of tweets: ' + str(tweet_count))
print('Total number of likes: ' + str(favorite_count))
print('Total number of retweets: ' + str(retweet_count))

# Draw a nice plot of the likes and retweets
tweetData.plot.bar(subplots=True, figsize=(10,6),
    y=  ['favorite_count','retweet_count'])
plt.show()

# Now do thesame thing for two Twitter accounts
# Note that this probably looks better when run in a Jupyter Notebook

names = ['CNN','BBCWorld']

for name in names:
    tweets = pd.DataFrame(twitter_api.search.tweets(q="from:"+name, 
      count=10)['statuses'])
    tweet_count = len(tweets)
    favorite_count = tweets['favorite_count'].sum()
    retweet_count = tweets['retweet_count'].sum()
    
    print("Data for "+name)
    print('Number of tweets: ' + str(tweet_count))
    print('Number of likes: ' + str(favorite_count))
    print('Number of likes per tweet: '+str(favorite_count/tweet_count))
    print('Number of retweets: ' + str(retweet_count))
    print('Number of retweets per tweet: '+str(retweet_count/tweet_count))
    
    tweets.plot.bar(subplots=True, figsize=(10,6),y=
        ['favorite_count','retweet_count'],
        legend=False,label=['Favourites','Retweets'],title=name)
    plt.show()