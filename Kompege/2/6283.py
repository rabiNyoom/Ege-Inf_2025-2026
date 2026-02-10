from itertools import permutations, product

def f(x,y,z,w):
    return ((not((not (x <= (not w))) and z)) and (not(w <= z)) and (x <= (not z)))

a = set()
for a1,a2,a3,a4 in product([0,1], repeat=4):
    t = [(a1,0,a3,0),(1,a2,a3,a4),(1,1,0,0)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**(dict(zip(p, r)))) for r in t] == [1,0,0]:
                a.add(p)
print(len(a))

# 8