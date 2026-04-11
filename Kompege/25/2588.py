def edels(n):
    d = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i % 2 == 0:
                d.add(i)
            ii = n // i
            if ii % 2 == 0:
                d.add(ii)
    return sorted(d)


for n in range(190201, 190261):
    d = edels(n)
    if len(d) == 4:
        print(d[3], d[2])
