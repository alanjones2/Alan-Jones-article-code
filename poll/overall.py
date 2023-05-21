import streamlit as st
import pandas as pd
import plotly.express as px

def overall(tab):
    with tab:

            st.subheader("The overall result")

            # Data for the overall result
            result = pd.read_csv("poll/referendumvote.csv")

            #st.markdown("### Convert to percentages")
            #st.markdown("A total column and percentage columns have been added, (you may need to scroll the table to see all of the values)")

            result['total'] = result['Stay out of the EU'] + result['Rejoin the EU'] + result['I would not vote this time'] + result['Don\'t know']
            result['Stay%'] = round(result['Stay out of the EU']/ result['total']*100,1)
            result['Rejoin%'] = round(result['Rejoin the EU']/ result['total']*100,1)
            result['DK%'] = round(result['Don\'t know']/ result['total']*100,1)
            result['NoVote%'] = round(result['I would not vote this time']/ result['total']*100,1)

            #st.dataframe(result)

            col1, col2 = st.columns((1,2))
            with col1:
                st.write("""This one shows the overall result as a set of grouped bars. 
                The groups represent those that originally voted to leave the EU, those that voted to remain
                and a group that represents all voters.
                """)
            with col2:
                fig = px.bar(result, x='Original Vote', y=['Rejoin%','Stay%','DK%','NoVote%'], text_auto=True, barmode='group')
                st.plotly_chart(fig)

            col3, col4 = st.columns((1,2))
            with col3:
                st.write("""Now the same things but represented as a stacked bar chart. 
                The voting intentions are stacked above each other and the bars represent the same groups as above.
                """)
            with col4:
                fig = px.bar(result, x='Original Vote', y=['Rejoin%','Stay%','DK%','NoVote%'], text_auto=True, barmode='stack')
                st.plotly_chart(fig)

            col5, col6 = st.columns((1,2))
            with col5:
                st.write("""Here we have the result for all voters. 
                """)
            with col6:
                fig = px.bar(result[result['Original Vote']=='All'], x='Original Vote', y=['Rejoin%','Stay%','DK%','NoVote%'], text_auto=True, barmode='group')
                st.plotly_chart(fig)

            col7, col8 = st.columns((1,2))
            with col7:
                st.write("But if you remove those who don't know and those who would not vote, the difference is more pronounced")
            with col8:
                fig = px.bar(y=[55.9,44.1],  
                            x=['Rejoin%','Stay%'], 
                            text_auto=True)
                st.plotly_chart(fig)


            st.markdown("### Who has changed their mind")

            l = result[result['Original Vote'] == 'Leave']
            dl = round(l['Rejoin the EU']/l['total']*100,1)
            r = result[result['Original Vote'] == 'Remain']
            dr = round(r['Stay out of the EU']/r['total']*100,1)

            col9, col10 = st.columns(2)
            with col9:
                st.metric("% of __Remainers__ who switched to __Leave__",dr.iloc[0])
            with col10:
                st.metric("% of __Leavers__ who switched to __Rejoin__",dl.iloc[0])

