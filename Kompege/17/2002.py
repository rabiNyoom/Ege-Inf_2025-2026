nums = list(map(int, open('2002.txt')))
cnt = 0
m = 10e10
for a, b, c, d in zip(nums, nums[1:], nums[2:], nums[3:]):
    if a >= b and b >= c and c >= d and a - d > 1000:
        cnt += 1
        m = min(m, a+b+c+d)
print(cnt, m)
