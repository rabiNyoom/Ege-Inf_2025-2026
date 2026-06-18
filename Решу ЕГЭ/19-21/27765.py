def f(a, b, m):
    if a + b >= 69:
        return m % 2 == 0
    if m == 0:
        return 0
    moves = [
        f(a + 1, b, m - 1),
        f(a, b + 1, m - 1),
        f(a * 2, b, m - 1),
        f(a, b * 3, m - 1),
    ]
    return any(moves) if m % 2 == 1 else all(moves)


print(7)
print("".join([str(s) for s in range(1, 59) if not f(10, s, 1) and f(10, s, 3)]))
print(*[s for s in range(1, 59) if not f(10, s, 2) and f(10, s, 4)])
