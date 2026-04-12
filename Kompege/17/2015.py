nums = list(map(int, open('2015.txt')))
c = 0
mi = 10001
ma = 0
for n in nums:
    if n % 10 in [5, 7] and n % 9 != 0 and n % 11 != 0:
        c += 1
        mi = min(mi, n)
        ma = max(ma, n)
print(c, mi+ma)
