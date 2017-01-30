"""Implementation of insertion sort."""

def insertion_sort(input_list):
    """Return the list in sorted form."""
    for i in range(len(input_list)):
        value = input_list[i]
        position = i
        while position > 0 and input_list[position-1] > value:
            input_list[position] = input_list[position - 1]
            position -= 1
        input_list[position] = value
    return input_list


print(insertion_sort(['a','z','gggdgd','ttrt','gfggfgd']))

