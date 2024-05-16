# pands-project

**by Matthias Wiedemann**

Student at [ATU] (https://www.atu.ie/).

<img src="https://www.embedded-robotics.com/wp-content/uploads/2022/01/Iris-Dataset-Classification-1024x367.png">

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [1. Introduction / About this project](#1-introduction-about-this-project)
   * [1.1 Iris flower dataset](#11-iris-flower-dataset)
   * [1.2 Disclaimer:](#12-disclaimer)
   * [1.3 Code action](#13-code-action)
- [2. Imported libraries and modules](#2-imported-libraries-and-modules)
- [3. Dataset properties](#3-dataset-properties)
- [4. Graphical representation of data in a histogram](#4-graphical-representation-of-data-in-a-histogram)
- [5. Graphical representation of data in pairplots](#5-graphical-representation-of-data-in-pairplots)
- [6. Graphical representation of sepal length vs width of species combinded in scatter, -hist, & KDE plot](#6-graphical-representation-of-sepal-length-vs-width-of-species-combinded-in-scatter-hist-kde-plot)
- [7. Graphical representation of petal length vs width of species combinded in scatter, -hist, & KDE plot](#7-graphical-representation-of-petal-length-vs-width-of-species-combinded-in-scatter-hist-kde-plot)
- [8. Two variable plot with best fit line](#8-two-variable-plot-with-best-fit-line)
- [9. Person Correlation Coefficient.](#9-person-correlation-coefficient)
- [10. References and further readings:](#10-references-and-further-readings)

<!-- TOC end -->

<!-- TOC --><a name="1-introduction-about-this-project"></a>
## 1. Introduction / About this project

This [project](https://atu-main-mdl-euwest1.s3.eu-west-1.amazonaws.com/66/82/6682ae48f67ebab9c769ddae345221f3d6405bfe?response-content-disposition=inline%3B%20filename%3D%22Project%202024.pdf%22&response-content-type=application%2Fpdf&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAWRN6GJFLWCMOG6H7%2F20240503%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20240503T150953Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21547&X-Amz-Signature=acbfbd441db6e3cd56ef3e3b9fcc1c2b1921963e00667cebf1c714bd8cd504a6) for the Programming and Scripting module is my analysis on the widely available [Iris flower data set](https://archive.ics.uci.edu/dataset/53/iris).

<!-- TOC --><a name="11-iris-flower-dataset"></a>
### 1.1 Iris flower dataset
The Iris flower dataset or Fisher's Iris data set is a multivariate data set used and made famous by the British statistician and biologist Ronald Fisher in his 1936 paper 'The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis' (https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-anderson35-3).

<!-- TOC --><a name="12-disclaimer"></a>
### 1.2 Disclaimer:
Please note that I used some code from the [Principals of Data Analytics module project](https://github.com/MattiDoubleU/Principles_of_Data_Analytics_mywork/blob/main/penguins.ipynb) I completed two weeks earlier. 

<!-- TOC --><a name="13-code-action"></a>
### 1.3 Code action
Upon execution of the code, it will generate the following outputs:
    * The code will compile the items into a text file named "summary.txt."
    * Graphical representations  will be saved as .png image files.

<!-- TOC --><a name="2-imported-libraries-and-modules"></a>
## 2. Imported libraries and modules
* [pandas](https://pandas.pydata.org/): pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language. 
* [Seaborn](https://seaborn.pydata.org/): Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
* [Matplotlib](https://matplotlib.org/): Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible. 
* [NumPy](https://numpy.org/): The fundamental package for scientific computing with Python.

<!-- TOC --><a name="3-dataset-properties"></a>
## 3. Dataset properties
First of all I have chosen to display the data in its entirety as opposed to truncated *df.to_string()*. It requires a bit of scrolling down in the text file but it's still reasonable as there are a total of 150 lines only which translates to 150 samples taken, that is 50 taken from three different flower species each *df.groupby()*: Setosa, Versicolor & Virginica. Next we see the stastical description *df.describe()* of the data set devided into four columns for each of the variables, which are sepal -length & width and petal -length & width and eight lines: Count, mean, standard deviation, min & max (minimum & maximum value observed for each feature), 25%, 50%, & 75% percentile, hence first quartile, which is the value below which 25% of the observations fall, median half of the observation fall below and half above that value and last third quartile, which is the value below which 75% of the observations fall. Finally the data types are presented *df.types*: variables are float64 whereas species is object.

<!-- TOC --><a name="4-graphical-representation-of-data-in-a-histogram"></a>
## 4. Graphical representation of data in a histogram
As per the project instructions, a histogram for each variable is required. For this task, I used Matplotlib's *fig, axs = plt.subplots()* function to generate histograms of the four variables identified in 3. within a single 2x2 figure. Each species is represented by a different color, allowing for easier comparison.

To demonstrate how bar opacity varies with different values, I utilized descending alpha values, to show opacity decreases with smaller values.

The four histograms provide clear insights:
* Virginica species exhibits the largest petal width, petal length, and sepal length on average.
* On the contrary, Setosa species, although having the smallest petal width and length, features the largest sepal width among the three species.

<!-- TOC --><a name="5-graphical-representation-of-data-in-pairplots"></a>
## 5. Graphical representation of data in pairplots
I decided to use Seaborn's pairplot function *sns.pairplot()*: A single line of code that generates pairplots that illustrate pairwise relationships between all the numeric features of all variables in the Iris dataset (df) with a 'Kernel Density (kde) Plot' for each individual feature on the diagonal. Additionally, the hue parameter is set to 'species', which colors the data points based on the value of the 'species' column, allowing for easy visualization of how the variables relate to different species of Iris flowers. The palette parameter is set to 'rocket', which specifies the color palette used for differentiating between species.

Let's examine the plots to identify some useful insights and patterns from the dataset:

Kde plots for petal width and petal length show that Iris Setosa can be distinguished from Iris Versicolor and Iris Virginica using either of these features.
Scatter plot between petal width and petal length reveals a linear relationship. Additionally, this relationship allows for linear separation of all the classes.
When petal width/length is plotted against sepal width/length, Iris Setosa is clearly separated from Iris Versicolor and Iris Virginica.
sepal width shows a linearly separable relationship between all the classes, whereas sepal length shows a mix of the classes, making them not linearly separable.

This has also been demonstrated in [Awais Naeem's](https://www.embedded-robotics.com/iris-dataset-classification/) January 27, 2022 published work who used the same Seaborn pairplot function *sns.pairplot()* to perform exploratory data analysis of the Iris dataset.

<!-- TOC --><a name="6-graphical-representation-of-sepal-length-vs-width-of-species-combinded-in-scatter-hist-kde-plot"></a>
## 6. Graphical representation of sepal length vs width of species combinded in scatter, -hist, & KDE plot
* Scatter plot
* Histogram
* Kernel Density Estimate (KDE) plot

<!-- TOC --><a name="7-graphical-representation-of-petal-length-vs-width-of-species-combinded-in-scatter-hist-kde-plot"></a>
## 7. Graphical representation of petal length vs width of species combinded in scatter, -hist, & KDE plot
* Scatter plot
* Histogram
* Kernel Density Estimate (KDE) plot

<!-- TOC --><a name="8-two-variable-plot-with-best-fit-line"></a>
## 8. Two variable plot with best fit line
* tba
* tba
* tba

<!-- TOC --><a name="9-person-correlation-coefficient"></a>
## 9. Person Correlation Coefficient.
* tba
* tba
* tba

<!-- TOC --><a name="10-references-and-further-readings"></a>
## 10. References and further readings:

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

matplotlib.pyplot.subplots https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html