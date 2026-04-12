nums = list(map(int, open('2310.txt')))
ok4 = [n for n in nums if n % 10 == 4]
s = max(ok4) + min(ok4)
c = 0
m = 0
for a, b in zip(nums, nums[1:]):
    if (a+b) < s:
        c += 1
        m = max(m, a+b)
print(c, m)
