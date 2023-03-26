import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
from utilities.file_paths import processed_data_path, raw_data_path


# st.title('How does Alcohol consumption and Blood Pressure vary by country?')
st.title('How does Alcohol consumption vary by country?')

df_continents = pd.read_csv(raw_data_path / 'continent_data.csv')
df_continents = df_continents[['alpha-3', 'region']]
df_continents.columns = ['Country_Code', 'region']

selected_continent = st.radio('Choose which continent\'s data will be shown', options=df_continents.region.unique()[:-1], index=0)
df_europe = df_continents[df_continents.region == selected_continent]

selected_data = st.radio('Choose to see blood pressure or alcohol data', options=['Alcohol', 'Blood Pressure'], index=0)

df_country_codes = pd.read_csv(processed_data_path / 'country_codes.csv')

def plot_chloropleth(data_file_path, year_range, default_year, chloropleth_subheader):
    min_year, max_year = year_range
    
    df = pd.read_csv(data_file_path)
    
    year = st.slider('Choose year', min_value=min_year, max_value=max_year, value=default_year, step=1)

    df = df.set_index('Year')
    df_single_year = pd.DataFrame({'Level': df.loc[year]})
    df_single_year = df_single_year.reset_index()
    df_single_year.columns = ['Country', 'Level']

    df_merge = pd.merge(df_single_year, df_country_codes, on='Country', how='left')
    df_merge = pd.merge(df_europe, df_merge, on='Country_Code', how='left')

    chloropleth_subheader = chloropleth_subheader + f' in {year}'
    st.subheader(chloropleth_subheader)
    fig = px.choropleth(df_merge, locations="Country_Code",
                        color="Level",
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        center={'lat': 50, 'lon': 14})

    st.plotly_chart(fig)

if selected_data == 'Alcohol':
    plot_chloropleth(data_file_path=processed_data_path / 'alcohol_data.csv',
                    year_range=(1960, 2019), 
                    default_year=2002, 
                    chloropleth_subheader='Chloropleth showing how alcohol consumption per capita (in pure litres of alcohol consumed per year) varied across the globe')

if selected_data == 'Blood Pressure':
    plot_chloropleth(data_file_path=processed_data_path / 'BMI_data.csv',
                    year_range=(1975, 2015), 
                    default_year=2000, 
                    chloropleth_subheader="Chloropleth showing how average blood pressure varied across the globe")