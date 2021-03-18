      
import sys
tn=0
##tn = triangle number
for i in range (1,99999999999):
    n=0
    tn=tn+i
    for counter in range (1,(int(tn)+1)):
        
        if tn%counter == 0:
            n=n+1
            if n ==500:
                print (tn)
                sys.exit()
 


