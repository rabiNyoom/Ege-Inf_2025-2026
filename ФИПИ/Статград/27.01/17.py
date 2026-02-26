nums = list(map(int, open('17.txt')))
c = m = 0

maxi = max([n for n in nums if str(n).endswith('70')])
for i in range(2, len(nums)):
    ns = nums[i-2:i+1]
    if any(map(lambda x: x < 0, ns)):
        continue
    if sum(ns) <= maxi:
        c += 1
        m = max(m, sum(ns))
print(c, m)

# 152 93769
