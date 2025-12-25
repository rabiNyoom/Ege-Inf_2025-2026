from itertools import permutations, product
from turtle import *
from collections import Counter
def t1():
    t = '12 14 21 24 26 35 36 41 42 46 47 53 56 62 63 64 65 67 74 76'
    g = 'АБ БА АВ ВА БВ ВБ ВД ДВ ЕД ДЕ ВЕ ЕВ ВГ ГВ ГЕ ЕГ ЕК КЕ ГК КГ'
    for p in permutations('АБВГДЕК'):
        tc = t
        for i in range(1, len(p)+1):
            tc = tc.replace(str(i), p[i-1])
        if set(g.split()) == set(tc.split()):
            print(p)
            return
def t2():
    def f(x,y,z,w):
        return (((y <= z) or (not x and w)) == (w == z))
    for a1,a2,a3,a4 in product([0,1], repeat=4):
        t = [(a1,1,0,0),(0,0,0,1),(0,1,a3,a4)]
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in t] == [1,1,1]:
                print(''.join(p))
                return
def t5():
    def algo(n: str) -> int:
        s: list[int] = [int(n[0]) + int(n[1]), int(n[1])+int(n[2]), int(n[2])+int(n[3])]
        s.sort()
        return s[1]*100 + s[2]
    for n in range(1000, 10000):
        if algo(str(n)) == 1418:
            print(n)
            return
def t6():
    screensize(3000,3000)
    tracer(0)
    k = 10
    for _ in range(4):
        fd(4 * 5**0.5 * k); rt(150); fd(4 * 5**0.5 * k); rt(300)
    up()
    for x in range(-50,50):
        for y in range(-50,50):
            goto(x*k,y*k)
            dot(2, 'red')
    update(); done()
def t8():
    c = 0
    for p in product('БОРИС', repeat=6):
        if p.count('Б') == 1 and p.count('Р') == 1 and p.count('С') <= 1:
            c += 1
    print(c)
def t9():
    c = 0
    for l in open('9.txt'):
        s = sorted([int(i) for i in l.split()])
        rep = [i for i in s if s.count(i) != 1]
        norep = [i for i in s if s.count(i) == 1]
        if len(set(s)) == 5 and sum(rep)/len(rep) < sum(norep)/len(norep):
            c += 1
    print(c)
def t12():
    s = '1' * 101
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    print(s)
def t14():
    def to6(n: int) -> str:
        s = ''
        while n != 0:
            s += str(n % 6)
            n //= 6
        return s
    n = 36**7 + 6**19 - 18
    print(to6(n).count('5'))
def t15():
    for a in range(1, 100):
        f = True
        for x in range(1, 150):
            for y in range(1, 150):
                if not((3*x + 4*y != 70) or (a > x) or (a > y)):
                    f = False
        if f:
            print(a)
            return
def t16():
    def f(x):
        if x == 1:
            return 1
        return f(x-1) * x
    print(f(5))
def t17():
    s = [int(i) for i in open('17.txt')]
    c = 0
    m = 0
    for i in range(1, len(s)):
        p = [s[i-1], s[i]]
        if p[0] % 3 == 0 or p[1] % 3 == 0:
            c += 1
            m = max(m, sum(p))
    print(c,m)
def t23():
    def f(x,y):
        if x > y or x == 33:
            return 0
        if x == y:
            return 1
        return f(x+1,y) + f(x*2,y) + f(x*3,y)
    print(f(3,15)*f(15,50))
def t24():
    s = ''
    l = open('24.txt').read().strip()
    for i in range(1, len(l)):
        if l[i-1] == 'A':
            s += l[i]
    s.replace('A', '')
    print(Counter(s).most_common()[0][0])
def t25():
    def divs(n: int) -> list[int]:
        s = set()
        for d in range(2, int(n**0.5)+1):
            if n % d == 0:
                s.add(d)
                s.add(n/d)
        return sorted(s)
    c = 0
    for n in range(452_022, 1000000000):
        d = divs(n)
        if len(d) > 0:
            m = min(d) + max(d)
        else:
            m = 0
        if m % 7 == 3:
            c += 1
            print(n,m)
            if c == 5:
                return
t25()
