# TwitterStats
import tweepy 
from textblob import TextBlob
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import sys


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

    if resp:
        try:
            tweets = api.user_timeline(screen_name=username, count=number_of_tweets)


        except:
            print("Unexpected error receiving tweet")

        if tweets:
            st.success(f"Retrieved {len(tweets)} tweets from __{username}__")
            positive_count = 0
            negative_count = 0
            neutral_count = 0
            
            tweet_panel = st.expander("Show Tweets", expanded=False)
            with tweet_panel:
                cols = st.columns((8,2,2))
                with cols [0]: st.info("Text")
                with cols [1]: st.info("RTs")
                with cols [2]: st.info("Favorites")

            total_rts = 0
            total_fav = 0

            # Create a df to contain all the tweets and other info

            df_t = pd.DataFrame()
            df_t['text'] =[i.text for i in tweets]
            df_t['favourites'] =[i.favorite_count for i in tweets]
            df_t['rts'] =[i.retweet_count for i in tweets]
            #df_t
            
            for tweet in tweets:
                total_rts+=tweet.retweet_count
                total_fav+=tweet.favorite_count
                with tweet_panel:
                    cols = st.columns((8,2,2))
                    with cols[0]: st.write(tweet.text)
                    with cols[1]: st.write(tweet.retweet_count)
                    with cols[2]: st.write(tweet.favorite_count)

                #
                # WRONG - this is getting the sentiment of the tweet IF it is a reply
                # try something like this:
                #r = tweets = api.search_tweets(q="to:CNN", count=10)
                #print(f"t{r}")
                #


                if tweet.in_reply_to_status_id is not None:
                    #tweet.in_reply_to_status_id
                    try:
                        response_tweet = api.get_status(tweet.in_reply_to_status_id)
                        sentiment = sentiment_analysis(response_tweet.text)
                        if sentiment == "positive":
                            positive_count += 1
                        elif sentiment == "negative":
                            negative_count += 1
                        else:
                            neutral_count += 1
                    except:
                        print(f"Unexpected error getting response")

            labels = ['Positive', 'Negative', 'Neutral']
            values = [positive_count, negative_count, neutral_count]
            
            #df = pd.DataFrame(values,labels)
            
            st.info(f"Responses")

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

            df = pd.DataFrame()
            df['tweet'] = range(0,len(tweets),1)
            df['fav'] = [i.favorite_count for i in tweets]
            df['rt'] = [i.retweet_count for i in tweets]
            #df

            col = st.columns(2)

            with col[0]:
                st.info(f"Favourites (totaL:{total_fav})")
                fig, ax = plt.subplots()
                df.plot.bar(x="tweet",y="fav",ax=ax)
                st.pyplot(fig)
            with col[1]:
                st.info(f"Retweets (totaL:{total_rts})")
                fig, ax = plt.subplots()
                df.plot.bar(x="tweet",y="rt",ax=ax)
                st.pyplot(fig)


main(setup_tweepy())
