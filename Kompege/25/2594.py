def even_divs(n):
    s = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            s.append(d)
            if d * d != n:
                s.append(n // d)
    e = sorted(list(filter(lambda x: x % 2 == 0, s)))
    if len(e) == 3:
        return e[1]
    return None


for n in range(113_000_000, 114_000_001):
    delit = even_divs(n)
    if delit is None:
        continue
    print(n, delit)
