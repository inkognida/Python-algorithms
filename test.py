import itertools
chars = ['А', 'Н', 'Д', 'Р', 'Е', 'Й']
params = list(itertools.product(chars, repeat = 6))
count = 0 
for par in params:
    if (''.join(par).count('А') >= 1) and (''.join(par).count('Й') <= 1):
        count += 1
print(count) #24135
