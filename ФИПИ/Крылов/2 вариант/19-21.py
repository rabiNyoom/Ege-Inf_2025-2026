def f(s, m):
    if s <= 65:
        return m % 2 == 0
    if m == 0:
        return 0
    mov = [f(s-3, m-1), f(s-5, m-1), f(s//4, m-1)]
    return all(mov) if m % 2 == 0 else any(mov)


print('19:', *[s for s in range(66, 500) if f(s, 2)])
print('20:', *[s for s in range(66, 500) if not f(s, 1) and f(s, 3)])
print('21:', *[s for s in range(66, 500) if not f(s, 2) and f(s, 4)])
