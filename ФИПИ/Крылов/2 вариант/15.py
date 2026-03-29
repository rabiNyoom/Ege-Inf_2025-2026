def dels(n):
    a = set()
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            a.add(d)
            a.add(n//d)
    return a


A = list(range(7, 27))
B = dels(77)


def check_y(y):
    C = dels(y)
    if len(C) == 0:
        return False
    for x in range(1, 1000):
        if not ((x in C) <= ((x in A) and (x not in B))):
            return False
    return True


for y in range(1, 1000):
    if check_y(y):
        print(y)
        break
