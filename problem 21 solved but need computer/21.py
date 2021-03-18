def SumOfProperDivisors (i):
    
    Sum = 0
    for n in range (1,(i//2)+1):
        if i%n == 0:
            #print (n)
            Sum = Sum + n
    return (Sum)


sumofall=0
for ameciblenumber1 in range (200,10000):
    for ameciblenumber2 in range (200,10000):
        if (SumOfProperDivisors (ameciblenumber1) == ameciblenumber2) and (SumOfProperDivisors (ameciblenumber2) == ameciblenumber1) and ameciblenumber1!=ameciblenumber2:
            
            sumofall= sumofall + ameciblenumber1
            print (ameciblenumber1 , ameciblenumber2)
            #print(SumOfProperDivisors (ameciblenumber1) ,SumOfProperDivisors (ameciblenumber2) )
print (sumofall)

