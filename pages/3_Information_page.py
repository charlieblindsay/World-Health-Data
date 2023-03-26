import streamlit as st

st.title('How do Alcohol consumption and Blood Pressure vary by country?')
st.subheader('[GitHub Repo](https://github.com/charlieblindsay/global-blood-pressure-data)')

st.subheader('Purpose of this app')
st.write('The purpose is to...')
st.write('I originally used this WHO data as part of the \'Data Visuzalization\' section of a [Python course](https://icsm-python-course.netlify.app/).')

st.subheader('Data Sources')
st.write('Both datasets are from the WHO website:')
st.write("- [Link to Alcohol data](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/alcohol-recorded-per-capita-(15-)-consumption-(in-litres-of-pure-alcohol))")
st.write("- [Link to Alcohol data](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/alcohol-recorded-per-capita-(15-)-consumption-(in-litres-of-pure-alcohol))")

st.subheader('What does the blood pressure data show?')
st.write('Blood pressure measures the force of your blood pushing against the walls of your blood vessels.')
st.write('If your blood pressure is high, it means your heart is working too hard and the force of the blood flowing through your vessels is too high. This increased pressure can cause your arteries to thicken or harden, and for your blood vessels to weaken, which can lead to serious health conditions.')
st.write('https://www.healthpartners.com/blog/which-numbers-mean-high-blood-pressure/')

st.subheader('What does the alcohol consumption data show?')
st.write('The alcohol data is from the WHO website')

st.subheader('Purpose of different pages:')
st.write('1. Chloropleth: A coloured map where different colours correspond to different levels of alcohol consumption or blood pressure.')
st.write('2. Time Variation (Country Selection): Select the countries of interest for Time Variation (Plots) page - see below')
st.write('3. Time Variation (Plots): For the countries selected, alcohol consumption against time and blood pressure against time are plotted')