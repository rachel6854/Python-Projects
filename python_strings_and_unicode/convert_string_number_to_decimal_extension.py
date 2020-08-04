def string_number_to_decimal(string, base):
    result = 0
    for digit in string:
        if not 0 <= ord(digit) - ord('0') < base:
            return "Mistake! can not convert string to int"
        result *= base
        result += ord(digit) - ord('0')
    return result


# base 2
print(string_number_to_decimal("10", 2))  # output: 2
print(string_number_to_decimal("101", 2))  # output: 5
# print(string_number_to_decimal("12", 2)) # output: Mistake! can not convert string to int

# base 8
print(string_number_to_decimal("7", 8))  # output: 7
print(string_number_to_decimal("123", 8))  # output: 83
print(string_number_to_decimal("10", 8))  # output: 8
# print(string_number_to_decimal("9", 8))# output: Mistake! can not convert string to int

# base 10
print(string_number_to_decimal("10", 10))  # output: 10
print(string_number_to_decimal("123", 10))  # output: 123
print(string_number_to_decimal("99", 10))  # output: 99
# print(string_number_to_decimal("ABC", 10)) # output: Mistake! can not convert string to int
