for A in range(1,100): 
    f = 0
    for x in range(1,100): 
        if ((120%A==0) and (x%A==0 or (x%18!=0 or x%24!=0))) == False: 
            f = 1
            break
    if f == 0: 
        print(A)

def t_f(A):
    for x in range(1,1000):
        for y in range(1,1000): 
            func = ((5*y) + (7*x) != 129) or ((3*x) > A) or ((4*y) > A)
            if func == False:
                return 'suck'
    return ('fine', A)

for A in range(1,100): 
    if (t_f(A)) != 'suck':
        pass
