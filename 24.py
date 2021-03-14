# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле сразу после буквы A.
# Например, в тексте ABCAABADDD после буквы A два раза стоит B, по одному разу — A и D. Для этого текста ответом будет B.

# import itertools
# with open('24.txt', 'r+') as f: 
#     s = f.read()
# chars = [chr(i) for i in range(65,91)]
# params = list()
# for ch in list(itertools.product(chars, repeat = 2)):
#     if ch[0] == 'A':
#         params.append(''.join(ch))
# result = list()
# for par in params: 
#     result.append((s.count(par), par))
# sorted(result, reverse = True)
#G
