#!/usr/bin/env python
# coding: utf-8

# In[99]:


# i = input
# n = all numbers before i
# this program takes too much time unfortunately
for i in range (2,999999999):
    c = 1
    if c==0:
        break
    for n in range (1,20):
        if c==0:
            break
        if (i%n) == 0:
            a=1
            c=c * a
        else:
            a=0
            c=c * a
            break
    if c== 1 :
        print (i)
        break

    

