#!/usr/bin/env python3

# 12 вариант Решу ЕГЭ - Январь
# https://inf-ege.sdamgia.ru/test?id=19512095

def n1():
    from itertools import permutations

    t = '15 18 23 25 32 35 36 45 47 51 52 53 54 56 57 58 63 65 74 75 78 81 85 87'
    g = 'AB BA AC CA AD DA AE EA AF FA AG GA AH HA BC CB CD DC EF FE FG GF GH HG'

    for p in permutations('ABCDEFGH'):
        tc = t
        for i in range(1, len(p)+1):
            tc = tc.replace(str(i), p[i-1])
        if set(tc.split()) == set(g.split()):
            print(*range(1, len(p)+1))
            print(*p)
            return


def n2():
    from itertools import permutations, product

    def f(x, y, z, w):
        return (((x <= y) and (z or w)) <= ((x == w) or (y and not z)))

    for a1, a2, a3, a4 in product([0, 1], repeat=4):
        t = [(0, 0, a3, 0), (1, a2, 1, 1), (0, a2, a3, a4)]
        if len(t) == len(set(t)):
            for p in permutations('xyzw'):
                if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
                    print(''.join(p))
                    return


def n5():
    def algo(n: int) -> int:
        nb = f'{n:b}'
        for _ in range(3):
            if sum(map(int, str(nb))) % 2 == 1:
                nb += '1'
            else:
                nb += '0'
        r = int(nb, 10)
        return r

    n = 0
    c = 0
    while True:
        r = algo(n)
        if 123_456_789 <= r <= 1_987_654_321:
            c += 1
        elif r > 4_000_000_000:
            break
        n += 1
    print(c)


def n6():
    import turtle as t
    t.lt(90)
    t.screensize(3000, 3000)
    t.tracer(0)
    k = 5

    for _ in range(4):
        t.fd(10*k)
        t.rt(90)
    t.up()
    for x in range(-50, 50):
        for y in range(-50, 50):
            t.goto(x*k, y*k)
            t.dot(2, 'red')
    t.update()
    t.done()


def n8():
    from itertools import product
    c = 0
    for p in product('АПРСУ', repeat=4):
        c += 1
        if p.count('А') == 0:
            print(c)
            return


def n9():
    c = 0
    for l in open('9.txt'):
        nums = sorted([int(n) for n in l.split()])

        fst = len(set(nums)) == len(nums)
        snd = 2 * (nums[0] + nums[4]) <= (nums[1] + nums[2] + nums[3])
        if fst and snd:
            c += 1
    print(c)


def n10():
    print(8 * 30)


def n12():
    def algo(s: str) -> str:
        while '72' in s or '522' in s or '2222' in s:
            s = s.replace('72', '2', 1)
            s = s.replace('522', '27', 1)
            s = s.replace('2222', '5', 1)
        return s

    for n in range(4, 10000):
        s = '5' + '2' * n
        if sum(map(int, algo(s))) == 63:
            print(n)
            break


def n14():
    def to_base7(n: int) -> str:
        ds = ""
        while n != 0:
            ds += str(n % 7)
            n //= 7
        return ds
    n = 49**7 + 7**21 - 7
    print(to_base7(n).count('6'))


def n16():
    from functools import lru_cache

    @lru_cache(None)
    def f(n):
        if n == 0:
            return 0
        return f(n // 10) + (n % 10)

    c = 0
    for n in range(765_432_015, 1_542_613_239 + 1):
        if f(n) > f(n+1):
            c += 1
    print(c)


if __name__ == '__main__':
    n16()
