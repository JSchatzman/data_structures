"""Implementation of insertion sort."""


def insertion_sort(input_list):
    """Return the list in sorted form."""
    for i in range(len(input_list)):
        value = input_list[i]
        position = i
        while position > 0 and input_list[position - 1] > value:
            input_list[position] = input_list[position - 1]
            position -= 1
        input_list[position] = value
    return input_list


if __name__ == '__main__':
    import timeit
    reverse_nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    order_nums = reverse_nums[::-1]
    reverse_string = ['zzz', 'xxz', 'xxx', 'ggg', 'bbb', 'aaz']
    order_string = reverse_string[::-1]
    random_list = [32, 543, 122, 1, 99999, 22, 3453, 34432, 1, 766]
    print('Sort Time for 1000 reverse num sort calls:',
          timeit.timeit(stmt="insertion_sort(reverse_nums)",
                        setup='from __main__ import reverse_nums, insertion_sort',
                        number=1000))
    print('Sort Time for 1000 order num sort calls:',
          timeit.timeit(stmt="insertion_sort(order_nums)",
                        setup='from __main__ import order_nums, insertion_sort',
                        number=1000))
    print('Sort Time for 1000 reverse string sort calls:',
          timeit.timeit(stmt="insertion_sort(reverse_string)",
                        setup='from __main__ import reverse_string, insertion_sort',
                        number=1000))
    print('Sort Time for 1000 order string sort calls:',
          timeit.timeit(stmt="insertion_sort(order_string)",
                        setup='from __main__ import order_string, insertion_sort',
                        number=1000))
    print('Sort Time for 1000 random list sort calls:',
          timeit.timeit(stmt="insertion_sort(random_list)",
                        setup='from __main__ import random_list, insertion_sort',
                        number=1000))
