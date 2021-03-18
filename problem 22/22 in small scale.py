names=[ "JACQUILINE","HILDE","FE","FAE","EVAN","EUGENE","ELOIS","ECHO","DEVORAH","CHAU","BRINDA"]
names=sorted(names)

SUMSUM = 0



for n in range (0, len(names)):
    
    
    stringname = str(names[n])
    
    Sum = 0
    for i in stringname:
        
        if i == "A":
            i=1
        if i == "B":
            i=2
        if i == "C":
            i=3
        if i == "D":
            i=4
        if i == "E":
            i=5
        if i == "F":
            i=6
        if i == "G":
            i=7
        if i == "H":
            i=8
        if i == "I":
            i=9
        if i == "J":
            i=10
        if i == "K":
            i=11
        if i == "L":
            i=12
        if i == "M":
            i=13
        if i == "N":
            i=14
        if i == "O":
            i=15
        if i == "P":
            i=16
        if i == "Q":
            i=17
        if i == "R":
            i=18
        if i == "S":
            i=19
        if i == "T":
            i=20
        if i == "U":
            i=21
        if i == "V":
            i=22
        if i == "W":
            i=23
        if i == "X":
            i=24
        if i == "Y":
            i=25
        if i == "Z":
            i=26
       
        Sum = Sum + i
    
    
    SUMSUM = SUMSUM +(Sum * (n+1))
print (SUMSUM)
