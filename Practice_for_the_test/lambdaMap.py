def lambdaMap(arr):
    return list(map(lambda list_: [x ** 2 for x in list_ if x >= 0], arr))


print(lambdaMap([[5, 0, -1], [9, 0, 7, -3, -7], [8, 5, -4, -3, 1]]))
