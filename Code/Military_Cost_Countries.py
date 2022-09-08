#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[1]:


import pandas as pd
import warnings
import numpy as np
import matplotlib.pyplot as plt
import bar_chart_race as bcr

warnings.filterwarnings("ignore")


# ---
# * Extract Data

# In[2]:


df = pd.read_csv('CSV_FILE')
df.drop(['Code','Type','Indicator Name'], axis=1, inplace=True)
df = df.T
df = df.iloc[:,1:]
df.columns = df.iloc[0,:]
df = df.iloc[1:,:]
df.index.name = 'Dates'
df = df.fillna(0)

df = df[['Hungary','Austria','Germany','Bulgaria','United Kingdom','France','Luxembourg',
         'Italy','Denmark','Finland','Slovak Republic','Ireland','Spain','Malta','Croatia',
         'Poland','Lithuania','Slovenia','Romania','Latvia','Netherlands','Estonia','Belgium',
         'Czech Republic','Greece','Portugal','Sweden','Cyprus']]


# * Create the plot

# In[ ]:


bcr.bar_chart_race(df = df, 
                   figsize = (6,3),
                   #filename = 'European_Military_Cost.html',  
                   n_bars = 20, 
                   fixed_max = True, 
                   #fixed_order = True,
                   dpi = 300, 
                   filter_column_colors = True,
                   cmap = 'dark12',
                   title = 'European Military Costs')


# In[ ]:




