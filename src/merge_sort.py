"""Implementation of merge sort."""


def _merge(list1, list2):
    """Merge two lists."""
    new_list = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            new_list.append(list1[0])
            list1.pop(0)
        else:
            new_list.append(list2[0])
            list2.pop(0)

    if len(list1) == 0:
        new_list += list2
    else:
        new_list += list1
    return new_list


def merge_sort(input_list):
    """Return the sorted list using the merge sort algorithm."""
    if len(input_list) < 2:
        return input_list
    else:
        middle = len(input_list) // 2
        list1 = merge_sort(input_list[:middle])
        list2 = merge_sort(input_list[middle:])
        return _merge(list1, list2)




