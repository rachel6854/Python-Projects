def encode(msg, n):
    ret = ""
    for c in msg:
        ret += chr(ord("A") + ((ord(c) - ord("A") + n) % 26))
    return ret


def decode(msg, n):
    ret = ""
    for c in msg:
        ret += chr(ord("A") + ((ord(c) - ord("A") - n) % 26))
    return ret


print(encode("ABXYZ", 3))  # "DEABC"
print(decode("DEABC", 3))  # "ABXYZ"
print(decode(encode("HELLOWORLD", 700), 700))
