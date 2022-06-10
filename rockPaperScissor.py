#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
game=['rock','paper','scissor']
score={'user':0,'computer':0}
for i in range(10):
    computerChoice=random.choice(game)
    print(computerChoice)
    userChoice=input('choice rock or paper or scissor')
    if userChoice=='rock' and computerChoice=='scissor' or userChoice=='paper' and computerChoice=='rock' or userChoice=='scissor'and computerChoice=='paper':
        score['user']+=1
        print('user win')
    elif computerChoice=='rock' and userChoice=='scissor' or computerChoice=='paper' and userChoice=='rock' or computerChoice=='scissor'and userChoice=='paper':
        score['computer']+=1 
        print('computer win')
    else:
        print('no one win')
    
    
if score['user']>score['computer']:
    print('user score:',score['user'],'\n','computer score:',score['computer'],'\n','user win')
elif score['user']<score['computer']:
    print('user score:',score['user'],'\n','computer score:',score['computer'],'\n','computer win')
else:
    print('user score:',score['user'],'\n','computer score:',score['computer'],'\n','no one win')


# In[ ]:




