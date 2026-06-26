import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('male-elephant-tusk-size.csv')
pre_poaching = df.query('period == "1966-68"')
post_recovery = df.query('period == "2005-13"')

# print(pre_poaching.head(3))

# print("Before:", pre_poaching['tusk_length'].mean())
# print("After:", post_recovery['tusk_length'].mean())