# Loading data into Snowflake

import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

tsv_file_path = 'title.basics.tsv' 

df = pd.read_csv(tsv_file_path, sep='\t')
df['isAdult'] = df['isAdult'].replace(0, False)
df['isAdult'] = df['isAdult'].replace(1, True)
df['tconst'] = df['tconst'].astype(str)
df['tconst'] = df['tconst'].str.lstrip('t')
df['tconst'] = df['tconst'].str.lstrip('0')
df['tconst'] = df['tconst'].astype(int)
df = df.rename(columns={'tconst':'id'})
df['endYear'] = df['endYear'].replace('\\N', None)
df['runtimeMinutes'] = df['runtimeMinutes'].replace('\\N', None)

print(df.head())

# dummy connection details
conn = snowflake.connector.connect(
    user='your_username',
    password='your_password',
    account='your_account_identifier',
    warehouse='your_warehouse',
    database='your_database',
    schema='your_schema'
)

table_name = 'imdb_title_basics'
success, nchunks, nrows = write_pandas(conn, df, table_name, auto_create_table=True)

if success:
    print(f"Successfully loaded {nrows} rows into {table_name} in {nchunks} chunks.")
else:
    print("Failed to load data.")

# Close the connection
conn.close()