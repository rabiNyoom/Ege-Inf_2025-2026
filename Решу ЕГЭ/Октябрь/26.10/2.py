from itertools import permutations, product

def f(x,y,z,w):
    return ((not x and z and not y and not w) or (not x and z and y and not w) or (not x and z and y and w))
for a1,a2,a3,a4 in product([0,1], repeat=4):
    t = [(a1, 1, 0, a4),(0, 0, a3, a4), (a1, a2, 1, a4)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1,1,1]:
                print(''.join(p))

# xyzw