
from functools import lru_cache
import time

# @lru_cache()
def long_func(num: int) -> int:
    r = 0
    for i in range(1000000):
        r += num * i
    return r


if __name__ == '__main__':
    for i in range(10):
        print(long_func(i))

    start = time.time()
    for i in range(10):
        print(long_func(i))
    print(time.time() - start)
