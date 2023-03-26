import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

# st.title('How does Alcohol consumption and Blood Pressure vary by country?')
st.title('How does Alcohol consumption vary by country?')

# user_data_choice = st.radio('Choose to see blood pressure or alcohol data', options=['Alcohol', 'Blood Pressure'], index=0)

df_country_codes = pd.read_csv('data/processed/country_codes.csv')
year = 2000

def plot_chloropleth(data_file_path, year_range, default_year, chloropleth_subheader):
    # min_year, max_year = year_range
    
    df = pd.read_csv(data_file_path)
    
    # year = st.slider('Choose year', min_value=min_year, max_value=max_year, value=default_year, step=1)

    df = df.set_index('Year')
    df_single_year = pd.DataFrame({'Level': df.loc[year]})
    df_single_year = df_single_year.reset_index()
    df_single_year.columns = ['Country', 'Level']

    df_merge = pd.merge(df_single_year, df_country_codes, on='Country', how='left')

    chloropleth_subheader = chloropleth_subheader + f' in {year}'
    st.subheader(chloropleth_subheader)
    fig = px.choropleth(df_merge, locations="Country_Code",
                        color="Level",
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma)

    st.plotly_chart(fig)

# if user_data_choice == 'Alcohol':
plot_chloropleth(data_file_path='data/processed/alcohol_data.csv',
                    year_range=(1960, 2019), 
                    default_year=2002, 
                    chloropleth_subheader='Chloropleth showing how alcohol consumption per capita (in pure litres of alcohol consumed per year) varied across the globe')

# if user_data_choice == 'Blood Pressure':
#     plot_chloropleth(processed/data_file_path='data/processed/blood_pressure_data.csv',
#                     year_range=(1975, 2015), 
#                     default_year=2000, 
#                     chloropleth_subheader="Chloropleth showing how average blood pressure varied across the globe")