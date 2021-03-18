a=1
b=1
n=2
digits = 1000

for counter in range (1,(10**9999)):
    c = a+b
    a=b
    b=c
    n = n+1
    if c >((10**(digits - 1))):
        print (n)
        break
