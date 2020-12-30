import math
import random
def first():
    number = int(input())
    if number == 1 or number == 2 or number == 3: 
        print(number)
    else:
        result = []
        result__ = []
        for num in range(1,number):
            fact_num = math.factorial(num)
            while fact_num <= number: 
                result.append(fact_num)
                break
            while fact_num >= number: 
                result__.append(fact_num)
                break    
            pass

        if number - result[-1] > abs(number - result__[0]): 
            print('Min close from higher:',result__[0])
        elif number - result[-1] == abs(number - result__[0]): 
            print('Min of two close:',result[-1])
        else:
            print('Min close:',result[-1])

def second():
    massive = random.sample(range(-100, 100), 10)
    massive = list(map(lambda i: abs(i), massive))
    replace_num = max(list(filter(lambda x: x % 2 == 0, massive)))
    print(replace_num)
    for index in range(len(massive)): 
        if massive[index] % 2 == 0: 
            massive[index] = replace_num
    print(massive)
def third():
    massive = random.sample(range(1,1500), 10)
    try: 
        min_minus_number = min(list(filter(lambda x: x % 3 == 0, massive)))
    except ValueError: 
        print(massive)
    for index in range(len(massive)): 
        if massive[index] % 2 == 0: 
            massive[index] = min_minus_number
    print(massive)

### КАМНИ ДЕТЯМ НЕ ИГРУШКА, А Я ЕЩЕ МАЛЕНЬКИЙ :) 
### С НАСТУПАЮЩИМ! ХОЧУ ПОЖЕЛАТЬ, ЧТОБЫ В НОВОМ ГОДУ КОРОЛЬ СТОЛБИКА СКИДЫВАЛ СВОИ ТАСКИ ВОВРЕМСЯ. НУ И ПОМЕНЬШЕ ГОВНОКОДА, ВРОДЕ МОЕГО :) 

#               #
#              ***
#             *****
#            *****~~
#             **~~~
#            *~~~***
#           ~~~******
#          ~~*********
#         *************
#          ***********
#         *************
#        ***************
#       *@***************
#      ***@************@**
#     *@****************@**
#       @****************
#      *******************
#     *****@***************
#    ***********************
#   ********@****************
#  *****************@*********
# *****************************
#             ******
#             ******
#             ******
