from functools import reduce


def cache_decorator(func):
    dict_ = {}

    def inner(*args):
        nonlocal dict_
        if dict_.get(args, None) is None:
            res = func(*args)
            dict_[args] = res
            return res
        else:
            print("We use the  cache now with", *args)
            return dict_[args]

    return inner


@cache_decorator
def fib(n):
    return reduce(lambda x, num: [x[1], x[0] + x[1]], range(n), [0, 1])[0]


print("fibbonacci 6 first:", fib(6))
print("fibbonacci 6 second:", fib(6))
print("fibbonacci 6 third:", fib(6))

print("And with recursive function:")


@cache_decorator
def fib_recursive(n):
    return n if n < 2 else fib_recursive(n - 2) + fib_recursive(n - 1)


print("fibbonacci 6 recursive:", fib_recursive(6))
