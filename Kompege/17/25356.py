nums = [int(l) for l in open('25356.txt')]
maxi = max(n for n in nums if str(n).endswith('30'))
c = m = 0

for i in range(2, len(nums)):
    ns = nums[i-2:i+1]

    if any(1000 <= abs(n) <= 9999 for n in ns):
        continue
    if sum(ns) <= maxi:
        continue

    c += 1
    m = max(m, sum(ns))
print(c, m)
