import pandas as pd
import sqlite3

from utilities.file_paths import processed_data_path

conn = sqlite3.connect('database')
c = conn.cursor()

df = pd.read_csv(processed_data_path / 'population_data.csv')

print(df.columns)
 
c.execute('CREATE TABLE IF NOT EXISTS products (product_name text, price number)')
conn.commit()

df.to_sql('products', conn, if_exists='replace', index = False)
 
c.execute('''  
SELECT * FROM products WHERE price BETWEEN 300 AND 450
          ''')

for row in c.fetchall():
    print (row)