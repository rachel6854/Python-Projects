numbers = [2, 3, 55, 4, 6, 8, 43, 10]
print(sum(map(lambda x: x ** 2, sorted(list(filter(lambda x: x % 2 == 0, numbers)),reverse=True)[:4])))
