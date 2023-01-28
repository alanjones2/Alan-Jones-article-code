# TwitterStats
import tweepy 
from textblob import TextBlob
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import sys

st.set_page_config(layout="wide")

def setup_tweepy():
    # Twitter API credentials
    consumer_key = st.secrets["consumer_key"]
    consumer_secret = st.secrets["consumer_secret"]
    access_token = st.secrets["access_token"]
    access_token_secret = st.secrets["access_token_secret"]

    # Authenticate with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create a Tweepy API object
    api = tweepy.API(auth)
    return api

def sentiment_analysis(text):
    sentiment = TextBlob(text)
    if sentiment.sentiment.polarity > 0:
        return "positive"
    elif sentiment.sentiment.polarity == 0:
        return "neutral"
    else:
        return "negative"

def get_to_tweets(api, name, count):
    r = api.search_tweets(q=f"to:{name}", count=count)
    return r

def get_tweets(api, name, count):

    df_t = pd.DataFrame()
    try:
        tweets = api.user_timeline(screen_name=name, count=count)
        #tweets = api.search_tweets(q=f"from:{name}", count=count)
    except:
        print("Unexpected error reciiving tweet")
    if tweets:
        # Create a df to contain all the tweets and other info
        df_t['text'] =[i.text for i in tweets]
        df_t['favourites'] =[i.favorite_count for i in tweets]
        df_t['rts'] =[i.retweet_count for i in tweets]
        #df_t
        return df_t, True
    else: return df_t, False
    pass

def main(api):
    st.title("Twitter Sentiment Analysis")

    # Set up sidebar
    with st.sidebar:
        # Get the twitter username
        st.header("Enter the Twitter name")
        st.write("that you want to retrieve tweets from")
        username = st.text_input("Enter the Twitter username:")
        number_of_tweets = st.select_slider("Number of tweets", options=(10,20,30,40,50,60,70,80,90,100), value=10)
        resp = st.button('Submit')

    # If submit button pressed the run rest of app
    if resp:
        df_t, success = get_tweets(api, username, number_of_tweets)    
        if success:
            st.success(f"Retrieved {len(df_t)} tweets from __{username}__")

            # Add and expander panel to contain the text of the tweets - this is minimised by default
            tweet_panel = st.expander("Show Tweets", expanded=False)
            with tweet_panel:
                # Display headers
                cols = st.columns((8,2,2))
                with cols [0]: st.info("Text")
                with cols [1]: st.info("Retweets")
                with cols [2]: st.info("Favorites")

            # Display text favourites and RTs 
            for index, tweet in df_t.iterrows():
                #tweet
                with tweet_panel:
                    cols = st.columns((8,2,2))
                    with cols[0]: st.write(tweet.text)
                    with cols[1]: st.write(tweet.rts)
                    with cols[2]: st.write(tweet.favourites)

            # Display charts in two columns
            col = st.columns(2)

            # Favourites chart
            with col[0]:
                st.info(f"Favourites (totaL:{df_t.favourites.sum()})")
                fig, ax = plt.subplots(figsize=(10, 5))
                df_t.plot.bar(y="favourites",legend= False, ax=ax)
                plt.xlabel('Tweet', fontsize=12)
                plt.ylabel('Likes', fontsize=12)
                ax.tick_params(axis='x', labelsize=4, rotation=0)
                st.pyplot(fig)
            # RTs chart

            with col[1]:
                st.info(f"Retweets (totaL:{df_t.rts.sum()})")
                fig, ax = plt.subplots(figsize=(10, 5))
                df_t.plot.bar(y="rts",legend= False, ax=ax)
                plt.xlabel('Tweet', fontsize=12)
                plt.ylabel('Retweets', fontsize=12)
                ax.tick_params(axis='x', labelsize=4, rotation=0)
                st.pyplot(fig)


main(setup_tweepy())
"""
def sentiment():
    labels = ['Positive', 'Negative', 'Neutral']
    values = [positive_count, negative_count, neutral_count]
    
    #df = pd.DataFrame(values,labels)
    
    st.info(f"Received tweets")

    col = st.columns(2)

    with col[0]:
        st.write(f"Positive: {positive_count}")
        st.write(f"Negative: {negative_count}")
        st.write(f"Neutral:  {neutral_count}")
    with col[1]:
        if sum(values) == 0:
            col[1].write("No responses")
        else:
            fig, ax = plt.subplots()
            #df.plot.bar(legend=False,ax=ax)
            plt.pie(values, labels=labels, autopct='%1.1f%%')
            st.pyplot(fig)
"""