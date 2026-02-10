nums = [int(l) for l in open('21712.txt')]
mini = min(n for n in nums if 1000 <= n <= 9999 and n % 10 == 6)
c = m = 0

for i in range(2, len(nums)):
    ns = nums[i-2:i+1]

    if len([n for n in ns if 1000 <= abs(n) <= 9999 and abs(n) % 10 == 6]) != 1:
        continue
    if sum(ns) > mini:
        continue

    c += 1
    m = max(m, sum(ns))

print(c, m)
