import pandas as pd

df = pd.read_parquet('yellow_tripdata_2009-01.parquet')
df.to_csv('Jan_2009_yellow.csv', index=False)

print(df.head(20))