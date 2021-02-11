def sys_base(num,base): 
    new_num = ''
    while num > 0: 
        new_num = str(num%base) + new_num
        num //= base
    return new_num

#Enter your example, enter your base
number =((16**5) + (8**6) + (4**9) -128)
base = 4
count_char = 3 
print(sys_base(number, base).count(str(count_char)))
