#!/usr/bin/env python
# coding: utf-8

# In[130]:


cd C:/Users/Suyog Thengale/Desktop


# In[131]:


import pandas as pd


# In[132]:


from sqlalchemy import create_engine


# In[133]:


db_file = r'datasets/salesdata.db'


# In[134]:


engine = create_engine(r"sqlite:///{}".format(db_file))


# In[135]:


sql = 'SELECT * from scores'


# In[136]:


sales_data_df=pd.read_sql(sql,engine)


# In[137]:


sales_data_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




