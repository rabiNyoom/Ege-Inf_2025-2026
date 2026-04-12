nums = list(map(int, open('2003.txt')))
c = m = 0
for n in nums:
    if n % 3 == 0 and all(map(lambda x: n % x != 0, [7,17,19,27])):
        c += 1
        m = max(m, n)
print(c, m)