def prime(): 
    res = []
    for i in range(int(input('Enter the start number: ')), int(input('Enter the last number: '))): 
        for j in range(2,i): 
            if i % j == 0 :
                break
        else: res.append(i)
    print(list(filter(lambda i: i > 0 and i != 1, res)))     
prime()

def fibb(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fibb(10)))

def square(): 
    print('Square =',int(input('wide: ')) * int(input('lenght: ')))
square() 
'''OUTPUT:  wide: 10
            lenght: 10
            Square = 100'''
pass


def first():
    f = input('Enter your message here: ')
    if '@' in f:
        if '.ru' in f:
            print(f) #OUTPUT test@.ru else: nothing
        
        
def second(): 
    import functools, string, operator
    print('Lenght of the string:',len('На дворе - трава, на траве - дрова, не руби дрова на траве двора!'))
    print('String with .replace ' + 'На дворе - трава, на траве - дрова, не руби дрова на траве двора!'.replace('дрова', 'trash'))
    f = string.punctuation
    text = 'На дворе - трава, на траве - дрова, не руби дрова на траве двора!'
    print('Punctuation symbols:',len(list(filter(functools.partial(operator.contains, f), text))))
second() 
''' #OUTPUT:   Lenght of the string: 65
    String with .replaceНа дворе - трава, на траве - trash, не руби trash на траве двора!
    Punctuation symbols: 5'''
pass

import random
def lists():
    f = [random.randrange(0,1000) for i in range(100)]
    print(f'Random {list(filter(lambda i: i % 2 == 0, f))}', f'Min: {min(f)}', f'Max: {max(f)}', f'Sorted: {sorted(f)}', sep = '\n')
lists()

import random
def choose_sort(f):  
    for i in range(len(f)):
        low = i
        for j in range(i + 1, len(f)):
            if f[j] < f[low]:
                low = j
        f[i], f[low] = f[low], f[i]
    print(f, list(reversed(f)), sep = '\n')

def squares(f, start, end): 
    print(f'Without range(20,25): {list(filter(lambda i: i < start or i > end,f))}')
    print(f'Squares: {list(map(lambda x: x*x, f))}')
    
squares(f, int(input('start range number: ')), (int(input('end range number: '))))
choose_sort(f)
f = [random.randrange(0,100) for i in range(500)] 

import numpy as np 
def equation():
    rates = [float(input('Enter first: ')), float(input('Enter second: ')), float(input('Enter third: '))]
    print(np.roots(rates))
equation()

def encode():
    f = {'A':0, 'B': 1101, 'C' :101, 'D':1100, 'E': 100, 'F' : 111}
    res = list(input('Stroke: '))
    fin = []
    for char in res: 
        fin.append(f[char])
    print(''.join([str(elem) for elem in fin]))
def decode():
    f = {'A':0, 'B': 1101, 'C' :101, 'D':1100, 'E': 100, 'F' : 111}
    f_1 = dict([(value, key) for key, value in f.items()])
    beg = list(map(int, input('Enter your number using split: ').strip().split()))
    fin_1 = []
    for num in beg:
        fin_1.append(f_1[num])
    print(''.join(fin_1))
decode()


import collections 
import random
def first(a,b):
    print(list(set(a).intersection(b)))
def second(a):
    a_result = dict(collections.Counter(a))
    result = {key:value for key,value in a_result.items() if value > 1}
    for key,value in result.items():
        print('Element',key,'Reapeted',value,'times')

def third(a):
    result = collections.Counter(a)
    result_1 = list(filter(lambda i: i != 20, a))
    print(result[20], result_1, sep = '\n')

a = [random.randrange(0,50) for i in range(1000)]
b = [random.randrange(0,100) for i in range(100)]


class Triangle():
    #spizdil polychaetsa, v syti razberys' chutok pozhe :) 
    def printPascal(n) : 
        for line in range(0, n) : 
            for i in range(0, line + 1) : 
                print(binomialCoeff(line, i), 
                    " ", end = "") 
            print() 
    def binomialCoeff(n, k) : 
        res = 1
        if (k > n - k) : 
            k = n - k 
        for i in range(0 , k) : 
            res = res * (n - i) 
            res = res // (i + 1)   
        return res 

Triangle.printPascal(10)
  
