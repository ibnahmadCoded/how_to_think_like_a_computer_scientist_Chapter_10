def recursive_max(nested_list):
    """
        Find the maximum in a recursive structure of lists
        within other lists.
        Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for element in nested_list:
        if type(element) is list:
            value = recursive_max(element)
        else:
            value = element

        if first_time or value > largest:
            largest = value
            first_time = False

    return largest

a = recursive_max([1, 2, [11, 13], 8])

print(a)
