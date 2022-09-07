#12 visuals 1 text
import streamlit as st
import matplotlib.pyplot as plt

days = ['Yesterday','Today']
temps = [24,29]
caption = f"Today's temperature was {temps[1]}ºC"
caption2 = "That's 5º up from yesterday"

fig, ax = plt.subplots()
plt.bar(days,temps)
plt.suptitle(caption, fontweight = 'bold')
plt.title(caption2)
st.pyplot(fig)

st.markdown("---")

col3, col4 = st.columns([1,4])
col3.metric("Temperature", temps[1],temps[0])
col4.markdown(f"#### {caption}")
col4.markdown(caption2)

st.markdown("---")

col1, col2 = st.columns([1,4])
col1.markdown(f"# {temps[1]}")
col2.markdown(f"#### {caption}")
col2.markdown(caption2)

st.markdown("---")

fig2, ax2 = plt.subplots(figsize=(5,1))

ax2.text(0, 0.9, temps[1],
        verticalalignment='top', horizontalalignment='left',
        color='red', fontsize=18, fontweight = 'bold')
ax2.text(0.2, 0.9, caption,
        verticalalignment='top', horizontalalignment='left',
        color='Black', fontsize=10)
ax2.text(0.2, 0.55, caption2,
        verticalalignment='top', horizontalalignment='left',
        color='darkgrey', fontsize=6)

ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.xticks([])
plt.yticks([])

st.pyplot(fig2)

st.markdown("---")

fig3, ax3 = plt.subplots(figsize=(4,2))

ax3.text(0.5, 0.9, temps[1],
        verticalalignment='top', horizontalalignment='center',
        color='darkblue', fontsize=64, fontweight = 'bold')
ax3.text(0.5, 0.3, caption,
        verticalalignment='top', horizontalalignment='center',
        color='blue', fontsize=8)
ax3.text(0.5, 0.2, caption2,
        verticalalignment='top', horizontalalignment='center',
        color='lightblue', fontsize=6)

#ax3.spines['right'].set_visible(False)
#ax3.spines['left'].set_visible(False)
#ax3.spines['bottom'].set_visible(False)
#ax3.spines['top'].set_visible(False)
plt.xticks([])
plt.yticks([])

st.pyplot(fig3)
