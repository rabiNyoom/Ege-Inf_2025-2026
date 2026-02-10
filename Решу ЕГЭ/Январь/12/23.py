def divs(n: int) -> int:
    s = 0
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            s += d
            if d * d != n:
                s += n // d
    return s


def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(divs(a), b)


print(f(2, 24))
