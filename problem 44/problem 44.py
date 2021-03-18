

mainlist = []

for i in range (1,100000):
    p = ((i*((3*i)-1))/2)
    mainlist.append (p)
    
    for n in mainlist:
        for m in mainlist:
            
            if (p == m+n and ((m-n) in mainlist)):
                print(m , n )
                break
        






print("finish")
