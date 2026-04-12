nums = list(map(int, open('1993.txt')))
c = 0
m = 0
for a, b in zip(nums, nums[1:]):
    s = a + b
    if s % 3 == 0 and s % 6 != 0 and abs(a * b) % 10 == 8:
        c += 1
        m = max(m, s)
print(c, m)
