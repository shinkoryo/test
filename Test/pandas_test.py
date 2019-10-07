#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# df = pd.DataFrame(np.arange(12.0, 32.0).reshape((5, 4)), index=["a", "b", "c", "d", "e"], columns=["WW", "XX", "YY", "ZZ"])

df = pd.DataFrame({'A': [-20, -10, 0, 10, 20],
                   'B': ['2017-12-01 12:24', '2017-11-01 12:24', '2017-11-01 12:24', '2017-11-01 12:24', np.nan],
                   'C': ['2017-12-11 12:24', '2017-11-01 12:24', np.nan, np.nan, np.nan],
                   'D': ['2017-11-01 12:24', '2017-12-01 12:24', '2017-11-01 12:24', np.nan, np.nan]})

df


# In[2]:


df['E'] = pd.to_datetime(df['B'])
df['F'] = pd.to_datetime(df['C'])
df['G'] = pd.to_datetime(df['D'])


# In[3]:


df


# In[4]:


# df['max'] = np.vstack([df['E'],df['F']]).max(axis =0)
df['max'] = np.vstack([df['E'],df['F'],df['G']]).max(axis =0)


# In[5]:


df


# In[ ]:




