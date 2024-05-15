# pands-project

**by Matthias Wiedemann**

Student at [ATU] (https://www.atu.ie/).

<img src="https://www.embedded-robotics.com/wp-content/uploads/2022/01/Iris-Dataset-Classification-1024x367.png">

## 1. Introduction / About this project

This [project](https://atu-main-mdl-euwest1.s3.eu-west-1.amazonaws.com/66/82/6682ae48f67ebab9c769ddae345221f3d6405bfe?response-content-disposition=inline%3B%20filename%3D%22Project%202024.pdf%22&response-content-type=application%2Fpdf&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAWRN6GJFLWCMOG6H7%2F20240503%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T150953Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21547&X-Amz-Signature=acbfbd441db6e3cd56ef3e3b9fcc1c2b1921963e00667cebf1c714bd8cd504a6) for the Programming and Scripting module is my analysis on the widely available [Iris flower data set](https://archive.ics.uci.edu/dataset/53/iris).

### 1.1 Iris flower dataset
The Iris flower dataset or Fisher's Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper 'The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis' (https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-anderson35-3).

### 1.2 Disclaimer:
Please note that I used some code from the [Principals of Data Analytics module project](https://github.com/MattiDoubleU/Principles_of_Data_Analytics_mywork/blob/main/penguins.ipynb) I completed two weeks earlier. 

### 1.3 Code action
Upon execution of the code, it will generate the following outputs:
    * The code will compile the items into a text file named "summary.txt."
    * Graphical representations  will be saved as .png image files.

## 2. Imported libraries and modules
* pandas 
* Seaborn
* Matplotlib
* NumPy

## 3. Dataset properties
* Species & count
* Variables
* Statistical description of dataset
* Data types

## 4. Graphical representation of data in a histogram
* Petal length 
* Petal width
* Sepal length
* Sepal width

## 5. Graphical representation of data in pairplots
* Pairwise relationships
* Hue parameter
* Color palette
* Insights and patterns

## 6. Graphical representation of sepal length vs width of species combinded in scatter, -hist, & KDE plot
* Scatter plot
* Histogram
* Kernel Density Estimate (KDE) plot

## 7. Graphical representation of petal length vs width of species combinded in scatter, -hist, & KDE plot
* Scatter plot
* Histogram
* Kernel Density Estimate (KDE) plot

## 8. Two variable plot with best fit line
* tba
* tba
* tba



3. Dataset properties
First of all I have chosen to display the data in its entirety as opposed to truncated. It requires a bit of scrolling down in the text file but it's still reasonable as there are a total of 150 lines only which translates to 150 samples taken. We now learn that 50 samples were taken from three different flower species each: Setosa, Versicolor & Virginica. Next we see the stastical description of the data set devided into four columns for each of the variables, which are sepal -length & width and petal -length & width and eight lines: Count, mean, standard deviation, min & max (minimum & maximum value observed for each feature), 25%, 50%, & 75% percentile, hence first quartile, which is the value below which 25% of the observations fall, median half of the observation fall below and half above that value and last third quartile, which is the value below which 75% of the observations fall.

4. Graphical representation of data in a histogram
As per project instruction a histogram of each variable is required. For this task I used Matplotlib *plt.hist()* function to generate histograms of the four variables in the dataset: Petal width & length as well as sepal width & length. I chose to use a different color to represent each species in the bar which allows for easier comparison.

5. Graphical representation of data in pairplots
I decided to use Seaborn's pairplot function: It generates pairplots that illustrate pairwise relationships between all the numeric features of all variables in the Iris dataset (df) with a 'Kernel Density (kde) Plot' for each individual feature on the diagonal. Additionally, the hue parameter is set to 'species', which colors the data points based on the value of the 'species' column, allowing for easy visualization of how the variables relate to different species of iris flowers. The palette parameter is set to 'rocket', which specifies the color palette used for differentiating between species.

Let's examine the plots to identify some useful insights and patterns from the dataset:

Kde plots for petal width and petal length show that Iris Setosa can be distinguished from Iris Versicolor and Iris Virginica using either of these features.
Scatter plot between petal width and petal length reveals a linear relationship. Additionally, this relationship allows for linear separation of all the classes.
When petal width/length is plotted against sepal width/length, Iris Setosa is clearly separated from Iris Versicolor and Iris Virginica.
sepal width shows a linearly separable relationship between all the classes, whereas sepal length shows a mix of the classes, making them not linearly separable.

This has also been demonstrated in [Awais Naeem's](https://www.embedded-robotics.com/iris-dataset-classification/) January 27, 2022 published work who used the same Seaborn pairplot function *sns.pairplot()* to perform exploratory data analysis of the Iris dataset.



Let's explore the items in 4.
* Each subplot displays different visualizations of the relationship between the measurements of sepal length and sepal width of iris flowers. Specifically:
* 1. Scatter plot showing the distribution of sepal length and sepal width.
* 2. Histogram representing the distribution of sepal length and sepal width.
* 3. Kernel Density Estimate (KDE) plot illustrating the density of the distribution of sepal length and sepal width.

Explore 5.  Different visualizations of the relationship between the measurements of petal length and petal width of iris flowers.
* 1. Scatter plot showing the distribution of petal length and petal width.
* 2. Histogram representing the distribution of petal length and petal width.
* 3. Kernel Density Estimate (KDE) plot illustrating the density of the distribution of petal length and petal width.
 
 Explore 6.
* tba, tba, tba, tba, tba, tba, tba






# References and further readings:

Iris flower data set: https://en.wikipedia.org/wiki/Iris_flower_data_set.

January 27, 2022 Awais Naeem, Iris Dataset Classification using Support Vector Machine, Random Forest, and Gradient Boosting Classifier https://www.embedded-robotics.com/iris-dataset-classification/.

Overview of seaborn plotting functions: https://seaborn.pydata.org/tutorial/function_overview.html.

Directing print output to a .txt file: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file.

November 27, 2022 by Shikha Mishra, print entire dataframe panda – Python Pandas: How to display full Dataframe i.e. print all rows & columns without truncation https://btechgeeks.com/python-pandas-how-to-display-full-dataframe-i-e-print-all-rows-columns-without-truncation/.

Plotting Histogram in Python using Matplotlib: https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/.

seaborn.pairplot https://seaborn.pydata.org/generated/seaborn.pairplot.html.

Create specific plots using Pandas and then store them as PNG files: https://stackoverflow.com/questions/64542466/how-to-create-specific-plots-using-pandas-and-then-store-them-as-png-files.

January 25, 2020 Vijaykrishna Ram, Python – Print to File https://www.askpython.com/python/built-in-methods/python-print-to-file

matplotlib.pyplot.hist https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html.

Histograms https://matplotlib.org/stable/gallery/statistics/hist.html.

Histograms in Matplotlib https://www.datacamp.com/tutorial/histograms-matplotlib.

scatter subplot for iris dataset https://stackoverflow.com/questions/66493893/scatter-subplot-for-iris-dataset.

Userwarning https://stackoverflow.com/questions/76901874/userwarning-the-figure-layout-has-changed-to-tight-self-figure-tight-layouta

How to disable Python warnings? https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings

Plotting a heatmap based on a scatterplot in Seaborn https://stackoverflow.com/questions/70416424/plotting-a-heatmap-based-on-a-scatterplot-in-seaborn 

Choosing color palettes https://seaborn.pydata.org/tutorial/color_palettes.html

seaborn.axes_style https://seaborn.pydata.org/generated/seaborn.axes_style.html

Matplotlib Install an official release https://matplotlib.org/stable/users/installing/index.html

Pearson correlation coefficient https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

Best fit line https://www.cuemath.com/geometry/y-mx-c/

numpy.polyfit https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy-polyfit 

https://github.com/MattiDoubleU/Principles_of_Data_Analytics_mywork/blob/main/penguins.ipynb

pandas.DataFrame.groupby https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

Change the line opacity in Matplotlib https://www.geeksforgeeks.org/change-the-line-opacity-in-matplotlib/

