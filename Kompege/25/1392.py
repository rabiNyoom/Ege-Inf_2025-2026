def F(n):
    d = set()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) == 0:
        return 0
    return sum(d) // len(d)


n = 550001
c = 0
while c != 5:
    f = F(n)
    if f % 31 == 13:
        print(n, f)
        c += 1
    n += 1
