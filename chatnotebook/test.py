# Write a Streamlit program that will use pandas and matplotlib, read in data from londonweather.csv into a dataframe, Create a new column 'Tmean' as the average of 'Tmax' and 'Tmin' and Draw a line chart of Tmean over Month



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("London Weather Analysis")

# Read in data from londonweather.csv into a dataframe
df = pd.read_csv('londonweather.csv') 
st.write(df) 

# Create a new column 'Tmean' as the average of 'Tmax' and 'Tmin' 
df['Tmean'] = (df['Tmax'] + df['Tmin']) / 2 
st.write(df) 

 # Draw a line chart of Tmean over Month 
plt.plot(df['Month'], df['Tmean']) 
plt.xlabel('Month') 
plt.ylabel('Average Temperature (Celsius)') 
st.pyplot()