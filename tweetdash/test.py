
import streamlit as st
import tweepy

# authentication
# Twitter API credentials
consumer_key = st.secrets["consumer_key"]
consumer_secret = st.secrets["consumer_secret"]
access_token = st.secrets["access_token"]
access_token_secret = st.secrets["access_token_secret"]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) 
 
# get the tweet 
#tweet = api.get_status(0) 

tweets = api.user_timeline()
        
tweet = tweets[0]

tweet.in_reply_to_status_id
# get the number of responses to the tweet 
numResponses = len(tweet.in_reply_to_status)

st.write(tweet.in_reply_to_status)

st.write(numResponses)