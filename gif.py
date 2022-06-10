#!/usr/bin/env python
# coding: utf-8

# In[2]:


import imageio
import os

images=[]
for file_name in os.listdir('images'):
    image=imageio.imread(f'images/{file_name}')
    images.append(image)
    
imageio.mimsave('fun.gif',images)

