import pandas as pd
from utilities.file_paths import raw_data_path, processed_data_path

if __name__ == '__main__':
    df_continents = pd.read_csv(raw_data_path / 'continent_data.csv')
    df_continents = df_continents[['alpha-3', 'sub-region', 'region']]
    df_continents.columns = ['Country_Code', 'sub-region', 'Continent']

    df_continents.to_csv(processed_data_path / 'continent_data.csv')