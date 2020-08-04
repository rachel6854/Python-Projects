def filter_vowels(string):
    return "".join([x for x in list(string) if x not in "aoieu"])


def filter_consonants(string):
    return "".join([x for x in list(string) if x in "aoieu"])
