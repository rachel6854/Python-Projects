def my_accumulate(list_):
    sum = 0
    for i in range(len(list_)):
        sum += list_[i]
        yield sum


for elem in my_accumulate([1, 2, 3, 4, 5]):
    print(elem)
