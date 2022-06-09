#!/usr/bin/env python
# coding: utf-8

# In[11]:


def mul(x,y):
    result['s']=x['s']*y['s']
    result['m']=x['m']*y['m']
    return result
def summ(x,y):
    result['s']=x['s']*y['m']+y['s']*x['m']
    result['m']=x['m']*y['m']
    return result
def subb(x,y):
    result['s']=x['s']*y['m']-y['s']*x['m']
    result['m']=x['m']*y['m']
    return result
def div(x,y):
    result['s']=x['s']*y['m']
    result['m']=x['m']*y['s']
    return result
def show(z):
    print(z['s'],'/',z['m'])

result={}
a = {'s':4 , 'm':3}
b = {'s':3 , 'm':4}

r = mul(a,b)
show(r)
s=summ(a,b)
show(s)
c=subb(a,b)
show(c)
d=div(a,b)
show(d)


# In[ ]:




