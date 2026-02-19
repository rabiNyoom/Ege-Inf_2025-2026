from itertools import product
m = 0
for i, p in enumerate(product('АЕЛРСТ', repeat=5), 1):
    s = ''.join(p)
    if i % 2 == 0 and s[0] not in 'АСТ' and s.count('Л') == 2 and 'ЛЛ' not in s:
        m = i
print(m)

# 4518
