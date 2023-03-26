import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('How have Alcohol consumption and Blood Pressure varied in the last 50 years?')

st.header('Steps:')
st.write('1. Select the countries of interest')
st.write('2. Click on the \'Time Variation (Plots)\' in the sidebar to see how blood pressure and alcohol consumption has varied over time in the selected countries ' )

df = pd.read_csv('data/processed/blood_pressure_data.csv')
countries = list(df.columns[1:]) # Choose the first 188 countries so is divisible by 4

selected_countries = st.multiselect('Countries', countries)

df_blood_pressure = pd.read_csv('data/processed/blood_pressure_data.csv')
df_alcohol = pd.read_csv('data/processed/alcohol_data.csv')

try:
    user_data_choice = st.radio('Choose to see blood pressure or alcohol data', options=['Alcohol', 'Blood Pressure'], index=1)

    if user_data_choice == 'Blood Pressure':
        fig = sns.lineplot(data=df_blood_pressure[selected_countries])
        st.header("Blood Pressure By Country")
        plt.xlabel('Year')
        plt.ylabel('Blood pressure')
        fig.set_xticklabels(['1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015'])
    
    if user_data_choice == 'Alcohol':
        fig = sns.lineplot(data=df_alcohol[selected_countries])
        st.header("Alcohol Consumption By Country")
        plt.xlabel('Year')
        plt.ylabel('Alcohol consumption per capita (in litres of pure alcohol)')
        fig.set_xticklabels(['1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020'])

    st.pyplot(plt.gcf())

except TypeError:
    st.warning('No countries selected. Please select countries by clicking on \'Time Variation (Country Selection)\' in the sidebar.')