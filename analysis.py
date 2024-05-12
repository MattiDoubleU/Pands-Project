# Data frames: Pandas:
import pandas as pd

# Data frames: Seaborn:
import seaborn as sns

# Plotting.
import matplotlib.pyplot as plt

# Numerical arrays.
import numpy as np

# I kept getting the following warning: UserWarning: The figure layout has changed to tight self._figure.tight_layout(*args, **kwargs). 
# It's a warning so the pair plot (line 154) would still generate though it's cleaner without it. I found out that apparently there's a bug and I would need to install
# matplotlib 3.7.3 (mine is 3.7.2): https://stackoverflow.com/questions/76901874/userwarning-the-figure-layout-has-changed-to-tight-self-figure-tight-layouta but I also researched a quick fix:

import warnings                                # https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings.
warnings.filterwarnings('ignore')

# Load Data: We we will use df to define data frame.
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

df = sns.load_dataset('iris')

# Let's have a look at the imported data set (I wanted an entire view of it as opposed to truncated, therefore df.to_string():
entire_df = df.to_string()

# Show.
print(entire_df)

# Group the DataFrame by 'species' and count the number of occurrences. This code was proposed by ChatGPT.
species_counts = df.groupby(['species']).size().reset_index(name='count')

print("Number of samples for each species:")
print(species_counts)

# Inspect data types:
print(df.dtypes)

# Return a statistically description of the data in df:
summary_stats = df.describe()
print(summary_stats)

# Save summary and statistics to a text file:
with open("summary.txt", "w") as f:     # changed "a" append to "w" (write) so after each iteration the file is overwritten.
    print(entire_df, file=f)
    print("Number of samples for each species:", file=f)
    print(species_counts, file=f) 
    print(summary_stats, file=f)
    print(df.dtypes, file=f)
    

# In order to be able to create plots on the data we need to set variables and transform the data to numpy array. Let's begin with the petal lengths.
plen = df['petal_length']

# Numpy array.
plen = plen.to_numpy()

# Now petal width. In fact, we can condense the previous two lines into one:
pwidth = df['petal_width'].to_numpy()

# Sepal length.
slen = df['sepal_length'].to_numpy()

# Sepal width.
swidth = df['sepal_width'].to_numpy()

# Create histogram for a) petal width for each of the three species
plt.hist([df[df['species'] == 'setosa']['petal_width'],
          df[df['species'] == 'versicolor']['petal_width'],
          df[df['species'] == 'virginica']['petal_width']],
         bins='auto', stacked=False, color=['green', 'blue', 'orange'],
         alpha=0.6, label=['setosa', 'versicolor', 'virginica']) # The alpha parameter in Matplotlib adjusts the transparency of the plotted elements.

# Set labels and title
plt.xlabel('Petal width (cm)')
plt.ylabel('Count')
plt.title('Petal width for Setosa, Versicolor & Virginica species')

# Add legend.
plt.legend()

# Save to png
plt.savefig('petal_width_histogram.png')

# Show plot.
plt.show()

# Repeating above code for b) petal length
plt.hist([df[df['species'] == 'setosa']['petal_length'],
          df[df['species'] == 'versicolor']['petal_length'],
          df[df['species'] == 'virginica']['petal_length']],
         bins='auto', stacked=False, color=['green', 'blue', 'orange'],
         alpha=0.6, label=['setosa', 'versicolor', 'virginica'])

# Set labels and title
plt.xlabel('Petal length (cm)')
plt.ylabel('Count')
plt.title('Petal length for Setosa, Versicolor & Virginica species')

# Add legend
plt.legend()

# Save to png
plt.savefig('petal_length_histogram.png')

# Show plot
plt.show()

# c) Sepal width
plt.hist([df[df['species'] == 'setosa']['sepal_width'],
          df[df['species'] == 'versicolor']['sepal_width'],
          df[df['species'] == 'virginica']['sepal_width']],
         bins='auto', stacked=False, color=['green', 'blue', 'orange'],
         alpha=0.6, label=['setosa', 'versicolor', 'virginica'])

# Set labels and title
plt.xlabel('Sepal width (cm)')
plt.ylabel('Count')
plt.title('Sepal width for Setosa, Versicolor & Virginica species')

# Add legend
plt.legend()

# Save to png
plt.savefig('sepal_width_histogram.png')

# Show plot
plt.show()


# d) Sepal length
plt.hist([df[df['species'] == 'setosa']['sepal_length'],
          df[df['species'] == 'versicolor']['sepal_length'],
          df[df['species'] == 'virginica']['sepal_length']],
         bins='auto', stacked=False, color=['green', 'blue', 'orange'],
         alpha=0.6, label=['setosa', 'versicolor', 'virginica'])

# Set labels and title
plt.xlabel('Sepal length (cm)')
plt.ylabel('Count')
plt.title('Sepal length for Setosa, Versicolor & Virginica species')

# Add legend
plt.legend()

# Save to png
plt.savefig('sepal_length_histogram.png')

# Show plot
plt.show()


# Pairplots of all variables
sns.pairplot(df, hue='species', palette='viridis')

# Save to png
plt.savefig('pair_plot_all_variables')

# Show plot
plt.show()

# Heatmaps
# Plotting heatmaps sepal_length vs sepal_width - this won't save to .cng file as I decided to create one single figure as per below
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(10, 4), sharex=True, sharey=True)

sns.set_style('darkgrid')
sns.scatterplot(x=df['sepal_length'], y=df['sepal_width'], ax=ax1)
sns.histplot(x=df['sepal_length'], y=df['sepal_width'], ax=ax2)
sns.kdeplot(x=df['sepal_length'], y=df['sepal_width'], fill=True, ax=ax3)

ax1.set_title('scatterplot')
ax2.set_title('histplot')
ax3.set_title('kdeplot')
plt.tight_layout()

# Show plot
plt.show()

# Plotting heatmaps petal_length vs length_width 
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(10, 4), sharex=True, sharey=True)

sns.set_style('darkgrid')
sns.scatterplot(x=df['petal_length'], y=df['petal_width'], ax=ax1)
sns.histplot(x=df['petal_length'], y=df['petal_width'], ax=ax2)
sns.kdeplot(x=df['petal_length'], y=df['petal_width'], fill=True, ax=ax3)

ax1.set_title('scatterplot')
ax2.set_title('histplot')
ax3.set_title('kdeplot')
plt.tight_layout()

# Show plot
plt.show()

# Plotting heatmaps petal_length vs petal_width & sepal_length vs sepal_width
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(ncols=3, nrows=2, figsize=(10, 6), sharex=True, sharey=True)

sns.set_style('darkgrid')
sns.scatterplot(x=df['sepal_length'], y=df['sepal_width'], ax=ax1)
sns.histplot(x=df['sepal_length'], y=df['sepal_width'], ax=ax2)
sns.kdeplot(x=df['sepal_length'], y=df['sepal_width'], fill=True, ax=ax3)

sns.scatterplot(x=df['petal_length'], y=df['petal_width'], ax=ax4)
sns.histplot(x=df['petal_length'], y=df['petal_width'], ax=ax5)
sns.kdeplot(x=df['petal_length'], y=df['petal_width'], fill=True, ax=ax6)

ax1.set_title('sepal_length vs sepal_width - Scatterplot')
ax2.set_title('sepal_length vs sepal_width - Histplot')
ax3.set_title('sepal_length vs sepal_width - KDE Plot')
ax4.set_title('petal_length vs petal_width - Scatterplot')
ax5.set_title('petal_length vs petal_width - Histplot')
ax6.set_title('kpetal_length vs petal_width - KDE Plot')
plt.tight_layout()     # plt.tight_layout() to ensure the plots don't overlap.

plt.savefig('heatmaps.png')

# Show plot
plt.show()

# Below here is just scrippling for now.

'''
from plotly.express import scatter_3d
# Plotting in 3D by plotly.express that would show the plot with capability of zooming,
# changing the orientation, and rotating
scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_length', size="petal_width",
                   color="species", color_discrete_map={"Joly": "blue", "Bergeron": "violet", "Coderre": "pink"})\
            .show()




# Create simple Plot.
plt.plot(plen, pwidth, 'o')   # Displays as 'Os'

# Axis labels.
plt.xlabel('Petal Length (cm) ')
plt.ylabel('Petal Width (cm) ')

# Title.
plt.title('Iris Data Set')

# X limits
plt.xlim(0, 8)

# Y limits
plt.ylim(0, 4)

# Show.
plt.show()


# Let's create a basic histogram on petal length.
plt.hist(plen, bins=30, color='skyblue', edgecolor='black')
 
# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
 
# Display the plot
plt.show()

# Creating a customized histogram with a density plot
sns.histplot(plen, bins=30, kde=True, color='lightgreen', edgecolor='red')
 
# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Customized Histogram with Density Plot')
 
# Display the plot
plt.show()
'''
