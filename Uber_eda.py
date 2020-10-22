#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


udata = pd.read_csv('uber_ride.csv')


# In[3]:


udata


# In[4]:


udata.isnull().sum()


# In[ ]:


## Deleting last row as least null values is there.


# In[7]:


udata.drop(udata.tail(1).index, inplace=True)


# In[8]:


udata.tail()


# In[9]:


udata.isnull().sum()


# In[10]:


udata.shape


# In[11]:


udata.dtypes


# In[13]:


udata['START_DATE*']=udata['START_DATE*'].astype('datetime64[ns]')
udata['END_DATE*']=udata['END_DATE*'].astype('datetime64[ns]')


# In[ ]:


## Presenting the time in a valuable way


# In[17]:


udata['duration']= udata['END_DATE*']-udata['START_DATE*']
udata['duration']= udata['duration'].dt.total_seconds()/60.0
udata['duration']= udata['duration'].astype('float')
udata['speed']=udata['MILES*']/(udata['duration']/60)


# In[ ]:


## Adding two new variable i.e duration and speed.


# In[18]:


udata


# In[36]:


plt.figure(figsize=(18,5))
sns.countplot(udata['PURPOSE*'], )


# In[19]:


gr=udata.groupby(['PURPOSE*']).mean()
print(gr)


# In[ ]:


## The above data table tells us the average time that can be taken w.r.t speed and distance for different places.


# In[26]:


udata.groupby(['PURPOSE*'])['duration'].sum().sort_values(ascending=True).plot(kind='barh',)


# In[27]:


## The above figure shows the total number of ride taken for each loctaion


# In[28]:


udata.groupby(['PURPOSE*'])['MILES*'].sum().sort_values(ascending=True).plot(kind='barh',)


# In[29]:


## The above table shows the total number of miles driven for each loction


# In[31]:


udata['speed'].median()


# In[38]:


## Creating Columns for Month and Hour in a Day
udata['month']=udata['START_DATE*'].dt.month
udata['hour']=udata['START_DATE*'].dt.hour


# In[40]:


udata.groupby('month')['MILES*'].sum().plot(kind='bar',)


# In[41]:


## From above table we can conclude that,the highest number of ride is in month 10.


# In[50]:


udata['hour'].value_counts().plot(kind='bar')
plt.title('Number of rides in particular hour')


# In[ ]:


## So, from above table we can conclude that the most drives are taken from 9am to 9 pm.

