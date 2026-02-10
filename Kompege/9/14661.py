c = 0
for l in open('14661.txt'):
    ns = list(map(int, l.split()))
    even = [n for n in ns if n % 2 == 0]
    odd = [n for n in ns if n % 2 == 1]

    # fst = len(even) > 0 and len(odd) > 0
    if len(even) == 0 or len(odd) == 0:
        continue
    snd = len(even) % 2 == 0 and len(odd) % 2 == 1
    trd = max(even) % 4 == 0
    if snd and trd:
        c += 1
print(c)

# 254
