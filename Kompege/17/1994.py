nums = list(map(int, open('1994.txt')))
c = 0
m = 10e10
for a, b in zip(nums, nums[1:]):
    p = a * b
    s = a + b
    if p > 0 and s % 7 == 0:
        c += 1
        m = min(m, p)
print(c, m)
