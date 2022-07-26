#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get("https://www.bbc.com/")
doc = BeautifulSoup(response.text)


# In[10]:


# Grab all headlines
# Use two underscores! 
titles = doc.select(".media__link")
titles


# In[12]:


for title in titles:
    print(title.text.strip())


# In[13]:


# Start with an empty list
rows = []

for title in titles:
    # Go through each title, building a dictionary
    # with a 'title' and a 'url'
    row = {}
    
    # title
    row['title'] = title.text.strip()
    # link
    row['url'] = title['href']
    
    # Then add it to our list of rows
    rows.append(row)

# then we're going to make a dataframe from it!!!
df = pd.DataFrame(rows)
df.head()


# In[14]:


df.to_csv("bbc.csv", index=False)


# In[ ]:




