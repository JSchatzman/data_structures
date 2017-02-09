def quicksort(ins_list):
    import random
    """Sort seemingly by random."""
    if not hasattr(ins_list, '__iter__'):
        raise TypeError("Please insert an iterable")
    length = len(ins_list)
    return_list = []
    smaller_list = []
    bigger_list = []

    if length > 1:
        pivot = ins_list[random.randint(0, length-1)]
        for item in ins_list:
            if item < pivot:
                smaller_list.append(item)
            elif item == pivot:
                return_list.append(item)
            else:
                bigger_list.append(item)
        return quicksort(smaller_list) + return_list + quicksort(bigger_list)
    return ins_list


if __name__ == '__main__':
    import timeit
    from random import randint
    quicklist_string = [chr(randint(97, 123)) for i in range(100)]
    quicklist_num = [randint(0, 101) for i in range(100)]
    print('Sort Time for 1000 quicksort calls on 100 randomly generated string characters:',
          timeit.timeit(stmt="quicksort(quicklist_string)",
                        setup='from __main__ import quicksort, quicklist_string',
                        number=1000))
    print('Sort Time for 1000 quicksort calls on 100 randomly generated integers:',
          timeit.timeit(stmt="quicksort(quicklist_num)",
                        setup='from __main__ import quicksort, quicklist_num',
                        number=1000))