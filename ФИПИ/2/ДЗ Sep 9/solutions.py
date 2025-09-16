from itertools import product, permutations

# C8147F
def f1():
    def f(x, y, z, w):
        return (not (y <= z) or (x <= w) or not x)
    
    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(a1, 0, a3, 0), (a1, a2, 1, a4), (a1, 1, 0, a4)]
        
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**(dict(zip(p, r)))) for r in t] == [0, 0, 0]:
                    return ''.join(p)

# 6E287D
def f2():
    def f(x, y, z, w):
        return (x and not y and (not z or w))
    
    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(1, 0, 0, 0), (1, 0, 1, 0), (1, 0, 1, 1)]
        
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**(dict(zip(p, r)))) for r in t] == [1, 1, 1]:
                    return ''.join(p)

# 3CF37C
def f3():
    def f(x, y, z, w):
        return (not (y <= w) or (x <= z) or not x)
    
    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(a1, a2, 0, 0), (a1, 1, a3, a4), (a1, 0, 1, a4)]
        
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**(dict(zip(p, r)))) for r in t] == [0, 0, 0]:
                    return ''.join(p)

# 804673
def f4():
    def f(x, y, z, w):
        return (not (x <= z) or (y == w) or y)
    
    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(1, 0, a3, a4), (a1, 1, 0, a4), (0, a2, a3, a4)]
        
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**(dict(zip(p, r)))) for r in t] == [0, 0, 0]:
                    return ''.join(p)

# 42A6BC
def f5():
    def f(x, y, z, w):
        return ((not x or not y) and not (y == z) and w)
    
    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(a1, 0, 0, 1), (0, a2, 0, a4), (1, 0, a3, 1)]
        
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**(dict(zip(p, r)))) for r in t] == [1, 1, 1]:
                    return ''.join(p)

# 75A1B7
def f6():
    def f(x, y, z, w):
        return ((x and not y) or (x == z) or w)
    
    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(1, a2, 0, 0), (1, 1, a3, 0), (a1, 1, 1, a4)]
        
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**(dict(zip(p, r)))) for r in t] == [0, 0, 0]:
                    return ''.join(p)

# 7848B2
def f7():
    def f(x, y, z, w):
        return (not x or y or (not z and w))
    
    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 1, 1)]
        
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**(dict(zip(p, r)))) for r in t] == [0, 0, 0]:
                    return ''.join(p)

# 72DFBC
def f8():
    def f(x, y, z, w):
        return ((not x or not y) and not (y == z) and not w)
    
    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(a1, 0, 0, 1), (1, a2, 0, a4), (0, 1, a3, 1)]
        
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**(dict(zip(p, r)))) for r in t] == [1, 1, 1]:
                    return ''.join(p)

# B58EBB
def f9():
    def f(x, y, z, w):
        return (not (x <= z) or (y <= w) or not y)
    
    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(1, 0, a3, a4), (a1, 1, 0, a4), (0, a2, a3, a4)]
        
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**(dict(zip(p, r)))) for r in t] == [0, 0, 0]:
                    return ''.join(p)

# 5D6819
def f10():
    def f(x, y, z, w):
        return ((x or not y) and not (y == z) and not w)
    
    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(1, 0, a3, 0), (1, a2, 1, 0), (a1, 1, 1, a4)]
        
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**(dict(zip(p, r)))) for r in t] == [1, 1, 1]:
                    return ''.join(p)

SLNS = {
    'C8147F': f1(),
    '6E287D': f2(),
    '3CF37C': f3(),
    '804673': f4(),
    '42A6BC': f5(),
    '75A1B7': f6(),
    '7848B2': f7(),
    '72DFBC': f8(),
    'B58EBB': f9(),
    '5D6819': f10(),
}

for _, (k, v) in enumerate(SLNS.items(), 1):
    print(f'{(str(_)):>2}. {k}: {v}')