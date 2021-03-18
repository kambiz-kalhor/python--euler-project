import time
start = time.time()



n=0
string = "0123456789"

for a in range (0,10):
    d_1 = string[a]
    string1 = string.replace(string[a] , "")
    
    for b in range (0,9):
        d_2 = string1[b]
        string2 = string1.replace(string1[b] , "")

        for c in range (0,8):
            d_3 = string2[c]
            string3 = string2.replace(string2[c] , "")
            
            for d in range (0,7):
                d_4 = string3[d]
                string4 = string3.replace(string3[d] , "")
                
                for e in range (0,6):
                    d_5 = string4[e]
                    string5 = string4.replace(string4[e] , "")
                    
                    for f in range (0,5):
                        d_6 = string5[f]
                        string6 = string5.replace(string5[f] , "")

                        for g in range (0,4):
                            d_7 = string6[g]
                            string7 = string6.replace(string6[g] , "")

                            for h in range (0,3):
                                d_8 = string7[h]
                                string8 = string7.replace(string7[h] , "")
                                
                                for i in range (0,2):
                                    d_9 = string8[i]
                                    string9 = string8.replace(string8[i] , "")

                                    for j in range (0,1):
                                        d_10 = string9[j]
                                        string10 = string9.replace(string9[j] , "")
                                        n=n+1
                                        
                                        if n == 1000000:
                                            print (n,"++++++++", d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8,d_9,d_10)








                                        string10=string9
                                    string9=string8
                                string8=string7
                            string7=string6
                        string6=string5
                    string5=string4
                string4=string3
            string3=string2
        string2 = string1
    string1 = string
exittime = time.time()
executiontime = exittime - start
print(executiontime)
