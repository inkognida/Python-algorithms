import itertools
with open('24.txt', 'r+') as f: # open some file
    s = f.read()
chars = [chr(i) for i in range(65,91)]
params = list()
for ch in list(itertools.product(chars, repeat = 2)):
    if ch[0] == 'A':
        params.append(''.join(ch))
result = list()
for par in params: 
    result.append((s.count(par), par))
print(sorted(result, reverse = True))
