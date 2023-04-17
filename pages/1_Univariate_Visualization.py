import streamlit as st
import plotly.express as px
import pandas as pd
from utilities.file_paths import processed_data_path

df_country_code = pd.read_csv(processed_data_path / 'country_codes_who.csv')
df_continents = pd.read_csv(processed_data_path / 'continent_data.csv')

df_alcohol = pd.read_csv(processed_data_path / 'alcohol_data.csv')

df_bmi = pd.read_csv(processed_data_path / 'BMI_data.csv')
df_population = pd.read_csv(processed_data_path / 'population_data.csv')
df_gdp = pd.read_csv(processed_data_path / 'GDP_data.csv')

st.title('How does BMI, Alcohol Consumption and Population vary by Continent?')

year = st.slider('Choose year', min_value=1990, max_value=2015, value=2015, step=1)

variable = st.radio(label='Select which variable you want to plot', options=['Alcohol Consumption', 'BMI', 'Population', 'GDP per capita'])

def plot_univariate_scatter(df, variable_axis_name, remove_China_and_India):
    df = df.set_index('Year')
    df_single_year = pd.DataFrame({'Variable': df.loc[year]})
    df_single_year = df_single_year.reset_index()
    df_single_year.columns = ['Country', variable_axis_name]

    if remove_China_and_India == 'Yes':
        df_single_year = df_single_year[(df_single_year.Country != 'China') & (df_single_year.Country != 'India')]

    df_single_year = pd.merge(df_single_year, df_country_code, on='Country', how='left')

    df_single_year = pd.merge(df_single_year, df_continents, how='left', on='Country_Code')

    fig = px.strip(df_single_year, x="Continent", y=variable_axis_name,
                    hover_data=['Country', 'sub-region'])

    st.plotly_chart(fig)

if variable == 'Alcohol Consumption':
    plot_univariate_scatter(df=df_alcohol, variable_axis_name="Alcohol Consumption per Capita (in pure litres of alcohol per year)", remove_China_and_India=False)

if variable == 'BMI':
    plot_univariate_scatter(df=df_bmi, variable_axis_name="Average BMI", remove_China_and_India=False)

if variable == 'Population':
    remove_China_and_India = st.radio(label='Remove China and India from plot?', options=['Yes', 'No'], index=1)
    plot_univariate_scatter(df=df_population, variable_axis_name="Population", remove_China_and_India=remove_China_and_India)

if variable == 'GDP per capita':
    plot_univariate_scatter(df=df_gdp, variable_axis_name="GDP per capita", remove_China_and_India=False)