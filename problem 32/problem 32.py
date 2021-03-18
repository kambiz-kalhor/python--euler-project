import math
from statistics import mode
SquareNumbers = []

for x in range (1, 500):
    SquareNumbers.append(x**2)



alltriples = []

for a_2 in SquareNumbers:
    for b_2 in SquareNumbers:
        c_2 = a_2 + b_2
        if c_2 in SquareNumbers:
            a = math.sqrt(a_2)
            b = math.sqrt(b_2)
            c = math.sqrt(c_2)
            p = a + b + c
            alltriples.append(p)


print (mode(alltriples))





                
                
