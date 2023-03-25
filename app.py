import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

user_data_choice = st.radio('Choose to see blood pressure or alcohol data', options=['Alcohol', 'Blood Pressure'], index=0)

df_country_codes = pd.read_csv('data/country_codes.csv')
df_country_codes = df_country_codes.drop(['Unnamed: 0'], axis=1)

if user_data_choice == 'Alcohol':
    df = pd.read_csv('data/processed_alcohol_data.csv')
    df = df.set_index('Year')
    
    year = st.slider('Choose year', min_value=1961, max_value=2019, value=2002, step=1)

    df_single_year = pd.DataFrame({'alcohol': df.loc[year]})
    df_single_year = df_single_year.reset_index()
    df_single_year.columns = ['Country', 'alcohol']

    df_merge = pd.merge(df_single_year, df_country_codes, on='Country', how='left')

    fig = px.choropleth(df_merge, locations="Country_Code",
                        color="alcohol",
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma)

    st.plotly_chart(fig)

if user_data_choice == 'Blood Pressure':
    df = pd.read_csv('data/processed_blood_pressure_data.csv')
    df = df.drop(['Unnamed: 0'], axis=1)
    df = df.set_index('Year')

    year = st.slider('Choose year', min_value=1975, max_value=2015, value=2000, step=5)

    df_single_year = pd.DataFrame({'alcohol': df.loc[year]})
    df_single_year = df_single_year.reset_index()
    df_single_year.columns = ['Country', 'alcohol']

    df_merge = pd.merge(df_single_year, df_country_codes, on='Country', how='left')

    fig = px.choropleth(df_merge, locations="Country_Code",
                        color="alcohol",
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma)
    
    st.plotly_chart(fig)