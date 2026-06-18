def f(s, m):
    if s <= 15:
        return m % 2 == 0
    if m == 0:
        return 0
    mov = [f(s - 3, m - 1), f(s - 7, m - 1), f(s // 4, m - 1)]
    return all(mov) if m % 2 == 0 else any(mov)


print([s for s in range(16, 100) if not f(s, 1) and f(s, 2)][0])
print(*[s for s in range(16, 100) if not f(s, 1) and f(s, 3)][:2])
print([s for s in range(16, 100) if not f(s, 2) and f(s, 4)][0])
