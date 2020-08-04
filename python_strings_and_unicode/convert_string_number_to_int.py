def string_number_to_int(string):
    result = 0
    for digit in string:
        if not digit.isdigit():
            return "Mistake! can not convert string to int"
        result *= 10
        result += ord(digit) - ord('0')
    return result


print(string_number_to_int("987"))  # output: 10
print(string_number_to_int("123"))  # output: 123
print(string_number_to_int("99"))  # output: 99
print(string_number_to_int("ABC"))  # Print the ASCII value
