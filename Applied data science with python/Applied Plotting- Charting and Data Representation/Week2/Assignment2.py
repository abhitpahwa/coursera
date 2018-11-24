
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[1]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))
    
    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# In[36]:

df=pd.read_csv("data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv")
df=df.sort(['ID','Date'])
df['year'], df['Month-Date'] = zip(*df['Date'].apply(lambda x: (x[:4], x[5:])))
df = df[df['Month-Date'] != '02-29']


# In[52]:

import numpy as np
df1=df[df['year']!='2015']
min_temp_df=df1[df1['Element']=='TMIN']
min_temp=min_temp_df.groupby(['Month-Date']).aggregate({'Data_Value':np.min})          
max_temp_df=df1[df1['Element']=='TMAX']
max_temp=max_temp_df.groupby(['Month-Date']).aggregate({'Data_Value':np.max})
df2=df[df['year']=='2015']
min_temp_df2=df2[df2['Element']=='TMIN']
min_temp2=min_temp_df2.groupby(['Month-Date']).aggregate({'Data_Value':np.min})
max_temp_df2=df2[df2['Element']=='TMAX']
max_temp2=max_temp_df2.groupby(['Month-Date']).aggregate({'Data_Value':np.max})
broken_min=np.where(min_temp['Data_Value']>min_temp2['Data_Value'])[0]
broken_max=np.where(max_temp['Data_Value']<max_temp2['Data_Value'])[0]
print(broken_min)


# In[91]:

plt.figure(1)
plt.gcf().set_size_inches(10,6.5)
plt.plot(min_temp.values,'springgreen',label='min_temp 2005-14')
plt.plot(max_temp.values,'lightcoral',label='max_temp 2005-14')
plt.scatter(broken_min,min_temp2.iloc[broken_min],c='r',label='broken record low')
plt.scatter(broken_max,max_temp2.iloc[broken_max],c='b',label='broken record high')
plt.xticks(range(0, len(min_temp), 20), min_temp.index[range(0, len(min_temp), 20)], rotation = '45')
plt.xlabel("Day of the year (Month-Day)")
plt.ylabel("Temperature (Tenths of ° celsius)")
plt.gca().fill_between(range(len(min_temp)), min_temp['Data_Value'], max_temp['Data_Value'], facecolor = 'silver', alpha = 0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.legend(loc=4,frameon=False)
plt.title("Climate Record (2004-15) for region near Ann Arbor, Michigan, United States")
plt.show()

