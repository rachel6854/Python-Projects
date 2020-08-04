def count_digit(num):
    ret = ""
    sum_ = 1
    num = str(num)+"9"
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            sum_ = sum_ + 1
        else:
            ret += str(sum_) + num[i]
            sum_ = 1
    return ret


print(count_digit(6))
print(count_digit(334))
print(count_digit(1121))
print(count_digit(2235))
