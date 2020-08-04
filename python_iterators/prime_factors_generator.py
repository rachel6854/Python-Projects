from math import ceil, sqrt


def get_prime_factors_generator(num):
    if num < 2:
        return []
    prime = next((x for x in range(2, ceil(sqrt(num)) + 1) if num % x == 0),num)
    return [prime] + get_prime_factors_generator(num // prime)


for x in get_prime_factors_generator(17):
    print(x)
