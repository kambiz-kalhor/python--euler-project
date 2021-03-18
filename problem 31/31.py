N=0
a=200
b=100
c=50
d=20
e=10
f=5
g=2
h=1

for A in range (0,2):
    if (A*a)>200:
        break
    for B in range (0,3):
        if ((A*a) + (B*b)) >200:
            break
        for C in range (0,41):
            if A*a + B*b + C*c >200:
                break
            for D in range (0,11):
                if A*a + B*b + C*c + D*d >200:
                    break
                for E in range (0,21):
                    if A*a + B*b + C*c + D*d + E*e >200:
                        break
                    for F in range (0,41):
                        if A*a + B*b + C*c + D*d + E*e + F*f >200:
                            break
                        for G in range (0,101):
                            if A*a + B*b + C*c + D*d + E*e + F*f + G*g >200:
                                break
                            for H in range (0,201):

                                if A*a + B*b + C*c + D*d + E*e + F*f + H*h == 200:
                                    N = N +1


print(N)



