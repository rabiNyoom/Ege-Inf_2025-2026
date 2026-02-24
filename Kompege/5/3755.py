def algo(n):
    s = str(n)
    ns = []
    for i in range(1, len(s)):
        ns.append(int(s[i-1:i+1]))
    if ns:
        return max(ns) - min(ns)


for n in range(1, 1000000):
    if algo(n) == 44:
        print(n)
        break
