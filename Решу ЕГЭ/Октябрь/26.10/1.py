from itertools import permutations

g = 'AC CA GC CG GB BG BD DB ED DE AE EA FE EF GF FG CF FC'
t = '16 17 23 25 26 32 34 37 43 45 52 54 56 61 62 65 71 73'
print(*range(1, 8))
for p in permutations('ABCDEFG'):
    tc = t
    for i in range(1, len(p)+1):
        tc = tc.replace(str(i), p[i-1])
    if set(g.split()) == set(tc.split()):
        print(*p)

# 105