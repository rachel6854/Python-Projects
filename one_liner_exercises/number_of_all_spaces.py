def number_of_spaces(string):
    return string.count(" ") + string.count("\n") + string.count("\t")


print(number_of_spaces("Here is"
                       "a new line"))
