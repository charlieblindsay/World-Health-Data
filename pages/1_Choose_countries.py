import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/processed_blood_pressure_data.csv')
df = df.drop('Year', axis=1)
countries = list(df.columns[1:-3]) # Choose the first 188 countries so is divisible by 4

st.title('How do Alcohol consumption and Blood Pressure vary by country?')
st.write('Find GitHub repository here: https://github.com/charlieblindsay/global-blood-pressure-data')
st.subheader('Purpose of different pages:')
st.write('1. Chloropleth: A coloured map where different colours correspond to different levels of alcohol consumption and blood pressure.')
st.write('2. Time Variation Country Selection: Select the countries of interest to display on Time Variation Plots')
st.write('3. Time Variation Plots: For the countries selected on Time Variation Country Selection, plots of alcohol consumption and blood pressure variation of time are produced')
st.write('4. What does this data mean?')

num_cols = 4
cols = st.columns(num_cols)

num_countries = len(countries)
num_countries_per_column = int(num_countries / num_cols)
countries_array = np.array(countries).reshape(num_cols,num_countries_per_column).transpose()
n,m = countries_array.shape

for i in range(n):
    for j in range(m):
        cols[j].checkbox(countries_array[i, j], key='dynamic_checkbox_' + countries_array[i, j])