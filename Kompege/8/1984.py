from itertools import permutations
c = 0
for p in permutations('ИГРОК'):
    s = ''.join(p)
    if s[0] != 'К' and 'РОК' not in s:
        c += 1
print(c)
