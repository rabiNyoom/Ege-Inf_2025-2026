def f(s,m):
    if s >= 31:
        return m == 0
    if m == 0:
        return 0
    h = [f(s+1, m-1), f(s*3-2, m-1)]
    return any(h)
print(19, *[s for s in range(2, 30+1) if f(s, 2)])
print(20, *[s for s in range(2, 30+1) if not f(s, 1) and f(s, 3)])


