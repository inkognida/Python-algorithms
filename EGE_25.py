# (№ 2603) Рассматриваются целые числа, принадлежащих числовому отрезку [523456;
# 578925], которые представляют собой произведение двух различных простых делителей.
# Найдите такое из этих чисел, у которого два простых делителя меньше всего отличаются
# друг от друга. В ответе запишите простые делители этого числа в порядке возрастания.
# Если подходящих чисел несколько, запишите в ответе делители наименьшего из них.


nums = [int(i) for i in range(523456,578926)]
def is_prime(num): 
    return(sympy.isprime(num))
primes = list()
for num in range(1,20000):
    if sympy.isprime(num): 
        primes.append(num)
def prod(num):
    divs = list()
    flag = range(523456,578926)
    for n in primes:
        if ((n*num) in flag) and (num != n):
            divs.append((abs(n-num),num,n))
    return divs
delta = list()
for num in primes: 
    if prod(num) != []:
        delta.append(sorted(prod(num)))
sorted(delta)
