nums = list(map(int, open('2403.txt')))
c = 0
m = 0
for a, b in zip(nums, nums[1:]):
    fst = a % 9 == 0 and b % 9 != 0 and oct(b).endswith('3')
    snd = b % 9 == 0 and a % 9 != 0 and oct(a).endswith('3')
    if fst and not snd or snd and not fst:
        c += 1
        m = max(m, a, b)
print(c, m)
