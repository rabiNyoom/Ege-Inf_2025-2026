nums = [int(l) for l in open('17_28938.txt')]
cnt = 0
maxsum = 0
maxi = max(n for n in nums if (abs(n) % 100) == 28)
for a, b, c in zip(nums, nums[1:], nums[2:]):
    if any(100 <= abs(n) <= 999 for n in [a, b, c]) and 0 < (a+b+c) / 3 < maxi:
        cnt += 1
        maxsum = max(maxsum, a+b+c)
print(cnt, maxsum)
