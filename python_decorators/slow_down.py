import time


def slow_down_decorator(func):
    def slow_down(*args, **kwargs):
        time.sleep(1)
        res = func(*args, **kwargs)
        return res

    return slow_down


print("We'll be back in a second")


@slow_down_decorator
def foo():
    print("We paused for one second and now we move on")


foo()
