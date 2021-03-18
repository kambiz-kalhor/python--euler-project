import sys
Sum = 5
itsprime=True
for i in range (4,99999999999999):
    itsprime=True
    for counter in range (2, (int(i/2)+1)):
        if (i%counter)==0 :
            itsprime = False
            #print (i,"can be devided by " ,counter , "so its not prime")
            if itsprime == False:
                break
                
    if itsprime == True :
        #print ( i , "is prime ===================")
        Sum = Sum + i
        if i > 2000000:
            print( "the total some is:", Sum , "~~~~~~~~~~~~~~~~~~~~~")
            sys.exit()
