nums = list(map(int, open('2402.txt')))


def tri(n):
    s = ''
    while n > 1:
        s = str(n % 3) + s
        n //= 3
    return s


cnt = 0
s = 0
for i in range(2, len(nums)):
    n = nums[i-2:i+1]
    if any(map(lambda x: tri(x).endswith('2'), n)):
        cnt += 1
        s += min(n)
print(cnt, s)
