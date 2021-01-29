with open('27-school.txt', 'r+') as f: 
    pairs = [list(map(int, line.split())) for line in f][1:]
    diff = [abs(i[0] - i[1]) for i in pairs if (i[0] - i[1]) != 0 and (i[0]- i[1]) % 5 != 0]
    local_sum = sum([max(i) for i in pairs])
if local_sum % 5 == 0: 
    local_sum -= min(diff)
    print(local_sum)
else: 
    print(local_sum) #118951/394491666
    
    
with open('FileB_10.txt', 'r+') as f:
    nums = list(map(int, f.readlines()))

import itertools
delta = [(a, b) for idx, a in enumerate(nums) for b in nums[idx + 1:]]
result = list()
for pairs in delta: 
    if abs(pairs[0] - pairs[1]) % 2 == 0 and (pairs[0] % 11 == 0 or pairs[1] % 11 == 0):
        result.append((sum(pairs), pairs))
sorted(result, key = lambda x: x[0], reverse = True)



with open('FileB_10.txt', 'r+') as f:
    nums = list(map(int, f.readlines()))[1:]
nums
def pairs(num): 
    a = num
    for i in range(1, len(nums)):
        if abs(a - nums[i]) % 2 == 0 and (nums[i] % 11 == 0 or a % 11 == 0): 
            return((nums[i], a))
delta = list()
for num in nums: 
    if pairs(num) != None:
        delta.append(pairs(num))
res = list()
for pairs in delta: res.append([sum(pairs), pairs])
sorted_list = sorted(res, key=lambda x: x[0], reverse = True)
sorted_list
