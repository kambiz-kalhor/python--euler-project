#!/usr/bin/env python
# coding: utf-8

# In[10]:


a=1
b=2
c=a+b
Sum = 2

while c <4000000:
    a=b
    b=c
    c=a+b
    if (c%2==0):
        Sum = Sum + c
print (Sum)

