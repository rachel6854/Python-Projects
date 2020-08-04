import time
from functools import reduce


def timer_decorator(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        print('Done in %2.4f ms' % ((te - ts) * 1000))
        return result
    return timed


@timer_decorator
def fib(num):
    return reduce(lambda x, num: [x[1], x[0] + x[1]], range(num), [0, 1])[0]


fib(6347)
