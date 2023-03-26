import pandas as pd

df = pd.read_csv('data/raw/BMI_data.csv')

df = df[['Period', 'Location', 'Dim1', 'SpatialDimValueCode', 'Value']]
df.columns = ['Year', 'Country', 'Gender', 'Country_Code', 'BMI']

df = df[df.Gender == 'Both sexes']
df = df.drop('Gender', axis=1)

df = df[df.BMI != 'No data']

def remove_range(cell):
    return cell.split(' ')[0]

df.BMI = df.BMI.apply(remove_range)

df.BMI = pd.to_numeric(df.BMI)

countries = df.Country.unique()
years = df.Year.unique()
years.sort()

dict = {country: [] for country in countries}
for country in countries:
    for year in years:
        value = df[df.Country == country][df.Year == year].BMI
        if value.empty == True:
            dict[country].append(float('NaN'))
        else:
            dict[country].append(float(df[df.Country == country][df.Year == year].BMI))

df = pd.DataFrame(dict)

df['Year'] = [i for i in range(years[0], years[-1]+1)]

df = df.set_index('Year')

df.to_csv('data/processed/BMI_data.csv')