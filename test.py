def prime(): 
    res = []
    for i in range(int(input('Enter the start number: ')), int(input('Enter the last number: '))): 
        for j in range(2,i): 
            if i % j == 0 :
                break
        else: res.append(i)
    print(list(filter(lambda i: i > 0 and i != 1, res)))
              
prime()
