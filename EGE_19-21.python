def game_theory(max_sum, first_heap, first_operation, second_operation, max_value):
    def winpos(a,b):
        if (a+b < max_sum) and ((a+first_operation+b >= max_sum) or (a+b+first_operation >= max_sum) \
                                or (second_operation*a+b >= max_sum) or (a+second_operation*b >= max_sum)):
            return True
        else:
            return False
    def losspos(a,b):
        if not winpos(a,b) and (winpos(a+first_operation,b) and winpos(a,b+first_operation) and \
                                winpos(second_operation*a,b) and winpos(a,second_operation*b)):
            return True
        else:
            return False
    def preloospos(a,b):
        if not winpos(a,b) and (losspos(a+first_operation,b) or losspos(a,b+first_operation) \
                                or losspos(second_operation*a,b) or losspos(a,second_operation*b)):
            return True
        else:
            return False
    x=first_heap #Камней в данной куче
    delta = list()
    """19"""
    for i in range(1,max_value):
        if winpos(x+first_operation,i) or winpos(x,i+first_operation) or \
            winpos(second_operation*x,i) or winpos(x,second_operation*i):
            print("19:",i)
            delta.append(('19', i))
            break
    "20"
    for i in range(1,max_value):
        if losspos(x+first_operation,i) or losspos(x,i+first_operation) or losspos(second_operation*x,i) or \
            losspos(x,second_operation*i):
            print("20:",i)
            delta.append(('20', i))
    "21"
    for i in range(1,max_value):
        if (winpos(x+first_operation,i) or preloospos(x+first_operation,i)) and \
        (winpos(x,i+first_operation) or preloospos(x,i+first_operation)) and \
        (winpos(x*second_operation,i) or preloospos(x*second_operation,i)) and \
        (winpos(x,second_operation*i) or preloospos(x,second_operation*i)):
            print("21:", i)
            delta.append(('21', i))
    return delta
print(game_theory(77,7,1,2,69)) #https://inf-ege.sdamgia.ru/problem?id=27416   EXAMPLE
