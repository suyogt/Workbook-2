#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[2]:


import numpy as np


# In[ ]:


import glob


# In[16]:


all_data = pd.DataFrame()


# In[64]:


for f in glob.glob("downloads\datasets/weekly_call_data/weekdata*.xlsx"):
    df=pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)


# In[67]:


all_data.describe()


# In[ ]:





# In[ ]:





# In[ ]:




