import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utilities.file_paths import processed_data_path

selected_country = st.radio('Choose a country', options=['United States of America', 'Austria'], index=0)

alpha = st.radio('Choose a value of the parameter alpha', options=[0.02, 0.3, 0.5, 0.9])

df_alcohol = pd.read_csv(processed_data_path / 'alcohol_data.csv')

country_data = df_alcohol[selected_country]

years = [i for i in range(1960, 2020)]

dict_exponential_smoothing = {}

smoothed_data = [df_alcohol[selected_country].iloc[0]]
for i in range(1, len(years)):
    smoothed_data.append(alpha * df_alcohol[selected_country].iloc[i] + (1 - alpha) * smoothed_data[i - 1])

df = pd.DataFrame({selected_country: country_data, 'Exponentially Smoothed Data': smoothed_data})    

fig = sns.lineplot(data=df)
st.header("How has Alcohol Consumption varied over time?")
plt.xlabel('Year')
plt.ylabel('Alcohol consumption per capita (in litres of pure alcohol per year)')
fig.set_xticklabels(['1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020'])

st.pyplot(plt.gcf())