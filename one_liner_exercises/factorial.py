def factorial(num):
    return lambda b: (lambda a, b: a(a, b))(lambda a, b: b * a(a, b - 1) if b > 0 else 1, b)(num)


print(factorial(3))

def print_args(func):
    def inner(*args, **kwargs):
        print("args: ", end=" ")
        for x in args:
            print(x, end=" ")
        print()
        res = func(*args, **kwargs)
        print(res)
    return inner


@print_args
def add2(x, y):
    return x+y


@print_args
def add3(x, y, z):
    return x+y+z


@print_args
def add4(w, x, y, z):
    return w+x+y+z


add2(1,2)
add3(1, 2, 3)
add4(1,2, 2, 4)
