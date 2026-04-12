nums = list(map(int, open('2400.txt')))
c = 0
m = float('-inf')
for a, b in zip(nums, nums[1:]):
    if a + b >= 100 and (a < 0 or b < 0):
        c += 1
        m = max(m, a*b)
print(c, m)
