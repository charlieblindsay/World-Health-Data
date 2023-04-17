# Global Blood Pressure Data

### App Link: https://charlieblindsay-world-health-data-time-variation-hlt21d.streamlit.app/

# User Guide

### Purpose of streamlit pages

- Time_Variation.py: For the countries selected, the selected dependent variable is plotted against time
- Relationship_between_variables.py: For the year selected, the 2 selected dependent variables are plotted against each other
- Global_Variation.py: A chloropleth shows how the dependent variable varies across the globe in the chosen year

### FAQ
#### What does BMI mean?
Body Mass Index (BMI) gives an indication of whether a person\'s weight is healthy. It is a person\'s weight (in kilograms) divided by their height (in metres) squared.

#### What are healthy levels of alcohol consumption?
According to the [NHS](https://www.nhs.uk/live-well/alcohol-advice/calculating-alcohol-units/), the maximum amount people should drink is 14 units per week, which equates to around 8 litres of pure alcohol per year.

# Developer Guide

## Data Sources
2 datasets are from The World Health Organisation:
- [BMI data](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/mean-bmi-(kg-m-)-(age-standardized-estimate))
- [Alcohol data](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/alcohol-recorded-per-capita-(15-)-consumption-(in-litres-of-pure-alcohol))

2 datasets are from The World Bank:
- [Population data](https://data.worldbank.org/indicator/SP.POP.TOTL)
- [GDP data](https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD?end=2021&start=1990&view=chart)

I originally used this data as part of a Data Visuzalization section in a [Python course](https://icsm-python-course.netlify.app/) I created.

st.write('I originally used this data as part of a \'Data Visuzalization\' section in a [Python course](https://icsm-python-course.netlify.app/) I created.')

## Files

### Data Cleaning Files

Run these files convert raw data in the data/raw folder into the processed data in the data/processed folder.
The processed data is in a year-country format; the index column is the year and all the other columns are the countries. The value contained in each cell is the average variable value (e.g. average BMI) for that country in that year.

data_cleaning_BMI.py
data_cleaning_alcohol.py: 
data_cleaning_world_bank.py

#### What does 'cleaning' data mean in this context?
- Removing unnecessary columns
- Imputing missing values
- Casting data to the correct type
- Converting dataframe to the correct format, e.g. year-country format

### SQL Database Files

Run these files to create a SQL database table which contains information from all processed data created in the files above.

These files should be run after running the Data Cleaning files above. They should be run in the following order:
create_sql_dataframe.py: Creates a dataframe which contains the year, country, population, GDP per capita, Average BMI and Average alcohol consumption as the columns. 
create_sql_database.py: Creates a sqlite database table of the dataframe created with the above file.

#### What does 'cleaning' data mean in this context?
- Removing unnecessary columns
- Imputing missing values
- Casting data to the correct type
