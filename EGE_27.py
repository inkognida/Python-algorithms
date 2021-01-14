with open('27-school.txt', 'r+') as f: 
    pairs = [list(map(int, line.split())) for line in f][1:]
    diff = [abs(i[0] - i[1]) for i in pairs if (i[0] - i[1]) != 0 and (i[0]- i[1]) % 5 != 0]
    local_sum = sum([max(i) for i in pairs])
if local_sum % 3 == 0: 
    local_sum -= min(diff)
    print(local_sum)
else: 
    print(local_sum)
