from itertools import permutations, product


def f(x, y, z, w):
    return (x and (y <= z) and ((not y) <= ((not z) == w)))


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    t = [(a1, a2, 0, 0), (a3, 0, 0, a4), (1, a5, 1, 1)]
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in t] == [1, 1, 0]:
            print(''.join(p))
            break

# xzyw
