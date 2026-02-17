from functools import lru_cache
from sys import setrecursionlimit
import threading


def main():
    @lru_cache(None)
    def f(n):
        if n > 10000:
            return n - 10000
        return f(n+1) + f(n+2)
    print(f(12345) * (f(10)-f(12))/f(11) + f(10101))


setrecursionlimit(300000)
threading.stack_size(32 * 1024 * 1024)
threading.Thread(target=main).start()
