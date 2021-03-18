import time
starttime = time.time()


listofnumbers = [0,1,2,3]

n=0
for counter in range (1023456788,10000000000):
    counter = str(counter)
    listofnumbers = [0,1,2,3,4,5,6,7,8,9]

    
    listofnumbers.remove(int(counter[0]))
        
    if int(counter[1]) in listofnumbers:
        listofnumbers.remove(int(counter[1]))


        if int(counter[2]) in listofnumbers:
            listofnumbers.remove(int(counter[2]))
        
            if int(counter[3]) in listofnumbers:
                listofnumbers.remove(int(counter[3]))
           
                if int(counter[4]) in listofnumbers:
                    listofnumbers.remove(int(counter[4]))
                
                    if int(counter[5]) in listofnumbers:
                        listofnumbers.remove(int(counter[5]))

                        if int(counter[6]) in listofnumbers:
                            listofnumbers.remove(int(counter[6]))
                                                
                            if int(counter[7]) in listofnumbers:
                                listofnumbers.remove(int(counter[7]))
                            
                                if int(counter[8]) in listofnumbers:
                                    listofnumbers.remove(int(counter[8]))
                                
                                     
                                    if int(counter[9]) in listofnumbers:
                                        listofnumbers.remove(int(counter[9]))
                                        print(counter)
                                        n = n+1
                                        if n == 1000:
                                            break
                                    


                
finishtime = (time.time() - starttime)
print ("execution time is :  ",finishtime , "   seconds")
