import pandas as pd
import matplotlib.pyplot as plt
"""
Create a horizontal bar chart to compare the diving depths of animals within a specific group, such as penguins."""
def clean_bar_axes( ):
    ax = plt.gca() # get current axis
    ax.spines[['top','bottom','left','right']].set_visible(False)
    ax.grid(axis='x', color='black', alpha=0.5)
    ax.tick_params(axis='both', length=0)

df = pd.read_csv('deepest-diving-animals.csv')
# print(df)
penguins = df.query('category == "penguins"')

penguins = penguins[['animal', 'depth']]

plt.figure(figsize=(12, 6))
penguins = penguins.sort_values('depth')
penguins['color'] = 'C0'
plt.barh(penguins['animal'], penguins['depth'], color=penguins['color'])
clean_bar_axes()
# plt.show()

