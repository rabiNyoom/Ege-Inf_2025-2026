from itertools import *

def f(x, y, z, w):
    return ((not x and not y) or (y == z ) or w)

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    t = [(a1, a2, 1, a4), (1, 0, a3, 1), (0, 0, 1, 1)]

    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(''.join(p))

# zwyx