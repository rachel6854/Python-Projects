def reverse_arguments(f):
    def g(*args):
        return f(args[::-1])

    return g


def foo(*args):
    for a in args:
        print(a)


func = reverse_arguments(foo)
func(4,9)
