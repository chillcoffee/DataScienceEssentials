import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('male-elephant-tusk-size.csv')
pre_poaching = df.query('period == "1966-68"')
post_recovery = df.query('period == "2005-13"')

# print(pre_poaching.head(3))

# print("Before:", pre_poaching['tusk_length'].mean())
# print("After:", post_recovery['tusk_length'].mean())

"""
Activity Goals:
Plot tusk length vs shoulder height for both groups
Use a triangle marker for pre_poaching.
Use a square marker for post_recovery.
"""
plt.scatter(pre_poaching['shoulder_height'], pre_poaching['tusk_length'], marker='^')
plt.scatter(post_recovery['shoulder_height'], post_recovery['tusk_length'], marker='s')

plt.xlabel('Shoulder Height (cm)')
plt.ylabel('Tusk Length (cm)')
plt.text(x=200, y=120, s='Pre-poaching', color='C0')
plt.text(x=220, y=35, s='Post-recovery', color='C1')
