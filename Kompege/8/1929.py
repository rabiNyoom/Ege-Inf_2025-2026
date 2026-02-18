from itertools import permutations
c = 0
for p in permutations('ДЕЙКСТРА', 6):
    if 'Й' not in p:
        continue
    i = p.index('Й')
    if i == 5:
        continue
    if p[i+1] in 'ДЙКСТР':
        c += 1
print(c)
