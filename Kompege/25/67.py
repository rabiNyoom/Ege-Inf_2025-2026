def divs(n):
    s = []
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            s.append(d)
            if d * d != n:
                s.append(n // d)
            if len(s) > 3:
                return None
    return sorted(s)


for n in range(81234, 134870):
    delit = divs(n)
    if delit is None:
        continue
    if len(delit) == 3:
        print(*delit)
