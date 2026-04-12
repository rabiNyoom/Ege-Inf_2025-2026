nums = list(map(int, open('1998.txt')))
cnt = 0
m = 0
for a, b, c in zip(nums, nums[1:], nums[2:]):
    p = a * b * c
    s = a + b + c
    if p % 7 == 0 and s % 10 == 5:
        cnt += 1
        m = max(m, s)
print(cnt, m)
