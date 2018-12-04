
# coding: utf-8

# # Assignment 3 - Building a Custom Visualization
# 
# ---
# 
# In this assignment you must choose one of the options presented below and submit a visual as well as your source code for peer grading. The details of how you solve the assignment are up to you, although your assignment must use matplotlib so that your peers can evaluate your work. The options differ in challenge level, but there are no grades associated with the challenge level you chose. However, your peers will be asked to ensure you at least met a minimum quality for a given technique in order to pass. Implement the technique fully (or exceed it!) and you should be able to earn full grades for the assignment.
# 
# 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ferreira, N., Fisher, D., & Konig, A. C. (2014, April). [Sample-oriented task-driven visualizations: allowing users to make better, more confident decisions.](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf) 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 571-580). ACM. ([video](https://www.youtube.com/watch?v=BI7GAs-va-Q))
# 
# 
# In this [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf) the authors describe the challenges users face when trying to make judgements about probabilistic data generated through samples. As an example, they look at a bar chart of four years of data (replicated below in Figure 1). Each year has a y-axis value, which is derived from a sample of a larger dataset. For instance, the first value might be the number votes in a given district or riding for 1992, with the average being around 33,000. On top of this is plotted the 95% confidence interval for the mean (see the boxplot lectures for more information, and the yerr parameter of barcharts).
# 
# <br>
# <img src="readonly/Assignment3Fig1.png" alt="Figure 1" style="width: 400px;"/>
# <h4 style="text-align: center;" markdown="1">  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 1 from (Ferreira et al, 2014).</h4>
# 
# <br>
# 
# A challenge that users face is that, for a given y-axis value (e.g. 42,000), it is difficult to know which x-axis values are most likely to be representative, because the confidence levels overlap and their distributions are different (the lengths of the confidence interval bars are unequal). One of the solutions the authors propose for this problem (Figure 2c) is to allow users to indicate the y-axis value of interest (e.g. 42,000) and then draw a horizontal line and color bars based on this value. So bars might be colored red if they are definitely above this value (given the confidence interval), blue if they are definitely below this value, or white if they contain this value.
# 
# 
# <br>
# <img src="readonly/Assignment3Fig2c.png" alt="Figure 1" style="width: 400px;"/>
# <h4 style="text-align: center;" markdown="1">  Figure 2c from (Ferreira et al. 2014). Note that the colorbar legend at the bottom as well as the arrows are not required in the assignment descriptions below.</h4>
# 
# <br>
# <br>
# 
# **Easiest option:** Implement the bar coloring as described above - a color scale with only three colors, (e.g. blue, white, and red). Assume the user provides the y axis value of interest as a parameter or variable.
# 
# 
# **Harder option:** Implement the bar coloring as described in the paper, where the color of the bar is actually based on the amount of data covered (e.g. a gradient ranging from dark blue for the distribution being certainly below this y-axis, to white if the value is certainly contained, to dark red if the value is certainly not contained as the distribution is above the axis).
# 
# **Even Harder option:** Add interactivity to the above, which allows the user to click on the y axis to set the value of interest. The bar colors should change with respect to what value the user has selected.
# 
# **Hardest option:** Allow the user to interactively set a range of y values they are interested in, and recolor based on this (e.g. a y-axis band, see the paper for more details).
# 
# ---
# 
# *Note: The data given for this assignment is not the same as the data used in the article and as a result the visualizations may look a little different.*

# In[4]:

import pandas as pd
import numpy as np
np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])


# In[5]:

get_ipython().magic('matplotlib notebook')
import math
cols=list(df.columns.values)
global ct
ct=0
def average_year(row):
    global ct
    try:
        values=[row[cols[i]] for i in cols]
        row['avg']=np.mean(values)
        row['std']=np.std(values)
        row['err']=1.96*row['std']/math.sqrt(3650)
    except:
        None
    ct=ct+1
    return row
df1=df.apply(average_year,axis=1)


# In[114]:

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
fig=plt.figure(figsize=(5,2.5))
def plotgraph(event):
    plt.clf()
    my_cmap = plt.cm.get_cmap('viridis')
    if event!=None:
        data_colors=[i/max(df1['avg'])*event.ydata/max(df1['avg']) for i in df1['avg']] 
        #i took event.ydata/max(df1['avg']) as factor which can be changed as per use
    else:
        data_colors=[i/max(df1['avg']) for i in df1['avg']]
    colors = my_cmap(data_colors)
    rects = plt.bar(df1.index, df1['avg'], yerr=df1['err'], color=colors)
    sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(min(data_colors),max(data_colors)))
    sm.set_array([])
    cbar = plt.colorbar(sm)
    cbar.set_label('Color', rotation=270,labelpad=25)
    plt.xticks(df.index)
    h_line=plt.axhline(y=35000,color="black",linestyle='-')
    y_vals=list(plt.yticks()[0])
    plt.yticks(y_vals+[35000])
    print(data_colors)
    plt.title("Assignment 3")
    plt.xlabel("Years")
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    def xyz(event):
        h_line.set_ydata(event.ydata)
        plt.yticks([])
        plt.yticks(y_vals+[event.ydata])
    if event!=None:
        xyz(event)
plotgraph(None)


# In[115]:

def onclick(event):
    plotgraph(event)
plt.gcf().canvas.mpl_connect('button_press_event', onclick)

