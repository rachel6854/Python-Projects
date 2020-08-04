def func(*args):
    if 'max_' not in func.__dict__:
        func.max_=0
    func.max_=max(func.max_,len(args))
    def return_max():
        return func.max_
    return return_max()


print(func())  # 0
print(func(1, 2, 3, 4))  # 4
print(func(1, 2))  # 4
print(func(1, 2, 3, 4, 5))  # 5
