
finalrow = [1]
newmembers = [1]
totalrows = 10
for counter in range (1,totalrows +1):
    for i in range (0,len(finalrow)-1):
        newmembers.append(finalrow[i] + finalrow[i+1])
        
    newmembers.append(1)
    print (newmembers)
    finalrow = newmembers
    newmembers = [1]
