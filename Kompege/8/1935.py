from itertools import permutations
c = 0
for p in permutations('ВАЙФУ', 4):
    s = ''.join(p)
    if p[0] != 'Й' and 'ВФ' not in s and 'ФВ' not in s:
        c += 1
print(c)
