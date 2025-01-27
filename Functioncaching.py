import functools
import time


@functools.lru_cache(maxsize=None)
def fib(n):
    time.sleep(5)
    return n*5
    if n<2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(20))

#memoization