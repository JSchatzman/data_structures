"""The Radix Sort Module."""
from math import log10


def radix_sort(ins_list):
    """Sort using the radix sort method."""
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


if __name__ == '__main__':
    import timeit
    from random import randint
    rad_list = [randint(0, 1000000) for i in range(100)]
    print('Sort Time for 1000 radix_sort calls on 100 randomly generated integers:',
          timeit.timeit(stmt="radix_sort(rad_list)",
                        setup='from __main__ import radix_sort, rad_list',
                        number=1000))