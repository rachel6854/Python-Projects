def numCharsFoundd(subject,words):
    counter =0
    l=[]
    for word in words:
        for w in word:
            if w in set(subject):
                counter+=1
        l.append(counter)
        counter=0
    return l
print(numCharsFoundd("abbc",["aaa","bbb","cc","dd"]))