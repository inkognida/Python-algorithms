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
with open('24_demo.txt', 'r+') as f:
    s = f.read()
local_max = 1
count = 1
for ch in range(1, len(s)): 
    if s[ch] != s[ch - 1]: 
        count += 1 
    else: 
        if count > local_max: 
            local_max = count
        count = 1
local_max #out: 35
