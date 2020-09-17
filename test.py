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
