def longest_word(string):
    return len(max(string.replace(".", "").split(" "), key=lambda word: len(word)))


print(longest_word("If you can't explain it simply you don't understand it well enough."))
