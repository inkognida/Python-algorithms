#23 

def first_type():
    #Прибавить 2
    #Прибавить 1
    #Умножить на 3
    #Из 1 в 40
    delta = [0]*500
    delta[1] = 1

    for i in range(2,141): 
        delta[i] = delta[i-2] + delta[i-1]
        if i % 3 == 0: 
            delta[i] += delta[i//3]
    print(delta[40])
    return

def second_type():
    #Прибавить 2
    #Прибавить 1
    #Умножить на 3
    #Из 1 в 40, но не проходящих через 18
    delta = [0]*500
    delta[1] = 1
    for i in range(2,141): 
        delta[i] = delta[i-2] + delta[i-1]
        if i % 3 == 0: 
            delta[i] += delta[i//3]
        if i == 18:
            delta[i] = 0
    print(delta[40])
    return

def third_type():
    #Прибавить 2
    #Прибавить 1
    #Умножить на 3
    #Из 1 в 40, проходящих через 18
    delta = [0]*500
    delta[1] = 1
    for i in range(2,300):
        delta[i] = delta[i-1] + delta[i-2]
        if i % 3 == 0: 
            delta[i] += delta[i//3]
        if i == 18: 
            for j in range(18): 
                delta[j] = 0
    print(delta[40])
    return
#Прибавить 2
#Прибавить 1
#Умножить на 3
#Из 1 в 40, проходящих через 18
delta = [0]*500
delta[1] = 1
for i in range(2,300):
    delta[i] = delta[i-1] + delta[i-2]
    if i % 3 == 0: 
        delta[i] += delta[i//3]
    if i == 18: 
        for j in range(18): 
            delta[j] = 0
print(delta[40])
