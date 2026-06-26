import pandas as pd

df = pd.read_csv('solar-eclipses.csv')
# print(df)

ec = df[['date', 'duration']]
# print(ec)

ec['duration'] = ec['duration'].str.replace('s', '')
print(ec)

ec_duration = ec['duration'].str.split('m',  expand=True)
ec_duration = ec_duration.dropna()
ec_duration = ec_duration.astype('int')
print(ec_duration)

ec[['m', 's']] = ec_duration
# print(ec)

ec = ec.dropna()
ec['total_seconds'] = ec.eval('m * 60 + s')
print(ec)
print(ec.query('total_seconds == total_seconds.max()'))


