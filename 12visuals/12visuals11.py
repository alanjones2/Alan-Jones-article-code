#12 visuals 11 waterfall chart
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import waterfall_chart
from waterfall_ax import WaterfallChart

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

###############################################

st.markdown("---")

fig, ax = plt.subplots()

# Cumulative values
step_values = [100,130,138,126,116]#[80, 70, 90, 85, 60, 50]

# Labels
metric_name = 'Balance'
step_names = ['Beginning HC','Hires','Transfers In','Transfers Out','Exits']#['Balance0', 'Spend_clothes', 'Salary', 'Spend_grocery', 'Spend_phone', 'Spend_parking']
last_step_label = 'End Balance'

# Styles#
bar_labels = [x for x in range(7)]
bar_kwargs = {'edgecolor': 'black'}
line_kwargs = {'color': 'red'}

# Plot waterfall
waterfall = WaterfallChart(
    step_values, 
    step_names=step_names, 
    metric_name=metric_name, 
    last_step_label=last_step_label,
)
wf_ax = waterfall.plot_waterfall(
    title='Change Styles and Labels',
    bar_labels = bar_labels,
    bar_kwargs = bar_kwargs,
    line_kwargs = line_kwargs,
    ax = ax
)
#plt.show()
plt.xticks(rotation=45)
st.pyplot(fig)