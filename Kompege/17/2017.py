nums = list(map(int, open('2017.txt')))
c = 0
s = 0
for n in nums:
    if hex(n).endswith('b') and n % 7 == 0 and n % 6 != 0 and n % 13 != 0 and n % 19 != 0:
        c += 1
        s += n
print(s, c)
