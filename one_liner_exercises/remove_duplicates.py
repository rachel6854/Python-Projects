from functools import reduce


def remove_duplicates(list_):
    return list(set(list_))
    # return reduce(lambda prev, x: prev + [x] if x not in prev else prev, list_, [])


print(remove_duplicates([1, 2, 1, 3, 3, 2, 2]))
