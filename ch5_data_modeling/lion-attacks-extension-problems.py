from linear_model import LinearModel, LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

"""
Use the model to predict how many people are attacked per lunar day 
when the moon's brightness is 0 (completely dark).
"""
df = pd.read_csv('lion-attacks-lunar-cycle.csv')
dark_attacks = df.query('evening_moonlight == 0')
dark_attacks = dark_attacks.sort_values('lunar_day')
print(df)
print(dark_attacks)

plt.figure(figsize=(6, 4))
plt.scatter(dark_attacks['lunar_day'], dark_attacks['attacks'], alpha=0.5)
plt.xlabel('Lunar Day')
plt.ylabel('No. of Attacks')

people_attacked_model = LinearModel('dark_attacks')
people_attacked_model.fit(dark_attacks['lunar_day'], dark_attacks['attacks'])
people_attacked_model.plot_model(0,31)
plt.show()
people_attacked_model.print_model_info()

