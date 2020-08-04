from functools import wraps


def call_counter(func):
    def increase_count(*args):
        increase_count.calls += 1
        return func()

    increase_count.calls = 0
    return increase_count


# def coall_count(function, count=[0]):
#     @wraps(function)
#     def increase_count(*args, **kwargs):
#         count[0] += 1
#         return function(*args, **kwargs), count[0]
#
#     return increase_count


@call_counter
def foo():
    return 42


print(foo(), foo(), foo())
print("The function called", foo.calls, "times")
