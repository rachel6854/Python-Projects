def getMinimumDifference(a, b):
    list_ = []
    for i in range(len(a)):
        aa = list(a[i])
        bb = list(b[i])
        if len(aa) == len(bb):
            for c in aa:
                if c in bb:
                    bb.remove(c)
            list_.append(len(bb))
        else:
            list_.append(-1)
    return list_


print(getMinimumDifference(["aba", "as", "poiu", "oip", "uytre", "kjh", "fdser"],
                           ["baa", "lkj", "lk", "poi", "ertyu", "lkj", "oiuyh"]))
