def f(s, m):
    if s <= 1207:
        return m % 2 == 0
    if m == 0:
        return 0

    mov = [f(s-3, m-1), f(s-5, m-1), f(s//4, m-1)]

    return all(mov) if m % 2 == 0 else any(mov)


print('19:', min([s for s in range(1207, 5000) if not f(s, 1) and f(s, 2)]))
