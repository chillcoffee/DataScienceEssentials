import pandas as pd

df = pd.read_csv('solar-eclipses.csv')
# print(df)

ec = df[['date', 'duration']]
# print(ec)

