from collections import deque
with open('813.txt') as f:
    s, _ = map(int, f.readline().split())
    sizes = [int(l) for l in f]

d = deque(sorted(sizes))
b = True
c = l = 0
while True:
    if b:
        popped = d.pop()
        b = False
    else:
        popped = d.popleft()
        b = True

    if s - popped >= 0:
        c += 1
        l = popped
        s -= popped
    else:
        break

print(c, l)
