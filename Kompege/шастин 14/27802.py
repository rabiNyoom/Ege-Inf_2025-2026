def f(s, m):
    if s >= 68:
        return m % 2 == 0
    if m == 0:
        return 0
    mov = [f(s + 1, m - 1), f(s + 4, m - 1), f(s * 5, m - 1)]
    return all(mov) if m % 2 == 0 else any(mov)


print(*[s for s in range(1, 68) if not f(s, 2) and f(s, 4)])
