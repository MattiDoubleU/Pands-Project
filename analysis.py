# Data frames: Pandas:
import pandas as pd

# Data frames: Seaborn:
import seaborn as sns

# Plotting.
import matplotlib.pyplot as plt

# Numerical arrays.
import numpy as np

# Latest version of matplotlib now installed (v.3.7.3) but I decided to keep the error warning module but inside triple quotes to see if the program now doesn't throw the error without it, but
# also to demonstrate my work and I am learning by doing.
# I kept getting the following warning: UserWarning: The figure layout has changed to tight self._figure.tight_layout(*args, **kwargs). 
# It's a warning so the pair plot (line 154) would still generate though it's cleaner without it. I found out that apparently there's a bug and I would need to install
# matplotlib 3.7.3 (mine is 3.7.2): https://stackoverflow.com/questions/76901874/userwarning-the-figure-layout-has-changed-to-tight-self-figure-tight-layouta but I also researched a quick fix:
'''
import warnings                                # https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings.
warnings.filterwarnings('ignore')
'''
# Load Data: We we will use df to define data frame.
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

df = sns.load_dataset('iris')

# Let's have a look at the imported data set (I wanted an entire view of it as opposed to truncated, therefore df.to_string():
entire_df = df.to_string()

# Show.
print(entire_df)

# Group the DataFrame by 'species' and count the number of occurrences. Pandas documentation pandas.DataFrame.groupby: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
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

# I previously had created four individual histograms for each of the four variables but decided to create one single figure with four histograms. My research brought me to
# matplotlib documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html. The fig & axs parameters helped to achieve this without much change to
# my original code but I had to add the axs[] before operation to define the location of the histogram on the plot e.g. [0, 0] top left etc. (in clock wise order)
# Create a figure with four subplots on two rows.
fig, axs = plt.subplots(2, 2, figsize=(10, 6.5))  # figsize=(): selected values (10 y axes & 6.5 x axes) so the figures fits a 14" laptop screen nicely.

# a) Create histogram for petal width.
axs[0, 0].hist([df[df['species'] == 'setosa']['petal_width'],    # axs[0, 0] top left.
                df[df['species'] == 'versicolor']['petal_width'],
                df[df['species'] == 'virginica']['petal_width']],
               bins='auto', stacked=False, color=['green', 'blue', 'orange'], # bins set to auto for the most appropriate representation.
               alpha=1, label=['setosa', 'versicolor', 'virginica'])          # The alpha parameter in Matplotlib adjusts the transparency of the plotted elements: https://www.geeksforgeeks.org/change-the-line-opacity-in-matplotlib/

# Set labels and title.
axs[0, 0].set_xlabel('Petal width (cm)')
axs[0, 0].set_ylabel('Count')
axs[0, 0].set_title('Petal width for Setosa, Versicolor & Virginica species')

# Add legend.
axs[0, 0].legend()

# b) Create histogram for petal length. 
axs[0, 1].hist([df[df['species'] == 'setosa']['petal_length'],  # axs[0, 1] top right.
                df[df['species'] == 'versicolor']['petal_length'],
                df[df['species'] == 'virginica']['petal_length']],
               bins='auto', stacked=False, color=['green', 'blue', 'orange'],
               alpha=0.8, label=['setosa', 'versicolor', 'virginica'])
axs[0, 1].set_xlabel('Petal length (cm)')
axs[0, 1].set_ylabel('Count')
axs[0, 1].set_title('Petal length for Setosa, Versicolor & Virginica species')
axs[0, 1].legend()

# c) Create histogram for sepal width.
axs[1, 0].hist([df[df['species'] == 'setosa']['sepal_width'],    # axs[1, 0] bottom left.
                df[df['species'] == 'versicolor']['sepal_width'],
                df[df['species'] == 'virginica']['sepal_width']],
               bins='auto', stacked=False, color=['green', 'blue', 'orange'],
               alpha=0.6, label=['setosa', 'versicolor', 'virginica'])
axs[1, 0].set_xlabel('Sepal width (cm)')
axs[1, 0].set_ylabel('Count')
axs[1, 0].set_title('Sepal width for Setosa, Versicolor & Virginica species')
axs[1, 0].legend()

# d) Create histogram for sepal length.
axs[1, 1].hist([df[df['species'] == 'setosa']['sepal_length'],   # axs[1, 1] bottom right.
                df[df['species'] == 'versicolor']['sepal_length'],
                df[df['species'] == 'virginica']['sepal_length']],
               bins='auto', stacked=False, color=['green', 'blue', 'orange'],
               alpha=0.4, label=['setosa', 'versicolor', 'virginica'])
axs[1, 1].set_xlabel('Sepal length (cm)')
axs[1, 1].set_ylabel('Count')
axs[1, 1].set_title('Sepal length for Setosa, Versicolor & Virginica species')
axs[1, 1].legend()

# plt.tight_layout() to ensure the plots don't overlap.
plt.tight_layout()

# Save the figure as a single .png file
plt.savefig('histograms_all_variables')

# Show plot
plt.show()

# Pairplots of all variables. https://seaborn.pydata.org/generated/seaborn.pairplot.html
sns.pairplot(df, hue='species', palette='rocket', markers=["o", "s", "D"], height=1.6, aspect=1) # height=1.6 & aspect=1 tweaking output size to fit a 14" laptop screen nicely.
                                                                                                 # and added markers=[] to demonstrate that there is a variety of options.

# Save to png.
plt.savefig('pair_plot_all_variables')

# Show plot.
plt.show()

# Heatmaps.
# I also wanted to explore heatmaps and again decided to plot in multiple subplots, this time demonstrating different tyoes of heatmaps:
# scatterplot, histplot & kde plot, though strictly speaking a scatterplot is not a heatmap.

# Plotting heatmaps petal_length vs petal_width & sepal_length vs sepal_width.
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(ncols=3, nrows=2, figsize=(10, 6.5), sharex=True, sharey=True)

sns.set_style('darkgrid')
sns.scatterplot(x=df['sepal_length'], y=df['sepal_width'], ax=ax1)
sns.histplot(x=df['sepal_length'], y=df['sepal_width'], ax=ax2)
sns.kdeplot(x=df['sepal_length'], y=df['sepal_width'], fill=True, ax=ax3) # kde plot (Kernel Density Estimate) plot.

sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species', ax=ax4) # Assigning a variable to hue will map its levels to the color of the points.
sns.histplot(data=df, x='petal_length', y='petal_width', hue='species', multiple='stack', ax=ax5) # stacks the histograms for different categories on top of each other within the same plot.
sns.kdeplot(data=df, x='petal_length', y='petal_width', hue='species', palette="Spectral", fill=True, common_norm=False, ax=ax6) # Adding 'palette' to demonstrate the use of different color schemes.
                                                                                                                                 # By setting common_norm=False, each subset will be normalized independently.
# Add titles.
ax1.set_title('sepal_length vs sepal_width - Scatterplot')
ax2.set_title('sepal_length vs sepal_width - Histplot')
ax3.set_title('sepal_length vs sepal_width - KDE Plot')
ax4.set_title('petal_length vs petal_width - Scatterplot')
ax5.set_title('petal_length vs petal_width - Histplot')
ax6.set_title('kpetal_length vs petal_width - KDE Plot')
plt.tight_layout()     # plt.tight_layout() to ensure the plots don't overlap.

# Save to png.
plt.savefig('heatmaps')

# Show plot.
plt.show()

# Distribution plot.
sns.displot(df, x="petal_length", hue="species", bins=30)

# Save to png.
plt.savefig('distribution_plot')

# Show plot.
plt.show()

# Below lines and ideas are loosely based on Ian's lectures.

# Two variable plot: sepal_length vs petal_width with best fit line.
# Define colors for each species by creating dictionary. 
colors = {'setosa': 'green', 'versicolor': 'orange', 'virginica': 'blue'}

# Create a new figure and set of axes.
fig, ax = plt.subplots(1, 1)

# Plot the data points with color coding based on species.
for i in range(len(slen)):
    species_color = colors[df['species'][i]] if df['species'][i] in colors else 'k'  # Access species column / # It's a common convention in programming to use 'k' to represent black and 'i'(index) as loop variable.
    ax.plot(slen[i], pwidth[i], 'o', c=species_color)

# Compute the best fit line: y = mx + c (https://www.cuemath.com/geometry/y-mx-c/).
m, c = np.polyfit(slen, pwidth, 1) 
bf_x = np.linspace(min(slen), max(slen), 100)  # X values for best fit line & 100 for 100 evenly spaced numbers between min & max.
bf_y = m * bf_x + c                            # Y values for best fit line.

# Plot the best fit line.
ax.plot(bf_x, bf_y, 'r-', label='Best Fit Line')  # r is for red, - dash for line.


# Axis labels.
ax.set_xlabel('sepal length (cm) ')
ax.set_ylabel('petal width  (cm) ')

# Add legend.
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='setosa', markerfacecolor='green', markersize=5),
                   plt.Line2D([0], [0], marker='o', color='w', label='versicolor', markerfacecolor='orange', markersize=5),
                   plt.Line2D([0], [0], marker='o', color='w', label='virginica', markerfacecolor='blue', markersize=5)]
ax.legend(handles=legend_elements, loc='upper left')

# Title.
ax.set_title('sepal length vs petal width')

# Save to .png.
plt.savefig('sepal_length_vs_petal_width')

# Show plot.
plt.show()

# Pearson correlation coefficient (https://en.wikipedia.org/wiki/Pearson_correlation_coefficient).
# Combine pwidth and slen into a 2D array.
data = np.array([pwidth, slen])

# Measure the correlation.
correlation_coefficient_matrix = np.corrcoef(data)

# Extract the correlation coefficient between body mass and flipper length from the correlation matrix.
correlation_coefficient = correlation_coefficient_matrix[0, 1]

print("Correlation coefficient between petal width and sepal length is:",correlation_coefficient)

with open("summary.txt", "a") as f:    # "a" append to summary.txt (if "w" is used it would overwrite the .txt generated in line 47 to 52).
    print("Correlation coefficient between petal width and sepal length is:", correlation_coefficient, file=f)

