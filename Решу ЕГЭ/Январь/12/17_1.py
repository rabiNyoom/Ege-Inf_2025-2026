# 14653
nums = [int(l) for l in open('17_14653.txt')]
c = 0
m = float('inf')

mini1, mini2 = sorted([i for i in nums if i > 0 and i % 17 == 0])[:2]
maxi = max([i for i in nums if str(i).endswith('69')])


for i in range(3, len(nums)):
    ns = nums[i-3:i+1]
    fst = len([i for i in ns if 100 <= abs(i) <= 999]) == 2
    snd = sum(ns) % (mini1 + mini2) == 0
    trd = (ns[0] * ns[1] * ns[2] * ns[3]) <= (maxi ** 2)
    frth = len([i for i in ns if i % 18 == 0]) == 1
    if fst and snd and trd and frth:
        c += 1
        m = min(m, sum(ns)**2)
print(c, m)
