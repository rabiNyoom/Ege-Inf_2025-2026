nums = list(map(int, open('2016.txt')))
c = 0
mi = 10001
ma = 0
for n in nums:
    if n % 13 == 7 and n % 7 != 0 and n % 11 != 0:
        c += 1
        mi = min(mi, n)
        ma = max(ma, n)
print(ma-mi, c)
