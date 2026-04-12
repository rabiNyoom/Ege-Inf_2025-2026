nums = list(map(int, open('1999.txt')))
cnt = 0
m = 10e10
for i in range(2, len(nums)):
    n = nums[i-2:i+1]
    if any(map(lambda x: x % 12 == 0, n)) and all(map(lambda x: x % 3 == 0, n)):
        cnt += 1
        m = min(m, sum(n) // 3)
print(cnt, m)
