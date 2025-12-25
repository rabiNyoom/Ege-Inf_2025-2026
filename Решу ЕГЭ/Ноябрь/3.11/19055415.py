from itertools import product, permutations
from ipaddress import *
from turtle import *
from functools import lru_cache
from sys import setrecursionlimit
from math import ceil

def t1():
    t = '15 16 18 23 26 32 34 37 43 46 48 51 57 58 61 62 64 73 75 81 84 85'
    g = 'АЖ ЖА ЖД ДЖ ДК КД ЕК КЕ ЕБ БЕ АБ БА БГ ГБ АГ ГА ГВ ВГ ЕВ ВЕ ВД ДВ'
    print(*range(1, 9))
    for p in permutations('АБВГДЖЕК'):
        tc = t
        for i in range(1, len(p)+1):
            tc = tc.replace(str(i), p[i-1])
        if set(tc.split()) == set(g.split()):
            print(*p)
def t2():
    def f(x,y,z,w):
        return (((not y) <= (z == w)) and ((z <= x) == w))
    for a1,a2,a3,a4 in product([0,1], repeat=4):
        t = [(1,1,0,1), (0,1,1,1), (0,a2,a3,0)]
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**dict(zip(p, r))) for r in t] == [1,1,1]:
                    print(''.join(p))
                    return
def t5():
    def algo(n):
        nb = f'{n:b}'
        for _ in range(3):
            ones, zeros = nb.count('1'), nb.count('0')
            if ones == zeros:
                nb += nb[-1]
            elif ones < zeros:
                nb += '1'
            else:
                nb += '0'
        return int(nb, 2)
    r = [i for i in range(100, 1000) if algo(i) % 4 == 0]
    print(min(r))
def t6():
    lt(90)
    screensize(3000,3000)
    tracer(0)
    k = 10
    for _ in range(4):
        fd(7*k);rt(90);fd(7*k);lt(90);fd(7*k);rt(90)
    pu()
    for x in range(-50,50):
        for y in range(-50, 50):
            goto(x*k,y*k)
            dot(2, 'red')
    done()
def t8():
    c = 0
    for p in product('АКРУ', repeat=5):
        c += 1
        if p[0] == 'К':
            print(c)
            return
def t9():
    c = 0
    for l in open('9.txt'):
        n = [int(i) for i in l.split()]
        rep3 = [i for i in n if n.count(i) == 3]
        rep1 = [i for i in n if n.count(i) == 1]
        
        if len(rep3) == 3 and len(rep1) == 3 and rep3[0] >= sum(rep1)/3:
            c += 1
    print(c)
def t11():
    letters = ceil(22*5/8)
    year = 7
    num = 9
    print(letters + ceil((year + num)/8))
def t12():
    def algo(s: str) -> str:
        while '00' not in s:
            s = s.replace('01', '210', 1)
            s = s.replace('02', '3101', 1)
            s = s.replace('03', '2012', 1)
        return s
    for o, t, th in product(range(1, 30+1), repeat=3):
        s0 = '0' + '1' * o + '2' * t + '3' * th + '0'
        s = algo(s0)
        if s.count('1') == 70 and s.count('2') == 56 and s.count('3') == 23:
            print(len(s0))
            return
def t14():
    m = float('inf')
    for x, y in product('0123456789ABC', repeat=2):
        n = int(f'8{x}78{y}', 13) + int(f'79{x}{y}7', 18)
        if n % 9 == 0 and n < m:
            m = n
    print(m//9)
def t16():
    def f(n) -> int:
        if n < 3:
            return 2
        if n > 2:
            if n % 2 == 0:
                return f(n-2)+f(n-1)-n
            return f(n-1)-f(n-2)+2*n
        return 0
    print(f(32))
def t23():
    def f(x,y):
        if x > y or x == 31:
            return 0
        if x == y:
            return 1
        return f(x+1,y)+f(x*2,y)
    print(f(2,15)*f(15,35))
t23()