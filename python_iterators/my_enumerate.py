def my_enumerate(list_):
    for i in range(len(list_)):
        yield i, list_[i]


for index, elem in my_enumerate([10, 20, 30, 40]):
    print(index, elem)
