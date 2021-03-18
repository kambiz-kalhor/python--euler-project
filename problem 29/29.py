List=[]
for a in range (2,101):
    for b in range (2,101):
        iinput = a**b
        if iinput not in List:
            List.append(a**b)
List.sort()
print(len(List))
