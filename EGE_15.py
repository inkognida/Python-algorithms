#ДЕЛ
for A in range(1,100): 
    f = 0
    for x in range(1,100): 
        if ((120%A==0) and (x%A==0 or (x%18!=0 or x%24!=0))) == False: 
            f = 1
            break
    if f == 0: 
        print(A)
