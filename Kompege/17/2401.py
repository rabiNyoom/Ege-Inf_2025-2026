nums = list(map(int, open('2401.txt')))
c = 0
m = 10e10
for a, b in zip(nums, nums[1:]):
    if 50 <= abs(a) + abs(b) <= 200:
        c += 1
        m = min(m, min(a, b))
print(c, m)
