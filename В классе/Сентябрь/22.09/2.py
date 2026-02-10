from itertools import *

def f(a,b,c,d):
    return ((a <= b) and (b <= (not c)) and ((not c) <= d))

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    t = [(1, a2, a3, a4), (1, a2, 1, a4), (1, a2, 1, 1)]

    if len(t) == len(set(t)):
        for p in permutations('abcd'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(''.join(p))

# dcba