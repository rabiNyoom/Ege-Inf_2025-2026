nums = list(map(int, open('2309.txt')))
k11 = k17 = 0
maxi = 0
mini = 10e10

for n in nums:
    if n % 11 == 0:
        k11 += 1
        mini = min(mini, n)
    if n % 17 == 0:
        k17 += 1
        maxi = max(maxi, n)

if k11 > k17:
    print(k11, mini)
else:
    print(k17, maxi)
