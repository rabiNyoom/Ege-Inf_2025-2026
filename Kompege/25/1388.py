def S(n):
    d = set()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) == 0:
        return 0
    return sum(d)


n = 150001
c = 0
while c != 7:
    s = S(n)
    if s % 13 == 10:
        print(n, s)
        c += 1
    n += 1
