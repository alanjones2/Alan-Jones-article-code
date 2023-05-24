import streamlit as st
import pandas as pd

def data_tables(tab):
    with tab:
            st.subheader("The overall result")

            # Data for the overall result
            result = pd.read_csv("poll/referendumvote.csv")
            st.dataframe(result)

            st.markdown("### Add percentages")
            st.markdown("A total column and percentage columns have been added, (you may need to scroll the table to see all of the values)")

            result['total'] = result['Stay out of the EU'] + result['Rejoin the EU'] + result['I would not vote this time'] + result['Don\'t know']

            result['Stay%'] = round(result['Stay out of the EU']/ result['total']*100,1)
            result['Rejoin%'] = round(result['Rejoin the EU']/ result['total']*100,1)
            result['DK%'] = round(result['Don\'t know']/ result['total']*100,1)
            result['NoVote%'] = round(result['I would not vote this time']/ result['total']*100,1)

            st.dataframe(result)

            st.subheader("Age data")
            age_data = pd.read_csv("poll/age.csv")
            st.dataframe(age_data)

            age_data_temp = age_data
            age_data_temp['total'] = age_data['Stay out of the EU']+ age_data['Rejoin the EU']+age_data['I would not vote this time']+age_data['Don’t know']
            age_data_temp
            age_data_pc = pd.DataFrame()
            age_data_pc['Age Range'] = age_data['Age Range']
            age_data_pc['% Rejoin'] = age_data_temp['Rejoin the EU']/age_data_temp['total']*100
            age_data_pc['% Stay out'] = age_data_temp['Stay out of the EU']/age_data_temp['total']*100
            age_data_pc['% No vote'] = age_data_temp['I would not vote this time']/age_data_temp['total']*100
            age_data_pc['% DK'] = age_data_temp['Don’t know']/age_data_temp['total']*100

            st.dataframe(age_data_pc)