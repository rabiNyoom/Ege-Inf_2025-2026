def F(n):
    d = []
    i = 2
    while n > 1:
        if n % i == 0:
            d.append(i)
            n //= i
        else:
            i += 1
    if len(d) == 4:
        s = sum(d)
        ss = str(s)
        if ss == ss[::-1]:
            return s
    return 0


c = 0
n = 7305679
while c != 5:
    s = F(n)
    if s:
        print(n, s)
        c += 1
    n += 1
