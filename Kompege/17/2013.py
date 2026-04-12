nums = list(map(int, open('2013.txt')))
c = 0
m = 10001
for n in nums:
    if n % 10 in [2, 7] and n % 3 == 0 and n % 11 == 0:
        c += 1
        m = min(m, n)
print(c, m)
