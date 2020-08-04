def largest_lexicographically(string):
    return max(string.replace(".", "").split(" "))


print(largest_lexicographically("Imagination is .more important than knowledge."))
