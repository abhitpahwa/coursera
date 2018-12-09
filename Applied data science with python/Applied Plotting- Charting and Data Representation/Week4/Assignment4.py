
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **economic activity or measures** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **economic activity or measures**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **economic activity or measures**?  For this category you might look at the inputs or outputs to the given economy, or major changes in the economy compared to other regions.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
get_ipython().magic('matplotlib notebook')


# In[143]:

df=pd.read_csv("Data USA - Tree Map of Employment by Occupations in Ann Arbor, Mi.csv")
df1=df[df['year']==2013]
df1=df1.set_index('acs_occ_name')
total_emp_2013=np.sum(df1['num_emp'])
df1['percentage_contrib']=df1.apply(lambda x: x['num_emp']/total_emp_2013*100,axis=1)
df2=df[df['year']==2014]
df2=df2.set_index('acs_occ_name')
total_emp_2014=np.sum(df2['num_emp'])
df2['percentage_contrib']=df2.apply(lambda x: x['num_emp']/total_emp_2014*100,axis=1)
df3=df[df['year']==2015]
df3=df3.set_index('acs_occ_name')
total_emp_2015=np.sum(df3['num_emp'])
df3['percentage_contrib']=df3.apply(lambda x: x['num_emp']/total_emp_2015*100,axis=1)
df4=df[df['year']==2016]
df4=df4.set_index('acs_occ_name')
total_emp_2016=np.sum(df4['num_emp'])
df4['percentage_contrib']=df4.apply(lambda x: x['num_emp']/total_emp_2016*100,axis=1)
df1.head()


# In[175]:

plt.figure(figsize=(10,6))
x_ticks=list(df1.index)
x_values=[i*1.5 for i in range(len(x_ticks))]
grp1=[i*1.5 for i in range(11)]
grp1_df=df1[:11]
grp2=[17*1.5,18*1.5]
grp2_df=df1[17:19]
grp3=[i*1.5 for i in range(11,17)]
grp3_df=df1[11:17]
grp4=[22*1.5,23*1.5,24*1.5]
grp4_df=df1[22:25]
grp5=[i*1.5 for i in range(19,22)]
grp5_df=df1[19:22]
plt.bar(grp1,grp1_df['num_emp'],color='pink',width=1.2)
plt.bar(grp2,grp2_df['num_emp'],color='blue',width=1.2)
plt.bar(grp3,grp3_df['num_emp'],color='orange',width=1.2)
plt.bar(grp4,grp4_df['num_emp'],color='red',width=1.2)
plt.bar(grp5,grp5_df['num_emp'],color='brown',width=1.2)
plt.xticks(x_values,x_ticks,rotation=90,size=7)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
pink_patch=mpatches.Patch(color="pink",label="Management, Business, Science and Arts")
blue_patch=mpatches.Patch(color="blue",label="Sales and Office")
orange_patch=mpatches.Patch(color="orange",label="Service")
red_patch=mpatches.Patch(color="red",label="Production and transportation")
brown_patch=mpatches.Patch(color="brown",label="Natural resources, construction and maintenance")
plt.legend(handles=[pink_patch,blue_patch,orange_patch,red_patch,brown_patch],loc=1,prop={'size':7})
plt.xlabel("Occupation Name")
plt.ylabel("Number of employements")
plt.title("Employments by Education for year 2013",loc="left")
ax=plt.gca()
for i in ax.patches:
    x,y=i.get_x(),i.get_y()
    ax.text(x,y+i.get_height()+100,str(round(i.get_height()/total_emp_2013*100,2))+"%",size=5.5)
plt.tight_layout()


# In[176]:

from matplotlib.widgets import Button
class navigate(object):
    curr=1
    anim=list(set([occ for occ in df['acs_occ_name']]))
    def __init__(self,axes_next,axes_prev,ax,df):
        self.nextbtn=Button(axes_next,"next")
        self.nextbtn.on_clicked(self.next_fig)
        self.prevbtn=Button(axes_prev,"prev")
        self.prevbtn.on_clicked(self.prev_fig)
        self.ax=ax
        self.ax.set_xticks([2013,2014,2015,2016])
        self.df=df
        dfx=self.df[self.df['acs_occ_name']==self.anim[0]]
        self.ax.plot(dfx['year'],dfx['num_emp'])
        self.ax.set_title("Trend of "+self.anim[0])
        self.ax.set_ylim(0,11000)
        self.ax.set_xlabel("Years")
        self.ax.set_ylabel("Number of employees")
    def clear(self):
        for artists in self.ax.lines:
            artists.remove()
    def next_fig(self,event):
        if self.curr<24:
            self.curr=self.curr+1
            self.clear()
            self.ax.set_title("Trend of "+self.anim[self.curr])
            dfx=self.df[self.df['acs_occ_name']==self.anim[self.curr]]
            self.ax.plot(dfx['year'],dfx['num_emp'])
    def prev_fig(self,event):
        if self.curr>0:
            self.curr=self.curr-1
            self.clear()
            self.ax.set_title("Trend of "+self.anim[self.curr])
            dfx=self.df[self.df['acs_occ_name']==self.anim[self.curr]]
            self.ax.plot(dfx['year'],dfx['num_emp'])

plt.figure(5,figsize=(5,5))  
ax=plt.subplot(111)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
axprev = plt.axes([0.7, -0.01, 0.1, 0.05])
axnext = plt.axes([0.81, -0.01, 0.1, 0.05])
nav=navigate(axnext,axprev,ax,df)

