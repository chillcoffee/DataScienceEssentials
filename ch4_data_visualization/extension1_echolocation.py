import pandas as pd
import matplotlib.pyplot as plt
"""
Explore deep-sea divers of the midnight zone (depths exceeding 1,000 meters). Incorporate color encoding to indicate which of these species use echolocation.
"""

def clean_bar_axes( ):
    ax = plt.gca() # get current axis
    ax.spines[['top','bottom','left','right']].set_visible(False)
    ax.grid(axis='x', color='black', alpha=0.5)
    ax.tick_params(axis='both', length=0)

df = pd.read_csv('deepest-diving-animals.csv')
midnight = df.query('depth > 1000')
print(midnight)