from itertools import permutations

t = '12 13 21 24 25 31 36 42 47 52 56 57 63 65 67 74 75 76'
g = 'AF FA CF FC CG GC GE EG AE EA DE ED DB BD FB BF DA AD'

for p in permutations('ABCDEFG'):
    tc = t
    for i in range(1, len(p)+1):
        tc = tc.replace(str(i), p[i-1])
    if set(g.split()) == set(tc.split()):
        print(*range(1, len(p)+1))
        print(*p)
        