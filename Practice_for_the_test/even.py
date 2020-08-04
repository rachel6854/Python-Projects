def even(n, start):
    return [x for x in range(start, start + n * 2) if x % 2 == 0]


print(even(4, 2))
print(even(4, 3))
print(even(5, 3))
print(even(5, 2))

