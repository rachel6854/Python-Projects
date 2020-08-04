# your script need to print all data about the line that calling the function.
# Name of the function
# all arguments (regular, *args, **kwargs)
# execute the original function
# print all the returning data. (value and type)


def information_decorator(func):
    def information(*args, **kwargs):
        print("we are execute the func", func.__name__, "now")
        print("args: ", end=" ")
        for x in args:
            print(x, end=" ")
        print()
        print("kwargs: ", end=" ")
        print(kwargs)
        res = func(*args, **kwargs)
        print(res)
        return res
    return information


@information_decorator
def foo(*args, **kwargs):
    print("Now we are in foo. len of args: ", len(args), "len of kwargs: ", len(kwargs))
    return "We are out of the function now."


foo(1, 2, kwarg=3, kwarg2="some_thing")
