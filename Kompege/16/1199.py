from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return 3 * n + f(n-1)
    return 2 * f(n-2)


print(f(31))
