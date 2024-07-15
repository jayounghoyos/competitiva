n = list(map(int,input()))
counterCero = 0
counterOne = 0
entre = False

for i in n:
    if i == 0:
        counterOne = 0
        counterCero += 1
        if counterCero >= 7:
            entre = True
            print("YES")
            break  
        
    if i == 1:
        counterCero = 0
        counterOne += 1
        if counterOne >= 7:
            entre = True
            print("YES")
            break

if not entre:
    print("NO")