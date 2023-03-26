import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

df_alcohol = pd.read_csv('data/processed/alcohol_data.csv')
df_bmi = pd.read_csv('data/processed/BMI_data.csv')
df_country_code = pd.read_csv('data/processed/country_codes.csv')

df_alcohol = df_alcohol.set_index('Year')
df_bmi = df_bmi.set_index('Year')

year = st.slider('Choose year', min_value=1975, max_value=2015, value=2000, step=1)

df_a_single_year = pd.DataFrame({'alcohol': df_alcohol.loc[year]})
df_bmi_single_year = pd.DataFrame({'BMI': df_bmi.loc[year]})

df_a_single_year = df_a_single_year.reset_index()
df_a_single_year.columns = ['Country', 'Alcohol']

df_bmi_single_year = df_bmi_single_year.reset_index()
df_bmi_single_year.columns = ['Country', 'BMI']

df_a_single_year = pd.merge(df_a_single_year, df_country_code, on='Country', how='left')

df_merge = pd.merge(df_a_single_year, df_bmi_single_year, on='Country')

df_merge = df_merge.dropna()

df_cont = pd.read_csv('data/raw/continent_data.csv')
df_cont = df_cont[['alpha-3', 'sub-region', 'region']]
df_cont.columns = ['Country_Code', 'sub-region', 'region']

df_merge = pd.merge(df_merge, df_cont, how='left', on='Country_Code')

fig = px.scatter(df_merge, x="Alcohol", y="BMI",
                 hover_data=['Country'], color='region')

st.plotly_chart(fig)