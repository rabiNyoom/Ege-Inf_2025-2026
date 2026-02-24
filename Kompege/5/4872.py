def algo(n, m):
    p1 = 1
    p2 = 1
    sn = str(n)
    sm = str(m)
    for d in sn + sm:
        if d in '2468':
            p1 *= int(d)
        elif d in '13579':
            p2 *= int(d)
    return abs(p1-p2)


for m in range(1, 1000):
    r = algo(120, m)
    if r == 29:
        print(m)
        break
