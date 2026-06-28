from linear_model import LinearModel, LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

"""
Use the model to predict how many people are attacked per lunar day 
when the moon's brightness is 0 (completely dark).
"""
df = pd.read_csv('lion-attacks-lunar-cycle.csv')
dark_attacks = df.query('evening_moonlight == 0')
print(dark_attacks)

plt.figure(figsize=(6, 3))
plt.scatter(dark_attacks['lunar_day'], dark_attacks['attacks'], alpha=0.5)
plt.xlabel('Lunar Day')
plt.ylabel('No. of Attacks')
plt.show()

