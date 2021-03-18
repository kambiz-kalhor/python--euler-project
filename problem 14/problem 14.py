n=1

for i in range (1,1000000):
    
    k=i
    if i==1:
        m=1
    n=1
    while i > 1:

        if ((i%2)!=0):
            i =(3*i)+1
            n=n+1
            
        if ((i%2)==0):
            i=i/2
            n=n+1
            
    if n>m:
        m=n
        kk=k


print ( m , "is the highest chain ~~~~~~~~~~~~~~~~~~~~~~~")
print ( kk , "is the number ~~~~~~~~~~~~~~~~~~~~~~~")
            
        

    
