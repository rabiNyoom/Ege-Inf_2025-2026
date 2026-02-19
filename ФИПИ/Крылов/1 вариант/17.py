nums = list(map(int, open('17.txt')))
dvuz = [n for n in nums if 10 <= abs(n) <= 99]

mini = min(dvuz)
maxi = max(dvuz)

cnt = m = 0
for i in range(len(nums)):
    ns = nums[i-2:i+1]
    if len([n for n in ns if 10 <= abs(n) <= 99]) < 2:
        continue
    if sum(ns) <= (mini + maxi):
        continue
    cnt += 1
    m = max(m, sum(ns))
print(cnt, m)

# 8 99191
