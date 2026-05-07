from itertools import permutations
t = '14 17 24 25 28 36 37 41 42 45 52 54 56 63 65 71 73 78 82 87'
g = 'AH HA AB BA BG GB GE EG EF FE FH HF BC CB GC CG CD DC DF FD'

for p in permutations('ABCDEFGH'):
    tc = t
    for i in range(1, len(p)+1):
        tc = tc.replace(str(i), p[i-1])
    if set(tc.split()) == set(g.split()):
        print(*range(1, len(p)+1))
        print(*p)
