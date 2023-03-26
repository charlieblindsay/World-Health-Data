import pandas as pd

def change_dataframe_structure(df: pd.DataFrame) -> pd.DataFrame:
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
    
    return df
