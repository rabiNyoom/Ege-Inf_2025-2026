from functools import lru_cache
from sys import setrecursionlimit
from math import factorial
import threading


def main():
    @lru_cache(None)
    def f(n):
        if n >= 5000:
            return factorial(n)
        return 2 * f(n+1) // (n+1)
    print(1000 * f(7)/f(4))


setrecursionlimit(300000)
threading.stack_size(32 * 1024 * 1024)
threading.Thread(target=main).start()
