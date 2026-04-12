nums = list(map(int, open('2238.txt')))
avg = sum(nums) / len(nums)
cnt = 0
m = 0
for a, b, c in zip(nums, nums[1:], nums[2:]):
    if len([1 for n in [a, b, c] if n > avg]) >= 2:
        cnt += 1
        m = max(m, a+b+c)
print(cnt, m)
