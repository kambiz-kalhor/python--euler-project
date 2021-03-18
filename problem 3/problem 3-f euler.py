#!/usr/bin/env python
# coding: utf-8

# # define a function  ***is it prime number***

# In[27]:


# I is the input
#is it prime function
def ISITPRIME(I):
    I= int(I)
    r=1   
    for counter in range (2, ((I//2)+1)):
        if (I%counter)== 0:
            r=0
            break
    if r==0:
        print ("its not prime")
    if r==1:
        print ("its prime")
        print("here----------stop--------------here")
        
ISITPRIME (input("please give me a number"))


# # define a function to find the biggest factors one by one

# In[46]:


MI = int(input("please give me the main input:"))
for counter in range (2, int((MI/2)+1)):
    if ((MI% counter)==0):
        SmallFactor = counter
        BigFactor= (MI/counter)
        print(BigFactor)
        


# # combine the two programs above

# In[50]:


MI = int(input("please give me the main input:"))
for counter in range (2, int((MI/2)+1)):
    if ((MI% counter)==0):
        SmallFactor = counter
        BigFactor= (MI/counter)
        print(BigFactor)
        print (ISITPRIME (BigFactor))
        
        
        
# I is the input
#is it prime function
def ISITPRIME(I):
    I= int(I)
    r=1   
    for counter in range (2, ((I//2)+1)):
        if (I%counter)== 0:
            r=0
            break
    if r==0:
        print ("its not prime")
    if r==1:
        print ("its prime")
        print("here----------stop--------------here")












# In[5]:


finish = False
# I is the input
#is it prime function
def ISITPRIME(I):
    I= int(I)
    r=1   
    for counter in range (2, ((I//2)+1)):
        if (I%counter)== 0:
            r=0
            break
    if r==0:
        print ("its not prime")
    if r==1:
        print ("its prime")
        print("stop----------",I,"--------------stop")
        finish = True
            
            
MI = int(input("please give me the main input:"))
if finish == False :
    for counter in range (2, int((MI/2)+1)):
        if ((MI% counter)==0):
            SmallFactor = counter
            BigFactor= (MI/counter)
            print(BigFactor)
            print (ISITPRIME (BigFactor))
        
        
        











# In[ ]:




