from functools import lru_cache


@lru_cache(None)
def f(n):
    match n:
        case 0:
            return 1
        case 1:
            return 3
        case 2:
            return 2
        case _:
            return f(n-1) * f(n-3)


print(f(7))
