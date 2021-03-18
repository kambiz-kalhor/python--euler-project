#!/usr/bin/env python
# coding: utf-8

# In[ ]:


r=0
while r==0:   
    # I is the input
    #is it prime function
    def ISITPRIME(I):
        I= int(I)
       
        for counter in range (2, ((I//2)+1)):
            if (I%counter)== 0:
                r=0
                break
        if r==0:
            print ("its not prime")
        if r==1:
            print ("its prime")
            print("here------------------------here")
            


    MI = int(input("please give me the main input:"))

    for counter in range (2, int((MI/2)+1)):
        if ((MI% counter)==0):
            SmallFactor = counter
            BigFactor= (MI/counter)
            print(SmallFactor,BigFactor)
            result = ISITPRIME(int(BigFactor))
            print(result)


print ("finish")


# In[ ]:




