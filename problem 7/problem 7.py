#!/usr/bin/env python
# coding: utf-8

# In[9]:


ListPrimeNumbers=[2,3]
import sys
for i in range (4,99999999999999):
    ListPrimeNumbers.append(i)
    #length = len(ListPrimeNumbers)
    for counter in range (2, (int(i/2)+1)):
        if (i%counter)==0:
            ListPrimeNumbers.remove(i)
            if len(ListPrimeNumbers)==10001:
                print(ListPrimeNumbers)
                print(len(ListPrimeNumbers), "is the length of list")
                print(ListPrimeNumbers[10000], "is th 10001 th number of list")
                sys.exit()
            break


# In[3]:


import sys
for i in range(1,100):
    print(i)
    if i==5:
        sys.exit()


# In[ ]:




