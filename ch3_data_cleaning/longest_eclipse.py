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
longest = ec.query('total_seconds == total_seconds.max()')
print(longest)
# print(f"\nLongest eclipse was on {str(longest['date'])} which was {longest['m']} and {longest['s']} seconds total of {longest['total_seconds']}.\n")
# print(type(longest))

"""
What is the average duration of total solar eclipses?
Show the next 10 solar eclipses?
"""
print(ec['total_seconds'].mean())



