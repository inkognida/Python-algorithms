def sys_base(num, base): 
    digits = '0123456789ABCDEF'
    remain = []
    while num > 0: 
        remainder = num % base
        remain.append(remainder)
        num //= base
    new_num = []
    while remain: 
        new_num.append(digits[remain.pop()])
    return ''.join(new_num)

def reverse_sys_base(num, base): 
    return int(str(num), base)

#1
with open('1_A.txt', 'r+') as f:
    s = f.read()
param = 'X'
symbol = 'X'
while param in s: 
    param += symbol
if param in s: 
    print(len(param))
else: 
    print((len(param) - 1), s.count(param[:-1])) #out: 23 

#2 
import itertools
with open('1_A.txt', 'r+') as f:
    s = f.read()
options = list(itertools.product(['X', 'Y', 'Z'], repeat = 3))
params = []
for par in options: 
    if par[0] != par[1] and par[1] != par[2] and par[0] != par[2]: 
        params.append(''.join(par))

def len_of_param(param): 
    symbol = param
    while param in s: 
        param += symbol 
    if param in s: 
        return len(param)
    else: 
        if s.count(param[:-3]):
            return len(param[:-3])
max_len = 0
for cond in params: 
    if len_of_param(cond) > max_len: 
        max_len = len_of_param(cond)
print(max_len) #out: 12
