from functools import lru_cache


@lru_cache(None)
def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    s = str(a)
    if int(s[-1]) > int(s[-2]):
        return f(a+1, b) + f(int(s[:-2] + s[-1] + s[-2]), b)
    else:
        return f(a+1, b)


print(f(101, 154))

# 89
