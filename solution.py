#!/usr/bin/env python
# coding: utf-8

# ## Plotly Imports

# In[1]:


import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True) 


# Importing pandas and reading the csv file "2014_World_Power_Consumption" :

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('2014_World_Power_Consumption')


# The head of the DataFrame:

# In[4]:


df.head()


# Creating a Choropleth Plot of the Power Consumption for Countries using the data and layout dictionary:

# In[5]:


data = dict(type='choropleth',
           locations= df['Country'],locationmode = "country names",
            z = df['Power Consumption KWH'],
            text = df['Text'],
            colorbar={'title':'Power consumptions in KWH'},
            colorscale = 'YlGnBu') 


# In[6]:


layout = dict(title = '2014_World_Power_Consumption',
              geo = dict(showframe = False, projection = {'type':'mercator'}))


# In[7]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap, validate=False)


# ## USA Choropleth
# 
# Importing the 2012_Election_Data csv file using pandas:

# In[8]:


usdf=pd.read_csv('2012_Election_Data')


# The head of the DataFrame:

# In[9]:


usdf.head()


# Now I'll create a plot that displays the Voting-Age Population (VAP) per state:

# In[10]:


data = dict(type='choropleth',
            colorscale = 'Viridis',
            reversescale = True,
            locations = usdf['State Abv'],
            z = usdf['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
            text = usdf['State'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar = {'title':"Voting-Age Population (VAP)"}
            ) 


# In[11]:


layout = dict(title = '2012 General Election Voting Data',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )


# In[12]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)

