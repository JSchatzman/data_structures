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
