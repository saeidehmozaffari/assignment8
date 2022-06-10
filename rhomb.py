#!/usr/bin/env python
# coding: utf-8

# In[88]:


n=int(input('enter a number:'))

for i in range(n):
    if i<n//2+1:
        print((n//2-i)*' ',i*'*',end='')
        print((i-1)*'*')
    else:
        print((i-n//2)*' ',(n-i)*'*',end='')
        print((n-i-1)*'*')
        

