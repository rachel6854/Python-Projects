def reverse_words_in_a_sentence(sentence):
    return " ".join([word[::-1] for word in sentence.split(" ")])


print(reverse_words_in_a_sentence("hello world"))
