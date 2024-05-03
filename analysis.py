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

# Inspect data types:
print(df.dtypes)

# Return a statistically description of the data in df:
summary_stats = df.describe()

# Save summary statistics to a text file:
with open("summary.txt", "a") as f:     # "a" append: Output added to previous output instead of overwriting it.
    print(entire_df, file=f)
    print(summary_stats, file=f)
    print(df.dtypes, file=f)
