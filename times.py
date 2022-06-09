#!/usr/bin/env python
# coding: utf-8

# In[18]:


def sumtime(x,y):
    result['h']=x['h']+y['h']
    result['m']=x['m']+y['m']
    result['s']=x['s']+y['s']
    if result['s']>=60:
        result['s']-=60
        result['m']+=1
    if result['m']>=60:
        result['m']-=60
        result['h']+=1
    return result
def show(t):
    print(t['h'],':',t['m'],':',t['s'])
def subtimes(x,y):
    if x['s']<y['s']:
        if x['m']!=0:
            x['m']-=1
            x['s']+=60
        else:
            x['h']-=1
            x['m']+=59
            x['s']+=60
    if x['m']<y['m']:
        x['h']-=1
        x['m']+=60
    result['h']=x['h']-y['h']
    result['m']=x['m']-y['m']
    result['s']=x['s']-y['s']
    return result
def timeTosecond(x):
    result=x['h']*3600+x['m']*60+x['s']
    return result
def secondTotime(n):
    result['h']=n//3600
    n=n%3600
    result['m']=n//60
    result['s']=n%60
    return result
result={}
t1={'h':12,'m':45,'s':59}
t2={'h':2,'m':45,'s':12}
show(sumtime(t1,t2))
show(subtimes(t1,t2))
show(secondTotime(7200))
print(timeTosecond(t1))

