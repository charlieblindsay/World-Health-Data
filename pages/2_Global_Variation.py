import streamlit as st
import pandas as pd
from utilities.file_paths import processed_data_path, raw_data_path
from utilities.plotting import plot_chloropleth

st.title('How does Alcohol consumption and Blood Pressure vary by country?')

df_continents = pd.read_csv(raw_data_path / 'continent_data.csv')
df_continents = df_continents[['alpha-3', 'region']]
df_continents.columns = ['Country_Code', 'region']

selected_data = st.radio('Choose to see blood pressure or alcohol data', options=['Alcohol Consumption', 'BMI', 'Population', 'GDP per capita' ], index=0)

df_country_codes_who = pd.read_csv(processed_data_path / 'country_codes_who.csv')

if selected_data == 'Alcohol Consumption':
    plot_chloropleth(data_file_path=processed_data_path / 'alcohol_data.csv',
                    year_range=(1960, 2019), 
                    default_year=2002, 
                    chloropleth_subheader='Chloropleth showing how alcohol consumption per capita (in pure litres of alcohol consumed per year) varied across the globe',
                    df_country_codes_who=df_country_codes_who)

if selected_data == 'BMI':
    plot_chloropleth(data_file_path=processed_data_path / 'BMI_data.csv',
                    year_range=(1975, 2015), 
                    default_year=2000, 
                    chloropleth_subheader="Chloropleth showing how average blood pressure varied across the globe",
                    df_country_codes_who=df_country_codes_who)
    
if selected_data == 'Population':
    plot_chloropleth(data_file_path=processed_data_path / 'population_data.csv',
                    year_range=(1960, 2021), 
                    default_year=2021, 
                    chloropleth_subheader="Chloropleth showing population variation by country",
                    df_country_codes_who=df_country_codes_who)
    
if selected_data == 'GDP per capita':
    plot_chloropleth(data_file_path=processed_data_path / 'GDP_data.csv',
                    year_range=(1960, 2021), 
                    default_year=2021, 
                    chloropleth_subheader="Chloropleth showing GDP per capita variation by country",
                    df_country_codes_who=df_country_codes_who)





