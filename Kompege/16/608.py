from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    return f(n-1) + 5 * n**2


print(f(39))
