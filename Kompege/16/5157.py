from functools import lru_cache
from sys import setrecursionlimit
import threading


def main():
    @lru_cache(None)
    def f(n):
        if n >= 10000:
            return n
        if n % 3 == 0:
            return n + f(n/3)
        return 2 * n + f(n+3)
    print(f(999)-f(46))


setrecursionlimit(300000)
threading.stack_size(32 * 1024 * 1024)
threading.Thread(target=main).start()
