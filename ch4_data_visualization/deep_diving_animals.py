import matplotlib.pyplot as plt
import pandas as pd

def clean_bar_axes( ):
    ax = plt.gca() # get current axis
    ax.spines[['top','bottom','left','right']].set_visible(False)
    ax.grid(axis='x', color='black', alpha=0.5)
    ax.tick_params(axis='both', length=0)

divers = pd.read_csv('deepest-diving-animals.csv')

max_depths = divers.groupby('category')['depth'].max()
df = max_depths.reset_index(name='max_depth')
print(df)

df['color'] = 'C0'
df.loc['ref_0'] = ['submarine implosion', 730, 'C1']
df = df.sort_values('max_depth')
print(df)

plt.figure(figsize=(500, 100))
plt.barh(df['category'], df['max_depth'], color=df['color'])
plt.xlabel('Maximum Diving Depth (meters)')

clean_bar_axes()
plt.show()



