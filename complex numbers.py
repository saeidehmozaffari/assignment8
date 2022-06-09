#!/usr/bin/env python
# coding: utf-8

# In[9]:


def summ(x,y):
    result['r']=x['r']+y['r']
    result['i']=x['i']+y['i']
    return result

def subb(x,y):
    result['r']=x['r']-y['r']
    result['i']=x['i']-y['i']
    return result

def mull(x,y):
    result['r']=x['r']*y['r']-x['i']*y['i']
    result['i']=x['i']*y['r']+x['r']*y['i']
    return result

def show(m):
    print(m['r'],'+',m['i'],'i')
    
result={}
m1={'r':10,'i':20}
m2={'r':5,'i':4}

show(summ(m1,m2))
show(subb(m1,m2))
show(mull(m1,m2))

