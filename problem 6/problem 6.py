#!/usr/bin/env python
# coding: utf-8

# # a code to tell us the sum of the square of the numbers in a range

# In[102]:



SumOfSquares=0
for i in range (1,11):
    SumOfSquares=(SumOfSquares + (i**2))
print (SumOfSquares)

    


# # a code to tell us the square of the sum of the numbers in a range

# In[116]:


Sums=0
for i in range (1,11):
    Sums=(Sums + i)
SquareOfSums = Sums**2    
print (SquareOfSums)


# # a code to calculate the difference

# In[ ]:


difference = SquareOfSums - SumOfSquares


# # combine all

# In[121]:



###############
SumOfSquares=0
for i in range (1,101):
    SumOfSquares=(SumOfSquares + (i**2))
print (SumOfSquares)

###############
Sums=0
for i in range (1,101):
    Sums=(Sums + i)
SquareOfSums = Sums**2    
print (SquareOfSums)

##############
difference = SquareOfSums - SumOfSquares
print("the difference is :", difference)


# In[ ]:




