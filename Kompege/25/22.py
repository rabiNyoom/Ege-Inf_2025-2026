for n in range(174457, 174506):
    delit = [d for d in range(2, n) if n % d == 0]
    if len(delit) == 2:
        print(*delit)
