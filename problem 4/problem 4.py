#!/usr/bin/env python
# coding: utf-8

# In[14]:


#producing all 2-digit * 2-digit
a=999
for counter1 in range (100,1000):
    b=999
    for counter2 in range (100,1000):
        c = a*b 
        c = str(c)
        if (c[0]==c[-1])and(c[1]==c[-2]and (c[2]==c[-3])):
            
            if (int(c)> 900009):
                print (c)
        b=b-1  
    a = a-1


# In[ ]:





# In[ ]:





# In[ ]:




