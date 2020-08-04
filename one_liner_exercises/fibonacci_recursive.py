from functools import reduce


def fibonacci(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)
    return reduce(lambda x,num:[x[1],x[0]+x[1]], range(num),[0,1])[0]


print(fibonacci(6))
