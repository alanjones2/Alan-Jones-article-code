# TwitterStats
import streamlit as st
import plotly.express as px
import pandas as pd
import twitter

# Set up credentials for Twitter developer API

CONSUMER_KEY = 'sRLpbdbEX07ZJNw3KhFinasKE'
CONSUMER_SECRET = 'XglmGnO9TGCuu8y5x78MdhS8cMASkC5LkpIhW08kQuJrrxHaR2'
OAUTH_TOKEN = '1022515213151686657-aena7S5IpKSy5ZQsYFM5234OJ2AloT'
OAUTH_TOKEN_SECRET = 'kPX6hu7ln6MBHp4QHnDsY3E6z0dvIMS6uVAsiDNnFlbXj'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)



twitter_api = twitter.Twitter(auth=auth)


#api.get_tweets(["1261326399320715264","1278347468690915330"],expansions="author_id",tweet_fields=["created_at"], user_fields=["username","verified"])

#Response(data=[Tweet(id=1261326399320715264, text=Tune in to the @MongoDB @Twitch stream...), Tweet(id=1278347468690915330, text=Good news and bad news: 2020 is half over)])



# search for tweets from CNN
tweets = twitter_api.search.tweets(q="from:CNN", count=10)

# Get the data into a Pandas dataframe
tweetData = pd.DataFrame(tweets['statuses'])
#tweets
tweetData

# Now do the same thing for two Twitter accounts

names = ['CNN']#,'BBCWorld']
cols = st.columns(3)

for name in names:
    tweets = pd.DataFrame(twitter_api.search.tweets(q="from:"+name, 
      count=10)['statuses'])
    tweet_count = len(tweets)
    favorite_count = tweets['favorite_count'].sum()
    retweet_count = tweets['retweet_count'].sum()
    
    with cols[0]:
        st.header("Data for "+name)
        'Number of tweets: ' + str(tweet_count)
        'Number of likes: ' + str(favorite_count)
        'Number of likes per tweet: '+str(favorite_count/tweet_count)
        'Number of retweets: ' + str(retweet_count)
        'Number of retweets per tweet: '+str(retweet_count/tweet_count)
    
    with cols[1]:
        fig = px.bar(tweets['favorite_count'])
        st.plotly_chart(fig)
    with cols[2]:
        fig = px.bar(tweets['retweet_count'])
        st.plotly_chart(fig)

