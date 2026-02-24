from collections import deque
with open('838.txt') as f:
    f.readline()
    sizes = [int(l) for l in f]
big = small = 0
bigf = smallf = 0

d = deque(sorted(sizes))
while d:
    big += d.pop()
    bigf += 1
    while small <= big:
        small += d.popleft()
        smallf += 1
print(bigf, smallf)
