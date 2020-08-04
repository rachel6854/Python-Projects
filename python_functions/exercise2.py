def longest_string(string1, string2):
    if len(string1) > len(string2):
        return string1
    elif len(string2) > len(string1):
        return string2
    else:
        return "same length"
#print(longest_string("helloo","world"))
