nums = [int(l) for l in open('14653.txt')]
ls = sorted([n for n in nums if n % 17 and n > 0])
mini = ls[0] + ls[1]
maxi = max([n for n in nums if str(n).endswith('69')])
c = 0
m = float('inf')
for i in range(3, len(nums)):
    ns = nums[i-3:i+1]
    if len([n for n in ns if 100 <= abs(n) <= 999]) != 2:
        continue
    if len([n for n in ns if n % 18 == 0]) != 1:
        continue
    if sum(ns) % mini != 0:
        continue
    if ns[0] * ns[1] * ns[2] * ns[3] > maxi * maxi:
        continue
    c += 1
    m = min(m, sum(ns)**2)
print(c,m)