nums = [int(l) for l in open('17.txt')]
maxi = max(nums)
c = m = 0

for a, b in zip(nums, nums[1:]):
    if a + b != maxi:
        continue
    c += 1
    m = max(m, a*a + b*b)
print(c, m)

# 2 9997800125
