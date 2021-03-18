List=[0,5616185650518293,1,3847439647293047  ,3,5855462940810587 ,3,9742855507068353 ,3,4296849643607543 ,1,3174248439465858 ,2,4513559094146117,3,7890971548908067 ,1,8157356344118483 ,2,2615250744386899 ,3,8690095851526254,1,6375711915077050 ,1,6913859173121360 ,2,6442889055042768 ,0,2321386104303845 ,2,2326509471271448 ,2,5251583379644322,3,1748270476758276  ,1,4895722652190306 ,3,3041631117224635,3,1841236454324589,2,2659862637316867]
print(len(List))



for place in range (0,16):
    A=0
    B=0
    C=0
    D=0
    E=0
    F=0
    G=0
    H=0
    I=0
    J=0
    possiblenumber =[]

    for number in List:
        
        if number <100:
            
            
            n= number
            #print(n,"____________________")
            possiblenumber.append(n)
            if n == 0:
                #print(n,"____________________")
                A=0
                B=0
                C=0
                D=0
                E=0
                F=0
                G=0
                H=0
                I=0
                J=0
            
        if number>100:
            #print(number,"~~~~~~~~~~~~~~~~")
            number = str(number)
            possiblenumber.append(number[place])
           
            if int(number[place]) == 9:
                a=9
                A=A+n
            if int(number[place]) == 8:
                b=8
                B=B+n
            if int(number[place]) == 7:
                c=7
                C=C+n
            if int(number[place]) == 6:
                d=6
                D=D+n
            if int(number[place]) == 5:
                e=5
                E=n+E
            if int(number[place]) == 4:
                f=4
                F=n+F
            if int(number[place]) == 3:
                g=3
                G=n+G
            if int(number[place]) == 2:
                h=2
                H=n+H
            if int(number[place]) == 1:
                i=1
                I=n+I
            if int(number[place]) == 0:
                j=0
                J=n+J

    bestscore=[A,B,C,D,E,F,G,H,I,J]
    print(bestscore)
    bestscore=sorted(bestscore)
    print(bestscore)
    

    if 100>20:
        
        if A>=bestscore[-1]:
            print(A , ": is the score for 10th")
        if B>=bestscore[-1]:
            print(B , ": is the score for 9th")
        if C>=bestscore[-1]:
            print(C , ": is the score for 8th")
        if D>=bestscore[-1]:
            print(D , ": is the score for 7th")
        if E>=bestscore[-1]:
            print(E , ": is the score for 6th")
        if F>=bestscore[-1]:
            print(F , ": is the score for 5th")
        if G>=bestscore[-1]:
            print(G , ": is the score for 4th")
        if H>=bestscore[-1]:
            print(H , ": is the score for 3th")
        if I>=bestscore[-1]:
            print(I , ": is the score for second number")
        if J>=bestscore[-1]:
            print(J , ": is the score for first number")





