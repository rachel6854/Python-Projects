def longest_string(string1, string2):
    return string1 if len(string1) >= len(string2) else string2


def is_long_string(string):
    return True if len(string) > 10 else False


def judge(string1, string2):
    long = longest_string(string1, string2)
    if is_long_string(long):
        print(long + " is a long string")
    else:
        print(long + " is a normal string")
