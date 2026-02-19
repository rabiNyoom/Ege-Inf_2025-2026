def check_n(n):
    p = 0
    while True:
        p += 1
        power = 3**p
        if power > n:
            return None
        r = n - power
        if r % 2 == 1 and r % 103 == 0:
            return p


c = 0
for n in range(100000, 1000000):
    if '1' in str(n):
        continue
    r = check_n(n)
    if r is not None:
        print(n, r)
        c += 1
        if c == 5:
            break

'''
200004 4
200034 6
200036 9
200050 7
200056 10
'''
