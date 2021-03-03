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
