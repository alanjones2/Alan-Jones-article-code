#12 visuals 11 waterfall chart
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import waterfall_chart

a = ['sales','returns','credit fees','rebates','late charges','shipping']
b = [10,-30,-7.5,-25,95,-7]

my_plot = waterfall_chart.plot(a, b)
st.pyplot(my_plot)

a = ['Beginning HC','Hires','Transfers In','Transfers Out','Exits']
b = [100,30,8,-12,-10]

my_plot = waterfall_chart.plot(a, b, net_label = "Ending HC")
st.pyplot(my_plot)

my_plot = waterfall_chart.plot(a, b, net_label = "Ending HC", blue_color='blue',red_color='blue', green_color='blue')
st.pyplot(my_plot)