import streamlit as st
import pandas as pd
import plotly.express as px
import json

def regions(tab):
        with tab:
            st.markdown("""### Results by location""")

            regions = pd.read_csv("poll/region.csv")
            #regions

            #st.markdown("""### Add percentages and majorities""")
            # 
            regions['Rejoin Majority'] = regions['Rejoin the EU'] > regions['Stay out of the EU']
            regions['Actual Rejoin Majority'] = regions['Rejoin the EU'] - regions['Stay out of the EU']
            regions['Rejoin Majority %'] = round(regions['Actual Rejoin Majority']/(regions['Rejoin the EU'] + regions['Stay out of the EU'])*100,1)
            regions['Rejoin %'] = round(regions['Rejoin the EU']/(regions['Rejoin the EU'] + regions['Stay out of the EU'])*100,1)
            #regions

            st.write("__The regions and where there is a majority to rejoin or stay out__")
            col_r2, col_r3 = st.columns((3,3))
            #with col_r1: 
            #    st.write("__The regions and where there is a majority to rejoin or stay out__")
            with col_r2:
                f = open("poll/uk_regions.geojson")
                uk_districts = json.load(f)

                fig = px.choropleth_mapbox(regions, 
                                    locations="Region", 
                                    featureidkey="properties.rgn19nm", 
                                    geojson=uk_districts,  
                                    hover_name="Region", 
                                    color='Region', 
                                    mapbox_style="carto-positron", 
                                    zoom=3.1, 
                                    center = {"lat": 54.5, "lon": -4}, 
                                    width=400, height=420, 
                                    title="GB Regions")

                st.plotly_chart(fig, use_container_width=True)
            with col_r3:
                fig = px.choropleth_mapbox(regions, 
                                    locations="Region", 
                                    featureidkey="properties.rgn19nm", 
                                    geojson=uk_districts,  
                                    hover_name="Region", 
                                    color='Rejoin Majority', 
                                    mapbox_style="carto-positron", 
                                    zoom=3.2, 
                                    center = {"lat": 54.5, "lon": -4}, 
                                    width=400, height=420, 
                                    title="Regions with a rejoin majority")
                st.plotly_chart(fig, use_container_width=True)

            st.markdown("""__How they would vote__""")

            col_r5,col_r6 = st.columns((2,2))
            #with col_r4: 
            #    st.markdown("""__How they would vote__""")
            with col_r5:
                fig = px.choropleth_mapbox(regions, locations="Region", 
                                    featureidkey="properties.rgn19nm", 
                                    geojson=uk_districts,  
                                    hover_name="Region", 
                                    color='Rejoin %', 
                                    color_continuous_scale="Blues", 
                                    mapbox_style="carto-positron", 
                                    zoom=3.2, 
                                    center = {"lat": 54.5, "lon": -4}, 
                                    width=400, height=400, 
                                    title="Rejoin % by regions")
                st.plotly_chart(fig, use_container_width=True)

            with col_r6:
                fig = px.bar(regions, y='Rejoin Majority %', x='Region', text_auto=True, color='Rejoin Majority',
                            color_discrete_sequence=["blue","red"], title="The percentage support in the regions", 
                                    width=400, height=400)
                st.plotly_chart(fig, use_container_width=True)