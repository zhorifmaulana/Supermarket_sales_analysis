#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


pwd


# In[11]:


csv_data = pd.read_csv(r"C:\Users\User\Downloads\supermarket_sales - Sheet1.csv")


# In[15]:


#MEnampilkan data berdasarkan kolom
print(csv_data['City'])


# In[16]:


print(csv_data.iloc[1])


# In[17]:


print(csv_data.describe(exclude=['O']))


# In[20]:


print(csv_data.describe(include='all'))


# In[21]:


print(csv_data.isnull().values.any()) #to check the missing value


# In[ ]:




