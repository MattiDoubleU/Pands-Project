# Pands-Project

**by Matthias Wiedemann**

Student at [ATU](https://www.atu.ie/).

<img src="https://www.embedded-robotics.com/wp-content/uploads/2022/01/Iris-Dataset-Classification-1024x367.png">

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [1. Introduction / About this project](#1-introduction--about-this-project)
   * [1.1 Iris flower dataset](#11-iris-flower-dataset)
   * [1.2 Disclaimer:](#12-disclaimer)
   * [1.3 Code action](#13-code-action)
- [2. Imported libraries and modules](#2-imported-libraries-and-modules)
- [3. Dataset properties](#3-dataset-properties)
- [4. Graphical representation of data in a histogram](#4-graphical-representation-of-data-in-a-histogram)
- [5. Graphical representation of data in pairplots](#5-graphical-representation-of-data-in-pairplots)
- [6. Heatmaps: Graphical representation of sepal length vs width & petal length vs width of species combinded in scatter, -hist, & KDE plot](#6-heatmaps-graphical-representation-of-sepal-length-vs-width--petal-length-vs-width-of-species-combinded-in-scatter--hist--kde-plot)
   * [6.1 Scatter plot](#61-scatter-plot)
   * [6.2 Bivariate Histogram](#62-bivariate-histogram)
   * [6.3 Kernel Density Estimate (KDE) plot heatmap](#63-kernel-density-estimate-kde-plot-heatmap)
- [7. Graphical representation: Distribution plot](#7-graphical-representation-distribution-plot)
- [8. Two variable plot with best fit line](#8-two-variable-plot-with-best-fit-line)
- [9. Pearson Correlation Coefficient](#9-pearson-correlation-coefficient)
- [10. Conclusion](#10-conclusion)
- [11. References and further readings](#11-references-and-further-readings)
   * [11.1 pandas](#111-pandas)
   * [11.2 Seaborn](#112-seaborn)
   * [11.3 Matplotlib](#113-matplotlib)
   * [11.4 NumPy](#114-numpy)
   * [11.5 stackoverflow.com](#115-stackoverflowcom)
   * [11.6 Miscellaneous](#116-miscellaneous)

<!-- TOC end -->

## 1. Introduction / About this project

This [project](https://atu-main-mdl-euwest1.s3.eu-west-1.amazonaws.com/66/82/6682ae48f67ebab9c769ddae345221f3d6405bfe?response-content-disposition=inline%3B%20filename%3D%22Project%202024.pdf%22&response-content-type=application%2Fpdf&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAWRN6GJFLWCMOG6H7%2F20240503%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T150953Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21547&X-Amz-Signature=acbfbd441db6e3cd56ef3e3b9fcc1c2b1921963e00667cebf1c714bd8cd504a6) for the Programming and Scripting module is my analysis on the widely available [Iris flower data set](https://archive.ics.uci.edu/dataset/53/iris).

### 1.1 Iris flower dataset
The Iris flower dataset or Fisher's Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper 'The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis' (https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-anderson35-3).

### 1.2 Disclaimer:
Please note that I used some code from the [Principals of Data Analytics module project](https://github.com/MattiDoubleU/Principles_of_Data_Analytics_mywork/blob/main/penguins.ipynb) I completed two weeks earlier. 

### 1.3 Code action
Upon execution of the code, it will generate the following outputs:
    * The code will compile numerical items into a text file named "summary.txt."
    * Graphical representations will be saved as .png image files.

## 2. Imported libraries and modules
* [pandas](https://pandas.pydata.org/): pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language. 
* [Seaborn](https://seaborn.pydata.org/): Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
* [Matplotlib](https://matplotlib.org/): Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible. 
* [NumPy](https://numpy.org/): The fundamental package for scientific computing with Python.

## 3. Dataset properties
First of all I have chosen to display the data in its entirety as opposed to truncated *df.to_string()*. It requires a bit of scrolling down in the text file but it's still reasonable as there are a total of 150 lines only which translates to 150 samples taken, that is 50 taken from three different flower species each *df.groupby()*: Setosa, Versicolor & Virginica. Next we see the stastical description *df.describe()* of the data set devided into four columns for each of the variables: 
* sepal length (*slen*) 
* sepal width (*swidth*) 
* petal length (*plen*) 
* petal width (*pwidth*) 
and eight lines: Count, mean, standard deviation, min & max (minimum & maximum value observed for each feature), 25%, 50%, & 75% percentile, hence first quartile, which is the value below which 25% of the observations fall, median half of the observation fall below and half above that value and last third quartile, which is the value below which 75% of the observations fall. Finally the data types are presented *df.types*: 
* variables are 'float64'.
* species is 'object'.

## 4. Graphical representation of data in a histogram
As per the project instructions, a histogram for each variable is required. For this task, I used Matplotlib's *fig, axs = plt.subplots()* function to generate histograms of the four variables identified in section 3 within a single 2x2 figure. Each species is represented by a different color, allowing for easier comparison.

To demonstrate how bar opacity varies with different values, I utilized descending alpha values e.g *alpha=0.4*, to show opacity decreases with smaller values.
Also, since all histograms are displayed on the same figure, I tweaked the output size by adding parameter 'figsize' (*fig, axs = plt.subplots(2, 2, figsize=(10, 6.5))*). This ensures that the entire figure is clearly visible on a 14" laptop screen.

Clear insights the four histograms provide:
* Virginica species exhibits the largest petal width, petal length, and sepal length on average.
* On the contrary, Setosa species, although having the smallest petal width and length, features the largest sepal width among the three species.

## 5. Graphical representation of data in pairplots
I decided to use Seaborn's pairplot function *sns.pairplot()*: A single line of code that generates pairplots that illustrate pairwise relationships between all the numeric features of all variables in the Iris dataset (df) with a 'Kernel Density (kde) Plot' for each individual feature on the diagonal. The Kde plots generated by the this code use the Gaussian Kernel technique which models smooth curves indicating data density, influenced by the bandwidth parameter. Additionally, the hue parameter is set to 'species' (*hue='species'*), which colors the data points based on the value of the 'species' column, allowing for easy visualization of how the variables relate to different species of Iris flowers. The palette parameter is set to 'rocket' (*palette='rocket'*), which specifies the color palette used for differentiating between species. I also included markers 'o', 's' & 'D' using the *markers=["o", "s", "D"]* parameter to distinguish each species with a different symbol in addition to color. Finally, to ensure the plot displays conveniently on a 14" laptop screen, I specified the 'height' and 'aspect' parameters (*height=1.6, aspect=1*) at the end of the code.

```python
sns.pairplot(df, hue='species', palette='rocket', markers=["o", "s", "D"], height=1.6, aspect=1)
```

Let's examine the plots to identify some useful insights and patterns from the dataset:

It is the Setosa species that typically has smaller sepal lengths and widths, often forming a tight cluster in the lower left of the scatter plot.
On the contrary Versicolor and Virginica species usually have larger sepal lengths and widths, with Virginica generally being the largest. They form separate clusters that might overlap.
Scatter plot between petal width and petal length reveals a linear relationship. Additionally, this relationship allows for linear separation of all the classes.
When petal width/length is plotted against sepal width/length, Iris Setosa is clearly separated from Iris Versicolor and Iris Virginica.
Sepal width shows a linearly separable relationship between all the classes, whereas sepal length shows a mix of the classes, making them not linearly separable.

This has also been demonstrated in [Awais Naeem's](https://www.embedded-robotics.com/iris-dataset-classification/) January 27, 2022 published work who used the same Seaborn pairplot function *sns.pairplot()* to perform exploratory data analysis of the Iris dataset.

## 6. Heatmaps: Graphical representation of sepal length vs width & petal length vs width of species combinded in scatter, -hist, & KDE plot
Heatmaps are another useful tool to examine relationships between two different variables. First, instead of color-coding each species, I wanted to explore another Seaborn function *fig, ax = plt.subplots()* to compare variables in aggregate and generated three different heatmaps for sepal length vs width. Second,for variables petal length vs width I did want to color code each species by tweaking previous code slightly and adding *data* and *hue* parameters.

### 6.1 Scatter plot
Though not a heatmap I found it relevant to include a scatter plot in this paragraph for a lean 2x3 output figure so the same data can be easily compared through different visualization techniques. 

```python
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species', ax=ax4)
```

### 6.2 Bivariate Histogram
Strictly speaking not a heatmap but closely related, bivariate histogram bins the data into rectangles that tile the plot, displaying the count of observations within each rectangle using fill color. 

```python
sns.histplot(data=df, x='petal_length', y='petal_width', hue='species', multiple='stack', ax=ax5)
```

### 6.3 Kernel Density Estimate (KDE) plot heatmap
A KDE plot heatmap displays data values in a matrix format (as opposed to Gaussian Kernel, see section 5) by using color to represent the density of data points in two dimensions. Instead of showing counts in bins like a traditional 2D histogram, it shows the estimated density of data points. 

```python
sns.kdeplot(data=df, x='petal_length', y='petal_width', hue='species', palette="Spectral", fill=True, common_norm=False, ax=ax6)
```

## 7. Graphical representation: Distribution plot
Another graphical representation I was keen to explore is the distribution plot. It is used to visualize the distribution of a single variable, in this plot *petal_length* (or the relationship between multiple variables for that matter). Distribution plots help in understanding the underlying frequency or probability distribution of the data. I used bins size 30 *bins=30* to provide a more detailed view of the data. As demonstrated in section 5, the distribution of petal length clearly distinguishes Iris Setosa from both Iris Versicolor and Iris Virginica.

```python
sns.displot(df, x="petal_length", hue="species", bins=30)
```    

## 8. Two variable plot with best fit line
I wanted to demonstrate the application of a best-fit line (or regression line) to summarize the overall trend between two variables, sepal length vs petal width. For this operation I used *np.polyfit()* to fit a polynomial of specified degree to the data points, and *np.linspace(min(slen), max(slen), 100)* for 100 evenly spaced numbers between min & max.
The line clearly slopes upwards from left to right what suggests a positive correlation, meaning that longer sepals are associated with wider petals.
    
```python   
m, c = np.polyfit(slen, pwidth, 1) 
bf_x = np.linspace(min(slen), max(slen), 100)  
bf_y = m * bf_x + c
```   

## 9. Pearson Correlation Coefficient
Since I have modeled a straight line on the scatter plot in section 8, which visualizes a positive correlation between sepal length and petal width, it is logical to further quantify this relationship by computing the Pearson Correlation Coefficient. This can be easily done by using *np.array()* (to combine *pwidth* and *slen* into a 2D array) & *np.corrcoef()* This coefficient, which measures the strength and direction of the linear relationship between the two variables, is calculated to be 0.82. This high value confirms what the straight line visually suggests: a strong positive relationship between sepal length and petal width.

```python
data = np.array([pwidth, slen])
correlation_coefficient_matrix = np.corrcoef(data) 
```

## 10. Conclusion
Running analysis.py explores various facets of the Iris flower dataset and demonstrates a range of code techniques to perform both graphical and numerical analyses of the dataset.

## 11. References and further readings

Iris flower data set: https://en.wikipedia.org/wiki/Iris_flower_data_set.

January 27, 2022 Awais Naeem, Iris Dataset Classification using Support Vector Machine, Random Forest, and Gradient Boosting Classifier https://www.embedded-robotics.com/iris-dataset-classification/.

### 11.1 pandas

pandas.DataFrame.groupby https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html.

### 11.2 Seaborn

Overview of seaborn plotting functions: https://seaborn.pydata.org/tutorial/function_overview.html.

seaborn.pairplot https://seaborn.pydata.org/generated/seaborn.pairplot.html.

Choosing color palettes https://seaborn.pydata.org/tutorial/color_palettes.html.

seaborn.axes_style https://seaborn.pydata.org/generated/seaborn.axes_style.html

seaborn.scatterplot https://seaborn.pydata.org/generated/seaborn.scatterplot.html.

seaborn.color_palette https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette. 

Visualizing distributions of data https://seaborn.pydata.org/tutorial/distributions.html.

### 11.3 Matplotlib

matplotlib.pyplot.hist https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html.

Histograms https://matplotlib.org/stable/gallery/statistics/hist.html.

Matplotlib Install an official release https://matplotlib.org/stable/users/installing/index.html.

matplotlib.pyplot.subplots https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html.

### 11.4 NumPy

numpy.polyfit https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy-polyfit.

numpy.linspace https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy-linspace.

numpy.array https://numpy.org/doc/stable/reference/generated/numpy.array.html.

numpy.corrcoef https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html.

### 11.5 stackoverflow.com

Directing print output to a .txt file: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file.

Create specific plots using Pandas and then store them as PNG files: https://stackoverflow.com/questions/64542466/how-to-create-specific-plots-using-pandas-and-then-store-them-as-png-files.

scatter subplot for iris dataset https://stackoverflow.com/questions/66493893/scatter-subplot-for-iris-dataset.

How to disable Python warnings? https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings.

Userwarning https://stackoverflow.com/questions/76901874/userwarning-the-figure-layout-has-changed-to-tight-self-figure-tight-layouta.

Plotting a heatmap based on a scatterplot in Seaborn https://stackoverflow.com/questions/70416424/plotting-a-heatmap-based-on-a-scatterplot-in-seaborn.

How to plot in multiple subplots? https://stackoverflow.com/questions/31726643/how-to-plot-in-multiple-subplots.

### 11.6 Miscellaneous

Plotting Histogram in Python using Matplotlib: https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/.

Histograms in Matplotlib https://www.datacamp.com/tutorial/histograms-matplotlib.

November 27, 2022 by Shikha Mishra, print entire dataframe panda – Python Pandas: How to display full Dataframe i.e. print all rows & columns without truncation https://btechgeeks.com/python-pandas-how-to-display-full-dataframe-i-e-print-all-rows-columns-without-truncation/.

January 25, 2020 Vijaykrishna Ram, Python – Print to File https://www.askpython.com/python/built-in-methods/python-print-to-file.

Histograms in Matplotlib https://www.datacamp.com/tutorial/histograms-matplotlib.

Pearson correlation coefficient https://en.wikipedia.org/wiki/Pearson_correlation_coefficient.

Best fit line https://www.cuemath.com/geometry/y-mx-c/.

https://github.com/MattiDoubleU/Principles_of_Data_Analytics_mywork/blob/main/penguins.ipynb.

Change the line opacity in Matplotlib https://www.geeksforgeeks.org/change-the-line-opacity-in-matplotlib/.



