def longest_string(string1, string2):
    return string1 if len(string1) >= len(string2) else string2
print(longest_string("hello","world"))
