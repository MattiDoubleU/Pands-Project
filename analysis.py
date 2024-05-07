# Data frames: Pandas:
import pandas as pd

# Data frames: Seaborn:
import seaborn as sns

# Plotting.
import matplotlib.pyplot as plt

# Numerical arrays.
import numpy as np

# Load Data: We we will use df to define data frame.
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

df = sns.load_dataset('iris')

# Let's have a look at the imported data set (I wanted an entire view of it as opposed to truncated, therefore df.to_string():
entire_df = df.to_string()

# Show.
df.to_string()

# Inspect data types:
print(df.dtypes)

# Group the DataFrame by 'species' and count the number of occurrences. This code was proposed by ChatGPT.
species_counts = df.groupby(['species']).size().reset_index(name='count')

print("Number of samples for each species:")
print(species_counts)

# Return a statistically description of the data in df:
summary_stats = df.describe()

# Save summary and statistics to a text file:
with open("summary.txt", "w") as f:     # changed "a" append to "w" (write) so after each iteration the file is overwritten.
    print(entire_df, file=f)
    print(summary_stats, file=f)
    print(df.dtypes, file=f)
    print("Number of samples for each species:", file=f)
    print(species_counts, file=f) 


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

# Create histogram.

plt.hist([df[df['species'] == 'setosa']['petal_width'],
          df[df['species'] == 'versicolor']['petal_width'],
          df[df['species'] == 'virginica']['petal_width']],
         bins=10, stacked=False, color=['green', 'blue', 'orange'],
         alpha=0.8, label=['setosa', 'versicolor', 'virginica'])

# Set labels and title
plt.xlabel('Petal width (cm)')
plt.ylabel('Count')
plt.title('Petal width for Setosa, Versicolor & Virginica species')

# Add legend.
plt.legend()

# Show plot.
plt.show()

# Below here is just scrippling for now.

'''

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
