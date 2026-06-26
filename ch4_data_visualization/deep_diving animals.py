import matplotlib.pyplot as plt
def clean_bar_axes( ):
    ax = plt.gca() # get current axis
    ax.spines[['top','bottom','left','right']].set_visible(False)
    ax.grid(axis='x', color='black', alpha=0.5)
    ax.tick_params(axis='both', length=0)

