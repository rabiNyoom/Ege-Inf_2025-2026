from itertools import product, permutations


def f(x, y, z, w):
    return (x <= (not ((y <= z) and (z == (not w)))))


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    t = [(0, a2, a3, 0), (a1, 1, 1, a4), (a1, 1, 0, 0)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(''.join(p))

# wxzy
# ???
