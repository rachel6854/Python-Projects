def to_upper(c):
    return chr(ord(c) - 32) if "a" <= c <= "z" else c


print(to_upper("d"))    # "D"
print(to_upper("Q"))    # "Q" (no change)
print(to_upper("!"))    # "!" (no change)


def upper(string):
    return ''.join([to_upper(c) for c in string])


print(upper("I love Python!"))  # "I LOVE PYTHON!"
