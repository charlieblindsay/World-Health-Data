import pandas as pd

df=pd.read_csv('data/raw/alcohol_data.csv')

# Selecting columns of interest
df = df[['Period', 'Location', 'Dim1', 'SpatialDimValueCode', 'Value']]

# Renaming columns
df.columns = ['Year', 'Country', 'Alcohol_Type', 'Country_Code', 'Alcohol_consumption_per_capita']

df_country_codes = df[['Country', 'Country_Code']]
df = df.drop('Country_Code', axis=1)

# Selecting only rows which have alcohol type equal to 'all types'
df = df[df.Alcohol_Type == 'All types']

# Remving 'Alcohol_Type' column as it now contains no information
df = df.drop('Alcohol_Type', axis=1)

# Removing rows where alcohol consumption is zero
def check_if_consumption_is_zero(consumption_value):
    if consumption_value in [0.0, '0', '0 [0 – 0]', '0.000\xa01']:
        return False
    else:
        return True
    
df = df[df.Alcohol_consumption_per_capita.apply(check_if_consumption_is_zero)]

def convert_consumption_values_to_floats(consumption_value):
    if isinstance(consumption_value, float):
        return consumption_value
    else:
        if '\xa0' in consumption_value:
            consumption_value = consumption_value.replace('\xa0', '')
        return float(consumption_value.split(' ')[0])
    
df.Alcohol_consumption_per_capita = df.Alcohol_consumption_per_capita.apply(convert_consumption_values_to_floats)

df = df.sort_values(by=['Country', 'Year'])

countries = df.Country.unique()
years = df.Year.unique()
years.sort()

dict = {country: [] for country in countries}
for country in countries:
    for year in years:
        value = df[df.Country == country][df.Year == year].Alcohol_consumption_per_capita
        if value.empty == True:
            dict[country].append(float('NaN'))
        else:
            dict[country].append(float(df[df.Country == country][df.Year == year].Alcohol_consumption_per_capita))

df = pd.DataFrame(dict)

df['Year'] = [i for i in range(years[0], years[-1]+1)]

df = df.set_index('Year')

df.to_csv('data/processed/alcohol_data.csv', index=False)
df_country_codes.to_csv('data/processed/processed/country_codes.csv', index=False)