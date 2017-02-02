from math import log10


def radixSort(ins_list):
    n = 10
    maxlen = int(log10(max(ins_list))) + 1
    for x in range(maxlen):
        bins = [[] for i in range(n)]
        for y in ins_list:
            bins[(y // 10**x) % n].append(y)
        ins_list = []
        for section in bins:
            ins_list.extend(section)
    return ins_list

print (radixSort([1,2,3,5,6,3,2,33,22,5,77, 111111]))