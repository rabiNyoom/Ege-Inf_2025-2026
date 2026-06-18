def check(n):
    st = 1
    while n > (five := 5**st):
        n2 = n - five
        if n2 % 2 == 0 and n2 % 197 == 0:
            return st
        st += 1
    return 0


c = 0
for n in range(200000, 1000000):
    if "1" in str(n):
        continue
    r = check(n)
    if r:
        print(n, r)
        c += 1
        if c == 7:
            break
