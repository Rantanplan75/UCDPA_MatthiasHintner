import pandas as pd

df = pd.read_csv('athlete_events.csv')
df1 = pd.read_csv('noc_regions.csv')
print(df.head())
print(df.info())
print(df1.head())
print(df1.info())
