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
    for i in range(len(nums)):
        low = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[low]:
                low = j
        nums[i], nums[low] = nums[low], nums[i]
    print(nums, list(reversed(nums)), sep = '\n')

def squares(f): 
    print(f'Without range(20,26): {list(filter(lambda i: i != 24 and i != 22 and i != 21 and i != 23 and i != 25 and i != 20,f))}')
    print(f'Squares: {list(map(lambda x: x*x, f))}')
    
squares(f)
choose_sort(f)
f = [random.randrange(0,100) for i in range(500)] 
