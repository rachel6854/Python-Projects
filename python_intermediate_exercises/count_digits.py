def count_digits(num):
    ret_str = ""
    count = 0
    num = str(num) + "9"
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            count += 1
        else:
            ret_str += str(count + 1) + str(num[i])
            count = 0
    return ret_str


print(count_digits(6))
print(count_digits(334))
print(count_digits(1121))
print(count_digits(2235))
