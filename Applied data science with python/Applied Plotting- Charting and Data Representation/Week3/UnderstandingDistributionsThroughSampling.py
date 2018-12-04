
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[2]:

import matplotlib.pyplot as plt
import numpy as np

get_ipython().magic('matplotlib notebook')

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

# plot the histograms
plt.figure(1,figsize=(9,3))
plt.hist(x1, normed=True, bins=20, alpha=0.5)
plt.hist(x2, normed=True, bins=20, alpha=0.5)
plt.hist(x3, normed=True, bins=20, alpha=0.5)
plt.hist(x4, normed=True, bins=20, alpha=0.5);
plt.axis([-7,21,0,0.6])

plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')
print(np.max(x2),np.min(x2))
print(np.max(x3),np.min(x3))
print(np.max(x4),np.min(x4))


# In[3]:

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
ax1.hist(x1,normed=True,bins=20,alpha=0.5)
ax2.hist(x2,normed=True,bins=20,alpha=0.5)
ax3.hist(x3,normed=True,bins=20,alpha=0.5)
ax4.hist(x4,normed=True,bins=20,alpha=0.5)


# In[4]:

fig1, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharey=True)
import matplotlib.animation as anim
ax=[ax1,ax2,ax3,ax4]
x=[x1,x2,x3,x4]
bins1=np.arange(-6.5,1.2,0.5)
bins2=np.arange(0,14.5,0.3)
bins3=np.arange(7,15,0.3)
bins4=np.arange(14,20,0.2)
bins=[bins1,bins2,bins3,bins4]
def animations_func(curr):
    if curr==100:
        a.event_source.stop()
    for i in range(4):
        ax[i].cla()
        ax[i].hist(x[i][:curr],bins=bins[i],alpha=0.5,normed=True)
a=anim.FuncAnimation(fig1,animations_func,interval=10)      
        

