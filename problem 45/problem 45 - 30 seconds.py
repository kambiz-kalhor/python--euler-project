import time
startTime = time.time()
listh=[]
n=0
for i in range (1,100000):
    p = ((i*((3*i)-1))/2)
    h = (i*((2*i)-1))
    listh.append(h)
    if p in listh:
        print (p)
        n=n+1
        if n ==3:
            break
        

    




print ("finish")


executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
