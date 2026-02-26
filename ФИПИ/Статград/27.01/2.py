from itertools import permutations, product


def f(x, y, z, w):
    return (not w or ((z <= x) <= y))


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    t = [(a1, 0, a3, a4), (0, 1, a3, 0), (a1, a2, a3, 1)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                print(''.join(p))

# yxwz
