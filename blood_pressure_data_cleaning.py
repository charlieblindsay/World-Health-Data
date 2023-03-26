import pandas as pd
from utilities.file_paths import raw_data_path, processed_data_path

df = pd.read_csv(raw_data_path / 'BMI_data.csv')

def get_column_name(column):
    if column.name == 'Unnamed: 0':
        return 'Country'
    else:
        year = column.name[:4]
        gender = column.iloc[2].replace(' ', '_')
        return f'{year} ({gender})'

df.columns = [get_column_name(df[column_name]) for column_name in df.columns]

# Removing the first 3 meaningless rows
df = df.iloc[3:]

df = df.set_index('Country')

def remove_range(cell):
    return cell.split(' ')[0]

for column_name in df.columns:
    df[column_name] = df[column_name].apply(remove_range)

column_names_of_columns_to_drop = []

for column_name in df.columns:
    if column_name.split(' ')[1] != '(Both_sexes)':
        column_names_of_columns_to_drop.append(column_name)

df = df.drop(labels=column_names_of_columns_to_drop, axis=1)

df.columns = [column_name.split(' ')[0] for column_name in df.columns]

countries = df.index
countries_to_remove = []

for country in countries:
    if df.loc[country]['2015'] == 'No':
        countries_to_remove.append(country)

df = df.drop(labels=countries_to_remove, axis=0)

for column_name in df.columns:
    df[column_name] = pd.to_numeric(df[column_name], downcast='float')

# To use the lineplot function from seaborn, the years must be the rows and the countries the columns. 
# This is so that the years appear onthe x-axis of the plot.
df = df.transpose()

df = df.reset_index()

df.columns = df.columns[1:].insert(0, 'Year')

# Sort years into ascending order so they are displayed in this way in the lineplot
df = df.sort_values(by='Year', ascending=True)

df.set_index('Year')

df.to_csv(processed_data_path / 'BMI_data.csv', index=False)