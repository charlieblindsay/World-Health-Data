import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df_blood_pressure = pd.read_csv('data/processed_blood_pressure_data.csv')
df_alcohol = pd.read_csv('data/processed_alcohol_data.csv')

selected_countries = [i.replace('dynamic_checkbox_','') for i in st.session_state.keys() if i.startswith('dynamic_checkbox_') and st.session_state[i]]

try:
    fig = sns.lineplot(data=df_blood_pressure[selected_countries])
    st.title("Blood Pressure By Country")
    plt.xlabel('Year')
    plt.ylabel('Blood pressure')
    fig.set_xticklabels(['1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015'])
    st.pyplot(plt.gcf())

    plt.clf()
    fig = sns.lineplot(data=df_alcohol[selected_countries])
    st.title("Alcohol Consumption By Country")
    plt.xlabel('Year')
    plt.ylabel('Alcohol consumption per capita (in litres of pure alcohol)')
    fig.set_xticklabels(['1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020'])
    st.pyplot(plt.gcf())

except TypeError:
    st.warning('No countries selected. Please select countries by clicking on \'app\' in the sidebar.')