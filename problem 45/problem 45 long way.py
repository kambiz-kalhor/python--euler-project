import time
startTime = time.time()
listp=[]
listh=[]
n=0
for i in range (1,100000):
    t = (i*((i+1))/2)
    p = ((i*((3*i)-1))/2)
    h = (i*((2*i)-1))
    listp.append(p)
    listh.append(h)
    if t in listp and t in listh:
        print (t)
        n=n+1
        if n ==3:
            break
        

    




print ("finish")


executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
