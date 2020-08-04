def reverse_word_order(sentence):
    return ' '.join(reversed(sentence.split(' ')))


print(reverse_word_order("hello dear world"))
