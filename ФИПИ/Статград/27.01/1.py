from itertools import permutations

t = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'
g = 'AB BA BC CB CE EC EG GE GD DG DF FD FA AF AC CA ED DE'

for p in permutations('ABCDEFG'):
    tc = t
    for i in range(1, len(p)+1):
        tc = tc.replace(str(i), p[i-1])
    if set(tc.split()) == set(g.split()):
        print(*range(1, len(p)+1))
        print(*p)

# 18
