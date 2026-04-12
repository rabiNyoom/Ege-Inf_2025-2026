nums = list(map(int, open('2398.txt')))
cnt = 0
s = 0
for a, b, c in zip(nums, nums[1:], nums[2:]):
    if list(map(lambda n: n > 0 and n % 10 == 9, [a, b, c])) == [False, True, False]:
        cnt += 1
        s = max(s, a+b+c)
print(cnt, s)
