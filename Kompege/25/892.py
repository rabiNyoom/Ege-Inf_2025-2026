def dels(n):
    return sorted([d for d in range(1, n+1) if n % d == 0])


for n in range(154026, 154044):
    d = dels(n)
    if len(d) == 4:
        print(d[-2], d[-1])
