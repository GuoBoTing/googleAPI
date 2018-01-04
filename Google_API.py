
# coding: utf-8

# In[1]:

import googlemaps
import pandas as pd


# In[15]:

gmaps = googlemaps.Client(key='AIzaSyCLuAKWgmYUvkmHweNE03XacrVkM3pW4_w') 


# In[16]:

cities = ["台北市", "桃園市", "新竹市"]


# In[17]:

ids = []


# In[26]:

for city in cities:
    geocode_result = gmaps.geocode(city)
    loc = geocode_result[0]['geometry']['location']
    print("以"+city+"為中心半徑25000公尺的燒肉店家數量: "+str(len(gmaps.places_radar(keyword="燒肉", 
                                                                      location=loc, radius=25000)['results'])))


# In[ ]:



