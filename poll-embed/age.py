import streamlit as st
import pandas as pd
import plotly.express as px


def age(tab):
    with tab:

        age_data = pd.read_csv("poll-embed/age.csv")
        #st.dataframe(age_data)

        age_data_temp = age_data
        age_data_temp['total'] = age_data['Stay out of the EU']+ age_data['Rejoin the EU']+age_data['I would not vote this time']+age_data['Don’t know']
        age_data_temp
        age_data_pc = pd.DataFrame()
        age_data_pc['Age Range'] = age_data['Age Range']
        age_data_pc['% Rejoin'] = round(age_data_temp['Rejoin the EU']/age_data_temp['total']*100,1)
        age_data_pc['% Stay out'] = round(age_data_temp['Stay out of the EU']/age_data_temp['total']*100,1)
        age_data_pc['% No vote'] = round(age_data_temp['I would not vote this time']/age_data_temp['total']*100,1)
        age_data_pc['% DK'] = round(age_data_temp['Don’t know']/age_data_temp['total']*100,1)

        #st.dataframe(age_data_pc)

        st.header("Voters attitude towards EU membership by age")
        col1, col2 = st.columns(2)

        with col1:
            fig = px.bar(age_data_pc, x='Age Range', y='% Rejoin', text_auto=True, barmode='group', title='Rejoin by age',width=300,height=300)
            st.plotly_chart(fig)
        with col2:
            fig = px.bar(age_data_pc, x='Age Range', y='% Stay out', text_auto=True, color_discrete_sequence=["red"], title="Stay out by age",width=300,height=300)
            st.plotly_chart(fig)
