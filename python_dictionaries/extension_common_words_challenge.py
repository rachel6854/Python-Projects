from collections import defaultdict


def get_5common(string):
    split_string = string.split(" ")
    d = defaultdict(int)
    for i in split_string:
        d[i] += 1
    return sorted(d.items(), key=lambda x: x[1], reverse=True)[:5]


line = "wee wee goo koo goo doo doo so go go yo yo yo yo fo zo"
print(get_5common(line))
