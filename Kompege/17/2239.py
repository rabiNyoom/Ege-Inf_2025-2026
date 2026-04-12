nums = list(map(int, open('2239.txt')))
maxi = max(n for n in nums if n % 19 == 0)
cnt = 0
m = 10e10
for a, b in zip(nums, nums[1:]):
    if a > maxi or b > maxi:
        cnt += 1
        m = min(m, a+b)
print(cnt, m)
