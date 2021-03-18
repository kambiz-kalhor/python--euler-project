#!/usr/bin/env python
# coding: utf-8

# # euler project  problem 1

# In[49]:


#give me the maximum number##in this problem it is 100
Sum = 0
for i in range (1,10):
    if ((i%3 == 0) or (i%5 == 0)):
        Sum = Sum + i
print("the final Sum is : ", Sum )


# In[ ]:




